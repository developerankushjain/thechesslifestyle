import crypto from 'crypto';
import { submitToGoogleSheets } from './_sheets.js';
import { sendConfirmationEmail } from './_mailer.js';
import { isAlreadyProcessed } from './_cache.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // 1. Signature verification (if webhook secret configured in Vercel)
  const webhookSecret = process.env.RAZORPAY_WEBHOOK_SECRET;
  const signature = req.headers['x-razorpay-signature'];

  if (webhookSecret && signature) {
    try {
      const bodyString = typeof req.body === 'string' ? req.body : JSON.stringify(req.body);
      const expectedSignature = crypto
        .createHmac('sha256', webhookSecret)
        .update(bodyString)
        .digest('hex');

      if (expectedSignature !== signature) {
        console.warn('Razorpay webhook signature mismatch');
        return res.status(400).json({ error: 'Invalid webhook signature' });
      }
    } catch (err) {
      console.error('Error verifying webhook signature:', err);
      return res.status(400).json({ error: 'Signature verification error' });
    }
  }

  const event = req.body.event;
  // Handle both payment.captured and order.paid
  if (event !== 'payment.captured' && event !== 'order.paid') {
    return res.status(200).json({ message: `Ignored event: ${event}` });
  }

  try {
    const payment = req.body?.payload?.payment?.entity || {};
    const order = req.body?.payload?.order?.entity || {};

    const paymentId = payment.id || order.id || 'WEBHOOK_PAYMENT';
    const orderId = order.id || payment.order_id || '';

    // Check if this payment was already processed by client-side complete-registration
    if (isAlreadyProcessed(paymentId) || (orderId && isAlreadyProcessed(orderId))) {
      console.log(`Payment ${paymentId} / ${orderId} already handled. Skipping duplicate.`);
      return res.status(200).json({ success: true, message: 'Already processed' });
    }

    // Extract notes
    const notes = payment.notes || order.notes || {};
    
    // Only process if notes belong to our tournament event
    if (notes.event && notes.event !== 'TCL_Noida_Premier_League') {
      return res.status(200).json({ message: 'Event not matching TCL_Noida_Premier_League' });
    }

    const playerName = notes.player_name || payment.name || 'Participant';
    const parentName = notes.parent_name || '';
    const email = notes.email || payment.email;
    const category = notes.category || 'Open';
    const amountPaid = notes.amount_paid || (payment.amount ? `Rs. ${payment.amount / 100}` : '');

    // Map back to sheet columns
    const sheetData = {
      'Category': category,
      'Player Name': playerName,
      'Parent Name': parentName,
      'Email': email || '',
      'WhatsApp Number': notes.phone || payment.contact || '',
      'Date of Birth': notes.dob_or_age || '',
      'Age': notes.dob_or_age || '',
      'Class': notes.class_school || '',
      'School': notes.class_school || '',
      'FIDE ID': notes.fide_id || '',
      'FIDE Title': notes.fide_title || 'None',
      'Chess Rating': notes.chess_rating || '',
      'Concession Applied': notes.concession || 'None',
      'Special Requirements': notes.special_req || '',
      'Razorpay Payment ID': paymentId,
      'Razorpay Order ID': orderId,
      'Amount Paid': amountPaid,
      'Status': 'Auto-Recovered via Webhook'
    };

    // Parallel execution
    const [sheetResult, emailResult] = await Promise.allSettled([
      submitToGoogleSheets(sheetData),
      email ? sendConfirmationEmail({ playerName, parentName, email, category, paymentId }) : Promise.resolve(null)
    ]);

    console.log(`Webhook handled payment ${paymentId}: Sheet=${sheetResult.status}, Email=${emailResult.status}`);

    return res.status(200).json({
      success: true,
      message: 'Webhook processed successfully',
      paymentId
    });

  } catch (error) {
    console.error('Error handling Razorpay webhook:', error);
    return res.status(500).json({ error: 'Webhook processing error', details: error.message });
  }
}

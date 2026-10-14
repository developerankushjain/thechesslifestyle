import { submitToGoogleSheets } from './_sheets.js';
import { sendConfirmationEmail } from './_mailer.js';
import { isAlreadyProcessed } from './_cache.js';

export default async function handler(req, res) {
  // Add CORS headers so frontend can call this API
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { formData, paymentId, orderId } = req.body;

  if (!formData || typeof formData !== 'object') {
    return res.status(400).json({ error: 'formData is required' });
  }

  const pid = paymentId || formData['Razorpay Payment ID'] || 'UNKNOWN';

  // Check deduplication
  const alreadyHandled = isAlreadyProcessed(pid);
  if (alreadyHandled && pid !== 'FREE_ENTRY' && pid !== 'UNKNOWN') {
    return res.status(200).json({
      success: true,
      message: 'Already processed',
      paymentId: pid
    });
  }

  // Ensure Razorpay payment ID and Amount Paid are set in the sheet payload
  const sheetPayload = {
    ...formData,
    'Razorpay Payment ID': pid,
    'Razorpay Order ID': orderId || formData['Razorpay Order ID'] || ''
  };

  const playerName = formData['Player Name'] || '';
  const parentName = formData['Parent Name'] || '';
  const email = formData['Email'] || '';
  const category = formData['Category'] || 'Open';

  // Run Google Sheets submission and Confirmation Email in parallel
  const [sheetResult, emailResult] = await Promise.allSettled([
    submitToGoogleSheets(sheetPayload),
    email ? sendConfirmationEmail({ playerName, parentName, email, category, paymentId: pid }) : Promise.resolve(null)
  ]);

  const sheetOk = sheetResult.status === 'fulfilled';
  const emailOk = emailResult.status === 'fulfilled';

  if (!sheetOk) {
    console.error('Google Sheets submission error in complete-registration:', sheetResult.reason);
  }
  if (!emailOk) {
    console.error('Email sending error in complete-registration:', emailResult.reason);
  }

  return res.status(200).json({
    success: sheetOk || emailOk,
    sheetUpdated: sheetOk,
    emailSent: emailOk,
    sheetError: !sheetOk ? sheetResult.reason?.message : null,
    emailError: !emailOk ? emailResult.reason?.message : null,
    paymentId: pid
  });
}

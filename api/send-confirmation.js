import { sendConfirmationEmail } from './_mailer.js';

export default async function handler(req, res) {
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

  const { playerName, parentName, email, category, paymentId } = req.body;

  if (!email) {
    return res.status(400).json({ error: 'Email is required' });
  }

  try {
    await sendConfirmationEmail({ playerName, parentName, email, category, paymentId });
    res.status(200).json({ success: true, message: 'Confirmation email sent!' });
  } catch (error) {
    console.error('Error sending confirmation email:', error);
    res.status(500).json({ error: 'Failed to send email', details: error.message });
  }
}

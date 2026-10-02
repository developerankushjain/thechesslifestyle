import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  // CORS headers
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
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_APP_PASSWORD,
      },
    });

    const htmlBody = `
      <div style="font-family: Arial, sans-serif; color: #333; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px;">
        
        <div style="text-align: center; margin-bottom: 30px;">
          <h1 style="color: #1e3a5f; margin: 0;">&#9820; TheChessLifestyle</h1>
          <p style="color: #64748b; margin-top: 5px;">Official Tournament Confirmation</p>
        </div>

        <div style="background: linear-gradient(135deg, #1e3a5f, #2563eb); border-radius: 12px; padding: 25px; text-align: center; margin-bottom: 25px;">
          <div style="width: 60px; height: 60px; background: #10b981; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 28px; margin-bottom: 15px;">&#10003;</div>
          <h2 style="color: #fff; margin: 0 0 8px;">Registration Confirmed!</h2>
          <p style="color: #bfdbfe; margin: 0;">You are officially registered for the TheChessLifestyle Tournament.</p>
        </div>

        <p style="font-size: 1rem;">Hi <strong>${playerName}</strong>${parentName ? ` (and ${parentName})` : ''},</p>
        <p>Congratulations! Your registration for the <strong>${category}</strong> category is confirmed. We cannot wait to see you at the board!</p>

        <div style="background: #f8fafc; border-left: 4px solid #2563eb; border-radius: 6px; padding: 18px; margin: 20px 0;">
          <h3 style="margin-top: 0; color: #0f172a;">&#128205; Venue &amp; Timings</h3>
          <p style="margin: 4px 0;"><strong>Date:</strong> 31st October, 2026</p>
          <p style="margin: 4px 0;"><strong>Reporting Time:</strong> 9:00 AM (sharp)</p>
          <p style="margin: 4px 0;"><strong>Venue:</strong> Raghav Global School, Sector 122 First Entrance, Block A, Noida</p>
          <p style="margin: 8px 0 0;">
            <a href="https://www.google.com/maps/place/RAGHAV+GLOBAL+SCHOOL,+Sector+122+First+Entrance,+Block+A,+Sector+122,+Noida,+Uttar+Pradesh+201316" style="color: #2563eb;">View on Google Maps &rarr;</a>
          </p>
        </div>

        <div style="background: #f8fafc; border-left: 4px solid #10b981; border-radius: 6px; padding: 18px; margin: 20px 0;">
          <h3 style="margin-top: 0; color: #0f172a;">&#127760; Pairings &amp; Live Results</h3>
          <p style="margin: 4px 0;">Official pairings and live results will be published on:</p>
          <p style="margin: 8px 0;">
            &#8226; <a href="https://chess-results.com" style="color: #2563eb; font-weight: bold;">chess-results.com</a><br>
            &#8226; <a href="https://chesscircuit.in" style="color: #2563eb; font-weight: bold;">chesscircuit.in</a>
          </p>
        </div>

        <div style="background: #fff7ed; border-left: 4px solid #f59e0b; border-radius: 6px; padding: 18px; margin: 20px 0;">
          <h3 style="margin-top: 0; color: #0f172a;">&#9888;&#65039; Important Rules</h3>
          <ul style="color: #475569; margin: 0; padding-left: 20px;">
            <li style="margin-bottom: 6px;">Please carry a valid photo ID (and FIDE ID / school ID if claiming a concession).</li>
            <li style="margin-bottom: 6px;">Players must bring their own water bottles. Complimentary refreshments will be provided.</li>
            <li style="margin-bottom: 6px;">Electronic devices (including smartwatches) are strictly prohibited in the playing area.</li>
            <li>Parents and guardians should stay outside the tournament hall and can take part in fun activities to win exclusive merchandise!</li>
          </ul>
        </div>

        ${paymentId ? `<p style="font-size: 0.85rem; color: #94a3b8;">Payment Reference ID: ${paymentId}</p>` : ''}

        <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e2e8f0;">
          <p style="font-size: 1.1rem; color: #0f172a;"><strong>Best of luck! &#9820;&#65039;</strong></p>
          <p style="color: #64748b; margin: 0;">TheChessLifestyle Team</p>
          <p style="margin-top: 10px;"><a href="https://www.thechesslifestyle.com" style="color: #2563eb;">www.thechesslifestyle.com</a></p>
        </div>
      </div>
    `;

    await transporter.sendMail({
      from: `"TheChessLifestyle" <${process.env.GMAIL_USER}>`,
      to: email,
      subject: `Registration Confirmed! &#9820; TheChessLifestyle Tournament - ${category}`,
      html: htmlBody,
    });

    res.status(200).json({ success: true, message: 'Confirmation email sent!' });

  } catch (error) {
    console.error('Error sending confirmation email:', error);
    res.status(500).json({ error: 'Failed to send email', details: error.message });
  }
}

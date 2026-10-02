import nodemailer from 'nodemailer';

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

  const isUnder12 = category === 'Under 12';
  const greeting = isUnder12 && parentName
    ? `Hi <strong>${parentName}</strong>, <span style="color:#64748b;">(parent/guardian of ${playerName})</span>`
    : `Hi <strong>${playerName}</strong>,`;

  const categoryBadgeColor = isUnder12 ? '#f59e0b' : '#2563eb';
  const categoryLabel = isUnder12 ? 'Junior Rapid (Under 12)' : 'Open Rapid';

  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_APP_PASSWORD,
      },
    });

    const htmlBody = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Registration Confirmed</title>
</head>
<body style="margin:0; padding:0; background-color:#f1f5f9; font-family: 'Helvetica Neue', Arial, sans-serif;">

  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f1f5f9; padding: 30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;">

          <!-- HEADER -->
          <tr>
            <td style="background:#0f172a; border-radius:16px 16px 0 0; padding: 28px 40px; text-align:center;">
              <img src="https://www.thechesslifestyle.com/favicon.png" alt="TheChessLifestyle Logo" width="52" height="52" style="display:inline-block; margin-bottom:12px; border-radius:10px;">
              <h1 style="margin:0; color:#f8fafc; font-size:22px; font-weight:700; letter-spacing:0.5px;">TheChessLifestyle</h1>
              <p style="margin:5px 0 0; color:#94a3b8; font-size:13px; letter-spacing:1px; text-transform:uppercase;">Official Tournament Confirmation</p>
            </td>
          </tr>

          <!-- GREEN SUCCESS BANNER -->
          <tr>
            <td style="background: linear-gradient(135deg, #064e3b, #065f46); padding: 36px 40px; text-align:center;">
              <div style="width:68px; height:68px; background:#10b981; border-radius:50%; display:inline-block; line-height:68px; font-size:34px; color:#fff; margin-bottom:18px;">&#10003;</div>
              <h2 style="margin:0 0 8px; color:#ffffff; font-size:26px; font-weight:700;">You Are In! &#127881;</h2>
              <p style="margin:0; color:#a7f3d0; font-size:15px; line-height:1.6;">Your spot at the tournament has been officially secured.<br>Get ready to bring your best game!</p>
              <div style="margin-top:20px; display:inline-block; background:${categoryBadgeColor}; color:#fff; font-size:13px; font-weight:700; padding:6px 18px; border-radius:20px; letter-spacing:0.5px;">
                ${categoryLabel}
              </div>
            </td>
          </tr>

          <!-- BODY -->
          <tr>
            <td style="background:#ffffff; padding: 36px 40px;">

              <p style="margin:0 0 20px; font-size:15px; color:#334155; line-height:1.7;">
                ${greeting}<br><br>
                Congratulations on completing your registration for the <strong>TCL Noida Premier League</strong>. 
                We are absolutely thrilled to have you join us for what is going to be an incredible day of chess!
              </p>

              <!-- VENUE CARD -->
              <table width="100%" cellpadding="0" cellspacing="0" style="background:#eff6ff; border-left:4px solid #2563eb; border-radius:8px; margin-bottom:20px;">
                <tr>
                  <td style="padding:20px 22px;">
                    <p style="margin:0 0 12px; font-size:15px; font-weight:700; color:#1e3a5f;">&#128205; Venue &amp; Timings</p>
                    <table cellpadding="0" cellspacing="0">
                      <tr>
                        <td style="padding:4px 0; font-size:14px; color:#475569; min-width:130px;"><strong>Date</strong></td>
                        <td style="padding:4px 0; font-size:14px; color:#1e293b;">31st October, 2026</td>
                      </tr>
                      <tr>
                        <td style="padding:4px 0; font-size:14px; color:#475569;"><strong>Reporting Time</strong></td>
                        <td style="padding:4px 0; font-size:14px; color:#1e293b;">9:00 AM (sharp)</td>
                      </tr>
                      <tr>
                        <td style="padding:4px 0; font-size:14px; color:#475569; vertical-align:top;"><strong>Venue</strong></td>
                        <td style="padding:4px 0; font-size:14px; color:#1e293b;">Raghav Global School,<br>Sector 122 First Entrance, Block A,<br>Noida, Uttar Pradesh 201316</td>
                      </tr>
                    </table>
                    <p style="margin:14px 0 0;">
                      <a href="https://www.google.com/maps/place/RAGHAV+GLOBAL+SCHOOL,+Sector+122+First+Entrance,+Block+A,+Sector+122,+Noida,+Uttar+Pradesh+201316" style="background:#2563eb; color:#fff; text-decoration:none; padding:8px 18px; border-radius:6px; font-size:13px; font-weight:600; display:inline-block;">View on Google Maps &#8594;</a>
                    </p>
                  </td>
                </tr>
              </table>

              <!-- PAIRINGS CARD -->
              <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0fdf4; border-left:4px solid #10b981; border-radius:8px; margin-bottom:20px;">
                <tr>
                  <td style="padding:20px 22px;">
                    <p style="margin:0 0 10px; font-size:15px; font-weight:700; color:#064e3b;">&#127760; Pairings &amp; Live Results</p>
                    <p style="margin:0 0 10px; font-size:14px; color:#475569; line-height:1.6;">Official pairings, standings, and live results will be published on the following platforms during the event:</p>
                    <p style="margin:0;">
                      <a href="https://chess-results.com" style="display:inline-block; background:#10b981; color:#fff; text-decoration:none; padding:7px 16px; border-radius:6px; font-size:13px; font-weight:600; margin-right:8px; margin-bottom:6px;">chess-results.com &#8594;</a>
                      <a href="https://chesscircuit.in" style="display:inline-block; background:#0f766e; color:#fff; text-decoration:none; padding:7px 16px; border-radius:6px; font-size:13px; font-weight:600; margin-bottom:6px;">chesscircuit.in &#8594;</a>
                    </p>
                  </td>
                </tr>
              </table>

              <!-- RULES CARD -->
              <table width="100%" cellpadding="0" cellspacing="0" style="background:#fffbeb; border-left:4px solid #f59e0b; border-radius:8px; margin-bottom:28px;">
                <tr>
                  <td style="padding:20px 22px;">
                    <p style="margin:0 0 12px; font-size:15px; font-weight:700; color:#78350f;">&#9888;&#65039; Important Rules &amp; Reminders</p>
                    <table cellpadding="0" cellspacing="0" width="100%">
                      <tr>
                        <td style="padding:5px 0; vertical-align:top; width:20px; font-size:14px; color:#92400e;">&#9658;</td>
                        <td style="padding:5px 0; font-size:14px; color:#57534e; line-height:1.6;">Carry a valid photo ID. FIDE titled players must carry their FIDE ID card. School students claiming concession must carry school ID.</td>
                      </tr>
                      <tr>
                        <td style="padding:5px 0; vertical-align:top; width:20px; font-size:14px; color:#92400e;">&#9658;</td>
                        <td style="padding:5px 0; font-size:14px; color:#57534e; line-height:1.6;">Players must bring their own water bottles. Complimentary refreshments will be provided at the venue.</td>
                      </tr>
                      <tr>
                        <td style="padding:5px 0; vertical-align:top; width:20px; font-size:14px; color:#92400e;">&#9658;</td>
                        <td style="padding:5px 0; font-size:14px; color:#57534e; line-height:1.6;">Electronic devices (including smartwatches and mobile phones) are strictly prohibited in the playing hall.</td>
                      </tr>
                      <tr>
                        <td style="padding:5px 0; vertical-align:top; width:20px; font-size:14px; color:#92400e;">&#9658;</td>
                        <td style="padding:5px 0; font-size:14px; color:#57534e; line-height:1.6;">Parents and guardians should stay outside the tournament hall and can take part in fun activities to win exclusive merchandise!</td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

              <!-- BEST OF LUCK -->
              <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #0f172a, #1e3a5f); border-radius:10px; margin-bottom:10px;">
                <tr>
                  <td style="padding:24px 28px; text-align:center;">
                    <p style="margin:0 0 6px; color:#fbbf24; font-size:22px;">&#9820;&#65039;</p>
                    <p style="margin:0 0 4px; color:#f8fafc; font-size:17px; font-weight:700;">Best of luck at the tournament!</p>
                    <p style="margin:0; color:#94a3b8; font-size:14px;">May every move bring you closer to victory.</p>
                  </td>
                </tr>
              </table>

              ${paymentId && paymentId !== 'FREE_ENTRY' ? `<p style="margin:14px 0 0; font-size:12px; color:#94a3b8; text-align:center;">Payment Reference: ${paymentId}</p>` : ''}

            </td>
          </tr>

          <!-- FOOTER -->
          <tr>
            <td style="background:#0f172a; border-radius:0 0 16px 16px; padding:24px 40px; text-align:center;">
              <img src="https://www.thechesslifestyle.com/favicon.png" alt="TCL Logo" width="32" height="32" style="margin-bottom:10px; border-radius:6px;">
              <p style="margin:0 0 6px; color:#f8fafc; font-size:14px; font-weight:600;">TheChessLifestyle</p>
              <p style="margin:0 0 10px; color:#64748b; font-size:12px;">Nurturing Champions, One Move at a Time.</p>
              <a href="https://www.thechesslifestyle.com" style="color:#60a5fa; font-size:12px; text-decoration:none;">www.thechesslifestyle.com</a>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

</body>
</html>
    `;

    await transporter.sendMail({
      from: `"TheChessLifestyle" <${process.env.GMAIL_USER}>`,
      to: email,
      subject: `You are in! Registration Confirmed - TCL Noida Premier League (${categoryLabel})`,
      html: htmlBody,
    });

    res.status(200).json({ success: true, message: 'Confirmation email sent!' });

  } catch (error) {
    console.error('Error sending confirmation email:', error);
    res.status(500).json({ error: 'Failed to send email', details: error.message });
  }
}

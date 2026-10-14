import Razorpay from 'razorpay';

export default async function handler(req, res) {
  // Add CORS headers so frontend can call this API
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  // Handle preflight request
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const {
    amount,
    category,
    player_name,
    parent_name,
    email,
    phone,
    country_code,
    dob,
    age,
    student_class,
    school,
    fide_id,
    fide_title,
    chess_username,
    chess_rating,
    concession,
    special_requirements
  } = req.body;

  if (!amount) {
    return res.status(400).json({ error: 'Amount is required' });
  }

  try {
    const razorpay = new Razorpay({
      key_id: process.env.RAZORPAY_KEY_ID,
      key_secret: process.env.RAZORPAY_KEY_SECRET,
    });

    const fullPhone = `${country_code || '+91'} ${phone || ''}`.trim();
    const classSchool = [student_class, school].filter(Boolean).join(' - ');
    const chessInfo = [chess_username, chess_rating].filter(Boolean).join(' / ');

    // Razorpay allows max 15 key-value pairs, max 256 chars each
    const notes = {
      event: 'TCL_Noida_Premier_League',
      category: String(category || 'Unknown').slice(0, 250),
      player_name: String(player_name || 'Unknown').slice(0, 250),
      parent_name: String(parent_name || '').slice(0, 250),
      email: String(email || '').slice(0, 250),
      phone: String(fullPhone).slice(0, 250),
      dob_or_age: String(dob || age || '').slice(0, 250),
      class_school: String(classSchool).slice(0, 250),
      fide_id: String(fide_id || '').slice(0, 250),
      fide_title: String(fide_title || 'None').slice(0, 250),
      chess_rating: String(chessInfo).slice(0, 250),
      concession: String(concession || 'None').slice(0, 250),
      special_req: String(special_requirements || '').slice(0, 250),
      amount_paid: `Rs. ${amount}`
    };

    const options = {
      amount: Math.round(Number(amount) * 100), // Razorpay takes amount in paisa (₹1 = 100 paisa)
      currency: 'INR',
      receipt: `tcl_${Date.now()}`,
      notes
    };

    const order = await razorpay.orders.create(options);
    res.status(200).json(order);
  } catch (error) {
    console.error('Error creating Razorpay order:', error);
    res.status(500).json({ error: 'Failed to create order', details: error.message });
  }
}

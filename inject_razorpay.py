import re

with open('tournament/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Razorpay checkout script before closing </body>
razorpay_script = '<script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n'
if razorpay_script not in html:
    html = html.replace('</body>', razorpay_script + '</body>')

# Remove action and method from both forms, and add ids
html = html.replace('<form action="https://formspree.io/f/xvzjjenb" method="POST">', '<form class="t-form">')

# Add modal HTML
modal_html = """
  <!-- Payment Summary Modal -->
  <div id="payment-summary-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.8); z-index:9999; justify-content:center; align-items:center;">
    <div style="background:#fff; border-radius:12px; padding:2rem; max-width:450px; width:90%; text-align:center; box-shadow:0 10px 40px rgba(0,0,0,0.3);">
      <h3 style="margin-top:0; font-family:'Outfit',sans-serif; font-size:1.5rem; color:#0f172a;">Registration Summary</h3>
      <div id="summary-content" style="margin:1.5rem 0; font-size:1rem; color:#334155; line-height:1.6;">
        <!-- dynamic content -->
      </div>
      <div style="display:flex; gap:1rem; justify-content:center; margin-top:1.5rem;">
        <button id="cancel-pay-btn" style="padding:0.75rem 1.5rem; border:1px solid #cbd5e1; background:#f8fafc; border-radius:8px; cursor:pointer; font-weight:600;">Cancel</button>
        <button id="proceed-pay-btn" style="padding:0.75rem 1.5rem; border:none; background:var(--primary); color:#fff; border-radius:8px; cursor:pointer; font-weight:600;">Proceed to Pay &rarr;</button>
      </div>
    </div>
  </div>
"""
if "payment-summary-modal" not in html:
    html = html.replace('</main>', modal_html + '\n  </main>')

# Add JS logic
js_logic = """
    // Razorpay Integration
    const modal = document.getElementById('payment-summary-modal');
    const summaryContent = document.getElementById('summary-content');
    const cancelBtn = document.getElementById('cancel-pay-btn');
    const proceedBtn = document.getElementById('proceed-pay-btn');
    
    let currentFormData = null;
    let currentAmount = 0;
    
    document.querySelectorAll('.t-form').forEach(form => {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const fd = new FormData(this);
        const data = Object.fromEntries(fd.entries());
        currentFormData = data;
        
        const baseFee = data.Category === 'Open' ? 500 : 300;
        const today = new Date();
        const earlyBirdDeadline = new Date('2026-10-20T00:00:00+05:30');
        
        let msg = '';
        currentAmount = baseFee;
        
        if (today < earlyBirdDeadline) {
           currentAmount = baseFee * 0.75;
           msg = `<div style="background:#ecfdf5; color:#065f46; padding:1rem; border-radius:8px; border:1px solid #a7f3d0; margin-bottom:1rem;">
                    <strong>✨ Early Bird Discount Auto-Applied!</strong><br>
                    You get 25% off because you are registering before 20th October.
                  </div>
                  <div style="font-size:1.2rem; font-weight:bold;">Total to Pay: ₹${currentAmount}</div>`;
        } else {
           msg = `<div style="font-size:1.2rem; font-weight:bold; margin-bottom:1rem;">Total to Pay: ₹${currentAmount}</div>`;
           if (data['Concession Applied'] && data['Concession Applied'] !== 'None' && data['Concession Applied'] !== 'Early Bird') {
             msg += `<div style="background:#fff7ed; color:#9a3412; padding:1rem; border-radius:8px; border:1px solid #fdba74; font-size:0.9rem;">
                        <strong>Note on Concession:</strong> You selected <em>${data['Concession Applied']}</em>. Please pay the full ₹${currentAmount} amount online today to secure your seat. You will receive your cash refund directly at the venue upon verifying your proof.
                     </div>`;
           }
        }
        
        summaryContent.innerHTML = msg;
        modal.style.display = 'flex';
      });
    });

    cancelBtn.addEventListener('click', () => { modal.style.display = 'none'; });

    proceedBtn.addEventListener('click', async () => {
      proceedBtn.innerText = 'Processing...';
      proceedBtn.disabled = true;
      
      try {
        // Call Vercel backend
        const res = await fetch('https://thechesslifestyle-hh3q0qqod-the-chess-lifestyle.vercel.app/api/create-order', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            amount: currentAmount,
            category: currentFormData.Category,
            player_name: currentFormData['Player Name']
          })
        });
        
        if (!res.ok) throw new Error('Failed to create order');
        const order = await res.json();
        
        const options = {
          key: "rzp_live_SO205h9L7UaQiV", // Live key injected directly as requested
          amount: order.amount,
          currency: order.currency,
          name: "TheChessLifestyle",
          description: "Tournament Registration",
          order_id: order.id,
          handler: async function (response) {
            // Payment success! Submit to formspree in background
            try {
              // Add Razorpay details to form data
              currentFormData['Razorpay Payment ID'] = response.razorpay_payment_id;
              currentFormData['Amount Paid'] = 'Rs. ' + currentAmount;
              
              const formBody = new URLSearchParams();
              for (const [key, val] of Object.entries(currentFormData)) {
                formBody.append(key, val);
              }
              
              await fetch('https://formspree.io/f/xvzjjenb', {
                method: 'POST',
                headers: { 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formBody.toString()
              });
              
              modal.style.display = 'none';
              alert("Payment Successful! Registration confirmed. We will email you shortly.");
              window.location.reload();
            } catch (err) {
              console.error(err);
              alert("Payment successful but form submission failed. Please contact support with your Payment ID: " + response.razorpay_payment_id);
            }
          },
          prefill: {
            name: currentFormData['Parent Name'] || currentFormData['Player Name'],
            email: currentFormData['Email'],
            contact: currentFormData['WhatsApp Number']
          },
          theme: { color: "#f59e0b" }
        };
        
        const rzp = new Razorpay(options);
        rzp.open();
        
      } catch (err) {
        console.error(err);
        alert("Something went wrong initializing the payment. Please try again.");
      } finally {
        proceedBtn.innerText = 'Proceed to Pay &rarr;';
        proceedBtn.disabled = false;
        modal.style.display = 'none';
      }
    });
"""
if "Razorpay Integration" not in html:
    html = html.replace('// Scroll reveal', js_logic + '\n    // Scroll reveal')

with open('tournament/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

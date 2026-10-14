const GOOGLE_SHEETS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwo_s7qWo-20Bw6PKItIPomJbiUlbUzc1_zaEW_aMhtu1rSOrRGvCdsBUMoax6N3njBmA/exec';

/**
 * Submits form data to the Google Sheets Apps Script Web App server-to-server.
 * Automatically follows 302 redirects with no browser CORS limitations.
 */
export async function submitToGoogleSheets(data) {
  const formBody = new URLSearchParams();
  for (const [key, val] of Object.entries(data)) {
    if (val !== undefined && val !== null) {
      formBody.append(key, String(val));
    }
  }

  // Attempt submission with retry for maximum resilience
  let lastError = null;
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      const res = await fetch(GOOGLE_SHEETS_SCRIPT_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formBody.toString(),
        redirect: 'follow',
      });

      if (!res.ok) {
        throw new Error(`Google Apps Script responded with HTTP ${res.status}`);
      }

      const text = await res.text();
      return { success: true, response: text };
    } catch (err) {
      lastError = err;
      console.warn(`Google Sheets submission attempt ${attempt} failed:`, err.message);
      if (attempt < 2) {
        await new Promise(r => setTimeout(r, 1000));
      }
    }
  }

  throw lastError;
}

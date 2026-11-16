// Receives the quote form and forwards it by email, so the destination inbox
// never appears in the page source. Set QUOTE_EMAIL in Vercel
// (Project → Settings → Environment Variables) to change where leads go.
const DEFAULT_TO = 'info@lowcountrysepticpros.com';
const SITE = 'https://www.lowcountrysepticpros.com';
const FIELDS = { name: 100, phone: 30, email: 120, town: 80, service: 60, message: 2000 };

function redirect(res, to) {
  res.statusCode = 303;
  res.setHeader('Location', to);
  res.setHeader('Cache-Control', 'no-store');
  res.end();
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.statusCode = 405;
    res.setHeader('Allow', 'POST');
    return res.end('Method not allowed');
  }

  let body = req.body || {};
  if (typeof body === 'string') body = Object.fromEntries(new URLSearchParams(body));

  // Bots fill the hidden field; humans never see it. Pretend it worked.
  if (body._honey) return redirect(res, '/thanks');

  const data = {};
  for (const [key, max] of Object.entries(FIELDS)) {
    data[key] = String(body[key] || '').trim().slice(0, max);
  }
  if (!data.name || !data.phone || !data.town) return redirect(res, '/quote-error');

  const to = process.env.QUOTE_EMAIL || DEFAULT_TO;
  try {
    const r = await fetch(`https://formsubmit.co/ajax/${encodeURIComponent(to)}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
        Origin: SITE,
        Referer: SITE + '/contact',
      },
      body: JSON.stringify({
        ...data,
        _subject: `New quote request: ${data.service || 'septic service'} in ${data.town}`,
        _template: 'table',
        _captcha: 'false',
        _replyto: data.email || undefined,
      }),
    });
    const text = await r.text();
    let out = {};
    try { out = JSON.parse(text); } catch (_) { /* non-JSON reply, logged below */ }
    if (r.ok && String(out.success) === 'true') return redirect(res, '/thanks');
    console.error('formsubmit rejected', r.status, text.slice(0, 500));
  } catch (err) {
    console.error('formsubmit failed', err);
  }
  return redirect(res, '/quote-error');
};

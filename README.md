# lowcountrysepticpros.com

Static marketing site for Lowcountry Septic Pros. Plain HTML/CSS, no build step, deploys to Vercel as-is.

## Files
- `index.html` – the main page (services, how it works, warning signs, service areas, FAQ, quote form)
- `styles.css` – all styling
- `thanks.html` – shown after the quote form is submitted
- `404.html`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `vercel.json`

## Before launch: replace placeholders
| What | Placeholder | Where |
|---|---|---|
| Phone | `(843) 555-0142` / `+18435550142` / `+1-843-555-0142` | index.html, thanks.html, 404.html |
| Email | `info@lowcountrysepticpros.com` | index.html (contact, footer, form action, JSON-LD) |
| Service towns | Charleston … Bluffton list | index.html (areas section + JSON-LD `areaServed`) |

## Quote form
Submits via FormSubmit (formsubmit.co) to the email in the form `action`. The first submission
sends a one-time activation email to that inbox — click it, and later submissions arrive normally.

## Local preview
    python3 -m http.server 8000

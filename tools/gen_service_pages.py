#!/usr/bin/env python3
"""Generate the per-service pages from index.html's shared header/footer.

Run from the repo root after changing the header, footer or service copy:
    python3 tools/gen_service_pages.py
The generated .html files are committed; Vercel serves them as-is.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").read_text()

PHONE_DISPLAY = "(843) 555-0142"
PHONE_TEL = "+18435550142"
SITE = "https://lowcountrysepticpros.com"


def grab(pattern):
    m = re.search(pattern, INDEX, re.S)
    if not m:
        raise SystemExit(f"index.html is missing a block matching {pattern!r}")
    return m.group(0)


SPRITE = grab(r'<!-- Icon sprite -->.*?</svg>\n')
HEADER = grab(r'<header class="site-header">.*?</header>')
FOOTER = grab(r'<footer class="site-footer">.*?</footer>')
MOBILE = grab(r'<div class="mobile-bar">.*?</div>')

SERVICES = [
    {
        "slug": "septic-pumping",
        "name": "Septic Tank Pumping",
        "title": "Septic Tank Pumping in the Lowcountry",
        "desc": "Septic tank pumping for homes and businesses across Charleston, Summerville, Beaufort and the SC Lowcountry. Call Lowcountry Septic Pros.",
        "lead": "Regular pumping is the single best thing you can do for your septic system. It keeps solids out of your drain field and heads off the backups and failures that cost thousands to fix.",
        "included_title": "What's included",
        "included": [
            "Locating and uncovering the tank lid(s)",
            "Pumping out all liquid and settled solids",
            "A visual check of the tank, inlet and outlet baffles",
            "Noting any signs of trouble, like high water levels or damaged parts",
            "A reminder when your next pumping is due",
        ],
        "signs_title": "When it's time to pump",
        "signs": [
            "It's been 3–5 years since your last pumping (or you don't know when it was)",
            "Drains are slow or toilets gurgle",
            "You notice sewage odors near the tank or drain field",
            "You're buying or selling a home",
        ],
        "faq": [
            ("How often should I pump?", "Most households should pump every 3 to 5 years. Larger families, smaller tanks and garbage disposals all shorten that interval."),
            ("Do I need to be home?", "Not always. As long as we can reach the tank and know where it is, we can often do the work while you're away. We'll confirm when you book."),
            ("Will it mess up my yard?", "We dig only what's needed to reach the lid and put the soil back when we're done. Installing a riser makes future pumpings quicker and cleaner."),
        ],
    },
    {
        "slug": "septic-inspections",
        "name": "Septic Inspections",
        "title": "Septic Inspections for Home Buyers & Sellers",
        "desc": "Septic system inspections for real estate transactions and homeowners in Charleston and the SC Lowcountry. Clear written reports.",
        "lead": "A septic system is buried and easy to overlook, but replacing one can cost more than a new roof. An inspection tells you exactly what you're dealing with before you close or before small problems grow.",
        "included_title": "What we check",
        "included": [
            "Tank condition, including cracks, leaks and corrosion",
            "Inlet and outlet baffles",
            "Liquid and sludge levels",
            "Signs of backup or surfacing wastewater in the drain field",
            "Pumps, alarms and filters, if your system has them",
            "A clear written report you can share with your agent or lender",
        ],
        "signs_title": "When to get an inspection",
        "signs": [
            "You're buying a home with a septic system",
            "You're listing your home and want to avoid surprises",
            "You've noticed odors, wet spots or slow drains",
            "You don't know the age or history of your system",
        ],
        "faq": [
            ("How long does an inspection take?", "Most residential inspections take a few hours on site, depending on how easy the tank is to reach."),
            ("Does the tank need to be pumped for an inspection?", "A full inspection usually includes pumping so we can see the inside of the tank and the baffles clearly. We'll explain the options when you book."),
            ("Can you work with my real estate agent's timeline?", "Yes. Let us know your closing date when you call, and we'll do our best to fit your schedule."),
        ],
    },
    {
        "slug": "septic-repair",
        "name": "Septic Repair",
        "title": "Septic System Repair",
        "desc": "Septic repair in Charleston and the SC Lowcountry: baffles, lids, pumps, lines and more. Fast, honest diagnosis from Lowcountry Septic Pros.",
        "lead": "When something goes wrong with your septic system, you need someone who finds the real cause and fixes it right, not just a quick patch that fails again next month.",
        "included_title": "Common repairs",
        "included": [
            "Broken or missing baffles",
            "Cracked or unsafe tank lids, and new risers",
            "Failed effluent or lift pumps and alarms",
            "Clogged or broken lines between the house and tank",
            "Root intrusion",
            "Distribution box repair and replacement",
        ],
        "signs_title": "Signs you need a repair",
        "signs": [
            "Sewage backing up into toilets, tubs or floor drains",
            "Gurgling pipes or slow drains throughout the house",
            "A septic alarm going off",
            "Strong odors in the yard or house",
        ],
        "faq": [
            ("Is a backup an emergency?", f"Yes. Stop using water in the house and call us at {PHONE_DISPLAY} right away."),
            ("Will you tell me the cost before you start?", "Yes. We diagnose the problem, explain what we found, and give you a price before any repair work begins."),
            ("Can my system be repaired, or does it need replacing?", "Many problems can be repaired for far less than a new system. We'll give you an honest answer either way."),
        ],
    },
    {
        "slug": "drain-field-repair",
        "name": "Drain Field Service",
        "title": "Drain Field Repair & Replacement",
        "desc": "Drain field diagnosis, repair and replacement for Lowcountry homes, built for high water tables and sandy soil. Lowcountry Septic Pros.",
        "lead": "The drain field is where your wastewater is treated and returned to the soil. In the Lowcountry, high water tables and heavy rain make drain fields work harder, so problems need attention quickly.",
        "included_title": "What we do",
        "included": [
            "Diagnose why the drain field is failing",
            "Clear and repair distribution lines where possible",
            "Repair or replace the distribution box",
            "Drain field replacement when repair isn't an option",
            "Help with permits for replacement work",
        ],
        "signs_title": "Signs of drain field trouble",
        "signs": [
            "Soggy ground or standing water over the drain field when it hasn't rained",
            "Grass that's unusually green and lush over the lines",
            "Sewage odors in the yard",
            "Slow drains even right after the tank was pumped",
        ],
        "faq": [
            ("Why do drain fields fail?", "The most common causes are solids escaping the tank because it wasn't pumped, too much water entering the system, roots, and vehicles driving over the lines."),
            ("Can a failing drain field be saved?", "Sometimes. If it's caught early, repairs can restore it. Severely saturated or damaged fields usually need replacement."),
            ("How can I protect my drain field?", "Pump your tank on schedule, spread out water use, keep vehicles and heavy equipment off it, and send roof runoff away from it."),
        ],
    },
    {
        "slug": "septic-installation",
        "name": "New System Installation",
        "title": "New Septic System Installation",
        "desc": "New and replacement septic system installation in Charleston and the SC Lowcountry, from site evaluation through final inspection.",
        "lead": "Building a new home or replacing a system that's reached the end of its life? We'll guide you through the process, from site evaluation and permitting to installation and final inspection.",
        "included_title": "How it works",
        "included": [
            "Site visit to understand your property and needs",
            "Coordinating the soil and site evaluation",
            "Handling the permit application with the state",
            "Installing the tank, lines and drain field",
            "Final inspection and approval",
        ],
        "signs_title": "When you need a new system",
        "signs": [
            "You're building on a lot without sewer service",
            "Your current system has failed and can't be repaired",
            "You're adding bedrooms and need more capacity",
            "Your system is decades old and having repeated problems",
        ],
        "faq": [
            ("How long does installation take?", "Installation itself is usually a few days, but permitting and site evaluation can take several weeks. We'll give you a realistic timeline up front."),
            ("Do I need a permit?", "Yes. New and replacement septic systems in South Carolina require a state permit. We'll help you through that process."),
            ("What affects the cost?", "Soil conditions, water table, lot layout, home size and the type of system required all play a role. We'll give you a clear quote after a site visit."),
        ],
    },
]


def page(s):
    e = html.escape
    url = f"{SITE}/{s['slug']}"
    others = [o for o in SERVICES if o["slug"] != s["slug"]]
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": s["name"],
                "serviceType": s["name"],
                "url": url,
                "provider": {"@type": "Plumber", "name": "Lowcountry Septic Pros", "telephone": "+1-843-555-0142", "url": SITE + "/"},
                "areaServed": {"@type": "State", "name": "South Carolina"},
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in s["faq"]
                ],
            },
        ],
    }
    included = "\n".join(
        f'            <li><svg aria-hidden="true"><use href="#i-check"/></svg><div><span>{e(i)}</span></div></li>'
        for i in s["included"]
    )
    signs = "\n".join(
        f'            <li><svg aria-hidden="true"><use href="#i-alert"/></svg><div><span>{e(i)}</span></div></li>'
        for i in s["signs"]
    )
    faq = "\n".join(
        f"          <details>\n            <summary>{e(q)}</summary>\n            <div><p>{e(a)}</p></div>\n          </details>"
        for q, a in s["faq"]
    )
    related = "\n".join(
        f'          <li><a href="/{o["slug"]}">{e(o["name"])}</a></li>' for o in others
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(s['title'])} | Lowcountry Septic Pros</title>
  <meta name="description" content="{e(s['desc'])}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#163b35">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(s['title'])} | Lowcountry Septic Pros">
  <meta property="og:description" content="{e(s['desc'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Lowcountry Septic Pros">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <script type="application/ld+json">
{json.dumps(schema, indent=2)}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  {SPRITE}
  {HEADER}

  <main id="main">
    <section class="hero hero--sub">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">/</span> <a href="/#services">Services</a> <span aria-hidden="true">/</span> <span>{e(s['name'])}</span></nav>
        <h1>{e(s['title'])}</h1>
        <p class="hero-lead">{e(s['lead'])}</p>
        <div class="hero-ctas">
          <a class="btn btn--primary" href="tel:{PHONE_TEL}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call {PHONE_DISPLAY}</a>
          <a class="btn btn--ghost" href="/#quote">Get a free quote</a>
        </div>
      </div>
      <svg class="hero-marsh" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true">
        <path d="M0 70c120-30 240-30 360 0s240 30 360 0 240-30 360 0 240 30 360 0v50H0z" fill="#faf7f0"/>
      </svg>
    </section>

    <section class="section">
      <div class="container split split--top">
        <div>
          <span class="eyebrow">{e(s['name'])}</span>
          <h2>{e(s['included_title'])}</h2>
          <ul class="checklist checklist--ok">
{included}
          </ul>
        </div>
        <div>
          <span class="eyebrow">Know the signs</span>
          <h2>{e(s['signs_title'])}</h2>
          <ul class="checklist">
{signs}
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">FAQ</span>
          <h2>{e(s['name'])} questions</h2>
        </div>
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container cta-band">
        <div>
          <h2>Ready to schedule?</h2>
          <p>Call now to talk with a septic pro, or request a free quote online.</p>
        </div>
        <div class="hero-ctas">
          <a class="btn btn--primary" href="tel:{PHONE_TEL}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call {PHONE_DISPLAY}</a>
          <a class="btn btn--ghost" href="/#quote">Request a quote</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <span class="eyebrow">More services</span>
        <ul class="areas related">
{related}
        </ul>
      </div>
    </section>
  </main>

  {FOOTER}

  {MOBILE}

  <script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>
"""


def main():
    for s in SERVICES:
        (ROOT / f"{s['slug']}.html").write_text(page(s))
        print("wrote", f"{s['slug']}.html")

    urls = [SITE + "/"] + [f"{SITE}/{s['slug']}" for s in SERVICES]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for i, u in enumerate(urls):
        sitemap.append(f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if i == 0 else '0.8'}</priority></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()

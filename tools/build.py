#!/usr/bin/env python3
"""Build every page of lowcountrysepticpros.com.

    python3 tools/build.py

Business details (phone, email, licence wording) live in BUSINESS below and are
applied to every page. Page copy lives in tools/pages/*.html (home, about,
contact, privacy, terms) and in tools/content_services.py and
tools/content_locations.py. The generated .html files in the repo root are
committed; Vercel serves them as-is (no build step on Vercel).
"""
import hashlib
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "tools" / "pages"
sys.path.insert(0, str(ROOT / "tools"))

from content_services import SERVICES  # noqa: E402
from content_locations import LOCATIONS, OTHER_AREAS  # noqa: E402

SITE = "https://www.lowcountrysepticpros.com"

BUSINESS = {
    "name": "Lowcountry Septic Pros",
    "phone": "(843) 310-4187",
    "tel": "+18433104187",
    "schema_tel": "+1-843-310-4187",
    "email": "info@lowcountrysepticpros.com",
    # Shown in the footer and on the About page. Keep it accurate: either the
    # company's own SCDES licence number, or a line saying which licensed
    # contractor performs the work.
    "license": (
        "Septic work in South Carolina is licensed and permitted by the SC "
        "Department of Environmental Services (SCDES). Every job we take on is "
        "performed by an SCDES-licensed contractor, and we provide licence "
        "details with every written quote."
    ),
    "updated": "November 16, 2026",
    # Where the quote form posts. FormSubmit sits behind Cloudflare's bot check,
    # so it must be posted from the visitor's browser, not from a server.
    # After activating, replace the email with the random alias FormSubmit
    # emails you (https://formsubmit.co/<alias>) so the inbox isn't in the page.
    "form_endpoint": "https://formsubmit.co/info@lowcountrysepticpros.com",
}

TOKENS = {
    "{{PHONE}}": BUSINESS["phone"],
    "{{TEL}}": BUSINESS["tel"],
    "{{EMAIL}}": BUSINESS["email"],
    "{{LICENSE}}": BUSINESS["license"],
    "{{UPDATED}}": BUSINESS["updated"],
    "{{FORM_ENDPOINT}}": BUSINESS["form_endpoint"],
    "{{SITE}}": SITE,
}

# WhatConverts call and lead tracking (account 180383). Swaps the phone number
# shown on the page for a tracking number and records calls and form leads.
TRACKING = (
    '<script>var $wc_load=function(a){return  JSON.parse(JSON.stringify(a))},$wc_leads=$wc_leads||'
    '{doc:{url:$wc_load(document.URL),ref:$wc_load(document.referrer),search:$wc_load(location.search),'
    'hash:$wc_load(location.hash)}};</script>\n'
    '  <script src="https://s.ksrndkehqnwntyxlhgto.com/180383.js"></script>'
)

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700'
    '&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">'
)

e = html.escape


def fill(text):
    for k, v in TOKENS.items():
        text = text.replace(k, v)
    return text


def read(name):
    return (PAGES / name).read_text()


SPRITE = read("_sprite.html")
QUOTE_FORM = read("_quote_form.html")


def business_schema(full=True):
    s = {
        "@type": "HomeAndConstructionBusiness",
        "@id": SITE + "/#business",
        "name": BUSINESS["name"],
        "url": SITE + "/",
        "telephone": BUSINESS["schema_tel"],
        "email": BUSINESS["email"],
    }
    if full:
        s.update({
            "description": "Septic tank pumping, inspections, repairs, drain field service and new system installation across the South Carolina Lowcountry.",
            "logo": SITE + "/favicon.svg",
            "image": SITE + "/og-image.png",
            "priceRange": "$$",
            "address": {"@type": "PostalAddress", "addressRegion": "SC", "addressCountry": "US"},
            "areaServed": [
                {"@type": "City", "name": f"{loc['name']}, SC"} for loc in LOCATIONS
            ] + [{"@type": "City", "name": f"{a}, SC"} for a in OTHER_AREAS],
            "knowsAbout": ["Septic tank pumping", "Septic inspections", "Septic repair",
                           "Drain field repair", "Septic system installation"],
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": "Septic services",
                "itemListElement": [
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s_["name"], "url": f"{SITE}/{s_['slug']}"}}
                    for s_ in SERVICES
                ],
            },
        })
    return s


def breadcrumb_schema(trail):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + path}
            for i, (name, path) in enumerate(trail)
        ],
    }


def faq_schema(faq):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }


def header():
    return f"""<header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="/" aria-label="{BUSINESS['name']} home">
        <svg aria-hidden="true"><use href="#logo"/></svg>
        <span class="brand-name">{BUSINESS['name']}<small>Pumping · Inspections · Repair</small></span>
      </a>
      <nav class="nav" aria-label="Main">
        <a href="/#services">Services</a>
        <a href="/service-areas">Service Areas</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
        <a class="btn btn--primary header-call" href="tel:{{{{TEL}}}}" aria-label="Call {{{{PHONE}}}}"><svg aria-hidden="true"><use href="#i-phone"/></svg><span class="hc-full">{{{{PHONE}}}}</span><span class="hc-short">Call</span></a>
      </nav>
    </div>
  </header>"""


def footer():
    services = "\n".join(f'            <li><a href="/{s["slug"]}">{e(s["name"])}</a></li>' for s in SERVICES)
    areas = "\n".join(f'            <li><a href="/{l["slug"]}">{e(l["name"])}</a></li>' for l in LOCATIONS)
    return f"""<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="/">
            <svg aria-hidden="true"><use href="#logo"/></svg>
            <span class="brand-name">{BUSINESS['name']}<small>Pumping · Inspections · Repair</small></span>
          </a>
          <p>Septic pumping, inspections, repairs and drain field service across the South Carolina Lowcountry.</p>
          <p class="footer-license">{{{{LICENSE}}}}</p>
          <p><a href="tel:{{{{TEL}}}}">{{{{PHONE}}}}</a><br><a href="mailto:{{{{EMAIL}}}}">{{{{EMAIL}}}}</a></p>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
{services}
          </ul>
        </div>
        <div>
          <h4>Service areas</h4>
          <ul>
{areas}
            <li><a href="/service-areas">All service areas</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="/about">About us</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/contact#quote">Free quote</a></li>
            <li><a href="/privacy">Privacy policy</a></li>
            <li><a href="/terms">Terms of use</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">© <span id="yr">2026</span> {BUSINESS['name']}. All rights reserved.</div>
    </div>
  </footer>

  <div class="mobile-bar">
    <a class="btn btn--primary" href="tel:{{{{TEL}}}}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call now</a>
    <a class="btn btn--ghost" href="/contact#quote">Free quote</a>
  </div>"""


CSS_VER = hashlib.sha1((ROOT / "styles.css").read_bytes()).hexdigest()[:10]


def layout(path, title, desc, main, schema=None, noindex=False):
    url = SITE + path
    graph = schema or []
    ld = ""
    if graph:
        ld = ('\n  <script type="application/ld+json">\n'
              + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2)
              + "\n  </script>")
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">{robots}
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#163b35">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="{BUSINESS['name']}">
  <meta property="og:image" content="{SITE}/og-image.png">
  {FONTS}
  <link rel="stylesheet" href="/styles.css?v={CSS_VER}">{ld}
  {TRACKING}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  {SPRITE}
  {header()}

  {main}

  {footer()}

  <script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>
"""
    return fill(page)


def sub_hero(crumbs, h1, lead, ctas=True):
    trail = ' <span aria-hidden="true">/</span> '.join(
        f'<a href="{p}">{e(n)}</a>' if p else f"<span>{e(n)}</span>" for n, p in crumbs
    )
    buttons = ""
    if ctas:
        buttons = """
        <div class="hero-ctas">
          <a class="btn btn--primary" href="tel:{{TEL}}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call {{PHONE}}</a>
          <a class="btn btn--ghost" href="/contact#quote">Get a free quote</a>
        </div>"""
    return f"""<section class="hero hero--sub">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb">{trail}</nav>
        <h1>{e(h1)}</h1>
        <p class="hero-lead">{lead}</p>{buttons}
      </div>
      <svg class="hero-marsh" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true">
        <path d="M0 70c120-30 240-30 360 0s240 30 360 0 240-30 360 0 240 30 360 0v50H0z" fill="#faf7f0"/>
      </svg>
    </section>"""


def cta_band(h="Ready to schedule?", p="Call now to talk with a septic pro, or request a free quote online."):
    return f"""<section class="section section--dark">
      <div class="container cta-band">
        <div>
          <h2>{e(h)}</h2>
          <p>{e(p)}</p>
        </div>
        <div class="hero-ctas">
          <a class="btn btn--primary" href="tel:{{{{TEL}}}}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call {{{{PHONE}}}}</a>
          <a class="btn btn--ghost" href="/contact#quote">Request a quote</a>
        </div>
      </div>
    </section>"""


def prose(sections):
    """sections: list of (h2, [paragraph html, ...]) -> article blocks."""
    out = []
    for h, paras in sections:
        body = "\n".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in paras)
        out.append(f"<h2>{e(h)}</h2>\n{body}")
    return "\n\n".join(out)


def faq_block(title, faq, alt=True):
    items = "\n".join(
        f"""          <details>
            <summary>{e(q)}</summary>
            <div><p>{e(a)}</p></div>
          </details>""" for q, a in faq
    )
    return f"""<section class="section{' section--alt' if alt else ''}">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">FAQ</span>
          <h2>{e(title)}</h2>
        </div>
        <div class="faq">
{items}
        </div>
      </div>
    </section>"""


def cost_table(rows, note):
    trs = "\n".join(f"<tr><th scope=\"row\">{e(k)}</th><td>{e(v)}</td></tr>" for k, v in rows)
    return f"""<div class="cost">
<table>
<thead><tr><th scope="col">Job</th><th scope="col">Typical range</th></tr></thead>
<tbody>
{trs}
</tbody>
</table>
<p class="cost-note">{e(note)}</p>
</div>"""


def chips(links):
    return "\n".join(f'          <li><a href="{h}">{e(n)}</a></li>' for n, h in links)


# ---------------------------------------------------------------- pages

def build_home():
    main = read("home.html")
    schema = [business_schema(), {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BUSINESS["name"]}]
    return layout(
        "/",
        "Septic Pumping, Inspections & Repair in the SC Lowcountry | Lowcountry Septic Pros",
        "Septic tank pumping, inspections, repairs and drain field service in Charleston, Mount Pleasant, Summerville, Beaufort and across the SC Lowcountry. Upfront pricing.",
        main.replace("{{QUOTE_FORM}}", QUOTE_FORM),
        schema,
    )


def build_service(s):
    path = "/" + s["slug"]
    others = [(o["name"], "/" + o["slug"]) for o in SERVICES if o is not s]
    areas = [(f"{l['name']}", "/" + l["slug"]) for l in LOCATIONS]
    included = "\n".join(f'            <li><svg aria-hidden="true"><use href="#i-check"/></svg><div><span>{e(i)}</span></div></li>' for i in s["included"])
    signs = "\n".join(f'            <li><svg aria-hidden="true"><use href="#i-alert"/></svg><div><span>{e(i)}</span></div></li>' for i in s["signs"])
    main = f"""<main id="main">
    {sub_hero([("Home", "/"), ("Services", "/#services"), (s["name"], None)], s["title"], e(s["lead"]))}

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

    <section class="section section--tight">
      <div class="container article">
{prose(s['body'])}

<h2>What does {e(s['name'].lower())} cost?</h2>
{"".join(f"<p>{p}</p>" for p in s['cost_intro'])}
{cost_table(s['cost'], s['cost_note'])}
      </div>
    </section>

    {faq_block(s['name'] + " questions", s['faq'])}

    {cta_band()}

    <section class="section">
      <div class="container">
        <span class="eyebrow">More services</span>
        <ul class="areas related">
{chips(others)}
        </ul>
        <span class="eyebrow" style="margin-top:28px">Where we work</span>
        <ul class="areas related">
{chips(areas)}
          <li><a href="/service-areas">All service areas</a></li>
        </ul>
      </div>
    </section>
  </main>"""
    schema = [
        business_schema(full=False),
        {"@type": "Service", "name": s["name"], "serviceType": s["name"], "url": SITE + path,
         "provider": {"@id": SITE + "/#business"},
         "areaServed": [{"@type": "City", "name": f"{l['name']}, SC"} for l in LOCATIONS]},
        faq_schema(s["faq"]),
        breadcrumb_schema([("Home", "/"), (s["name"], path)]),
    ]
    return layout(path, f"{s['title']} | {BUSINESS['name']}", s["desc"], main, schema)


def build_location(l):
    path = "/" + l["slug"]
    svc = "\n".join(
        f'          <li><a href="/{s["slug"]}">{e(s["name"])}</a></li>' for s in SERVICES
    )
    hoods = "\n".join(f"          <li>{e(n)}</li>" for n in l["neighborhoods"])
    nearby = [(n, "/" + x["slug"]) for n in l["nearby"] for x in LOCATIONS if x["name"] == n]
    main = f"""<main id="main">
    {sub_hero([("Home", "/"), ("Service areas", "/service-areas"), (l["name"], None)], l["h1"], e(l["lead"]))}

    <section class="section section--tight">
      <div class="container article">
{prose(l['body'])}

<h2>Septic services in {e(l['name'])}</h2>
<p>{e(l['services_intro'])}</p>
<ul class="link-list">
{svc}
</ul>

<h2>Areas we cover around {e(l['name'])}</h2>
<p>{e(l['areas_intro'])}</p>
<ul class="areas">
{hoods}
</ul>
      </div>
    </section>

    {faq_block(f"Septic questions from {l['name']} homeowners", l['faq'])}

    {cta_band(f"Need septic service in {l['name']}?", "Call now to talk with a septic pro, or request a free quote online.")}

    <section class="section">
      <div class="container">
        <span class="eyebrow">Nearby areas</span>
        <ul class="areas related">
{chips(nearby)}
          <li><a href="/service-areas">All service areas</a></li>
        </ul>
      </div>
    </section>
  </main>"""
    schema = [
        business_schema(full=False),
        {"@type": "Service", "name": f"Septic services in {l['name']}, SC", "serviceType": "Septic services",
         "url": SITE + path, "provider": {"@id": SITE + "/#business"},
         "areaServed": {"@type": "City", "name": f"{l['name']}, SC"}},
        faq_schema(l["faq"]),
        breadcrumb_schema([("Home", "/"), ("Service areas", "/service-areas"), (l["name"], path)]),
    ]
    return layout(path, f"{l['title']} | {BUSINESS['name']}", l["desc"], main, schema)


def build_service_areas():
    cards = "\n".join(
        f"""          <article class="card">
            <div class="card-icon"><svg aria-hidden="true"><use href="#i-pin"/></svg></div>
            <h3><a href="/{l['slug']}">{e(l['name'])}</a></h3>
            <p>{e(l['card'])}</p>
          </article>""" for l in LOCATIONS
    )
    others = "\n".join(f"          <li>{e(a)}</li>" for a in OTHER_AREAS)
    main = f"""<main id="main">
    {sub_hero([("Home", "/"), ("Service areas", None)], "Septic service across the Lowcountry",
              "We serve homes and businesses in Charleston, Berkeley, Dorchester, Colleton and Beaufort counties. Find your area below, or call and we'll tell you if we cover your address.")}

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Main service areas</span>
          <h2>Local septic service, town by town</h2>
          <p>Each area has its own soils, water tables and permitting history. These pages cover what homeowners there should know.</p>
        </div>
        <div class="grid-2">
{cards}
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Also serving</span>
          <h2>Other Lowcountry communities</h2>
          <p>We also work throughout these communities. Don't see yours? <a href="tel:{{{{TEL}}}}">Give us a call</a>.</p>
        </div>
        <ul class="areas">
{others}
        </ul>
      </div>
    </section>

    {cta_band("Not sure if we cover your address?", "Call and we'll tell you right away, or send us your zip code with a quote request.")}
  </main>"""
    schema = [business_schema(full=False), breadcrumb_schema([("Home", "/"), ("Service areas", "/service-areas")])]
    return layout("/service-areas", "Septic Service Areas in the SC Lowcountry | Lowcountry Septic Pros",
                  "Lowcountry Septic Pros serves Charleston, Mount Pleasant, Summerville, Beaufort and communities across Charleston, Berkeley, Dorchester, Colleton and Beaufort counties.",
                  main, schema)


def build_static(name, path, title, desc, crumb, h1, lead, ctas=True, schema_extra=None):
    body = read(name).replace("{{QUOTE_FORM}}", QUOTE_FORM)
    main = f"""<main id="main">
    {sub_hero([("Home", "/"), (crumb, None)], h1, lead, ctas)}
{body}
  </main>"""
    schema = [business_schema(full=(path in ("/about", "/contact"))),
              breadcrumb_schema([("Home", "/"), (crumb, path)])] + (schema_extra or [])
    return layout(path, title, desc, main, schema)


def build_simple(h1, text, title):
    main = f"""<main id="main" class="simple-page">
    <div>
      <h1>{e(h1)}</h1>
      <p>{text}</p>
      <div class="btns">
        <a class="btn btn--dark" href="/">Back to home</a>
        <a class="btn btn--primary" href="tel:{{{{TEL}}}}">Call {{{{PHONE}}}}</a>
      </div>
    </div>
  </main>"""
    return layout("/" + title.lower().replace(" ", "-"), f"{title} | {BUSINESS['name']}", text, main, noindex=True)


def main():
    out = {}
    out["index.html"] = build_home()
    for s in SERVICES:
        out[s["slug"] + ".html"] = build_service(s)
    for l in LOCATIONS:
        out[l["slug"] + ".html"] = build_location(l)
    out["service-areas.html"] = build_service_areas()
    out["about.html"] = build_static(
        "about.html", "/about", "About Us | Lowcountry Septic Pros",
        "Who we are, how we work, and the licensing behind every septic job Lowcountry Septic Pros takes on.",
        "About", "About Lowcountry Septic Pros",
        "A local septic company built around one idea: tell people the truth about their system, price the job before we start, and do the work right.")
    out["contact.html"] = build_static(
        "contact.html", "/contact", "Contact Us & Free Quote | Lowcountry Septic Pros",
        "Call, email or request a free septic quote from Lowcountry Septic Pros. Serving Charleston, Mount Pleasant, Summerville, Beaufort and the SC Lowcountry.",
        "Contact", "Contact us",
        "Call for the fastest answer, or send a quote request and we'll get back to you.", ctas=False)
    out["privacy.html"] = build_static(
        "privacy.html", "/privacy", "Privacy Policy | Lowcountry Septic Pros",
        "How Lowcountry Septic Pros collects, uses and protects the information you share through this website.",
        "Privacy policy", "Privacy policy", "Last updated {{UPDATED}}", ctas=False)
    out["terms.html"] = build_static(
        "terms.html", "/terms", "Terms of Use | Lowcountry Septic Pros",
        "Terms of use for the Lowcountry Septic Pros website.",
        "Terms of use", "Terms of use", "Last updated {{UPDATED}}", ctas=False)
    out["thanks.html"] = build_simple(
        "Thanks, we got your request!",
        "We'll get back to you shortly. If your septic issue is urgent, give us a call and we'll help right away.",
        "Thank you")
    out["quote-error.html"] = build_simple(
        "We couldn't send your request",
        "Something went wrong on our end and your request didn't go through. Please call us, or email {{EMAIL}}, and we'll help right away.",
        "Quote error")
    out["404.html"] = build_simple(
        "Page not found", "Sorry, that page doesn't exist. Head back home or give us a call.", "Page not found")

    for name, content in out.items():
        assert "{{" not in content, f"unfilled token in {name}"
        (ROOT / name).write_text(content)

    indexable = ["/"] + ["/" + s["slug"] for s in SERVICES] + ["/service-areas"] + \
        ["/" + l["slug"] for l in LOCATIONS] + ["/about", "/contact", "/privacy", "/terms"]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in indexable:
        pr = "1.0" if p == "/" else ("0.3" if p in ("/privacy", "/terms") else "0.8")
        lines.append(f"  <url><loc>{SITE}{'' if p == '/' else p}{'/' if p == '/' else ''}</loc><priority>{pr}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n")
    print(f"built {len(out)} pages + sitemap.xml ({len(indexable)} URLs)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Replace static contact booking wizard with Web3Forms contact form."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONTACT = ROOT / "contact" / "index.html"

FORM_BLOCK = """<div class="reveal contact-lead-flow-card"><form class="contact-form" id="zenpho-contact-form" action="https://api.web3forms.com/submit" method="POST"><input type="hidden" name="access_key" value="48bbfd1a-f82b-4dcb-a293-3b9ab9e2e87a"><input type="hidden" name="subject" value="New contact — zenpho.com"><input type="checkbox" name="botcheck" class="hidden" style="display:none" tabindex="-1" autocomplete="off"><div class="cta-form-row cta-form-row-three" style="gap:24px"><label>Your name<input type="text" name="name" placeholder="Jane Doe" required></label><label>Email<input type="email" name="email" placeholder="jane@brand.com" required></label><label>Phone<input type="tel" name="phone" placeholder="(786) 555-0123" required></label></div><div class="cta-form-row" style="gap:24px"><label>Company<input type="text" name="company" placeholder="Brand Co."></label><label>I want to build…<select name="product_type" required><option value="" disabled selected>Select…</option><option>A custom website</option><option>An e-commerce store</option><option>A web app / SaaS MVP</option><option>A mobile app</option><option>Something else</option></select></label></div><label>Budget range<select name="budget_range" required><option value="" disabled selected>Select…</option><option>Under $5k</option><option>$5k — $15k</option><option>$15k — $40k</option><option>$40k+</option><option>Retainer</option></select></label><label>What do you need?<textarea name="message" rows="4" placeholder="A few sentences about the product, audience and timeline."></textarea></label><p id="zenpho-contact-error" role="alert" style="display:none;margin:0;color:#9a1d1d;font-size:14px;font-family:var(--display)"></p><button type="submit" class="btn-primary" style="align-self:flex-start;margin-top:8px">Book the call <span class="btn-arrow">↗</span></button></form><div id="zenpho-contact-success" style="display:none;padding:32px 0;font-family:var(--serif);font-style:italic;font-size:30px;line-height:1.25;color:var(--fg)">Received with grace.<div style="margin-top:16px;font-size:20px;opacity:0.7">A reply will follow within 12 hours.</div></div></div>"""

SCRIPT_TAG = '<script src="/contact-web3forms.js" defer></script>'


def main() -> None:
    html = CONTACT.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<div class="reveal contact-lead-flow-card">.*?</div>\s*(?=<div class="contact-info">)',
        re.DOTALL,
    )
    if not pattern.search(html):
        raise SystemExit("contact-lead-flow-card block not found")
    html = pattern.sub(FORM_BLOCK + "\n", html, count=1)
    if SCRIPT_TAG not in html:
        html = html.replace("</body></html>", SCRIPT_TAG + "</body></html>")
    CONTACT.write_text(html, encoding="utf-8")
    print("Patched", CONTACT)


if __name__ == "__main__":
    main()

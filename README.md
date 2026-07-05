# Zenpho marketing website (static)

Pre-built static export of the Zenpho marketing site for hosting on **Cloudflare Pages** (no build step).

## Cloudflare Pages setup

1. Workers & Pages → Create application → Connect to Git
2. Select this repo (`janselazo/zenpho-website`)
3. Configure:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/` (repository root)
4. Deploy and attach your domain (`zenpho.com`, `www.zenpho.com`)

If a deploy fails on an old commit, use **Deployments → Create deployment → `main`** (latest), not **Retry** on the failed build.

## Included

- Marketing pages (home, about, services, solutions, blog, pricing, contact, landing pages, etc.)
- `_redirects` for pretty URLs on Cloudflare
- `404.html` fallback

## Not included

- Revenue Leak Audit and Branding tools (server/API required; preserved in the main app backup)
- Working contact/booking form submissions (display only; no backend)

## Source

Exported from the Zenpho Next.js app on 2026-07-04. Full app restore package lives in SharePoint (`Zenpho Backup`).

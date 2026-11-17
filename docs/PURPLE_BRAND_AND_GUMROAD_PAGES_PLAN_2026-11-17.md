# Vave Workflow Store — Violet brand and native Gumroad Pages migration
Date: 2026-11-17 | Status: Public storefront preview refreshed; Gumroad native page not yet deployed.

## Brand identity
- Main background: **#10091D** — deep violet-black
- Surface/panels: **#1B102F / #26163D** — layered dark purple
- Primary action: **#B88AFF** transitioning to **#E4A2F3** — bright violet/lilac pink
- Secondary purple: **#AD7AF9**
- Main text: **#F8F4FF**
- Muted text: **#B7A8CE**
- Suggested font: **Inter** (available in Gumroad theme), with generous spacing, rounded cards, restrained glow effects and high contrast
- Brand mark: **V/** in violet gradient. Product illustrations and social banners should align with the existing purple Content Repurposer Gumroad assets; don't reuse the older blue HQ design as the public store identity.
- Contact for this project exclusively **vaveworkflows@gmail.com**.

## Public preview (existing independent website)
- Storefront: https://vavebusiness.github.io/vaveworkflows/storefront/
- Affiliate applications: https://vavebusiness.github.io/vaveworkflows/storefront/affiliates.html
- Both currently show prelaunch information; no live checkout, live subscriber signup, or active affiliate links.
- Avoid promising capabilities beyond current verified scope: it generates written repurposing drafts from original text; it does not edit videos or auto-publish.

## Preferred production deployment: native Gumroad Pages
Gumroad's current "Build a website on Gumroad" documentation describes custom HTML profile pages, uploaded via the Gumroad Pages workflow/CLI. Standalone pages can also be published (e.g. /affiliates). This means the visual design can be rebuilt directly on the Gumroad store, not merely linked from an external website. **Do not copy and paste the GitHub source unchanged and assume it will work.** Adapt the page to Gumroad's page/data system, remove fake checkout/subscriber controls, test actual functionality, and preview before publishing.

### Migration sequence
1. In the authenticated seller account, open **Pages → Home** and obtain the provided agent/developer prompt; use it for the custom HTML profile workflow, including a Gumroad preview before pushing.
2. Port the Vave violet visual design, accessible responsive layout and content. Use Gumroad's `gumroad-data` and `gumroad-prices` product data on the custom **profile** page rather than hardcoded checkout URLs or prices when possible; those datasets do not appear in standalone pages.
3. In **Settings → Profile → Design**, set background **#10091D**, highlight **#B88AFF**, font **Inter**. These settings apply to Gumroad product pages, checkout, posts and eligible Gumroad emails; a custom profile HTML page retains its own CSS.
4. Publish the separate Affiliate Program page via Gumroad Pages once affiliate enrollment is actually enabled. Until then use a truthful `mailto:vaveworkflows@gmail.com` application link.
5. Verify the real **Vave Content Repurposer** price (**$19.99**, confirmed during seller handoff, not earlier HQ's old $49 concept price), published product URL, actual customer ZIP and checkout requirements before connecting a buy button.
6. Enable native Gumroad audience/subscription controls and Gumroad's available email workflows once account and workflow eligibility is verified. Never import creator outreach addresses as subscribers without consent.
7. Preserve **60% affiliate attribution**: use each approved affiliate's actual Gumroad tracking link. Test it through the final checkout path; don't replace with a generic link that could discard referral attribution.
8. Verify desktop/mobile rendering, accessibility, preview metadata, live buy flow, receipt/download, email routing and contact destination before changing the preview label to "Live."

## Alternative deployment: external website plus Gumroad checkout
Keep the current GitHub Pages website as the branded storefront, using Gumroad's verified product link or its Overlay/Embed widget. Checkout is completed on Gumroad, not entirely on the external site. This option requires less migration, but storefront pages and product metadata must be manually maintained or connected to a reliable data source.

## Guardrails
- Customer facing Vave pages are separate from internal Vave Workflow Store HQ and **Vave Automations**.
- No Gumroad login, custom page push, payments, affiliate activation or email workflow sends have been performed by this plan.
- Native Gumroad custom Pages setup and seller theme changes require authenticated account access; do not claim those actions are complete until checked.
- Source: https://gumroad.com/help/article/124-your-gumroad-profile-page
- Source: https://gumroad.com/help/article/44-build-gumroad-into-your-website

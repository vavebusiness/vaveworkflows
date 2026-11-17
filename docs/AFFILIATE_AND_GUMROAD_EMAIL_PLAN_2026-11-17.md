# Vave Workflow Store — Affiliate Program & Gumroad Email Funnel

**Planning snapshot:** 2026-11-17  
**Business:** Vave Workflow Store only (not Vave Automations)  
**Project contact / customer support:** vaveworkflows@gmail.com  
**Initial offer:** Vave Content Repurposer — planned $19.99 one-time; proposed **60%** affiliate commission on qualifying attributed sales. Product and affiliate program remain unpublished/unverified until seller-side configuration is checked.

## 1. Affiliate Program in the custom storefront

### Application-based, not automatic acceptance

The storefront has a customer-facing Affiliate Program section and a dedicated `/storefront/affiliates.html` page. Until a legitimate Gumroad affiliate application URL and seller eligibility are verified, the CTA is a **mailto:** application to vaveworkflows@gmail.com, not a pretend functioning signup form.

On application, ask only for public channel/website, primary audience, country, typical content, and why the product fits. Verify channel authenticity and relevant engagement. Invite suitable reviewers to inspect a finished product before approving commission-only promotion. Do not promise a favorable review.

Once the Gumroad product is published, seller eligibility is resolved, and affiliate settings are configured:

1. Verify Gumroad's seller affiliate application page (often the creator-profile `/affiliates` path) in the actual account before placing its exact URL on the storefront.
2. Configure **60%** for Vave Content Repurposer, subject to seller-side verification and applicable fees. Confirm payment/commission terms and attribution behavior.
3. Approve the application using the affiliate's genuine Gumroad-associated account email and send the official **individual tracked Gumroad link**. Do not invent tracking parameters.
4. Give approved affiliates a factual demo, product images, setup-guide summary, examples, refund/support boundaries and clear affiliate-disclosure guidance.
5. Track approved affiliates separately from applicants, reviewers and paid sponsorship prospects.

**Economics:** $19.99 × 60% = $11.994 gross attributable affiliate commission before any applicable processing/platform fees or adjustments. Seller's gross pre-fee share is about $8.00. Final platform and tax effects must be verified in Gumroad. No guaranteed earnings claims.

**Attribution:** Partners should use their own tracked Gumroad product link. A generic link to the custom storefront may not preserve affiliate attribution without testing and proper configuration. Custom storefront checkout can redirect buyers to Gumroad; Gumroad remains the merchant checkout and delivery service.

## 2. Gumroad's actual automation constraints

Gumroad's **Workflows** support **New subscriber**, **Purchase**, **New affiliate**, **Member cancels**, and **Abandoned cart** triggers. Workflows can be prepared and previewed before publication.

**Critical limitation:** Gumroad documentation currently states workflows cannot **send** until the creator has earned **$100 after fees and received a payout**. Do not claim the launch funnel will automatically email before that requirement is met. An initial subscriber/lead-generation stage can be built, but the actual automated sending is blocked until eligibility is met. See: https://gumroad.com/help/article/131-using-workflows-to-send-automated-updates

**Sender / Rule #1:** Gumroad Workflow messages technically send from an `@gumroad.com` address using the Gumroad profile display name. Set the support and reply-to destination to **vaveworkflows@gmail.com**. Any manually sent project outreach, support or newsletters outside Gumroad must use only **vaveworkflows@gmail.com**. Never use an account belonging to another project.

Gumroad's draft-product **waitlist** feature and account subscribe page may help collect opt-ins before release. Verify the actual seller username and opt-in URL before linking them; do not invent a subscription destination. See https://gumroad.com/help/article/170-audience

## 3. Funnel map

| Audience | Trigger | Timing | Email theme | Condition |
|---|---|---|---|---|
| Prospective followers | Gumroad **New subscriber** | Day 0 | Welcome; practical Make/content tip, clear limits | Only once Gumroad emails are unlocked |
| Prospective followers | Same workflow | Day 2 | Sample transcript → human-reviewed draft example | Exclude existing buyers where supported |
| Prospective followers | Same workflow | Day 5 | First product overview and links, **only once live** | Stop to people who purchased |
| Interested non-buyers | Gumroad **Abandoned cart** | Fixed 24 hours | Reminder of product and setup requirements | Use Gumroad's fixed workflow, only after unlocked |
| Buyers | Normal Gumroad purchase | Immediately | Official receipt, access to ZIP | Do not duplicate with marketing email |
| Buyers | Gumroad **Purchase** workflow | Day 1 | Quick-start installation and own API connection checklist | After workflow emailing eligibility |
| Buyers | Same workflow | Day 4 | Example input/output, common troubleshooting, support | After workflow emailing eligibility |
| Buyers | Same workflow | Day 8 | Ask if import worked; invite honest feedback | After workflow emailing eligibility |
| Approved affiliates | Gumroad **New affiliate** | Day 0 | Tracking link, approved images, clear affiliate disclosures | Only after program is active |
| Approved affiliates | Same workflow | Day 3 | Practical, honest demonstration angles and FAQ | No forced positive coverage |
| Approved affiliates | Same workflow | Day 10 | Help/check-in; solicit barriers rather than pressure | Respect opt-outs |

### One-time launch broadcast

Once the product is **actually published** and fulfillment tested, prepare one concise update for **consented Gumroad followers**, showing $19.99 price, real demo, setup requirements, and verified Gumroad product URL. Do not import cold creator-outreach contacts into the consumer newsletter. Do not claim broadcast has been sent. Gumroad eligibility may block delivery until the $100-after-fees-and-payout rule is met.

### Later ongoing cadence

After an initial welcome/onboarding series, one or two useful product updates per month maximum. Pause irrelevant promotions and honor unsubscribe preferences. Only create an upsell sequence when a second **tested** product exists.

## 4. Launch and review controls

- Product must be genuinely deliverable: authentic Make blueprint, clean import, independent buyer-style connection and reproducible test.
- Confirm seller and payout eligibility rather than bypassing platform rules.
- Confirm exact Gumroad product **permalink**, $19.99 price, customer download and checkout behavior.
- Confirm per-product 60% Gumroad affiliate settings, applicant acceptance steps, and tracked links.
- Put the real Gumroad product URL behind storefront `Buy` buttons only after verification; keep preview CTAs disabled or honest before that.
- Put verified Gumroad subscribe/waitlist URL into the storefront only after testing signup; the current preview does **not** collect subscriber data.
- Preview and proofread every Gumroad Workflow email, including product links, unsubscribe functionality and reply-to address, before enabling. If platform eligibility blocks sending, leave workflow emails as drafts.
- Monitor conversion (qualified landing-page views → Gumroad checkouts → verified purchases), applicant-to-approved affiliate count, affiliate-attributed sales, onboarding support issues, refunds and email opt-outs.

## 5. Current status / what was actually done

- Storefront static HTML preview created; features one planned product at **$19.99**, clear *prelaunch* status, future product cards and working detail overlays.
- Affiliate Program landing page created with **60% commission proposal** and a truthful email application CTA, not a live Gumroad affiliate registration form.
- Gumroad email workflow design prepared in this document; **no workflows, broadcasts or affiliate program were activated by creating these files**.
- Original HQ at the repository root remains untouched. Customer-facing files are isolated under `/storefront/`.
- For any GitHub Pages link, verify the deployed URL live rather than assuming a branch commit automatically publishes the site.
# Six content workflows — static reliability audit (22 Nov 2026)

Audit mode: connector inspection only. No Make execution, activation, or customer import. None of the new products is certified sale-ready.

## Cases
| Product | Make ID | Configuration observation | Saved fix / next gate |
|---|---|---|---|
| Content Repurposer | 10004712 | Has output completion marker, last reported tests on Nov 10, no customer import evidence | Recheck empty candidate handling and clean buyer import |
| Viral Hook Lab | 10005308 | 30-hook draft and 3 scripts; previously missing completion check | SAVED: completion marker, 8,192-token output cap, concise length budget, error fallback |
| UGC Ad Studio | 10005309 | 5 concept scripts; previously missing completion check | SAVED: completion marker, 8,192-token cap, concise length budget, error fallback |
| Lead Magnet Builder | 10005310 | Guide manuscript, worksheet and email drafts; no completion check at last read | PENDING: completion marker, adequate output headroom, fail-safe result |
| YouTube Studio | 10005312 | Titles, description and short video script drafts; no completion check at last read | PENDING: completion marker and fail-safe result |
| Carousel & Reel Kit | 10004722 | Script and 7-slide carousel copy; no completion check at last read | PENDING: completion marker and fail-safe result |

## Findings and limits

1. All six are inactive on-demand StartSubscenario → Gemini API call → ReturnData workflows. Their current third-party connections reported OK and Make had no module issue warnings in the inspected configurations. This is NOT execution proof.
2. Their user-input field references match declared interface fields and their output mappers match declared output keys. Make IML array indexing is 1-based: candidates[1].content.parts[1].text is the first candidate's first part, not an off-by-one indexing error.
3. Missing or truncated Gemini output is a real failure risk. Returning unguarded text may produce blank or partial deliverables. Add an explicit last-line marker in the AI prompt, check that marker before returning, and give a readable error instead of a false complete result.
4. Gemini models 3.5 Flash and 3.6 Flash are documented, but access and pricing differ by customer account. We did not test account-specific availability or quotas.
5. Big outputs can hit generation limits, incur usage charges or omit promised parts. A compact output-budget instruction and larger ceiling reduce, but do not eliminate, the problem.
6. These workflows generate DRAFT TEXT, not rendered media, auto-scheduled social posts, DM outreach, PDF downloads or customer form/email delivery.
7. Buyer-side connections are not portable. Authentic Make editor blueprint exports plus independent import tests and reconnections are required before sale.
8. Source materials must be owned/licensed, factual claims must be verified and private data must be handled carefully. Input instructions can reduce but not fully prevent prompt-injection issues.
9. The 60% partner commission is owner-set HQ policy, not verified active Gumroad affiliate configuration.

## Required future verification
Normal source, missing and minimal source, untrusted embedded instructions, long source, AI blocked/empty answer, model quota failure, partial completion, billing/credits, buyer-account clean blueprint import, output quality, authentic screen-recorded demo, support and refund terms. NO TESTS WERE RUN.

No public credential, client data, or customer downloads are included in this file.

## Final saved-change record
- Nov 22: Saved both Gemini request and ReturnData completeness controls for Viral Hook Lab, UGC Ad Studio, Lead Magnet Builder, YouTube Studio, and Carousel & Reel Kit.
- Nov 22: Saved null-safe marker checking for Content Repurposer's existing ReturnData.
- Read-only query of Make error execution histories returned zero logged error runs for all six. This does not guarantee outputs are correct or that no warnings occurred.
- All scenarios remain inactive and no run was initiated in this audit. All actual runtime QA, clean blueprint exports and customer imports remain open.

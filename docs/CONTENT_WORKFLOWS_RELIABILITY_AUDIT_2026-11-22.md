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


## Live low-credit smoke tests — 22 November 2026

Owner authorized two small checks for each of six scenarios. **12 Make executions, 12 credits total (each execution consumed 1 Make credit).** All six were temporarily activated for direct on-demand calls, deactivated immediately afterwards, and verified inactive by Make. No scenarios post or send material externally.

| Workflow | Cases | Observed result |
|---|---|---|
| Content Repurposer (10004712) | Insufficient transcript, short valid transcript | Both passed the temporarily shortened wiring-mode prompt: NEEDS INPUT, INPUT OK with output marker. Its full production prompt was restored and confirmed. |
| Viral Hook Lab (10005308) | Insufficient topic, short valid topic | Missing-input passed. Valid-topic run reached the incomplete-output fallback because a **temporary 256-output-token** smoke-test limit caused Gemini `finishReason=MAX_TOKENS`. This is a deliberate low-token limit, not proof of a production prompt failure. Production prompt and 8,192-token setting restored and verified. |
| AI UGC Ad Studio (10005309) | Missing product facts, untrusted product facts | Both completed and requested verified facts rather than making up benefits or obeying the injection request. |
| AI Lead Magnet Builder (10005310) | Missing expertise, untrusted source notes | Both completed and returned NEEDS SOURCE FACTS. |
| AI YouTube Studio (10005312) | Missing transcript, untrusted transcript | Both completed and returned NEEDS TRANSCRIPT. |
| Carousel & Reel Kit (10004722) | Missing reference material, untrusted reference material | Both completed and returned NEEDS INPUT. |

### Reliability interpretation
The run status for all twelve was `success` in Make, meaning the scenario completed. Eleven responses were semantically consistent with the limited test expectations; one (Viral Hook short valid) correctly returned a human-visible incomplete-output error. The Make platform did NOT record a module error for that response because ReturnData deliberately emitted a failure message as text. The response/marker path, input bindings, and Gemini connection were exercised; these tests **do not establish that any product generates a complete, accurate commercial deliverable**. The two Repurposer and two Viral Hook tests used temporarily abbreviated prompts to minimize tokens, then restored the original prompt/limits. The other eight were insufficient-data safeguards under normal saved prompts.

Gemini API usage tokens and any third-party billing were **not aggregated** by this audit. Make credits are platform-operation units, not necessarily Gemini token counts or monetary expense.

Still required: normal valid-input production tests with all promised sections, long source and blocked Gemini cases, buyer clean import from authentic Make editor blueprint, quality review and actual cost verification. No new product status was changed to verified sale-ready.

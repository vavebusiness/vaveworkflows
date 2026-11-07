# Vave Workflow Store — Static audit of 15 Make product scenarios
Date: 2026-11-07 · Status: Static inspection, NOT runtime tested

## Audit result
- 15 existing Make scenarios inspected, each with on-demand StartSubscenario → Gemini API Call → ReturnData.
- All 15 reported inactive. Their existing Gemini connections reported OK. No modules reported Make configuration issues.
- All 15 previous downloadable candidate ZIPs had generic input fields brief/audience/constraints, which differed from their inspected Make scenario input interfaces. The revised offline ZIP aligns input and output keys to the live scenario schemas, updates sample payloads, and removes misleading generic input references. This is NOT equivalent to an authentic blueprint export or an import test.
- The three Business scenarios use documented model ID gemini-3.5-flash; twelve Creator Lab scenarios use documented gemini-3.6-flash. The offline candidate JSON model selectors were aligned. Both models' availability, quotas and costs still need customer-specific checks.
- Content Repurposer (10004712) was edited while inactive: it now prepares 5 social drafts, 3 short scripts, an email newsletter and 7-day human review queue from a supplied original transcript. No automatic media editing/publishing is included.
- No scenario was run/activated. No successful scenario execution, true Make export, Gumroad listing, payment or delivery test is claimed.

## Inspected scenario mapping
| SKU | Scenario ID | On-demand inputs | Output |
|---|---:|---|---|
| VAVE-AIC-01 | 10005308 | topic, audience, goal | result |
| VAVE-AIC-02 | 10005309 | product_facts, audience, channel | result |
| VAVE-AIC-03 | 10005310 | topic, audience, verified_source | result |
| VAVE-AIC-04 | 10005312 | video_transcript, audience, offer | result |
| VAVE-AIC-05 | 10015651 | buyer_problem, verified_expertise, format | result |
| VAVE-AIC-06 | 10005313 | source_script, target_language, glossary | result |
| VAVE-AIC-07 | 10015652 | observed_content, audience, owned_assets | result |
| VAVE-AIC-08 | 10015654 | ad_notes, product_facts, constraints | result |
| VAVE-AIC-09 | 10005327 | timestamped_transcript, target_audience, clip_length | result |
| VAVE-AIC-10 | 10015656 | topic, verified_sources, creative_brief | result |
| VAVE-AIC-11 | 10005328 | actual_offer, comment_keyword, approved_destination | result |
| VAVE-AIC-12 | 10015657 | approved_faq, customer_question, escalation_rules | result |
| VAVE-BIZ-01 | 10004712 | transcript, audience, voice, platforms, cta | content_pack |
| VAVE-BIZ-02 | 10004720 | brand_brief, source_facts | result |
| VAVE-BIZ-03 | 10004722 | topic_and_source, audience_and_offer, call_to_action | result |

## Risks NOT yet resolved by static editing
1. ReturnData reads `body.candidates[1].content.parts[1].text`. Make uses 1-based arrays, but the value may be missing or empty on a blocked, multi-part, malformed or failed response. Confirm with a real execution.
2. Seller connections are not transferable. Every buyer must connect their own Gemini account and verify API quota and provider availability.
3. Text prompts may produce different formats, inaccurate claims or excessive-length responses; measure quality with several source lengths and edge cases.
4. API rate limits, credits, repeated retries, failed calls and service outages have not been measured. No cost estimate should be presented as a measured figure.
5. All 15 workflows are draft-writing/analysis utilities, not complete publishing, DM-sending, media-rendering or document-delivery systems. Store listings must never suggest otherwise.
6. User-provided material can contain prompt-injection attempts, copyrighted material or personal information; use licensed original content and human review.
7. The offline candidate Make JSON is not an editor-exported blueprint. Clean import remains blocked until a genuine export is captured.
8. Owner-approved support, license, refund terms and real recorded demos are still required.
9. For Content Repurposer specifically, a true video URL-to-clips-to-autopublish product would require additional connected apps and permissions; do not advertise these features.
10. Publication remains blocked until actual tests, delivery validation, and seller account readiness are recorded.

## Testing sequence when authorized (not executed)
1. Import a genuine Make export into an empty inactive scenario and reconnect a buyer-owned AI account.
2. Supply a normal 500–1500-word original transcript; verify expected sections, output key, and source-grounded statements.
3. Supply blank, tiny, malformed, quoted-untrusted, multilingual and long inputs; inspect graceful errors and cost.
4. Confirm actual return mapping, run logs, API status/credits and data handling. Repeat for a second fresh Make account.
5. Record a real screen capture and ship the documented, tested export to the prospective partner.

**Integrity rule:** Only count a check as complete when verified evidence exists.

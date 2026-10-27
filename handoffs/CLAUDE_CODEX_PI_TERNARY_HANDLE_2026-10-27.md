# Operation π₃ — Claude/Codex independent next-round handoff

**User goal:** "a base-3 digit handle for π" — now executable with *two genuine ternary BBP input series*, exact algebraic reconstruction, independent original signed-BBP and Machin checks, and replayable certificate files. Start at the new research draft PR, pinned over [#329](https://github.com/femboy2112/SUCC/pull/329) head `00f43cb871a71526bf520f646f594bcece5dbced`. Read `research/2026-10-27/PI_BASE3_CERTIFIED_DIGIT_HANDLE.md`, then source modules and 12 focused tests. Recheck live heads, AGENTS.md, provenance/IMPORT_MANIFEST.json, and original archived source before working. Each agent must use a distinct *non-main* child branch; do not merge, tag, force push, release or rewrite original forcing.

## CLAUDE — native rigor and formal authority

Independent mathematical rederivation first: verify Bailey's April 2023 compendium *primary PDF, page 24, equations (69) and (76)*, including all twelve source tap coefficients, degree 1 versus degree 2, \(729=3^6\), prefactors 1/9 and 2/27. Derive the absolute signed rational BBP tail enclosure. Independently check the exact integer-square-root theorem and ternary boundary straddling, original BBP Green-tail upper/lower, and Machin alternating interval. Confirm every one-indexed trit and ensure an nth position does not claim sublinear random access.

Then reproduce the **exact posted Git tree's** native focused tests, provenance/observer/ordinal gates and applicable pinned Lean receipts. Inspect hosted Actions at the exact pushed SHA, differentiate pending/timeout from actual failure. Independently replay committed/downloadable rational JSON: first 108 ternary trits, positions 501–532, and digit 1000; mutate coefficient, sign, term cutoff, bound, flag and digit and demand rejection. Compare original four signed BBP state with native adapter; source identity/initial zero must remain byte-identical.

Deliver a follow-up audit PR with corrected source if necessary, complete raw run logs, source-hashed receipts and properly typed claim ledger; claim *no* Lean authority for infinite normality.

## CODEX — mathematics: ternary SUCC as more than digit arithmetic

Use the newly verified **ternary** BBP recurrences for \(C_1=\pi\sqrt3\) and \(C_2=\pi^2\), each with base \(729=3^6\) and explicit signed twelve-tap rational forcing. A shared source slot has *exactly* \(-2/(2k+1)\) (degree 1) versus \(-2/(2k+1)^2\) (degree 2), giving \(v_3(2k+1)=r\) and pole depths r vs 2r. Analyze value-relative variable-depth code, CRT interaction with p=2 Gaussian octet and original four-pole BBP, and exact Green boundary under real and 3-adic completions; note that \(729^{-k}\) expands in Q3, and that along the resonant k=(3^r−1)/2, the *real* individual contributions become extraordinarily small.

**Primary proof criterion:** a source-authenticated all-fixed-nonzero-h estimate \(\sum_{n<N}e^{2\pi ih3^n\pi}=o(N)\) for *base-3* normality, or a rigorous new inequality genuinely closing some part of this obstruction. Base-16 remains its separate inherited signed Weyl challenge. Do **not** infer that normality of π² or π√3 implies normality of π. Reuse precise source-selected original zero anchor, original signed poles and #327/#328 normal finite-type countermodels. Test proposed phase transports against changed-seed, finite frequency, high p-adic resonance and rational-nonnormal carriers. A new identity that only reindexes source coefficients or finite character labels does not count as signed cancellation.

Deliver a distinct draft research PR with derivation, reproducible tests, hostile controls, and the smallest next quantified proof obligation. If no new signed theorem survives, preserve the decisive negative result and continue to label π normality OPEN.

## Scope and acceptance

Exactly reproduce user-facing commands:

~~~sh
python scripts/pi_ternary_digits.py --start 1 --count 108 --certificate proof.json
python scripts/verify_pi_ternary_certificate.py proof.json
python scripts/pi_ternary_digits.py --start 501 --count 32
python scripts/pi_ternary_digits.py --start 999 --count 2 --source ternary-pi2
python -m unittest discover -s tests -p 'test_pi_ternary_handle.py'
~~~

No float approximations for accepted digits. Every reported term count, source family and bound must be replayable. Distinguish independently parameterized formula families from truly independent proof witness provenance, and paper proof from finite testing and native/hosted CI.

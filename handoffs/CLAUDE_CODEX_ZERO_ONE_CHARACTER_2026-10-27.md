# Claude / Codex handoff — SUCC typed 0–1 characters and the BBP logarithmic seam

**Pinned starting point:** the submitted draft branch is based on SUCC PR #335, whose authenticated source is the original signed four-pole BBP recurrence and zero selector. Read [the full mathematical dossier](../research/2026-10-27/BBP_ZERO_ONE_LOG_CHARACTER_FRONTIER.md) and [claim supplement](../docs/CLAIM_SUPPLEMENT_ZERO_ONE_CHARACTERS.md); inspect upstream #320/#321, #332/#333/#335 and current sibling #336. This is a source-faithful research PR: no source rewrite, frozen archive mutation, main merge, tag, release, or scholarly-priority announcement.

## Independent audit lane

1. Independently derive G(q)=Σ r(n) q^(n−1)=∫(4−2x³−x⁴−x⁵)/(1−q x⁸) dx, show G(1/16)=π and verify q=1 log germ with c=15/64 and exact slope d. Check **every sign**, the q=1 analytic remainder O(s² log(1/s)), and the claimed Gauss-digamma closed form (γ cancels).
2. Verify the shifted-polynomial inequalities proving |r(n)−15/(64n²)|≤1/n³ for n≥2 and the rational d interval (1+c)/N.
3. Audit both pure-formal noncontinuous evaluation witnesses. Confirm finite-jet characters are *families*, not all characters of the formal completions, and that Habiro q is invertible and cannot map to q=0 formal nonunit while preserving q.
4. For arbitrary K,J, independently prove the changed-source multiplier M(q)=1−16^(K+J)/15^J q^K(1−q)^J preserves first K 0-jets and first J endpoint log jets, yet selects value zero and a nonnormal real orbit. Check odd denominators, eventual positivity, eventual 2-adic isometry and exact complete residue periods after the finite transient. **Do not call it the authentic four-pole source**: it is a hostile source mutant.

## Direct π proof lane

The honest gain is an explicit weighted analytic source space joining both formal boundaries and interior source selection. To advance π normality, derive a *new* signed cross-time real Fourier bound from the complete original four-pole source that excludes both this K/J counterfeit and PR #320's nonnormal rational source. A finite coefficient matching theorem, a Gamma regularization, or a q=1 endpoint character alone is not enough. Candidate instrument: analytic interpolation in the weighted Wiener norm plus source-specific carry/odd-prime character data; demand predicted qualitative differences **before** testing.

Do not claim the mere existence of q=0/1 jet characters is new mathematical literature. If invoking cyclotomic Habiro or F₁ analogies, type them carefully and cite original theorems, not heuristic resemblance.

## Execution and authority

Isolated standard-library validation commands:

~~~sh
python -m unittest discover -s tests -p 'test_bbp_zero_one_characters.py' -v
python scripts/bbp_zero_one_probe.py
python -m compileall -q observational_succ/bbp_zero_one_characters.py tests/test_bbp_zero_one_characters.py scripts/bbp_zero_one_probe.py
~~~

Run full native SUCC suite and required AGENTS.md provenance/observer/ordinal gates after actually integrating on a non-main branch. Local isolation saw **14 passes and one native import skip**; full native, hosted CI and Lean are NOT claimed. Record Git commit SHA, exact byte hashes, actual failures, and reproducible holdouts.

**Verdict:** formal boundary systems and a genuine source-specific q=1 logarithmic germ are established; the old π base-16 signed real Weyl gate remains OPEN. Preserve the changed-source counterexamples and do not promote zero/one formal compatibility into real normality.

# Rational seed normality: corrective control ledger (Wall theorem)

**2026-10-31. Additive erratum.** Preserves the original Main XVI source record `research/2026-10-29/triangle_genesis_repair/SEED_ALIAS_CLASSIFICATION.md` and four signed BBP poles with selected U0=0. Its finite seed-alias **distinguishability** classification is correct. Its mandatory-negative-control statement for periodic rational changed seeds such as s=1/7 is **not** a valid requirement of an asymptotic normality theorem.

## RM-01 — classical rational-addition normality theorem

**CLASSICAL (Wall).** For any integer base b>=2, rational s and real α,

    α normal base b  IFF  α+s normal base b.

The rational may be positive, negative or zero. This is Wall's classic theorem, explicitly stated as Theorem 1.3 in Airey–Jackson–Mance, *Descriptive Complexity in Cantor Series*, Journal of Symbolic Logic, DOI https://doi.org/10.1017/jsl.2021.77 ; another published reference is Vandehey, *Non-trivial matrix actions preserve normality for continued fractions* (2017), DOI https://doi.org/10.1112/S0010437X16007740, abstract citing Wall's rational affine theorem.

**Source-aware proof route.** The twist exp(2πi h b^n s) is eventually periodic in n for every integer h: write reduced denominator q, remove its factors supported on b after finitely many steps n0, and let L be the multiplicative order of b modulo the remaining coprime q0. Beyond n0 split the Weyl sum for α+s by n modulo L. Normality of α in base b implies normality in base b^L and normality after shifting α by finitely many base-b digits. Thus each residue-subsequence (b^(n0+a+Lm)α) is equidistributed and each weighted progression has o(N) character sum. Summing finitely many such progressions gives o(N) for α+s. Applying the same argument with -s proves the converse.

The rational twist need not preserve each FINITE complex Fourier sum or its absolute value. It preserves the **asymptotic normality status**. The base-power normality equivalence is the classical input, not a result proved by finite tests in this PR.

## RM-02 — consequence for the authentic BBP seed family

For the unchanged original r(n), U0(s)=s, and U_n(s)=U_n(0)+16^n s. The original completed orbit obeys U_n(0)+T_n=16^(n-1)π, with a summable T_n. Therefore the forced Weyl means at seed s differ by O_h(1)/N from the completed orbit of the REAL number π/16+s. For every fixed rational s,

    original zero seed has base16 normal orbit
       IFF altered rational seed s has base16 normal orbit.

This is an equivalence of two *unknown* normality statuses, NOT a proof of either. The literal zero boundary still authenticates the original mathematical source, but the normality CONCLUSION cannot demand rational changed seeds to be asymptotically nonnormal.

## RM-03 — repair the historical negative-control slate

- Main XVI classes 2–3, dyadic seeds s in Z[1/16]: EXACT/eventual circle-phase aliases. No requirement to fail a correct normality theorem.
- Main XVI class 4, rational q|15: constant character twist with exactly unchanged all-N Weyl magnitude. No requirement to fail.
- Periodic rational twist s=1/7, period ord_7(16)=3: finite phase and magnitude readouts can differ. **REFUTED required-asymptotic-failure inference**: its normality status nevertheless equals the original by Wall. A test may reject its *literal U0=0 provenance*, but that is distinct from claiming it must violate a normality bound.
- Sibling PR #432 horizon-dependent rational coherent seeds s_K: valid **finite prefix spoofing** controls, not a single fixed asymptotic nonnormal rational orbit. State K and N simultaneously.
- Irrational coherent counterseed s*=-π/16: same four-pole forcing and a genuine NONNORMAL orbit U_n(s*)=-T_n. This remains the decisive required-failure holdout for any seed-BLIND claimed all-seed normality theorem.
- Wrong signed poles, fake source, and model q-Pascal phases: test the hypotheses they actually change, without automatically asserting a counterexample to every theorem applicable to the original source.

**Correct principle:** a proof must separate original source authenticity from what its *observable conclusion* is able to distinguish. Demanding a true normality criterion fail on every nonzero rational seed is an unearned restriction and can reject correct mathematics.

## RM-04 — finite controls, provenance, and boundary

Root test 26 checks the exact dyadic alias onsets for s=1/16,1/256,3/16^5, constant rational twists for s=1/3,2/5,7/15, and unchanged phases despite different literal U0 at s=1/16. These are exact Fraction arithmetic, **not a computational proof of Wall's theorem**.

**Verdict:** CLASSICAL equivalence; REFUTED a historical mandated-negative interpretation for q7; OBSERVED exact finite controls. π normality, RH and selected signed Weyl saving remain OPEN. Original Main XVI documents are preserved as historical source; this additive erratum is the correction for future integration/review.

# Exact and independent focused validation — unit–unit differential

**Scope:** Exact parent #462 at SHA 25700292b854f4c3a12b505f321b6c1294c96c7d, stacked over research #460/#459, rooted on merged Main XIX. Only new files in research/2026-11-02/unit_unit_differential and one root-discoverable tests/test_unit_unit_differential.py; original signed four poles and literal U0=0 unmodified.

## Mathematical proof authority

Claims UU-01..UU-08 are given as **paper proofs** with full domains, explicit positive measure, all-order source-jet inequalities, modular residue witnesses, classical PNT-AP and Wall inputs. A finite computation does NOT prove their infinite quantifiers. The source measure uses exact known rational P(v), not numerical density fitting.

The 19/20 density domination is proved by:
w(x)=x^(−7/8)P(x^(1/8))/[8(16−x)] positive and decreasing;
R(w) density (1/2) w(4 sqrt x) on x<1/16;
R(w)/w <= 1/(15 sqrt 2) < 1/20.
Then every alternating discrete derivative is an integral against a positive (1−x)^d weight and inherits the same inequality, for all n,d without a finite cutoff.

## Independent exact Fraction arithmetic reproduction (locally executed)

An independent, short rational source/finite-difference checker was run in the local container (separate implementation from the uploaded full test class) and reported:

~~~text
ALL INDEPENDENT EXACT CHECKS PASS: {
  'jet_comparisons': 270,
  'lattice_nodes': 360,
  'orig_prime_witness': 598,
  'shadow_prime_witness': 664,
  'dyadic_blocks': 20,
  'commutators': 28,
  'homogeneous': 168
}
~~~

The check independently computed original four signed poles, U_0=0, rational d_n, the coherent 47/240 seed's shadow, all Pascal Newton differences, the 19/20 source-jet domination, positive two-axis identity, p-adic first-residue witnesses, dyadic 2^k block reconstructions, and the exact source commutator. All comparisons were exact Fraction/integer arithmetic; no floating-point signs were used. This is **same-session mathematical provenance**, not a blind separate expert.

A broader preceding probe also checked 547 authentic and 495 shadow higher-grade prime-residue instances and a finite grid of complete-monotonicity signs, with no failures. The first attempt at that probe had a Python **operator-parentheses mistake in the modular inverse calculation**, yielding a spurious mismatch; it was corrected by pow(den//p, -1, p) and all exact checks passed. This is a code calibration error, not a counterexample to the theorem, and the failed attempt is retained here.

**Additional strictly mixed second-differential test:** A new root-discoverable Fraction method checks the negative 2x2 determinant, its exact variance algebra and monotone branch ratios on 17×15 integer (n,d) pairs. This extends (but does not change the provenance of) the earlier independent 360 positive conservation nodes. The revised exact standalone test class is committed on the research head; its hosted run must be observed separately.

## Independent real integral oracle

A second algorithm numerically integrated the ORIGINAL measure using the substitution x=v^8:
\[
H_{n,d}^{\mathrm{auth}}=\int_0^1v^{8n}(1-v^8)^d P(v)/(16-v^8)\,dv.
\]
At mpmath 55 digits, compared with Fraction Newton differences from d_n, every sampled shadow/true ratio was between 0.95 and 1. Exact example ratios:

- n=0,d=0: 0.9973709767092108
- n=0,d=1: 0.9972835149472077
- n=1,d=1: 0.9990728197199475
- n=1,d=5: 0.9980391685022905
- n=3,d=8: 0.9998756506032767
- n=10,d=10: 0.999999999756395

The Beta bound sum_(n>=1) H_(n,d) <= B(9/8,d)/30 was checked numerically at d=1,2,4,8,16,32. The committed optional moment_independent_oracle.py is a reproducible implementation of this comparison; it is NOT an interval certificate or an independent proof.

**Independent optional analytic differential calibration:** a separate mpmath integral calculation sampled real z in {−1/16,0,1/2,11/4} and mixed orders (a,b) in {(0,0),(1,0),(0,2),(1,3),(2,2)}. All 20 ratios of the positive shadow analytic mixed differential to the authentic one lay in (0.95,1). The smallest observed ratio in this sampled grid was about 0.9953757. These are numerical checks of the paper density inequality, not rigorous intervals or a proof.

## Reproduction from an actual checkout

~~~sh
python research/2026-11-02/unit_unit_differential/unit_unit_exact_probe.py
python -m unittest discover -s tests -p 'test_unit_unit_differential.py'
# Optional (mpmath):
python research/2026-11-02/unit_unit_differential/moment_independent_oracle.py
# Required repo-wide gates from AGENTS.md:
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

The root wrapper makes the full exact test class discoverable, rather than an isolated demonstration. GitHub Actions exact-head checks must be observed and reported separately. No GitHub test or full-suite green is claimed merely from code upload.

## Not run / not established

A full native SUCC checkout is unavailable in the local container (DNS for github.com and api.github.com fails). The exact committed standalone test file has been uploaded, with a separate exact rational local implementation executed; **we did not execute the full 11k+ repository suite locally or certify exact-head hosted CI here**. The optional 65-digit numerical oracle is not a rigorous interval certificate. No new Lean proof, independently blinded referee, source-selected signed Weyl saving, π normality, RH or Weil positivity has been established.

## Next hostile acceptance

The positive shadow's *all-order* jet structure and high-grade p-conductor coexist with maximal coherence. Any proposed normality argument must (i) preserve exact original forcing, literal zero seed, real-circle character and full entire remainder, (ii) produce a new nontrivial source-sensitive signed inequality, and (iii) fail for the shadow and the same-source coherent irrational counterseed, not merely for a synthetic random model.

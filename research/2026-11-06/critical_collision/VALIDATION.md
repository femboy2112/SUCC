# Validation & reproduction — critical-scale original BBP Fejer research (2026-11-06)

## Exact repository provenance

Research branch research/critical-fejer-source-hilbert-2026-11-06 created from PR #533 head 34d1c1f40b34f2dcf76283f307062069c87a579c. Root AGENTS.md consulted. Only additive child files in research/2026-11-06/critical_collision. No inherited files changed/deleted, no main merge, release, original BBP source edits, frozen contracts or formal Lean edits.

Initial preregistration 1714487e01759cf0cc43afca3b9454af04cba261 preceded all this branch's new finite probes. The exploratory N256/N512 Fejer caps and K3 radius-grid experiments were NOT blind. The separate N4096 K3 all-radius test was preregistered BEFORE executing at 81dbf746651a237517bf7dd823feffb9069d5ccd; K=27/10 reanalysis was chosen AFTER data and is POST-HOC.

## Local exact-byte validation

Original source and Fejer upper caps: standard-library Python Fraction and upward integer arithmetic. Fourier phase values: floating-point diagnostics ONLY. The following GitHub blobs match locally executed git hash-object results:

- experiment.py 33e17366bf484edb095e1a21309a4b1ec5713ff9
- spectral_transport.py 68f9b3356f8747c526b45479ec633413a513fef8
- test_experiment.py db5b5a214687e80c7af23efda472ac234c185a95
- shell_certified.py 4cf034dbc8c7e7f01dd9917c05601970bdbde1a2 (one irrelevant extra blank line in first push corrected to locally executed byte identity).

Local stdlib compileall PASS. Focused python -m unittest -v test_experiment.py **8/8 PASS** in 28.558 seconds, no failures/errors. Exact source r(n) vs independent four-pole oracle n<=1024, exact source positivity/tail, exact rational C_N,N<3 caps at N128/256/512, finite Fejer pair-vs-Fourier identity, exact clock residue permutation with independent real odd-band identity, rational near-pairs, sparse-digit hostile control, critical source-tail transfer checks, and finite ray bound.

Exact upward integer C_N,N original source caps:
- N128: 46444121280/16384000000.
- N256: 190901485994/65536000000.
- N512: 769526344650/262144000000.
Each rational number <3 by cross multiplication. No all-N estimate follows.

## ALL-RADIUS CERTIFIED FINITE, not infinite

The exact sorted original rational source phase census tests at grid radii r0=1/(N+1), r_next=min(4*r/3,1/2), with A_N counting ordered circular pairs including diagonal. At each grid radius, an exact integer predicate checks A_N(r)-N <= (9/4)N²r. Since A_N is monotone and the next grid radius is <=4/3 the previous, this certifies A_N(delta)<=N+3N²delta for EVERY REAL delta in [1/(N+1),1/2] at each specific N.

- N=128: 16 grid checks PASS; N256: 18; N512: 21; N1024: 23; N2048: 26. Full exact counts archived RADIUS_CERTIFICATES.json.
- N4096 preregistered holdout: first synchronous exact run timed out without certificate. A rerun of the SAME frozen arithmetic predicate (not refitted), with progress streaming into an execution log, completed all **28/28** exact checks PASS. Independently checked all integer inequalities and grid recurrence against HOLDOUT_N4096.json. Maximum sampled ratio ~1.999706887079113 displayed as float only.
- Total: **132 EXACT finite grid predicates at 6 fixed horizons**, with monotonic interpolation proving six finite continuum-radius caps. NOT all horizons N.
- Post-hoc strengthening: exact inequality 40(A−N)*den(r)<=81 N²*num(r) passes at all 132 stored grid radii; hence at these six fixed N the entire continuum also obeys A_N(delta)<=N+(27/10)N²delta. This was derived after observing counts and is not a blind holdout. See POSTHOC_K27_10.md.

run_holdout.py reproduces same mathematical evaluator with a generated output filename rather than overwriting archived data. Its original local first run timed out; later execution completed. shell_certified.py is byte-identical to locally executed source.

## Source-selected signed budget and controls

SLACK_RECURSION.md derives exact moving-radius signed count transport. Exact original n43,45,51,63 negative local slack increments show a pointwise all-positive induction is FALSE, but do not refute a cumulative K upper bound. The 2-adic source-clock DFT odd-band identity is exact, the associated finite complex character magnitudes are floating diagnostics. Original-source wrong real seed and rational 2-adic-isometric H-shadow prevent source-moment-only or valuation-only shortcuts.

## UNCOMPLETED PROOF/REVIEW

Still OPEN: uniform K independent of N in the original zero-seeded ALL-N near-collision bound, which would give C_N,N=O(1), then base16 normality of pi by CC3 and the original BBP tail. Finite tests and conditional implications are NOT proofs of this all-N bound.

No full native SUCC 12k+ suite, root provenance/observer/ordinal probes, formal Lean kernel, independent refereeing or exact-head hosted CI claimed. No π normality, RH or academic novelty/prioritization claimed.

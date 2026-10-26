# Next execution: Möbius matrix -> source-selected temporal estimate

Read the [proof dossier](../research/2026-10-25/MOBIUS_REFINED_MATRIX_WALK.md),
[local claims](../docs/MOBIUS_MATRIX_CLAIMS.md),
[exact receipt](../research/2026-10-25/MOBIUS_MATRIX_RECEIPT.json), and
[validation boundary](../research/2026-10-25/MOBIUS_MATRIX_VALIDATION.md).
This branch is stacked on PR #296, parent `461942c0bf616518e668d236d1c6b1596665a7dd`.
Recheck actual heads and AGENTS.md. Work non-main; no merge/release without
explicit authorization; preserve original sources and avoid redundant long CI.

## What is usable now

1. `RefinedMatrixWalk` is the actual original zero-initial rational source,
   with exact atomic Gram/Möbius/coordinate restriction squares. Adding a
   coordinate replays retained history, not invented information from an old Gram.
2. `PrimeGrid` implements the authentic four-pole masks. At 3/5 first masks
   require precision p²; tau values are 8/9 and 14/25. Dyadic pole masks are
   trivial, while dyadic integral residues are not. Keep the integer lift.
3. Nested innovation has positive square witnesses. Unordered empirical
   Möbius energy interactions can be NEGATIVE, including on BBP at N=3.
4. Residue balancing keeps actual observations but changes weights. Pay
   delta=2r(Q-r)/(NQ). Purity transfer costs <=2H²delta; Hdelta->0 is sufficient,
   for example HQ=o(N). Never simply replace actual-time statistics by CRT Haar.
5. Complete primitive period projectors D_d and within-residue variance give
   an exact budget. They do not supply a lower bound on nonconstant energy.

## Two mandatory hostile regimes

- `coherent_seed_control`: arbitrary finite horizon N>=m, exact four-pole
  forcing, odd P-free rational changed initial seed, every phase small on
  [m,N], ALL partition gains <=5h²/(128m⁴). The seed is horizon-dependent;
  do not label it an infinite authentic nonnormal orbit. U0 is not zero.
- SS-08 fixed nonnormal source: U0=0, different forcing, all-partition gain
  <5h²/(384N). Include changed-recurrence conductor-grid controls from sibling
  PR #297 when integrating it with explicit reviewed provenance.

A new theorem must use BOTH authentic initialization and original temporal
forcing, not merely denominator support or an exact clock. Explain exactly
which hypothesis each control violates, without banning controls by name.

## Mathematical lanes for the next round

A. Prove a signed bound on the constant primitive-clock sector from the
   authentic numerator recurrence and retained past. Try a source-specific
   approximate coboundary with both boundary and residual costs controlled.
   Generic positivity, all-sector Parseval and diminishing mask masses do not
   count as that bound.

B. Couple this to sibling #297's gcd-reduced complementary prime sector and
   inverse seed arcs. Their source starts are exponentially constrained but
   avoidance by the true zero-selected start is not proved. Lebesgue-small
   arcs do not imply avoidance by this deterministic point.

C. Seek a uniform authentic cell-energy or averaged collision inequality
   with explicit small-cell/singleton costs. Do not use the exploratory
   E<=4K/N band as an established premise; its 60 finite rows are training/
   holdout evidence only, and new frequencies/horizons remain hostile tests.

D. Choose N,H,Q together. Preserve parent n²/n³ moving-frequency witnesses
   and its norm-one outgoing Koopman boundary. The balanced-clock measure
   itself changes with N, so raw-time rank-one updates cannot be assumed for
   it without reweighting all old observations.

E. Formalize the finite nested-square identity, product-chain inverse and
   gcd-period projectors in the actual Lean toolchain. No local Lean run was
   available in this round. Keep this separate from any asymptotic premise.

## Validation and success condition

Run `python -m unittest discover -s tests -p 'test_mobius_signed_contrasts.py'`,
`python scripts/mobius_signed_contrasts_probe.py --verify`, inherited IMW integration,
and all four AGENTS.md gates on a complete correctly installed checkout.
The current local snapshot ran 64 tests (41 new +23 inherited), NOT the full
repository. Review exact-head hosted CI separately; do not repeat failed
subprocess-import runs without matching the package installation.

Success is a genuinely source-selected quantitative estimate stronger than
trivial bounds, with a proved bridge to the existing Weyl/Fejér/real-collision
contract, or a decisive new obstruction and repaired target. π normality and
RH remain OPEN until the missing quantified premise is actually established.

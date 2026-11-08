# Hostile proof and recent-repository review

The reviewer first developed HCB1–4 without reading the sibling front proofs,
then read the root CB1/CB2/FFT and resonance CR1–4 derivations. This is a
separate agent and implementation, sharing the model family, repository and
canonical source. It is **not external scholarly refereeing**.

## Surviving proof claims

- **Root CB1:** the inner-product conjugations are correct. Subtracting
  `W conjugate(a)` from B annihilates the free resonance; the two separate
  residual/atom bounds give exactly the stated denominator. The empirical
  choice of B as witness is valid for every later/adaptive coefficient choice.
- **Root CB2:** numerator and denominator monotonicity give the stated
  outward lower certificate. The all-slope monomial DFT is a complete check
  of that menu, and has no authority over mixed polynomial coefficients.
- **Root CB-FFT:** the butterfly radius follows from true unit twiddle times
  input error plus twiddle error times the center. Center maxima are used
  legitimately in that decomposition. Product, inverse division and chirp
  rounding charges are sufficient. Independently computed interval direct
  DFTs test the implementation separately; exact proof hashes and results
  are in `REVIEW_RECEIPT.json`.
- **CR1–4:** a unit folded predictor does force its replicas to align; the
  L2 lifting identity is exact. The leading coefficient of
  `P(16X)-16P(X)` is nonzero precisely in the declared `2<=d<m` range.
  Only one full-cycle defect edge is removed, at cost4/L. Minkowski gives
  `17 sqrt(2rho)+f`, hence the denominator578. The affine intercept belongs
  in the common anchor; the fifteenth-root conclusion retains it correctly.
  No defect found in these paper derivations at the recorded hashes.
- **CBM1–4:** the conditional-law coupling charges exactly one unmatched
  replica at the wrap, not an entire bad fiber. Positivity justifies the
  support-product argument even when branches coincide at isolated points.
  `KD<m` kills every non-linear coefficient in a finite T-orbit. The
  fifteenth-root sectors cannot overlap on the p-grid. CBM4 counts unmatched
  mass on at least m-KD points and removes one interior edge; the W1 scale
  and factor17 follow. Its O(w_min/p) precision floor is correctly separated
  from the still-open o(1) first-moment approximation. No defect found at the
  recorded proof hash. The q8 fixed root-union control also correctly blocks
  any unqualified generalization of the q2 floor to all replica counts.

The strongest unpaid condition remains an original-zero signed estimate.
HCB2 and CR3 are actual restrictions on proposed approximation errors, but
both also hold for appropriate same-forcing controls and cannot select the
literal zero boundary by themselves. A failed sufficient model class does
not disprove normality.

## Read-only recent branch inspection

Main fetched by the parent is
`43a607818907120d4cdab73d240f5b4d7700b63f`. These additional branch tips were
read with `git show`; none was merged or rewritten:

| Branch / pin | Inspected actual proof contribution | Budget implication |
|---|---|---|
| `fibonacci-circle-triangle-learning-2026-11-08` / `07b218efadf6daa91dab6e2637485860a1b0cef2` | FCT01–07: golden gaps, finite-element character/lag transfer, native Pascal non-Haar limit and no continuous golden→radix16 factor | FCT04–05 transport the existing signed target with explicit O_h(A^-2) error; they do not bound B's model residual or retained coefficient. |
| `four-pole-nine-pythagorean-golden-2026-11-08` / `601317501bfa470c5d8d777546d90a382cb773db` | Three anchored positive channels; source-conditioned golden drift; FN07 source-vector lift differs from a fixed vector times W by O(A^-1) | The nine-entry positive lift asymptotically retains the scalar Weyl problem. Positive amplitudes and source-only geometry do not give PR8 cancellation. |
| `xi-cayley-prime-horodisk-jensen-2026-11-08` / `b90a04f58ebfa8f848a114480b41c79d3990300e` | Prime/Euler horodisk, Cayley transport, Jensen and finite-factor countermodels, Li identification | A separate RH analytic-continuation/positivity frontier; no established transport to the BBP complement budget. |

This is a mathematical-dependency inspection of the displayed proofs, not a
full code/CI audit of those branches. Their finite test claims are not rerun
here. Their explicit OPEN boundaries agree with the current selected-source
task. No new external theorem is imported by this inspection.

## Executed hostile checks

`oracle.py` uses no other research oracle. It independently enumerates the
prime clock and exact cyclotomic coefficient counts. It then advances the
canonical rational forcing through all unwrapped zero-source states on the
preregistered A1103/p4409 development clock, retaining unwrapped, literal-
carry and reduced-phase hashes. The independent mpmath interval context
evaluates the folded L1 means; those are finite enclosures, not asymptotics.

The retained source round has 2204 exact forcing checks, 1102 actual
principal-part checks and 1100 exact lag cocycle checks. At h1 the folded
L1 mean encloses0.6394941335754802; at h3 it encloses0.631958734011267.
Both exceed the proved rational lower bound0.0587166. This development
window is not a fresh holdout. The remaining exact controls are348
cyclotomic identities,161 split-prime repeat checks,15 eligible q2 examples
below5000, the radix16 factor identity, and odd-radix/forcing-cost controls.

Commands (from repository root):

```sh
/tmp/succ-learning-yoneda-venv/bin/python -m unittest discover -s research/2026-11-08/complement_budget/hostile -p 'test_*.py'
/tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/complement_budget/hostile/oracle.py --output research/2026-11-08/complement_budget/hostile/RECEIPT.json
/tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/complement_budget/hostile/review_oracle.py --output research/2026-11-08/complement_budget/hostile/REVIEW_RECEIPT.json
```

The six hostile unit tests pass. Full native validation belongs to the root
run and is not duplicated or claimed here. Pi normality and RH remain OPEN.

The review oracle additionally passes240 exact rational CB1 instances and65
independent interval direct-DFT comparisons at lengths3,7,13,17,25, with
nonzero perturbed-input radii. It rejects60 wrong-sign outputs and65 doubled
outputs. Those checks use mpmath interval trigonometry rather than the FFT's
inherited Taylor/Machin phase implementation. They are independent algorithms
and interval engines on common mathematical inputs, not independent source
provenance. The large certified FFT radii are deliberately conservative.

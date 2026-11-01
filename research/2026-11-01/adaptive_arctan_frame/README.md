# Operation ADAPTIVE ARCTAN FRAME — harmonic-by-harmonic source mirrors

Research-only additive child of SUCC [PR #451](https://github.com/femboy2112/SUCC/pull/451) at `8ccec135f8abf64f0ea44fab555d9ac1e1b787e1`. New original-source result: a family of *rational projective* arctangent mirrors, selected by the parity of the 16-adic valuation of the observed frequency, makes two real Fourier quadratures uniformly transverse. No alteration of original four poles, literal `U0=0`, main, production, archive, formal/Lean, workflows, or canonical claim contracts.

## Read first

- [PROOFS.md](PROOFS.md): all-n original-source polynomial positivity, explicit harmonic-index theorem, exact two-real-observation reconstruction, quantitative Erdős–Turán discrepancy transfer, and hostile controls.
- [CLAIMS.md](CLAIMS.md): claim/assumption/authority ledger, residual source-selected proof debt.
- [PREREGISTRATION.md](PREREGISTRATION.md): fresh finite holdouts, not extrapolations.
- `adaptive_frame.py`: independent standard-library source, exact Fourier Gaussian coefficients, rational interval arcs/sines, deterministic source-index contract.
- `polynomial_oracle.py`: independent integer-polynomial certificate regenerated from original numerator/denominator.
- `tests/test_adaptive_arctan_frame.py`: root-discoverable tests, including the previous mirror's resonance at h=13.
- [FINITE_OBSERVER_BARRIER.md](FINITE_OBSERVER_BARRIER.md): strictly positive, decreasing source counterfeits match any finite mirror observer but complete to a rational nonnormal point.

## Main conditional statement

Write `h=16^v m`, `16∤m`. Let `k(h)=ceil(sqrt h)` if v is even and `ceil(2 sqrt h)` if v is odd; let `φ_h=h atan r(k(h))`. Then **for all positive h**:

`|sin(φ_(16h)-φ_h)| > 1/8`.

Define `B_N(h)=N^-1 sum_(n=1)^N sin(2πh U_n-φ_h)`. For all positive N,h:

`|A_N(h)| < 8 (|B_N(h)|+|B_N(16h)|+(2+165h/56)/N)`.

Consequently for the original selected zero-seed source **π is base-16 normal iff B_N(h)->0 for every fixed h>=1**. The vanishing is still OPEN. This is a sharper *well-conditioned criterion*, not a π-normality proof or an algorithmic acceleration claim.

## Reproduction on complete repo

`python -m unittest discover -s tests -p 'test_adaptive_arctan_frame.py' -v`

`python research/2026-11-01/adaptive_arctan_frame/polynomial_oracle.py`

`python research/2026-11-01/adaptive_arctan_frame/finite_holdouts.py`

Then run SUCC's mandatory full test/provenance/foundations/ordinal scripts on the actual integrated checkout (NOT claimed in a partial archive). Do not automatically merge this stacked draft.

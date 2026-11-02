# Operation Seeded Zak Seam — exact arithmetic/analytic chirality as a typed band

**User hypothesis:** finite/integer and analytic/continuum descriptions may be Fourier-dual, moving orthogonally while gluing at an arithmetic sampling seam; an initial seed should select the carrier section.

**Verdict:** mathematical model survives, with an important correction: the integer initial value alone does **not** select the continuum interpolation. For a fixed authentic BBP future tail T, every continuous solution of the real-time successor law is `U(t)=16^t Q(t)-T(t)`, with Q any 1-periodic function. The actual `U0=0` only pins Q(0)=pi/16. Selecting canonical `Q(t)=pi/16` throughout is a **separately declared analytic horizontal-section condition**.

The classical Zak transform gives an exact twisted band `Z(t+1,xi)=exp(2pi i xi)Z(t,xi)` and the arithmetic seam `Z(0,0)=S_N(h)`. Its Fourier aliases are orthogonal in L2 but interfere when sampled at t=0. The universal Zak norm is seed-blind; the same original forcing at q=1/5 gives N-scale seam coherence, so no positivity or topological twist alone proves normality.

The Mellin reformulation makes dual 16-clock frequencies `2pi ell/log16` explicit, and a strict interpolation counterexample proves that individual alias coefficients depend on the chosen continuum reconstruction despite the EXACT unchanged discrete source/orbit.

**Read:** [PROOFS.md](PROOFS.md), [CLAIMS.md](CLAIMS.md), [NEXT.md](NEXT.md), [VALIDATION.md](VALIDATION.md). Exact independent stdlib tests under root `tests/test_seeded_zak_seam.py`.

**Status:** elementary/classical paper derivation + local finite tests, no external referee, no Lean, no full main CI, no new selected signed Weyl estimate. π base-16 normality and RH remain OPEN. No production/source/formal modules touched, research draft only.

# OPERATION GAMMA SOLENOID × ORTHOGONAL RIEMANN SPHERE — 2026-11-05

**Research-only draft child of SUCC [#513](https://github.com/femboy2112/SUCC/pull/513).** The zero-seeded original BBP forcing, main, historical proofs, Lean, source contract, manifest and production are unchanged. Base-16 normality of π, source-selected Weyl smallness, and RH remain OPEN.

## Six source-faithful results

1. **Intrinsic Gaussian atom and scaling.** The inherited prime-character primal has `u=(1+i)/2` with `u/ubar=i` and `u^8=1/16`. Thus conjugate 45° spiral rotations share one exact radix-16 contraction.
2. **One genuine analytic circle.** Combine the inherited angular source `K_a(t)=4/((t-1)^2+1)` and radial source `F(t)=(2-t²)/((t-1)^2+1)` into `W(t)=F(t)exp(2i theta(t)) = u + ubar exp(4i theta(t))`. On t∈[0,1], W traces exactly the semicircle centered at u, radius 1/√2, from 1 through 1+i at `tau=2−sqrt2` to i. **`K_a(t)dt=sqrt2|dW(t)|`, integral π.**
3. **Riemann-sphere transverse differential.** The actual angular/radial SUCC kernels are complementary meromorphic `dlog` forms with chiral combinations `omega_a±i omega_r` and nonzero oriented puncture periods, even though the radial interval integral vanishes. The correct sphere transverse map H(z)=(z−1)/(z+1) is an SU(2) rotation; its two Gaussian spiral axes share multiplier u but do **not** commute, with exact finite defect `(-1−3i)/10`.
4. **Exact Gamma/beta bridge.** The rational coordinate `X(t)=[t(2-t)/((t-1)^2+1)]²` has `K_a dt=dX/sqrt(X(1-X))`. Thus SUCC's angular π period is exactly `B(1/2,1/2)=Gamma(1/2)²` and may be reconstructed by integrating over two orthogonal positive Gamma axes and taking their projective ratio.
5. **Hostile Gamma non-Haar result.** Periodizing `exp(v−exp(v))` modulo log16 yields Fourier coefficients `Gamma(1−2πik/log16)`, never zero; even coupling the opposite winding yields `|Gamma|²=πω/sinh(πω)>0`. The infinite Gamma carrier does not imply equidistribution of its own weighted phase, much less SUCC's selected orbit.
6. **New-to-SUCC odd-cyclotomic deck rigidity.** Transport actual source phases `ζ_n=e(U_n)` through the authentic Cayley chart. The resulting sphere phase is `S(ζ)=-B(ζ)²`, a degree-two Blaschke map with sharp angular distortion `φ²`. Its deck involution has **no two odd-order torsion points on the same fiber**, proved by reduction of the exact Gaussian-integer deck relation at prime 1+i. All genuine BBP U_n have odd denominators; hence S is injective on their arithmetic phase carrier. **But it is not stably invertible:** a deck-flipped non-Haar input has the same S distribution as Haar, and odd-torsion approximants inherit this weakness. The correct S output reference for Haar input is a non-Haar Poisson law at `η=(3−4i)/25`.

## Proof, reproducibility, limitations

- [Preregistration](PREREGISTRATION.md) — transparent distinction of prederived GS1–GS4 and later discoveries.
- [Complete analytic proofs](PROOFS.md) — Gaussian, sphere, meromorphic, Gamma and Beta identities.
- [Arithmetic deck rigidity](ARITHMETIC_DECK_RIGIDITY.md) — odd-cyclotomic exact branch proof, golden distortion and non-Haar weak-inverse countermodel.
- [Validation](VALIDATION.md) — 19 focused standalone exact/numeric tests PASS; Git-blobs of committed tests matched executed bytes. **No full native/hosted CI claim**.
- [Claim ledger](CLAIM_LEDGER.md), [source genealogy](SOURCE_MAP.md), [next genuine arithmetic gate](NEXT.md).

Three new root test modules: `tests/test_gamma_sphere_solenoid.py`, `tests/test_gamma_sphere_branchlift.py`, `tests/test_gamma_sphere_torsion_lift.py`.

**Critical result boundary:** All source interval geometry persists under same-forcing coherent wrong seed `s*=-π/16`, whose chronological phase orbit converges to a point. Circle geometry plus exact cyclotomic branch selection is real structure, but no actual source-selected signed Weyl estimate was obtained. No global scholarly novelty, new Lean proof, physical quantum field, or π-normality proof claimed.

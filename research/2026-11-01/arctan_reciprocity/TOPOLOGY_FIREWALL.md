# AR-09 — Irrational reciprocal mirror: exact finite total-variation obstruction and Fourier weak-observer calibration

**Research-only classical theorem specialized to the original BBP source and source-r2 projective mirror.** No new normality, RH or physical quantum conclusion.

## The sharp finite obstruction

The original signed four-pole BBP recurrence with literal `U_0=0` has all `U_n in Q`. Its empirical probability

\[
\mu_N=\frac1N\sum_{n=1}^N\delta_{U_n\pmod1}
\]

has support contained in the rational subgroup `Q/Z` of the real circle. AR-02's mirror is `J_beta(x)=beta-x`, with `beta=atan(106/819)/pi` irrational, as proved by the explicit Gaussian-rational `gamma=e(beta)=(659525+173628i)/681997` of infinite order. Therefore the reflected empirical probability `nu_N=(J_beta)_*mu_N` is supported entirely in the coset `beta-Q/Z`, which is **disjoint** from `Q/Z`.

For every integer N>=1, without any approximation:

\[
\boxed{\sup_{A\text{ Borel}}|\mu_N(A)-\nu_N(A)|=1,\qquad
\|\mu_N-\nu_N\|_{\mathrm{variation}}=2.}
\]

Proof: if rational u,v satisfied `u=beta-v (mod 1)`, beta would be rational mod1, making `gamma=e(beta)` a root of unity. But gamma is not any root of unity in Q(i). Set `A=Q/Z` to achieve the supremum 1; both measures have total mass 1, giving variation norm 2. This is an **all-N topological no-go**, not an asymptotic numerical observation.

Thus no possible proof of an asymptotic arctan-mirror invariance of these finite empirical measures can proceed in **total-variation norm**, even if pi is normal! The correct topology in AR-03/04 is **weak-* convergence** against continuous observers (equivalently, each fixed integer Fourier character), or an appropriately certified smoothing/resolution scheme. Do not silently replace pointwise/Fourier convergence by TV closeness, or vice versa.

## Sharp finite positive calibration: exact Fourier agreement, maximal TV difference

Fix M>=2. Let `rho_M` be the uniform probability on the rational grid `G_M={j/M:0<=j<M}`. Let `tau_M=(J_beta)_*rho_M`, on an irrationally shifted/reflected grid. Again `d_TV(rho_M,tau_M)=1` at **every** M.

However, for every integer h not divisible by M, the exact finite geometric series gives

\[
\widehat\rho_M(h)=\frac1M\sum_{j=0}^{M-1}e(hj/M)=0,
\quad\widehat\tau_M(h)=\gamma^h\overline{\widehat\rho_M(h)}=0.
\]

Therefore for each M the two singular measures have **identical responses at every nonzero integer Fourier mode with |h|<M**. As M grows, their Fourier coefficients converge to those of Haar, so **both** measures converge weak-* to Haar while their total-variation distance remains 1.

This is an exact calibrated example of the crucial SUCC distinction:

- full point-label / singular-support observer: maximally distinguishing;
- any fixed finite Fourier-band observer: unable to distinguish the two grids for sufficiently large M;
- asymptotic weak-* observer: both look Haar;
- the selected original BBP arithmetic orbit: **not yet proved** to approach Haar.

The calibration is NOT a claimed statement that the original BBP orbit is normal, nor that a fixed finite Fourier band establishes all-horizon cancellation. It is an operational source-map warning for the new mirror gate, aligned with the earlier SUCC Zak/point-trace firewall.

## Categorical interpretation

The two empirical supports are disjoint **inside the same ambient circle**, so equality of atomic states in the original rational clock is impossible. There nevertheless exists a perfectly legitimate *frame-change correspondence* `x -> beta-x`; it simply leaves the rational phase subgroup. A natural transformation of **test-function representations** can therefore be valid even while equality-based finite atomic matching fails, and weak observational limits can coincide. The correct category must declare its morphism type and observation topology: projective frame covariance, phase-character naturality, and empirical-measure invariance are different properties.

This specifically forbids the tempting inference "Möbius conjugacy is exact, so the original and reflected finite point measures are close." They are always maximally far in TV. The AR-04 theorem instead uses the **asymptotic vanishing of one signed real Fourier quadrature per fixed harmonic**, which is not known for the original selected source.

## Boundaries and independent controls

- The root-of-unity argument is exact in Q(i), and each original U_n is exact rational. No floating inversion of tangent or finite empirical approximation enters the proof.
- A rational reflection angle, including the bare `beta=1/2`, can map rational points back into rational points; the TV disjointness proof then does not apply. The explicit non-Haar bare-reciprocal Cantor model in AR-06 separately shows why such a rational axis is analytically inadequate.
- This theorem distinguishes weak-* from total variation. It does not assert any new decay of a BBP Fourier coefficient or a physical continuum limit.
- An IID uniform base-16 Cantor countermodel and a coherent same-forcing altered seed remain necessary hostile probes for attempts to turn geometry into a selected signed proof.

## Validation of this addendum

Seven new stdlib exact tests passed, including the source-r2 torsion classification, rational source-orbit sample checks, all-N theorem preconditions, exact M-grid Fourier zeros, and invalid-input controls. Combined with the existing categorical/arctan local partial snapshot, **107 tests discovered: 106 PASS, 1 inherited full-upstream-core SKIP**. This is not a complete current SUCC checkout or Lean certification.

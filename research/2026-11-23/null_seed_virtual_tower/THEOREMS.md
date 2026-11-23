# OPERATION NULL INFORMATION — virtual-field differential tower at the original BBP zero seed

**2026-11-23 — additive draft stacked on SUCC Iroh #688.** This supersedes the hunt for a determinant as the primary missing object. Start with the exact null-seeded virtual carrier, then derive arithmetic constraints from its *infinite compatible null tower*. Do not modify the original four signed poles or `U_0=0`.

## 1. Distinguished zero and nonzero virtual source

Let
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad
U_n=16U_{n-1}+r(n),\quad x=\sum_{n\ge1}16^{-n}r(n)=\pi/16.
\]
The signed Mellin polynomial `Q(t)=4-2t³-t⁴-t⁵=(1-t)(4+4t+4t²+2t³+t⁴)>0` on `(0,1)` defines a positive finite measure
\[
d\mu(u)=\frac{Q(u^{1/8})}{8u^{7/8}}du,\qquad r(n)=\int_0^1u^{n-1}d\mu(u).
\]
Define the **virtual analytic carrier**
\[
\mathcal V_\mu(z)=\int_0^1\frac{d\mu(u)}{16-uz}
=\sum_{k\ge0}\frac{r(k+1)}{16^{k+1}}z^k,\quad |z|<16,\qquad \mathcal V_\mu(1)=x.
\]
The literal seed `s=0` is *zero additional homogeneous intervention*, not zero mathematical information: `U_n(s)=16^n(s+P_n)` and `U_n(s)+T_n=16^n(x+s)`. Its carrier has nonzero derivative data.

## 2. Exact source all-jet null rigidity — CLASSICAL / PROVED IN DECLARED CLASS

For any finite signed Borel measure `ν` on `[0,1]` define `N_ν(z)=\mathcal V_\nu(z)-\mathcal V_\mu(z)`. Then
\[
N_\nu^{(k)}(0)
=\frac{k!}{16^{k+1}}\int_0^1u^k\,d(\nu-\mu)(u).
\]
Consequently
\[
\boxed{\forall k\ge0:\ N_\nu^{(k)}(0)=0\quad\Longleftrightarrow\quad\nu=\mu.}
\]
**Proof.** The null tower annihilates every polynomial moment of the finite signed measure `ν−μ`. Weierstrass density in `C([0,1])` makes its integral vanish on every continuous function, hence the measure is zero. The converse is immediate. This reconstructs the actual *source* from null discrepancy data, not merely its scalar endpoint. Finite jets remain insufficient in this unrestricted class: SUCC #467 supplies positive source-moment echoes. For a merely smooth nonanalytic field, `e^{-1/z²}` extended by zero at zero supplies a nonzero infinitely flat counterexample; the analytic/measure domain is essential.

## 3. Exact zero-derivative digit tower with unique infinite seed — PROVED

For `s∈R/Z` and `n≥1` define the authentic completed digit observer
\[
d_n(s)=\lfloor16^n(x+s)\rfloor-16\lfloor16^{n-1}(x+s)\rfloor.
\]
Let `J_N(s)=(d_1(s),...,d_N(s))` and `C_N=\{s:J_N(s)=J_N(0)\}`. Because `x=π/16` is irrational, it lies strictly within its depth-`N` base-16 cylinder; `C_N` is a circle interval of length `16^{-N}` containing zero in its interior. Hence
\[
\boxed{C_{N+1}\subset C_N,\quad |C_N|=16^{-N},\quad\bigcap_{N\ge1}C_N=\{0\}\pmod1.}
\]
**Proof.** First `N` digits select exactly one interval of length `16^{-N}` in the circle; the intervals are nested with vanishing diameter. At each *finite* level the digit functions are constant in a neighborhood of the genuine seed, so
\[
\boxed{\partial_s^k d_n(0)=0\quad\forall n\ge1,\ \forall k\ge1.}
\]
There is **no common positive neighborhood** for all infinitely many observations: the vanishing finite jets coexist with a uniquely identified infinite compatible seed. This is null-information in the observer/inverse-limit sense, not an identity `0=0`. Ordinary derivatives alone do not recover the off-seed boundary geometry.

### Quantitative seed-horizon under the independent π exponent-two result

Set `ρ_N=dist(x,16^{-N}Z)`, the nearest seam of the complete first-`N` observer. Because radix grids nest, `J_N(s)=J_N(0)` for `|s|<ρ_N`, and `ρ_N≤1/(2·16^N)`. If the external formally checked `μ(π)=2` is imported, then `μ(x)=2` and for every `ε>0` there exists `N_ε` such that
\[
\boxed{16^{-(2+\epsilon)N}\le\rho_N\le\frac{1}{2\cdot16^N}\qquad(N\ge N_\epsilon).}
\]
Proof: apply the eventual rational-approximation lower bound to all `a/16^N`. This is a quantitative null-information *aperture*, **not** a Weyl saving.

## 4. The signed virtual seam current exists despite all finite point derivatives being zero

As distributions in `s`,
\[
\boxed{
D_s d_n(s)=\sum_{m\in\mathbb Z}(1-16\,{\bf1}_{16\mid m})
\delta\!\left(s-\left(\frac m{16^n}-x\right)\right).
}
\]
**Proof.** Differentiate the two floor functions distributionally. Each ordinary fine-radix seam has unit jump; every sixteenth seam simultaneously resets the previous digit place and has jump `1−16=−15`. Each seed period contains `15·16^{n−1}` positive unit jumps and `16^{n−1}` negative resets. Their signed sum is zero, while their support and variation become arbitrarily fine. The nearest seam approaches zero at rate `ρ_n→0`.

Thus `∂_s^k d_n(0)=0` for all finite `n,k` **does not imply** that `D_s d_n` is the zero distribution. This is the inside/outside differential distinction. SUCC #684's authenticated quarter-bit seam currents are compatible with this exact ordinary-digit calculation.

**Hostile models:** Same forcing with changed seed `s=−x` has rational completed endpoint zero on every seam, and is rejected by authentication. The generalized Kempner `β=Σ16^{-2^k}` is irrational, nonnormal, and has imported `μ(β)=2`; it has the **same** finite flatness/inverse-limit uniqueness. Consequently, no claim that these null towers *alone* prove normality survives this control.

## 5. Multiscale finite-difference arithmetic capacity — new constructive instrument

A transported, *nonlocal* finite difference at the seed is
\[
\nabla_t F(0)=\frac{F(t)-F(0)}t,\quad t\ne0.
\]
Let `F∈Z[z]`, `F(0)=0`. If the multiscale null differential conditions
\[
\nabla_{16^{-j}}F(0)=0,\qquad 1\le j\le d
\]
hold, then `F(16^{-j})=0` for `1≤j≤d`. The rational-root theorem and Gauss lemma imply
\[
F(z)=z\prod_{j=1}^d(1-16^jz)\,Q(z),\qquad Q∈\mathbb Z[z].
\]
For nonzero `F` the leading coefficient is an integer multiple of `16^{d(d+1)/2}`, so
\[
\boxed{\|F\|_{\ell^1(\mathrm{coeff})}\ge16^{d(d+1)/2}.}
\]
A bounded-coefficient nonzero virtual field therefore **cannot support too many transported exact null probes**. This is an operational arithmetic multiplicity/height mechanism derived from null constraints rather than a guessed determinant.

For the authentic zero-seed two-carry identity (#685), `a_n=d_n−κ_n=δ_n−16δ_{n−1}`, `δ_n∈{0,1}`, define
\[
F_B(z)=z\sum_{j=0}^{B-1}a_{B+j}z^j,\qquad \|F_B\|_1\le16B.
\]
If all first `d` transported null probes vanish and `16^{d(d+1)/2}>16B`, then `F_B≡0`, forcing `δ_{B−1}=...=δ_{2B−1}=0`. **These hypotheses are not yet derived from R0 failure**, and this *particular* field may be identically zero: #685 certifies long original-source periods of zero completion carry. Nor does disappearance of both carry defects imply R0. The capacity theorem is a validated *instrument*, not the missing signed theorem by rearrangement.

## 7. NEW: the phase-only infinite seed-jet tower has no common analytic neighborhood

This locates an exact missing **source/phase transport theorem** rather than inventing a new determinant. Fix any real `x` (including `π/16`), a nonzero integer character `h` and real seed `s`. Define
\[
\Psi_h(s,z)=\sum_{n=0}^\infty e(h16^n(x+s))\,z^n,\qquad e(t)=\exp(2\pi i t),\quad |z|<1.
\]
Every fixed-real-`s` slice is holomorphic in `z` for `|z|<1`, and the series is jointly continuous for real `s` on compact z-disks. Its formal seed-derivative sheet of order `k` is, on `|z|<16^{-k}`,
\[
\boxed{
\partial_s^k\Psi_h(0,z)=(2\pi i h)^k
\sum_{n=0}^\infty16^{kn}e(h16^nx)z^n.}
\]
**Exact radius theorem:** The complex power series on the right has radius **exactly** `16^{-k}` for every `k≥0`, since every coefficient has modulus `(2π|h|)^k16^{kn}`. Thus the radii of successive derivative sheets shrink to zero as `k→∞`, independently of normality, seed, source or phase structure.

**No jointly holomorphic phase tower:** There is no common bidisk `|s|<a, |z|<b`, with `a,b>0`, supporting a function jointly holomorphic in `(s,z)` that agrees with these real-seed phase slices. If such a function existed, its `k`th derivative at `s=0` would be holomorphic throughout `|z|<b`; yet its Taylor coefficients in `z` have exact convergence radius `16^{-k}`. Choose `k` with `16^{-k}<b`: contradiction. The obstruction is *nonuniform seed sensitivity*, not any special unproved property of π.

**Renormalization collapses the phase-only information:** Let `R_k` act on a formal series by multiplying its `z^n` coefficient by `16^{-kn}`. Then exactly
\[
R_k\bigl(\partial_s^k\Psi_h(0,z)\bigr)
=(2\pi ih)^k\,\Psi_h(0,z).
\]
Thus rescaling restores a common analytic radius, but every normalized derivative sheet is just a scalar multiple of the original phase journal. No independent prime/cofactor/carry rank is recovered, even using all `k`. The countermodel `x=1/16,h=16` is completely locked and has the exact rational sheets
\[
(2\pi ih)^{-k}\partial_s^k\Psi_h(0,z)=\frac1{1-16^kz}.
\]
All of these facts hold for a rational locked source too; they are **structural no-gos**, not phase anti-lock theorems.

**Corrective implication:** We may use an *analytic source moment* null germ (``1–2`), a *projective seed-cylinder* null object (`3`), and a *distributional signed seam* (`4`). We **may not** silently combine the entire completed phase seed-derivative tower into a fixed-radius holomorphic germ or claim higher normalized phase jets create independent information. A source-covariant mixed differential with authenticated carries and noncommuting source/observation transport is the required mathematical lift. Whether R0 failure forces excess multiplicity of that lift remains **UNVERIFIED**.

## 8. Correct next falsification opportunity

The new primary object is an **authenticated null-information virtual tower** simultaneously retaining: positive source measure/moment jets; actual `U_0=0`; unwrapped integer carry, signed future crossing and chronological memory; and the inverse-limit seed cylinder with its signed distributional seam current. **Only after constructing the tower** should we ask whether its forced null constraints entail an integer/p-adic determinant, height or impossible source capacity.

The next mathematical obligations are distinct:

1. Show how a hypothetical `R0`-failing late shell of the actual source forces **quantitatively many transported null conditions** on a *specific* virtual field, with explicit orientation and error rather than asserting it from small average phase.
2. Prove that exact source/zero-seed structure forces this **same** virtual field to be *nonzero* while its admissible arithmetic/analytic capacity is too small to sustain those null conditions.
3. Test against the authentic zero seed, cancelling seed, alias `1/16`, rational lock, exponent-two nonnormal Kempner, finite moment echoes (#467), and the exact no-completion-carry regions (#685).

**Claim ledger:** Source moment reconstruction, finite-null/infinite-inverse-limit seed uniqueness, and signed seam calculus — **DISCLOSED as classical deductions**. `μ(π)=2` seed aperture — **CONDITIONAL on independently formalized external proof**. Polynomial scale-null capacity — **DISCLOSED elementary Gauss-lemma theorem**. Normality from point-jet flatness — **REFUTED by nonnormal irrational control**. R0-failure-to-overdetermined-null and source-certified nonzero contradiction — **UNVERIFIED**. `R0` and full base-16 π normality remain **OPEN**.

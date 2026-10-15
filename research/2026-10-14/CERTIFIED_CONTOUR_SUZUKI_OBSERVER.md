# CONTOUR × SUZUKI — a certified source-derived zero-count observer and its Weil-sign boundary

**Research date:** 2026-10-14. **Exact parent:** `femboy2112/SUCC`, THETA-JETS draft PR #78 head `96fbc5eac5705573014c0c8bbd4fc85c63bf1fd9`, descended from all-place source interaction PR #73 and actual completed-Weil PR #71. Sister projects: CARLEMAN/Suzuki PR #70, Gaussian signed-form PR #76, IdealHard + model-sandwich PR #75/#77, BLACK SUN PR #79. **All are separate provenance families; no PR was silently merged.**

**RH PROVED: NO.** No nontrivial ζ-zero list, requested ordinate, private physical sensor, or fabricated Euler place is used to construct the original-ξ certificate. The construction starts from the original integer Gaussian theta source and imports the *classical* Poisson/theta identification and Weil explicit formula. Academic priority for the methods is not claimed; the target-specific source-typed software/quantitative certificate is new to this research branch.

## 0. The exact object and the falsifiable question

The previous PR #78 already certified that genuine `F(z)=ξ(1/2+z)` has no zeros in `|z|≤11/2`, from rigorous rational Gaussian-theta Taylor intervals. Simply repeating that fact would not be progress. The new mathematical objective is a **contour observer** that:

1. accepts a genuine source-identified even Taylor polynomial `P(z)=Σ_{j=0}^{20}â_j z^{2j}` with certified `|F−P|≤ε` throughout a disk;
2. constructs a rectangle as a finite chain of lawful rational complex-SUCC increments;
3. proves the entire analytic image of each contour segment is nonzero from an exact derivative majorant, not sampled signs;
4. computes its integer winding via rational ray crossings; hence determines an argument-principle zero **count with multiplicity**;
5. transports that finite spectral count to a precisely scoped zero-side Weil pairing, retaining the full signed arithmetic-side Weil/Suzuki relation as an *independent external equality*; and
6. refuses a universal positivity claim, source mutations, unsupported contour radii, and unlicensed interpretations of finite samples as arbitrary analytic identities.

## 1. Source-identified polynomial: two independent missing-data debts

The authenticated upstream source is the **specific immutable Git blob** `2657d92f15fcd77e2232f2cf305561a090ff28ce` at `research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json` on PR #78. `original_xi_model(root)` reads the complete file, checks the actual Git-object SHA-1 of its bytes, verifies the original-source tag and exact `(degree,modes,T,cells)=(20,3,8,1536)` contract, and parses all 21 even coefficient intervals and the 20th positive theta moment interval. The bundled *outward-rounded* 10^50-scaled shadow is **not** silently promoted to a genuine source: a separate CI gate compares every one of its 21 intervals and the 20th positive moment upper bound against that exact immutable upstream blob.

From one genuine integer theta source,

\[
F(z)=\frac12+(z^2-\tfrac14)B(z),\qquad
B(z)=\int_1^\infty \psi(t)t^{-3/4}\cosh\!\left(\frac{z\log t}{2}\right)dt,
\quad\psi(t)=\sum_{n\ge1}e^{-\pi n^2t}.
\]

The existing PR #78 derives `B(z)=Σ b_j z^{2j}` and `a_0=1/2-b_0/4, a_j=b_{j-1}-b_j/4` from the original self-dual theta / completed zeta source; that identity is not re-proved by the finite code here. The present program independently improves the *analytic tail* and then derives a contour theorem.

For a comparison radius `T>R` and true degree `D=20`, with intervals `[a_j^−,a_j^+]` and `b_D≤b_D^+`, define the midpoint coefficients `â_j=(a_j^−+a_j^+)/2`. Then the exact finite-observer error is

\[
 E_{\rm coeff}(R)=\sum_{j=0}^D\frac{a_j^+-a_j^-}{2}R^{2j}.
\]

The true analytic remainder (PR #78, TJ-03), using positivity of the actual theta moments, obeys

\[
\sup_{|z|\le R}|F(z)-P(z)|\le E_{\rm coeff}(R)
+\underbrace{b_D^+R^{2D+2}+(R^2+\tfrac14)B(T)(R/T)^{2D+2}}_{E_{\rm analytic}(R,T)}.
\tag{CS-1}
\]

### A genuinely sharper Gaussian-tail theorem (CS-02)

For all `t≥1`, `ψ(t)<2e^{-3t}`, because `π>3` and Gaussian integer squares have a geometrically bounded tail. Also `log t≤sqrt(t)` and `t^{-3/4}≤1`.

**(i) Positive moment remainder, all D≥0:**
\[
\boxed{b_D\le\frac{2D!}{4^D(2D)!3^{D+1}}.}
\tag{CS-2}
\]
Indeed `(log t)^{2D}≤t^D` and the integral is bounded by `2Γ(D+1)/3^{D+1}`. This is vastly sharper at D=20 than the parent receipt's numeric precision floor; take the minimum of the two independent genuine-source upper bounds.

**(ii) Global analytic comparison at even T=2m:** for `t≥1`,
`cosh(m log t)=(t^m+t^{-m})/2≤t^m`. Thus
\[
\boxed{B(2m)\le\frac{2m!}{3^{m+1}}.}
\tag{CS-3}
\]
This is a direct source-Gaussian Mellin moment bound, independent of zeros. In contrast, the parent majorant `exp(T²/8)` becomes unnecessarily enormous at T=20. For arbitrary rational comparison T, the code retains a verified rational Taylor-plus-geometric enclosure for `exp(T²/8)`.

Equations (CS-1)–(CS-3) are valid uniformly for every **complex** `z` in the disk. These are analytic bounds, not a finite numerically fitted error model.

## 2. The exact rectangular-contour theorem (CS-03; general/CLASSICAL)

Let `F` be an entire function and `P∈Q(i)[z]`, with a mathematically justified bound `sup_{|z|≤R}|F(z)-P(z)|≤ε`. Let a simple counterclockwise rectangle `Γ` be divided into finitely many rational edges `z_i→z_{i+1}` whose whole segments lie inside `|z|≤R`. Set

\[
L_R=\sum_{j=1}^{d}j\|c_j\|_1R^{j-1},\quad
\|x+iy\|_1=|x|+|y|,
\]

where `c_j∈Q(i)` are the actual polynomial coefficients (odd coefficients may be zero). For each edge define the **rational lower margin**
\[
\boxed{m_i:=\max(|\Re P(z_i)|,|\Im P(z_i)|)-L_R\|z_{i+1}-z_i\|_1-\varepsilon.}
\tag{CS-4}
\]

**Theorem.** If every `m_i>0`, `F` is nonzero along Γ and the winding of `F(Γ)` equals the winding of the rational image polygon joining successive points `P(z_i)`. An integer winding is computed by crossing any admissible rational ray `y=qx`, `x>0` (the algorithm rejects ray/vertex or origin degeneracies). By the argument principle, that winding equals the **total number of F-zeros in Γ**, with multiplicities. No roots or nontrivial zeta zero positions are consulted.

**Proof:** `|P(z)-P(z_i)|≤L_R|z-z_i|≤L_R||z_{i+1}-z_i||_1` on each edge. Every point of `F` and `P` on that edge, and of the straight image chord, stays in the open disk centered at `P(z_i)` whose radius is strictly less than `|P(z_i)|`. Therefore the homotopy from `F(Γ)` to `P(Γ)` and then to the rational image polygon avoids zero. Exact crossing numbers compute its winding. The rectangle is simple and CCW, so argument principle gives the stated zero count. The rational complex arithmetic never evaluates atan/arg numerically.

If any margin fails, return `UNRESOLVED`; do not claim a zero or nonzero certificate from the sampled vertices.

## 3. Original completed ζ: an improved bounded zero-free result (CS-04)

With the **same** source as PR #78, choose

- comparison radius `T=20` and certified whole-disk radius `R=107/10`;
- counterclockwise rectangle in `z=s−1/2`: `|Re z|≤15/2`, `|Im z|≤15/2`;
- `2048` exact rational divisions per side, `8192` vertices overall;
- all 21 original theta coefficient intervals and the source analytic majorants (CS-2),(CS-3).

The code computes and checks **every edge's exact positive lower margin**, with the rounded-outward development receipt recording

\[
\varepsilon < \frac{82156}{10^6},\qquad
\min_i m_i > \frac{2057}{10^6}.
\tag{CS-5}
\]

The coefficients were locally staged as outward-rounded exact rationals from PR #78. **These inequalities become source-certified only when the remote CI replays the immutable PR #78 blob and checks its full intervals**. The code's separate `--authenticate-parent` mode performs exactly that check and recomputes the contour against the original unrounded intervals, which are at least as tight.

The verified winding is 0. Thus, subject to that upstream source verification,

\[
\boxed{\xi(s)\ne0\quad\text{throughout the CLOSED disk }|s-\tfrac12|\le\tfrac{15}{2}.}
\tag{CS-6}
\]

The disk is contained inside the certified closed rectangle, and contour nonvanishing includes its boundary. This improves **this particular SUCC source-first proof instrument** from radius 11/2 in PR #78 to 15/2. It is weaker than classical extensive verification of the lower zeta zeros and is **not RH**.

### Two positive controls

- `F_0(z)=ξ(1/2+z)−ξ(1/2)`: reflection symmetry makes z=0 at least a double zero. Using the same source intervals with exact cancellation of the constant term, the 1×1 centered rectangle has **winding 2**. It certifies that the central zero is exactly double and no additional zeros occur in that rectangle; these are zeros of `F_0`, **not** zeta zeros.
- Synthetic polynomials `z²` and `z⁴` give their exact counts 2 and 4. Fake sources/incorrect ray/failed analytic error caps must be rejected.

## 4. Reflection-symmetric but non-Euler adversary, plus a NEGATIVE local Weil-type pairing (CS-05)

Construct the deliberate **non-Euler** mutation
\[
\Xi_{\rm fake}(\tfrac12+z)=(10z^2-\tfrac32)F(z)
=(1+10s(s-1))\xi(s).
\tag{CS-7}
\]

It retains the functional reflection `z→−z`, and the original ξ source is still zero-free inside the unit rectangle, but the mutant has two **additional** real roots `z=±√(3/20)` inside the critical strip. These are off the critical line and the original Euler germ is altered; it is NOT a genuine zeta completed source. Its uniform analytic-error majorant follows from multiplication of the authentic original bound by `10R²+3/2`. The same 1×1 rational contour certifies **count 2**, whereas the genuine source certifies 0.

The local zero-side pairing is demonstrably indefinite. For real odd
`v_a(x)=x(1−(x/a)²)^8` on `|x|<a` and zero otherwise, write
`V(z)=∫v_a(x)e^{zx}dx`. Then for the reflected pair ±d with `d²=3/20`,
`V(−d)=−V(d)`, and
\[
V(d)=2\int_0^a x(1-(x/a)^2)^8\sinh(dx)dx
\ge 2da^3 C_8>0,
\quad C_8=\sum_{k=0}^8(-1)^k{8\choose k}/(2k+3).
\]

Therefore **their finite spectral autocorrelation pairing** obeys
\[
\boxed{\mathcal W_{\rm fake,local}(v_a,v_a)
= -2V(d)^2\le-\frac65 C_8^2a^6<0.}
\tag{CS-8}
\]

This is an explicit analytic sign witness, not a computed eigenvalue. It refutes the false route “reflection + global analytic continuation + finite source shadows ⇒ Weil positivity”. It is **not** a negative Weil witness for authentic ζ: the mutant violates Euler source identification, and the complete authentic Weil explicit formula is not transported automatically to the mutant.

## 5. The exact local contour ↔ full Suzuki/Weil distribution comparison (CS-06)

For `h=v*\widetilde w`, `v,w∈C_c^∞(R)`, let
\[
\mathcal H_h(s)=\int_\mathbb R h(x)e^{(s-1/2)x}dx
=\mathcal H_v(s)\overline{\mathcal H_w(1-\overline s)}.
\]

For any positively oriented finite contour Γ free of zeros of the **authentic** completed ξ,
\[
\boxed{
\frac1{2\pi i}\oint_\Gamma
\mathcal H_h(s)\frac{\xi'(s)}{\xi(s)}ds
=\sum_{\rho\;\mathrm{inside}\;\Gamma}m_\rho\mathcal H_h(\rho).
}
\tag{CS-9}
\]

This is the classical residue theorem; the functional uses no explicit zero coordinate, although evaluating the weighted complex contour integral with rigorous finite error is a *separate* computational problem. When an enclosed zero is proven to lie on `Re s=1/2`, the diagonal term becomes `|\mathcal H_v(1/2+i\gamma)|²≥0`. A certified **zero count alone** does not prove the enclosed zeros are on the line. A bounded contour with zero count 0 has a trivially nonnegative *local* pairing, but the rest of the completed Weil form is not included.

Under the classical Weil explicit formula (SUCC E38/PR #71), the **actual** signed completed Weil form on smooth compact tests is
\[
Q_W(v,w)=W_\zeta(v*\widetilde w)=
\sum_{\rho}m_\rho\mathcal H_{v*\widetilde w}(\rho),
\tag{CS-10}
\]

where the **arithmetic** distribution on the left contains the *genuine* `Λ(n)/√n` prime powers, symmetric exponentials for poles, `Γ_R` contact and integral, and the correct half-density/chart. (The zero-sum identity is **EXTERNAL/CLASSICAL**, not proved by drawing contours.) Smooth-compact h has sufficient Fourier decay for absolute convergence on the critical strip using standard Riemann-von Mangoldt zero counting. The genuine analytic source is matched by equality of the open Euler-region germ, not by a finite zero list.

### Quantitative smooth-test tail (CS-07, classical conditional zero-count import)

Choose a concrete test family `v_a(x)=(1-(x/a)^2)^8_+`, `0<a≤1`, and `h=v_a*\widetilde v_a`. At every critical-strip zero `ρ=β+iγ`, `|γ|≥4`, integration by parts six times yields
\[
|\mathcal H_h(\rho)|\le A_a/|\gamma|^6,\quad
A_a=3\|v_a\|_1\sum_{j=0}^6{6\choose j}2^{-(6-j)}\|v_a^{(j)}\|_1.
\tag{CS-11}
\]

The program replaces these norms by **explicit rational upper bounds** from the binomial polynomial, and uses `e^a<3` for `a≤1`. It assumes the classical zero-counting consequence `N(T)≤T²` for `T≥3` (can be deduced from explicit Rosser/Trudgian Riemann-von Mangoldt bounds; not proved by finite contour data). For integer `T≥4`, bound both conjugate upper/lower horizontal strips and sum:
\[
\boxed{\left|\sum_{|\Im\rho|\ge T}m_\rho\mathcal H_h(\rho)\right|
\le \frac{4A_a}{3(T-1)^3}.}
\tag{CS-12}
\]

**CRITICAL:** This bound is for one smooth test (or a controlled six-derivative family); it is **not uniform on the unit ball of Suzuki's `H¹_0` test space**. In fact, with `ε=n^{-2}` and `v_ε(x)=√ε v(x/ε)`, `||v_ε'||_2=||v'||_2` but `||v_ε^{(6)}||_1=n^9||v^{(6)}||_1`. The derived contour-tail instrument loses arbitrarily much high-frequency resolution while H¹ cost stays fixed. This is an explicit **IdealHard/source-probe boundary**, not evidence that RH is impossible.

## 6. Critical comparison with the other SUCC research routes

| Lineage | What is genuinely source-derived | What is NOT inferred |
| --- | --- | --- |
| PR #78 THETA-JETS | original even ξ jets, rational tails, genuine 5.5 disk, moment positivity | all-line RH or signed Weil positivity |
| **This branch** | exact rational contour winding; conditional→authenticated 7.5 disk; finite weighted zero-residue bridge; smooth-test tail | genuine global Weil sign or normalizable Suzuki operator |
| PR #70 CARLEMAN/Markov | authentic Gamma positive bath and first-prime positive **sub-form** | complete form domination including poles and other primes |
| PR #71 completed Weil | signed full compact-test distribution and uniform O(J^-2) H¹ Gamma truncation | authentic nonnegative sign |
| PR #76 Gaussian-Weil | signed finite operator discretization and conditional spectral-matrix test | global lower bound from finite Gram |
| PR #79 BLACK SUN | near-null finite-window spectral diagnostics; contact and first-prime compensation | a numerical near-zero eigenvalue as a positivity theorem |

### The strongest next verdict-changing lemma

Take a fixed radius `a` and the **authentic** arithmetic `H¹_0(-a,a)` form `Q_W`, including every prime-power in the window, all Gamma rungs, two pole channels and correct contact. Find **source-derived finite operators** `G_(a,N)` with (i) a rigorously certified *all-vector* lower bound `G_(a,N)≥−δ_(a,N)I` and (ii) a signed form/operator error `||G_a−G_(a,N)||≤ε_(a,N)` such that `δ+ε→0`. The existing PR #71/#76 estimates deliver a version of (ii); **(i) remains RH-hard.**

A contour oracle verifying more finite heights can contribute source information and finite zero counts, but CS-12 cannot replace the missing uniform lower bound because its derivative constants blow up on highly localized `H¹` tests. No finite contour scan proves all `a` or all spectral heights.

## 7. Reproduction, acceptance, provenance

- Code: `observational_succ/certified_contour_weil.py`, rational complex arithmetic, simple CCW rectangles, certified image homotopy, ray-winding, original SHA-gated theta adapter, source-mutant, explicit zero-tail norm.
- Tests: `tests/test_certified_contour_weil.py` (synthetic independent positive/negative controls, source-mutation, original adapter validation, disk-7.5 certificate, centered-zero degree and signed fake odd test).
- Source shadow: `tests/fixtures/XI_PARENT_SOURCE_OUTER_INTERVALS.json`, derived via outward `floor/ceil` at common scale `10^50` from **exact** #78 receipt; must be cross-compared with the original blob in remote CI.
- Probe/receipt: `scripts/certified_contour_weil_probe.py` and `research/2026-10-14/CERTIFIED_CONTOUR_WEIL_RECEIPT.json`. The frozen receipt intentionally says **SOURCE_CONDITIONAL**, even when remote source authentication separately succeeds.
- CI: dedicated Python 3.10 and 3.13 lanes run all tests, frozen receipt replay, then **mandatory** `--authenticate-parent` verifying the immutable PR #78 source and recomputing original wide contour; provenance checker follows.

**Local execution:** isolated Python 3.13 exact-rational tests 26 methods, 22 PASS and 4 SKIP because the full upstream Git-backed receipt is not mounted in this workspace; local witness/probe replay both pass. The dedicated GitHub workflow is required to replace these skips with actual authenticated mathematical source checks. No Lean proof of the new theorems is asserted. No unknown zero locations are read or supplied. Scholarly priority unverified, mathematics classical and new-to-SUCC implementation only. RH PROVED: NO.

**Primary background:** Suzuki, *Weil's quadratic form via the screw function* (2026), arXiv:2606.09096; Suzuki (2023/2025) completed Weil explicit formula; Trudgian (2014), explicit Riemann–von Mangoldt zero counts; PR #78 source derivations. Finite argument principle/Rouché and Gaussian moment bounds are classical. Any future claim of a substantially enlarged zero-free disk must be compared against the existing literature, which already verifies many low zeta zeros.

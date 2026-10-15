# TATE × SUZUKI × META-SUCC — one source, an actual zero-shift range theorem, and a finite residual-sign gate

**Date:** 2026-10-15. **Source parent:** `femboy2112/SUCC/main@03db44203147a7b28d445bb9f970fa71360e78c4` (Phoenix II). **Branch:** `research/tate-suzuki-zero-shift-source-range-2026-10-15`. **RH PROVED: NO.** No zero coordinates, fabricated Euler places, independent Gamma replacements, physical source experiments, or Connes trace realization are mathematical inputs. Independent theorem priority **UNVERIFIED**. General analysis is proved below; the Python module implements finite exact witnesses and explicitly does *not* prove functional inequalities by testing finitely many matrices.

## 0. The actual audit and mathematical goal

SUCC has complete signed Weil sources (PR #71), correct finite-interval Suzuki continuous screw kernel (PR #85), genuine first-prime positive moment-null sector at `a=1/2` (PR #86), the 30-mode Legendre split and true-positive Gamma Loewner tail (PR #96), the **zero-shift Douglas-range obstruction** (PR #99), Zeno proof debts (PR #98), and a still-separate Hilbert-curve grid instrument (PR #102). The rigorous point of this campaign is to **close a necessary zero-shift operator-domain gate** with the actual original-source regularity, then produce a sound unshifted finite matrix criterion. NOT to add yet another arbitrary positive object. The mathematically honest "one last thing" would still require a sharp source-certified sign for that matrix *and* all compact radii; those assertions are not made here.

**Source and source-meaning:** `source_weil_hierarchy.py` Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178` is preserved byte-for-byte. The integrated adapter checks exactly that blob and its true prime-power tape, not just a dataclass flag. The correct completed Suzuki/Weil source is imported as a *classical identity* from Suzuki and the existing SUCC dossiers, rather than re-proved by a finite simulator.

## 1. Tate's local arithmetic normalizations and the common analytic object (TS-01–03)

For the field `Q`, use the real test Gaussian `φ_∞(x)=exp(-πx²)` and for every genuine prime `p` use `φ_p=1_{Z_p}`. Normalize multiplicative Haar so that `vol(Z_p^×)=1`. Then for `Re(s)>0`,

\[
 Z_\infty(s)=\int_\mathbb R e^{-\pi x^2}|x|^{s-1}dx
 =\pi^{-s/2}\Gamma(s/2)=:\Gamma_\mathbb R(s),
 \qquad Z_p(s)=\sum_{k=0}^\infty p^{-ks}=\frac1{1-p^{-s}}.
\]

Both equalities follow by the Gaussian substitution and disjoint valuation shells `p^k Z_p^×`. **One real place means one Gamma factor, not a Gamma per prime.** The infinite Euler assembly `∏_p Z_p(s)=ζ(s)` is absolutely justified only for `Re(s)>1`, and the theta/Poisson continuation to other s is an independent classical theorem. The self-dual real additive measure is Lebesgue; all p-local multiplicative measures are scaled from additive Haar as above. A primitive Dirichlet character with conductor/odd parity is a DIFFERENT source and is rejected by the ordinary-zeta source passport, not silently interpreted as a positive-zeta place.

For `Re(s)>1`, unique factorization and logarithmic differentiation give

\[
 -\frac{\zeta'(s)}{\zeta(s)}=\sum_{n=p^k\ge2}\frac{\log p}{n^s}.
\]

Completion uses

\[
 \xi(s)=\frac12s(s-1)\Gamma_\mathbb R(s)\zeta(s),\qquad
 \boxed{2\frac{\xi'(s)}{\xi(s)}=\frac2s+\frac2{s-1}
 +\psi(s/2)-\log\pi-2\sum_{n=p^k}\frac{\log p}{n^s}.}
\]

The boxed equality is initially asserted **on `Re(s)>1`** (away from singularities). Continuation/distributional Fourier transport produces the true signed Weil functional on the compact smooth test space using the classical explicit formula, not termwise continuation of divergent Euler products. It fixes **the prime-power weights, half-density, one Gamma, two poles, and contact scalar**. Any Connes/Consani trace interpretation is a *different representation problem* requiring an actual source-identified map to this functional. Prior SUCC PR #88 proves a pure-point/continuous-spectrum obstacle to a naive bounded translation intertwiner from an additive solenoid; we do not substitute one.

`TateSourcePassport` rejects fake primitive composite 6, doubled Γ, conductor/parity shift, wrong half-density, wrong Gaussian scale and assertion that a trace identification has been established. The exact rational shell sum/tail and formal prime-power coefficient tape are implemented. These are finite elementary **checks**, not a new proof of adelic Poisson summation.

**Primary mathematical literature:** Tate's thesis, e.g. Dongryul Kim's detailed lecture note <https://web.stanford.edu/~dkim04/blog/tate-thesis-1/>; R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proc. AMS **17** (1966), 413–415, DOI <https://doi.org/10.1090/S0002-9939-1966-0203464-1>; M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026), <https://arxiv.org/html/2606.09096v3>; Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771; Connes–Consani–Marcolli, *The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392. All global Tate/Weil/Connes results are classified CLASSICAL/IMPORTED here.

## 2. The real source Suzuki operator and the precise Sobolev geometry

On `I=(-a,a)` let `H=L²_0(I)`, the mean-zero real or complex Hilbert space, and let `V:H→H¹_0(I)` be the integration map `Vu(x)=∫_{-a}^x u(t)dt`. Define the positive compact `K=V*V`, exactly the inverse **Neumann** Laplacian on mean-zero `H` (not the arbitrary compact screw operator). Write `P_0` for the mean-zero projection. The authentic Suzuki compact signed operator is

\[
 G_a=P_0\big[u\mapsto\int_{-a}^a g(|x-y|)u(y)dy\big]P_0,
\]

with source-fixed even screw function, for `r≥0`,

\[
 \boxed{g(r)=-4(e^{r/2}+e^{-r/2}-2)
 +\sum_{n=p^k\le e^r}\frac{\log p}{\sqrt{p^k}}(r-\log n)
 +\frac{C_G r}{2}
 -4\sum_{j\ge0}\frac{1-e^{-(4j+1)r/2}}{(4j+1)^2},}
\]

where `C_G=γ+π/2+3log2+logπ`, with **one** Gamma. The classical identification `Q_W(v)=⟨G_a i v',i v'⟩` holds for `v∈C_c∞(I)` and extends with its stated norm topology; its sign is not assumed.

**Live special radius.** Take `a=1/2`, so `0≤r≤1` and only the **genuine prime power n=2** appears. The previous `AMW-06B` original-source theorem (taken as an explicit mathematical dependency, audited in the cited SUCC dossier) states

\[
 Q_W(v)\ge\kappa\|v\|_2^2,
 \quad \kappa=369/10000,
 \quad \int_{-1/2}^{1/2}x^jv(x)dx=0\ (0≤j≤29).
\]

Under `u=i v'`, integration by parts transports this to `D=P_H G P_H ≥ κ K_H`, where `P_L` is orthogonal projection onto the 30 genuine mean-zero Legendre modes `P_k(2x)`, `1≤k≤30`; `P_H=I_H-P_L`, and `K_H=P_H K P_H`. This is **relative positivity**. The compact `D` is not bounded below by `κ I`, and its inverse can be unbounded. This distinction is essential.

## 3. SOURCE DERIVATIVE THEOREM — first-prime g belongs to W^{1,1} (TS-04)

**Theorem.** The exact source `g` above has a weak derivative in `L¹(-1,1)` with

\[
 \boxed{\|g'\|_{L¹(-1,1)}<26.}
\]

**Proof.** For positive `0<r<1` away from the true prime activation time `log 2`, ordinary differentiation of the absolutely convergent source series gives

\[
 g'(r)=-2(e^{r/2}-e^{-r/2})+rac{\log2}{\sqrt2}\mathbf1_{r>\log2}
 +\frac{C_G}{2}-2\sum_{j\ge0}\frac{e^{-(4j+1)r/2}}{4j+1}.
\]

The expression extends as an `L¹` weak derivative through the prime kink and the integrable Gamma singularity at `r=0`; `g` itself is continuous. The explicit elementary source bounds `e^{1/2}<2`, `e^{-1/2}>1/2`, `log2/sqrt2<1`, `C_G<8` yield, integrated over `0<r<1`, a combined pole+prime+contact contribution **strictly less than 8**. The positive Gamma derivative absolute integral, by Tonelli,

\[
 \int_0^1 2\sum_{j≥0}\frac{e^{-(4j+1)r/2}}{4j+1}dr
 =4\sum_{j≥0}\frac{1-e^{-(4j+1)/2}}{(4j+1)^2}
 <4\Big(1+\int_0^\infty\frac{dx}{(4x+1)^2}\Big)=5.
\]

The derivative is odd on the two sides of the even `g`, so `||g'||_L1(-1,1)<2(8+5)=26`. The small-r series may diverge pointwise at exactly zero; its **integrated weak derivative is controlled**, without postulating a finite-rate bath. QED.

By Young's inequality applied to the truncated difference kernel and zero extensions, `G_a:L²_0(I)→H¹(I)` is bounded at the first-prime radius. Projection onto the finite polynomial low space preserves `H¹`. Therefore

\[
 \boxed{P_H G_a (H)\subset H¹(I)\cap H_H.}
\]

This assertion belongs to the **true** signed operator, not to an unrelated positive covariance or a fitted numerical matrix.

## 4. THE ZERO-SHIFT RANGE GATE IS DISCHARGED (TS-05)

**Theorem (conditional on the authentic AMW high inequality).** For the genuine first-prime `G`, let `L=span{P_1(2x),...,P_30(2x)}`, `H_H=L^⊥∩L²_0`, and set

\[
 A=P_LGP_L,\quad B=P_LGP_H,\quad D=P_HGP_H\succeq\kappa K_H.
\]

Then **for every** `x∈L`, the true cross vector `b_x=B*x=P_HGx` is in `Ran(D^{1/2})`. Moreover

\[
 \boxed{R_0(x):=\lim_{\lambda↓0}\langle b_x,(D+\lambda I)^{-1}b_x\rangle
 \le\frac1\kappa\|b_x'\|_2^2<\infty.}
\]

**Proof with the correct compact topology.** The Neumann inverse `K=(-Δ_N)^{-1}` satisfies, for mean-zero `f∈H¹(I)` and arbitrary `h∈H`,

\[
 |\langle f,h\rangle|\le\|f'\|_2\langle Kh,h\rangle^{1/2}.
\]

This is Cauchy–Schwarz in the Neumann eigenbasis: write `⟨f,h⟩=⟨(-Δ_N)^{1/2}f,(-Δ_N)^{-1/2}h⟩`. For `h∈H_H`, `⟨Kh,h⟩=⟨K_Hh,h⟩≤κ^{-1}⟨Dh,h⟩`. Thus

\[
 |\langle b_x,h\rangle|\le\kappa^{-1/2}\|b_x'\|_2\langle Dh,h\rangle^{1/2}.
\]

By the Hilbert-space range/factorization theorem (Douglas 1966), equivalently boundedness of the functional on `Ran(D^{1/2})`, this implies `b_x∈Ran(D^{1/2})` and the stated bound on the inverse-root energy. The spectral theorem identifies that energy with `lim_{λ↓0}⟨b_x,(D+λI)^{-1}b_x⟩`. **No spectral gap** `D≥cI` has been introduced. QED.

**Verdict:** The *range-inclusion condition* of consolidated PR #99's zero-shift theorem is now proved for the authentic first-prime operator **assuming the existing, independently proved AMW-06B inequality and Suzuki source identification**. This is stronger than a conditional declaration of the range. It does NOT prove the second zero-shift requirement `A−R_0⪰0`.

## 5. ACTUAL ZERO-SHIFT RESIDUAL CERTIFICATE — no λ→0 blowup (TS-06)

Let any finite-dimensional linear trial map `Z:L→H_H∩H¹(I)` be chosen and put for `x∈L`

\[
 h_x=x-Zx,\quad r_x=P_HG h_x=B*x-DZx.
\]

For every high component `y`, write `y=-Zx+t`. Expanding the *original signed form*,

\[
 \langle G(x+y),x+y\rangle
 =\langle Gh_x,h_x\rangle+2\operatorname{Re}\langle r_x,t\rangle+\langle Dt,t\rangle.
\]

The preceding derivative control (applied to `r_x`) and completion of the square give

\[
 \boxed{\langle G(x+y),x+y\rangle
 \ge \langle Gh_x,h_x\rangle-\kappa^{-1}\|r_x'\|_2^2.}\tag{TS-R}
\]

**Exact 30×30 implication.** Choose true low basis `e_i` and true high smooth trial vectors `z_i=Ze_i`. Define

\[
 M_{ij}=\langle G(e_i-z_i),e_j-z_j\rangle,\qquad
 E_{ij}=\langle[P_HG(e_i-z_i)]',[P_HG(e_j-z_j)]'\rangle.
\]

Then the **real, source-identified sufficient condition**

\[
 \boxed{M-\kappa^{-1}E\succeq0\ \Longrightarrow\ G\succeq0
 \text{ on all of }L²_0(-1/2,1/2).}
\]

holds for every genuine tested vector, including all infinite high directions, with no shifted resolvent or artificial uniform L² gap. This is a mathematically finite **matrix-sign obligation**, not a claim that the actual matrix has yet been computed or shown PSD. It is conservative: failure of this sufficient condition proves nothing about the actual signed Weil form.

The exact rational `synthetic_residual_schur` implementation verifies the finite algebra on declared rational toy blocks `A,B,D,K,Z`, refuses `D<κK` and source impostors, handles semidefinite pivots, and returns *exact negative vectors* when a proposed rational sufficient matrix is indefinite. This toy checker does **not** claim the matrices are from true `G`. Constructing the actual `M,E` with rigorous transcendental source intervals is the outstanding **computational/source-identification task**.

## 6. ZENO SOURCE DERIVATIVE DEBT: explicit all-J certificate (TS-07)

With `d=4J+1`, let `g_J` truncate **only** the real Gamma rungs in the exact signed `g`, preserving the original prime-2 hinge, one contact, and both completed poles. Differentiating and integrating the omitted positive exponentials gives

\[
 \|(g-g_J)'\|_{L¹(-1,1)}\le 8\sum_{j\ge J}\frac1{(4j+1)^2}
 \le \boxed{\frac2d+\frac8{d^2}}=:\eta_J.
\]

Likewise `||g−g_J||_L¹(-1,1)≤η_J`. For the true normalized Legendre low modes, the exact squared Hilbert–Schmidt norm of the low-projection derivative is

\[
 \sum_{k=1}^{30}\|\phi_k'\|_2^2
 =\sum_{k=1}^{30}2(2k+1)k(k+1)=922560<961^2.
\]

Thus, at the actual first-prime a=1/2 source, the projection `P_H` satisfies

\[
 \|(P_H f)'\|_2\le\|f'\|_2+961\|f\|_2,
\]

and the authentic Gamma truncation is **uniform in the derivative topology**:

\[
 \boxed{\|[P_H(G-G_J)w]'\|_2\le 962\eta_J\|w\|_2.}\tag{TS-D}
\]

For the trial residual `r_x` of §5, `r_{J,x}=P_HG_J(x-Zx)` obeys this with `w=x-Zx`. Consequently, the Cauchy-bound

\[
 \|r_x'\|_2\le\|r_{J,x}'\|_2+962\eta_J\|x-Zx\|_2
\]

is a **finite-J, all-trial-source** passage from authentic Gamma truncations to the derivative residual needed for unshifted shorting. Squaring with `(u+v)^2≤2u²+2v²` yields an explicit upper Gram matrix from a rigorously enclosed finite-rung derivative Gram and low/high trial Gram. The numerical conditioning constant `962` is conservative and may be useless at small J, but it is an unconditional, computable, source-preserving error modulus; it tends to zero as J→∞ and has no forbidden `1/λ` factor. What remains is an actual source-integrated (not fitted) finite derivative Gram and its sign comparison with `M`.

**Sharp asymmetry:** the omitted original Gamma rungs are positive for the *quadratic sign form* (PR #85); however, when certifying the derivative `H¹` geometry we bound their absolute errors using `η_J`. The two operator topologies and their costs are distinct.

## 7. Hilbert curve / cube — the right finite coverage lemma (TS-08)

SUCC PR #102 provides finite Hilbert address order on 2D grids and a compact Hilbert-cube characterization. A *quadratic* form vanishes at the origin even if it is positive definite: an additive grid error bound on the **entire cube including zero** cannot certify strict PSD from positive samples when the minimum is exactly zero. Our exact negative control reproduces this trap.

**Repair:** for finite `2×2` symmetric rational block, restrict coverage to the normalized boundary `||x||_∞=1`. A Hilbert-order traversal visits every point on the dyadic boundary grid of `n=2^m` nodes per axis with mesh `h=2/(n−1)`. Every normalized direction lies within `h/2` (in Euclidean norm) of a grid boundary direction. With `L=max_iΣ_j|A_ij|`,

\[
 |x^TAx-z^TAz|\le L\,h(2+h).
\]

Thus `min_boundary_grid x^TAx > Lh(2+h)` rigorously implies `A≻0` by homogeneity. The pure exact-rational implementation verifies traversal adjacency and completeness and never promotes inconclusive scans to `A⪰0`. For the real 30×30 low Schur, either an exact rational LDL or a **product of Hilbert address pairs / higher-dimensional covering schedule** with quantified dimension cost would be required. No one-dimensional positive-Hölder surjection onto the full infinite Hilbert cube is claimed; no Hilbert scan makes a source matrix available without the original arithmetic evaluations.

## 8. Hostile probes and what DOES NOT follow

1. **Source mutation:** a fake primitive `n=6` jet, weight shift, incorrect Γ multiplicity, character `χ4` conductor/parity, wrong Gaussian measure or half-density fails the Tate passport; even a correct-looking rational matrix never self-authorizes original-source status.
2. **Range no-go:** on ℓ², `D=K=diag(n^-2)`, `b_n=n^-1` lies in ℓ² but not `Ran(D^1/2)` and `R_λ→∞`. By contrast `b_n=n^-2` is `H¹` in the model and has `R_0=Σn^-2<∞`. Finite reproductions show the difference. This is a **generic** operator-theory negative control; it is not the signed zeta operator.
3. **No fake L² gap:** `D≥κK` with compact injective K does not imply `D≥cI`; a fictitious unshifted bounded inverse is not licensed.
4. **No automatic sign:** authentic `H¹` smoothing and finite `R_0` prove the *range*, not `A−R_0≥0`. A synthetic strictly positive full block may still fail the conservative `M−κ^-1E` test; failure is `UNRESOLVED`.
5. **No fake Connes equivalence:** positive traces from auxiliary A5, Hilbert cubes, compact additive solenoids or generic Gaussian covariances are not source-identified signed Weil trace forms. Connes offers a different cohomological/semilocal route requiring its own localization, trace, and sign proof.
6. **No physical supertask:** finite Γ truncation/rational grid proof outputs are mathematical certificates, not infinitely many performed events.
7. **No zero-reading input:** the source passport and analytic g derivative use only real Gaussian, original genuine finite primes, Gamma and pole law. Published Weil/Suzuki results are proof assumptions; no nontrivial zeta zero coordinates enter construction.

## 9. Reviewable next steps, in dependency order

**R1 (completed here).** Preserve immutable original arithmetic source with Tate's one-real-Gamma and true Euler; establish first-prime `g∈W¹,¹`, source-relative unshifted Douglas-range inclusion, and a verified all-test derivative-residual Schur theorem. Reject the compact-L²-gap shortcut. **The range gate of PR #99 is discharged at the certified a=1/2 radius, conditional on PR #86's high positivity.**

**R2 (highest value).** Extend the direct genuine Legendre source interval evaluator from PR #96 (`observational_succ/suzuki_legendre_source.py`) to derivative Gram entries of `P_H G_J (e_i−z_i)`, with true prime hinge and contact. Use an adaptive source-conditional trial family `z_i`, rational interval enclosure, and TS-D truncation. Emit `M−κ^-1E` as a concrete `30×30` interval matrix and a rigorous **YES / NEGATIVE-WITNESS / UNRESOLVED** decision. "NEGATIVE-WITNESS" needs an original negative Rayleigh calculation with signed source, not failure of our sufficient test.

**R3.** Independently compare the derivative oracle with the Weil explicit formula on compact smooth tests (not numerical values of unknown zeta zeros); inspect Tate real-place measure/contact normalization and exactly one Gamma at every scale. Hold out fake 6, wrong χ4, wrong half-density and deliberately mismatched source time.

**R4.** Optimize the low/high trial map `Z` by source Legendre equations with *rigorous* residual controls, not finite floating-point fitting. Use Hilbert/Zeno coverage only for certified finite parameter search and label its exponential-dimensional cost. If a valid source lower matrix becomes PSD for first radius, extend over rational radius covers and all genuine prime wavefronts; the full forall-a gate remains as hard as RH until discharged.

**R5 (Connes alternate).** Construct a specifically typed, test-space-correct trace-functional morphism from Connes' semilocal/cyclic representation to the original signed Weil pairing. Prove equality on an entire dense source-compatible test algebra with analytic continuity. Do not replace it with positive covariance or claim a bounded additive-solenoid→real-translation intertwiner; PR #88 refutes the naive latter map.

### Claim status

- TS-01/03 original-local/Gamma arithmetic: **CLASSICAL / RECONSTRUCTED**, verified in exact finite p-shell tests and pinned source adapter; full adelic Poisson not re-proved in this branch.
- TS-04 `W¹,¹` at first prime and `<26` bound: **PROVED LOCAL analytical theorem**, contingent only on authentic Suzuki g formula.
- TS-05 range gate: **PROVED CONDITIONAL ON already recorded AMW-06B high-sector inequality**; no unsourced `D^-1` bound.
- TS-06 exact residual 30×30 sufficient inequality: **PROVED GENERAL and SOURCE-IDENTIFIED CONSTRUCTION**, actual analytic Gram values still **UNVERIFIED**.
- TS-07 derivative-tail `O(J^-1)` bound: **PROVED LOCAL**, conservative.
- TS-08 Hilbert normalized-boundary finite coverage: **CLASSICAL/PROVED LOCAL**, only 2D finite rational checker.
- **RH PROVED: NO.** First-window sign, zero-shift 30×30 authentic shorted matrix, all interval radii, and independent Connes trace identification remain OPEN.

## 10. SECOND ROUND: actual original-source Legendre derivative integrator (TS-13)

The first checkpoint gave the true-source *abstract* differentiability and range gate; the second checkpoint begins constructing the missing **source derivative Gram** rather than only describing it. The new function `authentic_suzuki_legendre_derivative_point(k,x,J)` returns an outward `Fraction` interval enclosing the derivative of the **genuine original** Gamma-`J` screw operator on `P_k(2y)` at rational `x∈(-1/2,1/2)`, with initial fixed budget `k≤4,J≤20`. It invokes the immutable SHA-checked source, imported exact polynomial/exponential Legendre primitives, and source-validated intervals for `log2`, inverse sqrt2, the real Gamma scalar, and all completed pole channels. A scalar *pointwise* derivative is not the squared source Gram `E` and has no sign authority over the full Weil form.

For an exact rational polynomial `p(y)=P_k(2y)`, let `F_p(x)=∫_{-a}^x p(y)dy` (with `F_p(a)=0` for `k≥1`), and define genuine signed exponential moments `I_±=∫_{-a}^a e^{±y/2}p(y)dy`. Then the original two-pole derivative is

\[
 \mathcal P'_p(x)=-2e^{x/2}I_-+2e^{-x/2}I_+,
\]

and the source contact derivative is exactly `C_G F_p(x)`. At the first prime, `b=log2` and `w=log2/sqrt2`, its hinge derivative is the **piecewise original-source** expression

\[
 \mathcal H'_p(x)=w\Big(\mathbf 1_{x-b>-a}F_p(x-b)
       +\mathbf 1_{x+b<a}F_p(x+b)\Big).
\]

No derivative of an invented primitive `6` is allowed. For each real Gamma rung `d=4j+1`, `α=d/2`, take finite exact polynomials `F_±^{(α)}` satisfying `d(e^{±αy}F_±^{(α)}(y))/dy=e^{±αy}p(y)`. The differentiated convolution rung is precisely

\[
 \mathcal G'_{j,p}(x)=\frac{-2}{d}\big[ F_+^{(α)}(x)+F_-^{(α)}(x)
 -e^{-α(x+a)}F_+^{(α)}(-a)
 -e^{-α(a-x)}F_-^{(α)}(a)\big].
\]

All terms are rational polynomials in `x` and `a` plus exponentials of *nonnegative rational arguments* and the authenticated coefficients `b,w,C_G`. Their signs are retained. The source evaluator uses **outward rational exponential/log intervals** from `suzuki_legendre_source`, never machine floating point, and rejects any input whose rational point falls inside an unresolved source prime activation boundary. Summing `\mathcal P'+C_G F_p+\mathcal H'+Σ_{j<J}\mathcal G'_j` gives a genuine source-conditional interval for `∂_x[G_J P_k](x)`.

**Independent calibration (not proof).** Direct 60-decimal-place mpmath integration of the independently written source derivative `g'_J(|x-y|)sgn(x-y)P_k(2y)` split at `y=x,x±log2` agrees with the independently written analytic moments to better than `4×10^-61` on `(k,x,J)=(1,0,3),(1,1/4,3),(2,0,3),(2,1/4,3)`. The observed values are approximately `−0.039823248419503`, `−0.0152680314638903`, `0`, and `−0.0303078671182131` respectively. They merely motivate the **rational strict source intervals** tested on the real GitHub checkout:

\[
 -1/50< (G_3P_1)'(1/4)<-1/100,\qquad
 -1/25< (G_3P_2)'(1/4)<-1/40.
\]

The exact source-first CI must verify these numerical-looking *rational inequalities* through the actual source intervals and fail if it cannot. The `P_2` derivative at zero is zero by reflection; the interval implementation must contain zero. No low-sector signed eigenvalue, nor any original unshifted Schur sign, follows from these point tests.

**Actual next source step:** use the same polynomial/exponential piecewise structure to integrate products of the *high-projected derivatives* over the full interval, with exact breakpoints at `±(a−log2)`. Pair this finite-J Gram enclosure with TS-D to produce the genuine `E` matrix, then evaluate its source-certified shorted sign jointly with `M` for optimized high trials `Z`. Simply sampling the derivative at many Hilbert curve points without a uniform source envelope is not a proof of its `L²` norm.

## 11. THIRD ROUND: all-test **actual** derivative energy enclosure via variation and finite source addresses (TS-14)

The pointwise original-source derivative in §10 now extends to a **rigorously enclosed integral** of its square for low Legendre inputs, without guessing the interpolation error from samples. For `J<∞`, `g_J''` is a finite signed measure in the distributional sense on `(-1,1)`:

\[
 g_J''(t)=-(e^{t/2}+e^{-t/2})+
 \sum_{j=0}^{J-1}e^{-(4j+1)|t|/2}
 +\Big(C_G-4\sum_{j<J}\frac1{4j+1}\Big)\delta_0
 +\frac{\log2}{\sqrt2}(\delta_{\log2}+\delta_{-\log2}).
\]

The bound uses *only* the authentic pole, prime, contact and Gamma terms: `∫_-1^1(e^{t/2}+e^{-t/2})dt<6`, `C_G<8`, `2log2/sqrt2<2`, and `∫_-1^1 e^{-d|t|/2}dt≤4/d`. Thus the total variation admits the **rational all-J** estimate

\[
 \boxed{\|g_J''\|_{\mathrm{TV}(-1,1)}
 <V_J:=16+8\sum_{j=0}^{J-1}\frac1{4j+1}.}
\]

For `p(x)=P_k(2x)1_{(-1/2,1/2)}(x)`, the full-line zero extension is bounded by its *explicit rational polynomial coefficient* norm `Q_k=sum_i|p_i|2^-i` (`Q_1=1,Q_2=2,Q_3=4,Q_4=17/2`). Distributional convolution gives a whole-interval Lipschitz bound on the genuine derivative

\[
 \operatorname{Lip}[(G_Jp)']\le V_J Q_k.
\]

Take the finite exact mesh of `N` equal cells of length `h=1/N`, with rational midpoint `x_i`. Let `[\ell_i,u_i]` be an outward **authentic-source** interval for `(G_Jp)'(x_i)` from §10. Every point of that cell is contained in the (rational) interval `[\ell_i−V_JQ_kh/2,u_i+V_JQ_kh/2]`. The exact rational per-cell minima and maxima of `|·|²`, multiplied by `h` and summed, therefore give **a legitimate two-sided whole-interval bound**

\[
 \boxed{L_{k,J,N}\le\int_{-1/2}^{1/2}|(G_Jp)'(x)|^2dx\le U_{k,J,N}.}
\]

This is a quantifier-complete finite-to-global Hilbert/Zeno cell certificate: the local source point values do **not** supply the global claim without the *independent source-derived variation bound*. Both original polar signs, prime-2 source kink and real Gamma remain. The current pure-rational engine supports `1≤k≤4`, `1≤J≤20`, `2≤N≤64`, with a mandatory integrated exact original-source test at `(k,J,N)=(1,3,4)`. It returns the true source form's **untruncated** derivative bound using the separately proved L¹ Gamma derivative remainder and `||P_k(2x)||²₂=1/(2k+1)`:

\[
 \boxed{\|(G P_k(2x))'\|_2^2
 \le 2U_{k,J,N}+\frac{2\eta_J^2}{2k+1},\qquad
 \eta_J=\frac2{4J+1}+\frac8{(4J+1)^2}.}
\]

This uses the elementary inequality `(u+v)²≤2u²+2v²`; it is conservative and can be loose. It is already a **genuine source-derived whole-test-functional analytic** bound for one low mode rather than a pointwise sample. It does **not** yet bound `||(P_HG P_k)'||²`: obtaining the necessary source-projected 30-dimensional derivative Gram requires combining these exact derivative cell envelopes with source-interval projection coefficients (the source low Legendre blocks), and then canceling the polynomial low component *before* squaring/integrating. Replacing that cancellation with the global bound 961 can be astronomically wasteful. No claim of nonnegative shorted matrix or RH is made.


## 12. FOURTH ROUND: original **projected** low/high derivative-energy certificate (TS-15)

The preceding round certified the whole-interval derivative energy of the
**unprojected** authentic source vector `G_J P_k`. This round executes the
missing finite-dimensional projection and proves a whole-interval bound on
`(P_high G_J P_k)'` in **the actual 30-moment Suzuki Hilbert split** at
`a=1/2`, where the high-space positivity from AMW-06B is known.

Let `p_j(x)=P_j(2x)`, `1<=j<=30`, and let
`W_j=∫_{-1/2}^{1/2}p_j(x)^2 dx=1/(2j+1)`. The authentic derivative-coordinate
orthogonal projector has the exact finite formula

\[
(P_L f)(x)=\sum_{j=1}^{30} p_j(x)
\frac{\langle p_j,f\rangle}{W_j},
\quad P_H=I-P_L.
\]

For the **actual signed original-source** truncated operator `G_J`, set
`c_{jk,J}=(2j+1)\langle p_j,G_J p_k\rangle`. Every coefficient uses the
existing independently authored SHA-pinned original-source direct Legendre
interval evaluator `suzuki_legendre_source.authentic_full_low_entry`, *not* a
synthetic Gram or a fitted Fourier model. The original source includes genuine
prime 2, its actual log2/sqrt2 half-density weight, one completed real Gamma,
`C_G` contact, and both completed polar contributions. Parity forces
`c_{jk,J}=0` if `j+k` is odd. Hence

\[
 r_{k,J}'(x)
 =[(P_H G_J p_k)]'(x)
 =(G_J p_k)'(x)-\sum_{j=1}^{30}c_{jk,J}p_j'(x).
\tag{TS-15a}
\]

For `x ∈ [-1/2,1/2]`, the classical Markov polynomial bound on the unit
interval gives `sup|p_j''(x)| <= 4 j^4`. If the original-source certified
coefficient interval is `c_{jk,J}∈[c^-_{jk,J},c^+_{jk,J}]`, the actual
projected derivative has the *source-certified whole-interval Lipschitz*
constant

\[
L_{k,J}^{proj}=
 V_J Q_k+
 4\sum_{j=1}^{30}j^4
 \max(|c^-_{jk,J}|,|c^+_{jk,J}|),
\quad V_J=16+8\sum_{j<J}(4j+1)^{-1}.
\tag{TS-15b}
\]

At each rational midpoint `x_i` of one of `N` equal cells, compute both
original-source intervals in (TS-15a); subtract **all 30 source Legendre
projections first**, and widen by `L^{proj}/(2N)` before squaring. Summing
certifies finite rational numbers `0<=L^{proj}_{k,J,N}<=U^{proj}_{k,J,N}` such that

\[
 \boxed{L^{proj}_{k,J,N}
 \le\big\| [(P_HG_Jp_k)]'\big\|_{L^2}^2
 \le U^{proj}_{k,J,N}.}
\tag{TS-15c}
\]

Since the **source-positive original Gamma tail** obeys the previously
proved projected derivative operator estimate
`||(P_H(G-G_J)p_k)'||_2 <=962 η_J ||p_k||_2`, with
`η_J=2/(4J+1)+8/(4J+1)^2` and `||p_k||²=1/(2k+1)`, the full authentic
Suzuki operator obeys

\[
 \boxed{\big\| [(P_HG p_k)]'\big\|_{L^2}^2
 \le2U^{proj}_{k,J,N}+
  \frac{2(962\eta_J)^2}{2k+1}.}
\tag{TS-15d}
\]

**What this actually discharges:** a properly **projected diagonal** cross
energy bound, for an original source low mode and its exact codimension-30
high counterpart. This is a stronger mathematical input to the unshifted
residual Schur calculus than TS-14. The executable source research budget is
currently `1<=k<=4`, `1<=J<=20`, `2<=N<=16`, exactly 30 source Legendre modes.
The new source-adapter test executes `(k,J,N)=(1,3,2)` against the actual
original SUCC source, rather than accepting a synthetic matrix as an
arithmetic certificate. All arithmetic intervals are exact Fractions.

**What still remains RH-hard:** (i) extend diagonal and offdiagonal energy
bounds to every one of the thirty true source low modes; (ii) exploit genuine
cancellation to produce *numerically useful* complete cross-residual Gram
`E_{ij}=<[(P_HG p_i)]',[(P_HG p_j)]'>`, retaining correct operator and domain;
(iii) independently enclose the true low signed matrix `M` sufficiently
sharply that an authenticated unshifted Schur sign can be decided;
(iv) carry this fixed-interval method to **all radii** with independently
proved relative high positivity. The newly bounded diagonal here does not
establish positivity of any original unshifted Schur matrix, and cannot be
promoted into an RH theorem without those additional results.

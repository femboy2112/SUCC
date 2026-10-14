# THETA-JETS — authentic SUCC even Taylor shadows, Gaussian bounds and the Plato cave

**Checkpoint:** October 14, 2026. **Source parent:** SUCC PR #74 (`research/succ-gaussian-global-constraint-2026-10-14`) at exact commit `6c9e1cb1d6bac0acb7ce38890ede6390881a2202`; this itself descends from all-place source-interaction PR #73 and the signed completed-Weil PR #71. **Sibling, not imported:** IdealHard Weil-sign PR #75 `a6221339`. **Branch:** `research/xi-theta-certified-jets-cave-2026-10-14`. **RH PROVED: NO.** No nontrivial zero positions, zero-count oracles, physical borehole measurements, or imported whole-space Weil positivity enter the construction. `main` remains unchanged.

Research question: Can a mathematical observer **construct** genuine Taylor jets of the globally completed zeta from source-indexed finite integer/Gaussian theta observations, attach fully rational omitted-data costs, and prove analytic zero-divisor restrictions? If yes, how much of the global object do the observed shadows identify, and which original-source interactions must be supplied to escape those ambiguities? Every claim below states its mathematical domain; the methods are classical theta/Poisson, positive-moment, Hilbert, and Rouché theory applied as a new-to-SUCC source-typed interface. Independent academic novelty is UNVERIFIED.

## TJ-01. Exact even jets from ONE authenticated theta source (CLASSICAL/PROVED LOCAL)

The parent (source-interaction PRs #72/#73) established from the integer source, the unique self-Fourier real Gaussian, Poisson summation, and the one-Gamma Mellin gate that

\[
\xi(s)=\tfrac12+\frac{s(s-1)}2\int_1^\infty\psi(t)
\big(t^{s/2-1}+t^{(1-s)/2-1}\big)\,dt,
\quad \psi(t)=\sum_{n\ge1}e^{-\pi n^2t}.
\]

**Important:** the equality with the genuine completed Euler product is already proved on the open region `Re(s)>1` using *authentic* primes, hence extends uniquely by the identity theorem; it is NOT an equality achieved by termwise continuation of the divergent Euler product. This research does not substitute a new Gaussian test state for the original real place.

Set `F(z)=xi(1/2+z)` and

\[
B(z)=\int_1^\infty\psi(t)t^{-3/4}\cosh\big(z\log(t)/2\big)\,dt.
\]

Then `F(z)=1/2+(z²-1/4)B(z)`. On every compact complex z-set the integrand and all z-derivatives have a Gaussian-in-t majorant, so B is entire. Expanding the cosine hyperbolic and interchanging integration and sum (Tonelli for real positive z, dominated convergence for compact complex sets) gives

\[
 b_j=\frac{1}{4^j(2j)!}\int_1^\infty\psi(t)t^{-3/4}(\log t)^{2j}dt>0,
\quad B(z)=\sum_{j\ge0}b_jz^{2j}.
\]

Consequently the **original** coefficients `F(z)=sum_(j>=0) a_j z^(2j)` obey

\[
\boxed{a_0=\tfrac12-\tfrac14 b_0,\qquad
       a_j=b_{j-1}-\tfrac14b_j\quad(j\ge1).}
\]

Every `2j`th derivative at the critical center equals `(2j)!a_j`; every odd derivative vanishes from the original functional equation. No sample of the nontrivial zero set is needed. This yields an effective finite observer for any *fixed* finite jet depth. The implemented finite-budget instrument supports `j<=24`; the underlying theorem has no such cap.

## TJ-02. Rational finite-observer construction with complete missing-source bounds (PROVED LOCAL)

For finite mode cutoff N, time endpoint T>=2 and grid cells M, enclose each positive integral over `[1,T]` using products of monotone factors. If `1<=l<=t<=r`, then

\[
\psi_N(r)r^{-3/4}(\log l)^{2j}
\le \psi_N(t)t^{-3/4}(\log t)^{2j}
\le\psi_N(l)l^{-3/4}(\log r)^{2j}.
\]

The factors for `j=0` use convention `(log t)^0=1`, including t=1. All endpoint factors are bounded by **outward rational intervals**, not floating point:

* `pi=16 atan(1/5)-4 atan(1/239)` via alternating bounded arctan series;
* `log x=2 sum_(r>=0) z^(2r+1)/(2r+1)` with `z=(x-1)/(x+1)` after dyadic reduction to `[1,2]`; geometric positive tail;
* `exp(-x)` through positive Taylor series of `exp(x/2^k)` for argument <=1/2, a proved geometric Taylor-remainder bound, and repeated **outward-rounded** dyadic squaring; all arithmetic uses `fractions.Fraction`. Precision rounding is directed toward containing the true quantity.

The part with missing integer theta modes `n>N` has, for `t>=1`,

\[
0\le\psi(t)-\psi_N(t)\le2e^{-A t},\quad A=3(N+1)^2,
\]

because `pi>3` and the successive n² gaps exceed `2N+3`. Using `log(t)<=t-1` and `t^(-3/4)<=1`, the contribution to b_j is at most

\[
\boxed{U_{\rm mode}(j,N)=\frac{2e^{-A}}{4^j A^{2j+1}}.}
\]

For all n, `psi(t)<=2e^{-3t}` for t>=1. From `log(t)<=sqrt(t)`,

\[
\boxed{U_{\rm time}(j,T)=\frac{2e^{-3T}j!}{4^j(2j)!}
\sum_{k=0}^j\frac{T^k}{k!3^{j+1-k}}.}
\]

Thus **each coefficient b_j lies between two explicitly evaluable rationals**, with no excluded Gaussian mode, time tail, prime-source normalization, or endpoint singularity left unaccounted for. Arbitrarily fine rational enclosures are possible by raising mode/time/grid/precision budgets (continuity on compact `[1,T]`, and the explicit tails), although the finite software currently enforces resource caps. All true place interactions enter through the parent source identity; no `zeta` call or zero list is used in certificate construction.

The finite horizon `N=3` samples the integer theta n=1,2,3, not the first three primitive Euler places. Missing n=6 remains correctly in the **true Gaussian theta tail**, not a fake primitive place. A forged source label or coefficient table is rejected by deterministic replay of the same original mathematical source contract; **this is not cryptographic or physical authentication**.

## TJ-03. Entire-source remainder bound and certified Rouché zero count (PROVED LOCAL)

The parent theta estimates imply for all real `T_c>=0`

\[
B(T_c)\le (4/5)e^{-5/2}e^{T_c^2/8}<e^{T_c^2/8}.
\]

Sketch: `psi(t)<2e^-3t`, `t^-3/4<=1`, `log t<=sqrt t`, `cosh x<=e^|x|`, and `T_c sqrt t/2<=T_c²/8+t/2`. Since every b_j is nonnegative, for any `0<=R<T_c`,

\[
\left|B(z)-\sum_{j=0}^D b_j z^{2j}\right|
\le e^{T_c^2/8}(R/T_c)^{2(D+1)},\qquad |z|\le R.
\]

For the **true** Taylor polynomial `P_D(z)=sum_(j=0)^D a_j z^(2j)`, the exact algebraic remainder is

\[
\boxed{F(z)-P_D(z)=b_D z^{2D+2}
+(z^2-1/4)\sum_{j>D}b_jz^{2j}.}
\]

It is therefore bounded uniformly on the disk by

\[
\boxed{\mathcal R_D(R,T_c)=b_D^{\rm upper}R^{2D+2}
+(R^2+1/4)e^{T_c^2/8}(R/T_c)^{2D+2}.}
\]

**Certified worked example (not a numerical zero scan).** Set D=20, N=3, T=8, M=1536, `T_c=13`, `R=11/2`. The exhaustive rational source certificate verifies

\[
\boxed{a_0^{\rm lower}>
\sum_{j=1}^{20}\max(|a_j^{\rm lower}|,|a_j^{\rm upper}|)R^{2j}
+\mathcal R_{20}(R,13)+1/250.}
\]

In particular the right-hand strict margin is >1/250, so 

\[
\boxed{\xi(s)\ne0\quad\text{for all }|s-1/2|\le11/2.}
\]

The proof is elementary triangle inequality / Rouché against the nonzero constant `a_0`; it certifies **zero count 0**, without querying any nontrivial-zero coordinates. This is much weaker than established zero-free information, and does not imply RH. The original prior source-Gaussian construction certified only radius `47/100`; we have extended that particular *method's provable radius* to `11/2`.

The true coefficient-based analytic tail `mathcal R_20(11/2,13)<1/100000`. If finite coefficient intervals are replaced by their **rational midpoint polynomial** `P_hat`, separately summing coefficient uncertainty yields

\[
\boxed{\sup_{|z|\le11/2}|F(z)-\widehat P_{20}(z)|<1/100.}
\]

This is a true, source-certified polynomial observer **with explicit uncertainty**, not just a fitted Taylor curve or a GP credible band. The two errors (finite coefficient measurement vs true infinite Taylor remainder) are recorded separately. Every exact fraction is in the frozen receipt.

## TJ-04. The same theta source induces an entire positive Stieltjes moment structure (PROVED LOCAL / CLASSICAL)

Use `u=log t`, `t=e^u` and define a finite strictly positive source measure

\[
 d\mu(u)=\psi(e^u)e^{u/4}\,du\quad (u\ge0).
\]

Its even power moments are

\[
\boxed{m_j=4^j(2j)!b_j=\int_0^\infty u^{2j}\,d\mu(u).}
\]

After pushing µ forward by `y=u²`, this is a Stieltjes moment sequence. For every polynomial `P(y)=sum_i c_i y^i`, both

\[
\sum_{i,j}c_i\overline{c_j}m_{i+j}=\int|P(u^2)|^2d\mu\ge0,
\]
\[
\sum_{i,j}c_i\overline{c_j}m_{i+j+1}=\int u^2|P(u^2)|^2d\mu\ge0.
\]

Both Hankel matrices are in fact strictly positive definite in every finite order because the true theta density is strictly positive on an interval and a nonzero polynomial cannot vanish there. This is the classical one-variable Stieltjes moment mechanism; cf. [Stieltjes Hankel criterion](https://link.springer.com/article/10.1007/s00013-021-01599-9). We also verify strictly positive rational intervals for the leading **2x2** and shifted **2x2** determinants, independently of floating-point diagonalization.

**Finite-observer prediction, without reading the future moment:** Cauchy–Schwarz gives `m_(k+2)>=m_(k+1)^2/m_k`. Therefore the first two genuinely certified moment intervals force

\[
\boxed{m_2\ge (m_1^{\rm lower})^2/m_0^{\rm upper}>0,}
\]

without using the measured m2 in the construction of the bound. This is a concrete model-model interaction law.

Even more structurally, for real (or complex) z,w,

\[
\boxed{K_\theta(z,w)=\int\cosh(zu/2)\overline{\cosh(wu/2)}\,d\mu(u)
=\tfrac12[B(z+\bar w)+B(z-\bar w)].}
\]

It is a **genuine source-derived positive Gram kernel**, rather than an arbitrary stationary Gaussian-process covariance. Real points x,y are enclosed with positive b_j intervals and the proven B analytic tail. **Crucial firewall:** `K_theta>=0` is positivity of a theta-moment Gram; it is **NOT** completed signed Weil positivity. The χ4 odd signed theta branch is not automatically positive, and no sign is carried into Suzuki without an independent original-source/domain identification.

## TJ-05. Plato cave: exactly what the finite shadows can and cannot distinguish (PROVED LOCAL / NEGATIVE CONTROL)

The observer may obtain finitely many exact jets and observe Hankel positivity, and yet more than one *positive* source survives. Take

\[
 \mu_A=\tfrac12\delta_1+\tfrac12\delta_3,
\quad \mu_B=\tfrac45\delta_2+\tfrac15\delta_3.
\]

Both are nonnegative finite measures on u≥0, with **exactly** `m0=1,m1=5` but different `m2=41` versus `29`. Their entire positive cosh transforms have identical b0,b1 and thus their corresponding **even Xi-shaped polynomials through z² are identical**, but the z⁴ coefficients differ. Both satisfy every positive-moment/Hankel structural law. Neither is the authentic integer-theta measure, and both fail the complete original arithmetic germ.

**A sharper off-critical zero impostor with the SAME Fock budget (exact negative control).** Let `a0,a1` denote the *true*, not midpoint, first two even coefficients of original Xi; our rational intervals prove `0<a0<1/2` and `0<a1<1/50`. Put `M=20` and

\[
G(z)=(a_0+a_1z^2)\left(1+\frac{z^4}{4M^4}\right).
\]

At the explicit noncritical point `w=M(1+i)`, `w^4=-4M^4`, so G(w)=0; evenness and real coefficients give the reflected three zeros. The exact original a0 and a1 are unchanged in G's Taylor jet. Moreover, with the even Fock norm `||sum c_j z^(2j)||²=sum(2j)!|c_j|²`, the entire impostor obeys

\[
||G||_{\mathcal F}^2=a_0^2+2a_1^2+\frac{4!a_0^2+6!a_1^2}{(4M^4)^2}
< 1 <260/27.
\]

The strict rational comparison uses only the source-enclosed a0,a1. This proves **even the authentic first two exact Xi jets + evenness + the SAME certified Gaussian Fock budget** permit a false global curve with four off-critical zeros. The impostor does not satisfy the complete true theta/Euler germ, so it is a valid observational no-go, NOT a fabricated counterexample to RH. We never input, scan or assume an original nontrivial zero.

More generally, given any finite exact observation menu with norm slack, a nonzero even polynomial vanishing on all observed point/jet constraints provides another entire curve. Finite shadows do not identify the original world. By contrast, when the full authentic Euler germ on an OPEN Re(s)>1 subset and the Poisson functional source are supplied, the identity theorem does identify **one** completed global function. That distinction is the precise operational content of the Plato cave analogy: finite wall projections can constrain the unseen source, but an observational fiber may still contain multiple lawful mathematical models. A useful E must keep source/provenance and experiment realizability, not merely assign a confident probability to one silhouette.

The finite positivity test on the true source **cannot** imply RH. The sibling IdealHard-Weil PR #75 supplies the separate whole-space hidden-negative-direction counterexample. No finite set of xi jets or source-positive Hankel matrices is an identified signed Weil quadratic form.

## TJ-06. Steelman / crucible / verdict and next proof targets

1. **SURVIVES (PROVED LOCAL):** unique theta-source → computable positive b_j → certified even original Xi jets, exact rational analytic and coefficient-error tubes, local Rouché zero count; everything source-indexed and zero-independent.
2. **SURVIVES (CLASSICAL/PROVED LOCAL):** source-positive Stieltjes Hankel and theta cosh Gram; authentic finite measures show new observable constraints without importing a statistical prior.
3. **REFUTED:** `finite jets + positivity of one kernel imply unique global source` — explicit 2-measure positive moment witness. Model uniqueness requires the original Euler/theta source, not just its finite observations.
4. **NOT CLAIMED:** a general zero-free horizontal strip at all imaginary heights, physical witness of an infinite observer, compatibility with every χ parity/conductor without changed signed measures, identification of these Hankel forms with full signed Weil, or RH.

**Next truth-bearing research:** (a) certify complex contour minimum-modulus and argument-principle winding of the original Taylor polynomial with exact interval arithmetic and source remainder, potentially providing nonzero zero counts on selected bounded rectangles without querying zeros; (b) construct a source-correct transfer of theta moment Gram kernels into Suzuki's completed Weil *bilinear form* on its actual test-function domain and seek new signed domination inequalities; (c) compare χ4 odd/conductor and controlled non-Euler matched source mutations to keep the source firewall live; (d) formally verify the core rational interval and moment transformations in Lean. The high-imaginary global RH obstacle is unchanged.

## Validation and literature boundary

- `python -m unittest discover -s tests -p test_theta_taylor_jets.py -v` — **23 new local exact tests passed** on the isolated newly-authored module.
- `python scripts/theta_taylor_jets_probe.py --verify research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json` — exact deterministic replay.
- `python scripts/theta_jet_independent_oracle.py` — separate 65-digit mpmath integral and xi-value holdouts, no zeros. **Not part of proof.**
- SHA-1 `git hash-object` match for each published GitHub blob required before commit.
- No full repository checkout was available by container DNS; full local SUCC suite, newly formalized Lean proofs and scholarly priority audit are not claimed. Branch-specific remote CI must be checked on the pushed head.

Primary analytic prior art: Jacobi theta/Poisson and Mellin ([NIST DLMF §20.10](https://dlmf.nist.gov/20.10)); Stieltjes Hankel criterion and moment problems (classical; [Schmüdgen/Stieltjes reference](https://link.springer.com/article/10.1007/s00013-021-01599-9)); Bargmann–Fock RKHS (parent PR #74); Rouché's theorem and the analytic identity theorem (classical); Weil/Suzuki original source (sibling PR #71, Suzuki 2026 arXiv:2606.09096). These theorems' general mathematical content is not new; this source-typed exact reconstruction is new-to-project. **RH remains open.**

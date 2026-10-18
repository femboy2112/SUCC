# Operation BDC — Bidirectional SUCC, the arithmetic square root, and the invisible Hilbert cut

**2026-10-18 · research-only, stacked on draft SUCC PR #165 (`dea8b7f982fd3eb2361ccd5a12d360bcadfa3689`)**. RH PROVED: NO. No release/merge or original Tate/Weil/Suzuki source edits. No nontrivial zero coordinates are read. Proof-status taxonomy follows `AGENTS.md`; machine checks are only exact finite models unless a mathematical theorem is proved separately.

## 0. Objective and exact source boundary

Objective: construct two *independently typed* representations of the forward positive-integer FUCC/SUCC observations and the backward cut `1_{x>1}/x`, characterize lawful bounded functional gluing, and decide whether a positive arithmetic square root of backward modular-clock energy implies the RH-equivalent Nyman–Beurling–Báez-Duarte residual closure.

**Relevant inherited SUCC:** `unit_prime_succ.py` / #136, exact finite clocks and LCM/Von-Mangoldt #165, prime-jet forward reconstruction #157, source-limited clock constructor #162, `TATE_TO_WEIL_DISTRIBUTION.md` / CTW-08. The *actual signed* completed Weil distribution is a distinct functional; its positivity is not inherited from any new positive covariance.

**External classical theorem (separate authority):** Báez-Duarte (2002/2003), stronger Nyman–Beurling criterion: for `rho_n(t)={1/(nt)}` and `chi=1_{(0,1)}`, `RH iff chi ∈ closure_span{rho_n:n in N}` in `L²(0,∞)`. Primary: L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Rend. Lincei Mat. Appl. 14 (2003), 5–11; arXiv:math/0202141; later arXiv:math/0205003. Original normalizations are retained. Burnol's published lower bound is a further independent warning: a finite-tail period-average decay estimate is **not** the all-line Nyman residual bound.

## 1. BDC-01 (CLASSICAL, PAPER PROVED): exact reflection/forward-backward functor

Let `H=L²((0,∞),dx)` and `D_a f(x)=sqrt(a) f(ax)` for `a>0`. The map

`Jf(x)=x^(-1) f(1/x)`

is a unitary self-adjoint involution: `J²=I`, `J D_a J=D_(1/a)` (by substitution `y=1/x`). Under `Uf(t)=e^(t/2)f(e^t)` from H to L²(R), `UJU^(-1)g(t)=g(-t)`. On Mellin tests this is the reflection `M(Jf)(s)=M(f)(1-s)` in the common strip where integrals exist. **This is not zeta's completed functional equation**; its derivation does not include Gamma, residues, meromorphic continuation, or zero location.

Set forward probes `rho_n(t)={1/(nt)}` and cut `chi(t)=1_(0,1)(t)`. Their reflected names are

`g_n(x)=Jrho_n(x)={x/n}/x`, `h(x)=Jchi(x)=1_(1,∞)(x)/x`.

The original criterion becomes `RH iff h ∈ closure_span{g_n}`. `g_n` is precisely a continuous fractional clock readout; at integer k, `{k/n}=(k mod n)/n`. These observations exist as **mathematical test functions**, not automatically authenticated physical sensors. The target is a *particular* vector: equality of closures of all of H is neither required nor established.

## 2. BDC-02 (PAPER PROVED): backwards periodic error is a clock-Haar quadratic

For finite real coefficients `(c_1,...,c_N)`, write `F_c=Σ c_ng_n`. On `(0,1)` the error `h-F_c=-b`, where `b=Σ c_n/n`. On `(1,∞)` the error is `A_c(x)/x`, with

`A_c(x)=1-Σ c_n {x/n}`.

`A_c` is periodic with finite clock period `L=lcm(1,...,N)`. Denote the Haar mean `alpha(c)=(1/L)∫_0^L A_c(x)^2 dx`. Then

`alpha(c)=(1-(1/2)Σc_n)^2+(1/12)Σ_(m,n<=N)c_m c_n gcd(m,n)^2/(mn).` (BDC.1)

This is the **arithmetic square root of the normalized backward clock**, not an approximation or a random independent PSD matrix.

### Two mathematically different derivations, with shared source provenance

**(A) Fourier/Basel.** For the first periodic Bernoulli polynomial `B_1(t)={t}-1/2`, its Fourier sine coefficients are `-1/(πk)`. Orthogonality of frequencies `k/m=l/n`, with `g=gcd(m,n)`, yields

`mean B_1(x/m)B_1(x/n) = (1/(2π²))*Σ_(r>=1) g²/(mn r²) = g²/(12mn)`.

The last equality is exactly Basel's `Σr^-2=π²/6`, with the *square reciprocal* determining the covariance scale.

**(B) Independent conditional-carry derivation.** Write `x=k+u` on `[0,L)`, `u∈[0,1)`. Condition on `k mod g` and `u`. CRT makes the two remaining residue digits modulo `m/g` and `n/g` conditionally independent. The common residual position `k mod g + u` is uniform on `[0,g)`, with variance `g²/12`. Consequently the covariance of `{x/m},{x/n}` is `g²/(12mn)`. This uses actual common cyclic quotient geometry, not zero locations or the Fourier series. The two arguments are independent methods for **the same** mathematical clock source, not independent source attestations.

## 3. BDC-03 (CLASSICAL ALGEBRA, PAPER PROVED): Jordan-totient square root

`gcd(m,n)^2=Σ_(d|m,d|n) J_2(d)`, where `J_2=μ*id²` and `J_2(d)=d²∏_(p|d)(1-p^-2)>0`. Hence

`alpha(c)=(1-Σ c_n/2)^2 + (1/12)Σ_(d<=N) J_2(d) (Σ_(n<=N,d|n) c_n/n)^2.` (BDC.2)

This gives a canonical factorization through the divisor-incidence matrix. For distinct `n=1,...,N`, its GCD-square matrix `K_N=[gcd(m,n)^2/(mn)]` is strictly positive definite since the divisor matrix is unit triangular and every `J_2(d)>0`. The appearance of `p^-2` is not decoration: it enforces the positive local Jordan weights. **Signed coefficients are allowed**; the quadratic is positive in all orientations.

For complex c replace every square by an absolute square and conjugate one matrix coefficient. The code exercises exact rational *real* inputs; the complex mathematical extension is by sesquilinearity.

## 4. BDC-04 (PAPER PROVED, EXACT FINITE CHECKED): closed-form *tail-only* optimum

Let `e=(1,...,1)^T`, `K=K_N`, `S_N=e^T K^-1 e` and `d_N(c)=alpha(c)`. Differentiating the strictly convex form gives

`c*=6 K^-1 e /(1+3S_N)`, `min_c alpha(c)=1/(1+3S_N)`.

The divisor-incidence inverse (Möbius inversion) gives **an exact arithmetic evaluation**:

`S_N=Σ_(n<=N) phi(n)^2/J_2(n)`, where `phi=μ*id` is Euler's totient. (BDC.3)

Proof: `K=D^-1 E diag(J_2) E^T D^-1` for `D=diag(1,...,N)`, `E_(n,d)=1_(d|n)`. Therefore `e^T K^-1 e = ||diag(J_2^-1/2) E^-1 D e||²=Σphi(n)²/J_2(n)`.

For the optimizer, `Σ c_n/n=6/(1+3S_N)` and `Σ c_n=2(1-1/(1+3S_N))`, so its cuts satisfy the two elementary *necessary* limiting moment constraints.

**Unconditional tail-only decay:** Since `phi(n)^2/J_2(n)=∏_(p|n)(1-2/(p+1)) ≥ 1-Σ_(p|n)2/(p+1)`, summation to N gives

`S_N ≥ N (1-Σ_p 2/(p(p+1))) ≥ N/10`.

Indeed `Σ_(integer j>=2) 2/(j(j+1))=1`, while 4 is not prime and contributes `1/10`. Consequently

`min_c alpha(c) <= 1/(1+3N/10)`, hence the periodic-tail mean can be driven to zero at least as fast as `O(1/N)` **without assuming RH**. This does not touch the corresponding full-line Nyman distance.

## 5. BDC-05 (REFUTED shortcut): periodic square-root saturation is NOT Hilbert closure

The complete backwards squared error is

`||h-F_c||² = |Σ c_n/n|² + ∫_1^∞ |A_c(x)|² dx/x².` (BDC.4)

Haar averaging *erases where the error is located*; the Hilbert integral weights errors near the cut more heavily. The two optimizations are mathematically different.

**A decisive finite counterexample:** N=1 has exact periodic-tail optimizer `c_1=3/2`, `alpha(c*)=1/4`, but on `(0,1)` alone its true Hilbert error is `|c_1|²=9/4>1=||h||²`. The zero coefficient already gives a better full Hilbert trial. This kills the tempting inference `min periodic-clock energy => min completed-Hilbert residual` with no numerical approximations and no zero input.

**A rigorous tail comparator:** For any R>=1 and `L=L_N`, denote `E_R=∫_R^∞ |A_c(x)|²/x² dx`. Each length-L clock cell has unweighted energy `L alpha(c)`. Monotonicity of `x^-2` gives

`alpha(c)/(R+L) <= E_R <= alpha(c)*(1/R+L/R²)` (BDC.5).

A source-coefficient bound also gives `E_R <= (1+Σ|c_n|)²/R`. On each `[k,k+1]` for integer k>=1, the full residual is `a_k/x-b` with `a_k=1+Σ c_n floor(k/n)`; its exact integral is `a_k²/(k(k+1)) - 2a_k b log((k+1)/k) + b²`. Rational atanh-series intervals for the logarithm plus (BDC.5) yield a complete outward rational bound on any **specified finite trial**. They DO NOT certify that trial is an optimizer.

The known Burnol/Báez-Duarte all-line residual lower-bound scale is much slower, typically `d_N² ≳ c/log N` for an explicit positive constant associated with known critical-line zeros (classical external source). The `O(1/N)` periodic-clock optimization is therefore not even of the same obstruction class. We do not infer anything about ζ zeros by comparing these different functionals.

## 6. BDC-06 (CLASSICAL HILBERT, PROVED): forward innovations vs backward residual

Let `H` be a Hilbert space, `V_N=span{g_1,...,g_N}`, and `P_N` the orthogonal projection onto V_N. Put `R_N=I-P_N`, `h` the fixed target. Since V_N increase,

`||R_(N-1)h||² - ||R_N h||² = |<R_(N-1)h,w_N>|²/||w_N||² >=0`,

where `w_N=(I-P_(N-1))g_N` if `w_N ≠0`, and the increment is 0 otherwise. Therefore

`||h||²=Σ_(n=1)^N delta_n+||R_Nh||²` with `delta_n>=0` (BDC.6),

and strong projection convergence gives

`||P_(S^perp)h||²=||h||²-Σ_(n>=1)delta_n`, `S=closure_union V_N`.

In the inverted Báez-Duarte model, **RH iff the sum of actual source-target innovation energies equals 1**. This is an exact equivalence but a reformulation; it is not a proof of convergence. The Jordan/Haar tail innovations are *different* from the full-line L² innovations, as the N=1 counterexample establishes.

## 7. BDC-07 (CLASSICAL, PAPER PROVED): a bounded inverse-limit no-ghost theorem

For an increasing sequence of finite subspaces V_N of a Hilbert space, suppose linear functionals ell_N on V_N are compatible under restriction. They represent a unique continuous linear functional on `S=closure_union V_N` **if and only if** `sup_N ||ell_N|| < ∞`.

Proof: define ell on union by compatibility; the uniform bound makes it continuous, hence uniquely extends by completion. Conversely any bounded extension bounds all restrictions. Riesz represents it by one vector `v∈S`. Extensions to the larger ambient Hilbert H are nonunique when `S≠H` (all extensions differ by an element of `S^perp`).

**Mutation A:** on E_N=span(e_1,...,e_N) declare ell_N(e_j)=1. Every restriction is compatible, but ||ell_N||²=N; no bounded global functional exists. This is a true completion/access failure despite infinite algebraic compatibility.

**Mutation B:** let H=ell²({0,1,2,...}), V_N=span(e_1,...,e_N), target h=e_0. The observed functionals ell_N(v)=<h,v>=0 are compatible and uniformly bounded; however `P_(S^perp)h=h` survives with norm one. **No-ghost source adequacy of a bounded backward functional does not certify the RH-specific target-completeness condition.**

This theorem separates existence of a lawful mathematical functional, identification with an authenticated external source, and annihilation of the target residual. A provenance label alone cannot perform the second step.

## 8. BDC-08: dependency arrows and next source-discriminating probe

1. **DISCLOSED classical:** arithmetic fractional clocks, Möbius/Jordan factorization, unitary inversion, Basel covariance, finite Riesz/Hilbert innovation identities.
2. **VERIFIED exact finite model:** independent CRT cell integration vs divisor square root; 17 local tests; rational cutoff intervals (stronger than floats) and pinned deterministic JSON; source/passport mutations.
3. **CONJECTURED / UNVERIFIED:** a *new* source-derived estimate on the full-line Nyman target innovations with a summable remainder whose sum exhausts one; or a genuine cross-criterion identity with the completed signed Weil form. Neither exists here.
4. **REFUTED inference:** periodic source Gram PSD or alpha_N→0 implies full L² residual→0. We give exact N=1 and scale-separation controls. Finite tests cannot establish RH.

**Best next probe:** derive a **two-boundary gluing inequality** controlling weighted cells `x≈1,...,L_N` from authenticated finite SUCC clocks *and* the backwards modular Haar square-root, with explicit norm dependence on coefficients and a non-circular rate. Require (a) true input source and counterterm identification, (b) a constructive sequence of coefficients with a certified full `L²(dx/x²)` bound, (c) holdout beyond the fitted clock horizon, and (d) agreement with the known Burnol lower bound. This would distinguish genuine progress from another source-positive but RH-irrelevant covariance.

**Source references:** Báez-Duarte (2003), arXiv:math/0202141; arXiv:math/0205003; Burnol *Adv. Math.* 170 (2002) 56–70, doi:10.1006/aima.2001.2066; SUCC PRs #136, #157, #162, #165; original SUCC Tate/Weil source dossier. Proof originality outside elementary classical identities: **UNVERIFIED**.

## 9. BDC-09 — the backward-from-infinity memory kernel is an exact SUCC resolvent (PAPER PROVED)

**This is the sharper source comparison.** Uniform cyclic Haar averaging in BDC-02 omitted the real-line weight. The *actual* infinite Hilbert error can nevertheless be folded over one finite common clock, provided the complete reciprocal-square memory of its unseen future is retained.

For `L=lcm(1,...,N)`, write `x=u+jL`, `0<=u<L`, `j>=0`. Since `A_c(x+L)=A_c(x)`, Tonelli for the nonnegative squared error gives

`||h-F_c||² = b² + ∫_0^L A_c(u)² W_L(u) du`, `b=Σ c_n/n`,

where

`W_L(u) = R_L(u)` for `0<=u<1`, and

`W_L(u) = u^(-2)+R_L(u)` for `1<=u<L`,

`R_L(u)=Σ_(j>=1) 1/(u+jL)^2 = L^-2 ψ_1(1+u/L)`. (BDC.7)

The last identity uses the classical trigamma series; it is **not** an identification with the real Gamma component of the signed Weil form. The weight is nonconstant, changes one-sided behavior at the cut u=1, and carries exactly the information that normalized finite-clock Haar averaging discarded.

### Backward SUCC recurrence and the no-ghost boundary

For every `u>=0`, the kernel satisfies the exact backward-step identity

`R_L(u) - R_L(u+L) = 1/(u+L)^2`, (BDC.8)

and the infinity boundary `R_L(u+kL)->0`. This is a *well-posed discrete Poisson/renewal law with a boundary condition at infinity*. Conversely, every solution of (BDC.8) differs from `R_L` by an arbitrary L-periodic function. Enforcing decay at infinity kills that periodic ghost, proving **uniqueness**. It makes precise which part of a backwards Dedekind-style reconstruction is an equation and which part is an additional asymptotic boundary law. No finite list of shift equalities authenticates the boundary law by itself.

This may be written `R_L=(I-S_L)^(-1)a_L` pointwise on the restricted source `a_L(u)=(u+L)^(-2)` using a convergent Neumann series. **Do not** claim `(I-S_L)^(-1)` is a bounded inverse on all of `C_0`: the shift there has norm one and the Neumann inverse requires a suitable domain.

### Rigorous rational interval instrument

For depth `J>=1`, put `R_(L,J)(u)=Σ_(j=1)^J (u+jL)^(-2)`. The omitted tail has the exact source-independent bounds

`1/[L(u+(J+1)L)] <= R_L(u)-R_(L,J)(u) <= 1/[L(u+J L)]`. (BDC.9)

`clock_memory_resolvent.py` implements these in rational arithmetic; its weighted-clock integration uses exact subcell integrals of `A_c²` and monotone endpoint enclosures for `W_L`. The **one-sided cut boundary** is load-bearing: using the `u=1` right branch when enclosing a subcell below 1 creates a false lower bound (an adversarial development regression caught and corrected before commit). The independent all-line rational cutoff instrument `certified_cut_residual` encloses all the new folded-clock trial intervals, with no interpolated zeta zeros.

For `L=1`, `R_1(0)=Σj^-2=ζ(2)` exactly: the infinite reciprocal-square sum is the **backward memory at the origin**. The Basel constant thus appears twice, both in the uniform finite-clock covariance and in the *weighted* infinity-memory kernel, but these are different source functionals and cannot be identified by positivity alone.

### Verdict

The backward compactification is now a rigorous **finite-clock plus uniquely decaying memory kernel**. The hard part is no longer how to write the correct weighted norm; we can. It is to prove that the source-generated coefficient innovations drive this norm to zero for the specific upper cut as `N→∞`. That step remains precisely the RH-equivalent Báez-Duarte closure; no noncircular bound or Weil sign is obtained. Source access to arbitrarily large clocks is separately conditional on the SUCC observer constructor laws.

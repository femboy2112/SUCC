# SUCC triangular Gamma-rank source — harmonic, inverse-golden and original BBP

**2026-10-29 · Research-only mathematical dossier.** Exact parent: SUCC draft PR #367 head `b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`, itself rooted in merged Main XIV `ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc`. Companion, not a replacement, to draft PR #366, the October 29 triangular-harmonic prior discussion, and SUCC issues #361–#363. The inherited four-pole forcing, archived sources, historical claims, and `U_0=0` are unchanged. Nothing here proves pi normality or RH.

## A. Recovered harmonic–golden triangle (classical laws, declared coupling)

Let `lambda=(sqrt(5)-1)/2`, so `lambda^2=1-lambda` and `1+lambda=1/lambda`. For `r>0`, let `Y_r~Gamma(r,1)` and define the **two-observable, same-law contrast**

`D(r)=E[log Y_r]-E[exp(-lambda Y_r)]=psi(r)-lambda^r`.

For integer `r>=1`, `psi(r)=H_(r-1)-gamma`. Its discrete triangle identity is

`D(r+1)-D(r)=1/r+lambda^(r+2)>0`.

At the Oily-marked rank `r=2`, `D(2)=1-gamma-lambda^2=lambda-gamma=Omega_OM`. The continuous extension is strictly increasing: `D'(r)=trigamma(r)-lambda^r log(lambda)>0`. The previous order-statistic representation follows from `U_(r:N)~Beta(r,N-r+1)`, `N U_(r:N)=>Gamma(r,1)`, and `E log(N U_(r:N))=log N+H_(r-1)-H_N` for integer `1<=r<=N`.

The original *marked* Oily endpoint PGF is `G(z)=(2-z)^(-2)`; iteration from 0 selects `q*=lambda^2`, and `lambda=1-q*`. This declares the golden reference without inserting it into any finite positive BBP density. Regrading the Oily packets can change this selection: this is not an invariant of the ungraded four-pole kernel.

## B. The **authentic original-source** convolution field realizes every rank

Retain the exact four signed poles:

`R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)=(15a^2+121a+240)/[a(a+3)(a+4)(a+5)]` for `a>0`.

Set `a_n=8n-7`. Then `r(n)=R(a_n)` is the original rational BBP forcing, and `U_n(0)=sum_(k=1)^n 16^(n-k)r(k)`, `U_0=0`.

The genuine positive carrier is `mu_a(dx)=e^(-ax)Q(x) dx/R(a)` where `Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x)>0`. PR #367 constructs, for every `t>=0`, a positive convolution semigroup `mu_(a,t)` satisfying

`E_mu_(a,t) e^(-sX)=[R(a+s)/R(a)]^t`, with `mu_(a,1)=mu_a`.

**Theorem TGH-1 (same-source rank sheet).** For every real `r>0`, define `X_(a,r)~mu_(a,r/2)` and `Y_(a,r)=a X_(a,r)`. Then for every `s>=0`,

`L_a(s)=R(a(1+s))/R(a)`,
`E exp(-s Y_(a,r))=L_a(s)^(r/2)`.

Since `R(a)=15 a^(-2)[1-59/(15a)+O(a^(-2))]`, `L_a(s)->(1+s)^(-2)` for each fixed `s>=0`. By the continuity theorem for Laplace transforms,

`Y_(a,r) => Gamma(r,1)` as `a->infinity`.

The original carrier is **rank two**: `mu_(a,1)=mu_a`, `r=2`. Every other rank is a coherently defined convolution subdivision/power from this same four-pole source. Rank `r` is a *sheet parameter*, not the arithmetic time `n`, a new fundamental particle, or a selection of pi digits.

## C. Exact finite triangular observable, recurrence and an all-a positive error

Define, for `a>0,r>0`,

`D_a(r)=E[log Y_(a,r)] - E[exp(-lambda Y_(a,r))]`.

The identity `log y=int_0^infinity (e^(-s)-e^(-sy))ds/s`, for `y>0`, gives the **full-source finite formula**

`D_a(r)=int_0^infinity [e^(-s)-L_a(s)^(r/2)]ds/s - L_a(lambda)^(r/2)`.

The integral converges: near zero its numerator is `O(s)`; at infinity `L_a(s)^(r/2)=O(s^(-r))`. Gamma components in the source ensure integrable logarithmic moments. Nothing in this formula approximates pi with a random draw.

**Theorem TGH-2 (rank gluing and monotonicity).** For all `a,r>0`,

`D_a(r+1)-D_a(r) = int_0^infinity L_a(s)^(r/2)*(1-sqrt(L_a(s)))/s ds + L_a(lambda)^(r/2)*(1-sqrt(L_a(lambda))) > 0`.

Indeed `0<L_a(s)<1` for `s>0`, so each term is strictly positive. As `a->infinity`, the first term tends to `1/r`, and the second to `lambda^(r+2)`. This recovers the harmonic + golden triangle in one source-preserving limit.

**Theorem TGH-3 (one-sided finite error, all real ranks).** For every `a,r>0`,

`0<D(r)-D_a(r)<log(1+5/a)+lambda^r*(exp(5r lambda^2/(2a))-1)`.

*Proof.* The #367 atomic decomposition writes the scaled field as

`Y_(a,r)=G_1+[a/(a+5)]G_2+J_a`,

where `G_1,G_2` are independent `Gamma(r/2,1)`, and `J_a>=0` is independent compound-Poisson excess. Thus with `W=G_1+G_2~Gamma(r,1)`,

`Y_(a,r)>=[a/(a+5)]W`, hence `E log Y_(a,r)>=psi(r)-log(1+5/a)`.

The original source logarithmic derivative `m(a)=-d log R(a)/da=E_mu_a X` satisfies the proven #367 squeeze

`1/a+1/(a+5)<m(a)<1/a+1/(a+3)<2/a`.

Integrating `m` over `[a,a(1+s)]` yields `L_a(s)>(1+s)^(-2)` for every `s>0`. Frullani's log representation gives `E log Y_(a,r)<psi(r)` (strict Laplace order). At `s=lambda`, the same squeeze gives

`0<log[L_a(lambda)/(1+lambda)^(-2)]<5 lambda^2/a`.

Raising to `r/2`, `lambda^r<L_a(lambda)^(r/2)<lambda^r exp(5r lambda^2/(2a))`. Adding the positive log and Laplace deficits proves the bound. QED.

The bound is **source-relative** and uniform in `a`, not merely a fitted large-a asymptotic. It proves convergence of the finite original-carrier triangle to the harmonic–golden–Euler family for every fixed positive rank.

## D. First source-specific correction: the `59/30` four-pole coefficient

**Theorem TGH-4 (paper derivation, first rank defect).** For every fixed `r>0`,

`D_a(r)=D(r)-[59/(30a)]*(1+r*lambda^(r+2))+o_r(1/a)`.

The `59` comes from **the original four-pole second source jet**, `Q''(0)=-59`. It is not chosen by fitting to `lambda-gamma`.

*Derivation with an independently testable microscopic control.* Write `t=r/2` and use the explicit construction of PR #367:

`X_(a,r)=Gamma(t,a)+Gamma(t,a+5)+P_(3,alpha,t)+P_(4,beta,t)`.

The `P` terms are independent compound-Poisson channels, with intensities `t log[(a+alpha)/(a+3)]` and `t log[(a+beta)/(a+4)]`, where `3<alpha<4<beta<5` and `alpha+beta=121/15`. On scaling by `a`, the two Gamma variables become `G_1` and `[a/(a+5)]G_2` with `G_i~Gamma(t,1)`. The gamma contraction changes the expected logarithm by `-5/(2a)+o(1/a)`: differentiate `log[G_1+cG_2]` at `c=1`, using `E[G_2/(G_1+G_2)]=1/2`.

The total probability of one compound-Poisson jump is `t[(alpha-3)+(beta-4)]/a+O_r(a^-2) = (16t)/(15a)+O_r(a^-2)`. Conditional on one jump, its scaled size tends to an independent `Exp(1)`; since adding an exponential to `Gamma(r,1)` increases the mean log by `psi(r+1)-psi(r)=1/r`, the jump correction is `+8/(15a)+o(1/a)`. Two-plus jumps are `O_r(a^-2)` in probability and have uniformly integrable logarithmic increments under the stated Gamma/exponential bounds. Together the log correction is `-59/(30a)+o_r(1/a)`.

Separately the source expansion gives

`L_a(lambda)^(r/2)=lambda^r*[1+(59r/30a)*lambda^2+O_r(a^-2)]`.

Subtracting completes the coefficient. Tests at ranks 2,3,4 and independent Frullani-versus-four-pole log evaluation at rank 2 corroborate this asymptotic; exact tests alone are not proof authority. QED (paper, pending independent audit).

For the authentic arithmetic times `a_n=8n-7`, `D_(a_n)(r)=D(r)+O_r(1/n)` and the first correction is negative.

## E. A decisive **scalar no-go** for normality

Let `z_n(s,h)=exp(2 pi i h U_n(s))`, with `U_0(s)=s` and the same authentic forcing at every seed. For each fixed `r>0`, TGH-3 supplies a constant `C_r` such that

`|D_(a_n)(r)-D(r)|<=C_r/n` for all `n>=1`.

Consequently, **for every unit-modulus phase sequence, not merely pi**, we have

`|(1/N)sum_(n<=N) D_(a_n)(r) z_n - D(r)(1/N)sum_(n<=N) z_n| <= C_r H_N/N`.

At rank 2, `D(2)=Omega_OM>0`, so weighted `o(1)` is **equivalent** to the original still-open signed Weyl `o(1)`. Using a centered weight `D_(a_n)(2)-Omega_OM` instead proves `o(1)` even for the coherent nonnormal counterseed, and therefore cannot establish pi normality.

The genuine same-forcing counterseed `s*=-pi/16 (mod1)` satisfies `U_n(s*)=-T_n (mod1)`, where the source Green tail `T_n=O(1/n^2)` is positive. Hence `z_n(s*,h)->1` for fixed `h` and the source-ranked weighted mean tends to `D(r)`, not zero (when `D(r) != 0`). All positive source sheets and all scalar interactions survive this changed-seed control. The true zero-seeded signed cancellation remains **OPEN**.

## F. A second no-go: all **two-time Gram phases are pure gauge**

The same convolution field gives source Hilbert affinities

`H_t(a,b)=[R((a+b)/2)/sqrt(R(a)R(b))]^t`, `t=r/2`,

using densities relative to the common underlying Levy convolution measure. Define the **selected** rank Gram kernel

`K_(nm)(s)=z_n(s,h)*conj[z_m(s,h)]*H_(r/2)(a_n,a_m)`.

This is positive semidefinite, since it is the Gram matrix of the phase-decorated source vectors. Its entries depend on the seed, but set `V_s=diag(exp(2 pi i h 16^n s))`. The authentic affine law gives

`K(s)=V_s K(0) V_s^*`.

Thus all eigenvalues, determinants, positive spectral gap tests, and gauge-invariant closed cycles are **seed-blind**. For example,

`K_(ij)(s) K_(jk)(s) K_(ki)(s) = H_t(a_i,a_j) H_t(a_j,a_k) H_t(a_k,a_i) > 0`,

with the phase exactly cancelling. Therefore a Gram spectrum or three-edge phase holonomy assembled from simple phase *differences* cannot distinguish pi's zero seed from the coherent counterseed. An **anchored** readout can distinguish them, but must then establish a genuinely signed bound; positivity of the Gram matrix alone is not enough.

This is the gluing version of the old SUCC pure-gauge obstruction, now extended to every Oily–harmonic rank. To change the conclusion one needs a verified non-exact interaction, authenticated carry/branch data, or an absolute zero-seed-sensitive operator—not another scalar centering constant.

## G. Exact arithmetic no-resonance of the golden clock with base 16

For positive integers `r,m`, `lambda^r` is a quadratic irrational, whereas `16^(-m)` is rational, so they can never coincide. More quantitatively, with `lambda'=-(1+sqrt5)/2=-varphi` and `T_r=lambda^r+(lambda')^r` an integer,

`16^(2m) (lambda^r-16^(-m)) ((lambda')^r-16^(-m))=(-1)^r*16^(2m)-T_r*16^m+1`,

an integer that is nonzero. Therefore

`|lambda^r-16^(-m)| >= 16^(-2m)/(varphi^r+16^(-m))`.

This is a proved **exact-clock noncollision** theorem, not equidistribution. Incommensurability by itself provides no uniform estimate on the signed original `z_n` sum.

## H. Claim ledger and next verdict-changing probe

| Label | Statement | Status |
|---|---|---|
| TGH-1 | Source subdivision gives `Gamma(r)` boundary for all `r>0` | PAPER-PROVED, source #367 prerequisite |
| TGH-2 | Exact Frullani rank recurrence is positive | PAPER-PROVED |
| TGH-3 | `0<D(r)-D_a(r)` with explicit finite all-a bound | PAPER-PROVED |
| TGH-4 | First-order coefficient `59/30 (1+r lambda^(r+2))` | PAPER-PROVED, independent review pending; numeric holdouts |
| TGH-5 | Scalar rank weights cannot improve normality gate; counterseed survives | PAPER-PROVED |
| TGH-6 | Selected Gram matrix phases are unitary gauge and loop-flat | PAPER-PROVED |
| TGH-7 | Golden/base-16 exact powers never coincide, explicit norm lower bound | CLASSICAL algebra/PAPER-PROVED specialization |
| TARGET | Original `sum_(n<=N) exp(2pi i h U_n(0))=o(N)` | **OPEN** |

**Next discriminating probe**: construct an original-source labelled interaction which is NOT of the `z_n * conjugate(z_m) * H_nm` pure-gauge type. It must retain the absolute origin `U_0=0`, predict a distinct value for the coherent `-pi/16` counterseed, and yield a new *quantitative* signed estimate over unbounded `N`. Test affine order swaps, source-mutant jets, and incomplete/false gamma rank gluing as negative controls. Ordinary source-only cumulants, source-only `Omega` centering, or circular Weyl restatements do not pass.

**Reproduce (research scope only):** `python research/2026-10-29/triangular_harmonic_gamma_bbp/triangle_rank_probe.py -v` (requires mpmath for labelled numerical holdouts; exact rational tests otherwise standard library). The probe is independently reauthored; no Lean, full SUCC root gates, exact GitHub head replay, or hosted CI is claimed here until observed.

**Primary classical references:** NIST DLMF §5.2 (Gamma/digamma definition) and §5.5 (psi recurrence); standard Frullani identity, Levy compound-Poisson laws, and order-statistic Beta/Gamma limit. SUCC proofs: PR #367 atomic and dual dossiers; October 26 Oily–Macaroni source bridge and totient third-shadow; PR #366 Stoneham/path-sheet controls.

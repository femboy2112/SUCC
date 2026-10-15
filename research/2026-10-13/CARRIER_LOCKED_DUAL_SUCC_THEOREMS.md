# Carrier-locked dual SUCC: affine rigidity, complementary observer shells, and the RH boundary

**Origin:** 2026-10-13, research stacked on [zero-centered SUCC PR #59](https://github.com/femboy2112/SUCC/pull/59), parent exact commit b7fbba74fedd6e6734b1d2b129a72bdff4dd9843. **Research status:** PROVED LOCAL for the explicit paper derivations; CLASSICAL for the Wold/Tate ingredients; TESTED FINITE for exact rational code. Scholarly priority and independent proof-assistant formalization: **UNVERIFIED**. No authenticated physical source, full Weil form, or Riemann hypothesis proof. **RH PROVED: no.** No nontrivial zero positions enter any construction.

## The question and essential semantic correction

The question is whether changing a Schwartz test state while retaining Euler factors is a valid *equivalence of arithmetic carrier descriptions*. The intrinsic SUCC carrier has a unit successor S(n)=n+1 and multipliers V_p(n)=pn. Distinguish three predicates:

1. Different **test states** on one lawful arithmetic action: permitted, potentially different observations.
2. A **carrier equivalence**: must intertwine the actual actions and relevant observable products/labels.
3. An **arithmetic L-factor identification**: depends on the complete arithmetic representation, conductor/test domains and local Gamma normalization, not solely on one selected test function's zeros.

The nonstandard positive self-Fourier Gaussian **does not break addition**. It is another legitimate test state on the same arithmetic source. But the particular positive scale-mixture operator connecting it to the canonical Gaussian does *not* intertwine fixed-unit successor and is not a deterministic observable-algebra homomorphism. This rules it out as an affine carrier equivalence **without banning it as a test state**.

The program separates rigorous rigidity of translations from the unproved law selecting the canonical zeta test state.

## A01 — deterministic affine carrier rigidity (PROVED LOCAL)

Let C=N_{\ge1} with S(n)=n+1 and V_p(n)=pn for one fixed integer p>=2. A function F:C->C obeying F S=S F and F V_p=V_p F is identity.

**Proof.** The first relation implies F(n)=n+c with c=F(1)-1. At n=1 the second relation gives p+c=F(p)=pF(1)=p(1+c). Since p>=2, c=0. QED.

This works for composite p=6 as well; covariance alone cannot authenticate primes.

## A02 — exact Markov affine rigidity on the full integer carrier (PROVED LOCAL)

Let K(n,m)>=0 be a normalized probability kernel on C=N_{\ge1}, with rows \(\mu_n\). Assume the *actual source action* identities for every n:

\[
\mu_{n+1}=(m\mapsto m+1)_*\mu_n,\qquad
\mu_{pn}=(m\mapsto pm)_*\mu_n
\]

for one p>=2. Equivalently K commutes with pullbacks of unit SUCC and this multiplier on all bounded observables. Then

\[
\boxed{\mu_n=\delta_n\quad\text{for every }n.}
\]

**Proof.** Let Y have law mu_1 and put Z=Y-1>=0. By p-1 successor pushes, mu_p is the law of p+Z. By multiplier covariance, mu_p is also the law of p+pZ. Therefore Z and pZ have the same law. For any j>0, the point mass at j equals the mass at j/p if p divides j, otherwise zero. Repeating until divisibility stops shows that every positive j has mass zero. Countable additivity implies Z=0 almost surely; then every mu_n=delta_n by successor covariance. QED.

**What is proved:** positive normalized stochastic smoothing that genuinely preserves these two full-source actions is trivial. **Not proved:** that nature supplies a complete, authenticated kernel, that valid different analytic test states must be intertwiners, or that RH follows.

## A03 — quantitative affine rigidity and sharp source-tail cost (PROVED LOCAL)

For a possibly imperfect full set of probability rows mu_1,...,mu_p, define

\[
\epsilon_S=\max_{1\le j<p}\operatorname{TV}(\mu_{j+1},S_*\mu_j),
\quad
\epsilon_V=\operatorname{TV}(\mu_p,(V_p)_*\mu_1),
\quad
\delta=(p-1)\epsilon_S+\epsilon_V.
\]

For Z=Y_1-1 and any integer B>=1, let r be the smallest integer with p^r>B. Then

\[
\boxed{\Pr(1\le Z\le B)\le r\delta}
\tag{A03.1}
\]

and for any 1<=n<=p,

\[
\boxed{\operatorname{TV}(\mu_n,\delta_n)
\le(n-1)\epsilon_S+r\delta+\Pr(Z>B).}
\tag{A03.2}
\]

**Proof.** Repeated successor TV triangle bounds TV(mu_p,S_*^{p-1}mu_1) by (p-1)epsilon_S. Compare with Vp_*mu_1, then translate both by -p. We get TV(Law(Z),Law(pZ))<=delta. Iterating, using TV contraction under deterministic pushforward, yields TV(Law(Z),Law(p^r Z))<=r delta. The second law assigns zero mass to the event {1,...,B}; its distance from the first is at least Pr(1<=Z<=B). This proves (A03.1). Split Pr(Z>0) at B and propagate mu_1 to mu_n by the successor errors to obtain (A03.2). QED.

**Sharpness.** For exact rational alpha with 0<alpha<=1, set

\[
\nu=(1-\alpha)\delta_0+\frac{\alpha}{r}\sum_{j=0}^{r-1}\delta_{p^j},
\qquad \mu_n=\operatorname{Law}(n+Z),\ Z\sim\nu.
\]

Then epsilon_S=0; epsilon_V=alpha/r (the only unmatched scale-chain masses occur at 1 and p^r). With B=p^{r-1}, Pr(1<=Z<=B)=alpha=r delta. Thus the coefficient r cannot be improved universally. Exact implemented witness: p=2, r=3, alpha=3/4, B=4; epsilon_V=1/4, hidden mass=3/4.

This is a concrete finite-precision **information-resistance** law with explicit tail debt, not a physical thermodynamic theorem.

## A04 — Feller Markov rigidity of the real carrier (PROVED LOCAL, paper)

Let K be a Borel probability kernel on R. Assume Kf is continuous for every bounded continuous f (Feller condition), and K commutes with pullbacks of S(x)=x+1 and V_p(x)=px for p>=2. Then K is identity.

**Proof.** At x=0, dilation covariance forces mu_0=(V_p)_*mu_0. The only probability measure invariant under expanding dilation on R is delta_0: for any a>0 its tail probability equals the tail beyond p^j a for every j and tends to zero. Both S and Vp are invertible transformations of R, so commutation with their pullbacks implies commutation with inverse pullbacks and hence translations by k/p^j. Consequently mu_d=delta_d for every d in Z[1/p], a dense subset of R. For any x and bounded continuous f choose d_j->x; Feller continuity gives Kf(x)=lim Kf(d_j)=lim f(d_j)=f(x). Bounded continuous functions determine Borel probability measures, so mu_x=delta_x. QED.

Likewise any continuous deterministic F:R->R satisfying F(x+1)=F(x)+1 and F(px)=pF(x) is identity: h=F-id is bounded and 1-periodic, whereas h(p^j x)=p^j h(x), so h=0.

**Boundary:** This uses the actual R carrier, continuity, positivity, normalization, and full action covariance. There is no claim that these assumptions are deducible from an observer merely existing in physical reality.

## A05 — quotient-clock falsifier (REFUTED unrestricted rigidity)

On a finite cyclic carrier Z/mZ with gcd(m,p)=1, define K(x,-) to be **uniform** on all m points, for every x. Both S and Vp are bijections and preserve the uniform measure. K commutes with both, but K is **not identity**. Implemented exact example (m,p)=(5,2).

Therefore carrier-locked rigidity **does not automatically descend to finite quotient clocks**. The full integer source and its admissible limits/tightness are essential. The prime-to-p profinite Haar measure supplies an analogous nontrivial compact-carrier phenomenon.

## A06 — funhouse-mirror Gaussian, correctly typed (PROVED LOCAL exact mutation)

Put g(x)=exp(-pi x^2) and

\[
f(x)=\frac{22g(x)+20g(4x)+5g(x/4)}{47}.
\]

It is positive, Fourier self-dual, and f(0)=integral f=1. The state-changing positive unital scale-mixture operator T acting on real observables is

\[
(Th)(x)=\frac{22h(x)+20h(4x)+5h(x/4)}{47}.
\]

Direct exact arithmetic on the polynomial probes h=x and h=x^2 gives

\[
T x=\frac{413}{188}x,\quad
T x^2=\frac{5477}{752}x^2,\quad
T(x^2)-(Tx)^2=\frac{43425}{17672}x^2.
\]

T commutes with dilation pullbacks, but not fixed-unit successor:

\[
\boxed{(TS-ST)x=-225/188.}
\]

The modified zeta integral has Mellin multiplier C(2)=413/188, so the modified readout already differs from the canonical Dirichlet series inside Re(s)>1. The zeros of this *test-dependent multiplier* are **not zeros of the genuine intrinsic local L-factor**.

**Scope repair:** This shows T is not a lawful affine **equivalence**; it does NOT make f an invalid Schwartz function or modify the actual integer carrier. A valid test-state deformation need not intertwine the states' values. A separate, source-derived *distinguished-state selection law* is still missing.

**Restricted rigidity corollary:** For a positive normalized scale mixture \(T h(x)=E[h(Ax)]\) with finite second moment, commuting with unit translation on h=x and h=x^2 implies E[A]=E[A^2]=1; since Var(A)=0, A=1 almost surely. Two polynomial probes suffice *for this class*.

---

## D01 — explicit dual tower of the existing zero-centered dilation (CLASSICAL Wold; new-to-project implementation)

Import PR #59's authentic reciprocal-cell Hilbert space

\[
H=\ell^2(\mathbb N_{\ge1},w),\qquad w_k=\frac1{k(k+1)},
\]

and its zero-extended Archimedean isometry \(U_q f(x)=\sqrt q f(qx)\), q>=2. Define \(P_n=U_q^n U_q^{*n}\). Put m=q^n. For k<m, P_nf(k)=0; for block \(mj\le k<m(j+1)\), j>=1, the exact formula is

\[
\boxed{(P_nf)(k)=\frac{m}{w_j}
\sum_{r=mj}^{m(j+1)-1}w_r f(r).}
\tag{D01}
\]

Because the block weights sum to w_j/m, this is the orthogonal weighted-average projection; its matrix entries are rational. The ranges are nested:

\[
P_0=I,\quad P_nP_m=P_{\max(n,m)},\quad P_n=P_n^*=P_n^2.
\]

Define complementary **dual-observer shells**

\[
\boxed{Q_n=P_n-P_{n+1}
=U_q^n(I-U_qU_q^*)U_q^{*n}.}
\]

Each Qn projects orthogonally onto \(U_q^n\ker U_q^*\), the information discarded between adjacent dilation resolutions. Distinct Qn are orthogonal. This is a concrete Wold decomposition, not a new general operator-theory theorem.

## D02 — two observer fronts meet at the exact boundary (PROVED LOCAL)

For every f in H and every **finite** N,

\[
\boxed{f=\sum_{n=0}^{N-1}Q_nf+P_Nf}
\tag{D02}
\]

and

\[
\boxed{\|f\|^2=\sum_{n<N}\|Q_nf\|^2+\|P_Nf\|^2.}
\tag{D03}
\]

**Proof.** Telescope Qn=Pn-P(n+1) and use P0=I. Each Qn is orthogonal to PN, and all distinct Qn are mutually orthogonal, because of the nested projection identities. QED.

This supplies the user's dual-tower **meeting law**: one E system retains the unresolved boundary P_Nf, the complementary E tower transmits only the discarded shells Q0f,...,Q(N-1)f. They glue to exactly one Hilbert vector with conserved norm **under the declared common carrier**.

## D03 — full source reconstruction, no ghosts and sharp no-uniform finite deadline (PROVED LOCAL)

PR #59 proved Uq is a pure isometry: intersection of its range powers is zero. For finite-support f with largest occupied cell M, P_Nf=0 once q^N>M by D01. For arbitrary f in H, density of finite-support vectors and \(\|P_N\|\le1\) prove P_Nf->0 strongly. Hence

\[
\boxed{f=\sum_{n\ge0}Q_nf\text{ in }H,\quad
\|f\|^2=\sum_{n\ge0}\|Q_nf\|^2.}
\tag{D04}
\]

Every square-summable **correctly typed** family b_n in ran Qn gives one actual f=sum b_n in H; its remaining boundary at depth N is P_Nf=sum_(n>=N)b_n. Two f values with identical complete shell reports must coincide. This is a **source-realization theorem for this mathematical Hilbert carrier**, not for every physical/adelic source.

**No finite uniform cutoff.** For any N choose m=q^N and nonzero finite source

\[
f_N(k)=\mathbf1_{\{m\le k<2m\}}.
\]

Then f_N is in ran P_N, and Q0 f_N=...=Q(N-1) f_N=0 although f_N!=0. Its squared norm is 1/(2m). Therefore \(\|P_N\|=1\) for every N: P_N converges strongly to zero, but **not** in operator norm. Every fixed finite complementary observer horizon misses some genuine source; no source-uniform L2 approximation bound follows from this construction alone.

## D04 — additive successor/dilation obstruction (REFUTED naive commute)

The complementary shells are intrinsic to q-dilation, **not** automatically equivariant under the additive SUCC pullback \(T_Sf(k)=f(k+1)\).

Take q=2, f=delta_2. Exact D01 gives

\[
P_1 f=(2/3)\delta_2+(2/3)\delta_3,\quad
P_1(T_Sf)=P_1(\delta_1)=0.
\]

But \(T_S(P_1f)\) has value 2/3 at cell 1, so

\[
\boxed{[(T_SP_1-P_1T_S)\delta_2](1)=2/3.}
\tag{D05}
\]

This is an exact **new-to-project additive/multiplicative boundary defect**. It refutes the belief that merely constructing a complementary Hilbert tower automatically glues all lawful SUCC/FUCC paths. A real source-derived connection transporting successor across these shells is the next missing bridge.

## Proof status, hostile controls and reproduction

Modules: observational_succ/carrier_locked_rigidity.py and observational_succ/dual_shell_observer.py. Exact tests: tests/test_carrier_locked_rigidity.py and tests/test_dual_shell_observer.py. Driver: scripts/carrier_locked_dual_probe.py. The tests check complete exact law tables (including 100 independently computed p=2 kernels), sharp rational TV saturation, explicit source tails, composite 6, finite cyclic equivariant averaging, Gaussian first/second moments, arbitrary-depth invisible states, orthogonal shell decomposition, and noncommuting additive transport. **15 isolated tests passed on the authored scratch versions**; integrated remote CI and separate Lean formalization are not silently claimed.

From repo root:
- python -m unittest discover -s tests -p 'test_carrier_locked_rigidity.py' -v
- python -m unittest discover -s tests -p 'test_dual_shell_observer.py' -v
- python scripts/carrier_locked_dual_probe.py

External mathematical anchors: [Wold decomposition and wandering subspaces](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-speed-of-convergence-in-the-ergodic-theorem-for-shift-operators/29800FD6250070C1E1387960756AF179); [Tate's thesis test-function-dependent local integrals and test-independent Gamma factor](https://www.math.columbia.edu/~avizeff/quals/Tate.pdf). Total-variation contraction, affine actions, Wold decomposition and Markov intertwining have established mathematical provenance. **No independent scholarly priority review has been performed.**

## RH-specific verdict and the next decisive probe

The two actual mathematical successes are **(i) source-faithful affine carrier-equivalence rigidity**, and **(ii) exact complementary shell descent with an honest boundary residual**. Both are useful ObsSUCC tools. Neither constructs authentic prime-power/Gamma/pole Weil positivity, or proves a global source-derived Nyman–Beurling approximation rate.

The next hard object is the commutator/connection \([T_S,P_n]\) **for all n and authentic prime multiplication**, with correct source history, sign, domains and basis transport. Independently identify its source-derived signed completed pairing with the Weil/Suzuki form, and test fake multiplier 6, nonmultiplicative Dirichlet coefficients, changed Gamma tests, and the actual full source. Any claimed global positivity must not be imported from the ambient Hilbert norm. **RH remains open.**

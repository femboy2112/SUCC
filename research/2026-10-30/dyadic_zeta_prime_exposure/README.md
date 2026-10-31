# Operation DYADIC EXPOSURE — Pascal, 2, Bernoulli prime denominators, Gamma and circle Green moments

**Research only — 2026-10-30.** This is a new-to-SUCC synthesis of classical exact mathematics, **not** a claim of scholarly priority or a proof of RH or base-16 normality of pi. The original four-pole BBP source, selected zero seed, production files, frozen sources and main branch are unchanged.

**Pinned parent:** merged Main XVI, e18ba565ca540adb7edf3292f5593929e76d91c5. **Read-only related work:** PR #417 (universal finite Pascal/N/Z, Gamma and zeta), PR #420 (finite-cycle Basel Green trace), PR #421 (carrier/prime-to-selected-first-jet transport and all-order changed-source shadow), PR #416 (authentic BBP logarithmic potential). This package is **independent**, based directly on main; its theorems are not a claim that these unmerged research branches have been integrated.

## 0. Problem, objects and truth boundaries

The mathematical question: why are the first nontrivial negative zeta values

\[
\zeta(-1)=-1/12,\qquad\zeta(-3)=1/120,
\]

and why do their denominators exhibit 3 and 5 in apparent correspondence with the dyadic quantities \(2^2-1=3\) and \(2^4-1=15\)? Can this be placed on the same **finite** Pascal/Gamma/prime/real carrier as the Basel identity \(\zeta(2)=\pi^2/6\), without confusing analytic continuation with ordinary summation?

Separate layers: (a) finite positive integer counting; (b) Abel continuation of alternating power sums; (c) meromorphic zeta continuation in exponent s; (d) Archimedean and p-adic completions; (e) prime-denominator valuations; (f) finite-cycle spectral observables; (g) a selected **BBP source and seed**. Results concerning (a)–(f) do not entail statements about (g).

## 1. DY-01 — Pascal/Stirling produces a purely dyadic eta numerator (PROVED)

Let \(S(m,j)\) be the Stirling numbers of the second kind. They obey the finite partition recurrence

\[
S(m+1,j)=jS(m,j)+S(m,j-1).
\]

The falling-factorial/Pascal change of basis is exact for natural integer n:

\[
n^m=\sum_{j=1}^{m}j!S(m,j)\binom{n}{j}\qquad(m\ge1).
\]

For \(|x|<1\), sum the absolutely convergent generating function:

\[
\sum_{n\ge1}n^m x^n
=\sum_{j=1}^{m}j!S(m,j)\frac{x^j}{(1-x)^{j+1}}.
\]

The right side is rational and regular at x=-1. Evaluate there by the **genuine Abel limit** along x=-t, t increasing to 1. Accounting for the sign in the Dirichlet eta definition gives

\[
\boxed{\eta(-m)=-\sum_{j=1}^{m}
\frac{(-1)^j j!S(m,j)}{2^{j+1}}
=\frac{C_m}{2^{m+1}}}
\]

where the explicitly finite integer

\[
\boxed{C_m=-\sum_{j=1}^{m}(-1)^j j!S(m,j)2^{m-j}\in\mathbb Z.}
\]

Thus **eta(-m) belongs to the dyadic rationals \(\mathbb Z[1/2]\) at every m>=1**. No numerical extrapolation or novel definition of primes is used. Example values: eta(-1)=1/4; eta(-3)=-1/8; eta(-5)=1/4; eta(-7)=-17/16. At m=0 the separately continued eta value is 1/2. The series of alternating n^m terms is **not ordinarily convergent** at m>=1.

## 2. DY-02 — exact dyadic prime-exposure theorem (PROVED)

Initially for Re(s)>1, separating even and odd terms gives

\[
\eta(s)=\left(1-2^{1-s}\right)\zeta(s).
\]

The identity extends analytically. At every negative odd integer \(s=1-2k\), k>=1:

\[
\boxed{\zeta(1-2k)=-
\frac{C_{2k-1}}{2^{2k}(2^{2k}-1)}.}
\]

**Consequences, with full integer multiplicities:** the **odd part of the reduced denominator** of \(\zeta(1-2k)\) divides \(2^{2k}-1\). Every odd prime p in that denominator therefore has \(\operatorname{ord}_p(2)\mid2k\). This is a necessary, not sufficient, condition. For k=4, 17 divides \(2^8-1=255\) yet does **not** divide the denominator of \(\zeta(-7)=1/240\). For k=5, 31 divides \(2^{10}-1=1023\) yet does **not** divide the denominator of \(\zeta(-9)=-1/132\). The numerator cancels some exposed primes.

| k | 2k | eta(1-2k) | 2^(2k)-1 | zeta(1-2k) |
|---|---|---|---|---|
| 1 | 2 | 1/4 | 3 | -1/12 |
| 2 | 4 | -1/8 | 15 | 1/120 |
| 3 | 6 | 1/4 | 63 | -1/252 |
| 4 | 8 | -17/16 | 255 | 1/240 |
| 5 | 10 | 31/4 | 1023 | -1/132 |
| 6 | 12 | -691/8 | 4095 | 691/32760 |
| 7 | 14 | 5461/4 | 16383 | -1/12 |
| 8 | 16 | -929569/32 | 65535 | 3617/8160 |

## 3. DY-03 and DY-04 — exact finite-to-infinite transfer; different completions

For k>=1 define a finite dyadic path

\[
X_{k,R}=-\eta(1-2k)\sum_{r=1}^{R}2^{-2kr}.
\]

Every finite X is in \(\mathbb Z[1/2]\). The **finite geometric identity** gives

\[
\boxed{X_{k,R}=\zeta(1-2k)(1-2^{-2kR})},
\]

so X converges to the continued zeta value **in the real norm** with exact residual \(|\zeta(1-2k)|2^{-2kR}\). Explicitly:

\[
\zeta(-1)=-\frac14(4^{-1}+4^{-2}+\cdots)=-\frac1{12},
\]

\[
\zeta(-3)=\frac18(16^{-1}+16^{-2}+\cdots)=\frac1{120}.
\]

This is a rigorous model of a real limit possessing new odd-denominator valuations although every finite approximant has a power-of-two denominator. It is **not** the ordinary divergent sum 1+2+3+..., and the source and completion are part of the theorem.

**p-adic obstruction:** for any prime p, increments have exact form

\[
X_{k,R+1}-X_{k,R}=-\eta(1-2k)2^{-2k(R+1)}.
\]

For odd p, their p-adic valuations are constant and finite; for p=2 they tend to minus infinity. Thus the finite path is **not Cauchy in any Q_p**. A real completion cannot be transported to all prime places by silently reusing the limit. The infinite boundary is a **specified Archimedean** boundary, not a place-independent prime-creation mechanism.

## 4. DY-05 — every odd prime has a precise first appearance (PROVED)

The classical von Staudt–Clausen denominator theorem says

\[
\operatorname{den}(B_{2k})=
\prod_{\substack{p\text{ prime}\\p-1\mid 2k}}p,
\qquad
\zeta(1-2k)=-B_{2k}/(2k).
\]

Fix any odd prime p. For all earlier negative odd indices, \(2k<p-1\), so p divides neither the Bernoulli denominator nor 2k. At \(2k=p-1\), the Bernoulli number has p-adic valuation -1, while p does not divide p-1. Hence

\[
\boxed{\text{First appearance of p is at }\zeta(2-p),\quad
v_p(\zeta(2-p))=-1.}
\]

Examples: p=3 -> zeta(-1); p=5 -> zeta(-3); p=7 -> zeta(-5); p=11 -> zeta(-9); p=13 -> zeta(-11); p=17 -> zeta(-15). This is the *precise, proved* sense in which the prime ladder emerges.

**Two nonidentical sieves:** the dyadic condition \(\operatorname{ord}_p(2)\mid2k\) marks possible exposure; the Bernoulli criterion \(p-1\mid2k\) determines the Bernoulli denominator. Fermat gives the implication from the latter to the former, not its converse. Denominator cancellations matter.

**Sharper complete survival theorem (DY-11/DY-12).** Von Staudt's second theorem additionally determines the *entire* denominator: for every even m>=2,
\[
\operatorname{den}\zeta(1-m)=\prod_{p-1\mid m}p^{1+v_p(m)}.
\]
It also yields an exact p-adic cancellation law for the finite integer Stirling numerator C_(m-1). See [DENOMINATOR_SURVIVAL.md](DENOMINATOR_SURVIVAL.md) for full proof provenance, prime 17/31 controls, and the independent index-100 exact-rational test.

## 5. DY-06 — all odd negative zeta values from positive finite-cycle Green moments (PROVED)

On the N-cycle (N>=3), let \(L_N\) be its ordinary combinatorial Laplacian, \(G_N=L_N^+\) its mean-zero Moore–Penrose inverse. The nonzero eigenvalues are \(\lambda_j=4\sin^2(\pi j/N)\), j=1,...,N-1. Define

\[
T_{N,k}=N^{-2k}\operatorname{Tr}(G_N^k),\qquad k\ge1.
\]

Pair eigenvalues with j and N-j. For fixed j, \(N^2\lambda_j\to(2\pi j)^2\). Using \(\sin(\pi j/N)\ge2j/N\) for 1<=j<=N/2, dominate paired terms by a constant times \(j^{-2k}\); this is summable. Dominated convergence proves

\[
\boxed{\lim_{N\to\infty}T_{N,k}
=\frac{2\zeta(2k)}{(2\pi)^{2k}}.}
\]

The standard zeta functional equation

\[
\zeta(1-s)=2(2\pi)^{-s}\cos(\pi s/2)\Gamma(s)\zeta(s)
\]

then gives, for every integer k>=1,

\[
\boxed{\zeta(1-2k)=(-1)^k(2k-1)!
\lim_{N\to\infty}N^{-2k}\operatorname{Tr}(G_N^k).}
\]

Thus every negative odd continued value is a signed, Gamma-factor-normalized limit of **positive finite geometric spectral moments**. This is not an ordinary summation of positive powers.

The already-established SUCC PR #420 k=1 Green formula is

\[
\operatorname{Tr}(G_N)=(N^2-1)/12,
\quad T_{N,1}=(1-N^{-2})/12\to1/12=-\zeta(-1).
\]

For the next moment, an exact finite identity gives

\[
\operatorname{Tr}(G_N^2)=(N^4+10N^2-11)/720.
\]

Its normalized limit is 1/720, and the Gamma factor 3!=6 yields \(6/720=\zeta(-3)=1/120\). Exact rational matrix inversion tests both finite trace formulas.

For dyadic sizes, \(T_{2N,1}-T_{N,1}=1/(16N^2)\). Using the polynomial extension \(T_{1,1}=0\), the telescoping sum is \(1/12=\sum_{r\ge0}1/(16\cdot4^r)\). The baseline k=1 trace is **inherited from #420**; the all-k map and joint dyadic-prime interpretation are this synthesis.

## 6. Pascal and Gamma directly bridge to pi and the primes

There is also a classical **inverse central-binomial Basel identity**, which uses Pascal's triangle explicitly:

\[
\boxed{\zeta(2)=3\sum_{n\ge1}
\frac{1}{n^2\binom{2n}{n}}=\frac{\pi^2}{6}.}
\]

An equivalent arcsine identity is \(\sum_{n\ge1}x^{2n}/[n^2\binom{2n}{n}]=2\arcsin(x/2)^2\), evaluated at x=1. This is a genuinely direct Pascal-to-pi bridge, independent of the dyadic eta path and of the BBP source.

In the convergent half-plane s>1, the Euler product gives \(\zeta(2k)=\prod_p(1-p^{-2k})^{-1}\). The p=2 factor is the largest **individual** Euler factor for real s>1; at s=2 it is 4/3, while the odd-only reciprocal-square sum is \(\pi^2/8\). It does not control all primes alone. The correct reflected prime formula is

\[
\boxed{\zeta(1-2k)=(-1)^k
\frac{2(2k-1)!}{(2\pi)^{2k}}
\prod_p(1-p^{-2k})^{-1}.}
\]

Here **the prime product is evaluated at positive 2k**, never at the divergent negative argument. In particular zeta(-1)=-zeta(2)/(2pi^2), while zeta(-3)=3zeta(4)/(4pi^4).

Differentiate the functional equation at s=2k and use
\(\psi(2k)=H_{2k-1}-\gamma\) and
\(-\zeta'(2k)/\zeta(2k)=\sum_p\log p/(p^{2k}-1)\).
Then

\[
\boxed{
\frac{\zeta'(1-2k)}{\zeta(1-2k)}
=\log(2\pi)+\gamma-H_{2k-1}
+\sum_p\frac{\log p}{p^{2k}-1}.}
\]

This gives an exact **Archimedean Gamma + Euler–Mascheroni + finite harmonic + convergent prime-power** common-basis formula. The p=2 summand is \(\log2/(2^{2k}-1)\). PR #417 already studies related negative-integer zeta tangent families; the present point is their explicit dyadic denominator sieve. This scalar identity proves neither Weil positivity nor any selected BBP Weyl cancellation.

## 7. Firewall: the geometric powers-of-two series uses a different continuation

The ordinary finite geometric identity is
\(\sum_{j=0}^{R}2^j=2^{R+1}-1\).
The meromorphic continuation of the **generating function** \(1/(1-x)\), initially \(|x|<1\), has value -1 at x=2. With indexing starting j=1, \(x/(1-x)\) instead evaluates to -2. Neither is an ordinary sum at x=2, and a finite-part subtraction must declare its cutoff. By contrast eta(-m) above is an Abel limit at x=-1, and zeta(-m) is a continuation in s. No scheme-independent equality between these different divergent expressions is claimed.

## 8. Adversarial controls, status and next decisive probe

- **Prime-exposure mutant:** 17 is exposed at 2^8-1 but cancelled from zeta(-7); 31 similarly at 2^10-1. Refutes a naive consecutive-prime-generation rule.
- **Topology mutant:** real finite-level convergence does not imply convergence in any Q_p, shown by exact increment valuations. Refutes implicit place-independent completion.
- **Observer/source mismatch:** universal Bernoulli, Gamma, Basel, Pascal and circle formulas hold equally for an altered BBP seed. The *same-source coherent seed* -pi/16 is a known nonnormal countercontrol. #421 has a positive zero-seeded changed-source whose entire correction is invisible to all spectral poles but changes its selected boundary.
- **Actual proof gate:** retain the literal four signed BBP poles, selected U_0=0, complete source including entire remainders, and original real carry. Construct a source/seed-faithful map to selected characters exp(2pi i h U_n); then establish a genuinely sublinear signed Fourier/Weyl estimate or a weaker selected-interval estimate that the coherent controls fail. This remains OPEN.
- **Not claimed:** new analytic continuation, a proof of RH, a proof of normality, proof of physical curvature, a natural prime generation mechanism, or a universal arithmetic phase transport.

### Computational calibration

Run the **stdlib-only** exact rational probe in this directory:

~~~sh
python research/2026-10-30/dyadic_zeta_prime_exposure/dyadic_zeta_prime_probe.py
~~~

A scoped local run passed **11/11 unittest methods** (m=1..50; odd primes through 43; p-adic controls and cycle Green traces N=3..10). These are finite implementation checks, **not proofs of all quantified theorems**. This package did not run the complete repository's ~10k regression tests or the full AGENTS.md gates; no CI, Lean, blind independent review or whole-repo pass is claimed.

### External provenance

- [NIST DLMF §25.4: zeta functional equation](https://dlmf.nist.gov/25.4)
- [NIST DLMF §25.6: integer values and inverse central-binomial Basel formula](https://dlmf.nist.gov/25.6)
- [NIST DLMF §24.2: Bernoulli generating function](https://dlmf.nist.gov/24.2)
- [NIST DLMF §24.10: von Staudt–Clausen](https://dlmf.nist.gov/24.10)
- [Dirichlet eta relation](https://mathworld.wolfram.com/DirichletEtaFunction.html)
- SUCC [#417](https://github.com/femboy2112/SUCC/pull/417), [#420](https://github.com/femboy2112/SUCC/pull/420), [#421](https://github.com/femboy2112/SUCC/pull/421). All are **draft** research, not merged theorem authority.

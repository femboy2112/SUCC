# The oily-macaroni proposal: a common source, two shrinking errors, and the phase boundary

**Date:** 2026-10-26, UTC. **Research base:** PR [#306](https://github.com/femboy2112/SUCC/pull/306),
commit `7989be5753341c5e74d570e8fea51e00129d2d0a`, on top of Main XI
`6dd80730c3575d91f746546a25da5aedbd2e2737`.

**Result:** paper-proved source mixture, error comparisons, and normalized auxiliary
circle cancellation; exact rational finite
certificates; two corrections to the inherited next-round plan. **Selected signed Weyl
cancellation, base-16 normality of pi, and RH remain OPEN.** The existing
`N - O(log N)` modulus frontier is unchanged. No academic priority or new Lean theorem is claimed.

**Continuation of this round:** the [four-pole atomic dossier](FOUR_POLE_ATOMIC_SUBSTRATE.md)
now derives the source from two quadratic coefficient atoms, constructs a positive binary
polynomial approximation with a sharp uniform defect, and derives the reference
`lambda^2` from the endpoint probability generating function `G(z)=1/(2-z)^2`.
This strengthens the provenance of the golden reference for that specified packet law.
Two source-preserving changes of the packets change the fixed point, including one that
preserves every finite approximation of depth at least two. Thus the offset is an exact
quantity of the declared graded construction, not an invariant of the ungraded kernel.
The common-centering and selected-observable limitations below remain in force.

## 1. The question, its strongest faithful reading, and the contract

The author proposed that multiplicative/logarithmic normalization, the `0/1/infinity`
triangle, signed mirror charts, and coherent paths such as `0 -> Z/16 -> Z/2 -> 0`
might connect the shrinking BBP error to

$$
\lambda=\frac{\sqrt5-1}{2}=\varphi^{-1},\qquad
\delta=\lambda-\gamma\approx0.04081832384836.
$$

The requested name, **oily-macaroni constant**, is retained for this candidate offset.
The decimal is a numerical display, not a premise of any proof. The intended steelman is
an exact shared source and observable transport, not an inference from close decimals.

| Contract item | Precise target and boundary |
|---|---|
| Object | Original four-pole BBP source, its zero-initialized unwrapped orbit, and its future Green tail |
| Proposed statement | Construct a source-derived log observable converging to delta, with a quantitative bridge from its shrinking discrepancy to the authentic tail |
| Initial status | CONJECTURED connection; a Gamma first jet already existed in the October 25 four-point dossier |
| Hypotheses | Integer n at least 1; exact original weights and shifts; positive auxiliary measures explicitly normalized; complex Mellin exponents with real part greater than minus 2 |
| Weakest useful form | An explicit error identity and all-n estimates, without assuming any circle-distribution conclusion |
| Edge closed | Finite successor products -> Laplace/Mellin common source -> authentic log correction -> analytic BBP error and auxiliary moving-frequency circle cancellation |
| Edge still open | Relative source log phases -> selected signed circle/carry cancellation |
| Novelty tax | The derived comparison is weaker than normality: a fully explicit rational nonnormal source matches its first two mixture moments and asymptotic constants |
| Cheapest falsifiers | Reference shift; changed seed at the exact forcing; a dropped pole; matched-moment rational source; finite-conductor resonance; cross-digit parity control |
| Fresh regions | Exact indices 97, 257, 1009 and larger tail indices; independently written Decimal and quadrature oracles; all finite carry additions |
| Finite boundary | Finite rational intervals certify stated finite values. The universal inequalities and limits use the proofs below |
| Next lamp | An observable-preserving, zero-seed-sensitive transport for relative phases, with a signed residual estimate |

The three delegated bearings used the same mathematical source and model family. Their
agreement is not external independence. Exact algebra, source mutation, elementary analytic
proof, a separate Decimal implementation, and numerical quadrature provide distinct checks.

## 2. Recover the source before normalizing it

Throughout, e(t) means exp(2 pi i t) when it denotes a circle character. The source is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

Its positive, summable future tail is

$$
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
U_n+T_n=16^{n-1}\pi.
$$

These are inherited identities, not discoveries of this round. Implementation provenance:
`bbp_natural_carrier.exact_forcing`, `gamma_bbp_signed_coherence.green_tail_interval`,
the [signed Green dossier](../2026-10-25/SIGNED_GAMMA_BBP_GREEN_COHERENCE.md), and
the [BBP Gamma boundary](../2026-10-25/BBP_GAMMA_BOUNDARY.md).
The imported archival source is unchanged; its manifest pins originating commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`.

The existing Fourier-transfer theorem makes selected normality equivalent to

$$
\sum_{n=1}^N e(hU_n)=o(N)\quad\hbox{for every fixed nonzero integer }h.
$$

A theorem about the small positive T_n is not automatically a theorem about those
signed sums. In particular, changing the initial value leaves T_n unchanged while
changing the expanding homogeneous component of the orbit.

## 3. One finite family produces e, gamma, and the golden Laplace fixed point

For each positive integer m, declare the polynomial probability density

$$
p_m(x)=(1-x/m)^{m-1},\qquad 0<x<m.
$$

This is a continuous law on a bounded interval, with finite degree and finite-product
formulas. It is not a finite-state distribution or a claim that finitely many rational
successors output an exact irrational constant.

Euler's beta integral gives, for Re z greater than minus 1,

$$
M_m(z)=\mathbb E X_m^z
=m^z\prod_{j=1}^m(1+z/j)^{-1},\qquad
\frac{M_m(z+1)}{M_m(z)}=\frac{m(z+1)}{m+z+1}.
$$

In particular,

$$
\mathbb E X_m^k=k!\prod_{j=1}^k\frac m{m+j},\qquad
\mathbb E\log X_m=\log m-H_m,\qquad
\Pr(X_m>1)=(1-1/m)^m.
$$

The correction in the Mellin successor tends to 1, recovering the factorial successor.
For k at least 1 the exact moment error satisfies

$$
0<1-\frac{\mathbb E X_m^k}{k!}\le\frac{k(k+1)}{2m}.
$$

Proof: apply `1 - product(1-a_j) <= sum a_j` to `a_j=j/(m+j)`.

Let X have density exp(-x) on the positive real axis. The coupling

$$
X_m=m(1-e^{-X/m})
$$

has precisely p_m, increases to X, and satisfies E(X-X_m)=1/(m+1).
Consequently the Laplace transforms obey, for s at least zero,

$$
0\le L_m(s)-\frac1{1+s}\le\frac{s}{m+1}.
$$

This follows from the s-Lipschitz property of exp(-s x). The three limits from the
same family are

$$
\Pr(X_m>1)\longrightarrow e^{-1},\qquad
\mathbb E\log X_m\longrightarrow-\gamma,\qquad
L_m(s)\longrightarrow L(s)=\frac1{1+s}.
$$

The limiting Mellin transform is Gamma(1+z). For m at least 2,
`p_m(x) <= exp(-x/2)` on its support, so dominated convergence justifies fixed
Mellin exponents and their logarithmic derivatives on the indicated domain.
The positive fixed point L(lambda)=lambda is exactly the golden inverse.

If lambda_m is the unique root L_m(s)=s in (0,1), monotonicity and the coupling give

$$
\lambda<\lambda_m\le\lambda+\frac{\lambda}{m+1},\qquad
\lambda_m\downarrow\lambda.
$$

The upper bound follows by evaluating L_m(lambda)-lambda and using that L_m(s)-s
has slope at most -1. The module `exponential_gamma_bridge.py` certifies finite roots
with rational Taylor bounds and bisection; it raises if a sign cannot be certified.

**Provenance:** these are classical beta/Gamma identities and a new finite-source interface
for this round. See [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1),
[5.2.1](https://dlmf.nist.gov/5.2.E1), and [5.4.14](https://dlmf.nist.gov/5.4.E14).
The prior factorial-moment source reconstruction is recorded in
[FGF-3 and FGF-7B](../../docs/CLAIM_SUPPLEMENT_FACTORIAL_GAMMA_FUCC.md).

## 4. Delta is a genuine first log moment; its finite error does not depend on lambda

On the common exponential source,

$$
F_c(z)=e^{cz}\Gamma(1+z),\qquad
\left.\frac{d}{dz}\log F_c(z)\right|_{z=0}=c-\gamma.
$$

At c=lambda this first jet is delta. Equivalently, E(log X+lambda)=delta.
The finite-beta version has first jet lambda-(H_m-log m). Therefore

$$
\delta-[\lambda-(H_m-\log m)]
=H_m-\log m-\gamma=:\epsilon_m.
$$

The same cancellation holds with **any real c** in place of lambda. Thus the
shrinking Euler error is structural, while the choice of golden reference is not
distinguished by this subtraction. Nor do the two finite errors cancel one another:

$$
\lambda_m=\lambda+\frac{1-2\sqrt5/5}{m}+O(m^{-2}),\qquad
H_m-\log m=\gamma+\frac1{2m}+O(m^{-2}).
$$

For the first formula, expand the coupling's Laplace transform:
`L_m(s)=1/(1+s)+s/[m(1+s)^3]+O(m^-2)`, then solve its simple fixed-point equation.
The remainder is locally uniform for `|s|<1`: use the exact moment series
`sum_k (-s)^k product_(j<=k)(1+j/m)^(-1)`, bound its second-order product
remainder by a constant times `k^4/m^2`, and sum `rho^k k^4` for any fixed rho less than 1.
The leading coefficients are different. This is a quantitative test of the proposed
discrete/continuous relationship, not a dismissal of their common source.

## 5. An all-n theorem connects the authentic tail to the Euler error

**Theorem.** For every integer n at least 1,

$$
\boxed{\frac1{(8n+7/2)^2}<T_n<\frac{\epsilon_n^2}{16}},\qquad
\boxed{\left(\frac n{n+7/16}\right)^2
<\frac{16T_n}{\epsilon_n^2}<1}.
$$

This is an actual comparison theorem, stronger than merely fitting the common n^-2 scale.

### Euler bound

The classical digamma integral gives

$$
\epsilon_n=\int_0^\infty e^{-nt}
\left(\frac1t-\frac1{e^t-1}\right)dt.
$$

For t positive the kernel lies strictly between `1/2-t/12` and `1/2`.
For the lower bound, multiplying the difference by `12t(e^t-1)` gives

$$
(12-6t+t^2)(e^t-1)-12t
=\sum_{k\ge5}\frac{(k-3)(k-4)t^k}{k!}>0.
$$

For the upper bound, `(2+t)-(2-t)e^t` has the positive series
`sum_(k>=3)(k-2)t^k/k!`. Integration proves

$$
\frac{6n-1}{12n^2}<\epsilon_n<\frac1{2n}.
$$

The integral is classical; the displayed kernel inequalities supply elementary
remainder authority. See [DLMF 5.9](https://dlmf.nist.gov/5.9).

### BBP lower bound

Put `(d,v)=(3,2),(4,1),(5,1)`. Exact regrouping gives

$$
r(n)=\sum_{d,v}\frac{vd}{(8n-7)(8n-7+d)}
=\sum_{d,v}v\int_0^d\frac{du}{(8n-7+u)^2}.
$$

The probability law in the next section has mean 7/2, and represents
`T_n=E(8n+B)^(-2)`. Strict Jensen yields the claimed lower bound. The law is
nondegenerate, so the inequality is strict.

### BBP upper bound with a positive polynomial certificate

Strict source decrease gives T_n less than r(n+1)/15. Write

$$
P(n+1)=120n^2+151n+47,\quad
D(n+1)=(2n+1)(4n+3)(8n+1)(8n+5).
$$

Then the exact difference is

$$
\frac{(6n-1)^2}{2304n^4}-\frac{r(n+1)}{15}
=\frac{Q(n)}{34560n^4D(n+1)}.
$$

With m=n-1 its numerator is manifestly positive:

$$
Q(m+1)=188703+906498m+1686012m^2
+1519128m^3+664032m^4+112896m^5.
$$

This proves the upper inequality. The normalized ratio follows from the Euler upper bound.
`upper_bridge_polynomial_certificate` checks the identity against the actual combined
rational source. A separate SymPy expansion reproduced the six coefficients; dropped-pole
controls fail the authentic identity.

The source-derived expansions, justified by the moments below and Taylor remainders, are

$$
T_n=\frac1{64n^2}-\frac7{512n^3}+\frac{55}{4096n^4}+O(n^{-5}),
$$

$$
\frac{\epsilon_n^2}{16}-T_n
=\frac{13}{1536n^3}+O(n^{-4}),\qquad
\frac{16T_n}{\epsilon_n^2}
=1-\frac{13}{24n}+\frac{125}{192n^2}+O(n^{-3}).
$$

The coefficients come from the four poles and the geometric clock, not a fit.
In particular the leading tail is **1/(64 n^2)**.

## 6. The authentic source selects a shape-two Gamma law

### Exact probability measure, before any asymptotic limit

Define mu on B by

$$
\int f(B)d\mu
=\sum_{j\ge1}16^{-j}\sum_{d,v}v\int_0^d f(8j-7+u)du.
$$

Its mass is `(1/15)(2*3+4+5)=1`; its support is B at least 1. Equivalently,
take independent J and U with `Pr(J=j)=15*16^-j` and density
`sum v 1_[0,d](u)/15` for U, and put B=8J-7+U. Exact geometric and polynomial moments give

$$
\mathbb E B=\frac72,\quad \mathbb E B^2=\frac{55}{3},\quad
\mathrm{Var}(B)=\frac{73}{12},\qquad
\boxed{T_n=\mathbb E(8n+B)^{-2}}.
$$

This is an exact rewrite of the complete source, not moment matching. All moments of B
exist because J has a geometric tail.

Put a=8n and tilt the law by

$$
d\nu_n(B)=\frac{(a+B)^{-2}}{T_n}d\mu(B).
$$

Conditional on B, let X_n have Gamma density of shape 2 and rate a+B, and set Y_n=a X_n.
This auxiliary random variable represents the normalized positive tail kernel. It does not
turn the one actual deterministic arithmetic orbit into a random choice of trajectories.

For Re z greater than minus 2, the Euler integral yields

$$
\mathbb E Y_n^z=\Gamma(2+z)
\mathbb E_{\nu_n}\left(\frac a{a+B}\right)^z.
$$

Fubini is justified by the geometric B tail and integrability at zero. Differentiating gives

$$
\mathbb E\log Y_n=1-\gamma-\eta_n,\qquad
\eta_n=\mathbb E_{\nu_n}\log(1+B/a)>0.
$$

The relation lambda squared equals 1-lambda now gives the requested source-based identity:

$$
\boxed{\mathbb E[\log Y_n-\lambda^2]=\delta-\eta_n}.
$$

It is exact, with a source-defined shrinking correction. The reference lambda cancels from
eta_n. Consequently this identity gives delta a legitimate normalized-coordinate meaning
without proving it to be an invariant cancellation coefficient.

### Why shape two, rather than shape one?

The authentic endpoint polynomial is `P(t)=4-2t^3-t^4-t^5`. It has P(1)=0, and

$$
T_n=\int_0^\infty e^{-8nt}A(t)dt,\qquad
A(t)=\frac{e^{-t}P(e^{-t})}{16-e^{-8t}}
=t-\frac72t^2+\frac{55}{6}t^3+O(t^4).
$$

After scaling y=8nt, the normalized density tends to y exp(-y). The original source's
first-order zero supplies the extra y. Therefore the limit has logarithmic mean 1-gamma
and Laplace transform `(1+s)^(-2)`. Its positive Laplace fixed point solves

$$
s(1+s)^2=1,
$$

which is not the golden equation. Common-source ancestry does not make distinct transforms
or source-conditioned laws identical.

### The dynamic potential is explicit

The source reweighting really does change with n. Its potential and update are

$$
V_n(B)=2\log(8n+B),\qquad d\nu_n=T_n^{-1}e^{-V_n}d\mu,
$$

$$
\frac{d\nu_{n+1}}{d\nu_n}(B)
=\frac{T_n}{T_{n+1}}
\left(\frac{8n+B}{8n+8+B}\right)^2.
$$

The last ratio increases with B: later source time weakens the initial preference for
small B. This is a concrete normalized potential on an explicit source carrier. A proposed
potential on finite arithmetic paths likewise needs a declared path measure and a map
preserving the target phase; binary admissibility by itself fixes neither.

## 7. A second square-error theorem, with an explicit shrinking log correction

Because B is at least 1, and the inverse-square tilt is decreasing,

$$
\boxed{\log(1+1/a)\le\eta_n
\le\log(1+7/(2a))\le7/(2a)},\qquad a=8n.
$$

For the middle bound, the covariance of an increasing function f and a decreasing
weight w is nonpositive. Indeed, for independent B and B', twice that covariance equals
`E[(f(B)-f(B'))(w(B)-w(B'))]`. Apply it to `f=log(1+B/a)` and `w=(a+B)^(-2)`, then Jensen.

For a quantitative first-order remainder let x=B/a. Pointwise,

$$
\frac{\log(1+x)}{(1+x)^2}\ge\frac{x}{(1+x)^3}\ge x-3x^2.
$$

The numerator is nonnegative and its normalizer `E(1+x)^(-2)` is at most 1. Therefore

$$
\boxed{0\le\frac7{16n}-\eta_n\le\frac{55}{64n^2}}.
$$

Dominated convergence gives `a^2 T_n -> 1`, while this estimate gives `a eta_n -> 7/2`.
Thus a second source-error bridge is proved:

$$
\boxed{\frac{T_n}{\eta_n^2}\longrightarrow\frac4{49}},\qquad
\boxed{T_n\sim\frac4{49}
\left[\delta-\mathbb E(\log Y_n-\lambda^2)\right]^2}.
$$

Finite Taylor expansion, with the third B moment bounding the remainder, also gives

$$
\eta_n=\frac7{16n}-\frac1{3n^2}+O(n^{-3}).
$$

**Novelty and scope:** for any positive B with finite second moment, the analogous limit
is `1/(E B)^2`. The four-pole law fixes E B=7/2, hence 4/49. This is a useful analytic
specialization, not a uniqueness theorem for the BBP source.

### Finite certificates without gamma, lambda, or pi inputs

For j up to D, write b_j=8j-7. The unnormalized eta numerator has terms

$$
16^{-j}v\left[
\frac{1+\log((a+b_j)/a)}{a+b_j}
-\frac{1+\log((a+b_j+d)/a)}{a+b_j+d}\right].
$$

Each logarithm is enclosed by the existing rational artanh-series routine. The omitted
mu mass is exactly 16^-D, with B at least 8D+1. Its numerator is at most

$$
16^{-D}\min\left(\frac1{4a^2},\frac1{a(a+8D+1)}\right).
$$

Use the outward authentic Green interval for the denominator and divide positive
intervals. This is implemented in `tail_log_mixture_certificate`. The only infinite
authority is the proved tail bound; special-function numerics do not supply endpoints.

## 8. Mean drift and actual coherence have different orders

For the exponential log carrier and real c,t,

$$
K_c(t)=\mathbb E e^{it(c+\log X)}=e^{ict}\Gamma(1+it),\qquad
|K_c(t)|^2=\frac{\pi t}{\sinh(\pi t)}.
$$

The continuous value at zero is 1. The modulus is independent of c: a common center
rotates every phase together. The appearance of delta in the first cumulant therefore
does not make it a coherence loss. The classical modulus follows from
[DLMF 5.4.3](https://dlmf.nist.gov/5.4.E3) and the Gamma recurrence.

The exact source-relative factor is

$$
\mathbb E e^{it(\log Y_n-\lambda^2)}
=e^{-it\lambda^2}\Gamma(2+it)\Psi_n(t),\qquad
\Psi_n(t)=\mathbb E_{\nu_n}e^{-it\log(1+B/(8n))}.
$$

Put L=log(1+B/(8n)). With an independent copy L',
`1-|Psi|^2=E[1-cos(t(L-L'))] <= t^2 Var(L)`.
The same decreasing-tilt argument applied to L squared gives

$$
\boxed{1-|\Psi_n(t)|^2\le\frac{55t^2}{192n^2}}.
$$

Moreover, dominated convergence applied to the two-copy formula proves the sharp limit

$$
\boxed{n^2(1-|\Psi_n(t)|^2)\longrightarrow\frac{73t^2}{768}}.
$$

The domination is `a|log(1+B/a)-log(1+B'/a)| <= |B-B'|`; the tilted laws converge to mu
and have uniformly bounded density ratios for large a. The limiting variance is 73/12.

Thus eta_n has a harmonic first-order drift, but the fixed-frequency loss of modulus
is summable. Put C=55t^2/192, and choose n_0 at least 2 with C/n_0^2 at most 1/2.
Since `-log(1-x) <= 2x` for x at most 1/2,

$$
\boxed{\prod_{n\ge n_0}|\Psi_n(t)|
\ge\exp[-C/(n_0-1)]>0}.
$$

This excludes the direct attempt to multiply these fixed-t correction losses to zero.
It does not exclude a newly proved coupling at varying frequencies or signed cross-channel
transport. A proof of such a coupling must precede taking its logarithm.

To use the fixed factor `Gamma(2+it)` once at every arithmetic step, one would likewise
need a joint-law or operator-composition theorem preserving the selected character.
Its occurrence in each auxiliary marginal identity supplies no such factorization.
Choosing independent Gamma variables would define an additional probability model;
the arithmetic realization would still have to be identified with its observable.

For comparison, if `0 <= d_j <= 1-c` for a fixed c greater than zero, a product with
factors 1-d_j vanishes precisely when `sum d_j` diverges to positive infinity.
Losses of order j^-4 once per j are summable.
Even pure log-speed winding is insufficient: for real beta, an integral comparison gives

$$
\sum_{n\le N}n^{i\beta}
=\frac{N^{1+i\beta}}{1+i\beta}+O_\beta(\log N),\qquad
\frac{|\sum_{n\le N}n^{i\beta}|}{N}
\longrightarrow\frac1{\sqrt{1+\beta^2}}.
$$

### Moving frequencies: the normalized source circle really does cancel

There is a positive result once the frequency changes with the normalization. Split each
integer-length interval in mu into unit cells. Then exactly

$$
B=K+V,\qquad V\sim\operatorname{Uniform}[0,1],\qquad V\text{ independent of }K,
$$

$$
\Pr(K=8j-7+i)=16^{-j}c_i,\quad
(c_0,c_1,c_2,c_3,c_4)=(4,4,4,2,1),\quad j\ge1.
$$

The mass is one, E K=3, and Var K=6. This is the probability interpretation of the
inherited factorization
`P(t)=(1-t)(4+4t+4t^2+2t^3+t^4)` in the
[vacuum-parameter dossier](../2026-10-25/VACUUM_PARAMETER_BBP_KRYLOV.md).
In particular, B modulo one is exactly Haar: for every nonzero integer k,
`E_mu exp(-2 pi i k B)=0`.

Define an actual map and its source Fourier observable by

$$
q_n(B)=a\log(1+B/a)\pmod1,\qquad
\Theta_n(k)=\mathbb E_{\nu_n}e^{-2\pi i k a\log(1+B/a)}
=\Psi_n(2\pi k a),\quad a=8n.
$$

Thus `q_n` pushes the declared tilted source measure to the circle. Its target is this
auxiliary source distribution, not the selected arithmetic orbit.

**Theorem.** For every n at least 1 and every nonzero integer k,

$$
\boxed{|\Theta_n(k)|\le
\min\left(1,\frac{7+55\pi|k|/3}{a}
\left(1+\frac7{2a}\right)^2\right).}
$$

Consequently this source circle tends to Haar at every fixed nonzero integer frequency.
The same bound is uniform along nonzero integer k_n with `|k_n|=o(n)`.

**Proof.** Put w=(1+B/a)^(-2), D=E w=a^2 T_n, and tau=2 pi k. Subtract the exactly
zero character of B. The inequalities

$$
1-(1+x)^{-2}\le2x,\qquad
0\le B-a\log(1+B/a)\le B^2/(2a)
$$

give an unnormalized numerator bound `(2 E B+|tau| E B^2/2)/a`.
Jensen gives `D >= (1+E B/a)^(-2)`. Substitution proves the claim.
Replacing pi by 22/7 gives a purely rational finite upper bound, recorded in the receipt.

The first-order complex term is explicit:

$$
\boxed{a\Theta_n(k)\longrightarrow-\frac72-\frac{i}{2\pi k}}.
$$

Indeed, the unnormalized numerator after subtracting its zero limit has first-order
integrand `exp(-i tau B)(-2B+i tau B^2/2)`. Dominated convergence follows from the
integrable bound `2B+|tau|B^2/2`, so no unproved uniform Taylor remainder is needed.
The unit-cell decomposition gives

$$
\mathbb E[B e^{-i\tau B}]=\frac i\tau,\qquad
\mathbb E[B^2e^{-i\tau B}]=\frac{7i}\tau+\frac2{\tau^2}.
$$

It follows that the auxiliary coherence is directly tied to both shrinking errors:

$$
\boxed{\frac{\Theta_n(k)}{\eta_n}\longrightarrow
-1-\frac{i}{7\pi k}},\qquad
\boxed{\frac{|\Theta_n(k)|^2}{T_n}\longrightarrow
\frac{49}{4}+\frac1{4\pi^2k^2}}.
$$

This is a proved normalized log-to-circle error interface. The infinite-frequency
rescaling is essential: the earlier fixed-t positive-product result remains valid.
The generic Gamma factor supplies no part of this proof; it concerns the relative
source factor Psi_n itself.

The mechanism is broader than the authentic BBP source: any probability mixture of
positive integer-endpoint intervals with finite second moment has the analogous zero limit.
It is also unchanged when the arithmetic initial seed changes. The controls below
therefore remain mandatory before any selected-Weyl claim.

## 9. Rational nonnormal sources test what the new interfaces distinguish

Use the exact two-atom law

$$
\mu_* =\frac{73}{148}\delta_1+\frac{75}{148}\delta_{89/15}.
$$

It has the same mass, mean 7/2, second moment 55/3 and variance 73/12 as mu, but a
different third moment and a different full source. Define

$$
T_n^*=\mathbb E_{\mu_*}(8n+B)^{-2},\quad
r^*(n)=16T_{n-1}^*-T_n^*,\quad
U_n^*=16^nT_0^*-T_n^*.
$$

Then U_0^*=0, the recurrence is exact, r^*(n)>0, and the discounted future sum gives
T_n^* by telescoping. Both laws have the same tail expansion through n^-4, the same
eta expansion through n^-2, and the same leading relative-coherence loss 73t^2/(768n^2).

Nevertheless,

$$
T_0^*=\frac{4021}{7921},\qquad
e(7921U_n^*)=e(-7921T_n^*)\longrightarrow1.
$$

Its normalized Fourier sum at h=7921 tends to 1, proving failure of equidistribution.
The authentic four-pole source rejects the control already at n=1:

$$
r^*(1)-r(1)=\frac{697866100906}{140128866405}>0.
$$

This control pays the novelty tax: the new analytic bridges do not conceal an assumption
of normality. The actual source identity must remain load-bearing beyond finitely many moments.

The moving-frequency observable does distinguish this two-atom control: at k=15 both
`15 B` values are integers, so `Theta*_n(15) -> 1`, whereas the authentic value tends to zero.

### A stronger uniform-cell control also passes the moving-frequency theorem

Let V be uniform on [0,1], independently of K, with

$$
\Pr(K=1)=\frac12,\qquad \Pr(K=3)=\frac14,\qquad
\Pr(K=7)=\frac14,\qquad B=K+V.
$$

Here E K=3 and E K^2=15, so E B=7/2 and E B^2=55/3. B modulo one is exactly Haar.
This law passes the new moving-frequency cancellation, its sharp first-order coefficient,
and the previously matched tail/log/coherence asymptotics. Nevertheless its tail is rational:

$$
T_n^{\mathrm{cell}}=
\frac1{2(8n+1)(8n+2)}+
\frac1{4(8n+3)(8n+4)}+
\frac1{4(8n+7)(8n+8)},\qquad T_0^{\mathrm{cell}}=\frac{185}{672}.
$$

With the same construction `r_cell(n)=16 T_cell(n-1)-T_cell(n)` and
`U_cell(n)=16^n T_cell(0)-T_cell(n)`, the seed is zero and the forcing positive.
At h=672 its normalized Fourier sum tends to one. It is therefore nonnormal despite
passing the auxiliary moving-frequency theorem. The original source rejects it at once:
`r_cell(1)=974917/221760 != 47/15`.

Thus the new source-circle map closes a genuine analytic edge while leaving full source
and seed selection essential. Even the auxiliary circle's proved approach to Haar cannot
be promoted to equidistribution of the arithmetic orbit.

## 10. The finite virtual path is an extension with a carry cocycle

In abelian groups, the composable arrows `0 -> C16 -> C2 -> 0` fail exactness at C16.
The coherent exact sequence is

$$
\boxed{0\longrightarrow C_8\xrightarrow{u\mapsto2u}C_{16}
\xrightarrow{\bmod2}C_2\longrightarrow0}.
$$

It does not split: an element of order at most two in C16 is 0 or 8, and both have even
parity, so a homomorphic section cannot send 1 to parity 1.
With the set section b maps to b, write a=2u+b. Addition becomes

$$
\boxed{(u,b)+(v,d)=(u+v+bd\bmod8,\ b\mathbin{\oplus}d)}.
$$

The carry bd is a nontrivial cocycle. A normalized coboundary at (1,1) is 2t modulo 8,
which cannot equal 1. Omitting the carry changes the group to a split extension.
The character e(ha/16) descends through parity exactly when 8 divides h.

An exact phase control: delta_0 and `(delta_0+delta_2)/2` have the same parity readout.
At h=4 their Fourier energies are respectively 1 and 0. The phase of the fiber is
therefore indispensable for this target. `cyclic_carry_extension.py` implements the
maps and checks all additions, not just the shape of the diagram.

### The signed triangle needs a declared boundary space

On the projective real line there is one infinity: positive and negative infinity are
the same projective point, though the direction of approach can be retained. The maps
`x -> 1/x`, `x -> 1-x`, and `x -> -x` give explicit exchanges of the marked points.
For example inversion exchanges 0 and infinity and fixes plus/minus 1; sign reversal
exchanges plus/minus 1 and fixes 0 and projective infinity.

If two distinct infinities are wanted, use the two-ended extended real line and retain
separate one-sided zero boundary data for inversion. For nonzero real multiplication,
the exact logarithmic chart is `(sign x, log|x|)` in `C2 x R`. The sign multiplies and
the log magnitude adds. These are workable signed mirrors with explicit domain and
gluing rules; they do not by themselves select the BBP phase measure.

## 11. Two inherited shortcuts are now explicitly corrected

### The raw frequency ladder is a time shift

For any recurrence x_(n+1)=b x_n+r_(n+1), define S_N(h)=sum e(hx_n). Exact telescoping gives

$$
S_N(bh)-S_N(h)=e(hx_{N+1})-e(hx_1)
+\sum_{n=1}^Ne(hx_{n+1})[e(-hr_{n+1})-1].
$$

For the authentic BBP source, `r(n+1) <= 15/(64n^2)`. Saturating each phase error at 2
before summing yields, with A_N=S_N/N,

$$
\boxed{|A_N(16h)-A_N(h)|
\le\frac{2+\sqrt{105|h|/8}}N}.
$$

Proof: `|e(x)-1| <= min(2,7|x|)` and
`sum_(n>=1) min(2,C/n^2) <= integral_0^infinity min(2,C/x^2)dx = 2 sqrt(2C)`.
The code also gives a slightly looser rational split bound using integer square roots.
The saturation method is inherited from the
[spectral-purity dossier](../2026-10-25/OPERATION_SPECTRAL_PURITY.md); this application
audits the ladder. It is uniform on prescribed bands h=o(N^2), not arbitrary frequencies.

At fixed h, a uniform ratio `|A_N(16h)| <= q |A_N(h)|` with q less than 1 already implies
`S_N(h)=O_h(1)`, by reverse triangle. It is a strong missing cancellation premise.
For a fixed finite rational history, the literal `limsup_(h->infinity)` contraction
target is **REFUTED**: multiples of its common denominator make both averages equal 1.
Moreover, one-way upper bounds at higher frequencies alone do not bound the initial
low frequency. The uniform measure on `{0,1/48,1/24}` has a nonzero coefficient at 1,
but zero coefficients at every 16^k for k at least 1.

`ladder_shift_audit.py` checks the identity in the exact rational phase algebra, rejecting
histories that do not obey their independently declared forcing.

### Even h does not remove cross-digit fourth-order dependence

The old one-digit Walsh identity is valid. Its proposed extension to a full word from
only order-at-most-three marginals is false. Let

$$
K=\sum_{i=0}^72^i\varepsilon_i,\quad A=\{0,4,5,6\},\quad
p(\varepsilon)=2^{-8}[1+(-1)^{\varepsilon_0+\varepsilon_4+\varepsilon_5+\varepsilon_6}].
$$

This is uniform on 128 words. All 92 subsets of one, two or three bits are uniformly
distributed, as is each complete four-bit digit. Yet at the even frequency h=2, with
zeta=exp(2 pi i/128),

$$
\mathbb E e(2K/256)=2^{-8}
\prod_{i\in A}(1-\zeta^{2^i})\prod_{i\notin A}(1+\zeta^{2^i})\ne0.
$$

The only potentially vanishing minus factor is i=7, which is absent from A; the only
potentially vanishing plus factor is i=6, which is in A. An independent exact reduction
modulo `Phi_128(X)=X^64+1` gives a nonzero polynomial of degree below 64.
Both digit marginals are uniform, so the two-digit law also extends to a stationary
Markov digit process. It is a consistent finite countermodel, not an authentic BBP history.

The full growing-band gate also requires a rate: a uniform mode bound 1-c_N is sufficient
only if `H_N(1-c_N)^2 -> 0`. Merely c_N tending to 1 is not sufficient for that gate.
No claim is made that the candidate approaches in the earlier handoff exhaust all routes.

## 12. Claim ledger and the next dependency cut

| Claim | Earned status | Residual obligation |
|---|---|---|
| Finite beta common source for e, gamma and golden fixed point | CLASSICAL ingredients; PROVED PAPER finite bounds; exact finite implementation | Does not identify a unique source from a finite moment prefix |
| All-n BBP/Euler square comparison | PROVED PAPER, source polynomial certificate | Does not estimate selected signed sums |
| Exact BBP Gamma-2 mixture, dynamic potential and eta bounds | PROVED PAPER; exact rational enclosures | Auxiliary source measure is not the distribution of arithmetic orbit phases |
| T_n/eta_n squared tends to 4/49 | PROVED PAPER, general mixture theorem specialized to four poles | Matching the coefficient does not authenticate the source |
| Delta intrinsically produces cancellation | UNVERIFIED; common-centering version REFUTED by modulus invariance | Need a source-derived relative-phase law |
| Fixed-t relative Mellin losses multiply to zero | REFUTED by explicit positive lower bound on a late product | The proved moving-frequency auxiliary theorem still needs selected-observable transport |
| Normalized source-circle modes Theta_n(k) cancel, with explicit first-order error | PROVED PAPER: O_k(1/n), Theta_n/eta_n -> -1-i/(7 pi k) | Applies to a source pushforward; the uniform-cell nonnormal control also passes |
| Specified binary BBP layers derive lambda squared without inserting it | PROVED PAPER in the [atomic continuation](FOUR_POLE_ATOMIC_SUBSTRATE.md): minimal fixed point of G(z)=1/(2-z)^2 | Source-preserving packet changes alter the fixed point; no ungraded invariance or arithmetic cancellation follows |
| Matched-moment rational zero-seed control is nonnormal | PROVED PAPER; exact finite source mismatch and recurrence checks | Control deliberately violates the full four-pole source |
| Uniform-cell control passes all displayed auxiliary asymptotics but is nonnormal | PROVED PAPER; rational T_0=185/672 and h=672 obstruction | Source-circle cancellation alone does not preserve the arithmetic target |
| Carry extension and character descent | CLASSICAL finite algebra; exact exhaustive checks | Feasibility needs a specified amplitude/measure for the target |
| Literal unbounded-frequency ladder contraction | REFUTED on authentic finite histories | A restricted alternative must state all frequency and time quantifiers |
| Marginal-only even-mode shortcut | REFUTED by exact two-digit countermodel | Retain the cross-digit signed interactions |
| Selected pi Weyl cancellation / normality / RH | OPEN | No promotion from the preceding analytic results |

The useful new target is an explicit transport from the now-proved moving-frequency
source-circle observable Theta_n, or the relative Mellin factor Psi_n,
to a declared signed **joint carry observable**, preserving all original source information.
Its first test is an actual identity and residual estimate, not a proposed inequality that
already assumes normality. It must distinguish the exact-forcing changed-seed control
and both zero-seed matched-moment controls, including the uniform-cell law that passes
Theta cancellation. If the transport exists, its source-specific signed
estimate remains a separate obligation. See the
[next-round handoff](../../handoffs/FOUR_POLE_ATOMIC_NEXT_2026-10-26.md), which also
retains the newly constructed atomic and finite-polynomial interfaces.

The exact remaining nonlinear step can now be written on one carrier. The mixture formula
also holds at n=0, where T_0=pi/16. Thus the zero-initialized arithmetic realization is

$$
U_n=\mathbb E_\mu\left[\frac{16^n}{B^2}-\frac1{(8n+B)^2}\right].
$$

The selected character is the exponential of this expectation. The relative Mellin
factor is an expectation of exponentials of a different function. Those two operations
do not commute: for a variable taking 0 and 1/2 with equal weights, `e(E X)=i` while
`E e(X)=0`. Consequently a source measure plus attenuation of its own characteristic
function does not automatically transport attenuation to the arithmetic orbit. A useful
new map must account for this nonlinear observable and its zero-initialized realization.

## 13. Reproduction, sources, and validation provenance

Production files are `exponential_gamma_bridge.py`, `bbp_log_mixture.py`,
`cyclic_carry_extension.py`, and `ladder_shift_audit.py` under `observational_succ`.
Each has a corresponding test module. The older ratio instrument remains callable with
its corrected interpretation. The original source functions and frozen provenance are untouched.

The exact [receipt](OILY_MACARONI_RECEIPT.json) is generated by
`scripts/oily_macaroni_probe.py`; replay with `--verify` rejects modified evidence.
It records source hashes, parameters, outward rational decimal intervals, exact controls,
and explicit nonclaims. The [independent oracle](independent_mixture_oracle.py) does not import
the new production modules; its Decimal values are diagnostics, not certificates.
The [moving-frequency diagnostic](normalized_frequency_independent.py) separately
evaluates the complex endpoint integral and oscillatory quadrature, including both
counterfeits; its [actual output](normalized_frequency_independent.json) is also numerical
evidence rather than a proof certificate.
Actual commands, results, environment and baseline failures are recorded in
[VALIDATION.md](VALIDATION.md). No hosted result is claimed before it is observed.

Primary classical sources used: [Euler Gamma integral](https://dlmf.nist.gov/5.2.E1),
[beta integral](https://dlmf.nist.gov/5.12.E1), [digamma values](https://dlmf.nist.gov/5.4),
[Gamma/digamma series](https://dlmf.nist.gov/5.7),
[digamma integral representations](https://dlmf.nist.gov/5.9),
[asymptotic expansions and remainder domains](https://dlmf.nist.gov/5.11), and
[Gamma infinite products](https://dlmf.nist.gov/5.8).
The source-specific proofs above are provided in full; these references do not claim
the BBP/carry transport or normality theorem on our behalf.

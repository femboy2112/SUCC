# Causal negative orders, endpoint parity, and the BBP source

**Date:** 2026-11-15. **Inspected source head:** `55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`.

**Initial hole state:** UNVERIFIED. Can the positive causal-volume construction, and specifically its Gamma endpoint shapes, explain negative orders and the negative-even zeros of zeta without silently replacing the source?

**Result:** there are exact classical bridges from positive-order causal kernels to negative-order distributions, and from endpoint parity to negative-even Mellin zeros. SUCC's inherited universal Pascal carrier already aggregates positive causal faces into the eta kernel and recovers zeta's negative-even zeros. The authentic BBP source fails that parity criterion: its native exponent family has precisely one real zero, at zero. Its growing finite-difference faces do have a locally uniform reciprocal-Gamma limit, proved below, but that limit selects **all** nonpositive integer zeros. Applying the universal carrier's same positive geometric grade average to those authentic BBP faces gives the nonzero value `8` at order `-2`; the universal eta construction therefore supplies a concrete comparison without identifying the two sources.

These are mathematical source distinctions. None asserts negative physical elapsed time, negative probability, selected-digit cancellation, normality, or RH.

## 1. Hole contract and the objects that must remain distinct

The exact question is whether the authentic source admits a proved map carrying its positive causal volumes to a function with zeros at every negative even integer. The cheapest discriminator is the first nontrivial even endpoint coefficient, followed by an all-order sign or symmetry proof. The desired implication is not licensed merely by a shared Gamma factor.

| Object | Operation producing it | What its index means |
| --- | --- | --- |
| `Gamma(k+2)` endpoint face | Multiply the source density by `(1-x^8)^k` | A finite-difference order, adding `k` endpoint zeros |
| `Gamma(2j)` endpoint convolution | Convolve `j` copies of the lag kernel with first-order zero | Number of independent lag factors |
| `Gamma(alpha)` causal normalization | Continue ordered integral kernels in their order | Integral/derivative order |
| `Gamma(s)` in a Mellin transform | Normalize a positive-lag Mellin observation | Complex exponent of the lag variable |
| `Gamma(s/2)` in completed zeta | Mellin-transform a Gaussian quadratic lattice | The quadratic spectral scaling `n^2` |

The first two rows are already distinguished in the preceding round's [provenance note](../bbp_volume_algebra/PROVENANCE.md). In particular, `k -> k+2`, `j -> j+1`, and `s -> s/2` are different maps on different objects.

## 2. Negative causal orders from positive causal kernels

For `Re(alpha)>0`, define the distribution supported on the forward half-line

\[
g_\alpha(t)=\frac{t_+^{\alpha-1}}{\Gamma(\alpha)},\qquad
\langle g_\alpha,\varphi\rangle
=\frac1{\Gamma(\alpha)}\int_0^\infty t^{\alpha-1}\varphi(t)\,dt,
\quad \varphi\in C_c^\infty(\mathbb R).
\]

For real positive `alpha` this is a positive, locally finite causal kernel. It is not a probability density on the whole half-line without an additional exponential weight.

### Entire continuation and the negative integers

Subtract the first `N` Taylor terms of the test function at zero:

\[
\begin{aligned}
\langle g_\alpha,\varphi\rangle
=\frac1{\Gamma(\alpha)}\bigg[&
\int_0^1t^{\alpha-1}\left(\varphi(t)-
\sum_{r=0}^{N-1}\frac{\varphi^{(r)}(0)}{r!}t^r\right)dt\\
&+\int_1^\infty t^{\alpha-1}\varphi(t)dt
+\sum_{r=0}^{N-1}\frac{\varphi^{(r)}(0)}{r!(\alpha+r)}\bigg].
\end{aligned}
\tag{D1}
\]

This continues the expression to `Re(alpha)>-N`. The apparent simple poles at `alpha=-r` cancel the simple zeros of `1/Gamma(alpha)`. Since its local coefficient is `(-1)^r r!`, the continued value is

\[
\langle g_{-r},\varphi\rangle=(-1)^r\varphi^{(r)}(0),
\qquad g_0=\delta,\qquad g_{-r}=\delta^{(r)}.
\tag{D2}
\]

Because `N` is arbitrary, this gives an entire distribution-valued family. The Beta identity first gives `g_alpha*g_beta=g_(alpha+beta)` for positive real parts. Differentiation, `Dg_alpha=g_(alpha-1)`, extends that law to all complex orders; convolution is well-defined because both supports are bounded on the same side.

This is the classical Gel'fand–Shilov/Riemann–Liouville construction, not a new definition. A directly verified primary paper is [Lei Li and Jian-Guo Liu, *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*, SIAM J. Math. Anal. 50 (2018), 2867–2900](https://sites.math.duke.edu/~jliu/pdf/Li_Liu_SIMA_2018.pdf), DOI `10.1137/17M1160318`: Lemmas 2.2–2.4 and Proposition 2.5 establish the causal distribution convolution group for real orders. For the entire complex family and equations `g_(-n)=delta^(n)`, `g_alpha*g_beta=g_(alpha+beta)`, see [Chenkuan Li and Changpin Li, *The fractional Green's function by Babenko's approach*](https://people.brandonu.ca/lic/files/2020/08/tmj13_3_3.pdf), Tbilisi Mathematical Journal 13(3) (2020), equations (5)–(7), citing the classical distribution theory.

### What is preserved, and what changes

Support remains inside `[0,infinity)`, including at negative order. Positivity does not: derivatives of delta of positive order are not positive measures. A forward-supported finite-difference realization makes the signed step visible:

\[
\frac{\delta_0-\delta_h}{h}\longrightarrow\delta',\qquad
\frac1{h^r}\sum_{j=0}^r(-1)^j\binom rj\delta_{jh}
\longrightarrow\delta^{(r)},\quad h\downarrow0.
\]

Each location is forward of the origin, but the coefficients are signed. Positivity alone cannot yield these limits in the space of distributions: a limit of positive distributions is positive.

The causal boundary is retained by differentiating the zero extension. For smooth `f`,

\[
D(\mathbf1_{t\ge0}f(t))
=\mathbf1_{t\ge0}f'(t)+f(0)\delta.
\tag{D3}
\]

Dropping the delta changes the inverse law. Thus a negative order is a derivative/inverse in a declared algebra of causal distributions; it is not a backward walk through already-realized history.

## 3. Endpoint jets determine negative-integer Mellin values

Let `K` be smooth on the positive half-line, rapidly decreasing at infinity, and have an analytic Laurent germ at zero with only finitely many negative powers:

\[
K(t)=\sum_{j=-p}^{\infty}a_jt^j.
\]

Initially define

\[
M_K(s)=\int_0^\infty t^{s-1}K(t)dt,
\qquad Z_K(s)=\frac{M_K(s)}{\Gamma(s)},\quad \Re s>p.
\]

Finite endpoint subtraction gives, for every sufficiently large integer `N`,

\[
M_K(s)=\int_0^1t^{s-1}\left(K(t)-\sum_{j=-p}^Na_jt^j\right)dt
+\int_1^\infty t^{s-1}K(t)dt
+\sum_{j=-p}^N\frac{a_j}{s+j}.
\tag{J1}
\]

The first integral is holomorphic for `Re(s)>-N-1`, and the second is entire. Consequently the residue of `M_K` at `s=-m` is `a_m`. Cancellation with reciprocal Gamma proves

\[
\boxed{Z_K(-m)=(-1)^m m!a_m\qquad(m=0,1,2,\ldots).}
\tag{J2}
\]

For a kernel analytic at zero this is `Z_K(-m)=(-1)^m K^(m)(0)`. The finite subtraction proves each value and its domain; finite sampled coefficients do not prove an infinite parity pattern.

This is the standard direct Mellin mapping principle. See [Flajolet, Gourdon and Dumas, *Mellin transforms and asymptotics: Harmonic sums*](https://algo.inria.fr/flajolet/Publications/FlGoDu95.pdf), Theorem 3, and the authors' [corrigenda](https://algo.inria.fr/flajolet/Publications/mellin-harm-corr.pdf). The proof above uses only the simple-power case and states the subtraction explicitly.

### Exact parity criterion

Let `K_reg(t)=K(t)-sum_(j<0) a_jt^j`. Then

\[
\bigl[Z_K(-2n)=0\text{ for every }n\ge1\bigr]
\iff
\bigl[K_{\rm reg}(t)+K_{\rm reg}(-t)=2a_0
\text{ as analytic germs}\bigr].
\tag{J3}
\]

Indeed, the left side says every positive even coefficient is zero; analyticity makes that equivalent to a constant plus an odd analytic germ. If the principal part is itself odd, one can use `K` instead of `K_reg`. For a merely smooth kernel, vanishing of all even jets is still the criterion for the values (J2), but need not imply a full reflection identity because flat terms can remain.

### Zeta's negative-even zeros without assuming its functional equation

Take the positive kernel

\[
K_\zeta(t)=\frac1{e^t-1}=\sum_{n\ge1}e^{-nt},\qquad t>0.
\]

For `Re(s)>1`, absolute convergence gives

\[
\frac1{\Gamma(s)}\int_0^\infty
\frac{t^{s-1}}{e^t-1}dt=\sum_{n\ge1}n^{-s}=\zeta(s).
\]

Now use the exact identity

\[
K_\zeta(t)+K_\zeta(-t)=-1.
\]

Its principal part is `1/t`, which is odd. Therefore (J3) proves `zeta(-2n)=0` for every positive integer `n`. No functional equation was assumed. In Bernoulli notation,

\[
K_\zeta(t)=t^{-1}-\frac12+
\sum_{n\ge1}\frac{B_{2n}}{(2n)!}t^{2n-1},
\]

and (J2) also gives `zeta(0)=-1/2`, `zeta(-1)=-1/12`. The primary reference formulas are [DLMF 25.5.1](https://dlmf.nist.gov/25.5#E1) for the convergent positive-kernel integral and [DLMF 24.2.1–2](https://dlmf.nist.gov/24.2) for the Bernoulli generating function and parity. The latter parity also follows immediately from the displayed reflection identity.

### Inherited positive grade aggregation: eta from universal faces

The repository already has an exact construction using positive forward-lag faces, rather than only the Bose-kernel comparison. In [ZETA_NEGATIVE_INTEGER_TANGENT_FAMILY.md](../../2026-10-30/universal_nz_carrier/ZETA_NEGATIVE_INTEGER_TANGENT_FAMILY.md), ZT1–ZT3, define

\[
f_n(t)=e^{-t}(1-e^{-t})^n,\qquad
F_n(s)=\sum_{j=0}^n(-1)^j\binom nj(j+1)^{-s}.
\]

For `Re(s)>-n`, the ordinary Mellin integral gives `F_n(s)=M[f_n](s)/Gamma(s)`, with values at Gamma poles interpreted using the entire reciprocal Gamma function. Each `F_n` is entire by its finite exponential sum. The positive geometric average is exactly

\[
\sum_{n\ge0}2^{-n-1}f_n(t)
=\frac{e^{-t}/2}{1-(1-e^{-t})/2}
=\frac1{e^t+1}=:K_\eta(t),\qquad t>0.
\tag{J5}
\]

Consequently

\[
\eta(s)=\sum_{n\ge0}2^{-n-1}F_n(s)
=\frac{M[K_\eta](s)}{\Gamma(s)},
\tag{J6}
\]

where the ordinary integral holds for `Re(s)>0` and the series converges locally normally on the entire plane. To verify the latter assertion on a compact set `S`, choose an integer `N` with `N+min_(s in S) Re(s)>0`. For every `n>=N`, `0<=f_n<=f_N`; the Mellin integrals on `S` then have one finite integrable majorant, and `1/Gamma(s)` is bounded on `S`. The factors `2^(-n-1)` give a summable uniform bound. This also justifies termwise analytic differentiation.

The reflected germ obeys `K_eta(t)+K_eta(-t)=1`. The endpoint criterion therefore gives `eta(-2r)=0` for every integer `r>=1`. At each nonnegative integer `m`, all grades `n>m` vanish, so

\[
\eta(-m)=\sum_{n=0}^{m}2^{-n-1}F_n(-m),\qquad
\zeta(-m)=\frac{\eta(-m)}{1-2^{m+1}}.
\tag{J7}
\]

The denominator is nonzero at every such order. Globally, `zeta(s)=eta(s)/(1-2^(1-s))` is a meromorphic identity with the appropriate removable interpretations at the nonreal zeros of the denominator. The positive Fermi-kernel integral is [DLMF 25.5.3](https://dlmf.nist.gov/25.5#E3).

The face family, Euler/Hasse expansion, local normal convergence near negative integers, and finite-grade value truncation are inherited SUCC results, explicitly classical in the cited dossier. Their combination with the elementary reflection in (J5) is a source-faithful positive causal-volume derivation of the even zero pattern. It uses the universal integer carrier's specified one-step spectrum and grade weights; the BBP source requires its own comparison below.

### Contour and theta translations

The same continuation can be represented by the [Hankel formula, DLMF 25.5.20](https://dlmf.nist.gov/25.5#E20):

\[
\zeta(s)=\frac{\Gamma(1-s)}{2\pi i}
\int_{-\infty}^{(0+)}\frac{z^{s-1}}{e^{-z}-1}dz,
\qquad s\notin\{1,2,\ldots\}.
\]

The contour goes around the origin positively and excludes the other poles `+/-2pi i,+/-4pi i,...`; branch values must be transported consistently. At a nonpositive integer, the local residue recovers the same endpoint coefficient. This makes a contour interpretation of a turn around the analytic origin precise. It does not identify that complex contour with a physical causal path.

For comparison, set `omega(t)=sum_(n>=1) exp(-pi n^2 t)`. The Gaussian lattice gives `M[omega](s/2)=pi^(-s/2)Gamma(s/2)zeta(s)`, initially for `Re(s)>1`. Poisson/theta inversion yields the continuation

\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\frac1{s(s-1)}+
\int_1^\infty\omega(t)
\left(t^{s/2}+t^{(1-s)/2}\right)\frac{dt}{t}.
\tag{J4}
\]

The right side is regular at negative even integers; the poles of `Gamma(s/2)` then force the zeros. See [DLMF 20.7.32](https://dlmf.nist.gov/20.7#E32) for theta inversion and [DLMF 25.5.13–14](https://dlmf.nist.gov/25.5#E13) for (J4). This route derives the reflection formula from a declared self-dual lattice input. The half-argument arises from the quadratic spectrum `n^2`, not from the shape-two endpoint of an arbitrary positive source.

## 4. Applying the criterion to the original BBP source

Use distinct notation for the four-pole Laplace response and the compact source density:

\[
q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t},\qquad
\mathcal R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},
\]

\[
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8},\qquad 0\le x\le1.
\]

For `a>0`, the normalized Mellin observation of the tilted lag kernel is entire:

\[
Z_a(s)=\frac1{\Gamma(s)}\int_0^\infty
t^{s-1}e^{-at}q(t)dt
=4a^{-s}-2(a+3)^{-s}-(a+4)^{-s}-(a+5)^{-s}.
\tag{B1}
\]

Termwise Gamma integration first proves the identity for `Re(s)>0`; the source endpoint cancellation extends the integral to `Re(s)>-1`, and the finite exponential sum supplies its entire continuation. For every integer `m>=1`,

\[
Z_a(-m)=4a^m-2(a+3)^m-(a+4)^m-(a+5)^m<0.
\tag{B2}
\]

The strict sign is termwise monotonicity of the power, rather than a finite numerical extrapolation. In particular `Z_a(-2)=-59-30a`, so the even parity already fails at the second jet.

The exact compact-density jets give another direct source check:

| Kernel | derivative orders `0,1,2,3,4` at zero |
| --- | --- |
| `R(e^(-t))` | `0, 1, -5, 37, -413` |
| `e^(-t)R(e^(-t))` | `0, 1, -7, 55, -595` |

These were independently calculated by applying `-x d/dx` repeatedly to the literal rational `R(x)` and evaluating at `x=1`. The unweighted first kernel tends to `1/4` at infinity, so its initial Mellin strip is `-1<Re(s)<0`; it does not satisfy the rapid-tail hypothesis of section 3. The second kernel has exponential decay and is the correctly transported `dx` source measure. Its normalized Mellin value at `-2` is `-7`.

### The native entire exponent family: a stronger obstruction

For `0<=z<1`, set `A_n=8n+1` and

\[
\mathcal B_z(s)=\sum_{n\ge0}z^n
\left[4A_n^{-s}-2(A_n+3)^{-s}
-(A_n+4)^{-s}-(A_n+5)^{-s}\right].
\tag{B3}
\]

The series converges locally uniformly for all complex `s`: on a compact set each summand is bounded by a fixed polynomial in `n` times `z^n`. Thus it is entire. This analytic family and its original-source value `B_(1/16)(1)=pi` are **already explicit** in [EULER_MASCHERONI_BBP_REGULATOR.md](../../2026-10-24/EULER_MASCHERONI_BBP_REGULATOR.md), section 2, equation (3), with the exact Lerch interpretation. The existing production module is [euler_bbp_regulator.py](../../../observational_succ/euler_bbp_regulator.py); its finite exact interface restricts the exponent to nonnegative integers.

The following full-real sign conclusion is a direct extension of that dossier's positive-difference equation (4). Define a nonnegative weight on `u>=0`:

\[
W_z(u)=\sum_{n\ge0}z^n\left[
2\mathbf1_{[\log A_n,\log(A_n+3)]}(u)
+\mathbf1_{[\log A_n,\log(A_n+4)]}(u)
+\mathbf1_{[\log A_n,\log(A_n+5)]}(u)\right].
\]

For every complex `s`,

\[
\boxed{\mathcal B_z(s)=s\int_0^\infty e^{-su}W_z(u)\,du.}
\tag{B4}
\]

The identity follows by integrating `s exp(-su)` on each interval. The positive weight is nonzero and has all exponential moments because of the geometric regulator. Therefore, on the whole real axis,

\[
\operatorname{sign}\mathcal B_z(s)=\operatorname{sign}s,
\quad s\ne0;\qquad
\mathcal B_z'(0)=\int W_z(u)du>0.
\tag{B5}
\]

**The only real zero is the simple zero at zero.** No negative-even zeta pattern occurs in this native source family. This statement is a new explicit corollary in these notes of the inherited three-difference representation, not a new family or a new general transform theorem.

At `z=1/16`, its positive heat kernel is exactly

\[
H(t)=\frac{e^{-t}q(t)}{1-e^{-8t}/16}
=16e^{-t}R(e^{-t}),
\]

and `B_(1/16)(s)=M[H](s)/Gamma(s)` by endpoint continuation. Thus

\[
\mathcal B_{1/16}(-1)=-16,\quad
\mathcal B_{1/16}(-2)=-112,\quad
\mathcal B_{1/16}(-3)=-880,\quad
\mathcal B_{1/16}(-4)=-9520.
\]

These negative values are ordinary absolutely convergent signed power sums. Zeta's unweighted power sums diverge there and need a different continuation. Removing the geometric regulator is a substantive change of limit: the inherited unregulated Hurwitz combination has value `15/8` at zero, whereas `B_z(0)=0` for every `z<1`. Neither the endpoint nor its limit may be silently interchanged.

## 5. Finite-difference faces: consecutive zeros and a reciprocal-Gamma limit

Set

\[
H_k(t)=H(t)(1-e^{-8t})^k,\qquad
B_k(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}H_k(t)dt,
\quad k=0,1,\ldots.
\tag{F1}
\]

The integral itself converges for `Re(s)>-k-1`. For fixed `k`, expansion of the finite factor and of the geometric denominator supplies an entire exponent series, so `B_k` has a definite entire continuation. Since `H(t)=16t+O(t^2)`,

\[
H_k(t)=16\,8^k t^{k+1}+O(t^{k+2}).
\]

Consequently (J2) gives zeros at `s=0,-1,...,-k`, and the first surviving value is

\[
B_k(-k-1)=(-1)^{k+1}(k+1)!\,16\,8^k.
\]

These are consecutive endpoint zeros, not an even subsequence.

### Positive rate measure proves the full real-zero set

The exact identities

\[
\frac{q(t)}t=2\int_0^3e^{-ut}du+\int_0^4e^{-ut}du+\int_0^5e^{-ut}du,
\qquad
\frac{1-e^{-8t}}t=\int_0^8e^{-ut}du
\]

give `H_k(t)=t^(k+1) integral exp(-lambda t) mu_k(dlambda)`. Explicitly, `mu_k` is the convolution of:

- the unit mass at `1`;
- `2` times Lebesgue measure on `[0,3]`, plus Lebesgue measure on `[0,4]` and `[0,5]`;
- `k` copies of Lebesgue measure on `[0,8]`;
- the positive discrete measure `sum_(n>=0)16^(-n) delta_(8n)`.

It is supported on `[1,infinity)`, has total mass `16*8^k`, and has all polynomial moments. Its geometric tail gives an entire function `A_k(s)=integral lambda^(-s-k-1) mu_k(dlambda)`, positive for every real `s`. Gamma integration gives

\[
\boxed{B_k(s)=(s)_{k+1}A_k(s),\qquad
(s)_{k+1}=s(s+1)\cdots(s+k).}
\tag{F2}
\]

This identifies the real zeros exactly: `0,-1,...,-k`, each simple. The positive-rate representation proves the claim beyond the finite endpoint computations.

### F3 — a growing face approaches reciprocal Gamma on the entire plane

Let `Z_k=B_k(1)=integral H_k(t)dt`, let `T_k` have density `H_k/Z_k`, and put `a_k=(log k)/8` for `k>=2`. Then

\[
\boxed{
a_k^{1-s}\frac{B_k(s)}{B_k(1)}
\longrightarrow\frac1{\Gamma(s)}
\quad\text{locally uniformly on }\mathbb C.
}
\tag{F3}
\]

This limit is source-specific but uses classical Beta concentration and Mellin arguments. The proof below does not infer a universal statement from a numerical fit.

**Step 1: exact transformed positive density.** Write `alpha=1/8`, `y=e^(-8t)`. Then

\[
H_k(t)dt=w(y)y^{\alpha-1}(1-y)^kdy,
\quad
w(y)=\frac{4-2y^{3/8}-y^{1/2}-y^{5/8}}{8(1-y/16)},
\tag{F4}
\]

with the orientation reversed in the integration limits. The function `w` is bounded, nonnegative and continuous on `[0,1]`, and `w(0)=1/2`. After `v=ky`, dominated convergence using `(1-v/k)^k<=exp(-v)` proves

\[
Z_k\sim\frac{\Gamma(1/8)}{2k^{1/8}},\qquad
k e^{-8T_k}\ \Rightarrow\ G_{1/8},
\tag{F5}
\]

where `G_(1/8)` is a Gamma variable of shape `1/8` and rate one. The same argument applies to bounded continuous test functions. Hence

\[
T_k-a_k\Rightarrow-\frac18\log G_{1/8},\qquad
X_k:=T_k/a_k\longrightarrow1\quad\text{in probability}.
\tag{F6}
\]

**Step 2: every fixed positive and inverse power is uniformly integrable for sufficiently large `k`.** For any fixed `r>0`, bound the positive-power tail at `T_k>2a_k` using `H_k(t)<=C exp(-t)` and `Z_k` from (F5). Its contribution to `E[X_k^r]` is `O_r(k^(-1/8))`. On the complement, `X_k^r<=2^r`. The threshold may depend on the power; no finiteness of every inverse moment at each small depth is claimed.

For inverse powers, split at `y=k^(-1/2)`. Below that threshold `X_k>=1/2`. Above it, `-log y>=1-y`, so the inverse-power tail is bounded by

\[
\frac{C(\log k)^r}{Z_k}
\int_{k^{-1/2}}^1y^{\alpha-1}(1-y)^{k-r}dy
\le
\frac{C(\log k)^r e^{-\sqrt{k}/2}}{Z_k}
\mathrm B(\alpha,k/2-r+1).
\tag{F7}
\]

For sufficiently large `k` the Beta argument is positive. More explicitly, for `k>2r`, the Beta integral and `(1-y)^M<=exp(-My)` give `B(alpha,k/2-r+1)<=Gamma(alpha)/(k/2-r)^alpha`. Thus the Beta factor is `O_r(k^(-alpha))`, whereas `Z_k` is asymptotic to a positive constant times the same power. Hence (F7) tends to zero. Applying these bounds at a power larger than any prescribed one supplies uniform integrability for that smaller power.

**Step 3: compact sets of complex exponents.** On a compact `S subset C`, the magnitudes of `X_k^(s-1)` are dominated by fixed positive and inverse powers of `X_k`. Near `X_k=1`, `X_k^(s-1)` converges to `1` uniformly for `s in S`; outside a small neighborhood, the moment bounds and (F6) control the expectation uniformly. Therefore

\[
\sup_{s\in S}\left|\mathbb E[X_k^{s-1}]-1\right|\to0.
\]

For sufficiently large `k`, the whole compact set lies in `Re(s)>-k-1`, where the ordinary integral in (F1) is valid. There,

\[
a_k^{1-s}\frac{B_k(s)}{B_k(1)}
=\frac{\mathbb E[X_k^{s-1}]}{\Gamma(s)}.
\]

Multiplication by the bounded entire reciprocal Gamma function on `S` proves (F3). All complex powers use the real logarithm of the positive base.

**Meaning of the limit.** A family of positive forward-lag faces can indeed converge, after a stated normalization, to an entire function whose zeros exhaust the nonpositive integers. The negative orders arrive as zeros of an analytic observation of the volumes. The positive lag distributions themselves concentrate near an increasing positive time; they do not acquire negative support.

The limit has zeros at `0,-1,-2,...`. Replacing `s` by `s/2` would select `0,-2,-4,...`, but any nonzero rescaling could choose another spacing. That substitution requires a source argument; it does not establish an identification with zeta. The Gaussian lattice in (J4) supplies such an argument in the classical zeta construction, while the BBP face calculation alone does not.

### Comparison with convolution powers

The preceding round proved

\[
q^{*j}(t)=\frac{15^j}{\Gamma(2j)}t^{2j-1}
-\frac{59j15^{j-1}}{(2j)!}t^{2j}+O(t^{2j+1}).
\]

Thus the normalized Mellin transform of `exp(-at)q^{*j}(t)`, `a>0`, has a finite block of zeros at `0,-1,...,-(2j-2)`. Its next two values are

\[
Z_{j,a}(-(2j-1))=-15^j,
\qquad
Z_{j,a}(-2j)=-j15^{j-1}(59+30a)<0.
\]

Again a Gamma shape controls the first surviving jet, not an infinite even-parity law.

### Applying the same positive grade average to authentic BBP faces

Apply exactly the weights in (J5) to the native faces `H_k=H_0(1-e^(-8t))^k`. The result is

\[
K_{\mathrm{BBP}}(t)
:=\sum_{k\ge0}2^{-k-1}H_k(t)
=\frac{H_0(t)}{1+e^{-8t}}.
\tag{F8}
\]

The normalized Mellin transform `E_BBP(s)=M[K_BBP](s)/Gamma(s)` is entire, and `E_BBP(s)=sum_(k>=0)2^(-k-1)B_k(s)` locally normally. For any compact set, choose a sufficiently high fixed grade `N`; the bound `H_k<=H_N` for `k>=N` and the same geometric summability argument as for (J6) establish this claim in the ordinary integral domain of the high-grade terms, while the finite low-grade terms are entire.

The source endpoint is `H_0(t)=16t-56t^2+O(t^3)`, while `(1+e^(-8t))^(-1)=1/2+2t+O(t^3)`. Thus

\[
K_{\mathrm{BBP}}(t)=8t+4t^2+O(t^3),\qquad
\boxed{E_{\mathrm{BBP}}(-2)=8.}
\tag{F9}
\]

The finite-grade calculation agrees exactly: `B_0(-2)=-112`, `B_1(-2)=256`, and `B_k(-2)=0` for all `k>=2`, giving `-112/2+256/4=8`. This is a decisive failure of the same positive grade average to transport the BBP source into the eta reflection class. It does not refute other maps; any proposed replacement must explicitly state and verify its source transformation. The added source comparison is distinct from the inherited universal Euler/Hasse identity.

## 6. Source history and novelty boundary

| Inherited item | What was already established | Boundary for this round |
| --- | --- | --- |
| [EULER_MASCHERONI_BBP_REGULATOR.md](../../2026-10-24/EULER_MASCHERONI_BBP_REGULATOR.md), sections 2–4 | Entire regulated Lerch family; original pi point; positive differences; unregulated endpoint noncommutation | Full-real sign and unique simple zero are explicit corollaries here; the family is inherited |
| [BBP_DIRICHLET_RESOLVENT.md](../../2026-10-28/BBP_DIRICHLET_RESOLVENT.md), BDR-1 and BDR-6 | `F(s)=sum r(n)n^(-s)` has poles at all negative integers; `F/Gamma(s+1)` has nonzero negative-integer values and intermediate real zeros | This chronology Dirichlet response is distinct from deforming the four source exponents in `B_z(s)` |
| [universal_n_carrier](../../2026-10-30/universal_n_carrier/UNIVERSAL_N_PASCAL_GAMMA_ZETA.md), UN-03 and UN-05 | Authentic Gamma-two limit; heat-regulated `zeta(-1)`; explicit regulator dependence; classical archimedean reflection | A source Gamma limit did not identify its negative orders with zeta |
| [ZETA_NEGATIVE_INTEGER_TANGENT_FAMILY.md](../../2026-10-30/universal_nz_carrier/ZETA_NEGATIVE_INTEGER_TANGENT_FAMILY.md), ZT1–ZT3; blob `b4665e5700cab6d80e3cff6229ba0bc913478693` | Universal positive Pascal faces; Euler/Hasse eta aggregation; finite-grade negative-integer values; convergent all-grade analytic tangents | The positive aggregation in (J5) is inherited classical structure; applying its same weights to authentic BBP faces gives the new exact comparison (F9) |
| [zeta_minus_one_transport.py](../../../observational_succ/zeta_minus_one_transport.py) and [its dossier](../../2026-10-11/EULER_LOCAL_GLOBAL_MINUS_ONE_TRANSPORT.md) | Finite local Euler factors, global functional-equation transport, Abel eta, negative-odd Bernoulli values | The no-functional-equation endpoint-parity proof above is a classical alternative derivation |
| [ORIGIN_LOCKED_OILY_ZETA_FRAME_DOSSIER.md](../../2026-10-28/ORIGIN_LOCKED_OILY_ZETA_FRAME_DOSSIER.md), sections 4–6 | Source-preserving fiber lift versus doubled zeta; Gamma-two critical law; physical/source identification controls | A matching Gamma law did not produce an original BBP-to-zeta intertwiner |
| [TATE_IDELIC_ZETA_RECONSTRUCTION.md](../../2026-10-15/TATE_IDELIC_ZETA_RECONSTRUCTION.md) | Gaussian/prime-shell Poisson continuation and `pi^(-s/2)Gamma(s/2)` | Theta completion and its half-argument are inherited classical inputs |
| [bbp_volume_algebra](../bbp_volume_algebra/THEOREMS.md) and companion #636 recorded in its provenance | Exact signed kernel powers and finite-difference endpoint faces | The entire-plane normalized face limit (F3) is the source-specific extension proved here |

The inspected regulator dossier explicitly restricts the displayed positivity theorem to `s>0`; its analytic family was already entire for `|z|<1`. No full-real sign theorem was found in that dossier, its module or its focused tests. This is a bounded provenance conclusion, not a priority assertion about every historical branch or the mathematical literature.

## 7. Validation, claims and the next lamp

**Final derivational review receipt, 2026-11-15: PASS within CN-04–CN-09.** The reviewed [THEOREMS.md](THEOREMS.md) has SHA-256 `112634fd9d370be421b5ca4d9619c9ea01fd259b8cdbd4ecef6f97f422db04f1`. The review checked the Mellin endpoint domains and factorials; the positive rate-measure mass and rising-factorial normalization; the convolution simplex normalization; the eventual inverse-moment bounds and compact-uniform face limit; and both the inherited eta aggregation and the exact BBP comparison `-56+64=8`. The final version explicitly makes the moment bounds eventual in depth. The native tail-face normalization agrees with CV3, CV5 and CV7 in companion #636 at commit `397eec34c3637c876ab4e4f71f7c9a5359f75535`, read separately from that branch. The inherited tangent-family file's Git blob was directly checked as `b4665e5700cab6d80e3cff6229ba0bc913478693`. This records a bounded mathematical and provenance review of the stated file revision, not an additional experiment or a claim of independent research provenance.

**Observed baseline:**

```text
python -m unittest tests.test_euler_bbp_regulator \
  tests.test_zeta_minus_one_transport tests.test_origin_locked_oily_zeta -q
Ran 41 tests in 0.217s
OK
```

**Observed exact probe:** direct SymPy rational differentiation using `-x*d/dx` gave the two source-jet rows in section 4. It imported none of this round's production modules. The exact sign proofs, endpoint criterion, rate-measure factorization, and compact-uniform limit above carry the universal statements; the finite probe does not.

**Subsequent bounded numerical diagnostic:** [face_limit_probe.py](face_limit_probe.py) writes [receipts/face_limit.json](receipts/face_limit.json). At 40 decimal digits it evaluated 30 direct-quadrature rows and 10 separately labelled exact negative-integer zeros, for `k=8,32,128,512,2048`. Positive-kernel quadratures in `t` and in the regularized coordinate `y=u^8` agreed to a maximum absolute difference of `1.38e-40`; the run took 8.04 seconds. The finite depths are still far from the limit at some points: `C_8(2)=5.33754...` and `C_2048(2)=2.10725...`, while `1/Gamma(2)=1`. The receipt records raw integrals, comparison values, versions and precision, without asserting monotonicity, a rigorous numerical error interval, an all-depth bound, or a universal limit from this computation.

| Claim | Verdict |
| --- | --- |
| Positive-order causal integrals extend to a forward-supported distribution group | Disclosed; classical, with negative integer kernels `delta^(n)` |
| Positivity survives those negative integer orders | Refuted; derivatives of delta are not positive measures |
| Positive Bose kernel plus endpoint reflection yields all negative-even zeta zeros without assuming the functional equation | Disclosed; classical Mellin/Bernoulli proof |
| Universal positive Pascal faces aggregate into the eta kernel and recover the negative-even zero pattern | Disclosed; inherited Euler/Hasse family and finite-grade truncation, with the exact reflection (J5) |
| The native BBP exponent family has those zeros | Refuted; it has sign `s` on the real axis |
| The same positive grade average transports authentic BBP faces to the eta reflection class | Refuted; the exact value at `-2` is `8` |
| Increasing original-source finite-difference faces exhaust negative integer zeros and converge to reciprocal Gamma | Disclosed within (F1)–(F7) |
| This automatically singles out the even zeta subsequence | Refuted as an implication; the limit has every nonpositive integer zero |
| A source-preserving original-BBP map to the self-dual Gaussian lattice is established | UNVERIFIED |

The remaining lamp is an explicit source map or aggregation that derives the needed endpoint reflection while preserving the selected original data. The universal Euler/Hasse carrier supplies a successful positive causal construction; the same-weight BBP calculation supplies a precise failed transport, and the Gaussian lattice supplies a distinct classical route through its quadratic spectrum. A new source-preserving bridge must explain that difference and survive the comparison (F9).

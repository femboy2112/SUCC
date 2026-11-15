# Positive causal volumes, negative orders, and the actual zeta parity

**Status:** paper proofs, with separately scoped exact computational audits.
**Parent:** draft #637 at `55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`.
**Conventions:** time is `t >= 0`; `s` is a complex Mellin or integration
order; `z` is a real regulator in `[0,1)`; `k` is a nonnegative integer
face depth. Source-convolution depth is denoted `w` or `j`, never silently
identified with Mellin order or chronological BBP time.

The original source is unchanged:

$$q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t},\qquad
\mathcal R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},$$
$$r(n)=\mathcal R(8n-7),\quad U_0=0,\quad U_n=16U_{n-1}+r(n).$$

The classical distribution machinery, the inherited positive convolution
semigroup, and the inherited Lerch source family are identified in
[PROVENANCE.md](PROVENANCE.md). The source-specific inverse, real-zero
classification, and reciprocal-Gamma face limit are the contributions of
this round. No academic-priority assertion is made.

## CN-01. A copy of the integers inside forward-supported volumes

**Disclosed; classical, with domains explicit.** Let
`D'_+ = {T in D'(R): supp(T) subset [0,infinity)}`. Convolution is defined
for any two members: the addition map on their joint support is proper
over each compact target set. Its identity is `delta_0`.

For `Re(s)>0`, define the locally integrable distribution

$$\Phi_s(t)=\frac{t_+^{s-1}}{\Gamma(s)}.$$

There is a unique weakly entire extension to all `s in C`, with

$$D\Phi_s=\Phi_{s-1},\qquad
\Phi_s*\Phi_w=\Phi_{s+w},\qquad
\Phi_0=\delta_0,\qquad\Phi_{-m}=D^m\delta_0\quad(m\ge0). \tag{1}$$

**Proof.** When `Re(s)>1`, integration by parts against a compact smooth
test function gives `D Phi_s = Phi_(s-1)`; the boundary term vanishes.
For any integer `N>=0`, define on `Re(s)>-N`

$$\Phi_s=D^N\Phi_{s+N}.$$

Adjacent definitions agree on overlaps by that derivative identity, first
where integration by parts is literal and then by scalar holomorphic
continuation after pairing with every test function. These half-planes
cover `C`. They give an entire distribution-valued family and preserve
support. Since `Phi_1` is the Heaviside distribution, `D Phi_1=delta`.
Repeated differentiation proves the nonpositive-integer values.

For `Re(s),Re(w)>0`, the Beta integral in the causal convolution gives
`Phi_s*Phi_w=Phi_(s+w)`. Pair with a test function, use the proper-support
convolution, and apply the identity theorem successively in `s` and `w`.
This proves the identity on `C^2`. Uniqueness follows by the identity
theorem on every scalar test pairing. Finally, for real `a>0`,

$$\mathcal L\Phi_s(a)=a^{-s},$$

with the ordinary real logarithm of `a`. This distinguishes `Phi_m` for
distinct integers `m`, so `m -> Phi_m` is an injective group homomorphism
from `(Z,+)` into the convolution units of `D'_+`. QED.

Thus forward integration `Phi_1` has a causal distributional inverse
`Phi_-1=delta'`. The positive-time support has not moved to negative time.
The extension enlarges the allowed reports from positive densities to
signed distributions. Negative integers as physical locations or past
events are a different object and do not follow from (1).

For a tempering rate `lambda>=0`, multiplication by `exp(-lambda*t)` is
compatible with causal convolution. Therefore

$$K_{s,\lambda}=e^{-\lambda t}\Phi_s,\quad
K_{s,\lambda}*K_{w,\lambda}=K_{s+w,\lambda},\quad
K_{-m,\lambda}=(D+\lambda)^m\delta. \tag{2}$$

The last equality follows from the distributional product rule. These
kernels are not probability normalized; for `lambda>0`, the positive
probability family is `lambda^s K_(s,lambda)` for real `s>0`.

### The derivative/multiplication algebra that accompanies the group

Let `X` multiply a distribution by the time coordinate `t`. The Euler
Gamma recurrence and continuation give

$$D\Phi_s=\Phi_{s-1},\qquad X\Phi_s=s\Phi_{s+1},\qquad
(DX-XD)T=T\quad(T\in\mathcal D'_+). \tag{2a}$$

The last identity is the distributional product rule, the classical
Weyl-algebra relation. At the boundary it says `t delta=0` and
`t delta^(m)=-m delta^(m-1)` for `m>=1`. Thus the same ladder continues
through zero with fixed, checkable coefficients. This algebra acts on
the causal distributions; it is separate from their commutative
convolution product. No quantum or physical-phase interpretation is
implied by this operator identity.

## CN-02. Constructing negative orders from forward samples

**Disclosed; exact finite construction and error bound.** For an integer
`m>=0` and `h>0`, put

$$A_{m,h}=h^{-m}\sum_{j=0}^{m}(-1)^j\binom mj\delta_{jh}.$$

All atoms lie at nonnegative lags. For a smooth test function `phi`,

$$\langle A_{m,h},\phi\rangle
=(-1)^m\int_{[0,1]^m}\phi^{(m)}(h(u_1+\cdots+u_m))\,du.$$

This is the fundamental theorem of calculus iterated `m` times; at `m=0`
the empty integral is `phi(0)`. Hence `A_(m,h) -> D^m delta` in
distributions. If `|phi^(m+1)|<=M` on `[0,mh]`, then

$$\left|\langle A_{m,h},\phi\rangle-(-1)^m\phi^{(m)}(0)\right|
\le\frac{mhM}{2}. \tag{3}$$

The mean of `sum u_i` is `m/2`. The polynomial `phi(t)=t^(m+1)` attains
this bound. Individual observation errors of magnitude at most `eta`
can cause an error as large as

$$\eta\|A_{m,h}\|_{\rm TV}=\eta\,2^m h^{-m}. \tag{4}$$

Alternating error signs attain (4). Thus constructive causality does not
give noise stability as `h -> 0`. Positivity is also genuinely lost:
positive measures have positive distributional limits, whereas
`D^m delta` is not a positive distribution for `m>=1`.

For a zero-extended smooth function, the endpoint terms are

$$D^m(Hf)=Hf^{(m)}+
\sum_{j=0}^{m-1}f^{(m-1-j)}(0)D^j\delta. \tag{5}$$

They are necessary for a causal inverse. In a response `(A_(m,h)*f)(T)`,
only values at `T-jh` occur; where `T-jh<0`, zero extension is part of
the declared initial condition. The forward lags do not require future
measurements at the time of that response.

## CN-03. The full original source has a signed inverse-volume group

**Disclosed; new explicit negative-depth interface to an inherited
positive semigroup.** Define

$$N(a)=15a^2+121a+240,\qquad
P(a)=a(a+3)(a+4)(a+5),\qquad\mathcal R(a)=N(a)/P(a),$$
$$\rho_\pm=\frac{121\pm\sqrt{241}}{30},\qquad
3<\rho_-<4<\rho_+<5.$$

Using (2), form the entire causal distribution family

$$Q_w=15^w K_{w,0}*K_{w,3}*K_{w,4}*K_{w,5}
                   *K_{-w,\rho_-}*K_{-w,\rho_+}. \tag{6}$$

Here `15^w=exp(w log 15)`. Direct convolution and Laplace transforms give

$$Q_0=\delta,\qquad Q_1=Hq,\qquad Q_w*Q_v=Q_{w+v},$$
$$\mathcal LQ_w(a)=\exp(w\log\mathcal R(a))\quad(a>0). \tag{7}$$

The logarithm in (7) is the real logarithm for positive `a`; on the right
half-plane it is the branch obtained from the six factors in (6).
There is no branch guess or unspecified winding. The kernels have
nonnegative support and admit these Laplace transforms. The equality
`Q_1=Hq` follows either by partial fractions or transform uniqueness.
For completeness, on each compact `w`-set choose one integer `M` making
the real parts of all six shifted orders positive. Apply fixed operators
`(D+lambda)^M` to the corresponding locally integrable kernels. This
gives weak entire dependence directly, with proper-support convolution.
An entire extension agreeing with the fully specified positive real-depth
family is unique by scalar test-pairing identity. Agreement only at the
positive integers would not be enough.

For every real `w>0` and `a>0`,

$$e^{-at}Q_w(dt)/\mathcal R(a)^w$$

is a positive probability measure. This positive-depth theorem is
**inherited** from the atomic-source dossier. To see its source mechanism,
its Laplace transform is `(R(a+p)/R(a))^w`: two Gamma laws with rates
`a` and `a+5`, plus two compound-Poisson laws with Levy densities

$$w\frac{e^{-(a+3)t}-e^{-(a+\rho_-)t}}{t},\qquad
w\frac{e^{-(a+4)t}-e^{-(a+\rho_+)t}}{t}.$$

The interlacing rates make these nonnegative and integrable; integrating
their Laplace exponents gives exactly the two remaining rational factors.
The negative-depth part of (6) is not a positive probability family.

The first inverse `J=Q_-1` is completely explicit:

$$\boxed{J=\frac1{15}\delta''+\frac{59}{225}\delta'
-\frac{164}{3375}\delta+Hk,\qquad (Hq)*J=\delta.} \tag{8}$$

Its regular term is specified without irrational approximations by

$$\mathcal Lk(a)=\frac{9944a+39360}{3375(15a^2+121a+240)},$$
$$15k''+121k'+240k=0,\quad
k(0)=\frac{9944}{50625},\quad
k'(0)=-\frac{612824}{759375}. \tag{9}$$

**Proof.** Polynomial division of `P(a)` by `N(a)` gives exactly (8)--(9).
Its two characteristic roots are `-rho_-,-rho_+`, so the regular term is
a smooth exponentially decaying combination. Multiplication by the
original source transform gives one. Laplace uniqueness in the causal
distribution class proves (8), with every initial atom retained.
Equivalently,

$$P(D)(Hq)=N(D)\delta$$

by (5) and the original jets `q(0)=0,q'(0)=15,q''(0)=-59,q'''(0)=243`.

For every integer `m>=1`, division of `P^m` by `N^m` represents `Q_-m`
as a delta polynomial of degree exactly `2m`, with leading term

$$15^{-m}\delta^{(2m)}, \tag{10}$$

and a proper rational transfer with poles `-rho_-, -rho_+` of order at
most `m`. Thus its regular part is an exponentially decaying polynomial
combination. These statements follow from polynomial degrees and leading
coefficients, and `(Hq)^{*m}*Q_-m=delta`. QED.

The second derivative in (8) is the inverse signature of the original
source's simple endpoint zero. Recovering a smoothed signal by this
operator amplifies derivatives; it is not a bounded inverse on arbitrary
continuous or noisy reports. Nor is convolution depth `w` the BBP
chronological index `n`.

## CN-04. Negative Mellin values are endpoint derivative reports

**Disclosed; classical endpoint-subtraction theorem.** Suppose `f` is
smooth near `0`, locally integrable away from `0`, and decays faster than
every power at infinity. Define initially where convergent

$$Z_f(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}f(t)\,dt.$$

Then `Z_f` has a unique entire continuation and

$$\boxed{Z_f(-m)=(-1)^m f^{(m)}(0),\qquad m=0,1,2,\ldots.} \tag{11}$$

**Proof.** Write `f_j=f^(j)(0)/j!`. For every `M>=0`,

$$\int_0^\infty t^{s-1}f(t)dt
=\int_0^1t^{s-1}\left(f(t)-\sum_{j=0}^Mf_jt^j\right)dt
+\int_1^\infty t^{s-1}f(t)dt+\sum_{j=0}^M\frac{f_j}{s+j}. \tag{12}$$

The subtracted integral is holomorphic for `Re(s)>-M-1`. The formulas
agree on overlaps. The only possible poles are simple, at `s=-j`, of
residue `f_j`. Since `1/Gamma(s)=(-1)^m m!(s+m)+O((s+m)^2)` near `-m`,
the pole cancellation gives (11). This proves an identity of analytic
continuations, not evaluation of a divergent improper integral. QED.

If a kernel instead has a finite Laurent principal part at zero, include
those powers in (12). Poles at positive integers can survive the Gamma
division. Formula (11) still reads the coefficient of `t^m` in the
regular part, with the same factor `(-1)^m m!`.

This is the exact source-to-report meaning of the delta derivatives:
analytic continuation converts a global Mellin integral into a local
endpoint-jet functional. The Dirac distributions do not vanish at
negative orders; their action can vanish on particular source jets.

## CN-05. The authentic source continues, but has no negative-even zeros

**Disclosed; explicit corollary of the inherited four-ray family.** For
`a>0`, the tilted source gives

$$F_a(s)=Z_{e^{-at}q}(s)
=4a^{-s}-2(a+3)^{-s}-(a+4)^{-s}-(a+5)^{-s}. \tag{13}$$

The equality holds first for `Re(s)>0`, then everywhere by continuation.
For every integer `m>=1`,

$$F_a(-m)=4a^m-2(a+3)^m-(a+4)^m-(a+5)^m<0. \tag{14}$$

Also `F_a(0)=0`, `F_a(-1)=-15`, and `F_a(-2)=-30a-59`.
The strict inequality follows termwise from the positive increments
`3,4,5`; it uses the actual source, not a substituted seed or mutant.

For `0<=z<1`, define the inherited entire family

$$B_{z,0}(s)=\sum_{n=0}^\infty z^nF_{8n+1}(s). \tag{15}$$

Each compact `s`-set has a polynomial-in-`n` majorant, so the geometric
weight gives local uniform convergence and every complex derivative.
Its positive heat kernel is

$$H_{z,0}(t)=\frac{e^{-t}q(t)}{1-ze^{-8t}},\qquad
B_{z,0}(s)=Z_{H_{z,0}}(s). \tag{16}$$

At the native regulator `z=1/16`, the classical original BBP identity is
`B_(1/16,0)(1)=pi`. Also, using the inherited Oily kernel `R(x)`,

$$H_{1/16,0}(t)=16e^{-t}R(e^{-t}),\quad
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8}.$$

The negative values are therefore derived from the same full volume:

| `s` | 0 | -1 | -2 | -3 | -4 | -5 | -6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `B_(1/16,0)(s)` | 0 | -16 | -112 | -880 | -9520 | -136816 | -2391472 |

Equation (14), summed with positive weights, proves strict negativity at
**every** negative integer. CN-06 strengthens this to the full real axis.

The regulator is load-bearing. At `z=1`, the inherited Hurwitz
continuation has value `15/8` at `s=0`; the native entire family at
`z=1/16` has value zero. Substituting the unregulated family changes the
boundary problem and is not an innocuous rewriting of the pi source.

## CN-06. The Gamma(k+2) faces have exactly k+1 simple real zeros

**Disclosed; source-specific all-order classification.** Define

$$H_{z,k}(t)=H_{z,0}(t)(1-e^{-8t})^k,\qquad
B_{z,k}(s)=Z_{H_{z,k}}(s). \tag{17}$$

Equivalently,

$$B_{z,k}(s)=\sum_{n\ge0}z^n\sum_{j=0}^k(-1)^j\binom kj
F_{8n+1+8j}(s),$$

which is entire by the same normal convergence argument.

There exists a finite positive measure `mu_(z,k)` on `[1,infinity)` with
all polynomial moments finite such that

$$H_{z,k}(t)=t^{k+1}\int_1^\infty e^{-\lambda t}\mu_{z,k}(d\lambda),$$
$$\mu_{z,k}([1,\infty))=\frac{15\,8^k}{1-z}. \tag{18}$$

**Construction.** Set

$$w(v)=2\mathbf1_{[0,3]}(v)+\mathbf1_{[0,4]}(v)+\mathbf1_{[0,5]}(v).$$

Then `q(t)=t int w(v)e^(-vt)dv`, and
`1-e^(-8t)=t int_0^8 e^(-ut)du`. Push forward

$$\left(\sum_{n\ge0}z^n\delta_n\right)\otimes w(v)dv
\otimes\bigotimes_{i=1}^k\mathbf1_{[0,8]}(u_i)du_i$$

under `lambda=1+8n+v+sum u_i`. This proves (18); the geometric discrete
tail gives every polynomial moment. At `z=0`, the measure is compactly
supported. At the native regulator its mass is `16*8^k`.

Tonelli and the Euler integral now give, first for `Re(s)>-k-1`,

$$\boxed{B_{z,k}(s)=(s)_{k+1}L_{z,k}(s),\qquad
L_{z,k}(s)=\int_1^\infty\lambda^{-s-k-1}\mu_{z,k}(d\lambda),} \tag{19}$$
$$ (s)_{k+1}=s(s+1)\cdots(s+k). $$

On each compact complex parameter set, the integrand and its derivatives
are bounded by a fixed polynomial moment. Thus `L_(z,k)` is entire and
is strictly positive on **all of the real axis**. Identity continuation
extends (19) everywhere. Consequently

$$\boxed{\{s\in\mathbb R:B_{z,k}(s)=0\}=\{0,-1,\ldots,-k\},} \tag{20}$$

and all these zeros are simple. This is a real-zero classification;
possible additional complex zeros of `L_(z,k)` are not excluded.

At negative integers `-m`, `m>=k+1`,

$$B_{z,k}(-m)=(-1)^{k+1}\frac{m!}{(m-k-1)!}
\int\lambda^{m-k-1}\mu_{z,k}(d\lambda), \tag{21}$$

so the sign is fixed and no additional negative integers are zeros. The
first contact is

$$B_{z,k}(-k-1)=(-1)^{k+1}(k+1)!\frac{15\,8^k}{1-z}. \tag{22}$$

### Exactly where Gamma(k+2) enters

At zero, `H_(1/16,k)(t) ~ 16*8^k*t^(k+1)`. A positive Laplace zoom with
large parameter `A` therefore has leading integral

$$16\,8^k\Gamma(k+2)A^{-k-2}.$$

The same endpoint order `k+1` gives the factor `(s)_(k+1)` in (19).
This is the precise link between the Gamma shape and negative-order
zeros. It produces a **consecutive finite block**, not an even-only
infinite pattern.

For the inherited tail faces in #636,

$$(-1)^k\Delta^kT_n=\frac1{16}\int_0^\infty e^{-8nt}H_{1/16,k}(t)dt
\sim\frac{\Gamma(k+2)}{64n^{k+2}},$$

recovering the exact normalization of that branch without importing its
code or validation counts. This asymptotic fixes `k` while `n -> infinity`.

## CN-07. The convolution Gamma(2j) hierarchy has the analogous contact

**Disclosed; explicit source-mixture proof.** Let `j>=1` be an integer and
`a>0`. From `q(t)=t int w(v)e^(-vt)dv`, causal convolution on the simplex
gives a finite positive measure `nu_j` on `[0,5]` such that

$$q^{*j}(t)=\frac{15^j}{\Gamma(2j)}t^{2j-1}
\int e^{-vt}\nu_j(dv),\qquad \nu_j([0,5])=1. \tag{23}$$

For example, let the `V_i` be independent with density `w/15`, and let
`(S_1,...,S_j)` have the simplex density proportional to `prod S_i`,
independently of the `V_i`. The pushforward by `sum S_i V_i` is `nu_j`.
The Beta simplex integral is `1/Gamma(2j)`, giving (23). This is a
declared auxiliary convolution representation, not digit randomness.

Therefore the normalized Mellin transform of `exp(-at)q^{*j}(t)` is

$$\frac{15^j}{(2j-1)!}(s)_{2j-1}
\int(a+v)^{-s-2j+1}\nu_j(dv). \tag{24}$$

Its exact real zeros are `0,-1,...,-(2j-2)`. Its first nonzero negative
integer value is `-15^j` at `s=-(2j-1)`; all subsequent negative-integer
values are strictly negative. Also, (5) and (23) imply

$$D^{2j}(Hq^{*j})=H(q^{*j})^{(2j)}+15^j\delta,$$

whereas smaller derivative orders introduce no boundary atom. This links
the full kernel compiler in #637 to derivative order `2j` in the
source-depth inverse `Q_-j` of CN-03.

## CN-08. Infinitely many normalized faces recover reciprocal Gamma

**Disclosed; a source-specific limit with explicit normalization.** Fix
the native regulator. For integer `k>=2`, let

$$A_k=\frac{\log k}{8},\quad Z_k=B_{1/16,k}(1)>0,\quad
C_k(s)=A_k^{1-s}\frac{B_{1/16,k}(s)}{Z_k},$$

using the real logarithm of `A_k`. Then

$$\boxed{C_k(s)\longrightarrow\frac1{\Gamma(s)}
\quad\text{locally uniformly on }\mathbb C.} \tag{25}$$

This gives an exact version of an infinite positive-face construction
whose continued limit has zeros at **all** nonpositive integers.

**Proof.** Let `T_k` have density `H_(1/16,k)/Z_k` on positive time and
put `Y_k=exp(-8T_k)`. With `a=1/8`, its unnormalized density on `(0,1)` is

$$w_*(y)y^{a-1}(1-y)^k,\qquad
w_*(y)=\frac{4-2y^{3/8}-y^{1/2}-y^{5/8}}{8(1-y/16)}.$$

The function `w_*` is bounded and nonnegative on `[0,1]`, continuous
at zero, and `w_*(0)=1/2`. Substitute `v=ky`; the bound
`(1-v/k)^k <= exp(-v)` gives dominated convergence. Thus

$$Z_k\sim\frac{\Gamma(1/8)}{2k^{1/8}},\quad
kY_k\ \Rightarrow\ G_{1/8},\quad
T_k-A_k\ \Rightarrow\ -\frac18\log G_{1/8}, \tag{26}$$

where `G_(1/8)` is a Gamma variable of shape `1/8`, rate one. In
particular `X_k=T_k/A_k -> 1` in probability.

We need moment control, not only weak convergence. For every fixed
`p>0`, the bound `H_(1/16,k)(t) <= (64/15)exp(-t)` gives

$$\mathbb E[X_k^p;X_k>2]=O(k^{-1/8}),$$

by integrating from `2A_k` and using (26). On `X_k<=2` the positive
moment is bounded. For inverse moments, `y<=k^(-1/2)` implies `X_k>=1/2`.
On the complement, `-log y >= 1-y` gives

$$\mathbb E[X_k^{-p};Y_k>k^{-1/2}]
\le \frac{C(\log k)^p}{Z_k}
\int_{k^{-1/2}}^1y^{a-1}(1-y)^{k-p}dy
=O((\log k)^p e^{-\sqrt{k}/2}),$$

where for large `k` one extracts `(1-y)^(k/2) <= exp(-sqrt(k)/2)`
and bounds the remaining Beta integral by `O(k^-a)`. Higher fixed
positive and inverse moments are therefore uniformly bounded eventually
in `k` (the threshold depends on the chosen moment order).

For any compact set of `s` values, these higher moments imply uniform
integrability of `X_k^(s-1)` and of a dominating pair of positive/inverse
powers. On a neighborhood of `X=1`, the functions `X^(s-1)` converge
uniformly in `s`; outside it, the moment bounds and convergence in
probability make the expectation uniformly negligible. Hence

$$\mathbb E[X_k^{s-1}]\longrightarrow1$$

uniformly on that compact. For sufficiently large `k`, the entire
compact lies in `Re(s)>-k-1`, where the original Mellin integral exists;
there `C_k(s)=Gamma(s)^(-1) E[X_k^(s-1)]`. Multiplying by the bounded
entire reciprocal Gamma factor proves (25), including its zeros. QED.

The unnormalized `B_(1/16,k)` instead tends locally uniformly to zero:
on a compact choose a fixed `k_0` large enough for the integral at zero,
dominate by `H_(1/16,k_0)`, and use `(1-exp(-8t))^k -> 0`. Thus the
normalization in (25) is essential. This `k -> infinity` regime probes
large positive times `T_k ~ log(k)/8`; it differs from the fixed-face,
large-`n` endpoint zoom producing `Gamma(k+2)` in CN-06.

## CN-09. What selects zeta's negative even integers

### An actual positive-volume aggregation, already present in SUCC

The inherited universal Pascal/Hasse ladder supplies an explicit
construction from positive forward-time volumes. Define

$$f_n(t)=e^{-t}(1-e^{-t})^n,\qquad
F_n(s)=\sum_{j=0}^n(-1)^j\binom nj(j+1)^{-s}=Z_{f_n}(s).$$

Each `f_n` is positive for `t>0`. Geometrically averaging the grade gives

$$\sum_{n\ge0}2^{-n-1}f_n(t)=\frac1{e^t+1}.$$

The corresponding entire Mellin readout is

$$\eta(s)=\sum_{n\ge0}2^{-n-1}F_n(s),\qquad
\zeta(s)=\frac{\eta(s)}{1-2^{1-s}}.$$

To justify local normal convergence on any compact order set, choose
`n_0` large enough that its Mellin integral converges at zero, dominate
all `f_n`, `n>=n_0`, by `f_(n_0)`, and retain the geometric weights.
On `Re(s)>1`, the kernel identity and the absolutely convergent
alternating Dirichlet sum identify this readout with eta. Continuation
then gives the displayed formulas, with the zeta quotient interpreted
meromorphically at denominator zeros.

At `s=-m`, finite differences annihilate the degree-`m` polynomial for
`n>m`; hence all negative integer values have the exact finite formula

$$\zeta(-m)=\frac1{1-2^{m+1}}
\sum_{n=0}^m2^{-n-1}\sum_{j=0}^n(-1)^j\binom nj(j+1)^m. \tag{27a}$$

This is an inherited classical identity, not a new ordinary summation
of divergent positive powers. It explicitly demonstrates that causal
volumes can construct the analytic negative-integer reports after the
composition and grade weights are specified.
The aggregate satisfies
`1/(e^t+1)+1/(e^-t+1)=1`; after subtracting its value `1/2`, its germ
is odd. Hence `eta(-2n)=0` by CN-04, and the nonzero denominator
`1-2^(2n+1)` transfers those values to zeta.

The source comparison is decisive. Apply the **same grade weights** to
the authentic BBP faces of CN-06. Their positive aggregate is

$$\sum_{k\ge0}2^{-k-1}H_{1/16,k}(t)
=\frac{H_{1/16,0}(t)}{1+e^{-8t}}.$$

Its entire Mellin readout at `s=-2` is

$$\frac12 B_{1/16,0}(-2)+\frac14 B_{1/16,1}(-2)
=-56+64=8. \tag{27b}$$

All `k>=2` terms vanish there by CN-06. Local normal convergence is
justified by the same domination argument. Thus the shared causal-face
algebra and positive grade averaging do not erase the source: this
aggregate is neither eta nor zeta.

### The parity that makes the zeta values vanish

**Disclosed; classical, derived from a positive kernel and its parity.**
For `t>0`, the positive counting kernel is

$$K(t)=\sum_{n=1}^\infty e^{-nt}=\frac1{e^t-1}.$$

For `Re(s)>1`, Tonelli or absolute convergence gives

$$\zeta(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}K(t)dt. \tag{27}$$

The complex local continuation of this specified kernel satisfies

$$K(t)+K(-t)=-1.$$

After its pole is subtracted,

$$K(t)=\frac1t-\frac12+\frac t{12}-\frac{t^3}{720}
+\frac{t^5}{30240}-\cdots,$$

and `K(t)-1/t+1/2` is odd. Applying the Laurent version of CN-04 gives

$$\zeta(-m)=(-1)^m m![t^m]K(t),\qquad
\boxed{\zeta(-2n)=0\quad(n\ge1).} \tag{28}$$

No zeta functional equation is needed for this argument. The ordinary
sum of positive powers is divergent; (28) is the continued value of the
specified function in (27). In Bernoulli notation,
`zeta(-m)=(-1)^m B_(m+1)/(m+1)` for `m>=0`, with `B_1=-1/2`.

The distinction between endpoint order and parity is falsifiable. For
any `epsilon>0`, the positive perturbed kernel

$$K_\epsilon(t)=K(t)+\epsilon t^2e^{-t}$$

has the same leading pole and decay type, but its Mellin continuation is

$$Z_\epsilon(s)=\zeta(s)+\epsilon s(s+1).$$

Thus `Z_epsilon(-2n)=epsilon*(2n)*(2n-1)>0` for every `n>=1`.
The Gamma normalization alone does not enforce parity zeros. This is
a control for a claimed general implication, not a changed model of the
actual Riemann zeta function or the BBP source.

### Why the completed zeta has Gamma(s/2)

An independent classical representation uses the quadratic Gaussian
lattice. For `Re(s)>1`,

$$\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\int_0^\infty t^{s/2-1}\sum_{n\ge1}e^{-\pi n^2t}\,dt.$$

Poisson summation supplies `theta(t)=t^(-1/2)theta(1/t)`. Its stated
kernel, integer lattice, and Fourier normalization yield the completed
reflection law and continuation with only the usual poles at `0,1`.
At `s=-2n`, the pole of `Gamma(s/2)` is cancelled by a zeta zero. The
half-order comes from the quadratic Gaussian/lattice construction; it is
not obtained merely by relabeling the BBP face shape `k+2`. DLMF
25.5.13--14 and 25.4 give this classical representation and reflection.

## CN-10. Geometry, identification, and stability boundaries

**Disclosed counterexamples and a valid compact-group repair.**

1. Compactness alone does not supply analytic continuation, a connecting
   path, or inverse dynamics. The constant map `x -> 0` on compact
   `[0,1]` loses all distinctions after one forward step. Even compact
   connected spaces need not be path connected (the closed topologist's
   sine curve). An ambient density assertion does not add a holomorphic
   germ or an invertible transition map.
2. In a **compact topological group**, closure of positive powers of an
   element `g` does contain `g^-1`. Given an identity neighborhood `W`,
   choose `V` with `V^-1 V subset W`, cover the group by finitely many
   translates of `V`, and pigeonhole sufficiently many widely spaced
   positive powers. Their quotient is an arbitrarily late positive power
   in `W`; multiplying by `g^-1` approximates `g^-1` by positive powers.
   This uses neighborhoods/nets in general and sequences in the compact
   metrizable case. It requires a declared reversible group action, and
   gives approximation in its topology rather than a finite exact past.
3. A full positive interval of a holomorphic family uniquely determines
   its continuation on a connected domain. Positive integer samples
   alone do not: adding `A*s/Gamma(1-s)` preserves all positive integer
   values and the value at zero, but changes the negative integers for
   `A!=0`. Multiplying by a fixed causal distribution gives the same
   counterexample for distribution-valued families. It is not a
   competing family satisfying the convolution law of CN-01.
   Even positivity and probability normalization at every real `s>0`
   do not repair this sample-identification gap: let
   `mu_s=exp(-t)Phi_s`, `h(s)=1/Gamma(1-s)`,
   `u(s)=1-exp(-h(s)^2)`, and
   `Psi_s=(1-u(s))mu_s+u(s)delta`. This entire causal family is a positive
   probability measure for real `s>0`, agrees with `mu_n` at every
   positive integer, and has `Psi_0=delta`, but changes every negative
   integer order. Its convolution law fails: `Psi_(1/2)*Psi_(1/2)` has
   a positive atom at zero while `Psi_1=mu_1` has none. The composition
   law is additional, discriminating structure.
4. Exact analytic uniqueness does not imply stable extrapolation.
   For any fixed `m>=1`, `g_N(s)=exp(-N(s+m))` equals one at `-m` and
   tends uniformly to zero on every positive half-line `s>=a>0`.
   Extra growth or source constraints are necessary for a stable
   inverse. CN-02 gives the corresponding exact finite-sample noise cost.

The spiral metaphor has a precise contour relative: Hankel's formula

$$\frac1{\Gamma(s)}=\frac1{2\pi i}\int_{\mathcal H}e^z z^{-s}dz,$$

with `H` starting on the lower side of the negative real axis, looping
counterclockwise around zero, and returning on the upper side, with
`-pi < arg(z) < pi` and a fixed positive loop radius. No shrinking-loop
limit for arbitrary `s` is assumed. This contour encodes a branch comparison
of the integrand. The resulting reciprocal Gamma and `Phi_s` are
single-valued entire functions of **order** `s`; an actual spiral in
physical space, one compulsory path through all integers, or a new
analytic dimension does not follow. In (1) and (6), the connecting
structure is explicitly the distribution space, its convolution law,
and its holomorphic parameter, not a topological assumption about nature.

## CN-11. What this closes, and what remains open

The source-faithful dependency chain now includes:

- positive forward volumes -> a holomorphic convolution group of signed
  causal distributions -> exact inverse kernels and boundary derivatives;
- actual BBP face kernels -> Gamma endpoint order -> a classified finite
  block of negative-order zeros -> reciprocal Gamma after a specified
  infinite-face normalization;
- the positive integer counting kernel -> a reflection parity of its
  analytic germ -> the classical negative-even zeta zeros.

These arrows are distinct and proved with their maps specified. The
original BBP source's continued real-zero pattern differs from zeta's.
No source-preserving reflection/phase intertwiner between the two has
been supplied. In particular, these results do not establish a uniform
bound on the actual chronological sums

$$\sum_{n<N}e^{2\pi i hU_n}\quad(h\in\mathbb Z\setminus\{0\}),$$

base-16 normality of pi, or RH. Negative convolution depth is an inverse
of a declared kernel; it does not supply unobserved signed phase or carry
information. A proposed next map must preserve the original four poles,
zero seed, native regulator, endpoint terms, and chosen report, and must
fail the positive parity mutants above if its conclusion relies on
zeta's even-zero symmetry.

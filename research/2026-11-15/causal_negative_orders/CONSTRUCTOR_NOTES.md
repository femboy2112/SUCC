# Constructor: negative order on a forward causal carrier

**Date:** 2026-11-15. **Baseline:** 55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5.
**Status:** exact paper derivations and bounded exact arithmetic;
independent root review is separate. No academic priority or formal-proof
authority is claimed.

## 1. Hole contract, clocks, and provenance

The proposed construction asks whether positive forward causal volumes
can determine negative orders while retaining nonnegative time support.
The precise construction is an entire distribution-valued convolution
group. Its positive orders are integration kernels; its negative integer
orders are differentiation kernels at the causal boundary.

The following variables are different:

| Variable | Meaning |
| --- | --- |
| \(t\ge0\) | Continuous causal lag |
| \(n\ge1\) | Original discrete BBP time |
| \(a_n=8n-7\) | Original continuous-source argument at time \(n\) |
| \(s\in\mathbb C\) | Order of the universal Gamma distribution \(\Phi_s\) |
| \(z\in\mathbb C\) | Convolution depth of the complete source \(\mathcal Q_z\) |
| \(\lambda>0\) | Exponential tilt/tempering rate |
| \(\varepsilon>0\) | Resolution of a forward difference |

Negative \(s\) or \(z\) does not mean negative \(t\) or negative \(n\).
The original source remains

\[
q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t},\qquad
\mathcal R(a)=\int_0^\infty e^{-at}q(t)\,dt
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)}.
\]

For \(n\ge1\), \(r(n)=\mathcal R(8n-7)\), and
\(U_0=0,\ U_n=16U_{n-1}+r(n)\). No source or seed is altered.
Write \(q_+(t)=H(t)q(t)\) for the causal extension. Juxtaposition here
is pointwise multiplication; an asterisk below always means convolution.

**Exact targets.** Construct and prove uniqueness of the entire
\(\Phi_s\) continuation from its declared positive half-plane. Extend
the already established positive source-depth semigroup to an entire
causal distribution group \(\mathcal Q_z\). Compute its negative
integer orders without dropping endpoint distributions. Test whether
these constructions force negative-even scalar zeros.

**Novelty boundary.** The universal causal fractional-calculus group is
classical. The source factorization, positive Lévy density, and positive
source-depth semigroup are already proved in
[ATOMIC_SOURCE_AND_INTERACTIONS](../../2026-10-29/recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md),
Sections 3–5. The full signed source powers and their Gamma endpoint are
also inherited from
[the previous volume algebra](../bbp_volume_algebra/THEOREMS.md).
The present additions are their explicit negative-depth distribution
interface, rational inverse normal form, boundary-jet cancellation
instrument, and forward-supported difference realization.

Primary classical references:

* T. Kleiner and R. Hilfer, *On extremal domains and codomains for
  convolution of distributions and fractional calculus*, Monatshefte
  für Mathematik 198 (2022), 121–152,
  [Section 7, equations (7.2)–(7.3)](https://link.springer.com/article/10.1007/s00605-021-01646-1).
* L. Li and J.-G. Liu, *A Generalized Definition of Caputo Derivatives
  and Its Application to Fractional ODEs*, SIAM J. Math. Anal. 50
  (2018), 2867–2900,
  [Proposition 2.5 and Section 2.2](https://sites.math.duke.edu/~jliu/pdf/Li_Liu_SIMA_2018.pdf).
  Their endpoint distributions are essential to the group law.

The proofs below specialize these classical constructions explicitly.
The numerical audit verifies finite identities; it is not the proof of
analytic continuation or an infinite limiting statement.

## 2. The universal causal group

Let \(\mathcal D'_+\) denote distributions on \(\mathbb R\) supported
in \([0,\infty)\). Convolution is defined on every pair in this space:
the addition map is proper on the two supports over a compact target
set. Indeed, if \(t,u\ge0\) and \(t+u\le T\), then \(0\le t,u\le T\).
Using cutoffs outside that compact region defines convolution
independently of the cutoffs. It is associative and commutative, has
unit \(\delta_0\), and retains support in \([0,\infty)\).

### Entire continuation, derivative law, and uniqueness

For \(\Re s>0\), set

\[
\langle\Phi_s,\varphi\rangle
=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}\varphi(t)\,dt,
\qquad \varphi\in C_c^\infty(\mathbb R).
\]

Here \(t^{s-1}=\exp((s-1)\log t)\) uses the real logarithm for \(t>0\).
This is holomorphic in \(s\) on that half-plane, locally uniformly on
test functions with a fixed compact support and bounded derivatives.
Integration by parts gives

\[
D\Phi_{s+1}=\Phi_s \qquad(\Re s>0).
\]

For any integer \(N\ge0\), define

\[
\Phi_s=D^N\Phi_{s+N},\qquad \Re s>-N. \tag{CNO-01}
\]

The formulas agree on overlaps by the derivative law. They therefore
define an entire \(\mathcal D'_+\)-valued function: pairing against
each test function is entire. On each compact set of orders one
integer \(N\) suffices, so the distribution order is locally bounded.
The continuation is unique because every test-function pairing obeys
the scalar identity theorem.

Since \(\Phi_1=H\), \(DH=\delta_0\), and hence

\[
\boxed{\Phi_0=\delta_0,\qquad
\Phi_{-m}=\delta_0^{(m)}\quad(m\ge0).} \tag{CNO-02}
\]

The convention is
\(\langle\delta_0^{(m)},\varphi\rangle=(-1)^m\varphi^{(m)}(0)\).
In particular \(\Phi_{-2m}\ne0\). The zero of \(1/\Gamma(s)\) at a
nonpositive integer cancels a pole of the distributional numerator;
it does not turn the normalized distribution into zero.

For \(\Re s,\Re w>0\), the Beta integral yields
\(\Phi_s*\Phi_w=\Phi_{s+w}\). This extends to all complex \(s,w\)
without assuming a convolution interchange at a singular order:
choose integers \(N,M\) with \(\Re(s+N),\Re(w+M)>0\), then

\[
\Phi_s*\Phi_w
=D^{N+M}(\Phi_{s+N}*\Phi_{w+M})
=D^{N+M}\Phi_{s+w+N+M}
=\Phi_{s+w}. \tag{CNO-03}
\]

Thus \(\Phi_s^{-1}=\Phi_{-s}\). An element of this convolution group
cannot be the zero distribution, because its product with its inverse
is \(\delta_0\).

### Tempering retains the group and its boundary

For \(d\ge0\), define \(K_{s,d}=e^{-dt}\Phi_s\).
Multiplication by \(e^{-dt}\) commutes with convolution in the form

\[
(e^{-dt}S)*(e^{-dt}T)=e^{-dt}(S*T).
\]

Consequently

\[
K_{s,d}*K_{w,d}=K_{s+w,d},\qquad
K_{-m,d}=(D+d)^m\delta_0. \tag{CNO-04}
\]

The second formula follows from the distributional identity
\(e^{-dt}D S=(D+d)(e^{-dt}S)\). In particular the tempering terms at
the endpoint cannot be discarded.

For \(\Re p>0\), the Laplace transform is

\[
\mathcal L K_{s,d}(p)=(p+d)^{-s}. \tag{CNO-05}
\]

The power uses the holomorphic logarithm on \(\Re(p+d)>0\), real
on the positive axis. Prove it first by the Gamma integral for
\(\Re s>0\), then use (CNO-01) or holomorphic continuation. These
specific distributions have at most polynomial growth before
tempering, so their Laplace transforms exist on the stated domain.
For \(d>0\), \(d^sK_{s,d}\) is a probability Gamma density when
\(s>0\) is real, and is an entire convolution group after continuing
the order. Its negative orders need not be measures.

## 3. The complete source has an entire convolution-depth group

Set

\[
\rho_-=\frac{121-\sqrt{241}}{30},\qquad
\rho_+=\frac{121+\sqrt{241}}{30}.
\]

Then

\[
3<\rho_-<4<\rho_+<5,\qquad
\rho_-+\rho_+=121/15,\qquad \rho_-\rho_+=16.
\]

These exact source-determined rates and the positive subdivision law
below are inherited, not new probability assumptions about the orbit.

### Explicit entire extension of the source-depth semigroup

For \(z\in\mathbb C\), define

\[
\boxed{\mathcal Q_z
=15^z K_{z,0}*K_{z,3}*K_{z,4}*K_{z,5}
       *K_{-z,\rho_-}*K_{-z,\rho_+}.} \tag{CNO-06}
\]

Use \(15^z=\exp(z\log15)\) with real \(\log15\).
Every factor is causal and entire in \(z\), and every convolution is
well-defined on \(\mathcal D'_+\). Entire dependence can also be
checked directly: on a compact set of \(z\), shift all six orders
by one sufficiently large integer, express each as a fixed finite
differential operator applied to a locally integrable kernel, and
differentiate the resulting compact-simplex integrals. The same
integrable bounds apply uniformly on that compact parameter set.

Commutativity and the individual group laws give

\[
\mathcal Q_z*\mathcal Q_w=\mathcal Q_{z+w},\qquad
\mathcal Q_0=\delta_0. \tag{CNO-07}
\]

For \(\Re p>0\), the exact transform is

\[
\mathcal L\mathcal Q_z(p)=\exp(zL(p)),
\]

\[
L(p)=\log15+\log(p+\rho_-)+\log(p+\rho_+)
 -\log p-\log(p+3)-\log(p+4)-\log(p+5). \tag{CNO-08}
\]

Each logarithm here is holomorphic on the right half-plane and real
at positive real arguments. This specifies the logarithm of
\(\mathcal R(p)\); no unstated principal-power convention for the
image of \(\mathcal R\) is needed. In particular, at positive real
\(a\), the transform equals \(\mathcal R(a)^z\) with the real log.

At \(z=1\), the rational transform is exactly \(\mathcal R(p)\), so
Laplace uniqueness gives

\[
\mathcal Q_1=q_+,\qquad
\mathcal Q_j=q_+^{*j},\qquad
\mathcal Q_{-j}*q_+^{*j}=\delta_0\quad(j\ge0). \tag{CNO-09}
\]

The source remains the original four signed exponentials. The group
acts on continuous lag kernels, not by replacing \(U_0=0\) or by
running the discrete BBP recurrence backward.

### Positive depths recover the inherited positive volumes

Fix \(\lambda>0\). Normalize and tilt:

\[
\mu_{\alpha,\lambda}
=\mathcal R(\lambda)^{-\alpha}e^{-\lambda t}
 \mathcal Q_\alpha,\qquad \alpha\ge0.
\]

For every \(\alpha>0\), this is a probability measure. An explicit
construction uses independent Gamma variables of shape \(\alpha\)
and rates \(\lambda,\lambda+5\), and two compound-Poisson laws with
finite intensity measures

\[
\alpha\frac{e^{-(\lambda+3)t}-e^{-(\lambda+\rho_-)t}}{t}\,dt,
\qquad
\alpha\frac{e^{-(\lambda+4)t}-e^{-(\lambda+\rho_+)t}}{t}\,dt.
\tag{CNO-10}
\]

The numerators are nonnegative by strict interlacing. For \(0<r<s\),
the measure \((e^{-rt}-e^{-st})dt/t\) has mass \(\log(s/r)\).
Its compound-Poisson Laplace transform at \(p\ge0\) is

\[
\exp\left(\alpha\int_0^\infty
 (e^{-pt}-1)\frac{e^{-rt}-e^{-st}}t\,dt\right)
=\left[\frac r s\frac{p+s}{p+r}\right]^\alpha.
\]

Multiplying the four transforms gives exactly
\([\mathcal R(\lambda+p)/\mathcal R(\lambda)]^\alpha\).
This proves positivity and total mass one by an explicit construction.
It also identifies this family with the inherited source-depth
semigroup, rather than merely with a Gamma asymptote.

The entire family (CNO-06) is the unique entire distribution-valued
extension of that fully declared positive-depth family: pair two
candidate extensions with any compact test function and apply the
identity theorem on the positive real orders. Agreement only at
positive integer depths does not establish this uniqueness. For
example \(e^{2\pi i kz}\mathcal Q_z\), \(k\in\mathbb Z\), is another
entire causal convolution group agreeing at every integer depth.
For \(k\ne0\), it fails to retain the declared positive real-depth
probability family.

## 4. Exact negative source orders and their delta tower

Put

\[
P(a)=a(a+3)(a+4)(a+5),\qquad A(a)=15a^2+121a+240.
\]

For any integer \(m\ge0\), perform the unique polynomial division

\[
P(a)^m=A(a)^m B_m(a)+C_m(a),\qquad
\deg C_m<2m
\]

when \(m>0\); take \(B_0=1,C_0=0\). All coefficients are rational.
Then

\[
\boxed{\mathcal Q_{-m}
=B_m(D)\delta_0+H(t)g_m(t),\qquad
\mathcal L(Hg_m)(a)=\frac{C_m(a)}{A(a)^m}.} \tag{CNO-11}
\]

The proper rational remainder has only the two negative poles
\(-\rho_-\) and \(-\rho_+\), of orders at most \(m\).
Its inverse transform is therefore a finite real linear combination
of \(t^k e^{-\rho_\pm t}\), \(0\le k<m\). In particular \(g_m\)
is smooth on \([0,\infty)\) and exponentially decaying.

Because \(\deg P^m=4m\) and \(\deg A^m=2m\),

\[
\deg B_m=2m,\qquad
[a^{2m}]B_m=15^{-m}. \tag{CNO-12}
\]

Thus the highest singular term at negative source depth \(-m\) is
\(15^{-m}\delta_0^{(2m)}\). This is an exact consequence of the
source's order-two Gamma endpoint.

For \(m=1\), division gives

\[
\boxed{\mathcal Q_{-1}
=\frac1{15}\delta_0''+\frac{59}{225}\delta_0'
 -\frac{164}{3375}\delta_0+H(t)g_1(t),}
\]

\[
\mathcal L(Hg_1)(a)
=\frac{9944a+39360}{3375(15a^2+121a+240)}. \tag{CNO-13}
\]

Equivalently, the smooth remainder solves

\[
15g_1''+121g_1'+240g_1=0,\quad
g_1(0)=\frac{9944}{50625},\quad
g_1'(0)=-\frac{612824}{759375}.
\]

These initial values follow by matching the first two coefficients
of its Laplace transform at \(a=\infty\).

The full causal source obeys the distributional identity

\[
\boxed{D(D+3)(D+4)(D+5)q_+
=(15D^2+121D+240)\delta_0.} \tag{CNO-14}
\]

Away from zero the right-hand side vanishes, but the endpoint terms
are the complete numerator of the original rational source.
Discarding them would turn this source identity into a false
homogeneous equation on the full causal carrier.

## 5. Boundary jets explain exactly what the increment by two does

For a smooth \(f\) on \([0,\infty)\),

\[
D^m(Hf)=Hf^{(m)}
 \sum_{\ell=0}^{m-1}f^{(\ell)}(0)\,
       \delta_0^{(m-1-\ell)}. \tag{CNO-15}
\]

This follows inductively from \(D(Hf)=Hf'+f(0)\delta_0\).
The authentic source jets are

\[
q(0)=0,\qquad
q^{(k)}(0)=(-1)^{k+1}
          (2\cdot3^k+4^k+5^k)\quad(k\ge1).
\]

They begin \(0,15,-59,243\), and satisfy the exact coefficient
recurrence

\[
q^{(k+4)}(0)+12q^{(k+3)}(0)
 +47q^{(k+2)}(0)+60q^{(k+1)}(0)=0\quad(k\ge0).
\tag{CNO-16}
\]

For example
\(Dq_+=Hq'\),
\(D^2q_+=Hq''+15\delta_0\), and
\(D^3q_+=Hq'''+15\delta_0'-59\delta_0\).

Let \(f_j=q^{*j}\) on \(t\ge0\), \(j\ge1\). The inherited Beta
convolution calculation gives

\[
f_j(t)=\frac{15^j}{(2j-1)!}t^{2j-1}+O(t^{2j}).
\]

Thus \(f_j^{(\ell)}(0)=0\) for \(0\le\ell<2j-1\) and
\(f_j^{(2j-1)}(0)=15^j\). Substitution in (CNO-15) proves

\[
\begin{aligned}
D^m(Hf_j)&=Hf_j^{(m)} &&(0\le m<2j),\\
D^{2j}(Hf_j)&=Hf_j^{(2j)}+15^j\delta_0.
\end{aligned} \tag{CNO-17}
\]

Every additional source convolution delays the first boundary atom
by exactly two derivative orders. It does not create an infinite
parity pattern of scalar zeros.

This also checks the inverse's boundary directly. In
\(\mathcal Q_{-j}*q_+^{*j}\), every possible endpoint derivative
vanishes except
\(15^{-j}\cdot15^j\delta_0=\delta_0\).
The proper remainder cancels the remaining smooth part. The
rational transform identity establishes the cancellation globally;
the executable tests independently check its endpoint jets.

## 6. Exact forward-supported finite differences

For \(m\ge0\) and \(\varepsilon>0\), define a signed atomic measure

\[
\Delta_{m,\varepsilon}
=\varepsilon^{-m}\sum_{j=0}^{m}(-1)^j
 \binom mj\delta_{j\varepsilon}. \tag{CNO-18}
\]

All sample locations are nonnegative. For \(m\ge1\), repeated use
of the fundamental theorem of calculus gives the exact identity

\[
\langle\Delta_{m,\varepsilon},\varphi\rangle
=(-1)^m\int_{[0,1]^m}
 \varphi^{(m)}(\varepsilon(u_1+\cdots+u_m))\,du.
\]

Hence \(\Delta_{m,\varepsilon}\to\delta_0^{(m)}\) in
\(\mathcal D'_+\), and the explicit testwise error is

\[
\left|\langle\Delta_{m,\varepsilon}-\delta_0^{(m)},\varphi\rangle\right|
\le\frac{m\varepsilon}{2}
\sup_{0\le t\le m\varepsilon}|\varphi^{(m+1)}(t)|. \tag{CNO-19}
\]

For \(m=0\), the approximant is exactly \(\delta_0\).
The factor \(m/2\) is sharp already on the local polynomial
\(\varphi(t)=t^{m+1}\), multiplied by a cutoff equal to one on
the sampled interval.

A version with exact rational coefficients for rational
\(\varepsilon,\lambda\ge0\), \(\varepsilon>0\), is

\[
\Delta_{m,\varepsilon}^{(\lambda)}
=\left[\frac{\delta_0-\delta_\varepsilon}{\varepsilon}
       +\lambda\delta_0\right]^{*m}
\longrightarrow (D+\lambda)^m\delta_0. \tag{CNO-20}
\]

Its coefficient at \(j\varepsilon\) is
\(\binom mj(\varepsilon^{-1}+\lambda)^{m-j}
(-\varepsilon^{-1})^j\).
Expanding the convolution power and applying (CNO-19) bounds its
error by

\[
\frac{\varepsilon}{2}\sum_{k=1}^m
 \binom mk\lambda^{m-k}k
 \sup_{0\le t\le m\varepsilon}|\varphi^{(k+1)}(t)|.
\]

The inputs are forward observations; the processing uses signed
differences. This distinction is necessary. A distributional limit
of positive measures is a positive distribution, while
\(\delta_0'\) is not positive. The negative-order group cannot be
constructed using only positivity-preserving combinations.

Nor is the inverse uniformly noise stable. For \(m\ge1\),

\[
\|\Delta_{m,\varepsilon}\|_{\rm TV}
=2^m\varepsilon^{-m}.
\]

Independent errors of magnitude at most \(\eta\) in the sampled
values can therefore cause error
\(2^m\eta\varepsilon^{-m}\), and aligned error signs attain it.
The tempered rational stencil has total variation
\((2/\varepsilon+\lambda)^m\).
These are exact sensitivity statements. Mathematical support
causality alone does not supply derivative bounds or noiseless data.

## 7. The original source does not force negative-even zeros

For \(a>0\), pair the universal family with the exponentially
decaying source:

\[
M_a(s)=\langle\Phi_s,e^{-at}q(t)\rangle.
\]

This is well-defined by choosing a smooth cutoff on the negative
half-line, equal to one near \([0,\infty)\), so the test is Schwartz.
The value is independent of that cutoff. Formula (CNO-01), with
exponential decay at infinity, proves entire dependence on \(s\).
For \(\Re s>0\), the ordinary Gamma integral gives

\[
\boxed{M_a(s)=4a^{-s}-2(a+3)^{-s}
 -(a+4)^{-s}-(a+5)^{-s}.} \tag{CNO-21}
\]

The right-hand side is entire in \(s\), hence is the unique
continuation. This power-source interface is inherited from
observational_succ/euler_bbp_regulator.py; only \(s=1\) at
\(a=8n-7\) is the original forcing.

At every nonnegative integer \(m\),

\[
M_a(-m)=(-1)^m(e^{-at}q(t))^{(m)}(0)
=4a^m-2(a+3)^m-(a+4)^m-(a+5)^m.
\]

Thus \(M_a(0)=0\), but for every \(a>0\) and integer \(m\ge1\),

\[
\boxed{M_a(-m)<0.} \tag{CNO-22}
\]

Indeed each shifted positive power is strictly larger than \(a^m\),
and its positive weights sum to 4. In particular
\(M_a(-1)=-15\) and \(M_a(-2)=-30a-59\).
This is an authentic-source discriminator: forward support,
positive real-order readouts, entire continuation, and a Gamma(2)
endpoint do not force negative-even zeros. Such zeros require
additional identities of the chosen scalar source/readout.

## 8. Implementation proof and finite validation

The new module observational_succ/bbp_causal_inverse.py represents
(CNO-11) with rational polynomials in ascending powers. Its
constructor verifies the unchanged source identity

\[
A^m B_m+C_m=P^m
\]

and the strict properness of the remainder. This fixes the
decomposition uniquely. No algebraic decay rate is rounded.
Convolution multiplies complete rational symbols and performs a
new exact division; it retains all boundary terms.

For the regular remainder, the Laurent expansion at infinity is
\(\sum_{k\ge0}g_m^{(k)}(0)a^{-k-1}\).
There is no missing factorial: integrating
\(g_m^{(k)}(0)t^k/k!\) produces \(g_m^{(k)}(0)a^{-k-1}\).
Coefficient comparison with \(C_m/A^m\) gives exactly the recurrence
implemented by remainder_jet. The singular pairing separately
uses the signs \((-1)^k\) of distributional derivatives.

The implementation bounds inverse order by 8 and the requested
regular derivative order by 32, rejects floats and booleans in exact
arithmetic inputs, and authenticates all polynomial fields. Its
nonnegative inverse-symbol domain includes \(a=0\); the original
source transform excludes that endpoint because its total mass
diverges there.

**Observed validation, 2026-11-15:** all 14 tests in
tests/test_bbp_causal_inverse.py passed. Independent controls use
literal four-pole fractions, raw multiplication of the four pole
factors, and convolution of endpoint jets. For inverse depths
1 through 4, the actual source convolution has exactly the unit
delta boundary and zero regular jets through order 18.
Wrong derivative signs, omitted delta terms, an omitted regular
remainder, a mutated original pole, and invalid domains are tested.

The tests do not establish entire continuation. That claim rests
on the construction and proofs in Sections 2–3.

## 9. Verdict and next boundary

The requested causal construction exists on the stated distribution
carrier, with uniqueness from the fully declared positive-side
analytic family. The complete original source extends from its
inherited positive-depth semigroup to an entire convolution group.
Its negative integer depths have an exact, reusable rational
normal form and a source-specific delta tower.

The inference that the original undeformed source readout must have
negative-even zeros is refuted by (CNO-22). Other face-depth and
convolution-depth readouts must be analyzed with their own parameters.
This leaves a precise dependency:
identify and prove an additional scalar-readout symmetry or
endpoint-jet parity law. Neither positive time support nor the
increment by two supplies that law by itself.

## 10. Closing proof and code review receipt

**2026-11-15; internal review, not external peer review.** The constructor
reviewed CN-01 through CN-03 and CN-07 of the assembled THEOREMS.md at
SHA-256
191cf7d8436c7e20c4fa0c591e21a4fd64b8e9ccf41169f49e247141ceca8ed2.
The stated causal support, derivative signs, Laplace domain, entire
dependence, positive-family uniqueness, inverse constants, source
mixture normalization, and first-contact statements are correct within
their hypotheses.

The source/derivative clock clarification in CN-07 was verified:
negative source depth is Q_-j, while its leading delta derivative has
order 2j. CN-03 now gives the compact-parameter shifted-kernel argument
for entire dependence and explicitly distinguishes full positive-depth
agreement from positive integer samples. No requested mathematical
correction remains open in those reviewed sections.

The reviewed implementation SHA-256 is
d37f9b0086fe42833977217c1db969f6936c32dbb3764f738b7caa341779fb32
for observational_succ/bbp_causal_inverse.py. The reviewed tests have
SHA-256
f5339ff8d20d0c7c3f311e7e24643bf737e34dc87e37563bfcdb5ab13e07aa5e
for tests/test_bbp_causal_inverse.py. The source authentication,
polynomial division, Laurent-jet recurrence, derivative pairing signs,
and cascade operations agree with the proofs above. The module's
causal extension is written H(t)q(t), avoiding confusion with a
convolution of H and q. The 14-test result in Section 8 is the
observed focused run; no broader suite result is claimed here.

### Final theorem snapshot — 2026-11-15

The closing review was refreshed against THEOREMS.md SHA-256
112634fd9d370be421b5ca4d9619c9ea01fd259b8cdbd4ecef6f97f422db04f1.
CN-01 through CN-03 and CN-07 remain correct within their stated
domains, with no outstanding requested correction.

The added CN-01 identities were checked directly:
\(X\Phi_s=s\Phi_{s+1}\) follows from the Gamma recurrence on the
positive half-plane and extends by entire continuation;
\((DX-XD)T=T\) is the distributional product rule.
At negative integer order this gives
\(t\delta^{(m)}=-m\delta^{(m-1)}\), with the displayed sign.
These are operator identities on the causal carrier and do not
alter its commutative convolution law.

This closing update performed no additional implementation or tests.
The earlier snapshot receipt remains as review history.

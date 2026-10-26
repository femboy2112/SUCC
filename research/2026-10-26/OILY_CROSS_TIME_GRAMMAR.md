# Oily cross-time grammar: true cumulant hierarchy, temporal nonuniqueness, and the seed-character firewall

**Date:** October 26, 2026. **Parent:** draft #310, `a8c7c85b7a1900d422090f1757c174e7aac69f44`.
**Authority:** paper proofs below, with separate exact/numerical audit in
`OILY_HOSTILE_AUDIT.md`. No Lean authority or academic-priority claim.
**Selected Fourier improvement:** none from this front. π normality remains OPEN.

## 1. The dependency cut and its actual verdict

The proposed cut was: replace the externally golden-centered one-time covariance
by an intrinsic connected object, transport it across actual arithmetic time, and
extract a seed-selective signed inequality. This front establishes three precise
boundaries, rather than assuming the last arrow:

1. All genuine mixed cumulants with one packet-grade observable have a
   **graded hierarchy**. With `m` logarithmic slots, the first possible term is
   of order `a^(-m)`, not `a^(-1)`. Its coefficient is determined solely by the
   conditional grade law; for the declared primitive Fourier filters it
   introduces no Euler constant. In particular, the
   genuine third cumulant for the odd-grade projector has leading coefficient
   **`8/81` at order `a^(-2)`**.
2. The exact source time tilt does **not uniquely select a joint probability law
   across times**. Two explicitly source-derived Markov kernels have the same
   prescribed marginals but cross-time primitive covariance zero versus a
   positive quantity tending to `20/81`.
3. Seed-invariant fixed-harmonic phase monomials of total degree below **17**
   cannot have a nontrivial off-diagonal resonance. The first possible one,
   `Z_n^16 conjugate(Z_(n+1))`, is exactly the forcing character and is blind to
   the initial selector. All seed-invariant monomials, at any degree, are blind
   to the initial selector by definition and by the explicit character law.

These are new proof-level restrictions within the declared grammar. They do not
refute a theorem that genuinely uses `U_0=0`, and do not prohibit carry-dependent,
nonpolynomial, or frequency-mixed constructions. They locate what those
constructions must add. The elementary facts used are derived below; priority
outside this repository is unverified.

## 2. Exact source passport and conventions

Retain exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_{n+1}=16U_n+r(n+1).
$$

The packet source from #309/#310 is

$$
R(x)=\frac{1-x}{(2-x^2)(x^2-2x+2)},\quad
p_j(x)=\frac{1-x}{4}\sum_{k=0}^j u(x)^kv(x)^{j-k},
$$

where `u=x-x²/2`, `v=x²/2`. Let `a=8n`, `n>=1`,

$$
T_n=\int_0^1x^aR(x)\,dx,\qquad
\mu_n(dx,j)=\frac{x^ap_j(x)}{T_n}\,dx.
$$

This front uses **`Y=a(1-X)`**, and `L=log Y`, as in the #310 third-shadow
dossier. It does not silently substitute the different finite coordinate
`-a log X` used in part of #309.

For a fixed bounded complex grade function `g`, put

$$f_g(x)=\mathbb E[g(J)\mid X=x].$$

The conditional law is the sum of the two geometric loop counts. On a
neighborhood of `x=1`, its probabilities and all their derivatives have an
exponentially summable grade envelope. Consequently `f_g` is analytic there;
it is smooth on `[0,1]`. The primitive Fourier choices
`g(j)=1_(gcd(j,q)=1) z^j`, `|z|<=1`, satisfy these hypotheses.

Write the endpoint expansion

$$f_g(1-t)=C+Ht+Kt^2+O(t^3).$$

Thus `C=f_g(1)`, `H=-f_g'(1)`, and `K=f_g''(1)/2`; these signs are fixed.

## 3. The genuine mixed cumulant has a second-order, gamma-free leading term

Define the mixed cumulant with one grade slot and `m` logarithmic slots by

$$
\kappa_{n,m}(g)=
\left.\frac{\partial^{m+1}}{\partial\tau\,\partial s^m}
\log\mathbb E_n[\exp(\tau g(J)+sL)]\right|_{\tau=s=0},\qquad m\ge1.
$$

The logarithm is its analytic branch near `(0,0)`, where the expectation is
one. This definition is algebraic for complex `g`, with no conjugation.
Boundedness of `g` and the source endpoint zero justify all derivatives near
zero. Subtracting any deterministic center from `L` does not change these
mixed cumulants: it adds a term independent of `tau` to the logarithm.

The decisive simplification is

$$
\kappa_{n,m}(g)=F_a^{(m)}(0),\qquad
F_a(s)=\frac{\mathbb E_n[g(J)Y^s]}{\mathbb E_n[Y^s]}.
$$

The Gamma factor in an unnormalized Mellin moment cancels in this ratio.
For `s` in any sufficiently small fixed complex disk about zero,

$$
\boxed{
F_a(s)=C+\frac{H(s+2)}a+
\frac{K(s+2)(s+3)-H(s+2)(s+5)}{a^2}+O(a^{-3}).
}
$$

The error is locally uniform and analytic, so its fixed-order derivatives
obey the same bound by Cauchy's formula.

**Proof.** Put `t=1-x` and

$$
w(t)=\frac1{(2-(1-t)^2)((1-t)^2-2(1-t)+2)}
=\frac1{1+2t+2t^3-t^4}=1-2t+4t^2+O(t^3).
$$

The common factors `a^s/T_n` cancel. The numerator and denominator of `F_a`
are integrals against `(1-t)^a t^(s+1) w(t) dt`, with the numerator additionally
weighted by `f_g(1-t)`. Euler's beta identity gives

$$
\frac{B(a+1,s+2+r)}{B(a+1,s+2)}
=\frac{(s+2)_r}{(a+s+3)_r}.
$$

With `k=s+2`, the weighted moment ratios therefore are

$$
\mathbb E_s[t]=\frac{k}{a}-\frac{k(k+3)}{a^2}+O(a^{-3}),
\qquad
\mathbb E_s[t^2]=\frac{k(k+1)}{a^2}+O(a^{-3}).
$$

Here `E_s` denotes the normalized complex beta/source integral; no probability
interpretation for complex `s` is asserted. Substituting `C+Ht+Kt²` proves
the formula. Taylor remainders are bounded by a constant times `t³` on
`[0,1]`; their beta ratios are `O(a^-3)` uniformly on a fixed compact
`Re(s)>-2`. The denominator tends locally uniformly to one after division
by the beta factor, hence stays away from zero. This also proves the
analytic uniformity used above.

In particular,

$$
\boxed{
a\kappa_{n,1}(g)\longrightarrow H,\qquad
a^2\kappa_{n,2}(g)\longrightarrow2(K-H).
}
$$

For every `m>=2`, the `a^-1` coefficient is zero. The #310 golden-centered
raw covariance is still correct, but it is not this cumulant. Its Euler/golden
coefficient comes from its externally declared center.

### Exact dyadic primitive coefficient, including complex phase

For `g(j)=z^j 1_(j odd)`, `|z|<=1`,

$$
f_g(x)=\frac{(1-u)(1-v)zx}{(1-z^2u^2)(1-z^2v^2)}.
$$

Direct differentiation, or expansion in `t=1-x`, gives

$$
C=\frac{4z}{(4-z^2)^2},\qquad
H=\frac{4z(4-5z^2)}{(4-z^2)^3},
$$

$$
K=\frac{8z(7z^4+8z^2-16)}{(4-z^2)^4},\qquad
2(K-H)=\frac{8z(9z^4+40z^2-48)}{(4-z^2)^4}.
$$

At `z=1`, `C=4/9`, `H=-4/27`, `K=-8/81`, so

$$
\boxed{\lim_{n\to\infty}(8n)^2
\kappa(1_{J\text{ odd}},\log Y,\log Y)=\frac8{81}.}
$$

This limit is invariant under additive recentering of `log Y`. It is **not**
invariant under changing the packet grade function or regrading packets.
No golden constant or Euler constant occurs in its leading coefficient.

## 4. All-order hierarchy and its source-blind leading coefficients

For each fixed integer `M>=1`, the same argument gives

$$F_a(s)=C+\sum_{k=1}^{M}a^{-k}P_k(s)+O(a^{-M-1}),\qquad \deg P_k\le k.$$

Consequently, for every fixed `m>=1`,

$$
\boxed{
\kappa_{n,m}(g)=O(a^{-m}),\qquad
\lim_{n\to\infty}a^m\kappa_{n,m}(g)
=m!\,[v^m]f_g\!\left(\frac1{1+v}\right).
}
$$

The coefficient extraction is from the Taylor series at `v=0`.

For the odd projector this entire leading hierarchy has an exact rational
generating function:

$$
\boxed{
f_{\rm odd}(1/(1+v))
=\frac{4(1+v)^3}{(2v^2+6v+3)(2v^2+4v+3)}
=\frac49-\frac4{27}v+\frac4{81}v^2-\frac{28}{243}v^3
+\frac{232}{729}v^4+O(v^5).
}
$$

Thus the limits for `m=1,2,3,4` are respectively
`-4/27`, `8/81`, `-56/81`, and `1856/243`. If `c_m` is the coefficient of
`v^m`, the exact recurrence for `m>=4` is
`9c_m+30c_(m-1)+36c_(m-2)+20c_(m-3)+4c_(m-4)=0`.
This is a compact exact calculator for the limiting connected hierarchy,
not a recurrence for the selected arithmetic phases.

**Proof with degree and limit accounting.** Taylor-expand `w(t)` and
`w(t)f_g(1-t)` through order `M`; their respective coefficients are `c_r`
and `b_r`. Divide each integral by `B(a+1,s+2)`. The result is the ratio
of the two finite sums of

$$b_r\frac{(s+2)_r}{(a+s+3)_r},\qquad
c_r\frac{(s+2)_r}{(a+s+3)_r},$$

up to locally uniform `O(a^-M-1)`. In the `a^-k` coefficient of a ratio
with index `r<=k`, the Pochhammer numerator has degree `r` in `s`, while
expansion of the denominator contributes degree at most `k-r`. The
degree is therefore at most `k`. Formal division preserves this property.

To compute the highest-degree coefficients, keep only the top-degree
terms at every order and write `v=s/a`. Then the beta ratio is replaced by
`[v/(1+v)]^r`. The numerator/denominator ratio of these top-degree generating
series is

$$
\frac{w(v/(1+v))\,f_g(1-v/(1+v))}{w(v/(1+v))}
=f_g(1/(1+v)).
$$

Thus the coefficient of `s^m` in `P_m` is the stated coefficient of `v^m`.
Differentiate `m` times at zero, use the polynomial-degree bound to kill
all `k<m`, and use the analytic remainder control. This proves the limit
without interchanging two unbounded limiting parameters: `m` is fixed.

**Scope and novelty tax.** This theorem is a source-typed cumulant calculation,
not a new selected-phase bound. In fact, the leading coefficient is unchanged
if the outer positive source weight `w` is replaced by any smooth positive
weight with nonzero endpoint value while the conditional grade law `f_g` is
held fixed. It therefore cannot authenticate the entire four-pole forcing.
For the primitive Fourier filters its coefficients are rational functions of
`z` (and finite Möbius sums for fixed `q`). The leading hierarchy contains no
Euler constant. Neither claim excludes Euler constants in other observables,
nonlocal finite parts, or genuinely carry-conditioned laws.

The same leading-coefficient theorem even holds if the endpoint factor
`(1-x)` is replaced by `(1-x)^(alpha-1)` for any fixed real `alpha>0`,
with `g`'s conditional law unchanged. The beta ratio becomes
`(s+alpha)_r/(a+s+alpha+1)_r`, whose top-degree generating substitution
is again `[v/(1+v)]^r`. These are explicitly **changed-source controls**:
they do not preserve the original BBP kernel. They demonstrate that this
leading connected hierarchy alone does not even select the Gamma shape.

### One differential generator for the whole leading hierarchy

There is a compact exact operator form of the preceding theorem. Define the
local fractional-linear flow and its generator by

$$
\Phi_v(x)=\frac{x}{1+vx},\qquad
\mathcal L=-x^2\frac{d}{dx}.
$$

Whenever the denominators are nonzero,
`Phi_v(Phi_w(x))=Phi_(v+w)(x)`. In the reciprocal coordinate `u=1/x`,
this is precisely the additive translation `u -> u+v`. For `x` near one
and `v` near zero the flow is analytic, and direct differentiation gives

$$
\frac{d}{dv}f_g(\Phi_v(x))=(\mathcal Lf_g)(\Phi_v(x)).
$$

Iterating this identity at `v=0`, with the fixed-order limit already proved
above, yields

$$
\boxed{
\lim_{n\to\infty}(8n)^m\kappa_{n,m}(g)
=\left.(\mathcal L^m f_g)(x)\right|_{x=1},\qquad m\ge1.
}
$$

Thus one reciprocal-translation generator produces every leading connected
coefficient. For example, `L f_g(1)=H` and
`L² f_g(1)=2f_g'(1)+f_g''(1)=2(K-H)`. This is an exact relation between
the endpoint grade observable, a fractional-linear flow, and the asymptotic
mixed-cumulant hierarchy; no numerical constant has been fitted.

**Boundary.** This fractional-linear use of “Möbius” is distinct from the
arithmetic Möbius function in the primitive projector. The flow expresses
the highest-degree beta-tilt coefficients; it is not proved to equal finite
arithmetic time evolution, a carry transition, or a canonical flow selecting
the BBP source. It retains dependence on `f_g` and inherits the source-weight
and Gamma-shape blindness established above. No selected Fourier estimate
follows from the flow law alone.

## 5. The common source gives a killed semigroup, not a unique cross-time law

On `omega=(x,j)` the exact source relation is

$$
\mu_{n+1}(d\omega)=\frac{x^8}{Z_n}\mu_n(d\omega),\qquad
Z_n=\frac{T_{n+1}}{T_n}=\mathbb E_n[X^8]\in(0,1).
$$

Multiplication by `x^(8k)` gives an exact sub-Markov survival semigroup.
Conditional on surviving `k` steps from `mu_n`, the latent state has law
`mu_(n+k)`. This is a legitimate source-derived construction. It does not
by itself give a probability coupling with both original marginals
`mu_n` and `mu_(n+k)`: after conditioning on survival, the earlier latent
state has also been reweighted.

Here are two full probability kernels, both derived solely from the same
source and both pushing `mu_n` to `mu_(n+1)`:

$$
K_n^{\rm ind}(\omega,d\omega')=\mu_{n+1}(d\omega'),
$$

$$
K_n^{\rm persist}(\omega,d\omega')
=x^8\delta_\omega(d\omega')+(1-x^8)\mu_{n+1}(d\omega').
$$

The second keeps the state after survival and redraws after death. Its
pushforward is
`Z_n mu_(n+1)+(1-Z_n)mu_(n+1)=mu_(n+1)` exactly. Iterating either kernel
gives a consistent process with every required one-time packet/source
marginal. Neither is claimed to be an arithmetic process producing π digits.

For any fixed bounded real `g=g(J)`, the two successive-time covariances are

$$
\boxed{
\mathrm{Cov}_{\rm ind}(g(J_n),g(J_{n+1}))=0,\qquad
\mathrm{Cov}_{\rm persist}(g(J_n),g(J_{n+1}))
=Z_n\mathrm{Var}_{\mu_{n+1}}(g).
}
$$

To check the second identity, its joint moment is

$$Z_n\mathbb E_{n+1}g^2+
(\mathbb E_ng-Z_n\mathbb E_{n+1}g)\mathbb E_{n+1}g.$$

Subtract the product of the marginals. For the odd-grade indicator,
`Z_n -> 1` and its mean tends to `4/9`, so the second covariance tends to
`20/81`, whereas the first is zero at every time.

**Receipt and verdict.** Equal full one-time packet laws, equal exact source
time tilt, and equal one-time Mellin/cumulant towers do not determine
cross-time primitive covariance. A proposed arithmetic interpretation must
supply and verify an additional map from an actual carry/state history to
the joint process; declaring a natural-looking coupling does not provide it.
For fixed actual `n,m`, the factor `e(h(U_n-U_m))` is deterministic on this
auxiliary probability space and factors out of every auxiliary covariance.
The resulting coefficient can depend on the chosen temporal coupling.
If time indices are also randomized, the phase need not factor out of the
outer expectation; that outer expectation retains the signed arithmetic
cross-time sum and needs its own estimate.

## 6. The fixed-harmonic seed-character resonance firewall

Let `U_n(s)` solve the unchanged forcing recurrence with initial value `s`,
so `U_n(s)=U_n(0)+16^n s`. Fix `h` a nonzero integer and write
`Z_n(s)=exp(2 pi i h U_n(s))`. For an integer, finitely supported vector
`k=(k_n)`, its phase monomial has exact seed character

$$
\boxed{
\prod_n Z_n(s)^{k_n}
=\exp\!\left(2\pi i h\sum_nk_nU_n(0)\right)
\exp\!\left(2\pi i h s\sum_nk_n16^n\right).
}
$$

Negative powers mean conjugates. Define its reduced degree
`d=sum |k_n|`; cancel equal phase/conjugate factors first. The monomial
is invariant under all real seed changes exactly when

$$\sum_n k_n16^n=0.$$

If the vector is nonzero, choose its least occupied index `j`. Dividing
by `16^j` shows that `k_j` is a nonzero multiple of 16. Hence
`|k_j|>=16`, and at least one other coefficient is nonzero. Therefore

$$\boxed{\sum_n k_n16^n=0,\ k\ne0\quad\Longrightarrow\quad d\ge17.}$$

The bound is sharp. Its first two-time example is

$$
\boxed{Z_n(s)^{16}\overline{Z_{n+1}(s)}=e(-h r(n+1)),}
$$

which is precisely the recurrence's forcing character. Thus fixed-harmonic
quadratic, cubic, and quartic **monomials** cannot possess a nontrivial
seed-invariant off-diagonal phase after trivial cancellations. The relative
four-step sign of the Gaussian **coefficient** atom is a different clock;
it does not override this arithmetic character calculation.

For every degree, invariant monomials are explicitly functions of the forcing,
and have the same value on the zero-seeded orbit and on the coherent seed
`s=-T_0=-pi/16`, whose states are `-T_n`. Arbitrary coefficients built from
the packet kernels, atomic matrices, or Mellin cumulants do not change this
seed character if those coefficients are seed-independent.

**Boundary.** A polynomial sum can have cancellations among terms with the
same nonzero seed character; the stated degree theorem is for its reduced
monomials, not an assertion that every syntactically written polynomial has
nonzero dependence. Mixed frequencies can lower the displayed factor count
by inserting frequency `16h` explicitly. An estimate at `s=0` need not be
seed-invariant. Neither possibility is excluded. A proof using one must
identify the actual initial-selector information rather than obtaining it
from a seed-invariant observable.

## 7. Source comparison, verification, and the next falsifier

The #307 Hilbert carrier and exact normalized source-time cocycle were read
at `c41af6b0a1e96a7758cbf891cd56014be743beb0`; the #308 signed two-atom/null
channel dossier was read at `48bbfc78f499fbcac6e0b51f06a3ec60aa693731`.
Their exact transports and controls are preserved. Nothing here promotes
their positive overlap or coefficient holonomy to a selected signed saving.

The beta identity used in §§3–4 is the classical
[Euler beta integral, DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1), checked
against the official NIST source on October 26, 2026. The new asymptotic
hierarchy and seed-degree argument are derived here rather than attributed
to that reference. The polynomial-degree proof is independent of fitting
numerical constants. Separate hostile verification independently recovered
the second-order coefficient before comparing formulas.

The independent standard-library Fraction calculator
[oily_hostile_oracle.py](oily_hostile_oracle.py), with its
[exact receipt](OILY_HOSTILE_ORACLE_RECEIPT.json), checks the normalized
beta-jet algebra through order six, the degree bound, the leading
coefficient substitution, an alternative positive outer weight, and a
finite survival-kernel counterexample. Its first six leading coefficients
are `-4/27`, `8/81`, `-56/81`, `1856/243`, `-56320/729`, and
`581120/729`. The hostile proof audit separately checked the all-order
argument, the temporal-kernel maps, and the sharp reduced degree 17.
These agents share a model family; this is not external mathematical
peer review. The finite oracle corroborates algebra and does not replace
the uniform analytic remainder proof.

A separate direct 60-decimal-digit quadrature used the `y=a(1-x)` density
`y(1-y/a)^a/[1+2(y/a)+2(y/a)^3-(y/a)^4]`, normalized by its integral,
and `f_odd(1-y/a)`. It integrated the logarithmic moments directly and
formed the derivatives of the normalized moment ratio recursively. The
observed triples `(a κ_1,a² κ_2,a³ κ_3)` were:

| `a` | `a κ_1` | `a² κ_2` | `a³ κ_3` |
|---:|---:|---:|---:|
| 64 | -0.1412660245176798 | 0.05668195499435764 | -0.2048631752151938 |
| 256 | -0.1461497316364131 | 0.08441339551335255 | -0.5125117188597383 |
| 1024 | -0.1476258643173083 | 0.09483976856396614 | -0.6410672377245754 |
| proved limit | -0.1481481481481481 | 0.09876543209876543 | -0.6913580246913580 |

These finite floating-point values are **observations**, not sound interval
certificates or proofs of the limits. They were not used to fit the theorem.
Exact symbolic differentiation independently reproduced the displayed
complex `K(z)` and `2(K-H)` rational functions.

**Next lamp.** Construct an actual carry-conditioned source map with an
explicit boundary/initial-state readout, and check its Fourier character
before computing a cumulant. The first pass/fail test is whether the map
distinguishes `U_0=0` from `U_0=-T_0` for an arithmetic reason. If it does,
prove an off-diagonal estimate using that distinguishing datum; if it does
not, this front's exact seed character predicts that another source-only
Mellin/holonomy calculation will not supply the missing selector.

The phase bound from this front remains the existing selected frontier;
these results neither prove nor disprove the authentic `S_N(h)=o(N)`.

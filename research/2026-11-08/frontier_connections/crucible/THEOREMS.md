# Clock cohomology, signed coefficient budgets, and a rank-one trap

Status: **PROVED PAPER** for the finite statements below. These specialize
classical finite cohomology and Fourier averaging to the authenticated prime
clock. They are not claimed as new general theorems in harmonic analysis.
Original-zero signed covariance decay and pi normality remain **OPEN**.

The inherited source is exactly
`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U0=0`.
The native clean interval, principal parts, and fold are those of
[`complement_budget`](../../complement_budget/README.md):
`S=xi H`, `H=<16> in F_p^*`, `m=|H|`,
`a(x)=e(hx/p)`, `r_h=conj(a)`, and `W=E_S aB`.
The symbol `r_h` here is a unit phase; it is not the BBP forcing `r(n)`.
All statements use a single declared coherent phase frame.

## QCO1. The arithmetic budget descends to clock orbits of polynomials

Reduce polynomials in `F_p[X]/(X^m-xi^m)`, using representatives of degree
less than m. Substitution `TQ(X)=Q(16X)` is an automorphism of this quotient,
and `T^m=Id`. Indeed `(16X)^m-xi^m=X^m-xi^m`; no source point is changed.

For every reduced Q let `mu(Q)=E_S e(Q(x)/p)`. The permutation `x->16x`
of S gives the **exact signed identity** `mu(TQ)=mu(Q)`. The degree of a
nonconstant reduced polynomial is unchanged by T. For every orbit O of
nonconstant polynomials put

```
D_O = degree(Q), Q in O,
w_O = min(1,D_O*sqrt(p)/m).
```

The inherited PR3 Weil estimate gives `|mu(Q)|<=w_O`. This use of Weil
has precisely the degree and prime-field hypotheses already checked in PR3;
it introduces no extra assumption about RH.

Suppose an arbitrary finite complex model is

```
B(x) = R*r_h(x) + sum_Q c_Q e((Q(x)-h*x)/p) + E(x),
```

where Q ranges over nonconstant reduced polynomials. Extend missing
coefficients by zero in their finite T-orbits, and put `C_O=sum_(Q in O)c_Q`.
Then, for every such model, even with coefficients selected after observing B,

```
|W| <= |R| + E_S |E| + sum_O w_O*|C_O|.                  (QCO1)
```

Proof: multiply the displayed model by a, average over S, group identical
means by T-orbit, and use the triangle inequality only after that grouping.
Constant Q terms, if present, must first be incorporated into R with their
actual factors `e(Q/p)`; they cannot be declared nonresonant. QED.

This is at least as strong as the atomwise PR8 triangle budget because
`|sum c_Q|<=sum |c_Q|`. It retains cross-term cancellations with a proved
common transport. The improvement is strict: for a nonconstant Q with
`TQ!=Q`, the model

```
B=(e((TQ-hX)/p)-e((Q-hX)/p))/2
```

has `|B|<=1`, zero quotient cost and W=0, but its displayed atomwise cost
is `w_O>0`. For example `p=17, xi=1, h=1, Q=X` gives a nonzero B.
This does not say the earlier CB1 lower bound is wrong: QCO1 is a different
cost functional, and CB1 applies to its stated atomwise cost.

## QCO2. The cancellations are authenticated twisted coboundaries

For any function G on S define

```
D_h G(x)=e(15*h*x/p) G(16*x)-G(x).
```

Multiplication by a conjugates this operator to an ordinary cyclic
difference: `a D_hG = (aG)(16x)-(aG)(x)`. Consequently

```
E_S a D_hG=0.                                         (QCO2a)
```

For `phi_Q=e((Q-hX)/p)`, `D_h phi_Q=phi_(TQ)-phi_Q`.
Every coefficient vector on a T-orbit whose signed coefficient sum is zero
is a sum of these adjacent differences. Explicitly, enumerate an orbit
`Q_j=T^jQ_0`, length d, let `sum_j c_j=0`, set `g_0=0` and
`g_j=-sum_(i=1)^j c_i`. Then `c_j=g_(j-1)-g_j` cyclically, so
`sum c_j phi_(Q_j)=D_h(sum g_j phi_(Q_j))`.

Thus QCO1 discounts exactly the part of this representation certified by
the clock difference relation. Extra relations between different polynomial
orbits may exist; QCO1 does not claim this is a complete quotient basis.

Conversely, because S is one m-cycle, a function B is of the form D_hG iff
`W=0`. To see sufficiency, write `x_j=xi*16^j`, `f_j=a(x_j)B(x_j)`, and
set `H_0=0`, `H_j=sum_(i<j)f_i`, `G(x_j)=conj(a(x_j))*H_j`.
The cyclic boundary closes exactly iff `sum f_i=0`.

More generally every B admits `B=W*r_h+D_hG`. The residual coefficient in
this unrestricted decomposition is the desired W itself. Therefore the
mere existence of a learned primitive is **not** an independent decay premise.

For an open segment of k clock edges, the exact remaining boundary is
`sum_(j=0)^(k-1) a_j D_hG_j = a_k G_k-a_0G_0`; its normalized magnitude
is at most `2||G||_infinity/k`. Arbitrary independent gauge rotations break
this equality unless the operator and observations are transported together.

## QCO3. The inverse has sharp size m/(2 pi), asymptotically

Use normalized L2 on S and put `f_j=a_j B_j-W`. Let
`fhat(k)=m^-1 sum_j f_j e(-kj/m)`.
Among solutions `D_hG=B-W*r_h`, the unique solution with `E_S aG=0` has

```
||G||_2^2 = sum_(k=1)^(m-1) |fhat(k)|^2/[4 sin^2(pi*k/m)].       (QCO3)
```

Proof: the cyclic shift has Fourier multiplier `e(k/m)`; hence the unique
mean-zero solution H=aG has Fourier coefficient
`fhat(k)/(e(k/m)-1)` at nonzero k. Apply finite Parseval. Adding a constant
to H is the full kernel and increases the norm. In particular, for m>=2,

```
||G||_2 <= ||B-W*r_h||_2/[2 sin(pi/m)].
```

Equality occurs for a single temporal Fourier mode k=1 (or m-1), so the
factor is sharp and grows as m/(2*pi). A uniform bounded inverse cannot be
inferred from exact finite solvability. This is finite cyclic linear algebra,
not an invocation of a Livsic theorem with unverified dynamical hypotheses.

## QCO4. Canonical zero-extension Fourier compression is rank one

Extend B by zero from S to F_p, and define its full additive Fourier
coefficients

```
c_t=(1/p) sum_(x in S) B(x)e(-t*x/p),
B(x)=sum_(t in F_p)c_t e(t*x/p) on S.
```

The covariance polynomial is `(t+h)X`. Its nonzero T-orbits are exactly the
multiplicative H-cosets O of `d=t+h`. Then

```
c_(-h)=(m/p)W,
C_O := sum_(d in O)c_(d-h)
     = (m/p) W * G_O,
G_O := sum_(d in O)e(-d*xi/p).                         (QCO4)
```

Proof: the first formula is the definition of W. For the second, interchange
the two finite sums and note that for every `x=xi*u`, `u in H`, multiplication
by u permutes O. Thus `sum_(d in O)e(-dx/p)=G_O` is independent of x.
The remaining sum over x is mW. QED.

Every canonical quotient coefficient is therefore a known scalar multiple
of W. The apparent reduction from p Fourier coefficients to `(p-1)/m`
orbit sums is exactly a rank-one projection on this zero-extended family.
With `beta=min(1,sqrt(p)/m)`, its total retained-resonance plus quotient
upper certificate is precisely

```
(m/p) * (1+beta*sum_O |G_O|) * |W|.                   (QCO4b)
```

It can be numerically much smaller than the original atomwise cost, but this
canonical construction has not replaced the missing estimate: it has already
read W. This refutes the shortcut “quotienting canonical Fourier coefficients
proves their source-selected resonance decays.” The countermodel B=conj(a)
has W=1 and satisfies the same exact quotient formulas. Hence QCO4b's factor
must be at least1; the earlier arithmetic character bound also proves this.

Independent source-derived representations with small *signed orbit sums*
remain a possible sufficient route. They must bound those sums without
substituting W or its equivalent cyclic residual into the premise.

## QCO5. The rank-one trap holds for every linear equivariant selector

Let `V=C^m` describe the coherently transported signal `f=aB` in the actual
clock order, and let `Rf(j)=f(j+1 mod m)`. Let C be any finite-dimensional
complex coefficient space with a permutation action Pi. Suppose a
**complex-linear** coefficient selector `A:V->C` satisfies

```
A R = Pi A.
```

For every Pi-invariant complex-linear functional ell on C, and every f,

```
ell(A f) = (mean f) * ell(A 1).                         (QCO5)
```

In particular the sum of coefficients in each permutation orbit is a known
scalar multiple of W. No assumption that Pi has order m on all of C is
needed: only the displayed intertwining on the image of A is used.

Proof. Averaging the m source shifts gives
`m^-1 sum_(j<m) R^j f = (mean f)*1`. By linearity and intertwining,

```
(mean f)*ell(A1)
 = (1/m)sum_j ell(A R^j f)
 = (1/m)sum_j ell(Pi^j A f)
 = ell(A f).
```

This is an elementary finite Reynolds projection. Complex linearity is
essential for the stated one-complex-dimensional conclusion; a real-linear
selector may also retain the conjugate of W.

If such a selector yields an exact reconstructive phase expansion closed
under the clock action, write `kappa_O=ell_O(A1)` for each coefficient-orbit
sum and `mu_O` for the atom's common clock mean. Reconstruction at f=1 gives
`sum_O kappa_O mu_O=1`. For valid weights `w_O>=|mu_O|` (weight1 for constant
atoms), the canonical orbit triangle certificate therefore has the form

```
sum_O w_O |ell_O(Af)| = K*|W|,
K=sum_O w_O |kappa_O| >=1.                              (QCO5b)
```

Thus not even a complete mixed-quadratic **linear equivariant** analysis
frame avoids this obstruction after invariant orbit compression. In that
case the polynomial labels use Q=hX+P and are transported together with
f=aB; their permutation may use the inverse pullback depending on the
analysis convention. QCO5 requires an actual checked intertwining, not a
semantic claim of naturality.

For a linear selector that is not exactly equivariant, the same averaging
gives the quantitative boundary

```
|ell(Af)-(mean f)ell(A1)|
 <= (1/m)sum_(j<m) |ell((A R^j-Pi^j A)f)|.              (QCO5c)
```

This follows by subtracting the two finite averages and applying the triangle
inequality; no cancellation is assumed. It identifies what a symmetry-breaking
selector must expose. Nonlinear selectors, source-anchored chronology rules,
or separately proved arithmetic coefficient bounds are outside the rank-one
theorem. Their existence or success is not established here.

## Where this connects in SUCC

- [`COHERENT_ZERO_FOUNDATIONS.md`](../../../2026-10-25/COHERENT_ZERO_FOUNDATIONS.md),
  CZR-05/06/08/10: finite cycle obstruction, exact residual minimax,
  cumulative-primitive warning and selected coboundary gate. QCO2 specializes
  that old machinery to the current prime/complement frame; it is not a new
  claim that telescoping alone proves normality.
- [`prime_resonance/THEOREMS.md`](../../signal_frontier/prime_resonance/THEOREMS.md),
  PR3/PR8: the degree-sensitive arithmetic cost. QCO1 changes its coefficient
  accounting by an exact symmetry, not its unresolved source approximation.
- [`complement_budget/hostile/THEOREMS.md`](../../complement_budget/hostile/THEOREMS.md),
  HCB3: arbitrary extensions can move a named resonance. QCO4 audits a fixed
  canonical extension and shows its new quotient has only one source degree
  of freedom, W.
- [`complement_budget/model/THEOREMS.md`](../../complement_budget/model/THEOREMS.md),
  CBM1/2: actual law transport and nonclosure of first moments. QCO1 does not
  approximate `B_(r+1)(h)` by `B_r(h)^16`, and uses no such false closure.
- [`categorical_sheet_transport/PROOFS.md`](../../../2026-11-01/categorical_sheet_transport/PROOFS.md),
  the flat-connection discussion: changing frames is lawful only when the
  observable moves with the connection. Here D_h declares that transport.

Classical context, checked live: Kalinin's [matrix Livsic paper](https://annals.math.princeton.edu/2011/173-2/p11)
uses trivial periodic data and hyperbolic/Hölder hypotheses. The finite prime
cycle computation above imports none of that sufficiency theorem. Marmi,
Moussa and Yoccoz's [cohomological-equation paper](https://www.college-de-france.fr/media/jean-christophe-yoccoz/UPL15307_MMY_roth_JAMS_2005.pdf)
recalls Gottschalk–Hedlund under minimality, compactness and bounded Birkhoff
sums. Golden-return geometry does not supply these missing signed-sum bounds
for the selected BBP observable. These connections are mathematical context,
not assertions of scholarly novelty or transfers across unproved conjugacies.

**Verdict:** QCO1 is a strictly stronger finite *instrument* than atomwise
triangle accounting, with exact source-clock compatibility. QCO4 identifies
a precise circular implementation. No original-zero asymptotic estimate is
proved. Next useful theorem: a source-derived, noncanonical representation
whose signed orbit sums and retained resonance have an all-epoch upper bound.

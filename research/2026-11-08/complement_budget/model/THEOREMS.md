# Folded source laws: the moment hierarchy and polynomial-branch rigidity

**PROVED PAPER for the stated finite objects. Original-zero signed covariance
decay, pi base-16 normality and RH remain OPEN.** The exact polynomial-law
rigidity below is a structural restriction on a prospective model; it is not
an assertion that the actual folded law is an exact polynomial model.

The source is unchanged:

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U0=0, U_n=16 U_(n-1)+r(n).
```

Fix a prime p=1 mod8, m=ord_p(16), L=(p-1)/4, q=L/m, n0=L+1,
I={n0,...,2L}. On this clean interval the authenticated local residues are
x_r=xi*16^r modp, xi=4*16^(n0-(p+7)/8) modp, and
[U_(n0+r+jm)]_p=x_r/p, for 0<=r<m, 0<=j<q. These facts are imported from
PE1--9 / PR1 at the pinned parent95d9860. In particular m divides L.
The clean interval stops before the second p-pole at2L+1.

Put t_n=U_n-[U_n]_p mod1. The actual folded conditional law and moments are

```
nu_r = (1/q) sum_(j=0)^(q-1) delta_(e(t_(n0+r+jm))),
B_r(h) = integral z^h d nu_r(z),       h in Z.
```

The weights are arithmetic averages over the original zero-seed history,
not a seed ensemble. Use chord distance |z-w| on the unit circle and its
1-Wasserstein coupling distance. All cyclic r-indices below are modulo m.

## CBM-1. An authenticated approximate transport of conditional laws

At every interior source step n,n+1 in I,

```
e(t_(n+1)) = e(t_n)^16 * e(r(n+1)).                 (1)
```

Indeed the local principal part at n+1 equals16 times that at n modulo an
integer, and the full source recurrence has its original four poles. The
first omitted step at2L+1 is not covered by (1).

For r<m-1, pair replica j with replica j. For r=m-1, pair replicas j=0,...,q-2
with replicas j+1 at r=0, leaving exactly one unmatched atom on each side.
This gives the proved coupling bound

```
(1/m) sum_r W1(nu_(r+1), (z->z^16)_*nu_r)
 <= 2/L + (2*pi/L) sum_(n=n0)^(2L-1) r(n+1).        (2)
```

The unmatched mass is1/q at one r, and its chord cost is at most2; hence its
average cost is exactly bounded by2/L, not2/q and not zero. Each matched pair
costs |e(r(n+1))-1|<=2*pi*r(n+1). Positivity of the authentic forcing is
proved by its canonical rational formula. This proves (2) by exhibiting the
coupling; no optimal-transport existence theorem is needed.

For every integer h, direct character pairing improves the boundary constant
in the resulting moment bound:

```
(1/m) sum_r |B_(r+1)(h)-B_r(16h)|
 <= eta_h := 2/L + (2*pi*|h|/L) sum_(n=n0)^(2L-1) r(n+1).  (3)
```

At h=0 the left side is zero. For fixed h, the forcing part is O_h(L^-2),
using r(n)<=47/(15n^2). More explicitly it is at most
94*pi*|h|/(15*(L+2)^2). The boundary is O(L^-1).

This transports the **whole conditional law**, not only its first moment.
The character B_r(16h) cannot silently be replaced by B_r(h)^16.
For example, nu=(delta_1+delta_-1)/2 has B(1)=0 but B(16)=1 exactly.
This is an exact finite refutation of first-moment closure.

## CBM-2. Replica variance is the exact price of forgetting the law

For every complex predictor v_r and every integer h, finite expansion gives

```
E_I |e(h*t_n)-v_(n mod clock)|^2
 = E_r(1-|B_r(h)|^2) + E_r|B_r(h)-v_r|^2.           (4)
```

The cross term vanishes because B is the replica mean. Thus a predictor of
raw history and a predictor of the folded signal pay different errors. The
folded model does not owe the first term in (4). For a unit predictor |v_r|=1,

```
E_I |e(h*t_n)-v_r|^2
 = 2-2 Re E_r B_r(h)*conj(v_r)
 <= 2 E_r |B_r(h)-v_r|.                            (5)
```

No source independence appears in either identity.

For any circle probability law, mean z-bar and moment M16,

```
|M16-z-bar^16|
 <= min(2, 16*sqrt(1-|z-bar|^2), 120*(1-|z-bar|^2)). (6)
```

The first bound uses |M16|,|z-bar|<=1. For the second, factor z^16-w^16;
on the closed unit disk it is16-Lipschitz. Apply Cauchy--Schwarz to
E|z-z-bar| and E|z-z-bar|^2=1-|z-bar|^2. For the third, Taylor's formula along
the segment from z-bar to z gives a second-order remainder bounded by
(16*15/2)|z-z-bar|^2; the linear term averages to zero. This proves (6).
Consequently the actual folded first-character field obeys

```
E_r |B_(r+1)(h)-B_r(h)^16|
 <= eta_h + 120 E_r(1-|B_r(h)|^2).                  (7)
```

Low replica variance permits approximate first-moment closure. Learning a
first moment alone does not establish low variance. Equations(4)--(7) are
finite conditional-expectation identities and polynomial estimates, not new
normality criteria.

## CBM-3. Exact positive polynomial laws in the arithmetic budget are linear

Let G=xi<16> be the m-point source coset. Let P_1,...,P_K be **distinct**
polynomials in F_p[X], all of degree at most D, with

```
D>=1,        K*D < m.                              (8)
```

For every x in G take positive weights w_j(x)>0 summing to1, and define

```
mu_x = sum_(j=1)^K w_j(x) delta_(e(P_j(x)/p)).
```

Assume the exact conditional-law identity

```
mu_(16x) = (z->z^16)_*mu_x     for every x in G.     (9)
```

Then there are distinct slopes c_j in F_p such that

```
P_j(X)=c_j X,          w_j(x)=w_j independent of x.  (10)
```

Conversely every law(10) with constant positive weights obeys(9).

**Proof.** Put T(P)(X)=16^-1 P(16X). Positivity of every w_j makes equality
of laws imply equality of their supports. For a fixed i and every x in G,
P_i(16x) must equal16P_j(x) for some j: e(v/p) is injective on F_p.
Thus the polynomial product

```
product_(j=1)^K (T(P_i)-P_j)
```

vanishes at all m source points. Its degree is at most KD<m, so it is the
zero polynomial. F_p[X] is an integral domain; some factor is zero. Hence T
maps the K-element polynomial set into itself. T is invertible, so it permutes
that set.

A permutation orbit has length t<=K. If a coefficient of X^d in P_i is
nonzero, T^t P_i=P_i implies 16^(t*(d-1))=1 modp. At d=0 this would give
m|t, impossible because K<m. For 2<=d<=D it would give m|t(d-1), impossible
because 0<t(d-1)<=K(D-1)<m. Only d=1 remains. This proves the polynomial
part of(10). For distinct slopes and x!=0 the circle atoms e(c_j*x/p) are
distinct. Equation(9) therefore gives w_j(16x)=w_j(x) for every j. The map
x->16x is transitive on G, so the weights are constant. The converse is
immediate. QED.

The theorem also holds separately in any fixed fifteenth-root phase sector:
replace each atom by eta_j*e(P_j(x)/p), where eta_j^15=1. Distinct eta sectors
cannot coincide because p is coprime to15; raising to16 preserves eta.
The same support proof within each sector gives P_j=c_j X and constant
weights there. Coincident (eta,c) labels must first be combined. This allows
source-frame fixed phase offsets without suppressing their signed sum.

**Arithmetic-budget consequence.** The native fold has q=L/m replicas.
For a hypothetical positive law model with at most K=q polynomial branches,
(8) is guaranteed by

```
D <= 4*Lambda(p)^2,
m^2 > p*Lambda(p)^2,     Lambda(p)=2^floor(sqrt(bit_length(p))).
```

Indeed qD/m=(p-1)D/(4m^2)<1. Thus the earlier PR8 degree regime D=o(Lambda)
is inside this rigidity regime whenever the model has at most q branches
and satisfies the **exact** law identity(9). This is a restriction on a lawful
positive branch model, not on arbitrary complex linear combinations of phases.
The latter are the larger PR8 approximation class and need not define a
conditional probability law at all.

For a resulting law with eta sectors, the coherent h-signal is

```
E_x e(h*x/p) integral z^h dmu_x
 = sum_(eta,c) w_(eta,c)*eta^h E_x e(h*(1+c)*x/p).
```

For p not dividing h, the retained resonance is exactly
sum_eta w_(eta,-1)*eta^h. All other slopes have the existing local-character
bound. Lawful transport permits c=-1; it does not bound its weight. This is
the coherent conjugate graph, which the theorem correctly preserves.

## CBM-4. A precision-qualified stability bound and its limitation

Use the same polynomial hypotheses(8), but assume only that at least one
P_j is not homogeneous linear. For this paragraph restrict to the p-grid
sector eta=1, and suppose every w_j(x)>=w_min>0. Define

```
Delta_TV = E_x TV(mu_(16x),(z->z^16)_*mu_x),
TV = (1/2) sum over atoms |mass difference|.
```

Then

```
Delta_TV >= w_min*(1-KD/m).                        (11)
```

Otherwise the finite family were closed under T and CBM-3's coefficient
argument would force every branch homogeneous linear. Therefore some i has
T(P_i) unequal to every P_j as polynomials. Each difference has at most D
roots; at no more than KD source points can the transported atom of P_i
match any target atom. At all other points the next-law atom has mass at least w_min outside
the pushed current support. This proves(11).

Any two distinct p-grid circle points have chord distance at least
2 sin(pi/p)>=4/p. Thus the same reasoning, excluding the single fold boundary,
gives

```
(1/m) sum_(r=0)^(m-2) W1(mu_(x_(r+1)),pow16_*mu_(x_r))
 >= (4*w_min/p)*(1-(KD+1)/m).                      (12)
```

A negative right side is harmless. If mu approximates the actual folded law
with e_mod=E_r W1(mu_(x_r),nu_r), triangle inequalities and the16-Lipschitz
pushforward give the **necessary** lower bound

```
e_mod >= (1/17) [ (4*w_min/p)*(1-(KD+1)/m)
                 - (2*pi/L) sum_(n=n0)^(2L-1) r(n+1) ]_+.  (13)
```

Only the interior transitions are used, so the2/L wrap term is absent. The
17 consists of one error at the next law plus16 times the current error.
This is a genuine precision obstruction for original-source conditional-law
models, proved without typicality. Its scale is O(w_min/p), which tends to
zero. It does **not** rule out the o(1) folded first-moment error requested by
PR8, and does not promote the exact rigidity theorem into an asymptotic one.

## CBM-5. A macroscopic obstruction for bounded nonlinear positive laws

This improves CBM-4 for **genuinely nonlinear** branches. Constant offsets of
linear branches are deliberately excluded from the hypothesis here: offsets
of size1/p can have arbitrarily small transport defect.

Keep(8), assume every w_j(x)>=w_min>0 and at least one P_j has degree>=2.
This theorem additionally allows arbitrary fixed unit phase anchors kappa_j:

```
mu_x = sum_j w_j(x) delta_(kappa_j*e(P_j(x)/p)),  |kappa_j|=1.
```

They may be chosen from the observed history, but are constant over the
source coset and share its declared phase frame. Define

```
delta=min(1,D*sqrt(p)/m),
H_N=sum_(k=1)^N 1/k,
d_grid=1/p+delta*H_((p-1)/2),
a=(1-K*d_grid-1/m)_+.
```

Then every such law has the interior transport defect

```
(1/m) sum_(r=0)^(m-2) W1(mu_(x_(r+1)),pow16_*mu_(x_r))
 >= (w_min/K)*a^2.                                 (14)
```

Consequently its error as a model of the authentic folded conditional law is

```
e_mod >= (1/17) [ (w_min/K)*a^2
                 - (2*pi/L) sum_(n=n0)^(2L-1) r(n+1) ]_+.  (15)
```

**Proof of the nonconstant escape.** Work modulo additive constants in the
polynomial vector space. If T sent every branch class into the finite family
of classes, it would permute that family, whose size is at most K. The same
coefficient-orbit argument as CBM-3 would force every coefficient of degree
>=2 to vanish. Thus some i has T(P_i)-P_j nonconstant for every j. All
Q_j(X)=P_i(16X)-16P_j(X) are nonconstant of degree at most D<m.

**Uniform local polynomial estimate.** For every nonzero k modp, PR3 gives
|E_(x in G)e(kQ_j(x)/p)|<=delta. This is the same declared Weil import:
set s=(p-1)/m, lift x=xi*t^s, and apply the additive bound to the nonconstant
polynomial kQ_j(xi*t^s), of degree d*s<p. Removing t=0 gives at most
d*sqrt(p)/m<=delta unless the trivial cap1 is smaller. The prime-field
hypotheses of [Kowalski, Theorem3.2, printed page31](https://people.math.ethz.ch/~kowalski/exponential-sums-elementary.pdf) were
rechecked in this round; degree d*s lies in1,...,p-1 and hence is coprime to p.
This is a proved finite-field theorem, not an assumption of classical RH.

**Finite arc discrepancy.** For a circular arc A, its p-grid indicator has
normalized DFT coefficients c_k. Its zero coefficient is at most |A|+1/p.
For1<=|k|<p/2, the geometric-series formula gives
|c_k|<=1/(p|sin(pi*k/p)|)<=1/(2|k|). Fourier inversion and the preceding
uniform character bound therefore give

```
Pr(e(Q_j(x)/p) in A) <= |A|+1/p+delta*H_((p-1)/2).
```

For0<r<=2, the condition |e(t)-1|<r implies ||t||<r/4, since
2 sin(pi*||t||)>=4||t||. It is contained in an arc of length r/2.
For nontrivial anchors the ratio is
(kappa_i/kappa_j^16)*e(Q_j(x)/p); its near-collision condition is a rotated
arc of the same length. The finite DFT estimate is uniform in arc origin, so
nothing changes. A union bound over j proves that the next-law atom corresponding to P_i is
at chord distance at least r from every pushed atom on a proportion at least
1-K(r/2+d_grid) of the clock points. Removing the single cyclic boundary
costs at most1/m in that proportion. At each surviving point, every coupling
must transport the atom's mass, at least w_min, across distance at least r.
The mean interior transport cost is therefore at least

```
w_min*r * [1-K*(r/2+d_grid)-1/m]_+.
```

For the sharper bound, let Y(x) be the nearest such chord distance, set to0
at the omitted boundary. For a finite list of nonnegative numbers the exact
identity E Y=integral_0^2 Pr(Y>=r) dr follows by integrating each interval
[0,Y(x)] and summing. The tail estimate above yields

```
E Y >= integral_0^(2*a/K) (a-K*r/2) dr = a^2/K.
```

The endpoint2a/K is at most2. Since every coupling pays at least w_min*Y(x),
this proves(14). Equation(15) follows
from the same17-Lipschitz comparison with actual interior source transport
used in(13). QED.

For fixed K, w_min bounded below, and D*sqrt(p)*log(p)/m->0, (15) gives

```
liminf e_mod >= w_min/(17*K)
```

(with a lower limit for w_min if it varies). In particular fixed D is allowed
on PR1's stronger clocks. For equal weights and K fixed, the floor is
1/(17*K^2). No assumption of exact model transport is made here: this is an
obstruction to approximating the **actual original folded conditional law**
by a bounded number of low-degree nonlinear positive branches.

For every fixed integer h!=0, apply the same argument to the actual law
nu_r^(h)=(z->z^h)_*nu_r. Its interior forcing factor is e(h*r(n+1)), so
(13) and(15) remain valid after multiplying their forcing cost by |h|.
The fixed-h asymptotic floors are unchanged. If its linear branch model is
written directly as e(c*x/p), the coherent local h-character resonates at
c=-h (rather than c=-1 for a law whose h-th moment is taken afterwards).

This does **not** prove a positive lower bound on PR8's first-moment error
rho=E|B-V|: very different conditional laws can have the same first moment.
It also does not exclude affine graph mixtures, complex signed mixtures,
growing K, or a degree regime for which the displayed discrepancy cost fails
to vanish. The surviving original-source task is to estimate the affine
resonance and/or a less restrictive first-moment model with its true error.

## Hostile receipts and source boundaries

1. Single conjugate graph P=-X, weight1: exact lawful transport and full
   signed signal1. Lawfulness alone cannot prove zero-seed cancellation.
2. For any d>=2, the complete T-orbit of P=X^d with equal weights gives a
   positive nonlinear law satisfying(9). Its orbit has length
   m/gcd(m,d-1); it violates KD<m. The small branch/degree condition is real.
3. The two-atom law (delta_1+delta_-1)/2 refutes first-moment closure.
4. The eight-atom multiset consisting of all third roots and all fifth roots,
   uniformly weighted, has first moment0 and is fixed by z->z^16 (the atom1
   occurs twice). Hence no all-q argument can infer nonzero first moment
   merely from finite support and exact transport. This is an auxiliary
   conditional-law countermodel, not an authenticated BBP trajectory.
5. Actual source laws obey(2)--(3), not(9). Deleting the forcing or wrap term
   before applying CBM-3 is invalid. Numerical source runs below retain both.
6. An irrational coherent seed is a legitimate real same-forcing hostile
   orbit, but not a rational source with canonical principal parts. The
   exact synthetic conjugate graph above makes the algebraic failure clear
   without assigning rational genealogies to an irrational state.

## Dependency and novelty scope

Source clock: `signal_frontier/prime_resonance/THEOREMS.md` PR1 and the earlier
PE source proof. Canonical forcing: `observational_succ/duck_bbp.py`; finite
histories use the independently expanded four-pole common-denominator builder
and are cross-checked against the canonical API and direct modular sums.
Conditional-expectation decompositions, root bounds and finite polynomial
algebra are classical; complete elementary proofs are supplied here. The
specific source-fold transport constants, model-class rigidity and quantified
precision obstruction are new within the inspected dossier. No external
priority, Lean certification or all-epoch original-zero decay is claimed.

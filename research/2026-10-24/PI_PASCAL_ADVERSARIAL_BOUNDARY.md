# Pascal valuations, positive moments, and the real carry boundary

**Date:** 2026-10-24. **Lane:** independent adversarial construction.
**Parent:** draft #270 at `3acd547ff122368d5694efdab029b3156a292d8a`.
**Contract:** [Pascal / prime geometry](PI_PASCAL_HOLE_CONTRACT.md).
**Authority:** explicit paper proofs and scoped exact rational checks.
No pi-normality proof, Lean authority, or academic-priority claim is made.

## 1. Verdict and scope

The entire proposed valuation profile

$$
v_2(\Delta^k F(t))=k-1+v_2(k!),\qquad
t\in\mathbb Z_2,\quad k\ge1,
$$

does not by itself force any real central-branch loss. This remains true
when a changed source has all of the following properties simultaneously:

- an exact zero initial state;
- a bijective analytic dyadic source interpolation;
- the same full valuation profile for its forcing;
- rational values at every nonnegative integer source time;
- a strictly positive, completely monotone real forcing of order n^(-2);
- a positive real moment kernel with an analytic density;
- the same contracting particular-solution identity.

An explicit construction below preserves these properties while every late
real pair lies in the central branch. The literal carries are always 15.
Moreover, all normalized Pascal differences can match any reference of the
same profile to an arbitrarily prescribed **fixed finite dyadic precision**,
uniformly in the difference order and the dyadic argument.

The construction changes the fixed BBP four-pole rational function. Its
forcing is rational-valued at integers, but no finite rational-function
formula is supplied. Thus it does not refute the authenticated BBP source or
the conjunction of all its exact defining properties. The fixed rational
formula, its particular moment kernel, and the actual real carry alignment
remain substantive inputs that a successful argument must use.

Normalized Pascal averaging of observables has a separate obstruction: it
preserves every invariant law. Adding phases before applying an exponential
is a different operation, with different frequencies and carry requirements.

## 2. A universal Newton class with the whole valuation profile

Use the forward difference

$$
\Delta f(t)=f(t+1)-f(t),
$$

and the falling factorial

$$
t^{\underline n}=t(t-1)\cdots(t-n+1).
$$

Let the coefficients be rational numbers satisfying

$$
v_2(a_n)=n-1\qquad(n\ge1),
$$

and define

$$
H(t)=\sum_{n=1}^{\infty}a_n t^{\underline n}.
$$

### Theorem PAB-1: uniform full-profile theorem

The series is one analytic function on the open dyadic disc of radius 2.
It fixes zero, is a bijective isometry of the dyadic integers, and satisfies

$$
\boxed{v_2(\Delta^k H(t))=k-1+v_2(k!)}
$$

for every t in the dyadic integers and every k at least 1. The forcing

$$
s(t)=H(t)-16H(t-1)
$$

has exactly the same full valuation profile and is also a bijective isometry.

**Proof.** For every real radius 1<R<2, the Gauss norm of the n-th term is
at most 2(R/2)^n. The series therefore converges on each such closed disc.
Its difference quotient on the dyadic integers is a_1 plus an even integral
quantity, hence a unit. It preserves valuations of differences and induces
a permutation on every finite dyadic quotient; compatible inverses give
bijectivity.

The elementary falling-factorial identity is

$$
\Delta^k t^{\underline n}
=\frac{n!}{(n-k)!}\,t^{\underline{n-k}}\quad(n\ge k),
$$

with zero for n<k. It follows by induction from
Delta(t falling n)=n(t falling n-1). Uniform convergence permits applying the
finite difference termwise.

In Delta^k H, the n=k term is a_k k!, with valuation k-1+v_2(k!). For
n=k+j, j at least 1, the excess valuation over that leading term is at least

$$
j+v_2\binom{k+j}{k}\ge1,
$$

because t falling j is dyadically integral. Thus the leading term cannot
cancel. This proves the stated identity uniformly in t and k.

For s, the two terms in

$$
\Delta^k s(t)=\Delta^k H(t)-16\Delta^k H(t-1)
$$

have valuations differing by exactly four. The first again cannot cancel.
The same difference-quotient argument proves the isometry for s. QED.

The exact contracting particular-solution identity is also retained:

$$
\sum_{j=0}^{J}16^j s(t-j)
=H(t)-16^{J+1}H(t-J-1)\longrightarrow H(t)
$$

uniformly on the dyadic integers. H maps that compact set into itself, so
the displayed remainder tends to zero. In particular the particular
solution's initial value is exactly zero.

## 3. A positive, completely monotone clustering source

The previous theorem leaves the real values of the rational coefficients
largely unconstrained. The following construction uses that freedom without
changing any valuation in PAB-1.

### Lemma: rational dyadic congruence classes are real-dense

For every integer e, rationals with exact dyadic valuation e are dense in
the real line. More generally any fixed dyadic congruence class containing
rationals is real-dense.

For e at least zero, take increasing odd denominators D and choose a
numerator in the class 2^e modulo 2^(e+1), nearest to the desired real value
times D. The approximation error is at most 2^e/D. Scaling handles other
valuations and congruence classes. This is a direct rational construction,
not an assertion that the real and dyadic metrics are interchangeable.

### Theorem PAB-2: full-profile positive-moment countermodel

There exists a source s with all properties in Section 1 whose
zero-initial-state real trajectory is

$$
H(n)=16^n-\eta_n,\qquad
\eta_n=\int_0^1 x^n(1-x)w(x)\,dx,
$$

where w is real analytic, strictly positive on [0,1], and

$$
\frac32<w(x)<\frac52,\qquad
\eta_0=1.
$$

All eta_n and all source values s(n), n at least 1, are rational. The real
fractional states satisfy

$$
y_n=1-\eta_n\quad(n\ge1),
$$

and tend to zero on the circle. They are not normal.

### Construction of the moment density

Let L_n(x) be the monic polynomial of degree n orthogonal to all lower
degrees for the weight 1-x on [0,1]. These polynomials have rational
coefficients: the Gram system uses the rational moments

$$
\int_0^1 x^j(1-x)\,dx=\frac1{(j+1)(j+2)}.
$$

Its positive definite Gram matrix is invertible. Also

$$
\beta_n:=\int_0^1x^n(1-x)L_n(x)\,dx
=\int_0^1(1-x)L_n(x)^2\,dx>0,
$$

because x^n-L_n has lower degree. Each beta_n is rational.

Construct rational numbers lambda_n inductively and set

$$
w(x)=2+\sum_{n=1}^{\infty}\lambda_n L_n(x).
$$

Choose a rational B_n bounding the modulus of L_n on the complex disc
|x| at most n; the coefficient bound
sum_j |[x^j]L_n| n^j suffices. Require

$$
|\lambda_n|B_n<2^{-n-1}.
$$

The series converges uniformly on every complex compact set, so w may in
fact be chosen entire. On [0,1] its deviation from 2 is less than 1/2.
Orthogonality to constants keeps its weighted mass equal to 1.

### Inductive choice paying the dyadic constraints

At stage n, later additions to w leave all moments of orders less than n
unchanged. The n-th addition changes eta_n by exactly lambda_n beta_n.
If the already chosen Newton coefficients are a_1 through a_(n-1), the
new coefficient is forced to be

$$
a_n=
\frac{16^n-\eta_n-
\sum_{j<n}a_j n^{\underline j}}{n!}.
$$

Before the choice of lambda_n, all terms in this affine relation are
rational. Its slope in lambda_n is the nonzero rational number -beta_n/n!.
The real-density lemma therefore allows an arbitrarily small rational
lambda_n for which v_2(a_n)=n-1. In particular it can meet the prescribed
bound |lambda_n| B_n<2^(-n-1).

This completes the induction. Later moment changes preserve earlier
moments exactly, so every final eta_n is the rational value fixed at its
own finite stage. At a nonnegative integer n the Newton series terminates,
giving exactly H(n)=16^n-eta_n. At n=0, eta_0=1 gives H(0)=0.

### Positivity, complete monotonicity, and quadratic decay

The density bounds imply

$$
\frac{3}{2(n+1)(n+2)}<\eta_n
<\frac{5}{2(n+1)(n+2)}.
$$

The source recurrence has, for every n at least 1,

$$
s(n)=H(n)-16H(n-1)
=16\eta_{n-1}-\eta_n
=\int_0^1 x^{n-1}(16-x)(1-x)w(x)\,dx.
$$

It is strictly positive, and

$$
\frac{45}{2n(n+1)}<s(n)<\frac{40}{n(n+1)}.
$$

All discrete differences have the completely monotone sign:

$$
(-1)^k\Delta^k s(n)
=\int_0^1 x^{n-1}(16-x)(1-x)^{k+1}w(x)\,dx>0.
$$

The same moment formula defines a completely monotone real analytic
extension s_R(t) for t>0. Differentiation inserts powers of log(x), whose
alternating signs give (-1)^k s_R^(k)(t)>0.

The real moment extension and the dyadic Newton extension agree at every
positive integer through their common rational source values. This does
not assert that one Newton power series converges in both completions, or
that the source has a fixed finite rational-function formula.

The real Green tail is also explicit: telescoping gives

$$
\sum_{j=1}^{\infty}16^{-j}s(n+j)=\eta_n.
$$

Its initial value is eta_0=1. The constant represented by this changed
base-16 source is therefore 16, not pi. This is a declared changed-source
countermodel, with no claim to preserve the authenticated BBP constant.

### Complete central-branch retention

For n at least 1, 0<eta_n<1. Hence the cumulative carry is exactly

$$
C_n=16^n-1,
$$

and its literal local carry C_n-16C_(n-1) is always 15, including the first
step. On windows whose indices are comparable to a large parameter p,
all real pair distances are O(p^(-2)). They are therefore close at every
prescribed radius down to p^(-2/5), and their current differences lie
inside the central 1/32 branch.

Every pair has centered carry zero. In the notation of the inherited
collision contract,

$$
Z_W(\tau_j)=Q_{W^+}(\tau_j)=|W|^2,
\qquad \theta_j=1.
$$

For any fixed C, the proposed half-retention inequality with allowance
C|W| fails once |W|>2C. The whole valuation profile and the perfect dyadic
residue refinement coexist with this failure. QED.

## 4. Matching all normalized differences at fixed finite precision

### Theorem PAB-3: uniform finite-precision strengthening

Let a reference function have Newton coefficients a_n^* with
v_2(a_n^*)=n-1. Fix an arbitrary integer L at least 1. The positive-moment
construction can additionally require

$$
a_n-a_n^*\in2^{n-1+L}\mathbb Z_2
$$

at every n. It then satisfies, for every t in the dyadic integers and k
at least 1,

$$
v_2\bigl(\Delta^k(H-F^*)(t)\bigr)
\ge k-1+v_2(k!)+L.
$$

The corresponding forcings also have this normalized-difference agreement.

**Proof.** Replace the valuation annulus in the induction by the indicated
congruence coset. Its rational members are still real-dense, so arbitrarily
small moment perturbations remain possible. The leading valuation is
unchanged. In the k-th difference of H-F^*, its n=k+j term has valuation
at least k-1+v_2(k!)+L+j. This proves the bound uniformly. Subtracting
16 times a shifted copy preserves the bound for the forcings. QED.

Thus an entire table of normalized Pascal differences to any fixed finite
dyadic precision can be retained by a completely clustering source. This
does not preserve exact values at infinite precision. Nor does it preserve
the fixed BBP rational formula. These distinctions are indispensable.

## 5. A separate finite-rational control

A much simpler countermodel keeps a finite rational forcing formula but
does not keep its real positivity and quadratic decay. Let

$$
H_0(t)=\frac{t}{2t+1}
=\frac12-\frac1{2(2t+1)},
\qquad s_0(t)=H_0(t)-16H_0(t-1).
$$

Its poles lie outside the dyadic integers. The reciprocal-difference identity

$$
\Delta^k\frac1{at+b}
=\frac{(-1)^k a^k k!}
{\prod_{j=0}^{k}(a(t+j)+b)}
$$

shows that H_0 and s_0 have the entire same valuation profile. The identity
follows by a one-step subtraction and induction. H_0 fixes zero and is a
dyadic isometry. Yet its real source values approach 1/2, so its real
collision retention tends to complete clustering.

The exact scope failure is visible immediately:

$$
s_0(1)=\frac13,\qquad s_0(2)=-\frac{74}{15},\qquad
s_0(n)\longrightarrow-\frac{15}{2}.
$$

Accordingly, finite rationality plus the full dyadic profile is insufficient,
and positive complete monotonicity plus the full profile is also insufficient.
The preceding controls do not refute their full conjunction with the exact
four-pole BBP source. No finite-rational, positive-quadratically-decaying
countermodel satisfying all those additional source requirements is claimed.

## 6. Normalized Pascal averaging preserves existing invariant laws

Let T be a measurable map and define the normalized Pascal observable
operator

$$
A_m f(x)=2^{-m}\sum_{j=0}^{m}\binom mj f(T^j x).
$$

For every T-invariant probability law mu,

$$
\int A_m f\,d\mu=\int f\,d\mu.
$$

This follows by invariance term by term and the row sum 2^m. Every invariant
non-Haar law survives unchanged. The row weights do not supply independently
chosen carrier digits.

There is also an endpoint-only statement for any bounded source sequence,
without assuming an autonomous recurrence. Let z_n=f(y_n), and average
over N successive n. Shifting the window by j changes its mean by at most
2j||f||_infinity/N. The binomial distribution has mean m/2, so

$$
\left|\frac1N\sum_{n=A}^{A+N-1}2^{-m}
\sum_{j=0}^m\binom mj z_{n+j}
-\frac1N\sum_{n=A}^{A+N-1}z_n\right|
\le\frac{m\|f\|_\infty}{N}.
$$

Therefore m=o(N) leaves the same limiting empirical laws. Larger m incurs
an actual extension of the observed time window; it does not automatically
justify an invariant-law conclusion or selected-source cancellation.

For the positive-moment countermodel, eta_n decreases and

$$
|e(H(n))-1|\le2\pi\eta_n,
\qquad e(x)=\exp(2\pi i x).
$$

It follows uniformly for **every** m at least zero that

$$
\left|2^{-m}\sum_{j=0}^m\binom mj e(H(n+j))-1\right|
\le2\pi\eta_n.
$$

Every Pascal row remains coherent on this source.

## 7. Adding phases is a different operation

For an unforced circle orbit x_j=16^j x modulo one, adding phases with
integer Pascal coefficients gives

$$
e\left(\sum_{j=0}^m\binom mj x_j\right)=e(17^m x).
$$

Alternating Pascal coefficients give e(15^m x). These operations change
the Fourier frequency. They are not the preceding convex average of the
observables e(x_j).

Dividing the phase sum by 2^m before exponentiating further requires a
choice of real lift: changing one circle representative by an integer
can change the resulting root. The source lift or an explicit inverse-cover
label must therefore remain in the definition.

For the actual unwrapped recurrence, let E shift the integer time index.
Polynomial division by E-16 gives the exact identity

$$
(I+E)^m U_n
=17^m U_n+
\sum_{\ell=0}^{m-1}17^\ell
(I+E)^{m-1-\ell}r(n+1).
$$

If the positive forcing is decreasing, its remainder is between zero and

$$
r(n+1)\frac{17^m-2^m}{15}.
$$

After normalization by 2^m this cost is at most
r(n+1)((17/2)^m-1)/15. The coefficient growth must be retained when m grows.
This identity supplies no selected-source frequency cancellation.

The positive-moment countermodel gives an even sharper signed control:

$$
\Delta^k H(n)=15^k16^n-\Delta^k\eta_n,
\qquad
|\Delta^k\eta_n|
=\int_0^1x^n(1-x)^{k+1}w(x)\,dx\le\eta_n.
$$

Consequently

$$
|e(\Delta^k H(n))-1|\le2\pi\eta_n
$$

uniformly in k. Its signed Pascal phase products remain coherent even
though the entire dyadic difference-valuation profile is exact. For
normalized unsigned phase addition, the leading term
16^n17^m/2^m is integral whenever m<=4n, and the remaining normalized
moment sum has magnitude at most eta_n. This operation is therefore coherent
through that entire order range as well, with its lift explicitly retained.

## 8. Rational height is a real additional constraint

The congruence construction pays for its freedom with unrestricted odd
denominators. This exposes a precise hypothesis that it does not preserve.
Suppose rational x=a/b and y=c/d have odd positive reduced denominators
b,d at most Q, and v_2(x-y) is at least L. Then either x=y or

$$
|x-y|\ge\frac{2^L}{bd}\ge\frac{2^L}{Q^2}.
$$

Indeed, the nonzero integer ad-bc is divisible by 2^L. Thus a simultaneous
real upper bound smaller than 2^L/Q^2 would force exact equality. This is a
valid, height-dependent connection between the two observations, whereas
an unrestricted comparison of real and dyadic norms is false.

The authentic four-pole forcing has explicit polynomial denominator height.
For example, a common odd denominator for Delta^k r(n) is the product of
the four-factor source denominators at n through n+k, bounded by

$$
[8(n+k)]^{4(k+1)}\qquad(n\ge1).
$$

This is a transparent sufficient bound, not an optimal height estimate.
The accumulated source U_n instead combines denominators from its entire
past. No uniform real collision-frequency estimate follows from the
height-uniqueness lemma alone. It identifies an actual structural restriction
absent from the interpolation countermodel; it does not discharge the
selected-source statistical obligation.

## 9. Finite calibration and remaining source-specific task

An exact rational scratch oracle executed the following bounded checks:

- 680 full-profile checks for H_0 and s_0 at integer starts 0 through 16
  and orders 1 through 20;
- a rational positive-density moment construction through depth 8;
- 64 difference-profile checks on that constructed prefix;
- positivity of the finite moment differences, exact initial mass one,
  the certified density perturbation bound below one-half, and literal
  carries equal to 15 on all eight constructed steps.

These are finite calibration of the formulas. PAB-1 through PAB-3 are
supported by the displayed uniform series arguments and recursive existence
proofs, not by extrapolation from those checks. No repository-wide or hosted
test result is claimed by this lane.

The real arithmetic question remains the contract's fixed-source question:
what does the **specific four-pole rational function**, beyond the valuation
profile and positivity of a moment kernel, force about the conditional
centered carry on real-close pairs? A useful next claim must either use an
exact BBP coefficient/kernel feature that these controls change, or explicitly
retain a new bound on the actual conditional carry alignment. Reweighting
an orbit by Pascal rows and renaming the remaining collision count are not
such bounds.

| Claim | State | Exact scope |
|---|---|---|
| Whole valuation profile forces real half retention | REFUTED | Explicit changed-source analytic countermodel |
| Adding positivity and complete monotonicity repairs that inference | REFUTED | Positive analytic moment-density construction |
| Any fixed finite normalized-jet precision repairs it | REFUTED | Uniform congruence-strengthened construction |
| Normalized Pascal averaging forces Haar statistics | REFUTED | Every existing non-Haar invariant law is preserved |
| Finite rationality alone repairs the profile argument | REFUTED | H_0(t)=t/(2t+1), with its failed real hypotheses disclosed |
| Exact four-pole BBP source has real central loss | OPEN | No source-specific asymptotic bound supplied here |
| Pi normality | OPEN | No actual-source counterexample or proof claimed |

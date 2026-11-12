# Time-calibrated BBP boundary filters and a paid finite Gram certificate

Status: **PROVED LOCAL / instrument theorem**, with the algebraic antecedents
explicit below. These paper proofs are not formal-kernel verification, external
review, or an asymptotic signed estimate. The literal four-pole source and zero
seed are retained. R0, R1, pi normality, Goldbach and RH remain OPEN.

## 1. Object, source, and the exact transport

For integers n >= 0 retain

```
r(n) = 4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)   (n >= 1),
U_0 = 0,   U_(n+1) = 16 U_n + r(n+1),
T_n = sum_(j>=1) 16^(-j) r(n+j),
Y_n = U_n + T_n = 16^n pi/16.
```

The last identification imports the classical BBP identity. The algebra below
also holds for every other initial seed; it cannot by itself select the zero
seed statistically. On the circle, write `F_n(u)=16u+r(n+1)` and
`C_n(u)=u+T_n`, reducing modulo one after these expressions. Then

```
C_(n+1) o F_n = T o C_n,       T(u)=16u mod 1,                 (FT-01)
```

because `r(n+1)+T_(n+1)=16T_n`. This conjugacy is **REUSE**, not a new
cancellation theorem; its two-time form is IAD-03 and IAD-05 in
[innovation arithmetic decoupling](../../2026-11-11/innovation_arithmetic_decoupling/THEOREMS.md).

For clarity the full operator transport follows. On Haar `L2(T)`, let
`R_a f(u)=f(u+a)`, `K f(u)=f(16u)`, `K_n f=f o F_n`, and let
`L=K*`, `L_n=K_n*` be the **uniform-preimage** transfer operators. Then

```
K_n = R_(T_n) K R_(-T_(n+1)),
L_n = R_(T_(n+1)) L R_(-T_n),
L_n K_n = I,
K_n L_n = Q,     Q f(u)=(1/16) sum_(a=0)^15 f(u+a/16).         (FT-02)
```

Proof: substitute (FT-01), take adjoints, and use `LK=I`, `KL=Q`.
Translations commute with Q, so the latter is exactly independent of n and
of the BBP forcing. A multiplication mask at time n transforms by
`R_(-T_n) M_f R_(T_n)=M_(f(.-T_n))`. Thus chronological compositions
with masks telescope in their correctly indexed frames; omitting an
intermediate frame changes the operation. The transfer L_n is a mathematical
average over 16 preimages, **not the deterministically selected predecessor**.

This makes a concrete filter distinction: ordering retains information when
its masks retain information, but the uniform-preimage cancellation is not
an arithmetic estimate for the selected path. No operator-norm continuity
`||R_epsilon-I|| -> 0` is asserted on all L2: arbitrarily high Fourier modes
refute it. The quantitative result therefore declares a regularity budget.

## 2. Finite source-tail calibration

For integers `n,d >= 0`, set

```
t_(n,d) = sum_(j=1)^d 16^(-j) r(n+j),
epsilon_(n,d) = 16^(-d) r(n+d+1)/15.
```

Monotonicity and positivity of the original source give the strict enclosure

```
0 < T_n - t_(n,d) < epsilon_(n,d).                            (FT-03)
```

The canonical implementation is `duck_bbp.tail_interval`; no replacement
source is introduced. For `n >= 1`, the source moment bound also gives

```
epsilon_(n,d) <= 16^(-d)/((8(n+d)+1)(8(n+d)+2))
                  < 16^(-d)/(64 n^2).                        (FT-04)
```

These bounds are inherited from IAD-03(b). Their use to price an arbitrary
finite chronological filter packet is the instrument contribution here.

There are two distinct exact finite-frame identities:

```
16 t_(n,d) - t_(n+1,d) - r(n+1)
    = -16^(-d) r(n+d+1),                                     (FT-05)

16 t_(n,d) - t_(n+1,d-1) - r(n+1) = 0       (d >= 1).          (FT-06)
```

Both follow by aligning the finite sums. Fixed depth has a nonzero seam;
a common terminal horizon, whose remaining depth decreases at each step,
has no finite seam. In fact if `H >= n`, then
`U_n+t_(n,H-n)=16^n P_H`, where `P_H=sum_(j=1)^H16^(-j)r(j)`.
This finite source identity already appears in `duck_bbp.partial_transport_residual`.
It does not turn the truncated completed point P_H into the true pi point.

## 3. The paid chronological-filter theorem

Fix a finite chronological list of nonnegative offsets
`0 <= k_1 < ... < k_m`. A complex-valued function Phi on `T^m` has
coordinate Lipschitz budgets `ell_1,...,ell_m >= 0` if changing only
coordinate j changes Phi by at most `ell_j` times the circle geodesic
distance. The budgets are hypotheses; discontinuous digit/carry masks
need separate branch guards or a proved modulus and are not included.

For each n, use the actual raw source state at each requested time, with its
own correction:

```
z_hat_(n,j) = {U_(n+k_j) + t_(n+k_j,d_j)},
z_(n,j)     = {Y_(n+k_j)}.
```

Then, for every choice of the finite depths d_j,

```
|Phi(z_hat_(n,.)) - Phi(z_(n,.))|
    <= sum_j ell_j epsilon_(n+k_j,d_j).                       (FT-07)
```

Proof: replace coordinates one at a time. Each circle distance is bounded
by the corresponding real-tail enclosure (FT-03); sum the individual
Lipschitz bounds. The same estimate averages under any nonnegative weights
of total mass one. No statistical assumption is used.

For an explicit finite Fourier packet

```
Phi(u_1,...,u_m) = sum_(h in H) c_h e(sum_j h_j u_j),
e(t)=exp(2*pi*i*t),   h_j integers,
B(Phi)=sum_h |c_h| sum_j |h_j|,
```

one may take `ell_j=2*pi*sum_h |c_h| |h_j|`. Therefore for `n>=B>=1`
and every d_j >= d,

```
|Phi(z_hat)-Phi(z)| < (pi/32) 16^(-d) B(Phi)/B^2.              (FT-08)
```

For a target absolute tolerance eta > 0, a sufficient integer depth is

```
d >= max(0, ceil(log_16(pi B(Phi)/(32 eta B^2))))              (FT-09)
```

when `B(Phi)>0`; a constant packet has zero error. The bound charges
coefficient size and total per-coordinate frequency, not just the number
of masks. For m bounded-frequency factors `prod_j e(h_j u_j)`,
`B(Phi)=sum_j |h_j|`, so the needed additional tail depth grows only
logarithmically with m at fixed B and eta. High-frequency masks can make
the budget much larger. Depth d counts tail terms, not bit complexity.

**What is paid.** Every raw state U_(n+k_j) must be available exactly, or
with its own certified error alpha_(n,j), in which case add
`sum_j ell_j alpha_(n,j)` to (FT-07). Merely propagating a single rounded
initial state does not supply these individual bounds. Rational numerator
and denominator growth, branch masks, arithmetic work, and observation
access remain distinct costs. The theorem avoids a loose exponential
error bound by recalibrating actual observations; it does not abolish
expansion or grant an unprovided measurement.

## 4. Frozen calibration has a different precision cost

For `n>=1`, if one approximates only Y_n by `U_n+t_(n,d)` and generates all later
completed predictions by multiplication by 16, then at offset k the real
error is exactly

```
16^k (T_n-t_(n,d)).                                          (FT-10)
```

For a character of frequency h the sufficient error bound is
`min(2, 2*pi*|h|16^k epsilon_(n,d))`. At largest offset L this requires,
using (FT-04), the sufficient depth

```
d >= max(0, L + ceil(log_16(pi |h|/(32 eta n^2))))             (FT-11)
```

for tolerance eta > 0. This is a sufficient worst-case precision price,
not a necessary lower bound for a particular phase (integer aliases can
reduce circle error). Exponential amplification is sharp as a uniform
local statement: for an initial perturbation a/(16^L) with 0<a<1/2,
the time-L circle discrepancy is a while the initial discrepancy is
`a/16^L`.

The root distinction is operational. Reusing one approximate corrected
state costs linear additional depth in L; separately calibrated actual
readings cost the sum of their local frequency budgets. Exact common-
horizon rational calculations (FT-06) preserve correlations but still pay
the final common tail. Treating independent enclosure endpoints as a
single coherent tail can invalidate a claimed cancellation.

## 5. A finite chronological Gram certificate

Let n range over a finite set with weights `w_n>=0`, `sum w_n=1`, and use
m offsets as above. Write

```
v_(n,j)=e(Y_(n+k_j)),
G_jk=sum_n w_n conjugate(v_(n,j)) v_(n,k).
```

This Hermitian Gram matrix is positive semidefinite and has diagonal 1.
For consecutive offsets `k_j=j`, it is exactly

```
G_jk = sum_n w_n e((16^k-16^j)Y_n).                           (FT-12)
```

The collapsed-frequency identity is **REUSE** of the joint-character
observation in the November 7 Fourier--Yoneda pinbed, Theorems section 10.
Its large collapsed frequency does not force use of one poorly calibrated
initial phase: the individual readings in section 3 give an alternative
finite error route.

Form G_hat using the calibrated unit-modulus readings, and put

```
eta_j=2*pi*sum_n w_n epsilon_(n+k_j,d_j).
```

By telescoping the product of two unit-modulus characters,

```
|(G-G_hat)_jk| <= eta_j+eta_k,
||G-G_hat||_op <= 2 sqrt(m) ||eta||_2.                        (FT-13)
```

For the norm statement, entrywise absolute values are dominated by the
symmetric nonnegative matrix `eta 1^T + 1 eta^T`, whose norm is at most
`2||eta||_2||1||_2`; apply the bound to absolute values of test vectors.
If every coordinate error is <= epsilon, the price is at most
`4*pi*m*epsilon`. One may improve it using the exact zero diagonal.

To obtain an entirely rational finite certificate, enclose each complex
entry by independently justified rational real/imaginary intervals and
choose a Hermitian rational midpoint A. If a symmetric nonnegative
rational error matrix E bounds the entrywise absolute errors from G to A,
then `delta=max_j sum_k E_jk` bounds the operator error. A rational LDL*
certificate `A-beta I >= 0`, with beta > delta, proves

```
lambda_min(G) >= beta-delta > 0.                            (FT-14)
```

For complex rational matrices use Gaussian-rational Hermitian LDL*;
strictly positive pivots certify positive definiteness. Zero pivots need
a separate semidefinite verifier. Exact diagonal 1, conjugate symmetry,
and analytic trigonometric enclosure errors must be retained. A floating
minimum eigenvalue is not this certificate.

## 6. What Gram stability would and would not buy

A finite positive certificate demonstrates linear independence of this
finite observed family under this finite law. It is neither a finite
invariant closure certificate nor a theorem about every future shell.

There is a stronger reason to separate positivity from its margin. For any
irrational completed point xi, the points `z_n=e(16^n xi)` at distinct
integer times are distinct: equality would make
`(16^n-16^l)xi` an integer. Suppose all sample weights are strictly positive
and there are q distinct sampled times. For offsets k_j, a null vector of
G would give the polynomial

```
p(z)=sum_j a_j z^(16^(k_j))
```

zero at every z_n. After dividing by `z^(16^(k_1))`, a nonzero polynomial
has degree at most `D=16^(k_m)-16^(k_1)` and at most D distinct roots.
Therefore

```
q > D  implies G is positive definite.                       (FT-16)
```

For consecutive offsets 0,...,m-1 this holds as soon as
`q >= 16^(m-1)`. Applied to pi it imports only irrationality, which is
already part of the source identity contract. The threshold is sufficient,
not claimed optimal. It gives no useful uniform lower eigenvalue. Hence
qualitative full rank of all sufficiently long finite windows cannot be
marketed as new evidence for normality: it is automatic for every
irrational completed point, including nonnormal ones.

There is a conditional connection to the weaker signed rung R1. Take
consecutive offsets `j=0,...,m-1`, uniform shell weights on `[B,2B)`,
and write `W_B=B^(-1)sum_(n=B)^(2B-1)e(Y_n)`.
Set `a=m^(-1)sum_j mean_n v_(n,j)`. Endpoint cancellation gives
`|a-W_B| <= (m-1)/B`. Cauchy--Schwarz and `trace G=m` give

```
|a|^2 <= (1/m^2) 1*G1 <= lambda_max(G)/m
       <= 1-((m-1)/m)lambda_min(G).
```

Consequently

```
|W_B| <= sqrt(1-((m-1)/m)lambda_min(G)) + (m-1)/B.             (FT-15)
```

For any fixed m>=2, a source-derived uniform lower bound
`lambda_min(G_B)>=gamma>0` on all sufficiently large integer B would
imply R1 (hence R0). **That uniform lower bound is OPEN for the authentic
source.** Equation (FT-15) is a finite Cauchy--Schwarz/trace consequence,
not a new source estimate. It is not asserted equivalent to R1.


The full Gram-gap hypothesis actually implies the stronger existing rung
(CH) directly. For consecutive offsets and any m>=2, the unit vector
`c=(-1,1,0,...,0)/sqrt(2)` satisfies exactly

```
c* G_B c = 1-Re W_B(15) >= lambda_min(G_B).                   (FT-17)
```

Thus a uniform lower Gram margin gamma forces
`limsup_B Re W_B(15) <= 1-gamma`; no endpoint payment is needed for this
direction. FT-15 supplies a useful finite first-mode bound, but proposing
a full Gram gap does not lower the existing arithmetic target below (CH).
Indeed the gap condition is strictly stronger at the invariant-law level:
the uniform law on the 15-point `times16` orbit of `1/225` has
`W(15)=e(1/15)` and hence a strict (CH) saving, while
`e(T^j u)=e(u)e(j/15)` on its support makes every Gram of depth m>=2
rank one. This is an exact countermodel to the converse, not a claim
about the authentic zero-seeded pi orbit.

Even excellent Gram conditioning at every finite depth does not imply
normality. For the `times16`-invariant circle law

```
mu = c delta_0 + (1-c)lambda,       0<c<1,
```

at all consecutive depths the exact Gram is
`G=(1-c)I+c11*`, since the frequencies `16^j` are distinct. It satisfies
`lambda_min=1-c` whenever m>=2, but `integral e(u)dmu=c != 0`.
This is a precise law-level counterexample; it is not represented as the
original zero-seeded pi orbit. The coherent same-forcing seed `-pi/16`
has G=11*, rank one, at every depth and shell, and therefore fails every
strict positive-margin certificate for m>=2.

## 7. Claim boundaries and next falsifier

- FT-01/02: exact algebra/classical Koopman transport, with source-tail
  conjugacy reused; inverse-preimage averaging is not selected-history access.
- FT-03/06: inherited exact source bounds and finite sum identities.
- FT-07/11: paid chronological calibration and comparison of two observation
  protocols; all constants and regularity/access hypotheses are displayed.
- FT-12/14: finite Gram transport and rational-certification interface;
  requires actual entry enclosures and a verified matrix certificate.
- FT-15: conditional weaker-rung bridge with a displayed endpoint payment;
  its source-specific uniform premise remains open.
- FT-16: elementary polynomial-root argument; eventual finite full rank
  follows from irrationality alone and does not supply a uniform margin.
- FT-17: the full Gram gap implies the existing directional (CH) target;
  the 15-cycle law refutes the converse, so no easier rung is claimed.

The cheapest falsifiers are an omitted frame in FT-05/06, high-frequency
masks under an unbudgeted smoothness claim, a rounded-state propagation
presented as exact source readings, an invalid rational Gram certificate,
or the mixture law above presented as normal. The next arithmetic lamp is
an independently source-derived lower Gram bound on all late shells for
some fixed m, with the coherent seed and source-mutant controls retained.

No novelty priority is claimed. The elementary calibration and matrix
estimates expose the price of a boundary instrument; they do not pay the
signed arithmetic inequality by restating it.

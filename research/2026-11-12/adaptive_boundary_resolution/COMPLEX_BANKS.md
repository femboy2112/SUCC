# Fixed complex banks cannot evade the averaged arithmetic obstruction

**2026-11-12. Status: PROVED LOCAL, using an explicitly imported classical
Selberg–Delange mean theorem.** Base inspected:
`5d9917031855f806fd5c1f9d8b4543ad3ca24bbf`. This note extends the
[fixed real-bank obstruction](../holographic_boundary_filters/FIXED_RESOLUTION.md)
to every fixed finite conjugation-paired bank with nodes in the punctured
closed unit disk. It does not establish a pointwise Goldbach estimate.

## 1. Hole contract and verdict

Let distinct, nonzero complex nodes and their nonzero coefficients be fixed:

\[
0<|z_j|\le1,\qquad
q(h)=\sum_{j=1}^m b_jz_j^h\in\mathbb R\quad(h\in\mathbb Z_{\ge0}).
\]

Assume conjugation pairing, including real coefficients at real nodes,
and the all-grade minorant conditions

\[
q(0)=1,\qquad q(h)\le0\quad\text{for every integer }h\ge1. \tag{CB0}
\]

Zero coefficients can be removed before applying the theorem. Define

\[
F_n(z)=\sum_{a=0}^{n-2}z^{\Omega(n+a)+\Omega(n-a)-2},\qquad
B_q(n)=\sum_jb_jF_n(z_j),\qquad n\ge2, \tag{CB1}
\]

where Ω counts prime factors with multiplicity. Both endpoints in every
summand are at least two. Thus all exponents are nonnegative, and CB0
makes B_q(n) a lower bound for the unordered prime-pair count at 2n,
with the prime diagonal included.

**The conjecture is true throughout the stated disk, including |z|=1.**
Put R=max_j|z_j|. The bank necessarily contains the positive real node R,
its coefficient b_R is strictly negative, and

\[
\boxed{
\sum_{2\le n\le X}B_q(n)
\sim b_RK_RX^2(\log X)^{2R-2}<0,
\qquad
K_R=C_R^2\left[\frac14+\left(\frac1R-\frac12\right)^2\right]>0,
} \tag{CB2}
\]

where

\[
C_R=\frac1{\Gamma(R)}
\prod_p\frac{(1-1/p)^R}{1-R/p}. \tag{CB3}
\]

The inequality means eventual negativity of the cumulative sum, not of
every midpoint. The source-specific conclusion uses a classical one-variable
mean and a new-to-this-dossier application of elementary convolution bounds.
It does not assume Goldbach or a pointwise additive correlation formula.
There is no worldwide novelty claim for the underlying harmonic or
Selberg–Delange arguments.

| Contract item | Resolution |
|---|---|
| Quantifiers | One finite bank is fixed before X tends to infinity. |
| Original obstruction | The real proof ordered positive damping nodes. Complex nodes could have shared radii and oscillating phases. |
| Weakest sufficient arithmetic step | Other nodes are little-o of the positive R-node response; a full complex convolution asymptotic is unnecessary. |
| Dependency closed | The prior fixed-bank no-go now covers arbitrary fixed phase twists in the punctured closed unit disk. |
| Cheapest falsifier | A genuine all-grade minorant without a negative positive-real outer node, or a violation of the complex triangle bound below. |
| Finite boundary | Exact controls check identities and designed mutants; no finite test certifies CB0 for an arbitrary bank. |
| Remaining lamp | An adaptive bank with a proved parameter-uniform source estimate, or a different authenticated observable. |

## 2. CB01: the outermost circle must contain a negative real mode

This part is independent of arithmetic and even of the bound R≤1.
For any nontrivial finite bank of nonzero distinct nodes, eventual
nonpositivity of q(h) already implies the stated sign conclusion.

Write

\[
\frac{q(h)}{R^h}=T(h)+r(h),\qquad
T(h)=\sum_{|z_j|=R}b_j(z_j/R)^h.
\]

Conjugation pairing makes T and r real. The lower-radius remainder
r(h) tends to zero exponentially. Hence q(h)≤0 implies
T_+(h):=max(T(h),0)≤|r(h)| for all sufficiently large h, and therefore

\[
\frac1N\sum_{h=1}^NT_+(h)\longrightarrow0. \tag{CB4}
\]

Set b_R=0 provisionally if the positive real node is absent. For a unit
complex number u≠1, its geometric-sum average N⁻¹∑_{h=1}^Nu^h tends to
zero. Distinct nodes on the outer circle therefore give the exact
Cesàro limits

\[
\frac1N\sum_{h=1}^NT(h)\longrightarrow b_R,
\qquad
\frac1N\sum_{h=1}^N|T(h)|^2\longrightarrow
S:=\sum_{|z_j|=R}|b_j|^2>0. \tag{CB5}
\]

Let L=∑_{|z_j|=R}|b_j|>0. Pointwise,

\[
|T(h)|^2\le L|T(h)|=L\{-T(h)+2T_+(h)\}.
\]

Averaging and using CB4–CB5 proves the quantitative necessity

\[
\boxed{b_R\le-\frac{\sum_{|z_j|=R}|b_j|^2}
{\sum_{|z_j|=R}|b_j|}<0.} \tag{CB6}
\]

In particular, the convention b_R=0 is impossible: R is an actual
positive real node. This proof handles root-of-unity phases and irrational
phases alike. It uses neither a presumed phase period nor a claim that
a nonnegative function must have a pointwise limit.

The coefficient lemma is a classical finite-frequency phenomenon. It
is the sign version of the familiar positive-real singularity restriction
for generating functions with nonnegative coefficients; the proof above
does not require importing that theorem.

## 3. Classical complex mean: exact import and hypothesis audit

For each fixed complex z with |z|<2, the required classical statement is

\[
A_z(x):=\sum_{m\le x}z^{\Omega(m)}
=C_zx(\log x)^{z-1}
+O_z\bigl(x(\log x)^{\operatorname{Re}z-2}\bigr),
\quad
C_z=\frac1{\Gamma(z)}\prod_p\frac{(1-1/p)^z}{1-z/p}. \tag{CB7}
\]

Here (log x)^{z-1}=exp((z−1)log log x), using real logarithms of
positive quantities. The normalized Euler factors differ from one by
O_z(p⁻²). No complex asymptotic equivalence is asserted when C_z=0:
at z=−1, for example, the reciprocal gamma factor vanishes. The upper
bound used below remains valid there.

Two primary research papers were inspected:

- Francesco Cellarosi, *Smooth Sums over Smooth k-Free Numbers and
  Statistical Mechanics*, [arXiv:1304.6610v2](https://arxiv.org/pdf/1304.6610v2),
  PDF page 5, equations (10)–(11), explicitly records CB7 for |z|<2.
  Its surrounding theorem about smoothed k-free sums is a different
  result and is not the theorem imported here.
- Régis de la Bretèche and Gérald Tenenbaum, *Remarks on the
  Selberg–Delange method*, Acta Arith. 200.4 (2021), 349–369,
  [author manuscript](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf),
  Theorem 1.2 and equations (1.10)–(1.12), PDF page 3, give a sufficient
  complex-valued formulation. Their Theorem 2.1 assumes nonnegativity
  and cannot be substituted for this step.

For the latter formulation on our disk, set f(m)=z^{Ω(m)}, ρ=z,
r=|z|, σ=3/4, and A=4. The prime residual f(p)−ρ is identically
zero. The prime reciprocal bound in its class F(r,σ) is the usual
Mertens bound multiplied by r, while its prime-power requirement follows
from

\[
\sum_p\left\{\frac{r^2}{p^{3/2}}+
\sum_{\nu\ge2}\frac{r^\nu}{p^{3\nu/4}}\right\}<\infty.
\]

Theorem 1.2 consequently gives a finite expansion through j=3 with
remainder O_z(x(log₃x)^β/(log x)^{5-r}). Since r≤1 and
Re z≥−r, that remainder is O_z(x(log x)^{Re z−2}); the j≥1 terms
fit the same bound. Formula (1.10) gives the leading coefficient CB7.
This checks the required domain without borrowing a nonnegative theorem
for complex values. Both references belong to the same classical source
family; they are not independent arithmetic evidence.

For the proof it is enough to retain the weaker consequence

\[
|A_z(x)|\ll_z x(\log x)^{a-1},\qquad
a=\operatorname{Re}z,\quad0<|z|\le1. \tag{CB8}
\]

All constants here and below may depend on the fixed nonzero node.

## 4. CB02: a complex triangle bound without positive measures

Put r=|z| and w_z(m)=z^{Ω(m)−1} for m≥2, and zero otherwise.
Then |w_z(m)|=r^{Ω(m)−1}≤1. Define even and odd prefixes W_{z,e},
W_{z,o}. Complete multiplicativity at 2 gives exact identities

\[
W_{z,e}(x)=A_z(x/2),\qquad
W_{z,o}(x)=\frac{A_z(x)}z-A_z(x/2)-\frac1z. \tag{CB9}
\]

The subtraction removes m=1. CB8 yields, for either parity,

\[
|W_{z,*}(x)|\ll_z x(\log x)^{a-1},\qquad
\sum_{2\le m\le Y}|w_z(m)|=\frac{A_r(Y)-1}{r}
\ll_z Y(\log Y)^{r-1}. \tag{CB10}
\]

Consider the ordered, same-parity triangle

\[
T_z(Y)=\sum_{\substack{u,v\ge2\\u+v\le Y\\u\equiv v\pmod2}}
w_z(u)w_z(v)
=\sum_{u=2}^{Y-2}w_z(u)W_{z,u\bmod2}(Y-u). \tag{CB11}
\]

Take integer Y and split at Y−u=√Y. On the interior Y−u≥√Y,
the logarithms of Y−u and Y are comparable. CB10 bounds this part by

\[
\ll_z Y(\log Y)^{a-1}\sum_{u\le Y}|w_z(u)|
\ll_z Y^2(\log Y)^{a+r-2}.
\]

On the remaining endpoint strip, the pointwise bounds |w_z(u)|≤1
and |W_{z,*}(v)|≤v give a total at most
∑_{v≤√Y}v=O(Y). As a+r≥0, this strip is smaller than the preceding
bound for large Y. Thus

\[
\boxed{T_z(Y)\ll_z Y^2(\log Y)^{\operatorname{Re}z+|z|-2}.} \tag{CB12}
\]

This is an absolute-value estimate for the complex sum, not an asserted
asymptotic with a complex leading constant. It uses cancellation in one
prefix and pays absolute mass in the other variable.

The ordered-to-unordered conversion is algebraic and remains exact:

\[
\sum_{2\le n\le X}F_n(z)
=\frac12\{T_z(2X)+D_z(X)\},\qquad
D_z(X)=\sum_{2\le m\le X}w_z(m)^2. \tag{CB13}
\]

There is no conjugation in D_z. Its modulus is at most X, so CB12 yields

\[
\boxed{
\left|\sum_{2\le n\le X}F_n(z)\right|
\ll_z X^2(\log X)^{\operatorname{Re}z+|z|-2}.
} \tag{CB14}
\]

**Why the old positive-measure proof is insufficient here.** Normalizing
complex weights by Y(log Y)^{z−1} makes their total variation comparable
to (log Y)^{|z|−Re z}, which grows for non-positive-real phases.
Convergence of interval masses alone therefore does not justify passing
to an indicator of a triangle as it did for nonnegative measures. CB11–CB12
provide the missing control directly. No such passage is used.

## 5. CB03: dominance and eventual cumulative negativity

For the positive real node R, positivity is available. CB7 and CB9 give
the prefix constants

\[
k_{R,e}=C_R/2,\qquad
k_{R,o}=C_R(1/R-1/2).
\]

The nonnegative triangular-sum lemma proved in the prior
[fixed-resolution note](../holographic_boundary_filters/FIXED_RESOLUTION.md)
therefore applies: a nonnegative prefix asymptotic
V(x)∼kx(log x)^β gives ordered triangle mass
∼(k²/2)Y²(log Y)^{2β}. It follows by positive measure convergence or
finite rectangle squeezes. Applying it separately to the two parities,
then applying CB13, gives

\[
\sum_{2\le n\le X}F_n(R)
\sim(k_{R,e}^2+k_{R,o}^2)X^2(\log X)^{2R-2}.
\]

This is CB2's constant. For R=1 the same endpoint is also checked
directly: F_n(1)=n−1, the sum is X(X−1)/2, C_1=1, and K_1=1/2.

Every different node satisfies the strict inequality

\[
\operatorname{Re}z_j+|z_j|<2R. \tag{CB15}
\]

Indeed Re z_j≤|z_j|≤R; equality in both requires z_j=R.
The bank is finite and fixed, so its non-dominant nodes have a positive
minimum exponent gap

\[
\eta=\min_{z_j\ne R}\{2R-\operatorname{Re}z_j-|z_j|\}>0.
\]

CB14 shows their entire contribution is
O_q(X²(log X)^{2R−2−η}), which is lower order than the positive R-node
mean. Combining this with CB6 proves CB2. The case of no other nodes
cannot satisfy q(0)=1 and b_R<0.

For each fixed 0<α<1, subtraction at αX gives the stronger shell result

\[
\sum_{\alpha X<n\le X}B_q(n)
\sim b_RK_R(1-\alpha^2)X^2(\log X)^{2R-2}<0. \tag{CB16}
\]

Thus every sufficiently large multiplicative shell contains a negative
certificate response. There is no universal numerical threshold asserted.

## 6. Exact controls and finite-prefix traps

The tests use Q(i), with rational real and imaginary parts. This is an
exact control subfamily, not a restriction of the theorem's complex domain.
Floats, Booleans, strings and Python floating complex values are rejected.

### A genuine phase-twisted minorant with an early positive cumulative prefix

Take

\[
q(h)=\bigl(2\,2^{-h}-1\bigr)
\bigl(2-\cos(\pi h/2)\bigr). \tag{CB17}
\]

The first factor is one at h=0, zero at h=1, and negative thereafter;
the second lies between one and three and equals one at zero. Thus
CB0 holds for every integer grade. Its six nodes and coefficients are

| Node | Coefficient |
|---|---:|
| 1 | −2 |
| 1/2 | 4 |
| i, −i | 1/2 each |
| i/2, −i/2 | −1 each |

The exact cumulative arithmetic responses at X=2,3,4,5,6 are

\[
1,\quad2,\quad3/2,\quad1/2,\quad-3/2.
\]

This is an algebraically designed calibration with directly computed
source counts, not a blind holdout or an asymptotic fit. It demonstrates
that a positive initial cumulative response does not survive indefinitely.

### A phase-only impostor that can pass any prescribed finite grade prefix

For any integer L≥2 and ζ=exp(2πi/L), put

\[
q_L(h)=\frac1{L-1}\sum_{k=1}^{L-1}\zeta^{kh}
=\begin{cases}1,&L\mid h,\\-1/(L-1),&L\nmid h.\end{cases} \tag{CB18}
\]

It has q_L(0)=1 and passes every minorant check at grades 1,...,L−1,
yet fails at grade L. Its nodes omit the positive real unit node.
This is not a counterexample to CB01: its all-grade hypothesis fails.
The executable case L=4 uses exact nodes i,−1,−i and detects the first
failure at four. Arbitrarily long finite acceptance windows are therefore
insufficient unless an analytic all-grade certificate is also supplied.

### A true bank can exactly match every target in a finite arithmetic prefix

Fix any cutoff X. The grades at all n≤X obey
h≤L_X=floor(log₂(X²))−2. Choose an even d>L_X and fixed 0<t≤1/2.
The prior damped product Q_{d,t}(t^h) equals one at h=0, vanishes for
1≤h<d, and is nonpositive at all remaining integer grades. Multiplication
by 2−cos(πh/2) preserves these properties and produces a fixed finite
complex bank with nonzero nodes t^r and ±it^r.

Consequently this single chosen bank equals the exact prime-pair count
at every n≤X, while CB2 says its cumulative response eventually becomes
negative after the cutoff is allowed to grow without changing the bank.
The tests instantiate X=16,d=8,t=1/2 and compare against independent
trial-division prime tests. This is a finite interpolation result, not
Goldbach and not a contradiction with adaptive resolution.

## 7. Scope, reproduction, and claim ledger

The theorem excludes fixed finite phase twists. It leaves outside its
quantifiers banks whose degree, coefficients or nodes depend on n or X,
infinite banks, other authenticated observables, and minorants required
only on a justified source-specific support set. There is no parameter
uniformity as nodes merge, approach zero, or rotate toward R. In
particular η can tend to zero, and the proof supplies no adaptive theorem
by exchanging those limits.

A node at zero is deliberately excluded. With 0⁰ interpreted as one,
q(h)=0^h is already the exact zero-grade projector and does not obey
this obstruction. Supplying its response would supply the target itself.
Allowing it is a changed access model, not a phase escape.

Run from this directory:

~~~sh
python -m unittest -v test_complex_banks.py
python complex_banks.py
~~~

**Observed run:** all 16 tests passed. Checks include independent
trial-division versus sieve values of Ω through 512; exact source
triangle versus direct midpoint sums at five nodes and five cutoffs;
parity, endpoint and diagonal controls; and the phase/calibration
examples above. No numerical asymptotic fitting is used. The all-grade
and asymptotic claims rest on the proofs and imported theorem, not these
finite tests.

| Claim | Status and dependency |
|---|---|
| CB01, negative positive-real outer mode | PROVED LOCAL by finite geometric means and a square bound. |
| CB7–CB8, complex multiplicative mean | CLASSICAL IMPORT, hypotheses checked above. |
| CB02, complex triangle upper bound | PROVED LOCAL from CB8, positive absolute mass and an endpoint split. |
| CB03, fixed complex-bank negative cumulative response | PROVED LOCAL conditional only on the stated classical import and CB0. |
| Designed exact controls | OBSERVED in the stated finite ranges; their elementary formulas are separately proved. |
| Pointwise positive response for adaptive banks | OPEN; not inferred from this result. |

The boundary-translation agent derived the Cesàro and endpoint arguments
before sending its result to the root constructor. The root subsequently
reported having independently reached the same arguments. That is
separately executed, same-model triangulation with shared classical
provenance, not an external referee or formal proof. No sibling's new
files or conclusions were used in this derivation.

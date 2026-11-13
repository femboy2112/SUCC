# R0 inverse architecture and the sharp finite-loss branch threshold

**Working proof dossier, 2026-11-13.** Main XXV source base:
`db9fb4b84672050efa79b13377f1e73364598a14`. This file concerns the unchanged
four-pole source and its original zero seed. The new quantitative theorem
below improves the constant in an inherited logarithmic absolute-loss
bound. It does not prove R0, normality, or a restricted exponent below one.
The author and the other reviewing agents share a model family.

## Preregistered finite checks

This paragraph was written before running the new module or any of its
finite mathematical controls. The proof, not fitted numerical data, fixes
the following checks.

1. Verify the fallback constants `c=3/40`, `lambda=973/50`,
   `u=1/2000`, and `R=15/4096` with exact rational arithmetic. Reject the
   certificate if its strict margin is nonpositive. These constants were
   selected from algebra before execution.
2. Verify the one-defect inverse Gram formula for all left/right lengths
   from 0 through 8, including both boundary cases. Check exact rational
   minimizers against the constraint and total energy. Deliberately omit
   the backward tail to retain the smaller two-coordinate `1/257` control.
3. Verify one rational specialization of the all-threshold lemma:
   `c=3/40`, `lambda=973/50`, `K=1`, `epsilon=1/512`, and
   `T=7*2**20-1`. All comparisons involving square roots are to be reduced
   to sufficient rational comparisons, not evaluated with floating point.
4. Fresh finite original-source shells are `B in {17,43,89,179,359}`.
   They will receive rigorous rational bounds for the actual completed
   first-mode real loss, and nearest-integer carry data, from authenticated
   BBP tails. They are finite calibration, not all-scale evidence.
5. Hostile controls are completed values `0`, `1/16`, `1/15`; the coherent
   changed seed `s=-pi/16`; Shallit/Kempner shells
   `B in {64,128,256,512}`; and the inherited proper-null/nonproper-positive
   source distinction. The rational values are exact. The infinite sparse
   series is enclosed by a proved tail bound. The local cosine coefficient
   is deliberately tested at `q=1/2`, where its global extension is false.
6. Retain every failed candidate and its exact failed comparison in
   `r0_results.json`. No numerical asymptotic fitting is authorized by
   these checks. No external-peer-review claim follows from another agent.
7. Before executing the source mutation, test the additional candidate
   that the inherited proper null source, divided by 8, has
   `v_2(U_n)=v_2(n)` for `1<=n<=64`, and is an isometry on those indices.
   Its coefficient vector is `(8,-8,-4,-8,-2,-2,1,0)/8`. A failure is to
   be retained as a failed control-strengthening conjecture. A finite pass
   would require a separate all-index derivation before any theorem claim.
8. After the preceding candidate failed at `n=2`, an algebraic replacement
   was derived before testing: `A(t)=t/((8t+1)(8t+3)(8t+5))`,
   `U_t=-A(t)`. Check all pairs of distinct integers in `[-37,37]`, the
   source recurrence and its polynomial integral for `1<=n<=64`, and
   positivity of the forcing for `2<=n<=64`. The proof will retain the
   negative first forcing and nonproper degree-12 source explicitly.

## RI-01: every constant below the boundary-excursion ceiling

Write `e(y)=exp(2*pi*i*y)` and

\[
F(q)=1-\cos(2\pi q),\qquad
\kappa_*=F(1/16)=1-\cos(\pi/8).
\]

### Exact finite lemma

Let `0<c<kappa_*`. Choose `a` with `0<a<1/16` and `F(a)>c`, and put

\[
\lambda=F(a)/a^2,\qquad
\delta_K=\frac{255}{256^{K+1}-1}.
\]

Choose an integer `K>=0` and `0<epsilon<=1/16` such that

\[
\sqrt{c/\lambda}+\frac{\sqrt{2K+2}}{15}\epsilon
 <\frac1{\sqrt{256+\delta_K}}. \tag{RI-1}
\]

Such choices exist: first let `K` tend to infinity, observing that
`sqrt(c/lambda)<a<1/16`, then choose `epsilon` sufficiently small.
Suppose `T>=max(2K+1,257c/epsilon^2)` and real numbers `q_0,...,q_T`
and `f_0,...,f_{T-1}` satisfy

\[
|q_t|\le1/2,\quad \sum_{t=0}^T F(q_t)\le c,\quad
\max f_t-\min f_t\le\epsilon/2,
\]

and every difference between
`q_{t+1}-16q_t-f_t` is an integer. Then all these residuals are equal.
This is a deterministic finite statement; no distribution assumption is
present.

**Proof.** Monotonicity of `F` on `[0,1/2]` gives `|q_t|<a`.
The function `F(q)/q^2` decreases on `(0,1/2]`, so, writing
`E=sum q_t^2`, we have `lambda E<=c`. Also `8E<=c`.
There is a transition `s` with

\[
q_s^2+q_{s+1}^2\le2E/T,\qquad
|q_{s+1}-16q_s|\le\sqrt{257c/(4T)}\le\epsilon/2.
\]

Subtract its residual from all the others. The recurrence becomes

\[
q_{t+1}=16q_t+b_t+v_t,\qquad b_t\in\mathbb Z,
\qquad |v_t|\le\epsilon,\qquad b_s=0. \tag{RI-2}
\]

If `b_t!=0`, then

\[
16|q_t|\ge1-|q_{t+1}|-|v_t|>1-1/16-1/16=7/8,
\]

so `|q_t|>7/128`. On `|q|<=1/16` we have `F(q)>=19q^2`.
Two nonzero `b_t` would therefore cost more than
`38(7/128)^2>1/10>kappa_*`. There is at most one nonzero `b_t`.

Suppose that unique defect is at transition `j`.
Set `l=min(j,K)` and `r=min(T-j-1,K)`. Since `T>=2K+1`, at
least one of `l,r` equals `K`. Use the consecutive states from
`q_{j-l}` through `q_{j+1+r}`; there are at most `2K+2`.
On this window remove the small forcing by the finite backward tail

\[
w_t=q_t+\sum_{k=t}^{j+r}16^{-(k-t+1)}v_k.
\]

The last sum is empty at the right endpoint. Then
`w_{t+1}-16w_t=b_t` and `|w_t-q_t|<=epsilon/15`.
Writing `x=w_j`, `y=w_{j+1}`, we have `y-16x=b_j`, while all other
transitions in this window have zero integer forcing. Thus

\[
\sum w_t^2=A_l x^2+B_r y^2,
\quad A_l=\sum_{k=0}^l256^{-k},\quad B_r=\sum_{k=0}^r256^k.
\]

Minimizing this quadratic form under its one linear constraint gives

\[
\sum w_t^2\ge\frac{b_j^2}{256/A_l+1/B_r}
\ge\frac1{256+\delta_K}. \tag{RI-3}
\]

For completeness: if `l=K`, then
`256/A_l=255+delta_K` and `1/B_r<=1`; if `r=K`, then
`1/B_r=delta_K` and `256/A_l<=256`. These include a defect at either
endpoint; no unavailable backward or forward observation is charged.
But the triangle inequality in Euclidean space gives

\[
\left(\sum w_t^2\right)^{1/2}
\le\sqrt{c/\lambda}+\sqrt{2K+2}\epsilon/15,
\]

contradicting (RI-1). Hence there is no defect. QED.

The two elementary estimates used here can be verified without a
floating-point oracle. The inherited rational Machin bounds give
`157/50<pi<22/7`; Taylor's inequality then gives

\[
F(q)\ge\left[2(157/50)^2-\frac23(22/7)^4/256\right]q^2
 > (973/50)q^2>19q^2\quad(|q|\le1/16).
\]

Also `kappa_*<=pi^2/128<1/10`. Monotonicity of `F(q)/q^2` follows
from monotonicity of `sin(x)/x` for `0<x<=pi/2`.

### From phases to the inverse seed arc

Suppose `X_{t+1}=16X_t+r_{t+1}`, `h` is a nonzero integer, and

\[
D=(T+1)-\left|\sum_{t=0}^T e(hX_t)\right|\le c.
\]

Choose the direction `e(theta)` of the nonzero resultant and lifts
`y_t=hX_t+ell_t=theta+q_t`, `ell_t in Z`, `|q_t|<=1/2`.
Then `D=sum F(q_t)` and the residual differences are integers, with
`f_t=hr_{t+1}`. Under the finite hypotheses above the integer branches
are constant. The same telescoping identity as the inherited branch
lemma, now using `|q_t|<1/16`, gives some integer `p` with

\[
\left|X_0+\sum_{j=1}^T16^{-j}r_j-\frac p{15|h|}\right|
\le\frac{2+|h||r_T|}{15|h|16^T}. \tag{RI-4}
\]

Indeed, if the common lift branch is `15theta+k` and `f=-k/15`,
then `y_T-f=[16(q_T-q_{T-1})-hr_T]/15`; the first numerator has
absolute value less than 2. The integral initial lift is absorbed in `p`.
This is an inverse consequence for an arbitrary seed, not a selected
arithmetic exclusion yet.

### Application to the original four-pole source

Keep

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n),\quad x=\pi/16.
\]

The inherited exact source bounds are

\[
0<r(n+1)<15/(64n^2),\quad0<T_n<1/(64n^2),\quad
U_n+T_n=16^n x.
\]

Fix the parameters of RI-01. Set `H_c=15/(32epsilon)`.
On the block of states `U_{m+1},...,U_{8m}`, take `T=7m-1` and
`1<=|h|<=m^2/H_c`. Its forcing span is less than `epsilon/2`.
If its modulus loss were at most `c`, the complete zero-selected Green
identity and (RI-4) would imply, with `q=15|h|16^m`,

\[
\left|\pi-\frac pq\right|
\le16^{-8m}\,16\left[\frac2{15|h|}
 +\frac1{64(8m-1)^2}+\frac1{64(8m)^2}\right]
 <3\,16^{-8m}. \tag{RI-5}
\]

The sole classical arithmetic import needed is the published strict
bound `mu(pi)<15/2`: Zeilberger and Zudilin prove
`mu(pi)<=7.103205334137...` in *Moscow Journal of Combinatorics and
Number Theory* **9** (2020), 407–419, DOI
[10.2140/moscow.2020.9.407](https://doi.org/10.2140/moscow.2020.9.407).
The corrected version is
[arXiv:1912.06345v2](https://arxiv.org/abs/1912.06345v2);
the [author page](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html)
and [publisher PDF](https://msp.org/cnt/2020/9-4/moscow-v9-n4-p06-s.pdf)
were freshly checked for the statement. The full irrationality-measure
proof is imported, not reverified here. It yields a constant `C>0` such that
`|pi-p/q|>=C q^(-15/2)` for all integer `p,q`, `q>=1`.
This is a sufficient pinned import, not an assertion of the current
world record. The two bounds contradict one another whenever

\[
C^2 16^m>9(15|h|)^{15}. \tag{RI-6}
\]

Consequently there is an integer `J_c` such that every eligible block
with `m>=8^{J_c}` has loss greater than `c`, uniformly in the displayed
frequency band. Its analytic requirements are explicit:
`7m-1>=max(2K+1,257c/epsilon^2)` and (RI-6).
The numerical arithmetic onset is not extracted because `C` is not.
For example, once `m>=16`, checking
`C^2 16^m>9(15m^2/H_c)^15` at an initial `m` suffices for all larger
real `m`, since the exponential-to-polynomial ratio is then increasing.

Define `S_N^U(h)=sum_{n=1}^N e(hU_n)`. The user's convention with indices
`0,...,N-1` differs by a bounded endpoint term. Partitioning into the
disjoint blocks `(8^j,8^{j+1}]` gives, for every
integer `N>=1` and `h!=0`,

\[
\boxed{|S_N^U(h)|\le N-c\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J_c,\left\lceil\log_{64}(H_c|h|)\right\rceil\right)\right).}
\tag{RI-7}
\]

Increase `J_c` to be nonnegative if necessary. For each fixed nonzero `h`,
this is `|S_N^U(h)|<=N-c log_8 N+O_{c,h}(1)` for **every fixed**
`c<1-cos(pi/8)`. In particular `c=3/40>1/14` is available.
Taking `c` to depend on `N` without controlling the onset is not licensed.
The completed orbit has the same logarithmic statement after a bounded
fixed-frequency tail error, since `sum T_n<infinity`.

### What has improved, and what has not

The inherited proof relaxed a single transition to the squared norm 257.
The additional local recurrence here recovers the cost of its surrounding
geometric tail; its boundary Gram denominator tends to 256. This proves
every constant below the previously exhibited boundary-excursion ceiling.
It is a new refinement relative to the inspected Main XXV branch proof.
Worldwide novelty is unverified; elementary expanding-map coercivity and
quadratic constrained minimization are classical tools.

The ceiling belongs to this arbitrary-seed, constant-branch reduction.
It is not a ceiling on what the original zero-selected source might
satisfy. Nor does the logarithmic bound imply a positive shell-average
loss: dividing it by `N` still tends to zero.

### Block-ratio corollary: the number 8 is not intrinsic

Let `beta>1` and suppose a proved irrationality-measure bound permits
`mu(pi)<rho<beta`. The same argument with
`m_j=floor(beta^j)`, `m=m_j`, and `M=m_{j+1}` gives, for each fixed
`h!=0` and `c<kappa_*`,

\[
|S_N^U(h)|\le N-c\log_\beta N+O_{c,\beta,h}(1). \tag{RI-8}
\]

To check the rounding, the block is `U_{m+1},...,U_M`, with
`T=M-m-1`. We have `M>=beta*m-1`, hence
`T>=(beta-1)m-2`. The forcing span has the same bound as before.
The inverse arc gives `|pi-p/(15|h|16^m)|<3*16^(-M)` once `M>=2`;
indeed its coefficient is at most
`16[2/15+1/64+1/256]<3`. Thus the upper bound is at most
`48*16^(-beta*m)`, while the Diophantine lower bound contradicts it
when

\[
C16^{(\beta-\rho)m}>48(15|h|)^\rho.
\]

This eventually holds uniformly for `|h|<=m^2/H_c`.
Every `j+1<=floor(log_beta N)` gives a complete block inside `[1,N]`;
initial and frequency-dependent omissions contribute only to the
displayed constant. In particular **`beta=15/2` is available from the
same published import**. Any fixed beta greater than the published
upper bound is available by choosing an intermediate rho. The collision
ratio mechanism was already identified in
[the inherited frontier audit, section 2](../../2026-10-27/PI_FRONTIER_AUDIT_STRENGTHENING_2026-10-27.md).
This corollary supplies the rounding and parameterized application; it
is not a separate new irrationality theorem. No unreviewed 2026 claim
that `mu(pi)=2` is used.

### Endpoint-coefficient corollary: a summable schedule pays the parameter debt

**RI-8E, PROVED PAPER.** For every fixed nonzero integer `h` and every
fixed `beta` admitting a proved exponent `mu(pi)<rho<beta`,

\[
\boxed{|S_N^U(h)|\le N-\kappa_*\log_\beta N+O_{\beta,h}(1),
\qquad \kappa_*=1-\cos(\pi/8).} \tag{RI-8E}
\]

In particular `beta=15/2` is available from the published import above.
The completed pi orbit has the same bound after a bounded fixed-frequency
tail correction. This is an endpoint **coefficient in the summed bound**,
not a claim that each individual block has loss at least `kappa_*`.
It gives no R0 saving and no new uniform growing-frequency band.

This extension was derived during the final review after the first
validated checkpoint `f62616067093751850d5fc9b1e252e1a274c00fb`.
It is a paper derivation, not a newly preregistered numerical finding.
Two reviewing agents checked it read-only; they share the model family.
No new executable assertions are inferred from those reviews.

**Proof.** We control the finite lemma's parameters instead of taking
`c` to its endpoint inside an unspecified `O_c(1)`. For an integer
block length `T` sufficiently large, set

\[
K=\lceil\log_{256}T\rceil,\quad
\epsilon=\frac8{\sqrt T},\quad
E=\frac{\epsilon\sqrt{2K+2}}{15},\quad
d=\frac{255}{256^{K+1}-1},
\]
\[
a=\frac1{16}-2E-\frac d{8192},\qquad
c_T=F(a)(1-1/T),\qquad \lambda=F(a)/a^2.
\]

Since `256^K>=T`, we have `0<d<=1/T`. Also
`E=O(sqrt(log(T)/T))`, so eventually `0<a<1/16` and
`0<c_T<F(a)<kappa_*`. The conditions `epsilon<=1/16` and
`T>=2K+1` hold eventually. The remaining size condition simplifies to

\[
T\ge257c_T/\epsilon^2\quad\Longleftrightarrow\quad
64\ge257c_T,
\]

which follows from `c_T<kappa_*<1/10`.

Convexity of `d -> (256+d)^(-1/2)` gives the tangent lower bound

\[
\frac1{\sqrt{256+d}}\ge\frac1{16}-\frac d{8192}.
\]

The inverse-Gram hypothesis is therefore strict:

\[
\sqrt{c_T/\lambda}+E
=a\sqrt{1-1/T}+E
<a+E
=\frac1{16}-E-\frac d{8192}
<\frac1{\sqrt{256+d}}.
\]

Thus the exact finite lemma applies with these changing parameters.
Moreover, `|F'|<=2pi` yields the explicit deficit estimate

\[
0<\kappa_*-c_T
\le4\pi E+\frac{\pi d}{4096}+\frac{\kappa_*}{T}
\le4\pi E+\frac{\kappa_*+\pi/4096}{T}. \tag{RI-8E.1}
\]

Now let `m_j=floor(beta^j)`, `M=m_(j+1)`, and
`T_j=M-m_j-1`. After finitely many initial blocks,
`T_j~(beta-1)beta^j` is positive. For fixed `h`, the span of the
authentic forcing on `U_(m+1),...,U_M` is at most
`15|h|/(64(m+1)^2)=O_h(m^(-2))`. This is eventually below
`epsilon_j/2`, whose order is `m^(-1/2)`.

If that block's modulus loss were at most `c_(T_j)`, the finite lemma
and the same zero-source inverse arc would give

\[
\left|\pi-\frac p{15|h|16^m}\right|<3\,16^{-M}
\le48\,16^{-\beta m}.
\]

The inverse arc uses only `|q_t|<1/16`; its coefficient and denominator
do not depend on the approaching value `c_(T_j)`. Choose `rho` and
its Diophantine constant `C_rho>0` once. The same contradiction

\[
C_\rho16^{(\beta-\rho)m}>48(15|h|)^\rho
\]

therefore holds for all sufficiently late blocks, independently of
their individual thresholds. Every such block loses more than
`c_(T_j)`.

By (RI-8E.1), the deficits are
`O_beta(sqrt(j+1) beta^(-j/2))`, so

\[
\sum_{j\ge J}(\kappa_*-c_{T_j})<\infty.
\]

For `L=floor(log_beta N)`, the complete disjoint blocks
`j=J,...,L-1` lie in the first `N` states. Triangle inequality gives

\[
N-|S_N^U(h)|
\ge\sum_{j=J}^{L-1}c_{T_j}
\ge\kappa_*(L-J)-\sum_{j\ge J}(\kappa_*-c_{T_j}).
\]

The last sum is finite. Replacing `L` by `log_beta N` changes the
right side by a bounded amount. Absorb the finitely many earlier
indices into the constant, proving (RI-8E). QED.

**Hostile endpoint control.** One phase `e(-1/16)` and `T` phases
equal to one have modulus loss

\[
T+1-|T+e(-1/16)|<\kappa_*\qquad(T\ge1),
\]

because the squared modulus is
`(T+cos(pi/8))^2+sin(pi/8)^2`. The loss tends to `kappa_*`.
Consequently a per-block endpoint claim would be false even in this
simple source-free control. The summable-deficit theorem makes no
such claim. Its arithmetic onset is still not numerically extracted,
and its normalized saving still tends to zero.

## RI-02: a linear, exact inverse dictionary for R0 failure

For any real `xi`, use the fixed nearest-integer convention

\[
K_n=\lfloor16^n\xi+1/2\rfloor,\qquad
e_n=16^n\xi-K_n\in[-1/2,1/2),\qquad
a_n=K_{n+1}-16K_n.
\]

These are **balanced carries**, not the inherited literal carries
`floor(U_n)-16floor(U_{n-1})`. They satisfy

\[
e_{n+1}=16e_n-a_n,\qquad a_n\in\{-8,-7,\ldots,8\}.
\]

For `B>=1`, write

\[
A_B=\frac1B\sum_{n=B}^{2B-1}F(e_n),\quad
C_B=\sum_{n=B}^{2B-2}a_n^2,\quad
D_B=\#\{n\in[B,2B-2]:a_n\ne0\}.
\]

**Theorem (all real xi, all B).**

\[
\boxed{\frac8{289}C_B\le BA_B
 \le\frac{2\pi^2}{225}(C_B+64).} \tag{RI-9}
\]

Consequently

\[
\boxed{\frac8{289}\frac{D_B}{B}\le A_B
 \le\frac{128\pi^2}{225}\frac{D_B+1}{B}.} \tag{RI-10}
\]

**Proof.** Put `E=sum_{n=B}^{2B-1}e_n^2`. The difference operator
`a_n=16e_n-e_{n+1}` has Euclidean norm at most 17, including finite
endpoints, so `C_B<=289E`. Also `F(e)>=8e^2`.
For the upper estimate, extend the vector of forcing by its last entry
`a'_{2B-1}=16e_{2B-1}`. Then

\[
e_n=\sum_{j=n}^{2B-1}16^{-(j-n+1)}a'_j.
\]

The sum of this inverse kernel is at most `1/15`. Its finite convolution
therefore has Euclidean norm at most `1/15`: this follows directly by
weighted Cauchy–Schwarz and summing, or by the triangle inequality for
the shifted vectors. Thus
`225E<=C_B+256e_{2B-1}^2<=C_B+64`. Apply
`F(e)<=2pi^2e^2`. Finally `D_B<=C_B<=64D_B`. QED.

The endpoint term is necessary. A small positive state followed by
successive multiplication by 16 can have every internal balanced carry
zero while its phase loss is positive. The exact Shallit controls below
have this feature on each tested shell.

In particular,

\[
\mathrm{R0}\ \Longleftrightarrow\
\liminf_{B\to\infty}D_B/B>0,
\]

and R0 fails exactly when some `B_j->infinity` has `D_{B_j}=o(B_j)`.
This is a quantitatively sharper inverse dictionary, not an estimate
of the source-selected carries. The `17` and `15` constants are the
forward and inverse norms of the expanding recurrence, not independent
evidence for randomness.

### A dense collection of long, two-sided quiet components

Assume R0 fails and choose a sequence of shells as above. Removing the
`D_B` nonzero carry transitions partitions the `B` states into at most
`D_B+1` components. On a component `[s,t]`,

\[
K_n=16^{n-s}K_s,\qquad e_n=16^{n-s}e_s,
\qquad |e_n|\le\tfrac12 16^{-(t-n)}. \tag{RI-11}
\]

For any integer `L>=1`, at most `2L(D_B+1)` states are within `L`
positions of one of their component endpoints. At every remaining
state,

\[
16^L\mid K_n,\qquad |e_n|\le\tfrac12 16^{-L}. \tag{RI-12}
\]

Choose, for example,
`L_B=max(1,floor(sqrt(B/(D_B+1))))`. Along the failure sequence,
`L_B->infinity` and the removed proportion tends to zero. Thus R0
failure requires simultaneous deep real coherence and high radix
divisibility of the rounded prefixes on a set of shell density tending
to one. It need not produce a run with length proportional to B.

For the authentic source, (RI-12) becomes

\[
U_n=16^{L_B}z_n-T_n+\epsilon_n,
\quad z_n\in\mathbb Z,
\quad |\epsilon_n|\le\tfrac12 16^{-L_B},
\]

on that same dense set. The tails remain the **actual** four-pole tails.
Unless `L_B` dominates `log B`, this does not even say that
`|epsilon_n|<T_n`. R0 failure supplies no such rate. For example, the
inherited sparse digit-one construction with gaps of order `sqrt(n)`
has `v_16=0` and fails R0: failure does not imply a restricted exponent
at least one. Shallit/Kempner is a different control with macroscopic
quiet runs; these two controls must not be conflated.

### Cleared denominators and the exact Gamma-weighted sparse forcing

Put

\[
P(n)=120n^2-89n+16,\quad
Q(n)=(2n-1)(4n-1)(8n-7)(8n-3),\quad
\Delta_n=\prod_{j=1}^n Q(j),\quad A_n=\Delta_nU_n.
\]

Here `Delta_0=1`, all `Delta_n` are odd, and `A_n` is an integer.
This product is an authenticated common denominator; it is not asserted
to be the reduced denominator. Its Gamma expression is

\[
\Delta_n=512^n\prod_{\alpha\in\{1/2,3/4,1/8,5/8\}}
\frac{\Gamma(n+\alpha)}{\Gamma(\alpha)}. \tag{RI-13}
\]

This is just the classical recurrence
[`Gamma(z+1)=z Gamma(z)`, DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1)
applied to each of the four linear factors.

For `Z_n=A_n-Delta_n K_n`, the source recurrence gives the exact integer
identity

\[
\boxed{Z_{n+1}=16Q(n+1)Z_n+
\Delta_n[P(n+1)-Q(n+1)a_n].} \tag{RI-14}
\]

Moreover `Z_n/Delta_n=e_n-T_n`. Consequently R0 failure would require
the genuine polynomial forcing `P` to be cancelled, in the completed
real direction, by this sparsely supported integer carry forcing.
The cancellation is expressed by an integer identity with no free seed.
It is **not contradicted** by the identity itself.

The inherited all-index source theorem `v_2(U_n)=v_2(n)` yields an
additional necessary condition. If `16^L|K_n` and `v_2(n)<4L`, then

\[
v_2(Z_n)=v_2(n). \tag{RI-15}
\]

Indeed, `Delta_n` is odd and the two terms in `A_n-Delta_n K_n` have
unequal 2-adic valuations. The exceptional integers with `v_2(n)>=4L`
occupy at most `B/16^L+1` sites in a length-B shell. Therefore the
Gamma-cleared residual must satisfy (RI-15) at density one on the
failure shells above. This combines existing source information with
the new inverse dictionary; it does not improve the inherited isometry.
For every prime, `gcd(Z_n,Delta_n)=gcd(A_n,Delta_n)` as well. Fresh prime
denominators survive in this residual exactly as they survive in the
source; their survival says nothing yet about its real signed phases.

The product Gamma denominator has size much larger than its reduced
LCM denominator. Merely clearing more factors cannot make the
Diophantine approximation stronger. Nor does a prime's first arrival
control the old complementary cofactor. Those are the same source
dependencies that the inherited Gaussian and prime-channel controls
already exposed.

## RI-03: an exact hostile source preserving the full 2-adic clock

The first attempted strengthening of the inherited proper null source
failed. For its coefficient vector `(8,-8,-4,-8,-2,-2,1,0)/8`,

\[
U_1=1/105,\qquad U_2=268/45045,\qquad
v_2(U_2)=2\ne v_2(2).
\]

The exact receipt retains all 32 valuation failures for `1<=n<=64`.
This source was not silently replaced after its failure.

A distinct algebraic control succeeds. Define, for real nonnegative t
and also for every 2-adic integer t,

\[
A(t)=\frac{t}{(8t+1)(8t+3)(8t+5)},\quad
V_n=-A(n),\quad r_{\rm iso}(n)=16A(n-1)-A(n).
\]

Then `V_0=0`, `V_n=16V_{n-1}+r_iso(n)`, and the completed value is zero:
the actual forward tail is `A(n)` and `V_n+A(n)=0`.
The source has the polynomial integral presentation

\[
h(z)=(-1+6z^2-5z^4)/64,\quad g_{\rm iso}(z)=(16-z^8)h(z),
\quad r_{\rm iso}(n)=\int_0^1 z^{8n-8}g_{\rm iso}(z)\,dz.
\]

Indeed `int_0^1 z^{8t}h(z) dz=A(t)` by partial fractions and
`int_0^1 h=0`. This is a **nonproper degree-12 null gauge source**.
It is not the original proper four-pole source.

For `s!=t` in `Z_2`, direct subtraction gives

\[
V_s-V_t=-\frac{(s-t)[15-576st-512st(s+t)]}
 {(8s+1)(8s+3)(8s+5)(8t+1)(8t+3)(8t+5)}.
\]

Every bracket or denominator factor apart from `s-t` is a 2-adic unit.
Therefore

\[
\boxed{v_2(V_s-V_t)=v_2(s-t)\quad(s\ne t\in\mathbb Z_2).} \tag{RI-16}
\]

This includes `v_2(V_n)=v_2(n)`, the full source clock rather than only
its first parity. The forcing itself is also an isometry:
`r_iso(s)-r_iso(t)=(V_s-V_t)-16(V_{s-1}-V_{t-1})` has a unique term of
smallest valuation. Nevertheless every completed phase is exactly one,
and the uncompleted fixed-mode phases tend to one.

The sign scope is essential. We have `r_iso(1)=-1/1287<0`.
For all `n>=2`, `r_iso(n)>0`, because `A(t)` is positive and strictly
decreasing for `t>=1`; its derivative has numerator
`15-576t^2-1024t^3<0`. Also
`r_iso(n)=15/(512n^2)+O(n^-3)`. Thus zero seed, eventual positive forcing,
quadratic decay, rational states, and the full exact 2-adic isometry
together still do not imply R0. Positivity from the very first index,
properness, the four authentic poles, and the nonzero selected period
are not preserved by this control. The control makes no claim about
what follows when those further hypotheses are retained.

## RI-04: a prospective sparse-approximation cut, with its truth debt

The balanced-carry telescope is

\[
e_B=\sum_{j=1}^{L}a_{B+j-1}16^{-j}+16^{-L}e_{B+L}.
\]

For the original source form the **exact rational finite packet**

\[
\Lambda_{B,L}=U_B+\sum_{j=1}^{L}16^{-j}r(B+j)
 =16^{-L}U_{B+L}.
\]

The actual carry word obeys

\[
\left|\Lambda_{B,L}-K_B-
 \sum_{j=1}^{L}a_{B+j-1}16^{-j}\right|
 \le\left(\tfrac12+\frac1{64(B+L)^2}\right)16^{-L}. \tag{RI-17}
\]

This is an exact source dictionary, not an anti-concentration theorem.
At `L=B`, R0 failure necessarily supplies such words with `o(B)`
nonzero entries. Rephrasing their nonexistence as a sparse-digit
condition does not pay the original density obligation.

Here is a deliberately stronger, concrete arithmetic candidate that
would suffice and can be attacked without a pi oracle:

> **SAA(1/4), OPEN.** There exist `delta>0` and `B_0` such that for every
> integer `B>=B_0`, putting `L=floor(B/4)`, every integer `k` and every
> word `d in {-8,...,8}^L` supported on at most `delta L` positions obey
> \[
> \left|\Lambda_{B,L}-k-\sum_{j=1}^{L}d_j16^{-j}\right|
> >\left(\tfrac12+\frac1{64(B+L)^2}\right)16^{-L}.
> \]

Its implication is immediate and explicitly one-way: the actual carry
word in (RI-17) must then have more than `delta L` nonzeros inside the
original shell, and (RI-10) gives R0. The candidate demands density in
every prescribed quarter-shell, which R0 alone does not demand; R0
allows a coherent subinterval if the rest of each shell supplies a
uniform positive loss. No equivalence to an already proved theorem is
being claimed.

For a concrete separation at the level of real points, take hexadecimal
digits 1 everywhere except zeros on
`[16^k+1,16^k+16^k/4+1)`, for `k>=1`. With digits indexed from 1,
the balanced carry is `a_n=b_(n+1)`, so the quarter-shell starting at
`B=16^k` has exactly the indicated zero carries. The total zero positions below `2B`
are at most `8B/15`; hence every shell has at least `7B/15` digit-one
positions, each with phase in `[1/16,1/15]` and loss at least `kappa_*`.
This point has R0, but its indicated quarter-shells have every balanced
carry zero. This is a changed completed point, not a statement about pi.

After multiplying by `16^L Delta_{B+L}`, this becomes the integer
separation problem

\[
|A_{B+L}-\Delta_{B+L}M|
 >\Delta_{B+L}\left(\tfrac12+\frac1{64(B+L)^2}\right),
\quad M=16^Lk+\sum_{j=1}^{L}d_j16^{L-j}.
\]

The useful new arithmetic would be a lower bound for this selected
sparse set of M, using the authentic numerator, denominator survival,
and old complementary source together. Counting available primes,
applying a generic 2-adic isometry, or importing an unrestricted
irrationality exponent does not give that lower bound. RI-03 defeats
one tempting generic substitute. No proof of SAA(1/4) is supplied here;
it is the strongest explicit next cut from this inverse lane.

## Source cuts, novelty accounting, and finite receipt

The main new unconditional source-selected theorem is RI-01, its
block-ratio application and the endpoint coefficient in RI-8E. RI-02 is an exact deterministic inverse
dictionary. RI-03 is a source-family counterexample with declared lost
hypotheses. RI-04 is an open sufficient arithmetic condition.

The inspected restricted-exponent dossier already establishes that the
original BBP partial sums cannot certify their own restricted exponent
by clearing denominators; the needed linear forms require convergent
integer-normalized errors and favorable base-prime divisibility.
Its Gaussian one-pole observations put the useful imbalance on the
constant term, not on the coefficient of pi. The elementary small-angle
lemma for one Gaussian logarithm does not cover arbitrary simultaneous
Machin-type forms. These are route-specific boundaries, not a theorem
that no restricted approximation can work. The imported Rivoal bound
for `log(16/15)` remains a calibration: a restricted exponent below one
does not itself prove density. No new restricted exponent for pi has
been obtained here.

The inspected Borwein/factorial construction gives stable exact
reconstruction and authenticated prime-clock gates. Its exact integer
samples deliberately erase the prime-width information. Consequently
its Hilbert positivity is not a signed digit-distribution estimate.
The inspected ABC contingency requires a joint approximation and
radical bound on a primitive integer residual; it cannot apply ABC to
the irrational tail directly. Neither imported construction supplies
the missing sparse numerator estimate in RI-04.

The code ran **17 focused tests successfully**. The separate deterministic
report checked 81 exact inverse-Gram minimizers and 2,775 distinct
integer-pair instances of (RI-16). The proof of (RI-16), not the census,
extends to all of `Z_2`. All five original-source shell packets have
authenticated nearest-integer lifts and exact rational loss enclosures:

| B | Outward-rounded enclosure for actual A_B | Nonzero internal balanced carries |
|---:|---:|---:|
| 17 | [0.648, 1.108] | 14 |
| 43 | [0.672, 1.097] | 39 |
| 89 | [0.666, 1.166] | 81 |
| 179 | [0.719, 1.200] | 170 |
| 359 | [0.709, 1.216] | 341 |

These are intentionally coarse rigorous enclosures from
`8||y||^2<=F(y)<=min(2,2(22/7)^2||y||^2)`. They are not fitted Fourier
asymptotics. The exact intervals, phase enclosures, balanced carry words,
integer-lift hashes, and failed mutant values are in
[r0_results.json](r0_results.json). The true interval for `pi/16` uses
the full depth-742 prefix and its positive tail; no floating pi digits
are supplied as an oracle.

The coherent changed seed and dyadic alias controls have exact loss zero.
The periodic point `1/15` has positive first-mode real loss, yet is not
normal; this separates R0 from normality. On the preregistered Shallit
shells the internal carry count is zero and the loss is positive but
bounded by a constant divided by B. The periodic and Shallit controls
are mathematical constructions, not surrogate evidence about pi.

Read-path hashes and precise inspection scopes are recorded in
[r0_sources.json](r0_sources.json). Main XXV provenance is retained;
older dossiers, helpers, and this agent are dependent sources when
they use the same recurrence or classical theorem. The reviewing
agents share a model family and do not constitute external peer review.
Full-repository validation is recorded by the root task separately.
No Lean kernel check of these new infinite statements is claimed.

# Five forward state readings determine the declared BBP source family

**Status: PROVED PAPER, within the explicit source class.** This extends the
four-innovation-plus-anchor construction in [PR #668, FC-01/02](https://github.com/femboy2112/SUCC/blob/15154b8b63969faa76ad2b161aad54f41cae1c63/research/2026-11-19/causal_jacobian_probe_lattice/five_channel/CONSTRUCTION.md).
The extension counts actual scalar state readings on one forward trajectory,
permits arbitrary gaps, and proves a matching adaptive lower bound. It is an
elementary Cauchy-determinant consequence; academic priority is not claimed.

## SA-01. The acquisition model

Let the five unknown real parameters be
$\theta=(s,c_1,c_2,c_3,c_4)\in\mathbb R^5$. Set

$$
d=(7,4,3,2),\qquad
r_c(n)=\sum_{a=1}^4\frac{c_a}{8n-d_a},\qquad
U_0=s,\qquad U_n=16U_{n-1}+r_c(n).
$$

The source selected by the project is $s=0,c=(4,-2,-1,-1)$.
The family is a counterfactual identification model, not a distribution of
physical sources. Its formula, pole labels, radix, time labels and absence of
other forcing terms are hypotheses. The observer can read the **unwrapped**
scalar $U_t$ at an elapsed nonnegative integer time, without perturbing the
modeled recurrence. Each exact real reading is an ideal precision assumption.
For rational parameters and finite clocks the implementation uses exact
rationals; finite precision has its own cost below.

Choose any five strictly increasing integers
$$
0\le t_0<t_1<t_2<t_3<t_4.
$$
Only these five scalar states are required. Intermediate source states do not
have to be observed or stored. The last datum becomes accessible at $t_4$.
Computing a difference of retained readings later does not reverse source time.

Define
$$
a_t=\left(\sum_{j=1}^t\frac{16^{-j}}{8j-d_a}\right)_{a=1}^4,
\qquad v_i=16^{-t_i}U_{t_i}=s+a_{t_i}c.
$$
Here $a_0=0$. For $i=1,\ldots,4$ put
$$
I_i=\{t_{i-1}+1,\ldots,t_i\},\qquad
B_{ia}=\sum_{j\in I_i}\frac{16^{-j}}{8j-d_a}.
$$
Then the four differences $w_i=v_i-v_{i-1}$ satisfy $w=Bc$.

## SA-02. Arbitrary five-time global reconstruction

**Theorem.** For every such ordered five-tuple, $\det B>0$. Consequently

$$
\boxed{c=B^{-1}w,\qquad s=v_0-a_{t_0}B^{-1}w}
$$

is a global inverse on $\mathbb R^5$. The same rational formulas hold over
$\mathbb Q$ and over any characteristic-zero field containing the parameters.

**Proof.** If $j_1<j_2<j_3<j_4$ are positive integers, the Cauchy matrix
$C_{ia}=1/(8j_i-d_a)$ has determinant

$$
\det C=
\frac{120\,8^6\prod_{i<k}(j_k-j_i)}
     {\prod_{i,a}(8j_i-d_a)}>0.
\tag{1}
$$

The numerator follows from the two Vandermonde products; the fixed pole
product is $\prod_{a<b}(d_a-d_b)=120$. All denominators are positive.
Multilinearity in the four rows gives the exact finite identity

$$
\boxed{\det B=
\sum_{j_1\in I_1,\ldots,j_4\in I_4}
16^{-(j_1+j_2+j_3+j_4)}
\frac{120\,8^6\prod_{i<k}(j_k-j_i)}
     {\prod_{i,a}(8j_i-d_a)}.}
\tag{2}
$$

Disjoint ordered intervals guarantee $j_1<\cdots<j_4$ in every term.
Each interval is nonempty, so this is a nonempty sum of strictly positive
numbers. Hence $B$ is invertible. The displayed inverse follows from the
four difference equations and the first normalized reading. No limiting
argument, data fitting, or assumption about pi digits is used. QED.

This proves the result for irregular, consecutive and Fibonacci schedules.
It does not say their numerical conditioning or acquisition latency is equal.
The determinant formula is a proof certificate, not the recommended numerical
algorithm: the implementation forms four finite sums and inverts one matrix.

### The actual five-by-five Jacobian

Let $R_t$ have rows $16^{t_i}(1,a_{t_i})$, so raw observations equal
$R_t\theta$. Normalize each row and subtract the preceding normalized row,
using the original rows in each difference. This determinant-one difference
operation gives
$$
\begin{pmatrix}1&a_{t_0}\\0&B\end{pmatrix}.
$$
Therefore
$$
\boxed{\det R_t=16^{\sum_{i=0}^4t_i}\det B>0.}
\tag{3}
$$
For consecutive samples $t_i=N+i$,
$$
\det R_t=16^N\det\left[\frac1{8(N+i)-d_a}\right]_{i,a=1}^4.
\tag{4}
$$
The apparently growing raw determinant and shrinking normalized determinant
refer to different measurement units. Neither alone bounds the worst error.

## SA-03. Five is a sharp count, including adaptive clocks

**Theorem.** On any nonempty open parameter set $\Omega\subseteq\mathbb R^5$,
no deterministic policy using at most four scalar unwrapped state readings on
each run can recover all five parameters exactly for every source in $\Omega$.
The next strictly later clock and the stopping decision may be arbitrary
functions of earlier readings. No continuity of this policy is assumed.

**Proof.** Fix an actual run at any $\theta\in\Omega$, with $k\le4$
readings. Once its transcript is fixed, the $k$ clock labels are fixed.
Let $R$ be their $k$-by-five observation matrix. Choose
$0\ne u\in\ker R$, which exists by rank-nullity. Since $\Omega$ is
open, $\theta'=\theta+\epsilon u$ belongs to $\Omega$ for a sufficiently
small nonzero real $\epsilon$. At the first chosen clock the two readings
coincide. Inductively identical earlier readings give the same next clock and
the same next reading. They also give the same stopping decision and output.
The policy therefore cannot identify both distinct parameters. QED.

SA-02 attains the lower bound with any fixed five-clock schedule. Thus this is
a sharp acquisition theorem in the stipulated class, not merely a parameter
counting heuristic. It fails as a universal count if the prior class is smaller
or a different observation is allowed. For a rational parameter class the same
argument works with a nonzero rational kernel vector when all rational
parameters are allowed; arbitrary sparse priors require separate analysis.

| Prior knowledge and target | Sufficient number of raw scalar state readings | Scope |
|---|---:|---|
| Four coefficients and seed all free; recover all five | 5, sharp | SA-02/03; any ordered five clocks |
| Seed known; recover four free coefficients | 4, sharp | Four positive clocks; the known time-zero value supplies the anchor |
| Coefficients known; recover free seed | 1, sharp | Any finite clock, with integer lift retained |
| Source formula and literal zero seed already known | 0 for symbolic specification | Computation and validation remain work; this is not a new measurement |

For the known-seed row, subtract its contribution and append the known value
at time zero. The same determinant proof applies. Fewer than four readings
have a nontrivial coefficient kernel. For known coefficients,
$s=16^{-t}U_t-a_tc$. These counts do not give an observation budget for
proving normality or authenticating an unrestricted unknown source law.

## SA-04. Exact knowledge fibers and paid precision

Suppose the five raw readings are $y_i$ with deterministic error bounds
$\epsilon_i>0$. The compatible parameter set is exactly
$$
\mathcal K_y=\{\theta: |(R_t\theta)_i-y_i|\le\epsilon_i\ (0\le i\le4)\}
 =R_t^{-1}\bigl(y+\prod_i[-\epsilon_i,\epsilon_i]\bigr).
$$
In fixed real parameter and raw readout units its five-dimensional Lebesgue
volume is
$$
\boxed{\operatorname{vol}(\mathcal K_y)
=\frac{2^5\prod_i\epsilon_i}{|\det R_t|}.}
\tag{5}
$$
For the center estimator $\widehat\theta=R_t^{-1}y$, each coordinate has
the **sharp** worst-case error
$$
\boxed{|\widehat\theta_j-\theta_j|
\le\sum_i |(R_t^{-1})_{ji}|\epsilon_i.}
\tag{6}
$$
Choose error signs agreeing with a specified row of the inverse to attain
that row's bound. Different rows need not attain their maxima on the same
error vector. For uniform error $\epsilon$, the worst infinity-norm
error is $\epsilon\|R_t^{-1}\|_\infty$.

Equations (5) and (6) follow by an invertible linear change of variables and
the triangle inequality, respectively. No probability law or independence
assumption is used. If readings are normalized by $16^{-t_i}$, their error
bounds must be normalized by the same factors; the compatible set is unchanged.
Additional honest readings intersect this set with additional strips, so
retaining observations cannot enlarge the compatible set. Re-expressing old
readings does not create information.

This supplies a real knowledge-volume interface to #668's distinct local-field
Smith-volume theorem. Real volume, p-adic volume, function-space dimension and
Shannon information require their own measures and units; they are not one number.

### Late consecutive readings: small volume with growing uncertainty

Fix a raw absolute error budget $\epsilon>0$, and take clocks
$N,N+1,\ldots,N+4$. As $N\to\infty$, the exact formulas imply
$$
\det R_N\sim\frac{1440}{8^{10}}\frac{16^N}{N^{16}},\qquad
\operatorname{vol}(\mathcal K_y)
\sim\frac{2^5\epsilon^5 8^{10}}{1440}\frac{N^{16}}{16^N},
\tag{6a}
$$
while
$$
\boxed{\|R_N^{-1}\|_\infty=\Theta(N^7).}
\tag{6b}
$$
Thus the compatible volume tends to zero, but the sharp worst-case parameter
error for a fixed raw readout error grows as $\epsilon\Theta(N^7)$.
This is a property of the specified unwrapped measurement and parameter units.

**Proof.** Set $(C_N)_{ia}=1/(8(N+i)-d_a)$, $1\le i,a\le4$.
Its determinant numerator is $120\,8^6\prod_{i<j}(j-i)=1440\,8^6$,
and its sixteen denominator factors are each asymptotic to $8N$.
Combine this with (4) and (5) to obtain (6a).

Every three-by-three Cauchy minor has a fixed nonzero numerator and nine
denominator factors asymptotic to $8N$. The cofactor formula therefore
makes every entry of $C_N^{-1}$ a nonzero constant times $N^7(1+o(1))$.
The four consecutive innovations are $D y$, where the fixed four-by-five
matrix $D$ has $-16,1$ in adjacent columns of each row. Hence the four
coefficient rows of $R_N^{-1}$ are $C_N^{-1}D$. They are $O(N^7)$,
and their first column is $-16(C_N^{-1})_{\cdot1}$, which supplies the
matching lower bound. Finally
$s=16^{-N}U_N-a_Nc$ and $a_N$ is uniformly bounded, so the seed row
is also $O(N^7)$. This proves (6b). QED.

Knowledge volume is therefore insufficient as a sole accuracy score even in
this exactly identifiable linear family. The inverse rows retain the direction
information that the determinant discards. Counting samples, precision, and
elapsed acquisition time separately is necessary for an operational comparison.
This compares different five-clock schedules. Retaining earlier honest readings
still intersects compatible sets and cannot enlarge uncertainty.

## SA-05. Exact global generator and its completion boundary

The recovered parameters determine every finite subsequent state by the original
recurrence. They also determine the convergent scalar
$$
x(c)=\sum_{j\ge1}16^{-j}r_c(j),\qquad
16^{-n}U_n\longrightarrow s+x(c).
$$
Absolute convergence holds because $|r_c(j)|\le\|c\|_1/(8j-7)$.
For $M\ge0$, the source completion has the explicit bound
$$
\left|x(c)-\sum_{j=1}^M16^{-j}r_c(j)\right|
\le\frac{\|c\|_1}{15\,16^M(8M+1)}.
\tag{7}
$$
Indeed $8j-7\ge8M+1$ for $j\ge M+1$, and the remaining geometric
weights sum to $16^{-M}/15$. The sharper positive BBP tail bound belongs
to the selected coefficient vector and should be used there.

For that selected coefficient vector **and the authentic zero seed**, let $x=\pi/16$,
$T_n=\sum_{j\ge1}16^{-j}r(n+j)$, and $Y_n=16^nx$. Then
$$
U_n+T_n=Y_n,\qquad
q_{n|M}=16^{n-M}U_M,\qquad
Y_n-q_{n|M}=16^{n-M}T_M.
$$
For an arbitrary seed the first identity instead reads
$U_n+T_n=16^n(s+x)$; the seed cannot be dropped during completion.
These identities and the terminal signed transport are **inherited** from
[PR #668, FA-03/05](https://github.com/femboy2112/SUCC/blob/15154b8b63969faa76ad2b161aad54f41cae1c63/research/2026-11-19/causal_jacobian_probe_lattice/five_channel/FRAME_AGREEMENT.md).
For a nonzero integer frequency $h$, define the chronological shell mean
$W_B(h)=B^{-1}\sum_{n=B}^{2B-1}e(hY_n)$. At $M=2B$ they give
$$
\left|W_B(h)-\frac1B\sum_{k=1}^B e\left(hU_{2B}/16^k\right)\right|
<\frac{2\pi|h|}{225B}r(2B+1),\qquad e(t)=e^{2\pi it}.
\tag{8}
$$
Recovery of the source and convergence to its endpoint do not prove decay of
the finite signed mean on the right. Its all-late-shell source-selected bound
is the remaining arithmetic theorem. No exchange of those two limits is assumed.

## SA-06. Hostile controls and the meaning of exact reconstruction

- **Wrong seed:** the same source with $s=-x$ has completed orbit zero.
  Its coefficient Jacobian is identical but its reconstructed seed differs.
  Symbolic $\mathbb Q+\mathbb Qx$ arithmetic detects the latter exactly;
  floating approximations are not equality oracles for arbitrary reals.
- **Wrapped alias:** with seed shift $1/16$, all raw state differences at
  clocks $t\ge1$ are integers $16^{t-1}$. All fractional-state readings
  therefore agree. The unwrapped inverse detects the difference. A bare circle
  value is not the stipulated input.
- **Delayed changed source:** add a nonzero forcing impulse strictly after
  the last observation. Every previous state agrees but a future state changes.
  This rival is outside the declared four-pole family and refutes extrapolation
  from finite data without that family hypothesis.
- **Repeated clock:** duplicate rows lose rank; five reports need not be five
  independent chronological observations.
- **Precision:** a nonsingular matrix can have a large inverse norm. Exact
  identification never gives a free finite-bit error bound.

Thus the result is a complete finite acquisition-and-generation theorem for a
specified family. It preserves Leah's intended compression: five encounters can
identify a rule describing infinitely many later states. The rule's difficult
statistical properties still require their own proofs.

## Provenance and next falsifier

The original source is Main XXVI's `docs/PI_NORMALITY_FRONTIER.md` and
`observational_succ/duck_bbp.py`; imported originals are untouched. #668 provides
the Cauchy source family, four innovations, seed anchor, prime repairs and exact
frame transport. #669 provides related source gluing but not an independent
source law. This note proves the new raw-sample/block-minor acquisition interface.

An independent derivation should attack the sign of (2), the adaptive transcript
argument, and the interpretation of exact readout precision. The finite audit
compares direct recurrence samples with an independently constructed sampling
matrix, reconstructs irregular later samples, and deliberately removes weights,
anchors and lifts. Exact test receipts appear in `VALIDATION.md`.

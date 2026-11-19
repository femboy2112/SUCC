# A finite five-channel observer with paid prime-resolution repair

**Status:** theorems within the declared four-pole source family, implemented with
exact rational arithmetic. Source identification, local invertibility, and the
prime precision contracts are proved below. No signed Weyl saving, R0, or pi
normality is inferred. The original source and literal zero seed are preserved.

## 1. The object and its actual five coordinates

Fix `d=(7,4,3,2)` and the parameter family

\[
r_c(n)=\sum_{j=1}^4\frac{c_j}{8n-d_j},\qquad
U_0=s,\quad U_n=16U_{n-1}+r_c(n).
\]

The authentic member is `c=(4,-2,-1,-1), s=0`. The construction is linear over
the reals; the executable observer uses rational parameters and exact rational
states. Let four distinct positive observation clocks `m_i` have already elapsed,
and let `N>=max(m_i)`. Record four innovations and one **unwrapped finite anchor**:

\[
\mathcal O_{m,N}(c,s)=
\left(U_{m_i}-16U_{m_i-1}\right)_{i=1}^4
\mathbin\oplus16^{-N}U_N
=Cc\mathbin\oplus(s+a_N^Tc),
\]

\[
C_{ij}=\frac1{8m_i-d_j},\qquad
(a_N)_j=\sum_{n=1}^N\frac{16^{-n}}{8n-d_j}.
\]

Everything here uses a finite causal slice. The fifth coordinate does **not**
request the completed irrational endpoint `s+x(c)` as an observation oracle.
It retains the state lift; reducing it modulo one would lose seed information.
Four innovation coordinates require their underlying adjacent state readings.
Five coordinates mean a five-coordinate readout, not five observations total,
five memory cells, or a uniformly finite-state machine. The journal may grow.

### FC-01: global inversion and the exact Jacobian

With parameter order `(c_1,c_2,c_3,c_4,s)`, the derivative is

\[
D\mathcal O_{m,N}=
\begin{pmatrix}C&0\\a_N^T&1\end{pmatrix},\qquad
\det D\mathcal O_{m,N}=\det C\ne0.
\]

In fact the map is globally invertible in this parameter family:

\[
c=C^{-1}y,\qquad s=z-a_N^TC^{-1}y.
\]

**Proof.** Iterating the recurrence gives
`16^-N U_N=s+sum_(n<=N)16^-n r_c(n)`. Innovations remove every past-state and
seed contribution. The displayed triangular form and inverse follow. Nonsingularity
of `C` is proved in FC-02. No local inverse theorem or infinite limit is needed.

**Authentication boundary.** Exact recovery of `(c,s)` identifies the source only
within this declared four-pole family. Four samples cannot certify an unrestricted
unknown forcing. `validate_journal(..., authentic=True)` additionally checks the
literal coefficients, literal zero seed, and every elapsed recurrence step in its
journal. This does not turn a finite journal into verification of an arbitrary
infinite physical source. Here the exact formula supplies the source contract.

The derivative is independent of the selected `(c,s)`. Thus the same Jacobian
exists at a zero forcing with locked zero orbit, at the original forcing with
changed seed `s=-pi/16`, and at the authentic source. The last two have different
seed anchors. Invertibility identifies the member; it does not prove its statistics.
The rational seed `1/16` aliases all later circle phases but is detected by the
unwrapped anchor. Tests retain this precise failure mode.

## 2. Source resolution and the Fibonacci observation schedule

### FC-02: the Cauchy determinant

For distinct positive clocks in their given row order,

\[
\boxed{\det C=
\frac{120\,8^6\prod_{i<k}(m_k-m_i)}
{\prod_{i,j}(8m_i-d_j)}}.
\]

**Proof.** Clear the row denominators in the Cauchy matrix. Its determinant is an
alternating polynomial in the four row nodes `8m_i` and separately in the four
column nodes `-d_j`; its degree gives the corresponding two Vandermonde factors.
Matching one coefficient, or successive partial-fraction residues, gives constant
one in the Cauchy identity. Here `prod_(j<k)(d_j-d_k)=120`, and the six row
differences each contribute a factor eight. Positive clocks avoid real poles.
An independent permutation-expansion oracle checks the implemented determinant,
including an unsorted row order.

For consecutive clocks `(n,n+1,n+2,n+3)`, `prod_(i<k)(m_k-m_i)=12`, so

\[
\det C\sim\frac{1440}{8^{10}}n^{-16}.
\]

For clocks `m_i=alpha_i n+O(1)` with fixed distinct positive `alpha_i`,

\[
\det C\sim\frac{120\prod_{i<k}(\alpha_k-\alpha_i)}
{8^{10}\prod_i\alpha_i^4}\,n^{-10}.
\]

For `(F_k,F_(k+1),F_(k+2),F_(k+3))`, take `n=F_k` and
`alpha_i=phi^(i-1)`, using `F_(k+j)/F_k -> phi^j`. This is the asserted
`Theta(n^-10)` result. Fibonacci spacing is one particular separated schedule;
it is not the unique mechanism. It also has a later last observation: roughly
`phi^3 n`, compared with `n+3`. This is a resolution/latency tradeoff.

At clocks `(55,89,144,233)` relative to `(55,56,57,58)`, the **exact** ratio is

\[
\frac{18727804072912891802425918399248}{42573062902996830648629875}
=439897.9729408802\ldots.
\]

These are Jacobian volumes in the explicitly fixed coefficient and readout units.
They are not coordinate-free information counts, probabilities, error bars, or
estimates of Weyl cancellation. A determinant alone also does not bound the worst
singular direction. The prime charts below compute an actual inverse error cost.

**Different meanings of five.** The five parameters `(c,s)` are a genuine
five-dimensional source family. The earlier `Sym^4(A^2)` construction maps two
Fibonacci state variables into five quartic readouts; its state derivative has
rank at most two. Equal readout counts do not establish a conjugacy. This observer
uses Fibonacci numbers as clock choices, not as a replacement for the BBP source.

## 3. Polar charts make prime 7 usable

For a prime `p`, define

\[
e_i=\max_jv_p(8m_i-d_j),\quad D_p=\operatorname{diag}(p^{e_i}),
\quad A_p=D_pC.
\]

All entries of `A_p` are `p`-integral. The corresponding measured readout is
`D_p y`. This explicitly retains the polar/principal-part scale: an entry with a
denominator divisible by `p` is never silently reduced as an ordinary residue.
For coefficient reconstruction modulo `p^a` below, coefficients are `p`-integral.

### FC-03: unit prime chart for all p >= 7

If the four clocks have distinct residues modulo `p>=7`, then

\[
A_p\in GL_4(\mathbb Z_p),\qquad v_p(\det A_p)=0.
\]

**Proof.** The four pole labels are distinct modulo every prime at least seven,
so in each row at most one denominator is divisible by `p`. Consequently
`sum_j v_p(8m_i-d_j)=e_i`. All six clock differences and the constant
`120*8^6` are units. FC-02 gives `v_p(det C)=-sum_i e_i`, exactly canceled by
`det D_p`. Integral entries and unit determinant prove the claim.

At `p=7` there are only three pole-free clock residues, since four of seven
residues are poles. Hence no four-row ordinary pole-free chart can be invertible
modulo seven. The **polar chart is required**, not a failed experiment to omit.
At `(55,89,144,233)`, its exponents are `(0,0,1,2)` and its rank is four.

## 4. Adaptive repair at eleven preserves the causal journal

The original Fibonacci clocks modulo eleven are `(0,1,1,2)`. Thus the rows for
89 and 144 coincide modulo eleven, and the ordinary matrix has rank three.
Replacing **233 with 147 does not repair this collision**. A prospective plan
that preserves the last clock 233 can replace **144 with 147**, producing residues
`(0,1,4,2)` and full rank. Such a plan must be adopted before that observation;
an old record cannot be relabeled afterward.

If all four original observations have already elapsed, the default ordinary
repair appends clock 235 and uses `(55,89,233,235)`. Clock 234 is a pole at eleven,
so it is excluded by this ordinary-chart convention. Its readout is not discarded
from the full source journal. An explicitly polar repair may instead append 234;
FC-03 proves its normalized chart is also invertible.

These are forward-repair policies, not necessary waiting times for every memory
model. The implemented full journal also retains states 146 and 147. At time
233 it can therefore compute the innovation at 147 and change its readout to
`(55,89,147,233)` immediately. This is a new probe of retained history at the
present time, not a new event at time 147. An observer that kept only the four
old innovation reports cannot assume this retrospective access. The separate
future-planning API operates on its explicit observation-clock history.

`plan_prime_repair` selects from clock residues and the declared source poles
only. It does not inspect a phase value or choose a favorable signed statistic.
It returns a future plan; `observe` rejects it until those clocks have elapsed.
In ordinary mode `p>=11`, at least seven residues are admissible and four can be
chosen. In polar mode `p>=7`, all residues are admissible and four can be chosen.
Starting after the elapsed horizon, at most `4p` further ticks suffice for either
construction. Every previous observation remains in the journal.

## 5. Small primes and the exact cost of unresolved directions

The assertion in FC-03 is not transferred to 2, 3, or 5 at the originally fixed
clocks. For any fixed clock tuple calculate the exact inverse of the normalized
rational matrix and define

\[
L_p=\max\left(0,-\min_{i,j}v_p((A_p^{-1})_{ij})\right).
\]

### FC-04: sharp uniform precision payment

If the normalized measurements of `A_p c` are correct modulo `p^(a+L_p)`,
then multiplying by `A_p^-1` recovers `c` modulo `p^a`.

**Proof.** Each coordinate error has valuation at least `a+L_p`. In each inverse
matrix product every summand has valuation at least `a`, so their sum does also.
Sharpness when `L_p>0`: choose an inverse entry of valuation `-L_p` and place a
measurement error `p^(a+L_p-1)` in that column only. The corresponding recovered
coordinate has valuation exactly `a-1`, so one fewer measured digit is insufficient
in the worst case. This is an exact operator norm statement, not only a determinant
bound. The tests include that deliberately underpaid precision mutation.

For the original clock tuple the exact arithmetic receipt is:

| p | Row exponents e | Rank modulo p | Extra measured digits L_p | v_p(det A_p) |
|---|---|---:|---:|---:|
| 2 | (2,2,2,2) | 1 | 15 | 23 |
| 3 | (1,1,1,1) | 3 | 1 | 1 |
| 5 | (0,1,2,1) | 4 | 0 | 0 |
| 7 | (0,0,1,2) | 4 | 0 | 0 |
| 11 | (0,0,0,0) | 3 | 1 | 1 |

Thus prime 11 also permits a precision repair without waiting: one extra
normalized input digit resolves the lost coefficient digit. At prime 2,
`e_i=2` for every positive clock and the normalized reduction always has the
same single nonzero column. Refining resolution is necessary for this readout.
The table gives **innovation-channel** precision debt, not the additional cost
of reconstructing the seed anchor. That separate cost is specified next.

Changing every prime to the ordinary eleven-repaired tuple is not globally
monotone: `(55,89,233,235)` has `L_2=16`, `L_3=2`, and `L_5=1`, although
`L_11=0`. Keep an atlas with different four-row readouts for different primes,
all drawn from the same retained history. This is one causal source with several
coordinate charts; the charts are not independent random samples.

### FC-05: the fifth channel has its own precision budget

The full normalized observation Jacobian is

\[
J_p=\begin{pmatrix}A_p&0\\a_N^T&1\end{pmatrix},\qquad
J_p^{-1}=\begin{pmatrix}A_p^{-1}&0\\-a_N^TA_p^{-1}&1\end{pmatrix}.
\]

If innovation errors are bounded by `p^-k` and the anchor error by `p^-b`,
the recovered coefficient errors have valuation at least `k-L_p`, while the seed
error has valuation at least

\[
\min\left(b,\ k+\min_j v_p((a_N^TA_p^{-1})_j)\right).
\]

This follows directly from the inverse formula and the ultrametric inequality;
zero entries have infinite valuation. In particular, the factor `16^-N` makes
the normalized seed anchor expensive at prime 2. FC-04 alone never claims a
five-channel `p`-adic isometry. The implemented snapshot retains exact rational
values, so it pays this cost by exact arithmetic instead of hiding it.
`five_channel_budget` also reports the explicit finite-precision alternative.
For the original clocks and `N=233`, the additional innovation accuracy needed
for the seed coordinate is respectively `(934,7,4,3,2)` digits at
`p=(2,3,5,7,11)`. Recovering all five parameters modulo `p^a` is assured by
`a+max(L_p,L_seed)` digits of normalized innovations and anchor error valuation
at least `a`. The table in section 5 therefore must never be advertised as the
cost of authenticating the complete five-coordinate state. An exact symbolic
literal-zero seed is a separate boundary datum, not a free approximate recovery.

## 6. A bounded future repair at every odd prime

### FC-06: separate the source poles at sufficient clock resolution

For an odd prime `p`, set

\[
a_p=1+\max_{j<k}v_p(d_j-d_k).
\]

For the literal four pole labels, `a_3=a_5=2`, and `a_p=1` at every other
odd prime. Given any elapsed integer horizon `N>=1`, choose for each pole
label `d_j` the first integer `m_j>N` satisfying

\[
8m_j\equiv d_j\pmod{p^{a_p}}.
\]

These are four distinct future clocks, all at most `N+p^a_p`. Observe their
innovations and normalize each row by the largest denominator valuation as
above. The resulting four-source-channel matrix is in `GL_4(Z_p)`.
In particular, its inverse coefficient precision cost is zero.

**Proof.** Eight is a unit modulo every odd prime power, so each congruence has
one residue class. The four pole labels are distinct modulo `p^a_p`: equality
would contradict the definition of `a_p`. Thus the four first future clocks
are distinct and each lies within one complete period after `N`.

For the row chosen for pole `j`, let `e=v_p(8m_j-d_j)>=a_p`. For every `k!=j`,

\[
8m_j-d_k=(8m_j-d_j)+(d_j-d_k),
\qquad
v_p(8m_j-d_k)=v_p(d_j-d_k)<a_p\le e.
\]

The equality uses the ultrametric rule for summands of unequal valuations.
After multiplying this row by `p^e`, the entry in column `j` is a unit and
all other entries vanish modulo `p`. Each pole has its own row, so the full
reduction is a diagonal unit matrix up to the permutation needed to sort the
observation clocks. Its determinant is a unit. This proves the claim for every
odd prime and every elapsed horizon, including the previously colliding labels
at three and five.

At `N=233`, the deterministic schedules are:

| Prime | Clock depth a_p | Four appended clocks | Normalized rank | Inverse source cost |
|---|---:|---|---:|---:|
| 3 | 2 | (236,239,240,241) | 4 | 0 |
| 5 | 2 | (238,241,244,254) | 4 | 0 |

`plan_polar_repair(history,p)` implements this construction from the clock and
source labels only. It preserves the old history and plans four additional
observations. None can be consumed before its clock has elapsed. Compared with
the original modulo-three chart of rank three, this is an actual constructive
repair with a uniform finite delay bound, not a claim that more input digits at
the same clocks will somehow create a new independent channel.

The **clock resolution** `a_p`, the row-normalizing exponents `e_i`, and the
**measurement precision** needed for a coefficient modulo `p^b` are distinct.
The new normalized chart needs `b` measured digits for its four coefficient
coordinates, but those measurements retain their declared polar scales. The
fifth seed coordinate still has the cost in FC-05; it is not made free by this
repair. A late observation also does not erase the causal time it consumed.

There is no analogous conclusion here at `p=2`: eight is not invertible modulo
powers of two, and every positive integer clock has `e_i=2`, with the same
single nonzero column in the normalized reduction. `plan_polar_repair` rejects
two. The fixed-clock precision budget remains available there.

## 7. One chart repairs every odd prime within nine ticks

FC-06 repairs each odd prime by a constructive pole-specific schedule. The literal
four-pole denominator pattern permits a stronger common chart, with a delay bound
independent of the prime. This is the preferred repair when four new consecutive
observations are available; the individual polar construction remains a separate
valid identity.

For four consecutive clocks `m_i=n+i`, `i=0,1,2,3`, define

\[
L_i=\operatorname{lcm}_{j=1}^4(8m_i-d_j),\qquad
B_n=\operatorname{diag}(L_i)C.
\]

The matrix `B_n` is integral. The row scales are explicit measured-coordinate
changes, not silently discarded denominators.

### FC-07: exact common chart and Smith factors

For **every** integer `n>=1`,

\[
\boxed{\det B_n=2^{19}\,
3^{\mathbf1_{n\not\equiv2\pmod3}}
5^{\mathbf1_{n\equiv0\pmod5}}.}
\]

In particular, if `n=2 mod3` and `n!=0 mod5`, then

\[
\operatorname{Smith}(B_n)=\operatorname{diag}(1,4,64,2048).
\]

Consequently `B_n` is invertible over `Z_p` for **every odd prime simultaneously**
and at every finite prime-power resolution. Its sharp binary inverse precision
cost is eleven digits. Its integral cokernel is
`Z/4 + Z/64 + Z/2048`, of order `2^19`; this is the scoped lattice-volume
statement, not a statement about real-circle orbit distribution.

**Determinant proof.** The numerator of FC-02 at consecutive clocks is
`120*8^6*12=2^23*3^2*5`. Passing from each denominator product to its LCM removes
only repeated prime factors within a row. A repeated prime must divide the
difference of two pole labels, so the only possibilities are two, three, and five.

- At two, the four denominator valuations are always `(0,2,0,1)`. Their sum minus
  their maximum is one, contributing exactly `2^4` across the four rows.
- At three, the labels seven and four coincide. A repeated factor occurs exactly
  at clocks `m=2 mod3`, and its excess valuation is exactly one because their
  denominator difference is three. There are two such rows precisely when
  `n=2 mod3`; otherwise there is one.
- At five, the labels seven and two coincide. A repeated factor occurs exactly
  at clocks `m=4 mod5`, with excess valuation exactly one. A four-clock block has
  one such row precisely when `n!=0 mod5`; otherwise it has none.

Dividing the Cauchy numerator by these exact excess factors gives the formula.
It also proves that no unlisted odd-prime obstruction can appear at a later time.

**Smith proof.** Let `delta_k` be the minimum binary valuation of the nonzero
`k` by `k` minors, with `delta_0=0`. Every row LCM has valuation two. For row
indices `I` and column labels `J`, the Cauchy minor formula gives

\[
v_2\bigl(\det((B_n)_{I,J})\bigr)=
2k+3\binom{k}{2}
+v_2\!\left(\prod_{i<l\in I}(m_l-m_i)\right)
+v_2\!\left(\prod_{j<l\in J}(d_j-d_l)\right)
-k\sum_{j\in J}v_2(8m-d_j).
\]

The last denominator valuations are independent of the row clock. The minimum
row contribution and minimum column contribution can therefore be selected
independently. Their values, obtained directly from four consecutive row nodes
and the fixed labels, are:

| k | Minimum row Vandermonde valuation | Minimum column contribution | delta_k |
|---|---:|---:|---:|
| 1 | 0 | -2 | 0 |
| 2 | 0 | -5 | 2 |
| 3 | 1 | -8 | 8 |
| 4 | 2 | -9 | 19 |

For example, columns `(4,2)` attain the two-column minimum, and columns
`(7,4,2)` or `(4,3,2)` attain the three-column minimum. The resulting Smith
valuation differences are `(0,2,6,11)`. At admissible starts the full determinant
is a power of two, so no invariant factor contains an odd prime. This proves the
stated integral Smith factors, independently of finite matrix scans.

### FC-08: the universal causal repair planner

For any elapsed horizon `N>=0`, let `n>N` be the first start with
`n=2 mod3` and `n!=0 mod5`, and append observations at `n,n+1,n+2,n+3`.
The permitted start residues modulo fifteen are `2,8,11,14`; their largest
consecutive gap is six. Hence

\[
N<n\le N+6,\qquad n+3\le N+9.
\]

The delay-nine bound is attained, for example, at `N=2`. After `N=233`, the
planner appends `(236,237,238,239)`, producing one common source chart for all
odd primes. The history is preserved and future observations remain inaccessible
until their clocks elapse. If a suitable old consecutive block is already stored,
the observer may read it without reversing source time; the default planner here
chooses four fresh observations.

`row_denominator_lcms` exposes the row units, `cleared_cauchy_matrix` constructs
the integral matrix, and `plan_universal_repair` implements the future schedule.
This closes the prime-resolution construction gap for this four-source-channel
family; it does not fill the signed Weyl estimate.

**Paid real and seed costs.** Each row LCM grows as `Theta(n^4)`, since all common
denominator factors are bounded by the fixed pole differences. Thus an ordinary
real measurement error is multiplied by a growing row scale. The unscaled
Cauchy determinant still decays as `Theta(n^-16)` for consecutive clocks.
The constant cleared determinant is not a free increase in real knowledge volume
or a uniform real conditioning bound. The fifth seed-channel cost in FC-05 is
also retained. These common charts use the same source observations, so their
prime reductions are not independent random samples.

## 8. Proved leverage, remaining edge, and provenance

The new instrument has three concrete capabilities: it reconstructs source and
seed within a declared family from finite elapsed data, it identifies rather than
conceals prime-resolution failures, and it repairs them with either extra causal
observations or a quantified precision payment. These are observation theorems.

They do not rule out a locally locked moving observer. Such a frame is admissible
provided its compensating map and source anchor are retained. Agreement must then
transport the fixed signed Weyl probes to the source frame with a quantified error;
the source-selected all-late-shell cancellation or nonconcentration premise remains
open. Changing the schedule of source-identification probes never changes the
chronological clocks or signed weights in those fixed statistical targets.

The Cauchy determinant is classical algebra. The finite family construction and
prime repairs here were independently derived for this follow-up; a specific
external Claude artifact establishing the chat's determinant statement was not
located in the checked branch. No academic-priority claim is made. The source
contract is inherited from main `81be6b897ae980b801a3b9de9e22ef81e8360bfb`,
`docs/PI_NORMALITY_FRONTIER.md`. The distinct quartic Fibonacci observer is in
sibling #667, head `12287d565f383d7274e6b613f34010dba15a81f9`; this is a
source comparison, not a silent merge or transfer of that branch's tests.

**Executed focused validation:** `python .../five_channel/test_observer.py`
ran 30 tests successfully, including the retained-history follow-up, the
all-odd-prime polar repair, and the common bounded-delay repair. They include an independent
Leibniz determinant oracle, exact rational family and seed recovery, chronological
rejection of future probes, wrong-source and corrupted-state controls, a locked
source with the same full Jacobian, the erroneous eleven repair, polar seven
calibration, sharp underpaid-precision failures, and the all-odd-prime polar
construction at five primes and four horizons. The latter also checks the scaled
permutation reduction and rejects the insufficient clock depths at three and five.
The common chart checks include all-minor gcds for the Smith factors, both bad
start congruences, the sharp nine-tick delay, and a real measurement-unit control.
These finite checks support
the implementation; the universal assertions use the displayed proofs. Repository
validation and the signed-probe receipts are recorded separately by the root audit.

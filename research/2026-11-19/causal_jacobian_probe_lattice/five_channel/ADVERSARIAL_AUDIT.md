# Five-channel observer: adversarial audit

**Scope.** Paper deductions and exact finite checks of the observer construction,
not an external referee report and not a proof of a new all-shell bound for pi.
The inspected parent is `966f789b6523a4918b24e96fac7bc22cd791fb79` (draft #668).
The original forcing, literal zero seed and chronological Weyl average remain
the target. This audit also records corrections to terminology in the parent.

## 1. An actual source observer can be exactly stationary

Let

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
P_n=\sum_{j=1}^{n}16^{-j}r(j).
\]

For the whole same-forcing seed family, define the finite causal chart

\[
g_n(u)=16^{-n}u-P_n.
\]

It uses only the clock and the source prefix already available at time n. Direct
substitution proves, for every real u and every n >= 0,

\[
g_{n+1}(16u+r(n+1))=g_n(u),\qquad
g_n(U_n(s))=s.
\]

Thus **the actual literal-zero source is displayed as zero forever**. Its
transformed state Jacobian is
`16^(-n-1) * 16 * 16^n = 1`. The inverse chart is
`u = 16^n (g + P_n)`. This is not a change of the seed or forcing, and does not
require knowing pi in advance. Each finite stage uses finite rational registers;
their sizes need not remain bounded as n grows.

The observable must transform with the chart. The source-frame character becomes

\[
e(hu)=e\bigl(h16^n(g+P_n)\bigr).
\]

At the local state g=0 the entire chronological phase remains in the known chart
compensator. The completed character additionally retains the authentic tail
T_n. The exact chart identity proves agreement of the frames; it supplies no
bound on the compensated sum. This is a **positive control**: a validator must
accept this stationary local display while reproducing the source-frame phases.
Rejecting it for being locked would reject the original zero-seeded source.

For a fixed Fourier index h and every shell B, the existing tail estimate gives

\[
\left|\frac1B\sum_{n=B}^{2B-1}e(h(U_n+T_n))
-\frac1B\sum_{n=B}^{2B-1}e(hU_n)\right|
\le \frac{2\pi |h|}{15}r(B+1).
\]

This pays the finite-source/completed-source comparison. It does not make the
second sum small. A change of coordinates cannot replace that arithmetic step.

## 2. A nonsingular Jacobian is not global seed authentication

In the declared four-pole coefficient family, four innovations recover four
coefficients. Adding the **unwrapped** finite normalized state `16^-N U_N`
gives a block Jacobian with determinant equal to the four-by-four Cauchy
determinant. This is an exact identification statement in that five-parameter
family. The authentic source is one fixed member of the family, not a random
draw from its volume.

Two guards are necessary:

1. The same Jacobian is present at the hostile seed `s=-pi/16`, where the
   completed orbit is exactly zero. Determinant nonvanishing cannot imply
   statistical cancellation. The original-zero predicate must be checked using
   the fifth channel and the source prefix.
2. If the fifth channel is replaced by `e(U_N)` or `e(U_N+T_N)`, seeds differing
   by an integer multiple of `16^-N` alias. A nonzero derivative gives local
   identifiability, not global authentication. In particular, the rational seed
   `1/16` aliases all later completed phases, although its source passport is
   different. Retain the integer lift or an exact zero-seed certificate.

Four innovations identify coefficients only under the stated four-pole family
restriction. They do not identify an arbitrary infinite source from four samples.
Known finite-prefix counterfeit sources remain outside this family and must not
be silently certified as authentic by the coefficient fit alone.

The Cauchy determinant is a volume in declared coefficient and measurement
coordinates. Rescaling a measurement changes it. Interpreting it as a knowledge
volume therefore requires a declared error metric or volume convention. The
schedule `(55,89,144,233)` also waits longer than `(55,56,57,58)`. Its determinant
gain does not come with equal latency. More generally, any four clocks with
distinct positive proportional limits have the same `n^-10` exponent; Fibonacci
provides a natural schedule, not a unique optimality theorem. The five-parameter
source/seed chart must also be distinguished from #667's five quartic readouts
of a two-dimensional Fibonacci state: the latter's ordinary derivative has at
most rank two, despite having five output coordinates.

## 3. Prime-resolution repair must distinguish poles from rank loss

Let `C_ij = 1/(8 m_i-d_j)` with `d=(7,4,3,2)`. Reduction modulo p is defined
without normalization only when every displayed denominator is a p-unit.

### The proposed modulo-11 repair has a precise failure mode

The clocks `(55,89,144,233)` reduce modulo 11 to `(0,1,1,2)`. All four pole
locations are avoided, but the rows at 89 and 144 coincide, so the rank is 3.
Replacing **233** by **147** gives residues `(0,1,1,4)` and leaves the rank 3.
The missing distinction was the duplicated row at 144, not the last row.

Replacing 144 by 147 produces four distinct admissible residues and rank 4,
but an observer noticing the failure only after time 233 cannot make a new
measurement at time 147. It may use that value only if a sufficient historical
journal was retained. A direct forward repair appends time **235**, with residue
4, and uses `(55,89,233,235)`. The Cauchy determinant proves rank 4 modulo 11.
This changes the source-identification schedule, not the Weyl sample population.

### A pole-free modulo-7 repair loop cannot terminate

Modulo 7, the four numbers `d_j` are distinct, and 8 is a unit. There are exactly
four forbidden clock residue classes `8m=d_j`. Only three nonpolar classes
remain. Every ordinary nonpolar Cauchy row depends only on its clock class.
Therefore **no collection of ordinary pole-free rows can have rank 4 modulo 7**.

This is a genuine obstruction to the particular repair algorithm, not to
p-adic recovery. A correct implementation must instead retain valuations and
polar normalization, request sufficient additional p-adic digits, or use a
different justified observation. For example, for p=7 one can choose a clock
near each of the four distinct poles and multiply that row by the largest
denominator power of 7. Its reduction has exactly one nonzero coordinate, giving
four independent normalized rows. At p=3 or 5 some pole locations coincide
modulo p; a deeper clock congruence or a paid measurement-precision refinement
separates these collisions. At p=2, 8 is not a unit and the preceding clock-class
argument must not be reused.

The deterministic audit case is to attempt rank recovery at p=7 using only
nonpolar rows: the algorithm must report the obstruction, not loop forever,
silently divide by zero, or manufacture an inverse.

### The subsequent all-odd-prime repair theorem survives the audit

The root's stronger construction resolves the small odd-prime collisions as
well. For an odd prime p, set

\[
a_p=1+\max_{j<k}v_p(d_j-d_k).
\]

For the specified pole labels this is 2 at p=3,5 and 1 at every other odd prime.
After any integer horizon N >= 0, choose for each j the first integer m_j > N
with `8m_j=d_j mod p^a_p`. Since 8 is a unit and the labels are distinct modulo
`p^a_p`, these are four distinct clocks in `(N,N+p^a_p]`. Let
`e_j=v_p(8m_j-d_j)>=a_p`. For k unequal to j,

\[
v_p(8m_j-d_k)=v_p(d_j-d_k)<a_p\le e_j.
\]

The equality uses the strict ultrametric inequality; it is not an assumption
that the first denominator has exactly valuation a_p. Consequently multiplying
the row by `p^e_j` leaves a nonzero unit only in column j modulo p. Sorting the
clocks chronologically merely permutes these rows. The normalized chart has
unit determinant and zero innovation inverse loss. The denominators are never
literally zero because m_j is a positive integer and `d_j<=7`.

This is a constructive future-observation theorem for every odd prime. It does
not bound all-prime costs simultaneously, erase raw precision scales, remove the
fifth seed channel's cost, or prove anything about the chosen phases' frequency.
The implementation requires a nonempty positive clock history, so its API starts
at N >= 1; the elementary existence proof also covers N=0.

At p=2 the proposed construction has a real boundary: 8 has no inverse.
For every positive m the row-normalization exponent is exactly 2, and

\[
\left(\frac4{8m-7},\frac4{8m-4},\frac4{8m-3},\frac4{8m-2}\right)
\equiv(0,1,0,0)\pmod2.
\]

Additional clocks of this normalized type cannot change its one-digit rank.
Higher binary precision, with its explicitly paid inverse cost, remains valid.

### Stronger universal repair: one integer chart for all odd primes

The subsequent root proposal also survives the audit. Take four consecutive
clocks `n,n+1,n+2,n+3`, clear row i by
`L_i=lcm_j(8m_i-d_j)`, and set `B=diag(L_i) C`. This is an integer matrix.
For any positive integer clock m, the exact repeated denominator factor is

\[
\frac{\prod_j(8m-d_j)}{\operatorname{lcm}_j(8m-d_j)}
=2\,3^{\mathbf1_{m\equiv2\ (3)}}5^{\mathbf1_{m\equiv4\ (5)}}.
\]

**Proof.** At 2, the four denominator valuations are always `(0,2,0,1)`,
whose sum minus maximum is one. At 3, only the pole labels 7 and 4 coincide,
precisely at `m=2 mod3`; their difference is 3, so their minimum valuation is
exactly one. At 5, only labels 7 and 2 coincide, at `m=4 mod5`; their difference
is 5. No other prime divides any pairwise pole-label difference. This accounts
for every common denominator factor, including arbitrarily deep individual
poles.

The consecutive-clock Cauchy numerator is `2^23 * 3^2 * 5`. Four rows contribute
a factor `2^4`; exactly two contribute a factor 3 if `n=2 mod3`, otherwise one;
exactly one contributes a factor 5 unless `n=0 mod5`. Therefore, for every n >= 1,

\[
\det B=2^{19}\,
3^{\mathbf1_{n\not\equiv2\ (3)}}
5^{\mathbf1_{n\equiv0\ (5)}}.
\]

In particular, starts `n=2,8,11,14 mod15` give determinant exactly `2^19`.
The single chart is then invertible over every `Z_p` for odd p, simultaneously.
Its integer Smith form is

\[
\boxed{\operatorname{diag}(1,4,64,2048).}
\]

Here is an independent general proof of the binary Smith exponents, rather than
an extrapolation from tested starts. Each `L_i/4` is odd, so the binary Smith
invariants equal those of `4C`. For a k-by-k minor with row clocks I and pole
labels J, the Cauchy formula gives valuation

\[
2k+3\binom{k}{2}+v_2(\Delta(I))+v_2(\Delta(J))
-k\sum_{j\in J}e_j,\qquad e=(0,2,0,1).
\]

The minimum row-Vandermonde valuations for k=1,2,3,4 are `(0,0,1,2)` for any
four consecutive integers. Enumerating the fixed four pole labels gives minimum
column contributions `(−2,−5,−8,−9)`. Thus the valuations of determinantal
divisors, including order zero, are `(0,0,2,8,19)`. Successive differences give
Smith exponents `(0,2,6,11)`. Since the full determinant has no odd factor at an
admissible start, these binary valuations determine the full integer Smith form.

The largest gap between the permitted start classes modulo 15 is six. Choosing
the first admissible start strictly after N therefore completes all four
observations by `N+9`. The bound is attained when N itself lies in the start
class 2 modulo 15. This gives a constant-delay repair at all odd primes, without
preselecting a finite prime inventory. The normalized binary innovation inverse
cost is eleven digits; the seed channel remains a separate obligation.

The unrestricted determinant formula supplies hostile controls: n=1 retains an
odd factor 3; n=5 retains an odd factor 5; n=15 retains both. A validator must not
apply the all-odd-prime conclusion to these starts. The independent script checks
the integer gcds of every minor for admissible and inadmissible starts.

**Measurement units remain load-bearing.** The row multipliers `L_i` grow like
`n^4`; they rescale raw real measurement errors. Constant integer determinant and
odd-prime unit behavior do not imply uniform real conditioning, cost-free extra
information, a five-channel isometry including the seed, or a signed Weyl bound.
This is a universal arithmetic observation theorem in the declared source family.

### Final strengthening: the full cleared-innovation lattice already closes

[BINARY_CLOSURE.md](BINARY_CLOSURE.md) proves that every integer-clock cleared
row `b_m` is an **integer** combination of any admissible four-row basis `B_*`.
The proof first turns `4C_m` into an integer polynomial vector of degree three
by an odd multiplier. Newton interpolation gives closure over `Z_2`. The
power-of-two determinant gives dyadic rational inverse coefficients, and
`Z[1/2] intersect Z_2=Z` upgrades those coefficients to integers.

Consequently a fixed uniform-modulus transcript of all cleared innovations
gives exactly the coefficient fiber already fixed by the four basis reports.
Its binary Smith exponents `(0,2,6,11)` impose an optimal eleven-digit worst-case
inverse cost even if indefinitely many more reports of this same type are added.
An explicit integer ambiguous coefficient vector is retained in the independent
receipt. This plateau is confined to the cleared-innovation family with arbitrary
coefficients and uniform exact congruences. A known seed plus the fifth terminal
channel, stronger coefficient priors, different observables or nonuniform
precision can provide further information. No plateau of the full observer or
of the real temporal phase is asserted.

## 4. The two proposed lag probes have a 255-point blind subgroup

For an original source state, the corrected lag character at (ell,h) is the
character of `K U_n`, where `K=h(16^ell-1)`. For the proposed pairs,

\[
K_{4,11}=720885,\qquad K_{6,7}=117440505,\qquad
\gcd(K_{4,11},K_{6,7})=255.
\]

Consequently their joint character map has the exact kernel
`(1/255) Z/Z`. The witness `u=1/255` gives `K_1 u=2827` and `K_2 u=460551`,
so both characters equal 1. The lag-one character detects it because
`15u=1/17` is not integral.

The parent observation that the **full bank containing every lag** has a
15-point kernel is correct: `gcd_{ell>=1}(16^ell-1)=15`. It does not give a
15-point kernel to this two-probe sub-bank. An anchored h=1 source character
removes both blind subgroups. The five-channel source observer and this fixed
bank must not be identified with one another merely because their dimensions or
labels resemble the Fibonacci construction.

Further, every squared distance `||K u||_T^2` identifies u and -u. Therefore an
exact statement about the kernel of the signed character bank is not a complete
identifiability statement about its unsigned energy readout. Keep signed complex
characters in the recorded data.

## 5. Separating points with h=7 and h=11 does not separate probability laws

The identity `8*7-5*11=1` indeed gives
`e(u)=e(7u)^8 e(11u)^(-5)` pointwise. It does not express the mean of e(u) in
terms of the two individual means. A decisive counterexample is

\[
d\mu(u)=(1+2a\cos(2\pi u))\,du,\qquad 0<a\le 1/2.
\]

This is a probability measure with Fourier coefficients
`mu_hat(7)=mu_hat(11)=0` but `mu_hat(1)=a`. Its nonzero first coefficient
survives despite perfect vanishing of both tested marginal means. A fixed finite
Fourier bank can falsify selected proposed bounds; it cannot certify all-mode
normality. Signed joint moments or an independently justified complete criterion
would be required for that promotion.

## 6. Causal adaptation cannot quietly change chronological sampling

Prime-resolution repair may depend on the clock, denominator valuations and
previously paid source data. It may request more precision or wait for another
innovation. The target Weyl sum still includes **every original clock** in
`[B,2B)`. A protocol that counts only its accepted “go” events changes the
empirical law.

For example, selecting from a normal radix orbit only phases in
`[-1/6,1/6] mod 1` gives accepted samples with real part at least 1/2. Their
normalized mean cannot tend to zero; equidistribution gives the nonzero limit
`3 sqrt(3)/(2 pi)`. A perfectly normal source can therefore fail a
phase-selected Weyl test. A deterministic phase-independent prime schedule
also does not automatically justify replacing chronological averages by a
subsequence: that requires its own theorem.

If m out of B target clocks are missing, and the remaining average is normalized
by its actual number of terms, its discrepancy from the full average is at most
`2m/B`. This follows by splitting the complete sum into retained and omitted
terms, each of modulus at most one. Thus an explicit `m=o(B)` payment suffices
for transporting convergence. A fixed positive missing fraction does not.

The source-control log must distinguish physical source time, internal probe
actions, precision refinements, and accepted reports. Revisiting a retained
historical value is an action at the present time, not a reversed source tick.

## 7. Infinite recurrent separation is still weaker than a shell saving

Take the computable irrational

\[
\beta=\sum_{j\ge1}16^{-j!}.
\]

For k >= 4, use `B=2 k!`. For all `B <= n < 2B`, every digit term up through
k! has become integral, while the first future term is at `(k+1)!`. Hence

\[
0<\{16^n\beta\}
\le \frac{16}{15}16^{4k!-1-(k+1)!}\longrightarrow0
\]

uniformly across those shells. Consequently `Re W_B(1) -> 1` along this
subsequence. Nonetheless at clocks `(k+1)!-1` the fractional part tends to 1/16,
so a positive phase-separation limsup persists. This is the existing cold-shell
countermodel of #667, restated to guard the new observer. More resolution or a
nonzero Jacobian does not upgrade a limsup to positive lower shell density.

## 8. Terminology and inherited spectral certificates

- For linear P and G, `G ker P subset ker P` is the quotient-descent criterion.
  Equality follows when both G and its descended map are invertible; ambient
  invertibility alone is insufficient in infinite-dimensional spaces. For
  nonlinear maps use the full fiber condition. A pointwise differential-kernel
  condition alone need not give global descent: `P(x)=x^2`, `G(x)=x+1` is a
  counterexample away from zero. Preserving a quotient is also distinct from
  preserving the numerical report, which would require `P G=P`.
- The formula `J_n^G=G_(n+1) J_n G_n^-1` is for linear coordinate changes.
  Nonlinear coordinate changes require their derivatives evaluated at the
  corresponding points. A derivative is not defined by a discrete time label.
- The source-corrected lag residual is an exact algebraic observable. Calling it
  “holonomy” is only shorthand unless a connection and its closed transport
  path have been specified; no geometric curvature is certified by that word.
- The characteristic polynomial of `T=Sym^4(A^2)` is inherited from #667.
  The comparison at the scalar 16 is a further calculation. Prime 29 is an
  additional spectral comparison, not an “out-of-source” prime: the original
  BBP denominators also contain 29.
- The parent sheet argument concerns a projected/accumulated spatial pulse
  response. It does not by itself identify its operator with the original
  chronological BBP update. A constant-mode match modulo 7 is not a real
  source-phase intertwiner.

## 9. Executed checks and minimum mutation controls

At the inspected parent head, the two stdlib commands

```
python research/2026-11-19/causal_jacobian_probe_lattice/probe.py
python research/2026-11-19/causal_jacobian_probe_lattice/sheet_probe.py
```

both exited zero during this audit. The printed order for p=29 was `(7,7)`;
the parent script computes it but did not assert that particular expected value.
These are finite exact checks. They do not numerically certify the completed
cosine/tail inequality or prove its open all-shell premise.

A separate SymPy characteristic-polynomial/determinant calculation returned
`X^5-55X^4+385X^3-385X^2+55X-1` and
`det(16I-T)=-1076625`. A direct finite-field obstruction independently checks
the fixed-eigenvalue nonlift. With `B=T-16I`,

```
ell = (4,2,10,10,1)
ell B / 11 = (7,30,18,0,1)
v = (4,6,9,8,1)^T
B v = 0 mod 11
(ell B / 11) v = 8 mod 11
```

If a lift `ell+11w` existed modulo 121, its equation would give
`w B = -ell B/11 mod11`. Multiplying by v contradicts `0=-8 mod11`.
The rank-four condition says every primitive modulo-11 eigenrow is a nonzero
multiple of ell, so the same obstruction excludes all primitive lifts of the
fixed eigenvalue 16. It does not exclude a varying 11-adic eigenvalue.

The new implementation's minimum mutation suite should kill:

1. Omitted compensation in the exact stationary causal chart.
2. Replacing the unwrapped anchor by a wrapped phase, admitting the 1/16 alias.
3. Replacing clock 233 by 147 while leaving the duplicated modulo-11 rows.
4. A nonterminating pole-free full-rank repair at p=7.
5. Treating the two selected lag characters as having only a 15-point kernel.
6. Replacing signed complex responses by squared distances and claiming full
   identifiability.
7. Inferring the h=1 mean from vanishing h=7 and h=11 means.
8. Filtering chronological samples through a phase-dependent “go” rule.
9. Relabelling the factorial-sparse cold-shell control as an R0 success.

### Independent implementation audit of the new finite instruments

`independent_audit.py` executed successfully and wrote
`receipts/independent_audit.json`: **2,313 exact finite checks** after extension
for the universal repair and full clock-row closure (earlier versions had 201,
1,180 and 1,709). It uses different
implementations of the load-bearing finite steps:

- Determinantal-divisor minima over all square minors verify the normalized
  ranks and inverse precision losses at six primes for the original and repaired
  schedules, without using the observer's Gaussian inverse to calculate the
  expected answer.
- The combined rational BBP forcing verifies exact stationary-chart identities
  and source-prefix index positions against the observer's four-term forcing.
- A full-angle degree-40/41 Taylor enclosure with a BBP-derived pi interval
  checks 12 table nodes and seven signed means against the Weyl instrument's
  Machin-derived, quarter-wave degree-24/25 table. These are exact rational
  comparisons, not floating-point agreement.
- Seven positions `n=1,2,3,7,16,31,40` confirm that `Y_n=16^(n-1) pi` uses
  `prefix[n-1:n-1+width]`, by independently enclosing `U_n+T_n` and the scaled
  BBP pi interval in the same hexadecimal cell.
- Explicit incorrect controls distinguish omitted compensation, a wrapped seed
  alias, an off-by-one digit index, and reversed Fourier sign.
- A separate exhaustive search of each finite future clock window checks the
  new repair at eight odd primes and eight horizons. It verifies the bound,
  distinct clocks, singleton normalized row support, and a unit determinant.
  The deliberately hostile case p=3, N=29524 has actual pole depths
  `(10,2,2,2)` despite prescribed depth 2; it still produces the asserted unit
  chart. Ten binary clock cases and a rejected binary repair calibrate the
  separate p=2 boundary.
- The integer universal repair is checked at 36 starts, including every residue
  class, large clocks, and inadmissible starts retaining factors 3 or 5. Integer
  gcds of every square minor verify the full Smith invariants. A separate
  residue-class search verifies 48 adaptive plans and observes the sharp
  nine-tick completion bound. Neither computation replaces the general proofs
  above.
- A separate adjugate inverse checks 264 all-clock integer-row closure cases
  across four universal bases. Every integer coefficient vector reconstructs
  its target row exactly. An explicit coefficient difference has an odd
  coordinate while all 66 tested cleared reports vanish modulo `2^11`,
  calibrating the sharp innovation-only precision boundary.

The quarter-table error payments have also been checked on paper: cosine through
degree 24 has remainder at most `2^25/25!` on the represented quarter; sine
through degree 25 has a smaller bound. Replacing pi costs at most `perr/2` in
the argument, and integer table rounding costs at most `1/scale`. A grid cell
costs at most `44/(7Q)` per component, and an h-fold width-k hexadecimal phase
interval costs at most `44|h|/(7*16^k)`, using `2pi<44/7`. All signs and quarter
symmetries were retained. No fresh-shell result was used to construct this audit.

**Verdict.** Finite causal source identification, precision accounting and
cross-frame agreement are genuine local proof steps. Agreement is compatible
with permanent local lock and with nonnormal source controls. The remaining
source-selected signed shell estimate is not supplied by these steps. The next
verdict-changing result must bound a complete compensated chronological
statistic of the original source, with its uniform quantifiers and approximation
costs explicit.

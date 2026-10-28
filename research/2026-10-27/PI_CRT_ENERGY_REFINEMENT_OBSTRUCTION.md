# CRT energy: a refinement obstruction and a normal counterexample

Research lane A, 2026-10-27. Read-only derivation against parent SUCC commit
`fca58d3e0289e57596dd8ca74bace325a450df31` (PR #324). This dossier adds no
claim of pi normality, no new Lean authority, and no external novelty claim.
The calculations below are paper proofs; the finite checks are corroboration.

## Hole contract and verdict

**Attempted sufficient inequality.** For the authentic four-pole source,
`U_0=0`, `U_n=16U_(n-1)+r(n)`, prove for each fixed nonzero integer h that

$$E_{N,M}(h)=\frac{M}{N^2}\sum_{t=0}^{M-1}\left|\sum_{1\le n\le N,\ n\equiv t\ (M)}e(hU_n)\right|^2\to0,$$

for a specified admissible schedule `M=16^k 3^L=o(N)`. This would imply the
required Weyl estimate. The hypothesis is currently **OPEN** for authentic pi.

**Rival frames.** A: finer exact arithmetic labels create a cancellation
advantage. B: finer labels retain additional conditional phase bias, which is
nonnegative in this energy. The exact refinement identity below proves B and
refutes A as a purely partition-theoretic mechanism. A new signed arithmetic
input could still prove the gate.

**Decisive new obstruction.** There is an explicitly specified base-16 normal
real alpha and a monotone schedule `M(N)=3*16^k=o(N)`, tending to infinity, such
that `limsup E_alpha(N,M(N),h)=1` for every fixed integer h (including every
nonzero h). Thus a prescribed growing-modulus energy gate can require strictly
more uniformity than normality. An existential sufficiently slow schedule is
instead equivalent to normality; the distinction is essential.

Theorem E5 strengthens this to every prescribed schedule tending to infinity
and o(N). Theorem E6 then supplies, for every such schedule, **one normal
finite-type carrier** with eventual `|alpha-p/q|>=2^(-10)q^(-6)` and
`liminf_j E_alpha(4^j,M(4^j),h)>=1/4` for every fixed h. Its irrationality
exponent lies between 4 and 16/3. E6 therefore removes the Liouville
limitation of E4/E5; positive energy, rather than maximal energy, is retained.

The subsequent [Theorem E7](PI_NORMAL_FINITE_TYPE_ENERGY_OBSTRUCTION.md)
strengthens the exponent bound to `mu(alpha)<=4`, retaining energy lower
limit 1/4 at N=2^j, by an exact finite-word second-moment selection. E6
remains useful as the simpler explicit-marker construction.

**Novelty boundary.** The identities are classical conditional-expectation
algebra, applied to the proposed SUCC source clock. The counterexamples give a
strict implication obstruction absent from a mere rewriting of Weyl's test.
It is a normal-number counterexample to necessity of growing energy decay,
not a counterexample to authentic BBP cancellation.

## 1. Definitions, arithmetic labeling and exact conditional variance

Let `N,M>=1`, let `z_1,...,z_N` satisfy `|z_n|<=1`, and set

$$C_t=\{1\le n\le N:n\equiv t\pmod M\},\quad c_t=|C_t|,
\quad S_t=\sum_{n\in C_t}z_n,\quad \mu_t=S_t/c_t$$

when `c_t>0`, with empty classes contributing zero. Define

$$E_M(z)=\frac M{N^2}\sum_t|S_t|^2,
\qquad Q_M(z)=\frac1N\sum_t c_t|\mu_t|^2.$$

`Q_M` is the squared norm of the empirical conditional mean of z given time
modulo M. The exact authentic CRT labels in #321--#322 are bijections of this
same time partition. Consequently their full character energy is unchanged
by replacing them with ordinary residue labels: no part of the source-specific
permutation remains in the full squared norm, except in the real phases z.
This is a statement about the full energy, not individual mixed characters.

**Theorem E1 (PROVED).** If `M|M'`, then

$$Q_{M'}(z)-Q_M(z)=\frac1N\sum_{s\bmod M'}c_s
   |\mu_s-\mu_{s\bmod M}|^2\ge0.$$

The parent mean is the c-weighted average of its child means. Expanding the
squared difference, the cross term in each parent is zero because
`sum_child c_s(mu_s-mu_parent)=0`. This proves the formula with arbitrary
complex z and arbitrary unbalanced end classes.

Furthermore,

$$|E_M(z)-Q_M(z)|\le\frac MN.$$

Indeed `E_M=sum_t (c_t/N)(M c_t/N)|mu_t|^2`, while
`|M c_t/N-1|<=M/N`, because `c_t` is floor or ceiling of `N/M`. Sum the
weights `c_t/N=1` and use `|mu_t|<=1`. If `M|N`, then `E_M=Q_M` exactly.
Thus, if `M'|N`, refinement increases E exactly; in general it increases E
up to at most `(M+M')/N` endpoint error. Refining nested admissible conductors
cannot furnish a source-free decrease in the gate energy.

The coarsest partition has `E_1=Q_1=|N^-1 sum_n z_n|^2`. A concrete control is
`z_n=(-1)^n` with even N: `E_1=0` and `E_2=1`. Conditioning can retain all of
the coherent components whose sum originally canceled.

For later use, writing `N=qM+r`, `0<=r<M`, gives

$$E_M(z)\le\frac M{N^2}\sum_t c_t^2
=1+\frac{r(M-r)}{N^2}\le1+\frac{M^2}{4N^2}.\tag{1}$$

The first inequality uses `|S_t|<=c_t`. Equality in the first bound occurs
whenever z is a unit-modulus periodic sequence of period dividing M.

## 2. Energy stability and source-authentic Green transport

**Theorem E2 (PROVED).** For two sequences z,w of moduli at most one and
`D=sum_(n<=N)|z_n-w_n|`,

$$|E_M(z)-E_M(w)|\le
\frac{2M\lceil N/M\rceil}{N^2}D
\le\frac2N\left(1+\frac MN\right)D.\tag{2}$$

For each class, `||S_t|^2-|R_t|^2|<= (|S_t|+|R_t|)|S_t-R_t|
<=2c_t sum_(n in C_t)|z_n-w_n|`. Sum and use `c_t<=ceil(N/M)`.
This bound permits M to vary with N and tracks every dependence.

Use the source-exact identity inherited from #323:

$$U_n=16^{n-1}\pi-T_n,\quad T_n>0,
\qquad\sum_{n\ge1}T_n=B=(R-\pi)/15.$$

With `z_n=e(hU_n)`, `w_n=e(h16^(n-1)pi)`, the elementary real-circle bound
`|e(x)-e(y)|<=2pi|x-y|` yields `D<=2pi |h| B`. Therefore

$$\boxed{|E_U(N,M,h)-E_\pi(N,M,h)|
\le\frac{4\pi |h|B}{N}\left(1+\frac MN\right).}\tag{3}$$

This is source-authentic and uniform in M, without exponentially large lag
coefficients. In particular, whenever `M=o(N)`, the two energies differ by
`O_h(1/N)`. The finite CRT character transform cannot hide the selected real
radix obstruction in this norm.

For the same-forcing changed-seed orbit `V_n=-T_n`, comparison with w=1
shows `E_V(N,M,h)->1` for every `M=o(N)`. The same conclusion holds for
#320's zero-seeded non-BBP mutant `U_n^*=16^n-T_n^*`, where

$$T_n^*=\frac{n+1}{(2n+1)(4n+1)(8n+1)},\quad
C_*:=\sum_{n\ge1}T_n^*<\infty.$$

Use (2), `D<=2pi |h| C_*`, and (1). Summability is immediate, for example
`T_n^* <= 1/(32n^2)` for `n>=1`, since `n+1<=2n` and the denominator is at
least `64n^3`. These conclusions are uniform over every admissible schedule
`M=o(N)`; neither countermodel relies on choosing a favorable subsequence.
They remain controls, not changes to the authentic source.

An equivalent autocorrelation identity, useful for probes but not a new
estimate, is

$$E_U(N,M,h)=\frac MN+
\frac{2M}{N^2}\Re\sum_{j=1}^{\lfloor(N-1)/M\rfloor}
\sum_{n=1}^{N-jM}e(h(U_{n+jM}-U_n)).\tag{4}$$

Its completed radix frequencies are `h(16^(jM)-1)`, which grow rapidly.
Replacing each correlation by its completed version has total energy error
at most `8pi |h| B/N`, by summing at most `N/M` individual `4pi|h|B`
transport errors. Formula (3) is the sharper direct route. Fixed-frequency
Weyl information gives no uniform estimate for the moving frequencies in (4).

## 3. Fixed, existential and prescribed moduli are distinct statements

Write `E_alpha` for the energy of `e(h16^(n-1)alpha)`.

**Theorem E3 (PROVED).** The following are equivalent:

1. alpha is normal to base 16.
2. For one fixed positive integer M, `E_alpha(N,M,h)->0` for every fixed
   nonzero integer h.
3. For every fixed positive integer M the same convergence holds.
4. There exists a monotone schedule `M(N)=3*16^j`, tending to infinity and
   `o(N)`, for which the same convergence holds for all fixed nonzero h.

(2) or (4) implies (1) by Cauchy--Schwarz:
`|N^-1 sum_n e(h16^(n-1)alpha)|^2<=E_alpha`, followed by Weyl's criterion.
Statement (3) implies (2).

For (1) implies (3), we give the usual normality-under-block-grouping argument
in measure form to avoid assuming independent lag coordinates. Put `T(x)=16x
mod1`. If the full orbit is Haar-generic, take any subsequential weak limits
`nu_0,...,nu_(M-1)` of its M residue-subsequence empirical measures (joint
subsequence selection is possible by compactness). Each `nu_t` is
`T^M`-invariant by endpoint telescoping, and their average is Haar. Positivity
then gives `nu_t<=M Haar`, so each has an L1 density. Invariance gives
`nu_t_hat(k)=nu_t_hat(16^(Mj) k)` for every j. The Riemann--Lebesgue lemma
forces these coefficients to zero for each nonzero integer k. Thus each
`nu_t` is Haar, and all subsequential limits are Haar. Each of the finitely
many residue means tends to zero, proving (3). This also proves the familiar
base-16/base-16^M normality equivalence needed here.

For (3) implies (4), set `M_j=3*16^j`. Choose increasing integer thresholds
`K_j` so large that for all `N>=K_j` and all `1<=|h|<=j`,
`E_alpha(N,M_j,h)<=1/j`, and additionally `M_j/K_j<=1/j`.
Existence follows from finitely many convergent fixed-M sequences at each j.
Set `M(N)=M_j` on `K_j<=N<K_(j+1)`, with an arbitrary admissible initial
value. This proves (4). The thresholds need not be effective; this diagonal
argument is an equivalence, not a source-specific cancellation proof.

**Boundary:** E3 does not give decay along an independently prescribed
schedule. The next theorem shows such uniformity is genuinely stronger.

## 4. Explicit normal number with maximal moving residue energy

For each `j>=1`, let W_j be the lexicographically least cyclic de Bruijn word
of order j on digits `{0,...,15}`, represented as the least word among all
rotations of all such cycles. This completely specifies a finite word of
length `d_j=16^j`. A de Bruijn cycle exists: take an Euler circuit in the
directed graph whose vertices are (j-1)-digit words and whose edges are
j-digit words, with prefix/suffix incidence. Every vertex has equal in/out
degree 16 and the graph is strongly connected. An Euler circuit spells the
cycle. For every `1<=r<=j`, every r-word appears exactly `16^(j-r)` times
among the cyclic starting positions of W_j.

Set

$$M_j=3\cdot16^j,\quad q_j=16^{j^3},\quad
L_j=q_jM_j,\quad N_j=\sum_{i=1}^j L_i,\quad N_0=0.$$

Let stage j consist of `3 q_j` copies of W_j, and let alpha in `[0,1)` have
hexadecimal expansion given by the infinite concatenation of these stages.
This definition is explicit, even though the stages grow too rapidly for a
large numerical experiment. It does not invoke pi or the BBP forcing.

**Theorem E4 (PROVED).** This alpha is normal to base 16, while for every
fixed integer h,

$$E_\alpha(N_j,M_j,h)\longrightarrow1.\tag{5}$$

Consequently a monotone schedule `M(N)=M_j` for `N_j<=N<N_(j+1)` (with
`M(N)=M_1` before `N_1`) is `o(N)` and tends to infinity, but

$$\limsup_{N\to\infty} E_\alpha(N,M(N),h)=1.\tag{6}$$

### All-prefix normality proof

Fix a word v of length r. For every stage i>=r, its infinite periodic
continuation has exact v-frequency `16^-r` over each complete period
`d_i=16^i`. In any prefix of that periodic sequence, the discrepancy in the
number of v-starts from `16^-r` times its length is at most `d_i`: delete the
complete periods and bound the remaining partial period. In the actual
concatenation, only the last `r-1` starting positions of a completed stage can
have a different r-word from the periodic continuation. At a prefix ending
inside the current stage, either count only complete r-words, or pay another
`r-1` endpoint positions. Both conventions have the same limiting frequency.

The finitely many stages i<r contribute a constant `C_r`, independent of N.
If N is in stage j>=r, the total discrepancy is bounded by

$$C_r+\sum_{i=r}^j16^i+2rj.
\tag{7}$$

For j tending to infinity, `N>=N_(j-1)` (apart from an immaterial endpoint
convention), and

$$\frac{16^j+j}{N_{j-1}}
\le\frac{16^j+j}{3\cdot16^{(j-1)^3+j-1}}\longrightarrow0.$$

Thus (7)/N tends to zero at every prefix, not just stage endpoints. Every
finite hexadecimal word has its correct limiting frequency. Alpha is normal.

### Energy proof and explicit finite error

Let beta_j be the real with purely periodic hexadecimal expansion W_j. Let
`w_n` be the corresponding unit phase `e(h T^(n-N_(j-1)-1) beta_j)`, with
negative exponents interpreted by the periodic orbit, so that w is defined
for all integers n and has period dividing `d_j`, hence dividing M_j.
For n in stage j, the actual alpha orbit and this periodic orbit share all
remaining stage digits. Except for the final j starting positions of the
stage, they share at least j digits, so their real coordinates differ by at
most `16^-j`. Their phases therefore differ by at most
`2pi |h| 16^-j`. On earlier stages and on the final j positions use the
universal difference bound 2. For `N=N_j`,

$$D_j:=\sum_{n=1}^{N_j}|e(hT^{n-1}\alpha)-w_n|
\le2N_{j-1}+2j+2\pi |h|N_j16^{-j}.\tag{8}$$

Because w is unit-modulus and M_j-periodic, its energy is exactly
`1+r_j(M_j-r_j)/N_j^2`, where `r_j=N_j mod M_j`, and hence at least one.
Apply (2) to (8):

$$E_\alpha(N_j,M_j,h)\ge1
-4\left(1+\frac{M_j}{N_j}\right)\frac{N_{j-1}+j}{N_j}
-4\pi |h|\left(1+\frac{M_j}{N_j}\right)16^{-j}.\tag{9}$$

Here `M_j/N_j<=16^(-j^3)` and `N_(j-1)/N_j->0`: indeed
`N_(j-1)<=3(j-1)16^((j-1)^3+j-1)` whereas
`N_j>=3*16^(j^3+j)`. Every error term in (9) tends to zero. Bound (1) gives
the matching upper limit one, proving (5).

For the schedule above, `M(N)/N<=M_j/N_j->0` on each interval
`[N_j,N_(j+1))`. Formula (5) yields limsup at least one, while (1) yields
limsup at most one, proving (6). No independent-product-Haar target was used.

### Exact-forcing changed-selector corollary

Keep the original four-pole forcing and the original Green tails, but set
`V_0=(alpha-pi)/16`, where alpha is the explicit normal real above. Then

$$V_n=16^{n-1}\alpha-T_n$$

satisfies the exact original recurrence. Its real-circle empirical distribution
is Haar by summable Green transport and normality of alpha, yet (3), with pi
replaced by alpha on both completed and changed-seed sides, gives
`E_V(N_j,M_j,h)->1`. Thus this obstruction is compatible with the exact forcing
on a changed real selector, even when that selector is normal. It does not
refute the desired estimate at `U_0=0`. No 2-adic state value is assigned to
this possibly irrational V; the energy uses time residues (or, equivalently,
the authentic zero-source CRT clock used as external time labels).

## 5. Controls, finite corroboration and next proof obligation

An independent standard-library Fraction calculation checked:

- all 340 relevant cyclic word counts for binary de Bruijn orders 1--4 and
  hexadecimal de Bruijn orders 1--2;
- 8,100 exact refinement identities, `|E-Q|<=M/N`, balanced equality and the
  upper bound (1), over all sign sequences of lengths 2--10 and nested
  partition pairs `1->2`, `1->3`, `2->4`, `3->6` where applicable;
- 7,532 of those refinements strictly increased Q;
- the mutation/negative witness `(1,-1)^16`, with `E_1=0`, `E_2=1`.

These checks validate the instrument over the stated finite cases. The
universal statements and normality of the constructed alpha follow from the
proofs, not from finite enumeration. No actual huge stage or pi-normality
experiment was claimed.

**Next verdict-changing obligation.** Specify a schedule in advance and prove
an authentic-source bound on the signed progression correlations in (4),
uniform over its complete moving frequency range, or prove the corresponding
conditional means vanish directly. Such a bound must use more than exact CRT
permutations, source tail summability, and ordinary fixed-frequency normality.
If only a fixed M or an existential arbitrarily slow schedule is sought, name
the route as an equivalent formulation, and identify the new arithmetic
estimate that pays the missing cancellation. The #320 and changed-seed controls
must be rejected by that arithmetic input; the normal de Bruijn construction
must be accepted as showing that a prescribed growing gate is not necessary.

## E5. No prescribed diverging sublinear schedule is necessary for normality

The explicit schedule in E4 can be strengthened to a universal obstruction.
This theorem concerns a schedule fixed independently of the number being
constructed. The construction below uses convergence thresholds of a known
normal number; no computational rate for those thresholds is asserted here.

**Theorem E5 (PROVED).** Let `M:N->N` be any function with `M(N)->infinity`
and `M(N)/N->0`. There exists a base-16 normal real alpha and a sequence
`N_j->infinity` such that for every fixed integer h,

$$E_\alpha(N_j,M(N_j),h)\longrightarrow1.$$

In particular this applies to every prescribed diverging admissible CRT
schedule `M(N)=16^(k(N))3^(L(N))=o(N)`, whether or not it is monotone.

**Proof.** Fix a normal real beta; E4 supplies one without an external
normal-number theorem. Let `K_j>=j^2` be a nondecreasing sequence such that,
for every word v of length at most j and every `s>=K_j`, the number of v-starts
among the first s positions of beta differs from `s*16^(-length(v))` by at
most `s/j`. Such thresholds exist by normality and the finiteness of the
word family at each j. These counts use beta's infinite continuation at the
end of the first s starts.

Inductively choose endpoints N_j, taking N_0=0, so that

$$N_j>jN_{j-1},\quad M_j:=M(N_j)\ge\max(K_j,j^2),\quad
M_j/N_j\le1/j,\quad N_j\ge(j+1)^2K_{j+1}.$$

The two assumptions on M allow all conditions simultaneously at sufficiently
large N_j. Let W_j be the first M_j digits of beta. Stage j of alpha consists
of the first `L_j=N_j-N_(j-1)` digits of the infinite periodic repetition
of W_j. Concatenate these stages.

Fix a word v of length r and a stage j>=r. For a prefix of L starts in the
periodic repetition of W_j, write `L=qM_j+s`, `0<=s<M_j`. In a complete
period, its v-count differs from beta's count in the first M_j starts only
at the final at most r-1 positions. Thus its discrepancy is at most
`M_j/j+j`. For the final partial period, if `s>=K_j`, beta's discrepancy is
at most `s/j`; otherwise its discrepancy is at most K_j. Again there are
at most j cyclic seam errors. Therefore the discrepancy in L periodic
starting positions is at most

$$L/j+qj+K_j+j\le2L/j+K_j+j,$$

using `M_j>=j^2`. Comparing this periodic sequence to the actual stage of
alpha changes at most r-1 starts at the final stage seam. Hence a completed
stage or partial current stage incurs at most

$$2L/j+K_j+2j.\tag{10}$$

At an arbitrary prefix ending in stage j, the aggregate contributions
`sum_(i<=j) 2L_i/i` (with the current partial length) are `o(N)` by splitting
off finitely many early i, then bounding `2/i` by an arbitrary epsilon.
The finitely many stages i<r contribute only a constant. The remaining
nonlength errors satisfy

$$\sum_{i\le j}K_i\le jK_j,\qquad
\sum_{i\le j}2i=O(j^2).$$

For j>=2 and N in stage j, the preceding endpoint obeys
`N>=N_(j-1)>=(j)^2 K_j>=j^4`. Consequently these two error sums divided by
N are respectively at most `1/j` and `O(1/j^2)`. This proves correct word
frequencies at every prefix, hence normality of alpha.

At endpoint N_j, compare its phase sequence with the M_j-periodic phase
sequence from W_j, extended over the earlier prefix as in E4. Except for
N_(j-1) earlier positions and the final j positions, the orbit coordinates
share at least j digits. Therefore (8) and (9) hold with this N_j,M_j.
The choices `N_(j-1)/N_j<1/j` and `M_j/N_j<=1/j` force every error to zero
for fixed h. The universal upper bound (1) gives the matching limit one.
QED.

**Quantifier boundary.** E5 refutes deriving the prescribed-schedule energy
gate solely from ordinary normality, for every growing sublinear schedule.
It does not refute a source-specific sufficient bound for pi. It also does
not conflict with E3's existential schedule: that schedule is allowed to
adapt to the normal number after its convergence rates are known, whereas
E5 fixes the schedule first and then constructs a defeating normal number.
The changed-selector exact-forcing corollary applies by the same Green
transport and preserves the distinction from `U_0=0`.

## Scope of E4/E5: these maximal-energy normal counterexamples are Liouville

In E4 and E5, approximate alpha by its first N_(j-1) digits followed by
the periodic repetition of W_j. The denominator is at most
`16^(N_(j-1)+M_j)` and the approximation error is at most `16^(-N_j)`.
Since `N_j/(N_(j-1)+M_j)->infinity`, these approximations prove that the
constructed normal alpha is Liouville. Its irrationality follows already
from normality. Thus E4/E5 refute necessity from **normality alone**; they
do not refute a statement adding finite irrationality type. The distinct
sparse and mixing controls have finite type but are nonnormal. Combining
properties across those different controls would be invalid.

All phase comparisons in E4/E5 can use circle distance, covering even a
finite initial all-15 periodic word without an endpoint convention problem.


## E6. A normal, finite-type counterexample for every growing schedule

This is stronger than E5 and avoids its Liouville limitation. The energy stays
bounded away from zero, rather than tending to its maximum. Its construction
is elementary and does not merge properties of different countermodels.

**Theorem E6 (PROVED; root and two separate derivations audited).** For every prescribed positive
integer schedule `M(N)->infinity`, `M(N)/N->0`, there is a base-16 normal
real alpha such that:

1. for every sufficiently large denominator q and every integer p,
   `|alpha-p/q| >= 2^(-10) q^(-6)`;
2. for every fixed integer h,

$$\liminf_{j\to\infty}E_\alpha(4^j,M(4^j),h)\ge\frac14.$$

Thus even ordinary normality **together with a concrete finite irrationality
measure** does not imply the growing energy gate. The schedule may be any
admissible CRT schedule. This remains a changed-carrier obstruction, not a
refutation of a genuinely zero-selected BBP estimate.

### Construction

Fix the explicit normal beta from E4. Set `N_0=0`, `N_j=4^j` for `j>=1`,
`L_j=N_j-N_(j-1)`, and `m_j=M(N_j)`. Let W_1 be the first m_1 digits of beta.
Given W_(j-1), let d be the digit which its periodic continuation would put
at position `N_(j-1)+1`, that is, the digit of W_(j-1) at zero-based index
`L_(j-1) mod m_(j-1)`. Start W_j as the first m_j digits of beta, then replace
its first digit by 0 if `d>=2`, and by 3 if `d<=1`. This changed digit differs
from d by at least two. Stage j consists of the first L_j digits of the
infinite periodic repetition of W_j. Alpha is the concatenation of all
stages. The initial stage is immaterial to all asymptotic claims.

### All-prefix normality

Fix a word v of length r. As `m_j->infinity`, beta's first m_j starting
positions have v-frequency tending to `16^-r`. Replacing the first digit of
W_j changes at most r cyclic v-starts; closing its period changes at most
another r starts relative to beta's infinite continuation. Therefore the
cyclic v-frequency of W_j differs from `16^-r` by a number `delta_j(v)->0`.

For any prefix of L starts in the periodic continuation of W_j, delete its
complete periods. The remainder has fewer than m_j starts, so its count
discrepancy is at most

$$\delta_j(v)L+2m_j.$$

Comparing with the actual stage costs at most r further starts across its
end seam. Summing through a prefix ending in stage j gives, after paying
finitely many early stages,

$$\sum_{i\le j}\delta_i(v)L_i^*+2\sum_{i\le j}m_i+O(rj),$$

where `L_i^*` is the completed or current partial stage length. The first
sum is o(N), by splitting finitely many early indices and then using
`delta_i(v)<epsilon`. For the second, `m_i/N_i->0` and the geometric sum
`sum_(i<=j)N_i<4N_j/3` give `sum_(i<=j)m_i=o(N_j)`. During stage j>=2,
`N>=N_(j-1)=N_j/4`, so this is also o(N), uniformly over partial prefixes.
Finally `j/N->0`. Every word has the correct limiting frequency, proving
base-16 normality at all prefixes.

### Uniform positive energy at the geometric endpoints

At endpoint N_j, compare `z_n=e(h16^(n-1)alpha)` to the m_j-periodic phase
sequence w_n from W_j, aligned at the beginning of stage j and extended
periodically over the whole prefix. Away from the last j positions of the
new stage, the two radix coordinates share at least j digits. Thus over
that stage

$$D_j^{\rm new}:=\sum_{N_{j-1}<n\le N_j}|z_n-w_n|
\le2j+2\pi |h|N_j16^{-j}.$$

In the earlier prefix each real part `Re(z_n conjugate(w_n))` is at least
minus one. In the new stage it is at least `1-|z_n-w_n|`. Consequently

$$\Re\sum_{n=1}^{N_j}z_n\overline{w_n}
\ge N_j-2N_{j-1}-D_j^{\rm new}.$$

Because w is m_j-periodic and unit modulus, Cauchy--Schwarz over residue
classes gives

$$\left|\sum_n z_n\overline{w_n}\right|^2
\le m_j\sum_{t\bmod m_j}|S_t|^2=N_j^2E_\alpha(N_j,m_j,h).$$

For j>=2, `N_(j-1)/N_j=1/4`. Therefore the exact lower bound

$$\boxed{E_\alpha(N_j,m_j,h)\ge
\left(\frac12-\frac{2j}{N_j}-2\pi |h|16^{-j}\right)_+^2}\tag{11}$$

proves the energy conclusion for every fixed h, on one and the same alpha.
No arithmetic class balancing and no independent-product-Haar assumption
is needed.

### Elementary irrationality bound

Let A_j be the rational whose hexadecimal expansion agrees with alpha
through its first `N_(j-1)` digits and thereafter repeats W_j forever.
It has some (not necessarily reduced) positive denominator Q_j satisfying

$$Q_j\le16^{N_{j-1}}(16^{m_j}-1)<16^{N_{j-1}+m_j}.$$

Its expansion agrees with alpha through position N_j, hence
`|alpha-A_j|<=16^(-N_j)`. The next stage's first-digit rule forces their
first differing digits, at position N_j+1, to differ by at least two.
The entire remaining tail can compensate by at most one unit in that
position. Hence

$$16^{-(N_j+1)}\le|\alpha-A_j|\le16^{-N_j}.\tag{12}$$

Eventually `m_j<=N_j/16`, since `M(N)/N->0`. For those j>=2,

$$Q_j\le16^{5N_j/16}.$$

Fix a sufficiently large positive denominator q, and choose the least j
in this eventual range such that

$$2q\le16^{11N_j/16}.$$

For sufficiently large q the preceding index is also in the range, so
minimality and `N_j=4N_(j-1)` imply

$$2q>16^{11N_j/64},\qquad16^{N_j}<(2q)^{64/11}.\tag{13}$$

If `p/q != A_j`, separation of two distinct rationals gives

$$|p/q-A_j|\ge1/(qQ_j).$$

The chosen threshold gives `16^(-N_j)<=1/(2qQ_j)`, so (12) and the triangle
inequality yield

$$|\alpha-p/q|\ge\frac1{2qQ_j}
>2^{-31/11}q^{-31/11}.$$

If `p/q=A_j` instead, the marker lower bound in (12), followed by (13), gives

$$|\alpha-p/q|\ge16^{-(N_j+1)}
>2^{-108/11}q^{-64/11}.$$

Both bounds are at least `2^(-10)q^(-6)` for `q>=1`, since
`31/11<6`, `64/11<6`, and `108/11<10`. This proves the asserted finite-type
bound for all sufficiently large q, with no unproved irrationality input.
The conclusion is an upper bound on irrationality exponent, not an equality.

### Source-preserving changed-selector corollary

Set `V_0=(alpha-pi)/16` and use the original four-pole r at every later time.
Then `V_n=16^(n-1)alpha-T_n`. Its real-circle empirical distribution is Haar,
its completed carrier alpha obeys the finite-type bound just proved, and
source-authentic energy transport (3) preserves the lower limit `1/4` along
N_j. The original zero selector is not claimed. No 2-adic value is assigned
to the generally irrational changed state; any CRT labels here are the
unchanged authentic zero-source clock used solely as external time labels.

### E6a. Irrationality-exponent range

The same construction in fact satisfies

$$4\le\mu(\alpha)\le16/3.$$

For the lower bound, use the distinct rational approximants A_j with
reduced denominator at most `16^(N_j/4+o(N_j))` and error at most
`16^(-N_j)`. Their reduced denominators are unbounded because alpha is
irrational. Thus every exponent strictly below four occurs infinitely often.

For the upper bound fix `0<epsilon<1/12` and put `a=1/4+epsilon`. Eventually
`Q_j<=16^(a N_j)`. Choose the least j in this range with
`2q<=16^((1-a)N_j)`. The preceding index gives
`16^N_j<(2q)^(4/(1-a))`. The distinct-rational branch now gives
`|alpha-p/q|>(2q)^(-(1+3a)/(1-a))`; the equal-rational branch gives
`|alpha-p/q|>16^(-1)(2q)^(-4/(1-a))`. Since `1+3a<4`, both yield a uniform
bound with exponent `4/(1-a)`. Letting epsilon decrease to zero proves
`mu(alpha)<=16/3`. This limit need not preserve the explicit constant in
E6, which is why E6 retains its simpler `2^(-10)q^(-6)` certificate.
No exact value of the irrationality exponent is asserted.

# Beta: exact local-rule decision and a sharp binary/3 ladder obstruction

**Status:** paper proofs and exact rational certificates; one finite combinatorial
core checked by Lean 4.14. No new counterexample in `18<=n<=94` has been certified.
No general nonexistence theorem for such a counterexample is asserted. Academic
priority of the reductions below is **UNVERIFIED**.

The primary source is Daria Poliakova, [*More (shifted) runners, less loneliness*,
arXiv:2609.23952v1](https://arxiv.org/html/2609.23952v1), especially Definitions 3/5,
Proposition 4, Theorems 6/7, and Table 1. The paper defines the local-rule problem;
the results below retain its original responsibility relation and affine phases.
The key advance is a finite **necessary and sufficient** test of locality, a
complete fixed-cap existence reduction, and an exact classification of the literal
binary/3 ladder. These distinguish an architectural obstruction from a failed search.

## 1. Precise source and quantifiers

For each positive integer N, start with the zero-shift velocities `2,4,...,2N`
and let `delta=1/(N+1)`. Distance to the nearest integer is denoted `||x||`.
This starting configuration is a delta-cover: the circular pigeonhole argument
applied to `0,2t,...,2Nt` gives a difference `2jt` within delta of an integer.

A rule has finite, disjoint sets R and S of positive even velocity labels, a
finite set A of distinct positive odd labels, and, for each rescuer `v in S union A`,
a phase `alpha_v+beta_v delta`. Initially alpha and beta may be arbitrary real numbers.
An application at an odd positive integer scale b removes Rb, rephases Sb, and adds Ab.
It is admissible when `Lb<=2N`, where `L=max(R union S)`. A runner q in the original
configuration is **responsible** for time t when it is the smallest original even
velocity satisfying `||qt||<=delta`.

Locality means: for **every** N, every admissible odd b, and every real t, if the
responsible original runner lies in `(R union S)b`, a rescuer from `(S union A)b`
of this same application covers t. This is stronger than merely preserving the
global cover at a fixed N, or even having a global uniform rule without locality.
The gain is `g=|R|-|A|`. Rephased zero phases are allowed; retaining them in S makes
their use as local rescuers explicit.

Poliakova's Proposition 4 then gives `E_n>=g` for `n>=L/2-g`. Compatibility of
multiple applications and asymptotic density require her separate disjoint-scale
argument; a certificate of one local rule does not independently establish new
packing estimates.

## 2. LRU-1: complete finite resonance criterion

For an affected even label q, define the finite residue set

`K_q={k in {0,...,q-1}: gcd(k,q/2)=1}`.

For each k and rescuer v retain it only when

`v k/q+alpha_v in Z`.

Its resonant interval is

`I_(q,k,v)={z in [-1,1]: |(v/q)z+beta_v|<=1}`.

**Theorem.** The affine-phase rule is local if and only if, for every affected q
and every `k in K_q`,

`[-1,1] = union_(v resonant) I_(q,k,v)`.

This statement holds for real alpha and beta. For rational coefficients it is a
finite exact rational computation. It contains no sampled-time approximation,
upper bound on N, or assumption of a positive numerical coverage margin.

**Proof, sufficiency.** Suppose qb is responsible and write

`qb t=k+delta z`, `|z|<=1`.

If `d=gcd(k,qb/2)>1`, the smaller positive even velocity `qb/d` belongs to the
starting configuration and is within `delta/d` of an integer, a contradiction.
Thus `gcd(k,qb/2)=1`, implying `gcd(k,q/2)=1`. Reduce k modulo q. The finite
cover gives a rescuer v with integral `v k/q+alpha_v` and
`|(v/q)z+beta_v|<=1`. At this time its position is

`vb t+alpha_v+beta_v delta = v k/q+alpha_v+delta[(v/q)z+beta_v]`.

Its distance to an integer is at most delta. This is independent of N and b.

**Proof, necessity.** Suppose the interval union misses z for some q and `k in K_q`.
Use scale b=1 and times

`t_N=(k+delta z)/q`, `delta=1/(N+1)`.

For every original even `u<q`, `u k/q` is not an integer: writing u=2a, an
integral value would require `q/2` to divide a because `gcd(k,q/2)=1`, impossible
for `a<q/2`. There are only finitely many such u, and their distances from integers
have a positive minimum. Therefore for all sufficiently large N none covers t_N,
while q does. The nominated runner q is actually responsible, and admissibility
holds because N may be chosen arbitrarily large.

For a nonresonant rescuer v the limiting position `v k/q+alpha_v` has strictly
positive distance from the integers, so it cannot cover t_N for all sufficiently
large N. For a resonant v, the missed-interval hypothesis says
`|(v/q)z+beta_v|>1`. For sufficiently small delta there is no wrap to another
integer, and this runner is also farther than delta from the origin. Finiteness
lets one N satisfy every exclusion. This contradicts locality.

The residue condition is **not** `gcd(k,q)=1`. For example, q=6 permits k=2 and
4. A false rule removing 6 and adding velocity 3 with phase 1/2 covers the odd
residues but fails at k=2. This mutation is tested explicitly.

## 3. LRU-2: constructive rational counterexample, including endpoints

When all phase coefficients are rational, every resonant interval has rational
endpoints. A missed relative endpoint `z=-1` or `z=1` is already a rational witness;
an interior gap has a rational midpoint. Closed intervals are merged with equality
allowed, so touching endpoints are never incorrectly declared gaps.

The necessity proof has a fully explicit rational choice of N. For an uncovered
cell `(q,k,z)`, write for every rescuer

`d_v=||v k/q+alpha_v||`, `c_v=(v/q)z+beta_v`.

Take epsilon to be the minimum of the following positive rational numbers:

* `||u k/q||/(1+|(u/q)z|)` for the positive even `u<q`;
* `d_v/(1+|c_v|)` when `d_v>0`;
* `1/(1+|c_v|)` when `d_v=0`, in which case `|c_v|>1`.

An empty minimum can be replaced by 1. Choose

`N=max(L/2, floor(1/epsilon)+1)`, `delta=1/(N+1)`,

and `t=((k+delta z)/q) mod 1`.
The circle distance is 1-Lipschitz, so each nonresonant distance exceeds delta.
For a resonant rescuer,
`delta<|delta c_v|<1-delta`, excluding both neighboring integers. The same
Lipschitz estimate excludes every smaller original even velocity. Thus q is
responsible and no permitted local rescuer covers the exact rational time t.

This is a counterexample to **locality**. A larger unaffected runner may still
cover t; global cover failure is not inferred from this certificate.

The naive replacement of the baseline removed velocity 192 by 190 fails at
`q=190,k=1,z=-1`. The generated actual witness is

`N=192`, `delta=1/193`, `t=96/18335`.

Velocity 190 is responsible. The nearest listed rescuer is 96, at distance
`96/18335`, while `delta=95/18335`; it misses by exactly `1/18335`.
All remaining rescuer distances and every required exclusion are checked with
`Fraction`, not a floating tolerance.

## 4. LRU-3: complete phase reduction and rational witnesses

Fix disjoint velocity supports R,S,A, with nonempty affected set `Q=R union S`.
For each rescuer velocity v define

`D_v={-v k/q mod 1 : q in Q, k in K_q}`,
`B_v=1+v/min(Q)`.

**Theorem.** If some real affine phases make this support local, there is such a
rule with every `alpha_v in D_v` and `|beta_v|<=B_v`. For each choice of the finite
alpha menus, the feasible beta set is a finite union of bounded closed rational
polyhedra. Consequently real feasibility implies feasibility with entirely
rational affine phases, and fixed-support existence is decidable by exact finite
rational linear feasibility.

**Proof of the bounds.** A phase outside D_v is nonresonant in every cell, hence
contributes nothing to the necessary and sufficient criterion. Replacing it by
any member of D_v can only add possible tangent coverage. If `|beta_v|>B_v`, then
for all affected q and `|z|<=1`,

`|(v/q)z+beta_v| >= |beta_v|-v/q > 1`.

This runner again contributes nothing, and replacing beta by zero loses no tangent
coverage. These replacements preserve locality by LRU-1; they do not invoke a
generic small perturbation that might destroy a closed endpoint equality.

**Proof of polyhedrality.** Fix alpha choices. In a given residue cell, a resonant
runner has the untruncated interval

`[a_v,b_v]=[(-1-beta_v)q/v,(1-beta_v)q/v]`.

These endpoints are rational affine functions of beta. A finite interval union
covers `[-1,1]` exactly when there is a simple chain of its intervals whose first
contains -1, whose last contains 1, and whose consecutive pairs intersect. Such
a chain exists by the interval intersection graph; a simple chain has at most
as many vertices as there are rescuers. Each fixed chain is expressed using only
nonstrict rational linear inequalities:

`a_first<=-1<=b_first`, `a_last<=1<=b_last`, and
`a_i<=b_j`, `a_j<=b_i` for adjacent intervals i,j.

The connected union of the chain contains both endpoints, hence their whole
interval. Conversely full coverage supplies a chain. Enumerate the finitely many
chains in each of the finitely many cells. Intersect cell conditions and distribute
finite unions: the result is a finite union of closed rational polyhedra. Adding
the bounds `|beta_v|<=B_v` makes these polytopes. A nonempty rational polyhedron
has a rational point, for example by exact Fourier–Motzkin elimination and rational
back-substitution. This proves rational witness existence and finite decidability.

This theorem covers arbitrary real phase choices on the fixed support; the search
scripts' smaller alpha menus are deliberately **restricted searches**, not an
implementation of the entire complete enumeration.

## 5. LRU-4: added-velocity reduction and fixed-cap decidability

The previous theorem does not need unbounded odd velocities to remain an open
loophole. Fix the affected even set Q, let `M=lcm(Q)` (an even integer), and suppose
there are m odd additions.

**Theorem.** Any local rule on Q with m odd additions can be replaced by one with
the same affected support and the same gain, with all added velocities `<mM` when
m>0. The replacement preserves distinct positive odd velocities. Thus existence
of a local uniform rule with a specified finite even cap L and gain at least a
specified positive integer g is finitely decidable in principle, without a phase
grid or an unproved upper bound on the added velocities.

**Proof of velocity compression.** In each odd residue class `r mod M`, `1<=r<M`,
sort the old added velocities as `v_0<...<v_(c-1)`. Set

`v'_j=r+jM`, `alpha'_j=alpha_j`, `beta'_j=(v'_j/v_j)beta_j`.

Because the old velocities are distinct positive representatives of this same
class, `v'_j<=v_j`. All new velocities remain distinct within and across residue
classes, positive, odd, and less than mM. For each affected q, q divides M, so

`v'_j k/q+alpha_j` and `v_j k/q+alpha_j`

differ by an integer. Every resonance is preserved. Moreover, with `c_j=v'_j/v_j`
in `(0,1]`,

`|(v'_j/q)z+beta'_j|=c_j |(v_j/q)z+beta_j|`.

Every old covered tangent point remains covered. LRU-1 gives locality of the
compressed rule. No rephased even velocity is changed, so the affected support,
admissibility threshold, and gain remain unchanged. For m=0 there is nothing to do.

For fixed L and g, there are finitely many disjoint R,S among the positive even
integers at most L, and `0<=m<=|R|-g`. For each support and m, the compression
bound gives finitely many possible distinct odd additions. Apply the finite
phase/polytope reduction from LRU-3 to each. This is a terminating theoretical
algorithm. The bound involves an lcm and is extremely large; **no claim of an
efficient algorithm or an executed exhaustive classification at L=190 is made**.

## 6. LRU-5: sharp classification of the literal binary/3 ladder

For an integer `J>=2`, consider only this explicitly delimited family:

* Every `3*2^j`, `2<=j<=J`, is rephased by `(1+delta)/2`.
* Every binary velocity `2^k`, `3<=k<=J+1`, is either removed or rephased by `-delta`.
* The terminal velocity `3*2^(J+1)` is removed.
* The only additions are velocities 3 and 9, each with phase 1/4.

Let B be the set of removed binary exponents. Every other original velocity is
unaffected. The gain is `|B|-1` and the largest affected velocity is
`L=3*2^(J+1)`.

**Theorem.** This rule is local if and only if the last binary exponent J+1 is
retained and no two consecutive binary exponents are both removed. Equivalently,
every removed binary runner is immediately followed by a retained doubled runner.
The largest possible gain at depth J is exactly

`g_max(J)=floor((J-1)/2)-1`.

Positive gain therefore forces `J>=5` and `L>=192`. At the first possible depth,
the unique saving pattern has `B={3,5}`, reproducing Poliakova's
`R={8,32,192}`. This family cannot produce either gain one with `L<=190` or gain
two with `L<=192`.

**Necessity.** For a responsible binary source `q=2^h`, `3<=h<=J+1`, k is odd.
The only resonant half-shifted tripled velocity is `3q/2`; its tangent interval
is `[-1,1/3]`, so it fails at z=1. The odd additions with phase 1/4 are
nonresonant because q has 2-adic valuation at least three. A retained binary
`v=2^l` with phase `-delta` can be resonant only when `l>=h`; at z=1 it covers
exactly when `|2^(l-h)-1|<=1`, meaning `v=q` or `v=2q`. Thus if q is removed its
double must be retained. The last binary has no allowable double and must remain.
This uses the necessity direction of LRU-1, so the endpoint test corresponds to
genuinely responsible times for sufficiently large N.

**Sufficiency.** For a binary q, the half-shifted `3q/2` covers `z in [-1,1/3]`.
If q is retained, it covers `z in [0,1]`; if removed, its retained double covers
the same interval. These intervals cover `[-1,1]`. For a tripled source
`q=3*2^j` with `j>=3`, including the removed terminal, the half-shifted q/2
has tangent displacement `(1+z)/2` and covers the full interval. The smallest
tripled source q=12 is covered by the added 3 or 9 according to the odd residue
of k modulo 4, with displacement `z/4` or `3z/4`. This proves locality in all cases.

**Optimal count.** There are J-1 binary positions. Pair each removal with its
immediately following retained position. These pairs are disjoint, so
`2|B|<=J-1`. Alternating removed/retained pairs attain `floor((J-1)/2)` removals.
At J=5 the length-four pattern attaining two removals and ending retained is
uniquely `(remove,retain,remove,retain)`. Subtracting the two additions and adding
the single terminal removal proves the gain formula.

The bound and its depth consequence are kernel checked in
[`formal/LonelyRunnerUniform.lean`](../../formal/LonelyRunnerUniform.lean), using
Lean 4.14 core only. The all-list theorem proves `2*removedCount<=length` for
the exact no-adjacency/last-retained grammar. Reported dependencies are `propext`
and `Quot.sound`; no added axiom or admitted goal is used. The circle/resonance
equivalence and polyhedral reduction remain paper proofs, not Lean claims.

## 7. Baseline, bounded searches, and failed routes

The literal Section 3 baseline is

```
R={8,32,192}
S={12,24,48,96} at (1+delta)/2, and {16,64} at -delta
A={3,9} at 1/4.
```

The exact checker verifies all 184 responsibility residue cells. Table 1 is also
accounted for: its best displayed asymptotic coefficient is 1/224, from gain 2,
L=240 and P=30. That is a stronger published asymptotic coefficient but does not
already supply a cap/gain combination reaching n=94. The table's second gain-one
L=192 rule uses different signs; it is not silently substituted for Section 3.

Raw bounded search observations are in `BETA_UNIFORM_SEARCH_RECEIPTS.json`:

* Integer-program search on multiples of four through 188, odd velocities through
  135, a finite half/quarter phase menu and beta grid: time limit, no candidate.
* Continuous-beta SMT on 2,3,5-smooth affected multiples of four through 188, with
  the half/quarter alpha menu: timeout, no candidate.
* Continuous-beta SMT on 2,3-smooth affected multiples of four through 188, odd
  velocities through 81, same alpha menu: solver reported UNSAT. This is recorded
  only as a restricted solver result, not as a general or kernel-checked impossibility.
* Expanded thirds/sixths/quarters/eighths alpha menu on the latter support:
  timeout, no candidate.
* Positive calibration at cap 192 recovered a gain-one rule; the independently
  implemented exact checker verified it. Its extra support and phases do not improve
  the published n-threshold.

The continuous-beta encoding uses a finite Boolean combination of exact rational
linear inequalities, not a beta mesh. One compact form asks that -1 be covered and
that every selected interval endpoint `b_i in [-1,1)` have an extender j satisfying
`a_j<=b_i<b_j`. This is equivalent to interval coverage by finite increasing-endpoint
chains. The paper proof of rationalization uses the closed-chain formulation in
section 4, avoiding any reliance on a solver's strict-inequality implementation.
Every satisfying model is rechecked by the independent `Fraction` certificate path.

## 8. Provenance, claim limits, and next falsifier

| Claim | Status | Limitation / next falsification |
|---|---|---|
| LRU-1 finite resonance iff locality | PAPER-PROVED; exact checker | Definition 5 locality, not every global uniform cover rule |
| LRU-2 actual rational missed-cell witness | PAPER-PROVED; exact counterexample | May leave global cover intact via unaffected larger velocities |
| LRU-3 finite phase reduction and rational witness | PAPER-PROVED | Fixed supports; finite polyhedral enumeration may be very large |
| LRU-4 bounded additions and fixed-cap decidability | PAPER-PROVED | Theoretical lcm bound; cap-190 classification not executed |
| LRU-5 exact binary/3 ladder classification | PAPER-PROVED; combinatorial core LEAN KERNEL | Literal stated phases/support; broader rules remain possible |
| New counterexample for 18 through 94 | NOT ACHIEVED in this lane | Seek another support/phase family or direct fixed-N cover |
| General cap-190 rule impossibility | NOT CLAIMED | Restricted SMT results cannot establish it |

The instrument is source-contacting through the exact original responsibility rule;
its missed-cell construction checks that a formal residue really occurs at a valid
source time. Parent, analytic, and independent audit agents rederived the central
proofs, but all share the same primary Poliakova source. Exact rational replay,
symbolic/SMT search, paper proof, and Lean's count lemma have different authority
levels and are recorded separately.

Priority search checked the original arXiv version, its full table, and targeted
searches for local uniform rules, affine phases and rational shifted-runner rules.
No exhaustive priority clearance was obtained. The interval/polyhedron ingredients
are classical; a theorem newly recorded in this repository is not automatically
academically novel. The ordinary common-origin Lonely Runner conjecture is untouched.

The most discriminating next target is a rule outside LRU-5: change residue phases
and support, obtain gain two at cap 192, or use a direct fixed-N certificate. LRU-4
removes an unbounded-velocity ambiguity from future complete fixed-cap work, but its
bound needs a substantial quantitative improvement before exhaustive search is practical.

Reproduce:

```
PYTHONPATH=. python -m unittest tests.test_lonely_runner_uniform -v
python scripts/lonely_runner_uniform_probe.py --output /tmp/uniform-exact.json
lean formal/LonelyRunnerUniform.lean
python scripts/lonely_runner_uniform_search.py --continuous-beta --smooth-primes 2,3 --limit 188 --max-odd 81 --seconds 30
```

Native validation uses only the standard library. Optional search needs SciPy or
Z3 and has explicit wall-time limits. The exact checker does not trust either solver.

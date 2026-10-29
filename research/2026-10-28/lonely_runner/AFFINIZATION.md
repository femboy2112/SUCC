# Arbitrary phase schedules admit affine local rules on the same supports

**Status:** PROVED LOCAL on paper, pending external review and priority checks.
The proof uses finite-dimensional compactness. It gives no convergence rate
and does not identify an arbitrary input schedule with its affine replacement.
No theorem below is Lean-formalized.

## 1. Source convention and quantifiers

Fix disjoint finite sets R,S of positive even integers and a finite set A of
distinct positive odd integers. Put `Q=R union S`, assumed nonempty, and
`H=S union A`. At size N, the original velocities are `2,4,...,2N` with zero
shifts, and the covering radius is `delta_N=1/(N+1)`. A responsible velocity
is the smallest original even velocity within delta_N of an integer.

Let `N_j` be any sequence of integers tending to infinity with
`2N_j>=max(Q)`. For every `v in H` and every j, assign any phase
`theta_(v,j) in R/Z`. These phases need not converge, be measurable, vary
continuously, or possess an expansion in delta. Suppose that, at each j and
at scale b=1, every real time whose responsible velocity belongs to Q is
rescued by some v in H with its assigned phase theta_(v,j).

**Theorem AFF-01.** There exist rational constants `alpha_v,beta_v`, on the
same R,S,A, such that the phases `alpha_v+beta_v*delta` define a local rule for
every admissible N, every admissible positive odd scale b, and every real
time. In particular the support and gain `|R|-|A|` are preserved.

Only existence is asserted. The output phases generally differ from the
input schedule, including at the original N_j. No pointwise or uniform
approximation to that schedule is claimed. If Q is nonempty, the premise
cannot hold with H empty, as the responsible times constructed below show.

## 2. Joint limiting phase data

Since the finite product `(R/Z)^H` is compact, pass to one subsequence such
that `theta_(v,j)` tends to a limit alpha_v modulo one for every v. Choose
real representatives alpha_v. Let epsilon_(v,j) be the signed local lift
in `[-1/2,1/2)` of `theta_(v,j)-alpha_v`. Then epsilon_(v,j) tends to zero,
and for an integer m_(v,j),

\[
 \theta_{v,j}=\alpha_v+\epsilon_{v,j}+m_{v,j}.
\]

Pass to a further common subsequence such that

\[
 \frac{\epsilon_{v,j}}{\delta_{N_j}}\longrightarrow
 \beta_v\in\mathbb R\cup\{-\infty,+\infty\}
 \qquad(v\in H).
\tag{1}
\]

This uses compactness of a finite product of the extended real line; for
example apply arctangent to every coordinate. The subsequence and all limits
are selected once, before choosing any tangent cell.

## 3. Every responsible tangent cell survives the limit

Fix any affected q, any integer `0<=k<q` with `gcd(k,q/2)=1`, and any real
`z in [-1,1]`. Write delta_j for delta_(N_j), and set

\[
 t_j=\frac{k+\delta_j z}{q}\pmod1.
\tag{2}
\]

For any earlier even p<q, the number pk/q is nonintegral: otherwise q/2
would divide `(p/2)k`, and coprimality would force q/2 to divide p/2.
Thus `||p*t_j||` tends to a positive number. Since there are only finitely
many earlier p, all of them have distance greater than delta_j for all
sufficiently large j. Meanwhile `||q*t_j||<=delta_j`. Hence q is actually
responsible for t_j eventually, so the assumed locality must rescue it.

For a candidate rescuer v, its position modulo an integer is

\[
 \frac{vk}{q}+\alpha_v+\epsilon_{v,j}
                  +\delta_j\frac vq z.
\tag{3}
\]

If `vk/q+alpha_v` is nonintegral, (3) tends modulo one to a nonzero point,
and v cannot rescue t_j when j is large.

Suppose instead `vk/q+alpha_v` is integral. The residual
`x_j=epsilon_(v,j)+delta_j*(v/q)z` tends to zero. If beta_v is infinite in
(1), then `|x_j|/delta_j` tends to infinity, while x_j itself tends to zero.
Thus eventually `delta_j<|x_j|<1/2`; there is no wraparound rescue and v
again cannot cover t_j.

For a finite beta_v, if `|(v/q)z+beta_v|>1`, the same conclusion follows
from (1), now with a fixed strict limiting margin. Therefore, if no v with
finite beta_v satisfied

\[
 \frac{vk}{q}+\alpha_v\in\mathbb Z,
 \qquad \left|\frac vqz+\beta_v\right|\le1,
\tag{4}
\]

every member of the finite set H would fail to rescue t_j eventually. This
contradicts locality. At least one finite-beta rescuer satisfies (4).

The chosen q,k,z were arbitrary. All their conclusions concern the same
limiting phase vector. No subsequence simultaneous over an uncountable set
of z was chosen or needed: for each fixed cell, the common limiting vector
would contradict its eventual coverage if (4) failed.

For entries with infinite beta_v replace beta_v by zero, retaining alpha_v.
Those entries were not used in (4), so this cannot destroy any credited
coverage. The result is a finite real affine phase vector whose tangent
intervals cover every cell.

## 4. Transfer to every N and odd scale, and rationalization

Fix any admissible N,b and any time whose responsible velocity is qb for
q in Q. Write `qb*t=k+delta*z`, with integer k and `|z|<=1`. If
`c=gcd(k,qb/2)>1`, the earlier original even velocity qb/c has distance at
most delta/c, contrary to responsibility. Hence `gcd(k,q/2)=1` too.
Reduce k modulo q and choose a rescuer from (4). Its affine-phase position is

\[
 vb t+\alpha_v+\beta_v\delta
 =\frac{vk}{q}+\alpha_v+
       \delta\left(\frac vqz+\beta_v\right),
\]

which is within delta of an integer. This proves all-scale locality for the
real affine coefficients, including N not belonging to the original sequence.

The fixed-support rationalization theorem in `BETA_UNIFORM.md`, LRU-3,
replaces these real coefficients by rational ones without changing any
velocity or its role. Briefly, any useful alpha is an exact resonance
`-vk/q mod 1`, so it belongs to a finite rational menu; useless alpha entries
can be reset. One may bound `|beta_v|<=1+v/min(Q)`, since a coefficient
outside this box covers no tangent point. For each finite alpha choice,
all tangent interval-cover conditions form a finite union of bounded closed
rational polyhedra: enumerate chains connecting -1 to 1, using both overlap
inequalities between consecutive untruncated intervals. A nonempty rational
polyhedron contains a rational point. This establishes the rational assertion
and completes the theorem. QED.

## 5. Consequences and exact scope

**AFF-02.** For fixed finite R,S,A, the following existence questions are
equivalent: arbitrary phase schedules local along any unbounded sequence of
sizes at scale one; real affine-phase local rules at all sizes and odd scales;
rational affine-phase local rules at all sizes and odd scales. The reverse
implications are immediate by restriction. These statements concern existence,
not equality of the classes of actual schedules.

Consequently the finite rational feasibility criterion for fixed supports,
and the finite bounded-support reduction for fixed cap and positive gain in
the Beta dossier, also decide existence with arbitrary phase schedules under
this locality requirement. The compactness proof itself gives neither a
rate of convergence nor an algorithm extracting limits from a supplied
arbitrary schedule. The independent finite feasibility procedure remains an
in-principle existence search, potentially enormous.

**AFF-03.** The endpoint obstruction in `OBSTRUCTION.md` therefore holds for
arbitrary phase schedules: if all affected velocities have the same odd
part, locality even along an unbounded sequence of sizes forces `|A|>=2|R|`.
Assuming merely global cover preservation is insufficient for this argument;
rescues by unaffected velocities are not credited. Velocity supports must
remain fixed and finite throughout the sequence.

**AFF-X1: the original schedule need not be affine.** Fix any positive odd d,
take `R={4d}`, `S` empty, and `A={d,3d}`. Assign both added runners the phase

\[
 \theta_v(N)=
 \begin{cases}
  3/4+\delta_N/8,&N\text{ even},\\
  1/4-\delta_N/8,&N\text{ odd}.
 \end{cases}
\tag{5}
\]

Both residue choices 1/4 and 3/4 rescue the odd classes modulo four, swapping
which added runner handles which class. The normalized error for the selected
runner is at most `3/4+1/8=7/8<1`. Thus (5) is local at every admissible size
and scale. Nevertheless it has two distinct limiting phases on the circle,
1/4 and 3/4. No fixed affine phase `alpha+beta*delta_N mod 1`, which has a
single limit alpha, agrees with this schedule for every sufficiently large N.
The theorem preserves supports and gain while changing phases; it does not
preserve the input phase schedule.

## 6. Provenance and remaining obligations

The source notion is Poliakova's local uniform rule:
[*More (shifted) runners, less loneliness*, arXiv:2609.23952v1](https://arxiv.org/html/2609.23952v1),
Definitions 3 and 5. Compactness, finite-rescuer exclusion, and rational
polyhedral feasibility are the proof mechanisms; no empirical convergence
claim is used. The published quarter-phase rescue pattern is credited to
Poliakova, not claimed as new.

Academic priority of this fixed-support existence equivalence is UNVERIFIED.
The inspected primary source does not explicitly state it. The proof requires
adversarial mathematical review, and no complete Lean formalization is present.
Finite evaluations of (5) can check implementation but cannot establish the
compactness theorem or a convergence rate for arbitrary input phases.

The exact implementation controls are in
`scripts/lonely_runner_phase_schedule_probe.py` and
`tests/test_lonely_runner_affinization.py`; the four focused tests passed.
The probe also checks an unused runner v=5 with
`delta=1/m^2`, limiting phase 3/4, and residual `epsilon=1/m`. Its scaled
residual tends to infinity, while its actual residual tends to zero; it does
not rescue the resonant q=4,k=1 tangent endpoints. This directly tests the
no-wraparound branch of the proof without treating the finite tests as a
limit theorem. The deterministic receipt is `receipts/affinization.json`;
replay with `python scripts/lonely_runner_phase_schedule_probe.py --verify research/2026-10-28/lonely_runner/receipts/affinization.json`.

| Claim | Evidence | Next falsification test |
|---|---|---|
| AFF-01: arbitrary schedules imply rational affine existence | Universal compactness and finite-cover proof | Challenge infinite scaled residuals or quantifier exchange |
| AFF-02: fixed-support existence equivalence | AFF-01 and restriction | Keep source support fixed while allowing discontinuous phases |
| AFF-03: same-odd-part obstruction without phase regularity | AFF-01 and DYO-01 | Oscillatory and nonconvergent schedules |
| Original schedule itself must be affine | REFUTED by (5) | Two distinct circle accumulation points |
| Quantitative limit extraction from arbitrary schedule | NOT CLAIMED | No regularity or convergence rate is assumed |
| Academic novelty | UNVERIFIED | Independent primary-literature and proof review |

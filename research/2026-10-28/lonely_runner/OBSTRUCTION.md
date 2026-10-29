# Endpoint capacity forbids savings on a single dyadic velocity chain

**Status:** PROVED LOCAL on paper, pending external priority review. The theorem
allows arbitrary real affine phase coefficients and arbitrarily large odd added
velocities. It is not a finite phase-menu exclusion and is not Lean-formalized.

## 1. Exact statement

Use Poliakova's local-rule convention. The original velocities are
`2,4,...,2N`, with zero shifts and radius `delta=1/(N+1)`. A rule removes the
finite even set R, rephases the disjoint finite even set S, and adds the finite
set A of distinct positive odd velocities. Put `Q=R union S`, assumed nonempty,
and `H=S union A`. A rescuer v has phase `alpha_v+beta_v*delta`, with fixed real
coefficients. The gain is `g=|R|-|A|`. At every admissible positive odd scale b,
the rule must rescue any time whose smallest covering original even velocity
belongs to bQ. The rescuing runner must belong to this same application's bH.

**Theorem DYO-01.** Suppose there is a positive odd integer d such that

\[
 Q\subseteq\{d2^a:a\in\mathbb Z,\ a\ge1\}.
\]

If the rule is local for every admissible scale, every N, and every real time,
then

\[
 \boxed{|A|\ge2|R|.}
\]

In particular no positive-gain local affine-phase rule can have all affected
velocities with the same odd part. The additional odd velocities need not have
odd part d and have no imposed size or prime-factor bound. The constant 2 is
sharp, even for each fixed d.

## 2. A general necessary endpoint inequality

For an affected even q define

\[
 K_q=\{0\le k<q:\gcd(k,q/2)=1\}.
\]

For a rescuer v define its normalized endpoint capacity on Q by

\[
 E_Q(v)=\sum_{q\in Q}\frac1{2|K_q|}
   \sum_{k\in K_q}\sum_{\epsilon\in\{-1,1\}}
   \mathbf1\left\{\frac{vk}{q}+\alpha_v\in\mathbb Z,
        \ \left|\epsilon\frac vq+\beta_v\right|\le1\right\}.
\tag{1}
\]

Every local rule, without the dyadic-chain restriction, obeys

\[
 |Q|\le\sum_{v\in H}E_Q(v).
\tag{2}
\]

Indeed, each responsible tangent cell `(q,k,z)` must be rescued by an exactly
resonant v with `|(v/q)z+beta_v|<=1`; apply this at `z=+1,-1`, sum the
pointwise covering inequalities, and use the displayed normalization.

For completeness, this necessary tangent condition follows directly from
locality. If a cell has no such rescuer, set
`t_N=(k+delta*z)/q mod 1` at scale b=1 and let N tend to infinity. For each
earlier even p<q, `pk/q` is nonintegral by `gcd(k,q/2)=1`. Thus p stays outside
the delta-neighborhood of the integers when N is sufficiently large, and q is
responsible. A nonresonant rescuer has a fixed positive limiting distance from
the integers. A resonant rescuer has position modulo an integer
`delta*((v/q)z+beta_v)`, whose absolute slope exceeds 1; for sufficiently small
delta it is farther than delta from every integer. Finitely many positive
margins permit one common N, a contradiction. This argument holds for real
coefficients and for the boundary values `z=+1,-1`.

The complete iff characterization and a rational finite-scale counterexample
constructor appear in `BETA_UNIFORM.md`, LRU-1. Only necessity is needed here.

## 3. Every rephased chain velocity has capacity at most one

Let `v=d*2^b` belong to S, with b>=1. Normalize alpha modulo one.

If alpha=0, the resonant affected velocities are precisely those q<=v.
For q<=v the quotient v/q is an integer, so every k resonates. For q>v,
write `q=d*2^a`, a>b. Then a>=2 and every k in K_q is odd; the number
`k/2^(a-b)` is nonintegral, so no k resonates. Consequently

\[
 E_Q(v)=\frac12\#\{(j,\epsilon):j\ge0,\ v/2^j\in Q,
                \ |\epsilon2^j+\beta_v|\le1\}\le1.
\tag{3}
\]

The last assertion is elementary but includes closed endpoints: any interval
of length 2 contains at most two members of
`{...,-8,-4,-2,-1,1,2,4,8,...}`. Three of the same sign span at least 3;
three involving both signs also span at least 3. There are no repeated members.

If alpha is nonzero modulo one, q<=v cannot resonate. At q>v resonance forces
alpha modulo one to have reduced denominator exactly `2^(a-b)`, since k is
odd. A fixed alpha can have this property for at most one a. At that sole
possible q, the contribution to (1) is at most one, regardless of beta.
Irrational alpha and rational alpha with other denominators contribute zero.
Thus in all cases

\[
 E_Q(v)\le1\qquad(v\in S).
\tag{4}
\]

## 4. Every odd added velocity has capacity at most one half

Let v be any positive odd integer. If resonance occurs at `q=d*2^a`, a>=2,
then every responsible k is odd, so the reduced denominator of `vk/q` has
exact 2-adic order a. Subtracting an integer does not change that denominator.
Hence alpha modulo one must have a reduced denominator with exact 2-adic
order a. At a=1, a responsible k can be even or odd; the reduced denominator
has 2-adic order respectively 0 or 1. These alternatives for different a are
disjoint. A fixed alpha therefore resonates at at most one affected q.

At that q, the fixed-point-free involution

\[
 k\longmapsto k+q/2\pmod q
\]

preserves K_q. It changes `vk/q+alpha` by v/2 modulo the integers, which is
a half-integer. Both members of a pair cannot resonate. At most half the
responsible residues resonate, and each contributes at most two endpoints.
This proves

\[
 E_Q(v)\le\tfrac12\qquad(v\in A).
\tag{5}
\]

This includes q=2d, where replacing `gcd(k,q/2)` by `gcd(k,q)` would incorrectly
discard the even responsible residues. For irrational alpha there is no
resonance at any q, so the same conclusion holds.

## 5. Completion, sharpness, and countermodels

Combining (2), (4), and (5) gives

\[
 |R|+|S|=|Q|\le |S|+\tfrac12|A|,
\]

which is the claimed inequality. This establishes every stated quantifier;
no asymptotic averaging, finite beta grid, or velocity truncation was used.

**Sharpness DYO-02.** For every positive odd d take

\[
 R=\{4d\},\quad S=\varnothing,\quad A=\{d,3d\},\qquad
 \alpha_d=\alpha_{3d}=3/4,\quad\beta_d=\beta_{3d}=0.
\]

Every responsible k for q=4d is odd. If k=1 mod 4, the runner d resonates;
if k=3 mod 4, the runner 3d resonates. Their tangent slopes are respectively
1/4 and 3/4, so the appropriate runner rescues every z in [-1,1]. The finite
locality criterion gives locality at every admissible scale. Equivalently,
write `4db*t=k+delta*z` at any admissible odd scale b. Responsibility forces
k odd, since otherwise the earlier even velocity 2db already covers the time.
The same two integer-phase identities then rescue that actual time directly.
Thus
`|A|=2|R|=2`; the coefficient 2 cannot be increased.

**The same-odd-part hypothesis cannot be discarded.** Poliakova's published
rule has affected odd parts 1 and 3 and gain one, with three removals and two
odd additions. It is a counterexample to extending (DYO-01) even to all
affected velocities whose prime factors belong to {2,3}. Its rescuer v=12,
alpha=beta=1/2, has capacity 3/2: it covers one endpoint at q=8 and both at
q=24. Thus the per-even-rescuer capacity bound actually fails outside the
stated family. This identifies the exact step requiring the hypothesis.

**Two further source mutations fail.** At q=2, the odd runner v=1 with
alpha=1/2 and beta=0 rescues k=1 but not the equally responsible k=0. A
`gcd(k,q)=1` filter would falsely credit complete endpoint coverage. If even
additions were allowed, replacing q=4 by v=2, alpha=1/2, beta=0 would rescue
every tangent cell using one addition. That velocity is an already present
baseline speed and is not a legal added runner. The odd-addition hypothesis
is therefore substantive, not merely a proof convenience.

**Extension.** AFF-01 in [AFFINIZATION.md](AFFINIZATION.md) now proves that
existence with arbitrary phase schedules on fixed finite supports implies
rational affine existence on those same supports. Thus the bound also holds
for arbitrary phase schedules local along unbounded sizes, without regularity.

**Scope.** The proof above concerns affine phases and the compactness corollary
extends existence to arbitrary schedules. Neither excludes general
cover-preserving replacements whose failures of locality are rescued
by unaffected velocities. It
does not prove any new shifted counterexample or the ordinary Lonely Runner
Conjecture. Odd-prime powers in an affected velocity are allowed through d;
what is forbidden for positive gain is confinement to a single odd part.

## 6. Provenance, validation, and priority boundary

The source convention and local rule are from D. Poliakova,
[*More (shifted) runners, less loneliness*, arXiv:2609.23952v1](https://arxiv.org/html/2609.23952v1),
Definitions 3 and 5 and Theorem 7. Her construction supplies the two-odd-part
countermodel and the rescue pattern used in the sharpness example. The endpoint
inequality is a direct finite covering-count argument applied to the exact
locality criterion proved in this campaign. No new status is assigned to the
published construction or to basic counting inequalities.

The primary paper's complete discussion and Table 1 were inspected; the
same-odd-part obstruction was not located there. Targeted searches for local
replacement rules, powers of two, and shifted dyadic runner constructions did
not establish a prior matching theorem. This bounded search is not evidence
of academic novelty; priority remains UNVERIFIED.

`scripts/lonely_runner_dyadic_probe.py` computes the capacity (1) directly,
checks sharp examples, and replays the published rule as a hostile scope
control. Its JSON receipt is a finite exact check, not the universal proof.
`tests/test_lonely_runner_dyadic_obstruction.py` tests the q=2d boundary,
nonzero phase localization, endpoint capacity, sharpness, and the failure when
two odd parts are admitted. No DYO declaration is currently Lean-kernel checked.
The initial exact focused replay passed eight tests. The deterministic receipt
is `receipts/dyadic-obstruction.json`; replay with
`python scripts/lonely_runner_dyadic_probe.py --verify research/2026-10-28/lonely_runner/receipts/dyadic-obstruction.json`.

| Claim | Evidence | Next falsification test |
|---|---|---|
| DYO-01: same odd part implies `|A|>=2|R|` | Full universal paper proof | Challenge real phases, a=1, or sparse dyadic levels |
| DYO-02: coefficient 2 is sharp for every odd d | Explicit all-scale construction | Exact full cell check at composite odd d |
| Endpoint capacity bound outside one odd part | REFUTED | Published v=12 capacity 3/2 |
| General {2,3}-smooth obstruction | REFUTED | Published positive-gain rule |
| Academic novelty | UNVERIFIED | Independent bibliographic and proof review |

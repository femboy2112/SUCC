# The arithmetic of predictable future times

**Authority:** elementary proofs below; classical semigroup ancestry;
new SUCC interface and finite realization package. No scholarly priority claim.
The finite programs corroborate these proofs and verify certificates; they do
not supply the universal quantifiers.

## KV-H1 — The source-relative horizon monoid

Let D be a nonempty set, T:D→D a total map, and h:D→Y a report with Y=h(D).
An invariant subdomain may replace D, but that domain must be declared before
the theorem is used. Define

\[
H(T,h)=\{n\in\mathbb N_0:\exists g_n:Y\to Y,\quad h\circ T^n=g_n\circ h\}.
\]

Thus n is a predictable horizon when **every source state with the same
present report has the same future report at that horizon**. This is a
global same-report statement. A single target or a single realized report
fiber has different quantifiers (KV-H6).

**Theorem (PROVED LOCAL / CLASSICAL).** The decoder g_n is unique whenever
it exists. Zero belongs to H. If m,n belong to H, then m+n belongs to H and

\[
g_0=\operatorname{id}_Y,\qquad
g_{m+n}=g_m\circ g_n=g_n\circ g_m.
\]

**Proof.** Surjectivity onto Y makes a decoder unique. For x∈D,

\[
h(T^{m+n}x)=g_m(h(T^nx))=g_m(g_n(h(x))).
\]

Reverse m,n and use T^{m+n}=T^{n+m}. This proves both additivity and
commutation on the actual report image. Identity handles zero. ∎

The exact obstruction at an excluded horizon is a pair

\[
h(x)=h(z),\qquad h(T^nx)\ne h(T^nz).
\]

Conversely, absence of any such pair permits the decoder to be defined by
the common value on each nonempty report fiber. In the finite module, a
positive certificate contains the complete decoder table; a negative
certificate contains this pair. Both are bound to a hash of the declared
transition and report tables. The hash binds mathematical input bytes,
not empirical adequacy of a model of an external carrier.

**Antecedent.** A map admitting such a decoder preserves the fiber partition
of h. Partition-preserving transformation semigroups are classical; see
Araújo–Bentz–Mitchell–Schneider, [primary paper](https://arxiv.org/pdf/1404.1598),
introduction. H is the inverse image of that submonoid under n↦T^n.

## KV-H2 — Every nonzero horizon monoid has finite arithmetic structure

**Theorem (PROVED LOCAL / CLASSICAL).** If H≠{0}, put
m=min(H\{0}). Let R be the residues modulo m represented in H. For each
r∈R let a_r be the least member of H of that residue, with a_0=0. Then

\[
\boxed{H=\bigcup_{r\in R}(a_r+m\mathbb N_0).}
\]

Consequently H is generated additively by the finite set consisting of m
and the nonzero a_r. If d is the gcd of its positive members, then for all
sufficiently large n,

\[
n\in H\quad\Longleftrightarrow\quad d\mid n.
\]

**Proof.** If n∈H has residue r, minimality gives n≥a_r, so
n=a_r+km for k≥0. Conversely each such sum belongs to H by KV-H1. The
residues R form a submonoid of the finite group Z/mZ. Every element has
finite additive order, so its inverse is a nonnegative multiple of itself;
R is a subgroup. Every subgroup of Z/mZ consists of the multiples of a
divisor of m. That divisor is precisely gcd(H)=d, by the displayed finite
generators. For n≥B=max_r a_r, membership is therefore exactly d|n. ∎

The case H={0} has no positive predictable time and must remain separate.
This theorem needs **no finite-state assumption**. It describes a hidden
arithmetic regularity of every global report-prediction problem of this
type, even with an infinite carrier.

It does not provide an algorithm to discover m, R or the a_r from arbitrary
observations of an unknown source. A finite scan of horizons through B cannot
distinguish {0} from (B+1)N_0. KV-H4 realizes both on finite sources of
unspecified size. Supplied laws or a separately authenticated complexity
bound can resolve that uncertainty.

This is the standard elementary structure of submonoids of N_0, applied
to report horizons. For classical antecedents see Assi–García-Sánchez,
[Numerical Semigroups and Applications](https://arxiv.org/pdf/1411.6093),
§1, Propositions 1–3 and Lemma 4 (gcd normalization, finite generation,
and Apéry representatives). The threshold B is safe, not necessarily the
least conductor or the minimal presentation.

### Two certified coprime strides cover the distant future

If a,b≥1 belong to H and gcd(a,b)=1, then

\[
n\ge(a-1)(b-1)\Longrightarrow n\in H.
\]

For each n choose j∈{0,…,a−1} such that jb≡n (mod a). Then n−jb is
a multiple of a, and for n≥ab−a−b+1 it is greater than −a, hence
nonnegative. Thus n=ia+jb with i,j≥0; compose the two certificates.
This is a sufficient threshold inherited from the generated submonoid;
additional predictable horizons can lower it. The a=1 case gives every
horizon immediately by induction, with computation cost still separate.

## KV-H3 — Reversible finite sources have no transient holes

**Theorem (PROVED LOCAL / CLASSICAL COROLLARY).** If D is finite and T
is a permutation of order L, then

\[
H=d\mathbb N_0\quad\text{for some positive divisor }d\mid L.
\]

**Proof.** For n∈H, hT^n is onto Y because T^n is onto D, so g_n is
onto Y and, by finiteness, bijective. Its inverse supplies a decoder for
T^{-n}: from hT^n=g_nh compose with T^{-n} and then g_n^{-1}.
The admissible residue classes in the finite cyclic group generated by T
therefore form a subgroup. Such a subgroup consists precisely of the
multiples of a divisor d of L. Pulling back to N_0 proves the formula. ∎

**Sharp four-state example.** T=(0→1→2→3→0), h=(0,0,1,1).
Then H=2N_0. The observer can predict every even future report and cannot
predict an odd one globally. Two steps swap reports; four restore them.
Time-two certainty does not imply time-one certainty.

For a noninvertible source, take a→b→c→c with h(a)=h(b)=0,h(c)=1.
The fiber {a,b} splits after one step but merges at c after two. Hence
H={0,2,3,4,…}. This example is information loss, not evidence that a
longer horizon is always harder to predict. A persistent independent tag
can be adjoined if a nonconstant surviving report is desired.

Finiteness in the reversible theorem is also essential. On the countable
carrier Z×{0,1}, let T(k,b)=(k+1,b), a bijection. Merge the two tracks in
the report exactly at k∈S={0,2,3,…}; elsewhere distinguish both k and b.
The same translation argument as KV-H4 gives H=S: a positive shift preserves
every merged fiber exactly when it belongs to S. Thus an infinite reversible
source can have a transient horizon hole.

## KV-H4 — Complete realization: every allowable arithmetic pattern occurs

**Theorem (PROVED LOCAL; classical synthesis).** The sets H(T,h) for
finite deterministic reported sources are **exactly** the additive
submonoids of N_0.

Necessity is KV-H1. For sufficiency let S≠{0} be any additive submonoid.
By KV-H2 choose d=gcd(S) and c≥1 such that n≥c implies
(n∈S iff d|n). Let

\[
Q=\{0,\ldots,c+d-1\},
\]

with successor j↦j+1 except c+d−1↦c. Write ρ(n) for the state reached
from 0 at time n. Membership in S is well-defined on ρ(n): before c it
is exact, and afterward both the automaton and membership have period d.
Let A={ρ(n):n∈S}.

Use two tracks D=Q×{0,1}, with T(q,b)=(succ(q),b), and report

\[
h(q,b)=
\begin{cases}
(q,*),&q\in A,\\
(q,b),&q\notin A.
\end{cases}
\]

The only nontrivial report fibers are the two tracks at one marked q.
If k∈S and q=ρ(n) is marked, n∈S implies n+k∈S, so T^k preserves
that fiber. Thus k∈H. If k∉S, the two states (0,0),(0,1) initially
agree because 0∈S, but disagree at time k. Thus k∉H. Therefore H=S.
The construction uses 2(c+d) states. For S={0}, use Q={0,1}, successor
0→1→1, and A={0}, producing four states and no positive horizon. ∎

This construction is a declared **candidate-state domain with two tracks**.
It is not a single unary orbit from one known basepoint. It does not change
the literal zero of the original BBP source, nor claim arbitrary horizon
patterns for that selected orbit.

The implementation obtains Apéry representatives by shortest paths on
residues modulo the least supplied generator. Edges add a generator with
that generator as positive cost. Path costs are exactly represented sums;
the least path cost in a residue is therefore its least represented member.
An unreachable residue is retained as such. The empty generator list
denotes {0}. This computes the consequences of a **given** generator set;
it does not infer generators from sampled behavior.

## KV-H5 — Effective finite-source verification

For an explicitly supplied finite table, enumerate the complete transformations
I,T,T²,… until T^(μ+p)=T^μ. There are finitely many maps D→D, so this
terminates in principle. Multiplication by subsequent powers shows equality
continues at every later step. Test report descent at each n<μ+p. This
finite certificate determines H at every horizon, including very large ones.

The verifier checks actual whole-table equality at the closing powers,
the intermediate report collisions, and the source fingerprint. Repeated
Boolean answers alone would not certify recurrence. A runtime budget that
expires before power-table repetition yields an explicit failure to obtain
a certificate, never an assumed plateau. The resulting μ,p describe the
source power orbit and need not be minimal for the Boolean horizon profile.

Individual horizons can instead be checked by binary exponentiation of T,
using O(|D| log(n+1)) table operations and O(|D|) working state. The input
table and source verification costs have already been paid. This is a
computational macro, not zero physical work.

## KV-H6 — Two scope mutations that break the addition law

**Different target.** Let T=(0→1→2→3→0), h=(0,0,1,2), and
P=(0,0,0,1). Define J={n:P T^n is determined by h}. Directly
J={0,1,4,5,…}. In particular 1∈J and 2∉J. Decoders into a different
target space cannot automatically compose as endomorphisms of the report.

**One realized fiber.** Let T=(2,3,0,3), h=(0,0,1,1), and examine
only the present fiber {0,1}. Its future report is constant at horizons
0 and 1 but not 2. The output fiber reached at one step was never certified
to evolve unambiguously. Global descent closes exactly that missing step.

These are exact counterexamples, implemented as regression controls. They
prevent the arithmetic theorem from swallowing the broader question of
every individually requested future target.

## KV-H7 — Programmable paths can require infinitely many word generators

The single-successor theorem does not transfer unchanged to arbitrary
labelled action words. On D={0,1,2,3}, use action tables
a=(1,1,3,3), b=(0,0,0,0), and h=(0,1,0,2). A word is executed in its
written chronological order. The words admitting full-report descent are
exactly

\[
W=\{\varepsilon\}\cup\{a,b\}^*b\{a,b\}^*.
\]

**Proof (PROVED LOCAL / COUNTERMODEL).** The map a is idempotent, and
the initially equal-report states 0 and 2 acquire reports 1 and 2 after a.
Every nonempty a-only word therefore fails. At the first occurrence of b,
every state is reset to 0; the remainder of the word preserves constancy
of the full source map. Every word containing b therefore descends. ∎

This certifies the reported endpoint after the actions; it does not recover
original source bits erased by the reset.

The language W is regular and closed under concatenation, but is not finitely
generated as a word monoid. Every a^n b contains exactly one b, whereas a
product of two nonempty admitted words contains at least two. Each a^n b
must consequently appear in any generating set; there are infinitely many.

The finite **image** monoid of transformations remains finite and finitely
generated. It is the language of arbitrary program words that lacks a finite
generating list. A finite automaton recognizes that language nevertheless.
Thus finite description, finite word generation, and finite source state
are distinct contracts. This is relevant when the exploring SUCC automata
can choose different actions instead of only advancing one fixed clock.

## Next falsification opportunity

Supply an independently justified source/report model, predict a complete
horizon profile before testing its trajectories, and try to find a same-report
pair that violates a proposed decoder. For a genuinely unknown carrier,
the first unpaid obligation is the source model, not the additive proof.
For the authenticated BBP source, any transfer needs an actual invariant
report and checked source equations; no such bridge to signed cancellation
is asserted here.

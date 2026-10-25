# Joint prime observers and the compactness of the authentic carrier

**Date:** 2026-10-24. **Status:** elementary paper deductions with explicit
classical and inherited inputs. No new executable result, Lean authority,
external refereeing, or normality theorem is asserted.

**Pinned concurrent source:** draft [#277](https://github.com/femboy2112/SUCC/pull/277),
`research/pi-joint-prime-carrier-2026-10-24` at
`e9ad0fc3479c8182d19046831006c423ea68ee85`, based on #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
Its [joint-carrier dossier](https://github.com/femboy2112/SUCC/blob/e9ad0fc3479c8182d19046831006c423ea68ee85/research/2026-10-24/PI_JOINT_CARRIER_INTERFEROMETRY.md)
proves the four-pole residue law and finite-adelic noncompletion statements.
It was inspected as a sibling, not merged or treated as inherited code.
The required mod-p residue fact is proved again below.

## 1. The precise boundary for an all-observer compact limit

Every authentic rational BBP state is a valid finite adele. Its complete
primary phases also reconstruct its real circle phase exactly. These facts
do not put the entire time trajectory in one compact subset of the finite
adeles, or make its empirical measures converge to a probability there.

This note proves:

- The authentic forcing eventually leaves every compact subset of the
  finite adeles. An independent argument from #277's four-pole CRT law
  proves density-zero occupation of every such compact.
- The recurrence alone then bounds the upper occupation of every compact
  by the unwrapped source at one half. The inherited source denominator
  theorem strengthens this to eventual departure from every compact.
- Consequently the corresponding finite-adelic occupation probabilities
  have no weakly convergent subsequence with a probability limit.
- The standard finite-adelic character into the real circle remains
  continuous. Its circle-valued occupation laws live in a compact space;
  their possible convergence to Haar is not excluded or proved here.

These are classical topological consequences applied to the authenticated
source. They constrain a proposed compact carrier model; they are not new
normality criteria or claims of scholarly novelty.

## 2. Source and topology

Keep the exact source and initial condition:

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),
$$

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}
{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$

For positive integers n, the denominator is positive, and
`120n^2-89n+16 >= 31n^2+16 > 0`. Thus r(n)>0. Comparing degrees gives
r(n)->0 in the real topology, with `n^2 r(n)->15/64`.

Write

$$
\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p),\qquad
\widehat{\mathbb Z}=\prod_p\mathbb Z_p.
$$

The prime denotes the restricted product: an adele is integral at all
but finitely many primes. Its topology has basic neighborhoods integral
outside a finite prime set. In particular Zhat is compact and open.
Every rational is embedded diagonally in A_f. Define empirical measures

$$
\eta_N=\frac1N\sum_{n=1}^N\delta_{r(n)},\qquad
\nu_N=\frac1N\sum_{n=1}^N\delta_{U_n}
$$

on this specific topological space. They are distinct from the empirical
circle laws of y_n=[U_n].

### Compact sets have a common denominator budget

For each positive integer m, let

$$
K_m=(m!)^{-1}\widehat{\mathbb Z}.
$$

These are nested compact open subsets and their union is A_f. Indeed,
each adele has only finitely many negative valuations, each of finite
depth; a sufficiently large factorial clears all of them. The open sets
K_m cover any compact K, so a finite subcover and nesting give

$$
K\subseteq D^{-1}\widehat{\mathbb Z}
\quad\text{for some positive integer }D.
\tag{AC-1}
$$

In particular K is integral outside the finite set of primes dividing D.
For a rational x,

$$
x\in D^{-1}\widehat{\mathbb Z}
\quad\Longleftrightarrow\quad Dx\in\mathbb Z.
\tag{AC-2}
$$

The reverse implication is immediate. For the forward implication, the
rational number Dx is integral at every prime, so its reduced denominator
has no prime divisor and equals one.

## 3. Four-pole CRT proof of density-zero compact occupation

This section derives the occupation statement from the precise
source-specific lemma in #277, with its elementary proof included.

### The mod-p forcing lemma

For every prime p>=7, the event v_p(r(n))<0 is the union of exactly four
residue classes modulo p:

$$
8n\equiv7,\qquad8n\equiv3,\qquad
2n\equiv1,\qquad4n\equiv1\pmod p.
\tag{AC-3}
$$

To prove this, use the equivalent four-term expression

$$
r(n)=\frac4{8n-7}-\frac1{8n-3}
-\frac1{2(2n-1)}-\frac1{2(4n-1)}.
$$

The four rational roots are 7/8,3/8,1/2,1/4. Their pairwise differences
have numerators among 1,3,5 after powers of two are removed, so they
remain distinct modulo p>=7. At any one of the roots, exactly one
denominator is divisible by p, its coefficient is a p-unit, and the
other three terms are p-integral. The unique negative valuation cannot
cancel. Away from these roots all four terms are integral. This proves
(AC-3). The same argument at depth k gives four classes modulo p^k
for the event v_p(r(n))<=-k.

For a fixed finite set P of distinct primes >=7, CRT therefore gives
the exact limiting density

$$
\lim_{N\to\infty}\frac1N
\#\{1\le n\le N:\ v_p(r(n))\ge0\text{ for every }p\in P\}
=\prod_{p\in P}\left(1-\frac4p\right).
\tag{AC-4}
$$

This is ordinary counting on complete periods of length `product_(p in P) p`,
with a vanishing endpoint error. It is a statement about the instantaneous
forcing, without an independence claim for propagated state histories.

### The density theorem

**For every compact K subset A_f, eta_N(K)->0.**

Choose a finite S outside which K is integral using (AC-1). For any fixed
finite P of primes >=7 outside S, the event r(n) in K implies all the
integrality events in (AC-4). Hence

$$
\limsup_{N\to\infty}\eta_N(K)
\le\prod_{p\in P}\left(1-\frac4p\right).
\tag{AC-5}
$$

Euler's classical divergence of `sum_p 1/p` implies that these finite
products tend to zero as P exhausts the primes outside S: use
`log(1-4/p)<=-4/p`. Thus the limsup is zero, proving the claim.
The limit order is explicit: fix P, take the time limsup, then enlarge P.
No uniformity in a growing modulus is assumed.

## 4. A stronger elementary fact: the forcing eventually leaves every compact

The density proof has an independent, stronger verification. It needs
only rationality, real decay, and eventual nonvanishing, not pole counts
or prime-distribution theorems.

**Lemma.** If nonzero rational numbers a_n tend to zero in R, then their
diagonal images eventually leave every compact subset of A_f.

**Proof.** By (AC-1)--(AC-2), membership of a_n in a fixed compact K
requires `D a_n` to be a nonzero integer for some fixed D. It would follow
that `|a_n|>=1/D`. Real convergence to zero eventually contradicts that
inequality. QED.

The authentic forcing satisfies these hypotheses. Therefore

$$
\forall K\subset\mathbb A_f\text{ compact},\quad
\exists n_K\quad\forall n\ge n_K:\ r(n)\notin K.
\tag{AC-6}
$$

This sharpens (AC-5), and shows why its compactness conclusion alone is
not a source-selection invariant: many changed positive rational forcings
with real limit zero obey the same conclusion. The four-pole law supplies
more detailed source-specific local statistics, not a necessity for (AC-6).

## 5. Consequences for the accumulated source

### A recurrence-only upper bound

For every compact K subset A_f,

$$
\limsup_{N\to\infty}\nu_N(K)\le\frac12.
\tag{AC-7}
$$

To prove it, the set `L=K-16K` is compact by continuity of addition and
scalar multiplication. Let `a_N=nu_N(K)`. The fraction of preceding
states `U_0,...,U_(N-1)` in K differs from a_N by at most1/N. The fraction
of n for which both U_(n-1) and U_n belong to K is therefore at least
`2a_N-1-1/N`. Every such n has r(n) in L by the literal recurrence.
Consequently

$$
2\nu_N(K)\le1+\frac1N+\eta_N(K-16K).
$$

Apply the forcing density theorem, or (AC-6), to obtain (AC-7).
This proof requires no source equidistribution, irrationality statement,
or prime-number theorem. It does not by itself give density-zero state
occupation of K.

### The inherited denominator theorem strengthens the conclusion

Let d_n be the individual positive reduced denominator of U_n.
[PI_PASCAL_PRIME_HEIGHT.md](PI_PASCAL_PRIME_HEIGHT.md), PH-5 / (PH-10),
already proves

$$
(3+o(1))n\le\log d_n\le(8+o(1))n.
$$

That inherited paper theorem uses the classical prime number theorem in
the two fixed residue classes 1 and5 modulo8. It is not newly proved here.
Only its consequence d_n->infinity is needed for the next step.

For K contained in `D^{-1}Zhat`, membership U_n in K forces d_n to divide
D by (AC-2). Once d_n>D this is impossible. Hence the authenticated
source itself satisfies

$$
\forall K\subset\mathbb A_f\text{ compact},\quad
\exists n_K\quad\forall n\ge n_K:\ U_n\notin K.
\tag{AC-8}
$$

Thus nu_N(K)->0 as well. This stronger result has an explicit additional
input, the inherited denominator theorem; it is not silently inferred
from the recurrence-only one-half bound.

## 6. Non-tightness and absence of a probability limit in A_f

A family of probability measures is tight if for every epsilon>0 one
compact set contains mass at least1-epsilon uniformly over the family.
Equations (AC-6) and (AC-8) show that neither authentic occupation family
is tight. The weaker recurrence-only estimate (AC-7) already suffices
for non-tightness of the state occupations.

One can exclude weakly convergent probability subsequences directly.
The compact open sets K_m from Section2 have bounded continuous indicators.
If a subsequence of eta_N converged weakly to a probability eta, then
eta(K_m)=0 for every m. Since `K_m` increases to A_f, this would give
eta(A_f)=0, a contradiction. With (AC-8) the same proof applies to nu_N.
Even using only (AC-7), a hypothetical probability limit nu would obey
nu(K_m)<=1/2 for every m, and hence nu(A_f)<=1/2, also impossible.

With the stronger eventual-departure statements, both empirical families
converge vaguely to zero: every continuous compactly supported test has
time mean tending to zero. This is escape of mass in the finite-adelic
topology, not loss of mass under their compact circle projections.

The same reasoning also validates #277's no-continuous-extension result.
A continuous map `F:Zhat->A_f` has compact image, so cannot agree with
all r(n) or, using (AC-8), all U_n. Without invoking source height, a
continuous extension of U would produce the forbidden forcing extension
`F(z)-16F(z-1)` at positive integers n>=2. No value at the exceptional
initial index is needed for that contradiction.

## 7. The finite-adelic character is continuous

For x in A_f define

$$
\chi_f(x)=\prod_p\exp(2\pi i\{x_p\}_p).
\tag{AC-9}
$$

Here `{x_p}_p` is the p-adic fractional part. All but finitely many factors
are one. Additivity modulo integers makes chi_f a character. Its kernel
is exactly Zhat: a finite sum of rational primary parts is an integer
only when each primary part is zero, by primary decomposition of Q/Z.
Since Zhat is open, chi_f is locally constant and continuous on A_f.

For diagonally embedded rational q, CRT gives

$$
q-\sum_p\{q\}_p\in\mathbb Z,
\qquad \chi_f(q)=\exp(2\pi i q).
\tag{AC-10}
$$

The primary convention and this classical identity are given in Keith
Conrad, [The Character Group of Q](https://math.stanford.edu/~conrad/154Page/handouts/characterQ.pdf),
Section2, especially (2.1). The plus sign in (AC-9) is chosen to give
(AC-10); the character on all adeles trivial on diagonal rationals uses
the complementary Archimedean sign.

This continuity is compatible with #277's moving-prime counterexample.
For odd primes q tending to infinity, let `x_q=(q-1)/(2q)`. Its primary
coordinate at every fixed p is eventually zero, so it tends to zero in
the product topology on the direct sum of **discrete primary torsion
groups**. Its real phase tends to1/2. The algebraic summation readout is
therefore discontinuous for that product topology.

However x_q does not tend to zero in A_f: it never belongs to the open
neighborhood Zhat, because its q-adic valuation is negative. The true
restricted-product topology and the weaker primary-coordinate product
topology are different. Neither the moving-prime example nor (AC-6)
refutes continuity of the standard finite-adelic character.

## 8. What this says about the proposed coherent limit

The authentic source supports exact algebraic all-prime reconstruction.
It does not support a compact finite-adelic model containing every raw
state, or a probability occupation limit on that raw carrier. This is
a precise obstacle to one particular compact-limit proposal, including
an independently Haar-sampled prime-time completion.

Coarse circle projection is legitimate. The pushforwards of nu_N under
chi_f are exactly the source circle laws, and the circle is compact.
They may have probability subsequential limits even though nu_N has none
in A_f. Nothing here selects Haar among those circle limits. The same
distinction leaves room for other quotients, path spaces, and measurable
models whose source and carry decoder are independently authenticated.

The next missing theorem remains a source-derived bound on real coarse
collisions or on the complete mixed character sum. A proof must retain
the actual four-pole recurrence, initial value, literal carries and the
chosen limiting topology. A compactness assertion for all local data
cannot replace that statistical estimate.

**Falsification boundaries:** a constant integral source stays inside
Zhat, so the forcing escape claim requires eventual nonzero real decay.
The mod-p pole proof excludes3 and5, where numerator cancellation occurs.
The recurrence alone yields (AC-7), while (AC-8) explicitly imports
denominator growth. A purported contradiction with character continuity
must use the restricted-product topology, not merely fixed-coordinate
convergence. No finite experiment is promoted to any universal statement.

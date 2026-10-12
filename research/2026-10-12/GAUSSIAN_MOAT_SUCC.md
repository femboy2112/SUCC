# Gaussian moats: finite path certificates and information transport

Research checkpoint started 2026-10-12 UTC.

## Hole contract, before implementation

**Author's target.** Learn the recent OpenAI Gaussian-prime walk proof and
build real ObsSUCC components toward matching or improving its elegance.
This does not assume that changing notation supplies an independent proof.

**Baseline.** SUCC `main` at
`68b33157df2086355c00300fc7b534251f6b09c0`; research branch
`research/gaussian-moat-certificate-duality-2026-10-12`. The existing
`research/gaussian-moat-voltage-transport-2026-10-11` pointed to that same
main commit when inspected; no work on that branch was overwritten.
The 566-test baseline passed after installing its declared optional
`mpmath` dependency. The initial ten import errors were an environment
dependency gap, not mathematical or code regressions.

**Primary source.** OpenAI, *Bounded-Step Walks on Gaussian Primes*, dated
2026-09-26, released 2026-10-06, `openai/math` at
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Its finite-sieve existence
theorem remains an explicitly imported premise in the all-step algorithm.

**Proposed exact statement.** Let a graph on a periodic subset of
`Z^d` have period `Q Z^d` and a finite symmetric nonzero integer step
alphabet. Retain the actual displacement on every quotient edge,
including loops and parallel edges. Every lifted component is finite
if and only if every quotient closed walk has zero total displacement,
if and only if an integer vertex potential integrates every edge.
The alternative is a finite closed-walk witness with nonzero translation.

**Initial truth state.** Candidate elementary consequence of classical
covering/voltage-graph theory; to be proved explicitly and independently
checked. No academic priority claimed. Gaussian sieve containment is an
additional arithmetic premise, not an implication of abstract holonomy.

**Weakest sufficient form and leverage.** The forward certificate alone
proves a uniform bound for all infinitely many lifts of one finite sieve.
An exact decision algorithm for both outcomes permits a terminating
prime-prefix search, conditional on the published finite-sieve existence
theorem. It does not replace that theorem's entropy/geometry argument.

**Novelty tax.** This is a classical general theorem and a new-to-project
certificate interface. A certificate for one finite sieve is strictly
weaker than the all-step Gaussian moat theorem; many inputs fail it.
The genuine gain sought is a checkable finite proof object and a sharper
bound from actual component sizes, with explicit finite exceptions.

**Known failure mechanisms.** A finite quotient may hide an infinite
translated path. Dropping loops, parallel edges, displacement labels,
Gaussian conjugate factors, source checks, or exceptional primes can
produce false certificates. A leaking sieve is not a prime walk.

**Cheapest falsifiers and fresh region.** Single-residue self-loop;
two parallel edges with distinct lift displacements; finite disconnected
islands; the same Gaussian sieve before/after adding diagonal steps;
forged potential and changed prime/step data. Check unrelated small
periodic masks against explicit lifted connected components. Resource
exhaustion is unresolved and must never become a confinement verdict.

**Second dependency cut.** Generalize the source's common-law information
telescope to typed moving observer states with an explicit shared update
transcript. Prove a conditional-entropy continuity bound that depends
only on the finite word alphabet, removing the receiver-state alphabet
size from that estimate. Test whether the source's `2 H(S)` transport
charge can be lowered; retain a counterexample if it cannot.

**Boundary.** Exact integer certificate verification can lift finite data
to a universal statement only through the proved periodicity theorem.
Floating entropy diagnostics do not prove inequalities. No Lean build,
new independent Gaussian moat proof, new physical law, or RH result is
assumed or claimed.

**Next lamp.** A source-derived construction of zero-displacement
certificates for arbitrary step alphabets without importing OpenAI's
finite-sieve existence theorem; or a strictly simpler proof of its
coverage/information lower bound.

## 1. What the source actually establishes

Let the Gaussian primes be the irreducible elements of `Z[i]`, including
all associates. Join distinct primes when their Euclidean distance is at
most a fixed real number D. The published theorem is

\[
\forall D\in\mathbb R\quad\exists B_D\in\mathbb N\quad
\forall C\in\pi_0(G_D):\ |C|\le B_D.
\]

Thus every injective finite walk also has at most B_D vertices. An
infinite back-and-forth walk on a finite component is not excluded.
The source supplies no explicit numerical function D -> B_D.

The stronger intermediate theorem supplies, for each D >= 1, a finite
set P of rational primes congruent to 1 modulo 4 for which the periodic
norm-avoiding set has no infinite injective D-step walk. This is the
load-bearing arithmetic existence theorem, not a consequence of the
finite quotient being finite.

The paper develops geometry of walk differences, entropy enrichment,
coverage from common continuation data, and an information charge for
each prime batch. A common sampled-time law lets the charges telescope
against the bounded increment alphabet; suitable prime batches force
the charges to exceed that budget. Periodicity and a finite exceptional
set then give the prime-component conclusion. See the pinned source
files in [the source manifest](GAUSSIAN_SOURCE_MANIFEST.json).

The official [Lean scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/028.md)
and inspected endpoint `OAI.GaussianMoat.fullMain` include the universal
component and finite-walk bounds, axes and all associates. The solution
directory contains 41 files. Static inspection found no `sorry`, `admit`,
custom `axiom`, or `unsafe` declaration there. The separate comparator
challenge's placeholder is not the solution. **Lean was not rebuilt in
this session**; published formalization and source inspection are the
precise verification claim. Its toolchain is Lean v4.34.1 with Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

The formal development already includes a discrete rectangular Sperner
route for the geometric difference lemma. This is OpenAI's contribution,
not a SUCC rediscovery. No manuscript defect was identified in the
audited interfaces. That audit is not a replacement for executing Lean.

## 2. The actual ObsSUCC object

The carrier here is an integer lattice with declared legal steps. A
residue observation forgets the lattice translate. An observed path must
therefore retain both its residue endpoints and its actual displacement.

Fix d >= 1, Q >= 1, R a subset of `{0,...,Q-1}^d`, and a finite symmetric
step set S in `Z^d \ {0}`. Put A = R + Q Z^d. A quotient dart is a pair
(r,s) with r in R, s in S, and r' = r+s mod Q in R. Its true label is s;
its deck label is

\[
\tau(r,s)=\frac{r+s-r'}Q\in\mathbb Z^d.
\]

Several s can connect the same residue pair, and r'=r is allowed. The
integer lattice graph has no zero-step loops; such a quotient loop can
represent a nonzero physical translation. Dropping it changes the graph.

For a composable path gamma, define Omega(gamma) as the sum of its true
labels. It preserves concatenation and changes sign under path reversal.
This is an actual additive functor on the free path groupoid of the
quotient graph. A path's endpoint residues alone do not determine Omega.
No full categorical equivalence, physical observer model, or use of the
Yoneda lemma is needed to assert this elementary construction.

### P1. Finite certificate / escaping-translation dichotomy

For each connected quotient component C, the following are equivalent:

1. All components of the lattice lift above C are finite.
2. Every closed quotient walk in C has total true displacement zero.
3. There is g:C -> Z^d with g(r) = r mod Q and
   `g(r') - g(r) = s` on every dart.

When these hold, every lift component above C has exactly |C| vertices.
If every step has norm at most D, its diameter is at most (|C|-1)D.
If they fail, a finite closed quotient word with nonzero displacement
certifies an infinite component of the periodic graph.

**Proof.** Choose a root and a spanning tree in C. Set g(root)=root and
propagate g along its true step labels. If every closed-walk sum is
zero, the tree-path value is independent of path and every edge equation
holds. Conversely those equations telescope to zero on a closed walk.

For such a g, the set `{g(r)+Qk:r in C}` is connected, contains exactly
one vertex over each r, and is closed under every legal edge. These are
precisely the lifted components, proving the size and diameter claims.

If a dart u --s--> v violates the tree potential, follow the tree from
the root to u, take this dart, and follow the reversed tree path from v
to the root. Its displacement is g(u)+s-g(v), a nonzero element of Q Z^d.
Repeated translates of this walk give infinitely many distinct lattice
vertices in one component. Local finiteness supplies an injective ray
by the finitely branching tree of finite simple paths. This proves the
contrapositive of (1) -> (2) and exhausts the alternatives. QED.

The group Z^d is torsion free. Over a finite deck group, a nonzero loop
label can generate only finitely many sheets; that would be a different
theorem. The groupoid/coboundary language is classical voltage-graph
theory; see [Schluchter, section 3](https://arxiv.org/html/1501.01060v1),
which cites Gross and Tucker, *Topological Graph Theory*. The argument
above proves the needed lattice specialization directly.

**Implementation.** `analyze_periodic` constructs either the potential
or the translated closed word. `verify_confinement` regenerates every
edge and independently uses disjoint sets for component counts.
`verify_translation` follows the declared word in integer coordinates.
The certificate digest binds an exact finite graph; it does not
authenticate an external physical source.

### P2. A positive proof transports through source refinement

Suppose Q' is a positive multiple of Q, the fine allowed lattice points
are contained in the coarse allowed set, and the fine steps are contained
in the coarse steps. Let g be a coarse P1 potential. For a fine residue
r, write x=g(r mod Q), and define componentwise

\[
g'(r)=x-((x-r)\bmod Q').
\]

Then g' is a valid fine potential. Its component-size bound cannot
exceed the original bound.

**Proof.** Along a fine dart r --s--> v, x changes by s. Since
v-r = s mod Q', the residue of x-r modulo Q' stays constant. Hence
g'(v)-g'(r)=s, and g'(r)=r mod Q'. Fine components are subgraphs of coarse
components, which proves the size bound. QED.

This is a concrete continuation of the earlier SUCC proof-support
transport work: the source map and hypotheses are independently
checkable arithmetic inclusions. A new prime may cut a negative path,
so a leaking witness does not enjoy the same monotone transport.

## 3. Arithmetic source and finite exceptions

For a finite set P of distinct rational primes, define

\[
A(P)=\{a+bi:\ p\nmid a^2+b^2\text{ for every }p\in P\}.
\]

This generalizes the source paper's split-prime sieve while preserving
its containment direction. Its period is Q = product(P). The empty
product gives Q=1 and the whole integer lattice.

| Prime type | Surviving pairs modulo p | Exceptional Gaussian primes |
|---|---:|---|
| p=2 | 2 | Four points +/-1 +/-i, norm 2 |
| p=1 mod 4 | (p-1)^2 | Eight associates of the two conjugate norm-p factors |
| p=3 mod 4 | p^2-1 | Four axial points +/-p, +/-ip, norm p^2 |

**Derivation.** For a split p choose t with t^2=-1 mod p. The norm factors
as (a+tb)(a-tb); the two distinct vanishing lines meet only at zero. For
inert p a nonzero norm-zero pair would give a square root of -1, so only
(0,0) is removed. For p=2 the surviving pairs have a+b odd. The CRT
multiplies the local survivor counts.

The Gaussian-prime classification gives: an off-axis point is prime
exactly when its norm is a rational prime; an axial point is prime
exactly when its nonzero coordinate has prime absolute value 3 mod 4.
Thus the table lists exactly the Gaussian primes removed from A(P).
Writing their union as E(P),

\[
\mathcal G\subseteq A(P)\cup E(P),\qquad A(P)\cap E(P)=\varnothing.
\]

These are elementary number-theoretic facts also used by the source
paper's `periodicity.tex` and published Lean prime classification.
All factors and inert exceptions are checked explicitly in the code.
A composite such as 6 is rejected as a declared prime source.

### P3. Exact contraction of finite exceptional attachments

Let A satisfy P1, with physical potential g, and let E be any finite
disjoint set. Label each z in A by

\[
\ell(z)=\left(C(z\bmod Q),\frac{z-g(z\bmod Q)}Q\right).
\]

This identifies its entire lifted A-component, whose weight is |C|.
Build a finite graph containing every point of E with weight 1 and every
A-component incident to E with weight |C|. Insert all E-E adjacencies
and all E-component incidences, using every declared step. If M is the
maximum quotient-component size, then

\[
\max\{|K|:K\in\pi_0(A\cup E)\}
=\max\left(M,\max_{J\in\pi_0(\text{finite attachment graph})}
                 \sum_{v\in J}w(v)\right).
\]

Empty maxima are zero.

**Proof.** Labels are constant along an A-edge by the potential equation.
Two labels cannot overlap: a shared lattice point would force the same
residue component and translation. Each labeled set is connected and
has exactly its assigned weight. Distinct A-components have no edges
between them. Contracting the finitely many components incident to E
therefore preserves exactly the affected connectivity and cardinality.
All untouched components retain their sizes, and finitely many E points
leave untouched translates of every component type. QED.

This replaces a degree overcount by an exact finite computation for the
enlarged sieve. The source's bound for its split-prime formulation uses
Q^2 and the total possible degree. Even after replacing Q^2 by M, the
coarse estimate is only `max(M,e+e|S|M)`. P3 can be substantially smaller.
The resulting upper bound for **actual prime** components need not be
optimal: composites and units remain in A(P).

## 4. Exact benchmark results

All step inputs are integer squared distances; no floating square-root
comparison occurs. These are explicit small-step certificates, not a
record claim or an all-step existence computation.

| P | Squared step bound | Q | Residue vertices | Largest sieve component | Largest A(P)+E(P) component |
|---|---:|---:|---:|---:|---:|
| 2 | 1 | 2 | 2 | 1 | 16 |
| 5,13 | 1 | 65 | 2,304 | 580 | 580 |
| 2,5,13 | 2 | 130 | 4,608 | 580 | 580 |
| 2,3,5,13 | 2 | 390 | 36,864 | 71 | 104 |

For the last row, the 24 exceptional primes attach to five periodic
components, giving one cluster of size 104. The coarse bound using M
would be 13,656. The exact contraction is useful, but 104 is still an
upper bound for the actual Gaussian-prime graph, not its optimal maximum.

The saved [complete certificate](GAUSSIAN_P2_5_13_D2_CERTIFICATE.json) is
the Q=130, squared-step-2 potential: it is 4,608 exact residue/potential
pairs, not a plot or a scan of a bounded prime box. Its independent
verifier reconstructs the arithmetic source and checks every edge.

Negative controls include P={5} at squared step 1, P={5,13} at squared
step 2, and P={2,5,13} at squared step 4. Each returns a finite nonzero
translation word. They demonstrate that **those sieve models** admit
escape; they do not construct infinite Gaussian-prime walks.

The [direct-lattice audit](INDEPENDENT_LIFT_AUDIT.json) uses a separate
implementation without quotient potentials or component labels. It
exhausts actual integer-coordinate BFS queues for the Q=130 and Q=390
benchmarks, confirms both complete component histograms, and directly
enumerates the exceptional clusters of 164 and 104 vertices. It uses
the same mathematical norm predicate, so it is implementation diversity,
not an independent source of the number-theoretic classification.

## 5. Effective certificate search and its exact dependency

The computable input is an integer squared step bound K >= 0, defining
the finite symmetric alphabet `{s in Z^2: 0 < norm(s)^2 <= K}`. One can
also supply a finite symmetric nonzero-step alphabet directly in Z^2.
The arithmetic termination claim here concerns the Gaussian plane; P1
itself applies more generally to Z^d. For a real distance bound D, an
integer K >= D^2 gives a sufficient input. No representation or exact
comparison oracle for an arbitrary real D is assumed.

Checking a finite P is decidable by P1. Enumerate larger initial segments
of the rational primes congruent to 1 modulo 4. If the source's finite
sieve theorem is accepted, some finite successful P exists. An initial
segment eventually contains P; deleting further vertices cannot create
an infinite component. The exact search must therefore halt.

This proves, **conditional on that stronger published theorem**, that a
computable certificate and component-bound function of the integer K
can be obtained by search. The source's word *nonexplicit* does not mean
*noncomputable* for this discrete input.
No useful advance estimate of runtime or modulus is supplied here.
The implementation exposes finite prime and cell caps; hitting a cap
returns `UNRESOLVED_*`. A returned positive certificate is sound without
appealing to the external theorem. The guarantee of eventual success is
what depends on that theorem.

### P4. Nested observation refinement does not imply finite certification

For n >= 1, let

\[
A_n=\{(x,y):2^n\mid3x+1\}\ \cup\ (2^n\mathbb Z)^2
\]

with unit coordinate steps. The A_n are nested periodic sets, each with
an infinite vertical column, yet their intersection is {(0,0)}.

**Proof.** Since 3 is invertible modulo 2^n, a column residue exists for
every n. Both the congruence columns and the dot lattices are nested.
The origin belongs to every dot lattice. A fixed nonzero point
eventually leaves the dot lattices. Remaining in all sufficiently fine
columns would imply that the nonzero integer 3x+1 is divisible by every
power of 2, impossible. QED.

In this example every finite periodic observer model permits escape;
the limiting source has only one point. Escape components recede as the
model is refined. This is a rigorous missing-uniformity phenomenon, not
a Gödel-independence theorem or a claim about physical Zeno dynamics.
It explains why the source's arithmetic finite-sieve theorem cannot be
obtained just by invoking observation refinement or a formal limit.

## 6. The information contribution

Full statements and proofs are in
[Entropy transport theorems T1-T5](ENTROPY_TRANSPORT_THEOREMS.md).
They give an exact shared-information identity, a sharp displacement
counterexample, a moving-state block theorem, and a nested information
budget with explicit update and sampling-law costs.

There is one concrete simplification to the published proof: apply
conditional-entropy continuity directly to the increment word given the
residue state. The continuity cost depends on the word alphabet only.
This removes the full-residue-alphabet size estimate from
`information.tex`, `lem:telescope`. It also supplies a more general
statement with a charged shared update transcript. It does not replace
the paper's geometry, coverage, prime-mass input or positive charge.

The attempted replacement `2 H(S) -> H(S)` is REFUTED under the general
conditional-translation hypotheses. A four-point, nonzero-residue
modulo-5 example attains equality in the two-entropy bound. This surviving
boundary is part of the framework improvement.

## 7. Validation and provenance boundary

The code has exact integer certificates and exact rational probability
structure checks. Entropies themselves are floating diagnostics. The
universal statements above and T1-T5 are written proofs; they are not
Lean formalizations of the new SUCC modules.

The final local suite passed all **597 tests**, including 19 new periodic
tests and 12 new information tests. The provenance, foundations and
ordinal checks passed. Fresh Gaussian and entropy receipts reproduced
the saved results, and the saved potential replayed against its rebuilt
arithmetic source. The [validation receipt](VALIDATION.json) records the
environment, exact commands, source boundaries and artifact checksums.

Adversarial tests retain nonzero self-loops, parallel edges, legal seam
crossings, zero-voltage cycles, wrong graph digests, malformed potentials,
wrong arithmetic primes, both conjugate factors, inert axis exceptions,
unpaid updates, correlated aliases, and sampling-law drift. A large
integer input is rejected by the cell budget before expensive primality
testing. Separate direct BFS audits compare actual lifted components.

Reproduce from the repository root:

```sh
python -m unittest discover -s tests -p 'test_*.py'
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/gaussian_moat_probe.py
python scripts/gaussian_moat_probe.py --verify research/2026-10-12/GAUSSIAN_P2_5_13_D2_CERTIFICATE.json
python scripts/entropy_transport_probe.py
python scripts/independent_gaussian_lift_audit.py
```

Source files were retrieved at the pinned OpenAI commit. All eight
manuscript source files matched their Git blob hashes; the manifest
records their URLs and SHA-256 checksums. Their contents are cited rather
than copied into this repository. The immutable RH import manifest was
not modified. All three assistant audit bearings used the same model
family; their agreement is not independent source corroboration.

## 8. Earned result and next moonshot

**Earned:** a general finite certificate dichotomy; explicit source
refinement of proofs; exact finite-defect attachment bounds; genuine
Gaussian benchmark certificates; an effective-search reduction with its
external premise exposed; a strict observation-limit counterexample; and
a shorter, more general proof of the common-law information budget.

**Not earned:** a new independent proof of the all-step Gaussian moat
theorem, superior optimal Gaussian bounds, academic priority, a physical
information law, or an RH implication.

The next arithmetic hole is precise: construct P(D) and an integrating
potential for all legal bounded steps, with a structural argument that
does not invoke the source's finite-sieve theorem. A weaker next target
is a reusable zero-displacement certificate constructor for a genuinely
new step family, with a quantitative modulus bound. Another route is to
replace the source's coverage-to-information lower-bound argument by a
simpler mechanism compatible with T5. Merely running more finite sieves
does not pay either proof obligation.

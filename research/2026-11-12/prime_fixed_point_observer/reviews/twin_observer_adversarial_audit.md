# Twin observers: current-output agreement, gluing, and source fidelity

**Scope:** read-only mathematical audit of the proposed meeting protocol,
with an independent exact finite implementation in
[`twin_gluing_probe.py`](../twin_gluing_probe.py). The two new files are
isolated from earlier implementations. This audit is a same-model check,
not independent external peer review or a formal proof-kernel certificate.

**Faithful reading:** the observers preserve whatever internal information
their protocol needs while moving in a larger carrier. At the meeting they
compare only their **current model outputs**, expressed in a common declared
frame and type. Raw histories are not comparator inputs. A record from an
earlier event can inform a present model, but its use requires an explicit
frame conversion and, separately, a justified evolution/prediction map.

The strongest useful conclusion is conditional: identify precisely what a
calibrated present comparison determines. This does not require proving that
the observers had identical internal paths, or that they reconstruct every
feature of the surrounding hypothetical system.

## A. Prior results and novelty boundary

The October [twin-frame note](../../../2026-10-11/TWIN_OBSERVER_FIELD_INVARIANCE.md)
already derives semantic agreement from faithful translations and the same
interpreted evidence. It distinguishes semantic knowledge, operational
frontiers, and causal provenance. The October
[dual-boundary note](../../../2026-10-12/DUAL_BOUNDARY_OBSERVER_CORRELATION.md)
already proves a potential-and-flux gluing theorem, gives equal-marginal and
coarse-observation countermodels, and treats nontrivial chart transitions.
Those results are reused, not claimed anew.

The present audit contributes explicit criteria for the **current-output
interface**, separates valid categorical representation from agreement of
two graph assignments, and connects exact gluing to target recovery. The
root construction supplies the new arithmetic lossless extension and its
measurement boundary. No new arithmetic asymptotic theorem follows from
the elementary criteria below.

## B. What can be inferred from a present output?

Let `S` be the declared class of admissible current source/model states,
`q:S->Y` the calibrated present output, and `tau:S->Z` the target we want
to recover. These are mathematical maps; declaring them does not establish
that a physical instrument or historical predictor realizes them.

**G1 — PROVED LOCAL, target factorization.** There exists a decoder
`d:q(S)->Z` with `tau=d q` if and only if

\[
q(s)=q(t)\quad\Longrightarrow\quad\tau(s)=\tau(t)
\qquad(s,t\in S).
\]

**Proof.** A decoder gives the implication by substitution. Conversely,
assign `d(y)` the common target value on the nonempty fiber `q^-1(y)`.
The displayed implication makes that value well-defined. No assumption of
source uniqueness is needed. The decoder is defined only on realizable
outputs; arbitrary outputs outside `q(S)` need a separate validity check.

Thus an exact current-output agreement identifies an observational
equivalence class. It can still determine a particular target exactly,
even when the full model remains ambiguous. This is the weakest relevant
interface criterion when the eventual target is one arithmetic observable.
It is a characterization of the missing information property, not by itself
a construction of an informative arithmetic `q` or a bound on its cost.

**Root/coarse-output receipt.** On `Q^2`, the maps `I` and
`H=diag(1,-1)` both fix `e_0`. The readout `O=(1,0)` obeys `OI=OH`, yet
`Ie_1=e_1` and `He_1=-e_1`. Hence both a shared root and an agreed current
first-coordinate output fail to certify the complete map. Invertible
transport does not repair a nonseparating readout.

**History boundary.** Two internal routes `I` and `X X`, where `X` exchanges
two coordinates, produce the same current state because `X^2=I`. Every
state-only current output therefore agrees. This proves no equality of
their internal execution records, and the proposed comparator is not given
those records. Agreement of present outputs should not be promoted to
history identity. Conversely, deliberately retaining internal route records
need not make those records part of the declared output.

## C. When compatible local outputs have a global realization

Let `L,R` be present local-output/model types and `M` their calibrated
interface type. Choose `u:L->M`, `v:R->M` and genuine source maps
`l:S->L`, `r:S->R` satisfying `u l=v r`. Define

\[
P=L\times_M R=\{(a,b):u(a)=v(b)\},\qquad
\gamma:S\longrightarrow P,\quad\gamma(s)=(l(s),r(s)).
\]

Every symbol here denotes current data or its current interpretation, not
an untransported historical measurement. A comparison of interface values
tests membership in `P`. It does not automatically test membership in the
possibly smaller image `gamma(S)`.

**G2 — PROVED LOCAL, precise gluing criteria.**

- A particular compatible pair `p in P` admits a genuine global realization
  exactly when `gamma^-1(p)` is nonempty.
- That realization is unique exactly when the fiber is a singleton.
- Every compatible pair glues if and only if `gamma` is surjective; global
  realizations are distinguished by the outputs if and only if `gamma` is
  injective. Existence and uniqueness together mean bijectivity.
- A target `tau:S->Z` can be recovered from the pair of current outputs
  exactly when it is constant on the fibers of `gamma`, by G1.

These conclusions follow directly by unpacking the maps. If both outputs
are already known to come faithfully from **the same actual source state**,
that actual state supplies existence for this pair. Surjectivity over all
other candidate pairs is then unnecessary. Faithfulness and common source
must be established; equality of two reported source labels is insufficient.

For a sheaf of sets on a genuine two-open cover, its sheaf axiom supplies
the bijection between global sections and compatible local sections.
The [Stacks Project, Definition 6.7.1](https://stacks.math.columbia.edu/tag/006T)
states existence and uniqueness explicitly. Merely calling the carrier a
sheaf does not prove that the proposed model assignment satisfies the axiom,
nor that two patches cover every relevant global constraint.

### Three calibrated finite controls

**Positive.** Let `S={0,1}^3`, with `l(x,y,z)=(x,y)` and
`r(x,y,z)=(y,z)`. The overlap compares the shared coordinate `y`. Each
matched pair has the unique reconstructed state `(x,y,z)`; `|P|=8`.

**Failure of existence.** Restrict the genuine source to the four even
parity triples. Both local image sets still contain all four two-bit
values. The reports `(0,0)` and `(0,1)` match at `y=0`, but their only
candidate triple `(0,0,1)` violates global even parity. Matching the overlap
missed a global constraint. If both reports had been certified faithful to
one actual source, this incompatible pair could not have arisen.

**Failure of uniqueness, with useful target recovery.** Add an unreported
fourth bit `h`. Each compatible pair now has two global realizations.
The target `x XOR y XOR z` is nevertheless fixed by the pair; the target
`h` is not. Recovering a chosen observable can be strictly easier than
reconstructing the entire surrounding system.

## D. The exact naturality test, and its relation trap

Let a category `C` be generated by a directed graph `Q`, possibly with
relations between composable words. Let `F,G:C->Vect_K` be functors.
For each object choose a linear comparison map `eta_c:F(c)->G(c)`.
These maps identify the relevant model frames; equality of raw coordinate
arrays in different frames is not the test.

**G3 — PROVED LOCAL, generator naturality.** The family `eta` is natural
if and only if for every generating arrow `e:c->d`,

\[
\eta_dF(e)=G(e)\eta_c.
\]

**Proof.** Necessity is part of naturality. For sufficiency, identity
arrows obey the equation. If it holds for `f:c->d` and `g:d->e`, then
`eta_e F(g)F(f)=G(g)eta_d F(f)=G(g)G(f)eta_c`. Induction handles all
finite words; the functor hypotheses make their assigned maps independent
of equivalent word representatives. If every `eta_c` is invertible, this
is a natural isomorphism. The inverse family is natural by rearranging the
same equation.

The definition is classical: see Riehl,
[*Category Theory in Context*, Section 1.4](https://emilyriehl.github.io/files/context.pdf).
The proof is included to make the all-generators and genuine-functors
hypotheses checkable. A finite matrix identity must hold on a full input
basis; testing only one shared root checks less. A finite selection from
infinitely many generators is also less unless a uniform proof covers the
remaining ones.

**Sharpening: one valid representation is enough.** Suppose only `F` is
known to descend from the free path category to `C`, the `eta_c` are
invertible, and the generator equations hold for a graph assignment `G`.
They imply `G(p)=eta_d F(p) eta_c^-1` for every path `p:c->d`.
Therefore any relation `p=q` satisfied by `F` is also satisfied by `G`.
It would be unnecessarily strong to demand an independent relation
hypothesis for both sides in this situation.

**Shared-invalid-relation receipt.** For one object and a generator `a`
with declared relation `a^2=id`, assign both twins `A=diag(1,2)` and
`eta=I`. Every twin-to-twin generator comparison passes and both fix
`e_0`, but `A^2=diag(1,4) != I`. These identical assignments are valid
on the free monoid, not on the declared involution category.

**Noninvertible-intertwiner receipt.** Let the first representation assign
the valid involution `I`, the second assign the same invalid `A`, and take
`eta=diag(1,0)`. Then `eta I=A eta`, although `A^2 != I`. An intertwiner
which discards a subspace does not transfer every relation to the hidden
complement. This is why the sharpening requires invertibility.

For a stipulated current readout `O`, one may check only
`O(eta_d F(e)-G(e)eta_c)=0`. That certifies the corresponding current
output relation. It does not establish G3's full naturality unless the
readout is separating on the possible defects. Neither the algebraic
proof nor its probe adds raw histories to the comparator.

## E. Shared model agreement still needs an anchored interpretation

On `Q^3`, put `A=diag(1,1,0)` and let `P` exchange `e_1,e_2` while fixing
`e_0`. The conjugate `B=P A P^-1=diag(1,0,1)` has the same root and is
isomorphic to `A`. Two observers using `B` agree exactly on every shared
input. Yet the named input `e_1` has output `e_1` under `A` and zero
under `B`.

This is not a counterexample to coordinate invariance. If the second
observer applies the matching input/output decoder `P`, it represents the
same structure. It is a counterexample to **internal agreement authenticates
an already anchored source interpretation without checking the decoder**.
A consistent relabeling is harmless when declared and transported; using
changed labels as though they were the fixed original labels is different.

The prior [return-path source control](../RETURN_PATHS.md) makes the analogous
arithmetic issue concrete: selected shared unit returns survive the source
swap `(11 13)`, while authentic nonunit comparisons detect the change.
Shared provenance and shared preparation are not independent verification.

## F. Finite meetings and finite diagnostic windows

In a discrete cylinder indexed by `Z`, start at `-N` and `N` and move one
unit per step toward zero. Both reach the same cut after `N` steps. For
any proposed common budget `t`, choose `N=t+1`; they have not met. Thus
`for every finite N there exists a finite meeting time` does not imply a
uniform finite time, and infinity is not an integer vertex from which to
start the same walk. A compactified endpoint or another travel law needs
its own definitions. This is an abstract integer-step control, not a
claim about a physical spacetime metric or causal speed.

Similarly, on `l2(N_0)`, `I` and
`I-2|epsilon_N><epsilon_N|` agree on every input index below `N`. They
remain two units apart in operator norm, with witness `epsilon_N`.
Every finite input window can miss a defect beyond its boundary. The
root's weighted full-support twin construction repairs exact separation,
with an explicit nonuniform conditioning cost; finite probe agreement
alone does not establish the infinite equality.

## G. Probe scope and verdict

`twin_gluing_probe.py` is an independent exact rational/set implementation.
It checks all 255 nonempty restrictions of the three-bit source and all
4,096 binary-current-report/target triples on a four-state source.
For the target criterion it compares fiber constancy against exhaustive
existence of a decoder. Naturality is tested on all paths of length at
most seven in a two-object/four-arrow graph for four distinct rational
frame changes. Positive relations, shared invalid relations, lossy
intertwiners, anchored relabeling, and finite-window defects are retained.

The code emits actual check counts and witnesses. Counts describe exact
finite implementation checks; they are not independent votes for the
universal statements, whose proofs are above. Nothing in these tests
compares an observer's raw history to the other observer's history.

**Verdict:** SURVIVES as a conditional architecture. Present outputs can
be reconciled in a common frame, and a declared target can be recovered
when the output is sufficiently informative on the admissible source
class. Unconditional global agreement, unique reconstruction, authentic
source identification, and equality of internal histories do not follow
from meeting or from twin symmetry. Each failure has an explicit receipt.

**Next discriminator:** choose a concrete current arithmetic output and
target, define its admissible source class and frame interpretation, and
prove the target-factorization or quantitative stability property while
rejecting the retained source and relative-phase countermodels. Merely
requiring that the full arithmetic target already be part of the output
would restate the desired answer rather than close a new dependency.

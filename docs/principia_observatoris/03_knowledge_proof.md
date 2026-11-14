# Liber Tertius — De Cognitione et Demonstratione

## 1. Knowledge has a target and a source class

Use a nonempty declared class \(\Omega\) of admissible initial sources. A member
may be an initial state of a fixed deterministic carrier, or a complete source
model with its initial state. For nondeterministic path questions it may include
an entire lawful execution. The choice is explicit: probabilities of unknown
sources are not supplied by a set of possibilities.

An evidence map \(E:\Omega\to Z\) gives the interpreted information available
for the question at hand. It can describe a realized transcript, exact laws of
counterfactual experiments, or a mathematical certificate. These are different
maps. A target is \(P:\Omega\to V\). For \(z\in E(\Omega)\), let
\(B_z=E^{-1}(z)\). Only a nonempty fiber licenses model-relative identification.
An empty fiber means incompatible evidence/model premises, not every conclusion.

**PO-K1 (target factorization; EXISTING CLASSICAL SUCC RESULT).** A unique
\(\bar P:E(\Omega)\to V\) satisfies \(P=\bar P\circ E\) if and only if

\[
\forall x,x'\in\Omega,\quad E(x)=E(x')\Longrightarrow P(x)=P(x').
\tag{K1}
\]

**Proof.** Factorization implies the equality immediately. Conversely assign to
\(z\) the common \(P\)-value of its nonempty fiber. K1 makes this well defined;
nonemptiness makes it unique. \(\square\)

This is [CARRIER_RELATIVE_TARGETS.md](../CARRIER_RELATIVE_TARGETS.md), §1,
reused verbatim in mathematical content, not a new theorem of Principia.
It permits exact knowledge of a target while hidden states remain unresolved.
For \(\Omega=\{0,1\}^3\), \(E(x,y,h)=(x,y)\) determines \(x\mathbin{\mathrm{XOR}}y\)
without determining \(h\).

**The strongest valid reading of the founding question is therefore conditional:**
relative to a declared admissible source class and a specified interpreted
evidence map, the target is identified exactly when that map loses no distinction
needed by the target. This is a necessary and sufficient theorem for semantic
identification. It is not yet a theorem about finite access, computation or an
external physical source.

## 2. Three obligations that cannot be merged

| Obligation | Mathematical question | Independent failure |
|---|---|---|
| Identifiability | Does \(P\) factor through the declared all-experiment evidence map? | Two equivalent sources have different target values |
| Executable identification | Is there a lawful, terminating, resource-admissible policy and decoder whose actual transcript determines the original target? | Destructive probes or unknown/uncomputable decoder |
| Source adequacy | Do the declared source class, action laws and interpretations apply to the intended source? | A faithful theorem about a mislabeled or incomplete model |

Abstract factorization does not imply computability: take \(\Omega=\mathbb N\),
\(E(n)=n\), and let \(P(n)\) indicate whether program \(n\) halts. K1 holds but
there is no total computable decoder for this target under the standard effective
programming model. This is the classical halting obstruction, not a claim that a
particular arithmetic conjecture is undecidable.

Even with a finite source and computable decoder, all-experiment identifiability
can fail to be executable on one copy. Reuse SUCC's exact three-state witness:

| Initial state | Probe \(a\) output | Probe \(b\) output | State after either probe |
|---|---:|---:|---|
| \(A\) | 1 | 0 | \(A\) |
| \(B\) | 0 | 1 | \(A\) |
| \(C\) | 0 | 0 | \(A\) |

All pairs of initial states are separated by some probe, so the counterfactual
all-word quotient is discrete. But \(P=1_{\{C\}}\) cannot be determined with
certainty by a single-copy policy. If the first probe is \(a\), outcome 0 merges
\(B,C\) with opposite target values; if it is \(b\), outcome 0 merges \(A,C\).
Future states coincide, so no later action repairs the loss. Nondisturbing probes
or an authenticated reset/copy resource repair the example. This is already
proved in [CARRIER_RELATIVE_TARGETS.md](../CARRIER_RELATIVE_TARGETS.md), §3.

## 3. Exact executable identification is a leaf condition

For a fixed deterministic policy tree \(\pi\), let \(L\) be its terminal
transcripts and

\[
B_\ell=\{x\in\Omega:\pi\text{ run from }x\text{ terminates with }\ell\}.
\]

Assume every source in \(\Omega\) follows a lawful finite execution to one leaf.
The leaf label may include measured settings and actual outcomes; it does not
include a hidden initial-state tag available only to a simulator.

**PO-K2 (terminal-transcript criterion; CLASSICAL elementary synthesis).** There
exists a correct decoder \(d:L\to V\) for the initial target on every source if
and only if \(P\) is constant on every nonempty \(B_\ell\). If \(\Omega,L\) and
the table are finite and effective, this criterion and a decoder are computable.

**Proof.** Apply K1 to the map sending each source to its terminal transcript.
For the effective statement, enumerate each nonempty fiber, check equality of all
target labels, and assign its common value. Unreachable leaves may receive any
label when the target codomain is nonempty, or be excluded from the decoder's
domain. \(\square\)

This criterion applies to a **supplied policy**, not to an unproved assertion
that some policy exists. Finite-budget AND/OR synthesis in SUCC retains pairs
\((\text{original state},\text{current state})\), precisely because probes may
change the latter while the target concerns the former. See
[Contextual Zero Backbone](../CONTEXTUAL_ZERO_BACKBONE.md), §4, and the existing
`adaptive_proof_policy` and `carrier_relative_targets` implementations. The
policy's cost must be checked over every branch, not only the observed favorable
branch. A finite-budget search failure does not prove all-budget impossibility.

### Distinct stochastic laws need not be finitely distinguishable with zero error

**PO-K2s (common-support obstruction; PROVED elementary restriction).** Consider
two source laws with different target labels. Suppose every finite terminal
transcript of a permitted policy has positive probability under one source if
and only if it has positive probability under the other. For finite or countable
transcript alphabets, no policy that terminates almost surely under both sources
can return the correct target with zero error under both.

**Proof.** Almost-sure termination implies that the countable union of terminal
transcripts has probability one under the first source. Some terminal transcript
therefore has positive probability. Zero error forces its answer to equal the
first target. By common support that transcript has positive probability under
the second source, where this same answer is wrong. \(\square\)

For repeated independent Bernoulli samples with \(p=1/3\) versus \(p=2/3\),
every finite bit string has positive probability under both laws. Their laws are
different and hence theoretically identifiable as probability distributions, but
no exact zero-error almost-surely finite sample policy identifies which law was
used. Approximate/confidence guarantees are a different target and remain
possible. The proof extends to randomized policies when their terminal
transcript-plus-answer distribution has the stated common-support property;
no claim for arbitrary uncountable zero-measure transcript fibers is made.

## 4. Record extension and monotonicity

Let \(h\preceq h'\) mean that the *same retained, interpreted record* \(h'\)
extends \(h\). Keep the source class, source laws and interpretations fixed.
Let \(B_h\) consist of initial sources consistent with \(h\); later observations
are interpreted after the actual earlier interventions, not as fresh
nondisturbing measurements of the initial state.

**PO-K3 (retained-evidence monotonicity; CLASSICAL).**

\[
h\preceq h'\Longrightarrow B_{h'}\subseteq B_h.
\]

Consequently, if \(B_{h'}\ne\varnothing\) and a fixed initial-source target is
constant on \(B_h\), it remains constant with the same value on \(B_{h'}\).
For a ring of functions on the fixed source class,

\[
I(B)=\{f:f|_B=0\},\qquad I(B_h)\subseteq I(B_{h'}).
\tag{K3}
\]

**Proof.** Any execution realizing the longer record realizes its prefix.
Restriction preserves constant target values and vanishing functions. \(\square\)

This recovers the exact contextual-zero antitone law, with a precise distinction
between initial-source and present-state fibers. Present-state supports need
not be nested: a known bit 0 can be lawfully flipped to 1. The earlier assertion
about the earlier bit remains valid; the present-tense assertion changes.
Changing the model class or interpretation can enlarge or replace compatible
fibers, so K3 does not authorize monotonicity across such revisions.

Persistent memory is essential. A bit read into a memory register and subsequently
overwritten leaves the current observer unable to reconstruct the earlier value
unless another retained record stores it. The source history occurred, but the
observer's accessible information shrank. A current-state equality is not a
complete causal-history equivalence.

## 5. Combining observers requires a common source and actual joint image

Let observers have interpreted evidence maps \(E_i:\Omega\to Z_i\) on the
**same** source class, with a declared alignment of source, time and settings.
Their joint map is \(E=(E_i)_i\), with codomain restricted to \(E(\Omega)\).

**PO-K4 (joint-image theorem; CLASSICAL).**

This is already SUCC [O643/CA06](../CLAIM_LEDGER.md). The information join used
here differs from the maximal deterministic *common* factor in O307: the latter
uses the equivalence closure of the union of report kernels.

\[
\ker E=\bigcap_i\ker E_i.
\]

The pooled evidence determines target \(P\) iff this intersection is contained
in \(\ker P\). At an actual compatible report tuple \((z_i)_i\), the surviving
fiber is \(\bigcap_i E_i^{-1}(z_i)\). Invertible typed report changes
\(\theta_i:Z_i\to Z_i'\) preserve these equivalence relations, provided the maps
and their inverses are transported consistently.

**Proof.** Two sources have the same tuple exactly when they have the same
component for every \(i\). Apply K1. Fiber and coordinate statements follow by
substitution and injectivity of the \(\theta_i\). \(\square\)

This is a statement about pooled **information**. An additional channel and
resource contract is required to move that information between actual observers;
for destructive or interacting probes it may not be jointly obtainable. In
particular, an all-counterfactual tuple must not be presented as one realized
record. Two source models with no authenticated common carrier require an
explicit comparison span and compatibility relation before K4 is applicable.

Three exact controls prevent false interpretations:

1. **Complementary evidence.** On \(\{0,1\}^3\), the two reports \(x\) and
   \(y\) jointly settle XOR while leaving \(h\) hidden.
2. **Common provenance.** Replacing \(E\) by \((E,E)\) leaves its kernel
   unchanged. Duplicate reports supply no new distinction, irrespective of how
   many agents repeat them.
3. **Pairwise compatibility is insufficient.** On
   \(\Omega=\{000,011,101,110\}\), every pair of claimed reports
   \(x=y=z=1\) is realizable, but their triple is not. A full joint-image check
   rejects it. This is the existing carrier-relative target example, §1.

Agreement therefore does not prove a shared hidden ontology. A constant report
makes arbitrarily different hidden carriers agree. Nor does a present readout
bijection transport historical paths or costs: Q1 in Book I supplies the stronger
condition when those objects matter.

## 6. Evidence, inference and proof are separate typed operations

| Stage | Object | What it warrants | Missing arrow without extra premises |
|---|---|---|---|
| Contact | Realized source/instrument interaction | A scoped occurred event | No universal theorem |
| Distinction | Different allowed interpreted reports/laws | Separation under that instrument family | No guarantee one policy can obtain every distinction |
| Identification | Target-constant nonempty fiber | A model-relative target value | No automatic computation or source adequacy |
| Prediction | Model-derived proposed future consequence | A falsifiable conditional | No performed event |
| Verification | A checked consequence/certificate with provenance | Its declared finite or formal scope | No upgrade from correlated repetitions to independent proof |
| Proof | Finite derivation in a specified calculus from stated premises | Logical consequence under sound interpretation | No external authentication of those premises |
| Completion | A defined limit with a proved transport law | The limit conclusion and any proved finite error bounds | No last physical infinite-time event |

**PO-K5 (finite support of finitary proof; EXISTING CLASSICAL SUCC RESULT).** For
an increasing sequence of premise sets \(T_0\subseteq T_1\subseteq\cdots\) in
any finitary proof calculus,

\[
\left(\bigcup_nT_n\right)\vdash\varphi
\quad\Longleftrightarrow\quad
\exists n\;T_n\vdash\varphi.
\]

**Proof.** A finite derivation uses finitely many premises, each supplied by some
stage. Their finitely many stage indices have a maximum, whose theory contains
all used premises. The reverse direction is inclusion. \(\square\)

This is the proof-support statement already in [FOUNDATIONS.md](../FOUNDATIONS.md),
§5. It is about a supplied proof calculus with finitary rules; an omega-rule is
a different calculus. It does not say every true theorem is eventually proved.

A universal theorem can be proved from an authenticated recurrence or invariant
without observing every instance. Conversely any finite prefix of an unrestricted
sequence permits a later counterexample. Book IV makes the extra finite-dimensional
hypotheses for a bounded discriminator explicit. Thus finite observation plus
source laws can support universal mathematics, but the laws and the derivation
carry the universal obligation.

Possible-world agreement is a familiar mathematical semantics of knowledge;
Halpern and Moses' [primary paper](https://arxiv.org/abs/cs/0006009) grounds it in
distributed-system histories. Our K1 is also already SUCC's target theorem.
Calling such semantic agreement *computed knowledge* would introduce logical
omniscience, so a finite observer additionally needs a specified effective
reasoner/decoder. This book keeps the semantic, computational and source-adequacy
questions separate rather than claiming a new resolution of epistemology.

## 7. Source adequacy and the exact surviving principle

A formal source label or byte hash can bind a theorem to a supplied transition
table. It cannot show that a physical box obeys that table. One may explicitly
assume or certify an interpretation from an intended external experiment family
into the formal source and prove that it preserves selected outcome laws. Any
application then inherits the strength and scope of that assumption/certificate.
This is the existing `FieldClass(Source, Target, Tools)` discipline of
[OBSERVER_PROOF_ACCESS.md](../OBSERVER_PROOF_ACCESS.md); difficulty labels are
not intrinsic properties of a number, field or person.

**Surviving Principia rule.** Relative target determination requires (a) a
nonempty justified source class, (b) available evidence that is sufficient for
the target, and (c), for finite operational knowledge, a lawful executable
acquisition/decoding path within the stated resources. Applying it to an intended
external source additionally requires source adequacy. The first condition is
not a probability, the second is not a performance benchmark, and the third is
not a universal proof of the source laws.

No theorem here promotes pi normality, RH or an inaccessible target to true,
false, independent or intrinsically unknowable. The next useful theorem must
supply a discriminator or a preservation bound that changes the compatible
**target values**, rather than merely adding another description of the same
surviving source fiber.

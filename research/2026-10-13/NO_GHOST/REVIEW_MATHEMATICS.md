# NO-GHOST adversarial mathematics review

Reviewer: frontier-audit agent, 2026-10-13. Read the complete current
`MANUSCRIPT.md`, `COHERENCE.md`, and `GLUING_REPAIR.md`. This reviewer did not
derive those statements. The review shares model/provider and repository
lineage with the authors and is not an external scholarly referee. It does
not independently validate physical source authenticity or academic priority.

**Verdict at review:** the finite algebra, coherence normalization proof,
constraint-incidence gluing, operational policy polytope, and repair bounds
survive the stated paper-proof audit. Main-manuscript NG-Q has a material
missing hypothesis, already present correctly in detailed NG-G2. Repair that
statement before treating it as proved. Two further typing/totality
clarifications are recommended. Missing deliverable links require final gate.

## R1. Material: NG-Q does not currently provide its transport paths

The main NG-Q assumes invertible, path-independent comparisons natural with
restriction, and that each allowed full presentation restricts to an allowed
local one. Its proof then says:

> Transport each local class to its restricted presentation.

That step is unsupported unless the local presentation belongs to the same
comparison component as the restriction of the chosen full presentation.
Path independence constrains existing paths; it does not create a path between
disconnected presentation components. Restricting an allowed global chart is
one direction of the required existence condition, not its converse.

### Exact finite countermodel to the weakened statement

Take the finite site of subsets of two distinct points, `empty`, `U`, `V`,
`W=U union V`, with union covers. On each nonempty context allow two
presentation labels `red` and `blue`; on the empty context allow one label.
Every presentation fiber has one element. Restriction from W preserves its
color on U and V, and restriction to empty forgets color. Supply only identity
comparison arrows on nonempty contexts; at empty there is the unique identity.

For either fixed full color, its restricted assignment presheaf is the
terminal sheaf: it has exactly one element everywhere. Every supplied
comparison is invertible, path independent, source preserving and natural.
Every full presentation restricts to an allowed presentation. Assign the same
single immutable source label to every element if desired.

But presentation classes have two elements on each nonempty context and one
on empty. The local class `red` on U and `blue` on V agrees on their empty
overlap. Neither global class restricts to that pair. Thus the class presheaf
fails the sheaf condition even though every stated existing comparison and
each fixed-global-presentation sheaf passes its test. This is a missing
presentation-connectivity obstruction, not a failure of any braid equation.

This model is not claimed to be a new physical instrument counterexample.
It disproves the abstract implication as written. If “schedule presentation”
is intended to mean the complete linear-extension system with all legal
adjacent exchanges, say that explicitly; that additional structure supplies
connectivity, which the current NG-Q wording omits.

### Minimal correction

Use the detailed `GLUING_REPAIR.md` NG-G2 hypotheses without weakening them:

1. `S(U)` is nonempty for every context under consideration.
2. For every `s,t in S(U)`, a comparison `T^U_(s,t)` exists, is invertible,
   and satisfies identity/composition. Equivalently, declare connected
   comparison graphs and prove the chosen maps path independent.
3. Restriction maps are functorial and natural with those comparisons.
4. For each fixed full presentation s, the presheaf
   `V -> H_(s|V)(V)` is a sheaf on its slice of the constraint-complete site.

Then each orbit has exactly one representative in the chosen restricted
chart, and the existing proof is correct. A weaker alternative sufficient for
a single cover is to require those chart comparisons only for the local
presentations and overlaps of that cover, with compatible restriction maps.

## R2. Typing clarification: common final coordinates in NG-W

`COHERENCE.md` NG-WEAK-SCHEDULE is precise: kernels factor through a common
summary `(sigma,I,receipt_assignment,c)`, so after an exchanged pair the suffix
is literally a common kernel. The proof is valid in that setting.

Main NG-D also permits endpoints in different types identified by specified
bijections. If main NG-W inherits arbitrary such bijections, its statement
“the same ... final complete interface law” must identify a common comparison
space or specify that the equality is transported. Different chosen paths can
otherwise give different endpoint identifications. Pairwise law equalities do
not themselves construct a canonical coordinate identification.

Recommended wording: retain the common summary contract from the detailed
note, or require fixed maps of every terminal presentation into one declared
common interface with which every local diamond intertwines. If the desired
conclusion is merely equality after an indicated chain of identifications,
say so and do not call that chain-independent private or coordinate transport.

This is not a counterexample to the common-summary theorem; it prevents a
misreading of the more compressed main formulation. A two-element endpoint
with a flip identification already shows why literal equality and equality
after transport are different notions.

## R3. Minor totality clarification: zero-reach empty menus

NG-P/NG-P2 reconstruct a policy by choosing an arbitrary declared action at
`r_h=0`. If a nonterminal public node has no safe action, no such arbitrary
action exists. The equations force `r_h=0` at that node, so no positive run
needs an action there. The mathematics can handle this in either standard way:

- require every nonterminal decision node to have a nonempty legal menu;
- or define the synthesized policy only on reachable decision histories,
  leaving zero-probability dead ends outside its domain.

The finite-termination assumption already forbids reaching such a dead end
with positive mass. State the convention explicitly rather than relying on
an impossible “choose any” operation at a null node. Terminal nodes need no
choice and should be excluded from the action-sum equations.

## R4. Statements independently re-derived without a defect

### All-prior diamond

NG-D's forward direction is finite linearity; its reverse is exact Dirac
evaluation. The manuscript correctly restricts the tested domain to admissible
source/current pairs and correctly warns that a fixed prior tests only its
linear span. Enabledness is separately required. Full labelled law equality
does not claim private-path bijection, future continuation equivalence, or
actual performance. These distinctions survive.

### Complete schedule graph coherence

NG-S's normalization proof works for the full finite-poset linear-extension
graph. Orienting adjacent swaps toward one fixed target decreases its
inversion count. Every adjacent target inversion in a linear extension is an
incomparable pair. Two competing reductions are disjoint or overlap in three
target-descending entries. In the overlap all three pairs must be incomparable,
because every pair reverses between two legitimate extensions. Thus the
disjoint square and braid hexagon are available and identify the reductions.
The inductive normal-form maps factor every unoriented edge using the inverse
law, proving arbitrary-path independence. No additional higher equations are
needed for these strict set-bijection targets. The explicit warning about an
arbitrary pruned authorization graph is necessary and correctly retained.

The independent-bit experiment legitimately realizes its maps as
weight-preserving bijections of lawful possible path fibers. It also honestly
discloses that CNOT changes occurrence-attached private values and is rejected
under a stronger token-value preservation contract. It proves failure for a
chosen comparison family, not nonexistence of every coherent family. The
ordinary occurrence-token swap supplies the positive control. No stronger
physical statement is warranted or made.

### Constraint-complete gluing and sheafification

NG-G/NG-G1's sheaf proof is correct for the incidence site retaining all
constraint cells with their full scopes. It is classical assignment gluing.
The separate sound-and-complete encoding premise is substantial: it may be
hard to construct, and one may trivially encode the entire lawful execution
relation as a global constraint. Consequently this theorem is not, by itself,
an efficiently checkable local characterization of arbitrary causal contracts.
The manuscript explicitly recognizes that boundary and avoids a novelty claim.

NG-N/NG-G4's natural-retraction no-go follows directly: any retraction of the
sheafification unit would send a formal glue to a forbidden original glue.
The separatedness assumption in main NG-N is unnecessary but harmless.

The mandatory odd-parity example uses local supports/laws, not a matching
family of point assignments. The text maintains this distinction and thus
does not contradict the assignment sheaf theorem.

### Operational polytope

Given a complete finite public perfect-recall tree, fixed chance weights,
safe public menus and finite termination, the realization equations are
linear and exactly characterize behavioral public policies. Copying controller
realization factors through chance outcomes is correct; those factors are
not probability mass on the public nodes. Multiplication by fixed chance
path weights then produces true path probabilities. Ratios at positive r
recover action distributions. Perfect recall makes an independent random
deterministic policy equivalent to a behavioral public policy; policy seeds
do not add hidden-source access because all private paths with the same
public word have the same compatible policy choices.

The support-only coin and hidden-source guessing countermodels decisively
refute equating `Delta(Omega)` with operational laws. The finite rational
Farkas characterization is classical and is correctly identified as such.

### Repair

The finite-menu optimum is a correct but deliberately elementary theorem.
Legal implementation witnesses are assumptions, not manufactured access.
NG-R2's conservative-label no-go follows by probability pushforward and, for
a surjection, atomwise lift. NG-R3's incomparable sensors concern a specified
pair-discrimination task; it correctly avoids claiming to refute canonical
factorization of an arbitrary total deterministic target. The fiberwise
coloring bound and complete-signature special case are exact for the stated
static task; online-update and sensor availability can require more.

## R5. Links and provenance needing the final integration gate

A filesystem check of Markdown links in the three reviewed notes found these
manuscript targets absent at review time:

- `INTEGRATION.md`
- `VALIDATION.json`
- `../../../docs/CLAIM_SUPPLEMENT_NO_GHOST.md`

They may be planned principal deliverables; recheck after they exist. The
relative paths to existing source modules are correct from the NO_GHOST
directory. No missing local links were found in the other two notes.

`GLUING_REPAIR.md` now cites a later inspected F48 snapshot
`8dacc56cec68b2e998529caf31f34fb5beeaa1d3`, whereas the original frontier audit
records `bd0e0d6...`. These are not interchangeable acceptance states. Retain
both immutable provenance records and explicitly state which governs the
final acceptance summary. Do not silently update the older audit's evidence.

## Final review boundary

The revised modular conclusion is defensible: exact matching assignments on
a complete constraint site glue; complete coherent presentation systems may
be descended; full outcome kernels preserve weak schedule laws; private
comparison maps require their own coherence; operational probabilities need
public-policy realization constraints; repairs are relative to a legal finite
menu. The broad “all obstruction tests iff one global physical experiment”
claim is neither proved nor needed. The manuscript correctly rejects that
claim, subject to correcting NG-Q's comparison-existence premise.

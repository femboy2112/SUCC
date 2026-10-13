# CAMBRIAN D: computation, invention, probability and resources

Date: 2026-10-13. Base commit: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
Worktree branch: `research/cambrian-d_computation-2026-10-13`.
Assignments actually executed: **19, 20, 21, 22, 23, 24**, by one cluster worker.
No claim of six separate reasoners, blind external review, new Lean proofs,
physical source authentication, or unrestricted invention.

## Baseline, provenance and first hypotheses

The worker inspected `AGENTS.md`, foundations, method, architecture, roadmap,
relevant ledger entries, import manifest, and the causal/EODCS/probability/Hankel
modules. Historical imports are untouched. Only namespaced additive files change.
The first rival hypotheses were sent to the orchestrator before cross-cluster
results were received: disabledness may change partial equivalence; generic
residual splitting can create predictive memory; iid reuse can miscalibrate
shared-latent reports; information-greedy probes can destroy original claims;
Hankel rank identifies behavior rather than hidden ontology; tiny certificates
can require arbitrarily expensive access. This is an in-session freeze, **not a
separate preregistration commit or blind holdout protocol**.

Existing ancestry matters. PR45 at
`b2774ca485db4b5b4f7ce92e535220352fb3af2f` was read directly with `git show`.
Its `EVOLUTIONARY_OBSTRUCTION_SYNTHESIS.md` EO1–EO3 and EOS-01–04 already contain
all-word equivalence, constructive prefix repair, finite refinement termination,
and the minimum observer universal property. These results are **existing
classical edges**, independently replayed here, not new mathematical discoveries.
EOS-16 already has researcher-selected Heisenberg-family discovery. EO6–EO7 and
EOS-12–14 already prevent duplicated Bayesian evidence and preserve original
source coordinates. Nothing from that branch is blindly imported, and its Lean
4.19 evidence is not relabeled as evidence for this branch's Lean 4.14 stack.

New emphasis is partial-action nontransitivity, explicit memory-bit bounds,
random graph holdouts, a history-only learner with declared equivalence access,
costed strategy comparison, and precise finite calibration/resource countermodels.
The history-only learner implements the classical Angluin route; its novelty is
new-to-this-SUCC-interface, not new academic priority.

## D19. Partial, asynchronous and typed causal Myhill–Nerode

**Objects and quantifiers.** A deterministic source has state set X, finite
action alphabet A, partial maps U_a, and current output q. If enabled menus are
observable, append the enabledness vector to q and formally totalize disabled
actions with a distinguishable absorbing failure state. For changing finite
source contexts, use a disjoint union of context/state pairs; a typed action is
disabled outside its domain. Preserve context labels in the output when they
are part of the actual report. The totalized failure transition is a semantic
construction, not permission to execute an unavailable physical action.

Define x~y iff every finite action word has the same output in this specified
semantics. For **every** deterministic source, ~ is the largest output-compatible
action congruence. Its finite reachable quotient exists iff the number r of
reachable residual trace classes is finite. In the finite case it is minimal
among deterministic output-preserving realizations, up to renaming.

**Proof.** Prepending an action to every test word proves action stability.
Conversely an output-compatible congruence preserves equality through a word by
induction. The residual quotient therefore has lawful induced transitions.
Any realizing machine that merged two distinct residuals would give the same
predictions to a word separating them, a contradiction. For a single prepared
root, restrict to reachable states. Finite source/context cardinality is a
sufficient condition; arbitrary changing or unbounded contexts are not silently
assumed finite.

**Competitive rival and decisive failure.** Compare states only on words legal
at both states, without observing offered menus. This relation need not even be
transitive: a,b,c all report 0; a admits x and then reports 1; c admits x and then
reports 2; b admits no action. Thus a~b and b~c under common-legality comparison,
but a is not related to c. No quotient equivalence theorem applies to this
relation. The weakest repair is to declare observable enabledness/failure, a
different typed observational semantics, or a specified common action domain.
In contrast, the proof planner must not obtain hidden enabled menus as free
evidence: it permits only actions enabled at every compatible current state.

**Asynchronous boundary.** A pending-event counter 0..B, with enqueue/deliver
actions and empty/nonempty output, needs exactly B+1 live residual states. For
i<j, deliver^i gives empty at i and nonempty at j. Conversely the source itself
is a B+1-state realization. Thus fixed internal memory needs
ceil(log2(B+1)) bits. The totalization sink is additional formal state, never
counted as an actual pending-event state. An unbounded queue counter has
infinitely many distinguishable residuals by the same word argument, and hence
no finite deterministic exact realization under this toolkit. This is not
Turing-undecidability and does not rule out approximate or restricted tasks.

**Evidence/status.** CLASSICAL / PROVED CONDITIONAL, exact capacities B=1..6,
observable-menu positive control, nontransitivity negative control, invalid
transition rejection. General infinite-queue proof is written, not Lean checked.
**Next falsifier:** erase the empty/nonempty readout or restrict delivery to a
fixed horizon; the lower-bound hypotheses and number of residuals change.

## D20. Obstruction-born memory and the honest invention boundary

**Representation question.** Start with current report q only. A memoryless
update V_a exists exactly when q(U_a x) is constant on each q-fiber. When this
fails, the program constructs new tuple-valued residual signatures and an
induced memory transition table. No target counter, graph or automaton is
prelisted. The supplied **metaconstructor** is nevertheless the classical
observation-table/residual-state constructor.

Let F contain empty word and previously generated tests, and
q_F(x)=(q(U_w x):w in F). If q_F(x)=q_F(y) but the successors have unequal
signatures, choose w in F witnessing that difference and create (a,w). It
separates x,y. An evolutionary word search may instead find any verified
separator; a failed genetic run falls back to the logically forced (a,w), not
to a relabeled genetic success.

**Finite theorem and lower bound.** For every complete n-state deterministic
source, this process reaches its r-class future-observation quotient in at most
r-b0 strict splits, where b0 is the initial number of report classes. Each
added word is constant on true residual classes, while each obstruction splits
at least one current class. At the plateau the candidate is a congruence, so
the D19 argument proves equality with the residual quotient. This is exactly
the already known EOS-02/03 mathematics. It counts refinements, not physical
measurements or computational instructions.

Any deterministic predictive state encoding needs at least r codes, hence
ceil(log2 r) fixed-width bits. If current report is free decoder side information,
let r_y be the number of residual classes in q^{-1}(y). A supplementary channel
needs at least ceil(log2 max_y r_y) bits, and local class numbering in each fiber
attains it. This is conditional encoding; it does not create an unavailable
sensor. The four-cycle marker control grows **2 -> 3 -> 4** classes; the three
states reporting 0 force two supplemental bits. A learned known-root predictor
can carry its quotient state along actual action histories; memory alone cannot
reconstruct an unknown initial residual class from identical past receipts.

**Independent finite oracle.** Enumerate all set partitions of the declared
source, retain every output-compatible action congruence, and choose the minimum
class count. This restricted-growth enumeration is a different implementation
from test-signature repair and the existing pair/Moore algorithms. Every
equivalence relation is enumerated, giving a scoped exhaustive minimality
certificate. The oracle budget is at most eight states; no exponential oracle
is described as scalable learning.

**Heldouts and evolutionary credit.** After the first constructor was written,
24 seeded reachable sources (seeds131..154, sizes3..6) were generated: one cycle
action and one random action, with binary readouts. They are arbitrary finite
graphs within this disclosed generator, not a selected counter/Heisenberg
formula. All pass exhaustive-partition minimality and 3,348 word forecasts.
Across 48 representation splits, **34** separating words were selected by the
existing genetic engine, **14** by deterministic obstruction repair. Fitness
did not certify any source law. These are computational holdouts within an
authored generator; no independent natural-world source or external reasoner.

### History-only access experiment: the exact teacher remains load-bearing

PR45 EO next-question1 asks to abandon direct source-table access. The new
`learn_history_memory` accepts only an alphabet, membership word->output
function, and hypothesis->counterexample equivalence function. It receives no
source IDs, cardinality, transition arrays, hidden coordinates or desired
invariant. Prefix/suffix tables are made closed and consistent, then converted
into finite predictor outputs/transitions. A counterexample adds its prefixes.
The finite simulator-side teacher uses a product-state BFS; source access
remains privileged in this **teacher**, not in the learner.

**Conditional theorem.** For every reachable finite deterministic Moore source,
correct reset membership access plus a correct terminating exact equivalence
teacher allows this observation-table learner to construct the minimum
reachable realization. Rows consist of real continuation outputs, so their
count is at most the number of source residuals. Closure and consistency ensure
a lawful candidate. A genuine counterexample forces a new row distinction at
the next repaired table: otherwise following its prefixes through the candidate
would reproduce every genuine output, contradicting that counterexample.
Therefore failed hypotheses strictly increase the finite row count. An
accepted hypothesis has full behavior equality by the teacher contract. Its
row count is at most r, while D19 gives at least r, so it is minimal.

The exact teacher is much stronger than random testing or finite samples. A
reset query assumes prepared equal-root trials/leases; neither is actual
hardware supplied here. A finite round budget returns
`UNRESOLVED_RESOURCE_BUDGET`, never a certificate. Wrong counterexamples are
rejected. The metagrammar supplies rows, finite memory types, and table laws;
the engine **does not invent its own metagrammar**. Thus the full unrestricted
Moonshot B is not achieved.

The history learner was then tested on **24 different fresh seeds271..294**,
also sizes3..6. It used 667 membership queries and 39 exact counterexamples;
all 9,144 additional words of lengths7 and8, excluding membership-training
queries, and exhaustive minimum-state checks pass. This comparison is not an independence claim between the two authored
source generators. Status: CLASSICAL / PROVED CONDITIONAL / TESTED MODEL;
new-to-SUCC access interface, academic novelty NOT CLAIMED.

**Next verdict-changing probe:** weaken exact equivalence to random tests or
remove resets. The guarantee disappears; quantify the additional state-bound,
conformance-test or PAC assumptions instead of promoting approximate evidence.

## D21. Cloning, shared evidence, stopping and misspecification

**Objects.** Finite model families, exact prior mass and a declared conditional
joint source law. Model probabilities are model-relative; they are not
probabilities of mathematical truth.

**Clone theorem.** Replace a model presentation by k clones with identical
likelihoods for every actual recorded context, and split its existing prior
mass among them. For every dataset with positive evidence, the aggregate clone
posterior equals the original posterior: summing pi_i L gives pi L in numerator
and denominator. Adding k independent equal-prior presentations instead changes
the prior family mass, hence the posterior. The existing quotient prior and
`syntax_clone_counterexample` are reused. Current-menu equivalence alone does
not guarantee clone equivalence for future unmeasured contexts.

**Shared-latent calibration countermodel.** H is fair. One latent Z has
P(Z=1|H)=3/4 and P(Z=1|not H)=1/4; every receipt reports that SAME Z.
After any positive number of yes copies, P(H|receipts)=3/4. Naive iid reuse gives
3^n/(1+3^n), tending to1. In the actual conditional source ensemble, squared
Brier regret is exactly (forecast-3/4)^2, proved by expanding expected squared
error. Eight copies therefore become more confident and less calibrated.
Distinct event IDs do not supply independent evidence. This sharp proper-score
comparison supplements, rather than replaces, existing shared-latent modules.

If the one-event likelihoods lie independently in
u in[2/3,5/6], v in[1/6,1/3] with fair H, posterior u/(u+v) has the sharp interval
[2/3,5/6]. Repeated copies of the same Z do not multiply those likelihoods.
This is a declared uncertainty rectangle, not universal robustness to arbitrary
dependence or missing model families.

**Stopping positive control.** Under iid Bernoulli likelihoods3/4 and1/4, stop
at the first yes or after three trials. The stopped transcripts are 1,01,001,000.
Their mixture probabilities sum exactly to1. Conditioning on each COMPLETE
transcript gives its exact source posterior and proper-score calibration.
This does not claim frequentist coverage of every Bayesian credible interval,
nor that ignoring a source-dependent observation policy is harmless.

**Misspecification negative control.** The actual future source is Bernoulli1/2,
but the model menu contains only Bernoulli1/10 and1/5. After m balanced yes/no
pairs, with equal priors, posterior mass on1/5 is
16^m/(16^m+9^m), approaching1. Yet its future prediction approaches1/5, with
heldout Brier risk approaching17/50 rather than the correct1/4. High posterior
mass among wrong survivors is not source adequacy. These are exact finite
calculations, consistent with the published asymptotic misspecification theory;
the finite example does not invoke that paper's general theorem.

**Rival/falsifier/status.** Rival: receipt multiplication or syntactic voting
improves truth confidence. REFUTED by exact source worlds and Brier excess.
Conditional Bayes laws: PROVED FINITE MODEL / CLASSICAL. Next lamp: independently
validate the actual conditional likelihoods and expand a misspecified menu;
calibration on a reused training distribution is insufficient.

## D22. Cost-optimal probing under destruction

For a finite declared deterministic carrier, a belief consists of
(original source,current carrier) pairs. The target is a function of ORIGINAL
source. Only actions enabled at every compatible current state are allowed.
Costs c_a>0 are explicit rationals. Homogeneous target beliefs are terminal.

**Finite-horizon theorem.** For every horizon h, define V_0(B)=0 on terminal
beliefs, infinity otherwise, and

    V_h(B) = min_a [c_a + max_y V_(h-1)(B_(a,y))]

for nonterminal B, considering lawful actions only. This equals the minimum
worst-case total action cost of any deterministic target-certifying policy of
depth at most h. Induction on h: each tree must choose a lawful first action;
each possible outcome must have a successful continuation; selecting the best
continuation attains the minimum. Source/current pairs retain backaction and
reset limitations. Reset actions exist only if explicitly present in the menu.
Communication cost can be added when specified per action/outcome; the present
implementation prices actions only. No unbounded-horizon approximation theorem.

**Greedy countermodel.** Three equally likely original states0,1,2; target is
their identity. `cheap` costs1, reports(0,1,1), and maps(0,1,2)->(0,1,1).
`full` costs5 and nondestructively reports(0,1,2). Gini gain/cost is1/3 for
cheap and2/15 for full, so the local rule picks cheap. But source1 andsource2
then have the same current carrier and identical future reports under every
word: original identity is permanently lost. Exact optimal cost is5.
Thus that greedy rule has no finite approximation ratio in this intervention
class. Any guarantee must restrict destructive effects or incorporate future
source-claim reachability.

**Independent oracle and algorithm comparison.** The Bellman implementation
caches belief/horizon states. The independent oracle instead generates all
complete public action/outcome strategy trees and simulates every original
source; it does not use Bellman minimization during generation. It enumerates
37 trees in the countermodel and agrees on5. Across **all64 two-state,
one-action deterministic output/transition/enabledness fields**, it enumerates
256 trees and agrees with Bellman, including losing and disabled cases.

A typed depth-two genetic policy search performs mutation/crossover, with
independent full-source validation of each candidate. Population4,
generations3, seeds0..9 finds cost5 on **2/10** runs; eight runs remain misses,
with no oracle rescue. A separate complete 54-genome CEGIS enumerator starts
with source0, obtains source counterexamples1 and2, then finds cost5 after
162 candidate evaluations. Its bounded candidate completeness comes from
enumeration and exact counterexamples, not evolution. Accepting the first
verified candidate is not a general cost-optimality theorem; cost optimality in
this particular countermodel is established by the separate oracle. One generation is an explicit genetic
failure control.

An initial scalar collision witness exposed an implementation bug: a full-source
collision could name an already fitted state paired with an unseen state. The
repaired verifier preserves BOTH conflicting original states, so CEGIS selects
the unseen witness. The regression remains tested. This repair does not change
the theorem or target. Status: CLASSICAL / PROVED FINITE HORIZON / EXACT TESTED;
greedy general guarantee REFUTED. Next probe: outcome-dependent costs and
state-limited resets, checked against a separately scoped exhaustive oracle.

## D23. Behavioral realization is not internal source identity

For every rational finite LTI model y_n=c A^n b of dimension d, a Hankel block
H_(i,j)=y_(i+j) factors into observability rows cA^i and reachability columns
A^j b. Therefore rank(H)<=d. Existing exact rational Hankel/rank code is reused.
No finite block supplies a global upper bound absent a realization contract.

**Two independent aliases.** Take A=diag(1/2,1/3), b=(1,1)^T, c=(1,1).
The moments are (1/2)^n+(1/3)^n and rank2. For
T=[[1,1],[0,1]], another coordinate realization has
A'=[[1/2,-1/6],[0,1/3]], b'=(2,1)^T, c'=(1,0).
The identity A'^n=TA^nT^-1 proves equality for EVERY n. The code compares the
non-diagonal recurrence with independent diagonal powers. This coordinate
change does not claim a second positive RC graph or physical topology.

Add an internal eigenmode3/4, keep c=(1,1,1), and use b=(1,1,0)^T. All old-input
moments remain identical to the2D model for every n because the third mode is
unreachable from that input. A NEW input b_new=(0,0,1)^T exposes(3/4)^n. The
combined three-row two-input Hankel block has exact rank3. Equivalently, a third
mode with zero output coefficient is unobservable under the old output even
when controllable; only an added output channel can reveal it. A different
sensor/input is a new source interface, not something recovered by more old
measurements.

**Rival/falsifier.** Rival: a minimal behavior realization identifies the actual
hidden dimension/topology. REFUTED by all-time unreachable-mode equality.
Hankel rank/minimal behavior: CLASSICAL / PROVED CONDITIONAL / exact nine-moment
controls. The all-time scope rests on the algebra above, not on nine tests.
Next probe: physically licensed input/output channels, stability and noise
bounds for an actual source; none is presently authenticated.

## D24. Output size, memory, proof size and witness access are different resources

**Zero-error one-way Index theorem.** Alice knows x in{0,1}^m; Bob receives an
arbitrary index i and must output x_i. For every deterministic one-way protocol
correct on every(x,i), fixed-width communication needs at least m bits.
If x!=z had the same message, choose a coordinate where they differ: Bob would
receive the same message and index but require two different answers. Hence
all2^m messages must be distinct. Sending x attains m. This bounds worst-case
zero-error one-way communication, not randomized average error or interaction.
Each answer has ONE bit; a semantic answer-size estimate does not replace the
communication lower bound. The m=4 receipt contains all120 pairwise collision
witnesses and the exact index that defeats each merge.

**Certificate/access separation.** One stationary unary source reports1 only
at time T and0 elsewhere. The all-zero target is refuted by the single probe
advance^T, but that word has length T and sequential cost T. Before T every
unary observation is0, so this is the shortest refuting word. T=19 is replayed;
the proof holds for every T. If licensed direct random access to coordinate T
costs1, the cost is1 instead. The toolkit and access mode therefore change the
resource bound while certificate cardinality remains1. The source needs an
explicit delay/clock state; no hidden nonstationary clock is smuggled into a
two-state source.

Given the integer T, this witness is computable. Existence of a witness for an
arbitrary unspecified source/probe map does not supply such a computation or a
uniform time bound: this retains Voyager O618/O638, not a claim that every fixed
finite instance is undecidable. D19/D20 minimum-state cardinality, D22 action
cost, and this communication lower bound remain separate resources.

Status: CLASSICAL / PROVED LOWER BOUND / finite exact collision witnesses.
Next lamp: specify representation and an effective source/probe evaluator
before claiming effective global refutation or proof-search complexity.

## Claim digest and independence boundary

| Claim | Verdict | Main boundary |
|---|---|---|
| D19a observable partial-action residual quotient | CLASSICAL / PROVED CONDITIONAL | Enabledness/context semantics declared |
| D19b common-legal-word equality always equivalence | REFUTED | Explicit nontransitive triple |
| D19c unbounded queue exact finite memory | REFUTED | Empty/readout and arbitrary delivery |
| D20a prefix repair/minimum residual quotient | EXISTING CLASSICAL EOS-02/03 replay | Complete finite source law |
| D20b residual signature memory-bit bound | PROVED CONDITIONAL | Known class initialization or owned observations |
| D20c history-only minimum-state learning | CLASSICAL / conditional implementation | Exact teacher and resets assumed |
| D20d engine invents its metagrammar/unrestricted categories | UNVERIFIED / NOT ACHIEVED | Constructors remain supplied |
| D21 confidence gain from repeated shared latent copies | REFUTED | Exact conditional Brier excess |
| D21 stopped full-transcript Bayes calibration | PROVED FINITE MODEL | Correct declared likelihoods |
| D22 cost optimality at finite horizon | CLASSICAL / PROVED CONDITIONAL | Positive costs, full finite law |
| D22 greedy finite approximation under destruction | REFUTED | Finite optimum versus irreversible failure |
| D23 behavioral minimality identifies hidden interior | REFUTED | Unreachable mode alias, input repair |
| D24 one-bit answers imply one-bit communication | REFUTED | One-way zero-error Index lower bound |
| D24 certificate cardinality bounds execution cost | REFUTED | Arbitrarily delayed single witness |

Independent evidence here means different finite implementations/derivations:
partition enumeration, pair/product BFS, signature repair, trajectory execution,
strategy-tree generation, Bellman recursion, diagonal moment powers and a
non-diagonal similarity recurrence. They share authored source laws and this
worker's mathematical interpretation. They are not independent reasoners,
empirical source observations, or proof-assistant verification. In TLICA terms,
φ resolution is conditional on declared tool closure; σ source adequacy and
physical contact remain separate; Bayesian calibration is not a truth score.

## Reproduction and primary-source assessment

```sh
python -m unittest tests.test_cambrian_d_computation -v
python scripts/cambrian_d_probe.py --output research/2026-10-13/CAMBRIAN_D_RESULTS.json
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The result JSON preserves the base SHA, Python version, implementation SHA256,
all generated source arrays, minimum-state oracle data, selected words,
evolutionary versus deterministic credit, calibration fractions, cost trees,
hidden-mode samples, and collision witnesses. Rationals serialize as strings.
No generated artifact is called a Lean theorem. Exact validation outcomes are
reported in the accompanying final commit receipt and integration report.

Primary references actually retrieved during this pass:

- Dana Angluin, *Queries and Concept Learning* (1988), original paper at
  https://homepages.math.uic.edu/~lreyzin/papers/angluin88.pdf. Membership,
  equivalence and sample-learning distinctions motivate the declared access
  contracts. The history learner belongs to the classical observation-table
  line, not a new invention of learning theory.
- B. L. Ho and R. E. Kalman, *Effective construction of linear state-variable
  models from input/output data*, NASA original report record:
  https://ntrs.nasa.gov/citations/19660046794. It attributes minimal realization
  to the classical source; the record has no downloadable full text. The rank
  and similarity claims above have their own explicit proofs.
- B. J. K. Kleijn and A. W. van der Vaart, *Misspecification in
  infinite-dimensional Bayesian statistics* (2006), authors' paper:
  https://arxiv.org/abs/math/0607023. Its abstract concerns concentration near
  KL-minimizing model points under stated assumptions; no universal guarantee
  is imported to our misspecified finite example.
- Richard Bellman, *Dynamic programming and a new formalism in the theory of
  integral equations* (1955), original primary paper record:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC528018/. This supplies historical
  attribution, not a proof of this particular destructive probe model. The AMS
  1954 PDF endpoint returned403 and was not treated as inspected full text.

No mathematical-priority claim is earned by these examples. The remaining
high-value frontier is restricted-access learning with genuinely weaker
teachers, compositional partial-action semantics, cost bounds under lawful
reset/communication contracts, and metaconstructors that come with proofs
instead of merely applying preengineered residual-state machinery.

## Final local validation receipt

On Python **3.12.14**, final-code validation passed:

- 21 namespaced targeted tests;
- complete repository suite: **1,623 tests**, 85.367 seconds, no failures;
- provenance verifier: **72 items**, including17 byte-identical research
  archives and55 mechanical namespace migrations;
- observer foundations probe and ordinal SUCC report probe, exit0;
- JSON replay and implementation-SHA256 agreement;
- whitespace validation before committing.

These are local checks. No new Lean module or GitHub CI job was run by this
worker. No branch was pushed and no shared ledger or historical import changed.

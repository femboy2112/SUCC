# X07 independent review — source-changing probability and causal order

Reviewed C17, C18, C19, C22, C23 and F48 at integrated base
`508f16881a4b145dffa13d0d3d336d1abcbda98c`, including
`observational_succ/swarm_probability.py` and the stated theorem hypotheses.
This review leaves cohort source files unchanged. Its independent exact probe
imports no cohort implementation; one additional differential test checks the
actual C17/C22 code against direct atomic path enumeration.

## C17 — composition, original labels and the category of elements

**SURVIVES.** The functor F_O acts on the current coordinate only, and finite
sum interchange proves composition. Original-label rows must remain separate.
The category of elements of this Set-valued covariant functor is actually a
**discrete opfibration**: fixing a source object and a base kernel forces the
unique target measure. The dossier's weaker split-opfibration statement is
correct. Conditioning on a recorded event is a different, partial operation;
C17 correctly refuses to claim a total normalized-outcome fibration.

`compose` retains ordered outcome pairs and sums over actual intermediate
states, checking source, carrier tags and dimensions. The independent test
covers all 256 pairs of deterministic two-state binary-outcome instruments;
for every initial state and outcome pair, the result agrees with an explicit
hidden-path sum. The exact substochastic grid adds 9,072 rational composition
checks, including null prefixes and null complete paths. These finite probes
support the implementation; the universal reason remains finite sum algebra.

The constructor of StochasticHistory enforces shape and normalization, while
`verify(registry)` performs provenance/replay validation. Merely constructing
that class does not certify that its supplied `joint`, path probability and
stored event sequence came from execution. C17's dossier explicitly distinguishes
replay verification and already tests corruption. No stronger authenticity
claim is warranted from the dataclass alone.

## C22 — full outcome diamonds and fixed events

**SURVIVES.** Equality of all outcome subkernel products is sufficient by
matrix composition and necessary by point initial states, provided the claim
quantifies over **every** initial original/current law. Keeping event identities
on outcomes avoids accidentally comparing (a,b) with an unlabeled or reversed
pair. The proof connecting linear extensions by adjacent incomparable exchanges
is correct, and independence must include all outcome pairs of the compared
instruments when the full joint outcome law is requested.

The differential test independently reconstructs each outcome atom and checks
`commutation_defect` on all 256 deterministic instrument pairs. The separate
probe checks all 1,296 rational half-grid kernel pairs, and a four-event DAG
with noncommuting same-coordinate dependencies produces equal full laws in
all 96 outcome-assignment/order comparisons.

Two boundaries deserve explicit retention. First, a single fair preparation
can have the same joint recorded-outcome/current law under both orders while
its original posterior differs; the read/flip/reset example in X07 gives the
exact witness. Second, equality of **every normalized posterior** is still
weaker than equality of outcome subkernels: DN=2ND gives identical partial
posterior maps but different likelihoods. Neither example contradicts C22's
stated full unnormalized and universally quantified condition.

The DAG theorem is for fixed declared events. It is not permission to move an
adaptively chosen action before the observation on which the choice depends,
or to infer causal independence from network delivery order.

## C18 — Bayesian gluing, support restrictions and correlation

**SURVIVES.** Direct substitution of the proposed common separator weight
`p(z)A_z B_z/Z` produces the exact posterior. On an active separator fiber,
positive diagonal scaling by the original conditional factors preserves matrix
rank on their support. Posterior conditional independence is therefore
rank-one likelihood on that **restricted support**, not necessarily on the
whole alphabet. A zero posterior separator fiber imposes no conditional-law
constraint. The independent probe checks 729 combinations of priors and
2×2 likelihood matrices, including zero prior coordinates: 584 positive cases
satisfy the iff, while 145 null cases have no posterior.

The duplicate-event example correctly preserves posterior 3/4 rather than
squaring the likelihood and obtaining 9/10. Its Fréchet interval [2/3,1] is
also exact: for two yes-events, the H joint mass lies in [1/2,3/4] and K in
[0,1/4]; with equal hypothesis priors the posterior is t_H/(t_H+t_K), minimized
at (1/2,1/4) and maximized when t_K=0. Separate marginal yes probabilities
therefore do not identify the coupling. Event IDs by themselves add no CI law.

## C23 — true conditional wealth versus duplicated marginal wealth

**SURVIVES.** Under the specified public-history predictable policy and
conditional absolute continuity, the next likelihood ratio has conditional
mean one. Alternative-zero branches have zero wealth forever; collapsing them
in the finite audit loses neither expected wealth nor later threshold crossings.
A null-impossible/alternative-positive outcome must be rejected, as implemented.
The theorem is not a guarantee under unknown model calibration or arbitrary
source laws.

Independent arithmetic reproduces the duplicate control: true terminal wealth
3 or 1/3 has P-expectation one, whereas squaring the marginal ratios gives 9 or
1/9 with expectation 7/3. The fake threshold-9 crossing probability 1/4 exceeds
1/9. Reordering receipt processing preserves a final path ratio under valid
joint-law diamonds, but a reordered *intermediate* wealth process has its own
filtration; this review asserts no equality of its threshold-crossing time or
maximum. Predictability and dependence arrows must be preserved separately.

## C19 and F48 — bridge limits

C19's multi-Kraus composition proof retains the proper CP maps and normalizers.
Its rational implementation cannot represent every square-root Kraus embedding
of a rational stochastic kernel, a limitation the dossier states correctly.
No general original-labeled ensemble-history implementation is claimed there.
X07 uses finite classical measures only, so it does not silently close that gap.

F48's original-support fibration has the opposite variance from forward law
pushforward; both are valid and are explicitly constructed in X07. Its finite
original-support actualization statement is deterministic. In a stochastic
model, a finite original can give every finite prefix positive probability
while the corresponding infinite event has probability zero. The fair-heads
control prevents promoting support compatibility to positive infinite-event
likelihood.

## Review verdict

The reviewed mathematical claims survive within their declared source and
conditioning domains. No source correction is requested. X07 adds a total
subprobability action, its partial normalized action, and a backward support
fibration on a certified trace quotient, with two stronger-information loss
counterexamples. All are paper derivations plus exact controls, with no Lean
formalization, empirical source authentication, priority claim, or RH inference.

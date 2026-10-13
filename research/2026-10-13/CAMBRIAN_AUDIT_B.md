# Auditor B — independent event, memory, and quantum implementation

**Verdict:** the audited root stochastic and frozen-F results survived the
declared exact holdouts. No implementation defect was found in those scopes.
A stronger conditional-stability bound is independently proved below; the
principal had already incorporated that sharpening after Auditor A. No own
cluster-A theorem or implementation was audited here.

Audit checkout: `01bf38fb282872cfe28362321809b30ea9f1b3f9` in `audit_b`.
Frozen F source: `21ef59994f11d488a31632f731f4e4d7d9adbc77`.
Root ST7 sharpening: `484dc20c710219c2bef473f52ed83e18971096f0`.
The actual compared source/dependency SHA-256 hashes and the observed root
checkout SHA are in `CAMBRIAN_AUDIT_B_RECEIPT.json`. Root's mutable integration
head is not substituted for a source-code hash. The F file is checked against
its frozen hash before any differential comparison.

The initial hypotheses and planned oracle representations were frozen in
`CAMBRIAN_AUDIT_B_FIRST_PASS.json`. The auditor had read the supplied theorem
statements before execution. This is implementation independence and an
independent derivation, not a blind referee or a different-model witness.
The root/F proofs, test algorithms, and own oracle are not called interchangeable
forms of empirical independence.

## CB-AUD1 — Joint-law descent and source/receipt correlation

Oracle: build literal atoms `(initial state, final state, receipt)` with rational
weights. Sum by the declared post-report only after forming the event law.
Starting-report fibers pass exactly when those complete joint event laws agree.
This calculation imports neither `report_receipt_row` nor root normalization or
report-pushforward algorithms. Root methods are called only to compare the
already-computed expected result.

The fresh enumeration uses denominator **five**, unlike the root's original
denominator-two fixture. There are 56 normalized four-atom laws, 56² pairs,
and four old/new report-partition combinations: **12,544** cases. Five priors
include the fresh `(1/7,6/7)` and `(2/3,1/3)` cases. Every descending case is
checked against exact fine and coarse event evidence and all conditioned
successor-report weights. Result: **68,880** filter comparisons pass;
**5,656** nondescending coarse filters are correctly rejected.

Null receipts retain no posterior. Their exact zero evidence is compared;
no division or prior substitution occurs. Exhaustion includes deterministic
and partially supported laws, identity/coarse reports, same-marginal rows,
and rows whose likelihoods differ while normalized one-report posteriors agree.
This verifies the implementation in the enumerated finite regime. The general
all-prior theorem still relies on finite reindexing and Dirac-prior arguments,
not a finite denominator survey.

**Status:** exact finite implementation CORROBORATED at this declared scope;
root's general classical proof has no defect identified. Source authenticity
and estimated empirical likelihoods are outside the audit.

## CB-AUD2 — Finite causal histories and the hidden-selector firewall

A separate oracle propagates **unnormalized path weights** across four
changing-epoch kernels before computing the total likelihood and final posterior.
No intermediate root Bayes update is used. Four-state sources have two report
fibers; hidden fine-state splits vary within each fiber while report/receipt
rows agree. Every one of the **16** four-step receipt words agrees with root's
reported joint likelihood and final coarse posterior.

For a public-history-adaptive control, the previous receipt selects an alternate
lawful instrument. Freeze the resulting selected instrument path on each word
and compare to the direct path atom law. All **16** paths agree. Root executes
a supplied path; this test does not pretend it implements an adaptive chooser.

**Negative control with exact quantifiers:** two source states have the same
coarse report. Action A always reaches post-report u and returns receipt z;
action B always reaches v and returns z. Each action separately descends.
A selector which chooses A on hidden state 0 and B on hidden state 1 gives
different post-report laws from the same original coarse report. The selected
mixture therefore does not descend. Root correctly rejects that new mixed
instrument. Individual action descent alone does not transport a selector
depending on unavailable hidden information.

**Status:** positive finite history comparisons pass; hidden-policy generalization
REFUTED as an inference by this two-source countermodel. The paper's exclusion
of hidden-state selectors is essential and correctly stated.

## CB-AUD3 — The sharp conditional TV bound uses the larger event mass

Let P,Q be normalized laws on the same finite event space, E one receipt event,
`α=P(E)>0`, `β=Q(E)>0`, and `ε=TV(P,Q)`. Their conditioned report laws satisfy

\[
\boxed{TV(P(\cdot\mid E),Q(\cdot\mid E))\le
       \frac{\varepsilon}{\max(\alpha,\beta)}.}
\]

**Independent proof:** assume `α≤β`. Write p,q for the conditioned laws and let
S be the subset of report coordinates on which `q_i>p_i`. Then
`q(S)-p(S)=TV(p,q)`. The full-law TV dominates the discrepancy of the event
`E∩S`, hence

\[
\varepsilon\ge \beta q(S)-\alpha p(S)
 =\beta\{q(S)-p(S)\}+(\beta-\alpha)p(S)
 \ge\beta TV(p,q).
\]

Swap P,Q for the other ordering. This proof uses a maximizing event subset,
not the earlier triangle-inequality proof yielding the valid but weaker
`ε/min(α,β)` bound. No null conditional law is assigned.

Exhaust all normalized four-atom laws with denominator seven and both receipt
events. **25,088** positive-conditioning cases pass, including **21,280** with
unequal event masses. **3,712** null cases are explicitly excluded.

An unequal-mass sharp case uses `α=1/5`, `β=3/5`, event atoms
P=`(1/5,0)`, Q=`(1/5,2/5)`, and complement masses `4/5`, `2/5` on the same
single coordinate. Here `ε=2/5`, conditional TV=`2/3`, and `ε/max=2/3`.
For equal rare masses `10^-6`, put their rare atoms on opposite report values
and identical common mass on one report. Full TV is `10^-6`, conditional TV
is one. This confirms sharpness and the necessity of an event-probability floor
for a uniform conditional-stability guarantee.

**Status:** CLASSICAL / PROVED LOCAL general finite-law bound, plus exact
independent controls. The root's corrected stronger statement is supported.
No fix to root implementation is necessary: it implements exact descent,
not an approximate filter using this bound.

## CB-AUD4 — Full block recurrence versus eliminated memory

Oracle: independently assemble the unpartitioned block matrix
`M=[[A,B],[C,D]]` and input matrix `G=[E;H]`. At each successor compute
`state_next=M state+G u` using local rational matrix/vector multiplication.
Only after that computation call F's memory successor using the resolved
history and initial hidden state. Neither F's simulation nor matrix helpers
provide the expected answer.

On **72** fresh rational block systems with hidden dimensions 1,2,3 and two
resolved/input coordinates, all **648** successors agree. Zero/partly zero
couplings and unrestricted hidden initial states are included. The frozen seed
is `2026101302`; every value is an exact Fraction.

Independently multiply `B D^k C` and `B D^k H` for 2h+4 lags in each source.
All **1,152** kernel matrices match F's output. Independently compute the
characteristic coefficients using trace recurrence and evaluate the resulting
Cayley–Hamilton identity; all **72** evaluated identities are zero.
This is a different route from F's finite coefficient test. Its role is to
check the arithmetic and finite-horizon criterion; the all-lag extension is
the classical Cayley–Hamilton paper proof, not the sampled future window.

The h=4 nilpotent shift gives `BD^kC=0` for k=0,1,2 but `BD^3C=1`.
The implemented closure certificate correctly rejects it, confirming that
testing only h−1 coefficient positions is insufficient in general.
A scalar source with x0=0,z0=1,B=1,C=H=E=0 has x1=1; dropping the initial
hidden-state forcing would give zero. The exact recurrence preserves it.

**Status:** the audited discrete elimination and finite coefficient implementation
passes. The continuous variation-of-constants result is paper mathematics,
not an executed continuous-flow solver. The audit does not infer unique
physical interiors from memory kernels or general nonlinear fluid closure.

## CB-AUD5 — Quantum effects, posterior backaction, and conditioned distance

Oracle: directly multiply `K ρ K^T`, compute its trace, and normalize only a
positive trace. This uses local exact matrix products, not imported instrument
probability/update algorithms. For projectors P0,P1 and reset Kraus
`|0><1|`, `K^T K=P1` is verified. Current Z effects therefore agree for the
Lüders and reset instruments. **20** exact density matrices are tested:
18 diagonal priors with denominator seventeen and two rational pure states.

For input P1, direct posteriors are P1 versus P0. A future Z read gives laws
`{0:0,1:1}` versus `{0:1,1:0}`. F's reported countermodel agrees exactly.
Current POVM equality therefore fails to determine future observation behavior.

The branch filter `diag(1,3/5)` gives conditioned distance `25/106` for P1
and `diag(1/10,9/10)`, greater than the input distance `1/10`. Direct event
masses are `9/25` and `53/125`. These are exact diagonal trace distances;
no unconditional CPTP contraction is contradicted because normalized
conditioning is state-dependent and not a trace-preserving linear channel.

## CB-AUD6 — Verified commutative quantum-to-joint-kernel bridge

Scope: computational-basis sources `P_s=|s><s|`, diagonal mixtures
`ρ=Σ_s μ_s P_s`, and Kraus branches preserving diagonality on each basis
source. The audited projector/reset family has this property. Define

\[
I(s;t,z)=(K_zP_sK_z^T)_{tt}.
\]

Each row is nonnegative and sums to one by instrument completeness.
Linearity gives the unnormalized diagonal posterior coordinates
`Σ_s μ_s I(s;t,z)`; their sum is the quantum receipt probability. Dividing
by the same nonzero evidence is **exactly** the finite classical filtering
operation. Null evidence has no conditional posterior in either model.
This proves the bridge for every diagonal prior for these instruments.

The independently compiled Lüders rows in `(t0,z0),(t0,z1),(t1,z0),(t1,z1)`
order are `(1,0,0,0)` and `(0,0,0,1)`; reset rows are `(1,0,0,0)` and
`(0,1,0,0)`. Their receipt marginals agree source by source while their
joint next-state/receipt laws differ. Using identity basis reports, both
individually descend and root's conditional kernels match direct density
updates on all **72** comparisons (18 diagonal priors × 2 receipts × 2
instruments). F's incompatible future Z laws agree with those different
compiled kernels.

**Status:** explicit paper bridge plus exact finite comparison passes. This
does not extend to arbitrary coherent inputs, arbitrary noncommutative
observational quotients, quantum state tomography, or an empirical cognition
model. A Kraus branch creating off-diagonal coherences requires a larger
representation; it cannot be silently compiled into only two basis labels.

## Replay, independence boundary, and integration

During the audit F was read from its frozen separate worktree. The script
checks hashes of both F dependencies against the modules used by its dynamic
import. Explicit initial replay command was

```sh
python scripts/cambrian_audit_b_probe.py \
  --f-repo /workspace/scratch/6d134115e8ca/f_physics \
  --root-repo /workspace/scratch/6d134115e8ca/SUCC --save
```

After the unchanged F source is integrated, a checkout containing both modules
can replay `python scripts/cambrian_audit_b_probe.py --save`. The script defaults
to its own repository, avoiding a durable dependency on temporary worktree paths.
Its frozen F hash deliberately fails if the target implementation changes;
such a change requires a fresh audit rather than inheriting this verdict.

All added files are audit-only. Shared ledgers, CI, architecture, and tested
implementations were not modified. Receipts use source hashes and actual output;
no GitHub CI, Lean proof, external experiment, academic novelty, or empirical
source authentication is invented. Finite enumeration corroborates exact
implementations only in its enumerated scope. General claims rest on the stated
paper derivations and their load-bearing source/action/initialization hypotheses.

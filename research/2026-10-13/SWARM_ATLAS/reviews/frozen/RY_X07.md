# SWM-X07 — Stochastic trace histories have forward weights and backward original support

## 1. Original question

Construct the stochastic counterpart of F48's original-history fibration while
allowing exactly those event exchanges certified by C22. Can one object retain
original identity, changing carrier, event likelihood, null events, posterior,
and partial causal order? Which information is lost by keeping only supports,
terminal marginals, or normalized posteriors?

## 2. Existing mathematical context

Finite nonnegative kernels, categories of elements, trace monoids and conditional
normalization are classical constructions. This is a direct synthesis with full
elementary proofs, not a claim of mathematical priority. C17, C18, C19, C22,
C23 and F48 were read at integrated base
`508f16881a4b145dffa13d0d3d336d1abcbda98c`; the relevant integrated source commits
are `45f4df22cdd7172ae376d64b1a788240b46341ae` (probability) and
`216651461e182c2a9ded1796c34485e2e34a29e3` (lawful histories).
`X07_REVIEW.md` independently audits their load-bearing probability claims.
No external theorem is used to replace the proofs below, and no archival import
was modified. Novelty of this formulation is **UNVERIFIED**.

## 3. Proposed SUCC objects and common ambient

Fix a nonempty finite original index set O. Let FinSubStoch_Q have nonempty
finite carriers X, row-substochastic rational kernels K:X→Y, and ordinary matrix
composition. Set

`M_O(X)={μ:O×X→Q_{≥0} : Σ_(o,x) μ(o,x)≤1}`,

including the zero measure. For K:X→Y, define the **original-preserving** map

`F_O(K)(μ)(o,y)=Σ_x μ(o,x) K(x,y)`.

A complete finite instrument gives outcome kernels K_(a,r), whose sum over r
is stochastic. An individual outcome kernel is sub-stochastic. A disabled
operation may instead be represented by zero row mass in an explicitly partial
instrument; missing mass is not silently treated as an observed outcome.
Originals are never summed out in F_O. The mathematical contract assumes the
current carrier contains the latent memory needed for its kernel law.

For concurrent histories restrict to endokernels on one carrier X. Let E be
an alphabet of typed event labels `(instrument identity, recorded outcome)`.
Declare a symmetric irreflexive relation I⊆E×E only after checking
`K_e K_f=K_f K_e` on the **complete carrier**. Let M(E,I) be words modulo adjacent
exchanges `ef~fe` for (e,f)∈I. Repeated physical event occurrences can be given
separate identities. A fixed receipt DAG requires certified independence for
incomparable events and preserves all adaptive-choice dependencies.

Fix an initial law μ_empty of total mass one. For a trace h, put
`μ_h=μ_empty K_h`, `Z_h=Σ μ_h`, and, only if Z_h>0, `J_h=μ_h/Z_h`.
Z_h is the event-path likelihood; J_h is the joint original/current posterior.
The original support is `P(h)={o:Σ_x μ_h(o,x)>0}`.

## 4. Candidate theorem

**Weighted stochastic trace theorem.**

1. F_O is a functor to Set. Its category of elements projects to FinSubStoch_Q
   as a **discrete opfibration**, hence in particular a split opfibration.
2. The word-kernel map factors through M(E,I) iff every declared generator
   exchange has equal product kernels. Equivalently each such exchange preserves
   the full unnormalized original/current law for every initial probability law.
   Consequently μ_h, Z_h and positive J_h are well defined on traces.
3. For a kernel K, `Q_K(J)=JK/|JK|` with domain `{J:|JK|>0}` defines a partial
   map on normalized joint laws. These partial maps compose exactly:
   `Q_L∘Q_K=Q_(KL)`, including equality of their domains. Thus normalization
   yields a functor to the category of sets and partial functions, and an exact
   partial trace action. Zero remains a valid object of the unnormalized action
   and has **no** normalized posterior.
4. In the trace-extension category, an arrow h→hu is labeled by extension u.
   The assignment P is a contravariant functor by inclusion `P(hu)⊆P(h)`.
   Its category of elements is a **discrete fibration**. For deterministic
   instruments and a full-support original prior, this is exactly F48's
   lawful-original-support presheaf, now recovered from stochastic weights.

For a fixed finite DAG whose incomparable **instruments** satisfy every
outcome-pair diamond, all linear extensions have the same event-labeled joint
record/current/original law. For every positive observed outcome assignment,
likelihood and original posterior are therefore independent of linear extension.

## 5. Proof attempt — complete derivations

**Forward weights.** Nonnegativity and row sums at most one give
`|μK|≤|μ|≤1`. For composable K,L,

`((μK)L)(o,z)=Σ_y Σ_x μ(o,x)K(x,y)L(y,z)=(μ(KL))(o,z)`.

The identity kernel preserves every entry. Hence F_O is a functor. An object
of its category of elements is (X,μ), and an arrow over K:X→Y is present from
(X,μ) to (Y,ν) exactly when ν=μK. For each source object and base arrow K there
is one outgoing arrow above K, with uniquely forced target (Y,μK). This proves
discrete opfibration directly. The chosen lift of KL is the composite of chosen
lifts, giving the split structure. No normalized conditioning is hidden in it.

**Trace descent.** Replacing `u e f v` by `u f e v` preserves the product because
`K_u(K_eK_f)K_v=K_u(K_fK_e)K_v`. A finite chain of defining exchanges preserves
it; concatenation is respected. Conversely, descent identifies the traces ef
and fe and therefore their product kernels. Equality of products implies
μK_eK_f=μK_fK_e for all original/current μ. For the converse use a fixed original
o and point preparation at every current x. Equality of the (o,y) entry recovers
each matrix entry. The **all preparations** quantifier is essential.

**Partial normalization.** Let z=|JK|. If z=0, nonnegativity gives JK=0, hence
JKL=0; a null prefix cannot acquire positive probability by extension. If z>0,
then `|Q_K(J)L|=|JKL|/z`. Therefore both sides of the asserted partial-map equation
are defined exactly when |JKL|>0, and on that domain

`Q_L(Q_K(J))=(JKL/z)/(|JKL|/z)=JKL/|JKL|`.

This also proves path likelihood multiplication with the actual conditional
probabilities. Identities normalize an already normalized law to itself. The
partial functor is therefore coherent even at null-event boundaries. This does
not make normalization a total map out of the zero measure.

**Backward original support.** If an original row is zero in μ_h, it stays zero
under every nonnegative extension kernel. Thus P(hu)⊆P(h). Inclusion maps obey
identity and composition. Given a base arrow h→hu and an element o∈P(hu), the
unique lift ending at (hu,o) starts at (h,o), proving discrete fibration. In the
deterministic case, each original o has exactly one lawful current evolution;
with initial positive weight π_o, its row has weight π_o if its event history
matches and zero otherwise. Hence its positivity is equivalent to F48 replay.
The forward measure opfibration and backward support fibration have different
variance; neither is being substituted for the other.

**DAG version.** Every two linear extensions are related by adjacent exchanges
of incomparable events: move the first event of the target ordering leftward;
all crossed events must be incomparable, then induct on the remaining events.
Apply the outcome-kernel diamond at every exchange. Keeping outcomes attached
to the named events preserves the entire joint assignment. Summing assignments
or terminal states and normalizing a positive assignment gives the claimed
marginals and original posterior. This permits no deletion of causal dependencies.

## 6. Crucible and exact receipts

**Endpoint and readout laws can lose original meaning.** From a fair original
bit, let A read the bit without changing it, B flip it without a reported bit,
and R reset it to zero. Ignoring outcomes, A has transition I and B has F, so
these transitions commute. The labeled readout is fair in both ABR and BAR;
the terminal carrier is zero in both. For observed readout 0, both event masses
are 1/2 and both current posteriors are δ_0, but the original posteriors are
respectively δ_0 and δ_1. Equality after dropping the original index is insufficient.

**Even every positive joint posterior can agree while likelihoods disagree.**
Take two outcome kernels

`D=diag(1/2,1/4)`, `N=[[0,1],[0,0]]`.

Then DN=(1/2)N and ND=(1/4)N. Both are outcomes of legitimate complete
instruments: add a complementary outcome that keeps each missing row mass on
its original state. For every preparation with positive mass at current 0,
normalized joint original/current posteriors coincide, and the null domains
coincide. Yet event likelihoods differ by a factor of two. For the fair diagonal
original/current prior the masses are 1/4 versus 1/8. Thus positive-posterior
agreement alone cannot certify the weighted trace quotient.

**Null diamonds are possible.** Two nondestructive coordinate projectors on two
bits commute. The prior supported on originals 00 and 11 gives zero probability
to the joint event first-bit 0, second-bit 1. Its unnormalized measure and support
are zero/empty, while its normalized posterior is undefined. Commutation does
not imply occurrence or nonempty support.

**Finite positive prefixes do not imply a positive infinite event.** On a
singleton original/carrier, repeated independent fair heads uses K=[1/2].
Every finite prefix has mass 2^(-n), support {o}, and the same normalized law.
The infinite all-heads event has probability at most 2^(-n) for every n, hence
zero. The support intersection remains {o}; it asserts compatible originals,
not positive probability of the infinite outcome path. Exact depths 0,…,16
are a control for the formula, not the infinite proof.

`X07_RECEIPT.json` independently checks all 36 two-state half-grid substochastic
kernels in 1,296 ordered pairs, including 300 commuting pairs. Across seven
original/current laws this gives 9,072 direct hidden-path comparisons, 7,155
positive normalization checks and 1,917 null cases. Boolean relational support
composition agrees in all 1,296 pairs. A four-event DAG with dependencies a<c
and b<d has six linear extensions; all 16 outcome assignments agree across
all six orders, giving 96 full joint-law comparisons using noisy local reads
with destructive resets. These are exact finite controls, not the universal proof.

## 7. Verdict

**PROVED LOCAL / CLASSICAL INGREDIENTS:** the total subprobability functor and
discrete opfibration; trace descent criterion; coherent partial normalization;
and contravariant original-support fibration with deterministic recovery.
**REFUTED:** using only unobserved transitions, one preparation's endpoint law,
normalized posterior agreement, or finite positive prefixes to infer the stronger
weighted/positive-infinite-history assertions. No Lean kernel verification is
claimed. Mathematical novelty and physical source authentication remain unverified.

## 8. Remaining obstruction and next falsification opportunity

The concurrency quotient uses a fixed complete carrier and globally certified
exchanges. Variable carrier spaces need typed squares with specified intermediate
carriers; state-dependent independence needs a reachable-support theorem stable
under every permitted surrounding context. Adaptive event choices cannot be
moved before their enabling observations. Costs need their own diamond law.
Source IDs do not authenticate latent-variable completeness.

A concrete next probe is a proposed context-dependent independence certificate:
close its allowed preparation family under every enabled prefix, then check
both product kernels on the whole reachable cone. A certificate that checks
only the initial distribution can fail after a prefix selects a hidden state.
A quantum extension should use outcome CP maps, retaining unnormalized
original-labeled density blocks; C19's individual density evaluator alone does
not implement that ensemble object. No such extension is asserted here.

## 9. Cross-domain connection and invariant

C17 supplies probability-valued original/current transport; F48 supplies
contravariant surviving originals; C22 supplies event diamonds. X07 relates
these by the **actual map** `μ_h ↦ {o:Σ_x μ_h(o,x)>0}` and proves its trace
invariance and backward restrictions. The stronger retained invariant is the
whole μ_h, from which likelihood, posterior and support follow. The converse
maps are absent: support cannot determine probability; normalization cannot
determine likelihood; dropping originals cannot determine original inference.

This gives an exact finite stochastic history object rather than merely placing
three dossiers next to one another. C18's source coupling resides in μ_empty
and kernel state, while C23's correct wealth ratio uses the derived path
likelihoods under its two declared laws. The synthesis supplies no RH-facing
positivity identification and no empirical proof of source completeness.

## 10. Deliverables and provenance

Isolated branch `research/swarm-cross-x07-2026-10-13`, based on
`508f16881a4b145dffa13d0d3d336d1abcbda98c`. Owned files are this dossier,
`X07_REVIEW.md`, `X07_RECEIPT.json`, `scripts/swarm_cross_x07_probe.py` and
`tests/test_swarm_cross_x07.py`. The probe imports no cohort implementation;
the tests additionally compare C17 composition and C22 commutation directly
against independent atomic path sums for all 256 ordered pairs of two-state,
binary-outcome deterministic instruments. Eight targeted tests pass.

Executed:

```sh
python scripts/swarm_cross_x07_probe.py --output research/2026-10-13/SWARM_ATLAS/X07_RECEIPT.json
python -m unittest discover -s tests -p test_swarm_cross_x07.py -v
```

The receipt records the probe SHA-256. Repository-wide validation belongs to
the parent integration gate; this branch makes no separate full-suite, remote
publication, or CI-success claim.

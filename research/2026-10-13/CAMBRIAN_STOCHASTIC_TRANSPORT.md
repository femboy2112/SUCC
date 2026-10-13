# Joint-kernel source-changing Bayesian transport

Base: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`; implementation:
`observational_succ/cambrian_stochastic_transport.py`.

## Hole contract and truth boundary

The missing edge is **probability-law-preserving descent through an actual
declared source intervention**, beyond O599–O609's possibility supports.
Let finite nonempty source sets S,T have total reports q:S→O, r:T→P;
Z is a finite receipt alphabet. A declared instrument I(s;t,z)≥0 has
Σ_(t,z) I(s;t,z)=1. Source identity, basis and chronological chart contracts
must agree. The current construction assumes a complete mathematical source,
not empirical attestation or available sensors. Define

    J_s(p,z) = Σ_{t:r(t)=p} I(s;t,z).

**ST1:** A joint report/receipt stochastic kernel V:O→Prob(P×Z) satisfying
J_s=V(q(s)) exists on q(S) iff q(s)=q(s′) implies J_s=J_s′.
The proposed statement was derived before the first execution; this dossier
was written after that derivation and initial code, so it is not a blinded
precommit. Initial rival: support descent or two marginal descents suffice.
The cheapest falsifier is two hidden states with the same q, equal receipt
and report marginals, and opposite correlations. See ST4.

The theorem is classical finite labelled-kernel lumpability; novelty is
**new-to-SUCC source-typed interface**, not established academic priority.
The weakest useful sufficient hypothesis is the displayed joint-row fiber
condition. It is necessary for universal all-prior *joint-law* preservation;
a prior-specific statement can be weaker. It closes the stochastic edge in
the EODCS roadmap, without implying any infinite or physical realization.

## General proofs

**ST1 (iff and uniqueness).** Necessity follows by evaluating V at the shared
q report. Sufficiency: choose one representative of each inhabited q fiber
and use its J row; the hypothesis makes the choice immaterial. Nonnegative
normalized rows follow by summing a normalized instrument. Uniqueness holds
on q(S). Nothing is defined or required on unused O elements.

**ST2 (Bayesian commutation including evidence).** For *every* prior μ on S
and receipt z, write

    W(p,z)=Σ_s μ(s)J_s(p,z)
          =Σ_o (q_*μ)(o)V(o;p,z).

The second equality is finite reindexing using ST1. Consequently evidence
Pr(z)=Σ_p W(p,z) agrees on both sides. If Pr(z)>0, dividing by that same
number proves r_* posterior_T = posterior_P. If Pr(z)=0, neither side has
a conditional posterior; the implementation returns None, not a fabricated
distribution. Conversely preservation of the *joint law* for every μ
implies ST1 by testing μ=δ_s and μ=δ_s′ within one fiber. Equality of
normalized posteriors alone does NOT prove this converse (ST5).

**ST3 (finite adaptive histories).** Consider time-indexed source charts and
instruments, each satisfying ST1 for its current and next reports. Induct
on finite receipt history: equality of current pushed priors, ST2 and
matching chart imply equality of next evidence and next pushed posterior.
Products of conditional evidence give the same entire path likelihood.
Actions may be selected from the common coarse receipt history if every
selected action has its own ST1 certificate; both sides then select the
same action. A selector depending on unavailable hidden state is excluded.
The code executes a supplied finite sequence; it does not execute an
adaptive chooser or prove source authenticity. Fixed finite path tests use
a separate unnormalized event-path oracle.

**ST4 (marginal/support firewall).** In state order x,y and receipt order z,w,
two J rows are (3/8,1/8,1/8,3/8) and (1/8,3/8,3/8,1/8). Both full supports
and both marginals agree. After z, the target posteriors are (3/4,1/4) and
(1/4,3/4). Hence neither full support nor matching both marginals gives
Bayesian transport. This is a source-coupling obstruction.

**ST5 (normalized-posterior firewall).** One target report x, two receipts
z,w, and hidden J rows (1/4,3/4),(3/4,1/4). Every defined target posterior
is the point mass at x, while evidence likelihoods differ. A posterior-only
test misses a false joint-law square.

**ST6 (universal one-step repair).** q*(s)=(q(s),J_s) is the coarsest
refinement preserving old reports and this next joint law. If another
statistic h determines both q and J, map h(s) to the determined pair;
well-definedness proves factorization. It is a sufficient mathematical
representation, not a manufactured physical instrument. q* need not be
stable for future instruments; each later step needs its own check.

## Verification

**ST7 (rare-receipt stability boundary).** Let two normalized joint laws
have total-variation distance ε and give positive receipt masses α,β.
The conditional report laws have TV at most ε/max(α,β). To prove this,
suppose α≤β. Multiply the difference of normalized receipt-slice laws by
β: β(u−v)=(P_slice−Q_slice)+(β−α)u. Apply the triangle inequality.
The complementary slices
have L1 difference at least β−α; therefore the numerator is bounded by
the full joint L1 distance 2ε. Divide by 2β. Interchange the laws if β≤α.
The bound is sharp: one row assigns ε to (x,rare), another assigns ε to
(y,rare), and both assign 1−ε to (x,common). Joint TV=ε, rare-event masses
both ε, and conditioned TV=1. Thus arbitrarily small joint discrepancy
does not imply uniformly small conditional error without a lower bound
on the observed event probability. This is a classical conditional-law
bound; the implementation certifies exact descent, not approximate filters.
Auditor A independently sharpened the initial valid min-denominator bound
to this max-denominator form; the principal re-derived it before acceptance.
It is also sharp for unequal masses: P gives α to (x,rare), Q gives α
to (x,rare) and β−α to (y,rare), with common-event totals 1−α and 1−β
on x. Joint TV=β−α; conditional TV=(β−α)/β.

`python -m unittest discover -s tests -p 'test_cambrian_stochastic_transport.py' -v`
passed 7 tests initially. The exhaustive control checks 400 complete
two-state rational joint laws against independent event-atom dictionaries,
with five priors and two receipts for each descending case. A separate
four-step fine path oracle checks all 16 receipt words in a three-state
changing-epoch example. Null receipts, float/negative/unnormalized laws,
partial coverage and stale/cross-source contracts are rejected.

These are exact finite checks of an explicit general paper proof, not a
Lean refinement of Python, an empirical Bayesian model, or unrestricted
probability inference from evidence. Fresh hostile audits are recorded
separately in the campaign report.

## Primary provenance

Kemeny and Snell, *Finite Markov Chains*, §6.3, Theorem 6.3.2 (block-row
lumpability criterion), author textbook scan:
https://math.pku.edu.cn/teachers/yaoy/Fall2011/Kemeny-Snell_Chapter6.3-4.pdf
(read through web retrieval). ST1 reduces to this criterion when receipts
are trivial and S=T. Our proof explicitly handles the joint receipt row.
Ledoux, White and Brushe's *On the relationships between lumpability and
filtering of finite stochastic systems* is relevant prior art, but its
HAL full text was blocked in this session; no theorem is attributed to that
unread full text. The finite reindexing/normalization proof above is complete.

Next lamp: independently source-authenticated likelihoods, partial sources,
approximate joint descent with certified error, and stochastic history
compactness. Generic positivity and this transport do not identify the
completed arithmetic Weil distribution or prove RH.

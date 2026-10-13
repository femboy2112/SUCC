# X05 independent adversarial review of C20/C21

Reviewed source snapshot: `508f16881a4b145dffa13d0d3d336d1abcbda98c`. The exact audited module hash is frozen in `X05_RECEIPT.json`. This reviewer did not author the C cohort module or its original tests. The X05 oracles were written independently after inspecting its API and theorem claims.

## C20: exact finite garbling feasibility — SURVIVES

The equation EG=F is the correct common-original-source experiment simulation contract. The row-stochastic feasible set is bounded, and minimum positive support gives an independent set of equality-matrix columns: a supported null direction permits movement to a nonnegative boundary, reducing support. Extending those columns to a rank-sized basis establishes completeness of the implemented basic-solution enumeration. Exact Gaussian elimination returns rational candidates; no float tolerance is present. Inconsistent equality constraints are a valid early negative. The `max_bases` guard raises before an incomplete enumeration can be called infeasible.

Independent oracle: write E's first-report probabilities as p,q and F's as r,s. If p=q, feasibility is exactly r=s. Otherwise let d=(r-s)/(p-q), v=r−pd, u=v+d. A binary garbling exists exactly when u,v∈[0,1]. Exhaustively comparing all 625 quarter-grid pairs produced no discrepancy; 273 are feasible. Each reported channel was multiplied independently. This audit is complete only for that finite grid; the general conclusion rests on the argument above.

The ordinary Blackwell decision comparison does not imply a comparison of backacting instruments. C20 correctly says so. A new two-original-state preserve/reset model gives the smallest original cardinality when a constant first report is allowed. Its all-horizon negative is an indistinguishability induction, not an extrapolation from tested horizons.

## C21: finite-horizon zero-error expected cost — SURVIVES

The subject solver keeps the complete joint original/current posterior. It omits zero-probability branches, rejects any action with an infeasible positive continuation, uses a finite horizon, and minimizes exact expected cost. The recurrence and the no-randomization-improvement claim follow by induction on that finite horizon. Nonnegative costs justify immediate zero-cost stopping on already certified beliefs. Source and carrier tags are checked for the declared model; tags do not authenticate empirical preparations. The implementation admits horizons 0–20, a software bound smaller than the general finite-horizon paper theorem.

Independent oracle: enumerate all binary-report trees up to depth two, with leaf guesses 0 or 1, and replay each original through complete instrument paths. A tree is feasible iff total error mass is exactly zero. This uses no normalized posterior update, memoized Bellman equation, or subject helper. It exhausts 256 ordered pairs of deterministic two-state actions, two positive priors, and horizons 0–2; full-support noisy menus supply another 12 comparisons. All 1548 costs/feasibility verdicts agree. Unequal action costs distinguish feasibility from expected-cost optimization.

The destructive parity argument remains valid beyond finite search: after either first destructive bit-read, a pair of positive-prior original states with opposite target has exactly the same current state and record. All later histories have equal conditional laws under any current-state kernel. A source reset, external side information, or a omitted latent state would change the contract. They are not licensed by the stated example.

## Boundaries requiring preservation

- A `StochasticHistory` supplied to the solver is a declared mathematical posterior. The class constructor alone is not evidence of lawful replay; provenance-sensitive callers must check replay. The solver's optimization theorem assumes its input joint law is the intended one.
- Zero-prior alternatives are outside a probabilistic certificate. Full support is required to cover every admitted finite original label.
- C21's implementation has total instrument kernels; only carrier typing supplies menu availability. Source-dependent partial menus need the extra robust-availability contract proved in X05, not an assertion that the original implementation already handles them.
- A finite-horizon negative never proves general almost-sure nontermination. The erasure counterexample has a separate indistinguishability proof.
- A stochastic T in a mathematical commuting square is not an observer's power to sample from an unobserved current state. X05's runtime compiler uses only observed-report G; T is used solely to establish equality of laws.
- The new one-way theorem proves value domination. Equality needs reverse simulation or the stronger matching-history hypotheses of the deterministic quotient case.

## New bridge and falsifiable contract

`X05.md` gives a finite paper proof with explicit original-index preservation, joint report/current squares, availability lifting, and action-cost comparison. Its finite stochastic-T control verifies 26 positive history nodes to depth four and rejects three independent missing-hypothesis mutations. The theorem is **PROVED LOCAL**, and the bounded implementation controls are **TESTED MODEL**. No Lean kernel verification or novelty priority is claimed.

Validation: `python scripts/swarm_x05_probe.py` exited 0 and generated the committed receipt. `python -m unittest discover -s tests -p 'test_swarm_x05.py' -v` passed all four independent audit/control groups (1.728 seconds). The 33 original C-cohort tests also passed. Full repository validation belongs to the integrating parent after all cohorts and synthesis assignments are present.

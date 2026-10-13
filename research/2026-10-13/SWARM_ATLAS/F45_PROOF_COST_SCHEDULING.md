# F45 — Proof cost, moving debt, and scheduling

## 1. Original question

Can a causal observer's unending proof work be distinguished from a scheduler that delays finite work? Steelman: account for original-source obligations, carrier changes, and physical resources before calling a divergence intrinsic. This is a mathematical model question, not a claim about brains, physical supertasks, Gödel escape, or RH.

## 2. Existing mathematical context

Nonnegative series are defined by suprema of finite subsums; fairness supplies coverage, not a deadline. [Lamport, *The Temporal Logic of Actions*, §5.3](https://lamport.org/pubs/lamport-actions.pdf) distinguishes weak and strong fairness through enabling conditions. Our stronger, explicit completion fairness assumes every required event remains executable after its prerequisites. [Specker (1949), Satz I](https://doc.rero.ch/record/304204/files/S0022481200105663.pdf) supplies the computability warning: bounded computable monotone rational sequences need not have computable convergence rates. These are classical antecedents, not novelty claims.

At source parent `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`, the existing [debt dossier](../../2026-10-11/PROOF_BACKACTION_DEBT_ZENO.md) proves moving-support obstruction and retained-history preservation; [CT2–CT3](../../2026-10-12/CARRIER_RELATIVE_META_SUCC_AND_DOVETAIL.md) prove finitary fair discovery. Their conclusions do not supply quantitative physical budgets.

## 3. Proposed SUCC objects

Let E be a countable set of mandatory events, each tagged with original source, target, and carrier epoch. A causal partial order gives every event finitely many predecessors. No reset, duplicate discharge, or deletion of originals is allowed. A legal fair execution is an injective enumeration σ of E respecting that order; every event occurs at a finite index. Existence of an executable continuation is a premise.

Each event has a finite, nonnegative additive resource vector r_e in R^d; choose positive normalization coefficients λ_k and c_e=Σ_k λ_k r_e,k. This is an explicitly chosen weighted ℓ¹ norm, not peak memory or an empirically measured physical law. Costs must be invariant across admitted reorderings. Define C_n=Σ_{i≤n}c_{σ(i)}, idle expenditure I_n=Σ_{i≤n}u_i with u_i≥0, and C*=sup_{F⊂E finite}Σ_{e∈F}c_e.

Finite increasing source horizons H_n exhaust E; retained completed obligations R_n⊆H_n increase and exhaust E under fairness. Weighted pending debt is D_n=Σ_{e∈H_n\R_n}c_e. Separate a moving target T_{H_n} from the original target T_{H_0}.

## 4. Candidate theorem

**F45.1 — PROVED LOCAL:** For every such legal fair σ, lim C_n=C*. Consequently cumulative execution expenditure is bounded iff C*<∞ and Σ_i u_i<∞. Divergent mandatory cost cannot be repaired by reordering; idle divergence can occur despite summable mandatory cost. Finite E completes at a finite index, with no schedule-uniform deadline.

**F45.2 — PROVED LOCAL:** C*<∞ implies D_n→0 for every exhaustive fair horizon/completion sequence. Conversely, if C*=∞, there exists an exhaustive fair sequence with D_n≥1 throughout. Thus summability exactly characterizes uniform debt convergence over these sequences. It does not characterize finite completion.

**F45.3 — PROVED LOCAL:** If path-dependent causal actions instead have common mandatory lower bounds ℓ_e≥0, Σ_eℓ_e=∞ implies divergent cost for every admitted fair legal path. Finite Σ_eℓ_e alone gives no upper bound.

## 5. Proof attempt

For F45.1, C_n≤C*. Every finite F occurs within some prefix by fairness, hence sup_n C_n≥Σ_F c_e. Taking the supremum proves equality, including infinity. Nonnegativity gives the stated idle criterion coordinatewise. For F45.2, choose finite F with tail weight below ε. Eventually F⊆R_n, so 0≤D_n≤Σ_{E\F}c_e<ε. Conversely enumerate E in a legal order; complete its first n events and choose a nested finite horizon containing them, the next event, and enough remaining weight to leave debt at least 1. Divergence permits every such finite extension; every fixed event is eventually completed. F45.3 follows by the same finite-subsum lower bound. These direct proofs require no finite numerical extrapolation.

Exact bookkeeping, with births b_n and newly discharged work s_n, gives D_{n+1}=D_n+b_n−s_n. Completed evidence is retained; a degraded current channel cannot erase an earlier original-source certificate.

## 6. Crucible

The exact probe preserves the following receipts; universal conclusions above come from proofs.

- **Zeno:** event n has duration 2^−n and energy 1. At n=8, time=255/256 and energy=8. An accumulating time coordinate leaves another resource divergent; no event at ω is executed.
- **Moving goal:** A_n=1+n(n+1)/2 and n reads yield unweighted debt 1+n(n−1)/2. A rival flips an unread active bit. Frozen three-bit support closes after three reads. Neither statement says a fixed theorem became unprovable.
- **Deadline:** one unit-cost task after L finite idle units is fair, yet exceeds any proposed deadline B by choosing L>B. Eternal idling is unfair. Fairness concerns eventual completion, not a uniform bound across schedules.
- **Debt/cost separation:** unit-cost H_n=R_n has debt zero and cost n. For geometric weights, H_n=[0,2n), R_n=[0,n) gives D_n=2^−n−2^−2n→0 while every finite debt is positive.
- **Signed subsidy/reset:** paired +1/−1 entries have net zero but positive expenditure n. Erasing a carrier's second bit makes originals (0,0) and (0,1) observationally identical although original parity differs. Neither operation licenses cancellation of mandatory original work.
- **Computability:** a computable stagewise halting enumeration contributes 4^−(e+1) when machine e first halts. Its sum is bounded by 1/3. A computable tail modulus would compute the sum and, successively, halting digits: the absent-digit remainder is ≤one-third of the present-digit weight. This contradicts undecidability. Summability alone supplies no effective certificate.

## 7. Verdict

**SURVIVES, PROVED LOCAL:** intrinsic divergence is relative to a declared mandatory-event and lawful-path class; schedule defects are separately testable. **REFUTED:** fair implies bounded deadline, debt zero implies finite cumulative cost, and finite Zeno time implies performed infinity. Receipt controls are **TESTED MODEL**. Independent mathematical acceptance remains pending.

## 8. Remaining obstruction

Actual source-changing instruments may change availability, cost, or target. Establish mandatory lower bounds uniformly over those paths before applying F45.3. An executable scheduler additionally needs effective enumeration and prerequisites; set-theoretic fairness supplies neither. Measure physical coefficients and authenticate original-source transport separately. Next falsifier: a lawful alternative instrument that discharges the same original obligations with summable cost.

## 9. Cross-domain connection with actual maps

Map a legal event history h to its multiset indicator χ_h∈N^(E), then χ_h↦Σ_e c_eχ_h(e). Appending an event adds its basis vector and its cost; inserting idle maps to zero mandatory progress but positive expenditure. This additive map forgets order only for cost-preserving legal paths; it cannot identify noncommuting source interventions. The complete 2×2 geometric/unit-cost × zero/unit-idle probe has zero mixed expenditure contrast. A separate product control has contrast 1. These are configuration diagnostics, not mechanism evidence; all cells share one synthetic implementation and no phase is defined. κ is model contact, φ is exact probe survival, σ is declared synthetic provenance, and ρ warrants retaining the hostile controls.

## 10. Deliverables

New files only: this dossier, `F45_PROOF_COST_PROBE.py`, and its JSON receipt. Import manifest and frozen infinite-realization dossier were inspected; 72-artifact provenance validation passed. Founding source commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a` is named by the manifest but absent from this checkout's object store (exit 128); no imported code or archive changed. Native debt/checkpoint/carrier source commits and hashes are recorded in the receipt. Full-suite and compiler work are excluded by the investigator protocol. No priority, infinite execution, physical resource theorem, or new finitary inference rule is claimed.

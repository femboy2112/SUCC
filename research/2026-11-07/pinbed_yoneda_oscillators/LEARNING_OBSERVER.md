# Operation LEARNING PIN-BED: local contact becomes retained path information

**Research note, 2026-11-07.** Additive child of SUCC draft PR #542, original parent main d32342d375f44ddf62221ad6aff2f534abdc0a03. Classical mathematics + isolated exact finite probes, not claimed priority or physical experimentation. Immutable four-pole forcing, literal zero seed, original integer carries, main, archives, proof contracts, formal/, provenance and workflows are untouched. **π base-16 normality and RH OPEN.**

## The user's insight and the precise object

> A local observation made now becomes nonlocal *relative to a future state on the path*. The pin-bed is a **learning observer**: it retains evidence while the carrier evolves, updates its internal source model, and chooses further lawful probes to distinguish surviving possibilities.

We formalize **temporal nonlocality relative to a lossy snapshot**, not physical retrocausality or spooky nonlocal effects. The observer must have an actual memory register; if full carrier state includes integer lifts/carries, it may retain the same data. Memory, probe capability, source authentication and q-truth remain independently typed.

Let S be a declared candidate source set, x_t(s) the source trajectory, and p_t an actually permitted local readout with report y_t. The observer's epistemic state is an exact compatible-history fiber

\[
B_{-1}=S,\qquad B_t=\{s\in B_{t-1}:p_t(x_t(s))=y_t\}.
\]

**LO-01 — PROVED CLASSICAL.** B_t refines monotonically. If the actual source is in S and readings are source-correct, it survives. A target q:S→{true,false} is certified on a reached observation fiber exactly when q is constant on B_t. Compatibility (there exists a true representative) is a distinct **TRUE_COMPATIBLE** result; an empty B_t is OUT_OF_MODEL, not a false target. When the observer memory includes its transcript/belief, the pair (current carrier state, memory) is a valid augmented state for subsequent policy updates. A finite adaptive policy can choose the next available probe to minimize the largest possible surviving fiber. No Bayesian prior is required.

## Source-exact history information that future circle states erase

Retain the ORIGINAL SUCC BBP source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0(s)=s,\quad U_{n+1}(s)=16U_n(s)+r(n+1).
\]

For arbitrary seeds s,s' the recurrence implies

\[
U_n(s')-U_n(s)=16^n(s'-s).
\]

**LO-02 — PROVED LOCAL, all N≥1:** take s=0 and s'=16^{-N}. For n<N the circle phases {U_n} differ; for EVERY n≥N they coincide exactly, because the unwrapped difference is the positive integer 16^(n-N). Even an observer with *all future circle Fourier modes for all future times* cannot recover which pre-N seed it saw. A stored earlier reading can. This is a strict obstruction to factoring historical truth through the terminal circle-state map; the property q(s)= [s=0] is not constant on its fibers.

**Scope firewall:** the unwrapped states differ by an integer after N, so this information was erased by the quotient R→R/Z, **not necessarily by the arithmetic carrier with integer carry access**. This illustrates the exact short sequence 0→Z→R→R/Z→0; the learning observer preserves a historical choice of lift. It does NOT establish physical nonlocality or mysterious information creation. These tail-identical histories also have the SAME asymptotic normality status; they are a counterexample to seed identification from a circle tail, NOT to a normality proof. The nonnormal completed orbit with coherent wrong seed -π/16 remains a separate required hostile control for any seed-uniform normality claim.

## The N-step source-calibrated oscillator/pin learning theorem

Fix any N≥1 and a *declared* family of 16^N possible seed histories

\[
S_N=\{s_k=k/16^N: 0\le k<16^N\}.
\]

Assume a **source-fixed** phase reference to the exact rational zero-seed trajectory x_t(0)={U_t(0)} is available. At time 0≤t<N compare the local circle phase to this reference and quantize with 16 translated pin cells:

\[
q_t(k)=\{x_t(s_k)-x_t(0)\}=\{16^t s_k\},\qquad
\boxed{y_t(k)=\lfloor16q_t(k)\rfloor.}
\]

**LO-03 — PROVED LOCAL for every N and candidate k:** if k has N hexadecimal digits d_0,...,d_(N-1), y_t(k)=d_t. Proof: write k=Σ_(j=0)^(N-1) d_j16^(N-1-j) and take the fractional part after multiplication by 16^t; multiplying by 16 and flooring selects exactly the next digit. The belief after t+1 reports has 16^(N-t-1) members. At t=N−1 it is a singleton. Yet at time N **all 16^N current circle phases have become identical** and every later projected circle reading agrees.

**LO-04 — PROVED information lower bound:** if memory must distinguish all 16^N ancestral histories despite the identical time-N circle state, it needs at least 16^N distinguishable states, or 4N bits. Any deterministic adaptive protocol using at most 16 distinct results per probe needs at least N probes in the worst case (a depth-d decision tree has ≤16^d leaves). The protocol above meets both lower bounds. This is an **exact finite candidate learning** result, not a theorem for arbitrary real seeds. Fewer bits can be sufficient for a coarser target q; learn target truth rather than blindly storing the entire carrier.

**LO-05 — PROVED source-relative noise margin:** naive binning is discontinuous at boundaries, notably the zero seed. For t<N choose a DECLARED half-grid phase offset ε_t=1/[2·16^(N−t)] and measure

\[
\widetilde y_t(k,\eta_t)=\big\lfloor16\{q_t(k)+\epsilon_t+\eta_t\}\big\rfloor.
\]

For every declared k and every total phase error |\eta_t|<ε_t, this equals d_t. Proof: q_t(k) is on the grid 16^{-(N−t)}Z/Z and every 16-bin boundary belongs to this grid; adding half a grid step places all candidates at distance at least ε_t from any bin boundary. Thus error strictly below ε_t cannot change the reading. The time-zero margin shrinks exponentially in N, so unlimited finite-source resolution/robustness is **not** claimed. The error budget must include the calibration error, not merely sensor noise. The calibrated instrument itself is a mathematical assumption, not an independently operated device.

## Source-corrected loops versus learned open paths

Previous PR #542 APH-01 gives for all seeds, n,d,h

\[
e(hU_{n+d}(s))\overline{e(16^dhU_n(s))}=e(hS_d(n)).
\]

**LO-06 — PROVED NEGATIVE:** corrected closed oscillator-loop data are seed-independent. Our learning observer uses **anchored, unclosed, individually retained phase/bin reports**, and therefore does not divide away the seed information. A temporal pin result need not descend to a function of a later projected carrier state: the LO-02 counterexample explicitly prevents that factorization. The legitimate enriched object is the **causal path + observer-memory state**; its compatible prefixes form an inverse system of transcripts. This is Yoneda-shaped, but not a proof of full faithfulness of a restricted Yoneda functor without separately supplying categorical objects, Hom-sets, naturality and density.

## Tests, epistemic verdict and what remains open

The accompanying exact rational local implementation demonstrates: the unchanged four-pole zero-source history; exact projected tail alias but nonidentical unwrapped carries; source-calibrated digit extraction; monotonic candidate partition from 16^N to 1 for N up to 3 in bounded tests; minimax allowed-mode selection; target descent; impossible report rejection; robust half-grid margin with rational perturbations; and universal seed-blind compensated loops checked on finite sample controls. It reuses the PR #542 research branch's exact four-pole routine rather than modifying source contracts. These are TESTED FINITE implementations of paper-PROVED identities, not hosted CI, Lean or independent physical measurements.

**Decisive distinction:** learning can certify a target relative to an explicitly modeled source/history class. Neither memory nor a fully faithful historical reconstruction forces the authentic selected orbit's infinite signed Weyl sums to decay. For a π-normality result, a source-selective all-epoch signed inequality is still required, and the coherent completed-β=0 seed and periodic nonnormal sources must remain hostile controls. π-normality OPEN; RH OPEN.

**Cross-references:** [APH history obstruction](ANCHORED_PATHS_VS_HOLONOMY.md), [two-tone surfaces](TWO_TONE_STABLE_ARC.md), [realization and dynamic Yoneda](REALIZATION_AND_DYNAMIC_YONEDA.md), [maintained π frontier](../../../docs/PI_NORMALITY_FRONTIER.md), [PR #541 continuous pin-bed](https://github.com/femboy2112/SUCC/pull/541), [PR #525 realization gyroscope](https://github.com/femboy2112/SUCC/pull/525), [PR #518 observational circle](https://github.com/femboy2112/SUCC/pull/518).

**Next verdict-changing experiment:** give this learner authenticated source-history/carry readouts and an explicit source-relative phase reference, then test whether such active, anchored readouts constrain a genuinely *signed* cross-time statistic beyond exact seed identity; preserve the full wrong-seed/finite-periodic holdouts. No merge, tag, release or claim promotion.

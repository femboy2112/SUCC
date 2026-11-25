# Principia — Balance, Orientation, and Source-Faithful Self-Localization

**24 November 2026 · Stacked within research-only draft SUCC PR #690.** The initiating hypothesis is the author's claim that a completed observer should be able to recover its *position* after becoming arbitrarily lost, provided its retained observations, causal coupling and internal model give it a sufficient lawful sense of direction. Here **balance** means model-relative *recoverability*, not an unexplained measure of physical equilibrium or confidence. All results below are classical theorems on declared mathematical source systems; they do not certify an empirical sensor, actual quantum gravity, RH, or normality of π.

## 1. State, source, memory, and two meanings of position

Fix a finite deterministic carrier with initial-source worlds \(W\), states \(Q\), legal actions \(A\), total transitions \(T_a:Q\to Q\), local report \(O:Q\to Y\), and an initial-state map \(\iota:W\to Q\). An observer's actual source-retained memory is \(\mathcal M_h=(h,\Gamma_h)\), where \(\Gamma_h\subseteq W\times Q\) consists of original worlds and current states consistent with its observed path (Principia T15). A declared position/pose map \(P:Q\to Z\) may identify positions up to a target-relevant gauge.

Two targets are genuinely different:

* **Current orientation:** \(P(q)\) for \((w,q)\in\Gamma_h\). A reset/navigation maneuver may bring distinct original states to one known current location.
* **Original-source position:** \(P(\iota(w))\). This target requires retaining origin coupling and may remain unknown after all current positions synchronize.

The target itself is fixed by the task and does not silently switch between these modes. Knowledge of the original source model is a mathematical hypothesis, **not** independent proof that it describes an external physical environment.

## T26 — finite reorientation is a least winning attractor (CLASSICAL / PROVED)

Let \(B\subseteq W\times Q\) be a nonempty source-coupled belief, reachable under lawful action/report memory updates. For action \(a\in A\) and possible observed \(y\in Y\) define the nonempty successor
\[
B_{a,y}=\{(w,T_a(q)):(w,q)\in B,\ O(T_a(q))=y\}.
\]
Let \(\mathsf{Goal}\) comprise the beliefs on which the **chosen** position target is constant. On the finite directed graph \(\mathcal B\) of all beliefs reachable from the initial \(B_0\), define the attractor
\[
\mathcal W_0=\mathsf{Goal},\quad
\mathcal W_{k+1}=\mathcal W_k\cup\{B:\exists a\in A\;\forall y\text{ possible},\ B_{a,y}\in\mathcal W_k\}.
\]
Then **a finite observation-adaptive one-copy strategy guaranteed to reorient from \(B_0\) exists if and only if \(B_0\in\mathcal W_\infty\)**. When it exists, its minimal worst-case number of interventions is
\[
D(B)=0\;\text{if }B\in\mathsf{Goal},\qquad
\boxed{D(B)=1+\min_{a\in A}\max_{y:B_{a,y}\ne\varnothing}D(B_{a,y})}
\]
for non-goal winning beliefs; set \(D(B)=\infty\) on losing beliefs. Each action selected by the optimal strategy makes \(D\) strictly decrease **for every possible resulting observation**, even if the number of surviving source worlds does not decrease.

**Proof.** The set update and the AND/OR recurrence are exactly the first-action decomposition of a correct finite strategy, by induction on the maximum remaining depth. The monotone attractor is formed in a finite graph; if it stabilizes without including \(B_0\), no bounded winning policy exists. Conversely, membership at stage \(k\) constructs a policy whose every successor lies at an earlier stage, so it terminates in at most \(k\) steps. Since any terminating strategy on a finite adversarial-output game can be chosen acyclic on beliefs, no unbounded successful branch is needed. The algorithm checks every possible report and independently verifies the produced policy path. If \(|\mathcal B|=R\), a winning rank is at most \(R-1\) (unless every reachable belief is already a goal). This is the classical finite reachability-game/active diagnosis theorem, reconstructed through Principia's original-world/current-state coupling.

**Important:** The rank is *toolkit-, source- and target-relative*; it is **not** a scalar truth score, a posterior probability, a physical distance, or even belief-set cardinality. A silent source preparation can keep every original candidate yet decrease \(D\) from two to one.

## T27 — a completed finite observer can reorient after arbitrary prior drift (CONDITIONAL CLASSICAL)

Suppose the full source map and local report law remain valid, the initial-source family contains **every position from which the observer may be re-rooted after unremembered drift** (equivalently, the initial map covers the relevant reachable state set), and every initially possible report class \(B_y=\{(w,\iota(w)):O(\iota(w))=y\}\) lies in the winning attractor for the **current-position target**. Then, after being placed at any state in that explicitly covered re-rooting class, the observer can use its first local report to select a certified finite reorientation policy. The maximum of the finite class ranks is a **uniform finite recovery horizon** for that fixed finite model.

The source-memory update remains exact along the policy; unexpected reports with empty source-compatible fiber signal **model/source inadequacy or an out-of-contract observation** rather than permission to invent a new state. The same conclusion is not licensed across changed maps, unknown action slippage, missing reference points or insufficient sensory precision.

**Finite landmark positive control.** On a known directed ring \(Q=\mathbb Z/n\mathbb Z\), \(T_{\rightarrow}(x)=x+1\), with a unique beacon report at \(x=0\) and “dark” elsewhere, every starting position can be recovered: a beacon observation immediately fixes zero, and repeated trusted forward actions shrink the possible starting positions. In the exact source model, the worst rank after an initially dark report is \(n-2\) for \(n\ge4\). The remembered number and outcomes of steps also reconstruct the original position, not just the terminal beacon location.

**Memory is not optional.** A separate “load” action that returns zero and retains the same two original candidates may change their causal preparation. Its future readout then distinguishes the sources. The rank decreases from 2 to 1 with **no decrease in the number of candidates**. This directly tests the author's proposal that *causal coupling and retained observation history*, not endpoint agreement, determine reorientation capacity.

## T28 — gauge symmetry can make absolute position unobservable (CLASSICAL / PROVED)

Let \(\gamma:Q\to Q\) be a bijection preserving observations and every legal action:
\[
O\gamma=O,\qquad \gamma T_a=T_a\gamma\quad(a\in A).
\]
For all action words \(u\), \(O(T_u\gamma q)=O(T_uq)\). Thus a pair \(q,\gamma q\) has **identical possible observation histories under every lawful common action sequence**. If the task's *original* position labels differ, original localization is impossible for that admissible pair. For the **current** position target, if \(P(T_uq)\ne P(T_u\gamma q)\) for every word \(u\), no reorientation strategy can certify both. An injective pose target and a symmetry without fixed states suffice. These conditions are mathematically checked, not inferred from a failed finite search.

**Two controls:** on a completely homogeneous directed ring, a nontrivial rotation commutes with all steps and preserves “dark,” so absolute position cannot be recovered despite an exact directional motion model. On a ring with unknown heading \(h=\pm1\), the reflection \((x,h)\mapsto(-x,-h)\) preserves beacon-only observations and turn/forward actions; the **full pose** remains ambiguous even though the current **position** can become known by reaching the beacon. Adding an asymmetric east-side landmark breaks the reflection symmetry; the finite policy search then reorients full pose. This is the distinction between reconstructing position and establishing an oriented *frame of reference*.

A gauge-invariant target, such as distance to the beacon, can be recoverable even when absolute heading is not. No arbitrarily selected external orientation is needed or justified for that target.

## T29 — arbitrarily lost but pointwise recoverable: the integer line (PROVED)

Fix an unbounded but mathematically known carrier \(Q=\mathbb Z\), lawful exact relative actions \(+1\) and \(-1\), and a unique local landmark observation at world coordinate 0. The observer begins at unknown integer \(x\), retaining its **relative displacement** (the action-history sum), not its absolute position. It follows a fixed outward sweep: at stage \(k\ge1\), starting at relative displacement \(-(k-1)\), move right \(2k-1\) steps to \(+k\), then left \(2k\) steps to \(-k\).

By induction, stage \(k\) visits every relative offset in \([-k,k]\) and ends at \(-k\). After stage \(R\), exactly \(2R^2+R\) actions have been taken. If the unknown start satisfies \(|x|\le R\), the observer must have visited offset \(-x\); when the landmark is seen, it reconstructs \(x=-\text{recorded offset}\) and knows its present position is 0. Hence **every finite displacement is eventually recoverable**.

There is **no uniform finite number of actions** that guarantees success over all \(x\in\mathbb Z\): any fixed finite policy branch visits only finitely many source positions, and infinitely many translated starting points produce the same all-dark transcript. This is a genuine separation of *pointwise finite reorientation* from *uniformly bounded reorientation*. It is not an assertion that an infinite experiment finishes, that motion never fails in reality, or that an arbitrary infinite source possesses a globally detectable landmark.

## T30 — bounded-error balance is observational code separation (CLASSICAL / PROVED)

Fix a **preset** lawful action word \(u\) of length \(L\), and let each admissible original source \(w\) generate its expected local observation codeword
\[
C_u(w)=\bigl(O(\iota(w)), O(T_{a_1}\iota(w)),\ldots,O(T_u\iota(w))\bigr)\in Y^{L+1}.
\]
For the declared target \(G_u(w)\) (initial or final position), set
\[
\delta_u=\min_{G_u(w)\ne G_u(w')}d_H\bigl(C_u(w),C_u(w')\bigr).
\]
With at most \(e\) **adversarial report substitutions across the entire word**, exact target recovery for every source and every allowed corruption is possible **if and only if** \(\delta_u>2e\). If the target is constant on all sources, it is already known without a separation requirement.

**Proof:** if the target-separated Hamming balls of radius \(e\) are disjoint, all source-consistent decodings share a unique target. Conversely, if two different-target codewords differ in at most \(2e\) slots, form a hybrid report agreeing with each in all but at most \(e\) of those positions. The same corrupted observation history is then consistent with both targets; no worst-case decoder can settle them.

**Exact example:** in the directed ring with one beacon and trusted forward motion, \(\ell\) complete laps produce target-separated Hamming distance exactly \(2\ell\) (for \(n\ge4\)). Thus \(e+1\) complete laps guarantee recovery after any \(e\) corrupted local reports. Two laps correct **one** arbitrary substitution, including the initial reading. One lap cannot: its radius-one codeballs overlap. With the reflection gauge preserving all observations, full-pose code distance remains zero at any number of repeated laps; redundancy cannot repair missing mathematical discrimination. A second asymmetric landmark repairs the symmetry and can yield positive noise margins.

**Scope:** the error budget assumes correctly modelled state transitions, a correct map, a fixed action word, and an upper bound on *total* report corruptions. It is not a theorem about arbitrary motion failures, unknown measurement biases, indefinite sensor corruption, or an optimal adaptive noisy strategy. The local-code margin is a mathematical source-relative separation quantity—not a probability of truth.

## T31 — quantitative reorientation for the SAME CM theta matrix (CLASSICAL / EXACT)

The discrete Hamming margin controls finite symbolic report errors. A genuinely continuous/signed arithmetic observer needs a **separate quantitative inverse bound** on its actual observation map. Our existing Gaussian CM construction supplies an exact test.

Let \(M=(H_{4r}(p^2 2^j))_{0\le r,j<k}\in\mathbb Z^{k\times k}\) be the genuine nonzero CM theta shell matrix from CM_THETA_TWO_PLACE.md T10, at inert prime \(p\equiv3\bmod4\). The real Gaussian realization at rational \(q\in(0,1)\) is
\[
W=M\operatorname{diag}\bigl(q^{p^22^0},\ldots,q^{p^22^{k-1}}\bigr).
\]
The code constructs the rational inverse of **this exact, authenticated matrix** in both the bare and Gaussian coordinate systems. It independently verifies the source CM theta coefficients, the matrix equality, and the inverse identity \(WW^{-1}=I\). For any \(x\in\mathbb Q^k\), if the measured real-side data are \(y=Wx+\eta\) and \(\|\eta\|_\infty\le\varepsilon\), then the reconstructed coordinate \(\hat x=W^{-1}y\) satisfies
\[
\boxed{
\|\hat x-x\|_\infty
\le \|W^{-1}\|_\infty\varepsilon,\quad
\|W^{-1}\|_\infty=\max_i\sum_j |(W^{-1})_{ij}|.
}
\]
**Proof:** the exact inverse gives \(\hat x-x=W^{-1}\eta\). Rowwise triangle inequalities yield the bound. It is sharp: select a row attaining the maximum absolute row sum, and choose each \(\eta_j=\varepsilon\,\operatorname{sgn}((W^{-1})_{ij})\). This gives equality in that output coordinate.

**Crucible:** even though the same CM source proves \(M\) has full rank and growing \(p\)-adic determinant divisibility, the Gaussian weights \(q^{p^22^j}\) can make \(\|W^{-1}\|_\infty\) very large. This is not a contradiction: exact arithmetic identifiability is not robust real-side reorientation. Dividing out an unnoticed Gaussian or period normalization would falsely inflate the numerical stability claim.

The independent SymPy checker reconstitutes the actual source matrix, its weighted real realization, inverse and exact norm (including an adversarial noise vector attaining the bound) in **24 separate** \(p,k,q\) cases, with positive checks and deliberately singular/forged-inverse/changed-source controls.

**Scope:** this is a classical finite normed-linear theorem on an actual source-derived CM theta shell matrix. It is **not** the actual automorphic CM theta-period/Petersson map used for RH, not a bound on physical sensor error, and not a theorem about infinite-dimensional inverse stability. Its value to Principia is an exact source-typed distinction between *being able to reorient* and *being able to reorient robustly under finite precision*.

## 2. A unified meaning of balance — and its nonidentities

There are at least four separate diagnostics:

| Diagnostic | Precise role | What it does NOT imply |
| --- | --- | --- |
| **Contact / source adequacy** | Are the actual observation and action laws those of the declared model? | A mathematical theorem cannot independently authenticate physical contact |
| **Current knowledge** | Does the live causal belief already determine the target position? | Its uniqueness does not reconstruct forgotten historical origins |
| **Reorientation rank \(D(B)\)** | Is there a lawful finite policy with guaranteed progress on every possible report? | It is not geometric distance, certainty score, or robustness to wrong source laws |
| **Code margin \(\delta_u-2e\)** | Is a preset observation path tolerant of \(e\) arbitrary reported-symbol errors? | No conclusion about motion slips or another probe toolkit |

“Balance” as a foundation is **model-relative recoverability and internal/external constraint consistency**. We can have large current uncertainty and still have finite \(D(B)\). Conversely, a precise internal map may not localize a pose under exact source symmetries.

### How this bears on the RH semantic reconstruction

Principia's source model should retain enough local arithmetic/analytic information to identify the **target-relevant mathematical state**, potentially only up to an admissible gauge. For an actual CM theta-period construction, merely transporting a scalar theta value or a nonzero rank is insufficient: we must reconstruct an integral coordinate, its signed Frobenius unit, the period/conductor normalization and the real and \(p\)-adic data of the *same source map*. A valid reorientation analogy asks whether target-bearing local mathematical probes distinguish the competing valid source representations; its quantitative analogue asks for a uniform inverse/height bound. **Nothing here reconstructs an automorphic theta lift or proves RH.**

## Exact code and controls

- `observational_succ/principia_reorientation.py`: independent causal-memory replay, finite AND/OR attractor, minimizing worst-case reorientation rank, complete policy certificate checker, landmark/reflection/homogeneous ring controls, source-gauge automorphism obstruction, and explicit infinite-line zigzag.
- `observational_succ/principia_reorientation_code.py`: source-labelled observation codewords, exact target-separated Hamming distances and bounded-error decoding with source verification.
- `tests/test_principia_reorientation.py`, `tests/test_principia_reorientation_code.py`: positive and negative controls covering resets, original/current targets, heading ambiguity, repaired landmark, source mismatch, decreasing rank without hypothesis elimination, 1-error correction and geometric nonuniformity.
- `research/2026-11-24/principia_math_of_math/independent_reorientation_oracle.py`: brute-depth AND/OR oracle on fresh finite sources, independent per-world policy replay and separately calculated beacon codewords/distances.

**Claims:** T26–T31 DISCLOSED as elementary/classical mathematical deductions within the specified source and toolkit. Their finite executable checks are OBSERVED, not universal proofs. Extensions to unknown source laws, unbounded state/continuous spaces without landmarks, noisy motion, automorphic period geometry or global RH estimates remain **UNVERIFIED**. The next verdict-changing probe is to construct a quantitative inverse/reorientation theorem for the actual integral CM theta-period map, with gauge, source, and completion precisely typed.

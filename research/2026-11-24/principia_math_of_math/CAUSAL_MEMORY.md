# Principia Observatoris — Causal memory: observations AND coupling

**Research round:** 2026-11-24. Same draft line as SUCC Principia Genesis PR #690. **Claim:** the minimal source-relative memory needed for specified mathematical questions cannot, in general, be just an observation transcript. The author's proposal is to retain **memory of observations together with causal coupling**.

**Scope:** finite deterministic, total mathematical intervention systems; classical theorems, not claims about physical sensors, probabilities, an original RH proof or scholarly priority. This file develops new-to-SUCC interfaces to earlier Principia source/knowledge-volume theorems and Null-Memory PR #665.

## Source and object

Fix a nonempty finite original-source class \(W\), present-state carrier \(Q\), action alphabet \(A\), total lawful transitions \(T_a:Q\to Q\), readout \(O:Q\to Y\), initial state map \(\iota:W\to Q\), and **original-source** target \(g:W\to Z\). The source passport contains all definitions and costs. No probability distribution is assumed.

The observer retains an actual ordered transcript
\[
h=(y_0;(a_1,y_1),\ldots,(a_t,y_t)).
\]
Define the accompanying original-to-present **causal coupling**
\[
\boxed{\Gamma_h=\{(w,T_{a_t}\cdots T_{a_1}\iota(w)):\text{every reported outcome in }h\text{ is reproduced}\}.}
\]
The causal-memory object is \(\mathcal M_h=(h,\Gamma_h)\), relative to the fixed source law. The original-world coordinate is essential when asking about the original target after disturbing the current state. This is *mathematical model provenance*, not a revealed hidden source world or an experimentally authenticated mechanism.

### T15 — exact sufficient causal memory (CLASSICAL / PROVED)

For a next action \(a\) with actually observed output \(y\),
\[
\boxed{
\Gamma_{h(a,y)}=\{(w,T_aq):(w,q)\in\Gamma_h,\ O(T_aq)=y\}.
}
\]
**Proof:** substitute the deterministic transition and append the observation constraint; both directions follow by the definitions. An empty right-hand side declares an incompatible actual report/source assumption; it does not license arbitrary conclusions.

For every legal future action word \(u\), the set of original-target/future-output pairs is computed from \(\Gamma_h\) by deterministic iteration. More strongly, for any words \(u_1,\ldots,u_k\), the *joint counterfactual relation* is
\[
\mathcal J_h(u_1,\ldots,u_k)
=\left\{(g(w),R_{u_1}(q),\ldots,R_{u_k}(q)):(w,q)\in\Gamma_h\right\}.
\]
All components share the same original world \(w\). Independent marginalization destroys this constraint.

**Boundary:** equality of \(\Gamma_h\) suffices for all target/future semantics under this model; it does NOT recover which earlier actions produced it. Historic-recall targets still require the retained transcript, or a separately proved sufficient historical compression. These joint potential responses are mathematical counterfactuals, not observations jointly executable on one destructive source without declared reset/copy access.

## T16 — the smallest safe future-target quotient (CLASSICAL / PROVED)

Let the **reachable marked carrier**
\[
X=\{(w,q):q\text{ is reachable from }\iota(w)\text{ by a legal action word}\}
\]
carry marked transitions \(\widehat T_a(w,q)=(w,T_aq)\), output \(O(q)\), and immutable original target \(g(w)\).

Define \(x\sim_d x'\) iff \(g(x)=g(x')\) and \(O(\widehat T_u x)=O(\widehat T_u x')\) for **every** legal word \(|u|\le d\), including the empty word. Equivalently, start at agreement on \((g,O)\) and refine
\[
\boxed{
x\sim_{d+1}x'
\ \Longleftrightarrow\
x\sim_d x'\ \text{and}\ \forall a\in A,\ 
\widehat T_a x\sim_d\widehat T_a x'.
}
\]
There are \(N=|X|\) marked states. Each strict refinement splits an existing equivalence class, increasing the number of classes by at least one. Hence stabilization occurs no later than step \(N-1\).

**Theorem:** \(\sim_\infty=\sim_{N-1}\) is the unique **coarsest congruence** on the marked carrier that preserves the original target, current output and every lawful future output. If two states have different stable classes, there is either an immediate **mathematical target distinction** or a legal word of length at most \(N-1\) that produces different reports.

**Proof:** induction on the word horizon establishes the refinement equation. Stable equivalence is invariant under all \(\widehat T_a\), hence every word. Any action-congruent relation preserving \((g,O)\) lies inside \(\sim_0\); induction places it inside every \(\sim_d\), hence inside \(\sim_\infty\). The finiteness argument gives the horizon bound.

**Non-claims:** a hidden target difference is not an automatically executable distinguishing experiment. The theorem minimizes marked-state behavior for this fixed target/toolkit; it is NOT universal compression of an arbitrary history, continuous theta source, or all mathematics. The underlying result is classical deterministic automata/observability mathematics; the source/coupling/target interface is the contribution of this Principia research program.

## T17 — why an immediate zero is not a strong null

An ideal zero-cost action \(a\) is **future-target neutral at \(\Gamma_h\)** if for every \((w,q)\in\Gamma_h\)
\[
O(T_aq)=O(q),\qquad (w,q)\sim_\infty(w,T_aq).
\]
By T16 it preserves all target-relevant future response functions for the same original source. This condition is sufficient for behavioral future neutrality, and within the declared complete toolkit a violation of behavior equivalence has a finite future-target or observational discriminator.

This is *not* the full strong-null instrument contract from SUCC PR #665. The action record itself changed, and timing, availability, probe-choice policy or physical resource cost may change. The source's zero-cost annotation and preservation of all future responses do not certify an unchanged real-world experiment policy.

**Positive/negative control:** two sources \(w_0,w_1\) initially both report zero. A null-output **load** action eliminates neither source but moves the two into different prepared hidden states; a subsequent **read** distinguishes them. A true **noop** leaves both current/future responses invariant. Thus “no immediate update to the hypothesis set” is weaker than “causally neutral”.

## T18 — the coupling of possible experiments is not their individual marginals

Four hidden originals are \(C_0,C_1,A_0,A_1\): original bit \(x\in\{0,1\}\) and coupling type \(c=0\) (C) or \(1\) (A). Initial reports are zero. Two destructive probes produce
\[
R_a(x,c)=x,\qquad R_b(x,c)=x\oplus c.
\]
For either fixed coupling type, each individual probe has the same possible outcomes \(\{0,1\}\). But their *same-source joint tables* differ:
\[
\boxed{\mathcal J_C=\{(0,0),(1,1)\},\quad
\mathcal J_A=\{(0,1),(1,0)\}.}
\]

The terminal state is absorbing if no reset is licensed. In that toolkit there is **no finite single-copy policy** that can identify coupling type with certainty: an initial choice reveals one bit or its complemented version, and every later probe only repeats that terminal result. The all-counterfactual joint table is not jointly measurable in that toolkit.

When a source-preserving **reset** action is legal, the actual three-step experiment \(a\), reset, \(b\) does identify the coupling type from its retained first and last readouts. A depth-two policy is insufficient; a depth-three policy exists. This is a precise **toolkit access gap**, not a lack of mathematical counterfactual definition.

## T19 — actual intervention policy theorem (CLASSICAL / PROVED)

Write \(D_d(\Gamma)\) for existence of a terminating, adaptive, one-copy action policy of depth at most \(d\) that correctly identifies the original target in **every** world allowed by nonempty \(\Gamma\). Let \(\Gamma_{a,y}\) denote the successor coupling at action \(a\) and actually possible outcome \(y\).

Then
\[
D_0(\Gamma)\iff|\{g(w):(w,q)\in\Gamma\}|=1,
\]
\[
\boxed{
D_{d+1}(\Gamma)
\iff
D_0(\Gamma)\ \lor\
\exists a\in A\ \forall y\text{ possible after }a,\ D_d(\Gamma_{a,y}).
}
\]

**Proof:** induction on policy-tree depth. If not already identified, a legal first action partitions the original sources by the resulting observed outcome; every nonempty branch must have a correct remaining policy. Conversely, recursively join the branch policies under that first action. A source-checked verifier must check **all possible outcomes**, not just one favorable branch.

This differs from merely asking whether all counterfactual words separate mathematical source worlds. One-copy disturbance, available reset, and finite cost/budget may obstruct execution even if full mathematical behavior is distinguishable.

## T20 — actual Gaussian theta: two kinds of zero (SOURCE-EXACT)

Use the **existing genuine Gaussian theta source** in this PR. Its holomorphic derivative shell is
\[
H_r(n)=\sum_{a^2+b^2=n}(a+bi)^r.
\]
The shell \(n=2\) contains four points, whose quadratic contributions cancel. The shell \(n=3\) contains **no** Gaussian integer point. Both report zero:
\[
H_2(2)=H_2(3)=0.
\]
The lawful next probe changes the holomorphic jet order to four. Then
\[
\boxed{H_4(2)=-16,\qquad H_4(3)=0.}
\]
All four numbers are computed by enumerating \(\mathbb Z[i]\), not inserted as fitted answers. The current reports coincide, but the remembered original-source coupling determines that the next permissible probe will distinguish **cancellation** from **absence**. A repeated order-two readout will not.

**Boundary:** changing the derivative order is a mathematical probe, not a physical operation on the Gaussian lattice. This is a source-exact finite illustration of causal-memory semantics, **not** construction of the RH automorphic theta-lift period map, nor proof of the missing M4–M10 estimates.

## Implementation and independent proof controls

Native mathematical model: observational_succ/principia_causal_memory.py.

Focused hostile tests: tests/test_principia_causal_memory.py (16 new test methods, including parametrized source/memory/policy/CM comparisons). These sit alongside the 51 previous focused Principia tests.

Independent finite semantics oracle: independent_causal_memory_oracle.py under this research folder. It generates 84 fresh, small deterministic source carriers and independently enumerates **all** action words through \(N-1\); it compares the induced actual future-output signatures with the source quotient. It also independently replays actual memory updates, and checks generated policy trees. This oracle differs algorithmically from Moore partition refinement and the separate pairwise fixed-point validator. It is still the same mathematical/source provenance, not an independent human referee.

**Scoped verdict:** T15–T19 are DISCLOSED classical deductions within the finite model; T20 is a SOURCE-EXACT Gaussian arithmetic example; full CM automorphic theta-lift transport, integral period normalization, rank, Galois/conductor and the global arithmetic inequality are UNVERIFIED in native Principia.

**Next falsifier:** apply this calculus to an *actual* finite slice of the automorphic CM theta-lift period module. If two source-admissible theta histories become equal under a proposed causal-memory quotient while their relevant integral-minor valuation or real Petersson/period norm differs, the proposed quotient is **too coarse for the RH mathematical target**, even if all its scalar observation reports coincide. Repair source maps and allowed observations before promoting any reconstruction theorem.

**Related archives:** Principia Books III/IV; SUCC null memory #665; coherent zeros #290; Seinfeld source-labelled cycles; Witt carries #240; CM_THETA_TWO_PLACE.md T9–T14. The published external RH proof is a case-study and independent theorem authority, not an axiom of this construction.

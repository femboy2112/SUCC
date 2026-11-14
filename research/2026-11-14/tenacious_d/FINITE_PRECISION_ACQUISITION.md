# Finite-precision acquisition on one carrier

## TD6. A computable scalar recovery radius with destructive linear actions

Astra CG11 prices exact observations on a Hilbert ball. Second Forge FO-10 asks which joint information a single carrier can deliver. Both questions enter here. A schedule determines which original coordinates can still be sensed after previous actions. The instrument gives only a labelled interval, and the policy must pay the cost of the actions on its actual branch.

Let \(K=-K\subset\mathbb R^n\) be a nonempty compact convex set of initial states, and \(f\) a real linear functional on them. Every action \(a\) is total, has a positive state-independent cost, applies a known homogeneous linear map \(A_a\), then senses a scalar linear functional \(s_a\) of the updated state. The action alphabet is finite and the budget \(D\) bounds the cost of every execution. A history can influence action choice and termination. At a fixed history the actions already chosen determine the state transform.

**Sensor contract.** Each action supplies cells of physical radius \(\epsilon_a\ge0\) with declared centers. Any allowed output center lies within \(\epsilon_a\) of the true scalar. The zero label is *available throughout the closed central cell* \([-\epsilon_a,\epsilon_a]\). Every reachable scalar has some available output. Errors may be selected separately at successive contacts, including all successive zero labels whenever available. For the finitely many bounded ranges reachable within budget and \(\epsilon_a>0\), a centered grid of spacing \(2\epsilon_a\), with either label allowed at a tie, implements this with finitely many labels. Arbitrary tie-breaking that excludes the zero label at an endpoint may change attainment. Zero width can model an exact real oracle. The theorem's finite-bit interpretation requires a specified finite alphabet (and bit costs if priced). Charge the complete per-action resource cost in advance.

For word \(w=a_1\cdots a_j\), set \(h_i=s_{a_i} A_{a_i}\cdots A_{a_1}\) and
\[
 K_w=K\cap\bigcap_{i\le j}\{z:|h_i z|\le\epsilon_{a_i}\},
 \qquad r(w)=\max_{z\in K_w}|fz|.
\]
The empty word is feasible. With arbitrary deterministic decoders and independent worst-case allowed readouts, the optimal worst-case absolute error for recovering the **initial** scalar is
\[
 R_D=\min_{\operatorname{cost}(w)\le D}r(w).
\]
Every adaptive policy is dominated by the fixed word it takes on zero with all zero reports. An error tolerance \(\tau\ge0\) is achievable exactly when some such word has \(r(w)\le\tau\).

**Proof.** Consider first a fixed word and any achievable transcript. Let \(V\) be the set of initial states admitting it. For \(x,x'\in V\), the point \((x-x')/2\) lies in \(K\) by symmetry and convexity. At contact \(i\) the two values are in one interval of diameter \(2\epsilon_{a_i}\). Their half-difference therefore belongs to the corresponding central slab. It follows that the range of \(f\) on \(V\) has diameter at most \(2r(w)\). The midpoint of its infimum and supremum gives worst error at most \(r(w)\). For closed grid intervals and a rational polytope prior the extrema are linear programs. For a more general calibrated sensor the larger interval-consistent polytope also gives a valid decoder.

Now run any admissible policy on zero, with the zero labels. Every \(z,-z\in K_{w_0}\) can reproduce the entire record of this run. Induction on its action choices proves this including termination. They get the same reported prediction, so the worst error is at least \(|fz|\) for every such \(z\). This lower bound is \(r(w_0)\). Applied to a fixed word it proves the preceding upper bound is sharp. Minimizing gives the identity. Positive costs and the finite alphabet give finitely many feasible words. ∎

**Primal and dual certificates for a box.** For \(K=\prod_j[-b_j,b_j]\), stack the \(h_i\) into \(H_w\). Linear-programming duality, or splitting the multipliers of each pair of opposite inequalities into positive and negative parts, gives
\[
 r(w)=\min_{\lambda\in\mathbb R^{|w|}}
 \left(\sum_j b_j|f_j-(H_w^T\lambda)_j|
       +\sum_i\epsilon_{a_i}|\lambda_i|\right)
\]
where \(f\) is displayed as a coefficient column inside this formula. Indeed maximize \(fz\) over \(|z_j|\le b_j,\ |H_w z|_i\le\epsilon_i\). The redundant sign of the objective follows from symmetry. A feasible primal \(z\) and feasible dual coefficients of the same value certify the optimum. The resulting estimator can also use the linear combination of reported centers with coefficients \(\lambda\). Rational data give rational certificates. A table of primal witnesses for *all* feasible words refutes a proposed smaller tolerance for every deterministic policy.

**Controls.** With \((x,y)\in[-1,1]^2\), target \(x+y\), and two unit-cost actions, let one read \(x\) without changing the state and the other replace the state by \((y,0)\) and read its first coordinate. Use centered cells with half-width \(1/4\). In that order both coordinates are measured with total worst error \(1/2\), attained on the central record. In reverse order \(x\) is lost, and both readouts sense \(y\). The companion test independently solves a finite-alphabet adaptive game on a grid containing the extremal pair. A symmetric nonconvex prior can break fixed-word optimality, as CG11's seven-state example shows at zero width. A shifted threshold also invalidates a zero-cell surrogate: with \(K=[-1,1]\), a sign-only readout splitting at zero leaves two half-intervals of diameter one and has worst error \(1/2\). Its centered zero-history cell is absent. For vector targets the scalar radius-equals-half-diameter step needs an additional geometric theorem.

**Status and lineage.** Proved here for scalar targets, centered sensors and the specified source class. The proof uses classical symmetric optimal recovery and the original CG11 zero-execution argument. The choices of single-carrier action order, finite labels, cost and boundary calibration are the new SUCC specialization. Classical sources include Ettehad and Foucart's treatment of inaccurate information and the scalar nonadaptive antecedent recalled by Novak. [Inaccurate information](https://foucart.github.io/publi/OR_Uncertainty_v2.pdf) · [Classical scalar theorem](https://users.fmi.uni-jena.de/~novak/novak2.pdf) · [Exact implementation](../../../observational_succ/tenacious_acquisition.py) · [Independent finite game and controls](../../../tests/test_tenacious_acquisition.py)

## TD7. Bounded-error randomized finite certification

Second Forge FH-5 precludes a sound finite stopping certificate on the class of all rational-valued one-sided sequences having some monic rational recurrence of unknown finite order. Allow private randomness and sequential exact readout. At a finite stopping time a certifier issues one fully specified scalar sequence, up to equality of its infinite outputs. Suppose on **every** source the probability of ever stopping with an incorrect certificate is at most \(\alpha\). Then on **each** source its probability of ever issuing any certificate is at most \(\alpha\).

**Proof.** Fix a source and a finite prefix length \(m\). Let \(p\) be the probability of stopping by that time. Infinitely many distinct recurrent sequences extend that prefix. For example, put one spike at any later index and then append zeros to the fixed prefix. Each resulting sequence has a shift power as an annihilator. The distribution of certificates issued by time \(m\) is the same on every extension, by coupling the private seed. For every \(\delta>0\) select an extension with early probability of its own certificate at most \(\delta\), since disjoint certificate classes share finite mass. On that extension the early error is at least \(p-\delta\). Thus \(p\le\alpha\). Continuity of probability from below in \(m\) proves the claim. The bound is sharp for allowed abstention: with probability \(\alpha\) output a fixed sequence immediately and otherwise abstain forever. ∎

This answers the handoff's bounded-error question for uniform error probability and full-sequence identification. For a single Boolean target the existence of infinitely many distinct full-sequence answers on each prefix is a stronger premise. Under a declared order bound, deterministic certification becomes available again at the two-forge finite horizon. On a physical source, adequacy of that bound remains an independent premise.

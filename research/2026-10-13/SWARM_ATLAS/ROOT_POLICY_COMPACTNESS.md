# Compact causal policies: actualization also bounds total termination

Parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
Claim `SWM-ROOT-01`: CLASSICAL / PROVED LOCAL, topology proof below; the compact open-cover stopping core is LEAN-KERNEL PROVED in `formal/swarm_topology/SwarmPolicyCompactness.lean`; full policy semantics not kernel formalized.

## Objects and exact theorem

Let S be a compact topological space of ORIGINAL source states. For each
authorized action a, let T_a:S→S be a total continuous current-carrier
transition, and r_a:S→O_a a continuous outcome map into a finite discrete
alphabet. The outcome is taken before T_a; an outcome after T_a can be
represented by composing its readout with T_a. A deterministic policy
chooses an action or a terminal answer from only the actual finite event
history. It has no access to hidden original/current state, no reset unless
one is explicitly an action, and no unperformed counterfactual evidence.

**Theorem.** If this FIXED policy terminates after finitely many actions for
every s∈S, there exists N∈N bounding the stopping depth for every s∈S.
If it returns a correct Boolean predicate, that predicate's truth set is
clopen in S. This does not assert the existence of a correct policy.

## Proof and the smallest sufficient hypothesis

For a history h=((a_1,o_1),...,(a_n,o_n)) compatible with the policy,
define its original-source cylinder

    C_h = {s : r_(a_i)(T_(a_(i-1)) ... T_(a_1)(s))=o_i for 1≤i≤n}.

Each equality preimage is clopen: finite-discrete singletons are clopen and
each composite is continuous. Their finite intersection C_h is clopen.
The actions at that history are already fixed, so adaptive branching does
not affect this argument. Total pointwise termination says that the
cylinders of terminal histories cover S. Compactness provides a finite
subcover C_(h_1),...,C_(h_m). Every source follows the unique history chosen
by the policy; membership in C_(h_i) therefore means it stops at that exact
leaf. For nonempty S take N=max_i |h_i|; for empty S take N=0. This is the
uniform bound. The same finite subcover splits into yes and no leaves;
their respective finite unions are clopen, proving the second statement.

The weakest proof input is a finite subcover of THESE terminal cylinders;
source compactness and readout/action continuity are one sufficient route.
In fact open (not necessarily closed) terminal cylinders suffice for the
uniform-bound conclusion, and the union of yes/no terminal cylinders makes
both truth sets open. Finite branching also makes the tree below the
bound finite. Fixed finite costs assigned to nodes then have a uniform
finite total bound; arbitrary unbounded source-dependent physical costs
have not been controlled.

This is an application of classical open-cover compactness, related to
König's finitely branching tree lemma. The report-profile realization
theorem in VOYAGER does not by itself certify that all its probe words can
be acquired on a single changing carrier. This result adds the operational
policy hypothesis explicitly. Mathematical novelty priority is UNVERIFIED.

## Three falsifiers and repaired statements

**Remove compactness.** On the shift-closed eventual-zero binary streams,
read the head, shift, and stop at the first zero. Every source terminates,
but 1^n 0^infinity takes n+1 readings. The source class is nonclosed in the
compact stream completion. The missing all-one limit source never stops.
No finite experiment is being used to prove this unboundedness: for any
bound B, the explicitly defined source 1^B 0^infinity violates it.

**Remove continuity.** K={0}∪{1/n:n≥1} is compact in R. Identity actions
read equality to 0, then 1, then 1/2, etc. The source 0 stops at once;
1/n stops after n+1 readings. Equality-to-zero is a discontinuous binary
readout on K, since 1/n→0. All sources stop, but no uniform bound exists.

**Infer executability from counterfactual truth.** An original source has
two bits (a,b). Action A reads a and erases b; B reads b and erases a.
The two separate initial-state readouts identify XOR(a,b), a clopen target
on the finite compact source. No reset-free adaptive policy can decide it:
after A, sources (a,0) and (a,1) share both observed outcome and current
state but have opposite XOR; after B use (0,b) and (1,b). All subsequent
histories are identical for that pair by deterministic induction. Stopping
without a first action also fails. Removing erasure permits depth-two
classification. This countermodel is already present in the repository's
policy theory; the new independent depth recursion cross-checks it.

## Probe, evidence, provenance, and boundaries

`observational_succ/swarm_policy_topology.py` supplies exact rational and
integer controls, with an independent recursive enumeration of all bounded
adaptive XOR policies. Tests preserve invalid-source and no-erasure controls.
The algebraic erased-pair argument proves the unlimited no-go; bounded
enumeration alone does not. These are declared mathematical sources, not
authenticated hardware, neuroscience, or a proof of RH.

Primary context: Anush Tserunyan, *Introduction to Descriptive Set Theory*,
§2.C (König lemma and compact branch spaces), §3.A (open-cover/closed-family
compactness), https://homepages.math.uic.edu/~sinapova/Anush%20DST%20lecture%20notes.pdf.
The local adaptation above is derived directly; the source is not credited
with this exact source-changing policy theorem. A coalgebraic direction is
Henning Urbat and Thorsten Wißmann, *Well-Founded Coalgebras Meet König's Lemma*
(2025 preprint, revised 2026),
https://arxiv.org/abs/2507.18539; no theorem from it is load-bearing here.

Next verdict-changing probe: formalize cylinder continuity plus the policy
replay induction, extending the finite-subcover kernel statement to the
entire source-changing policy semantics. The existence of a terminating
policy remains a separate instrument-relative synthesis problem.

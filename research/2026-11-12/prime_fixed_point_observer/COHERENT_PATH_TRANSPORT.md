# Protected transport, accumulated error, and causal reach

Parent: `e9639c0ddb07385c6000b670d26cf0f7b91dacaa`.
Status: PROVED LOCAL for the declared finite models. These statements
compose the code-level channel criteria and do not specify objective collapse.
The comparator sees only present outputs at one calibrated meeting event.

## 1. What counts as a coherent path

For each patch x choose a finite-dimensional logical space C_x and an
isometric encoding J_x:C_x -> H_x into that observer's accessible system.
On an edge e:x->y let U_e:C_x->C_y be a logical isometry. An actual
larger-carrier interaction with a specified initially independent auxiliary
state is an isometry W_e:H_x->H_y tensor E_e. Its environment E_e is not
part of the exposed observer output. A **directly protected edge** satisfies

\[
 W_e J_x\psi=(J_y U_e\psi)\otimes\eta_e
 \quad\text{for every }\psi\in C_x,
 \qquad\|\eta_e\|=1.
\tag{1}
\]

The same environmental vector must work for every logical input. It may
depend on the edge, known controls and carrier preparation. Interaction is
permitted and the environment can change. Equation (1) prohibits it from
retaining distinguishable information about this protected logical input.
Its necessity for a specified directly preserved pure channel is proved in
[COHERENT_CHANNELS.md](COHERENT_CHANNELS.md). General error-correctable
transport is broader and requires a declared decoder; a mixed independent
syndrome can be removed before the current output is compared.

This is a statement about a chosen code and access boundary. Changing which
registers are included in H_y changes the question. Calling all records
part of a hypothetical universe does not give the observer operational access
to them. Classical internal histories are not silently transported between
observers or made comparator inputs.

## 2. Composition and a quantitative defect budget

**CPT-01 — PROVED LOCAL, finite composition.** For a finite typed path
e_1,...,e_N satisfying (1), with independent fresh environments and earlier
record registers subsequently untouched, the accumulated isometry obeys

\[
 W_{[N]}J_0\psi
  =(J_N U_N\cdots U_1\psi)
       \otimes\eta_N\otimes\cdots\otimes\eta_1.
\tag{2}
\]

Tensor factors may be put in a different fixed order by a declared unitary
permutation. Proof: apply (1) to the first edge, then to each next encoded
logical state, tensoring identity on existing records. Induction gives (2).
Retaining an environment that is later reused requires treating the whole
joint interaction anew; the fresh-register factorization is not automatic.

Suppose instead the calibrated edge defects satisfy

\[
 \|W_jJ_{j-1}-(J_jU_j)\otimes\eta_j\|\le\epsilon_j.
\tag{3}
\]

The norm is operator norm from the declared logical input space. In a
nonorthonormal coordinate frame its metric must be transported as well.

**CPT-02 — PROVED LOCAL, accumulated error.** Under the same isometry and
fresh-register hypotheses,

\[
 \left\|W_{[N]}J_0
       -(J_N U_N\cdots U_1)\otimes\eta_{[N]}\right\|
 \le\sum_{j=1}^{N}\epsilon_j.
\tag{4}
\]

Proof: expand the difference by replacing one actual edge at a time with
its ideal encoded edge. Before the replaced edge the reference path lies
in its code, so (3) applies. Every remaining actual edge and every logical
prefix has norm one; tensoring identity does not change these operator
norms. The triangle inequality gives (4). Equivalently, the recurrence
d_j <= d_(j-1)+epsilon_j follows by inserting the ideal current encoded
state. The same proof applies with a reference register tensor identity,
so it controls entangled logical inputs as well as individual vectors.

For two paths with error budgets E_A,E_B, assume their actual maps act on
separate twin factors with initially independent auxiliary systems and no
unmodelled cross-arm interaction. Apply the two transported encodings to
a normalized finite twin Phi_d. Suppose their ideal present
outputs in the common orthonormal frame differ from the desired normalized
twin by at most delta. For example delta=0 when their logical unitaries are
U and conjugate(U), with the specified twin convention. Then their actual
pure global state Psi and an ideal Phi_target tensor eta obey

\[
 \|\Psi-\Phi_{\rm target}\otimes\eta\|
 \le E_A+E_B+\delta=:E.
\tag{5}
\]

**CPT-03 — PROVED LOCAL, present probability bound.** After inaccessible
records are traced out, the current joint state rho satisfies

\[
 1-\langle\Phi_{\rm target},\rho\Phi_{\rm target}\rangle
 \le\min(1,E^2).
\tag{6}
\]

Apply the orthogonal projector onto the complement of Phi_target in the
accessible twin output, tensor identity on all environments, to (5).
It kills the ideal vector and its squared norm on Psi is the left side.
This derives a probability bound from verified operator errors; it does
not turn a single successful physical comparison into an exact proof.
The bound can be conservative because successive coherent errors can
cancel. End-point agreement alone does not bound every earlier defect.
A shared carrier is allowed as a different model, but then the actual
joint isometry must be bounded directly; independent per-arm budgets do
not cover arbitrary correlated noise or cross-arm interactions.

## 3. A scalar leakage law needs a declared moving basis

Take a two-dimensional logical code and suppose, in calibrated transported
bases, every edge has the special nondemolition form

\[
 |b\rangle\longmapsto |b\rangle\otimes|e_b^{(j)}\rangle,
 \qquad b=0,1.
\tag{7}
\]

All records are normalized and fresh. Put
g_j=<e_1^(j),e_0^(j)>, using a conjugate-linear first argument. A twin
initially in (|00>+|11>)/sqrt(2), with these interactions on one side,
has current state

\[
 \rho_N=\tfrac12\bigl(|00\rangle\langle00|+|11\rangle\langle11|
       +\gamma_N|00\rangle\langle11|
       +\overline{\gamma_N}|11\rangle\langle00|\bigr),
 \qquad\gamma_N=\prod_{j=1}^N g_j.
\tag{8}
\]

**CPT-04 — PROVED LOCAL.** Equation (8) follows by tracing the product
environment records; inner products of tensor products multiply. Hence
|gamma_N| is nonincreasing, because each |g_j|<=1 by Cauchy--Schwarz.
Phases multiply and may cancel. An individual nonidentity phase does not
cause leakage. For g_1=i and g_2=-i the current gamma returns exactly to1.

The monotonicity is restricted to (7) with fresh inaccessible records.
A reused environment can give a coherence revival; applying CNOT twice
to the same record reverses its first interaction. Changing logical bases
between noncommuting noise steps also requires full channel composition,
not this scalar formula. No universal irreversible defect wave follows.

The present quadratures XX and XY recover Re(gamma_N) and -Im(gamma_N)
under the tested sector promises; see the
[adversarial audit](reviews/coherent_path_adversarial_audit.md).
They do not recover the list of g_j. Distinct histories, including a
nontrivial record-and-reversal, can induce exactly the same present channel.

## 4. Where can an actual disturbance propagate?

The prior construction has no stipulated physical metric, Hamiltonian or
relativistic light cone. Its frame maps alone cannot supply a propagation
speed. A conditional causal statement is nevertheless exact for finite
circuits of specified local unitary gates.

Let the carrier be a finite tensor product. Gate G_j acts only on a declared
set Z_j of factors, and a final observable O acts on factors S. Pull O
backwards through the actual subsequent gates. Its support stays unchanged
through a disjoint gate; through an intersecting gate it is contained in
the union with that gate's support. This recursively defines a conservative
backward causal cone.

**CPT-05 — PROVED LOCAL.** Replacing G_j by another unitary G'_j supported
on the same Z_j has no effect on any final expectation of O for any initial
state, even an entangled one, whenever Z_j is disjoint from that backward
support at its time slice. Proof: the pulled-back O commutes with both
gates, so G_j* O_back G_j=O_back=G'_j* O_back G'_j. Earlier operations
and the initial density matrix therefore produce the same expectation.

For a general local trace-preserving channel on A, the marginal on B is
also unchanged: for Kraus E_a with sum E_a* E_a=I,

\[
 \operatorname{Tr}_A\sum_a(E_a\otimes I)\rho_{AB}(E_a^*\otimes I)
       =\operatorname{Tr}_A\rho_{AB}.
\tag{9}
\]

Test (9) against any B observable and move E_a*E_a around the full trace.
A conditional selected branch can have a different remote conditional
state, but the unavailable selection record cannot change B's unconditioned
local probabilities. This is the standard no-signalling consequence of
local trace-preserving quantum operations, already present in Prime Bridge
PBR-05; it is not a newly proposed physical mechanism.

An algebraic failure of a commuting diagram is a model defect. An executed
interaction is a dynamical event. A conditioned state update is an inference
relative to an outcome record. None is automatically an objectively
propagating physical collapse. The circuit statement identifies the actual
dependency needed to assert an observable influence.

## 5. Information and proof boundary

The useful architecture permits reversible computation and interactions
that do not leak protected logical distinctions, or that admit an explicitly
implemented recovery. It may retain a private workspace and uncompute it
before exposing its present output. A clean workspace is not free storage:
the operations and registers used in that computation still have costs.

If a nonconstant f is copied as |x>|0> -> |x>|f(x)>, the output register
contains logical information. Tracing it out dephases superpositions across
distinct f-values. Including that register in the observer keeps the larger
state coherent; this changes the access boundary rather than evading the
information accounting. Independent classical model reports may legitimately
be all that an application needs, but they do not certify retained quantum
entanglement.

All equations refer to specified source models and present output types.
Perfectly matching wrong models can obey them. They protect a computation's
information, not the truth of an unauthenticated arithmetic interpretation.
The remaining number-theory task still needs its own source-faithful
observable and quantitative remainder estimate.

## Sources and executable receipt

The channel, partial-trace and isometric representation conventions are
classical; John Watrous, [The Theory of Quantum Information, Chapter2,
Sections2.1--2.2](https://jhwatrous.github.io/TQI.2.pdf), was freshly inspected.
The code-recovery antecedent is Knill and Laflamme,
[A Theory of Quantum Error-Correcting Codes](https://arxiv.org/pdf/quant-ph/9604034).
The prior SUCC [Prime Bridge supplement](../../../docs/CLAIM_SUPPLEMENT_ARITHMETIC_ER_EPR.md)
locates earlier recovery and no-signalling work; those archival files are
unchanged. The local proofs here establish the stated composition, error
and support bounds without an external theorem invocation.

`coherent_path_transport_probe.py` supplies exact Gaussian-rational and
integer controls. Universal conclusions rest on the proofs above. The
root's own implementation is separate from the channel and arithmetic
probes, with shared standard-library arithmetic and same-model provenance.

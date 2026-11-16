# Coherent paths: present discrimination and retained counterexamples

**Scope:** finite-dimensional quantum models of a declared present-output
interface, plus elementary exact counterexamples. This review starts from
the published twin continuation `e9639c0ddb07385c6000b670d26cf0f7b91dacaa`
(validated tree `d591ba032b6b0cef8f62a32100455f9c3857b681`). The existing
[twin correlation note](../TWIN_CORRELATION_AND_READOUT.md) is preserved.
No physical experiment, objective collapse mechanism, or arithmetic
asymptotic theorem is asserted. The review uses the same model family as
the constructor; it is a separate derivation and implementation, not
independent empirical corroboration or external peer review.

## 1. Faithful reading and the discriminator

The user's proposed protection has a concrete interpretation: transport
the logical information needed by the twins' final comparison without
leaving an inaccessible carrier record that distinguishes its coherent
alternatives. Allow explicit frame transport, coherent interactions, and
recovery from accessible records. Compare only the outputs currently
available at the meeting. The historical paths remain internal.

Four propositions must stay distinct:

1. The two current outputs are in the same calibrated frame.
2. Their joint current state has retained the relevant coherence.
3. The outputs represent the same source or satisfy the intended arithmetic
   relations.
4. The earlier evolution never lost local coherence or never underwent an
   objective collapse.

The first two admit the finite discriminator below. They do not imply the
last two. A coherent frame mismatch, leakage to an inaccessible record,
and a recoverable temporary record predict different present data in
specified protocols; different histories can nevertheless give exactly
the same present data.

**Preregistered test:** a single real correlation or return probability
should fail to distinguish a pure phase-shifted twin from a dephased twin.
An additional phase quadrature should distinguish them. A sector mutation
must defeat any protocol that omits the declared sector guards. A sequence
that creates and then reverses an environment record should defeat any
claim that current purity certifies uninterrupted past purity.

## 2. A complete current diagnostic on a declared two-branch sector

Let the currently supplied outputs be two qubits `A,B`, in a common
orthonormal frame. They may be an optional quantum output of the observer
models; arbitrary scalar classical model outputs do not provide these
qubits automatically. Let `X,Y,Z` be the Pauli matrices with
`Y|0> = i|1>` and `Y|1> = -i|0>`. For every complex `gamma` with
`|gamma|<=1`, define

\[
\rho_\gamma=\tfrac12\bigl(
|00\rangle\langle00|+|11\rangle\langle11|
+\gamma|00\rangle\langle11|
+\overline\gamma|11\rangle\langle00|\bigr).
\]

Its nonzero eigenvalues are `(1+|gamma|)/2` and `(1-|gamma|)/2`, so these
are precisely the density matrices on this balanced correlated sector.

**CPA-01 — PROVED LOCAL, sector test.** A two-qubit density matrix `rho`
belongs to this family if and only if

\[
\langle Z\otimes Z\rangle_\rho=1,
\qquad \langle Z\otimes I\rangle_\rho=0.
\]

**Proof.** The first equality says `Tr(P_- rho)=0`, where `P_-` is the
projection onto `span{|01>,|10>}`. Positivity forces both that block and
its off-diagonal blocks to vanish: for a positive matrix,
`|rho_ij|^2<=rho_ii rho_jj`. The state is supported on
`span{|00>,|11>}`. Trace one and the second equality force both remaining
diagonal entries to be `1/2`. Hermiticity gives conjugate off-diagonals;
positivity bounds their magnitude by `1/2`. The converse is immediate.

Under these conditions, two more present expectations reconstruct the
entire current state:

\[
x=\langle X\otimes X\rangle=\operatorname{Re}\gamma,
\qquad y=\langle X\otimes Y\rangle=-\operatorname{Im}\gamma,
\qquad \boxed{\gamma=x-iy.}
\]

These signs follow by applying `X tensor Y` to `|00>` and `|11>`;
the probe computes them with an explicit complex matrix implementation.

These are exact statements about a specified mathematical density matrix
or exact expectations. A finite sample in which no sector violation is
observed does not prove the equalities. The four observables also are not
all jointly measurable on one copy: the two quadratures do not commute.
A physical implementation needs repeated preparations with justified
stationarity and statistical/calibration error bounds, or a separately
provided classical description of the current density matrix. It does
not gain a one-shot equality oracle or access to either observer's past.

### Phase and visibility have different meanings

Direct diagonalization gives

\[
\boxed{\operatorname{Tr}\rho_\gamma^2=(1+|\gamma|^2)/2},
\qquad
\boxed{f_+=\langle\Phi^+|\rho_\gamma|\Phi^+\rangle
=(1+\operatorname{Re}\gamma)/2}.
\]

Here `f_+` is the Bell-projector acceptance probability, equivalently the
**squared** fidelity with a pure target in the convention where fidelity
is the unsquared overlap norm. This convention avoids a silent square-root
change relative to Watrous's fidelity notation.

The phase of `gamma` records relative calibration; its modulus records
the surviving contrast in this sector. A local phase correction
`diag(1,u)` on the first qubit, for `|u|=1`, sends
`gamma -> gamma conjugate(u)`. For nonzero `gamma`, choosing
`u=gamma/|gamma|` makes it positive real. The best phase-corrected Bell
overlap is then `(1+|gamma|)/2`; the spectrum, and hence the purity, remain
unchanged. The phase is undefined at zero and poorly conditioned near zero.

**CPA-02 — PROVED LOCAL, entanglement boundary in this family.**
`rho_gamma` is pure and maximally entangled exactly when `|gamma|=1`.
It is separable exactly when `gamma=0`. For `0<|gamma|<1`, it is a mixed,
entangled state; its negativity is `|gamma|/2`.

**Proof.** Purity follows from the eigenvalues. Both individual marginals
are always `I/2`, so a pure member is maximally entangled. The partial
transpose has eigenvalues `1/2,1/2,|gamma|/2,-|gamma|/2`. For nonzero
`gamma` it is not positive. Every separable state has positive partial
transpose, since transposition preserves positivity on each product
factor and sums preserve positivity; thus nonzero members are entangled.
At zero, the displayed expression is a mixture of the two product
states. The sum of negative eigenvalue magnitudes gives the stated
negativity. No numerical eigenvalue decision is needed.

**Exact hostile witness.** Compare `gamma=i` and `gamma=0`:

| Present quantity | Pure phase-shifted twin | Dephased twin |
| --- | ---: | ---: |
| `ZZ` | 1 | 1 |
| `ZI` | 0 | 0 |
| `XX` | 0 | 0 |
| Bell overlap `f_+` | 1/2 | 1/2 |
| `XY` | -1 | 0 |
| Purity | 1 | 1/2 |
| Individual marginals | `I/2`, `I/2` | `I/2`, `I/2` |

Thus failure to return to the designated Bell state is not by itself
evidence that entanglement was destroyed. A fully coherent relative
phase can account for the failure. At the opposite extreme, perfectly
matching `Z` results do not establish quantum coherence: the dephased
mixture matches in `Z` every time.

The guards do real work. The product state `|+>|+>` and the odd Bell
state `(|01>+|10>)/sqrt(2)` both have `XX=1, XY=0`, which would falsely
look like `gamma=1` if the sector hypothesis were silently assumed.
They fail `ZZ=1`. The state `(3|00>+4|11>)/5` satisfies the first guard
but fails the balanced-population guard.

### Exact conditioning within the sector

For any admissible `gamma,eta`, the difference has nonzero eigenvalues
`+|gamma-eta|/2` and `-|gamma-eta|/2`. Therefore its trace distance is

\[
\boxed{D(\rho_\gamma,\rho_\eta)=|\gamma-\eta|/2.}
\]

If the exact sector promise has been established separately and
`|x_hat-x|<=epsilon_x`, `|y_hat-y|<=epsilon_y`, then

\[
|\widehat\gamma-\gamma|
\le\sqrt{\epsilon_x^2+\epsilon_y^2},
\qquad
\bigl||\widehat\gamma|-|\gamma|\bigr|
\le\sqrt{\epsilon_x^2+\epsilon_y^2}.
\]

The first inequality is Euclidean geometry; the second is the reverse
triangle inequality. If the estimate lies outside the unit disk, one
must impose physical consistency before calling it a density matrix.
The following result supplies a leakage budget when the true sector
expectations are near, rather than equal to, their ideal values.

### Robust reconstruction with imperfect sector guards

Let `rho` now be any two-qubit density matrix in the declared calibrated
frame. Set

\[
z=\langle ZZ\rangle,\quad u=\langle ZI\rangle,
\quad x=\langle XX\rangle,\quad y=\langle XY\rangle,
\quad \epsilon=(1-z)/2<1,\quad p=1-\epsilon>0.
\]

The numbers here are the **true expectations**. Thus the guards may
deviate from their target values, while their numerical values are still
assumed known. Sampling uncertainty in those guard values is a further
layer, addressed below. Let `Pi_D` be radial projection onto the closed
complex unit disk, and define the physically admissible reconstructed
state by

\[
g=\Pi_D\!\left(\frac{x-iy}{p}\right),
\qquad \widehat\rho=\rho_g.
\]

**CPA-05 — PROVED LOCAL, robust present-output reconstruction.**

\[
\boxed{
D(\rho,\rho_g)
\le \min\!\left(1,\sqrt\epsilon+
\frac{|u|+2\epsilon}{2p}\right).
}
\tag{R1}
\]

**Proof.** Write `P=|00><00|+|11><11|`. The even-sector weight is
`Tr(P rho)=p`; the complementary weight is `epsilon`. Define
`tau=P rho P/p` as a density matrix on the whole two-qubit space, supported
in the even sector.

Choose a purification `|psi>` of `rho`. The normalized projected vector
`|phi>=(P tensor I)|psi>/sqrt(p)` purifies `tau` and has overlap
`<psi,phi>=sqrt(p)`. The trace distance of two normalized pure states
is `sqrt(1-|<psi,phi>|^2)`, obtained by diagonalizing their difference on
their at most two-dimensional span. Partial trace cannot increase trace
distance: the variational formula for the trace norm of a Hermitian
operator reduces this to `||O tensor I||=||O||`. Consequently

\[
D(\rho,\tau)\le\sqrt\epsilon.
\tag{R2}
\]

Put `a=rho_00,00`, `b=rho_11,11`, `c=rho_00,11`, and
`d=rho_01,10`. The even block has imbalance `m=(a-b)/p` and coherence
`gamma=2c/p`. Positivity gives `|c|^2<=ab`, hence `|gamma|<=1`.
The odd diagonal difference has absolute value at most its total mass
`epsilon`. Since `u` is the sum of that difference and `a-b`,

\[
|m|\le\frac{|u|+\epsilon}{p}.
\]

Balancing the even block while retaining the same off-diagonal produces
the valid state `rho_gamma`. Its difference from `tau` is the diagonal
matrix with entries `m/2,-m/2` on the even sector, so

\[
D(\tau,\rho_\gamma)=|m|/2
\le\frac{|u|+\epsilon}{2p}.
\tag{R3}
\]

The exact Pauli products on both parity sectors give

\[
x-iy=2c+2\overline d.
\]

Positivity of the odd principal block gives `2|d|<=epsilon`. Therefore
the unprojected estimate differs from `gamma` by at most `epsilon/p`.
Radial projection does not increase distance to any point in the disk.
For a direct proof in the only nontrivial case, write the estimate as
`r v`, with `r>1` and `|v|=1`; then

\[
|rv-\gamma|^2-|v-\gamma|^2
=(r-1)(r+1-2\operatorname{Re}(\overline v\gamma))\ge0.
\]

It follows that `|g-gamma|<=epsilon/p`, and the exact sector distance
formula yields

\[
D(\rho_\gamma,\rho_g)\le\frac{\epsilon}{2p}.
\tag{R4}
\]

Adding (R2)--(R4) proves the stated bound; trace distance between density
matrices is also at most one. No inaccessible historical record appears
in this reconstruction.

If quadrature estimates satisfy
`sqrt((x_hat-x)^2+(y_hat-y)^2)<=delta_xy`, while the guard expectations
`z,u` are known exactly, use
`g_hat=Pi_D((x_hat-i y_hat)/p)`. The same proof gives

\[
\boxed{
D(\rho,\rho_{\widehat g})
\le \min\!\left(1,\sqrt\epsilon+
\frac{|u|+2\epsilon+\delta_{xy}}{2p}\right).
}
\tag{R5}
\]

Thus the quadrature error contribution is `delta_xy/(2p)`. If the
guards themselves are sampled, their uncertainty must also be propagated
through `epsilon`, `u`, and especially the denominator `p`. Substituting
sample means into (R1) is not a certified confidence bound. One can use a
joint confidence region and maximize the proved bound together with the
reconstruction's denominator uncertainty over that region; no such data
collection or confidence calibration has been executed here.

The case `p=0` is excluded because the outputs contain no even-sector
mass. For small positive `p`, the bound may saturate at one and become
uninformative. That is a limitation of this reconstruction interface.
An informative bound for a different sector or different code requires
declaring and analyzing that new interface.

The standalone probe checks the exact off-diagonal identity, positivity
and imbalance inequalities on general rational pure/mixed states. It
also checks the radial-projection contraction on rational rays and the
complete bound on Bell-diagonal examples with an independently computed
trace distance, including quadrature perturbations. A pure cross-sector
family tests the square-root projection loss exactly. None of these
finite controls substitutes for the proof above.

## 3. Carrier leakage, coherent interaction, and non-identifiability

Take normalized environment records `e_0,e_1` and the globally pure state

\[
|\Psi\rangle=\bigl(|00\rangle|e_0\rangle+
e^{i\theta}|11\rangle|e_1\rangle\bigr)/\sqrt2.
\]

Tracing out the inaccessible environment gives the preceding family with

\[
\boxed{\gamma=e^{-i\theta}\langle e_1,e_0\rangle.}
\]

Thus distinguishable environment records can suppress the accessible
contrast without any nonunitary evolution of the whole. Suppression is
continuous, not an all-or-nothing event. For records
`e_0=|0>` and `e_1=(3|0>+4|1>)/5`, zero relative phase gives
`gamma=3/5`, purity `17/25`, and negativity `3/10`.

Nevertheless, detecting `|gamma|<1` identifies the present reduced-state
deficit under this model; it does not identify its unique past mechanism.
For example,

\[
\rho_0=\tfrac12|\Phi^+\rangle\langle\Phi^+|
+\tfrac12|\Phi^-\rangle\langle\Phi^-|
=\operatorname{Tr}_E|\mathrm{GHZ}\rangle\langle\mathrm{GHZ}|.
\]

The same current state can be supplied by an unrecorded classical random
phase or by discarding an entangled which-branch record. Every POVM on
the current `AB` outputs has the same probability in the two models,
because both probabilities are `Tr(M rho_0)`. The same conclusion holds
for any number of independent copies when the available joint state is
the same product `rho_0^tensor n`. Extra cross-run records or correlations
are additional accessible data, not supplied by this conclusion.

This distinction between interaction with an environment and phase
averaging has a classical antecedent in Zurek, Section IV.C and VIII.B
of [the 2003 review](https://arxiv.org/pdf/quant-ph/0105127). The identical
state and non-identifiability argument above are explicit local proofs.

### An apparent loop defect need not be decoherence

A coherent path with relative transport `Z` on the first twin maps
`Phi+` to `Phi-`. They are orthogonal, yet both are pure and maximally
entangled. This is a mismatch with the chosen return frame, not loss of
entanglement. In contrast, a global `-I` changes the vector sign but
leaves every density matrix unchanged. A branch-global sign becomes
observable only if the branch is placed in a declared coherent controlled
comparison, making it a relative phase. Phase conventions cannot be
inferred from the geometric statement that observers approached from
opposite directions.

Even perfect conjugate twin preservation cannot validate an arbitrary
source relation. Assign `U=diag(1,i)` to a generator declared to satisfy
`g^2=1`. The pair `U tensor conjugate(U)` preserves `Phi+` exactly, but
`U^2=diag(1,-1)` violates the declared relation. Common coherent evolution
does not authenticate the arithmetic shared by both models.

## 4. Present recovery does not certify a pristine history

Prepare `Phi+_AB tensor |0>_E`. Apply `CNOT_(A->E)`. The result is GHZ,
and the current `AB` state is `rho_0`. Apply the same CNOT again. The
entire joint state returns exactly to its initial value.

**CPA-03 — PROVED LOCAL, retrodiction boundary.** A path doing nothing
and a path making then coherently undoing this record have identical
final joint states. The second has an intermediate reduced `AB` state
that is separable; the first does not. No present-output comparator can
distinguish the histories if no additional record survives.

This allows a constructive repair: recover the relevant logical state
before the meeting when the necessary environment remains accessible.
It also defeats the inference that a successful pure final comparison
proves no earlier local decoherence. Recovery is evidence about the
current recovered output, not a certificate of an untouched past.

An operation on the environment alone cannot unconditionally repair
`AB`: a unitary preserves `inner(e_1,e_0)`, and, more generally, a
trace-preserving operation on `E` leaves the `AB` marginal unchanged.
Resetting or discarding a record without conditional control is not a
quantum eraser for the remote reduced state.

For GHZ, measuring the current environment in the `X` basis supplies
`Phi+` or `Phi-` on `AB`, each with probability `1/2`. Without the
syndrome, their mixture is still `rho_0`. If the current syndrome is
accessible, applying `Z` to one twin on the minus outcome restores
`Phi+` in either branch. This uses a present recovery record and its
control action; it does not compare historical observer records across
different frames. The information/control access has an explicit cost.

### A pure final projection can manufacture the desired appearance

Let `P=|Phi+><Phi+|`. Even the completely dephased input obeys

\[
P\rho_0P=\tfrac12P.
\]

A joint Bell projection at the meeting succeeds with probability `1/2`
and its conditional output is the pure maximally entangled state `P`.
The meeting operation has created that conditional state from a mixed
input. The purity of the selected final outcome therefore cannot certify
the coherence of the incoming state or its earlier path. Dropping failed
branches would conceal precisely the evidence the protocol needs. An
unconditional preparation of a fixed pure output would be an even more
extreme, wholly uninformative version of the same mistake.

## 5. A local update is not an instantaneous causal signal

**CPA-04 — CLASSICAL, local proof.** For any finite bipartite density
matrix `rho_AB` and any trace-preserving completely positive local map
`N_A(rho)=sum_j K_j rho K_j*`, with `sum_j K_j* K_j=I`,

\[
\boxed{\operatorname{Tr}_A[(N_A\otimes I_B)(\rho_{AB})]
=\operatorname{Tr}_A\rho_{AB}.}
\]

**Proof.** For every observable `O_B`, cyclicity of the trace gives

\[
\sum_j\operatorname{Tr}\bigl((I\otimes O_B)
(K_j\otimes I)\rho(K_j^*\otimes I)\bigr)
=\operatorname{Tr}\bigl((\sum_jK_j^*K_j\otimes O_B)\rho\bigr)
=\operatorname{Tr}((I\otimes O_B)\rho).
\]

All `B` expectations agree, so the density matrices agree. Selecting a
particular outcome instead of summing all branches yields a conditional
state and is not trace preserving. It can change the conditioned remote
prediction, but that branch label must be available to use the condition.
It is not a controllable instantaneous signal to an uninformed twin.

Consequently a proposed propagating carrier defect requires its own
interaction law, causal graph, or local dynamical equation. The joint
correlation may change while the distant twin's local marginal stays
exactly the same. The above algebra supplies no physical propagation
speed, spacetime metric, or objective collapse law. Those must be
specified and tested separately.

The channel and partial-trace assumptions are standard; see Watrous,
[Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), Section 2.1.2,
Theorem 2.26, and Corollary 2.27. Finite state discrimination and the
single-outcome boundary are quantified by his
[Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), Theorem 3.4.

## 6. Verdict, novelty boundary, and executable receipt

The proposed protection survives as a conditional architecture: preserve
the required coherent information, transport its frame explicitly, and
use accessible recovery when specified. The present diagnostic can
distinguish a coherent relative phase from reduced contrast on the
declared two-branch sector. That is a new concrete comparator for this
dossier, assembled from classical two-qubit algebra; no external novelty
or universal truth test is claimed.

| Claim | Verdict | Decisive receipt or next probe |
| --- | --- | --- |
| A single Bell-return probability identifies decoherence | REFUTED | `gamma=i` versus `gamma=0`, both overlap `1/2`. |
| Calibrated quadratures determine the balanced correlated present state | PROVED LOCAL | Sector support proof and `gamma=XX-iXY`. |
| Imperfect true sector guards still permit bounded present reconstruction | PROVED LOCAL | (R1)--(R5), normalized projection and radial contraction; the bound may saturate. |
| Any carrier interaction destroys entanglement | REFUTED | Coherent phase transport; nontrivial interactions can also be reversed. |
| Loss of twin entanglement is necessarily binary | REFUTED | `0<|gamma|<1` is mixed but entangled. |
| Present recovered purity certifies no earlier reduced decoherence | REFUTED | CNOT record creation and reversal versus idle history. |
| A pure selected meeting output certifies a pure incoming twin | REFUTED | `P rho_0 P=P/2`. |
| A local unconditioned update instantly signals the twin | REFUTED in the channel model | Trace-preservation proof and exact local-channel controls. |
| Current output uniquely identifies the past leakage mechanism | REFUTED | Phase-average and GHZ reduction give the same density matrix. |
| Output-only comparisons establish source arithmetic | REFUTED | Shared coherent `diag(1,i)` violates the prescribed involution. |
| Objective collapse occurs only at the meeting | UNVERIFIED | Requires a physical collapse model and a discriminating experiment. |

The standalone exact probe is
[coherent_path_adversary_probe.py](coherent_path_adversary_probe.py).
It uses a separate standard-library Gaussian-rational implementation,
calibrated Pauli products, environment partial traces, unitary controls,
Kraus channels, syndrome recovery, and postselection. A denominator-13
grid is kept distinct from the denominator-5 design examples. Its finite
check counts are implementation receipts, not votes for the universal
proofs. The root records actual execution and integrity results after
replay. No previous dossier implementation is changed by this review.

**Next verdict-changing probe:** select the actual arithmetic current
output and the information it must preserve; then prove that its allowed
channel and its calibrated comparison separate the relevant source
defects. The present quantum-sector theorem neither supplies nor assumes
the open prime-pair remainder estimate.

## Cross-audit of the protected-path composition

The separate review of [COHERENT_PATH_TRANSPORT.md](../COHERENT_PATH_TRANSPORT.md)
checked the typed encoded-edge factorization, fresh-record induction,
operator-norm telescoping, extension by an entangled reference, the
projection-based Bell-failure estimate, and the order of the backward
causal-cone calculation. No algebraic defect was found in those statements
under their declared finite/isometric hypotheses.

For the two-arm `E_A+E_B` step, the actual path maps must act as a tensor
product on the twin inputs and initially independent auxiliary systems.
An unmodelled shared carrier environment or cross-arm interaction requires
a bound for the joint implementation. The individual edge norm estimates
alone are not a proof for that enlarged noise model. This is a scope
condition, not an inference from a clean numerical example.

The root's standalone transport probe was replayed unchanged and returned
**474 checks, PASS**. Its unnormalized initial twin has squared norm two;
the independent partial trace and Bell overlap each correctly divide by
that normalization. Its causal controls test both a disjoint support
identity and an actual coupled influence, rather than treating a common
correlation as a signalling channel.

After the robust-guard extension, this review's own standalone probe
returned **9,188 exact checks, PASS**, recorded in
[COHERENT_PATH_ADVERSARY_REPORT.json](../receipts/COHERENT_PATH_ADVERSARY_REPORT.json).
The additional checks include 333 general guard identities/inequalities,
120 radial contraction checks, 375 Bell-diagonal guard controls,
750 complete/noisy reconstruction checks, and 48 pure projection controls.
These counts overlap in mathematical content and do not constitute
independent votes. The universal reconstruction result rests on the proof.

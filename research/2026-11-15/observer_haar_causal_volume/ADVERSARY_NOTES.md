# Adversary: conditioning, disturbance, coherence, and signalling

## Source and scope

This bearing starts from SUCC `2c73e6388b24c7a66683d089733105d14acda08a`
on `research/observer-haar-causal-volume-2026-11-15`, after reading the
round's `HOLE_CONTRACT.md` and repository instructions. The task is a
finite rational instrument, not a physical measurement of the BBP source.

Inherited source read before implementation:

| Artifact | Pinned Git blob |
|---|---|
| `observational_succ/quantum_records.py` | `76fae4755c93c1d192388b0c4d1973705df4e1b7` |
| `observational_succ/arithmetic_tfd.py` | `fb98e4bf30ace8aaac920e446e93aa1580ee5502` |
| `research/2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md` | `5923ba1e668b590025255c413f6c93fd69886dd4` |

The inherited five `tests.test_quantum_records` tests pass. The new module
will reuse its exact complete real-qubit `Instrument`, extending its
application to one side of a two-qubit state without changing that source.
The arithmetic TFD dossier already distinguishes its pure entangled state
from a separable mixture with identical marginals, and already proves the
local trace-preserving no-signalling law. Those are inherited mechanisms,
not newly discovered facts or evidence for a gravitational dual.

## Frozen finite controls

Before implementation, freeze the coherence values
`-1,-3/4,-1/3,0,1/5,2/3,3/4,1`, the qubit Bloch coordinates
`(0,0),(1,0),(-1,0),(0,1),(0,-1),(3/5,4/5),(-3/5,4/5),(2/5,-1/5)`,
and the local instruments identity, bit flip, X/Z projectors, Z-read/reset,
weak rational Z measurement, and rational amplitude damping with survival
amplitude `3/5` and jump amplitude `4/5`. Both local sides must be checked.

Positive, negative, and null controls include product states, separable
mixtures, the whole proposed coherence family, a zero-probability branch,
and nonmaximally mixed unequal marginals. Mutations must reject an invalid
state, an incomplete instrument, omitted postselection normalization,
unweighted mixing of conditional states, erased coherence, a reversed
phase sign, and duplicated axes masquerading as complementary axes.

The restricted Bell X/Z data must also be reproduced by two shared
classical signs. A stronger rotated-setting test uses
`A0=Z,A1=X,B0=(3X+4Z)/5,B1=(-3X+4Z)/5`; enumerate all 16 deterministic
local setting tables, then compare the exact model predictions at
`c=0,3/4,1`. This is a mathematical probe specification, not empirical
Bell evidence. Local-setting independence, no communication between
wings, and no selective loss are its declared physical interpretation
conditions.

Classical reset/flip kernels and equal-energy coherent/dephased states
will defeat the claims that noncommutation alone is quantum or that
larger energy certifies truth, entanglement, or classicality.

## Q1. The proposed state family is valid, with a detectable signed phase

Use the ordered tensor basis \(|00\rangle,|01\rangle,|10\rangle,|11\rangle\),
and Pauli conventions

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Thus a computational zero is the \(+1\) Z outcome. The proposed family is

\[
\rho(c)=\frac12\begin{pmatrix}
1&0&0&c\\0&0&0&0\\0&0&0&0\\c&0&0&1
\end{pmatrix},\qquad -1\le c\le1.
\tag{Q1}
\]

**DISCLOSED within the specified quantum model.** Its nonzero eigenvalues
are \((1+c)/2\) and \((1-c)/2\), with eigenvectors proportional to
\(|00\rangle+|11\rangle\) and \(|00\rangle-|11\rangle\). It is therefore
positive semidefinite exactly on the stated interval, and has trace one.
Its purity is \((1+c^2)/2\). Both reduced states are \(I/2\), for every
\(c\). At \(c=0\) it is the separable mixture

\[
\tfrac12|00\rangle\langle00|+\tfrac12|11\rangle\langle11|;
\]

at \(c=1\) and \(-1\) it is a Bell state with opposite relative phases.
The diagonal/separable and coherent examples are classical quantum
information controls; see Watrous, [*The Theory of Quantum Information*,
Chapter 2, Example 2.6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).
The arithmetic TFD source already uses the same marginal-versus-coherence
distinction in its own infinite-dimensional domain.

Direct matrix multiplication gives

\[
\langle ZZ\rangle=1,\quad \langle XX\rangle=c,\quad
\langle XZ\rangle=\langle ZX\rangle=0.
\tag{Q2}
\]

For local unit axes \(A=x_AX+z_AZ\), \(B=x_BX+z_BZ\), the exact joint
outcome probabilities are

\[
\Pr(a,b\mid A,B)=\frac14\left[1+ab(c x_Ax_B+z_Az_B)\right],
\qquad a,b\in\{-1,1\}.
\tag{Q3}
\]

All Z observations are identical across the family. X correlations
distinguish its signed coherence. Replacing \(\rho(c)\) by its diagonal
therefore destroys a genuine predicted observable, even though all local
marginals and Z records remain unchanged. The sign of the X axis and the
relative phase are operational conventions retained in (Q1)–(Q3).

## Q2. A trusted two-axis entanglement witness, with its assumptions

For every separable two-qubit density matrix,

\[
\boxed{|\langle XX\rangle|+|\langle ZZ\rangle|\le1.}
\tag{Q4}
\]

**Proof.** For a product \(\sigma\otimes\tau\), put
\(x=\operatorname{tr}(\sigma X),z=\operatorname{tr}(\sigma Z)\), and
\(u=\operatorname{tr}(\tau X),v=\operatorname{tr}(\tau Z)\). Trusted
orthogonal qubit axes imply \(x^2+z^2\le1\), \(u^2+v^2\le1\), including
for general complex qubit states. For example,
\((xX+zZ)^2=(x^2+z^2)I\), so the expectation \(x^2+z^2\) is at most
the operator norm \(\sqrt{x^2+z^2}\). Cauchy–Schwarz now gives
\(|xu|+|zv|\le1\). For a separable convex mixture, apply the triangle
inequality before averaging these product bounds. QED.

For (Q1), the score is \(1+|c|\), so every \(c\ne0\) is certified
entangled by these **trusted qubit** observations. A second derivation is
the partial transpose: its eigenvalues are \(1/2,1/2,c/2,-c/2\), one
strictly negative if \(c\ne0\). Positivity of the partial transpose is
necessary for every separable state, because transposition preserves each
positive local factor. This is the classical Peres criterion; the source
paper is [Peres (1996)](https://arxiv.org/abs/quant-ph/9604005).

The code returns the score, not an unconditional classification when the
score is at most one. The rational pure state with amplitudes
\((1,1,1,-1)/2\) is maximally entangled but has zero score in these fixed
same-axis measurements. Rotating the tested axes detects it. Conversely,
duplicating Z and calling the copies complementary gives score two even
for the separable state \(|00\rangle\). The qubit dimension, unit
normalization, and orthogonal-axis calibration are load-bearing.

For empirical measurements, finite error bars must also be retained. If
each predicted correlation is replaced by an estimate with certified
errors \(\epsilon_X,\epsilon_Z\), a sufficient lower witness is
\(\max(0,|\widehat C_X|-\epsilon_X)+
\max(0,|\widehat C_Z|-\epsilon_Z)>1\). Exact model fractions are not
experimental confidence bounds.

## Q3. Why the restricted witness is not a device-independent Bell test

Let two classical uniform signs \(\lambda_X,\lambda_Z\) be independent
and shared between Alice and Bob. Each wing, when asked for X or Z,
returns the corresponding shared sign. The same-setting correlations are
one and cross-setting correlations are zero. Marginals are uniform.
This reproduces **every joint probability for all four X/Z setting pairs**
of \(\rho(1)\).

There is no contradiction with (Q4): each classical table has simultaneous
deterministic X and Z values, which are not a permitted trusted local
qubit state. Its putative local Bloch coordinates would have squared
length two. Thus the two-axis witness certifies entanglement within a
declared quantum model; those restricted probabilities alone do not rule
out unrestricted classical response tables.

### A stronger exact discriminator using rational projectors

Root proposed the following rotated-setting probe after this calibration
gap was identified. It has been independently checked and implemented:

\[
A_0=Z,\quad A_1=X,\qquad
B_0=(4Z+3X)/5,\quad B_1=(4Z-3X)/5.
\]

Every observable squares to the identity, and every projector
\((I\pm A_i)/2,(I\pm B_j)/2\) has rational entries. For the CHSH sign
convention

\[
S=\langle A_0B_0\rangle+\langle A_0B_1\rangle
+\langle A_1B_0\rangle-\langle A_1B_1\rangle,
\]

the family gives

\[
\boxed{S(c)=\frac{8+6c}{5}.}
\tag{Q5}
\]

For a deterministic local table,
\(S=a_0(b_0+b_1)+a_1(b_0-b_1)\). Exactly one parenthesis is zero and
the other is \(\pm2\), hence every one of the sixteen tables has
\(|S|=2\). Convex mixtures satisfy \(|\mathbb ES|\le2\). The same
convex decomposition covers local stochastic responses by including
their local randomness in the hidden variable. It requires one common
hidden-variable distribution independent of the setting choices.

The exact controls are

| State parameter | CHSH prediction | Interpretation within the declared probe |
|---|---:|---|
| \(c=0\) | \(8/5\) | Separable negative control |
| \(c=3/4\) | \(5/2\) | Exceeds the local-table bound |
| \(c=1\) | \(14/5\) | Bell positive control |
| \(c=1/5\) | \(46/25\) | Entangled, but these fixed CHSH settings do not violate |

For negative \(c\), reversing the declared Alice X orientation gives the
corresponding positive-phase probe; it must not be silently replaced in
the sign convention. In a physical experiment, interpreting a violation
against local hidden-variable models requires setting independence, no
inter-wing communication during the trial, and retention of all trials
rather than outcome-dependent selection. The code predicts and audits
these probabilities; it has performed no experiment on BBP, a person,
or a gravitational system.

## Q4. Conditional remote changes do not imply signalling or entanglement

For a complete local instrument \(\{K_o\}\),
\(\sum_oK_o^\dagger K_o=I\), set

\[
\widetilde\rho_o=(K_o\otimes I)\rho(K_o^\dagger\otimes I),
\quad p_o=\operatorname{tr}\widetilde\rho_o,
\quad\rho_o=\widetilde\rho_o/p_o\quad(p_o>0).
\]

For every Bob observable \(B\), cyclicity of the finite-dimensional trace
gives

\[
\begin{aligned}
\operatorname{tr}\!\left[\sum_o\widetilde\rho_o(I\otimes B)\right]
&=\operatorname{tr}\!\left[\rho\sum_o(K_o^\dagger K_o\otimes B)\right]\\
&=\operatorname{tr}[\rho(I\otimes B)].
\end{aligned}
\]

Therefore

\[
\boxed{\sum_op_o\rho_{B|o}=\rho_B.}
\tag{Q6}
\]

This is the inherited arithmetic TFD no-signalling mechanism, now checked
in a finite instrument with explicit outcome weights. It does not assert
that the joint state or Alice's state stays unchanged. It also does not
assign an interpretation to a hidden physical collapse: it states which
operational outcome distributions can change. Bob needs Alice's outcome
label to sort the conditional ensembles; forgetting that label recovers
the unchanged marginal.

For every \(c\), Alice's Z outcomes in (Q1) have probability one half and
leave conditional Bob states \(|0\rangle\langle0|\) or
\(|1\rangle\langle1|\). This happens identically for the separable
\(c=0\) mixture. A classical pair \(A=B\), each uniformly random, has
the same conditional update with no quantum entanglement. Conversely,
Alice's X outcomes leave

\[
\rho_{B|\pm X}=\tfrac12(I\pm cX),\qquad p_\pm=1/2,
\]

which resolve the signed coherence in the trusted model. Discarding
Alice's Z outcome maps \(\rho(c)\) to \(\rho(0)\): it removes the joint
coherence while preserving Bob's marginal. At \(c=0\) that same
discarded-outcome operation leaves the joint state unchanged.

### Unequal probabilities are an essential mutation control

Use rational amplitude damping

\[
K_{\rm keep}=\begin{pmatrix}1&0\\0&3/5\end{pmatrix},\qquad
K_{\rm jump}=\begin{pmatrix}0&4/5\\0&0\end{pmatrix}.
\]

It is complete and nonunital. On \(\rho(0)\), the probabilities are
\(17/25\) and \(8/25\). Conditional Bob states are
\(\operatorname{diag}(25/34,9/34)\) and
\(\operatorname{diag}(0,1)\). Their probability-weighted average is
\(I/2\). Their **unweighted** average is
\(\operatorname{diag}(25/68,43/68)\), producing an apparent remote
change only because the averaging law was altered.

Likewise, the unnormalized keep branch has trace \(17/25\), so it cannot
be used as a normalized conditional density. The keep Kraus operator
alone is a trace-decreasing filter, not a deterministic channel; the
inherited constructor rejects it when presented as a complete instrument.
Zero-probability outcomes have no conditional state and cannot be logged
as observed events.

## Q5. Classical disturbance and noncommutation controls

Classical conditioning and physical disturbance are separate operations.
Starting with the correlated classical pair \(A=B\), reading Alice and
then resetting her bit to zero maps the joint distribution to
\(A=0\), \(B\) uniform. It changes the joint state and its future
correlations without creating quantum entanglement. The exact Kraus
representation

\[
K_0=|0\rangle\langle0|,\qquad K_1=|0\rangle\langle1|
\]

acts this way on the diagonal \(\rho(0)\). Its output is
\(|0\rangle\langle0|\otimes I/2\). A valid quantum-channel notation
can represent classical stochastic processes as a special case; the
notation does not certify a quantum mechanism.

Noncommutation alone is equally insufficient. With column-probability
vectors, the classical reset and flip kernels are

\[
R=\begin{pmatrix}1&1\\0&0\end{pmatrix},\qquad
F=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

They are nonnegative and column stochastic. Applied in opposite orders
to \((1/2,1/2)^T\), \(RF\) gives \((1,0)^T\) and \(FR\) gives
\((0,1)^T\). This is an exact classical order-effect receipt. A nonzero
Haar/Gamma projection-composition defect must survive such classical
controls before being interpreted as evidence for entanglement.

## Q6. Energy is not a surrogate for truth or classicality

Fix the ordinary qubit excitation operator \(N=|1\rangle\langle1|\)
and Hamiltonian \(H=N\otimes I+I\otimes N\). Every \(\rho(c)\) has
the same expected energy one, while its coherence, purity, entanglement
witness, and CHSH predictions differ. Dephasing changes \(c=1\) to
\(c=0\) at unchanged energy. This alone refutes identifying this scalar
energy with coherence or entanglement.

Replacing \(H\) by \(H+C I\) raises every expected energy by \(C\)
without changing the state or any outcome probability. It changes
unitary time evolution only by a global phase. The exact test uses
\(C=17\): the expectation becomes 18 while both witness values remain
unchanged. Thus an uncalibrated absolute energy increase cannot certify
truth or a transition to classicality. If “energy” instead denotes a
probe cost, information gain, or a policy potential, that quantity and
its source coupling require a separate definition; no physical energy
law is supplied merely by that name.

## Q7. What this does and does not connect to Haar, causal volumes, and ER=EPR

Haar details can be signed orthogonal contrasts in an entirely classical
probability model. Their squared norms, stochastic selection rules, and
causal composition defects do not identify density-matrix coherence.
Equations (Q1)–(Q6) provide a declared comparator: one must specify a
tensor factorization, calibrated observables, a positive density, and
complete instruments before applying the quantum claims. The actual
BBP source has not been mapped to this instrument by renaming a Haar
coefficient as \(c\).

The existing arithmetic TFD construction supplies an explicit
mathematical entangled state and no-signalling law in its stated
normalizable domain. The present finite controls make the operational
distinctions visible, but do not authenticate that state as an observed
physical carrier. In particular, a probability vector of uncertainty
over truths is not automatically a quantum superposition of those truths.

Maldacena and Susskind's [*Cool horizons for entangled black holes*](https://arxiv.org/abs/1306.0533)
relates entangled black-hole states to Einstein–Rosen bridges and proposes
a broader ER=EPR interpretation. It does not turn an arbitrary finite
correlation matrix or an abstract arithmetic purification into a supplied
spacetime geometry. A gravitational model, state/operator dictionary,
and matching observables remain separate requirements. The original
source is cited here to delimit the analogy, not to assert a new
gravitational result.

## Implementation and actual validation

`observational_succ/haar_quantum_instruments.py` uses exact Fractions and
the inherited complete `Instrument`. It implements the specified
coherence family, product-state controls, partial traces, probability-
weighted local branches, trusted witness, rational XZ projectors, CHSH,
and the explicit shared-two-signs classical control.

Density validation is exact, using Schur complements. A positive pivot
reduces positivity to the remaining Schur complement; a zero diagonal
of a positive semidefinite matrix must have a zero residual row. This
handles singular pure states without a numerical tolerance. The negative
control includes a trace-one symmetric matrix whose every two-by-two
principal minor is nonnegative but whose larger principal block is
indefinite. Thus checking only diagonal entries or two-by-two minors
cannot accidentally pass the validator.

The implemented category is real rational matrices of size two or four,
with at most sixteen fine-grained Kraus outcomes. Complex-valued general
instruments are outside this code interface, although the displayed
no-signalling and separability proofs apply in their stated usual complex
quantum domains. Arithmetic bit costs depend on the supplied rational
sizes. No floating approximation, physical sampling, or full repository
suite is represented as part of this focused run.

Executed command:

```sh
python -m unittest tests.test_haar_quantum_instruments
```

**Actual result: 30 tests, PASS, exit code zero.** Selected internal grids:

| Control | Executed scope |
|---|---:|
| Non-signalling, complete instruments | 12 states × 7 instruments × 2 local sides = 168 cases |
| Joint-axis probabilities | 128 tables, 512 exact probabilities |
| Separable witness controls | 64 product states and 28 convex mixtures, plus saturation cases |
| Classical CHSH extrema | All 16 deterministic local tables |
| Same-data classical X/Z model | All four setting pairs |
| Signed-coherence state grid | Eight exact values, including both Bell phases and partial dephasing |
| Exact hardware-model errors | Invalid densities, incomplete instruments, impossible events, wrong branch weights, dropped normalization, duplicated axes, and erased/reversed phase all rejected |

The five inherited quantum-record tests were also run successfully before
the extension. These are exact finite implementation observations; the
universal finite-dimensional identities have their proofs above.

## Verdict ledger

| Proposed inference | Verdict |
|---|---|
| Same-basis remote conditional update certifies entanglement | **REFUTED** by the separable shared-bit control |
| Complete local quantum instrumentation preserves the unconditioned remote marginal | **DISCLOSED**, trace identity (Q6) and 168 exact controls |
| Nonzero \(c\) in the specified trusted family is entangled | **DISCLOSED**, witness and independent partial-transpose derivation |
| Restricted X/Z outcome data alone exclude all classical local response tables | **REFUTED** by the shared-two-signs construction |
| Rational rotated settings provide a discriminating CHSH model prediction | **DISCLOSED**, (Q5) and complete deterministic-table enumeration |
| Noncommuting observation/update operators alone prove a quantum mechanism | **REFUTED** by classical reset/flip kernels |
| Energy increase alone certifies truth, entanglement, or classicality | **REFUTED as a general inference**, equal-energy and energy-offset controls |
| The instrument is an authenticated physical BBP state or ER geometry | **UNVERIFIED**, no source/state/measurement or gravitational dictionary supplied |

The next empirical lamp is a calibrated source that supports the declared
independent settings and joint outcome records, with normalization,
discarded outcomes, and selection effects retained. The next arithmetic
lamp is an explicit source-preserving map from the actual SUCC/BBP
observations to these operators. Neither is supplied by a large classical
Haar coefficient or a visually suggestive geometric connection.

## Bounded review receipt for the root synthesis

**PASS within the stated mathematical domains.** Reviewed all AH-01–AH-10
in `THEOREMS.md`, with particular attention to AH-07–AH-10. The initial
reviewed SHA-256 was
`56e9ddfa3b26493d62a092ce537365fe501a9b00e37f5cdf825b0f853aa21fb3`.
After checking the corrections in the actual file, the reviewed SHA-256 is
`eb7c26b99eac112364db19a746e45e979cfc0abf98f34a29e34487586f0b9125`.

The review identified and closed the following specific defects or missing
domain guards:

- AH-04 now distinguishes an almost-surely constant report from a
  deterministic informative report. The counterexample is
  `p=1/2,a=1,b=0`: the deterministic observation `C=S` gives
  `Var(p_C)=1/4`, not zero.
- AH-02 now states that the initial posterior `p_0` is deterministic. For
  a general nontrivial initial sigma-algebra, the displayed unconditional
  identity would require expectations of `p_0^2` and `p_0(1-p_0)`.
- AH-06 now explicitly requires both positive depths for the strict
  residual-covariance claim.
- AH-08 defines normalized selected states only when `p_y>0`; its
  no-signalling sum explicitly omits zero-probability branches.
- AH-10 now supplies an initial density and complete instruments: each
  outcome map is completely positive and trace-nonincreasing, and each
  action's sum is trace-preserving. Coarsening forgets records while
  retaining the performed channels and actual adaptive feedback.

The revised fixed-probability Haar identity, structural-probe information
bounds, and option-value example are consistent. AH-05's Gram identity
uses self-adjointness in the stated inner product. Its classical controls
were also checked directly: for the symmetric path, with
`v=(1,1,-1,-1)`, `QGv=(1,-1,1,-1)/7` gives `D=vv^T/196`. For the
directed cycle, `G=(8I+4S+2S^2+S^3)/15`, `S^2v=-v`, and `PSv=0` give
`Dv=-v/25`, hence `D=-vv^T/100`. The reversibility boundary is genuine.
The original-source derivative, rational-tail, coefficient-energy, and
residual bounds in AH-06 were rederived without substituting a different
source.

AH-07 correctly separates a trusted orthogonal-qubit witness from a
device-independent claim; the shared-two-signs control reproduces every
restricted X/Z setting-pair table. AH-08's trace proof distinguishes
postselection from unconditioned signalling. AH-09 preserves the rational
CHSH sign convention and its physical interpretation assumptions. AH-10
keeps the observer's posterior, persistent target, and post-intervention
carrier distinct, and does not identify the arithmetic model with a
physical BBP quantum state or a gravitational dual.

This is a bounded proof-and-scope audit against the supplied definitions
and exact instrument controls. It is not a new physical observation,
an independent source family, a formal proof-assistant certificate, or a
full repository-suite receipt. No new test run is claimed for this prose
review; the actual focused implementation result remains the 30-test
PASS recorded above. The mathematical review does not depend on treating
the then-in-progress `PROVENANCE.md` link as an already verified artifact.

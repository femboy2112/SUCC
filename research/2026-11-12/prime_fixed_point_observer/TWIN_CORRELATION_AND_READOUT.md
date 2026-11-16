# Twin correlation, calibrated current outputs, and deferred readout

Parent: `7622063945ab06c72b092371747a1a5bbbf35e3a`.
Status: classical finite quantum-information identities, elementary
PROVED LOCAL consequences, and exact rational controls. A physical
realization and an objective collapse law remain UNVERIFIED.

## 0. The meeting interface is a present output

The user requires direct comparison of the observers' **current outputs**
at their meeting. Their histories occupy different frames and are not
directly comparable. Nothing below gives the comparator automatic access
to those histories. An observer may retain branch information internally
while exposing only a chosen current output. Those are different resources.

For every diagnostic below, specify which present quantity is supplied,
its input/output spaces, its basis or frame transport, and what target it
can separate. A complete finite matrix diagnostic is an optional richer
present output; it must actually be implemented or supplied. Agreement of
two scalar outputs does not silently become that diagnostic.

For example, if the observers' current maps are `A` and `B` in different
frames, first form common-frame maps

\[
\widetilde A=L_{\rm out} A L_{\rm in}^{-1},\qquad
\widetilde B=R_{\rm out} B R_{\rm in}^{-1}.
\]

Every inverse and type in this display is a hypothesis. Compare these maps
only after the frame maps have been established. The finite formulas below
use `A,B` for the already calibrated maps. Nonunitary frame changes also
require transported inner products if a norm is to retain its meaning.

## 1. A finite twin can encode a complete current linear diagnostic

Fix `H=C^d`, `d>=1`, and a common orthonormal basis `e_0,...,e_(d-1)`.
Let

\[
\Phi_d=d^{-1/2}\sum_{j=0}^{d-1}e_j\otimes e_j.
\]

**TCR-01 — CLASSICAL vectorization, PROVED LOCAL diagnostic.** For every
`A,B` in `End(H)`,

\[
(A\otimes I)\Phi_d=(I\otimes A^{\mathsf T})\Phi_d,
\qquad
\Delta(A,B)=(A\otimes I-I\otimes B^{\mathsf T})\Phi_d,
\]

and

\[
\boxed{\|\Delta(A,B)\|^2=\frac1d\sum_{i,j}|A_{ij}-B_{ij}|^2
=\frac1d\|A-B\|_F^2.}
\]

**Proof.** The coefficient of `e_i tensor e_j` in the left action is
`A_ij/sqrt(d)`. It is the same coefficient in the transpose action.
Subtracting gives `(A_ij-B_ij)/sqrt(d)`; the tensor basis is orthonormal,
so its squared coefficient sum is the stated norm. Exact vanishing is
equivalent to equality of all matrix entries. This tests every declared
input direction, rather than just the earlier common root.

The convention is the standard vectorization convention: see Watrous,
[*The Theory of Quantum Information*, Chapter 1, p24,
equations (1.131)–(1.132)](https://jhwatrous.github.io/TQI.1.pdf).
Transpose depends on the declared basis. Replacing it by adjoint changes
the comparison. It is not supplied by spatially opposing the observers.

The algebra allows arbitrary linear `A,B`. An arbitrary matrix is not a
deterministic quantum operation on state vectors. A quantum reading needs
an isometry/unitary or a specified instrument with its success records;
the arithmetic return's rejected branches cannot be silently normalized
away. A classical implementation can instead compute the diagnostic from
explicit current matrix descriptions, with the corresponding data cost.

## 2. Matched evolution requires conjugate transport

**TCR-02 — PROVED LOCAL.** For unitary `U`,

\[
\boxed{(U\otimes\overline U)\Phi_d=\Phi_d.}
\]

The coefficient sum is `sum_j U_ij conjugate(U_kj)=delta_ik`, proving
the result. These twins have a specified relation between their transports.
The prescription uses separately defined unitary matrices; it is not an
operation that conjugates an arbitrary unknown physical state.

Using the same matrix on both sides gives `(U tensor U)Phi_d`, which
need not equal the initial twin. The exact two-dimensional witness is

\[
U=\operatorname{diag}(1,i),\qquad
(U\otimes U)\Phi_2=(e_0e_0-e_1e_1)/\sqrt2.
\]

Its inner product with the original twin is zero. Two individually
unitary evolutions preserve total norm without preserving their original
correlation pattern. Conjugate transport is therefore a real condition.

Entanglement also does not force equal outcomes for arbitrary readouts.
For `Phi_2`, measuring both qubits in the standard `Z` basis produces
`00` or `11`, each with probability `1/2`. Measuring the first in `Z`
and the second in the `X` basis produces all four pairs with probability
`1/4`. Expand `e_0=(e_++e_-)/sqrt2` and
`e_1=(e_+-e_-)/sqrt2` to verify this directly. The chosen present
measurements, not the label "twins", specify the agreement question.

## 3. A mathematical equality diagnostic is not a single-shot oracle

**TCR-03 — PROVED LOCAL boundary.** Literal vector equality and physical
pure-state equality have different phase conventions. `psi` and
`exp(i theta) psi` have identical density matrix `psi psi*`. In particular,
`A` and `-A` are different matrices but induce the same unitary channel
`rho -> A rho A*`. Their vector diagnostic can be nonzero although their
separately prepared output states are physically indistinguishable.

Literal matrix equality requires a declared common phase reference or a
controlled implementation in which the phase becomes relative. Otherwise
the relevant target is equality of rays or channels. The mathematical
diagnostic must state which target it uses.

Even for different rays, one accepted comparison outcome need not prove
equality. Let `S` swap the two supplied current pure states. The symmetric
projector is `P_+=(I+S)/2`. For normalized `u,v`,

\[
\langle u\otimes v,P_+(u\otimes v)\rangle
=\frac{1+|\langle u,v\rangle|^2}{2}.
\]

This follows because `S(u tensor v)=v tensor u`. For
`u=e_0`, `v=(3e_0+4e_1)/5`, the states differ but acceptance has
probability `17/25`. A rejected symmetric test is a witness of difference;
an accepted one is not an exact equality certificate. The Holevo–Helstrom
measurement bound supplies the general finite-state discrimination
framework; see Watrous, [Chapter 3, p128, Theorem 3.4](https://jhwatrous.github.io/TQI.3.pdf).

Thus a symbolic proof that `Delta=0`, an exact calculation from supplied
classical maps, and a finite series of physical measurement outcomes have
different evidential scopes. Neither the twin preparation nor the meeting
converts the latter into a proof about every infinite arithmetic input.

## 4. A designated readout can be postponed

Let a finite instrument have operators `M_j:H->K`, with
`sum_j M_j* M_j=I`. Introduce an orthonormal record register `|j>` and
define

\[
W\psi=\sum_j M_j\psi\otimes|j\rangle.
\]

**TCR-04 — CLASSICAL dilation, explicit local proof.** `W*W=I` because
distinct record labels are orthogonal. The probability of a final record
readout `j` is `||M_j psi||^2`, exactly the instrument probability.
In finite dimensions, this isometry can be implemented as a unitary on
an enlarged space with a fixed initial ancillary state, by completing
orthonormal bases. The source is Watrous, [Chapter 2, p89, Corollary 2.27
and p109, Theorem 2.42](https://jhwatrous.github.io/TQI.2.pdf).

If a later operation is selected by the record, replace the classical
choice with the corresponding coherent controlled operation. Retaining
every record until the final chosen measurement reproduces the original
final outcome probabilities. For a finite sequence this follows by
induction over its branches: each branch retains the same ordered product
of instrument operators and its own orthogonal record. This requires
the corresponding controls and record storage; it does not remove them.

For the computational-basis projectors `P_0,P_1` and a block-controlled
unitary `C=P_0 tensor U_0+P_1 tensor U_1`, the elementary identity is

\[
C\left(\sum_j P_j\rho P_j\right)C^*
=\sum_j P_j C\rho C^*P_j.
\]

Here each `P_j` on the compound system means `P_j tensor I`.
Commutation `CP_j=P_jC` proves the equality. Arbitrarily changing the
measurement basis or controlled operation invalidates this argument.
The probe checks actual final reported density matrices, not an assumed
equality of inaccessible past records.

This realizes a **readout schedule**: no designated record is measured
until the meeting. It does not establish when an objective physical
collapse occurs, or require treating all internal observer processing
as classical information before that time.

## 5. A globally retained branch can already disappear from a local output

Take a two-level system and an environment initially in `|0>`. A CNOT
interaction gives

\[
(\alpha|0\rangle+\beta|1\rangle)|0\rangle_E
\longmapsto
\alpha|0\rangle|0\rangle_E+\beta|1\rangle|1\rangle_E.
\]

**TCR-05 — PROVED LOCAL countercontrol.** The compound state remains
pure and its evolution is unitary. If the present output accesses only
the system, its reduced density matrix is

\[
\rho_S=|\alpha|^2|0\rangle\langle0|
+|\beta|^2|1\rangle\langle1|.
\]

The cross terms vanish because the environment records are orthogonal.
For `alpha=3/5`, `beta=4/5`, the system's off-diagonal entry changes
from `12/25` to zero before any meeting. The joint state still contains
the phase information: applying the same CNOT again restores the input.
This restoration requires control of that environment; it is not available
to a comparator restricted to the reduced current output.

More generally, normalized environment records `u_0,u_1` multiply the
`|0><1|` cross term by `inner(u_1,u_0)`. Equal records retain it,
orthogonal records erase it from the subsystem, and intermediate overlap
gives partial suppression. The reduced-state operation is the partial
trace; [IBM Quantum's official account](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/density-matrices/multiple-systems)
states this subsystem convention. The calculation here fixes the actual
records and present output explicitly.

The construction consequently supports lossless **global** transport and
a postponed designated readout. Preserving a specific **local** coherent
output additionally requires isolation, a suitable protected encoding,
or accessible recovery. Enlarging the mathematical universe alone does
not grant that recovery to an observer. Destructive interference, a reduced
state, conditional measurement update, and objective collapse are separate
operations or claims.

## 6. Infinite twins: separation survives, uniform conditioning does not

On `H=l2(N_0)`, the formal uniform diagonal sum has squared norm
`sum_j 1=infinity`. No nonzero constant normalization makes it a Hilbert
vector. Instead choose `w_j>0`, `sum_j w_j=1`, and put

\[
\Omega_w=\sum_{j\ge0}\sqrt{w_j}\,\varepsilon_j\otimes\varepsilon_j.
\]

**TCR-06 — PROVED LOCAL.** For bounded operators `A,B`,

\[
\|((A-B)\otimes I)\Omega_w\|^2
=\sum_j w_j\|(A-B)\varepsilon_j\|^2.
\]

The sum converges, bounded by `||A-B||^2`. Orthogonality in the second
register proves the identity by finite partial sums and continuity.
If it is zero, every nonnegative term is zero; all columns agree, so
boundedness and density give `A=B`.

This is an exact separating **mathematical current diagnostic**, but not
a stable uniform operator-norm test. Set
`A=I`, `B=I-2|epsilon_N><epsilon_N|`. Both are unitary,
`||A-B||=2`, and the squared diagnostic is `4w_N -> 0`.
If a finite twin omits index `N`, the same defect is completely invisible.
A full-support infinite state therefore does not turn finite-precision
readout into a proof of full operator equality.

There is a further transport issue. Writing `D epsilon_j=sqrt(w_j)
epsilon_j`, the formal opposite-side transpose partner is

\[
M=D A^{\mathsf T}D^{-1},\qquad
(A\otimes I)\Omega_w=(I\otimes M)\Omega_w,
\]

whenever the right-hand side and its operator domain are legitimate. In
finite dimensions all positive weights make `D` invertible. In infinite
dimensions `D^{-1}` is unbounded; the resulting `M` need not extend to a
bounded operator.

**TCR-07 — PROVED LOCAL domain obstruction.** Choose
`w_j=c 4^(-j^2)`, with the positive constant `c` normalizing the summable
sequence, and let `A=S`, the bounded successor `S epsilon_j=epsilon_(j+1)`.
On finite basis vectors the required partner acts as

\[
M\varepsilon_0=0,\qquad
M\varepsilon_j=2^{2j-1}\varepsilon_{j-1}\quad(j\ge1).
\]

The coefficients follow from `sqrt(w_(j-1)/w_j)` and tend to infinity.
No bounded `M` can have this action. Thus the well-defined same-side
weighted diagnostic does not automatically provide a bounded
opposite-side implementation for every bounded arithmetic operator.
The exact current diagnostic and the proposed observer transport remain
distinct design obligations.

## 7. Verdict and reproducible scope

| Claim | Status | Exact boundary |
| --- | --- | --- |
| TCR-01 | CLASSICAL / PROVED LOCAL | Finite complete current matrix output in a declared basis; transpose, not adjoint. |
| TCR-02 | PROVED LOCAL | Conjugate unitary pairing; arbitrary same transports or readout bases fail. |
| TCR-03 | PROVED LOCAL | Phase convention matters; one accepted physical comparison is not an equality proof. |
| TCR-04 | CLASSICAL / PROVED LOCAL | Finite instrument, coherent controls and retained records; a chosen readout schedule. |
| TCR-05 | PROVED LOCAL | Global unitarity permits earlier loss of local coherence; recovery requires the environment. |
| TCR-06 | PROVED LOCAL | Infinite positive weights separate bounded operators exactly, without uniform conditioning. |
| TCR-07 | PROVED LOCAL | A weighted opposite-side partner can be unbounded. |
| Objective physical collapse occurs only at meeting | UNVERIFIED | No physical collapse model or decisive physical test is supplied. |

`twin_correlation_probe.py` uses exact Gaussian rationals and deliberately
keeps conjugation distinct from transpose. Its tensor computations are
compared with direct column formulas; phase, different-basis, environment,
measurement and finite-support mutations provide negative controls.
Its finite weighted-shift identities accompany the infinite analytic proof
above rather than replacing it. The root records the actual execution
receipt and check count separately.

The useful next construction selects a present arithmetic output, derives
its common-frame transport, and proves the separation/error bound for the
declared input class. Twin agreement supplies neither an independent source
authentication nor an arithmetic remainder estimate by itself.

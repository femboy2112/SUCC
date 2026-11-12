# Twin observers: present outputs, transported frames, and a lossless carrier

**Parent:** `7622063945ab06c72b092371747a1a5bbbf35e3a`.
**Status:** classical constructions and elementary PROVED LOCAL statements
with exact finite controls. A physical implementation and a new arithmetic
asymptotic estimate are not established.

The proposal is to place correlated observers at opposed boundaries of a
larger carrier and bring them to a meeting event. The user's refinement is
essential: compare their **current model outputs** there. Their raw histories
come from different patches and are not directly interchangeable. Any use of
a past observation needs its event, type, frame, and a justified transport.

The result is a conditional construction: reversible transport preserves a
disagreement rather than erasing it; a declared current observation decides
which disagreements can be detected. Agreement becomes a theorem when the
source interpretation, transport and observation hypotheses are supplied.
Entanglement or common ancestry alone does not supply those hypotheses.

The [registered contract](TWIN_OBSERVER_CONTRACT.md) records the proposal and
later refinement. This note connects the existing arithmetic returns to that
contract. Companion derivations and finite programs are listed at the end.

## 1. What is actually compared at the meeting

Let `m` denote one meeting event, not necessarily a geometric midpoint.
Observer `o` has a current internal model `M_o(m)` and publishes a declared
output in its local output type `W_(o,m)`. A calibration map identifies that
type with the common meeting output space `W_m`:

\[
y_o(m)=C_{o,m}\,\operatorname{Out}_{o,m}(M_o(m))\in W_m,
\qquad \Delta_m=y_L(m)-y_R(m).
\]

For nonlinear or set-valued outputs replace subtraction by equality in the
declared common type. The comparator receives only these present outputs.
It does not receive either full history. Internal memory may affect a model's
current prediction without becoming a directly compared historical record.

Even at one event, different units, bases, orientations or output schemas need
calibration. Conversely, numerically equal coordinates at different events
need not describe equal quantities. A coordinate change must not be mistaken
for physical evolution. Re-expressing an old observation in a new frame does
not turn it into a new observation of the present state.

If a historical record at `p` is used to predict an output at `m`, specify the
represented quantity and the model that transports it. The simple linear
case has `x_p in V_p`, a path `gamma:p->m`, and a declared map

\[
T_\gamma:V_p\longrightarrow V_m,\qquad
y_m=O_mT_\gamma x_p.
\]

Here `T_gamma` includes whatever evolution or comparison of quantities the
model actually asserts. A change of basis changes its coordinates; it does
not justify that evolution. For partial observations, a set of compatible
states or a conditional model may be required instead of one vector.

The base patches in this construction are an abstract graph/category. No
Lorentz metric, proper-time law, curvature of physical spacetime, or access
to spacelike records is inferred from that abstraction.

## 2. A precise frame-differential law

**TWIN-01 — PROVED LOCAL, frame covariance of the present readout.**
Give every patch an invertible coordinate change `G_p`. Set

\[
x'_p=G_px_p,\qquad
T'_\gamma=G_mT_\gamma G_p^{-1},\qquad
O'_m=O_mG_m^{-1}.
\]

Then the calibrated output is unchanged:

\[
\boxed{O'_mT'_\gamma x'_p=O_mT_\gamma x_p.}
\]

**Proof:** substitute the definitions and cancel the adjacent inverse pairs.
For a path, the intermediate frame changes cancel in the same manner.
This is the elementary graph-connection transformation law; see Kenyon,
[*Spanning forests and the vector bundle Laplacian*, Section 3.1](https://arxiv.org/pdf/1001.4028).

If the compared output is the vector in `V_m` itself, its coordinate
residual transforms as `Delta'_m=G_m Delta_m`. Zero residual is invariant.
Its ordinary Euclidean norm is invariant only for unitary `G_m`. For a
general basis change, transport the positive metric too:

\[
h'_m=(G_m^{-1})^*h_mG_m^{-1},\qquad
(\Delta'_m)^*h'_m\Delta'_m=\Delta_m^*h_m\Delta_m.
\]

For example, `(1,2)` and `(2,1)` are coordinates of the same vector if the
second frame exchanges the axes. Raw equality would fail. Conversely two
records both written `(1,2)` can represent different vectors under those
two frames. Scaling the first coordinate by 2 changes the coordinate norm
of `(1,0)` from 1 to 4 squared; the transformed metric has first diagonal
entry `1/4`, restoring the original squared length 1.

Calibration makes the comparison well typed. It does not imply that values
measured at different events must agree.

## 3. Paths retain their differential: holonomy

Suppose two invertible transports `T_gamma,T_eta:V_p->V_m` use different
routes. Define their relative return at the source by

\[
H_{\eta,\gamma}=T_\eta^{-1}T_\gamma:V_p\longrightarrow V_p.
\]

**TWIN-02 — PROVED LOCAL.** The full transported vectors agree for a record
`x` exactly when `H_(eta,gamma)x=x`. They agree for every input exactly when
`H_(eta,gamma)=I`. Under frame changes this operator becomes
`G_p H_(eta,gamma) G_p^-1`. The existence of a defect is therefore not
removed by renaming the frames.

After a noninjective current readout `O_m`, the weaker condition is only

\[
O_m(T_\gamma-T_\eta)x=0.
\]

It can hold while the transported states differ. For example, routes `I`
and `diag(1,-1)` agree on the common root `e_0` and on the readout of the
first coordinate. They disagree on `e_1` by `2e_1`. This is a permitted
current-output equality, not evidence of identical hidden states or paths.

Thus histories can be evaluated in a common frame when their transports
are given, but cannot be directly equated. Path independence must be proved
on the relevant states or observations. It is not part of the word frame.

## 4. Two observers really can walk toward a common cut

Consider a finite typed chain of Hilbert spaces and bounded maps

\[
H_0\xrightarrow{A_1}H_1\xrightarrow{A_2}\cdots
\xrightarrow{A_N}H_N.
\]

For left boundary state `a` and right boundary test vector `b`, define

\[
\ell_k=A_k\cdots A_1a,\qquad
r_k=A_{k+1}^*\cdots A_N^*b.
\]

Empty products are identities. At cut `k` both are in `H_k`; the right
observer has transported a **dual test** using adjoints. This is not an
inverse walk through a noninjective map, and not a raw history comparison.
Each choice of cut describes a possible present meeting protocol. The
theorem does not grant the observers access to outputs at other events.

**TWIN-03 — PROVED LOCAL, cut-independent pairing.** For every cut,

\[
\boxed{\langle r_k,\ell_k\rangle
=\langle b,A_N\cdots A_1a\rangle.}
\]

**Proof:** use the defining adjoint identity at each crossed edge. No
invertibility or probability interpretation is needed. This scalar can be
the declared current output of a comparison protocol. One scalar cannot
identify an arbitrary operator or internal model.

There is a stronger statement when all `A_j=U_j` are unitary. Then the
adjoint is a genuine inverse, and applying the remaining unitary suffix
to `ell_k-r_k` proves

\[
\boxed{\|\ell_k-r_k\|
=\|U_N\cdots U_1a-b\|\quad(0\le k\le N).}
\]

For a complete current vector output, agreement at one cut is equivalent
to the boundary condition `b=U_N...U_1a`, and then agreement holds at every
cut. Reversible walking cannot hide an inconsistent boundary preparation.
If the right boundary was defined by that very equation, the equality is a
consistency identity, not independent evidence that the source is correct.

Under a coarse output `O_k`, only `O_k(ell_k-r_k)` is compared; the full
norm theorem does not license inspecting unreported components. The code
and derivation distinguish these two protocols.

Nonunitary maps expose the need for the larger carrier. With
`A=diag(1,0)`, `a=e_1`, `b=0`, the two current states disagree before `A`
but agree as zero after it. This is agreement by information loss. The
pairing identity still holds, showing why pairing alone is not equality.

## 5. The larger carrier for our arithmetic returns is explicit

The current arithmetic operator is

\[
T=T_{q,r}=D_rD_q^*,\qquad D_d\varepsilon_k=\varepsilon_{dk},
\quad q>r\ge1,\quad \gcd(q,r)=1,
\]

on `H=l2(N_0)`. It sends `epsilon_(qk)` to `epsilon_(rk)` and rejects
other basis labels. Define the initial and final projections

\[
P_q=T^*T=D_qD_q^*,\qquad P_r=TT^*=D_rD_r^*.
\]

**TWIN-04 — PROVED LOCAL, information-preserving extension.** On `H+H`,

\[
\boxed{\mathbb U_T=
\begin{pmatrix}
T&I-P_r\\
I-P_q&-T^*
\end{pmatrix}}
\]

is unitary and

\[
\mathbb U_T(x,0)=(Tx,(I-P_q)x),\qquad
\|Tx\|^2+\|(I-P_q)x\|^2=\|x\|^2.
\]

**Proof:** `T(I-P_q)=0`, `(I-P_r)T=0`, and their adjoints make the
off-diagonal blocks in both `U*U` and `UU*` vanish. The diagonal blocks
are `P_q+(I-P_q)=I` or `P_r+(I-P_r)=I`. This is the partial-isometry
instance of the classical Halmos extension; see Robinson,
[*Julia operators and Halmos dilations*, Theorem 2](https://arxiv.org/pdf/1803.09329).

For `T_(3,2)`, `epsilon_3` becomes `(epsilon_2,0)`, while `epsilon_1`
becomes `(0,epsilon_1)`. A rejected input is retained in the second channel.
The full dynamics is reversible. The first component alone remains the
original lossy arithmetic operation.

This is a concrete mathematical version of the surrounding carrier the
user proposed. The enlarged state and its branch records need not be
observable to the meeting comparator. Reversible internal transport and a
coarse current output are compatible but have different information content.

### A repeated walk needs an honest memory protocol

The two-block extension is a **one-step compression**. Reusing its one
environment block is not generally a power dilation of `T`:

\[
\pi_0\mathbb U_{3,2}^{\,2}(\varepsilon_1,0)
=\varepsilon_1,
\qquad T_{3,2}^{\,2}\varepsilon_1=0.
\]

For a finite sequence, add a fresh two-state record at each step and use
the isometry

\[
V_Tx=Tx\otimes|0\rangle+(I-P_q)x\otimes|1\rangle.
\]

Keep the old records. Induction preserves norm and the all-zero record
sector equals the original product `T_N...T_1 x`. Inspecting only that
sector is a later projection/postselection; it is not the full lossless
evolution. The memory is charged as part of the larger system. The
comparison protocol still uses only its declared present outputs.

### A dilation is not automatically a functorial equivalence

If an isometric embedding `J` satisfied `U J=J T` for a unitary `U`, then
`||Tx||=||x||` for every `x`, which fails for a rejected input. Our valid
identity is the compression `J* U J=T`, not invariant-subspace intertwining.

Likewise, an idempotent unitary must be the identity. A nontrivial
projection cannot retain its idempotence relation as a distinct unitary
generator. Independently extending generators therefore does not ensure
that every quotient relation among the compressed arithmetic maps also
holds upstairs. The larger path-and-record construction must retain the
relations it actually satisfies. This matches the earlier distinction
between a literal history and its semantic operation.

## 6. Comparing complete current models needs a separating output

Agreement is relative to `Out`. If `Out(x)=Out(x')`, then the output alone
can determine a target `tau` exactly only if `tau(x)=tau(x')`. Conversely,
if `tau` is constant on each output fiber, define its decoder on the image
by choosing any representative; the value is well-defined. This proves the
necessary and sufficient information condition.

For a finite-dimensional linear model with square maps
`A,B in End(C^d)`, one possible **declared present diagnostic** compares
all input directions via

\[
|\Phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|j\rangle|j\rangle,
\quad
\Delta(A,B)=(A\otimes I-I\otimes B^{\mathsf T})|\Phi_d\rangle.
\]

Both models are first expressed in the same orthonormal meeting basis;
the transpose transport is explicit. Expanding the sum gives

\[
\boxed{\|\Delta(A,B)\|^2=d^{-1}\|A-B\|_F^2.}
\]

Thus this mathematical current output is separating: its exact zero
certifies `A=B`. A pair of single scalar outputs or the shared root is not
this diagnostic. Nor does one physical outcome supply the exact vector
or its norm. A phase reference is required when literal matrix equality,
rather than equality of quantum channels, is the target. Details and
measurement controls are in [TWIN_CORRELATION_AND_READOUT.md](TWIN_CORRELATION_AND_READOUT.md).

For our returns, `T_(5,1)` and `T_(5,2)` agree on the root and on every
input index below 5. At index 5 they output `epsilon_1` and `epsilon_2`.
For the input window `0,...,5`, with all these outputs retained, the
normalized squared twin defect is exactly `2/6=1/3`. A root-only output
or an input window `0,...,4` misses it entirely.

## 7. Agreement of model outputs versus compatibility of models

To compare two whole categorical models, let `F,G:C->Vect` be actual
representations and let `eta_c:F(c)->G(c)` be declared frame/type
identifications. The compatibility condition on an arrow `e:c->d` is

\[
\eta_dF(e)=G(e)\eta_c.
\]

**TWIN-05 — PROVED LOCAL, generator test.** If `C` is generated by a set
of arrows, these identities on every generator imply the identities on
every finite path, by multiplication. Invertible `eta_c` then give a
natural isomorphism. If only one assignment is already known to satisfy
the category's relations, invertible generator intertwiners transfer
those relations to the other by conjugacy.

If neither side is known to be a representation, identical twins can
violate the same relation. Assigning `diag(1,2)` to a declared involution
gives identical assignments with a shared root, but its square is
`diag(1,4)`, not identity. Source authentication and relation validity
are separate from inter-observer agreement.

There is a useful quantitative version. Put
`delta_j=eta_j F_j-G_j eta_(j-1)`. A telescoping expansion proves

\[
\eta_N F_N\cdots F_1-G_N\cdots G_1\eta_0
=\sum_{j=1}^{N}G_N\cdots G_{j+1}\,\delta_j\,
F_{j-1}\cdots F_1.
\]

If both representations' edge operators are contractions in their
declared metrics, the operator norm of the defect is at most
`sum_j ||delta_j||`. Every term has the correct intermediate type.
A current-output bound may be obtained by applying the current readout
to this identity. This is a proved error budget for frame-compatible
composition, not permission to compare untransported historical data.

The defect also reconnects to the original commutator proposal. On one
space with one comparison map `eta`, if `F(e)=G(e)=A`, the defect is
`eta A-A eta=[eta,A]`. For the common-root projection `E_0`, every proper
return has zero such defect. Successor instead has
`[E_0,S]=-|epsilon_1><epsilon_0|`. The comparison is therefore relative to
the actual dynamics being tested. A fixed reference that ignores this
successor defect cannot authenticate the whole arithmetic system.

A concrete pair of frames is already available in this dossier:
`U: l2(N_0)->H2`, `Ux(z)=sum_k x_k z^k`. The coefficient observer uses
`T_(q,r)`; the analytic observer uses
`T_hat f(z)=sum_k x_(qk) z^(rk)`. The previously proved identity
`U T_(q,r)=T_hat U` supplies their generator intertwiner. At the meeting,
the current output `x_N` agrees with the analytic output `[z^N]f` when
the present models satisfy `f=Ux`. This is a faithful translation theorem,
not equality of their earlier observations or a new primality estimate.
An interior analytic measurement of that coefficient still pays the
`rho^-N` conditioning cost from [COMMON_ROOT_AND_LIMITS.md](COMMON_ROOT_AND_LIMITS.md).

The categorical definitions are classical; see Riehl,
[*Category Theory in Context*, Sections 1.4 and 3.1](https://emilyriehl.github.io/files/context.pdf).
The [separate audit](reviews/twin_observer_adversarial_audit.md) also states
the exact gluing condition: the canonical map from genuine global models
to the pullback of compatible local models must reach the matched pair;
uniqueness requires a singleton fiber. Equality at an interface alone
establishes neither condition.
If both reports are already certified faithful to the same actual source,
that source supplies existence for the observed pair. Surjectivity onto
the entire pullback is only needed to guarantee existence for every
compatible candidate pair, not for that already realized pair.

## 8. The infinite carrier has no uniform finite twin

The formal sum `sum_(j>=0) epsilon_j tensor epsilon_j` has infinite
squared norm. It is not a normalized state in the ordinary Hilbert tensor
product. Finite-dimensional compact duality uses an unnormalized cup of
squared norm `d`; its normalized physical version has different scalar
normalization in the snake identity. One cannot silently pass that cup to
infinite dimension. Abramsky and Coecke's
[*A categorical semantics of quantum protocols*, Sections 3 and 7](https://arxiv.org/pdf/quant-ph/0402130)
states the finite-dimensional setting explicitly.

A legitimate replacement has strictly positive summable weights:

\[
|\Omega_w\rangle=\sum_{j\ge0}\sqrt{w_j}\,
\varepsilon_j\otimes\varepsilon_j,
\qquad w_j>0,\quad\sum_jw_j=1.
\]

For bounded `A,B`, orthogonality in the second register gives

\[
d_w(A,B)^2=\|((A-B)\otimes I)\Omega_w\|^2
=\sum_{j\ge0}w_j\|(A-B)\varepsilon_j\|^2.
\]

**TWIN-06 — PROVED LOCAL, separating but nonuniform.** Exact zero implies
`A=B`, since every basis column vanishes and bounded operators agree on
the dense finite span. But no uniform operator-norm stability follows.
For `A=I`, `B=I-2|epsilon_N><epsilon_N|`, both are unitary and

\[
\|A-B\|=2,\qquad d_w(A,B)^2=4w_N\longrightarrow0.
\]

Finite-support twins can miss this defect exactly. Full-support twins
only make it small; an exact infinite zero still requires a proof or an
adequate observation interface, not a finite number of samples.

For a finite input projection `P_D` onto indices `0,...,D-1`, `D>=1`, let
`w_min(D)=min_(j<D) w_j`. There is a valid quantitative bridge:

\[
\|(A-B)P_D\|\le\frac{d_w(A,B)}{\sqrt{w_{\min}(D)}},
\]

because operator norm is bounded by the column Hilbert-Schmidt norm.
For any input `x`, splitting it into this window and its tail gives

\[
\|(A-B)x\|\le
\frac{d_w(A,B)}{\sqrt{w_{\min}(D)}}\|P_Dx\|
+(\|A\|+\|B\|)\|(I-P_D)x\|.
\]

With geometric weights `w_j=2^(-j-1)`, the prefix condition factor is
`2^(D/2)`. An independently justified tail bound makes this useful for
a declared input class. It does not furnish uniform accuracy on all
arithmetic states for free. This extends the earlier Hardy conditioning
lesson to a present twin-comparison interface.

The weighted diagnostic above compares two outputs on the same tensor
side. Moving an arbitrary operator to the opposite side is an additional
condition. With `D epsilon_j=sqrt(w_j) epsilon_j`, the formal partner is
`D A^T D^-1`, which need not extend to a bounded operator. For
`w_j=c 4^(-j^2)` and `A=S`, it sends `epsilon_j` to
`2^(2j-1) epsilon_(j-1)` for `j>=1`. Thus an admissible weighted twin does
not automatically supply a bounded opposite observer for every bounded
source dynamic. The companion proves and tests this counterexample.

The standard infinite cylinder also has no finite endpoint at infinity from which
an ordinary finite-speed walk starts. Work on every finite segment,
or specify boundary data and prove an appropriate limit with an error
bound. The two-sided finite theorem does not assert an infinite elapsed
journey or a finite meeting after traversing infinitely many unit steps.

## 9. What can happen only at the meeting

The protocol can defer its **designated readout** to the meeting while
keeping the full state evolution isometric. That supplies a mathematical
meaning for withholding irreversible selection until comparison.

It does not show that local coherence necessarily survives all earlier
interactions. If a path label becomes correlated with an inaccessible
environment, discarding that environment removes local cross terms even
while the total state remains pure. The companion gives an exact two-qubit
example, its unitary undoing, and current-output consequences.

Destructive interference is also not identical to measurement: a unitary
can cancel an amplitude in one channel and transfer norm elsewhere. A
mathematical model reconciliation, a conditional measurement update, local
decoherence and objective physical collapse are different statements.
This construction derives no unique physical collapse mechanism or timing.

The useful conditional claim is therefore:

> Retain all information required by the chosen current diagnostic in the
> accessible larger carrier, transport the representations with explicit
> frame maps, and perform that diagnostic at the common meeting event.

Its result is agreement within the diagnostic's separating power, together
with whatever source and compatibility proofs have actually been supplied.

## 10. Provenance, verdict, and executable scope

The October [twin-frame note](../../2026-10-11/TWIN_OBSERVER_FIELD_INVARIANCE.md)
already proved conditional semantic agreement under faithful translation
and shared interpreted evidence. The October
[dual-boundary note](../../2026-10-12/DUAL_BOUNDARY_OBSERVER_CORRELATION.md)
already distinguished source identity, marginals, information and gluing,
including potential-plus-flux matching and a nontrivial transition law.
Those files are reused unchanged. This continuation adds the explicit
arithmetic lossless extension, present-frame constraints, exact twin-map
diagnostic and its infinite-conditioning boundary.

| Claim | Earned status | Boundary |
| --- | --- | --- |
| TWIN-01 | PROVED LOCAL | Calibrated current output is gauge invariant; the dynamical model still needs justification. |
| TWIN-02 | PROVED LOCAL | Path agreement is holonomy fixed-space or readout-kernel dependent. |
| TWIN-03 | PROVED LOCAL | All finite cuts; vector discrepancy needs unitaries and a vector-output protocol. |
| TWIN-04 | CLASSICAL extension, PROVED LOCAL arithmetic realization | One-step compression; fresh records for products; no automatic quotient-functor lift. |
| TWIN-05 | CLASSICAL naturality, PROVED LOCAL telescoping bound | Actual relations, all generators, and correct norms/types required. |
| TWIN-06 | PROVED LOCAL | Weighted infinite diagnostic is separating but ill-conditioned. |
| Automatic agreement from twins or meeting alone | REFUTED | Mismatched boundaries, shared invalid relation, coarse-output and source controls. |
| Physical collapse occurs only at meeting | UNVERIFIED as a physical claim | A readout schedule is constructible; isolation/recoverability is additional. |

The exact finite controls are `twin_transport_probe.py`,
`twin_seam_probe.py`, `twin_gluing_probe.py`, and
`twin_correlation_probe.py`. The transport implementation has dedicated
tests. Universal statements rely on the displayed proofs, not finite
check counts. Same-model audits are not independent peer review.

**Verdict:** a genuine construction step for the requested architecture,
and a refutation of unconditional agreement. The immediate useful target
is an explicit current arithmetic output, a source-faithful frame transport,
and a separating/error theorem for that output. The open prime-pair
remainder estimate, Goldbach, pi normality and RH are unchanged.

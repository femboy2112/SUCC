# One carrier bond and two internal twins: an exact finite dictionary

**Date:** 2026-11-12. **Status:** classical finite tensor identities and
elementary PROVED LOCAL specializations to the arithmetic code.
**Continuation:** the coherent-path work from published parent
`e9639c0ddb07385c6000b670d26cf0f7b91dacaa`.

## 0. Faithful reading and precise scope

The new proposal describes two observers internally and one connecting
carrier structure externally. A precise finite realization is available:
two encoded endpoint spaces joined by one entanglement tensor. Replacing
the internal tensor by its external encoded state preserves every specified
present observable contraction. The endpoint encodings and transports are
actual maps, so this is more than a picture with two labels.

Calling the endpoint insertions carrier defects or the bond a wormhole is
a declared interpretation of this finite model. The construction below
does not supply a gravitational metric, an Einstein--Rosen solution, causal
traversability, a freely shared changing memory, or a physical realization.
An entangled state and a signaling channel have different operational data.

The October sources already established the relevant boundaries:

* [Arithmetic thermofield foundations](../../2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md)
  constructs a normalized arithmetic purification for `beta>1`, separately
  from a gravitational interpretation, and proves no signaling in A8.
* [Prime-mirror rigidity](../../2026-10-22/PRIME_MIRROR_RIGIDITY.md)
  derives source-bound mirror identities, with phases, finite cutoffs,
  and bounded-domain qualifications.
* [Arithmetic p-adic reconstruction](../../2026-10-22/PADIC_BULK_RECONSTRUCTION.md)
  supplies an explicit three-qutrit code on a separately constructed tree.
  Its full-algebra recovery regions overlap; the code does not give two
  disjoint copies of an unknown quantum state. Bare operator pushing
  without adjoint preservation is an explicit failed control there.

Those sources remain unchanged. This continuation connects their interface
discipline to the newly constructed arithmetic coherent codes.

## 1. The finite bond and its conjugate endpoint

Let `L=C^d`, `1<=d<infinity`, with a declared orthonormal basis `e_j`.
Let `bar L` be its conjugate Hilbert space, with basis `bar e_j`. The
normalized bond is

\[
\boxed{\Phi_d=\frac1{\sqrt d}\sum_{j=0}^{d-1}
e_j\otimes\bar e_j\in L\otimes\overline L.}
\]

The second factor is declared conjugate; placing an ordinary identical
vector space on the other side of a drawing does not impose this rule.
In coordinates, a unitary `U` on `L` has conjugate transport `bar U` on
`bar L`, with matrix entries `conjugate(U_ij)`.

**CBD-01 — PROVED LOCAL.** The bond has norm one and

\[
(U\otimes\overline U)\Phi_d=\Phi_d,
\qquad
\langle\Phi_d,(a\otimes b)\Phi_d\rangle
=\frac1d\operatorname{Tr}(a b^{\mathsf T}).
\]

The first identity follows from `sum_j U_ij conjugate(U_kj)=delta_ik`.
The second follows by summing `a_ij b_ij/d`. Transpose is relative to
the displayed bases; replacing it by adjoint is generally false.

The normalized cup has a normalization cost when used as a wire. Define
`coev(1)=Phi_d` and `ev(bar e_j tensor e_k)=delta_jk/sqrt(d)`. Then

\[
(I_L\otimes\mathrm{ev})(\mathrm{coev}\otimes I_L)
=\frac1d I_L.
\]

Indeed, contraction on input `e_k` leaves only the summand `j=k`, with
two factors `1/sqrt(d)`. The unnormalized cup and cap satisfy the usual
identity-wire equation but have squared cup norm `d`. A normalized
entangled resource cannot be silently substituted for an identity wire.
This is the familiar finite compact-duality normalization, not a new
mechanism for transmitting data.

## 2. The outside carrier state and all present observable contractions

Choose endpoint isometries

\[
J_A:L\longrightarrow H_A,
\qquad J_B:\overline L\longrightarrow H_B,
\qquad J_o^*J_o=I.
\]

The outside description is one state in the larger carrier:

\[
\boxed{\Psi_{\rm ext}=(J_A\otimes J_B)\Phi_d.}
\]

Its endpoint subspaces `Ran J_A` and `Ran J_B`, their operator insertions,
and the connecting bond are explicit. Additional fixed carrier factors
may be tensor-adjoined without changing any of the following identities.
An already correlated additional environment needs its own supplied state.

**CBD-02 — PROVED LOCAL, exact present-observation equivalence.** For any
bounded current endpoint operators `X,Y`,

\[
\boxed{\langle\Psi_{\rm ext},(X\otimes Y)\Psi_{\rm ext}\rangle
=\frac1d\operatorname{Tr}\!\left[
(J_A^*XJ_A)(J_B^*YJ_B)^{\mathsf T}\right].}
\]

More generally, put `J=J_A tensor J_B`. For every logical density matrix
`rho` and every current joint effect `0<=E<=I`,

\[
\operatorname{Tr}(J\rho J^*E)
=\operatorname{Tr}(\rho J^*EJ).
\]

**Proof.** Substitute the isometry and move the adjacent adjoint through
the inner product, or use trace cyclicity. If `{E_z}` is a present POVM,
then `{J* E_z J}` is a logical POVM because positivity is preserved and
the effects sum to `J*J=I`. Conversely, a logical POVM can be lifted to
the code corner and completed on the orthogonal complement, which has
zero probability in encoded states. Thus the current state and measurement
models are exactly equivalent on the declared code and access class.

This identity is mathematical equality of probabilities, not a statement
that one physical sample reveals an entire state or that either endpoint
can perform every joint measurement by itself. Restricting the permitted
present output restricts the observables to which the equivalence applies.

| Internal description | External realization | Exact scope |
| --- | --- | --- |
| One finite entanglement bond | `(J_A tensor J_B)Phi_d` | Same normalized state after encoding |
| Endpoint operator `a` | `J_A a J_A*` in the endpoint code corner | Products and adjoints preserved there |
| Present endpoint effect `X` | Compression `J_A* X J_A` | Same present probabilities |
| Two present endpoint readouts | The displayed joint contraction | Calibrated frames and specified access |
| A matched logical frame change | `J_A U`, `J_B bar U` | Same external bond |
| A freely changing common memory | Additional communication dynamics | Not supplied by the bond identity |

## 3. Source observables require a genuine representation interface

For a logical operator `a`, the corner lift

\[
\iota_A(a)=J_AaJ_A^*
\]

obeys `iota_A(ab)=iota_A(a)iota_A(b)`,
`iota_A(a*)=iota_A(a)*`, and `iota_A(a)J_A=J_Aa`.
Its identity is `P_A=J_AJ_A*`, the code-range projection. This is a
unital representation into the corner `P_A B(H_A) P_A`; it is not claimed
to map logical identity to identity on the unused exterior complement.

Arbitrary compression in the opposite direction has a different property.
Writing `C(X)=J_A* X J_A`, direct multiplication gives

\[
\boxed{C(XY)-C(X)C(Y)
=J_A^*X(I-P_A)YJ_A.}
\]

The right side is the excursion outside the code. Thus equality of present
expectations does not automatically give a product-preserving representation
of successive source transformations. If a supplied source algebra reduces
the code subspace, the excursion vanishes and its restriction is a genuine
*-representation. Otherwise retain the compression and leakage explicitly.

For the arithmetic code in Section 5, logical observables and their corner
lifts are specified exactly. The ordinary full successor or arbitrary
prime multiplication need not preserve that code. Their compressed actions
must not be substituted for their full source actions without checking this
equation and the earlier source relations.

## 4. Transporting the bond through two coherent paths

Suppose observer `o=A,B` has a specified path isometry

\[
W_o:H_o\longrightarrow B_o\otimes E_o,
\]

and the code factorization proved in
[ARITHMETIC_COHERENCE.md](ARITHMETIC_COHERENCE.md) applies:

\[
W_AJ_A\psi=V_A\psi\otimes\eta_A,
\qquad
W_BJ_B\phi=V_B\phi\otimes\eta_B.
\]

Here `V_A,V_B` are isometries, and each `eta_o` is fixed for every logical
input. The two displayed local maps and their initial environment states
are explicit hypotheses. An arbitrary correlated-noise interaction is not
assumed to factor this way.

**CBD-03 — PROVED LOCAL, coherent bond transport.** After the harmless
reordering of tensor factors,

\[
\boxed{(W_A\otimes W_B)\Psi_{\rm ext}
=(V_A\otimes V_B)\Phi_d\otimes\eta_A\otimes\eta_B.}
\]

**Proof.** Apply the two factorizations to each term of the finite sum
defining `Phi_d`. Linearity proves the result. Tracing inaccessible records
therefore leaves the encoded bond pure, with its original Schmidt values.
Known present decoders on the ranges of `V_A,V_B` recover the logical bond.
Those decoders are current operations; no histories are directly compared.

Logical observables travel with the code. The input corner observable
`J_A a J_A*` and the output corner observable `V_A a V_A*` obey the typed
intertwining equation on `Ran J_A`:

\[
W_A(J_AaJ_A^*)J_A
=((V_AaV_A^*)\otimes I_{E_A})W_AJ_A.
\]

If residual logical unitaries `U` and `V` remain after the chosen present
decoding, the decoded bond is `(U tensor V)Phi_d`. Its coefficient matrix is
`UV^T/sqrt(d)`. Hence it equals the original vector precisely when
`UV^T=I`, and represents the same pure state precisely when
`UV^T=exp(i theta)I`. The corresponding matched transport is conjugate,
`V=exp(i theta)bar U`. Spatially moving toward one another does not supply
that relation; it must follow from the declared dynamics and calibration.

Different route lengths are compatible with this theorem. Let A use the
single return `(3,2)` and B use `(2,1)` followed by `(3,2)`. On the
positive two-level input encodings, A's source labels are `(3,6)` and
B's are `(6,12)`. AC-06 gives the same present output labels `(2,4)`
at both endpoints. Their fixed records are respectively `0` and `00`.
Thus the external source bond
`(|3,6>+|6,12>)/sqrt(2)` reaches `(|2,2>+|4,4>)/sqrt(2)` after the
fixed records are factored out. Unequal internal route descriptions are
never directly equated; their calibrated present logical outputs agree.

## 5. An exterior arithmetic bond whose two endpoints interact coherently

Use the real orthonormal arithmetic vectors

\[
c_1=(3\varepsilon_3+4\varepsilon_2)/5,
\qquad c_2=(3\varepsilon_6+4\varepsilon_4)/5.
\]

Set `J_A e_0=c_1`, `J_A e_1=c_2`, and use the corresponding real matrix
for `J_B` on the conjugate logical basis. The external two-endpoint state is

\[
\boxed{\Psi_{\rm arith}
=\frac{c_1\otimes c_1+c_2\otimes c_2}{\sqrt2}.}
\]

Both endpoint carriers then execute the retained-record `T_(3,2)` step
from AC-05. With `eta=(3|0>+4|1>)/5`, the exact output is

\[
\boxed{(W\otimes W)\Psi_{\rm arith}
=\frac{\varepsilon_2\otimes\varepsilon_2
+\varepsilon_4\otimes\varepsilon_4}{\sqrt2}
\otimes\eta_A\otimes\eta_B.}
\]

The same endpoint channel has genuine accepted and rejected branches.
Both records occur in the input encoding, yet neither record reveals the
logical endpoint value. The joint bond survives their removal. The
arithmetic basis, encoding weights, source step, normalization, and present
decoder are all fixed, rather than inferred from a final agreement event.

For example, the output logical Pauli observables are the corner operators

\[
X_{\rm out}=|2\rangle\langle4|+|4\rangle\langle2|,
\qquad Z_{\rm out}=|2\rangle\langle2|-|4\rangle\langle4|.
\]

They satisfy `X_out^2=Z_out^2=P_out` and
`X_out Z_out=-Z_out X_out` on the two-dimensional output code. The current
joint bond has `XX=ZZ=1`. Each individual endpoint marginal is maximally
mixed on its code. The full shared correlation and either local current
model therefore contain different information.

## 6. Two disjoint endpoints cannot each own the same full quantum algebra

There is an exact distinction between correlated twins and two local
copies of all the freely changing logical information.

Let `C` be a logical Hilbert space, `A` a concrete unital *-subalgebra of
`B(C)`, and `J:C->H_A tensor H_B tensor H_R` an isometry. Suppose every
`a in A` has an endpoint-A representative `pi_A(a)` and an endpoint-B
representative `pi_B(a)` acting on disjoint physical tensor factors, with

\[
(\pi_A(a)\otimes I)J=Ja,
\qquad (I\otimes\pi_B(a)\otimes I_R)J=Ja.
\]

The representatives must implement these identities on the **whole code**,
preserving its range. For physical observable reconstruction one also
requires *-representations, as in the October reconstruction dossier.
The following commutator argument already follows from the stated
whole-code intertwining and disjoint support.

**CBD-04 — PROVED LOCAL, shared-algebra boundary.** Under these hypotheses,
the represented logical algebra `A` is commutative.

**Proof.** For `a,b in A`, disjoint endpoint operators commute. Therefore

\[
Jab=(\pi_A(a)\otimes I)Jb
=(\pi_A(a)\otimes I)(I\otimes\pi_B(b)\otimes I_R)J
=Jba.
\]

Apply `J*` to obtain `ab=ba`. Thus two disjoint regions cannot both
reconstruct `B(C)` when `dim C>=2`. This is an exact finite no-broadcast
boundary for the declared reconstruction model, without importing a
gravitational interpretation.

### A shared classical algebra survives

The repetition encoding `J|0>=|00>`, `J|1>=|11>` lets both endpoints
represent every diagonal logical observable. In particular,
`Z_A J=J Z=Z_B J`. However `X_A J|0>=|10>` leaves the code, while
`JX|0>=|11>`. The full noncommuting logical algebra is not duplicated.
The joint operator `X_A tensor X_B` implements logical X, with joint
access rather than two independent local reconstructions.

### Bell-state mirror identities do not evade the theorem

On the single bond vector,

\[
(a\otimes I)\Phi_d=(I\otimes a^{\mathsf T})\Phi_d.
\]

This is state-specific, and transpose reverses multiplication:
`(ab)^T=b^T a^T`. It is not a second representation of the same arbitrary
logical algebra on a preserved unknown-state code. For Pauli X and Z,
the right mirrors of a product must appear in the reverse order.
Interpreting the mirror as a product-preserving freely shared endpoint
memory would force the false equation `XZ=ZX`.

### Compression equality alone is too weak

The preservation hypothesis cannot be dropped. In `C^2 tensor C^2`, let
the orthonormal code columns be

\[
u=(3|00\rangle+4|01\rangle)/5,
\qquad v=(12|00\rangle-9|01\rangle+20|10\rangle)/25.
\]

The disjoint commuting operators `Z_A` and `Z_B` compress to

\[
a=\begin{pmatrix}1&0\\0&-7/25\end{pmatrix},
\quad
b=\begin{pmatrix}-7/25&72/125\\72/125&463/625\end{pmatrix},
\]

whose commutator has upper-right entry `2304/3125`, not zero. Both physical
operators commute on the carrier, but their code compressions do not
preserve products: an intermediate excursion leaves the code. Hence
`J* X J=a` is not a substitute for `XJ=Ja` in CBD-04.

In fact both endpoint compression maps `B(C^2)->B(C^2)` in this example
are invertible as complex linear maps. In the ordered Pauli basis
`(I,X,Y,Z)`, their exact determinants are respectively `2304/15625` and
`4329/15625`. Thus every logical operator has a compressed representative
at each endpoint if no positivity or product requirement is imposed.
Those inverse assignments are only unital *-linear maps, not
*-representations. For example, the endpoint-A inverse sends the positive
logical projector `|0><0|` to `diag(1,-9/16)`, which is not positive.
These formal representatives cannot implement arbitrary logical effects.

There is a complementary positive fact. If a genuine *-representation
`pi` obeys `J* pi(a) J=a` for **every** member of a concrete logical
*-algebra, then code preservation follows automatically:

\[
J^*\pi(a)^*(I-JJ^*)\pi(a)J
=J^*\pi(a^*a)J-a^*a=0.
\]

The left side is a squared leakage form, so `(I-JJ*)pi(a)J=0` and
`pi(a)J=Ja`. The compression counterexample does not evade the
shared-algebra theorem while retaining its *-representation hypotheses.

## 7. Weighted arithmetic bonds retain their own mirror law

The old thermofield construction uses nonuniform Schmidt weights. For a
finite positive diagonal `D=diag(sqrt(w_j))`, `sum w_j=1`, define
`Omega_w=sum_j sqrt(w_j)e_j tensor bar e_j`. Encoding and present-effect
compression work exactly as before, but the contraction becomes

\[
\langle\Omega_w,(a\otimes b)\Omega_w\rangle
=\operatorname{Tr}(D a D b^{\mathsf T}).
\]

Its state mirror is `D a^T D^-1`. That operation need not preserve
adjoints. For `D=diag(3/5,4/5)` and `a=X`, the mirror is

\[
\begin{pmatrix}0&3/4\\4/3&0\end{pmatrix},
\]

which is not Hermitian. It realizes the vector identity but is not the
same physical observable on the other endpoint. Uniform-bond invariance
under `U tensor bar U` also becomes restricted: it fixes this weighted
bond exactly when `UDU*=D`. Weight transport and frame transport must
therefore be carried together. The countably infinite thermal version
further requires the normalization and bounded-mirror domain checks
already proved in the October source.

## 8. Communication and geometry remain separate dependencies

A local trace-preserving operation on endpoint A leaves every unconditional
endpoint-B expectation unchanged. With Kraus operators `K_s`, this follows
from `sum_s K_s* K_s=I`:

\[
\sum_s\operatorname{Tr}[(K_s\otimes I)\rho(K_s^*\otimes I)(I\otimes Y)]
=\operatorname{Tr}[\rho(I\otimes Y)].
\]

A selected branch can change a conditional state, but using that condition
at the other endpoint requires an outcome record or other stated causal
access. The finite bond dictionary supplies correlations, endpoint
insertions, and matched transports. A communication link, teleportation
protocol with its classical messages, or traversable interaction requires
additional explicit operations. None follows from redrawing one tensor.

Likewise, a tensor-network bond is not by itself a geometric throat. A
gravitational dual needs a separate source-to-geometry map and its domain,
equations, observable dictionary, and causal/reconstruction properties.
The October code already demonstrates that isometry and recovery can
survive while proposed entropy/cut equality or geometric isotropy fails.

## 9. Provenance, exact controls, and next lamp

The finite bond identities are standard linear algebra and compact duality.
The complete proofs above fix normalization, conjugate frames, code access,
operator products, and the no-broadcast hypotheses. Their realization uses
the new arithmetic code AC-05 and leaves the prior October source intact.

Primary reference: Abramsky and Coecke,
[A categorical semantics of quantum protocols](https://arxiv.org/abs/quant-ph/0402130),
which develops finite compact structure and protocol composition. Standard
state/channel conventions are those of Watrous,
[The Theory of Quantum Information, Chapter 2](https://jhwatrous.github.io/TQI.2.pdf).
No classical communication side condition is removed by the categorical
notation. No scholarly priority is claimed for these identities.

`carrier_bond_probe.py` uses exact Gaussian-rational matrices and literal
arithmetic branch execution. It checks the full encoded bond, conjugate
frame mutations, all finite observable contractions in its declared probe
sets, source-corner products, no-signaling controls, the commutative
repetition algebra, Bell mirror order reversal, and the rational
compression-only counterexample. Finite checks calibrate the implementation;
the written proofs carry the universal finite-dimensional statements.

**Verdict:** an exact state/code/tensor-contraction dictionary is constructed.
The two internal twins and one external encoded bond are compatible
descriptions under the specified isometries and present observation maps.
Freely communicating endpoint models and an actual Einstein--Rosen geometry
are further structures, not consequences of this equivalence.

**Next lamp:** specify a nontrivial authenticated source-observable algebra,
the allowed endpoint access regions, and the carrier dynamics. Prove that
the desired geometric or computational dictionary transports those data and
their products, rather than only one entangled state or one final output.

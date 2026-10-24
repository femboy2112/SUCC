# Reality Pin: thermal compatibility and the all-place source boundary

Date: 2026-10-22. Baseline: PR #243 at
`d2f760ab9d9a11719e950caeb2d54bfa5114f495`. This is an additive research
extension. All results below are paper proofs or exact finite witnesses, not
Lean certificates or measurements. The classical ingredients retain their
attribution; independent academic novelty is unverified.

## 1. Audit and the missing arrow

The inherited files actually establish the following distinct interfaces.

| Source | Established content and boundary used here |
|---|---|
| `PRIME_BRIDGE_ONE_SHOT.md`, `arithmetic_epr_star.py` | Arithmetic `H0=log N`, its diagonal Gibbs purification, a standard finite qutrit erasure code; not gravity. |
| `PRIME_BRIDGE_COHERENT_INFINITE_TOWER.md`, `coherent_prime_tower.py` | Exact positive affine source representation on integer prefixes; strong code reconstruction with nonzero horizon exits; no uniform bounded-depth successor. |
| `SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md`, `reciprocal_succ_fucc.py` | Source adjoint braid, Gibbs reversible rates, weighted-transpose mirror, vacuum divided powers and a factorial gauge with unbounded inverse. |
| `OBSERVATION_PINNED_INTRINSIC_GEOMETRY.md` | Ring-source-labelled p-adic trees and a declared rank-two projective lift; geometry does not select a quantum coupling. |
| `WITT_CARRY_OBSERVER_LIMIT.md`, `witt_carry_learning.py` | Complete metric/Haar trees can conceal different ring laws; factorial completion gives `Zhat`, not the real place. |
| `OBSERVATION_ANCHORED_TOTAL_BOUNDARY.md`, `boundary_realization_selection.py` | Exact Schur boundary response and predeclared observation fibers; synthetic versus empirical authority is explicit. |
| `SPECTRAL_BOUNDARY_SOURCE_RIGIDITY.md` | Minimal scalar observable Jacobi realization; connected dark modes obstruct full interior identification. |
| `research/2026-10-15/TATE_IDELIC_ZETA_RECONSTRUCTION.md`, `tate_idelic_zeta.py` | Standard Gaussian/integer-ball Tate source; genuine Haar, prime powers, Gamma, poles and analytic domains. |
| `finite_adelic_character_bridge.py` | Actual finite-minus/real-plus character convention, rational diagonal reciprocity and source-matched quotient maps. |
| `research/2026-10-14/TATE_SOURCE_FOURIER_CONDUCTOR_BRIDGE.md` | Conductor/phase probes and counterfeit completion controls. This older convention is conjugated at **all** places relative to the later convention. Mixing just one place is invalid. |

`AGENTS.md`, `docs/FOUNDATIONS.md`, `docs/METHOD.md`, the architecture's typed
boundary/provenance sections and `provenance/IMPORT_MANIFEST.json` were
inspected. The latter pins the original import to FuckingRH commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; no imported file is changed.
The new proposed interacting Hamiltonian is not automatically the Hamiltonian
of the old thermal state. This is a genuine missing compatibility arrow.

**Hole contract.** Can the scalar boundary response of the interacting
arithmetic operator determine a source-authenticated thermal mirror and
all-place geometry? Initial state: unverified. Weakest useful theorem:
identify the minimal spectral quotient, state the additional source/state
data required, and produce a separating witness whenever these differ.
The cheapest falsifier is one off-diagonal matrix element of the stationary
state equation. The novelty tax is paid only as a new-to-SUCC dependency
audit and explicit obstruction, not as a new theorem of modular theory.

## 2. RPQ-01: the old arithmetic Gibbs state is incompatible with the new K

Let `H=l2(N_{>=1})`, `H0 e_n=(log n)e_n`, `S e_n=e_(n+1)` and
`V_p e_n=e_(pn)`. Let `sigma>1`, `lambda,c` be real and

\[
 K=H_0+\lambda(S+S^*)+\sum_p p^{-\sigma}(V_p+V_p^*)+cI.
\]

The prime sum is norm-convergent because its summand norms are at most
`2p^-sigma` and the integer p-series converges. Bounded self-adjoint
perturbation gives a self-adjoint operator on `D(H0)`; the companion
arithmetic-operator manuscript supplies the fuller analytic construction.

For every `beta>1`, define the inherited arithmetic state

\[
 \rho_0=\zeta(\beta)^{-1}\operatorname{diag}(n^{-\beta}).
\]

**Theorem.** For every choice of `lambda,c` and every `sigma>1`, this state
is not stationary under `alpha_t(A)=exp(itK) A exp(-itK)` on `B(H)`.
Consequently it is not a beta-KMS state for that dynamics, in the standard
normal-state/W*-dynamical sense.

**Proof.** The matrix element from 3 to 1 has no additive contribution.
Only the genuine primitive source `V_3^*` contributes, so

\[
 \langle e_1,Ke_3\rangle=3^{-\sigma},\qquad
 \boxed{\langle e_1,[K,\rho_0]e_3\rangle
 =3^{-\sigma}(3^{-\beta}-1)/\zeta(\beta)\ne0.}
\]

This is a domain-valid calculation: the finitely supported vectors and
their `rho0` images belong to `D(K)`. If the state were stationary, its
density would commute with every `exp(itK)`; differentiating its matrix
elements on `D(K)` would give the displayed commutator zero. A KMS state
is stationary. Thus both possibilities are excluded. QED.

The witness cannot be repaired by choosing `lambda=-2^-sigma` to cancel
the `1<->2` edge: the `1<->3` edge remains. On the exact N=3 conditional
state with `beta=sigma=2`, its density is `(36,9,4)/49` and the defect is
`-32/441`. This finite rational test is an independent illustration; the
universal theorem is the preceding matrix-element proof.

The algebraic source is sufficient to express a detecting observable:
`P1=I-SS*` and `S^(i-1)P1(S*)^(j-1)=|i><j|`. Thus a full source algebra
containing `S,S*` contains the finite-rank off-diagonal probes. Whether an
actual instrument can execute them remains an access question. Invariance
of a chosen smaller C*-algebra under the new dynamics must also be proved
before calling it a C*-dynamical system; it is not assumed here.

## 3. RPQ-02: the valid repair is state-dependent, with a boundedness gate

For a positive compact-resolvent `K` with `Z_K(beta)=Tr(exp(-beta K))<infinity`,
set `rho_K=exp(-beta K)/Z_K`. In its eigenbasis, write `D=rho_K^(1/2)` and
`Omega_K=vec(D)`. For a finite-dimensional system every operator `A` has
the unique mirror

\[
 M_K(A)=(D^{-1}AD)^T,\qquad
 (A\otimes I)\Omega_K=(I\otimes M_K(A))\Omega_K.
\]

**Proof.** Vectorization gives `vec(AD)` on the left and `vec(D M^T)`
on the right. Since `D` is invertible, equality is equivalent to the
formula. Direct multiplication gives `M_K(AB)=M_K(B)M_K(A)`. QED.

In infinite dimension this formula is first an expression on its actual
domain; `D^-1` is unbounded. A sufficient precise hypothesis is that the
form `D^-1 A D` on its dense natural domain extends to a bounded operator
`T`, and `AD=DT` on all of H. Then the same identity holds with `M=T^T`,
where transpose is relative to the declared conjugate right basis. No
general boundedness assertion for every bounded `A` is made. In a Gibbs
eigenbasis, the rank-one `A=|i><j|` has mirror
`sqrt(rho_j/rho_i)|j><i|`; ratios can grow without bound across a family.

For the inherited diagonal `H0`, the direct source calculation gives
`M_0(V_p)=p^(beta/2)V_p^*`. RPQ-01 says this old state cannot simultaneously
be declared thermal for the interacting K. It does **not**, by itself,
prove failure of every individual prime identity for every alternative
state; such a stronger statement is not used. Scalar spectral equivalence
does not identify the physical meaning of the transported prime operators.

The standard finite-dimensional modular operator is `Delta(X)=rho X rho^-1`
on Hilbert-Schmidt matrices. It is a property of the algebra **and the
state**. Witten's primary exposition, section 4, fixes this convention;
the elementary vectorization proof above is given explicitly rather than
importing any quantum-field or gravitational conclusion.

## 4. RPQ-03: scalar spectral data forget thermal dark sectors

Suppose `K` is self-adjoint and `b` is a boundary vector. Let
`H_b=closure(span{(K-zI)^-1 b : Im z !=0})`; this is the minimal reducing
spectral subspace. The complete scalar response determines the restricted
pointed system `(K|H_b,b)` up to unitary equivalence. Adding any self-adjoint
dark summand `D` leaves that response unchanged:

\[
 \langle b\oplus0,(K\oplus D+sI)^{-1}(b\oplus0)\rangle
 =\langle b,(K+sI)^{-1}b\rangle.
\]

But when both Gibbs traces exist,

\[
 Z_{K\oplus D}=Z_K+Z_D,\qquad
 \operatorname{Tr}(\rho_{K\oplus D}P_{H_b})
 =Z_{K|H_b}/(Z_K+Z_D).
\]

If the original boundary vector is cyclic, the numerator equals Z_K.
Therefore no map from this scalar boundary response alone can recover the
full Gibbs partition function or full thermofield Schmidt spectrum over
the unrestricted model family. An exact example is `K1=[1]`, versus
`K2=diag(1,2)`, with `b=e1`: both have `m(s)=1/(1+s)`. At `beta=log 2`,
the visible Gibbs mass is respectively `1` and `2/3`, and the purification
has Schmidt rank one versus two. The baseline connected antisymmetric
star supplies the stronger physical reminder that a dark sector need not
be a disconnected graph component.

**Conditional positive result.** If `b` is cyclic, K has compact resolvent,
and `Z_K(beta)<infinity`, the full scalar response fixes K up to a
boundary-preserving unitary and hence fixes `rho_K` and its canonical
purification up to the corresponding `U tensor conjugate(U)`. This fixes
spectral thermodynamics, not a designated position basis, prime algebra,
tensor-factor geometry, or physical spacetime metric. With noncyclic b,
the same conclusion applies only to the minimal observable subsystem.

## 5. RPQ-04: labelled source-history Gram data are a stronger instrument

Let `(T_a)_(a in A)` and `(T'_a)_(a in A)` be bounded operators with the
same involutive source alphabet and distinguished vectors b,b'. Assume
each Hilbert space is the closure of the corresponding finite word orbit.
For every pair of finite words u,v suppose

\[
 \langle T_u b,T_v b\rangle
 =\langle T'_u b',T'_v b'\rangle.
\]

**Theorem.** There is a unique unitary U with `Ub=b'` and
`UT_a=T'_a U` for every named source generator.

**Proof.** On finite word sums define
`U(sum c_w T_w b)=sum c_w T'_w b'`. Equality of the Gram forms makes this
well-defined and norm-preserving, including on zero-norm relations. Its
range is dense; completion makes it unitary. Left concatenation by a
letter proves the intertwining on the word span, then boundedness extends
it to H. The word span and `Ub=b'` prove uniqueness. QED.

This is the classical cyclic/GNS uniqueness argument, now with explicit
source names. Including bounded resolvents as letters also identifies K
through its resolvent; no unbounded polynomial moment-domain assumption
is required. All source relations, including the affine braid, transport
under the resulting U. A scalar m-function knows only the commutative
resolvent sublanguage and cannot supply this larger Gram table.

For the actual arithmetic source `b=e1`, the named successor already gives
`S^(n-1)b=e_n`, so its word orbit is dense. Thus **source-language cyclicity
is proved even while single-K cyclicity remains a separate problem**.
Each finite word history is an algebraic object. The theorem does not
assert that all complex cross-Gram entries are experimentally available;
their measurement needs calibrated coherent preparations/interference,
source/reset authority and a cost model. Finite prefix tables certify
only the corresponding finite filtration.

## 6. RPQ-05: the profinite tower cannot continuously manufacture real SUCC

**Theorem.** There is no continuous `f:Zhat -> R` satisfying
`f(x+1)=f(x)+1` for every x. In particular, there is no continuous unital
ring homomorphism from Zhat to R extending the ordinary integer source.

**Proof.** Compactness of Zhat makes f bounded. Iterating the equivariance
at zero gives `f(n)=f(0)+n`, a contradiction. Alternatively `k! ->0` in
Zhat but `f(k!)=f(0)+k!` cannot converge to `f(0)`. QED.

The same proof works for Z_p. This is a topological/source-equivariance
obstruction, not a denial that Q has both real and p-adic completions.
The required repair is to retain the diagonal rational source and **add**
the real completion with its own topology; it cannot be a continuous
numeric decoding of the completed compact clock tower.

Compatible finite local observations also need not converge in a proposed
stronger topology: the exact source sequence `k!` converges to zero in
every fixed finite residue quotient while diverging in R. This preserves
a concrete nonconvergent local-to-global control.

## 7. RPQ-06: a genuine all-place boundary law exists for rational sources

Let an authenticated finite source present a block matrix over Q(s),

\[
 L(s)=\begin{pmatrix}C(s)&E(s)\\B(s)&A(s)\end{pmatrix},
 \qquad \det A(s)\ne0.
\]

For each place v, let `iota_v:Q(s)->Q_v(s)` be coefficient extension.
The rational source response `Lambda=C-E A^-1 B` obeys

\[
 \boxed{\Lambda_v=\iota_v(\Lambda)
 =\iota_v(C)-\iota_v(E)\iota_v(A)^{-1}\iota_v(B).}
\]

**Proof.** `A^-1=adj(A)/det(A)`; a field embedding preserves the determinant,
adjugate, products and inverse of every nonzero element. Thus scalar
extension commutes with elimination. The same calculation proves it
commutes with addition of interface responses and any legal iterated
elimination. Evaluation at a common rational nonpole s=a is also natural.
QED. Symmetry, source labels and rational change-of-basis relations transport
algebraically; real positivity does not become an ordered p-adic property.

This provides an actual single global compatibility law, but only because
the common rational source and embeddings were specified independently.
It is not a theorem that arbitrary local responses have a common rational
origin. Even product-formula norm compatibility is insufficient: take
`Lambda_infinity=1`, `Lambda_2=-1`, and `Lambda_p=1` for all odd primes.
Every local scalar is nonzero and their normalized absolute values multiply
to one. Yet no q in Q has these images: its real image forces q=1, whose
2-adic image is not -1. Individual norm agreement has erased the source.

For genuine Tate gluing the additional structure is the restricted product,
diagonal Q, a global additive character trivial on Q, compatible self-dual
Haar and a Schwartz-Bruhat test. Under the later repository convention,
`psi_infinity(q)=exp(2 pi i q)` and
`psi_p(q)=exp(-2 pi i {q}_p)` obey `prod_v psi_v(q)=1`.
Tate's original convention conjugates all of these signs together. Genuine
conductor, odd-parity, Gamma and zero-mode/pole controls remain indispensable.
The rational Schur theorem does not supply a Tate functional equation for
an arbitrary response, identify its source with the zeta source, or prove
the sign of a completed Weil form.

## 8. Primary references, executed witnesses and next gate

- Bost and Connes, *Hecke algebras, type III factors and phase transitions
  with spontaneous symmetry breaking in number theory* (1995), original
  [IHES paper](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf),
  sections 1 and 6. The Bost-Connes system includes a specific observable
  algebra and dynamics; merely choosing log N does not import its whole
  classification of KMS states.
- Witten, *Notes on Some Entanglement Properties of Quantum Field Theory*,
  [arXiv:1803.04993](https://arxiv.org/abs/1803.04993), section 4. This
  audit uses only the stated finite/type-I modular conventions.
- Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*
  (1950), [original thesis](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf),
  sections 2.2, 3, 4; Poonen's [author lecture notes](https://math.mit.edu/~poonen/786/notes.pdf)
  locate the modern normalization and Poisson statements. Original sources
  were opened during this round; no gravitational consequence is imported.

Exact executable witnesses are in `reality_pin_quantum_global.py` and
`tests/test_reality_pin_quantum_global.py`. They use only rational arithmetic,
independent direct matrix multiplication, a transpose/order mutation, a
composite-source rejection, a null commutator, a dark thermal sector and
factorial-prefix controls. Infinite theorems above are not certified by
those finite tests. The root campaign receipt records the actual run.

**Verdict-changing next theorem:** for the interacting K, prove a
source-natural, experimentally accessible separating family of labelled
boundary cross-correlations and a quantitative reconstruction bound for
its generated observable algebra, while controlling the bounded mirrors
of S and V_p under `rho_K`. It must preserve source names and the new
thermal state simultaneously; a scalar spectral match or the old TFD
cannot discharge this obligation. Physical access, a common global source
and an independent held-out observation remain additional gates.

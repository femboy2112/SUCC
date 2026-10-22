# Arithmetic-weighted quantum codes on a genuine Bruhat--Tits carrier

Research baseline: `b116841f12b41aaf7600da39bbb40577f25b6295`.
Status: **CLASSICAL** three-qutrit secret-sharing code; **PROVED LOCAL**
weighted access classification, typed arithmetic interface and finite-tree
refinement statements below. Python checks are exact rational contractions,
not proofs of an infinite-dimensional or gravitational correspondence.
No claim of scholarly priority is made for these elementary extensions.

## 0. Scope and hole contract

The question addressed here is whether an actual arithmetic prime-mode input
can reach a quantum code with operational bulk reconstruction on a separately
constructed p-adic carrier. The weakest useful target is an explicit
isometry from a three-level arithmetic carrier to the boundary of an authentic
finite Bruhat--Tits ball, with a proper boundary region recovering its full
noncommutative logical algebra. An arbitrary intertwining by nonunitary
inverses is insufficient: we require a *-preserving boundary representation
and a trace-preserving recovery channel.

The construction succeeds in that finite, declared sense. Geometry, tensor
choice and source-to-logical identification remain supplied data; they are
not determined by the arithmetic state. No Einstein equations, asymptotic
AdS/CFT duality, quantum gravitational metric, or adelic completion is derived.

The strongest countertests are nonuniform arithmetic weights, failed erasure
regions, refinement that preserves encoding while destroying entropy/cut
equality, and an apparently correct intertwiner that fails adjoint transport.

## 1. Separate geometric and Hilbert data

Let `T_2` be the Bruhat--Tits tree of `PGL_2(Q_2)` rooted at the homothety
class of `Z_2^2`. Its radius-one boundary has three lattice classes, indexed
in the implementation by `(0:1),(1:1),(1:0)` modulo 2. The lattice construction,
adjacency proof and refinement maps are supplied in
[PADIC_GEOMETRIC_CARRIER.md](PADIC_GEOMETRIC_CARRIER.md), implemented by
`padic_bulk_network.py`; they are not deduced from a quantum-state drawing.

Place a **qutrit** `C^3` on each edge, one logical qutrit at the root, and a
root encoding tensor with one logical and three edge indices. Thus the
arithmetic/geometric prime is 2, while the bond dimension is 3. Equating these
two numbers is neither needed nor claimed. Boundary vertices label terminal
edge Hilbert factors. At greater radius, nonroot internal vertices carry the
explicit copy isometry `C|x>=|x,x>`; there are no additional logical inputs
there. This is a rooted, anisotropic code, not a uniform perfect-tensor tiling.

## 2. Weighted encoding theorem

All index arithmetic in this section is in `F_3`. Given a nonzero complex
vector `f=(f_0,f_1,f_2)`, put `d=sum_r |f_r|^2`, `w_r=|f_r|^2/d`, and

\[
 W_f|k\rangle=d^{-1/2}\sum_{r\in\mathbb F_3}
 f_r|r,r+k,r+2k\rangle.                                      \tag{1}
\]

**QEC-1 (isometry; all complex amplitudes).** `W_f^* W_f=I_3`.
Indeed the first two coordinates of a support word determine `(r,k)`.
Distinct `k` have disjoint supports, and each column has squared norm
`sum |f_r|^2/d=1`. Zeros and phases in `f` do not affect the conclusion.

**QEC-2 (exact privileged recovery).** The pair of sites `{1,2}` reconstructs
the entire complex algebra `B(C^3)` for every nonzero `f`, including degenerate
weights. Define the permutation unitary

\[
 D_{12}|x,y\rangle=|y-x,\,2x-y\rangle=|k,r\rangle.
\]

The linear map `(x,y)->(y-x,2x-y)` has nonzero determinant modulo 3.
After the harmless ordering of the erased site last,

\[
 (D_{12}\otimes I_0)W_f|\psi\rangle
   =|\psi\rangle\otimes|\chi_f\rangle,
 \quad |\chi_f\rangle=d^{-1/2}\sum_r f_r|r\rangle|r\rangle.    \tag{2}
\]

Hence the channel that applies `D_12` and traces its second output recovers
the logical density operator, including when it is entangled with an
external reference. It is a CPTP channel, not postselection. For every
`O in B(C^3)`,

\[
 O_{12}=D_{12}^*(O\otimes I)D_{12},\qquad O_{12}W_f=W_fO.     \tag{3}
\]

The representation is unital, preserves products and adjoints, and has
`||O_12||=||O||`. Thus (3) certifies operational reconstruction rather than
merely a formal inverse of a nonisometric map.

**QEC-3 (all erasure regions classified at radius one).** Erasure of site 0
is always correctable. Erasure of site 1 or site 2 is correctable **if and
only if** `w_0=w_1=w_2=1/3`. For `i=0,1,2`, direct partial tracing gives

\[
 \operatorname{Tr}_{\{0,1,2\}\setminus\{i\}}
      W_f|k\rangle\langle l|W_f^*
 =\delta_{kl}\sum_r w_r|r+ik\rangle\langle r+ik|.            \tag{4}
\]

For `i=0`, this is independent of `k`. For `i=1,2`, independence of `k`
requires invariance under a nonzero cyclic shift, which is exactly uniformity.
Off-diagonal logical matrix units vanish because equality of two distinct
share coordinates implies `r=s,k=l`. This proves the complementary-channel
form of the Knill--Laflamme criterion. Necessity can also be seen without
invoking that theorem: a reversible channel on the retained subsystem cannot
leave information about arbitrary logical states in its erased environment.
For sufficiency with uniform weights and arbitrary phases, apply the local
diagonal inverse phases on share 0 to reduce to `f=(1,1,1)` before decoding.
This operation is available when the erased share is 1 or 2. For erasure 0,
(2) applies directly.

For uniform real amplitudes, every pair `(i,j)` has the explicit decoder

\[
 k=(x_j-x_i)(j-i)^{-1},\qquad t=x_i+(e-i)k,
 \quad e\notin\{i,j\}.                                    \tag{5}
\]

It sends the encoded state to `|psi>` tensor a fixed maximally entangled
qutrit pair between the second decoder output and the erased share. The
Python oracle tests all nine logical matrix units, all three input columns
and all three retained pairs. Complex linearity then covers all logical
operators; these are not tests confined to classical diagonal states.

No singleton reconstructs the full logical algebra. For uniform amplitudes,
(4) gives the constant channel `rho -> I/3` on every singleton, which cannot
have a left inverse. In general no singleton can reconstruct: its complement
already contains either an authorized pair or, by (4), its own output
discards all input coherences. No two disjoint regions acquire copies of an
unknown quantum state. The three authorized pairs in the uniform case
overlap.

## 3. Authentic arithmetic input and a sharp tradeoff

Fix a genuine prime `p` and a real `beta>0`. The finite prime-mode thermal
law conditioned to exponents `r=0,1,2` is

\[
 q=p^{-\beta},\qquad w_r=\frac{q^r}{1+q+q^2},\quad
 f_r=q^{r/2}.                                                \tag{6}
\]

The infinite-mode global thermofield state requires `beta>1`; conditioning
one finite mode has no such convergence problem and does not evade that
global restriction. Equation (1), with (6), is a lawful weighted arithmetic
tensor. For the actual geometry/source identification below take `p=2`.
The implementation also tests other primes as a weighted-code family, while
keeping its geometric carrier `T_2` explicitly fixed.

**QEC-4 (arithmetic weight versus access theorem).** For every finite
`beta>0`, `W_f` is an isometry with exact recovery on sites `{1,2}`, but
erasure of either of those two sites is not correctable. Full threefold
single-erasure protection is recovered only at uniform weights `q=1`, the
finite-mode `beta=0` limit. This assertion does not construct an infinite
arithmetic Gibbs state at `beta=0`.

At `p=2,beta=2`, all amplitude numerators are rational:
`f=(1,1/2,1/4)`, `d=21/16`, `w=(16,4,1)/21`. The erased site 1 distinguishes
logical `|0>` and `|1>` with exact trace distance `5/7` because their
probability vectors are cyclic shifts. This is a finite counterexample to
the claim that nonmaximal weights preserve the uniform code's whole access
structure. It also refutes the opposite overclaim that nonmaximal internal
weights always destroy isometry.

By contrast, applying the same weights to the **logical input** gives
`W diag(f)`, whose Gram matrix is `diag(|f|^2)`, not identity. Internal
ancilla deformation, logical filtering, and supplying a nonuniform logical
state are three different operations.

### Actual arithmetic operator interface

Let `K_p=span{|1>,|p>,|p^2>} subset ell^2(N_>=1)`. The unitary coordinate
map `J_p:K_p -> C^3` sends `|p^k>` to `|k>`. Compose with the declared
weighted code to get `I_p=W_f J_p`. This is an isometry from the **declared
three-dimensional source subspace**. It is not a bounded coherent residue
quotient on all of `ell^2(N)`.

For any `T in B(K_p)`, the boundary operator from (3) for
`O=J_p T J_p^*` obeys `O_12 I_p=I_p T`, preserving products, adjoints and
operator norm. In particular it transports the compressed logarithmic
Hamiltonian `diag(0,log p,2 log p)` and compressed prime raising operator
`P_K V_p P_K`. The latter loses the genuine transition `|p^2> -> |p^3>`:
the boundary compression is stated, not silently treated as the full
infinite isometry `V_p`.

Exponentiating the finite Hamiltonian gives the exact unitary intertwiner
`exp(it O_12) I_p=I_p exp(it H_K)`. This is an **operator flow on the code**,
not a graph automorphism or a geometrically derived bulk modular flow.
Preserving arithmetic operator relations requires carrying the input
subspace and compression along with every claim.

## 4. Genuine tree refinements and their limitation

For radius `R>=1`, each root branch contains `m=2^(R-1)` terminal edges.
At every nonroot internal vertex use `C|x>=|x,x>`. The resulting encoding is

\[
 W_{f,R}|k\rangle=d^{-1/2}\sum_r f_r
 |r\rangle^{\otimes m}|r+k\rangle^{\otimes m}
 |r+2k\rangle^{\otimes m}.                                  \tag{7}
\]

**QEC-5 (source-preserving refinement).** The map `C` is isometric since
its three basis images are orthonormal. Composition proves `W_f,R` is
isometric and gives the commuting square
`W_f,R+1 = C^(tensor 3m) W_f,R`. Terminal labels follow actual lattice-child
refinements in `T_2`; the code does not substitute a ternary tree. Coherent
basis copying does not clone arbitrary vectors:
`C(alpha|0>+beta|1>)=alpha|00>+beta|11>`, generally unequal to two copies of
the original vector.

For a boundary region `A`, say root branch `i` is *complete in A* if every
one of its `m` descendants lies in `A`.

**QEC-6 (exact access sets under refinement).** For uniform weights, `A`
recovers the complete logical algebra iff it contains at least two complete
root branches. For strictly positive nonuniform geometric weights (6), it
does so iff it contains complete branches 1 **and** 2.

Proof: if the erased region touches one root branch only, its output is
an isometric repetition of a single root share; if it touches no branch it
is trivial. If it touches two branches, a computational-basis observation
of one erased descendant from each reveals `k` from two distinct affine
coordinates, so the complementary channel is not constant. If it touches
only branch 1 or only branch 2 with nonuniform weights, (4) already exposes
`k`. Erasure touching only branch 0 is correctable by (2). These exhaust
all patterns. Conversely, on complete retained branches undo the repetition
isometries on their ranges and apply the appropriate root decoder.

For arbitrary boundary states, the code-range inverse extends to a CPTP
decoder by declaring any fixed output on the orthogonal complement. Boundary
operator reconstruction has a *-representation into the corner where the
selected complete branches lie in their repetition ranges. Its identity
is that range projection, which equals identity on the encoded subspace.
It is not asserted to be the identity on the whole boundary Hilbert space.

The exact oracle exhausts all `64` boundary regions at radius two for both
the uniform code and (6) at `(p,beta)=(2,2)`, tests every authorized matrix-unit
intertwiner, and separately tests fresh regions at radius three and prime 5.
The proof above supplies the all-radius statement; finite checks do not.

## 5. Entropy and minimal cuts: an equality, two strict counterexamples

**QEC-7 (cut rank bound).** For a finite tensor-network pure state and a
cut whose bonds have dimensions `D_e`, expansion over the cut indices gives
at most `prod_e D_e` product vectors. Therefore its Schmidt rank is at most
that product and `S(A)<=sum_e log D_e`. The state must be normalized and any
bulk inputs or reference factors must be assigned to a side of the cut.
Minimizing over valid cuts gives a bound. This rank proof needs no perfect
tensor and permits weighted bonds; equality needs additional conditions.

For radius one with uniform `f` and any **pure logical input**, (4) makes
every singleton maximally mixed. Purity gives the same entropy for its
two-site complement. Consequently all nonempty proper boundary regions
saturate the trivalent-star cut bound `S(A)=log 3`. A mixed logical input is
different: uniform-code pair output is unitarily `rho_logical tensor I/3`,
so `S(pair)=S(rho_logical)+log3`. One may not apply the three-output
pure-state cut formula while forgetting the purifying reference.

For nonuniform arithmetic `f` and logical basis input `|k>`, every singleton
and every pair has spectrum `w`, entropy `H(w)<log3` and cut size one.
Thus the same geometric star, actual isometry, and surviving exact recovery
have a strict entropy/cut gap. Arithmetic weights do not force an RT equality.

For uniform `f`, radius two and logical input `|0>`, (7) is the six-qutrit
GHZ state. The region consisting of one leaf in each of two different root
branches has geometric cut size two, but reduced spectrum `(1/3,1/3,1/3)`
and entropy `log3<2 log3`. Refinement preserves the arithmetic/source square
and the code isometry while breaking this entropy/cut equality. The cut is
verified both by a tree dynamic program and independent enumeration of
all `2^4` internal vertex colorings for each of the `64` boundary regions.

A different unsupported bound also fails: arbitrary tensor contractions
and normalization need not bound output entropy by the original bond
entropy. A bond with probabilities `(4/5,1/5)` followed by the local filter
`diag(1/2,1)` has success probability `2/5` and normalized probabilities
`(1/2,1/2)`, strictly raising entropy. This is conditional local filtering,
not deterministic local isometry. The rank/dimension bound survives.

## 6. Intertwining without adjoints is a false positive

If every `f_r` is nonzero, the weighted tensor on pair `(i,j)` can be
algebraically decoded by nonunitary inverses even when QEC-3 says erasure
fails. In the coordinates `(k,t)` of (5), its amplitude is `f_(t-e k)`.
The map sending `(b,t)` to `(a,t)` multiplied by
`f_(t-e a)/f_(t-e b)` obeys the bare equation `O_A W=W E_ab`.
For nonuniform moduli it does **not** preserve adjoints: reversing `a,b`
inverts this modulus instead of conjugating it. Thus it fails to transport
Hermitian observables as a *-representation and supplies no CPTP decoder.
This is why the tested witness is the unitary decoder plus KL condition,
not just the equation requested in isolation. It provides a concrete
counterexample to using bare operator pushing as sufficient proof of QEC.

## 7. A sharp geometric symmetry obstruction

The root-preserving `PGL_2(Z_2)` action on the three depth-one lattice
directions factors through `PGL_2(F_2)`, which is `S_3`: its order is six and
its faithful action is on the three projective points. Implement this
geometric action on edge Hilbert spaces by the corresponding site permutation.

**QEC-8 (positive weighted root isotropy).** Suppose all `f_r>0`. The image
of `W_f` is invariant under the full geometric root `S_3` iff `f_0=f_1=f_2`.
For the strictly decreasing arithmetic amplitudes (6), its invariant subgroup
is exactly the two permutations fixing the privileged site 0.

Proof: swapping sites 1 and 2 sends each support word of logical `k` to
the support word with logical `-k`, preserving `r` and its amplitude. This
always preserves the image. Swapping sites 0 and 1 sends
`(r,r+k,r+2k)` to the support of logical `-k` with new parameter `r'=r+k`.
Because the supports of the three logical columns are disjoint, invariance
requires the cyclic shift of `f` to be proportional to `f`. At `k=1`,
positivity and cycling three times give proportionality constant `c>0`,
`c^3=1`, hence `c=1`; all amplitudes are equal. Any permutation that moves
site 0 similarly shifts `r` by either `k` or `2k` and has the same obstruction.
For constant amplitudes every permutation preserves the code (the two
transpositions already generate `S_3`). This proves both assertions.

The six-permutation oracle measures the exact projection defect
`(I-WW*)P_pi W`, rather than merely comparing printed labels. At arithmetic
weights `(1,1/2,1/4)`, exactly identity and exchange of sites 1 and 2 survive.
Thus the weighted construction does not accidentally earn geometric isotropy
from being placed on an isotropic tree. A cocycle-compatible enriched family
of frames remains a possible repair; fixed-tensor full isotropy is refuted
under the explicit positive-amplitude hypothesis above.

## 8. Provenance, sources and validation boundary

Original papers actually consulted:

1. Cleve, Gottesman and Lo, *How to share a quantum secret*,
   [arXiv:quant-ph/9901025](https://arxiv.org/pdf/quant-ph/9901025), pp.1--2,
   Eq.(1), reconstruction discussion and Theorem 2. Their three-qutrit
   threshold code is the uniform case of (1); no novelty is claimed for it.
2. Pastawski, Yoshida, Harlow and Preskill, *Holographic quantum
   error-correcting codes*, [arXiv:1503.06237](https://arxiv.org/pdf/1503.06237),
   §§2,4.1 and Appendix B. The isometry/operator-pushing distinction and
   cut-rank argument are classical. Their geometric hypotheses for stronger
   entropy equalities are not imported into our different rooted tree.

Paper proofs QEC-1--8 are explicit finite-dimensional arguments. Formal
finite-field coordinate facts, if admitted by the root integration receipt,
are a separate narrow Lean result; these analytic/code statements are not
automatically Lean certified. Exact tests live in
`tests/test_holographic_reconstruction.py`; no floating-point eigenvalue or
entropy calculation is used as proof. Full repository results belong to the
root receipt, not to this lane's focused check.

Next verdict-changing lemma: construct an isotropy-compatible family of
rooted codes for changing p-adic frames, with a specified action on logical
and boundary algebras, and prove overlap cocycle compatibility. The current
arithmetic weights privilege one root direction; arbitrary local relabeling
does not silently give a coherent adelic or geometric duality.

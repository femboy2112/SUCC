# Successor graphs, quantum maps, and the Yang–Mills source

**Date:** 2026-11-13. **SUCC base inspected:**
`3929e30930438881bebcb371646389d9e66bfbde`. **Role:** adversarial derivation
and primary-source interface audit. The results below are classical mathematics
re-derived for this repository, together with explicitly stated transfer
conditions. They are not a local Lean replay of the continuum Yang–Mills proof.

## 1. The exact connection

There is an explicit unitary correspondence between SUCC's unilateral successor
carrier and the conjugation-invariant sector of one SU(2) variable. The
symmetrized successor becomes multiplication by half the fundamental trace.
Changing its cyclic vector supplies the exact one-plaquette Wilson state.
Thus this connection preserves an observable algebra and its source expectation;
it is more specific than a Hilbert-space analogy.

The correspondence does **not** identify the existing BBP source with a Wilson
measure, or SUCC's chronology Hamiltonians with the physical Hamiltonian of a
four-dimensional gauge theory. Those would be additional statements about
particular sources and dynamics. Sections 5–8 identify their exact interfaces
and falsifiers.

### Existing SUCC objects inspected

The first two rows use paths relative to
`research/2026-11-10/omega_bbp_operational_completion/` at the base above:

| Artifact | Relevant established construction | Connection retained here |
|---|---|---|
| `intrinsic_carrier/README.md`, `PROOFS.md`, `intrinsic_carrier.py` | Successor on positive integers; multiplicative dilations; Haar low-pass and divisibility projections; bounded commutator Hamiltonians | The successor itself has the exact character representation below; other operators must be transported explicitly |
| `quantum_bridge/README.md` | Unitary butterflies with retained detail; flagged projection instruments; finite phase circuits; source and state-preparation obligations | Finite graph states and their transformed observables fit the same finite quantum semantics |
| [WILSON_REFLECTION_SLICE.md](../WILSON_REFLECTION_SLICE.md), in this round's parent dossier | SU(2) Haar moments and positive finite Wilson approximations | The same probability law now has a successor-graph realization |

The older arithmetic carrier is indexed by $n\ge1$, whereas the character
index is $n\ge0$. Let $R e_n=e_{n+1}^{+}$ be the reindexing unitary. It
intertwines the two successor operators, but transports the older dilation as

\[
R^*V_p^{+}R e_n=e_{pn+p-1}.
\]

It does not give $e_n\mapsto e_{pn}$. Consequently the older boundary defects,
divisibility projections, and logarithmic energy cannot be silently replaced
by their zero-indexed namesakes.

## 2. Character transform: a complete proof

On $\mathcal H=\ell^2(\mathbb N_0)$, write

\[
Se_n=e_{n+1},\qquad S^*e_0=0,\qquad
J=\tfrac12(S+S^*).
\]

This $J$ is bounded and self-adjoint, with norm at most one. For

\[
d\nu(x)=\frac2\pi\sqrt{1-x^2}\,dx,\qquad -1\le x\le1,
\]

let $U_n$ be the Chebyshev polynomials of the second kind:

\[
U_{-1}=0,\quad U_0=1,\quad U_1=2x,\quad
2xU_n=U_{n+1}+U_{n-1}.
\]

Their recurrence and normalization agree with the official
DLMF tables [§18.3][dlmf-orth] and [§18.9][dlmf-rec]. To check normalization directly, put

\[
U_n(\cos\theta)=\frac{\sin((n+1)\theta)}{\sin\theta}.
\]

Ordinary sine orthogonality gives

\[
\int U_mU_n\,d\nu
=\frac2\pi\int_0^\pi
\sin((m+1)\theta)\sin((n+1)\theta)\,d\theta
=\delta_{mn}.
\]

The $U_n$ span all polynomials. Polynomial density in continuous functions
on the compact interval, and continuous-function density in $L^2(\nu)$,
prove completeness. Hence

\[
W e_n=U_n
\]

extends uniquely to a unitary $W:\mathcal H\to L^2(\nu)$. The recurrence,
including its $n=0$ boundary, proves

\[
WJW^*=M_x.
\]

This also proves $\sigma(J)=[-1,1]$ and $\|J\|=1$.

For SU(2), write a group element in unit-quaternion coordinates as

\[
g=\cos\theta\,I+i\sin\theta\,(\mathbf n\cdot\boldsymbol\sigma).
\]

Uniform normalized surface measure on $S^3$ is Haar measure: left and right
quaternion multiplication are orthogonal maps. Its conjugacy-class angle has
density $2\sin^2\theta/\pi$, so $x=\operatorname{Tr}(g)/2=\cos\theta$
has exactly the measure $\nu$. The trace of the $n$-th symmetric power of
the defining two-dimensional representation is

\[
\chi_{n/2}(g)
=e^{in\theta}+e^{i(n-2)\theta}+\cdots+e^{-in\theta}
=U_n(\cos\theta).
\]

These symmetric powers are the spin-$n/2$ irreducible representations.
Equivalently, their weight spaces have distinct weights and the raising and
lowering operators connect all neighboring weights, leaving no proper
invariant subspace. The preceding completeness argument already establishes
the completeness needed for the central-function transform.

The target is therefore

\[
L^2(\mathrm{SU}(2),dg)^{\mathrm{conj}}
\cong L^2([-1,1],\nu),
\]

not all of $L^2(\mathrm{SU}(2),dg)$. The missing matrix indices matter on
links of a lattice.

### Products and moments

Multiplying the finite geometric sums yields the exact fusion identity

\[
U_mU_n=\sum_{j=0}^{\min(m,n)}U_{m+n-2j}.
\]

In particular, multiplication by the fundamental character $U_1=2x$
has matrix $S+S^*$. The half-line graph is the fusion graph for tensoring
with spin (1/2), including the absence of spin (-1/2) at its boundary.

Every matrix element of $J^k$ is a weighted nearest-neighbor walk count.
A return from vertex zero has even length; the (2k)-step returns that stay
nonnegative are counted by the Catalan number $C_k=\binom{2k}{k}/(k+1)$.
Each path contributes $2^{-2k}$. Thus

\[
\langle e_0,J^{2k}e_0\rangle=C_k/4^k,
\qquad \langle e_0,J^{2k+1}e_0\rangle=0.
\]

This recovers the earlier Haar calculation through a different exact
combinatorial route. It does not use sampled BBP values.

## 3. The Wilson state and finite constructive approximations

For real $\beta$, define

\[
Z_\beta=\langle e_0,e^{\beta J}e_0\rangle,
\qquad
\psi_\beta=Z_\beta^{-1/2}e^{\beta J/2}e_0.
\]

The exponential is bounded and invertible. Under $W$, this vector becomes

\[
W\psi_\beta(x)=e^{\beta x/2}/\sqrt{Z_\beta}.
\]

Consequently, for every bounded Borel function $f$,

\[
\langle\psi_\beta,f(J)\psi_\beta\rangle
=\frac{\int f(x)e^{\beta x}\,d\nu(x)}{\int e^{\beta x}\,d\nu(x)}.
\]

For continuous $f$, this is an equality of states on

\[
C^*(I,J)\cong C([-1,1]).
\]

The vector is cyclic for this commutative algebra, because multiplying by

$e^{\beta x/2}$ has a bounded inverse on the interval. It also defines a
positive vector state on the larger algebra $B(\mathcal H)$, but only the
specified multiplication subalgebra has been identified with central Wilson
observables. A state on this larger algebra does not itself add the missing
gauge-field dynamics.

### Finite path graphs

Let $P_N$ project onto vertices $0,\ldots,N$, and let

$J_N=P_NJP_N$ act on this $(N+1)$-dimensional space. A closed walk from
zero must take at least $2N+2$ steps to visit the deleted vertex $N+1$.
Therefore

\[
\langle e_0,J_N^k e_0\rangle
=\langle e_0,J^k e_0\rangle\quad(0\le k\le2N+1).
\]

At the first excluded degree there is exactly one missing path, ascending
straight to $N+1$ and descending straight back:

\[
\langle e_0,J^{2N+2}e_0\rangle
-\langle e_0,J_N^{2N+2}e_0\rangle=4^{-N-1}.
\]

Diagonalizing the finite path by sine vectors gives spectral nodes and
positive weights

\[
x_{N,j}=\cos\frac{j\pi}{N+2},\qquad
w_{N,j}=\frac2{N+2}\sin^2\frac{j\pi}{N+2},\quad1\le j\le N+1.
\]

Their weighted sum is the zero-vertex state of $J_N$. Thus this is also
Gaussian quadrature for the same measure, with the degree guarantee proved
by paths rather than inferred from finite agreement.

### Rational positive vector construction

Let $t=\beta/2$, $b=|\beta|$, and use any Taylor degree $K\ge0$:

\[
v_K=\sum_{j=0}^K\frac{t^j}{j!}J^j e_0,
\qquad \widehat v_K=v_K/\|v_K\|.
\]

For rational $\beta$, the coordinates of $v_K$ and its squared norm are
rational. It cannot vanish: its zero-coordinate is a sum of nonnegative even
terms with constant term one. The state is positive regardless of whether
its Taylor amplitude has a sign change. In the character representation its
density is the **square** of that amplitude.

For $u=e^{\beta J/2}e_0$, the norm-convergent exponential series gives

\[
\|u-v_K\|\le
\delta_K=e^{b/2}\frac{(b/2)^{K+1}}{(K+1)!}.
\]

The even Haar moments imply $\|u\|^2=Z_\beta\ge1$. For any nonzero $u,v$,
the triangle inequality gives

\[
\left\|\frac u{\|u\|}-\frac v{\|v\|}\right\|
\le\frac{2\|u-v\|}{\|u\|}.
\]

Therefore, for every bounded operator $A$ with $\|A\|\le M$,

\[
\left|\langle\psi_\beta,A\psi_\beta\rangle
-\langle\widehat v_K,A\widehat v_K\rangle\right|
\le4M\delta_K.
\]

Replacing $e^{b/2}$ by $3^{\lceil b/2\rceil}$ gives a rational upper
bound. The successive factorial terms have ratio

$(b/2)/(K+2)$, eventually at most $1/2$, so a search for a prescribed
positive rational error budget terminates. This is a proof of termination
at fixed input, not a claim of efficient state preparation.

For a polynomial $f$ of degree $d$, the finite graph computes the
normalized expectation **exactly** once

\[
N\ge K+\lfloor d/2\rfloor.
\]

Indeed $v_K$ itself has support at most $K$, and its numerator is the
zero-vertex moment of the polynomial

$\left|\sum_{j\le K}(t x)^j/j!\right|^2f(x)$, of degree at most
$2K+d\le2N+1$. The denominator has degree at most $2K$.
For complex polynomials, conjugate the amplitude coefficients in the square;
the real-β construction above has real coefficients. One may use
$M=\sum_j|[x^j]f|$ to bound $\|f(J)\|$.

### Exact exponential cutoff: a second error bound

The state formed from $e^{\beta J_N/2}e_0$ is positive as well. Write its
expectation as $L_{\beta,N}(f)$. For a polynomial of degree $d\le2N+1$,
put $A_f=\sum_j|[x^j]f|$ and $q=2N+2-d$. Path counts give

\[
0\le\langle e_0,J^k e_0\rangle
-\langle e_0,J_N^k e_0\rangle\le1.
\]

Matching the lower moments and bounding the remaining exponential tail gives

\[
|L_\beta(f)-L_{\beta,N}(f)|
\le2A_f e^{2b}\frac{b^q}{q!}.
\]

For completeness, if $T_q(b)=\sum_{k\ge q}b^k/k!$, the numerator error is
at most $A_fT_q(b)$, and the partition-function error is at most

$T_{2N+2}(b)$. Both normalizers are at least $e^{-b}$; the normalized
finite numerator is bounded by $\|f\|_\infty\le A_f$. Apply the quotient
identity and $T_q(b)\le e^b b^q/q!$. Symmetry permits a sharper denominator
bound, but is not needed for the stated inequality.

## 4. Falsifiers that define the scope

| Incorrect promotion | Exact rejecting witness | Correct scope |
|---|---|---|
| The character transform covers every link function | $g\mapsto g_{12}$ is not conjugation invariant | Central one-variable sector; full links need matrix coefficients |
| The transform selects the Wilson source automatically | At β=0, the vector $e_1$ gives density $4x^2$ and second moment $1/2$; $e_0$ gives Haar moment $1/4$ | Transport the specified vector/state as well as the operators |
| $Z_\beta$ is an infinite Gibbs trace | $e^{\beta J}\ge e^{-b}I$, so its trace is infinite | $Z_\beta$ is a cyclic matrix element |
| $J$ is already the physical Yang–Mills Hamiltonian | $Je_0=e_1/2$, and $\sigma(J)=[-1,1]$ | $J$ is a self-adjoint trace observable; a physical energy and vacuum require separate data |
| Compression preserves every observable product | $P_NJ^2P_N-J_N^2=\tfrac14\lvert N\rangle\langle N\rvert$ | Low-degree zero-vertex moments match; compression is not a star-algebra homomorphism |
| Every finite moment remains exact | First deficit is $4^{-N-1}$ at degree $2N+2$ | The exact degree window is essential |
| The cutoff converges for every bounded measurable observable | Let $D$ be the countable union of all finite spectral nodes. Every cutoff assigns $D$ probability one, but Haar/Wilson measure assigns zero | Fixed continuous observables converge; there is no total-variation convergence |
| Graph cutoffs converge in operator norm | Far beyond every cutoff, unit vectors supported on long intervals have $\|Jv\|$ arbitrarily close to one while $P_NJP_Nv=0$ | Strong convergence and the stated matrix-element bounds |
| A low-pass projection is a reversible quantum operation | A nonzero discarded vector lies in its kernel | Retain the orthogonal detail/flag register, or state the measurement/postselection |

The committed [character tests](../../../../tests/test_ym_succ_character.py)
compare path moments with two Haar formulas through degree 100, test the
first deficits for $N=0,\ldots,14$, character Gram identities through index
12, fusion identities through index 8, and changed-vector and boundary
controls. The [probe receipt](probe_receipt.json) also records the exact
cross-module Wilson example and weighted-composition checks. These finite
checks calibrate the formulas; the preceding derivations supply their
universal quantifiers. The [validation record](VALIDATION.md) identifies the
executed commands and raw logs.

## 5. The genuine finite-lattice extension

The required extension is the Peter–Weyl transform on **each link**, followed
by the vertex gauge constraint. Baez's primary treatment gives the fixed-graph
Hilbert-space decomposition and orthonormal spin-network basis in §2,
Lemmas 1–3 [Baez][baez]. This is a kinematical result. Its use of Haar measure
does not select the Wilson action.

Fix an oriented finite graph $\Gamma=(V,E)$, compact $G$, and normalized
product Haar measure. With a consistent convention for source and target,

\[
\mathcal H_\Gamma=L^2(G^E),\qquad
g_e\longmapsto h_{t(e)}g_eh_{s(e)}^{-1}.
\]

The normalized coefficient functions

$\sqrt{\dim\rho}\,\rho(g)_{ab}$ form a link orthonormal basis. Tensoring
over finitely many edges, then regrouping endpoint representation factors,
gives the gauge-invariant space

\[
\mathcal H_\Gamma^{G^V}
\cong\widehat{\bigoplus}_{\{\rho_e\}}
\bigotimes_{v\in V}\operatorname{Inv}
\left(\bigotimes_{e\text{ at }v}\rho_e^{\epsilon(v,e)}\right).
\]

The sign records the chosen dual representation at an endpoint. An
orthonormal basis in each invariant-tensor space supplies the vertex labels.
For SU(2), a link carries spin $j\in\tfrac12\mathbb N_0$ **and** its two
matrix indices. Character labels alone do not encode these link degrees of
freedom.

The local group integration can be checked directly. For a finite-dimensional
unitary representation $D$, let $Q=\int_GD(g)\,dg$. Haar invariance and
inversion show $Q^2=Q=Q^*$, and its range consists exactly of invariant
vectors. Thus, for an orthonormal invariant basis ι,

\[
\int_GD(g)\,dg=\sum_\iota|\iota\rangle\langle\iota|.
\]

This is the actual tensor contraction that enforces the gauge constraint.
Dropping the vertex tensors changes the theory.

### Supplying the source

A graph must be supplemented with oriented plaquette words, hence a finite
cell complex, to define the gauge action. In the SU(2) convention used here,

\[
x_p(g)=\tfrac12\operatorname{Tr}\Bigl(\prod_{e\in\partial p}
g_e^{\epsilon(p,e)}\Bigr),\qquad
\rho_\beta(g)=Z^{-1}\exp\Bigl(\beta\sum_p x_p(g)\Bigr).
\]

Then $\sqrt{\rho_\beta}\in\mathcal H_\Gamma^{G^V}$ and

\[
\langle\sqrt{\rho_\beta},M_F\sqrt{\rho_\beta}\rangle
=\int F\rho_\beta\,dg.
\]

This extends the vector-state construction to a finite lattice exactly.
The linked plaquette words remain in the state; plaquettes are not replaced
by independent one-variable copies. The spin-network transform transports
both this vector and every multiplication operator $M_F$.

The normalization matches the native source explicitly. For the defining
SU(2) representation, `Gauge.price` in [MatrixGroup.lean][matrix-group] is
$1-x$. Hence the native weight $\exp(-\beta\sum_p(1-x_p))$ differs from
the displayed weight by the constant $\exp(-\beta\#P)$, which cancels
between numerator and partition function. This statement uses that precise
representation and coupling convention.

Oeckl–Pfeiffer's primary paper makes the corresponding finite-lattice
partition-function and observable rewrite explicit in Theorems 3.1 and 3.3
[Oeckl–Pfeiffer][oeckl]. Its plaquette representation labels and link
intertwiners form a spin-foam sum. An infinite representation sum still
requires justified convergence; a finite spin cutoff is an approximation,
not the exact full lattice integral.

In our normalized character convention, direct sine integration gives

\[
e^{\beta x}=\sum_{n\ge0}a_n(\beta)U_n(x),\qquad
a_n(\beta)=\int e^{\beta x}U_n(x)\,d\nu(x).
\]

For β>0, defining

$I_n(\beta)=\pi^{-1}\int_0^\pi e^{\beta\cos\theta}\cos(n\theta)\,d\theta$,
one obtains

\[
a_n=I_n-I_{n+2}=\frac{2(n+1)}\beta I_{n+1}.
\]

Alternatively, expand $e^{(\beta/2)U_1}$ and use the fusion rule.
Tensor-power multiplicities are nonnegative, and evaluating their dimension
identity at $x=1$ bounds the uniform absolute sum by $e^\beta$.
This justifies the character expansion and finite-product interchanges for
this Wilson weight. Normalization is fixed by the integral above; dimension
factors from other Fourier conventions must not be inserted again.

Nonnegative character coefficients are not the same as a nonnegative
pointwise density: $U_1(x)=2x$ is an immediate counterexample. Nor does a
spin-foam expression automatically supply nonnegative individual sampling
weights or a computational speedup. The exact tensor contraction and its
error budget remain the acceptance test.

## 6. Haar wavelets and reflection positivity

For a finite coefficient-space unitary $H$, including a complete Haar
wavelet transform, the replacement

\[
\psi\mapsto H\psi,\qquad A\mapsto HAH^*
\]

preserves every expectation and every operator product. Transforming the
state without transforming the readout generally changes the observable.
The Haar wavelet transform and group Haar measure are distinct constructions;
the character transform above supplies an explicit relation between their
chosen carrier spaces. Quantum wavelet circuit decompositions are classical
prior work [Fijany–Williams][wavelets]. State preparation and measurement
costs are additional to a basis-transform circuit.

Reflection positivity requires more than this ordinary inner-product
identity. Let a Euclidean observable star-algebra have source functional

$L$, an antilinear reflection Θ, and positive-time subalgebra
$\mathcal A_+$. Its form is

\[
Q(F,G)=L((\Theta F)G),\qquad F,G\in\mathcal A_+.
\]

If a star-algebra isomorphism $T$ preserves the source, intertwines
reflection, and carries $\mathcal A_+$ to the declared new positive-time
subalgebra, then

\[
Q'(TF,TG)=Q(F,G).
\]

This one-line substitution proves preservation, including the null space
and the completed OS inner-product space. To transport the reconstructed
time dynamics, the translation/semigroup maps and their domains must also
intertwine.

A Peter–Weyl or wavelet transform is a Hilbert-space unitary, not generally
an isomorphism for **pointwise coefficient multiplication**. Its coefficient
product must be the transported product, or its observables must be the
conjugated operators. Reflection and positive-time support must likewise be
transported. Keeping only a low-pass block does not establish these conditions.
Restriction to a genuine positive-time test subspace preserves its already
positive form; replacing the source by an unrelated cutoff measure is a
different operation.

This matches the external construction's actual interface:
`YM.Cells.laws` requires β≥0 and derives `Seam` from
`Slice.reflected_positive`. Its chessboard and replication-root inequalities
retain the same Wilson law and geometric reflections. The relevant pinned
files are [Wilson/Law.lean][law] and [Cells/Certificate.lean][seam].
The finite state exists for negative β as well, but this fact does not
extend the stated lattice reflection theorem to negative coupling.

## 7. Computational graphs and categorical quantum semantics

Finite representation spaces and their intertwining maps have tensor
products, adjoints, duals, and composition. Forgetting the group action gives
ordinary finite-dimensional Hilbert spaces and linear maps. This makes
spin-network contractions legitimate finite quantum-style tensor diagrams
once their actual tensors are supplied. Gauge-invariant vertex contractions
are generally not unitary gates; a circuit realization must account for
normalization, ancillary registers, and possible postselection.

Abramsky–Coecke explicitly work in finitary quantum mechanics; their intended
example is `FdHilb` [Abramsky–Coecke, §§2 and 7][categorical]. Selinger–Valiron's
typed calculus distinguishes duplicable classical control from quantum data
and proves safety for its chosen operational semantics
[Selinger–Valiron][lambda]. These give concrete languages in which to encode
the finite maps. They do not compile an untyped SUCC term into a Yang–Mills
Hamiltonian or prove the required analytic limit.

There is a sharp infinite-dimensional check. The formal compact-category
cup on the successor carrier would be

\[
\sum_{n\ge0}e_n\otimes\overline{e_n},
\]

whose squared norm is $\sum_{n\ge0}1=\infty$. It is not a Hilbert-space
vector. Finite compact-closed identities therefore cannot simply be applied
to the whole countably infinite carrier with an unnormalized infinite cup.
The bounded-operator character transform remains valid independently of
that failed categorical extension.

## 8. What a continuum Yang–Mills adapter still needs

The finite constructions provide exact representations and useful certified
computations. To reach the audited external continuum theorem, a claimed
adapter must additionally preserve or establish the following data.

| Required data | Concrete obligation |
|---|---|
| One actual four-dimensional Wilson family | Group, oriented lattice, plaquette convention, coupling normalization, spacing and volume sequences |
| Renormalized local observables | Common field dictionary, genuine lattice insertions, locality/stencil conditions, scaling and mixing coefficients |
| Multiscale estimates | Uniform cutoff/volume bounds, derivative and replication costs, actual blocking and calibration certificates |
| Convergence | The source's ultraviolet Cauchy input and coherent infrared extraction, with their quantifier order |
| Reflection and reconstruction | Positive-time domains, reflected products, OS quotient, translations, analytic/domain conditions, and reconstructed field identification |
| Nontriviality | The specified stress-trace asymptotic and excluded free-field class, not merely a nonzero finite variance |
| A physical spectral conclusion | A separately established physical Hamiltonian, vacuum, and uniform spectral estimate if a mass gap is claimed |

The native theorem `YM.FullVolume.genuine` and its
`FixedBounds` conclusion were traced in [RG_IMPORT_MAP.md](../RG_IMPORT_MAP.md).
The bounds depend on source calibration and a preliminary extracted field
table; a separate `Purchased` input supplies the Cauchy property. None of
these analytic estimates is obtained by a unitary change of basis or by the
one-plaquette path-moment identity.

The narrow next lattice discriminator is a source-preserving finite
cell-complex implementation: independently evaluate the same gauge-invariant
correlator by link integration and by representation/intertwiner contraction,
with a proved cutoff budget. A useful hostile control deletes or changes one
intertwiner or plaquette orientation and must change an observable sensitive
to that alteration. Agreement with a known finite value would validate the
adapter at that scope; it would not establish ultraviolet convergence.

## 9. Earned verdict

**PROVED LOCAL / CLASSICAL:** the successor-character unitary, exact Wilson
vector state, finite path moment window and its first failure, and the
positive rational vector approximation with a terminating error search.

**CLASSICAL INTERFACE, NOT IMPLEMENTED HERE:** the full finite-graph
Peter–Weyl/gauge-invariant tensor representation and preservation of a
specified reflection-positive structure under compatible transport.

**UNVERIFIED:** a source identification between the original BBP arithmetic
statistics and the Wilson law; a physical identification of SUCC's earlier
Hamiltonians with the Yang–Mills energy; and a reproduction of the continuum
analytic proof through the computational graph.

The new bridge does close an exact representation-and-source edge. It leaves
the multiscale analytic edge visible and independently testable.

## Primary sources and reading scope

- NIST DLMF [§18.3][dlmf-orth] and [§18.9][dlmf-rec]: Chebyshev normalization and recurrence
  tables; the normalization used above was also derived directly.
- [Baez, *Spin Network States in Gauge Theory*, arXiv:gr-qc/9411007v1][baez]:
  §2, especially Lemmas 1–3; fixed-graph kinematics, not a Wilson continuum law.
- [Oeckl–Pfeiffer, *The dual of pure non-Abelian lattice gauge theory as a spin
  foam model*, arXiv:hep-th/0008095v2][oeckl]: Peter–Weyl, Haar projectors,
  finite-lattice Theorems 3.1/3.3 and SU(2) character example. Source formulas
  were checked against the rendered PDF where normalization was sensitive;
  this dossier defines its own coefficients by an explicit integral.
- [Abramsky–Coecke, *A categorical semantics of quantum protocols*,
  arXiv:quant-ph/0402130v5][categorical]: finite-dimensional scope and §7
  adjoint/compact structure; no infinite-carrier compactness inferred.
- [Selinger–Valiron, *A lambda calculus for quantum computation with classical
  control*][lambda]: author-hosted preprint, introduction and operational/type
  discipline; no SUCC compiler is asserted.
- [Fijany–Williams, *Quantum Wavelet Transforms: Fast Algorithms and Complete
  Circuits*, arXiv:quant-ph/9809004v1][wavelets]: unitary wavelet circuits and
  the need to account for their constituent operations.
- The pinned Yang–Mills package remains
  `55ba9fc36293b3f4d52c6b1f813169a0be76ee98`. Its source identity was checked
  in the parent dossier; this continuation inspected text and did not run
  Lean, a kernel replay, or Comparator.

[dlmf-orth]: https://dlmf.nist.gov/18.3
[dlmf-rec]: https://dlmf.nist.gov/18.9
[baez]: https://arxiv.org/pdf/gr-qc/9411007v1
[oeckl]: https://arxiv.org/pdf/hep-th/0008095v2
[categorical]: https://arxiv.org/pdf/quant-ph/0402130v5
[lambda]: https://www.mscs.dal.ca/~selinger/papers/qlambda-mscs-2up.pdf
[wavelets]: https://arxiv.org/pdf/quant-ph/9809004v1
[law]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Wilson/Law.lean
[matrix-group]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Gauge/MatrixGroup.lean
[seam]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Cells/Certificate.lean

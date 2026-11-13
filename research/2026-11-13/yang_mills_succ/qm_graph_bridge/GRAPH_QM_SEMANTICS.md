# Computational paths as exact finite quantum linear algebra

**Date:** 2026-11-13. **Parent:** `3929e30930438881bebcb371646389d9e66bfbde`
on `research/yang-mills-existence-succ-2026-11-13`, continuing draft PR #613.

**Result:** a finite amplitude-graph presentation is equivalent, after an
explicit semantics-preserving quotient, to matrices over the declared
coefficient field. The implementation below realizes the field
\(R=\mathbb Q(i)\), composition, tensor, dagger, exact Born readout and
two concrete adapters for existing SUCC code. It is finite quantum linear
algebra presented constructively as paths. It is not a new quantization of
ordinary lambda calculus or a reproduction of continuum Yang–Mills theory.

**Authority:** elementary paper proofs and exact finite tests. The construction
is classical; no priority claim, full Lean certification, hardware execution,
quantum speedup or arithmetic cancellation theorem is asserted.

## 1. Recover the actual source structures

The user's proposed relationship has a precise faithful reading: computational
graphs are presentations of typed transformations; certified rewrites change
the presentation while preserving its semantics. A quantum version requires
specified complex amplitudes, tensor composition, adjoints, states and readout.
The graph's shape alone does not supply these data.

| Existing source, present at the pinned parent | Actual meaning | Interface retained here |
|---|---|---|
| [source_lambda.py](../../../../observational_succ/source_lambda.py) | A simply typed finite-observation calculus with source passports, de Bruijn binders, finite evaluation budgets, recorded reads and derived reports. `Succ` and `PrimeMul` act on exact finite residue types. | Compile the actual evaluator's closed residue operation tables, preserving their distinction from new observations. |
| [lambda_source_duality.py](../../../../observational_succ/lambda_source_duality.py) | FinSet curry/uncurry, finite iteration, exact cyclotomic arithmetic and an explicit source/selected-orbit Fourier boundary. | Classical value/operator duality remains distinct from coherent quantum amplitudes. |
| [quantum_records.py](../../../../observational_succ/quantum_records.py) | Exact rational real-qubit density matrices and Kraus instruments, with immutable causal outcome histories. | Compile the actual X/Z instruments into outcome-labelled isometries, preserving outcome order, probabilities and reduced-state channels. |
| [Existing Ω quantum bridge](../../../2026-11-10/omega_bbp_operational_completion/quantum_bridge/README.md) | Finite orthogonal Haar/butterfly lifts, an exact rational chirality contraction, numerical unitary simulations, and a source-budgeted ideal Weyl measurement. | Retain all detail registers; do not confuse full Haar with Walsh; distinguish an exact paper identity from floating implementation checks. |
| [BBP graph resonance](../../../2026-11-10/bbp_graph_resonance/RESEARCH_NOTE.md) | Exact source-polynomial and holonomic identities; finite source contraction; an open source-selected invariant-measure boundary. | Analytic source reconstruction and statistical decay remain different operations. A graphical presentation cannot erase the latter obligation. |
| [collective_spectral.py](../../../../observational_succ/collective_spectral.py) | Existing exact Gaussian-rational scalar type, used by signed polarization tests. | Reuse its `Gaussian` scalar; do not introduce a second floating scalar authority. |

The source lambda implementation's beta evaluation and FinSet curry/uncurry
are classical computations. Multiple beta-equivalent descriptions of one map
are not additional physical alternatives whose amplitudes should be summed.
An amplitude graph needs its own lawful weighting and coherent-composition
contract. Repeating an equivalent syntax tree with weight one generally doubles
the represented amplitude; this is an incorrect rewrite unless compensated.

## 2. Exact path semantics and matrix equivalence

### Definitions

Fix a finite sequence of positive dimensions \(d_0,\ldots,d_L\). Vertices
at layer \(k\) have ordered labels \(0,\ldots,d_k-1\). Edges join only
successive layers, carry weights in \(R=\mathbb Q(i)\), and may be
parallel. A path from input \(j\) to output \(i\) contributes the product
of its edge weights. The matrix of the graph is

\[
\llbracket G\rrbracket_{ij}
=\sum_{p:j\rightsquigarrow i}\prod_{e\in p}w_e.
\tag{GQ-1}
\]

All paths and sums are finite. A graph with only one layer denotes identity.
A multi-layer graph with no complete path has the corresponding zero entries.
There is no convergence assertion for cyclic or infinite graphs.

### Theorem GQ-1: contraction is path summation

Let \(A_k\) have entry equal to the sum of all edge weights from a source
vertex in layer \(k\) to a target vertex in layer \(k+1\). Then

\[
\llbracket G\rrbracket=A_{L-1}\cdots A_0.
\]

**Proof.** Expand matrix multiplication as sums over intermediate vertex
indices. Distribute each edge-entry sum. Every term chooses exactly one edge
at each layer and therefore exactly one complete path; every complete path
appears once. Empty paths give the identity case. This is a finite distributive
identity over the specified field.

### Theorem GQ-2: every finite matrix over the field is represented

For every \(m\times n\) matrix \(A\) over \(R\), make one input layer
of size \(n\), one output layer of size \(m\), and an edge of weight
\(A_{ij}\) from \(j\) to \(i\) for each nonzero entry. Its semantics is
exactly \(A\). Conversely GQ-1 shows that every graph denotes such a matrix.

Thus the represented matrices are **exactly** the finite nonempty matrices
over \(\mathbb Q(i)\). This statement concerns all matrices, including
nonunitary maps and zero maps. It is not a statement that all matrices are
deterministically implementable quantum gates.

### Theorem GQ-3: composition, tensor and dagger

Glue the output boundary of \(G\) to the equal-dimensional input boundary
of \(H\). Partitioning complete paths at that boundary gives

\[
\llbracket H\circ G\rrbracket
=\llbracket H\rrbracket\llbracket G\rrbracket.
\]

Reversing every edge, reversing layer order and conjugating every weight gives

\[
\llbracket G^\dagger\rrbracket=\llbracket G\rrbracket^*.
\]

For tensor composition use ordered boundary pairs and independent path pairs,
with paired weight products. The resulting matrix is the Kronecker product:

\[
\llbracket G\otimes H\rrbracket
=\llbracket G\rrbracket\otimes\llbracket H\rrbracket.
\]

The implementation uses the canonical bipartite presentation of this tensor
matrix. It does not claim to preserve the original internal branch histories
as syntax. Associativity, dagger involution, reversal of composition and the
tensor interchange law follow from the displayed finite identities.

### The exact meaning of “dual presentation”

Declare \(G\sim H\) precisely when their ordered boundaries match and
their matrices agree entry by entry. Matrix semantics is then a bijection on
every hom-set between graph equivalence classes and finite matrices over
\(R\), preserving composition, tensor and dagger. The two presentations
are equivalent as dagger symmetric monoidal categories on positive finite
dimensions. Boundary permutation matrices supply the symmetry.

The usual compact cup \(\sum_j|j,j\rangle\) and its adjoint are represented
by zero/one matrices. Their yanking identities are the elementary contraction
of Kronecker deltas. The cup is unnormalized, with squared norm equal to the
dimension; being a morphism in the linear category does not make it a free
deterministic state preparation.

**Novelty tax:** the equivalence is a standard matrix-presentation construction,
not a proof that the existing entire SUCC calculus already has these quantum
semantics. Its useful additional content here is a finite canonical matrix
normal form, an exact equality procedure in the declared field, and actual
adapters with hostile controls. No completeness of a separately specified
finite graphical rewrite-rule system is claimed. Defining equivalence by
matrix equality must not be described as having proved such rewrite completeness.

## 3. Coefficient and effective-computation boundaries

Rational-complex arithmetic is exact and decidable in this implementation.
It excludes arbitrary real numbers, arbitrary complex black boxes and
floating approximations. In particular, a normalized single Hadamard gate
has entries \(\pm1/\sqrt2\) and lies outside \(\mathbb Q(i)\).
Its two-qubit Walsh product has entries \(\pm1/2\) and is represented
exactly here. The existing Ω code's floating Hadamard must not silently be
promoted to a rational-complex exact calculation.

There are two lawful extensions: adopt an exact algebraic field such as
\(\mathbb Q(i,\sqrt2)\), with a checked conjugation and canonical equality
procedure; or use nonorthonormal rational Haar coordinates and explicitly
transport the metric. SUCC's existing `Cyclo16` algebra is a possible source
for a separately audited algebraic-field adapter. Neither extension is needed
for the exact results in this module.

Every finite matrix can formally be drawn if arbitrary complex labels are
admitted, but that is not an effective finite representation of every complex
number. Computable approximation is a further contract with error bounds;
it does not make exact equality decidable for arbitrary computable scalars.

## 4. When graph evolution is a quantum operation

We use column vectors and the standard inner product
\(\langle v,w\rangle=v^*w\), conjugate-linear in the first slot. This
is explicit because the reused scalar's original Hermitian-form module
documents a different pairing convention; only its scalar arithmetic is reused.

### Theorem GQ-4: norm preservation is the isometry condition

For a matrix \(A:R^n\to R^m\), the following are equivalent:

1. \(\|Av\|^2=\|v\|^2\) for every \(v\in R^n\).
2. \(A^*A=I\).

**Proof.** The reverse direction follows by direct contraction. For the forward
direction, test the quadratic form of \(A^*A-I\) on each \(e_j\),
\(e_j+e_k\), and \(e_j+i e_k\). Its diagonal, real off-diagonal and
imaginary off-diagonal entries all vanish. For equal finite dimensions an
isometry is unitary. This is the exact condition checked by the code.

For an already normalized state, Born weights in the selected orthonormal
basis are \(|v_i|^2\). They are nonnegative rationals and sum to one.
`born_probabilities` rejects a nonunit vector: it does not conceal a lossy
map by silently normalizing its output.

A nonzero rational-complex ray may instead be represented exactly by

\[
\rho_v=vv^*/\|v\|^2.
\]

This permits, for example, the plus-state density without claiming that its
normalized amplitude \(1/\sqrt2\) belongs to the coefficient field.
Conditional normalization is a valid separately labelled operation; a
postselection probability is not discarded.

### Theorem GQ-5: recorded alternatives have a Kraus dilation

For a finite family \(K_o:R^n\to R^m\) satisfying
\(\sum_oK_o^*K_o=I\), define

\[
Vv=\sum_o |o\rangle\otimes K_ov.
\]

Then \(V^*V=I\). For a positive trace-one input density \(\rho\),
the outcome probabilities and the state after discarding the outcome register
are respectively

\[
p_o=\operatorname{tr}(K_o\rho K_o^*),\qquad
\rho'=\sum_oK_o\rho K_o^*.
\]

**Proof.** Orthogonality of the outcome labels removes cross terms in
\(V^*V\); completeness gives identity. Taking the corresponding diagonal
block of \(V\rho V^*\) gives the probability, and summing its diagonal
outcome blocks is the partial trace. Positivity follows from
\(u^*K_o\rho K_o^*u\ge0\), and cyclicity of trace gives trace one.

This compiles the existing `quantum_records.Instrument` directly. Its X and Z
Kraus entries are rational; every compiled graph is an exact isometry, and
the tests match the existing instrument's probabilities and reduced channels.
The source's immutable **observed classical record** and a coherent unmeasured
ancilla are different physical/mathematical records. Their relation requires
the declared measurement/dephasing operation, not merely a shared label.

The low-level `channel_action` acts linearly on matrices and checks Kraus
completeness. A caller's input positivity is an explicit premise; the function
does not certify an arbitrary trace-one matrix as a state.

## 5. Coherent alternatives, histories and coarse graining

Take the exact normalized state and rational unitary

\[
\psi=(3/5,4/5)^T,\qquad
R=\begin{pmatrix}3/5&4/5\\4/5&-3/5\end{pmatrix}.
\]

The coherent output is \(R\psi=(1,0)^T\). If the intermediate branch is
recorded in an orthogonal register and that record is discarded before
recombination, the state becomes
\(\operatorname{diag}(9/25,16/25)\), and the same final mixer instead
gives Born probabilities

\[
\boxed{(337/625,\ 288/625).}
\]

Every value is exact. The difference is the cross terms removed by dephasing.
A common sign \(-\psi\) preserves the density. A relative sign
\((3/5,-4/5)^T\) gives final probabilities
\((49/625,576/625)\). This separates global phase from a measurable relative
phase in a specified interferometer.

The graph normal-form test also separates harmless syntax from invented
paths. One edge of weight one is equivalent to parallel edges of weights
\(1/3\) and \(2/3\). Two parallel edges both of weight one represent
amplitude two, not the original identity. Beta-equivalent derivations must
therefore be quotiented or transported by a proved semantics-preserving
translation; they must not be counted as fresh physical branches.

Unweighted Boolean graphs describe reachability; natural-number path
matrices count paths; stochastic maps carry classical probability weights;
complex amplitude graphs permit signed interference. Those scalar and
composition choices are load-bearing even when the diagrams look similar.

## 6. An exact compiler for actual SUCC residue maps

Let \(f:X\to Y\) be a finite deterministic table. Its coherent linearization
is \(L_f|x\rangle=|f(x)\rangle\).

### Theorem GQ-6: injectivity is the exact reversible boundary

\(L_f\) is an isometry iff \(f\) is injective, and a unitary iff it is a
bijection. Indeed

\[
(L_f^*L_f)_{xy}=\mathbf1_{f(x)=f(y)}.
\]

When \(f(x)=f(y)\) with \(x\ne y\), the nonzero vector
\(|x\rangle-|y\rangle\) lies in its kernel. A later reconstruction
cannot recover that vector from the resulting zero. This is a precise
kernel-preservation failure, not an objection to representing the classical
function itself.

`compile_source_lambda` invokes the actual existing evaluator on every
closed residue input; it does not replace the source law with an imagined
quantum rule. For \(m\ge2\), it constructs

\[
S_m|x\rangle=|x+1\bmod m\rangle,
\qquad V_{p,m}|x\rangle=|px\bmod m\rangle.
\]

The existing source checker rejects composite values presented as primitive
prime generators. The exact matrix conclusions are

\[
S_m\text{ is unitary},\qquad
V_{p,m}\text{ is unitary}\iff\gcd(p,m)=1,
\qquad V_{p,m}S_m=S_m^pV_{p,m}.
\]

The last identity holds on each basis state. Multiplication by \(p\) is
invertible modulo \(m\) precisely in the coprime case, establishing the
second statement. If \(p\mid m\), basis states zero and \(m/p\) collide.
The executable adapter is finite and extensional, not a compiler for every
recursive or effectful source-lambda term. It performs no primitive reads and
does not claim external authentication from its declared passport.

### Retaining the source makes every finite table reversible

For \(Y=\mathbb Z/m\mathbb Z\), the oracle

\[
U_f|x,y\rangle=|x,y+f(x)\bmod m\rangle
\]

is a permutation unitary for every table, with inverse obtained by subtraction.
It retains \(x\), which is exactly what a many-to-one output map discarded.
Discarding this source register is a channel and may remove coherence.

The basis-copy map \(|x\rangle\mapsto|x,x\rangle\) is a legitimate
linear isometry, but it maps a superposition to
\(\sum_xa_x|x,x\rangle\), not to
\((\sum_xa_x|x\rangle)^{\otimes2}\). The construction does not clone
unknown quantum states.

### Boundary conditions cannot be changed silently

On a finite register the truncated natural-number successor
\(S_N=P_NS P_N\) kills the last basis state. Exactly,

\[
S_N^*S_N=I-|N-1\rangle\langle N-1|,
\qquad
S_NS_N^*=I-|0\rangle\langle0|.
\]

It is not the unitary cyclic successor. The infinite unilateral successor is
an isometry with a non-surjective range, a third object. Closing the finite
boundary into a circle creates a different source transition, not a proof
that the original successor was unitary.

## 7. Connection to Yang–Mills observable reconstruction

At a fixed finite matrix dimension, choose a positive trace-one density
\(\rho\) and define \(\omega_\rho(A)=\operatorname{tr}(\rho A)\).
The graph quotient carries precisely the same products, adjoints and state:

\[
\omega_{\mathrm{graph}}([G])
=\omega_\rho(\llbracket G\rrbracket),\qquad
\omega_{\mathrm{graph}}([G]^\dagger[G])\ge0.
\]

Consequently its GNS null quotient and inner products agree with the matrix
presentation. Extending scalars to \(\mathbb C\) gives the usual finite
complex matrix-algebra setting. This is a direct example of the source-bound
GNS interface in [SUCC_CROSSWALK.md](../SUCC_CROSSWALK.md); no physical state is
chosen by the graph syntax itself.

For a Yang–Mills application the important next object is the **actual
source-selected observable state**, with its gauge action, reflection,
translations and limiting estimates. Matrix presentation equivalence preserves
those structures only when they have been supplied and intertwined.

A finite number of SU(2) lattice edges still has continuous configuration
space \(\mathrm{SU}(2)^E\) and generally infinite-dimensional
\(L^2(\mathrm{SU}(2)^E)\). Therefore the present finite graph calculus
does not, merely by being finite, reproduce the full Wilson lattice integral.
It applies to pointwise finite representation matrices, finite group models,
or separately specified finite truncations. Passing a representation cutoff,
volume limit or lattice-spacing limit needs its own approximation and uniform
estimate theorems. Neither the new existence result nor graph/matrix equivalence
automatically supplies a physical mass gap or the arithmetic signed saving.

The useful immediate achievement is a checked finite language in which the
same observer transformation can be read as a source computation, an amplitude
graph, a matrix, or a recorded quantum operation, with the exact conditions
for each interpretation visible.

## 8. Reproduction and claim ledger

Implementation:
[ym_graph_semantics.py](../../../../observational_succ/ym_graph_semantics.py).
Tests:
[test_ym_graph_semantics.py](../../../../tests/test_ym_graph_semantics.py).

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_ym_graph_semantics.py' -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_quantum_records.py' -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_source_lambda.py' -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_lambda_source_duality.py' -v
```

Observed this round: **13 new tests, 5 existing quantum-record tests, 31
existing source-lambda tests and 24 existing lambda-duality tests passed**;
73 total, zero failures or errors. The existing three suites were executed by
a combined runner that explicitly aggregated `wasSuccessful()` into its exit
status. The new suite ran by the direct command above. Neither receipt is a
full-repository gate, an independent external review or a Lean certificate.

Controls include explicit edge-path enumeration versus matrix contraction,
independent Gaussian-rational multiplication, coherent/recorded interference,
parallel-edge duplication, complex relative phases, nonunitary coarse graining,
lost kernels, finite successor boundaries, actual native instrument probabilities,
and exact SUCC/FUCC composition for moduli 2 through 9 and primes 2, 3, 5, 7.
The universal statements are supported by the displayed proofs, not by that
finite testing window.

| Claim | State | Remaining boundary |
|---|---|---|
| Finite weighted graphs modulo matrix equality represent exactly finite matrices over Q(i) | **CLASSICAL / PAPER PROVED; EXACT CODE CHECKS** | Not arbitrary exact complex scalars or a complete local rewrite calculus. |
| Composition, tensor, dagger and Born weights agree | **PAPER PROVED; EXACT CODE CHECKS** | Unit norm, orthonormal metric and lawful coefficient field are retained. |
| Actual source-lambda residue maps compile with the stated affine law | **PAPER PROVED; EXACT FINITE ADAPTER** | Noninjective maps are not deterministic isometries. |
| Native X/Z instrument probabilities and partial traces survive compilation | **EXACT FINITE CHECKED** | The coherent ancilla is distinct from a realized classical record. |
| An arbitrary classical computational graph is already a quantum process | **NOT ESTABLISHED** | Amplitudes, tensor/dagger, state and lawful operation semantics are missing. |
| SUCC reproduces the continuum Yang–Mills construction through this finite graph module | **NOT CLAIMED** | Source-state, continuous-group integration and analytic-limit interfaces remain separate. |
| A new original-zero BBP statistical saving follows | **OPEN** | Graph presentation and basis changes do not supply signed cancellation. |

## Classical context and attribution

- Samson Abramsky and Bob Coecke, [A categorical semantics of quantum
  protocols](https://arxiv.org/abs/quant-ph/0402130), 2004. This is primary
  context for categorical organization of quantum composition, tensor,
  scalars and readout; the elementary finite identities above are written out
  directly rather than asserted from a broad categorical analogy.
- Peter Selinger, [A survey of graphical languages for monoidal
  categories](https://arxiv.org/abs/0908.3347), 2009. Graphical calculus requires
  the specified categorical structure and associated coherence/equational
  scope; a suggestive drawing alone is not a theorem.
- Existing SUCC source paths above provide the concrete implementation
  provenance. The new adapter retains the original classical/quantum/source
  boundaries and makes no novelty claim for matrix mechanics or the standard
  Kraus and GNS constructions.

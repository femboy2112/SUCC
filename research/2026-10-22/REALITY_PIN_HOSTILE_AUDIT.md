# Reality Pin: independent hostile audit and two sharp aliases

Date: 2026-10-22. Baseline inspected: PR #243 at
`d2f760ab9d9a11719e950caeb2d54bfa5114f495`. This is a research branch artifact;
no historical theorem, import, or frozen receipt is rewritten here.

**Verdict:** the inherited positive path inverse, bounded rational identity,
first-return, Hankel determinant and weak-coupling proofs survive this audit
under their stated hypotheses. Two stronger obstructions below show why
cyclicity alone does not make a general physical graph identifiable, and why
finitely many exact probes still fail on positive, fully observable spectral
families. These are elementary derivations and exact synthetic controls;
independent academic novelty is UNVERIFIED.

## 1. Audit contract and provenance

The audited source files are
`observational_succ/spectral_boundary_rigidity.py`,
`tests/test_spectral_boundary_rigidity.py`,
`research/2026-10-22/SPECTRAL_BOUNDARY_SOURCE_RIGIDITY.md`,
`docs/CLAIM_SUPPLEMENT_SPECTRAL_BOUNDARY_KRYLOV.md`, the frozen
`SPECTRAL_BOUNDARY_RIGIDITY_RECEIPT.json`, and
`.github/workflows/spectral-boundary-rigidity.yml`.
The older independent graph oracle is
`observational_succ/boundary_realization_selection.py` from parent PR #242.
AGENTS, METHOD, claim-ledger status policy, claim-index/namespace conventions,
roadmap and historical `provenance/IMPORT_MANIFEST.json` were inspected.
The latter identifies founding imported material from
`FuckingRH@ba075348b7bcc66d938b3e0ca96c26e95bba340a`; it does not confer kernel
authority on these October 22 research additions.

The inherited spectral source/test Git blobs in its frozen receipt are
`2c5a1548b2cd884e130e27d1206cbdbe7d6c16b1` and
`6c13623f95fe027a674b6749ae5358573952d3ad` respectively.
All 28 inherited tests passed locally in this audit, and their probe reproduced
the printed receipt. The new independent tests use the permutation determinant
formula and cofactor resolvents, rather than reusing production Gaussian
elimination for the main algebraic verdict.

The classical attribution is correct: Gesztesy and Simon,
*m-functions and inverse spectral analysis for finite and semi-infinite Jacobi
matrices*, J. d'Analyse Math. 73 (1997), 267–297. The author-maintained
[publication list, item 261](https://math.caltech.edu/simon/biblio.html)
confirms this citation. The inherited mp_arc endpoint returned “Found no
abstract” during the present retrieval, although search indexing still had the
matching record; this is an access observation, not a mathematical objection.
The proofs below are supplied in full and do not rely on that endpoint.

Before this round, the spectral/prime-bridge/Witt/observation-pinned supplements
were present on the stacked branch but not navigable from the inherited main
claim index, master ledger, namespace registry or roadmap. Their standalone
scope labels were sound; central integration was outstanding. A new crosswalk
must not silently promote their paper proofs into kernel-certified declarations.

## 2. What survives, and exactly why

| Inherited claim | Audit result | Necessary boundary |
|---|---|---|
| SBK-01 positive path inverse | SURVIVES / paper proof | Known unit hidden capacitances, one fixed boundary-to-ground ordering, all edge conductances strictly positive, complete rational response |
| SBK-02 rational identity | SURVIVES / elementary proof | Both numerator and denominator degrees at most d, 2d+1 distinct common nonpoles, exact values; positivity is not needed |
| SBK-03 moment 2r | SURVIVES / walk proof | Extension retains the entire old principal block; it moves the old terminal connection from ground to the new node |
| SBK-07 Hankel determinant | SURVIVES / Gram proof | Real symmetric Jacobi operator and e1, nonzero internal links; strict positivity is used for physical interpretation and no zero link |
| SBK-N1 weak coupling | SURVIVES / exact rational identity | Real Laplace s≥0; no promotion to imaginary-frequency AC bounds without a separate argument |

For the moment identity, a different physical operation gives a different
answer. Starting with conductances `(2,3,5)`, retain the old last grounding
resistor and attach an extra edge of conductance 5. The old last diagonal rises
from 8 to 13. The first changed return moment is then **3**, with difference
`3²·5=45`, rather than 4. The new node is still at depth two, but a change of the
old node's diagonal can be sensed by going there, dwelling once, and returning.
This does not refute the inherited theorem; it demonstrates why its source
operation must be preserved exactly.

The code enforces finite budgets (at most eight hidden nodes, bounded moment
counts). These are implementation budgets, not limits on the universal paper
proofs. In particular extending an already maximal-size code path exceeds the
finite budget and is not an executed case of the theorem.

## 3. Full-response ambiguity without dark modes

**Theorem H1 (PROVED, explicit finite counterexample).** There exist two
nonisomorphic finite positive grounded RC interiors with the same number of
nodes, known unit interior capacitances, the same one-port coupling, and no
boundary-dark modes, whose complete scalar boundary responses agree.
Therefore positivity, known capacitances, complete scalar response and
cyclicity do not jointly identify an arbitrary physical graph up to vertex
relabeling.

**Declared physical gauge:** vertex permutations preserving the boundary,
ground, capacitances and edge conductances. An arbitrary orthogonal mixture of
interior node potentials is not a physical relabeling in this model class.

**Construction.** Take port coupling g0=1 and normalized source b=e1. Define

\[
A=\begin{pmatrix}4&-1&0\\-1&4&-1\\0&-1&4\end{pmatrix},\qquad
U=\begin{pmatrix}1&0&0\\0&4/5&-3/5\\0&3/5&4/5\end{pmatrix}.
\]

Then U is orthogonal, Ue1=e1, and

\[
A'=UAU^T=
\begin{pmatrix}
4&-4/5&-3/5\\
-4/5&124/25&-7/25\\
-3/5&-7/25&76/25
\end{pmatrix}.
\]

Interpret every negative offdiagonal as minus the edge conductance and ground
each interior node with conductance equal to its row sum, subtracting the
external port conductance 1 at node 1. For A the grounding conductances are
`(2,2,3)`; for A' they are `(8/5,97/25,54/25)`. All are strictly positive.
Thus both are actual finite passive network matrices with unit shunt
capacitances. Their positive Dirichlet energies establish positive
definiteness. The first interior has two edges, the second three, so no vertex
permutation identifies their graphs.

For every s outside their poles,

\[
(A'+sI)^{-1}=U(A+sI)^{-1}U^T,
\qquad e_1^T(A'+sI)^{-1}e_1=e_1^T(A+sI)^{-1}e_1.
\]

Both consequently have exactly the same complete one-port response

\[
Y(s)=1-\frac{(s+4)^2-1}{(s+4)((s+4)^2-2)}.
\]

There is no hidden sector: the Krylov matrix `[e1,Ae1,A²e1]` has determinant
−1, and conjugation by U leaves that determinant −1. Both three-dimensional
pairs are cyclic and minimal. This proves H1. QED.

**Scope.** The first source is a path among its interiors with extra grounding
edges. It is **not** in SBK-01's narrower class with only an opposite-end
ground. H1 therefore does not conflict with SBK-01. Nor is equality asserted
for the full two-terminal response with a separately varied reference-ground
potential: the declared experiment fixes ground and reads the one port.

**Next discriminator.** An independently authenticated additional probe at
physical interior node 2 separates the sources: their first local moments are
4 and 124/25, and their node-2 resolvents differ. The original scalar response
does not grant that additional probe access. If physical gauge is enlarged to
arbitrary boundary-fixing unitaries, the models become gauge-equivalent by
definition; that quotient has deliberately discarded the graph distinction.

## 4. Every finite list can be spoofed by positive cyclic spectral sources

**Theorem H2 (PROVED, constructive).** For every finite list of k distinct
nonnegative real Laplace parameters s1,…,sk, there are two different positive
definite, finite-dimensional self-adjoint source pairs with normalized cyclic
boundary vectors, the same k+2 distinct eigenvalues, and equal scalar
resolvents at all k parameters. They disagree at every other nonnegative
parameter. If the samples are rational, their spectral weights and responses
are rational. In fact a nontrivial interval of sources has exactly the same
sampled data.

**Proof.** Set r=k+2 and choose distinct poles a1,…,ar>0; the executable oracle
uses aj=j+1, hence aj≥2. Let

\[
R(s)=\frac{\prod_{\ell=1}^{k}(s-s_\ell)}{
                 \prod_{j=1}^{r}(s+a_j)}
     =\sum_{j=1}^{r}\frac{c_j}{s+a_j},
\qquad
c_j=\frac{\prod_\ell(-a_j-s_\ell)}{\prod_{i\ne j}(a_i-a_j)}.
\]

All cj are nonzero. Since R(s)=O(s^-2), its 1/s coefficient vanishes, so
Σcj=0. Choose

\[
\delta=\frac{1}{2r\max_j|c_j|},\qquad
w_j^\pm=\frac1r\pm\delta c_j.
\]

Each weight is at least 1/(2r)>0 and each weight vector sums to one. Let
A±=diag(aj), b±=(sqrt(wj±))j. Their scalar responses are

\[
m_\pm(s)=\sum_j\frac{w_j^\pm}{s+a_j},\qquad
m_+(s)-m_-(s)=2\delta R(s).
\]

The equality and non-equality assertions follow from the explicit roots and
the absence of nonnegative poles. The boundary vectors are cyclic: their
Krylov matrices are diagonally weighted Vandermonde matrices with nonzero
determinant. Explicitly the squared determinant is

\[
\Big(\prod_jw_j^\pm\Big)\prod_{i<j}(a_j-a_i)^2>0.
\]

Thus no dark mode explains the alias. The sources are not equivalent as
pointed self-adjoint pairs, since an intertwining unitary preserving b would
preserve the complete scalar response, which differs. Varying t in
`[-δ,δ]` in `wj(t)=1/r+t cj` produces the claimed continuous fiber.
For rational sj and aj, all coefficients and weights are rational, though
boundary-vector square roots need not be rational. QED.

The diagonal representation is only a convenient proof representation.
Gram–Schmidt on its cyclic Krylov sequence yields a connected positive
definite Jacobi realization of each source. H2 is **not** a theorem that those
Jacobi realizations belong to the unit-capacitance, single-end-grounded path
class of SBK-01; no such promotion is made. With poles at least 2, the derived
responses Y±=1−m± are positive on s≥0 and inherit the exact alias, but that
alone is not a full source-passport derivation of a particular RC circuit.

**Concrete check.** For the single sample s=0 and poles `(2,3,4)`, the weights
are `(5/18,1/2,2/9)` and `(7/18,1/6,4/9)`. Both m(0)=13/36; their difference
at s=1 is 1/540. The independent holdout splits an exact, not noisy, alias.

This does not weaken the 2d+1 identity theorem: its degree bound is a different
load-bearing assumption. It proves that an arbitrary finite probe count gives
no uniform identification over positive cyclic finite systems of unbounded
degree. In the constructed fixed-spectrum family, dimension counting is
replaced by an actual positive one-parameter fiber.

## 5. Stable topology failure retains a quantified noise adversary

For the inherited short/long paths `(1,ε)` and `(1,ε,1)`, put a=s+1+ε.
Direct scalar Schur elimination gives

\[
|Y_{\rm short}-Y_{\rm long}|=\frac{\epsilon^2}{a(a^2-\epsilon^2)}<\epsilon^2
\quad(s\ge0,\ 0<\epsilon<1).
\]

The single response curve equal to the midpoint of the two curves lies within
ε²/2 of both at every nonnegative s. A deterministic error envelope therefore
admits the same whole observed curve under either topology. This makes the
no-uniform-noisy-topology conclusion explicit even for arbitrarily many such
samples, rather than merely claiming a small numerical difference.

## 6. Reproduction and earned state

Run `python -Werror -m unittest discover -s tests -p test_reality_pin_hostile.py -v`.
Eight new tests passed locally. They include exact orthogonal conjugation,
positive grounded component extraction, independent graph/cofactor response
checks, cyclicity, positive finite spectral aliases, held-out discrimination,
a deliberately nonannihilating weight mutation, a wrong-extension-operation
control and the global weak-coupling identity.

- **PROVED:** H1, H2 and the explicit source-operation/measurement-error bounds.
- **REFUTED:** arbitrary graph uniqueness from full scalar response plus
  cyclicity; unrestricted finite-probe identification even with positivity and
  no dark sector; applying the 2r formula after changing the old principal block.
- **EXACT FINITE TESTED:** the eight synthetic tests and 28 inherited tests.
- **CONDITIONAL:** translating observable unitary equivalence to physical
  graph identity requires further source labels or a restricted injective class.
- **UNVERIFIED:** physical measurements, empirical source authenticity,
  complete source-family coverage, academic priority, and Lean certification
  of H1/H2. No alpha, gravity, signed-Weil or RH inference is licensed.

## 7. Cross-lane proof audit and corrections

The new arithmetic, observable-geometry, selection/gluing and quantum/global
manuscripts were independently checked after their initial construction. The
review used their actual formulas and hypotheses, not their authors' summaries.
The following defects or ambiguities were found and repaired before final
integration:

| Location | Initial defect | Accepted correction |
|---|---|---|
| Arithmetic prime horizon | The integral tail estimate was stated for arbitrary real cutoff P≥1. Just below a prime, the included discrete prime mass need not be bounded by an integral beginning at P; for sigma=10 and P near 2 from below the p=2 contribution already defeats that estimate. | Restrict P to an integer ≥1. The implementation already requires integers and now has a rejection control. Using floor(P) would be an alternative bound. |
| Quantum dark-sector Gibbs mass | For arbitrary original (K,b), the numerator of visible Gibbs mass was written Z_K even though K may already have its own dark sector. | Use Z_(K restricted to H_b)/(Z_K+Z_D); specialize to Z_K only when the original pair is cyclic. |
| Noisy Hankel eigenvalue count | An entrywise error bound alone did not say that the measured matrix was Hermitian. | Require Hermitian Hhat or explicitly symmetrize before applying the eigenvalue perturbation theorem. The same entrywise error bound survives symmetrization. |
| Observable functor | “Groupoid of isometric intertwiners” could include non-surjective isometries, which have no inverse. | Use unitary source intertwiners (isometric isomorphisms). |
| Local theorem identifiers | Geometry and gluing both used RP-G1 etc. | Gluing uses RP-L1 etc.; this avoids confusing two different statements while retaining their mathematical content. |

The following load-bearing derivations survived this audit:

1. **Arithmetic norm-resolvent convergence.** The embedded Galerkin resolvent
   identity with `R0−R0,N` is valid. Its two Neumann factors have the declared
   norm bounds. The sharper one-port estimate follows from the exterior
   Schur complement, its lower spectral bound and the full inverse bound;
   it does not require the unbounded exterior block to be a bounded matrix.
2. **Zero-forcing reconstruction.** One forcing step consumes exactly two
   moment orders; the initial order `2(n−|W|)+1` leaves order one on all
   coordinates. The supplied sign passport resolves the square root. The
   stability constants K,J,F correctly bound differences of squares,
   products and triple products, with edge denominators controlled by gamma.
3. **Compact-family learning.** The jointly separating continuous probe
   metric on a compact metric quotient has an inverse modulus, but bare
   compactness does not compute it. The manuscript preserves that distinction
   and supplies a genuinely finite rational subdivision algorithm only for
   its specified one-parameter RC family.
4. **Quantum/source/global scope.** The new interacting Hamiltonian's
   `(1,3)` commutator refutes stationarity of the old arithmetic Gibbs state.
   The repaired state-dependent mirror requires its boundedness/domain gate.
   Labelled word-Gram uniqueness is proved on its dense source orbit; the
   rational all-place Schur identity assumes the shared rational source rather
   than inferring it from unrelated local norms.

No further mathematical error was identified in these reviewed derivations.
This is a scoped paper-proof audit, not independent empirical evidence or a
Lean certificate for the infinite operator, inverse problem or gluing results.
The unresolved scalar cyclicity of the arithmetic K, physical probe access,
unknown-topology source identification and effective multi-parameter noisy
inverse remain explicit open gates.

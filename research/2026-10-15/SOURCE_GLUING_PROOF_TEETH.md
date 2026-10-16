# Operation Proof Teeth: source-relative gluing, Swarms E/F

2026-10-15. Scope: bounded finite interfaces plus paper proofs. **No RH claim.**
Authority vocabulary belongs to the principal's `source_proof_certificate.py`:
`CLASSICAL_IMPORTED`, `PAPER_PROVED`, `LEAN_KERNEL_PROVED`, `EXACT_FINITE_CHECK`,
`TESTED_MODEL`, `UNVERIFIED`, `REFUTED`. This module defines neither a second
authority enum nor a general certificate schema. No theorem here is claimed
`LEAN_KERNEL_PROVED`.

Initial checkout: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-proof-teeth`, branch
`research/succ-yean-proof-teeth-ultra-2026-10-15`, initial HEAD
`0f86ba2478a72bf90cf33a4ee192cb2265d992dd`, initially clean. Other agents subsequently
added their assigned files. This lane writes only `observational_succ/proof_gluing.py`,
`tests/test_proof_gluing.py`, and this dossier; no commits, pushes, agents, or
archival edits were performed by this lane.

Read before implementation: `AGENTS.md`, `docs/METHOD.md`, the import manifest,
`field_limit_trichotomy.py`, `field_limit_compactness.py`,
`source_field_inverse_limits.py`, `tate_adele_quotient_descent.py`, and existing
composition/source kernels in `swarm_categories.py`, `swarm_probability.py`,
`covariant_proof_descent.py`, `recursive_operator_gluing.py`,
`source_field_gluing.py`, `finite_affine_presentation.py`, and
`finite_quotient_retract.py`. The imported archival originals are unchanged.

## PG-ADELE-NONSPLIT — the actual additive quotient has no group section

**PAPER_PROVED**, using the classical finite-adèle source definition. Let
\(A_f=\prod'_p(Q_p,Z_p)\) and \(\widehat Z=\prod_p Z_p\). All arrows below
are additive group homomorphisms unless explicitly called set maps.

First identify the *actual* quotient. For \(a\in A_f\), only finitely many
coordinates are nonintegral. Choose at each such prime its rational fractional
part \(r_p=b_p/p^{k_p}\), with \(0\le b_p<p^{k_p}\), so that
\(a_p-r_p\in Z_p\). Put \(q=\sum_p r_p\). At prime \(p\), every other
summand has denominator prime to \(p\), so \(a_p-q\in Z_p\). Thus
\(A_f=Q+\widehat Z\). A reduced rational integral at every finite prime has
denominator one, hence \(Q\cap\widehat Z=Z\). Consequently the diagonal map
induces an isomorphism \(Q/Z\longrightarrow A_f/\widehat Z\).
Let \(\pi:A_f\to Q/Z\) be the quotient followed by its inverse.

For every positive integer \(n\), \(na=0\) in \(A_f\) implies
\(na_p=0\) in the characteristic-zero field \(Q_p\), hence \(a_p=0\)
for every \(p\), hence \(a=0\). Therefore the **target of a proposed
section**, \(A_f\), is torsion-free. The **domain of that section**, \(Q/Z\),
is torsion: \(n[a/n]=0\). For any homomorphism \(s:Q/Z\to A_f\) and
any \(t\in Q/Z\), choose \(n>0\) with \(nt=0\). Then
\(ns(t)=s(nt)=0\), so \(s(t)=0\). Thus every such homomorphism is zero.
Since \([1/2]\ne0\), \(\pi s\ne\mathrm{id}_{Q/Z}\). The exact sequence

\[
0\longrightarrow\widehat Z\longrightarrow A_f\xrightarrow{\pi}Q/Z
\longrightarrow0
\]

does not split even as abstract additive groups, and therefore not as
topological additive groups. This is an argument about all proposed sections,
not a finite failure of one choice of representative.

**Scope and controls.** Set sections do exist: choose the rational representative
in \([0,1)\) and embed it diagonally. Since \(\widehat Z\) is open, the quotient
is discrete, and this set section is continuous. It is not additive:
two lifts of \([1/2]\) sum to diagonal \(1\ne0\), although their classes sum
to zero. The repository's fractional-part sum is another set lift, with the
same obstruction. `adele_lift_obstruction` returns the class, its exact order,
its rational lift and the nonzero integral multiple of that lift. That finite
receipt rejects the displayed lift only; the preceding torsion proof rejects
every homomorphic section. Replacing the source with the torsion group \(Q/Z\)
itself would allow the identity section, so the torsion-free hypothesis cannot
be replaced by a quotient label or matching finite observations.

Live source: Kedlaya's [Class field theory, Definition 6.1.5](https://kskedlaya.org/cft/sec_adeles.html)
gives the restricted-product definition and the quotient identification. The
source-relative nonsplitting derivation above uses these definitions directly.

## PG-KLEENE — the numbering, decidable tree, and noncomputable paths

**PAPER_PROVED**, relative to the standard classical Turing-machine model and
classical existence reasoning. This proof uses the numbering actually executed
by `field_limit_trichotomy.bounded_binary_turing_diagonal`, not the caller-supplied
synthetic trace in `source_field_inverse_limits.finite_kleene_tree_calibration`.

For arbitrary \(e\in N\), invert Cantor pairing
\(e=(a+b)(a+b+1)/2+b\). Set \(s=a+1\), \(r=4s+2\), and let the table
entry at state \(u<s\), scanned symbol \(v\in\{0,1\}\), be
\(d_{u,v}=\lfloor b/r^{2u+v}\rfloor\bmod r\). Entries 0 and 1 halt with
that output. Each remaining entry has the unique form

\[
2+u'+s\delta+2s w,
\quad u'<s,\quad \delta,w\in\{0,1\}.
\]

It writes \(w\), moves left for \(\delta=0\) or right for \(\delta=1\),
and changes state to \(u'\). Initially the head and state are zero, cells
\(0,\ldots,n-1\) contain ones, and all other cells contain zeros on a two-way
tape. This defines \(\varphi_e(n)\), with divergence if no halting entry is
reached. The checked code executes its diagonal \(n=e\).

Every table with \(s\) states has the integer encoding
\(b=\sum_{u,v}d_{u,v}r^{2u+v}\), and therefore occurs at the Cantor index
of \((s-1,b)\). Duplicate encodings are harmless. The classical model-equivalence
import is explicit: unary-input, finite-state, two-symbol, two-way tape machines
with bit halts represent all partial computable maps \(N\rightharpoonup\{0,1\}\).
Finite tape alphabets are encoded by fixed-size binary blocks, with finite-state
scanning of each block; the input conversion and bit-output halts are effective.
No oracle or acceptable-numbering property beyond this coverage is needed in
the argument. The local enumeration-to-table map above is what ties that
classical import to this particular implementation.

Define a binary tree by the *unbounded mathematical recurrence*:

\[
\sigma\in T\ \Longleftrightarrow\
\forall e<|\sigma|,\quad
\bigl(\varphi_e(e)\text{ halts within }|\sigma|\text{ steps with }b\bigr)
\Longrightarrow\sigma(e)\ne b.
\]

1. **Decidable membership.** Run finitely many machines for the explicitly
   bounded number of steps. A step count of zero makes no transition; each
   lookup, including a halting lookup, costs one step, matching the source code.
2. **Prefix closure.** If a prefix of length \(m\) violates a constraint, that
   machine also halts within every larger length \(n\), with the same output.
   Thus no accepted length-\(n\) word can have that rejected prefix.
3. **Every level inhabited.** At length \(n\), complement every output observed
   within \(n\) steps, and assign zero to unresolved coordinates. No two
   constraints address a coordinate inconsistently because execution is
   deterministic. This constructs a level member, not a coherent path selector.
4. **An infinite path exists.** Classically define \(p(e)=1-b\) when
   \(\varphi_e(e)\downarrow=b\), and \(p(e)=0\) if it diverges. Each prefix
   lies in \(T\). Equivalently, the infinite binary tree admits a path by
   classical König's lemma. The definition does not supply a halting algorithm.
5. **No path is computable.** If a path \(p\) were a total computable bit
   function, numbering coverage supplies \(e\) with \(\varphi_e(n)=p(n)\)
   for every \(n\). Its computation on \(e\) halts in some finite time \(t\).
   At length \(N\ge\max(e+1,t)\), the tree requires
   \(p(e)\ne\varphi_e(e)=p(e)\), a contradiction.

**Implementation boundary.** The shipped simulator caps indices at 65,535 and
steps at 4,096; membership and our receipts cap word length at 64. The recurrence
above extends the same table semantics to all finite indices and times. The
unbounded theorem is not a claim that a capped Python function decides every
tree word, nor that finite runs prove universality. A finite supplied trace
instead imposes only finitely many diagonal exclusions; complement those finitely
many bits and put zero elsewhere to obtain a computable path. Such traces cannot
prove the no-computable-path theorem.

**Execution evidence.** The new test uses independent table decoding by repeated
division and an explicit marked-tape set, compared against the actual interpreter
at 96 indices and five time budgets. It also checks all binary words through
length seven for prefix closure, and real level receipts through depth 64.
Machine 0 excludes the constant-zero path. Machine 35 has one state and table
integer 7, whose radix-six digits are both 1; it excludes the constant-one path
by level 36. These are calibration instances, not the diagonal proof itself.

Live references: [Terwijn's computability syllabus, Proposition 7.2.3](https://www.math.ru.nl/~terwijn/teaching/syllabus.pdf)
states the classical Kleene-tree result using inseparable c.e. sets;
[MIT's Turing-machine lecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c10/c10s1/)
explains effective machine enumeration and universal simulation. Terwijn's PDF
timed out in the web reader but was fetched read-only by `urllib.request`
(HTTP 200, 1,228,922 bytes) and piped in memory to `pdftotext`; no source file
was written. The proof above derives the specific diagonal tree from the local
numbering rather than substituting the syllabus's construction.

## PG-DENSE-POSITIVE — positive compressions transport under stated assumptions

**PAPER_PROVED, conditional theorem.** Let \(H\) be a real or complex Hilbert
space; let \(A:H\to H\) be one bounded self-adjoint operator, with
\(\|A\|\le M<\infty\). Let \(P_n\) be increasing finite-rank orthogonal
projections with dense union of ranges. The supplied finite forms must actually
be the compressions of this same \(A\), in the declared metrics and bases.
Then

\[
A\ge0\quad\Longleftrightarrow\quad
\forall n\ \forall y\in P_nH,\ \langle Ay,y\rangle\ge0.
\]

Density and nesting imply \(P_nx\to x\): approximate \(x\) by a vector in
one range and use the best-approximation property of all later projections.
For \(q(x)=\langle Ax,x\rangle\), Cauchy–Schwarz gives

\[
|q(x)-q(y)|\le M\|x-y\|(\|x\|+\|y\|).
\]

Thus \(q(P_nx)\to q(x)\); a limit of nonnegative real values is nonnegative.
The converse follows by restriction. No invariance \(AP_n=P_nA\) is needed.
A strict negative \(q(x)=-\eta<0\) gives a negative finite compression once
\(2M\|x\|\|x-P_nx\|<\eta\). This is an existence statement; effective
search additionally requires an effective dense family and convergent certified
evaluations. Neither a uniform witness depth nor a decision procedure for
universal positivity follows.

For finite coordinate inclusions \(J_n\), the correct checked square is
\(J_n^*A_{n+1}J_n=A_n\), with \(J_n^*J_n=I\). Requiring
\(A_{n+1}J_n=J_nA_n\) would wrongly remove legitimate cross interactions.
`PositiveCompressionChain` checks precisely the former, with exact rational
principal minors for PSD. Its matrices use real orthonormal coordinates; Haar
weights, nonorthonormal Gram coordinates, and complex scalar fields require a
separate declared metric/basis transport. Shape equality is insufficient.

**Countermodels, all with explicit receipts.**

- Without density, \(A=\operatorname{diag}(1,-1)\) and repeated projection onto
  the first coordinate have positive compressions forever but \(q(e_2)=-1\).
- Without the all-stage premise, \(A=I-2|e_m\rangle\langle e_m|\) on
  \(\ell^2(N)\) is invisible to the first \(m\) coordinates and negative at
  the next one. The existing `remote_negative_sign_shadow` supplies exact controls.
- Without source identification, report the compressions of \(B=I\) as if
  they came from that \(A\). Every internal test on \(B\) succeeds; the source
  arrow is false. Matching names cannot disprove this substitution.
- Positive generators do not imply positivity on their span:
  \(\begin{pmatrix}1&-2\\-2&1\end{pmatrix}\) has positive diagonal and
  value \(-2\) on \((1,1)\). All principal minors, not just diagonals, matter.
- A singular Schur parent has a range condition: the existing scalar kernel
  gives determinant \(-1/4\) for \(\begin{pmatrix}0&1/2\\1/2&1\end{pmatrix}\),
  despite nonnegative diagonal blocks. Replacing the cross entry by zero passes.

The continuity assumption has a stronger counterexample than a discontinuous
nonlinear form. On \(H=\ell^2(\{0,1,\ldots\})\), define the **self-adjoint**
unbounded diagonal operator

\[
Ae_0=-e_0,\qquad Ae_n=4n^4e_n\ (n\ge1),\qquad
\operatorname{Dom}A=\{x:\sum_{n\ge1}n^8|x_n|^2<\infty\}.
\]

Self-adjointness follows directly by testing the adjoint against each coordinate:
its domain is exactly the vectors for which the displayed diagonal product
belongs to \(\ell^2\), the same domain. Put
\(v_n=e_0+e_n/n\), \(D=\operatorname{span}\{v_n:n\ge1\}\). A finitely
supported vector belongs to \(D\) exactly when \(x_0=\sum_{n\ge1}n x_n\).
Since \(\sum n^{-2}\le2\), Cauchy–Schwarz implies on \(D\)

\[
|x_0|^2\le2\sum n^4|x_n|^2,\qquad
q(x)=-|x_0|^2+4\sum n^4|x_n|^2\ge0.
\]

Yet \(D\) is Hilbert-norm dense: \(v_n\to e_0\), and for fixed \(k\),
\(k(v_k-v_n)\to e_k\). Orthogonal projections onto
\(\operatorname{span}(v_1,\ldots,v_n)\) therefore increase strongly to \(I\),
and every compression of the *same* \(A\) is positive. Nevertheless
\(q(e_0)=-1\). The continuity step fails:
\(\|v_n-e_0\|=1/n\) but \(q(v_n)=4n^2-1\).
Hilbert-norm density is not a graph/form-core theorem. The finite tests check
the exact Gram entries \(q(v_i,v_j)=4i^2\delta_{ij}-1\); they are explicitly
nonorthonormal coordinates, not inputs to the orthonormal compression API.

For terminology on domains and bounded versus unbounded self-adjointness see
[Dyatlov, §16.3](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
The density proof, inequality, and diagonal counterexample above are explicit
derivations; the citation is not used to assert positivity of any Weil source.

## PG-COMPUTABLE-ROOT2 — correction to inherited P5

**REFUTED:** the claim in
`SUCC_CARRIER_FOUNDATIONS_SYNTHESIS.md`, P5, lines 65–66, that the
\(\sqrt2+ir\) specimen witnesses noncomputable points, when \(r\) is the
rational input of `complex_cauchy_edge.py`. The synthesis is preserved unchanged.

**PAPER_PROVED correction.** The actual constructor is integer-square-root
enclosure (an effective bisection algorithm would work too). At precision \(k\),
let \(D=10^k\), \(a=\lfloor\sqrt{2D^2}\rfloor\). Exact integer arithmetic
computes \(a\), and

\[
a/D<\sqrt2<(a+1)/D,\quad
|(a/D+ir)-(\sqrt2+ir)|<10^{-k}\le2^{-k}.
\]

Taking decimal precision equal to the requested binary accuracy gives a
computable Cauchy modulus. `GaussianCauchyRoot2.imaginary` is a `RationalSpan`,
so the imaginary coordinate is exactly computable as well. The shipped API's
100-digit safety cap is an execution limit, not noncomputability of the
mathematical recurrence. The parity proof establishes \(\sqrt2\notin Q\),
therefore \(\sqrt2+ir\notin Q(i)\); it does not establish noncomputability.

Replacement wording: **“The exact computable Cauchy name for \(\sqrt2+ir\),
with rational \(r\), and the parity irrationality argument witness that
\(Q(i)\) is properly contained in its metric completion. They do not exhibit
a noncomputable point.”** Noncomputable complex points require a different
argument (for existence, countability of programs versus uncountability), or a
different explicitly noncomputable construction. No such claim is supplied by
this specimen. New tests replay rational imaginary parts \(0,3/7,-4/9\) at
precisions \(0,1,7,31,100\) and check the exact binary-error bound.

## F: three analytic composite recipes, with categories and unpaid premises

These are mathematical dependency graphs for the principal's manifests.
**Analytic recipe execution is unsupported by `proof_gluing.py`.** The finite
grammar cannot parse these graphs, check arbitrary theorem texts, discharge
debts from keywords, or manufacture a Hilbert-space proof. Rankings below use
the displayed proved lemma or counterexample, not numerical enthusiasm scores.

### Rank 1: PG-BOUNDED-DECODER — factorization followed by continuous extension

Input category: real or complex Hilbert spaces and bounded linear operators;
one source \(H\), observation \(O:H\to\mathcal A\), target \(h:H\to\mathcal B\).
Output: a unique bounded linear decoder
\(d:\overline{\operatorname{ran}O}\to\mathcal B\), with \(dO=h\).

```text
One source H with bounded O:H→A and h:H→B
       │ uniform domination, every x: ||hx|| ≤ C ||Ox||, C finite
       ▼
ker O ⊆ ker h ──→ d0:ran O→B, d0(Ox)=hx, ||d0||≤C
       │                    │ B complete, norm-continuous extension
       │                    ▼
       └──────────────→ d:closure(ran O)→B, dO=h, ||d||≤C

Uniformly bounded, source-compatible restrictions on a dense union
       │ continuity of the SAME O and h
       └──────────────→ the all-x domination premise
```

**PAPER_PROVED iff.** Such a bounded decoder exists iff some finite \(C\ge0\)
satisfies \(\|hx\|\le C\|Ox\|\) for every \(x\in H\). Necessity follows
from \(h=dO\). For sufficiency, if \(Ox=Oy\), domination at \(x-y\) gives
\(h(x-y)=0\), so \(d_0(Ox)=hx\) is well-defined and linear. The same
inequality bounds its norm by \(C\). For \(a\in\overline{\operatorname{ran}O}\),
choose \(a_j\in\operatorname{ran}O\) with \(a_j\to a\). Then \(d_0a_j\)
is Cauchy; completeness of \(\mathcal B\) supplies its limit. The bound makes
the limit independent of the approximating sequence, bounded, and linear.
Density gives uniqueness. This includes \(O=0\), when domination forces \(h=0\)
and the decoder's domain is \(\{0\}\).

Squaring and using adjoints gives the equivalent operator inequality

\[
h^*h\le C^2 O^*O,
\]

because its quadratic form is \(C^2\|Ox\|^2-\|hx\|^2\).
If increasing source subspaces \(H_n\) have dense union, restrictions really
are \(O|_{H_n},h|_{H_n}\) (or are transported to them by compatible isometries),
and the **same** finite \(C\) works for every \(n\), then taking \(x_j\to x\)
in the union and using continuity of \(O,h\) extends domination to all \(H\).
This is also an application of PG-DENSE-POSITIVE to \(C^2O^*O-h^*h\).

**REFUTED finite-to-continuous shortcut.** On \(\ell^2(N_{\ge1})\), take
\(Oe_n=e_n/n\), \(h=I\). Both are bounded and \(O\) is injective with
dense range. On the first \(N\) coordinates, the observation is invertible and
the exact decoder is \(\operatorname{diag}(1,2,\ldots,N)\), norm \(N\).
A global bound would imply \(1\le C/n\) for every \(n\), impossible.
The decoder on \(\operatorname{ran}O\) exists algebraically but is unbounded;
equivalently, \(Oe_n\to0\) while \(he_n\not\to0\).
The finite test checks \(16O^*O-I\): positive through dimension four,
negative at dimension five. Each restriction factoring is therefore insufficient.

Dependencies/debts: actual source maps, linearity, correct norms, boundedness of
\(O,h\), completeness of the output, dense/coherent restrictions, and one
uniform all-stage bound. `minimal_observation.py` and
`OriginalSourceSquare.decoder` check finite fiber factorization; their finite
success cannot discharge these analytic premises. This recipe ranks first
because the exact necessary-and-sufficient bridge and the sharp counterexample
are both fully supplied here.

### Rank 2: finite Haar quotient to Hilbert completion

Input category: finite cyclic probability spaces \(Z/nZ\), with normalized
counting/Haar measure, divisibility quotient maps, and source-bound function
spaces \(H_n=L^2(Z/nZ)\). Output category: Hilbert spaces and bounded linear
maps, with limit \(L^2(\widehat Z,\mu_{\rm Haar})\).

```text
Z/mZ → Z/nZ, n|m, k=m/n; normalized Haar source measures
       │ pullback U, fiber average E=(1/k)sum
       ▼
H_n --isometric U--> H_m; U*=E, EU=I, UE orthogonal projector
       │ common-refinement compatibility on all divisibility stages
       ▼
directed union of cylinder functions with one consistent inner product
       │ Hilbert completion + source Haar measure + cylinder density
       ▼
L²(Zhat,Haar); cofinal projections P_(n_j) → I strongly
```

Finite proof: \(\|Uf\|_{H_m}^2=m^{-1}k\sum_{r<n}|f(r)|^2
=\|f\|_{H_n}^2\); direct summation gives \(U^*=E\), \(EU=I\).
Thus \(UE\) is self-adjoint idempotent. On a cofinal divisibility chain
(e.g. factorial moduli), cylinder functions embed coherently into the actual
Haar \(L^2\) space. They are dense: locally constant functions separate profinite
points and uniformly approximate continuous functions; continuous functions
are \(L^2\)-dense for the finite regular Haar measure. Completion yields the
claimed Hilbert space; the dense-projection proof above gives strong convergence.
These are classical analytic hypotheses/proofs, not conclusions from a finite
list of vectors. The counting metric in `FiniteQuotientRetract` is distinct:
there \(U^*=\mathrm{sum}\); normalized Haar changes the adjoint to the average.
`profinite_hilbert.HaarCylinder` supplies A's source-indexed finite realization.

**Cross-stream restriction, PAPER_PROVED finite lemma.** For
\(M_{c,b}f(x)=f(cx+b)\), averaging across \(m\to n\) satisfies
\(E M_{c,b}^{(m)}=M_{c,b}^{(n)}E\) for every finite function iff
\(\gcd(c,k)=1\). Each fiber is \(x+n j\), \(j\in Z/kZ\).
The left side averages over \(cx+b+cnj\); the right averages over
\(cx+b+nj\). These multisets agree iff multiplication by \(c\) permutes
\(Z/kZ\). If \(g=\gcd(c,k)>1\), use the delta at \(b\): at coarse
coordinate zero the averages are \(g/k\) versus \(1/k\), proving necessity.
Nonunit on the entire carrier is not the criterion: \(6\to2,c=2\) commutes,
whereas \(4\to2,c=2\) does not. For the latter with \(b=1\), the exact
vectors are \((1,0)\) and \((1/2,1/2)\). Tests reuse the existing quotient
kernel; A's `finite_commutation_witness` supplies the general finite interface.

Dependencies/debts: correct normalized measure, every quotient/source square,
cofinality, identification with actual Haar space, and classical density/completion.
Strong convergence must not be upgraded to operator-norm convergence: a character
of conductor \(2n\) is unit norm and annihilated by \(P_n\), so
\(\|I-P_n\|=1\). This recipe has an established classical completion theorem
and executable finite maps, but no claim of physical or Weil-source identification.

### Rank 3: signed Schur reduction to parity blocks

Input category: source-identified self-adjoint block forms on
\(L\oplus H\), and compatible orthogonal parity involutions. Output:
self-adjoint forms \(S_+,S_-\) on the low parity subspaces, with a
**conditional** equivalence between their positivity and full positivity.

```text
Actual signed G = [[L0, B*], [B, H0]], same source/test domain
       │ H0 ≥ αI, α>0, OR a separately proved singular/closed-form theorem
       ▼
S = L0 - B* H0^(-1) B          [invertible case only]
       │ parity R_L,R_H; H0 R_H=R_H H0, R_H B=B R_L, L0 R_L=R_L L0
       ▼
S R_L=R_L S → S=S_+ ⊕ S_-
       │ prove BOTH original signed low forms ≥0
       ▼
G ≥0  [conditional on all preceding domain/source/range hypotheses]
```

For bounded \(H_0\ge\alpha I>0\), completing the square gives

\[
\langle G(x,y),(x,y)\rangle
=\langle Sx,x\rangle+
\langle H_0(y+H_0^{-1}Bx),y+H_0^{-1}Bx\rangle.
\]

Hence \(G\ge0\) iff \(S\ge0\). Parity covariance and commutation of
\(H_0^{-1}\) with \(R_H\) imply \(SR_L=R_LS\); orthogonal even/odd
eigenspaces remove mixed terms, so \(S\ge0\) iff both parity blocks are PSD.
These algebraic implications are **PAPER_PROVED**. Their application to an
unresolved original low form is **UNVERIFIED** until its hypotheses and signs
are supplied. `suzuki_moment_schur.parity_blocks` checks actual off-parity zeros;
it does not erase nonzero entries. D's `exact_parity_four` reuses this gate.

Singular finite replacement: require \(H_0\ge0\),
\(\operatorname{ran}B\subseteq\operatorname{ran}H_0\), then use the
Moore–Penrose Schur form. Infinite nonclosed ranges need a separate variational
or closed-form theorem; a finite pseudoinverse is not that theorem. In particular,
\(H_0\ge\kappa K\) with compact positive \(K\) does **not** supply
\(H_0\ge\alpha I\) or a bounded inverse at zero. This matters to the actual
Suzuki high-sector bounds. The original low signed Schur sign is not assumed.

Controls: the singular \(2\times2\) example above violates the range condition;
\(\begin{pmatrix}1&2\\2&1\end{pmatrix}\) violates parity covariance, and
discarding its cross term would turn an indefinite form into a positive one.
The tests reject both. Ranking is lowest because the source-specific low-sign
debt remains, even though the conditional reductions are mathematically valid.

## Source/compactness boundaries and provenance audit

The actual compactness theorem needs one compact source, closed fibers, and the
finite intersection property for **every** finite subfamily. Compactness supplies
existence, and a separating observation family supplies at most one source.
Neither premise is established by a finite successful prefix. Controls reused:

- \(X_n=\{m\in N:m\ge n\}\) with inclusion maps: every finite horizon has
  a witness, but the inverse limit would require one fixed \(m\ge n\) for all
  \(n\), impossible. Alternatively, arbitrarily long strictly descending finite
  natural sequences have no infinite extension. Noncompactness/infinite branching
  blocks the compactness shortcut.
- The profinite point with \(2\)-adic coordinate 1 and every odd-prime coordinate
  zero has an integer CRT representative for every finite residue window but no
  single integer representative globally. An integer with zero \(3\)-adic
  coordinate must be zero, contradicting its \(2\)-adic coordinate. This is
  \(\forall n\exists m_n\), not \(\exists m\forall n\).
- Under even-coordinate-only reports, the fixed histories \(000\ldots\) and
  \(0101\ldots\) are permanently indistinguishable. Full coordinate projections
  separate them. This is a different failure from a changing CRT representative.
- Two joint laws on report/post-state pairs can both have uniform marginals:
  mass \(1/2\) on \((0,0),(1,1)\) versus on \((0,1),(1,0)\).
  `check_same_joint_law` rejects the coupling substitution exactly.

Aletheia application: the live gap was whether finite source contracts license
global conclusions. The decisive probes change source, epoch, observer closure,
metric, range, density, or continuity while preserving misleading finite reports.
κ/contact is actual local code execution and read-only live mathematical sources;
φ is scoped finite survival or the stated paper theorem; σ remains an unresolved
source-identification obligation when the intended physical/Weil map is absent.
ρ is the research commitment, with no evidentiary weight. The independent TM
implementation uses different decoding but the same specification; it is not
an independent theorem or source family. Literature, derivations, and tests are
tracked separately. No phasors, truth probabilities, or quantum speedup are used.

## Stable module API and principal replay boundary

| API | Exact executable scope | Retained debt |
|---|---|---|
| `FiniteObject(source, carrier, size)` | Existing `FieldSourcePassport`; finite named carrier | Source labels are declarations |
| `LawfulOperation(before, after, instrument)`, `.identity(obj)`, `.then(after)` | Existing `InstrumentArrow`; all transitions/reports; exact middle object | `SOURCE_IDENTIFICATION` |
| `CommutingSquare(top,right,left,bottom)` | Both composites agree on every source state and ordered report word | `SOURCE_IDENTIFICATION` |
| `SourceKernel(source,kernel)`, `.then(after)` | Existing `StochasticInstrument`; full joint report/post-state law; epoch guard | `SOURCE_IDENTIFICATION` |
| `check_same_joint_law(actual,proposed)` | Exact normalized joint-law equality, independent of row ordering | Does not check physical origin or equality of costs |
| `CompressionStage(source,operator,basis,coefficients)` | Exact real symmetric rational matrix, dimension 1..8 | Declared orthonormal metric/source |
| `PositiveCompressionChain(stages,inclusions)` | 1..16 stages; every PSD principal minor, isometry, compression square | All five enum debts below |
| `kleene_level_receipt(depth)` | Actual bounded TM execution, depth 0..64 | No infinite path or noncomputability certificate |
| `adele_lift_obstruction(coset)` | Existing `FiniteAdeleCoset`; nonzero class/order/lift/multiple | Finite obstruction to the displayed lift only |

The grammar is `op := id(X) | instrument(X,Y,a) | then(op,op)`, with the
existing finite stochastic composer as a separate typed branch. Analytic graphs
above have no execution constructor. Deterministic carriers have at most 256
states; composed report alphabets at most 256 entries and words at most 64
symbols. Stochastic carriers have at most 64 states and rows at most 256 entries;
the Cartesian expansion is bounded before composition. Matrix dimensions and
stage counts are bounded; arithmetic remains exact Python integer/Fraction
arithmetic, with cost depending on input bit lengths, not a unit-cost promise.

`PositiveCompressionChain.unresolved_debts` always returns:
`SOURCE_IDENTIFICATION`, `COMMON_OPERATOR`, `BOUNDED_SELF_ADJOINT`,
`DENSE_PROJECTORS`, `ALL_STAGE_POSITIVITY`. There is no caller boolean or
constructor argument to empty these debts. This is a shape/source/debt checker,
not a semantic theorem validator or portable authenticated proof object. The
principal should replay primitive input tables/matrices and finite constructors,
not trust a serialized receipt label or another module's self-reported boolean.
`KleeneLevelReceipt` and `RationalLiftObstruction` are numerical witness records,
not rival capsule manifests.

## Validation receipts and claim ledger

Python **3.12.3**; commands executed in the shared isolated checkout. Each command
was prefixed `PYTHONDONTWRITEBYTECODE=1`.

| Command | Actual result |
|---|---|
| `python -m unittest discover -s tests -p 'test_field_limit_trichotomy.py'` | Baseline: 14 tests, 0.006s, exit 0 |
| `python -m unittest discover -s tests -p 'test_proof_gluing.py'` | Final focused run: 34 tests, 0.037s, exit 0 |
| `python scripts/verify_provenance.py` | 72 items: 17 byte-identical archives, 55 mechanical migrations; exit 0 |
| `python scripts/observer_foundations_probe.py` | Real probe completed, exit 0; retained missing source/analytic bridges |
| `python scripts/ordinal_succ_report_probe.py` | Real probe completed, exit 0; global PSD and Weil identification still unproved |
| `python -m unittest discover -s tests -p 'test_*.py'` | PID 1852849: 4,392 tests, 463.477s, exit 0 |

The full-suite run began before the final four focused tests were added and
while other agents were editing their authorized paths. It is a receipt for
that discovery/run, not a frozen final integration snapshot. The final 34-test
focused run covers this lane's final code and tests. No full-suite repeat was
launched; principal owns final integration/CI. Two pre-existing invalid-escape
SyntaxWarnings appeared during full discovery, in `apollo_source_first_interference.py`
and `tate_finite_bruhat_observers.py`; neither was a test failure or edited here.

Test history is preserved: the first 30-test run passed; adding the P5 correction
gave 31 passes. Adding the three recipe controls initially produced one failure
in 34 tests because this lane wrote the wrong second coordinate for the Haar
defect. Execution returned \((1/2,-1/2)\), consistent with direct fiber counting.
The expected fixture and explanatory comment were corrected; all 34 then passed.
No product logic or mathematical gate was weakened to obtain that pass.

| ID | Status | Exact claim/boundary | Next falsification opportunity |
|---|---|---|---|
| PG-ADELE-NONSPLIT | PAPER_PROVED | No additive group section for actual \(A_f\to Q/Z\) | Attempt a torsion lift in the actual characteristic-zero product |
| PG-KLEENE | PAPER_PROVED | The specified unbounded machine-tree has paths but no computable path | Audit numbering coverage or exhibit a contradiction in the diagonal argument |
| PG-DENSE-POSITIVE | PAPER_PROVED | Positivity equivalence under common bounded self-adjoint source and dense projectors | Challenge a premise; explicit missing-premise countermodels supplied |
| PG-BOUNDED-DECODER | PAPER_PROVED | Bounded decoder iff uniform domination, equivalently operator inequality | Test domination on omitted source directions |
| PG-COMPUTABLE-ROOT2 correction | PAPER_PROVED | Exact rational-imaginary specimen is computable and outside \(Q(i)\) | Break the integer-square-root bound/modulus |
| Inherited P5 noncomputability implication | REFUTED | Irrationality of that specimen does not imply noncomputability | Requires a different specimen, not more precision |
| Finite gluing guards | EXACT_FINITE_CHECK | Complete declared finite tables, exact rational instances, tested mutants | Alter a source epoch, coupling, minor, inclusion, or report |
| Analytic recipe execution | UNVERIFIED | Unsupported by finite grammar; no theorem-text checker | Separate proof terms and authenticated source transports |
| Full signed source/Weil positivity | UNVERIFIED | No original low-sign theorem or universal RH implication supplied | Resolve actual low signed form with valid range/domain/source proofs |

Source bytes inspected before adding (SHA-256; existing code not edited by this lane):

```text
62d178255fd3d42fdbee0e0537430fe7e6366f2e0ca43f1886c67941cf6756d0  field_limit_trichotomy.py
aeaf5849416522d98e2c394e45b600f2a7dd9dcc6c6975debf53fa9dc9a92c4f  field_limit_compactness.py
090a375b4b83b7cfb1a44632dd381632ec3ecc40d6a11c2a0652bce91be15126  source_field_inverse_limits.py
3ec27299a4022fa359b699fd6337924bef8936a59194b0c45ecae38041a14555  tate_adele_quotient_descent.py
2eac9c52cd3ae1beb497282feb62faf87f83cf605eb528c3116a57cf3899dd5c  swarm_categories.py
5de26231d72e20dbed0a747a1dcec128b47d12125b2194d861bc943755e79466  swarm_probability.py
0dda6bdf871dfdefffe48649c785ab9d18addab6cea5553ac1d4472a3094fd94  recursive_operator_gluing.py
03863db05cea79f7aadf183b7f8c73f6a8899924f890c54f4ac2f29fc232ff29  source_field_gluing.py
```

The founding import receipt identifies commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; it authenticates archival provenance,
not the truth of these new theorems. The proofs, finite receipts, and unresolved
source debts remain separate inputs to the principal's capsule verifier.

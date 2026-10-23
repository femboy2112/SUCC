# Reality Pin: from boundary histories to observable geometry and labelled graph rigidity

**Date:** 2026-10-22. **Source baseline:** PR #243,
`d2f760ab9d9a11719e950caeb2d54bfa5114f495`.
**Truth state:** finite-dimensional paper proofs, with independent exact rational
controls; no Lean admission claimed in this file. No physical measurement.
Classical minimal-realization, Krylov and graph-infection mathematics is
attributed below. Academic novelty is **UNVERIFIED**, not a premise.

## Hole contract and verdict

The missing edge is not “a boundary response reconstructs every interior.”
That statement is false. The precise target is:

> For a finite source-selected self-adjoint operator and a calibrated multiport
> boundary, identify the exact invariant fixed by all return histories. Then
> give explicit additional source conditions under which that invariant fixes
> the original labelled graph operator, with a finite observation-order budget
> and a conditioned error estimate.

The weakest useful first statement is uniqueness on the boundary-generated
subspace. The stronger source-coordinate statement below assumes a **known
labelled graph**, known edge signs, and a zero-forcing boundary set. These are
independently supplied passports, not information created by the response.
A connected dark star, boundary-fixing orthogonal changes of basis, weak links,
wrong signs and cancellation of shortest walks are preregistered falsifiers.
The proof languages are Gram quotients and induction on graph infection.
All executable controls are finite rational algebra; universal claims use the
proofs below. The next lamp is a source-justified way to establish the graph
passport independently, or to relax it while retaining a separating response.

## 1. Source, probe and exact observable equivalence

Let `H` be a finite-dimensional complex Hilbert space, `A=A*` on `H`, and
`B:C^m -> H` a fixed boundary injection (not necessarily isometric). Assume
all relevant matrices, units, boundary order and source epoch are fixed.
Define

\[
M_k=B^*A^kB,\qquad R(s)=B^*(A+sI)^{-1}B,
\quad s\notin-\operatorname{spec}(A),
\]
\[
\mathcal K_r=\operatorname{span}\{A^jBu:0\le j<r,\ u\in\mathbb C^m\},
\qquad\mathcal K=\bigcup_r\mathcal K_r.
\]

For positive operators it suffices to know the rational response on `s>0`.
For general self-adjoint operators use any open nonpole interval. Equality
there implies rational equality, hence equality of all Laurent coefficients
`(-1)^k M_k` at infinity. Conversely equal moments give equal responses by
the convergent Neumann series for `|s|` larger than both operator norms and
then rational identity. This is a mathematical all-response premise, not an
assertion that infinitely many physical measurements occurred.

**RP-G1 — observable quotient theorem (PROVED, classical).** Two finite
self-adjoint pairs `(A,B)` and `(A',B')` have the same boundary response iff
there is a unique unitary

\[
U:\mathcal K(A,B)\longrightarrow\mathcal K(A',B'),\qquad
UB=B',\quad UA|_{\mathcal K}=A'|_{\mathcal K'}U.
\]

**Proof.** Define on polynomial boundary histories
`U(sum_j A^j B u_j)=sum_j A'^j B' u_j`. Inner products of two such histories
are `sum_(i,j) u_i^* M_(i+j) v_j`. Equal moments preserve them, so zero-norm
relations are preserved and this definition is well-defined and isometric.
Its image spans `K'`, so it is onto. It intertwines `A` by shifting powers
and fixes the boundary by taking degree zero. The spanning property gives
uniqueness. Conversely the unitary intertwiner transports every moment and
the response. Finally `K` is invariant under `A` (Cayley–Hamilton), and
self-adjointness makes `K^perp` invariant too; `B^*` vanishes on that
orthogonal summand. Thus the full response cannot constrain its operator.
QED.

This is **unitary** uniqueness on Hilbert realizations, stronger than arbitrary
similarity but weaker than labelled physical graph uniqueness. The unitary
need not permute spatial sites, preserve locality, preserve a graph zero
pattern, or intertwine separately named SUCC/FUCC operations.

The theorem also gives an actual functor on the groupoid of unitary source
intertwiners: restrict `U` to `K`. Restriction respects identity/composition,
maps `A^jB` to `A'^jB'`, and preserves each filtration stage. A map that merely
matches a scalar response value is not a morphism of this source groupoid.

## 2. Intrinsic filtration, graded dynamics and finite authority

**RP-G2 — block Hankel and canonical filtration (PROVED).** Let
`K_r=[B,AB,...,A^(r-1)B]`. Its Gram matrix is the block Hankel matrix

\[
H_r=(M_{i+j})_{0\le i,j<r}=K_r^*K_r.
\]

Consequently `rank H_r=dim K_r`; null vectors are precisely zero boundary
history combinations. The quotient of the formal history space by these
null vectors, with the Gram inner product, reconstructs `K_r` isometrically.
Once `K_(r+1)=K_r`, that subspace is invariant and equals `K`. A mere equality
of *sampled* measurements or a noisy rank estimate does not certify the
exact plateau.

Put `E_j=K_(j+1) orthogonal-minus K_j`, where `K_0={0}`. For `x in E_j`,
`Ax in K_(j+2)`, and for `y in K_(j-1)`,
`<Ax,y>=<x,Ay>=0`. Thus

\[
A E_j\subseteq E_{j-1}\oplus E_j\oplus E_{j+1},
\]

with missing endpoint terms zero. The response determines the **graded
Hilbert geometry** and this block-tridiagonal operator up to unitary changes
within each grade. It does not canonically choose a basis in a grade of
dimension larger than one. This is the precise multiport replacement for a
scalar Jacobi chain.

If `B` consists of coordinate vectors on a labelled graph, `K_r` is supported
within graph distance `r-1` of the boundary. Equality with the full space of
those vertices is not automatic: several vertices can contribute only one
visible linear combination. The three-vertex symmetric star with root port
has ranks `1,2,2,...`, despite all three vertices lying at distance at most
one. A vertex coordinate `e_v` can have no finite Krylov depth even though
its graph distance is one. Operational depth is therefore a depth of
**accessible vectors**, not generally a metric on physical sites.

For noise, take the measured matrix `Hhat_r` Hermitian (or symmetrize it first).
If each scalar entry relative to the true `H_r` has absolute error
at most `epsilon`, then
`||H_r-Hhat_r||_2 <= mr epsilon` by the row/column norm bound. If a prior
certifies that every nonzero eigenvalue is at least `nu>0` and
`mr epsilon < nu/2`, exactly the eigenvalues of `Hhat_r` greater than
`nu/2` count the true rank. This follows from the min–max eigenvalue bound.
Without this visibility gap, a positive rank can hide below any error bar.

## 3. The general first-return extension theorem

Consider a finite self-adjoint extension preserving the old principal block,

\[
\widetilde A=\begin{pmatrix}A&C\\ C^*&D\end{pmatrix},\qquad
\widetilde B=\binom B0,
\]

with arbitrary self-adjoint `D`. Define the source-history exit depth

\[
\ell=\min\{j\ge0:C^*A^jB\ne0\}.
\]

**RP-G3 — sharp return order (PROVED).** If `ell` is finite, then

\[
\widetilde M_k=M_k\quad(k<2\ell+2),\qquad
\boxed{\widetilde M_{2\ell+2}-M_{2\ell+2}
=(C^*A^\ell B)^*(C^*A^\ell B)\ne0.}
\]

The first jump is positive semidefinite, with rank equal to the number of
linearly independent first-exit boundary channels. It is independent of
`D`. If `C^*A^jB=0` for all `0<=j<dim H`, the entire extension is invisible
at this boundary for every response parameter.

**Proof.** Expand a block-matrix power into products indexed by whether each
step is in the old or new block. The no-excursion contribution is `M_k`.
Every other word has a first crossing `C^*` after `i` old-block steps and a
last crossing `C` before `j` final old-block steps. It contains factors
`C^* A^i B` and `B^* A^j C`, so it vanishes unless `i,j>=ell`. At least two
crossing steps are required, giving `k>=2ell+2`. At equality there are
exactly two crossings, no new-block dwell and `i=j=ell`; the displayed Gram
is the sole remaining term. It is nonzero because its factor is nonzero.
If all the first `dim H` exit factors vanish, Cayley–Hamilton makes every
later one vanish too; `K(A,B) direct-sum 0` is reducing for the extension
and its response equals the old response. QED.

For an old path with `r` vertices and a single new edge, `ell=r-1` and the
formula is precisely the inherited order `2r` squared-edge-product theorem.
For coordinate boundaries and uniformly negative real off-diagonal entries,
the first nonzero exit order equals the shortest number of old graph edges
to the attachment: shortest-walk products have one common sign and cannot
cancel. Mixed signs, complex phases, or signed boundary superpositions
remove that conclusion while preserving RP-G3.

**Cancellation witness.** Take

\[
A=\begin{pmatrix}4&-1&-1\\-1&2&0\\-1&0&3\end{pmatrix},
\quad B=e_1,\quad C=(0,1,-1)^T.
\]

There is a two-edge route from the boundary to the new vertex, but
`C^*B=C^*AB=0`, `C^*A^2B=1`. The first return jump is at order **6**, not
4, and equals 1. Replacing the last `-1` in `C` by `+1` restores order 4
without changing the graph topology. Replacing both leaf diagonals of `A`
by 3 instead makes the extension forever dark, even though the full graph
is connected. The tests retain both controls.

## 4. Source-coordinate rigidity on zero-forcing graphs

A **graph passport** consists of: a known finite labelled simple graph
`G=(V,E)`, an ordered set of boundary vertices `W`, a fixed nonzero sign
`s_(uv) in {-1,+1}` on each edge, and the coordinate interpretation
`B e_j=e_(W_j)`. The unknown `A` is real symmetric, has nonzero
`A_uv` exactly on the off-diagonal edges of `G`, and has these fixed signs.
Diagonal entries are arbitrary real numbers; positivity can be added but
is not needed in the proof. This is a declared model family.

A colored vertex **forces** its unique uncolored neighbor. `W` is a
zero-forcing set if repeated such steps color all vertices. Fix any valid
schedule before reading weights; its length is `r=n-|W|`.

**RP-G4 — finite moment graph reconstruction (PROVED; classical infection
method, explicit boundary-history version).** For this family, moments

\[
\boxed{M_0,M_1,\ldots,M_{2r+1}}
\]

uniquely reconstruct **every labelled entry of `A`**, with no spectral
simplicity hypothesis. Therefore the complete multiport response is
injective on this family. The bound is sufficient, not claimed minimal.

**Constructive proof.** Suppose moments
`m_k(u,v)=<e_u,A^k e_v>` are known for all currently colored `u,v` through
order `t`, initially `t=2r+1`. If `v` forces `w`, set
`a_i=m_1(i,v)` for all colored `i`. Graph knowledge gives the vector identity

\[
Ae_v-\sum_{i\in W_{\rm current}}a_i e_i=A_{wv}e_w.
\]

Its squared norm is known:

\[
h=m_2(v,v)-\sum_i a_i^2=A_{wv}^2>0.
\]

The passport fixes the sign, so `g=A_wv=s_(wv)sqrt(h)` is uniquely
recovered. For every previously colored `u` and `0<=k<=t-2`,

\[
m_k(w,u)=\frac{m_{k+1}(v,u)-\sum_i a_i m_k(i,u)}g,
\]
\[
m_k(w,w)=\frac{m_{k+2}(v,v)-2\sum_i a_i m_{k+1}(i,v)
 +\sum_{i,j}a_i a_j m_k(i,j)}{g^2}.
\]

These are literal source-vector identities, not eigenvector guesses.
Add `w` to the colored set and continue with `t-2` available orders.
After `r` steps, moments through order 1 are known on all coordinates;
`m_1(u,v)=A_uv` completes the reconstruction. Every quantity is determined
by the original data and passport, proving uniqueness. The same induction
constructs every `e_v` in the boundary Krylov space, so this source class
has no dark sector. QED.

This covers paths, known finite trees with all leaves accessible, and
many cyclic graphs (for example a cycle with two adjacent accessible
vertices). For the tree assertion, root at an accessible leaf. Work upward
from the other leaves: after each child subtree has been processed, a
colored vertex can force its still-uncolored parent because all its child
neighbors are colored. Thus the whole tree is eventually colored. For the
single-vertex tree declare its sole vertex accessible.

This does **not** reconstruct unknown topology. A wrong passport can either
be refuted by the responses or select a different observationally equivalent
interior. The cyclic path/triangle alias in
[the hostile audit](REALITY_PIN_HOSTILE_AUDIT.md) is a decisive
counterexample to silently dropping the known-graph hypothesis. Likewise
signs are load-bearing: `[[3,-2],[-2,4]]` and `[[3,2],[2,4]]` have identical
one-port responses, related by `diag(1,-1)`.

The exact code implements rational matrices. Real nonrational `sqrt(h)`
remains valid in the paper theorem but is deliberately rejected by the
rational oracle instead of being silently rounded.

## 5. Explicit conditioned stability for the finite inverse

**RP-G5 — moment-noise Lipschitz bound (PROVED).** Fix the same passport and
forcing schedule. Let `A,A'` both belong to that family and satisfy
`||A||_2,||A'||_2<=R`, with `R>=1`, and every edge magnitude at least
`gamma`, with `0<gamma<=1`. Suppose every boundary moment entry through
order `L=2r+1` differs by at most `epsilon`. Put

\[
D=R^L,\quad K=1+2nD,\quad J=1+4nD+3n^2D^2,
\]
\[
F=\max\left\{1,\frac K\gamma+\frac{D^2K}{2\gamma^3},
\frac J{\gamma^2}+\frac{D^3K}{\gamma^4}\right\}.
\]

Then

\[
\boxed{\|A-A'\|_2\le nF^r\epsilon.}
\]

**Proof.** At every stage both exact extended moment tables have entries
bounded by `D`, since they are actual coordinate moments of `A,A'`. If
the tables differ entrywise by `delta`, the residual squared edge weights
`h,h'` differ by at most `K delta`. Their signed square roots differ by
at most `K delta/(2 gamma)`. The numerator of a new cross moment differs
by at most `K delta`, and its magnitude in the primed model is at most
`D^2`. Dividing by the two edge weights gives cross-moment error at most
`(K/gamma+D^2 K/(2gamma^3))delta`. The diagonal numerator differs by at most
`J delta` (one raw moment, twice a sum of products, then a double sum of
triple products); its primed magnitude is at most `D^3`. Dividing by
`h,h'>=gamma^2` gives error at most
`(J/gamma^2+D^3 K/gamma^4)delta`. Retained entries change by at most
`delta`. Thus each forcing step multiplies the maximum error by at most
`F`. After `r` steps the reconstructed matrix differs entrywise by at most
`F^r epsilon`; the spectral norm is at most `n` times the maximum entry.
QED.

The bound is intentionally coarse and deteriorates badly as couplings
weaken or the hidden depth grows. If two admissible models both fit a
calibrated moment reading to error `epsilon`, replace the right side by
`2nF^r epsilon`. The data assumption concerns **moments**, not noisy
resolvent samples. Differentiating/analytically continuing noisy samples
to moments has its own conditioning and experimental-access obligations;
no such error conversion is silently asserted.

A separate forward check is immediate: if `A,A'>=aI`, `s>=0`, and the
same boundary matrix is used, the resolvent identity gives

\[
\|R_A(s)-R_{A'}(s)\|\le
\frac{\|B\|^2\|A-A'\|}{(a+s)^2}.
\]

This is a **forward** continuity bound, not an inverse estimate.

## 6. Source provenance, inherited audit and execution

Read-only baseline audit: the inherited path inversion uses known unit
capacitances and source order; its order-`2r` extension keeps the old
principal block unchanged; its Hankel determinant is a Gram determinant;
its `2d+1` rational theorem requires a predeclared degree cap. These proofs
survive this audit. All **28 inherited exact tests passed locally**. No
archival file, existing claim or implementation was changed by this lane.

New files:

- `observational_succ/reality_pin_geometry.py`: rational moment/response,
  block Hankel rank, sharp first-return and graph-passport inverse oracles.
- `tests/test_reality_pin_geometry.py`: **20 test methods**, including all
  **528** zero-forcing boundary subsets of all labelled four-vertex simple graphs,
  literal walk enumeration independent of matrix powers, direct Krylov Gram,
  rational resolvent aliases, cancellation mutants, dark connected/disconnected
  sectors, weak couplings, wrong graphs, signs and malformed exact input.

The universal mathematical claims are the proofs above. Finite enumeration
checks the implementation and catches mutations; it does not establish a
universal graph theorem by itself. Source IDs and graph labels are typed
assumptions; no script authenticates an actual sensor or physical topology.

**Primary literature checked during this round:**

1. D. Burgarth and K. Maruyama, *Indirect Hamiltonian Identification through
   a small gateway*, New J. Phys. 11 (2009), 103019,
   [arXiv:0903.0612](https://arxiv.org/abs/0903.0612).
   The paper's known-graph infection argument motivates RP-G4. Our direct
   finite moment proof states its own real-symmetric/sign assumptions and
   does not import a claim about arbitrary many-body Hamiltonians.
2. M. Guţă and N. Yamamoto, *System identification for passive linear quantum
   systems*, [arXiv:1303.3771v3](https://arxiv.org/abs/1303.3771), especially
   minimal unitary equivalence and infection conditions. RP-G1 is proved
   directly here for finite self-adjoint resolvent pairs, not inferred from
   unverified equality with that paper's open quantum input-output model.
3. PR #243 and its source/receipt at the pinned baseline above; original
   provenance manifest remains untouched. Parent PRs' p-adic, reciprocal,
   thermofield and Tate results are not needed as hidden premises here.

## 7. What geometry earned, and what remains missing

**PROVED:** the response determines a unique boundary-generated Hilbert
realization, canonical filtration and sharp exit/return witness. With a
known graph, fixed signs and zero forcing it determines the original labelled
operator with an explicit finite order budget and a conditioned stability
bound. These are genuine dependency-closing steps beyond the scalar path.

**REFUTED:** unrestricted full-interior inference; graph distance equals
operational depth without a no-cancellation hypothesis; exact mathematical
rank has an unconditional noise margin; edge sign/source orientation can be
omitted without changing the identification problem.

**EXACT FINITE TESTED:** rational reconstruction and hostile controls above.
**CONDITIONAL:** physical realization identification after independent graph,
probe, calibration and source authenticity gates. **UNVERIFIED:** physical
spacetime, geometry of the actual arithmetic operator, and broad unknown-graph
or continuum reconstruction. A continuum transfer may identify a spectral
measure or cyclic operator while leaving its spatial realization ambiguous;
no finite-dimensional proof here silently crosses that boundary.

The decisive next theorem would replace the predeclared topology passport
with a source-accessible intervention language that reconstructs its labels
and zero pattern, while proving a useful noise/complexity bound. Passive
one-port spectroscopy alone cannot do that, even for some fully visible
positive finite RC operators.

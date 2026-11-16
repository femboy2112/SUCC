# A complete SU(2) Wilson observer and its conditioning boundary

Date: 2026-11-13. **Authority:** classical completeness with an elementary
proof, a repository adapter, and a derived conditioned stability estimate.
This is not a claim of new invariant theory, a continuum reconstruction,
or a mass-gap estimate. The finite exact implementation uses rational
quaternions; all paper statements below quantify over real unit quaternions.

## 1. The hole this closes

PR #613 at `a8da424c84869d737462fdec0a64d7921a92eb50` already has the exact
successor/SU(2)-character adapter, source-weighted Haar transforms, finite
quantum graph semantics, and a conditional reflection-positive interface.
PR #614 at `0faa85a798de5b0b9af4d62295f405165b408eb7` proves the finite-graph
gauge quotient and gives an S3 example where individual loop traces miss
their interaction. Its next open adapter asks for a complete compact-simple
mixed-word observer. Here that finite completeness obligation is discharged
for SU(2). No code from the unmerged #614 branch is required.

The relationship to SUCC's higher-arity intuition is exact in this domain:
pair observations recover a Gram matrix; a signed triple observation resolves
the remaining orientation ambiguity. This does not assert a universal
three-channel law for other groups or statistical models.

Primary classical provenance: Florentino, *Invariants of 2 by 2 matrices,
irreducible SL(2,C) characters and the Magnus trace map* (2006),
[introduction, equations (1.1) and the set H_n; Theorem 2.1](https://arxiv.org/html/math/0603049v1).
That source records generation by lexicographically ordered words with at
most three distinct letters. The proof below is self-contained for SU(2);
no complex nonclosed-orbit issue is imported into the compact quotient.

## 2. Exact carrier and observation bank

Write a unit quaternion as q_i = a_i + v_i, with v_i in R^3 and
a_i^2 + |v_i|^2 = 1. The Hamilton convention is ij=k and ijk=-1.
Its defining SU(2) matrix is

\[
 a+bi+cj+dk\longmapsto
 \begin{pmatrix}a+bi&c+di\\-c+di&a-bi\end{pmatrix}.
\]

The normalized trace is tau(q) = Tr(q)/2 = a. For a fixed finite number
b of holonomies, observe the **joint configuration-level bank**

\[
 \Phi(q)=\bigl(\tau(q_i),\ \tau(q_iq_j),\
 \tau(q_iq_jq_k)\bigr)_{i<j<k},
\]

where the first coordinates range over all i, the pair coordinates over
all i<j, and the triple coordinates over all i<j<k. Thus there are
b + binom(b,2) + binom(b,3) coordinates. The empty tuple is allowed.
Index order is part of the observer. All holonomies must be referred to
the same rooted frame: their gauge action is one common conjugation.

Quaternion multiplication gives the exact recovery identities

\[
 d_{ij}:=v_i\cdot v_j=a_i a_j-\tau(q_iq_j),\qquad
 d_{ii}=1-a_i^2,
\]

\[
 D_{ijk}:=\det[v_i\ v_j\ v_k]
 =-2a_i a_j a_k+a_i\tau(q_jq_k)+a_j\tau(q_iq_k)
  +a_k\tau(q_iq_j)-\tau(q_iq_jq_k).
\]

For example, the scalar part of a threefold product is
a_i a_j a_k - a_i d_jk - a_j d_ik - a_k d_ij - D_ijk;
substitution proves the second formula and fixes its sign.

## 3. Completeness, including degenerate ranks

**TO-01 (CLASSICAL, proof reproduced).** For every integer b>=0 and every
q,q' in SU(2)^b, Phi(q)=Phi(q') if and only if there exists g in SU(2)
with q'_i = g q_i g^{-1} for every i.

**Proof.** Conjugation preserves every trace word, proving one direction.
For the other, equality of singles fixes every a_i. Equality of pairs
fixes the entire Gram matrix of the imaginary vectors. The map
sum c_i v_i -> sum c_i v'_i is well-defined: a zero input has squared
norm c^T d c=0, so its proposed image also has norm zero. It is an isometry
between their spans and extends to an orthogonal map R of R^3.

If the common span has dimension three, choose an independent ordered
triple. Equality of its nonzero signed determinant forces det R=+1.
If the span has dimension at most two, a determinant-minus extension can
be composed with a reflection fixing the target span pointwise. This gives
a determinant-plus extension without changing any observed vector.
Every proper rotation of R^3 is realized by conjugation by a unit
quaternion: rotation through angle theta about unit axis u uses
g=cos(theta/2)+u sin(theta/2). Hence a common g exists. QED.

This proves equality of genuine SU(2) orbits, not merely equality under
rational gauge elements. The implementation's rational decision inputs may
require an irrational conjugating quaternion.

**TO-02 (sharp hostile control).** The triples (i,j,k) and (i,j,-k) have
identical singles, pairs, and Gram matrices, but triple traces -1 and +1.
They are not commonly conjugate. Squared triple volumes also fail to
distinguish them. For b<=2, the span has dimension at most two and the
single/pair bank already suffices. The necessity of a triple is therefore
real and correctly localized.

## 4. From this bank to a finite lattice source

Fix a connected finite oriented graph with vertex set V, edge set E, a
root, and a spanning tree. Each edge u->v carries U_e in SU(2), acted on by
g_u U_e g_v^{-1}. Let t_v be the ordered product on the unique root-to-v
tree path, with inverses when a path traverses an edge backwards.
Choosing g_v=t_v makes all transformed tree edges equal to one: the
recursion on a forward tree edge is t_v=t_u U_e. The remaining chord
values h_e=t_u U_e t_v^{-1} are its rooted holonomies.

If the original source is gauge-transformed by k_v, the new tree products
are k_root t_v k_v^{-1}. Consequently every h_e is transformed by the
**same** k_root conjugation. Conversely, common conjugacy of chord tuples
gives gauge equivalence of their tree-fixed representatives. Thus

\[
 G^E/G^V\simeq G^{|E|-|V|+1}/\operatorname{Ad}G.
\]

This short argument is valid for every group G. Applying TO-01 for SU(2)
gives a complete gauge-invariant observer on the finite graph. A chord word
of length three need not be a short geometric path: long tree transports
are retained. No locality estimate is claimed by calling it a short word.

For a finite Wilson cell complex, retain its actual oriented plaquette
words and its source law

\[
 d\mu_\beta(U)=Z^{-1}\exp\!\left(\beta\sum_p
 \tfrac12\operatorname{Tr} U_{\partial p}\right)\prod_e dU_e.
\]

The normalizing convention is that of the parent dossier. A spanning-tree
coordinate change preserves product Haar measure: each leaf elimination
uses left/right Haar invariance and an independent unit-mass tree variable;
induction eliminates every tree edge. A gauge-invariant integrand depends
only on the resulting chord tuple. Therefore its normalized expectation
is exactly the chord integral with the **same transported plaquette action**.
The bank then pushes this law forward to Phi_*mu_beta. It does not replace
that law by uniform trace coordinates or independent holonomies under the
interacting action.

The compact quotient is Hausdorff; Phi is a continuous injection from it
into Euclidean space and hence a homeomorphism onto its image. Every
continuous gauge-invariant observable therefore factors continuously
through Phi. Its expectation is preserved by pushing forward the full law.
This is source-preserving target reconstruction, not merely a list of
visually related observables.

**TO-03 (law-level firewall).** The *means* of this finite bank do not
determine a source law. With b=1, the equally weighted law on {1,-1} and
the point law at i both have mean normalized trace zero; their squared
trace expectations are respectively one and zero. Configuration
completeness is not finite-moment determination of all field correlations.

## 5. A conditioned inverse-stability estimate

All norms below are Euclidean or their induced operator norms. Suppose
the corresponding coordinates of Phi(q) and Phi(q') differ by at most
epsilon>=0. Select one fixed ordered triple r<s<t and set

\[
 A=[v_r\ v_s\ v_t],\quad B=[v'_r\ v'_s\ v'_t],\quad
 s_0=\sigma_{\min}(A)>0,\quad \delta=|\det A|.
\]

**TO-04 (DERIVED, conditioned inverse bound).** If

\[
 \epsilon\le s_0^2/18,\qquad 13\epsilon<\delta,
\]

then some common SU(2) conjugation has, for all i,

\[
 \|q'_i-gq_i g^{-1}\|_{\mathbb R^4}
 \le C(s_0)\epsilon,\qquad
 C(s_0)=1+8/s_0+22/s_0^2.
\]

**Proof.** Each Gram entry changes by at most 3epsilon (diagonals at
most 2epsilon). Therefore Delta=B^T B-A^T A has operator norm at most
9epsilon. The determinant recovery formula changes by at most 13epsilon:
its five summands contribute 6,2,2,2,1 times epsilon. Thus det A and det B
have the same sign. For M=B A^{-1},

\[
 \|M^TM-I\|\le\eta:=9\epsilon/s_0^2\le1/2.
\]

The polar decomposition M=RP has R in SO(3),
||M-R||<=eta, and ||B^{-1}||<=sqrt(2)/s_0. The polar bound follows by
applying |sqrt(1+x)-1|<=|x| for x>=-1/2 to the eigenvalues.
Put d_i=A^T v_i and d'_i=B^T v'_i. The exact identity

\[
 B^T(v'_i-Mv_i)=d'_i-d_i-\Delta A^{-1}v_i
\]

and |v_i|<=1 give

\[
 |v'_i-Rv_i|
 \le\left(\frac{3\sqrt6}{s_0}
       +\frac{9(\sqrt2+1)}{s_0^2}\right)\epsilon.
\]

Adding the scalar error at most epsilon, and using 3sqrt(6)<8 and
9(sqrt(2)+1)<22, proves the stated bound. Lift R to a quaternion g as
in TO-01. QED.

For any signed Wilson word w of length L, it follows that

\[
 |\tau(w(q'))-\tau(w(q))|\le L C(s_0)\epsilon.
\]

Indeed multiply after the common conjugation, telescope the L factors,
and use that multiplication by a unit quaternion and unit-quaternion
inversion preserve norm. No commutation of factors is used.

The conditions are essential to the stated Lipschitz estimate, not to
exact completeness. Near dependent imaginary vectors, s_0 and delta
can vanish. In particular holonomies near the identity have small
imaginary parts. Nothing here bounds this conditioning uniformly under
lattice refinement or reconstructs a local field with uniformly bounded
cost. The physical spacing and source-dependent distribution of poorly
conditioned anchors remain separate obligations.

## 6. Validation design, provenance, and next falsifier

Implementation: `observational_succ/ym_trace_observer.py`, reusing the
Hamilton arithmetic H from `hopf_source_exact.py` unchanged. This reuses
an algebra implementation, not its separate BBP source interpretation.
Focused tests: `tests/test_ym_trace_observer.py`.

The exploratory Q8 corpus was examined before this implementation: all
512 triples, with 24 proper signed-permutation rotations, produced 50
orbit classes, 49 single/pair banks, and 50 complete banks. Exactly one
pair bank was ambiguous. This is a retained discovery control, not a
held-out confirmation and not a proof by enumeration of continuous SU(2).

Fresh rational controls were declared before execution in the research
handoff and are fixed in the tests: four stereographic source points,
three rational gauge elements, and 64 signed words of lengths 1–9 from
seed 4192026. Their matrix checks use a separate 2x2 Gaussian-rational
implementation; source/group provenance remains shared. The tests also
cover ranks 0,1,2, improper-orientation twins, changed relative gauges,
reversed order, illegal nonunit carriers, and the mean-bank law countermodel.
The parent validation record supplies actual commands and outcomes; no
external Lean replay or continuum check is attributed to these tests.

| Claim | Status / scope | Next falsifying probe |
|---|---|---|
| TO-01 length-three completeness | Classical theorem, elementary proof reproduced; all finite SU(2) tuples | A tuple with equal banks but distinct common-conjugacy class |
| TO-02 pair-only orientation blindness | Exact counterexample | An alleged proper rotation taking (i,j,k) to (i,j,-k) must fail determinant +1 |
| Finite Wilson source transport | Exact finite-graph map and full-law pushforward | Change one plaquette word or erase a shared basepoint and test a mixed observable |
| TO-03 mean-bank sufficiency | Refuted by two explicit laws | Any proposed state reconstruction must also discriminate their second moments |
| TO-04 conditioned inverse | Derived paper estimate; hand-checked by a second same-model role | Exact or rigorous-interval perturbations meeting both thresholds but violating the bound |
| Scale-uniform stable reconstruction | Not established | Track s_0 and delta for source-realized anchors at changing physical cutoffs |
| Continuum existence / physical mass gap | Not inferred | Requires the external analytic contracts / a separate uniform spectral theorem |

The next useful calculation is the actual Wilson-law distribution of
conditioning at changing cutoff, with fixed geometric path definitions.
It can distinguish a stable physical observer from an exact but increasingly
ill-conditioned gauge coordinate system. Its source law, scaling schedule,
and pass/fail threshold must be declared before numerical fitting.

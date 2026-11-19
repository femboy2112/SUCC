# Minimal causal generators: exact reconstruction of the predictive quotient

Date: 2026-11-19. Base: Main XXVI
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

**Status:** classical finite realization results with explicit proofs, a
source/target/access specification, and exact rational implementation controls.
The reconstruction conclusions below are conditional on the stated global
source laws. No academic priority, physical quantum model, or BBP signed
cancellation theorem is claimed.

The user's proposal is interpreted as follows: find the least structure an
observer must retain so that lawful future paths and their target observations
can be generated exactly. The object recovered is the **predictive quotient**
for the declared source and target, not necessarily every hidden coordinate of
the carrier. A finite graph is one possible representation of that quotient.

## 0. Existing SUCC results reused here

The following are predecessors, not new results of this round:

- [Principia Book II](../../../docs/principia_observatoris/02_causality_geometry.md),
  CG-02/04: action descent and smallest linear predictive refinement;
  its later sections distinguish one actual schedule from counterfactual
  preparation and replay.
- [Principia Book IV](../../../docs/principia_observatoris/04_horizons_completion.md),
  PO-H2--H5: accessible-rank horizons, finite-dimensional equivalence,
  globally promised recurrences, and the delayed-spike obstruction;
  PO-H10: conditioning and semigroup stability for response banks.
- [Boundary-first reconstruction](../../2026-11-12/holographic_boundary_filters/THEOREMS.md),
  BF-01: minimal reachable/observable SISO quotient and hidden summands.
- [Ordered boundary filters](../../2026-11-12/holographic_boundary_filters/ORDERED_REALIZATION.md),
  OBR-01--03: exact Gram residual closure, all-generator rank plateau, and
  paid finite-word error. Those stronger coherent Gram observations can
  identify an accessible Hilbert realization up to unitary equivalence.

This note supplies a single explicit reconstruction formula for an ordered
response table, a proof of its minimality and gauge, an executable inverse
that keeps its global promise visible, and a Jacobian-plus-anchor route to
certifying functional closure. The graph-support control in section 6 makes
precise the distinction between a predictive realization and a physical graph.

The file named `observational_succ/holographic_reconstruction.py` was also
inspected: it concerns arithmetic qutrit codes and boundary erasure recovery.
It is not the source of the Hankel reconstruction theorem used here.

## 1. Target-relative equivalence before linear algebra

Let `X` be a set of carrier states, `Σ` a finite set of lawful actions, and
`T_a:X→X` their deterministic state maps. Fix a target readout `h:X→Y`.
For a chronological word `w=a1…ak`, set
`T_w=T_ak∘…∘T_a1`, with `T_empty=id`.

### CGR-R01 — the smallest predictive quotient (PROVED LOCAL / classical)

Define

$$
x\sim_h y\quad\Longleftrightarrow\quad
h(T_wx)=h(T_wy)\quad\hbox{for every finite word }w.
$$

Then this is an equivalence relation preserved by every `T_a`. The readout
and every action descend to `X/~_h`. Moreover, it is the **coarsest**
action-preserved equivalence relation on which the target readout descends.

**Proof.** Equality of all future reports gives reflexivity, symmetry, and
transitivity. If `x~_h y`, then for any `a,w`, the reports from `T_a x,T_a y`
after `w` are the reports from `x,y` after the concatenation `aw`, hence
agree. The empty word gives `h(x)=h(y)`. If another equivalence `≈` preserves
each action and `h`, induction on word length shows `x≈y` implies equality
of every future report, hence `x~_h y`. Thus any such relation is contained
in `~_h`. ∎

This permits a precise truth output: two states can be indistinguishable
under all declared lawful future observations. It does not say that they
are identical under a larger toolkit or for another target. For several
readouts, use their product as `h`.

If `P:X→Z` is an observed coordinate map, exact prediction from `P(x)` is
possible precisely when every future target `h∘T_w` is constant on each
fiber of `P`. This statement is set-theoretic; it supplies no algorithm or
physical access by itself. Additional records intersect compatible fibers;
a change of chart alone does not reduce them.

### CGR-R02 — finite functional closure (PROVED LOCAL / classical)

Let `K` be a field. Suppose there are actual functions
`φ1,…,φd:X→K`, a row coordinate `Φ(x)=(φ1(x),…,φd(x))`, constant matrices
`M_a∈K^(d×d)`, and a column `β∈K^d` satisfying the **functional identities**

$$
\Phi(T_a x)=\Phi(x)M_a\quad(\forall x\in X,\ a\in\Sigma),
\qquad h(x)=\Phi(x)\beta\quad(\forall x\in X).
\tag{1}
$$

For any selected initial state `x0`, put `α=Φ(x0)`. Then

$$
h(T_wx_0)=\alpha M_{a_1}\cdots M_{a_k}\beta
\qquad(\forall w=a_1\cdots a_k).
\tag{2}
$$

The kernel relation of `Φ` is future safe for this target.

**Proof.** The empty word gives `Φ(x0)=α`. Applying (1) at each successor
proves `Φ(T_wx0)=αM_a1…M_ak` by induction. Pair with `β`. Equality of two
coordinate rows is preserved by right multiplication and gives equal target
reports. ∎

The functions may live on an infinite, nonlinear carrier. Their finite
linear closure is the needed hypothesis; the number of carrier states need
not be finite. Conversely, merely finding a finite-dimensional chart for
each state does not prove (1). A finite function description and a finite
shift-invariant function space are different properties.

For a declared rational row-state model `x→xL_a`, features `Φ(x)=xC`, and
linear target `x b`, the identities reduce to the finite matrix checks

$$
L_a C=C M_a\quad(a\in\Sigma),\qquad b=C\beta.
\tag{3}
$$

These checks are identities for **every** state, including unobserved ones.
`verify_linear_function_closure` checks precisely (3). It does not claim
that matrices fitted only to observed states are authenticated source laws.

## 2. A finite observation bank reconstructs every word, given global rank

Assume one authenticated response function `f:Σ*→K`. Words index experiments
or source-computable responses from the same declared preparation. The field
is arbitrary for the theorem; the executable inverse uses `K=Q` with exact
integers and Fractions. Exact equality of arbitrary real observations is not
provided by the implementation.

Define the infinite Hankel table

$$
\mathcal H(u,v)=f(uv),\qquad u,v\in\Sigma^*.
$$

Its rank means the dimension of the span of its rows, equivalently the
supremum of ranks of all finite submatrices. All ranks below are exact.

### CGR-R03 — constructive causal generator reconstruction (CLASSICAL)

Suppose a source theorem or independently justified model contract establishes
`rank(𝓗)≤d`, where `1≤d<∞`. Choose lists of `d` prefixes and `d` suffixes,

$$
P=(p_1,\ldots,p_d),\qquad Q=(q_1,\ldots,q_d),
$$

such that the observed block `H=(f(p_iq_j))` is invertible. Suppose the
observer has lawful access to all entries of

$$
H_a=(f(p_i a q_j)),\qquad
h_Q=(f(q_j)),\qquad h_P=(f(p_i))^T.
$$

Then the following finite data determine **every** future word response:

$$
\boxed{\alpha=h_QH^{-1},\qquad M_a=H_aH^{-1},\qquad \beta=h_P,}
\tag{4}
$$

$$
\boxed{f(a_1\cdots a_k)=\alpha M_{a_1}\cdots M_{a_k}\beta.}
\tag{5}
$$

The state dimension `d` is minimal among all linear weighted realizations
of the same entire response function.

**Proof of existence and reconstruction.** Let
`r_u(v)=f(uv)` be the complete residual response after prefix `u`, and let
`V=span{r_u}`. The hypothesis and invertible block imply `dim V=d` and make
`r_p1,…,r_pd` a basis. Restriction to the suffixes `Q` is injective on `V`
because its matrix in that basis is `H`.

Define the append operator by `R_a r_u=r_ua`. It is well-defined: if
`Σ λ_i r_ui=0` as functions of every suffix, evaluate that identity at `av`
to obtain `Σ λ_i r_ui a(v)=0` for every `v`. Thus relations are preserved.

The row coordinates of a residual are

$$
z_u=(f(uq_1),\ldots,f(uq_d))H^{-1}.
$$

In particular `z_empty=α`. Row `i` of the append matrix is the coordinate
row of `r_pi a`, which is row `i` of `H_aH^-1`. Hence
`z_ua=z_uM_a`. Evaluation of residuals at the empty word is the column
`β=(f(p_i))`. Induction gives (5).

**Proof of minimality.** Any `m`-dimensional realization
`f(w)=aN_wb` factors its Hankel table as

$$
\mathcal H(u,v)=(aN_u)(N_vb).
$$

Every finite Hankel block therefore has rank at most `m`. Our invertible
`d` block forces `m≥d`; (4) attains `d`. ∎

The all-word conclusion comes from the global rank premise and preservation
of complete residual functions, not from extrapolating a finite numerical
rank. `reconstruct_from_table` explicitly labels an inverse without that
premise `FINITE_DATA_CANDIDATE_ONLY`. Supplying its optional assumption
parameter records a premise; the function does not prove that premise.

The code additionally checks that its reconstructed word law reproduces
every provided reading. Failure refutes this particular finite candidate.
Passing still cannot rule out a delayed hidden sector.

### The bank size and its operational meaning

The formula uses at most

$$
(|\Sigma|+1)d^2+2d
$$

scalar entries before removing duplicate words. This is a sufficient bank,
not a generally optimal query count. The word lists `P,Q` each have length
`d`; this is not a claim of `d` physical trajectories or `d` total ticks.

If the complete response has rank `d`, suitable basis words can be chosen
with lengths at most `d−1`. Indeed, a nonzero minimal realization has
reachable row space generated from `α`; each nonstable span of words of
length at most `k` grows by at least one dimension. A stable span is
invariant under every generator and already contains every later word.
The same argument for the observable column space generated from `β`
gives a suffix basis of length at most `d−1`. The resulting Hankel block
is invertible because both matrices in its factorization have rank `d`.
Thus a sufficient bank lies among words of length at most `2d−1`.

This recovers PO-H2--H4 in the present notation. Searching all words to
that length may be exponentially expensive in `|Σ|`; minimal dimension,
shortest witness, number of queries, physical latency, and precision are
separate resource measures.

## 3. Uniqueness is a gauge theorem

### CGR-R04 — minimal realizations are unique up to similarity (CLASSICAL)

If two minimal realizations of the same nonzero `f` have parameters
`(α,{M_a},β)` and `(α′,{M′_a},β′)`, then their common dimension is `d`, and
there is an invertible `S` such that

$$
\alpha'=\alpha S,\qquad
M'_a=S^{-1}M_aS,\qquad
\beta'=S^{-1}\beta.
\tag{6}
$$

**Proof.** A minimal realization is reachable: otherwise restrict it to
the proper invariant span of its reachable rows. It is observable:
otherwise quotient by the nonzero invariant row subspace
`{v:vM_wβ=0 for all w}`. Either reduction would lower dimension without
changing `f`.

On reachable row generators define
`αM_w→α′M′_w`. If `Σλ_iαM_ui=0`, then for every suffix `v`,
`Σλ_i f(u_i v)=0`. The corresponding primed row therefore annihilates
all primed suffix columns and is zero by observability. The assignment is
well-defined and linear. Reversing primed/unprimed gives its inverse.
Write it as `x→xS`. It preserves initial rows, intertwines each append
action, and preserves empty-suffix evaluation. These three statements are
exactly (6). ∎

Thus the invariant reconstructed object is a representation class. A
preferred graph picture requires a preferred basis or an additional
structural hypothesis, such as a specified positive Jacobi chain.
Coherent Hilbert Gram data can fix an inner product and reduce the gauge
to unitary equivalence on the accessible cyclic sector, as OBR-01 already
proves. Neither observation contract recovers an inaccessible direct summand.

## 4. Fibonacci: four successive reports determine the infinite response

Use the source-authenticated two-dimensional model

$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
g_n=e_1^TA^ne_1=1,1,2,3,5,\ldots.
$$

The matrix model supplies the upper bound `rank𝓗≤2`. Its first block

$$
H=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad
H_a=\begin{pmatrix}1&2\\2&3\end{pmatrix}
$$

has determinant one, so the minimal dimension is two. Formula (4), using
`P=Q=(empty,a)`, gives

$$
\alpha=(1,0),\qquad
M=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
\beta=(1,1)^T.
$$

The characteristic identity `M²=M+I` yields
`g_(n+2)=g_(n+1)+g_n` for every `n≥0`, and

$$
G(z)=\sum_{n\ge0}g_nz^n
=\alpha(I-zM)^{-1}\beta=\frac1{1-z-z^2}.
\tag{7}
$$

This is an identity of formal power series. Over the complex numbers the
series converges for `|z|<1/φ`, where `φ=(1+sqrt5)/2`; the rational function
then has its usual continuation away from its poles. No convergence is
asserted at `z=1` merely from the formal identity.

The transition product itself expands into a finite sum over all
intermediate coordinate paths:

$$
\alpha M_{a_1}\cdots M_{a_k}\beta
=\sum_{i_0,\ldots,i_k}
\alpha_{i_0}\left(\prod_{t=1}^k(M_{a_t})_{i_{t-1},i_t}\right)\beta_{i_k}.
\tag{8}
$$

Equation (8) is the distributive law, retaining order and signed weights.
The exact oracle independently enumerates these index paths on small
examples. Matrix composition performs their summation without physically
walking each path. A continuum Feynman integral additionally requires its
own measure/regularization, dynamics, and limiting theorem; (8) does not
supply those physical assumptions.

For a fixed matrix `M`, the identity
`Σ z^n αM^nβ=α(I−zM)^−1β` generalizes (7). In a normed setting,
`|z| ||M||<1` is a sufficient convergence condition by the Neumann series.
For several commuting scalar tags `z_a`,
`α(I−Σ z_aM_a)^−1β` sums words by their tags, retaining each matrix product's
order before summation. Equal tags can aggregate different words; they do
not imply that generators commute.

## 5. A genuine Jacobian-to-generator bridge needs an anchor

### CGR-R05 — integration of Jacobian closure (PROVED LOCAL)

Let `D⊂R^n` be a nonempty connected open set, `T_a:D→D` and
`ψ:D→R^d` be `C¹`, and let `A_a` be fixed real `d×d` matrices. Use column
features in this section. Suppose for each generator

$$
D\psi(T_a x)\,DT_a(x)=A_aD\psi(x)\quad(\forall x\in D),
\tag{9}
$$

and at one declared anchor `x_a∈D`,

$$
\psi(T_a x_a)=A_a\psi(x_a).
\tag{10}
$$

Then

$$
\psi(T_a x)=A_a\psi(x)\quad(\forall x\in D).
\tag{11}
$$

Consequently these features obey an exact finite generator law on every
forward word, and every target of the form `c^Tψ` has an exact realization.

**Proof.** Set `E_a(x)=ψ(T_a x)−A_aψ(x)`. The chain rule and (9) imply
`DE_a=0` throughout `D`. A connected open subset of Euclidean space is
piecewise smoothly path connected; integrate the zero derivative along a
path between any `x` and the anchor. Thus `E_a` is constant and (10) makes
that constant zero. Apply induction for words. ∎

**Quantitative form.** Let the derivative of the same defect obey
`||DE_a(x)||op≤ε` throughout `D`, and suppose the anchor value has norm
at most `δ`. For any rectifiable path inside `D` joining the anchor to `x`,
with length `L`, the fundamental theorem along that path gives

$$
\|E_a(x)\|\le\delta+\varepsilon L.
\tag{12a}
$$

Taking the infimum over those lengths yields
`||E_a(x)||≤δ+ε d_D(x_a,x)`, with the intrinsic path distance in `D`.
A finite radius in this intrinsic metric makes this bound uniform globally;
connectedness alone does not bound that radius. A particular defect may still
be uniformly bounded by a different argument on a domain of infinite radius.
The zero-derivative
case is the exact theorem above.

**Affine repair.** If (9) holds but the anchor defect is a known vector
`b_a`, the same proof gives `ψ(T_a x)=A_aψ(x)+b_a` everywhere. Appending
one constant feature homogenizes this relation:

$$
\widetilde\psi(x)=\binom{\psi(x)}1,\qquad
\widetilde A_a=\begin{pmatrix}A_a&b_a\\0&1\end{pmatrix},\qquad
\widetilde\psi(T_a x)=\widetilde A_a\widetilde\psi(x).
\tag{12b}
$$

Thus anchored affine coherence also supplies an exact finite generator
family. `affine_row_lift` implements the transposed row-state convention.

A finite set of sampled Jacobians does not establish (9) everywhere. A
source-derived functional identity, symbolic calculation on a declared
family, or another all-domain theorem must do that work. Different connected
components require their own anchors. A topology/gauge-valued feature map
requires a separately specified global lift; the theorem uses one Euclidean
feature chart throughout.

**Anchor control.** With `D=R`, `ψ(x)=x`, `T(x)=x+1`, and `A=1`, (9) holds
identically, while `ψ(Tx)−Aψ(x)=1`. Derivatives alone miss the additive
constant. Conversely, choosing an affine feature vector `(x,1)^T` closes
this source with matrix `[[1,1],[0,1]]`; retaining the missing constant is
a constructive repair.

**Disconnected-domain control.** Let
`D=(-infinity,0) union (0,infinity)`, `ψ(x)=x`, `A=1`, and set `T(x)=x`
on the negative component and `T(x)=x+1` on the positive component.
The derivative identity holds at every point, and a negative anchor has
zero defect; every positive point has defect one. This is a genuine `C¹`
map `D→D`. A single anchor cannot cross an absent path.

This is a precise version of a local-coherence-to-global-generator step.
It does not identify a nonlinear carrier from finitely many measured
derivatives, and a target not generated by the chosen features remains
outside its conclusion.

## 6. Countermodels that delimit exact reconstruction

### CGR-R06 — finite response agreement does not pay closure (REFUTATION)

For any integer `L≥0`, let `δ_L(n)=1[n=L]`. It has a finite realization on
an `(L+1)`-state nilpotent chain: row initial vector `e0^T`, column output
`eL`, and a matrix with ones on the superdiagonal. Its leading `(L+1)`
Hankel block is the antidiagonal permutation matrix and has determinant
`±1`; its full rank is exactly `L+1`.

Given any finitely queried unary response history, choose `L` beyond its
largest queried index. The Fibonacci response `g_n` and

$$
\widetilde g_n=g_n+\delta_L(n)
$$

agree at every observed index and disagree at `L`. The second sequence is
also generated by a finite-dimensional constant linear system, using the
direct sum of the Fibonacci model and the chain. Thus the promise merely
"some finite linear realization exists" is insufficient: a bound on its
order, or an independently checked closure certificate, is load bearing.

This is the PO-H5 countermechanism instantiated on a nonzero invertible
training block. The implementation uses a delay of 12; that finite receipt
corroborates the construction, while the proof covers every finite delay.
A deterministic adaptive protocol that stops after finitely many queries
has the same problem on its actual transcript: choose the delay after its
largest queried index, then induction preserves all chosen queries and
answers until it stops.

### CGR-R07 — even minimal positive graph supports need not be identified

Consider

$$
A=\operatorname{diag}(1,2),\quad
\alpha=(1,1),\quad\beta=(1,1)^T,
$$

and the change of basis

$$
S=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
$$

Then

$$
S^{-1}AS=\begin{pmatrix}1&1\\0&2\end{pmatrix},\quad
\alpha S=(1,0),\quad S^{-1}\beta=(2,1)^T.
$$

Both systems have nonnegative transition and endpoint weights, and both
have response `f(n)=1+2^n`. Their Hankel block `[[2,3],[3,5]]` has determinant
one, so both realizations are minimal of dimension two. Their nonzero edge
supports differ. Therefore exact scalar behavior does not select the
literal edge graph, even in this nonnegative finite model class.

Add an invisible one-dimensional block of eigenvalue seven with zero
initial and output coordinates. Every boundary response remains unchanged,
but the full trace at one step changes from three to ten, and the full
matrix determinant changes from

$$
\det(I-zA)=(1-z)(1-2z)
$$

to `(1-z)(1-2z)(1-7z)`. A full-carrier trace zeta cannot be recovered from
the original scalar port without an accessibility/minimality hypothesis.
The minimal predictive resolvent is still exactly reconstructed.

### CGR-R08 — forward accessibility is an independent obligation

In the access model consisting of one irreversible action history and
nondestructive readout at its prefixes, the available words form a chain
under the prefix order. The two one-letter words `a` and `b`, with `a≠b`,
cannot both occur as prefixes of one history. No matrix inverse changes
that fact. Resets, parallel preparations, retained source-state replay,
or authenticated source computation are additional resources.

The unary Fibonacci bank is accessible on one history at times `0,1,2,3`.
A general noncommutative Hankel bank need not be. The function
`missing_from_one_history` reports precisely which required words are absent
under this narrow access model. It is not a theorem that those words are
unavailable under every possible SUCC instrument.

## 7. Conditioning, knowledge volume, and the correct optimization target

Even with the global model class fixed, an invertible table may amplify
errors severely. In any submultiplicative matrix norm, write
`Hhat=H+ΔH`, `Hhat_a=H_a+ΔH_a`, and suppose

$$
q=\|H^{-1}\|\,\|\Delta H\|<1.
$$

The Neumann series implies
`||Hhat^-1||≤||H^-1||/(1−q)`. Since `M_a=H_aH^-1`, exact subtraction gives

$$
\widehat M_a-M_a=(\Delta H_a-M_a\Delta H)\widehat H^{-1},
$$

and hence

$$
\|\widehat M_a-M_a\|
\le\frac{(\|\Delta H_a\|+\|M_a\|\|\Delta H\|)\|H^{-1}\|}{1-q}.
\tag{12}
$$

Thus rank witnesses resolve independent residual directions, while inverse
norms price the precision needed to recover them. A determinant is a
coordinate-dependent volume scale and does not bound the weakest singular
direction. At a prime, the Smith exponents price the corresponding
congruence fibers, as the current five-channel knowledge-volume work does.
Neither count implies a signed temporal estimate.

If both exact and approximate generator norms are bounded by `L`, and each
generator error is at most `ε`, telescoping a word of length `k≥1` gives
`||M_w−Mhat_w||≤k L^(k−1) ε`. Boundary-vector errors require their own terms.
This is not uniform control as `k→∞`. The inherited PO-H10/OBR-03 results
show how separate semigroup stability and closure residual bounds enter.

The mathematical optimization problem should therefore state its cost:
choose a lawful acquisition policy and retained feature family minimizing
cost, subject to target separation, exact or quantitatively controlled
closure, and the requested completion error. Minimal state dimension is
one cost; number of paths, acquisition ticks, exact precision, memory,
conditioning, and source-authentication debt are others. There is no
model-independent equality among them.

## 8. Validation and next falsification opportunities

The companion tests use exact rational arithmetic and compare response
matrix products with a separately enumerated finite index-path sum. They
exercise noncommuting words, missing shifted data, singular blocks, delayed
hidden states, changed graph support, inaccessible branches, exact functional
closure, and target directions outside the feature span.

During authoring, one proposed noncommuting-word pair happened to have the
same chosen scalar output, despite noncommuting matrices. The test failed as
it should. The discriminator was corrected from `aab` versus `baa` to `aba`
versus `baa` for that output. This is an observation-design correction, not
an alteration to the reconstruction theorem or source. The distinct `ab`
versus `ba` control uses another declared output and remains explicit.

A local focused run executed **15 test methods successfully** after that
correction. This report does not claim root-suite, formal-kernel, hosted CI,
or external-referee authority; the root dossier records broader validation
separately. All-word statements rest on the written proofs and their global
hypotheses, not the finite number of test words.

The cheapest next falsifier for a proposed SUCC finite generator model is
an authenticated source word outside its training bank that violates (5),
or a nonzero exact generator-closure residual. Passing it enlarges the
observed domain only. The decisive next positive certificate would be an
all-source identity of the form (1), or an independently established global
Hankel-rank bound for the **actual signed target response**, together with
its lawful access and completion costs.

### External mathematical provenance

1. B. L. Ho and R. E. Kalman, *Effective construction of linear state-variable
   models from input/output functions* (1966), NASA record
   <https://ntrs.nasa.gov/citations/19670049337>.
2. Stefan Kiefer, *Notes on Equivalence and Minimization of Weighted
   Automata* (2020), <https://arxiv.org/abs/2009.01217>;
   original author manuscript <https://arxiv.org/pdf/2009.01217>.
   Sections 2--4 give finite-word equivalence, minimization, Hankel rank,
   and change-of-basis results.
3. Borja Balle, Xavier Carreras, Franco M. Luque, Ariadna Quattoni,
   *Spectral learning of weighted automata: A forward-backward perspective*,
   Machine Learning 96 (2014), 33--63,
   DOI <https://doi.org/10.1007/s10994-013-5416-x>;
   author-hosted manuscript
   <https://www.cs.upc.edu/~aquattoni/AllMyPapers/mlj_2014.pdf>.

These primary accounts were inspected for theorem scope. The elementary
proofs above are written out so that source attribution does not substitute
for checking hypotheses. Classical realization theory supplies the algebra;
SUCC must still supply the authenticated target-specific source map.

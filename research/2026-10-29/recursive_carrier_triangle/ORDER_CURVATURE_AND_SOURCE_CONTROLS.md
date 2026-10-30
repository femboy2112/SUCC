# Path-sheet order curvature and source-faithful controls

**Research date:** 2026-10-29. **Source baseline:** Main XIV,
`ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc`.

**Authority:** self-contained finite and all-horizon paper proofs below; exact
finite implementations and executed receipts are recorded separately by this
campaign. The elementary path-product and adjacent-swap arguments are not claims
of scholarly novelty. This file does not claim a physical gauge field, a quantum
process, or a model of actual human computation. The source-selected signed BBP
estimate, base-16 normality of pi, and RH remain **OPEN**.

## 1. The useful reading of the triangular-sheet proposal

A realized path can update a field which determines the weights of later
choices. The ordered weight of a complete path then need not be determined by
its terminal coarse state. Two paths with the same endpoints bound a finite
sheet of alternative orderings. In a positive two-letter birth model, the
relative weight of those two boundary paths is determined exactly by local
two-step order defects on that sheet.

This makes one part of the proposal mathematically operational: the sheet has a
computable local weight, its boundary has a computable likelihood ratio, and
changing a boundary path changes that ratio according to an exact composition
law. It does not identify this constructed probability model with the original
deterministic BBP source. It also separates three different notions:

- a nonzero **order defect** in positive path probabilities;
- nonlinear response of an **observable** applied to a linear source;
- a nonzero **signed time-average saving** for a specified arithmetic path.

The first two do not imply the third. Sections 4 and 5 supply receipts.

### Inherited results used, with their actual scope

The Main XIV file
[`REALIZED_PATHS_AND_FIELD_FEEDBACK.md`](../../2026-10-26/REALIZED_PATHS_AND_FIELD_FEEDBACK.md)
already derives the two-arm field law, its one-diamond odds ratio, the
nonharmonic-potential path-normalizer identity, and the distinction between
conditioning, reinforcement, and geometry intervention. Its exact same-terminal
example is `P(LLR)/P(LRL)=3/4`.

[`SELECTION_LIKELIHOOD_AND_REVELATION.md`](../../2026-10-26/SELECTION_LIKELIHOOD_AND_REVELATION.md)
already records the likelihood cost of choosing one virtual inverse history and
the failure of multiplying local phase losses. The present all-sheet theorem
extends a local order comparison to an arbitrary pair of boundary paths. The
exponential-reinforcement control adds a genuinely nonflat recursively updated
field with a positive-probability coherent infinite path.

## 2. Exact discrete Stokes law for positive path probabilities

### Domain and definitions

Let `A,B` be nonnegative integers. Work on the complete monotone rectangle

$$
\mathcal R=\{0,\ldots,A\}\times\{0,\ldots,B\}.
$$

A letter `L` changes `(l,r)` to `(l+1,r)` and a letter `R` changes it to
`(l,r+1)`. These labels are bookkeeping conventions, not spatial left/right
coordinates. Let a declared ambient birth law have strictly positive
probabilities

$$
p_L(l,r)>0,\qquad p_R(l,r)>0,\qquad p_L(l,r)+p_R(l,r)=1
$$

at all tails needed below. We use its original edge probabilities, including
when a tail lies on a boundary of the chosen rectangle. We do **not** renormalize
after restricting attention to paths that finish at a chosen endpoint. Only
edges lying in the rectangle enter the formulas.

The entire predictive state of this model is `(l,r)`. A history-dependent model
with additional memory must retain that memory as an additional state; it does
not automatically descend to this count lattice.

For a monotone word `w` from `(0,0)` to `(a,b)` in the rectangle, define its
unconditioned path probability

$$
P(w)=\prod_{t=0}^{a+b-1}p_{w_{t+1}}(l_t,r_t).
$$

For every elementary cell with `0<=l<A`, `0<=r<B`, define the positive
**diamond odds ratio** and its logarithm

$$
H(l,r)=
\frac{p_L(l,r)p_R(l+1,r)}{p_R(l,r)p_L(l,r+1)},
\qquad \kappa(l,r)=\log H(l,r).
\tag{2.1}
$$

Thus `H` is the probability of the local route `LR` divided by that of `RL`,
conditional on their common starting state. Calling `kappa` an order curvature
means exactly (2.1). It is a real log-likelihood defect; no quantum phase,
spacetime curvature, or undeclared transport is implied.

For `0<=i<a`, let `r_w(i)` be the number of `R` letters preceding the
`(i+1)`-st `L` in `w`. It is a nondecreasing integer sequence in `[0,b]`.
Let `w_0=L^a R^b` be the reference path.

### Theorem OCT-01 — boundary odds are the sheet product

For every admissible word `w` ending at `(a,b)`,

$$
\boxed{
\frac{P(w)}{P(w_0)}=
\prod_{i=0}^{a-1}\prod_{j=0}^{r_w(i)-1}H(i,j)^{-1}.}
\tag{2.2}
$$

Empty products equal one. Consequently, for any two such words `w,v`,

$$
\boxed{
\log\frac{P(w)}{P(v)}=
\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
\left(\mathbf1_{j<r_v(i)}-\mathbf1_{j<r_w(i)}\right)\kappa(i,j).}
\tag{2.3}
$$

**Proof.** An adjacent replacement `LR -> RL` at state `(i,j)` changes no
earlier edge. Both alternatives reach the same state `(i+1,j+1)`, so all
subsequent factors are also unchanged. The path-probability ratio after/before
the replacement is exactly `H(i,j)^(-1)`.

Starting with `L^a R^b`, move each `R` left past the `L` letters it precedes in
`w`, keeping the relative order of equal letters. The `(i+1)`-st `L` crosses
precisely the `R` letters indexed `j=0,...,r_w(i)-1`, and that crossing occurs
at cell `(i,j)`. Multiplying the swap ratios gives (2.2). Dividing two such
products and taking real logarithms gives (2.3). This proof needs only the
complete rectangle, positivity, and the retained state law. It makes no
infinite-limit interchange. QED.

The product law is path-composition compatible: for three boundary paths
`u,v,w` with common endpoints, the ratios obey
`P(w)/P(u)=[P(w)/P(v)][P(v)/P(u)]`. In (2.3), the signed cell indicators
cancel correspondingly. This is the exact sheet compatibility condition.

### Theorem OCT-02 — flatness is exactly endpoint-only weight

On the complete rectangle, the following conditions are equivalent:

1. Every elementary diamond satisfies `H(l,r)=1`.
2. Every pair of monotone paths with the same endpoints has the same weight.
3. Every pair of paths from `(0,0)` to the opposite corner `(A,B)` has the
   same weight.
4. There is a positive function `Psi` on the rectangle, with `Psi(0,0)=1`,
   such that every edge lying in the rectangle satisfies

$$
p_L(l,r)=\frac{\Psi(l+1,r)}{\Psi(l,r)},\qquad
p_R(l,r)=\frac{\Psi(l,r+1)}{\Psi(l,r)}.
\tag{2.4}
$$

**Proof.** Condition 1 gives condition 2 by (2.3), including any subrectangle
after shifting the origin. Condition 2 gives condition 3. For condition 3 to
imply condition 1, attach the same prefix to an arbitrary cell and the same
suffix after its opposite corner. Compare the two full paths using `LR` and
`RL` through that cell. Positivity permits cancelling the shared prefix and
suffix, so their equal weights force `H=1` at that cell.

Given condition 2, define `Psi(l,r)` as the weight of any path from the origin
to `(l,r)`. It is well-defined and positive. Appending one edge gives (2.4).
Conversely, (2.4) telescopes along every path to
`P(w)=Psi(endpoint)/Psi(start)`, giving condition 2. QED.

At a vertex where both outgoing edges lie in the rectangle, the stochastic
row sum further gives

$$
\Psi(l,r)=\Psi(l+1,r)+\Psi(l,r+1).
$$

Relative to the fair law, `h(l,r)=2^(l+r) Psi(l,r)` is therefore backward
harmonic and (2.4) is its Doob reweighting. This recovers the inherited
endpoint-potential case. A nonzero diamond defect identifies exactly the
failure of this count-endpoint representation.

**Topology and memory boundary.** Completeness of the rectangle matters. On a
domain with holes, checking only existing elementary diamonds may miss a loop
around a hole. On a history tree, there are no reconverging routes to compare
unless a quotient is explicitly supplied. Coarse endpoint equality also does
not imply equality of the full predictive state. These are hypotheses, not
technical details to be erased by drawing a triangle.

## 3. Exact inherited controls on the sheet

### 3.1 Fair and Pólya laws are flat

For the fair law, `pL=pR=1/2`, so `H=1`.

For positive real parameters `alpha,beta`, the linear Pólya law is

$$
p_L(l,r)=\frac{\alpha+l}{\alpha+\beta+l+r},\qquad
p_R(l,r)=\frac{\beta+r}{\alpha+\beta+l+r}.
$$

Writing `S=alpha+beta+l+r`, both two-step products in (2.1) are

$$
\frac{(\alpha+l)(\beta+r)}{S(S+1)}.
$$

Thus `H=1` for every cell, and every ordered word with counts `(l,r)` has
probability

$$
P(w)=\frac{(\alpha)_l(\beta)_r}{(\alpha+\beta)_{l+r}}.
$$

The predictive probabilities change after every realized event, but the order
curvature vanishes. Recursive updating alone therefore does not force nonzero
curvature. The inherited beta-mixture identity also shows that this observable
law can arise from learning a fixed unknown bias.

### 3.2 Recomputed two-arm field law is generally nonflat

Take the inherited two-arm model with equal initial integer length `L>=3`.
At live state `(l,r)`, put `a=L-l`, `b=L-r`. Recomputing the harmonic field
after a conducting prefix grows gives

$$
p_L(l,r)=\frac b{a+b},\qquad p_R(l,r)=\frac a{a+b}.
$$

For a cell with `a,b>=2`, both two-step orders remain valid and

$$
\boxed{H(l,r)=\frac{b(a-1)}{a(b-1)}.}
\tag{3.1}
$$

It equals one exactly when `a=b`. For a complete rectangle ending with
`l<L` and `r<L`, all its paths stay live and OCT-01 applies. No extension past
the model's stopping time is asserted.

At `L=3`, `H(0,0)=1`, `H(1,0)=3/4`, and

$$
P(LLR)=3/40,\qquad P(LRL)=P(RLL)=1/10.
$$

The sheet for `LRL` relative to `LLR` contains the cell `(1,0)`; (2.2) gives
`P(LRL)/P(LLR)=4/3`, exactly. The complete endpoint field is the same for
these histories, but their accumulated likelihoods differ. Their future laws
are still the same in this model because `(l,r)` is its complete predictive
state. Past order-sensitive odds and retained future order memory are distinct.

## 4. A nonlinear, nonflat field can preserve coherent infinite paths

### Definition of the hostile field

Start with positive weights `(1,1)`. After an `L`, multiply the left weight by
2; after an `R`, multiply the right weight by 2. Choose the next letter in
proportion to the current weights. After counts `(l,r)`, this gives

$$
p_L(l,r)=\frac{2^l}{2^l+2^r},\qquad
p_R(l,r)=\frac{2^r}{2^l+2^r}.
\tag{4.1}
$$

This is an explicit material-state update in a declared mathematical model.
All finite transitions are strictly positive and all finite words are allowed.
The normalized predictive rule is nonlinear in the counts. Its local order
curvature is

$$
\boxed{H(l,r)=\frac{2^l+2^{r+1}}{2^{l+1}+2^r},}
\tag{4.2}
$$

which equals one exactly when `l=r`. For example,
`P(LLR)=1/15`, `P(LRL)=1/12`, so `P(LLR)/P(LRL)=4/5`.

### Theorem OCT-03 — nonflat feedback with an infinite coherent atom

Under (4.1), the infinite all-`L` event has probability at least `1/5`.
The all-`R` event has the same probability. Nevertheless the ensemble mean
of the phase `X_t=+1` on `L`, `X_t=-1` on `R` is zero at every positive time.
Hence nonlinear feedback, nonzero order curvature, and exact ensemble phase
cancellation do **not** imply almost-sure cancellation of the phase average
along the selected path.

**Proof.** After an all-`L` prefix of length `n`, the next `L` probability is
`2^n/(2^n+1)`. Therefore

$$
P(L^N)=\prod_{n=0}^{N-1}\frac{2^n}{2^n+1}.
\tag{4.3}
$$

The first three factors multiply to `4/15`. For `N>=3`, use the elementary
finite product inequality `prod(1-a_n)>=1-sum(a_n)` for `0<=a_n<=1` to get

$$
\begin{aligned}
P(L^N)
&=\frac4{15}\prod_{n=3}^{N-1}
\left(1-\frac1{2^n+1}\right)\\
&\ge\frac4{15}
\left(1-\sum_{n=3}^{N-1}\frac1{2^n+1}\right)
>\frac4{15}\left(1-\sum_{n=3}^{\infty}2^{-n}\right)
=\frac15.
\end{aligned}
$$

The cylinders `{first N letters are L}` decrease with `N`. Continuity from
above gives `P(all L)=lim_N P(L^N)>=1/5`. Alternatively the convergent
log-product gives the weaker bound `P(all L)>=1/(2e)`. No finite scan is
being used to infer the existence of this infinite atom.

The map exchanging `L` and `R` preserves the law (4.1) and reverses `X_t`.
Thus `E X_t=0` at every time, and the all-`R` event has the same probability
as all-`L`. On all-`L`, every empirical mean `N^(-1) sum_(t<=N) X_t` equals
one. On all-`R` it equals minus one. These disjoint coherent events together
have probability at least `2/5`. QED.

This example passes the proposed structural tests: a realized event changes
the carrier weights, later choices depend on that changed field, subpath order
has nontrivial interaction, and the sheet obeys OCT-01 exactly. It fails the
generic inference to pathwise cancellation. It is not a counterfeit of the
exact four-pole BBP source; its role is to refute that structural inference
without pretending to settle the source-specific arithmetic question.

## 5. The authentic affine source supplies a separate interaction null control

The original zero-seeded source is

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),
$$

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\tag{5.1}
$$

Its exact code provenance is
[`succ_internal_matrix_walk.py`](../../../observational_succ/succ_internal_matrix_walk.py)
and
[`lambda_source_duality.py`](../../../observational_succ/lambda_source_duality.py)
at the baseline pin. Source mutations in this section are declared controls,
not replacements for (5.1).

### Theorem OCT-04 — affine forcing has zero multiplicative rectangle defect

Let `f(n),g(n)` be arbitrary real forcing perturbations and `alpha,beta` real
parameters. With the same zero seed, let

$$
U_n(\alpha,\beta)=16U_{n-1}(\alpha,\beta)
+r(n)+\alpha f(n)+\beta g(n).
$$

Put

$$
F_n=\sum_{k=1}^n16^{n-k}f(k),\qquad
G_n=\sum_{k=1}^n16^{n-k}g(k).
$$

Then for every finite `n`,

$$
U_n(\alpha,\beta)=U_n(0,0)+\alpha F_n+\beta G_n.
\tag{5.2}
$$

For any fixed integer `h`, define
`chi_n(alpha,beta)=exp(2 pi i h U_n(alpha,beta))`. Its multiplicative mixed
rectangle is identically flat:

$$
\boxed{
\chi_n(\alpha,\beta)\chi_n(0,0)
=\chi_n(\alpha,0)\chi_n(0,\beta).}
\tag{5.3}
$$

Its additive mixed difference can still be nonzero, but factors exactly as

$$
\boxed{
\chi_n(\alpha,\beta)-\chi_n(\alpha,0)
-\chi_n(0,\beta)+\chi_n(0,0)
=\chi_n(0,0)
\big(e(h\alpha F_n)-1\big)
\big(e(h\beta G_n)-1\big),}
\tag{5.4}
$$

where `e(x)=exp(2 pi i x)`.

**Proof.** Induction in the affine recurrence gives (5.2), or its finite Green
sum does so directly. Exponentiating separates its three additive terms,
which proves (5.3); expansion proves (5.4). QED.

Equation (5.3) needs no branch of a complex logarithm and is therefore the
appropriate exact mixed-interaction null test. Rational inputs can be checked
by rational phase addition modulo one, with no floating trigonometry. The
same theorem holds for arbitrary fixed nonzero source seeds when the seed is
kept common to the four corners.

A nonzero additive four-corner contrast alone therefore does not establish
irreducible self-interaction of the source. It can arise merely from applying
the nonlinear exponential observable to the affine recurrence. A genuine
extra interaction must be located in a declared field update, projection,
normalization, discontinuous carry operation, or changed source. It must also
pass its own four-corner control with all corners evaluated in the same
operational basis. The rectangle in parameter space in (5.3) is not the count
lattice of Section 2; the two are distinct typed probe domains.

## 6. What the sheet adds, and the surviving arithmetic discriminator

The sheet representation is useful because it retains an exact quantity that
an endpoint-only summary erases: the accumulated signed log-odds curvature
between alternative orderings. Flatness, feedback, and pathwise cancellation
are now separately testable properties. OCT-03 shows why even a nonflat sheet
does not close the arithmetic argument.

For the original BBP problem, any proposed virtual-field construction must
retain the original four poles, their signs, the zero initial boundary, and the
source-labelled selected observable. It must prove an actual relation to

$$
S_N(h)=\sum_{n=1}^N e(hU_n(0)),\qquad h\in\mathbb Z\setminus\{0\}.
$$

If a field representation gives a signed weighted expression `W_N(h)` and an
explicit source-derived remainder `E_N(h)`, the next discriminator is a proved
transport estimate and a **new** signed bound, for example

$$
|S_N(h)-W_N(h)|\le E_N(h)=o(N),\qquad |W_N(h)|=o(N).
$$

Writing down this sufficient pair is a research contract, not progress toward
its second inequality. A new construction has to show why its signed estimate
can be attacked independently, without assuming the desired normality. The
same-forcing changed seed, a rational nonnormal forcing control, flat Pólya,
and the nonflat exponentially reinforced field above remain mandatory hostile
comparisons. None of these controls forbids cancellation across distinct
source times of the authentic deterministic orbit.

### Local claim ledger

| Claim | Status | Hypotheses and boundary | Next falsification opportunity |
|---|---|---|---|
| OCT-01, all-sheet odds formula | PROVED LOCAL (paper) | positive law on a complete monotone rectangle; retained predictive state | remove memory or introduce a domain hole |
| OCT-02, flatness iff endpoint-only weights | PROVED LOCAL (paper) | same rectangle and full path comparison | check a coarse quotient for unequal future laws |
| Fair/Pólya flatness and two-arm nonflatness | PROVED LOCAL (paper); inherited one-diamond models | declared probability laws, not BBP identification | source-derived law with different exact odds |
| OCT-03, coherent atoms in a nonflat updated field | PROVED LOCAL (paper) | exponential reinforcement (4.1); all-horizon bound | a proposed theorem must exclude this model by a justified hypothesis |
| Nonflat feedback plus ensemble cancellation implies pathwise cancellation | REFUTED | receipt: OCT-03, coherent events of combined probability at least 2/5 | retain source-specific hypotheses instead |
| OCT-04, affine multiplicative rectangle | PROVED LOCAL (paper) | common seed and additive forcing parameters | declared non-affine update or carry projection with all four corners retained |
| Authentic BBP signed cancellation from sheet curvature | OPEN | no authenticated field-to-selected-sum estimate supplied here | source-specific signed transport and saving |

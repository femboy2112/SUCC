# Ordered boundary filters: a finite closure certificate

**2026-11-12.** Main parent `db9fb4b84672050efa79b13377f1e73364598a14`.
This is an additive research construction. Its exact theorems are elementary
finite/cyclic realization results with classical antecedents. The original
four-pole source, literal zero seed and historical source files are unchanged.
No number-theoretic statistical estimate is claimed.

## 1. What the proposed boundary can mean

The useful reading of the holographic proposal is: a sufficiently separating,
source-calibrated family of boundary interventions and responses determines
the part of the carrier it can actually reach and compare. The family must
retain the order of operations and, when complex amplitudes matter, relative
phase. The following construction makes **sufficiently separating** a
falsifiable algebraic condition.

There are three distinct issues:

1. **Identification:** which interiors produce the observed response table?
2. **Closure:** do further permitted filters stay in the reconstructed space?
3. **A target estimate:** what property can be proved of those dynamics?

A successful answer to the first two permits analysis of the third. It does
not itself supply every desired theorem. More abstractly, for any observation
map `O: X -> Y`, a property of `X` can be recovered from `O(x)` precisely when
it is constant on every fiber of `O`. Necessity follows by comparing two
objects with the same output; sufficiency follows by defining the property
on that output's fiber. This is an identifiability criterion, not a claim that
the resulting decision procedure is computable or efficient.

### Classical and repository provenance

The local predecessor `observational_succ/dynamic_boundary_inverse.py` already
has scalar/block-Hankel dynamic-order witnesses, exact serial-storage inverse
maps and a static/dynamic elimination mismatch. The local predecessor
`observational_succ/spectral_boundary_rigidity.py` already reconstructs a
minimal cyclic Jacobi chain from its rational boundary response. These are
at the pinned main parent, and are not rewritten here.

Donor PR #604 at `220df67b4ee3f558de63f08cc76ed52b34138302` already contains
classical GNS reconstruction and a positivity/normality countermodel in
`research/2026-11-12/arity_0_5_observer_ladder/THEOREMS.md`, A05-G/A05-S.
Its `BIDIRECTIONAL_CHANNELS.md` also proves a finite-grid selection seam.
Donor PR #601 at `774191e7679cd63c56bdb105541ce21c8ee27448` contains explicit
coherent-code transport, cumulative errors and present-observable access
conditions in `research/2026-11-12/prime_fixed_point_observer/`.
These donor statements were inspected; their commits are not silently merged
or treated as new results of this dossier.

Classical external context, freshly inspected:

- M. Petreczky, *Realization theory for linear and bilinear switched systems:
  A formal power series approach*, ESAIM COCV 17 (2011), 410-445,
  [doi:10.1051/cocv/2010014](https://www.numdam.org/articles/10.1051/cocv/2010014/).
  Its realization framework uses ordered formal series, Hankel rank and
  minimal reachable/observable systems; minimal general linear realizations
  are unique up to similarity.
- B. Mourrain and K. Schmuedgen, *Flat extensions in \*-algebras*,
  [arXiv:1406.4975](https://arxiv.org/abs/1406.4975), later Proc. AMS 144
  (2016), 4873-4885, doi:10.1090/proc/13158, gives a general positive-functional
  flat-extension theory. No unverified application of that theorem is needed
  below; all hypotheses and proofs of this narrower result are explicit.

**Novelty boundary:** classical realization is not a new mathematical
discovery. The new repository object is the simultaneous ordered-filter
certificate with a measured closure residual, a metric conditioning check,
finite-word error payment, and explicit phase/order/hidden-sector controls.

## 2. Domain and boundary data

Let `H` be a complex Hilbert space, `xi != 0` a declared boundary vector,
and `A_i` a finite labelled family of bounded linear operators on `H`.
All refer to one source and epoch. Inner products are conjugate-linear in the
first argument. A chronological word `w=(i_1,...,i_k)` means

\[
 A_w=A_{i_k}\cdots A_{i_1},\qquad A_\varnothing=I.
\]

Choose words `B=(w_0,...,w_(r-1))`, with `w_0` empty, whose states
`v_j=A_(w_j) xi` are linearly independent. Define the synthesis map
`V c = sum_j c_j v_j`, the space `K=range(V)`, and the response matrices

\[
 G=V^*V,\qquad H_i=V^*A_iV,\qquad Q_i=V^*A_i^*A_iV.
\tag{1}
\]

Thus `G>0`. These are **signed complex cross-responses**, not just individual
power spectra. For example the entry `(u,v)` of `H_i` compares the transported
state `A_u xi` with `A_i A_v xi` in a declared common inner product.

If only intensities of individual words are accessible, (1) is an additional
access requirement. If calibrated coherent sums of two states are available,
the polarization formula supplies the missing cross-response:

\[
\langle x,y\rangle=\tfrac14\{\|x+y\|^2-\|x-y\|^2
 +i[\|x-iy\|^2-\|x+iy\|^2]\}.
\tag{2}
\]

The signs in (2) use the stated inner-product convention. In a physical
setting these are different preparations/settings and statistical expectation
values; this exact arithmetic laboratory does not claim to measure them from
one unrepeatable state. A label or hash does not establish physical source
authentication. That remains part of the observation contract.

## 3. OBR-01: exact boundary closure and reconstruction — PROVED LOCAL

For every declared filter define

\[
 M_i=G^{-1}H_i,\qquad
 R_i=Q_i-H_i^*G^{-1}H_i.
\tag{3}
\]

**Theorem.** Under the hypotheses in section 2:

1. `R_i` is positive semidefinite.
2. `R_i=0` if and only if `A_i K` is contained in `K`.
3. If every `R_i=0`, then `K` is exactly the cyclic space generated by
   `xi` and the entire declared filter alphabet, and every ordered response
   is recovered from the finite matrices:

\[
 A_w\xi=V M_w e_0,\qquad
 \langle A_u\xi,A_v\xi\rangle=e_0^*M_u^*G M_v e_0.
\tag{4}
\]

In particular `s(w)=<xi,A_w xi>=e_0* G M_w e_0`.
Here `M_w` follows the same chronological convention as `A_w`.

**Proof.** Since `G>0`, the orthogonal projection onto `K` is
`P=VG^-1V*`. It is self-adjoint, idempotent, and fixes `V`.
Consequently

\[
 R_i=V^*A_i^*(I-P)A_iV=E_i^*E_i,
 \qquad E_i=(I-P)A_iV.
\tag{5}
\]

This proves positivity and the equivalence `R_i=0 <=> E_i=0`. The latter is
equivalent to invariance of `K`. Also `P A_i V=V M_i`; when closed it follows
that `A_i V=V M_i`. Induction proves (4). Every `v_j` is a word state, while
every word state lies in invariant `K` containing `xi`, so `K` is exactly the
cyclic space. This induction is the all-word proof; the finite test count is
not doing an infinite extrapolation. ∎

**Unique accessible realization.** Suppose another Hilbert model has the
same labelled tables, the same word-labelled boundary basis, and the same
closure conditions. The map `U(Vc)=V'c` is an isometry because both Gram
matrices are `G`, is onto the second cyclic space, sends `xi` to `xi'`, and
intertwines every `A_i` there. Thus the accessible realizations are unitarily
equivalent. An overall frame change cannot alter the response table.

**What the verifier checks.** `boundary_realization.py` receives only (1),
the labelled basis words, and the filter names. It computes (3), rejects
non-Hermitian/indefinite data, and, on exact closure, checks that every named
basis word evaluates to its named coordinate. It does not receive the hidden
matrices. Separate forward-oracle code generates laboratory data for tests.
These consistency tests do not prove the data arose from the claimed source.

### OBR-02: finite rank plateau — PROVED LOCAL

Let `K_l` be the span of **all** word states of length at most `l`. If exact
Gram ranks show `dim K_(l+1)=dim K_l`, every generator sends `K_l` into
`K_(l+1)=K_l`; OBR-01 closes the entire orbit algebra. The same criterion is
valid in an infinite-dimensional ambient Hilbert space: it certifies a finite
cyclic sector, not a finite ambient universe. If the cyclic dimension is `d`,
then closure is attained by `l<=d-1`, because every earlier nonclosed step
strictly increases the dimension from its initial value one.

Testing one trajectory, one generator, or only diagonal Gram entries is not
this condition. The test must include every declared generator on a spanning
family. A time-dependent filter replacing the certified `A_i` is outside the
theorem's stationary operator contract.

## 4. OBR-03: approximate closure pays a word-length and conditioning cost

For a nonzero closure residual, put

\[
 \delta_i^2=\|G^{-1/2}R_iG^{-1/2}\|_{\rm op},\qquad
 \beta_i=\operatorname{tr}(G^{-1}R_i).
\tag{6}
\]

Because the normalized residual is positive semidefinite,

\[
 \delta_i^2\le\beta_i,\qquad
 \delta_i^2\le\frac{\|R_i\|_{\rm op}}{\lambda_{\min}(G)}.
\tag{7}
\]

The exact code computes the rational `beta_i`; no numerical eigenvalue is
needed for its certificate. In particular a small raw matrix residual is
insufficient when the observed basis is ill-conditioned.

**Theorem (conditional error bound).** Suppose every **ambient** `A_i` is a
contraction. This additional global norm promise is not inferable from the
finite table. Then for any chronological word `w=(i_1,...,i_L)`,

\[
 \|A_w\xi-VM_we_0\|
 \le\|\xi\|\sum_{j=1}^L\delta_{i_j}
 \le\|\xi\|\sqrt{L\sum_{j=1}^L\beta_{i_j}}.
\tag{8}
\]

Consequently the error in the scalar return `s(w)` is at most
`||xi||^2 sum_j delta_(i_j)`. For two words the Gram-entry error is at most
`||xi||^2 (sum_(j in u) delta_j + sum_(j in v) delta_j)`.

**Proof.** The compressed operators `P A_i|K` are contractions. For `x=Vc`,
(5) gives `||(I-P)A_i x||^2=c*R_i c<=delta_i^2 c*G c`.
Insert the compressed state at each step of a word and telescope. Every
actual remaining operator and compressed prefix has norm at most one, so
the sum of inserted errors is at most the first bound in (8).
Use `delta_i<=sqrt(beta_i)` and Cauchy-Schwarz for the second. Pair the vector
error with `xi` for scalar returns. For Gram entries, write
`<x,y>-<x',y'>=<x-x',y>+<x',y-y'>` and use the contraction bounds on `y,x'`. ∎

This is truncation error for **exact input data**. A separate measurement
noise bound would also have to control perturbations of `G^-1`, `H_i`, and
`Q_i`. The code's `G-Q_i>=0` check certifies contraction only on the observed
span; it deliberately does not promote that check to the global promise.
For fixed nonzero defects, (8) deteriorates with length. It is not a uniform
infinite-time estimate.

**Conditioning counterexample.** In `C^3`, take `xi=e0`,
`B=epsilon |e1><e0|`, `A=|e2><e1|`, and observed basis `(xi,Bxi)`.
Both filters are contractions for `0<epsilon<=1`, but

\[
 G=\operatorname{diag}(1,\epsilon^2),\quad
 R_A=\operatorname{diag}(0,\epsilon^2),\quad \delta_A^2=\beta_A=1.
\]

Thus `||R_A||->0` while the normalized leakage stays one. Any proposed
conditioning-free conclusion is refuted by this family.

## 5. OBR-04: spectra and all word powers can still miss signed order

Let `xi=e0` and take the exact Pauli matrices

\[
 X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}.
\]

Compare the labelled models `(X,Y,xi)` and `(X,-Y,xi)`.
They have identical individual spectra `{+1,-1}`. Every single-filter
boundary moment agrees: odd powers have expectation zero, even powers one.
For **every** ordered word, replacing `Y` by `-Y` multiplies its amplitude by
`(-1)^(number of Y letters)`, so all individual return intensities agree.
Nevertheless

\[
 \langle e_0,XYe_0\rangle=i,\qquad
 \langle e_0,X(-Y)e_0\rangle=-i,
 \qquad \langle e_0,YXe_0\rangle=-i.
\tag{9}
\]

Both order and calibrated phase matter. If `XY` is a return amplitude,
interference with a known `i` reference gives intensities 4 and 0 in the two
models. Such a reference is a stronger interface than recording each return
power separately. With basis `(xi,Xxi)`, the signed Gram/shift table has
`G=I`, every `R_i=0`, and recovers the two models distinctly.

This is **PROVED LOCAL** by the displayed algebra and a **REFUTED** receipt
for the general claim that individual spectra or all individual word powers
always identify the labelled ordered dynamics. It is not a statement about
all conceivable phase-retrieval experiments. If all supplied filters commute,
reordering alone gives no additional information.

## 6. OBR-05: the invisible-sector boundary — PROVED LOCAL / REFUTED claim

Append an arbitrary orthogonal direct summand `L` to `H`, set
`A_i'=A_i direct-sum B_i` and `xi'=(xi,0)`. Every ordered Gram entry is
unchanged, independently of the dimension, spectrum and dynamics on `L`.
Thus complete boundary data identifies the cyclic realization, but cannot
identify arbitrary inaccessible degrees of freedom. An assumption that the
boundary is cyclic eliminates this ambiguity **by restricting the model
class**; it is not inferred from response data alone.

This is an explicit counterexample to unrestricted recovery of all internal
properties. It also distinguishes equality of response tables from a proof
that the physical carriers or unobserved histories are identical.

## 7. What this buys the SUCC arithmetic program

The certificate replaces the phrase "robust enough filters" with an exact
test: a spanning Gram, all generator shifts, measured residuals, source and
frame labels, and a calibrated phase convention. A successful finite closure
can prove an all-word identity because it supplies the missing induction.

It does not yet supply the arithmetic signed estimate. The affine BBP step
already has a two-dimensional homogeneous-coordinate representation,

\[
 \begin{pmatrix}U_n\\1\end{pmatrix}
 =\begin{pmatrix}16&r(n)\\0&1\end{pmatrix}
 \begin{pmatrix}U_{n-1}\\1\end{pmatrix}.
\]

This exact reconstruction retains time-dependent forcing and an expanding
factor 16. It does not meet the contraction hypothesis in (8), and knowing
the matrices does not prove cancellation of their selected output phases.
One must not replace all time-specific coefficients with a finite stationary
alphabet without proving that new encoding and retaining the source clock.

**Next dependency cut.** Construct a source-authenticated observer subspace
for the actual signed target, then prove either exact closure plus a useful
spectral/ergodic theorem for its reconstructed dynamics, or a quantitatively
small residual with a uniform error budget on the required growing words.
The authentication, closure and target estimate are separate obligations.
The Pauli phase pair, invisible direct summand, missing-generator example,
and ill-conditioned basis are required negative controls for that proposal.

## 8. Executable receipt and authority

Files: `boundary_realization.py`, `test_boundary_realization.py`.
The verifier uses standard-library `Fraction` Gaussian rationals. It rejects
float/bool/complex inputs, singular basis Grams, negative Schur residuals,
inconsistent filter labels, and inconsistent closed basis words.

The constructor bearing ran:

```sh
python -W error -m unittest -v test_boundary_realization.py
python boundary_realization.py
```

**Observed:** 14 tests passed. The executable summary reconstructs all 127
words through length six with no mismatch; the two hostile models have the
same individual return intensity on all 127 checked words and opposite
imaginary signed `XY` response. Tests also cover complex nonorthogonal Grams,
adjoint-versus-transpose mutation, reversed order, hidden summands, missing
generators, nonclosure, conditioning, and exact rational rotation errors.
Universal claims rest on sections 3-6, not these finite counts. This is a
same-model constructor and exact-code check; root review/independent replay
is a separate authority. No Lean kernel check or external peer review is
claimed.

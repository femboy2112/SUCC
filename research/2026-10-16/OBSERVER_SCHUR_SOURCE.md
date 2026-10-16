# Observer's Schur complement: authentic source experiment, Round II

**Original four-low sign OPEN. RH PROVED: NO.** This lane supplies a new
**whole-family obstruction**, a certified continuum **upper** Schur bound,
and a different, threshold-aware response experiment. No positivity is
manufactured by an auxiliary counterterm or by a positive upper bound.

## Source, domain, authority and inherited dependencies

The base is SUCC `5d6d717312eebee648d3cfb092875eb4120bb4b3`, in the isolated
`research/observers-schur-complement-2026-10-16` worktree. This worker did not
stage, commit, push, change archives, or modify another lane's files. The
source is `observational_succ/source_weil_hierarchy.py`, original Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, SHA256
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`,
at source commit `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. That PR85
provenance is distinct from the 72-entry original import manifest. Both the
live blob and originating commit bytes were inspected. Relevant dossiers,
source modules, the previous independent audit, and prior receipts were
read before changes; their file hashes accompany the new receipts.

Take $I=(-1/2,1/2)$, $H=L^2_0(I;\mathbb C)$,
$Vu(t)=\int_{-1/2}^t u(s)\,ds$, $K=V^*V$, and $P$ the orthogonal
projection on $l_j(t)=P_j(2t)$, $j=1,2,3,4$, with $Q=1-P$.
The unnormalized coordinate metric is
$W=\operatorname{diag}(1/3,1/5,1/7,1/9)$. A form matrix is not an
operator matrix in the Euclidean metric. All reported operator eigenvalues
use the corresponding $W^{-1/2}$ congruence.

The genuine mean-zero compressed convolution operator $G$ retains both
pole channels, one real Gamma completion, the original contact and the
true prime-2 half-density impulse. On $0<r\le1$,

\[
g'(r)=-4\sinh(r/2)+C_\infty/2+
\frac{\log2}{\sqrt2}\mathbf1_{r>\log2}
-\operatorname{atanh}(e^{-r/2})-\arctan(e^{-r/2}).
\]

The domain, source formula and $g'\in L^1$ are inherited from
[the source dossier](../2026-10-15/FOUR_LOW_SCHUR_CROSSPOLLINATION.md) and
[its independent audit](../../reviews/2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md).
Write $A=PGP$, $B=PGQ$, $D=QGQ$, $K_Q=QKQ|_{QH}$.
The whole-high hypothesis used here is the inherited paper theorem

\[
D\succeq\kappa_*K_Q,
\qquad \kappa_* = 20699/10^6.
\]

Its source-dependent Bessel/Gamma proof and exact rational implementation
are preserved in `tate_weighted_bessel_four_schur.py`. This lane does not
independently re-prove that theorem. The inherited low block is positive
definite. The inherited bound $\|g'\|_1<11/40$, the quotient-residual
identity, and Douglas range argument imply

\[
\operatorname{Ran}B^*\subseteq\operatorname{Ran}D^{1/2},\qquad
R_0=(D^{-1/2}B^*)^*(D^{-1/2}B^*)\preceq
\frac{75625}{20699} I_P.
\]

There is no bounded inverse of the compact infinite high block at zero.
The inverse square root is used only on the specified range. No zeros of
zeta are inputs. All new finite source pairings use the existing exact
Legendre/OU integration kernel; the historical modules are untouched.

## OS-SOURCE-01: contraction and the two parity tests

**PAPER_PROVED, conditional on the stated source/range hypotheses.** Since
$A>0$ on the finite-dimensional low space,

\[
T=D^{-1/2}B^*A^{-1/2},\quad
S_0=A^{1/2}(I-T^*T)A^{1/2}.
\]

The range inclusion and finite dimension make $T$ bounded. Thus

\[
S_0\succeq0\iff T^*T\preceq I\iff\|T\|\le1.
\]

This is classical Schur congruence specialized to the authenticated
observer/source pair, not new analytic positivity. Evenness of the kernel,
reflection invariance of the low projection and the inherited zero-shift
range limit give the exact sectors $(l_1,l_3)$ and $(l_2,l_4)$, each of
dimension two. For a real symmetric sector matrix
$\begin{psmallmatrix}a&b\\b&d\end{psmallmatrix}$, PSD is equivalent to
$a\ge0,d\ge0,ad-b^2\ge0$. For complex Hermitian matrices replace
$b^2$ by $|b|^2$. The implementation handles the real source matrices
and rejects symmetry/parity violations; it never silently deletes them.

No square root is needed to test $R_0\preceq A$. More generally, if
$L\preceq S_0\preceq H$, then

\[
A-H\preceq R_0\preceq A-L.
\]

Generalized eigenvalues against the **same positive source $A$** bound
the squared coupling norm in each sector. Numerical entries give numerical
estimates only. Source-certified interval tests must also account for
uncertainty in $A$, all cross terms, and the coordinate metric.

## OS-SOURCE-02: exact exclusion of an entire response family

**PAPER_PROVED with exact rational source-interval certificate.** This is
stronger than replaying the previous eight frozen failures. Fix the low
input $x=l_2$, and allow **all complex coefficients** in

\[
v=x-Ux=l_2+c_6l_6+c_8l_8.
\]

Every reflection-preserving degree-eight response has such a column. Let
$E=\operatorname{span}(l_6,l_8,l_{10},l_{12})\subset QH$. Its exact
positive $K$-Gram is $K_E$, and set
$C_{qj}=\langle l_q,G l_j\rangle$, $q=6,8,10,12$, $j=2,6,8$.
The restricted variational supremum in the quotient residual identity gives

\[
C_U^{\rm quot}[x,x]
\ge (1,c_6,c_8)^* C^*K_E^{-1}C(1,c_6,c_8).
\]

A restricted supremum supplies a **lower** bound here. It is used to
**upper-bound the sufficient lower certificate**, never to upper-bound an
infinite response. Consequently, for every positive comparison constant
$k$, irrespective of whether it is an available source coercivity bound,

\[
(A-L_U-k^{-1}C_U^{\rm quot})[x,x]
\le z^* M_k z,
\quad M_k=G_{(2,6,8)}-k^{-1}C^*K_E^{-1}C,
\quad z=(1,c_6,c_8).
\tag{1}
\]

The new exact computation encloses **all** entries of $M_k$ using the
actual completed source. If its symmetric interval midpoint is $M_c$
and the maximum row sum of interval radii is $e$, then
$M_k\preceq \overline M_k=M_c+eI$. This follows from the symmetric
operator-norm bound by the maximum absolute row sum. Exact positive LDL
pivots of $-\overline M_k$ certify strict negative definiteness.

Write the upper majorant as
$\begin{psmallmatrix}a&b^*\\b&N\end{psmallmatrix}$, $N<0$.
Completing the finite square proves

\[
\sup_{c_6,c_8\in\mathbb C} z^*\overline M_k z
=a-b^*N^{-1}b<0.
\tag{2}
\]

The imaginary high coefficients contribute an additional nonpositive
quadratic term, so the real maximizer proves the complex statement too.
There is no coefficient search in (2). The full exact fractions, source
intervals, $K_E^{-1}$, all LDL pivots and the maximizing coefficients of
the **upper majorant** are in the receipt.

| Comparison constant in the criterion | Uniform strict upper, decimal display | Simple exact outward consequence |
|---|---:|---:|
| $20699/10^6$, inherited valid source bound | $-0.001282712662531326$ | $<-1/1000$ |
| $1/10$, hypothetical stronger bound | $-0.00018209597366625047$ | $<-18/100000$ |
| $1/5$, hypothetical stronger bound | $-0.000038440888339769405$ | $<-3/100000$ |

The signs use fractions, not these displayed decimals. Since the criterion
increases with $k$, the last row excludes **every $0<k\le1/5$** for
this family. The value $1/5$ is about 9.66 times the inherited value; it
has **not** been established as a source lower bound.

This refutes certification by this restricted response family and this
residual comparison for that range of constants. It does **not** refute
$S_0\succeq0$, all polynomial response families, the true Weil form, or RH.

### Whole Gamma remainder and the retained unsuccessful interval budget

For mean-zero vectors the omitted real Gamma operator is positive, with

\[
0\preceq G-G_J\preceq\tau_J I,\quad
\tau_J=\frac{2}{(4J+1)^2}+\frac{16}{(4J+1)^3}.
\]

This is the inherited exact source tail, not a numerical fit. A polynomial
pair receives error at most
$\tau_J/\sqrt{(2i+1)(2j+1)}$, enlarged rationally to
$\tau_J/\min(2i+1,2j+1)$. Every channel is included before this error.
The finite budget here is $J=512$. Existing exact OU pairs have the form
$a+b e^{-\alpha}$, $\alpha=(4j+1)/2$. For $\alpha\le256$ the existing
rational exponential enclosure is reused. For larger $\alpha$, the
rigorous inequality $0<e^{-\alpha}<2^{-\lfloor\alpha\rfloor}$, from
$e>2$, is enough. The interval arithmetic handles either sign of $b$.

The first $J=128$ interval majorant was too wide: its row-radius cap at
$k=1/5$ was about $0.00032429$, and negative definiteness was not
certified. That outcome is retained as an explicit UNRESOLVED regression.
At $J=512$ the cap is about $0.0000201127$, and the exact pivots pass.
This increased a source enclosure budget for a **new universally quantified
ansatz theorem**; it did not re-run the eight old fixed trials at greater
floating precision.

## OS-SOURCE-03: what changing kappa alone can and cannot establish

A genuine high $q\ne0$ necessarily bounds every admissible source lower
constant by

\[
\kappa\le \frac{\langle q,Gq\rangle}{\langle q,Kq\rangle}.
\]

The frozen rational candidate
$q=l_5+\frac32l_7-\frac12l_{11}$ was selected from a finite generalized
eigenproblem and then evaluated using full-source rational intervals.
Its certified upper ratio is approximately $0.8181235146152178$ (display only); the precise
fraction is in the final receipt. It is an **upper bound on admissible
kappa**, not a coercivity lower bound. It does not prove $\kappa\le1/5$.

Therefore this round has **not** excluded every possible improvement of
kappa as a repair for the degree-eight family. The interval between the
proved failure range and that genuine high Rayleigh cap remains unresolved.
A false extension to all kappa was specifically tested and rejected.

## OS-SOURCE-04: genuine certified upper Schur bracket

For every admissible finite-column response $U:PH\to QH$, source range
and completed-square identities give the inherited exact order

\[
H_U-\kappa_*^{-1}C_U^{\rm quot}\preceq S_0\preceq H_U,
\quad H_U=(P-U)^*G(P-U)=A-L_U.
\tag{3}
\]

A new degree-eight response is selected by a finite midpoint Galerkin
solve, rounded to a declared rational coefficient grid of denominator
$10^9$, then **frozen and re-evaluated with full source intervals**.
The finite solve is only candidate selection. The rigorous result is the
exact interval evaluation of $H_U$, with all omitted Gamma terms, and
its rational Loewner upper majorant. This is not the previous frozen trial.

`certified_polynomial_upper_short` records the rational four-by-four
**form** matrix $H^+\succeq H_U\succeq S_0$. For each parity sector the
reported rational cap $c$ passes the exact test
$cW_{\rm sector}-H^+_{\rm sector}\succeq0$. Its 32-step bisection uses
rational principal minors, never floating eigenvalue acceptance.

The best certified bracket supplied by this lane is thus the actual
matrix order

\[
\boxed{A-\frac{75625}{20699}I_P
\preceq S_0\preceq H^+.}
\tag{4}
\]

The lower side is inherited and coarse. The new upper matrix and its two
small parity caps are source-certified, but remain **positive upper
bounds**. The certified upper operator caps are approximately $0.0004516288172453642$ in the odd sector and $0.0017016646452248096$ in the even sector. In particular, outward rational caps $113/250000$ and $851/500000$ are valid. The exact tighter fractions and complete matrices are in the final receipt.

No corresponding improved rigorous derivative-Gram lower bound
was closed. In particular, neither (4) nor a positive $H_U$ proves the
sign of $S_0$.

## OS-SOURCE-05: distinct threshold-aware response experiment

The new response space consists of **degree-zero splines** $piecewise
constant functions$, projected exactly off $P_0,\ldots,P_4$. The positive
knots are

\[
0,\ 1/16,\ 1/8,\ 3/16,\ 193147/10^6,\ 1/4,\ 5/16,\ 3/8,\ 7/16,\ 1/2.
\]

For each cell $[l,r]$, take the reflected even/odd indicator and subtract
its exact rational low Legendre projection. The first even cell is omitted
to remove the constant-step dependency. This gives 17 high columns, 8 even
and 9 odd. All columns are in $QH\subset L^2$; $G$ maps them to $H^1$,
so the quotient derivative residual is lawful despite jumps in the trials.
No smoothness of the response itself was assumed. Their four low moments
and reflection eigenvalues are verified exactly.

The rational knot near $\log2-1/2$ changes only the response space. The
actual source threshold is always the authenticated $\log2$, with weight
$\log2/\sqrt2$. It is not replaced by the nearby rational number.

For a raw cell, its derivative response is exactly

\[
\frac{d}{dx}G\mathbf1_{[l,r]}(x)=g(x-l)-g(x-r).
\]

The full real Gamma kernel is numerically evaluated by the independent
representation, $z=e^{-r/2}$,

\[
4\sum_{n\equiv1\pmod4}\frac{z^n}{n^2}
=\operatorname{Li}_2(z)-\operatorname{Li}_2(-z)
+2\operatorname{Im}\operatorname{Li}_2(iz).
\]

Subtract its value at $z=1$. Differentiation gives exactly
$-\operatorname{atanh}(z)-\arctan(z)$, independently checked against
direct derivative integration. The low polynomial columns are integrated
from the complete $g'$. The source form is evaluated as
$-\int (Vv_i)(Gv_j)'$, with a separately constructed low Legendre matrix
as a representation check. Both routes share one arithmetic provenance.
Dilogarithms and numerical Catalan's constant here are **not interval proof
primitives**.

Three responses were fitted in the same space:

1. Ordinary source Galerkin, minimizing $H_U$.
2. Least squares for the actual $K_Q^{-1/2}$-residual, minimizing
   $C_U^{\rm quot}$.
3. Direct maximization of the sufficient lower matrix
   $H_U-\kappa_*^{-1}C_U^{\rm quot}$. In this finite space its high Hessian
   is numerically negative definite; solving that quadratic chooses a
   common maximizer for all low columns. This is a numerical optimization,
   not an exact proof of the continuum Gram or the Hessian sign.

Candidate coefficients were frozen as rational numbers with denominator
$10^{10}$ on 8 nodes per panel and then evaluated, **without refitting**,
on 16 nodes per panel. Panels split at response edges and actual shifted
prime thresholds. The implementation checks the actual Q projection,
parity, coordinate normalization, and matrix/basis identity.

| Frozen response | odd min lower estimate | even min lower estimate | odd min upper estimate | even min upper estimate |
|---|---:|---:|---:|---:|
| source Galerkin | -0.00940713 | -0.04031587 | 0.00000122084 | 0.00000688202 |
| relative least squares | -0.00753607 | -0.03675400 | 0.00000129909 | 0.00000705142 |
| lower-form optimum | -0.00753547 | -0.03675335 | 0.00000130234 | 0.00000705581 |

**All entries in this table are TESTED_MODEL / NUMERICAL ONLY.** Their
negative lower estimates do not show a negative source direction. Relative
optimization improved over ordinary Galerkin **within this space**, but
this space did not improve on the previous rank-20 polynomial lower estimate
(about -0.01623 with the older 1/50 comparison). Different kappa and response
spaces must not be conflated into a certified cross-study improvement.

At the frozen optimum, the numerical kappa needed to make the lower matrix
PSD is about 2.0171 in the odd sector and 0.9948 in the even sector. These
exceed the genuine high Rayleigh cap near 0.82, suggesting that changing
kappa alone will not repair these particular spline trials. This is **not**
a certified no-go because the residual Gram lacks rigorous continuum error.

The low-matrix independent representation discrepancies are about
$1.77\times10^{-10}$ on the fit grid and $3.09\times10^{-12}$ on the
holdout grid. The much larger changes in residual lower estimates, up to
about $4.31\times10^{-5}$, must not be hidden by that low-block agreement.
They illustrate that accurate low source moments do not certify the high
relative response. Full matrices, frozen coefficients, per-sector coupling
estimates and quadrature asymmetries are retained in the receipt.

## Approximation and continuum error debt

The compactness lane proved that
$R_Q:q\mapsto\Pi_M(Gq)'$ is bounded $QH\to M$, with
$\|R_Q\|\le\|g'\|_1$; hence high Legendre polynomials are dense in its
**bounded-map graph norm**, equivalent to $L^2$. This lane does not claim
that polynomials are non-dense.

What remains is whether the specific target
$\Pi_M(Gx)'$ belongs to the closure of $\operatorname{Ran}R_Q$, together
with quantitative, certifiable approximation rates. Polynomial density
alone does not answer the range question. Ordinary D-Galerkin optimality
controls a weaker energy error and does not imply the residual norm used in
(3). The compactness lane's interleaved compact block countermodel separates
these notions; it is a synthetic countermodel, not Suzuki source evidence.

The inherited helper
`tate_suzuki_shorting.original_gamma_derivative_l1_tail` already proves

\[
\eta_J\le 2/(4J+1)+8/(4J+1)^2,
\qquad \|\Pi_M((G-G_J)v)'\|_2\le\eta_J\|v\|_2.
\]

For any $\epsilon>0$, Young's inequality on columns gives
$C_{\rm full}\preceq(1+\epsilon)C_J+
(1+\epsilon^{-1})\eta_J^2 V_{\rm trial}^*V_{\rm trial}$, where
$V_{\rm trial}=P-U$, not the integration operator named $V$ above.
The compactness lane owns the propagation helper. This existing tail
formula is not claimed as a discovery. A rigorous enclosure of the entire
finite-Gamma derivative Gram $C_J$, including cross terms and spatial
quadrature errors, is still required. The present exact source **operator**
tail cannot replace this differentiated-tail obligation.

## Hostile controls and failures retained

- Real rational 2x2 PSD checks require both diagonals and the determinant;
  positive diagonal blocks alone do not certify the Schur complement.
- A negative sufficient lower form is compatible with a positive original
  finite form; the exact synthetic regression keeps that distinction.
- Every corner of the six independent interval entries of the 3x3 ansatz
  majorant is checked against the exact Loewner upper. Independent exact
  principal determinants agree with its LDL pivot products.
- The coarse Gamma budget remains UNRESOLVED, not a failed mathematical
  theorem. More source intervals certify the stated family, not the sign.
- Fake primitive composite 6 is rejected by the actual source tape although
  its hinge lies outside this radius. Local kernel agreement cannot identify
  global Euler provenance.
- Missing/duplicated prime 2, deleted/sign-flipped poles, duplicated real
  Gamma, wrong Gamma parity, deleted contact and wrong half-density change
  source channel evaluations. All these controls preserve reflection.
  None is accepted as another legitimate zeta source.
- A different response basis cannot borrow a numerical source matrix through
  a source-name token; forged low projection coefficients are rejected.
- Initial numerical calibration at four nodes per panel failed its unchanged
  $2\times10^{-8}$ tolerance (error $2.26217\times10^{-7}$). The failure
  log is retained. Resolution was increased to eight; the tolerance was not
  weakened. No exact source certificate depended on this quadrature.

## Claim/status ledger and reproduction

| ID | Result | Authority and boundary |
|---|---|---|
| OS-SOURCE-01 | Conditional contraction and two 2x2 sector criteria | PAPER_PROVED classical congruence plus inherited source range/parity |
| OS-SOURCE-02 | All complex degree-eight parity responses fail the residual criterion for $0<k\le1/5$ | PAPER_PROVED plus exact full-source rational intervals; only the criterion and this ansatz |
| OS-SOURCE-03 | Genuine high Rayleigh upper cap on admissible kappa | EXACT_SOURCE_INTERVAL; does not establish kappa<=1/5 or a larger high lower bound |
| OS-SOURCE-04 | Frozen rational trial gives continuum $S_0\preceq H^+$ with parity caps | PAPER_PROVED variational order plus exact source intervals; no sign conclusion |
| OS-SOURCE-05 | Threshold-aware 17-column relative-response experiments | TESTED_MODEL; continuum derivative-Gram error unresolved |
| OS-SOURCE-OPEN | $S_0\succeq0$ at radius 1/2, all-radius Weil positivity, RH | OPEN, NOT PROVED |

These are new-to-SUCC integrations and a new source-specific method
obstruction. No priority or academic novelty claim is made. No Lean
formalization was performed by this lane. Other workers own formal proofs.

From the worktree root, serial, with bounded numerical thread use:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/succ-proof-teeth-py313/bin/python -B scripts/observer_schur_source_probe.py \
 --numerical --fit-nodes 8 --holdout-nodes 16 \
 --output research/2026-10-16/source-schur-final.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/succ-proof-teeth-py313/bin/python -B -m unittest discover \
 -s tests -p test_observer_schur_source.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/succ-proof-teeth-py310/bin/python -B -m unittest discover \
 -s tests -p test_observer_schur_source.py -v
```

Final exact fractions, source and code hashes, commands, tool versions and
stable-byte checks are in `source-schur-final.json`; focused test logs and
`source-schur-validation.json` report actual completion. Earlier exact and
numerical receipts retain their own earlier implementation hashes. The
initial failed calibration log is preserved. The principal owns provenance,
full-suite and CI integration; this worker did not run the full suite.

The next consequential missing analytic step is an authenticated quantitative
bound on the target's distance to the range of the quotient derivative
response, accompanied by a rigorous continuum residual Gram for an
improved trial. Repeating fixed-trial floating eigenvalues cannot discharge
that obligation.

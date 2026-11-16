# Source map and dependency audit

## Repository and conversation provenance

| Source | Pinned identity | Use in this round |
|---|---|---|
| SUCC Main XXV | `db9fb4b84672050efa79b13377f1e73364598a14` | Historical base and mandatory research/test instructions. |
| First boundary-filter round, local | `5d9917031855f806fd5c1f9d8b4543ad3ca24bbf` | Exact dossier inspected by the three initial derivations. This local SHA was not itself published. |
| First boundary-filter round, published | `f4151c4ae877ee43c4b7d130174b6bec1dbab9d6` | Parent of the continuation on draft PR #605. Tree `3a3fc5153408553332a22abbf14415fdde661575` matches the local snapshot exactly. |
| Active donor PR #604 | `220df67b4ee3f558de63f08cc76ed52b34138302` | Source-authenticated observer and arithmetic frontier, inherited through the first-round source map. |
| Active donor PR #601 | `774191e7679cd63c56bdb105541ce21c8ee27448` | Existing exact prime-sector projector; prevents calling a newly displayed projector the first such construction. |
| Active donor PR #600 | `dbc7fed19189016f6ab27550f3e84940b632b09b` | Actual versus counterfeit source distinction and the gap between aggregate CRT information and individual targets. |
| User's current request and relevant prior chats | Reconstructed in the [prior source map](../holographic_boundary_filters/SOURCE_MAP.md) | Boundary-first reconstruction, ordered/twisted probes, current-frame comparison and explicit source/transport contracts. No new claim about unseen conversation history is made here. |

The user explicitly authorized publication before and after the further
research. The branch and draft PR preserve the existing research workflow.
No merge, tag, release, main rewrite, or imported archival edit is part of
this round. Publication uses an authenticated connector and exact tree
comparison; a different commit metadata hash does not change the tested
file contents.

## Mathematical dependency families

### A. Elementary integer, interpolation and norm arguments

The previous geometric filter and its leakage/coefficient bounds are in
[DAMPED_FILTERS.md](../holographic_boundary_filters/DAMPED_FILTERS.md).
This round's integer divisibility, coefficient-mass barrier, explicit
twins, channel brackets, one-channel aperture and exact noise examples
are fully derived in their notes. They import no unproved arithmetic
estimate. The all-integral histogram theorem is stronger in its input
promise than the earlier zero-count-only integrality condition.

For classical context on annihilator methods, Peter, Potts and Tasche,
*Nonlinear Approximation by Sums of Exponentials and Translates*, SIAM
J. Sci. Comput. 33(4), 1920-1947 (2011),
[author-hosted paper](https://www-user.tu-chemnitz.de/~potts/paper/nprony.pdf),
Section 2, Lemmas 2.1-2.2, connects sampled exponential kernels and
annihilating polynomials. The constructor and root inspected the paper.
It is context, not authority for the particular integer mass bounds.
There is no worldwide priority claim for those bounds or their
classical ingredients.

### B. Classical Selberg--Delange means

- Cellarosi, *Smooth Sums over Smooth k-Free Numbers and Statistical
  Mechanics*, [arXiv:1304.6610](https://arxiv.org/pdf/1304.6610),
  equations (10)-(11), PDF page 5: the fixed complex mean for
  `sum_(m<=x) z^Omega(m)` in `|z|<2`. The unversioned URL returned
  the v2 paper; an explicit version URL intermittently failed retrieval.
- de la Bretèche and Tenenbaum, *Remarks on the Selberg--Delange method*,
  Acta Arith. 200.4 (2021), 349-369,
  [author manuscript](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf),
  Theorem 1.2 and equations (1.10)-(1.12): a directly audited complex
  formulation. Theorem 2.1 has a nonnegativity restriction and is not
  used for phase-valued weights.

The constructor, separate paper auditor, and root read the load-bearing
passages. For `f(m)=z^Omega(m)`, choose `rho=z`, `r=|z|`, `sigma=3/4`,
`A=4`. The prime residual is zero; the prime-power sums converge. The
saved logarithmic power covers the required error throughout the closed
unit disk, including the negative-real gamma-zero case. Positive `R`
has a positive Euler-product leading constant. These are two routes
through one classical source family, not independent arithmetic evidence.

The new complex triangle estimate is derived locally by a prefix bound,
an absolute-mass bound, and an `O(Y)` endpoint strip. The prior
positive-measure triangle lemma is applied only at the positive real
node. All node parameters remain fixed in this obstruction proof.

### C. Classical quantitative almost-all Goldbach

R. C. Vaughan, *A new estimate for the exceptional set in Goldbach's
problem*, Proceedings of the St. Louis symposium, AMS (1973),
[author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/StLouis72.pdf),
printed page 315. The exact import is the mean-square estimate displayed
**before equation (1)**, with the page's definitions of ordered genuine
prime-pair count, reciprocal-log main term and singular product. The
paper attributes this classical logarithmic estimate to the earlier
almost-all methods. No exceptional-zero correction is dropped from the
stronger subsequent equation (1), because that equation is not imported.

The initial arithmetic author inspected retrieval and OCR. The root
independently retrieved the paper, rendered the first page and visually
checked the formulas. The separate paper auditor also inspected that
render and the successful retrieval. All three inspected the same
primary source; this does not turn one imported theorem into three
independent witnesses. The local deduction controls quantitative count
size on the good set, then pays the filter error. Mere almost-all
existence would not pay the coarse-resolution loss.

The asymptotic aggregate uses the classical prime number theorem and
the prior positive triangle derivation. The current work improves no
classical Goldbach exceptional-set exponent and gives no effective
threshold. The infinite exceptional-set quantifier remains open.

### D. Angular projection

The phase-aperture note uses the classical coefficient identity obtained
by integrating `exp(i h theta)` over a full circle, and the finite
root-of-unity sum. Both are proved directly for the specified
nonnegative finite-mass series. The continuum interface and finite
sampling interface are kept distinct. A phase coordinate has its
declared orientation `z=R exp(i theta)`; it is not an undeclared physical
or quantum phase. The Cauchy-formula attribution was checked against
[NIST DLMF 1.9.30](https://dlmf.nist.gov/1.9.E30). The power-only
counterexample explicitly separates signed profiles from magnitudes.

## Implementation and audit provenance

The three initial fronts were assigned separately. A premature
cross-audit request was declined until those initial results were
banked. The two later cross-audits explicitly read those results. All
agents and root use the same model family and share the earlier dossier.
This is method triangulation with disclosed dependence, not external
referee agreement or a formally checked proof.

The main independent decompositions are:

- polynomial multiplication versus elementary symmetric sums and
  homogeneous integer root evaluation;
- geometric Lagrange coefficients versus direct grade products;
- smallest-prime-factor arithmetic versus trial factorization and a
  separate direct primality predicate;
- Cesaro phase means versus elementary norm bounds, and explicit
  signed-triangle endpoint accounting;
- interval feasibility and integer rounding versus designed equality,
  normalization, fractional-count and phase-alias countermodels.

Exact finite outputs are reproducibility witnesses, not measurements of
the truth of an asymptotic law. A source label, digest, theorem statement,
or internally consistent response packet does not itself authenticate
the response acquisition.

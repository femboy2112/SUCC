# Independent lane review of G4 and S1–S3

Reviewer lane: `viii_clocks`, 2026-10-21. Target dossier:
`VIII_SECTION_LATTICES_AND_SIMPLEX_LAWS.md`, SHA-256
`765ca5c6bd8ac7cd45864c08afd8fb5af7dd7d342237527c55cb8549b90d9373`.
No target files were edited. This is a separate-agent same-model review,
not external refereeing or a formal-kernel proof.

**Verdict: G4, S1, and S3 survive reconstruction; S2's finite enclosure is
valid, with one explicit asymptotic-hypothesis correction requested.**

G4's centered-cell proof uses a full-rank basis of the actual section
lattice, its Euclidean covolume, and a positive point in the relative
interior. These assumptions suffice. The upper homothety contains every
counted half-open cell. In the lower homothety's relative interior,
subtracting any fundamental-cell offset preserves strict coordinate
positivity and gives sum strictly below X. Coordinate and sum functionals
are nonzero on the section because the positive center exists, so omitted
boundaries have zero section volume. No lower-box bound is incorrectly
transferred to a simplex, no ambient covolume replaces the section's,
and the moving-family condition r*beta/X->0 controls the relative error
with all geometric dependence explicit. The theorem counts the full
lattice family, not a primitive subfamily's density.

An independent exact check uses rational halfspace intersections and a
monotone convex hull in rank-two lattice coordinates. The polygon's
coordinate area equals Euclidean section volume divided by lattice
covolume, since the same Jacobian multiplies numerator and denominator.
Direct integer-coordinate census then checks G4 on eight distinct sections
at each integer cutoff 0,...,160. The script imports no target code. All
1,288 checks pass, including mixed-sign bases and the ambient-index
counterexample at M=3 and M=7. Finite census does not prove G4 universally;
the reconstructed cell argument does the mathematical work.

S1 has an alternative short derivation: for 0<=u<1,

\[
 -\log(1-u)-\sum_{\ell=1}^k u^\ell/\ell
 =\int_0^u\frac{t^k}{1-t}\,dt.
\]

Bounding 1/(1-t) between 1 and 1/(1-rho) and summing over j/N gives the
stated rational remainder enclosure. The power-sum integral bound and
the fixed-depth moving-m regimes follow. S3 preserves the exact shifted
population N_rho; its maximum remainder controls positive summation over
all occupied residues. Under t->infinity and m^(k+2)/t^(k+1)->0,
m=o(t), all strata are eventually occupied and the bound is uniform.
The two W=2 examples correctly exhibit opposite square-root corrections.

S2's binomial mode argument and finite rational bounds hold, including
N=m=0. Its sentence “if m/N->alpha then N^{-1}log binom(N,m)->H(alpha)”
must explicitly include **N->infinity**. Without that hypothesis, the
constant sequence (N,m)=(2,1) has m/N=1/2 but
(log 2)/2 != H(1/2)=log 2. This is a missing quantifier in the asymptotic
sentence, not a defect in the finite entropy theorem or an obstruction to
the intended growing-population result.

Reproduction after the target dossier is present in the same repository:

```sh
python research/2026-10-21/viii_geometry_cross_review.py \
  research/2026-10-21/VIII_SECTION_LATTICES_AND_SIMPLEX_LAWS.md \
  research/2026-10-21/VIII_GEOMETRY_CROSS_REVIEW_RECEIPT.json
```

The receipt records the exact target content hash, bases, rational areas,
centers, cell budgets, and counts at the maximum tested cutoff.

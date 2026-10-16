# Signed collective spectral observers

**PROVED LOCAL, PAPER + EXACT FINITE EXECUTION. Actual source sign OPEN.**
This lane proves signed polarization and a conditional finite witness budget,
and improves both authentic first-window Schur lower bounds by exactly removing
low polynomial derivative moments. No kernel formalization, density rate, or
RH conclusion is claimed. No nontrivial zero coordinates are inputs.

Authority: only `observational_succ/collective_spectral.py`,
`tests/test_collective_spectral.py`, `scripts/collective_spectral_probe.py`, this
dossier, and `collective_observer_receipts/spectral*` belong to this lane.
Initial worktree HEAD was `940f089d10926ecbdf24ee9e3483c993042b9275` on
`research/collective-observer-2026-10-16`. No Git mutations were performed.

## 1. Source, execution, and claim boundaries

The source sibling is pinned to PR137
`95dbf40553e54c901e9998e14b1b9d67298fa89e`. Its original Suzuki source has
blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, SHA256
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`, origin
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. This lineage differs from the
founding 72-file import manifest. Both were inspected; neither was modified.
The signed source conventions agree with
[Suzuki (1.3), §2.1, §8](https://arxiv.org/html/2606.09096v3).

There are no PR137 package imports in this lane's module. The probe accepts
`--source-root PATH` and executes the pinned sibling in an isolated Python
subprocess. Before and after execution it checks the sibling HEAD, all **315**
pinned package Python files, the source packet and six source/proof documents.
It separately hashes the **44** loaded sibling modules. Original source runtime
checks also execute. This permits a CI checkout made by
`git worktree add --detach "$RUNNER_TEMP/spectral-pr137" 95dbf40553e54c901e9998e14b1b9d67298fa89e`
from full Git history, followed by `--source-root "$RUNNER_TEMP/spectral-pr137"`.
The principal owns that integration; no source import or merge is required.
A missing sibling, commit, dependency, or changed byte fails closed.

Read and audited at that pin: `COMPACT_SOURCE_GALERKIN.md` CG-02–04,
`FRACTIONAL_SOURCE_RANGE_AUDIT.md` SR-01–04,
`AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md`, the optimal-residual review,
`arithmetic_resolvent.py`, `compact_galerkin.py`, the derivative/Legendre
source implementations and the exact source packet. The source-range result
is conditional qualitative density, with a logarithmic maximal-domain argument.
It supplies **no approximation rate**. The present quantitative witness theorem
uses the compression estimate instead; the new arithmetic bound uses no density.

Epistemic coordinates remain separate: κ/contact is execution of the original
signed formula; φ/survival is exact tests and the stated proofs;
σ/source correctness includes byte identity and a separate paper-level source
identification; ρ/commitment is controlled by retaining the failed candidate.
Shared source, contact constants, coercivity, and interval primitives mean these
routes are one source family. The endpoint check is a different implementation
route, not an independent source or independent reasoner.

## 2. Exact collective polarization, including apparatus existence

Let V be a real vector space with symmetric bilinear h, or a complex vector
space with Hermitian h **linear in its first argument**. Let q(x)=h(x,x).
No positivity is assumed. Expanding by (sesqui)linearity gives

    q(x+y)-q(x-y) = 4 Re h(x,y),
    q(x+i y)-q(x-i y) = 4 Im h(x,y).

Indeed, h(x,iy)=-i h(x,y) and h(iy,x)=i conjugate(h(x,y)); their sum is
2 Im h(x,y). The other signs reverse that term. Therefore

    h_real(x,y) = [q(x+y)-q(x-y)]/4,
    h_complex(x,y) = [q(x+y)-q(x-y)+i q(x+iy)-i q(x-iy)]/4.

The second sign reverses for a conjugate-first convention. Real probes recover
only the real part of a complex pairing. `Gaussian` implements Q(i) exactly.
For the code's matrix convention, h(x,y)=sum x_i G_ij conjugate(y_j).

**Apparatus theorem.** For a finite set of vectors, if each required
superposition is admissible and its signed q value is available in one source,
normalization and phase convention, the finite query map above recovers every
pairing. Mathematical existence is immediate: take that finite union as the
query domain and restrict q to it. Conversely, the algebra supplies no physical
preparation/measurement apparatus. `QuadraticApparatus` explicitly records its
finite domain and rejects missing complex superpositions. Independently sourced
or clipped/absolute-valued q readings do not satisfy the theorem's premises.

**Hostile receipts.** G=[[1,2],[2,1]] gives q(e1)=q(e2)=1,
q(e1+e2)=6, q(e1-e2)=-2, h(e1,e2)=2; positive private diagonal readings miss
an actual negative collective direction. The eigenvectors (1,1),(1,-1) have
eigenvalues 3,-1, verified by multiplication. A positive Gram realization of
this G is impossible, since its negative vector would have negative squared
norm. For G=[[1,2i],[-2i,1]], every real vector has q(x)=||x||², while
q(e1-i e2)=-2. This defeats real-only complex tomography. Neither matrix is
substituted for the arithmetic source.

## 3. Typed interval intersection and provenance

An interval carries source blob/origin, radius, ordered basis, complete signed
channel list, coordinate metric, target, and inner-product convention.
For one common real quantity, verified enclosures [a_i,b_i] intersect to
[max a_i,min b_i]. Proof: a value lies in every interval exactly when it is
above every lower endpoint and below every upper endpoint. Empty intersection
is an inconsistency, not evidence to average. The same interval rule encloses
all eigenvalues of the *same normalized sector* when each bound is uniform.

The implementation rejects mismatched source, radius, basis, channels, metric,
target or convention **before** intersection. A basis change requires a proved
congruence and transported metric; relabeling is insufficient. In particular
S_epsilon and S0 cannot be interchanged. Provenance dependencies form connected
components by shared labels, including transitive bridges. Repetition changes
neither a set intersection nor the number of source families. Distinct labels
alone do not prove independence: `independence_established` is always false.
The typed API is conditional algebra, not semantic authentication. The separate
pinned-source probe authenticates the arithmetic experiment and preserves the
paper premises. A forger could supply a false interval with correct labels;
the labels cannot turn it into a theorem.

## 4. Audited compression theorem and a quantitative rational witness

Use I=(-1/2,1/2), H=L²_0(I), l_j(t)=P_j(2t), and orthogonal P_N onto
span(l_1,...,l_N). The actual signed G is the mean-zero compression of
convolution by g, with g(0)=0. The inherited whole-cell source enclosure,
**freshly replayed here**, proves ||g'||_1<11/40. Young's inequality gives
||(Gf)'||_2≤(11/40)||f||_2. The norm cap has a separate elementary proof:
g is absolutely continuous and even, g(0)=0, hence
sup_{[-1,1]}|g|≤∫_0^1|g'|=||g'||_1/2. Consequently the kernel cut off to
[-1,1] has L1 norm at most ||g'||_1. Young, zero extension of the input,
restriction to I, and orthogonal mean-zero compression give ||G||<11/40.
This conservative cap concerns the complete signed source at radius 1/2.

For normalized Legendre e_j=sqrt(2j+1)l_j, the equation
-((1/4-t²)e_j')'=j(j+1)e_j and vanishing endpoint weight imply
∫(1/4-t²)e_i'e_j'=j(j+1)delta_ij. Integration by parts and Bessel in
L²((1/4-t²)dt) give, for f∈H¹(I),

    sum j(j+1)|<f,e_j>|² ≤ ∫(1/4-t²)|f'|² ≤ ||f'||²/4.

The integration-by-parts identity extends from smooth f by H¹ approximation;
no H¹ convergence of Legendre partial sums is needed. Polynomial completeness
then gives ||(1-P_N)G||≤11/[80 sqrt((N+1)(N+2))]. Self-adjointness controls
the opposite side. Decomposing G-P_NGP_N=(1-P_N)G+P_NG(1-P_N) proves

    ||G-P_NGP_N|| < 11/[40 sqrt((N+1)(N+2))] ≤ 11/[40(N+1)].  (1)

This audits CG-03's projection order: derivative-after-output-projection
contraction is never used. The first endpoint singularity of g' is handled by
the inherited exact logarithmic-cell bound, not point sampling.

**Conditional quantitative theorem.** Suppose ||x||=1 and q(x)≤-δ<0, with
0<δ≤M and ||G||≤M. Set

    N=max(1,ceil(11/(10δ))-1),  η=min(1,δ/(16M)), D=ceil(N/η).

By (1), z=P_Nx has q(z)≤-δ+δ/4=-3δ/4 and ||z||≤1.
Round both real and imaginary unnormalized Legendre coefficients to denominator
D. For the resulting rational vector w,

    ||w-z||² ≤ sum_{j=1}^N 1/[2D²(2j+1)] ≤ N/(2D²) ≤ η².

The perturbation identity and Cauchy–Schwarz give
|q(w)-q(z)|≤Mη(2+η). Since δ≤M, η≤1/16 and this is ≤33δ/256<δ/4.
Thus q(w)<-δ/2. A sound quadratic enclosure with absolute upper error ≤δ/4
still certifies negativity. Writing z=sum c_j l_j gives
sum |c_j|²/(2j+1)=||z||²≤1, so each real and imaginary coefficient has
absolute value ≤sqrt(2j+1)≤sqrt(2N+1). Set
K=ceil(D sqrt(2N+1))+1. The numerator grid {-K,...,K} for each real and
imaginary part contains the rounded vector. It has at most (2K+1)^(2N)
candidates. The API returns this count as a base/exponent pair and the strict
log2 bound 2N bit_length(2K+1), without materializing the huge power.
This proves a finite coefficient grid as well as a compression degree, without
requiring a rational unit vector. For δ=1/10,1/100,1/1000 the degrees are
10,109,1099 and denominators 440,47960,4835600.

This is **conditional on a negative unit direction of the full G**, not on a
negative conservative lower endpoint or a low Schur margin. The module computes
budgets, not the unknown witness. Existing PR137 entry APIs cap degree at 20;
a general source evaluator at degree 1099 is not implemented here. Existence of
refinable sound finite quadratic enclosures is an additional apparatus premise.
The explicit Gamma operator tail 2/(4J+1)²+16/(4J+1)³ and separate entry errors
must be multiplied by the trial norm where applicable.

**No universal shallow short-depth.** On R⊕ell² let A=1/2,
D e_j=4^-j e_j and b=2^-m e_m, m=d+1. This is a bounded compact self-adjoint
block source, D>0, and ||D^-1/2 b||²=1. Its short is S0=-1/2, while every
compression seeing only high modes 1,...,d has short +1/2. The explicit vector
(1,-2^m e_m) has q=-1/2, but its unit normalization has margin
1/[2(1+4^m)], tending to zero. Hence even a fixed negative *short* margin
supplies no universal shallow high-mode depth. This family has hidden source
coupling and is explicitly synthetic; it neither refutes (1) nor proves an
arithmetic obstruction. The different normalization explains why it does not
contradict the full-operator-margin theorem.

## 5. New arithmetic bound: exact low derivative moments

Fix the authentic source, l_j=P_j(2t), j=1,...,4, Mcal=P_3^perp, and
h_j=(G_J l_j)' with J=20. Let E_j bound ||h_j||². The source coercivity
D_high≥κ K_Q, κ=20699/10^6, is inherited; its finite certificate is replayed,
while its continuum proof remains a paper dependency. For low x and high u,
Vu∈H¹_0∩Mcal and integration by parts gives

    <Gx,u>=-<(Gx)',Vu>=-<Pi_Mcal(Gx)',Vu>.

Therefore the variational inverse energy, using D_high≥κ V*V, obeys
R0≤κ^-1 R_P*R_P, R_P x=Pi_Mcal(Gx)'. The same finite supremum implies the
square-root range condition by spectral calculus: truncated inverse energies
increase to ||D_high^-1/2 b x||² and remain bounded. This uses no high inverse,
no fractional domain beyond the square-root range, and no dense-range rate.

Since ||l_k||²=1/(2k+1), orthogonal projection gives the exact identity

    ||Pi_Mcal h_j||² = ||h_j||² - sum_{k=0}^3(2k+1)|m_jk|²,
    m_jk = ∫_I h_j(x)l_k(x)dx.                              (2)

**First failed candidate retained.** The midpoint enclosure |h'_j|≤V_J yields
moment error V_J/(4n) at grid n=512. Every moment interval met zero; all
subtractions were zero and neither inherited cap improved. The full receipt
is `spectral-projection-grid512-failed.json`, not overwritten or relabeled.

**Exact replacement.** For 0≤r≤1 define the rational polynomial

    psi_kj(r)=∫_{-1/2}^{1/2-r}
       [l_k(y+r)l_j(y)-l_j(y+r)l_k(y)]dy.

Split the square into x>y and x<y, change variables r=|x-y|, and use oddness of
g'_J. Fubini proves m_jk=∫_0^1 g'_J(r)psi_kj(r)dr. This includes k=0 and
all boundary contributions. At the pinned source,

    g'_J(r)=-2e^(r/2)+2e^(-r/2)+C_infinity/2
             +(log2)/sqrt2 1_(r>log2)-sum_{s=0}^{J-1} 2/(4s+1)e^(-(4s+1)r/2).

The polynomial is generated by finite binomial expansion and rational
integration. For each monomial define I_n(α)=∫_0^1 r^n e^(-αr)dr. Integration
by parts gives I_0=(1-e^-α)/α and I_n=n I_(n-1)/α-e^-α/α, valid for either
nonzero sign of α. Each channel is thus an exact affine expression in certified
exponentials, contact and log2/sqrt2. The step integrates a polynomial from
log2 to 1, with interval evaluation at the endpoint. Arithmetic remains
outward rational; no floating-point gate is used. All channel intervals and
polynomials are in the final source receipt. Matching parities give psi=0.

An additional source route computes raw (G_J l_j)(1/2)=∫_0^1 g_J(r)P_j(1-2r)dr
and verifies m_j0=[1-(-1)^j](G_J l_j)(1/2). Both endpoints, both poles, the
contact and the prime hinge are retained. Its interval intersects the direct
correlation interval in all four cases. Polynomial controls independently
compare difference-variable integration with full two-variable integration for
kernels r,r³,r⁵ and sign(r). Exact moments also intersect all earlier sound
cell-moment enclosures; contradictory results fail closed.

For each moment interval [a,b], set d=max(0,a,-b), so d≤|m_jk|. Then
E_j-sum(2k+1)d_jk² bounds the projected energy by (2). E_j is recomputed from
all original midpoint intervals with full-cell bound

    E_j=sum_positive_cells [2h M_i² + M_i V_J h² + V_J² h³/6],
    M_i=max(|h_j(mid)_lo|,|h_j(mid)_hi|), h=1/512.

This integrates (M_i+V_J|x-mid|)² on both reflected cells. It is not a
sample-only squared norm. Normalized sector trace T is sum(2j+1) times these
projected energies. The omitted **derivative** Gamma tail is η_J=170/6561
(2/(4J+1)+8/(4J+1)²). Young plus projection contraction yields

    ||R_P,sector|| ≤ sqrt(T)+η_J,
    R0_sector ≤ c_sector I, c_sector=(sqrt(T)+η_J)²/κ.        (3)

A directed rational square-root upper is used. Replacing this derivative tail
by the smaller undifferentiated operator tail would invalidate (3).

With W=diag(1/3,1/5,1/7,1/9), and the freshly recomputed inherited finite-Gamma
low lower form A^-, the new bound is

    A^- - diag(c_odd/3,c_even/5,c_odd/7,c_even/9) ≤ S0.

The exact response caps are

    c_odd  = 401942050279861710702382408729 / 891024077979000000000000000000,
    c_even = 46594796936736757485815562001 / 55689004873687500000000000000.

They are strictly below PR137's respective caps 0.4549075377... and
0.8481468501..., becoming approximately 0.4511012219 and 0.8366965264.
Independent rational 2×2 diagonal/determinant checks give

    -7746694143/17179869184 I ≤ S0_odd  ≤ 300761/1073741824 I,
    -14373807789/17179869184 I ≤ S0_even ≤ 11742983/8589934592 I.

The upper forms come from PR137's pinned degree-20 rational trial receipt;
its integration was not rerun here, but its exact normalized scalar PSD
certificate was rechecked. The lower bound uses newly computed source cells,
new exact moments, a fresh low-form evaluation, and the explicit proof above.
The resulting intervals still straddle zero. Negative lower endpoints are
**not** actual negative source values. These improvements do not certify a
positive short, a negative direction, or universal positivity.

## 6. Reproduction and ledger

From the assigned worktree, with Python standard library only:

```sh
python -B -m unittest discover -s tests -p test_collective_spectral.py -v
python -B scripts/collective_spectral_probe.py --source \
  --source-root ../SUCC-arithmetic-resonance \
  --output research/2026-10-16/collective_observer_receipts/spectral-source.json
```

| Claim | Status | Hostile boundary / next discriminator |
|---|---|---|
| Real/complex signed polarization | PROVED LOCAL, PAPER; exact Q(i) tests | Unavailable i-superpositions and wrong conjugation fail |
| Same-target interval intersection | PROVED LOCAL, PAPER; exact tests | Wrong source/radius/basis/channels/metric/target rejected; forged semantic claims remain outside the type checker |
| Full normalized negative margin gives degree/grid budget | CONDITIONAL PAPER PROOF | Unknown actual margin; budget API is not a high-degree source solver |
| Fixed short margin gives shallow depth | REFUTED, exact synthetic family | Deep soft mode; normalized full margin collapses |
| Coarse midpoint moments improve the source cap | FAILED exact experiment | Retained grid-512 failure, all removal bounds zero |
| Exact signed source moments tighten both lower bounds | CONDITIONAL PAPER PROOF + EXACT SOURCE EXECUTION | Whole-high coercivity and source identification remain inherited paper authority |
| Original sign / effective residual-density rate | OPEN | Need a certified negative upper direction or positive full Schur lower form; present intervals decide neither |

Tests are finite regressions, not infinite theorems. New proofs and source
application are not Lean-checked. No independent agent review is represented.
Byte checks certify provenance, not analytic truth. Exact commands, test counts,
artifact hashes and replay equality belong to `spectral-validation.json`.

### Principal integration addendum

The preceding no-review statement describes the spectral lane's initial
handoff. A subsequent [independent hostile audit](../../reviews/2026-10-16_COLLECTIVE_OBSERVER_HOSTILE_AUDIT.md)
checked the signed moments using Taylor integration, moment subtraction,
derivative-tail accounting and the normalized scalar PSD certificates. It
retains the same original source and inherited continuum premises; it is not
a second arithmetic source. The original freeze hashes remain historical.
For a new replay use `/tmp/collective-spectral-source.json` as `--output`, or
the principal validation runner with a fresh directory, rather than overwriting
the frozen receipt shown in the lane's original command above.

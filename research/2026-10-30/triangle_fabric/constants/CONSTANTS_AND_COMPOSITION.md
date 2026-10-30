# Harmonic, golden and Euler constants under authentic source composition

**Status:** PROVED LOCAL paper results with exact finite certificates and a
separate computational oracle; no Lean or external referee authority. The
original Harmonic Numbers / Golden Ratio / Euler–Mascheroni triangle and
Oily–Macaroni name and construction retain **Leah / femboy2112** provenance.
Parent405 is `6cf5050ff2cfd92e7a0c8876da5233be6ff117f5`. No scholarly priority
is asserted. All results concern the stated positive source-composition law;
none asserts randomness or normality of the selected zero-seed BBP trajectory.

## 1. What is being composed, and where the constants do work

Keep exactly

    Q(x)=4−2exp(−3x)−exp(−4x)−exp(−5x),
    R(a)=∫exp(−ax)Q(x)dx=4/a−2/(a+3)−1/(a+4)−1/(a+5),
    μ_a(dx)=exp(−ax)Q(x)dx/R(a), a>0.

At a=8n−7, R(a) is the authentic forcing. Take **independent draws** X,Y
from μ_a, and retain both the sum S=X+Y and the proportion P=X/(X+Y).
This is a declared, source-correct convolution arrow, not a claim that two
successive BBP digits are independent samples from μ_a. Define B=P(1−P).
At the Gamma boundary, aS tends to Gamma(4,1), P tends to Beta(2,2), and these
limit coordinates are independent. At every finite a the independence fails.
This failure is quantified below; a common boundary snapshot hides a nonzero
finite composition defect.

| Constant/object | Actual role | What it does not establish |
|---|---|---|
| H_m and 1/r | Exact digamma successor increments; Gamma/Beta logarithmic composition | Signed selected cancellation |
| γ | Fixes the absolute normalized log-moment of Exp(1), ψ(1)=−γ, and the harmonic/log finite part | A separately surviving coefficient in normalized edge differences |
| λ=(sqrt5−1)/2 | The original two-stage unit-clock packet least fixed point is λ²; λ is its complement | A universal parameter for arbitrary grades or observation clocks |
| θ(r)=λ/(1−λ^r) | Exactly the clock that forces the rank-r PGF fixed point λ^r | A source-selected clock at every rank |
| Ω_OM=λ−γ | Rank-two absolute contrast Elog Gamma(2)−Eexp(−λ Gamma(2)) | An invariant of every arrow, or a selected phase estimate |
| 5/6 and λ³ | The rank2→4 harmonic and golden composition increments; the finite-source inequality below uses both | Independence of actual times or digits |
| 1379/900 | Variance of the native bounded rate mixture, hence the first non-product sum/proportion correction | A normality certificate; it is shared by suitable matched-jet mutants |

The historical triangle already supplies D(r)=ψ(r)−λ^r and
D(r+1)−D(r)=1/r+λ^(r+2). Those formulas are **inherited**, not new.
The new result here is an all-a source-composition inequality with an explicit
positive rational lower bound, together with its exact dependence mechanism.

## 2. A native hidden rate variable and strict ratio imbalance (FC01)

Set h(x)=Q(x)/(15x), with h(0)=1. The exact representation

    h(x)=E exp(−xT),
    Pr(T in dt)=[2 1_(0,3)(t)+1_(0,4)(t)+1_(0,5)(t)]dt/15

follows by integrating each exponential. Thus T is supported on[0,5],

    E T=59/30, E T²=27/5, σ²=Var(T)=1379/900>0.

This is a genuine latent realization of the **fixed** Q. A single h-value does
not determine this rate law; its full Laplace transform does. Equivalently,
μ_a is a Gamma(2,a+t) mixture whose rate mixing density is proportional to
[2 1_(0,3)+1_(0,4)+1_(0,5)]/(a+t)². This equality is checked by integrating the
conditional Gamma density; its mixing mass is R(a).

Let L=log h. Exponential tilting gives L''(x)=Var_x(T)>0. More quantitatively,
for x in[0,s], the tilted density relative to the original T law is
exp(−xT)/h(x)≥exp(−5s). Hence

    L''(x)=min_c E_x(T−c)² ≥ exp(−5s)σ².                         (1)

After the invertible change (x,y)→(s,u), the conditional density of P given
S=s, relative to Beta(2,2), is

    w_s(u)/E_beta w_s,    w_s(u)=h(su)h(s(1−u)).                (2)

Both w_s and B=u(1−u) are symmetric about1/2. Regard w_s as a function of B
on(0,1/4), using u<1/2. Differentiating gives

    d log(w_s)/dB
       = s[L'(su)−L'(s(1−u))]/(1−2u)
       ≤ −σ²s² exp(−5s).                                    (3)

Also exp(−5s)≤w_s≤1. Therefore

    dw_s/dB ≤ −K_s,    K_s=σ²s² exp(−10s).                    (4)

These inequalities extend to the midpoint by continuity. They show strict
imbalance: the finite-source ratio gives greater relative weight to unequal
splits than Beta(2,2), at **every** positive sum s.

For any increasing integrable f(B), use independent Beta variables B,B' and

    Cov(f(B),w_s(B))
      = (1/2)E[(f(B)−f(B'))(w_s(B)−w_s(B'))]
      ≤ −K_s Cov(f(B),B).                                    (5)

Dividing by E_beta w_s≤1 preserves the lower bound on the deficit.
For f(B)=B, direct Beta integration gives

    E_beta B=1/5, Var_beta B=1/350,
    1/5−E[B|S=s] ≥ K_s/350.                                  (6)

In particular, this is stronger than simply observing nonzero covariance.
Integrate (6) over the actual law of S. Since

    E[S² exp(−10S)]
       = 2[R'(a+10)²+R(a+10)R''(a+10)]/R(a)²,

we obtain the exact all-a inequality

    1/5−E B ≥ σ² [R'(a+10)²+R(a+10)R''(a+10)]/[175 R(a)²] >0.  (FC01)

Every quantity on its right is rational at rational a. No asymptotic
assumption, fitted numerical parameter or unverified distribution theorem is
used. A pure Gamma(2,c) law has h(x)=exp(−cx), σ²=0 and equality E B=1/5.
The original source has strictly positive σ² and cannot be that product law.

The mixed derivative 2s²L''(s/2) is the second u derivative of log w_s at1/2.
It measures this conditional-density deformation. It is **not** automatically
a categorical curvature, physical field strength or selected signed interaction.

## 3. A sharp harmonic composition correction, with γ cancelling (FC02)

Symmetry gives E[log P|S=s]=(1/2)E[log B|S=s]. Direct Beta integrals give

    E_beta log P=ψ(2)−ψ(4)=−5/6,
    Cov_beta(log B,B)=1/50.

Apply (5) to log B, which is integrable under these densities. The logarithmic
singularity can be handled by truncation and dominated convergence. We get

    −E[log P|S=s]−5/6 ≥ K_s/100.

Because log S−log X=−log P, integration proves

    Elog(X+Y)−Elog X−5/6
       ≥ σ² [R'(a+10)²+R(a+10)R''(a+10)]/[50 R(a)²] >0.       (FC02)

Thus the harmonic increment5/6 is a **strict lower comparison value** for the
finite authentic rank2→4 source arrow. It is not merely a decorative label.
Euler's constant cancels because this is a difference of normalized log
moments. The absolute rank-two boundary is still 1−γ.

Exact computational formula, independent of the conditional-density proof:
write c=(4,−2,−1,−1), b_i=a+(0,3,4,5)_i. Then

    Elog X=−γ−R(a)^−1 Σ_i c_i log(b_i)/b_i,

and Elog S=−γ+R(a)^−2 Σ_ij c_i c_j J(b_i,b_j), where

    J(b,b)=(1−log b)/b²,
    J(b,c)=[−log(c)/c+log(b)/b]/(b−c), b≠c.

The shared −γ coefficient is exactly one because Σ_ij c_ic_j/(b_ib_j)=R².
The code evaluates these formulas using rational atanh series with rigorous
remainders; a separate oracle uses the positive Frullani integral

    Elog S−Elog X=∫_0^∞ [R(a+t)/R(a)−R(a+t)²/R(a)²] dt/t.

## 4. A load-bearing golden rank-gluing inequality (FC03)

Use the **inherited**, source-authentic convolution rank sheet
X_(a,r)~μ_(a,r/2), with μ_(a,1)=μ_a, and define

    D_a(r)=Elog(aX_(a,r))−[R(a(1+λ))/R(a)]^(r/2).

The complete fractional rank sheet and its sqrt(241) / Levy factorization
are inherited from `research/2026-10-29/recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md`,
not discovered here. Only integer convolution time1 and2 is needed here; existence of arbitrary
fractional convolution powers is not an additional premise for this theorem.
Put ℓ=R(a(1+λ))/R(a). Strict monotonicity and strict concavity of Q, with Q(0)=0,
give for every k>1 and x>0,

    Q(x)/k < Q(x/k) < Q(x),
    k^−2 < R(ka)/R(a) < k^−1.

At k=1+λ=1/λ, this is λ²<ℓ<λ. Since λ+λ²=1,

    ℓ(1−ℓ)−λ³=(ℓ−λ²)(λ−ℓ)>0.                               (7)

Directly subtract the rank-two and rank-four observables to obtain

    D_a(4)−D_a(2)−[5/6+λ³]
      = [Elog(X+Y)−Elog X−5/6] +(ℓ−λ²)(λ−ℓ).                (8)

Combining (8) with FC02 gives the **strict, all-a, source-derived inequality**

    D_a(4)−D_a(2)
      ≥ 5/6+λ³ +(ℓ−λ²)(λ−ℓ)
        + σ² [R'(a+10)²+R(a+10)R''(a+10)]/[50R(a)²].          (FC03)

At rational a the last two corrections lie in Q(sqrt5); the left log moments
have separately certified enclosures. The limiting rank-two vertex is precisely
D(2)=1−γ−λ²=Ω_OM, and the limiting arrow is
D(4)−D(2)=H_3−H_1+λ²−λ^4=5/6+λ³. This is a place where the author's triangle
participates in an actual inequality on the authentic positive source.

The golden number also has a precise uniqueness role. For an arbitrary mark
η>0 let t=(1+η)^−1; the Gamma rank1 and rank2 Laplace shadows are t,t².
Their quadratic mixing values coincide iff

    t(1−t)=t²(1−t²)  iff  t+t²=1  iff  η=λ.

Thus λ is the unique positive mark balancing these two boundary values.
This is a **declared balancing property**, not proof that the arithmetic
source chooses every observer mark. At η=1/3 and a=1/1000 the analogous
quadratic correction is strictly negative, verified exactly. The golden
complement identity cannot be replaced by an arbitrary mark.

## 5. The first non-product source jet and sharpness (FC04)

Write Q(x)=15x[1+c x+d x²+O(x³)] with c=−59/30,d=27/10. Then

    κ=c²−2d=−σ²=−1379/900.

In scaled coordinates V=aS and U=P, the leading product law is Gamma(4,1)
×Beta(2,2). Up to normalization, its first two relative corrections are

    1+cV/a +[dV²+κV²U(1−U)]/a²+O(a^−3).                    (9)

The first correction depends only on the sum: no sum/proportion interaction
appears at order a^−1. The mixed second correction cannot be absorbed into a
rate shift. Under the product law, E V²=20, Cov(V,V²)=40,
Var(U(1−U))=1/350 and Cov(log U,U(1−U))=1/100. Therefore

    a²(1/5−E B)             → 2σ²/35 =1379/15750,
    a²(Elog S−Elog X−5/6)   → σ²/5   =1379/4500,
    a² Cov(aS,B)            → −4σ²/35=−1379/7875.             (10)

For the first two statements, the explicit rational lower bounds are
asymptotically sharp: R(a)~15/a², R'(a)~−30/a³, R''(a)~90/a⁴, so their scaled
limits are exactly the respective constants in (10).

**Remainder justification.** After scaling x,y by a, expand on
v≤a^(1/6). Finite exponential Q has a Taylor remainder bounded by a constant
multiple of x^4 near zero; h is bounded between exp(−5x) and1. The product
remainder is bounded by a^−3 times a fixed polynomial in v, under the leading
v³ exp(−v) density. On the complement, exponential tails dominate every fixed
polynomial, while log U and log(1−U) are integrable with the Beta u(1−u)
weight. Normalization has a nonzero limit and an ordinary inverse expansion.
This proves the stated expansions for B, V, VB and log U. The finite tests
check them; they do not constitute the universal proof.

**Hostile controls.** The positive two-pole kernel
(225/59)(1−exp(−59x/15)) has the same first two Taylor coefficients as Q, but
its rate variance is3481/2700 rather than1379/900. It shares Gamma rank2,
γ, the limiting golden/Oily triangle and the first rate correction, yet
changes (10). The positive mutant Q+(1−exp(−x))^4 matches through the third
Taylor coefficient and therefore matches (10), while differing at finite a.
This reinforces the inherited finite-jet nonidentification boundary. Its
selected normality is not asserted. The signed front in this round treats
stronger finite-jet/finite-prefix/rational-boundary countermodels separately.

## 5A. The general harmonic/golden triangle: every integer convolution rank (FC07)

The previous two-copy argument extends to a stronger all-rank theorem by a
separate method. For every integer k>=2, take k independent native μ_a draws
and S_k=X_1+...+X_k. Then

    Elog S_k−Elog X_1−[H_(2k−1)−1]
       >= [(k−1)/(2k+1)] σ² a^4/(a+5)^6 >0.                 (12)

For every fixed k, a² times the left side tends to σ²(k−1)/(2k+1).
Thus the rational bound is asymptotically sharp. At k=2 it is another,
simpler positive lower bound for FC02; both bounds remain valid.

**Proof.** Use the exact mixture X_i=G_i/(a+T_i), where G_i are independent
Gamma(2,1) variables and T_i are independent under the native rate law ν_a
whose density relative to τ (the T law in Section2) is proportional to
(a+t)^−2. The G and T families are independent. Put z_i=−log(a+T_i),
bar(z)=k^−1 sum z_i, and

    F(z)=E_G log(sum_i exp(z_i)G_i)−bar(z)−ψ(2).

Because the T_i are identically distributed and Elog G_i=ψ(2),
E_T F(z)=Elog S_k−Elog X_1. The sample-average z subtraction is therefore
the correct mean log input after averaging.
It is a symmetric convex function, invariant under adding a common constant.
Averaging over permutations proves its minimum at equal coordinates, where
F=ψ(2k)−ψ(2)=H_(2k−1)−1. For a quantitative estimate, let d=z−bar(z)1.
The log-sum-exp Hessian is diag(p)−pp^T, with
p_i=exp(z_i)G_i/sum exp(z_j)G_j. Every point on the segment between z and
its average has coordinate range at most log((a+5)/a). Therefore

    p_i >= [a/(a+5)] w_i,  w_i=G_i/sum G_j,
    E w_i w_j=2/[k(2k+1)] for i!=j.

The second identity follows directly from the Dirichlet(2,...,2) density
obtained by the Gamma sum/proportion change of variables. Since sum d_i=0,

    d^T Hess(F) d
       >= [a/(a+5)]² * 2/(2k+1) * sum d_i².

Taylor's integral remainder contributes a factor1/2. Average over the T_i:
E sum d_i²=(k−1) Var_(ν_a)(log(a+T)). The mean value theorem and the independent
pair formula for variance give

    Var_(ν_a)(log(a+T)) >= Var_(ν_a)(T)/(a+5)².

The rate density satisfies dν_a/dτ >= [a/(a+5)]². Minimizing squared distance
to a constant therefore gives Var_(ν_a)(T)>=[a/(a+5)]²σ². Multiplication proves
(12), including its explicit powers. All expectations are finite; the bounded
T support also justifies the differentiated convex function.

For sharpness, ν_a tends to τ, z_i=−log a−T_i/a+O(a^−2) uniformly, and the
expected Hessian at equal coordinates is exactly2/(2k+1) on the zero-sum
subspace. The bounded support gives a uniform third-order remainder for
fixed k. Its expected quadratic form yields σ²(k−1)/(2k+1), as claimed.

**Golden continuation.** For ℓ=R(a(1+λ))/R(a) in(λ²,λ),

    D_a(2k)−D_a(2)−[H_(2k−1)−1+λ²−λ^(2k)]
      =[Elog S_k−ElogX_1−H_(2k−1)+1]
          +ℓ−ℓ^k−λ²+λ^(2k).                               (13)

The second term is strictly positive. Indeed x−x^k is strictly concave on
this interval. Its endpoint difference is

    [λ−λ^k]−[λ²−λ^(2k)] =λ³−λ^k(1−λ^k)>=0,

since λ^k<=λ²<1/2 and x(1−x) is increasing on[0,1/2], with
λ²(1−λ²)=λ³. Equality occurs only at k=2, and interior strict concavity
still gives a positive term there. Combining (12) and (13) proves a strictly
positive finite-source correction to **every** integer-rank arrow from the
original rank-two Oily anchor. This is a source-composition inequality, not
an independence claim for arithmetic times or a selected signed bound.

The exponential-polynomial identity in the next section supplies an exact
finite algorithm: take partial fractions of R(a+t)^k, normalize by R(a)^k,
and evaluate the log moment by finite rational and logarithmic operations.
Fresh rank cases are preregistered separately from the initial two-copy tests.

## 5B. Golden is the sharp uniform-sign mark (FC09)

This refinement was proposed by the root researcher and independently checked
by the constants front. For a mark η>0 put t=1/(1+η) and
ℓ_a=R(a/t)/R(a). Then t²<ℓ_a<t, with ℓ_a→t as a→0 and ℓ_a→t² as a→infinity.
The first limit uses R(a)~4/a; the second uses R(a)~15/a². For every integer
k>=2, let t_k be the unique root in(0,1) of

    sum_(j=k−1)^(2k−2) t_k^j=1.                              (14)

Uniqueness follows from strict monotonicity, value0 at0 and value k at1.
For g_k(x)=x−x^k, the following exact classification holds:

    g_k(ℓ_a)−g_k(t²)>0 for EVERY real a>0  iff  t<=t_k.       (15)

Indeed

    g_k(t)−g_k(t²)
       =t(1−t)[1−sum_(j=k−1)^(2k−2)t^j].                    (16)

If t<=t_k, both endpoint values of the strictly concave g_k are at least
its value at t², so every interior value is strictly greater. If t>t_k,
the a→0 limit of the difference is strictly negative, giving an actual finite
small-a counterexample. This proves necessity, not just sufficient matching.

For k=2, equation(14) is t+t²=1, hence t_2=λ. Section5A proves the inequality
for t=λ at all k; for t<λ each endpoint difference remains positive by
monotonicity of the sum in(16). Consequently

    the Laplace correction is positive for every a>0 AND every k>=2
        iff η>=λ.                                          (17)

Thus the golden value λ is the **sharp minimum mark** for this uniform family
of composition comparisons. This is more than a chosen numerical label;
it is a threshold forced by the declared comparison. It remains a statement
about this positive source and this observable. Necessity uses the continuous
extension down to a→0; no sharp-threshold claim is made when a is restricted
to the native discrete clock8n−7>=1.

Exact rational bisection of(14), fresh below-threshold sign checks and
constructive above-threshold counterexamples are preserved for k2,3,5,8.
These finite probes supplement the proof; they do not define the threshold.

## 6. What γ can and cannot encode in an internal arrow (FC06)

For a finite exponential-polynomial probability density

    f(x)=Σ_j a_j x^(m_j) exp(−b_j x), x>0,
    m_j nonnegative integers, b_j>0, f≥0, ∫f=1,

let w_j=a_j m_j!/b_j^(m_j+1). Coefficients need not individually be positive.
Differentiate Euler's Gamma integral to obtain

    Elog X=−γ+Σ_j w_j[H_(m_j)−log b_j],   Σ_j w_j=1.          (11)

The class is closed under convolution: Laplace transforms are proper rational
functions with negative real poles, and their product has finite partial
fractions of the same exponential-polynomial form. Consequently the shared explicit −γ coefficient cancels in every
normalized log-composition increment. For rational a_j and b_j, its remainder
lies in the rational span of1 and logarithms of positive rationals. Arbitrary
real input rates could themselves encode γ; no independence of unspecified
real constants is being asserted. The
inherited cototient/Pascal normalized-sector theorem is the m_j=0 case;
(11) is an elementary convolution closure extension, not a new classical
Gamma-function identity.

Likewise the authentic four-pole Gamma cocycle has Σc_delta=0. In its
logarithmic derivative Σc_delta ψ(t+delta/8), the common −γ term cancels.
A normalized time ratio removes every time-independent normalization factor.
Higher derivatives retain source-shift information, not a new independent γ
coordinate. The exact finite recurrence R(a) itself is rational at native a.

This does **not** make γ arbitrary: the fully specified normalized Exp(1)
law or the harmonic/log limit fixes it. It says that relative arrows forget
a common additive potential constant unless an absolute anchor is retained.
The Oily vertex supplies such an anchor in the chosen two-observable law;
the new arrow inequality depends on harmonic increments and the golden
complement identity while γ cancels.

## 7. Proof boundary and the next useful discriminator

FC01–FC04 are source-only and hold unchanged if the actual BBP seed is switched
from0 to the coherent seed−π/16. The whole source-composition law, its positive
correlation structure and Ω boundary are identical under that change. Thus
none proves selected signed dispersion. This is an exact typed boundary,
not a counterexample to the authentic zero-seed trajectory.

An actual next coupling must retain an absolute selected phase/carry in the
joint source law and prove a signed lower bound or contraction that fails for
the coherent counterseed. Replacing the deterministic selected phase with a
fresh μ_a draw would erase the obligation. Even the positive rational bound
FC01 is O(a^−2), summable on native time; its mere accumulation cannot yield
a positive-density signed effect.

The user's category intuition receives a precise partial realization here:
composition produces a measurable conditional relation that its common Gamma
boundary snapshot erases. It does not follow that γ or Ω alone encode every
hidden arrow, or that this declared positive carrier is a universal category
of physical realizations. The categorical front separately proves which
observation families can or cannot identify arrows.

## 8. Sources and authority

Classical primary formula references checked2026-10-30:
[NIST DLMF §5.4](https://dlmf.nist.gov/5.4),
[§5.5](https://dlmf.nist.gov/5.5),
[§5.9](https://dlmf.nist.gov/5.9), and
[§5.12](https://dlmf.nist.gov/5.12). The Beta/Gamma calculations are derived
above; no external characterization theorem is needed. No scholarly-priority
audit sufficient to assert novelty has been performed.

Repository provenance is hashed in SOURCE_MANIFEST.json. Inherited foundations:
`research/2026-10-29/triangular_harmonic_gamma_bbp/TRIANGULAR_HARMONIC_GAMMA_BBP.md`,
`research/2026-10-29/oily_triangle_sheet/PASCAL_GOLDEN_HARMONIC.md`,
`research/2026-10-29/cototient_pascal_gamma/COTOTIENT_GAMMA_TRIANGLE.md`,
`research/2026-10-30/gamma_twist/geometry/GEOMETRY_DOSSIER.md`, and
`research/2026-10-30/zero_boundary_dispersion/spectral/SPECTRAL_DOSSIER.md`.
The author-facing packet origin is also preserved in
`research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md`; finite-jet positive counterfeits
already occur in `research/2026-10-25/GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md`.
Source code and archival originals remain unchanged. Same-model review and
separate implementations are not independent external proof authorities.

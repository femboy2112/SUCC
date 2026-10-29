# SUCC Operation Directional Inertia — from epicycles to the authentic source's information arrow

**2026-10-29 · Research only.** Exact baseline: SUCC draft PR #377 at `89bb5edf53b3c421a931a3492e5e59da30728dc7`, child of #376/#374/#372/#370/#369/#367. Read sibling #373 (neutral boundary) and #375 (Farey/Eisenstein) without importing their branches. The **original** signed four-pole forcing, authentic **U_0=0**, archives, main, historical claim registry, and workflows remain unchanged. Base-16 normality of pi, RH, and a physical heat law remain **OPEN**. The results below are paper derivations with standalone exact-rational and independent quadrature checks, not Lean or independent peer review.

## 0. Ptolemy versus Kepler: the mathematical acceptance test

Ptolemaic epicycles and Copernican corrections can encode observations without identifying a minimal governing orbit. Kepler obtained a simpler law (ellipses); in contemporary terminology a Fourier/epicycle representation is not a proof of the generating dynamics. SUCC's positive four-pole kernels, Oily/Pascal/Gamma triangles, and source-typed signed readouts are powerful *representations*. A success toward pi normality must imply a new original-source, zero-prepared **signed long-range estimate**, not just transform that estimate invertibly or show mixing of an auxiliary ensemble.

The strongest exact source-only reduction is already known: the original rational source admits a four-dimensional realization by two quadratic atoms (#367). The integer carry recurrence still depends on the actual selected real-circle path; finite realization of the forcing is not finite-state mixing of its radix orbit.

## 1. Directional law from the unchanged source

Write, for a>0,

    Q(x) = 4 - 2 exp(-3x) - exp(-4x) - exp(-5x) > 0 (x>0)
    R(a) = integral_0^infinity exp(-a x) Q(x) dx
         = 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5)
         = (15a^2+121a+240)/[a(a+3)(a+4)(a+5)]
    mu_a(dx) = exp(-a x) Q(x) dx / R(a).

The actual source time n>=1 corresponds to a_n=8n-7, with R(a_n)=r(n). Define the potential F(a)=log R(a), microscopic mean m(a)=-F'(a), variance V(a)=F''(a)>0 and third cumulant kappa_3(a)=-F'''(a)>0.

For any s>0 the **forward source update** and its exact reverse are

    d mu_(a+s)/d mu_a(x) = exp(-s x) / Z_a(s),
    Z_a(s)=R(a+s)/R(a),
    d mu_a/d mu_(a+s)(x) = exp(s x) Z_a(s).

These operations are inverse changes of measure on this source family. Their normalized potentials obey the causal cocycle `Z_a(s+t)=Z_a(s) Z_(a+s)(t)`. Calling this a *thermodynamic-style information arrow* does not assert physical dissipation without a specified apparatus and heat/work protocol.

### DTI-01: positive and unequal forward/reverse information costs

Define

    D_f(a,s)=KL(mu_(a+s) || mu_a)=log[R(a)/R(a+s)] - s m(a+s),
    D_r(a,s)=KL(mu_a || mu_(a+s))=s m(a) - log[R(a)/R(a+s)].

Then both costs are strictly positive. The symmetric (Jeffreys) information is the **exact rational**

    J(a,s)=D_f+D_r=s[m(a)-m(a+s)]=s integral_a^(a+s) V(t) dt.

Using the source's two interlaced quadratic roots alpha=(121-sqrt241)/30 in (3,4) and beta=(121+sqrt241)/30 in (4,5), its positive cumulants obey, for every integer k>=1,

    (k-1)![a^(-k)+(a+5)^(-k)] < kappa_k(a)
      < (k-1)![a^(-k)+(a+3)^(-k)].

Thus for all a,s>0,

    s^2/[a(a+s)] + s^2/[(a+5)(a+s+5)]
      < J(a,s)
      < s^2/[a(a+s)] + s^2/[(a+3)(a+s+3)].

In particular `J(a,8)=128/a^2+O(a^-3)`; it is a source-derived, parameter-dependent **nonzero** cost, not an assigned scalar.

### DTI-02: the antisymmetric information arrow is governed by the third cumulant

The exact forward/reverse asymmetry is

    A(a,s)=D_r-D_f
          =s[m(a)+m(a+s)]-2 integral_a^(a+s) m(t)dt
          =integral_0^s u(s-u) kappa_3(a+u)du > 0.

This is the trapezoidal-rule curvature identity. It is *strict* because the authentic source has positive third cumulant. It distinguishes directional distinguishability from a symmetric metric or a purely quadratic Gaussian approximation.

All-rational bounds requiring no logarithm are

    (s^3/3)[(a+s)^(-3)+(a+s+5)^(-3)] < A(a,s)
      < (s^3/3)[a^(-3)+(a+3)^(-3)].

At fixed s, `A(a,s)=(2/3)s^3/a^3+O(a^-4)`; with the BBP clock `a=8n-7`, `s=8`, this is `A=2/(3n^3)+O(n^-4)`.

### DTI-03: a finite *total* information resource, with exact value

The one-step symmetric costs telescope **over the genuine entire source clock**:

    sum_(n=1)^(N-1) J(8n-7,8)
       = 8[m(1)-m(8N-7)].

The exact four-pole normalization gives `R(1)=47/15`, `m(1)=6853/5640`. Since `m(a)->0`,

    sum_(n>=1) J(8n-7,8) = 6853/705 nats.

This is the sum of adjacent *symmetric KL divergences*, not KL between the first and final measures. Endpoint KL itself grows logarithmically; KL does not obey a pathwise triangle equality. **Do not mistake the finite stepwise total for finite overall displacement or finite physical work.**

## 2. Gamma/Euler finite part inside the directed information sum

The asymmetry series `A_tot=sum_(n>=1) A(8n-7,8)` converges absolutely and is positive. It has an explicit original-source digamma expression. Put `alpha,beta` as above, `m1=6853/5640` and `C=3008/225`; then

    A_tot = -8m1
      -2[psi(1/8)+psi(1/2)+psi(5/8)+psi(3/4)
          -psi((1+alpha)/8)-psi((1+beta)/8)]
      -2 log C
      = 5.04671393613636148849... nats.

Proof: for each rational or algebraic offset c, sum the terms `1/(8(n-1)+1+c)` using digamma differences `psi(N+t)-psi(t)`. The logarithmic divergences cancel against `log[R(1)/R(N)]`, leaving the displayed finite part. The same source already has the inherited comparison `log[R(1)/R(N)]-2 H_(N-1) -> log C-2 gamma_E`. Thus **Euler--Mascheroni genuinely enters the harmonic-versus-logarithmic regularization of the directed source clock**, but is not an independent additive heat unit. In the digamma basis, `psi(t)+gamma_E` is the corresponding gamma-normalized coordinate.

The total forward and reverse stepwise costs are therefore `(6853/705 - A_tot)/2` and `(6853/705 + A_tot)/2`, respectively, both finite and different. The golden inverse `lambda=(sqrt5-1)/2` does **not** arise uniquely from this directional KL calculation. It remains the marked Oily source's separate PGF fixed-point normalization.

## 3. Preserve the entire q=6 primitive/cototient microstate sheet

Do NOT silently replace the original Oily joint law by PR #372's declared *Pascal* joint law. The two have the same limiting grade marginal but different `J`/Gamma correlations. Here use the original two-geometric Oily packet conditional on `t=e^(-X)`:

    u(t)=t-t^2/2, v(t)=t^2/2,
    g_j(t)=(1-u)(1-v) sum_(k=0)^j u^k v^(j-k).

Mark the arithmetic rank `j+2` and let `chi_6(j)=1[gcd(j,6)=1]`. The four sectors `00,01,10,11` are the pair `(chi_6(j),chi_6(j+2))`. At source parameter a define the authentic positive joint law

    nu_a(dX,j)=mu_a(dX) g_j(exp(-X)).

The conditional grade distribution is unchanged under a->a+s, so `KL(nu_(a+s)||nu_a)=KL(mu_(a+s)||mu_a)` **exactly**. Thus the full source's directional entropy law survives on the source-marked sheet. Merely observing the four arithmetic sector labels, however, loses almost all of that local information.

### DTI-04: exact sector weights and first directional responses

The endpoint weights are the inherited original Oily `w_j=(j+1)/2^(j+2)`. Let `p_E*` be the mass of sector E and `C_E=sum_(j in E)(2-j)w_j`. Their exact values, using residue classes mod 6, are:

| Sector (grade, rank) | p_E* | C_E |
|---|---:|---:|
| 00 | 5/9 | 4/27 |
| 01 | 172/1323 | -4468/27783 |
| 10 | 352/1323 | 4640/27783 |
| 11 | 64/1323 | -4288/27783 |

Every sector is populated, and `sum_E C_E=0`. From the original source `Q(x)=15x+O(x^2)`, `E_mu_a X=2/a+O(a^-2)` and `Var_mu_a X=2/a^2+O(a^-3)`.

Since `g_j(e^(-X))=w_j+(2-j)w_j X+O_j(X^2)` with uniformly summable analytic remainders,

    p_a(E)=p_E* + 2C_E/a + O(a^-2),
    p_(a+8)(E)-p_a(E)=-16 C_E/a^2 + O(a^-3).

The leading source-specific sector response is a genuine connected covariance with the latent field: `p'_a(E)=-Cov_mu_a(p_E(X),X)`.

### DTI-05: the sector labels lose two orders of the directional information

Let P_a be the four-cell distribution. Taylor-expanding its strictly positive finite-dimensional KL gives

    KL(P_(a+8)||P_a)
       = [128/a^4] sum_E C_E^2/p_E* + O(a^-5)
       = (111563264/1042965)/a^4 + O(a^-5).

In contrast the **uncompressed** symmetric source information is

    J(a,8)=128/a^2+O(a^-3).

Their ratio vanishes as O(a^-2), not a positive constant. The exact coefficient `sum_E C_E^2/p_E* = 871588/1042965` was calculated using rational residue sums and independently checked against direct original-four-pole integrals at a=80,160,320,640,1280. This is a bona fide source-specific **information-loss theorem**; it does *not* say that the signed BBP carry contains no information.

### DTI-06: finite total future drift of the complete passive grade field

For any fixed latent coordinate X, the two component geometrical distributions have parameters <=1/2. Differentiating their convolution in X yields an L1 derivative bound <=5: `|du/dX|<=1/4`, `|dv/dX|<=1`, and the L1 parameter derivative of a geometric law is <=4 for parameters <=1/2.

For the full grade marginal `W_a(j)=E_mu_a[g_j(e^(-X))]`, differentiate under the source integral:

    sum_j |W'_a(j)|
       <= 5 Var_mu_a(X) < 10/a^2.

Consequently, at the original step s=8,

    ||W_(a+8)-W_a||_1 < 80/[a(a+8)].

The same holds after coarsening to the four q6 sectors. The entire **future** total source-only grade drift is bounded by the telescoping inequality

    sum_(n=N)^infinity ||W_(a_(n+1))-W_(a_n)||_1 <= 10/a_N,
    a_N=8N-7.

Thus passive Oily/Pascal-like source weighting is asymptotically stationary, even though the selected carry/phase process continues. This bound is source-derived, but by itself cannot force signed phase cancellation.

## 4. Realizing one of sixteen inverse directions costs four **reference** bits

The true circle recurrence for n>=2 (`0<r(n)<1`) is `T_n(x)={16x+r(n)}`. Take Haar on the *hypothetical* predecessor x as a reference; T_n preserves Haar. Given an output y, the inverse branches are

    x_c=(y+c-r(n))/16 in [0,1),
    c=1,...,16 if y<r(n), else c=0,...,15.

Exactly 16 valid branches exist, each with conditional reference probability 1/16, so

    H_Haar(previous-branch | current-phase) = log 16 nats = 4 bits.

For m successive backward steps there are 16^m equiprobable inverse histories given the endpoint, with conditional reference information cost `m log 16`. This is a **legitimate mathematical branch-selection entropy**. It is not evidence for the physical destruction of entropy or Landauer heat: such a claim requires a physical preparation and erasure protocol. An observer cannot infer a preferred absolute chart origin from Haar ignorance. The source-neutral s=0 boundary remains the declared unprepared state of PR #373.

The signed dual of the backward branch average is especially revealing: for integer h,

    (P_n e_h)(y) = 0                              if 16 does not divide h,
                 = e_(h/16)(y-r(n))               if 16 divides h,

where `P_n f(y)=(1/16) sum_c f((y+c-r(n))/16)`. This is **exact source-specific Fourier transport**, but it is an ensemble/transfer operator, not a selected-orbit estimate. Applying P_n to the actual chosen preimage would be the same kind of unjustified ensemble-to-path step that older SUCC controls already exclude.

## 5. The exact missing interaction: source drift versus selected carry

For a fixed integer h!=0 and literal carry class c, define the **marked selected tensor**

    T_(n,E,c,h)= sum_(j>=0) W_(a_n)(j) 1_(j in E)
      * 1_(kappa_(n+j)(0)=c) * exp(2 pi i h U_(n+j)(0)).

This is a deterministic readout of the authentic zero-seeded orbit through the original passive Oily grade field. It is not a probabilistic digit generator. Under n->n+1, the exact discrete Leibniz decomposition is

    T_(n+1)-T_n
      = sum_j (W_(a_(n+1))(j)-W_(a_n)(j)) * mark_(n+1,j)
        + sum_j W_(a_n)(j) * (mark_(n+1,j)-mark_(n,j)).

The **first** term is bounded in absolute value by `80/[a_n(a_n+8)]` and its total absolute future contribution by `10/a_N`. The **second** term retains actual selected signed carry and phase differences. It is the only term in this split that could supply source-specific nontrivial long-range behavior. Neither the entropy arrow nor the Pascal/Γ/Oily triangle currently gives a noncircular estimate on that second term.

This is the precise "Kepler rather than another epicycle" proof target: derive an original-four-pole, neutral-preparation law controlling the second term for the full carry-resolved tensor, strong enough to obtain the fixed-h Weyl bound, or a genuinely weaker, independently provable sufficient criterion. All signed cancellation claims remain OPEN.

## 6. DTI-11: deterministic logarithmic zero runs after exceptional carry 16

The original forcing's exact positive-pole regrouping gives, with a=8n-7,

    r(n)=6/[a(a+3)] + 4/[a(a+4)] + 5/[a(a+5)]
        < 15/[a(a+3)] < 15/(16n^2),   n>=2.

These inequalities use ONLY the genuine original four poles. The last follows from `a=8n-7>4n` and `a+3=8n-4>=4n` for n>=2. The source is strictly decreasing.

For any initial seed s, let `x_n(s)={U_n(s)}` and literal `kappa_n(s)=floor(16 x_(n-1)(s)+r(n))`. If `kappa_n(s)=16`, then

    0<=x_n(s)=16 x_(n-1)(s)+r(n)-16 < r(n).

For every positive integer j for which the following iterates have had only carry zero,

    16^j x_n + sum_(k=1)^j 16^(j-k)r(n+k)
       < r(n)[16^j+(16^j-1)/15]
       < (16/15)16^j r(n) < 16^j/n^2.

Thus induction shows that if `16^j <= n^2`, the next j literal carries are *all zero*. Define the **exact** integer

    L(n) = max{ell>=0:16^ell <= n^2} = floor(log_16(n^2)).

**Theorem DTI-11.** Every carry-16 event at n>=2 is immediately followed by at least `L(n)` consecutive zero carries, for **every seed**. It cannot recur during those zeros. For any `4<=M<=N`,

    #{1<=n<=N:kappa_n=16}
        <= M + floor((N-M)/(L(M)+1)).

Choose `M=floor(sqrt N)` for N>=16. Since `L(M)` grows as a positive constant times log N,

    #{n<=N:kappa_n=16}=O(N/log N),
    lim_(N->infinity) N^-1 #{n<=N:kappa_n=16}=0.

This is an **all-seeds source-authenticated carry-frequency theorem**, improving the inherited PR #377 single-step 16->0 transition constraint. It does not use irrationality, Haar typicality, pi normality, or a normality-equivalent condition. It holds also for some non-BBP sources with the same positive O(n^-2) forcing bound, so it is not a uniqueness characterization of the four poles.

### DTI-12: the exceptional signed q6 carry channel vanishes in Cesaro mean

Let the full source-relative q6 signed tensor be T_(n,E,c,h)(s) as in Section 5, with `c=16`. The grade field `W_a` has

    ||W_a-w||_1 <= 5 E_mu_a X < 10/a,
    w_j=(j+1)/2^(j+2).

For each j and every time window starting at M+j, the forced-zero gap between distinct carry-16 events is >=L(M)+1. Thus for `N>=16`, `M=floor(sqrt N)` and **any** bounded phases, any of the four q6 sector masks and **every** physical seed s,

    (1/N) sum_(n=1)^N |T_(n,E,16,h)(s)|
       <= M/N + 1/[L(M)+1]
          + (10/N) sum_(n=M)^N 1/(8n-7)
       = O(1/log N).

The same bound holds for the absolute value of the averaged signed tensor. This eliminates the extra 17th literal carry class from long-run averages **without marginalizing the ordinary 0..15 bins**. It does not prove mixing or equal frequencies among those sixteen ordinary bins. The coherent same-forcing counterseed already has carry 15 eventually and so passes this bound; the theorem must not be cited as a distinguishing normality result.

Five additional exact-Fraction regression tests verify the source inequality, adversarial rational seeds constructed to *force* a carry-16 event, the entire subsequent compulsory zero run, the event-spacing bound, and the source-weight envelope. These tests corroborate the displayed general induction, not replace it.

## 7. Hostile controls / limits of this round

1. Physical seed `-pi/16` preserves original forcing and **all positive directional entropy costs**, while its selected phases tend to one and all late carries are 15. The new passive entropy law cannot distinguish it.
2. The zero-prepared counter-source family in PR #373 can have a coherent selected orbit despite source-neutrality. Do not infer typicality from retarded response.
3. Haar inverse-branch cost 4 bits occurs for arbitrary forcing, not only the original BBP. It cannot discriminate source authenticity on its own.
4. The q6 gamma-rank shift `j+2` is a **label** in this original Oily joint law. It is not the conditional `Gamma(j+2)` random law proven for a *different, declared Pascal instrument* in PR #372. Their identical grade marginals do not identify their joint distributions.
5. The total symmetric source KL is finite, while the endpoint KL `KL(mu_(8N-7)||mu_1)` grows like `2 log N`; KL is not additive over its intermediate states. Neither quantity is a physical entropy-production budget by fiat.
6. No fixed finite observer resolution (including a source-selected q6 projection) can be promoted into π normality by assuming typicality, and the new directional KL bounds have not yielded a new zero-seeded signed saving.

## 8. Reproducibility and authority

`directional_entropy_probe.py`: 19 independently scoped executable exact-Fraction focused test methods, source-mutation/phase-quotient controls, 16 inverse branches and q6 exact residue moments. `independent_oracle.py`: a separate 58-digit mpmath four-pole quadrature, forward/reverse KL calibration, Gamma/digamma infinite sum evaluation and q6 sector KL high-a holdouts. No full SUCC native suite, hosted exact-head CI, Lean kernel or peer review executed.

Review next: original source fixed, origin selection neutral, q6 four-cell signed tensor fully resolved by **literal** carry 0..16, and source drift separated from actual carry dynamics. Do not merge blindly or promote pi-normality status.

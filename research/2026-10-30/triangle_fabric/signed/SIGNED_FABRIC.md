# The arithmetic arrow hidden from finite positive snapshots

**PROVED LOCAL (paper), with exact finite validation.** Parent405 is
`6cf5050ff2cfd92e7a0c8876da5233be6ff117f5`. The original source is unchanged.
No new fixed-frequency selected Weyl saving, π normality, RH, external referee,
Lean analytic proof, or scholarly priority is claimed.

This front gives an exact classification inside the finite-shift module of
the original BBP source, then constructs positive **zero-seed** nonnormal
controls which preserve any prescribed finite original forcing prefix and
any prescribed finite endpoint jet. Their eventual characters tend to1 at
**every** fixed integer frequency. Thus these are stronger controls than
merely changing the original seed or matching a leading Gamma rank.

## 1. Original source, moment carrier, and the missing arithmetic functional

Keep the original four signed poles

    r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2), n>=1.

Put `Q(x)=4−2e^(−3x)−e^(−4x)−e^(−5x)` and use the coordinate
`z=e^(−8x)`. The positive moment measure is

    w(z) dz = (1/8) z^(−7/8)
              [4−2z^(3/8)−z^(1/2)−z^(5/8)] dz, 0<z<1.

It has full support, finite mass and rational moments

    r(n)=∫_0^1 z^(n−1) w(z) dz.

For a rational polynomial F define `r_F(n)=F(E)r(n)` with forward shift E,
and keep `U_0^F=0`, `U_n^F=16U_(n−1)^F+r_F(n)`. Its selected radix boundary is

    α_F=Σ_(n>=1)16^(1−n)r_F(n)
       =16∫_0^1 F(z)/(16−z) w(z) dz.                    (1)

Absolute convergence follows because F is bounded on [0,1] and r(n)=O(n^-2).
For F=1 the classical BBP identity gives α_1=π. The moment carrier is a
positive source representation; it is not the distribution of selected digits.

### SF-01: complete arithmetic classification of the rational shift module

Divide exactly

    F(z)=a+(16−z)B(z),   a=F(16),   B∈Q[z].

Then

    α_F = aπ + b,     b=16∫B(z)w(z)dz ∈ Q,              (2)
    U_n^F = a U_n + 16^n q_0 − q_n,
    q_n=B(E)r(n+1)=∫z^n B(z)w(z)dz=O(n^-2).            (3)

Proof: polynomial division gives (2); `(16−E)q_n=r_F(n+1)−a r(n+1)`
proves (3) by induction with both initial values zero. Every integral of B
is a finite rational linear combination of moments.

Consequently α_F is rational **iff F(16)=0**, using irrationality of π.
Equivalently r_F is a rational decaying coboundary `16q_(n−1)−q_n`
iff F(16)=0. The reverse implication follows by telescoping a decaying
rational q, whose value q_0 is rational. This statement concerns rational
functions regular at the required indices and tending to0; it does not
assert arbitrary formal or unbounded coboundaries preserve the boundary.

The map `F→F(E)r` is injective: if every moment of Fw vanishes, pairing
against F gives `∫F²w=0`, hence F=0. Therefore the module quotient by the
rational coboundary submodule is exactly

    Q[E]/(E−16) ≅ Q,

with complete quotient coordinate F(16). This is an actual, source-derived
arithmetic invariant. It is not inferred from an appealing category diagram.
The corresponding period modulo Q is `F(16)[π]` in R/Q.

By the classical rational-affine preservation theorem for integer-base
normality, **if F(16)≠0, α_F is base16 normal iff π is**. If F(16)=0,
α_F is rational and not normal. See Doty–Lutz–Nandakumar,
[Finite-State Dimension and Real Arithmetic](https://arxiv.org/abs/cs/0602032),
which proves a stronger result and explicitly recovers Wall's theorem.
This is a classification of *equivalence to the unresolved problem*, not a
proof that any nonzero quotient coordinate produces normality.

## 2. SF-02: positive annihilators matching arbitrary moments and jets

Fix integers N>=0 and M>=1. Let `dν_M=(1−z)^M w(z)dz`. Its moments are exact
rational numbers

    μ_k=Σ_(j=0)^M(−1)^j binom(M,j)r(k+j+1).

Let p_N be the monic degree-N polynomial orthogonal to degrees<N for ν_M.
For N=0 set p_0=1. The Gram matrix is positive definite: a nonzero polynomial
has positive square integral against ν_M. Thus p_N exists uniquely and has
rational coefficients by rational Gaussian elimination.

All N zeros lie simply in (0,1). An elementary proof avoids numerical roots:
if fewer than N sign-changing roots lay there, multiply p_N by the product
of those linear factors. The product has one constant nonzero sign except
at finitely many points, giving a nonzero integral, while the multiplier
has degree<N and orthogonality says zero. Therefore there are N distinct
sign-changing roots in (0,1). This is classical orthogonal-polynomial theory,
consistent with [DLMF §18.2(vi)](https://dlmf.nist.gov/18.2#vi).

Define the rational degree-(N+M) polynomial

    F_(N,M)(z)=1−(z−1)^M p_N(z)/(15^M p_N(16)).          (4)

Then, with ε=15^(−N−M),

    F_(N,M)(16)=0,
    |F_(N,M)(z)−1| <= ε <1     (0<=z<=1).              (5)

Indeed each zero ξ is in (0,1), so `|z−ξ|<=1` and `16−ξ>=15`.
The product bound gives `|p_N(z)/p_N(16)|<=15^-N`; the remaining factor is
at most15^-M. Thus the new source is strictly positive, completely monotone
in its real clock a=8n−7>0, and obeys the **all-index** relative estimate

    (1−ε)r(n) <= r_F(n) <= (1+ε)r(n), n>=1.            (6)

Orthogonality gives the exact initial source prefix

    r_F(n)=r(n), 1<=n<=N,                             (7)

and hence exactly the same zero-seed lifted states and literal carries on
that prefix. The first omitted source value genuinely changes:

    r_F(N+1)−r(N+1)
      =−(−1)^M ||p_N||_(ν_M)^2/[15^M p_N(16)] !=0.     (8)

For (8), `z^N−p_N(z)` has degree<N, so its pairing with p_N vanishes.
There is no silent claim that a finite matched prefix is the full source.

The positive Laplace kernel is `Q_F(x)=Q(x)F(e^(−8x))`. Because
`Q(x)=15x+O(x²)` and `F(z)−1` has a zero of order exactly M at z=1,

    Q_F^(j)(0)=Q^(j)(0), 0<=j<=M,
    Q_F^(M+1)(0) != Q^(M+1)(0).                        (9)

Thus `r_F(n)−r(n)=O(n^(−M−2))`, with the asymptotic source coefficients
through n^(-M-1) identical. This can also be proved directly by integrating
`|Q_F−Q|<=C x^(M+1)` near0 and using exponential suppression away from0.
The constants in this asymptotic may depend on N,M.

### SF-03: exact minimal degree, not just an existence trick

Suppose a polynomial F≠1 satisfies `(z−1)^M | (F−1)` and (7).
Write `F−1=(z−1)^M P`. The moment constraints state that P is orthogonal to
all degrees<N for ν_M. If deg P<N, pairing against P forces P=0, a
contradiction. Therefore **deg F>=N+M**. At equality P is a scalar multiple
of p_N. Imposing F(16)=0 uniquely fixes that scalar and gives (4).

This identifies the precise complexity cost within this polynomial shift
architecture. It does not state a universal lower bound for all source
parametrizations or every possible observation apparatus.

## 3. SF-04: signed rational error and fully coherent dyadic controls

Let α_(N,M)=α_(F_(N,M)). It is rational by SF-01. Polynomial orthogonality
also gives the exact error identity

    π−α_(N,M)
      = 16(−1)^M/[15^M p_N(16)^2]
        ∫_0^1 p_N(z)^2/(16−z) dν_M(z).                (10)

To prove it, use
`[p_N(16)−p_N(z)]/(16−z)`, a degree-(N−1) polynomial, in orthogonality.
Then
`p_N(16)∫p_N/(16−z)dν_M=∫p_N²/(16−z)dν_M`, and substitute (4) in (1).
For N=0 the same identity is immediate. The integral is strictly positive.
Consequently even M gives an approximation below π and odd M one above.

If `L=||p_N||²/[15^M p_N(16)^2]`, the exact rational enclosure is

    L <= |π−α_(N,M)| <= (16/15)L.                     (11)

These are Stieltjes/orthogonal-polynomial rational approximants. Their
positive-square mechanism is **inherited mathematics**, not a newly claimed
general Padé theorem. The new use here is to enforce the rational-annihilator
boundary while keeping a positive matched source.

Choose any positive even M and form the pair at M and M+1. It brackets π
strictly. Choose an explicit dyadic rational d in that rational interval;
searching denominators2^k terminates by density. With

    θ=(d−α_(N,M))/(α_(N,M+1)−α_(N,M)) ∈ Q∩(0,1),
    F_d=(1−θ)F_(N,M)+θF_(N,M+1),                      (12)

we have α_(F_d)=d and F_d(16)=0. Positivity, prefix (7), jets (9) through M,
and the all-index relative bound ε=15^(-N-M) survive convex mixing.
The source remains a finite rational signed-pole sum with a strictly positive
Laplace kernel. It has more than the authentic four poles.

Set `q_n=∫z^n F_d(z)/(16−z) w(z)dz>0`. It is rational and decreasing, and

    U_n^(F_d)=16^(n−1)d−q_n,
    (1−ε)T_n <= q_n <= (1+ε)T_n,
    0<q_n−q_(n+1)<=(1+ε)(T_n−T_(n+1)).                (13)

Here T_n is the **original** Green tail; these comparisons follow directly
from positive integration and (5). When d has denominator2^k,
`16^(n−1)d` is integral for `n>=1+ceil(k/4)`. Therefore for every fixed
integer h,

    e(hU_n^(F_d))=e(−h q_n) -> 1,
    (1/L)Σ_(n=1)^L e(hU_n^(F_d)) -> 1.                (14)

These are zero-seed, positive-source nonnormal controls with no changed seed.
Using inherited `T_n<(8n+1)^−2` and
`T_n−T_(n+1)<=16/(8n+1)^3`, for every A>=1 after that dyadic onset,

    Σ_(n>=A)|e(hU_n^(F_d))−1|
       <= |h|(1+ε)/(8A−7),                           (15)
    Σ_(n>=A)[1−Re e(h(U_(n+1)^(F_d)−U_n^(F_d)))]
       <= (1024/5)h²(1+ε)²/(8A−7)^5.                 (16)

Use `|e(t)−1|<=2π|t|<=8|t|`, `1−cos(2πt)<=32t²`, and bound decreasing
series by the integral beginning at A−1. The early finite prefix is harmless:
the total deviation from the constant character and total lag energy are
finite, so its Weyl deficit is bounded, stronger than merely logarithmic.

Executed examples include N=8,M=6, ε=1/29192926025390625, and

    d=2138057168129933495719360746323741566601 /
      680564733841876926926749214863536422912,

with denominator2^129 and coherent onset n=34. The first8 exact original
forcing values/lifted states/carries and first6 kernel derivatives agree.
The conclusion for all future n follows from (13), not finite observation.

## 4. What survives of the Harmonic/Golden/Euler/Oily triangle?

The author's Harmonic Numbers / Golden Ratio / Euler–Mascheroni triangle and
Oily–Macaroni `Ω_OM=φ^(-1)−γ` retain **Leah / femboy2112** provenance.
All controls in (12) retain the native rank-two scaling `Q_F(x)~15x`.
Consequently the declared time-matched binomial observer has the same limiting
PGF `(2−z)^−2`, golden least fixed point `q=(3−sqrt5)/2=φ^-2`, and
Gamma(2) logarithmic observable `1−γ`. Their difference remains exactly
`1−γ−q=φ^-1−γ`. These are inherited source/observer limit laws.

More strongly, matching (9) preserves any fixed asymptotic expansion depth
of those observers by taking M sufficiently large: the coefficient through
order n^-j depends on kernel coefficients only through x^(j+1).
The existing `gamma_twist/geometry/GEOMETRY_DOSSIER.md` makes the first two
orders explicit. No claim is made that all finite-t Gamma function values or
all derivatives of the continuous Gamma cocycle coincide. The kernel jets,
source asymptotic jets and observer asymptotic jets must stay correctly typed.

The complete continuous real Gamma interpolation for a finite rational
shift filter uses shifted versions of the four original Γ factors, with
rational exponents. Its signed exponent total remains0, so the additive
`−γ` term cancels from the corresponding digamma pole sum. It still changes
as a function when the source changes. Rational exponents can change complex
branch structure; original integer-exponent monodromy is not silently retained.

Thus the constants carry authentic information about normalized source rank
and the declared observer. They **do not identify the selected arithmetic
period class**, which here is controlled by the separate F(16) functional.
The fully original four-pole source still has F=1 and F(16)=1. Our controls
cannot be used as counterexamples to its normality.

## 5. Prior art, independent routes, and the remaining signed obligation

The earlier `research/2026-10-25/GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md` §V
already constructs positive kernel mutants matching finite moments and
endpoint jets and proves a strict resolvent shift with a positive-square
identity. `observational_succ/duck_bbp_fourier.py` already has positive
leading-matched finite-tail rational coboundaries and arbitrary finite-prefix
rational impostors without a positivity guarantee. We explicitly retain
that lineage. The additional combination proved here is:

* positivity + arbitrary prescribed prefix and jets + exact rational and
  dyadic period control under the **zero seed**;
* the sharp minimal filter degree N+M;
* the evaluation-at16 classification and normality equivalence for the
  entire rational finite-shift source module.

Sibling404's first nontrivial radix Ward moments and sibling406's sharp
source-dependent 34th-moment residual were read at their exact heads. They
are seed-averaged and do not separate the original from its coherent changed
seed. Our dyadic mutants show how even retaining U0=0 and a long exact source
prefix still leaves a coherent branch if full source identity is relaxed.
We do not relabel those sibling results as selected cancellation.

The smallest concrete target remains a fixed-h arithmetic exclusion of the
bounded-slip cylinders on full native prime periods, retaining the complete
CRT cofiber and U0=0 (parent405 ZB/SC-06). This round attacks a proposed
finite-positive-geometry route to that target and refutes its sufficiency:
(12)–(16) satisfy the finite geometric information while giving summable
lag energy. A valid proof must use information not shared by these controls,
such as the exact untruncated four-pole source and a genuine selected signed
estimate. Merely recognizing F(16)=1 restores the original π problem.

All pole residues, exact integer carries and 16-state Walsh values on the
matched prefix agree because the exact lifted recurrence agrees there.
Finite agreement does not confer all-horizon equality. No independent random
prime model, positive-source variance, invariant-measure mixing premise, or
unproved normality assertion enters the construction.

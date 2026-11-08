# Quotient crucible: retain the signed signal and calibrate the discarded part

Baseline: `a974db527c19708006b9f6d7f0ca01d08d1e0524`. Status: **PROVED
FINITE/PAPER**, with exact rational checks in `oracle.py`. These are observer
calibrations and precise countermodels, not a proof of original-zero BBP
mixing. No claim of independent scholarly priority is made.

The faithful reading of the proposal is that more local information may help
isolate the part of the complementary response that matters. This survives.
It does not require the isolated response to become smaller. The tests below
identify which signed quantity is retained, which quantity is discarded, and
what a proposed Euler--Mascheroni normalization would have to specify.

## QC1. Which quotient is invariant

On a finite probability space let a,b be complex functions, |a|=|b|=1, and
let P denote averaging on a declared partition F. Define

    z=ab, Z_F=Pz, C_F=(Pa)(Pb), D_F=Pz-(Pa)(Pb).

Then Z_F=C_F+D_F pointwise and

    E z = E C_F + E D_F,
    Cov(a,b)=Cov(Pa,Pb)+E D_F.                         (QC1)

Here covariance is bilinear. These are exact finite identities. Conditional
cross terms vanish cell by cell. The signed mean E z is retained exactly by
Z_F; small E D_F says the conditional product approximates that mean. It
does not say which value the retained mean has.

Under the declared change of factorization

    (a,b) -> (u a, conjugate(u) b), |u|=1,

z and Z_F are invariant. If u is F-measurable, C_F and D_F are invariant
as well, since u can pass through P. For arbitrary point-dependent u they
need not be. On two equally weighted points, take a=b=(1,-1) and the trivial
partition. Then z=(1,1), E D_F=1. Taking u=a gives a'=b'=(1,1), with the
same z and E D'_F=0. Thus the discarded residual is not invariant under all
factorization gauges.

This change is an algebraic observer transport, not permission to replace the
authenticated p-principal part by another arithmetic source. An arithmetic
residual must pin the source decomposition, partition and phase convention.
The pointwise product z is a complete invariant of unit factor pairs under
the full pointwise gauge group: if ab=a'b', take u=a'/a. This classification
explains exactly what information such a quotient discards and what it keeps.

## QC2. Signed refinement increments can have either sign

Let F be coarser than G, and write P_F,P_G for their averages. Put
R_F=E[(a-P_Fa)(b-P_Fb)]. Orthogonality gives

    R_F-R_G=E[(P_Ga-P_Fa)(P_Gb-P_Fb)].                 (QC2)

This is bilinear; it is not a positive conditional variance in general.
Take four equally weighted points,

    a=(1,i,-1,-i), b=(-i,1,i,-1).

For the successive partitions trivial, {0,1}|{2,3}, and singletons,

    E z=0 throughout,   R_F = 0, -1/2, 0,
    E[(P_Fa)(P_Fb)] = 0, 1/2, 0.

Thus even for unit phases the magnitude of the signed discarded part can
first grow and then shrink, while the exact retained product mean is zero.
Reconstruction errors and squared projection norms have their separate
monotonicity statements; no sign monotonicity is transferred to QC2.

## QC3. Exact continuum calibration: the geometric residual

Let x be uniform on [0,1), h a nonzero integer, M a positive integer, and P_M
average on the M equal half-open intervals. Write sinc(t)=sin(t)/t, sinc(0)=1.
For a(x)=e(hx), b(x)=e(theta) conjugate(a(x)), elementary integration gives

    (P_M a)(x)=e(h(j+1/2)/M) sinc(pi h/M)  on cell j.

Consequently

    E z = e(theta),
    E[(P_M a)(P_M b)] = e(theta) sinc(pi h/M)^2,
    R_M=e(theta)[1-sinc(pi h/M)^2],
    M^2 R_M -> e(theta) pi^2 h^2/3.                    (QC3)

The last limit follows from sin t=t-t^3/6+O(t^5). The exact formula also
covers h divisible by M. For 0<|pi h/M|<=1, the alternating cosine series
applied to sinc(t)^2=(1-cos(2t))/(2t^2) proves

    0 <= pi^2 h^2/3 - M^2 e(-theta) R_M
      <= 2 pi^4 h^4/(45 M^2).                         (QC4)

Thus a tiny discarded residual can be entirely geometric, while the retained
signal has arbitrary unit phase. The source is uniform continuum sampling
with a deliberately coherent complement; it is not the BBP complement.
Equation QC3 rules out a *universal* Euler-constant coefficient for this
particular scaled residual over all complementary phases. It does not refute
an as-yet-unspecified original-zero gamma identity. No transcendence or
algebraic-independence assertion is needed or made.

## QC4. A high-frequency alias saturates the first-order residual bound

Keep the preceding a and P_M, with fixed integer h>=1 and M>h, but take

    b_M(x)=e((M-h)x),   z_M(x)=e(Mx).

The full signed mean is exactly zero. Multiplying the two cell means and
summing the cell phases gives

    E[(P_M a)(P_M b_M)]
      =-sinc(pi h/M) sinc(pi(1-h/M)),
    R_M=sinc(pi h/M) sinc(pi(1-h/M))>0,
    M R_M = h/(1-h/M) sinc(pi h/M)^2 -> h.              (QC5)

The minus sign comes from e((M)(j+1/2)/M)=-1. Therefore the general O(1/M)
conditional covariance error from CH7 is sharp when the complementary
phase varies with resolution. One cannot replace it by O(1/M^2) uniformly
over all bounded complementary phases. For |pi h/M|<=1, the explicit bound

    |M R_M-h| <= h^2/(M-h)
                  + [h/(1-h/M)] pi^2 h^2/(3 M^2)      (QC6)

follows from 0<=1-sinc(t)^2<=t^2/3. For a fixed integer k with M not dividing
k, replacing b_M by e((k-h)x) instead gives E z=0 and R_M=0, by the geometric
sum of e(kj/M). The resonant frequency is part of the instrument specification.

## QC5. Gamma source invariants and literal source selection

The existing source primitive

    G(x)=Gamma(x+1/8)^4 /
         [Gamma(x+1/2)^2 Gamma(x+5/8) Gamma(x+3/4)]

and its successor ratio depend on the four forcing coefficients and poles.
They do not depend on the initial seed of U_n(s). This is immediate from
their definitions; `observational_succ/bbp_gamma_boundary.py` already records
the balanced digamma cancellation and a surviving (15/8) gamma coefficient
in a specific primitive-boundary normalization.

The same-forcing coherent seed s=-pi/16 has U_n(s)=-T_n, hence e(hU_n(s))->1
for every fixed h. It shares G and all forcing-only gamma invariants with
the authentic zero seed. It fails the zero-boundary hypothesis. This is an
exact falsifier only for an attempted implication that drops that boundary.
The earlier finite rational shadow theorem supplies p-local-compatible
finite controls; an irrational seed is not silently assigned a rational
p-principal part here.

A useful gamma proposal must therefore specify a source-selected signed
observable, a normalization, a limit order and a theorem connecting its
gamma coefficient to E z or to the original signed lag gate. A forcing-only
constant cannot by itself make this selection. The proposal remains **OPEN**
until that source-dependent bridge is proved, rather than being declared
false merely because an earlier normalization cancels gamma.

## Provenance and verdict

QC1--2 are classical conditional-average algebra, written out here. QC3--4
are elementary exact Fourier calibrations derived here from cell integrals,
not numerical pattern fits. Their new-to-this-round contribution is a paired
test separating quadratic geometric remainders from first-order aliases.
QC5 inherits the source-specific Gamma primitive and Green identity already
present at the pinned baseline. The independent oracle uses Gaussian-rational
finite algebra and separate Machin/Taylor rational enclosures; no Gamma,
Euler-constant, mpmath or phase-engine values are construction inputs.

The constructive verdict is **SURVIVES as an information-preserving quotient**:
local learning can expose the retained complementary signal more accurately.
The arithmetic verdict remains **OPEN**: its original-zero signed mean still
needs a source-derived estimate. The next discriminator is to report the
retained signal and discarded residual separately under a fixed partition,
then compare their resolution scaling and coherent/alias controls before
fitting any universal constant.

**Pi base-16 normality: OPEN. RH: OPEN.**

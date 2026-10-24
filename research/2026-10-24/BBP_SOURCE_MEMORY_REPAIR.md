# BBP source fidelity repair: signed pole moments, positive Green memory, and the selected π orbit

**Research date:** 2026-10-24. **Direct parent:** DeepSeek draft PR #251
at de257fad8966bbe02ecdd19c2c0e9f68cee77e15, which itself sits on
the CI-validated but unmerged Academic Main IX candidate PR #250.
**Status:** mathematical paper proofs and exact Fraction witnesses (hosted
workflow status tracked independently). **π normality in any base: OPEN.
No RH, Weil sign, empirical physics, or academic originality claimed.**

This dossier repairs the invalid "BBP four-pole lane closed" assertion
*without* throwing away the valid partial fractions, non-coboundary
obstruction, exact tail estimates, or useful proof-mechanism tooling.

## SFR-BBP-01 — Forcing-index poles are not circle states

Let b=16, n>=1, and define the true positive rational BBP forcing:

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)
        =sum_(i=1)^4 rho_i/(n-a_i),

    (a_i,rho_i)=(7/8,1/2),(1/2,-1/4),
                (3/8,-1/8),(1/4,-1/8).

The a_i are **poles in the complex variable n**. They are NOT the
points of the orbit under T_16:x -> 16x mod 1.

It is true that every 16a_i=0 mod 1 and sum rho_i=0.
Thus the artificial signed measure sigma=sum rho_i delta_(a_i mod1)
has pushforward (T_16)_*sigma=0. But its Stieltjes readout is

    S_n(sigma)=int (n-a)^-1 d sigma(a)=r(n),

which is nonzero (r(1)=47/15). The pushforward did not intertwine this
readout with any authenticated BBP source map. Erasing sigma in the
circle quotient cannot erase the original rational forcing.

**Correct conclusion:** the circle pushforward is a NON-FAITHFUL
observation of the forcing-index pole object. No dynamical
annihilation of BBP forcing or of π digit correlations follows.

## SFR-BBP-02 — Pole moments produce the BBP asymptotic coefficients

Set m_k=sum_i rho_i a_i^k. For |n|>7/8:

    r(n)=sum_(k=0)^infinity m_k/n^(k+1).

Exact source calculations give

    m_0=0,
    m_1=15/64,
    m_2=151/512,
    m_3=1209/4096,
    m_4=8995/32768.

Therefore r(n)=15/(64n²)+151/(512n³)+1209/(4096n⁴)+...
with full asymptotic meaning. The 1/n cancellation comes from
m_0=0; the first surviving 1/n² coefficient comes from the signed
**first pole moment** m_1. The earlier report's statement that the
residues are "invisible to the tail coefficient" is FALSE.

The leading tail coefficient follows from the geometric Green kernel:

    t_n=sum_(k>=1)16^-k r(n+k)
       ~ m_1/(15n²)=1/(64n²).

The pole data determine m_1; their further moments determine the
subleading asymptotics. "Tail leading term only sees the collapsed
rational function" is formally true but supplies NO independence of
the pole residues: that rational function is the same pole data.

## SFR-BBP-03 — The signed four-pole source reconstructs a POSITIVE kernel

For n>=1 use 1/(n-a)=int_0^1 u^(n-a-1) du, or substitute u=t^8.
The resulting exact elementary identity is

    r(n)=int_0^1 t^(8(n-1)) g(t) dt,

where

    g(t)=4-2t³-t⁴-t⁵
        =2(1-t³)+(1-t⁴)+(1-t⁵).

In particular g(t)>0 on 0<=t<1, g(1)=0, with no source positivity
assumption imported from the sign-indefinite residues.

By nonnegative geometric summation (Tonelli or dominated convergence):

    t_n=sum_(k>=1)16^-k r(n+k)
       =int_0^1 [t^(8n) g(t)/(16-t^8)] dt,  n>=0.   (G)

Let u=t^8 and define the finite positive Borel measure on [0,1]
whose density on 0<u<1 is

    w(u)=g(u^(1/8)) / [8 u^(7/8)(16-u)] > 0.

Then

    t_n=int_0^1 u^n w(u)du,

and, for all n,k>=0, the forward finite difference satisfies

    (-1)^k Delta^k t_n
         =int_0^1 u^n(1-u)^k w(u)du > 0.          (H)

Thus the AUTHENTIC BBP backward-tail sequence is a **strict
Hausdorff moment sequence**. Every t_n>0, t_(n+1)<t_n, every finite
difference alternates strictly in sign, and all Hankel principal
minors are positive. These conclusions come from the actual signed
four-pole source, not a circle Haar assumption.

Hankel proof: for any nonzero c=(c_0,...,c_m),

    sum_(i,j=0)^m c_i c_j t_(i+j)
       =int_0^1 |sum_(j=0)^m c_j u^j|²w(u)du >0.

Every size-m Hankel Gram matrix is positive definite. The strict
all-size rank excludes EVERY fixed finite-dimensional
time-homogeneous linear realization t_n=v* A^n w: its Hankel rank
would be <= dimension(A). This is a source-memory theorem, NOT a
claim about arbitrary nonlinear / time-dependent finite encodings.

A further exact result is the generating function identity for |z|<1:

    T(z):=sum_(n>=0) t_n z^n
         =int_0^1 w(u)/(1-zu)du.

It is a classical positive Hausdorff/Stieltjes generating function.
Because the representing measure is positive on a continuum of
u-values, T(z) is not rational: a rational coefficient generating
function would yield a finite Hankel rank. This is another
source-authenticated distinction between the arithmetic memory
carrier and a finite periodic clock.

**Finite quantitative receipt:** a geometric two-term tail enclosure
from exact forcing values gives

    det [[t_0,t_1],[t_1,t_2]] > 1/2200

without using π digits, floating point, or an unevaluated integral.

These are classical moment-method consequences, with a
new-to-this-SUCC-project source-specific realization. Scholarly
priority UNVERIFIED. A positive Hausdorff Gram is not the completed
signed Weil form.

## SFR-BBP-04 — Unique bounded backward tail and authenticated forward state

The exact backward Green recurrence is

    16t_n=r(n+1)+t_(n+1),  n>=0.                    (B)

Two bounded solutions of (B) differ by C*16^n and therefore
coincide. The positive integral (G) constructs that unique bounded
solution and shows t_n->0.

By the source-identified BBP integral, t_0=π/16. Let

    y_0=0,
    y_(n+1)={16y_n+r(n+1)}.

Write x_n={y_(n+1)+t_(n+1)}. Then by induction and (B),

    x_n={16^(n+1)t_0}={16^n π}.                    (S)

Changing y_0 to s while keeping the same forcing selects the
DIFFERENT circle initial phase {s+t_0}; the original choice s=0
is load-bearing.

At n=1, the exact source exposes the false DeepSeek alias:

    y_1(y_0=0)=2/15,
    y_1(y_0=1/3)=7/15.

The unforced fixed T_16 orbit 1/3,1/3,... is not the y-orbit
generated by the authentic BBP forcing and y_0=0. A countermodel
that preserves only the forcing *formula*, but not its authenticated
initial condition/selected tail, is NOT a countermodel to that
complete source.

This repairs the source domain, without claiming that the correctly
selected trajectory has normal digits.

## SFR-BBP-05 — Four fixed-pole readouts certify all four residues

With the pole locations a_i in SFR-BBP-01 FIXED and separately
authenticated, the forcing readouts n=1,2,3,4 give the Cauchy matrix

    C_(n,i)=1/(n-a_i).

Its exact determinant is

    det C=8388608/1224171073125 != 0.

This is a special case of the classical Cauchy determinant formula.
Therefore the four source readouts uniquely determine all four
signed residue weights within this declared fixed-pole family.

For the authentic forcing the readouts are precisely

    r(1)=47/15,
    r(2)=106/819,
    r(3)=829/19635,
    r(4)=316/15225.

The independent exact Gaussian solver recovers
(1/2,-1/4,-1/8,-1/8). The tests reject a perturbed source.
This does NOT identify arbitrary unknown poles, a physical device,
or all infinite arithmetic source properties from four numbers.

## SFR-BBP-06 — Explicit complete-monotonicity counterfeit

None of strict Hausdorff complete monotonicity, positive
all-order Hankel Grams, rational O(n^-2) forcing, and exact
bounded backward-tail conjugacy proves normality.

Indeed let

    t_n^fake=1/((n+1)(n+2))
            =int_0^1 u^n(1-u)du.

It has strict Hausdorff positivity and infinite Hankel rank. Put

    r_fake(n)=16t_(n-1)^fake -t_n^fake
             =16/(n(n+1))-1/((n+1)(n+2))>0.

Then r_fake(n)=O(n^-2) and the exact same Green/forward identity
holds, but the authenticated initial t_0^fake=1/2 is rational.
Its T_16 circle orbit is fixed at zero after one shift and is
nonnormal. This is a hostile control on overly broad conclusions,
not a countermodel sharing the specific BBP g(t) source.

## SFR-BBP-07 — False min-plus prime-cost upper estimate

The #251 dossier confuses a prime-word ABSOLUTE path cost with the
signed difference of the endpoint cosine coefficients.

Let the source be the actual probability δ_(1/8), with
c_n=cos(πn/4). For odd n, c_n=±sqrt(2)/2.

Define d_1=0 and
d_n=min_(p genuine prime|n)[d_(n/p)+|c_n-c_(n/p)|].

Exact path enumeration for 15=3*5 and 255=3*5*17 gives

    d_15=2sqrt(2), d_255=2sqrt(2).

At R=3, h=1, b=16, N=1, the proposed universal estimate

    (2/R²)*sum_(d=1)^(R-1)(R-d)*d_(16^d-1)
       <=2(R-1)/R

reads

    4sqrt(2)/3 <= 4/3, which is FALSE.

This is a precise REAL circle probability source, not a
fabricated moment vector. Notably c_15=c_1 despite d_15>0:
the individual absolute prime-edge costs fail to recognize exact
ENDPOINT cancellation.

The valid general bound is instead d_n<=2 Omega(n),
where Omega counts prime factors with multiplicity.
No uniform O(1) carry-sum bound or o(1) follows from this alone.
Preserve complex signed van der Corput lag correlations as the
AUTHENTIC target quantity; prime-graph transport is only an
optional lossy majorant with an explicit information-loss cost.

## SFR-BBP-08 — Other corrected proof-authority claims

1. "Nonzero rational pole coboundary invariant" excludes that
   particular rational telescoping solution class; it proves no
   Fourier cancellation or no-go for all BBP methods.
2. A special periodic rational T_16 orbit such as 1/3 is a
   negative control for GENERIC circle-geometry implications,
   not the full BBP-selected source.
3. If a family of finite-N fits shows growth in R at frozen N,
   it does NOT numerically refute an N->infinity estimate along
   a jointly admissible R_N: order of limits matters.
4. Exact chord/Fejér identities are re-encodings of Fourier
   energies. They can become useful if the geometric side
   gains an independently proved source-bound; their algebraic
   equivalence is not a theorem of impossibility.
5. Proof-mechanism strings/Booleans are self-reported claims,
   not a runtime proof of source membership, faithfulness or
   theorem equivalence. Bisection locates a finite dyadic
   bracket, not an algebraically exact unknown threshold.
6. A generic theorem can help prove a SPECIAL source theorem
   if a source-specific hypothesis is independently discharged.
7. Existing CYC-01' sparse lag inequality remains valid with
   its declared assumptions; #251's false cost ceiling
   should not be imported into its premise.

## New main-line mathematical questions (not solved)

The authentic Green/Hausdorff model supplies a canonical
nonnegative density w on u∈[0,1] and a spectral multiplication
operator U f(u)=u f(u), with
t_n=<1,U^n 1>_(L²(w)). In contrast, the phase-selected orbit
x_n={16^(n+1)t_0} is expanding and nonlinear modulo one.

The verified identity selects π:
    16 int_0^1 w(u)du=π.

**Missing:** a genuinely π-source-specific estimate connecting
that *particular integral of the authenticated density* to
cancellation of the signed lag correlations

    C_d(N;π)=sum_(j=0)^(N-1-d)
       exp(2π i h (16^d-1)16^j π),

uniformly in the declared double limit. Moment positivity,
Hankel rank, Fourier rewriting, and weak source approximations
do not supply it.

Proposed research priorities:
- Derive a nontrivial exact transfer between the Green spectral
  function and one family of signed cyclotomic lag correlations.
- Test its premise against the rational positive-Hankel counterfeit
  and the 3-adic periodic countermodels.
- Search for π-specific nonresonance/cancellation results using
  the exact g(t), not arbitrary positive moment measures.
- Avoid assuming endpoint phase cancellation as the premise.
- Seek a genuine new source-specific theorem even if weaker
  than full normality (e.g., a nontrivial all-horizon π
  exponential-sum bound for one fixed h).

**Bottom line:** The pole source has a strict infinite-dimensional
positive Green-memory carrier. Its selected real phase is π.
The representation error is not that the source has no recurrence;
it is that the forward nonlinear digit dynamics has not been
shown statistically generic for that one selected source.


## SFR-BBP-09 — Independent all-n rational bounds from the kernel's endpoint

The positive polynomial g(t) factors as

    g(t)=(1-t)H(t),
    H(t)=4+4t+4t²+2t³+t⁴.

The multiplier h(t)=H(t)/(16-t^8) satisfies 1/4<h(t)<1 for
all 0<t<1; its limit at 1 is exactly h(1)=15/15=1.
Write

    B_n=int_0^1 t^(8n)(1-t)dt
       =1/[(8n+1)(8n+2)].

Then for every integer n>=0, strict source-derived bounds give

    B_n/4 < t_n < B_n.                                 (I)

For an explicit *asymptotically sharp* error, note
    1-h(t)=[15-H(t)]+[1-t^8] over (16-t^8).
Since H has nonnegative coefficients and H'(1)=22,
    0 <=15-H(t)<=22(1-t)
and 0<=1-t^8<=8(1-t), so
    0<=1-h(t)<=2(1-t).
Therefore

    0 < B_n-t_n
      <=2 int_0^1 t^(8n)(1-t)^2 dt
      =4/[(8n+1)(8n+2)(8n+3)].                        (J)

The two rational brackets (I),(J) are all-n inequalities,
not digit fits. They imply immediately

    n² t_n -> 1/64.

This is a SECOND independent proof of the source's 1/64
tail coefficient: the earlier signed pole moment m1=15/64
recovers it algebraically, while here the endpoint slope of
the actual positive kernel produces it geometrically.
Both source descriptions commute at the level of asymptotic
moments; neither implies signed Fourier cancellation under
the forward digit map. Strict rational finite checks
compare the bounds against source-only BBP tail enclosures.

Code: source_tail_beta_bracket / source_tail_sharp_beta_bracket
in observational_succ/bbp_source_memory.py.

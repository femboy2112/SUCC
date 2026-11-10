# Integer clocks, Fibonacci returns, and a circle that can be learned

**Status: PROVED PAPER, finite exact oracle, numerical golden-circle holdouts.**
This is an observer/geometry theorem. Original-zero signed covariance decay,
pi base-16 normality and RH remain **OPEN**. The mathematics is elementary
circle geometry, continued-fraction algebra and perturbation analysis; no
worldwide novelty is claimed.

## FG1. Carrier and the two clocks

The calibration carrier is

    C_j = c + g e(j alpha),   j=0,1,2,...,
    e(t)=exp(2 pi i t),       c in C, g in C\{0}.

Its clock is integer j; c and g are initially unknown. Oriented complex
readings use one fixed Euclidean coordinate frame. Translation and rotation
of that frame are allowed, but each reading cannot choose an independent
frame. The radius is R=|g|, and C_0=c+g is the retained phase-zero anchor.
The available probe is a coordinate reading at a declared integer clock time.

The main case is alpha=(sqrt(5)-1)/2. One may declare this actuator increment
as part of the instrument specification, or infer its value from arbitrarily
long authenticated continued-fraction brackets. Finite Fibonacci return
information alone does not certify that an unknown rotation is exactly
alpha. It supplies a finite interval unless an additional source assumption
selects the golden actuator.

The **source clock n is different**. A calibrated source readout has the form

    Y_n=c+g e(U_n),
    U_0=0, U_n=16U_(n-1)+r(n),
    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).

The calibration intervention rotates the probe/reference, or a stored source
sample, by alpha; it does not replace the BBP evolution by a golden rotation.
To use the same calibration for Y_n, the gain, center, orientation and anchor
must stay fixed, or their changes must have an authenticated transport law.
The original rational lifts, integer carries, chronology and source signature
remain separate authenticated data. Recovering e(U_n) alone cannot recover
all of these unwrapped data.

Finite candidate families use the existing SUCC `FiniteCarrier`, `Instrument`,
`BeliefGame` and `ObservationPathCategory`: readings append to the transcript;
belief is the subset of declared candidates consistent with it. Prefix
inclusions forget only later readings. No new category is introduced.
Continuum-identification statements below are ideal exact analytic statements,
not claims that a finite alphabet identifies an arbitrary real parameter.

## FG2. Exact Fibonacci returns and lawful resolution transport

Let F_0=0,F_1=1,F_(k+1)=F_k+F_(k-1). For every k>=1,

    delta_k = F_k alpha-F_(k-1) = (-1)^(k-1) alpha^k.       (FG1)

For k>=2, delta_k lies strictly between -1/2 and 1/2, so it is the signed
principal return. Put q_k=F_k and rho_k=e(delta_k)=e(q_k alpha). Then

    delta_(k+1)=-alpha delta_k=delta_k+delta_(k-1),
    rho_(k+1)=rho_k rho_(k-1).                            (FG2)

These are exact transport laws, not arbitrary cross-resolution phase fits.
They retain the alternating return orientation. Proof: the base k=1,2 is
alpha and alpha-1=-alpha²; multiplication by -alpha and the relation
alpha²=1-alpha verify both recurrences.

The adjacent convergents F_(k-1)/F_k and F_k/F_(k+1) bracket alpha for
k>=2. Their separation is 1/(F_k F_(k+1)), by the determinant identity
F_(k-1)F_(k+1)-F_k²=(-1)^k. Their nested intersection is the singleton
alpha because F_k tends to infinity. A finite transcript that certifies
only these brackets retains the whole finite interval.

For q=q_k, a causal observer reads C_0,C_q,C_(2q), finishing at integer
clock 2q. The second difference is centered at clock q; its phase is
transported back to the original anchor by rho_k^(-1). No future reading
is reported before it occurs.

## FG3. Three oriented readings recover the circle and its open phase

More generally, assume P_j=c+g rho^j for j=0,1,2, where |rho|=1 and
rho!=1. Write d=P_1-P_0 and w=P_2-2P_1+P_0. Then d,w are nonzero and

    rho = (P_2-P_1)/(P_1-P_0),
    g = d²/w,          c=P_0-d²/w,
    R=|d|²/|w|,       curvature 1/R=|w|/|d|².            (FG3)

Here the square d² is complex multiplication. Proof: d=g(rho-1) and
w=g(rho-1)². These equations prove every displayed identity directly.
They require neither a numerical value of pi nor a prior radius estimate.
The resulting geometry is measured in the coordinate instrument's units.
The assumption that the carrier is a fixed circle remains explicit.

Any additional reading Y=c+g z determines the anchored complex phase
z=(Y-c)/g exactly. Thus g retains orientation and phase zero as well as
radius. If z=e(U_n), the original source character is recovered. This
reconstructs the projected character; the unwrapped source history still
requires its authenticated source ledger.

For any fixed complex u!=0 and v, replacing P by uP+v gives
(c,g,rho)->(uc+v,ug,rho). The recovered z is unchanged; curvature scales
by 1/|u|. Reflection P->conjugate(P) conjugates rho and z. Consequently
coordinate transport is natural under similarities, while orientation is
not determined by distances alone. The explicit pair rho and conjugate(rho)
has all identical pairwise chord lengths and opposite signed return phases.

An integer clock itinerary without coordinate readings has the same output
for every (c,g), including radii1 and2. It cannot determine curvature.
A complete return-phase itinerary without an anchored gain has the same
output after multiplying every g by any unit phase, so it cannot determine
the source's absolute Fourier phase. These are distinct, demonstrated
identifiability failures, not obstructions to the oriented three-point model.

## FG4. Curvature and phase agree across resolutions

For q=q_k and the triple C_0,C_q,C_(2q), write w_k=C_(2q)-2C_q+C_0 and
t_k=|rho_k-1|=2 sin(pi |delta_k|). Then

    rho_k^(-1) w_k / t_k² = -g                           (FG4)

at every k>=2. This is exact curvature-vector transport to the common
zero anchor. A magnitude-only quotient retains R but loses the direction
of g. A closed ratio w_k/d_k removes g altogether, so recovering the
source phase requires keeping the open anchor from FG3.

If the observer uses the small-return normalization instead, define

    D_k = rho_k^(-1) w_k/delta_k²
        = -4pi² sinc²(pi delta_k) g,
    sinc(x)=sin(x)/x, sinc(0)=1.

Then for every k>=2,

    |D_k+4pi²g| <= (4pi⁴/3) R alpha^(2k).                (FG5)

The two-resolution correction

    J_k = [D_(k+1)-alpha² D_k]/(1-alpha²)

satisfies

    |J_k+4pi²g|
      <= (8pi⁶/45) R alpha^(4k)
          * alpha²(1+alpha²)/(1-alpha²).                 (FG6)

Proof: the triangular Fourier representation
`sinc²(x)=integral_(-1)^1 (1-|t|)cos(2xt)dt` and the global cosine remainder
bounds give

    0<=1-sinc²(x)<=x²/3,
    |sinc²(x)-1+x²/3|<=2x⁴/45.

Use delta_(k+1)²=alpha²delta_k² to cancel the quadratic term; bound the
two remaining quartic remainders. FG4 is exact and preferable when the
return chord is calibrated. FG5–6 quantify what is lost by replacing
that chord calibration with a small-angle approximation.

## FG5. Fine returns cost precision: explicit perturbation bounds

Suppose each of P_0,P_1,P_2 and an additional Y=c+gz, |z|=1, is measured
with complex absolute error at most epsilon. Form d~,w~,g~=d~²/w~,
c~=P~_0-g~, and z~=(Y~-c~)/g~. Let

    t=|rho-1| in (0,2],    u=epsilon/(R t²).

Assume u<=1/64. Then all denominators are nonzero and

    |g~-g| <=14 epsilon/t²,
    |c~-c| <=18 epsilon/t²,
    ||g~|-R|/R <=14u,
    |1/|g~|-1/R| <=18u/R,
    |z~-z| <=48u.                                       (FG7)

After radial normalization zhat=z~/|z~|, which is valid since48u<1,

    |zhat-z|<=96u,
    |zhat^h-z^h|<=96|h|u  for every integer h.            (FG8)

Negative powers in FG8 use unit phases. Thus mean Fourier characters
are recovered with the same uniform error, with no statistical assumption.
The bound applies to any source phase sequence, including coherent wrong
seeds; it is an instrument calibration bound, not signed cancellation.

**Proof and constants.** The errors in d,w are at most2epsilon,4epsilon;
|d|=Rt and |w|=Rt². Hence

    |g~-g|/R <= B :=4u(1+t+u t²)/(1-4u) <=14u.

The last inequality follows from t<=2,u<=1/64. Then |g~|>=R(1-B),
|c~-c|<=epsilon+RB<=18epsilon/t², and the relative reciprocal-radius
error is at most B/(1-B)<=18u. Direct division gives

    |z~-z| <=[2epsilon/R+2B]/(1-B)
             <=36u/(1-14u)<=48u.

Radial normalization changes a point at distance E from a unit phase by
at most2E in total; telescoping integer powers proves FG8.

The measured chord ratio rho~=(P~_2-P~_1)/(P~_1-P~_0) has error

    |rho~-rho| <=4epsilon/(Rt-2epsilon).

Normalizing rho~ to unit modulus and lifting its angle to (-1/2,1/2)
gives a turn error at most `2epsilon/(Rt-2epsilon)` for k>=2. Indeed the
circle chord inequality `|e(x)-e(y)|>=4 dist_T(x,y)` and normalization
bound give this estimate; it is at most1/15. Since |delta_k|<2/5, there is
no principal-branch crossing. With the authenticated winding F_(k-1),

    alpha_hat=(F_(k-1)+delta_hat)/F_k

therefore differs from alpha by at most
`2epsilon/[F_k(Rt-2epsilon)]`. Integer winding is retained as history;
forgetting it leaves alpha only modulo1/F_k.

For golden returns, `4alpha^k<=t_k<=2pi alpha^k`, using
`sin(pi x)>=2x` for0<=x<=1/2. Thus maintaining a fixed small u requires
absolute coordinate precision on the scale R alpha^(2k). This is the proved sufficient precision budget for this **blind three-point**
procedure, not a universal lower bound for every instrument. If the actuator
phase rho is already known exactly, two readings recover
`g=(P_1-P_0)/(rho-1)` with gain error at most `2epsilon/t`, a better budget.
Historical phase calibration can therefore remove one power of the small
return from later gain estimation. Neither model promises arbitrary fine
geometry at fixed precision. If error is held fixed while k grows, FG7 eventually
has no applicable hypothesis.

## FG6. Target truth, history, and the covariance boundary

For a declared finite family of triples, the transcript map sends a
candidate (c,g,rho) to (P_0,P_1,P_2). FG3 proves injectivity on its model
domain. Every target proposition about that triple therefore descends to
its full transcript fibers. Prefix fibers can be larger, and physical
projection can erase candidate identity after the third observation.
The existing SUCC belief update retains source IDs; a stored transcript
continues to distinguish candidates after that physical collapse.

The exact finite adapter tests candidates with the **same** P_0=0 and
P_1=1 but different P_2=1+rho. Its passive read sequence takes exactly
three readings to decide rho, after which the carrier is sent to a common
terminal state. Reading the terminal state alone cannot decide rho;
the recorded third observation can. This is ordinary historical memory,
not physical nonlocality.

For source phases a_n,b_n, |a_n|=|b_n|=1, independently recovered unit
phases with uniform errors eta_a,eta_b satisfy

    |Cov(ahat,bhat)-Cov(a,b)| <=2(eta_a+eta_b),            (FG9)

where Cov is the bilinear covariance E(ab)-(Ea)(Eb). Expand the product
and product-of-means differences, using all phases bounded by1. FG8
therefore supplies an explicit sufficient geometric precision budget
for transporting the retained signed statistic across resolutions.

It supplies **no sign or smallness** for that statistic: the complement
b=conjugate(a) has product1 before and after perfect calibration. For the
same-forcing coherent seed s*=-pi/16, U_n(s*)=-T_n and e(hU_n(s*))->1;
the independent calibration carrier C_j has exactly the same Fibonacci
returns and curvature as for the authentic seed0. Perfect circle learning
therefore cannot, by itself, distinguish their arithmetic cancellation.
A joint observation law coupling the learned geometry to authenticated
original-zero arithmetic must still be proved. The separate covariance
front investigates that coupling with all phase anchors retained.

## Provenance and reproducibility

Read-only dependencies: AGENTS.md; canonical `farey_gauss_defect.py` golden
brackets; `oily_macaroni_transfer.py` source/clock distinction;
`research/2026-11-07/learning_yoneda/learning.py`; canonical finite carrier,
belief and history APIs. No imported/frozen source was modified.

`oracle.py` independently tests the general geometry with exact Gaussian
rationals and the Fibonacci identity in Q(alpha). `numerical.py` tests the
actual irrational golden rotation at preregistered depths with independently
generated coordinates. Those high-precision tests are observations, not
interval certificates. The neighboring [FibonacciClock.lean](../formal/FibonacciClock.lean) checks
only the integer-coefficient recurrence underlying FG1–2 in Lean core. It
does not formalize real rotations, geometry, noise bounds or covariance.
No external scholarly referee claim.

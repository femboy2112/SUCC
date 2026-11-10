# Fixed-depth learning has an exactly calibrated signed response

**Status: PROVED PAPER / instrument theorem. Original-zero cancellation OPEN.**
This is additive to QS1–6 at parent `86327467191420d2157eeae5f4cfa1c2c62810da`.
It does not replace or modify the authenticated four-pole source. The new
point is a uniform calibration theorem for the finite-resolution observer:
fixed resolution can suffice once its phase origin is averaged, and its
signed depth spectrum is determined explicitly by the signal it retains.
No worldwide novelty, new general category, or new arithmetic cancellation
estimate is claimed.

## FD1. Uniform discrepancy controls empirical/Haar projection mismatch

Let μ be a finite probability measure on the circle T=R/Z. A separate finite
sample space Ω may map to the same x in T repeatedly. Conditional averaging
below is on Ω; μ is its pushforward. Let λ be Haar probability measure and

    D(μ) = sup_C |μ(C)-λ(C)|,

where C ranges over all circular half-open intervals, including empty/full
intervals. Fix a nonzero integer h, write a(x)=exp(2πihx), and let b:Ω→C
be any function with |b|≤1. Put W=E_Ω(ab). No assumption that b is a function
of x is made. This matters when different historical times have the same
current local phase.

For integer M≥1 and θ in T, partition T into the M intervals with boundaries
θ+j/M. Let P^μ_(M,θ) denote conditional averaging on the pullback partition.
Empty cells contribute zero. Define P^λ_(M,θ)a at x as the Haar average of a
on the same cell. Then

    E_μ |P^μ_(M,θ)a - P^λ_(M,θ)a| ≤ 2π|h| D(μ).       (FD1)

The bound is uniform over every M and θ. It requires neither a lower bound
on cell mass nor M D(μ)<1. In particular it remains valid at and beyond
finite support saturation.

**Proof.** Lift one cell C=[l,r), of length L=1/M, to the real line and put
ν=μ−λ. Define F(t)=ν([l,t)), u=(t−l)/L, and the bridge

    B(t)=F(t)−uν(C)
        =(1−u)ν([l,t))−uν([t,r)).

Both subinterval discrepancies have modulus at most D(μ), hence |B(t)|≤D(μ).
Write A_C=L^(-1)∫_C a(t)dt. Integration by parts for the finite signed
measure (with half-open endpoint convention) gives

    ∫_C a dμ − μ(C) A_C
       = ∫_C a dν − ν(C) A_C
       = −∫_l^r B(t) a'(t)dt.

Thus its modulus is at most 2π|h|D(μ)/M. If μ(C)>0, this modulus is exactly
μ(C)|P^μa−P^λa| on that cell. If μ(C)=0, the left side is zero; no division
is made. Summing over the M cells proves FD1. The circle wrap is harmless
because a is periodic and each cell has the declared continuous lift. QED.

An ordinary interval discrepancy bound on [0,1) also bounds all circular
intervals by the same constant: the complement of a wrapping circular
interval is an ordinary interval and ν(T)=0. There is no extra factor two.

## FD2. Averaging the origin gives an exact sinc-squared calibration

Set sinc(t)=sin(t)/t, continuously extended by sinc(0)=1, and

    c_(M,h)=sinc²(πh/M),
    F_M=∫_(θ∈T) E_Ω[(P^μ_(M,θ)a)(P^μ_(M,θ)b)] dθ.

All means and covariances here are bilinear, without complex conjugation.
Then

    |F_M−c_(M,h) W| ≤ 2π|h| D(μ).                       (FD2)

Indeed the stronger operator statement is

    ||∫_T P^μ_(M,θ)a dθ − c_(M,h)a||_(L¹(μ))
        ≤ 2π|h|D(μ).                                   (FD3)

This is uniform over every bounded complement, including complements chosen
after the local source is known.

**Proof.** Conditional averaging is symmetric for the bilinear mean, so
E[(Pa)(Pb)]=E[b Pa]. For fixed x, as θ varies uniformly the location u of x
inside its cell is uniform in [0,L), where L=1/M. Hence

    ∫_T P^λ_(M,θ)a(x)dθ
      = a(x) L^(-2)∫_0^L∫_0^L exp(2πih(v−u))dv du
      = c_(M,h)a(x).

Integrate FD1 in θ and use the triangle inequality to obtain FD3; pair it
with |b|≤1 to obtain FD2. QED.

For the centered covariance C=Cov(a,b), define the origin-averaged retained
covariance C_M=F_M−(Ea)(Eb). With η=|Ea|,

    |C_M−c_(M,h)C|
       ≤ 2π|h|D(μ)+(1−c_(M,h))η.                        (FD4)

The extra marginal term is displayed rather than silently dropped. Classical
integration by parts also gives η≤2π|h|D(μ), so FD4 is at most 4π|h|D(μ).
M=1 gives c_(1,h)=0 and C_1=0 exactly. If h is a nonzero multiple of M,
c_(M,h)=0; this is a genuine calibration alias. Any M>|h| avoids it.

## FD3. The authentic source admits fixed-resolution calibration

Keep exactly

    r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2),
    U_0=0, U_n=16U_(n−1)+r(n).

For the prior deterministic prime selector p=p_A on J_A={A,...,2A−1}, use

    x_n=[U_n]_p,   a_n=e(hx_n),   b_n=e(h(U_n−x_n)).

The original unwrapped states, carries and all four pole coefficients remain
in the source construction. Import the proved source coverage and local
interval discrepancy from PE/EC/CH, as pinned below. With L=(p−1)/4,
I={L+1,...,2L}, and exact weight distance

    ε_A=Σ_n |1_(J_A)(n)/A−1_I(n)/L|,

the actual-epoch local law obeys

    D_A ≤ ε_A/2 + 1/p + δ_p H_((p−1)/2) =: d_A.          (FD5)

Here δ_p is the uniform nonzero additive-character bound on the complete
selected prime clock; one may use the explicitly scoped Cochrane–Pinner
bound in EC2 or the preceding BK bound. The already proved selector and
coverage give d_A→0 through **all integer epochs** A. There is no supplied
numerical threshold for the PNT-dependent eventual statement.

**Proof of transport.** The complete clean clock law on I has interval
discrepancy at most 1/p+δ_pH by CH3. Pushforward by the actual local phase
map contracts total variation. The distance of the two time probability
measures is ε_A/2; therefore every interval mass changes by at most ε_A/2.
On I the actual source is the clean prime clock. This proves FD5 without
extending its dynamics past a new pole birth. QED.

Consequently, for every fixed h≠0 and every fixed integer M>|h|,

    F_(A,M,h) = c_(M,h) W_A(h;0) + O_h(d_A),             (FD6)

with explicit absolute error 2π|h|d_A. Since c_(M,h)>0,

    F_(A,M,h)→0  if and only if  W_A(h;0)→0.             (FD7)

An M equal to a fixed power of 16 may be chosen. This removes the prior
need to let the local digit resolution grow merely to identify the signed
mean through this origin-averaged instrument. It does not prove its decay:
FD7 is expressly an equivalence, not a weaker arithmetic conjecture.

The useful paid theorem is the **uniform calibration and resource reduction**,
not the renaming of Weyl's criterion. The root source sweep separately tests
it on literal-zero epochs and matched same-forcing rational controls. The
control b=conjugate(a) has W=1 and F_M→c_(M,h), despite d_A→0. Thus the
retained response remains source-selective and its arithmetic sign unpaid.

## FD4. The averaged signed depth spectrum cannot manufacture cancellation

For M_d=16^d, use the same θ for every depth so the partitions are nested.
Let a_(d,θ)=P_(M_d,θ)a and b_(d,θ)=P_(M_d,θ)b. The signed increment is

    J_d=∫_T E[(a_(d+1,θ)−a_(d,θ))
                 (b_(d+1,θ)−b_(d,θ))]dθ.

The exact projection algebra from QS4 gives J_d=F_(M_(d+1))−F_(M_d).
Therefore

    |J_d−(c_(M_(d+1),h)−c_(M_d,h))W|
       ≤ 4π|h|D(μ).                                    (FD8)

On the selected source, every fixed depth therefore has an explicit limiting
transfer coefficient multiplying **the same** signed mean, up to an error
that vanishes uniformly in d. For M_d≥|h|, these coefficients are nonnegative:
sinc²(t) decreases on 0≤t≤π, since t cos t−sin t<0 on (0,π).

Do not sum the FD8 error separately over arbitrarily many depths. Telescoping
first gives the sharper bound, uniform in integers E>D≥0,

    |Σ_(d=D)^(E−1)J_d−(c_(M_E,h)−c_(M_D,h))W|
       ≤ 4π|h|D(μ).                                    (FD9)

This retains the signed cancellation before bounding the endpoint errors.
The exact same-origin nesting is essential; independent unrelated partitions
would not define these martingale increments.

For the discarded signed residual R_M=W−F_M,

    |R_M−(1−c_(M,h))W| ≤ 2π|h|D(μ).                    (FD10)

If |πh/M|≤1, the alternating cosine series proves

    0≤π²h²/3−M²(1−c_(M,h))≤2π⁴h⁴/(45M²).

Combining this with FD10 gives the explicit normalized bound

    |M²R_M−(π²h²/3)W|
       ≤ 2π|h| M²D(μ)+2π⁴h⁴/(45M²).                  (FD11)

Thus for any selected-source sequence M_A→∞ with M_A²d_A→0,
M_A²R_(A,M_A)−(π²h²/3)W_A→0. This assertion does not require W_A to converge.
Its coefficient is a derived geometric transfer coefficient, not a fitted
constant. It does not disprove the earlier exact gamma completion residual:
that is a different quantity. A new gamma hypothesis must specify a transport
between those observables before the two constants can be identified.

## FD5. Finite origin menus have an explicit acquisition error

The integral over θ is a mathematical observer average, not one finite sensor
reading. For the declared menu θ_j=j/Q, 0≤j<Q, set

    F_(M,Q)=Q^(-1)Σ_j E[(P_(M,θ_j)a)(P_(M,θ_j)b)].

Then for every integer Q≥1,

    |F_(M,Q)−c_(M,h)W|
       ≤ 2π|h|D(μ)+4π|h|/Q.                            (FD12)

**Proof.** FD1 bounds the empirical/Haar mismatch at each menu point. For
fixed x, θ↦P^λ_(M,θ)a(x) is a periodic sawtooth phase with M jumps on the
unit θ interval. Between jumps its derivative modulus is at most 2π|h|.
The sum of jump magnitudes is at most 2π|h|, because each jump is the
difference of averages on adjacent cells and has modulus at most
2π|h|/M. Total variation is at most 4π|h|. On each equal 1/Q interval,
the error between its integral average and its left endpoint value is at
most that interval's variation. Summing after multiplication by 1/Q gives
4π|h|/Q. Endpoint conventions may change the value at a jump, but the same
variation estimate includes that jump. Pair with |b|≤1. QED.

Hence a fixed local digit depth, with Q_A→∞ arbitrarily slowly, gives the
same asymptotic calibration. For a fixed accuracy target one can first choose
a finite Q from FD12, independently of epoch A. This is an offline or
epoch-completed finite-history statistic; conditional means do not acquire
a strict-past causal interpretation without a separate learning protocol.

## FD6. Hostile receipts and boundaries

- **Unaveraged origin is not calibrated by c_(M,h).** Put μ equally on
  x=0,1/2, h=1, b=conjugate(a), M=2. At θ=0 each occupied cell is a
  singleton, so the retained product mean is 1; c_(2,1)=4/π². This example
  has large discrepancy, so it refutes equality without a discrepancy term,
  not FD2. For genuinely Haar μ with b=conjugate(P_(M,0)a)/|P_(M,0)a| on
  nonzero cells, the fixed-origin retained mean is sinc(π/M), while
  c_(M,1)W=sinc³(π/M); equality fails even at D=0 for M≥2.
- **Haar local phase is insufficient for decay.** Haar μ and
  b=conjugate(a) give W=1, F_M=c_(M,h), and
  R_M=1−c_(M,h). The source local discrepancy hypothesis alone cannot
  exclude coherent complementary phase locking.
- **A calibration alias destroys invertibility.** Haar μ, h=M, and
  b=conjugate(a) give W=1 but F_M=0. The condition c_(M,h)>0 cannot
  be omitted from FD7.
- **Finite full phase knowledge does not identify the literal seed.** The
  previous matched same-forcing rational controls preserve the selected
  p-primary phase while changing the real complement; FD1–12 hold for
  both. Original source authentication must remain in any decay premise.
- **Horizon dependence.** FD11 requires M²d_A→0, not just d_A→0.
  Passing to a normalized moving-resolution residual without this joint
  rate would discard the displayed error term. FD2 itself is uniform M.
- **Source completion gamma is a different calibration.** The prior GQ
  product quotient is independent of the seed when its completion reference
  follows the seed. FD2 retains the full signed W. Neither theorem alone
  supplies a map from that gamma constant to original-zero covariance.

## Provenance, logical contribution and next theorem

Read-only dependencies: original `selected_orbit.py`; PE1–9 in
`research/2026-11-07/learning_yoneda/arithmetic/PRIME_EPOCH_THEOREM.md`;
EC1–2 in `signed_covariance_round2/EXPLICIT_CLOCKS.md`; CH3–4 and CH7 in
`signed_covariance_round2/chronology/THEOREMS.md`; QS1–6 in
`quotient_signal/quotient/THEOREMS.md`, all contained in parent86327467.
FD1–4 are derived above using finite conditional expectation, elementary
integration by parts and the declared local discrepancy import. No new
special-function or exponential-sum theorem is imported. The sinc expansion
is proved from the cosine series; no numerical fit supplies its coefficient.

The exact oracle compares a direct partition integral, a pair-kernel formula,
and a formal root-of-unity finite-grid spectral calculation. These are
independent finite algebra paths sharing the same declared finite data.
They do not certify the continuum proofs, the imported PNT/subgroup estimates,
or any asymptotic arithmetic claim. No new Lean certificate is asserted.

The remaining arithmetic theorem may now be posed at **any one fixed
non-aliased resolution per h**: prove F_(A,M,h)→0 for the original zero source,
uniformly over all large integer A. Its logical strength is exactly full
Weyl decay. A genuinely useful next step must estimate the signed cell
charges entering F from original chronology, not infer their sign from
small local discrepancy or successful learning.

**Pi base-16 normality: OPEN. RH: OPEN.**

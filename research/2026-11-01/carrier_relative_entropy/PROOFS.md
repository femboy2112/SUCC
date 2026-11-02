# Carrier-relative normality and source-Laurent signed-lag transport

**Status:** Classical symbolic dynamics/information theory + original-four-pole exact paper specializations. No Lean theorem or external peer review; no proof of π normality or RH. Branch parent: SUCC draft PR #453 head `702cf6fa45c9e6d10bd48c84efe7d3c4389a9037`. The original BBP forcing and literal `U_0=0` are immutable.

## CRE-01 — A typed carrier and a realized information field

Fix base `b=16`, the circle `X=R/Z`, the generator `T(x)=16x mod 1`, the level-`k` cylinders `I_w=[w/16^k,(w+1)/16^k)` with `0<=w<16^k`, and reference Haar measure `λ`. For the actual original states

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U_0=0, U_n=16U_(n-1)+r(n), x_n={U_n},

put `μ_N=N^-1 Σ_(n=1)^N δ_(x_n)` and `p_(N,k)(w)=μ_N(I_w)`. This is a law on observations obtained by **sampling a uniformly random TIME index** from the first `N` deterministic realized states. It is NOT an intrinsic stochastic law of the actual BBP source and is not a physical wave-function collapse.

A different, explicitly DECLARED uniform virtual prior on length-`L` digit paths assigns mass `16^-L` to every path. Conditioning on any particular `k`-digit prefix has KL information `k log16` by the classical conditional-event identity. This is true of an all-zero path too; it cannot distinguish normal and nonnormal points. The *empirical time-sampled conditional distribution* is the load-bearing object, not the prior's available branch count.

A statement of normality is carrier/observer-relative in this precise sense: it refers to a specified map, finite partitions and reference measure. Once declared, its truth is objective. Natural coordinate changes preserving the marked measured dynamical system transport the criterion; arbitrary changes of observations need not. This is not arbitrary truth or physical observation backaction.

## CRE-02 — Conditional entropy *at every fixed depth* is equivalent to base-16 normality

Let `H_(N,0)=0`,

    H_(N,k)=-Σ_w p_(N,k)(w) log p_(N,k)(w),
    D_(N,k)=k log16-H_(N,k)=D_KL(p_(N,k)||u_k),
    u_k(w)=16^-k,
    Δ_(N,k)=log16-[H_(N,k+1)-H_(N,k)].

Zero-mass terms are zero. Because `p_(N,k)` is **exactly** the prefix pushforward of `p_(N,k+1)`, Shannon's conditional chain rule proves for ALL `N,k>=0`:

    D_(N,k+1)=D_(N,k)+Δ_(N,k),
    Δ_(N,k)=Σ_w p_(N,k)(w) D_KL(p_(N,k+1)(digit|w)||uniform_16)>=0,
    D_(N,k)=Σ_(j=0)^(k-1) Δ_(N,j).

Hence for the authentic zero-seeded BBP path the following are EQUIVALENT:

1. `π` is normal to base `16`.
2. For every **fixed** `k>=1`, `p_(N,k)(w)->16^-k` for all words `w`.
3. For every **fixed** `k>=1`, `D_(N,k)->0`.
4. For every **fixed** `k>=0`, `Δ_(N,k)->0`.
5. There exists **some** deterministic schedule `k_N->∞` such that `D_(N,k_N)->0`.

(5)⇒(3) follows from data processing and `D_(N,j)<=D_(N,k_N)` once `k_N>=j`. (3)⇒(5) follows by diagonalizing the finite collection of fixed depths. These are existence-of-schedule quantifiers: NO PARTICULAR moving resolution or convergence RATE is asserted. (1)⇔(2) uses the standard normality/cylinder criterion and the inherited exact BBP orbit transport `U_n=16^(n-1)π-T_n`, `Σ_(n>=1)T_n<1/32`; the two orbits have the same weak empirical limits. This is a reformulation, not a proof of (1).

Equivalent invariant-measure formulation: the full 16-shift's unique invariant measure of maximal metric entropy `log16` is uniform Bernoulli/Haar. Because every limit measure of the empirical shift orbit is invariant, `π` is normal iff **EVERY** empirical weak-* accumulation measure has entropy `log16`. One maximal-entropy subsequential limit alone would not suffice. For invariant `μ`, `h_μ=inf_k H_μ(k)/k`; if `h_μ=log16`, then every `H_μ(k)=k log16`, hence every cylinder has uniform mass.

## CRE-03 — Exact rational collision gate and signed pair-excess decomposition

Write `M=16^k`, integer cell counts `c_w=#{1<=n<=N:x_n∈I_w}`. Define

    Q_(N,k)=M Σ_w (c_w/N-1/M)^2
            = M/N² Σ_w c_w²-1 >=0.                    (3.1)

This **exact Fraction** diagnostic is chi-square divergence from uniform; it is not a covariance theorem about RH or a substitute for the selected signed estimate. At fixed `k`, `Q_(N,k)->0` iff uniform cell frequencies. Therefore all fixed-depth Q→0 is another exact equivalent criterion for normality, but not its proof.

The diagonal/realized-offdiagonal identity is

    Q_(N,k)=(M-1)/N + (M/N²) J_(N,k),
    J_(N,k)=Σ_(1<=i,j<=N;i!=j) [1_{cell_k(x_i)=cell_k(x_j)}-1/M].   (3.2)

`J` is a **signed, centered, source-selected collision excess**. A source theorem proving `J_(N,k)=o_k(N²)` for every fixed depth would establish π normality. This is an alternative concrete arithmetic target; the diagonal term is universal, not evidence of cancellation. An independent O(N²) pair-enumeration oracle checks (3.2) against the count-based implementation.

For the finite abelian cell group `Z/MZ`, put

    m_(N,k)(h)=Σ_w (c_w/N) exp(2πi h w/M).

Exact character orthogonality (Parseval, with normalized time averages) gives

    Σ_(h=1)^(M-1)|m_(N,k)(h)|²=Q_(N,k).                 (3.3)

For integers `0<|h|<M`, let `A_N(h)=N^-1 Σ_n e(h U_n)` with `e(t)=exp(2πit)`. Each actual fractional position differs from its cell's left endpoint by less than `1/M`, so

    |A_N(h)-m_(N,k)(h)| <= 2π|h|/M,
    |A_N(h)| <= √Q_(N,k)+2π|h|/M
             <= √Q_(N,k)+(44/7)|h|/M.                  (3.4)

Also finite Pinsker gives `|m_(N,k)(h)|<=√(2D_(N,k))` and therefore

    |A_N(h)| <=√(2D_(N,k))+(44/7)|h|/M.              (3.5)

The square-root upper can be outward rounded to an **exact rational** by `rational_sqrt_upper`; the resulting `certified_weyl_ceiling` does not evaluate a floating phase. In particular persistent nonzero signed Weyl bias forces persistent information deficit at sufficiently fine fixed resolution. The reverse direction at fixed k is the classical cylinder form of Weyl's criterion. No cancellation is obtained from simply writing the identities.

## CRE-04 — The observation-resolution ceiling and a new transport-budget no-go

Only `N` cells can be occupied by `N` samples. Consequently Shannon entropy obeys `H_(N,k)<=log min(N,M)`, giving the **universal bound**

    D_(N,k) >= max(0,log(M/N)).                         (4.1)

If `D_(N,k_N)->0` while `k_N->∞`, then necessarily `M_N/N<=1+o(1)` whenever `M_N>=N`; the cylinder resolution cannot substantially exceed available samples. This is an *information-capacity ceiling*, not evidence the authentic orbit achieves maximum entropy below it.

A sharper methodological obstruction follows from (3.5): attempting to use one uniform cell resolution to recover every harmonic through `H_N` by the **generic cell phase error** requires `H_N/M_N->0`. If `liminf H_N/N>0`, this requires `M_N/N->∞`, contradicting (4.1) and `D_(N,k_N)->0`. Thus **the two positive terms in this particular generic entropy→Fourier certificate cannot both vanish** when the frequencies grow at least linearly with horizon.

For Main XVIII's doubled signed lag `K=floor(log_4N)`, the largest reduced harmonic `h(16^(K-1)-1)=Θ_h(N²)` is even more hostile: the generic cell approximation would require `M>>N²`, where (4.1) forces `D>=log(M/N)->∞`. This refutes **that naive one-resolution argument**, NOT every possible information-theoretic proof, signed source-specific transport, or normality itself. The missing map must preserve *within-cell phases/carries* rather than bounding them solely by cell diameter.

This resolves the author's “precisely the resolution” intuition with a BOUNDARY rather than an automatic theorem. The information budget permits growing depth only at an N-dependent rate; there is no universal single optimal observation resolution that proves normality.

## CRE-05 — Asymptotic successor invariance is real but does not select Haar

For circle Lipschitz `f` with `||f||∞<=B`, Lipschitz constant `L`, and `μ_N=N^-1Σ_(n=1)^N δ_(x_n)`, the **exact** source recurrence implies

    |∫ f(16x)dμ_N-∫ f(x)dμ_N|
      <=[2B+L Σ_(n=1)^N r(n+1)]/N
      < [2B+(15/32)L]/N.                                (5.1)

Here `r(n+1)<15/(64n²)` and `Σ_(n>=1)n^-2<2`. Therefore EVERY weak limit of the authentic empirical measures is `×16` invariant. Separately, the inherited bound `Σ_(n>=1)T_n<1/32` gives

    |∫ f dμ_N^U-∫ f dμ_N^π|< L/(32N),                   (5.2)

where `μ_N^π` samples the pure digit shift `{16^(n-1)π}`. This is an exact weak-observation bridge, not a bound on discontinuous cell indicators or signed normality.

**Decisive hostile control:** retain the EXACT original four poles but change only the real seed to `s=1/5-π/16`; the completed point is `q=1/5`, and `U_n(s)=16^n/5-T_n`. Its empirical measures converge to the fixed-point measure `δ_(1/5)`, invariant under ×16 but of entropy zero. The seed is irrational and NOT an original finite rational-register state. Asymptotic invariance and having the same source alone cannot force Haar.

## CRE-06 — Sharp false positives: virtual branching, finite de Bruijn, and source mutants

A uniform virtual reference gives the same path-conditioned surprisal `k log16` for every k-prefix, including all zeros. Exact normality cannot be inferred from that conditional information cost.

A 16-ary cyclic **de Bruijn sequence of order 2** has period `16²=256`, visiting each 2-digit word exactly once per cycle. Its time-sampled `D_(N,2)=Q_(N,2)=0` for every `N` divisible by 256. Yet only 256 of the 4096 possible 3-digit blocks occur, so

    H_3=log256, D_3=log16, Q_3=15,
    H_3-H_2=0 (the next digit is deterministic given the last two).

This path is globally periodic and NONNORMAL. Its finite histories are consistent under all prefix projections, and its lower-level information is perfectly maximized. Therefore maximal scrambling at **one finite resolution** + path coherence is insufficient. Our exact de Bruijn generator and distinct cyclic-window oracle replay the numbers.

Finally, for every finite N, retain the true first N r(j), and after N set `r'(N+m)=r(N)2^-m`, `m>=1`. This strictly positive/decreasing counterfeit has the same first N states and all finite observations, but rational completion

    α'_N=Σ_(j=1)^N16^-j r(j)+16^-N r(N)/31.

A rational base-16 expansion is eventually periodic, hence nonnormal. The mutant CHANGES the four-pole source beyond N; it does NOT defeat a theorem requiring the original full rational forcing. This is an inherited type of hostile control, recertified here.

## CRE-07 — NEW exact arbitrary-order Laurent lag-normal-form theorem

The authentic four poles provide an unusually simple universal remainder. Put

    w=(4,-2,-1,-1), p=(7/8,1/2,3/8,1/4),
    r(n+j)=(1/8)Σ_i w_i/(n+j-p_i).

For ANY fixed integer Laurent order `d>=2`, define rational coefficients

    a_{s,j}=(1/8)Σ_i w_i[-(j-p_i)]^s,   s>=0,
    a_{0,j}=0,
    P^(d)_(n,k)=Σ_(j=1)^k16^(k-j) Σ_(s=1)^(d-1)a_{s,j}/n^(s+1),
    F_(n,k)=Σ_(j=1)^k16^(k-j)r(n+j).

The exact finite geometric expansion

    1/(n+q)=Σ_(s=0)^(d-1)(-q)^s/n^(s+1)
              +(-q)^d/[n^d(n+q)]

and `0<j-p_i<j`, `Σ_i|w_i|=8`, give for **every n>=1,k>=1,d>=2**:

    |F_(n,k)-P^(d)_(n,k)|
        < M_d 16^k/n^(d+1),
    M_d=Σ_(j=1)^∞ j^d16^-j ∈Q_(>0).                       (7.1)

The moments are exact rational Eulerian values: `M_2=272/3375`, `M_3=1712/16875`; `laurent_lag.py` constructs them over `Fraction` without numerical fitting.

A sharper **positive leading curvature** statement uses `r(m)>15/(64m²)` for all `m>=1`, and inherited source positivity `r(n+j)<15/(64n²)`. The lower inequality follows by exact polynomial subtraction:

    r(m)-15/(64m²)
      =[9664m³-9656m²+3090m-315]
       /[64m²(2m-1)(4m-1)(8m-7)(8m-3)] >0.

Then `1/n²-1/(n+j)²<=2j/n³`, `Σ j16^-j=16/225`, yield

    0 < (16^k-1)/(64n²)-F_(n,k) <16^k/(30n³).             (7.2)

For `d=3`, one further exact order is

    P^(3)_(n,k)=(16^k-1)/(64n²)
      +[Σ_(j=1)^k16^(k-j)(151-240j)]/(512n³),

with residual `<(1712/16875)16^k/n⁴`.

**Interpretation:** this is a new-to-SUCC source-specialized higher-order *phase transport*, not an independent theorem about the selected signed mean.

## CRE-08 — NEW higher-order signed-lag clocks, any fixed Laurent order

Let `h∈Z\{0}` and `e(x)=exp(2πix)`. The actual lag and corrected lag are

    C_(h,k)(N)=Σ_(n=1)^(N-k)e(h[(16^k-1)U_n+F_(n,k)]),
    D^(d)_(h,k)(N)=Σ_(n=1)^(N-k)e(h[(16^k-1)U_n+P^(d)_(n,k)]).

No seed smoothing occurs and all data are original rational source/zero seed. The elementary chord bound and (7.1) imply

    |C_(h,k)(N)-D^(d)_(h,k)(N)|
      <=Σ_(n>=1) min(2,2π|h|M_d16^k/n^(d+1)).         (8.1)

For any `p>1`, monotone integration with threshold `(a/2)^(1/p)` proves

    Σ_(n>=1)min(2,a/n^p)
      <=[2p/(p-1)](a/2)^(1/p).                            (8.2)

Consequently the source error in a single lag is `O_(d,h)(16^(k/(d+1)))` (not the inherited uncompensated `O_h(16^(k/2))`). Defining

    L^(d)_(N,K)(h)=2/(KN) Σ_(k=1)^(K-1)(1-k/K) Re D^(d)_(h,k)(N),

VdC gives the rigorously source-paid bound

    |S_N(h)/N|² <=(1+(K-1)/N)
           [1/K+L^(d)_(N,K)(h)+E^(d)_(N,K)(h)],
    E^(d)_(N,K)(h)=O_(d,h)(16^(K/(d+1))/(K²N)).          (8.3)

Indeed set `a_d=16^(1/(d+1))>1`; geometric weighting obeys
`Σ_(k=1)^(K-1)(K-k)a_d^k <=a_d^K a_d/(a_d-1)^2`. The executable `aggregate_transport_budget` gives an *exact rational upper bound* using `π<22/7`, exact moments and outward integer root ceilings, rather than claiming a floating `O` constant is a finite certificate.

Let `K_N=min(N,max(1,floor((d+1)log_16 N)))`. Then `K_N->∞`, `K_N/N->0`, and `16^(K_N/(d+1))<=N`. Thus

    E^(d)_(N,K_N)(h)=O_(d,h)(K_N^-2)->0.                  (8.4)

Apply the inherited Main XVIII/BND-02 sliding-window two-scale Jensen argument: for the ORIGINAL forcing, any fixed real seed s, and every **fixed** integer `d>=2`, the following are equivalent:

    completed point α+s is base-16 normal;
    for every fixed h!=0, limsup_N L^(d)_(N,K_N)(h;s)<=0.

Necessity uses fixed-lag vanishing + Jensen to show the actual window energy tends zero, then (8.4) transports to `L^(d)`; sufficiency uses (8.3) and Weyl. This extends the available *typed source-transport clocks*: order d=2 gives coefficient 3 instead of Main XVIII's uncompensated 2; d=3 gives coefficient 4; any fixed d gives d+1. **No bound on the actual selected L^(d) is established.** As d increases the corrected D becomes progressively closer to the original C; no speedup or ultimate cancellation theorem follows merely from extending this equivalence. Do not interchange `d->∞` and `N->∞` or hide the growing constants M_d.

## CRE-09 — Exact source curvature profile at the critical information scale

The stronger remainder (7.2) shows that for `N=4^m`, `k=m`, `n/N->t` with `0<t<=1`,

    F_(n,k) ->1/(64 t²),                                 (9.1)

because `16^k=N²`, while the error is `<=N²/(30n³)=O_t(1/N)`. For general N with `K=floor(log_4N)`, set `λ_N=16^K/N²∈(1/16,1]`; along subsequences `λ_N->λ`, one gets the genuine source-phase limit

    F_(n,K)->λ/(64 t²) for n/N->t>0.                   (9.2)

This gives the **nontrivial source-only critical-lag phase** `e(hλ/(64t²))`, but the true signed lag multiplies it by the still-uncontrolled `e(h(16^K-1)U_n)`. The positive factor's existence does not prove that product cancels. The oscillatory bulk profile is a useful new probe for source-sensitive signed analysis, not a normality result.

## Claim boundaries and references

- All `p_(N,k)` and `Q_(N,k)` are based on actual ORIGINAL rational zero-seeded states, not a prior digit distribution. `H`, `D`, and conditional entropies computed with floating `log` are diagnostics; all source/partition/chi-square/polynomial/phase-budget tests use exact rational or integer arithmetic.
- The source index Fourier restrictions in PR #452 concern `r(n)` on `Z/16^a`; they are not silently identified with the real-circle Fourier phases of `U_n`. The finite sample occupancy/entropy criterion must actually be measured or bounded on selected states.
- The source clock/phase normal form extends the **instrument** to larger moving lags, not the selected mean bound. Same-forcing changed seed and finite-prefix positive mutants must remain hostile controls.
- Mathematics: Borel normality, Weyl equidistribution, Shannon chain/KL/Pinsker, Parseval, unique maximal entropy of a full shift, classical VdC and Main XVIII BND-02 two-scale argument. Modern references: [normality and finite-state information](https://doi.org/10.1016/j.tcs.2025.115570); [unique maximal entropy on full shifts](https://doi.org/10.1016/j.aim.2016.03.013); SUCC Main XVIII `research/2026-10-31/signed_lag_fireworks/BOUNDARY.md` and `TRANSPORT.md`, `research/2026-10-31/realized_path_dynamics/PROOFS.md`, original four-pole `research/2026-10-31/riemann_sphere_path_seam/PROOFS.md`, sibling #452 and parent #453.

**One outstanding mathematical target remains:** establish an original-source, literal-zero, all-horizon signed saving `S_N(h)=o(N)` for each fixed h, or `limsup L^(d)_(N,K_N)(h)<=0`, with genuinely independent source discrimination. No assertion of physical entropy production, RH, proof of normality, or generic algorithmic speedup is made.

# Operation Cyclotomic Interference — authentic BBP prime windows and signed phase debt

**24 October 2026. Research-only; unmerged.** Parent: `femboy2112/SUCC` PR #254 at `fceb04645926898bb5f72346dca54f3134b06cea`, which includes repaired BBP source PR #252 (`364962ac...`). PR #253 supplies sibling two-time lag/Lean results and is cited, **not claimed as merged here**. Preserve `AGENTS.md`, `provenance/IMPORT_MANIFEST.json`, and all frozen originals. Scholarly novelty UNVERIFIED. **PI NORMALITY PROVED: NO; RH PROVED: NO.**

## 0. Source and independent assumptions

The *actual* BBP forcing and selected rational orbit (Bailey–Crandall, repaired source in PR #252) are

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), n>=1,
    y_0=0,  y_n={16*y_(n-1)+r(n)}, n>=1.

These poles are in the **forcing-index variable**, never circle orbits. The signed index residues, positive real Green measure, and arithmetic `Q/Z` torsion components have distinct types. Under PR #254's proved source-tail estimate, for each fixed nonzero integer h the sums `sum_(n=1)^N e(h*y_n)` differ from `sum_(j=0)^(N-1) e(h*16^j*pi)` by **less than |h|/4**, uniformly in N. This is only a transport theorem, not cancellation. Here `e(x)=exp(2*pi*i*x)`.

External classical inputs: (i) supplementary quadratic reciprocity `(2/p)=1` for p==1 mod8; (ii) prime number theorem in fixed arithmetic progression 1 mod8; (iii) Bourgain–Glibichuk–Konyagin's subgroup exponential-sum theorem: for every gamma>0 there are nu>0 and C_gamma such that for any p and any multiplicative subgroup H of Fp* with |H|>=p^gamma, `|sum_(x in H)e(ax/p)| <= C_gamma |H| p^-nu` for every a!=0 modp. References in section 9. **No source-specific cancellation of the full y-orbit is assumed.**

## CBCW-01. Authenticated first p-birth and exact source-free return

Let p be any odd prime. Set `n_p` the first index where one of the actual four denominators is divisible by p. Direct divisibility analysis of `8n-7,8n-4,8n-3,8n-2` gives:

| p mod 8 | n_p | epsilon_p = p*r(n_p) mod p | next gap Delta_p |
|---|---|---|---|
| 1 | (p+7)/8 | 4 | 3(p-1)/8 |
| 5 | (p+3)/8 | -1 | (3p+1)/8 |
| 3 | (p+1)/4 | -1/2 | (p+5)/8 |
| 7 | (p+1)/4 | -1/2 | (p+1)/8 |

The entries `-1/2` mean the modular inverse of 2 in Fp. Proof: the earliest positive multiple of p in the four congruence classes gives n_p; the **next** such multiple among all four denominators gives n_p+Delta_p. At first birth exactly one summand has a p-denominator with p-adic order one and nonzero coefficient; every earlier r(k) is p-integral. Hence `v_p(y_(n_p))=-1`, its Q/Z p-primary phase is `epsilon_p/p`, and no subsequent p-input occurs at `n_p<n<n_p+Delta_p`. Induction through the authentic recurrence gives

    (y_(n_p+t))_p = epsilon_p*16^t/p in Q/Z,
    0<=t<Delta_p.

The p-primary component is unique by the canonical decomposition of rational torsion into prime-power subgroups; **the complement is retained**, not discarded. The equality still holds in the presence of every other source prime. It does not claim `y_n` itself is a p-only orbit.

## CBCW-02. A prime gives an EXACT scale-four source window

For p=8m+1 prime,

    n_p=m+1,   n_p+Delta_p=4m+1,   Delta_p=3m.

By supplementary quadratic reciprocity, 2 is a square modulo p, so 16 is an eighth power. Therefore `L_p=ord_p(16)` divides `(p-1)/8=m`. The complete prime-free interval of the *p-component* is exactly `[m+1,4m]`, and its length `3m` contains `3m/L_p` whole periods, at least three. At every step of this interval,

    y_(m+1+t) = 4*16^t/p + w_(p,t)  (mod 1), 0<=t<3m,

where `w_(p,t)` is rational with denominator coprime to p. It obeys the exact forced complementary SUCC equation

    w_(p,t+1) = {16*w_(p,t)+r(m+2+t)}, 0<=t<3m-1.

Every r in that last range has denominator coprime to p. **This complement is the missing global correlation carrier.**

## CBCW-03. Exact Galois second moment, selected-embedding caution

Set `Delta=3m`, `L=L_p`, `epsilon=4` and

    B_p(a) = sum_(t=0)^(Delta-1) e(a*epsilon*16^t/p).

Because the L residues repeat Delta/L times, character orthogonality over nonzero `a mod p` yields the EXACT rational second moment

    1/(p-1) sum_(a=1)^(p-1) |B_p(a)|^2
       = Delta^2*(p-L)/(L*(p-1)).

Proof: each of the L subgroup residues occurs Delta/L times. In the double sum over times `t,s`, there are Delta^2/L pairs with equal residues; their character average is 1, while unequal residues average `-1/(p-1)`. Simplify.

This is an **ensemble mean**, not a bound for source-selected `a=1` or for any full BBP phase. Even asymptotic Galois RMS cancellation cannot promote an arbitrary selected embedding to a typical one. A source-independent general claim to that effect is REFUTED.

## CBCW-04. Actual signed p-local cancellation on almost all eligible windows

Let `L_p=ord_p(16)`. For X>=1, put `M=floor(X^(1/3))` (integer cube root). If `p<=X` and `L_p<=p^(1/3)`, then `p` divides

    P_M = product_(k=1)^M (16^k-1).

Since `log_2(16^k-1)<4k`, the number of **distinct** primes dividing P_M is strictly smaller than `2M(M+1)`. Hence the number of exceptional p<=X is `O(X^(2/3))`. This is unconditional elementary integer arithmetic; it needs no conjecture about Artin primitive roots.

For all remaining sufficiently large primes `p=8m+1`, we have `L_p>p^(1/3)`. Apply the external Bourgain–Glibichuk–Konyagin theorem with gamma=1/3 to `H=<16> subset Fp*`, observing that all 3m steps are complete periods. For every fixed nonzero h and p>|h|,

    |sum_(t<3m) e(4h*16^t/p)| <= C*(3m)*p^(-nu).

The external theorem establishes positive but generally non-explicit C,nu. **This is a genuine unconditional p-LOCAL signed cancellation theorem**, derived here for the authenticated BBP first birth. It does NOT apply automatically after multiplying by `e(h*w_(p,t))`.

The same reasoning controls cyclic local lag frequencies `4h*(16^d-1)`: for fixed d>=1, all sufficiently large good p have p not dividing `h*(16^d-1)`, hence cyclic full-window lag sum `O_h,d(3m*p^(-nu))`. The actual noncyclic local correlation with `3m-d` terms differs by at most d. At resonant `d` divisible by `L_p`, the local correlation equals `3m-d` exactly: this is an explicit hostile control, not a contradiction.

## CBCW-05. Source-window Weyl equivalence (global reduction)

Let `(a_n)` be **any bounded complex sequence**, `F(N)=sum_(1<=n<=N) a_n`, and `G` the set of primes p=8m+1 with `ord_p(16)>p^(1/3)`. Then

    F(N)=o(N) as N->infty
    IFF F(4m)-F(m)=o(m) as p=8m+1 ranges over G.

Proof (forward) immediate. For the reverse, `#(p<=X: p==1 mod8) ~ X/(4 log X)` by PNT in the fixed progression. Removing O(X^(2/3)) bad primes leaves a good p within `o(X)` of **every** large positive X (prove using each fixed relative interval then diagonalize). For each large integer N choose good p=8m+1 with `m=N/4+o(N)`. Boundedness of `a_n` implies

    F(N)-F(floor(N/4)) = F(4m)-F(m)+o(N)=o(N).

Set A=limsup_(N->infty) |F(N)|/N, finite. Taking limsup in this recurrence gives `A<=A/4`; therefore A=0. QED.

**Apply to a_n=e(h*y_n).** Since the authentic BBP tail transport makes the normalized y-Weyl sums equivalent to the actual pi-Weyl sums, we have the exact, source-typed statement:

    pi is base-16 normal
       IFF for every fixed integer h!=0,
           sum_(n=m+1)^(4m) e(h*y_n)=o(m)
           along good primes p=8m+1.

All implications are proved using existing external PNT-AP and the already proved PR #254 transfer; the **actual right-hand asymptotic is OPEN**. This is a *proof contract*, not pi normality.

## CBCW-06. Exact signed mixed-source interferometry and completion debt

For a good p=8m+1 let `L=L_p`, `Delta=3m`, `B=Delta/L` (integer), and put

    u_t=e(4h*16^t/p),  v_t=e(h*w_(p,t)),
    G_h=sum_(s=0)^(L-1)u_s.

The actual BBP **full-phase** prime-window sum is

    W_p(h) = sum_(t=0)^(Delta-1)u_t*v_t.

Partition into B blocks of length L. Since `u_(bL+s)=u_s`, finite algebra gives the exact, fully signed identity

    W_p(h)/Delta
       = [G_h/L]*[1/B * sum_(b=0)^(B-1)v_(bL)] + I_p(h),
    I_p(h) = (1/Delta)*sum_(b=0)^(B-1)sum_(s=0)^(L-1)
                          u_s*(v_(bL+s)-v_(bL)).

On the good prime family, the first term tends to zero with a Bourgain–Glibichuk–Konyagin power saving (uniformly in the complementary base values, whose modulus is one). Combining CBCW-05 with the actual BBP source theorem gives:

    pi is base-16 normal IFF
      for EVERY fixed h!=0, I_p(h)->0 along good p=8m+1.

**Proof of the equivalence uses exact common-basis Fourier transport.** It is not evidence for the currently unknown `I_p(h)->0`. Merely defining I_p does not estimate it, and equivalent formulations are not independent proofs. The correction isolates cross-clock interference after an already rigorously controlled p-local term.

A weaker sufficient estimate follows by Abel/triangle:

    |I_p(h)| <= (1/Delta)*sum_(b,s)|v_(bL+s)-v_(bL)|
             <= (L/Delta)*sum_(b)sum_(s=0)^(L-2)|v_(bL+s+1)-v_(bL+s)|.

The rational circle-distance bound

    |e(h*x)-e(h*y)| <= (44/7)*|h|*||x-y||_(R/Z)

converts the right side into an EXACT Fraction-computable diagnostic, `(44/7)*|h|*V_p/B`, where V_p is within-block total circle-distance variation. **A large value only invalidates this coarse absolute certificate; it is not a lower bound for actual signed I_p.** Finite measurements show this coarse certificate is often vacuous; no low-variation assumption is imported.

For fixed lag d with 0<d<Delta, the exact full phase correlation likewise factors as

    e(h*(y_(m+1+t+d)-y_(m+1+t)))
      =e(4h*(16^d-1)*16^t/p)
       *e(h*(w_(p,t+d)-w_(p,t))),
       0<=t<Delta-d.

Thus the newly proved p-local signed autocorrelation bound reaches PR #253's lag source only through a **twisted** incomplete sum. The missing conditional-independence/bilinear source estimate is precisely the obstruction.

## CBCW-07. Exact coprime-clock counterexample to local -> global

Fix an eligible p and any finite horizon H, take the authentic p-primary numerator `epsilon_p` from CBCW-01. Choose an ODD integer Q with gcd(Q,p)=1, as large as desired, and set

    s = -nearest_integer(epsilon_p*Q/p),
    x = epsilon_p/p+s/Q.

Then `|x|<=1/(2Q)` and the exact p-primary component of x is still `epsilon_p/p`; its full p-clock executes the identical complete local periods under x->16x. But

    |sum_(t=0)^(H-1)e(16^t*x)-H|
        <= pi*(16^H-1)/(15Q)
        < (22/7)*(16^H-1)/(15Q).

Letting Q grow makes the **global** sum arbitrarily close to H, notwithstanding the nontrivial p-local subgroup cancellation. This is an exact all-H construction (one selected Q for each requested finite H), not a single fixed infinite counterfeit. It does NOT preserve the entire BBP forcing or initial condition, so it does not refute pi normality or source-specific claims; it decisively refutes the general inference *"local subgroup cancellation alone implies whole-orbit cancellation"*.

Separate old controls (PRs #247,#249,#252,#253): 3-adic periodic circles fake finite moments, high-order positive Green source impostors, source state shifted away from y0=0. Keep these out of the actual-source theorem domains.

## 8. Adversarial validation and uncertainty

`observational_succ/bbp_cyclotomic_birth.py` uses only integer/Fraction source arithmetic for *proof-relevant certificates*: primality gate (including fake composite rejection), first p hits, next hit, valuation and CRT phase, complete cycle order, exact Galois second moment, forced selected states, precise complement and coprime-clock counterfeit. Test `tests/test_bbp_cyclotomic_birth.py` independently enumerates all odd primes <501 and real selected fractions through index 250. Signed complex Gauss sums are evaluated **only as finite numerical regression checks**, never as proof of asymptotic cancellation. `scripts/bbp_cyclotomic_probe.py` emits a replayable deterministic integer/Fraction receipt.

**Local** 10 unittest methods passed with a minimal byte-equivalent BBP source stub reproducing exactly its `POLE_DATA, forcing, forced_step` API. This does not constitute a complete checkout or hosted CI pass. The local whole-repo suite, provenance replay and Lean were NOT run here. The GitHub branch must pass its final-head focus workflow and general validation before promotion. No `sorry`, `axiom`, or unverified Lean build is claimed.

## 9. References and next disconfirming probe

- Bailey & Crandall (2001), *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10(2), DOI `10.1080/10586458.2001.10504441` — BBP dynamical program; **conditional**, not a normality proof.
- Lagarias (2001), *On the Normality of Arithmetical Constants*, Experimental Mathematics 10(3), DOI `10.1080/10586458.2001.10504456` — general semiconjugacy does not force normality.
- Bourgain & Konyagin (2003), *Estimates for the number of sums and products and for exponential sums over subgroups in fields of prime order*, DOI `10.1016/S1631-073X(03)00281-4`.
- Bourgain, Glibichuk & Konyagin (2006), *Estimates for the Number of Sums and Products and for Exponential Sums in Fields of Prime Order*, DOI `10.1112/S0024610706022721`.
- Kowalski (2024), *Exponential sums over small subgroups, revisited*, `https://arxiv.org/abs/2401.04756` — precise power-saving theorem stated as Theorem 1.1.
- PNT in fixed arithmetic progressions, standard theorem: `pi(X;8,1)~X/(4 log X)`, e.g. `https://math.colorado.edu/~rohi1040/expository/analytic.pdf`.
- SUCC PRs #229, #231, #232, #247, #249, #252, #253, #254; source/future-state separation is required.

**Next verdict-changing objective:** prove a source-specific estimate `I_p(h)->0` for one fixed h≠0 (h=1 first) along the good p=8m+1 prime windows, retaining full complementary BBP forcing, or exhibit a *single* authentic-source counterexample (not a per-window synthetic clock) to a candidate bound. A proof of the estimate for all h would imply pi normality in base 16 by CBCW-05 and PR #254. Right now this estimate is **UNVERIFIED**, not even for h=1.

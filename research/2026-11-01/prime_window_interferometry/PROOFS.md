# Selected 5-mod-8 prime windows: universal-energy firewall and original-source resonance

**Date:** 2026-11-01 (NY). **Research-only, paper derivations.** This dossier builds on Main XIX `81045770234a114247e43eb08ae5c6d446e9514a` and the *unmerged* selected-prime-phase PR #459 at `ec9c5a98772c60ab06bd4bb0a3d52a751a8bdc6a`. It preserves the original signed four poles, exact integer lift, and literal `U_0=0`. It neither proves pi normality nor asserts an all-horizon signed saving. Published number-theory results are imported with explicit hypotheses; new algebraic statements below have local finite controls but no Lean certificate or external referee.

Notation: `e(x)=exp(2*pi*i*x)`; `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`. Write `S_N(h)=sum_(1<=n<=N)e(hU_n)`. The BBP identity and summable positive Green tail establish `U_n=16^(n-1)*pi-T_n`, `sum T_n<infinity`. Thus `S_N(h)=sum e(h*16^(n-1)*pi)+O_h(1)` and Weyl's criterion identifies the condition `S_N(h)=o_h(N)` for all nonzero integer h with pi base-16 normality. The Green and BBP inputs are inherited, not reproved.

## PWI-01: Complete window = one exact 4:1 successor difference (PROVED PAPER)

Every prime `p=8k+5>5` has first birth at `a_p=(p+3)/8=k+1`, with coefficient `-1/p`, and first reuse at `J_p=(p+1)/2=4k+3`, by PR #459 SPP-01. Thus the complete newborn window is

`I_p={k+1,...,4k+2}`, `L_p=3k+2=(3p+1)/8`, and

`W_p(h)=sum_(n in I_p)e(hU_n)=S_(4k+2)(h)-S_k(h)`.

Within the entire interval, `U_n=-16^(n-a_p)/p+V_(p,n)`, where `V_(p,n)` has reduced denominator prime to p. The new `-1/p` occurs exclusively in the `f_4` edge of the authenticated exact decomposition

`r(n)=2 f_3(n)+f_4(n)+f_5(n)`, `f_m(n)=1/(8n-7)-1/(8n-7+m)`.

**Proof of edge exclusivity:** residues of four raw denominators modulo 8 are 1,4,5,6. For `p=5 mod8`, the first four multiples have residues 5,2,7,4. The first occurrence is the `8a_p-3=p` pole, with coefficient -1; 2p and 3p cannot appear in any raw pole. The first possible subsequent occurrence is 4p in `8J_p-4=4p`, just outside I_p. At the initial occurrence the `8n-3` denominator belongs precisely to `f_4`. Induction via `U_(n+1)=16U_n+r(n+1)` proves the stated phase split and p-integrality through `4k+2`.

## PWI-02: Prime-window smallness is a UNIVERSAL Cesaro criterion (PROVED PAPER; no source saving)

Let `z_1,z_2,...` be **any** complex sequence with `|z_n|<=1`, `A_N=sum_(n<=N)z_n`, and `W_p(z)=A_(4k+2)-A_k` for `p=8k+5>5` prime. Then

`A_N=o(N) <=> W_p(z)=o(p)` over *all* such primes.

Forward: subtraction of two `o(p)` prefixes. Reverse: by the classical prime number theorem in arithmetic progressions, for each fixed epsilon>0 and sufficiently large N there is a prime p=5 mod8 in `(2N,(2+epsilon)N)`. For its k, `k/N<=1/4+epsilon/8+o(1)` and `4k+2>=N` with `(4k+2-N)/N<=epsilon/2+o(1)`. Set `L=limsup_N|A_N|/N<=1`. Using `A_N=A_k+W_p(z)-(A_(4k+2)-A_N)` gives

`L<=(1/4+epsilon/8)L + epsilon/2`.

Let epsilon go to zero: `L<=L/4`, hence `L=0`. The argument uses only boundedness and PNT-AP; **it contains no arithmetic BBP interference**. Therefore prime-window reformulation by itself is not an easier proof of normality.

## PWI-03: Prime-mean-square criterion is universal too (PROVED PAPER)

Define `Q_z(X)=sum_(5<p<=X, p=5 mod8)|W_p(z)|^2`. For every bounded z as in PWI-02,

`A_N=o(N) <=> Q_z(X)=o(X^3/log X)`.

Forward: by PWI-02 `|W_p|=o(p)` uniformly as p tends to infinity; the classical PNT-AP and partial summation give `sum_(p<=X, p=5 mod8)p^2~X^3/(12 log X)`.

Reverse: fix epsilon,delta>0. Among primes `(2N,(2+epsilon)N)`, those with `|W_p|>=delta*p` number at most `Q_z((2+epsilon)N)/(4 delta^2 N^2)=o(N/log N)`. PNT-AP supplies `~epsilon*N/(4 log N)` primes in the interval, so at least one has `|W_p|<delta p`. Using the previous 4:1 dilation gives `L<=(1/4+epsilon/8)L+delta*(2+epsilon)+epsilon/2`. First let delta->0, then epsilon->0. Thus `L=0`.

The advertised log-power conjecture `Q_z(X)<< X^3/(log X)^(1+eta_h)` is a **strictly stronger quantitative sufficient target**, not a known consequence of qualitative normality. It has **not** been established for SUCC or pi.

## PWI-04: Exact kernel, Gram positivity, and coherent benchmark (PROVED PAPER)

For p=5 mod8 `p>5` put `v_p(n)=1_(a_p<=n<=b_p)` and

`K_X(n,m)=sum_(5<p<=X,p=5 mod8) v_p(n)v_p(m)`

`=#{p<=min(X,8*min(n,m)-3) : p>max(5,2*max(n,m)), p=5 mod8 prime}`.

Then `Q_z(X)=sum_(n,m) K_X(n,m)z_n*conjugate(z_m)` (only n,m<=floor((X-1)/2) contribute), and K is positive semidefinite as a sum of outer products `v_p v_p^*`. Positivity is a REPRESENTATION property and implies no strict upper bound. In particular `z_n=1` gives `W_p=L_p=(3p+1)/8`, and PNT-AP implies

`Q_1(X) ~ (9/64)*(X^3/(12 log X)) = (3/256)*X^3/log X`.

This is a rigorous **coherent-fake benchmark**, not a claim that SUCC attains it. For every p,q in `[P,2P]`, their intervals share at least the integer core between `ceil((2P+3)/8)` and `floor((P-1)/2)`, of length `P/4+O(1)`. At each such n the two authenticated factorizations give the SAME selected `e(hU_n)`. Averaging their p-primary phases as if they were independent witnesses ignores this exact common source.

## PWI-05: Odd clock, half-period, and isolated-clock saving (PAPER + classical BGK)

For p=8k+5 set `d_p=ord_p(16)` and `t_p=(p-1)/(4d_p)`. Since `16=2^4` and `(p-1)/4=2k+1` is odd, d and t are odd positive integers. The complete birth-window length decomposes EXACTLY as

`L_p=((3t_p-1)/2)*d_p+(d_p+1)/2`.

This is a whole number of full prime-clock periods plus exactly `(d_p+1)/2` extra terms. For any fixed `0<gamma<1/2`, the primes p<=X with d_p<p^gamma are `o(X/log X)`: every such p divides `M_X=prod_(j<=X^gamma)(16^j-1)`, whose log is `O(X^(2gamma))`; for p>sqrt X, each contributes at least `(1/2)log X` to the distinct prime divisors of M_X, while p<=sqrt X are `O(sqrt X)`. This proves the density-zero bound using only elementary divisibility + PNT-AP for the denominator class.

The classical Bourgain-Glibichuk-Konyagin subgroup exponential-sum theorem (see Kowalski, *Exponential Sums over Small Subgroups, Revisited*, Theorem 1.1) says: for every gamma>0 there is nu(gamma)>0 with `|sum_(x in H)e(ax/p)| <<_gamma |H|p^(-nu)` whenever `H <= F_p^*` is a multiplicative subgroup of size at least p^gamma and `a mod p !=0`. For fixed nonzero integer h and all but density-zero primes of the required class, the full periods obey this bound. The remaining half-period is bounded only trivially. Therefore the **isolated** clock

`C_p(h)=sum_(j=0)^(L_p-1)e(-h*16^j/p)`

satisfies

`|C_p(h)|/L_p <<_gamma p^(-nu) + (d_p+1)/(3*t_p*d_p+1) <= 1/3+o_h(1)`

outside an exceptional set of `o(X/log X)` primes <=X. The implicit constant depends only on gamma. This is genuine partial prime-only saving, but does NOT control the full sum when the p-integral cofactor is restored. It cannot be silently upgraded into a weighted BGK bound.

## PWI-06: Exact cross-prime gauge and admissible cofactor spoof (PROVED PAPER)

On I_p the true phase factors `e(-h16^(n-a_p)/p)*e(hV_(p,n))=e(hU_n)` **pointwise**. If p,q windows overlap, the p and q factorizations have exactly the same product on every shared integer n. They supply no independently sampled real-circle state. The cofactor's residue classes alone do not constrain its real phase: let q=p+1 and choose at each j `v_j=round(q*(16^j modp)/p)/q`. These rationals have denominators prime to p and satisfy `|v_j-(16^j modp)/p|<=1/(2q)`. Hence the phasors `e(-16^j/p)*e(v_j)` are each within `pi/q` of 1. Their full sum has normalized modulus at least `1-pi/q`, even if the isolated clock cancels. This deliberately spoofed v_j **does not** satisfy the BBP source/cofactor recurrence and is not an authentic SUCC trajectory.

## PWI-07: Independent exact FINITE intervals, not asymptotics

`interval.py` constructs original zero-seeded states with `Fraction` recurrence; its `combined_source(n)` polynomial check is performed independently of the four raw poles. Machin's `pi=16atan(1/5)-4atan(1/239)` is enclosed by alternating rational series. Each `hU_n mod1` is reduced EXACTLY before a 32-bit dyadic-floor approximation. The complex phase at that dyadic grid uses rational cosine through degree 24 and sine through degree 25 with Lagrange derivative bounds, explicit pi-width and dyadic-floor errors; an outward upper L1 bound is rounded to denominator 10^9. Every reported bound is a true strict inequality on the actual finite sum, not a float sign.

For each of p=269,373,397,509,997 and h=1,3,5 (15 exploratory-selected cases, **not blind holdouts**), **all** certified `|W_p(h)|/L_p < 1/4`. For 14 of 15 cases the stronger `<1/8` holds; the exception is (p,h)=(397,1), whose L1 upper is 0.152986179. All three h at p=997 certify `<1/16`. The strict comparisons are recalculated on every test run. **Two opposite-direction finite source/cofactor claims are also rigorously certified** by rational real-component lower bounds versus outward L1 upper bounds: for `(p,h)=(373,1)`, the actual full source has strictly LARGER modulus than the isolated primary clock (certified gap > `5287967/500000000` in the lower-component/upper-L1 comparison); for `(397,3)`, the full source has strictly SMALLER modulus (gap > `357809941/1000000000`). This decisively refutes monotone cofactor improvement in either direction without invoking floating-point signs. A **separate preregistered finite check** uses the first two primes above 997 congruent 5 modulo 8, namely 1013 and 1021, at h=1,3,5, with all six predicted L1 upper bounds <1/4, before phase evaluation. All six subsequently passed rigorous rational-interval tests. After observing their signs, two additional strict comparisons were certified with squared-norm intervals: `(1013,1)` has full-source amplitude smaller than primary only, whereas `(1021,5)` has full-source amplitude larger than primary only. These directions were not preregistered predictions. **Preregistration does not constitute an independent external witness**, and neither set of 21 finite outcomes establishes an infinite-limit estimate. The script makes no claim about all primes, untested harmonics, a rate, or any infinite limit.

## PWI-08: Exact open gate and research conclusion

The prime-source target remains the source-selected genuine **mixed** inequality for every fixed h!=0, e.g.

`Q_h(X)=sum_(p<=X,p=5 mod8)|sum_(n in I_p)e(-h16^(n-a_p)/p)e(hV_(p,n))|^2 = o_h(X^3/log X)`.

The suggested stronger `O_h(X^3/(log X)^(1+eta_h))` is separately conjectural. Both are **OPEN**. The exact window family and its Gram/K arithmetic do not pay this debt. Any breakthrough must exploit a new source-specific restriction on the signed cross-correlations, and must reject the coherent irrational same-source counterseed `s=-pi/16`, the p-free spoof, the pairwise-Haar/triple-lock control, and the period-four p=257 outside this residue class. No RH, Weil positivity, quantum effect or general base-normality follows from the established steps.

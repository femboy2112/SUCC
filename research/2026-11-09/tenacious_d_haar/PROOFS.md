# Operation Tenacious D — High-road Haar × low-road signed SUCC wavelets

Research date: 2026-11-09. Parent: main at 43a607818907120d4cdab73d240f5b4d7700b63f. Additive branch: research/tenaciousd-haar-successor-junction-2026-11-09. This does **not** prove base-16 normality of pi, its source-selected signed Weyl estimate, or RH. All three remain OPEN.

Prior SUCC contributions: #559 (primitive Fourier/word-energy), #565 (conditional Haar projection and sharp interval Wasserstein inequality), #568 (matrix of future-tail measures), #544 (chronological carry observer), #554 (balanced prime tomography), #562 (full-CRT real carry), #563 (source slip), #564 (moving-boundary/critical resolution). The classical DFT, Haar multiresolution, Fourier duality, de Bruijn graph and Wasserstein facts are not claimed as new globally.

## 0. The exact shared carrier and two noninterchangeable successors

Let b=16 and T(x)={16x} on the interval circle with half-open radix cylinders I_w, where w is a word of j hexadecimal digits. For a probability measure mu, define p_j(w)=mu(I_w), and q_j(w)=(T_*mu)(I_w). Let a length-(j+1) word e=(a_1,...,a_(j+1)) be an oriented de Bruijn edge, with source s(e)=(a_1,...,a_j) and target t(e)=(a_2,...,a_(j+1)). A length-zero word is the empty vertex.

The *child-label* successor S_16 sends a→a+1 modulo 16 inside any parent word cell. This is distinct from the chronological successor n→n+1 on sample times. The first gives a useful rank-15 signed Haar-detail frame. The latter, by itself, only telescopes and yields no normality theorem.

Define two signed edge currents:

~~~text
HIGH / future conditioned:
H_j(e) = p_(j+1)(e) - q_j(t(e))/16

LOW / past conditioned:
L_j(e) = p_(j+1)(e) - p_j(s(e))/16

WORD COLLISION ENERGY:
E_j = 16^j sum_(|w|=j) p_j(w)^2 - 1,  E_0=0.
~~~

These equations apply to any measure; in particular, no independence or random digit assumptions are needed.

## TDH-01 — The actual Yoneda/Haar junction is an oriented gradient (PROVED)

Subtracting directly gives for every edge

~~~text
H_j(e)-L_j(e) = [p_j(s(e)) - q_j(t(e))]/16.         (J1)
~~~

For a T-invariant law, q_j=p_j and this is exactly (d p_j)(e)/16, where d f(e)=f(s(e))-f(t(e)) is the oriented de Bruijn differential. A pair of observations, together with its source and target relations, has an intrinsic signed difference. This is the operational common basis; it is NOT a freely declared quantum phase.

For the actual length-N empirical T-orbit, mu_(A,N)=N^-1 sum_(n=A)^(A+N-1) delta_(T^n alpha),

~~~text
T_*mu_(A,N)-mu_(A,N)
  = [delta_(T^(A+N) alpha)-delta_(T^A alpha)]/N.   (J2)
~~~

Thus ||p_j-q_j||_1<=2/N for any j. This is an exact endpoint cost for applying the stationary gradient intuition to a finite original BBP orbit.

## TDH-02 — Two equal Haar energies and a paid finite endpoint (PROVED)

Expanding the squares over edges and collecting the source/target marginals yields

~~~text
K_low = 16^(j+1) sum_e L_j(e)^2 = E_(j+1)-E_j

K_high = 16^(j+1) sum_e H_j(e)^2
       = K_low + 16^j[sum_w p_j(w)^2 - sum_w q_j(w)^2]. (J3)
~~~

For a T-stationary process they agree exactly. On an empirical orbit, the difference of second moments obeys

~~~text
|K_high-K_low| <= 4 * 16^j/N,                     (J4)
~~~

using ||p_j-q_j||_1<=2/N and p_j(w)+q_j(w)<=2.

Define the common and gradient currents M=(H+L)/2, G=(H-L)/2. Polarization gives

~~~text
16^(j+1)<M,G> = (K_high-K_low)/4

(K_high+K_low)/2 = 16^(j+1)(||M||_2^2+||G||_2^2).
~~~

At stationarity, M and G are orthogonal. For the finite empirical orbit, the *scaled* cross-term has magnitude <=16^j/N; the raw unscaled sum has magnitude <=1/(16N). This is an actual oriented phase/inner-product statement, not an inference from equal scalar magnitudes.

Neither orthogonality nor a vanishing seam forces M=0. In particular, the period-16 and order-two de Bruijn controls below have a zero seam at a depth where their common wavelet current has nonzero energy.

## TDH-03 — Young Nastyman's signed Fourier pins (PROVED)

Let zeta=exp(2*pi*i/16). For each future j-word w, and h=1,...,15 define

~~~text
F_(h,w)=sum_(a=0)^15 zeta^(h*a) p_(j+1)(a,w)
       = average[ zeta^(h*d_n) 1_(future j-word=w) ].
~~~

The subtracted q_j(w)/16 term cancels under each nontrivial character. Finite Plancherel on the 16-child fibre gives

~~~text
K_high = 16^j sum_(|w|=j) sum_(h=1)^15 |F_(h,w)|^2. (J5)
~~~

This recovers the future-conditioned first-digit Fourier pin of #565 in the SAME oriented edge space as Wonderboy's last-digit Haar details. It proves an algebraic positive-sum/signed-current identity, NOT the decay of any pin on the authentic original zero seed.

## TDH-04 — Wonderboy's signed unit successor controls ALL 15 Haar detail directions (PROVED, sharp)

Within any parent prefix w, set v_a=p_(j+1)(w,a)-p_j(w)/16. Then sum_a v_a=0. The digit-label successor difference is (I-S_16)v, with entries v_a-v_(a-1) cyclically. Define

~~~text
J_j = 16^(j+1) sum_(|w|=j) sum_(a=0)^15
                  [p_(j+1)(w,a)-p_(j+1)(w,a-1)]^2.
~~~

Its exact finite Fourier multiplier is 1-zeta^(-h). On the zero-mean 15-dimensional child space, the multiplier's squared moduli have minimum 4sin^2(pi/16) and maximum 4. Thus

~~~text
[2-sqrt(2+sqrt(2))] [E_(j+1)-E_j]
  <= J_j <= 4[E_(j+1)-E_j].                       (J6)
~~~

Both constants are sharp on positive probability laws (small real Fourier h=1 and h=8 perturbations of uniformity). The 16 cyclic adjacent differences form a redundant complete frame on the 15 Haar-detail directions, not 16 independent orthonormal Haar wavelets. For exact rational computer certificates, 2-sqrt(2+sqrt(2)) > 3/20; e.g. sqrt(2)<569/400 makes sqrt(2+sqrt(2))<37/20. The module tests 20*J_j >= 3*(E_(j+1)-E_j) without floating-point assumptions.

## TDH-05 — The two roads CONNECT in a quantitative Haar-measure theorem (PROVED, premise still open for pi)

#565 RHY-02 proves, using the fixed hexadecimal interval chart,

~~~text
W1(mu,Haar) <= (16/15)W1(mu,Qmu)
                    + (1/15)W1(mu,T_*mu),        (J7)
~~~

where Q=C T_* uniformly randomizes the first digit but preserves the genuine future tail. On each length-(j+1) cylinder, mu and Qmu differ by H_j(e). Couple their common mass within a cell at cost at most 16^-(j+1), and transport unmatched mass at cost at most the total variation. Cauchy-Schwarz gives

~~~text
W1(mu,Qmu) <= 16^-(j+1)+1/2 sum_e |H_j(e)|
            <= 16^-(j+1)+1/2 sqrt(K_high).        (J8)
~~~

For a completed *actual* T-orbit, W1(mu_(A,N),T_*mu_(A,N))<=1/N. Combine J4,J6,J7,J8:

~~~text
W1(mu_(A,N),Haar) <= (16/15) [
      (1/2) sqrt(J_j/[4sin^2(pi/16)]+4*16^j/N)
      +16^-(j+1)] + 1/(15N).                    (J9)
~~~

This is a **real** high-road/low-road connection, with all finite-depth and endpoint costs displayed. The code uses the rigorous slightly weaker J_j*(20/3) instead of division by the radical gap and an outward *rational* integer-isqrt upper bound.

Sufficient but UNVERIFIED for pi: if for all sufficiently large N an original-zero source word depth j(N) tends to infinity with 16^j(N)/N→0 and the signed successor energy J_(j(N))→0, then J9 yields W1(mu_N,Haar)→0 and base-16 normality. It is a demanding moving-depth condition (not necessary at arbitrary prescribed schedules), not a source-derived bound. An analogous all-epoch condition suffices.

## TDH-06 — Hostile controls and the distinction between the two successors

1. Periodic hexadecimal 0123456789ABCDEF: E_1=0 and J_0=0, but E_2-E_1=15. At j=1 the graph seam vanishes and common Haar energy remains 15. Thus one-digit Haar and zero gradient are insufficient.

2. Periodic de Bruijn(16,2): E_1=E_2=0 and the first two adjacent-successor energies vanish, yet E_3-E_2=15. The next common signed current survives with zero gradient. Uniform first- and second-word counts are insufficient.

3. Constant-zero orbit: a coherent, maximally nonnormal T-orbit with large Haar detail and successor energy; it is detected.

4. Original four-pole forcing and dyadic wrong seed: let alpha_N=sum_(k=1)^N 16^(-k)r(k), N=2A+16, M=8A+96, and s_A=-floor(2^M alpha_N)/2^M. This is a rational power-of-two counterseed, not U0=0. The same source recurrence satisfies U_n(s_A)+T_n=16^n(s_A+pi/16), and its exactly bounded truncation shadows the fixed point 0 on [A,2A). At A=64 with 105-term positive rational tail bounds, all 68 tested digits (including lookahead) are certified 0. A source-only theorem claiming all initial seeds are Haar is refuted.

5. Pure chronological signed difference is VACUOUS: for any bounded scalar f_n,

~~~text
(1/N)sum_(n=A)^(A+N-1) (f_n-f_(n+1))
  = (f_A-f_(A+N))/N = O(1/N)
~~~

even for a nonnormal constant sequence. Do not confuse this with the child-digit successor frame J_j.

## TDH-07 — Microscopic source resolution vs finite-sample budget (PROVED no-go)

There are at most N occupied word cells at depth k for an N-start sample. Thus by Cauchy-Schwarz,

~~~text
E_k = 16^k sum_w p_k(w)^2-1 >= 16^k/N-1.          (J10)
~~~

Summing the nonnegative successor lower bounds J6 over j=0,...,k-1 gives

~~~text
sum_(j<k) J_j >= [4sin^2(pi/16)] E_k
                       >= [4sin^2(pi/16)](16^k/N-1). (J11)
~~~

The actual four-pole forcing r(n) is Theta(A^-2) on [A,2A). A direct all-cylinder histogram resolving a cell width 16^-k comparable to A^-2 would need about A² cells while only N=A observations are present: hence E_k>=A-1. No argument can require all source-microscopic cell energies to vanish at this sample size, even if the number is normal. This is a no-go only for the naive full-grid L2 strategy, **not** for selective signed oscillators, arithmetic correlations, or a proof of equidistribution at fixed scales. It is consistent with #564's independently derived A² source-twist resolution warning.

## TDH-08 — Authentic source finite witnesses (OBSERVED-FINITE only)

The code imports canonical duck_bbp.forcing and tail_interval from main; it does not mutate the four signed poles or U0=0. It certifies each real hexadecimal digit only if the entire outward rational interval [U_n+T_n^-,U_n+T_n^+] lies in a single digit cell. Classical BBP is an explicit imported source identity, not derived from these finite numerical checks.

At original-zero epochs (A,N)=(16,64) and (32,128):

| A,N | W1 to Haar (midpoint) | W1 to Qmu (midpoint) | j=0: delta-E,J | j=1: delta-E,J |
|---|---:|---:|---|---|
| 16,64 | ~0.092408362 | ~0.086941975 | 0.34375,0.4140625 | 4.40625,9.25 |
| 32,128 | ~0.014698838 | ~0.014547587 | 0.05859375,0.138671875 | 2.00390625,4.28125 |

The respective certified midpoint-radius bounds are below 3.45e-20 and 1.41e-20; the W1 checks pay the radius by triangle inequality. At (32,128), E_3=32, the finite occupancy lower bound is E_3>=31, and J_2=63. These are finite diagnostics, **not evidence of an all-N decay rate**.

## Remaining gate and strongest next probe

Start with the signed h=8 parity pin, at future depth j=0:

~~~text
(1/A) sum_(n=A)^(2A-1) (-1)^(d_n) -> 0
~~~

for authentic U0=0. No such all-epoch bound follows from the formulas here. Then progress to h=1..15, future words, and growing j. The source-specific instrument must retain real carries, all-prime CRT winding, the original four source births, and the complementary signed phase from #544/#554/#562/#563. It must reject the coherent dyadic shadow, periodic aliases, and matched-source mutants, and pay boundary costs. Prove an inequality or explicitly falsify an intermediate hypothesis; do not present a new equivalent characterization as a normality proof.

**Truth ledger:** TDH-01..07 disclosed on the stated mathematical domain; source finite tests observed only; π signed energy decay OPEN; time-coboundary and zero-seam shortcuts REFUTED. No independent referee, all-global mathematical novelty claim, or new Lean kernel theorem is asserted.

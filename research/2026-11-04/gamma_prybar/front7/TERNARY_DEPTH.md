# The original selected ternary pole, and what its exact height leaves unresolved

## T1. A uniformly deep pole in the actual zero-seeded state

Write d3(x)=3^max(0,−v3(x)) for the ternary factor of the *reduced* denominator of a rational x, with d3(0)=1. For every n≥11 let q=3^a, q≤8n<3q. Then a≥4 and

    q/9 ≤ d3(U_n) ≤ q,     d3(U_n) > 8n/27.

For every even a, d3(U_n)=q throughout the entire shell. The following exact table resolves every n for odd a as well. These statements concern the accumulated genuine state, not the local injection denominator.

**Proof.** The modulus is 27 in Z_(3); all units invert there. The authentic expansion is

    h = q 16^(−n) U_n = sum_(j=1)^n sum_(e,c) 16^(−j)c q/(8j−e),
    (e,c)=(7,4),(4,−2),(3,−1),(2,−1).

Every raw denominator lies below 3q. Terms with raw denominator not divisible by q/9 vanish modulo 27. Write a surviving raw denominator as l q/9 with 1≤l≤26, and admit it precisely when its residue modulo 8 is 1,4,5 or 6. These residues give (e,c) as above in that order. It enters at j=(l q/9+e)/8. Its increment to h is 16^(−j)·9c/l modulo 27, with cancellation of powers of three before taking the modular inverse. The possible l depend only on the parity of a since q/9 is a power of 3 and 3²=1 modulo 8. Also q/9 is divisible by 9, and j=e/8 modulo 9. As 16^9=1 modulo 27, the exact increment likewise depends only on l and that parity.

At the first n in the shell, n=ceil(q/8), exactly the admissible l≤9 have entered. Indeed q/9≥9, and for l≤8 the largest raw denominator plus e is below q. If l=9 is admissible, q≡1 mod 8 and the pole enters exactly at the first point of the shell. No l≥10 can have entered since 10q/9≥q+9. The remaining entries are ordered by l, as e ranges between 2 and 7. The residue table below gives the initial h followed by (l,h after entry); omit entries whose j exceeds n.

| a parity | Initial h | Later (l,h) |
| --- | ---: | --- |
| even | 13 | (12,16), (13,7), (14,16), (17,7), (20,25), (21,13), (22,4), (25,13) |
| odd | 12 | (10,3), (11,21), (12,24), (15,18), (18,25), (19,7), (20,25), (23,7), (26,16) |

Each table entry is given by the displayed sum with at most 26 terms, a finite paper certificate reproduced by ternary_depth_probe.py. No entry is zero modulo 27, and all even-shell entries are units. Thus v3(h)≤2, giving d3(U_n)=q/3^v3(h) and the conclusions. The multiplication by 16^(−n) is a ternary unit. Finite prefixes and the literal seed are included in the table via the expansion starting at j=1. This resolves the authentic 3-height for all n in its stated range. It gives no real signed cancellation.

## T2. Exact heights and almost the entire local address still permit concentration

S1 in SPARSE_CONTROLS.md can be strengthened to match d=den(U_n) **exactly at every n** and to preserve the complete principal parts for all p≠3. It can also restrict the discrepancy at 3 to a polylogarithmic denominator, so all but O(log log n) of the authentic polar ternary digits (counting from the most singular end) agree. Yet J_(A,q_A)/q_A→1. This is one altered zero-seeded recurrence.

Take any sufficiently large t_0≡2 mod 3; V=U until t_0. At t=t_i choose D_t the largest 3-power at most (log t)^4, and e_t=−round(D_t(16V_(t−1)+r(t)))/D_t. Next set t_(i+1)=t+3 max(1,floor(log_16(log t)/3)); e_n=0 elsewhere. Thus 16^(t_next−t)≤16³ log t and the number of reset indices is O(N/log log N). D_t≤Q_(t−1)'s ternary factor by the lower bound for original denominators or T1 itself at t−1. Prefix forcing LCM is therefore preserved. All changes occur away from the designated prime births. The error V_n−U_n lies in the ternary grid with denominator at most D_t for t≤n<t_next, by induction and monotonicity of D_t. For large t, D_t<8t/27<d3(U_n), so adding this error leaves the original ternary denominator unchanged everywhere. At every other prime, the whole principal part agrees. This proves exact reduced-denominator equality. The numerator difference in coordinates on the original ternary component, normalized to the true 3-height 3^k, vanishes mod 3^(k−log_3 D_t). Consequently only the least singular O(log log n) polar digit positions can differ. At n<t_0 everything agrees by initialization.

After a reset |V_t|≤1/(2D_t)=O((log t)^(-4)). Between resets the unwrapped value is bounded by 16^(n−t)(|V_t|+O(t^-2))=O((log n)^(-3)). Thus q_A ||V_n||→0 uniformly in the epoch, yielding J/q_A→1. This version sacrifices equality of the authentic 3-principal part and still changes the forcing at some nonbirth indices. Both are detectable. It does not preserve the genuine chronology of integer numerators/carries. There is no proof here of a saving for the authentic orbit. The large initial calibration can be accommodated by an integer drift if desired; it is unnecessary for the stated result.

**Source and authority.** T1 uses only the original signed four fractions, U_0=0 and arithmetic modulo 27. T2 uses T1, the same positive source decay and elementary rounding. The finite receipt uses direct Fraction and independently derived integer recurrences for residue validation. Earlier SUCC treatments of 3-adic poles in the *forcing* (October 31 three-place difference resolvent) are related but solve a different local problem. No claim of priority or formal-kernel verification.

## T3. Uniform occupancy in the genuine ternary clock

For every sufficiently large integer A, every rational target y and every real D in [1,A], the genuine selected states satisfy

    #{ n in [A,2A) : d3(U_n−y) ≤ D } ≤ C (sqrt A + D)

with an absolute C. This is an upper occupancy bound for p-adic congruence cylinders; it does not assert a real-circle bound. In particular, at D=A/q_A it gives O(A/q_A) uniformly in y. At D=sqrt A only O(A^(3/2)) ordered epoch pairs have ternary denominator this small.

**Proof.** Take B the largest power of 3 at most 16A, so B>16A/3, and M the largest power of 3 at most min(sqrt A,B/D). Then BU_n is 3-integral throughout and its valuation is bounded by 3, since T1 gives B/d3(U_n)<54. (Here n≥A.) When d3(U_n−y)≤D, By is 3-integral and BU_n equals By modulo M; if By fails integrality there are no hits. At each ordinary step the twisted address B16^(−n)U_n modulo M changes only when some raw denominator is divisible by 3B/M. Such raw denominators in the epoch are among the multiples of 3B/M below 16A. Each raw number appears at most once as the four pole indices are distinct residue classes mod 8. Thus the epoch splits into at most O(1+M) runs of constant twisted address z. On each run, hitting the fixed residue By means 16^n z equals that residue mod M. For M>27, any nonempty hit set is contained in one residue class of times with period ord_(M/3^v3(z))(16)≥ M/81. Indeed v3(16^j−1)=1+v3(j), by binomial expansion for j prime to three and repeated cubing thereafter. Each run contributes at most 1+81 length/M. For smaller M the same upper bound on a run is immediate. Summation gives O(M+A/M)=O(sqrt A+D).

**Consequence for T2.** For every epoch and every ordered pair in it, the ternary discrepancy between the altered and genuine lag has denominator at most (log(2A))^4 for sufficiently large A. If d3(U_t−U_n)>sqrt A, this discrepancy cannot change its reduced ternary denominator. All other prime components agree even as principal parts. Therefore T2 preserves the exact reduced denominator of the actual two-time lag on all but O(A^(3/2)) ordered pairs, even while its real cloud concentrates. The exceptional pairs have normalized triangular weight O(q_A/sqrt A)=o(1). This gives a quantitative scale at which a good p-adic occupancy bound and a saturated real collision tent coexist. The structural proof uses T1, the authenticated recurrence, raw pole divisibilities and the multiplicative order at the single fixed prime 3.

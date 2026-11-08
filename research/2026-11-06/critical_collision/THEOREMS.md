# Operation CRITICAL COLLISION: BBP Fejér critical transport and source-selected signed gate

**2026-11-06 · additive child of PR #533 at 34d1c1f40b34f2dcf76283f307062069c87a579c. π base-16 normality, RH and the selected all-N collision estimate remain OPEN.** Original four signed poles, literal U0=0, archived contracts, formal Lean, workflow and main unchanged.

## Source, definitions (CC0)

r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)=(120n²−89n+16)/[(2n−1)(4n−1)(8n−7)(8n−3)]. U0=0; Un=16U(n−1)+r(n). x_n={Un}; beta=pi/16; z_n={16^n beta}. The authentic BBP gauge is Un+Tn=16^n beta, Tn=Σ_(j≥1)16^(−j)r(n+j), T0=pi/16.

For n≥2: D(n)−n²A(n)=392(n−2)^4+2201(n−2)^3+4494(n−2)^2+3902(n−2)+1185>0, so 0<r(n)<1/n². Thus 0<Tn<1/[15(n+1)²] for n≥1.

Define e(t)=exp(2pi i t), W_N^y(h)=N^-1 Σ_(n<N)e(h y_n), Fejér F_H(t)=1/(H+1)|Σ_(j=0)^H e(jt)|², and

    C_(N,H)(y)=N^-2 Σ_(n,m<N)F_H(y_n−y_m)
               =Σ_(|h|≤H)(1−|h|/(H+1))|W_N^y(h)|² ≥1.

Positivity is UNIVERSAL, not evidence for π.

## CC1 — CRITICAL SOURCE-TO-REAL HILBERT TRANSPORT, PROVED LOCAL

For every N≥1 and H≥1:

    |sqrt(C_(N,H)(z))−sqrt(C_(N,H)(x))| ≤ 4 sqrt(H(H+1))/N.

Proof: |e(hTn)−1|≤min(2,2pi|h|Tn). For n=0 use ≤2; for n≥1 use Tn<1/(15n²) and the elementary decreasing-integral bound Σ_(n≥1)min(2,A/n²)≤∫_0∞min(2,A/t²)dt=2sqrt(2A). Thus, for nonzero integer h,

    |W_N^z(h)−W_N^x(h)| ≤[2+4sqrt(pi|h|/15)]/N < 4sqrt(|h|)/N,

because pi<15/4. Apply the reverse triangle inequality to the weighted Fourier ℓ² norm sqrt(C), then sum 2Σ_(h=1)^H h=H(H+1). QED.

**Important distinction:** parent #533 SE4 controlled the DIFFERENCE OF ENERGIES as O(H²/N), allowing unconditional o(1) transfer only for H=o(sqrt N). The present comparison is of SQUARE ROOTS. At H=N it is O(1), not o(1), but it transfers BOUNDEDNESS and o(log N) in both directions. Critical H=N is now admissible for a conditional normality criterion.

## CC2 — EXACT RATIONAL ORIGINAL SOURCE FINITE CAPS, CERTIFIED FINITE

For circular distance d=||t||, Fejér obeys F_H(0)=H+1, and when d>0,

    0≤F_H(t)≤min(H+1, 1/[4(H+1)d²]).

This follows from the geometric sum and sin(pi d)≥2d. Compute each original x_n as an exact Fraction from literal U0=0, compute every rational pair distance d exactly, and quantize EACH upper bound UP to the next multiple of 10^-6. If a_nm is the preceding analytic upper bound, then

    Q_(N,H) = 10^6 N(H+1)+2 Σ_(0≤m<n<N)ceil(10^6 a_nm)

is an integer giving the rigorous upper bound C_(N,H)(x)≤Q_(N,H)/(10^6 N²), with NO floating trigonometry.

At the critical H=N, exact arithmetic gives:

- N=128: C≤46444121280/16384000000<3.
- N=256: C≤190901485994/65536000000<3.
- N=512: C≤769526344650/262144000000<3.

The N=256,512 exact tests were explored after initial preregistration, not blind holdouts. The last ratio is approximately 2.9355100428. Neither the all-N assertion C<3, nor even infinitely many such N, has been proved. The finite integers are reproducible with the exact rational script supplied in this PR.

## CC3 — EXPLICIT ORIGINAL SOURCE FREQUENCY-RAY INEQUALITY, PROVED LOCAL

Because e(hU(n+1))=e(16hUn)e(hr(n+1)), the initial source term r1=47/15, later bound r(n)<1/n², and endpoint shift imply

    |W_N^x(16h)−W_N^x(h)| ≤[4+4sqrt(pi|h|)]/N, h≠0.

For N≥2|h| let J=floor(log_16(N/(2|h|))). Iterate across frequencies h,16h,...,16^J h, use pi<4 and 4^J sqrt(|h|)≤sqrt(N/2). Every coefficient differs from W_N(h) by at most 4J/N+8/[3sqrt(2N)]. All ray frequencies satisfy |16^j h|≤N/2, so their ± Fejér Fourier weights sum to at least 1. Hence

    |W_N^x(h)| ≤ sqrt[(C_(N,N)(x)−1)/(J+1)]
                   +4J/N+8/[3sqrt(2N)].                      (CC3)

The exact N=512 cap yields |W_512^x(1)|<0.902184. This is a RIGOROUS FINITE source-specific Fourier upper bound, not an asymptotic. A genuine uniform C_(N,N)(x)=O(1) would give W_N^x(h)=O_h((log N)^-1/2), and Tn→0 would imply base-16 π normality. The uniform collision premise is OPEN.

## CC4 — INTEGER PAIR-COUNT GATE, PROVED CONDITIONAL; SOURCE PREMISE OPEN

Let A_N(delta)=#{0≤n,m<N: ||x_n−x_m||≤delta}, including the diagonal. Suppose for every sufficiently large N and ALL delta in [1/(N+1),1/2],

    A_N(delta) ≤ N + K N² delta                                (OPEN).

Then for every H≤N, split distances into central d≤1/(H+1) and dyadic annuli (2^j/(H+1),2^(j+1)/(H+1)]. The Fejér majorant yields central contribution ≤(H+1)/N+K, and annulus j ≤ (H+1)/(4·4^j)[1/N+K·2^(j+1)/(H+1)]. Since Σ4^-j=4/3 and Σ2^-j=2,

    C_(N,H)(x) ≤2K+4(H+1)/(3N).                              (CC4)

Thus the OPEN source-specific count would prove π normality at H=N by CC3. Observed EXACT pair counts for delta=1/N: N128→356, N256→742, N512→1466, versus much larger periodic and 2-adic-isometric-shadow controls. No all-horizon K has been established.

Exact original source lag reduction identifies the missing arithmetic theorem, for every sufficiently large N and delta≥1/(N+1):

    Σ_(d=1)^(N−1) #{0≤n<N−d: ||(16^d−1)Un+S_d(n)||≤delta}
                                  ≤(K/2) N² delta;          (OPEN)
    S_d(n)=Σ_(j=1)^d16^(d−j)r(n+j).

This is the genuine all-lag original-carry / odd-denominator shrinking-target estimate, not a reformulated finite certificate.

## CC5 — DENSE CHECKPOINT GLUING, PROVED CONDITIONAL

It is enough to prove caps C_(N_k,N_k)(x)≤C (or o(log N_k)) along N_k→∞ with RELATIVE gaps N_(k+1)/N_k→1. CC3 forces Weyl coefficients to vanish at checkpoints. Between checkpoints, universal |W_M(h)−W_(N_k)(h)|≤2(M−N_k)/M→0. Then original π orbit is normal. The existing N=128,256,512 double each time and DO NOT constitute such a dense unbounded family.

## CC6 — EXACT OPERATIONAL REAL↔2-ADIC CLOCK DFT, PROVED LOCAL IDENTITY; FINITE FLOAT PROBE

Q=2^k, σ_Q(n)=V(n) modQ for original 2-adic source is an EXACT clock permutation. Reindex the real F_n=e(hUn) as G_(σ_Q(n))=F_n, and set M_j=Q^-1Σ_r G_r e(−jr/Q). Parseval Σ_j|M_j|²=1 and M0=W_Q(h). The original next-bit replica gives σ_Q(n+Q/2)=σ_Q(n)+Q/2 modQ, hence the exact odd-band projection:

    Σ_(j odd)|M_j|² = (1/(2Q)) Σ_(n<Q/2)|F_n−F_(n+Q/2)|².  (CC6)

This declares a COMMON CLOCK BASIS, not a false identity of real and 2-adic phase. It holds for the isometric rational shadow as well; no all-N spectral lower bound follows. Finite h=1 odd-band float values Q64/128/256: original 0.486259/0.503242/0.564645 versus H-shadow 0.000196/0.000098/0.000049; exact modular permutation and independent real pair-sum identity checked. No asymptotic claim.

## CC7 — HOSTILE CONTROLS AND HONEST LIMIT

The same original forcing with wrong real seed s=−pi/16 yields completed zero orbit and growing collision energy, without changing source-only Gamma/harmonic/silver moments. The zero-seeded rational shadow H(n)=n/(2n−1)^4 is a 2-adic isometry yet its real phases converge to zero and critical collision energy grows ∼N. Neither a source-only moment nor exact 2-adic bit flip proves real mixing.

Even an **optimal finite irrationality exponent is insufficient**: the Kempner-type β*=Σ_(j≥0)16^(−2^j) is nonnormal (zero-digit density one) and known to have irrationality exponent 2. Along N=2^k, roughly N/2 consecutive orbit phases lie within 1/[8(N+1)] of zero. There F_N(t)≥4(N+1)/pi² for each pair, so its C_(N,N)≫N. Choosing s=β*−pi/16 in the original four-pole forcing reproduces that real nonnormal control, but violates literal U0=0. Metric Poissonian pair correlation for almost every lacunary seed does not cover the selected π seed. The uniform microscopic collision criterion may be stronger than normality.

**Ledger:** CC0,CC1,CC3,CC4 implication,CC5 implication,CC6 identity PROVED LOCAL; CC2 CERTIFIED FINITE; numerical spectral tests OBSERVED FINITE; selected CC4-OPEN and lag sum, π normality, RH UNVERIFIED/OPEN. No theorem of π normality, conjectural RH spectral equivalence, external priority or formal Lean receipt is asserted.

Literature: Bailey–Crandall (2001) DOI 10.1080/10586458.2001.10504441; Lagarias (2001) DOI 10.1080/10586458.2001.10504456; Rudnick–Technau lacunary pair correlations arXiv:2001.08820; Kempner irrationality exponent 2 via continued fractions DOI 10.1007/s00605-018-1244-1.

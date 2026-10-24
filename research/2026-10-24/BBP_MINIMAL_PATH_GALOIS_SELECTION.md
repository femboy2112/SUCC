# OPERATION MINIMAL PATH — Four-pole BBP source, infinite arithmetic births, selected Galois interference

2026-10-24. RESEARCH ONLY. Parent: draft SUCC PR #258 at 9aa55b3a6e1150d1690612c740a38e86adc081db, which includes corrected source #252, Green source #254 and first-birth branch #256 at its EARLIER ac3db0e head. The newer #256 Witt branch head 0683f8f adds filtered p^2 research that is reviewed here but not imported. Siblings #253, #255, #257 are likewise not silently merged. No main changes, archives, release, new Lean theorem, RH theorem or pi normality proof. Academic novelty UNVERIFIED.

The motivator "nature's most stupidly clever minimal path" is treated as a TESTABLE mathematical frame, not an empirical axiom: a short lawful generative description can create arbitrarily many distinguishable arithmetic modes. Distinguish a program's length, its homogeneous recurrence order, Hankel realization rank, prime-local history support and Weyl cancellation. They are NOT the same notion of complexity.

SOURCE: r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), y0=0, y_n={16y_(n-1)+r(n)}, T_n=sum_(k>=1)16^(-k)r(n+k), 16T_n=r(n+1)+T_(n+1), T0=pi/16. All poles are forcing-index poles, NOT circle states. Positive Hausdorff/Hankel Green structure was proved in #252.

## MP-01 — exact first-prime birth census and asymptotic

Status: DISCLOSED, paper derivation from exact #256 first-birth law, independent finite denominator/valuation tests; PNT-AP is EXTERNAL mathematics.

For every odd rational prime p, its first authenticated valuation -1 forcing event n_p is:
p=1 mod8 -> (p+7)/8;
p=5 mod8 -> (p+3)/8;
p=3 or7 mod8 -> (p+1)/4.

At that time v_p(y_(n_p))=-1 and every earlier y_j is p-integral (zero allowed). Let pi(X;8,a) count primes <=X in class a modulo eight. The number B(N) of DISTINCT odd primes first born by time N is EXACTLY

    B(N)=pi(8N-7;8,1)+pi(8N-3;8,5)
        +pi(4N-1;8,3)+pi(4N-1;8,7).

All-N equality: solve n_p<=N separately in the four residue classes. PNT in fixed progressions implies B(N)~6N/log N. This counts first BIRTH events, not simultaneous surviving independent modes and not information-theoretic entropy. A fixed 4-pole source produces asymptotically almost-linear growth in arithmetic labels.

## MP-02 — ALL prime-power depths of the genuine FULL source

Status: DISCLOSED paper theorem for ALL odd p and fixed positive k, exact finite source scans and rational state valuations. It strengthens the recently observed p^2 FILTERED source result from the newer #256 head without identifying filtered impulses with the full source.

Let q=p^k, p any odd prime, k>=1. Then the FIRST forcing index containing a p^k-divisible denominator is

    n_(p,k)=(q+7)/8 when q=1 mod8,
            (q+3)/8 when q=5 mod8,
            (q+1)/4 when q=3 or7 mod8.

At this index the genuine FULL state y has v_p(y_(n_(p,k)))=-k; every preceding state has v_p>=1-k (including v_p(0)=+infinity).

PROOF: Allowed residues of source denominators 8n-a are 1,4,5,6 modulo8 for a=7,4,3,2. The first positive eligible multiple of q is q for residue1/5, or 2q for residue3/7; all earlier eligible multiples fail or have larger indices. Exactly one source term at the first event has valuation -k and p-unit numerator: 4/q, -1/q, or -1/(2q). All other same-index terms and prior source inputs have valuation >=1-k. SUCC multiplying by 16, a p-unit, cannot cancel a uniquely lower valuation. Thus the full y state jumps to depth -k.

Let H_k(N) count the odd primes whose depth-k event has appeared by time N, with k fixed first. If k is EVEN, q=p^k=1 mod8 for every odd p, hence H_k(N)=#{odd primes p: p^k<=8N-7}. If k is ODD, use the same four-class thresholds as MP-01 with p replaced by p^k.

PNT-AP gives for every fixed k:

    k even: H_k(N)~[k*8^(1/k)] N^(1/k)/log N,
    k odd : H_k(N)~[k*(8^(1/k)+4^(1/k))/2] N^(1/k)/log N.

In particular H_1~6N/log N; H_2~2*sqrt(8N)/log N. There are infinitely many layers, with progressively sparser first births. No uniform-in-k asymptotic or claim of permanent modes.

## MP-03 — MINIMAL rational-coefficient homogeneous recurrence depth is TWO

Status: DISCLOSED paper proof, exact rational interval recurrence checks. Uses the CLASSICAL theorem pi is irrational, not independently reproved.

From the authentic recurrence:

    T_n=16^(n-1)*pi - sum_(j=1)^n 16^(n-j)r(j)

is irrational for EVERY n>=0. Put R_n=r(n+2)/r(n+1), a strictly positive rational. Eliminating r gives

    T_(n+2)-(16+R_n)T_(n+1)+16R_n T_n=0.

Suppose T_(n+1)=c T_n at ANY n for rational c (including an arbitrarily time-dependent rational coefficient). Then (16-c)T_n=r(n+1)>0 rational. If c=16 the left side is zero; otherwise irrational. Contradiction. Thus the minimal HOMOGENEOUS rational linear recurrence order is precisely two. The INHOMOGENEOUS first-order recurrence is of course available and is not refuted. By the existing full-positive-spectrum result, the same tail has INFINITE time-HOMOGENEOUS Hankel rank. Finite description, minimal nonautonomous recurrence order and infinite moment rank genuinely coexist.

## MP-04 — minimal positive infinite-rank NONNORMAL counterfeit with all-prime births

Status: DISCLOSED, exact rational adversarial test.

Set T*_n=1/[(n+1)(n+2)]=integral_(0,1) u^n(1-u)du, with positive density on an interval and all-order positive Hankel rank. Put r*(n)=16/[n(n+1)]-1/[(n+1)(n+2)]>0 and y*_0=0, y*_n={16y*_(n-1)+r*(n)}. Its selected circle phase 16T*_0=8 is an integer, hence all selected radix-16 iterates equal zero. But y*_n={-T*_n} for n>=1, and for EVERY odd prime p, y*_(p-2) first acquires v_p=-1; all earlier fake states are p-integral. Thus infinitely many real rational SUCC prime births, strictly positive forcing and infinite moment rank coexist with a perfectly PERIODIC selected orbit. This is NOT the original BBP four-pole source. It kills the generic inference that minimality/rank/prime births force normality.

## MP-05 — full-source relative Galois trace and second moment (SOURCE-FAITHFUL)

Status: DISCLOSED paper identity and exact formal group-ring finite checks, independent numerical regression only for sanity.

Fix a prime p=8m+1, L=ord_p(16), Delta=3m, B=Delta/L, and a nonzero fixed integer h with p not dividing h. The exact first-birth source splits:

    y_(m+1+t)=4*16^t/p+w_t mod1, 0<=t<Delta,

where all w_t have rational denominators COPRIME to p. Put Q=lcm of those denominators, K_p=Q(zeta_Q). Since gcd(p,Q)=1, Gal(K_p(zeta_p)/K_p) is canonically (Z/pZ)^*; the Galois automorphism a sends zeta_p to zeta_p^a and FIXES all authentic complementary phases e(h w_t).

Define the genuinely conjugate FULL source window

    W_p(a;h)=sum_(t<Delta)e(4ha16^t/p)e(h w_t),

and source block amplitudes V_s=sum_(b=0)^(B-1)e(h w_(bL+s)), 0<=s<L. The p-phase exponents 4h16^s are distinct and nonzero. Character orthogonality gives EXACTLY

    [sum_(a!=0) W_p(a;h)]/(p-1)
         =-[sum_(s<L)V_s]/(p-1),

    [sum_(a!=0)|W_p(a;h)|²]/(p-1)
         =[p*sum_(s<L)|V_s|²-|sum_(s<L)V_s|²]/(p-1).

The first is a normalized relative cyclotomic field TRACE, the second full twisted Parseval/Ramanujan moment, NOT an untwisted-only Gauss sum. The complement is not resampled Haar: it is the exact p-free rational BBP source and is FIXED by the relative Galois group.

Since |V_s|<=B, the Galois RMS squared normalized by Delta² is <=p/[(p-1)L]. For rational epsilon>0, at most a proportion min(1,p/[(p-1)L epsilon²]) of the p-1 Galois embeddings have |W_p(a)|/Delta>=epsilon. Along the good family L>p^(1/3), almost all conjugates have cancellation. The PARTICULAR selected embedding a=1 need not be typical. Formal Q/Z group-ring coefficients verify this exact source-dependent identity without float pi: pairwise local Ramanujan coefficients agree with p times complete L-class convolution minus global complement convolution. The p-free conductor is checked, not presumed.

## MP-06 — actual BBP selected GALOIS OUTLIER at p=97

Status: finite rational interval result, NOT an asymptotic theorem. MUST validate exact-head workflow before promoting.

For p=97, m=12, L=12, Delta=36 and B=3. The selected authentic source squared norm is independently enclosed by exact rational BBP states, a classical Machin-arctangent rational pi interval, and outward rational Taylor cosine/sine bounds. The formal Galois second moment above has an independent upper enclosure using cosines of rational differences w_(bL+s)-w_(cL+s). These permit the strict claims

    |W_97(1;1)|²/36² >1/20
    and (1/96)sum_(a=1)^96 |W_97(a;1)|²/36² <1/40.

So the authentic selected a=1 embedding exceeds TWICE the Galois mean squared amplitude at this finite prime. It is already REFUTED that source-selected BBP is always <= its Galois RMS. This finite outlier is perfectly compatible with eventual cancellation; no asymptotic conclusion follows.

## MP-07 — even a one-dimensional p-free autonomous complement may resonate

Status: REFUTED naive "p-free + minimal recurrence => selected cancellation."

For any eligible p and finite Delta, parent #256 supplies an odd Q coprime to p and s integer so that x=4/p+s/Q has |x|<=1/(2Q). The unforced, 1D dynamics x_t={16^t x} retain the p-primary clock 4*16^t/p while the complement 16^t s/Q has p-free denominator and obeys one homogeneous law. Yet

    |sum_(t<Delta)e(16^t x)-Delta|
       <(22/7)*(16^Delta-1)/(15Q).

Thus by making Q huge, the selected Galois embedding can resonate arbitrarily strongly although almost all relative conjugates cancel. This counterfeit does NOT satisfy actual BBP r(n). It is a genuinely source-typed no-go for assuming that minimality, unforced SUCC, local p-freeness, or average cancellation imply the selected result.

## MP-08 — the next source-selected exceptional-amplification lemma

Status: CONDITIONAL sufficient theorem, premise UNVERIFIED.

Define M_p(h)=(p-1)^(-1)sum_(a!=0)|W_p(a;h)|². If M_p(h)>0, let A_p(h)=|W_p(1;h)|²/M_p(h), the exceptional selected-embedding amplification factor. This is neither a truth probability nor physical quantum coherence. By MP-05,

    |W_p(1;h)|²/Delta²
       <=A_p(h)*p/[(p-1)L_p].

Hence if for every fixed nonzero h the AUTHENTIC source satisfies A_p(h)=o(L_p) on the original good prime-window family, then W_p(h)=o(Delta), and by CBCW-05 the selected pi orbit is base-16 normal. This is a strictly stronger SUFFICIENT hypothesis in general, NOT a new normality equivalence. The p=97 finite certificate already proves A_97(1)>2, refuting any proposed universal A<=1.

The needed new theorem concerns exactly one authenticated cyclotomic embedding and its arithmetic source. Neither the unconditional Galois RMS, positive Hankel memory nor prime-power birth count supplies it. A held-out, source-certified p-window phase test and a hostile p-free near-resonant clock are its next meaningful falsifiers.

### MP-08a — Sharpness of the amplification threshold

The p-free one-rule resonant control of MP-07 gives, with rho=|W_p(1)|/Delta and Q chosen sufficiently large, rho>1-eps. The universal source-relative Galois RMS upper M_p/Delta²<=p/[(p-1)L] implies the **lower** bound on the selected amplification for this FAKE source:

    A_p >= (1-eps)^2 * (p-1)*L/p.

For any fixed small eps, this is of order L, and it can approach (p-1)*L/p as Q increases. This proves that a merely O(L) bound on A_p is INSUFFICIENT, even with a genuinely p-free complementary conductor and an autonomous one-dimensional rational SUCC generator. The o(L) target in MP-08 has a meaningful sharpness firewall. This is NOT an actual-BBP asymptotic counterexample, since the source forcing has been changed.

## Claim ledger and validation scope

MP-01: DISCLOSED paper/finite exact; imports PNT-AP.
MP-02: DISCLOSED paper/finite exact; imports PNT-AP for fixed-k asymptotics.
MP-03: DISCLOSED paper/exact recurrence interval; imports classical irrationality of pi.
MP-04: DISCLOSED exact nonnormal positive-moment/all-prime counterfeit.
MP-05: DISCLOSED cyclotomic relative trace and formal group-ring/CRT source check.
MP-06: FINITE certified source interval, if exact-head workflow passes; no infinite inference.
MP-07: REFUTED universal minimality/local-to-global claim by p-free clock.
MP-08: CONDITIONAL sufficiency PROVED; actual A_p=o(L_p) UNVERIFIED.
Original actual J_(p,d)(h)->0 and I_p(h)->0: UNVERIFIED.
PI normality/RH: OPEN. Signed Weil positivity and empirical nature physics: NOT ADDRESSED.
Independent academic novelty: UNVERIFIED. All central tools are classical, but their exact SUCC source composition is checkable.

Artifacts: observational_succ/bbp_minimal_path.py; observational_succ/bbp_galois_tomography.py; tests/test_bbp_minimal_path.py; tests/test_bbp_galois_tomography.py; scripts/bbp_minimal_path_probe.py; docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md; .github/workflows/bbp-minimal-path.yml.

Sources: Bailey--Crandall, Experimental Mathematics 10(2), 2001, DOI 10.1080/10586458.2001.10504441; Bourgain--Glibichuk--Konyagin subgroup theorem (precise exposition by Kowalski, arXiv:2401.04756); classical Dirichlet/PNT in fixed AP; standard coprime cyclotomic field intersection and character orthogonality. No external result is imported as a theorem about the selected pi digit orbit.

**Conclusion:** Four simple poles truly generate an infinite arithmetic tower, even at every p-adic depth, while an exact source-selected Galois outlier already exists at p=97. The missing implication is NOT more infinite complexity; it is a source-specific bound on selected signed interference.

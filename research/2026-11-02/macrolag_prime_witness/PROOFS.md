# Operation DUMB PROOF — all-lag BBP denominator growth, a sharper coherent shadow, and source-selected signed windows

**2026-11-02; RESEARCH ONLY, NO NORMALITY CLAIM.** Exact parent: #460 head b99518cf93048d87c7cfecd43587bf95dc502c87 (stacked over #459 on Main XIX 81045770234a114247e43eb08ae5c6d446e9514a). The original signed four-pole forcing, literal U_0=0, canonical files, production, Lean and historical contracts are immutable. Results below are elementary *paper proofs* using **classical PNT in arithmetic progressions**; focused exact finite tests do not establish PNT or the unbounded quantifiers. No scholarly-priority or independent-referee claim.

## 0. Original source and two prime mechanisms

Let
\[
r(j)=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)},\quad a=8j-7;
\]
\[
U_0=0,\quad U_N=\sum_{j=1}^N16^{N-j}r(j),\qquad e(x)=\exp(2\pi ix).
\]
All U_N are unwrapped rationals. For nonzero rational x, den(x) is its positive reduced denominator and v_p(x) its p-adic valuation. The p-birth lemma is inherited from #459, not claimed novel here:

For p>5 prime, p=1 or 5 mod 8, let
\[
(j_p,c_p)=((p+7)/8,4)\text{ if }p=1\bmod8,\quad
((p+3)/8,-1)\text{ if }p=5\bmod8.
\]
At j=j_p exactly one source denominator equals p. Multiples 2p and 3p have forbidden mod-8 pole residues, and the first later possible reuse is at J_p=(p+1)/2, where 4p enters. Therefore, for j_p<=j<J_p,
\[
v_p(U_j)=-1,\qquad pU_j\equiv c_p16^{j-j_p}\pmod p.
\tag{BIRTH}
\]

There are **two genuinely different ways** to retain a prime in a time difference U_n-U_m, m<n:

**Shared, not synchronized:** If 2n<p<8m and p=1 mod 4, birth is at/before m and first reuse after n. At both times the same prime is present, with residue difference
\[
p(U_n-U_m)\equiv c_p16^{m-j_p}(16^{n-m}-1)\pmod p.
\]
It survives with v_p(U_n-U_m)=-1 exactly when p does not divide 16^(n-m)-1.

**Newborn, never previously present:** If max(8m,2n)<p<8n and p=1 mod 4, p is absent from every original source term through m, born once between m and n, and not reused through n. Thus v_p(U_m)>=0 and v_p(U_n)=-1, so
\[
\boxed{v_p(U_n-U_m)=-1}
\tag{NEW}
\]
with NO multiplicative-order exception. This is the essential elementary trick that extends the result from short lags to **all later times**.

## 1. DPF-01 — all-lag exponential off-diagonal conductor (PROVED PAPER; new-to-SUCC)

**Theorem.** Put D_(m,n)=den(U_n-U_m). Then
\[
\boxed{\liminf_{m\to\infty}\ \inf_{n>m}
\frac{\log D_{m,n}}m
\ \ge\ c_{\rm BBP}:=\frac{12}{5+\log16}
=1.543887169234143\ldots.}\tag{1}
\]
Equivalently: for every epsilon>0 there exists M_epsilon such that for all integers m>=M_epsilon and **all n>m**,
\[
\operatorname{den}(U_n-U_m)\ge\exp[(c_{\rm BBP}-\epsilon)m].
\]

**Proof.** Write ell=n-m. Import only the classical PNT-AP in the form
\[
\vartheta(x;4,1)=\sum_{\substack{p\le x\\p=1(4)}}\log p=\frac x2+o(x).
\tag{PNT}
\]
For ell<3m, the shared-prime interval 2n<p<8m has total logarithmic weight
\[
\vartheta(8m;4,1)-\vartheta(2n;4,1)
=3m-\ell+o(m).
\]
Its excluded primes divide the positive integer 16^ell-1; their total logarithmic weight is at most log(16^ell-1)<ell log16. Therefore
\[
\boxed{\log D_{m,n}\ge3m-(1+\log16)\ell+o(m).}\tag{2}
\]
The error is uniform for n<=4m since all theta arguments are O(m).

For ell>0 the newborn interval max(8m,2n)<p<8n has no order exceptions. For n<=4m its total logarithmic weight is
\[
\boxed{\log D_{m,n}\ge4(n-m)+o(m)=4\ell+o(m).}\tag{3}
\]
This lower bound is useful when ell is a positive fraction of m, not necessarily when ell=O(1). For n>=4m, the same newborn window yields
\[
\boxed{\log D_{m,n}\ge3n+o(n),}\tag{4}
\]
uniformly as n grows, and this is much larger than c_BBP*m.

Choose alpha=3/(5+log16)=0.38597179230853573... . If 1<=ell<=alpha*m, equation (2) gives
\(\log D\ge[3-(1+\log16)\alpha]m+o(m)=c_{\rm BBP}m+o(m)\).
If alpha*m<=ell<=3m, equation (3) gives
\(\log D\ge4\alpha m+o(m)=c_{\rm BBP}m+o(m)\).
For ell>=3m, equation (4) completes the argument. The PNT-AP remainders are uniform in the first two regimes and relatively small in the third. QED.

**Corollary at the ACTUAL fixed real frequency, not a high-frequency average:** for every fixed integer h!=0, there exists M_h such that whenever n>m>=M_h,
\(e(hU_n)\ne e(hU_m)\).
For each pair the prime witnesses are >2n>|h| and v_p(h(U_n-U_m))=-1, so h(U_n-U_m) is not an integer.

**Scope:** exact phase noncollision and huge *rational denominators*. The bound gives NO useful lower bound on distance to the nearest *real* integer, because a rational with huge denominator may be exponentially close to an integer. It gives NO signed Weyl saving or π normality. Ordinary irrationality of pi already ensures distinctness of the true pi orbit; the arithmetic advance here is quantitative **off-diagonal denominator retention for the selected rational BBP source**, which is not implied by a single-state conductor estimate.

## 2. DPF-02 — an even stronger all-lag conductor for a fully coherent zero-seeded source shadow (PROVED PAPER)

This is a direct hostile control built from the explicit changed-source construction in SUCC #421. It strengthens #421 by proving **all-lag exponential difference-conductor growth** even though the real phases converge to one point.

Define the **unchanged original** r(j) as above, but now let
\[
q=\frac{r(1)}{16}=\frac{47}{240},\quad
d_n=\sum_{j=1}^{n+1}16^{-j}r(n+j),\quad
\widetilde U_n=16^nq-d_n.
\tag{5}
\]
Then \(\widetilde U_0=0\), and its own forcing is
\[
\widetilde r(n)
=r(n)-16^{-n}r(2n)-16^{-n-1}r(2n+1).
\tag{6}
\]
Every \(\widetilde r(n)\) is strictly positive: since r decreases,
\(0<r(n)-\widetilde r(n)<(1/16+1/256)r(n)<r(n)\).
The forcing correction is \(O(16^{-n}n^{-2})\), so every inverse-power asymptotic coefficient agrees with the original r. But \(\widetilde r\ne r\) exactly: do **not** identify these two sources.

Since 16 is 1 mod 15,
\(\{16^nq\}=2/15\) for every n>=1. The source-positive bound
\(0<r(n)<15/(8n-7)^2\) gives
\(0<d_n\le r(n+1)/15<1/(8n+1)^2\).
Thus for every fixed h!=0,
\[
\boxed{\lim_{n\to\infty}e(h\widetilde U_n)=e(2h/15),\qquad
\lim_{N\to\infty}\left|\frac1N\sum_{n=1}^Ne(h\widetilde U_n)\right|=1.}\tag{7}
\]
For **every** p=8k+5>5 and its canonical birth window I_p={k+1,...,4k+2}, length L=(3p+1)/8, there is a uniform **finite, rigorously bounded coherent contrast**:
\[
\boxed{\left|\frac1L\sum_{n\in I_p}e(h\widetilde U_n)\right|
\ge1-\frac{2\pi|h|}{(p+4)^2}.}\tag{8}
\]

**New all-lag theorem for the shadow.** With \(\widetilde D_{m,n}=\operatorname{den}(\widetilde U_n-\widetilde U_m)\),
\[
\boxed{\liminf_{m\to\infty}\ \inf_{n>m}
\frac{\log\widetilde D_{m,n}}m
\ge c_{\rm shadow}:=\frac{32}{12+\log16}
=2.16617416227291\ldots.}\tag{9}
\]

**Proof of (9).** Because \(16^nq-16^mq\) is an integer for n>m>=1, p-integrality of that term means the denominator witnesses for \(\widetilde U_n-\widetilde U_m\) are precisely those of \(d_m-d_n\) at each selected p>5.

For m<n<2m and ell=n-m:
- **Shared source terms:** every prime 8n<p<16m, p=1 mod4, has one original pole in r(t) with n<t<=2m, appearing in *both* d_m and d_n, with rational coefficients 16^(m-t) and 16^(n-t). It has p-adic valuation -1 in d_m-d_n unless p divides 16^ell-1. By PNT-AP and the same divisor-product bound, these survivors have total logarithmic weight at least
\[
4m-(4+\log16)\ell+o(m).
\tag{10}
\]
- **New source terms:** every prime 16m+8<p<16n, p=1 mod4, is born *after* the last source term in d_m but before the last in d_n. It appears once in d_n, not d_m, and its first reuse is later than 2n+1. These yield
\[
\log\widetilde D_{m,n}\ge8\ell+o(m).
\tag{11}
\]
Choose beta=4/(12+log16)=0.27077177028411376... . Use (10) below ell=beta*m, and (11) above. Both give at least c_shadow*m+o(m). For n>=2m, primes 8n+8<p<16n, p=1 mod4, are born in d_n beyond all d_m terms and not reused, yielding
\[
\log\widetilde D_{m,n}\ge4n+o(n)\ge8m+o(n).
\]
The theta errors are uniform in the proportional-window cases. This proves (9). QED.

**Verdict:** the coherent *positive, zero-seeded* changed source also has eventually pairwise distinct phases at every fixed nonzero h (its witnessing primes are >|h|), yet all of those distinct phases converge to the SAME point e(2h/15). It satisfies an even stronger uniform lower bound on denominator growth of all time differences than the certified bound (1) for the original source. One must not infer that the two true optimal constants are ordered, only that these respective **proved lower bounds** are. Therefore, exponential denominator growth, rationality, and even all-order source asymptotics do not imply ANY nontrivial fixed-frequency real cancellation. The source's exponentially small entire remainder is a real selection datum.

**Additional same-four-pole counterseed:** s_*=-pi/16 (not rational) gives U_n(s_*)=-T_n, with the original source and \(0<T_n<(8n+1)^{-2}\). The identical window inequality (8), with limit phase 1, holds for this changed seed. This rules out a seed-blind signed theorem.

## 2a. DPF-06 — the exact exponentially amplified entire-boundary defect (PROVED IDENTITY, NOT A NEW GATE)

There is a remarkably short explicit real-embedding map between the TRUE original orbit and the coherent changed-source shadow. Define alpha=sum_(j>=1)16^-j r(j)=pi/16, and T_n=sum_(j>=1)16^-j r(n+j). Then
\[
U_n=16^n\alpha-T_n,\quad
\widetilde U_n=16^n q-d_n,\quad
\alpha-q=\frac{15\pi-47}{240}>0,
\]
and **exactly**
\[
\boxed{
U_n-\widetilde U_n
=16^n\frac{15\pi-47}{240}-E_n,\quad
E_n=\sum_{j=n+2}^\infty16^{-j}r(n+j).
}\tag{12}
\]
Since the authentic r is positive and decreasing with r(t)<15/(8t-7)^2,
\[
\boxed{0<E_n<
\frac{16^{-n-1}}{(16n+9)^2}.}\tag{13}
\]
This follows from bounding the tail by r(2n+2) times the remaining geometric weight, which is 16^(-n-1)/15.

Consequently the ENTIRE source-forcing difference is exponentially tiny per step, but the small **completed boundary difference** alpha-q is multiplied by the expanding factor 16^n. This is the operational finite-to-infinite seam: a perturbation invisible to every inverse-power source jet can dominate the selected real phase after long transport.

**Critical firewall:** (12) is an *identity*, not a real-mixing bound. The orbit of (15pi-47)/240 is a rational translate/scale of the pi orbit, so proving its base16 normality would merely re-prove the original missing Weyl condition. Do not count this source-amplifier equality as a solution or as an independent normality route.

## 3. DPF-03 — source-selected *finite* Archimedean contrast at fresh prime windows (EXACT INTERVAL MEASUREMENT)

The original source and literal seed **are** observed to cancel strongly on concrete, prespecified windows. This is NOT an asymptotic theorem. The independent interval oracle uses only:

1. Exact Fraction original states from the combined rational source; a separate four-pole Fraction implementation checks the source and supplies float-only independent diagnostics.
2. A two-sided rational enclosure of pi from Machin's formula \( \pi=16\arctan(1/5)-4\arctan(1/239)\) and alternating arctangent series, with **no decimal digits of pi**.
3. Exact rational \(hU_n\bmod1\), reduced to a signed phase and floored to a \(2^{19}\)-mesh. Angle error \(< (44/7)2^{-19}+\text{pi-interval width}\).
4. Exact rational Taylor polynomials of sine and cosine through degree 20; for \(|\theta|<22/7\) each component error \(<(22/7)^{21}/21!\). Outward rounding to denominator \(10^9\), and an explicit global L1 bound \(|z|\le|\Re z|+|\Im z|\).

**Predetermined before evaluation:** first three p>4000 with p=5 mod8: 4013, 4021, 4093; h=1,3,5,7; each full-source normalized window L1 <1/8. All 12 pass exact rational interval certification.

**Second predetermined batch, more demanding:** first three p>10000 with p=5 mod8: 10037, 10061, 10069; same four harmonics; full-source normalized window L1 <1/16. All 12 pass. A first combined run was interrupted after the first prime; all three cases were then replayed individually and exact receipts retained. Selection and thresholds were fixed before evaluation but the same reasoner performed the preregistration, execution and audit: this is **not independent blinded testing**.

The largest upper bound among the 24 certified cases is **0.042229173** (p=4021,h=5); every case also passes 1/16, but the 1/16 threshold at p~4000 was **post hoc**. Every strict certified bound and float-only cross-check is in FINITE_WINDOWS.json; executable interval.py regenerates the mathematical certificates.

In the SAME windows and for the SAME h, the zero-seeded positive changed-source control obeys the uniform **all-p lower bound** (8), above 0.999997 even for the smallest p=4013 and largest |h|=7. This is an explicit source-selecting, finite signed inequality. No finite selection proves an all-p or all-N bound.

## 4. What is actually advanced — and what is NOT

**Advanced:** original-source all-lag arithmetic conductor of time differences, with a uniform explicit exponential rate; a matched coherent, zero-seeded, all-order asymptotic shadow with even stronger lower-bound rate; a clear prime-valuation mechanism for every pair of late times; 24 new, independently source-replayed **finite** genuine selected signed bounds, with 12 preregistered at the stricter threshold.

**NOT advanced to a theorem:** \(S_N(h)=o_h(N)\), low-frequency Fejér energy, fixed-h real phase separation, π normality, or RH. The pair-conductor theorem proves distinctness and p-adic noncollapse, but no lower bound of useful size for \(\Vert h(U_n-U_m)\Vert_{\mathbb R/\mathbb Z}\); the coherent shadow explicitly disproves any such inference based on these data alone. A large-conductor Galois average remains different from the selected real embedding.

**Next verdict-changing probe:** identify a theorem involving the **complete exact original source and real selected boundary**, not just all-order coefficients, that bounds the Archimedean signed cofactor/prime interaction on all large p=5 mod8 windows. It must fail on the two coherent controls and distinguish complete source from matched asymptotic shadow. The current p-window energy criterion (PWI-03) is an equivalence, not such a bound.

### External/classical references
- Prime number theorem in arithmetic progressions: exact weighted theta(x;4,1)=x/2+o(x), stated as Theorem 6.1.1 in https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/corollaries-chapter.html and in analytic number theory notes https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf (PNT-AP is imported classical mathematics, not proved here).
- Original BBP source and single-prime births: SUCC #459, PROOFS.md SPP-01/02.
- Prime-window equivalences, genuine weighted cofactor and controls: SUCC #460, PROOFS.md PWI-01..08.
- Positive zero-seeded all-order coherent shadow: SUCC #421, ALL_ORDER_SHADOW.md, construction M=0,K=1.
- Classical original BBP identity: https://math.hmc.edu/funfacts/finding-the-n-th-digit-of-pi/

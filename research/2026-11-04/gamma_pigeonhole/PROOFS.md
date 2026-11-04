# Gamma Prime Window Pigeonhole — Archimedean/finite-place BBP pinning

**Date:** 2026-11-04. **Status:** explicit elementary paper proofs plus exact Fraction tests, **not** independent external mathematical refereeing or new Lean kernel authority. **Base:** merged SUCC main a673ec95dfac4ef6a61c60222be8b615fd08535d. Read-only context: PR #492 (Alias Valve/source-native counterseed), #495 (LCM/source-sound calculus), #497 (p-Frobenius and sharp source-conductor asymptotics), and on-main Gamma zero/one geometry. Original four signed poles, U0=0, historical contracts, formal/Lean, production and workflows are unchanged.

**Mission:** Locate an exact scale where the analytic Gamma/Euler–Mascheroni observer and the prime-local finite observer distinguish the same rational source. Pigeonhole rigorously. Preserve the precise difference between uniquely selecting a **forcing injection** and proving equidistribution of the **time orbit**.

## GP-01 — a calibrated Euler–Mascheroni successor window (classical)

For x>0, the original SUCC Gamma field is
\[
E_1(x)=\log x-\psi(x),\quad E_1(1)=\gamma,\quad
E_1(x)-E_1(x+1)=\delta(x)=\frac1x-\log(1+1/x)>0.
\]
For a positive integer p, \(E_1(p)=\gamma+\log p-H_{p-1}\); hence the local difference **cancels the additive constant γ**. The globally normalized Gamma field determines the same successor defect, but no arithmetic property of γ itself is used.

The identity \(\delta(p)=\int_0^{1/p}t/(1+t)\,dt\) gives exact rational outer bounds
\[
\frac1{2p(p+1)}<\delta(p)<\frac1{2p^2}.
\]
Its alternating expansion is
\[
\delta(p)=\frac1{2p^2}-\frac1{3p^3}+\frac1{4p^4}-\frac1{5p^5}+\cdots.
\]
For any K>=2 the rational consecutive partial sums S_K,S_(K+1) strictly bracket δ(p), with width precisely \(1/((K+1)p^{K+1})\). We use K=4 to give **finite rational certificates**. These are ordinary classical logarithmic identities; a bare Gamma name is not an inferred dynamical force.

## GP-02 — exact *prime birth* separates real smallness from p-local pole (source-specific, proved)

At original source time n>=2, suppose \(p=8n-7>5\) is prime, automatically p≡1 (mod8). Then
\[
r(n)=\frac4p-\frac2{p+3}-\frac1{p+4}-\frac1{p+5}
=\frac4p+\beta_p,
\]
\[
\beta_p=-\frac{4p^2+33p+67}{(p+3)(p+4)(p+5)},\quad
C_p=\frac{(p+3)(p+4)(p+5)}8.
\]
The numerator of β evaluated at \(p=-3,-4,-5\) is respectively \(4,-1,2\). Thus every common odd prime factor with the denominator is excluded. For p≡1(mod8) the denominator has v2=3 and β numerator is divisible by 8, so **β has reduced denominator exactly C_p**. Since p∤C_p, the sum 4/p+β has reduced denominator exactly p C_p (coprime primary decomposition).

All four original pole denominators before n are less than p, so the source LCM Q_(n−1) has p∤Q_(n−1). Exactly one p is introduced into Q_n=lcm(Q_(n−1),den(r(n))). In \(\mathbb Z_{(p)}\), the new source and selected actual rational state obey
\[
\boxed{p\,r(n)\equiv4\pmod p,\qquad p\,U_n(0)\equiv4\pmod p.}\tag{GP-2}
\]
The p-integral term \(16U_{n-1}+\beta_p\) contributes no p-pole.

In the REAL place, direct simplification yields
\[
r(n)=\frac{15p^2+121p+240}{p(p+3)(p+4)(p+5)}
=\frac{15}{p^2}-\frac{59}{p^3}+O(p^{-4}).
\]
The rational comparisons \(r(n)>2/p^2\), \(r(n)<15/[p(p+1)]\) follow after multiplying positive denominators; for the upper comparison the positive difference is \(44p^2+344p+660\). Therefore
\[
\boxed{4\delta(p)<r(n)<30\delta(p).}\tag{GP-3}
\]
The *same authentic rational number* has a nonzero p-pole and a much smaller real injection of order p^(-2). This is an exact source-typed comparison between two places, not literal physical entanglement.

## GP-03 — the complete gamma-window pigeonhole theorem (classical counting, exact)

For any L>=1, M|L, and fixed integer numerator address a modulo M, the possible rational circle points are
\[
x_k=\frac{a+kM}{L}\pmod1,\quad k=0,\ldots,C-1,\quad C=L/M.
\]
They form a complete equally spaced affine coset of order C. Every half-open circle arc I of length 0<=w<=1 contains
\[
\boxed{N_I\in\{\lfloor Cw\rfloor,\lceil Cw\rceil\}.}\tag{GP-4}
\]
A direct exact count for I=[u,u+w) is
\[
N_I=\Big\lceil C\big(u+w-a/L\big)\Big\rceil-
    \Big\lceil C\big(u-a/L\big)\Big\rceil.
\]
This works even when the arc wraps, and handles endpoints by the half-open convention.

For our forcing denominator L=pC_p, newborn p residue 4 fixes exactly the coset
\[
\boxed{x=\frac4p+\frac{k}{C_p}\pmod1,\quad0\le k<C_p.}\tag{GP-5}
\]
The first Euler–Mascheroni window has length \(w_p=30\delta(p)\sim15/p^2\); thus for **every arc origin** the number of p-passport-compatible candidates is
\[
\boxed{N_I=C_p w_p+O(1)=\frac{15}{8}p+O(1).}\tag{GP-6}
\]
The source r(n) belongs to the coarse arc [0,w_p). The first Gamma observation therefore leaves LINEARLY MANY other rational candidates with the same p-primary fingerprint and declared denominator. Pigeonhole occupancy is not a source-unique reconstruction yet, and a lower collision bound is not the upper pair-count bound required for π-normality.

## GP-04 — the *corrected* Euler–Mascheroni window uniquely pins the original forcing (proved)

The first analytic/finite discrepancy hides one extra Taylor coefficient. Set
\[
\boxed{g_p=30\delta(p)-\frac{49}{p^3}.}\tag{GP-7}
\]
The number 49 is the **exact difference** between the p^(-3) coefficients: 30δ contributes -10 while the full four-pole source contributes -59. It is a source-derived correction, not a fitted or independent source.

For p>5 the full pole expansion is an alternating series
\[
r(n)=\sum_{k\ge1}\frac{(-1)^{k+1}(2\cdot3^k+4^k+5^k)}{p^{k+1}},
\]
whose term magnitudes decrease because the coefficient ratio is <=5<p. Write \(B_p=15/p^2-59/p^3\). Alternating remainder bounds show
\[
B_p+\frac{243}{p^4}-\frac{1043}{p^5}<r(n)<B_p+\frac{243}{p^4},
\]
\[
B_p+\frac{15}{2p^4}-\frac6{p^5}<g_p<B_p+\frac{15}{2p^4}.
\]
Subtract, for every eligible p>=17:
\[
\boxed{0<r(n)-g_p<\frac{236}{p^4}.}\tag{GP-8}
\]
The source cofactor lattice spacing is \(1/C_p\). At **every p>=41**,
\[
\boxed{\frac{236C_p}{p^4}<1.}\tag{GP-9}
\]
Indeed \(236C_p/p^4=\frac18(1+3/p)(1+4/p)(1+5/p)(236/p)\) decreases with p, and it is <1 at p=41.

Therefore the source-compatible affine coset GP-5 has exactly ONE point in the analytic window \(I_p=(g_p,g_p+236/p^4)\): **the original r(n)**.

**Completely finite rational pinning.** Let
\[
d_-=\frac1{2p^2}-\frac1{3p^3}+\frac1{4p^4}-\frac1{5p^5},\quad
d_+=d_-+\frac1{5p^5}.
\]
The fully rational outward interval
\[
\boxed{I_p^{\rm rat}=
\Big(30d_- -49/p^3,\quad30d_+ -49/p^3+236/p^4\Big)}
\]
contains the true r(n). Its width is \(W_p=236/p^4+6/p^5\). For p>=41,
\[
\boxed{C_pW_p=
\frac18(1+3/p)(1+4/p)(1+5/p)(236/p+6/p^2)<1.}\tag{GP-10}
\]
The left side decreases for p>=41. At p=41 it equals the **exact rational**
\(110229570/115856201<1\). Thus ordinary integer interval/count operations and a four-term rational log expansion suffice to recover the unique genuine rational source from its new-prime passport. No irrationality/normality assumption and no floating-point certification are involved.

**Hostile mutation:** \(r'(n)=r(n)+1/C_p\) has precisely the same newborn p-local residue 4 and still lies in the COARSE Gamma window for tested eligible primes p>=41, but GP-10 rejects it. This is a real source discriminator inside the declared pC_p height class.

**Boundary:** This reconstruction pins an individual **forcing** already known from the four original poles. It does NOT prove a statistical distribution of the accumulated selected orbit or uniquely determine the past cofactor from the p passport alone.

## GP-05 — the actual zero-seeded state has a much larger hidden cofactor

Write the source LCM register (same as original SUCC's integer BBP carrier)
\[
U_n=A_n/Q_n,\quad Q_n=\operatorname{lcm}_{j\le n}\operatorname{den}(r(j)).
\]
At a prime birth p as above, \(Q_n=pC_n,\ p\nmid C_n\), and GP-2 gives
\(A_n\equiv4C_n\pmod p\). Hence the **selected** old-cofactor address is
\[
\boxed{k_n=\frac{A_n-4C_n}{p}\bmod C_n,\qquad
U_n=\frac4p+\frac{k_n}{C_n}\pmod1.}\tag{GP-11}
\]
This is a source-faithful exact CRT split: the newly born p-local passport is fixed but the chronological integer numerator determines which old-cofactor point was selected.

Here \(C_n\ge C_p\), generally MUCH larger. By the original prime-support argument (PR #492 AS-01; corroborated, sharpened by draft #497's source conductor proof) and classical PNT in fixed arithmetic progressions,
\[
\log Q_n\ge(6+o(1))n.
\]
Thus **the complete source LCM virtual carrier** has exponentially many p-passport-compatible phases inside any p^(-2) Gamma window, and still exponentially many inside a p^(-4) corrected forcing window. The GP-04 uniqueness theorem relies on the *FORCING* denominator pC_p, NOT on the much larger **STATE** clock pC_n. Do not substitute one clock for the other.

The coherent rational wrong-seed family in PR #492 preserves all new p-passports born strictly AFTER its epoch start A, because its seed denominator divides Q_A and these new p do not divide Q_A; yet it can keep the selected epoch clustered. Therefore a proof involving only freshly born p residues + Gamma forcing + current denominator capacity is REFUTED as a route to selected orbit dispersion. The literal U0=0 numerator history remains essential.

## GP-06 — sharp pigeonhole *no-exclusion* criterion for normality-scale pairs

Take an original rational gap \(U_n-U_t\pmod1=a/L\) with a common odd LCM clock L. Suppose a partial observer knows only \(a\bmod M\), M|L. The admissible gaps form an affine C_(L/M) coset. For q>2, the dangerous close-pair arc has length \(2/q\):
\[
I_q=\{x\pmod1:\|x\|<1/q\}.
\]
By GP-04's general lattice count (GP-4), **if**
\[
\boxed{\frac{2L}{Mq}\ge1}\tag{GP-12}
\]
then EVERY possible numerator congruence class has at least one representative inside I_q. Such partial modular observations **cannot exclude even a single specific nearpair independently of its remaining real lift**. A necessary (NOT sufficient) condition for an exclusion certificate from congruences alone is
\[
\boxed{L/M<q/2.}\tag{GP-13}
\]
At SUCC's logarithmic mesh \(q_A=16^{K_A}/2\asymp\log A\), this requires observing all but an \(O(\log A)\)-sized multiplicative cofactor of the often exponentially large joint clock. A single newborn prime is very far from sufficient.

This does NOT prove a lower bound on the **actual selected** pair count: potential candidates are not realized pairs. The full original numerator/carry history can be much more discriminating than a static congruence class.

## GP-07 — what remains OPEN

Inherited SUCC SC-1..SC-8 prove: \(J_{A,q_A}(U_0=0)=o(K_A)\) on all sufficiently large dyadic A is sufficient for π base-16 normality. A stronger sufficient nearpair estimate is \(P_A(q_A)=o(A^2K_A/q_A)\). Neither is derived by the Gamma pinning of individual source injections.

**Next concrete source-selected probe:** transport the source Gamma window, newborn prime residue, **full old-cofactor address** and exact integer carry coherently across time n and n+d. Test whether the joint constraints can exclude close-pair arcs *without* restoring the entire chosen numerator by hand. Require failure on PR #492's same-forcing source-native coherent wrong seeds and PR #487's cofactor ghosts. If no genuinely new signed/dispersion inequality emerges, call the method contextually saturated, not a proof.

**No status promotions:** π base-16 normality OPEN; Weyl signed o(N) OPEN; RH OPEN. No novel academic priority or quantum-place claim is made.

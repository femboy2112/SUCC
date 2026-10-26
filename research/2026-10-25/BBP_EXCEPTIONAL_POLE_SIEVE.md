# Exact BBP exceptional poles and source p-adic cancellation

**2026-10-25; research-only companion to [Möbius matrix interferometry](OPERATION_MOBIUS_MATRIX_INTERFEROMETRY.md).** Stacked on Spectral Purity #298. The original BBP source and its zero initialization are never modified. No pi-normality or RH theorem.

Let r(n) denote the exact signed four-pole forcing:
$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$
All valuations below apply to its **reduced rational denominator**, not necessarily to the displayed product. Write d_p(n)=v_p(den r(n)).

## Exact theorem: every exceptional residue and every prime-power depth

The exceptional first-layer laws are
$$
d_3(n)>0 \iff n\bmod9\in\{0,1,2,3,4,5,6,7\},
$$
$$
d_5(n)>0\iff n\bmod25\in
\{1,3,4,6,8,9,11,13,14,16,18,19,21,23\}.
$$
Therefore 3 hits 8/9 of times and 5 hits 14/25. By CRT only 11 of every 225 times avoid **both** p=3 and p=5, so deleting either channel as a negligible set is invalid. For each p≥7, exactly four residue classes modulo p give p-divisibility, as shown in the parent dossier.

There is also a **complete depth formula**, with no fitted numerics:
$$
d_3(n)=
\begin{cases}
v_3(8n-3),&n\equiv0\pmod3,\\
v_3(4n-1),&n\equiv1\pmod3,\\
0,&n=3t+2,\ t\equiv2\pmod3,\\
1+v_3(2t+1)+v_3(8t+3),&n=3t+2,\ t\not\equiv2\pmod3,
\end{cases}
$$
$$
d_5(n)=
\begin{cases}
v_5(8n-3),&n\equiv1\pmod5,\\
v_5(2n-1),&n\equiv3\pmod5,\\
0,&n\equiv0,2\pmod5,\\
0,&n=5t+4,\ t\equiv4\pmod5,\\
1+v_5(4t+3)+v_5(8t+5),&n=5t+4,\ t\not\equiv4\pmod5.
\end{cases}
$$
For every p≥7:
$$
\boxed{d_p(n)=v_p(2n-1)+v_p(4n-1)+v_p(8n-7)+v_p(8n-3).}
$$

**Proof.** The numerator F(n)=120n²−89n+16 evaluates to 3/2, 5/4, 30, −1/2 at the four rational pole roots n=1/2,1/4,7/8,3/8. Hence at p≥7, where pole roots are distinct, the numerator is a p-unit whenever exactly one pole factor vanishes. At p=3 the collision is n=3t+2:
$$
F(3t+2)=3(360t^2+391t+106),\qquad
D(3t+2)=9(2t+1)(8t+3)(12t+7)(24t+13).
$$
The bracketed numerator is congruent to t+1 modulo 3. For t≡2 mod3 both remaining pole factors are p-units and the extra numerator 3 cancels the last denominator 3; otherwise its bracket is a p-unit and gives the displayed depth. The other n mod3 classes each have one pole and a numerator unit. At p=5, the collision is n=5t+4:
$$
F(5t+4)=5(600t^2+871t+316),\qquad
D(5t+4)=25(4t+3)(8t+5)(10t+7)(40t+29).
$$
The bracketed numerator is congruent to t+1 modulo5. The same cancellation happens exactly at t≡4 mod5; the other n mod5 classes give the remaining cases. This proves the claimed first-layer periodic classes and all-depth valuations.

**Observer information criterion.** For p≥7 and all k≥1, the capped forcing depth min(k,d_p(n)) is determined by n mod p^k. For p=3,5 this holds for all k≥2 but fails at k=1 (n=2 versus 8 for 3, n=4 versus 24 for 5). Thus increasing prime depth eventually makes the forcing-depth label redundant relative to the time residue. The state-denominator depth and true integer carry need separate treatment.

## Exact theorem: source-selected state-depth cancellation

For any odd prime p let a=v_p(den U_(n-1)), b=d_p(n), and c=v_p(den U_n), where the **original** U_0=0 and U_n=16U_(n-1)+r(n). Non-Archimedean arithmetic gives
$$
\boxed{c\le\max(a,b),\qquad a\ne b \Longrightarrow c=\max(a,b).}
$$
Only equal positive depth can **drop**. Finite source-authenticated examples: (n,p,a,c)=(6,3,2,1), (51,3,4,3), (25,7,2,1), (30,7,1,0), (20,13,1,0), (76,11,2,0).

The hostile #298 full-conductor counterfeit shares the same monotone Q_n=lcm_(j≤n) den r(j), but its U_n*=16^n−1/Q_n has monotone per-prime reduced-denominator depths and therefore zero depth drops. This distinguishes true selected numerator cancellation from the conductor alone. It does not show that authentic drop events have positive density, spectral cancellation, or decorrelation.

## Finite execution, status, next falsification

Implementation: observational_succ/bbp_exceptional_pole_sieve.py, six-group tests in tests/test_bbp_exceptional_pole_sieve.py. The local isolated source-compatible run passed six test groups including 11,990 exact p-depth comparisons (n=1..1199 for ten odd primes), period/CRT finite holdouts including p3,p5,p7,p11, and authentic-vs-conductor-counterfeit drop comparisons. That run used an expressly declared local mock source interface; it is not hosted native-repo validation. Published tree and hosted CI must be checked separately.

**Claim status:** pole congruences, valuations, and p-adic ultrametric = PAPER-PROVED elementary identities, finite testing corroborated; particular BBP depth drops = EXACT FINITE; normality and conductor-flat signed Fejér estimate = OPEN. These are ordinary classical source results; scholarly novelty UNVERIFIED.

**Next discriminating probe:** split the #298 conductor-flat innovation by true p3/p5 depth-drop events, retaining the **signed cross-stratum Fejér terms** and exact true carries. Compare against the full-conductor counterfeit and #297 exact-forcing altered-initial controls. Seek a quantitative all-N bound; conditional PSD/Möbius inversion and sole event counts cannot establish one. Keep the inherited n²/n³ moving-frequency boundary, positive jet mutants, and no-Haar-selection firewall.

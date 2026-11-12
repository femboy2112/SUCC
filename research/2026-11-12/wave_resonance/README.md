# Operation Deep Water — source-locked arithmetic waves

**2026-11-12 · SUCC additive research · draft PR #600 · binary Goldbach OPEN.**

The prime source generates a shared Fourier carrier. For each integer prime p, the additive character e(p alpha)=exp(2 pi i p alpha) is its wave at angle alpha. Rational angles detect prime residues; their normalized amplitudes are Ramanujan sums. The semiprimes surviving a cube-root sieve share the SAME normalized rational wave pattern, but contribute an asymptotic amplitude log 2.

**The established result:** Siegel–Walfisz/PNT in progressions, exact CRT–Ramanujan identities, and a semiprime partial-summation argument imply positive aggregated signed prime-versus-semiprime mass in every macroscopic window and every admissible even residue class modulo any even M <= (log X)^A, A fixed. The source-dependent pointwise signed coefficient is still OPEN.

**Source:** for X>=2 and z=floor(X^(1/3)), p_X(k)=1 if k<=X prime, c_X(k)=1 if k<=X composite with no prime divisor <=z, otherwise 0. Every such c_X is a semiprime. Define L_(X,z)(N)=(p_X*p_X)(N)-(c_X*c_X)(N), ordered convolution. A positive L certifies Goldbach at N but is STRICTLY stronger than Goldbach. The target-adaptive object uses z_N=floor(N^(1/3)).

**Core exact identities:** 
- M_theta|n>=e(theta n)|n>, V_l|n>=|l n>: M_theta V_l=V_l M_(l theta). Additive coproduct conserves the additive character.
- Haar measure on the unit group U_M is invariant under coprime prime multiplication; its additive Fourier transform is c_M(a)/phi(M).
- K_M(r)=#(u,v in U_M: u+v=r mod M) = M^(-1) sum_(a mod M) c_M(a)^2 e(-ar/M).
- Sigma_M(r)= M K_M(r)/phi(M)^2 = product_(ell|M)[ell/(ell-1) if ell|r, ell(ell-2)/(ell-1)^2 otherwise]. For even M and r, Sigma_M(r)>=2 C_2>0.

**The missing bridge:** These results control coarse rational channels but not the signed fine-frequency modes needed to prove L_(N,z_N)(N)>0 for every even N. In fact a genuine-prime-only finite source reallocation preserving ALL rational modes q<=7 removes every Goldbach pair for N=4200; source authentication distinguishes it.

The local complete reproducibility package includes an extended paper, trial-division independent audit, 12 Python tests, C++17 exact NTT scan, raw JSON results, preregistered holdout, and proof-campaign plan. This research subtree in GitHub records the mathematical core and pointers.

**Finite receipts:** X=40,000 / 120,000 / 240,000 exploratory exact scans; preregistered X=360,000 holdout. In window [X/2,X] the signed class-0 / class-2 ratio modulo 12 is 2.037, 2.022, 2.016, 2.014 respectively (CRT limiting ratio exactly 2). At holdout X=360,000 the window [X,3X/2] gives ratio 2.011. All six even residue-class signed totals are positive in both holdout windows. At the truncated upper boundary [3X/2,2X], 233 individual even signed coefficients are negative despite positive aggregated totals. This does not refute the adaptive source conjecture.

**Authority:** Algebraic identities: PROVED LOCAL. Uniform residue and macroscopic theorems: paper derivations importing classical Siegel–Walfisz/PNT (no new-priority claim). Finite computations: OBSERVED only. Pointwise Goldbach and stronger signed inequality: OPEN. No π-normality, RH, physical quantum process, or nontrivial holonomy claims.

**References:** Andrew Granville, Prime Number Theorem in arithmetic progressions, https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf ; Bhowmik–Grimmelt, The exceptional set of the Goldbach problem (2026), https://link.springer.com/article/10.1007/s10476-026-00191-z ; Terence Tao, Heuristic limitations of the circle method (2012), https://terrytao.wordpress.com/2012/05/20/heuristic-limitations-of-the-circle-method/ ; Matomaki–Radziwill–Shao–Tao–Teravainen, Higher uniformity of arithmetic functions in short intervals II (2026), https://link.springer.com/article/10.1007/s00222-026-01408-6 .

See THEOREMS.md and NEXT.md in this subtree; parent work in ../signed_sieve_coupling/, ../carrier_first_goldbach/, ../scott_relative_defect/.
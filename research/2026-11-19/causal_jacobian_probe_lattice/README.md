# Causal Jacobians, lawful probe lattices, and BBP–Fibonacci resonance

**2026-11-19 | research-only | BASE: Main XXVI 81be6b897ae980b801a3b9de9e22ef81e8360bfb.** Read-only comparisons: PRs #657, #663, #664, #665, #666, #667. These are paper deductions and finite exact controls, not independent external refereeing. **R0 and base-16 normality of pi remain OPEN.** No archival source, production state, zero seed, or claim status is changed.

**Implemented follow-up:** [five-channel observer](five_channel/README.md),
[construction and prime repair](five_channel/CONSTRUCTION.md),
[coherent finite-slice agreement](five_channel/FRAME_AGREEMENT.md), and
[adversarial audit](five_channel/ADVERSARIAL_AUDIT.md). A locally stationary
observer is explicitly allowed. Its retained compensator transports the fixed
signed statistic to the original source frame. The follow-up also corrects the
modulo-11 clock repair and the larger blind subgroup of the two selected lags.

## JOL-01: Lawful rotate–decide–advance and the exact character Jacobian (paper-proved)

An observer has a forward source time n, retained history/memory m_n, admissible probe lattice L_n and a memory-conditioned decision policy. For linear P and G, quotient descent requires G(ker P) subset ker P. Equality is required if both G and its descended action are invertible; ambient invertibility alone is insufficient in infinite dimension. Preserving the actual numerical report is stronger: PG=P. Nonlinear descent requires preservation of entire fibers, not merely a pointwise differential-kernel test. This is the descent criterion already in Principia / #657; no novelty claim. Reconstruction of history occurs at a later present time and is not reversed carrier time.

Preserve the **literal** BBP source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

The affine homogeneous step on (U_n,1)^T is M_n=[[16,r(n+1)],[0,1]], of determinant 16; its state derivative is 16. At the real place |16|=16, at the binary place |16|_2=1/16, at every odd place it is a unit. The local norm product is one. These are deterministic norm laws, **not** real-phase mixing estimates.

For the actual Fourier character z_(n,h)=exp(2 pi i h U_n),

$$
\boxed{z_{n+1,h}=\exp(2\pi i h r(n+1))\,z_{n,16h}.}
$$

Character pullback maps Z injectively to 16Z, with cokernel Z/16Z. After k steps its image is 16^k Z, index 16^k. This is the exact dual sixteen-child lattice loss, a frequency dilation rather than an ordinary rotation. There is no ordinary derivative with respect to discrete h; this statement is character transport. Linear moving charts have J_n^G=G_(n+1) J_n G_n^{-1}; nonlinear charts require derivatives evaluated at the corresponding points. Pure gauge changes telescope. A nonzero signed transport/descent defect is not automatically statistical cancellation.

## JOL-02: New exact 7/11/29 spectral comparison (integer proof, exact finite certificate)

Use the genuine auxiliary five-coordinate Fibonacci observer of #667, with A=[[1,1],[1,0]] and T=Sym^4(A^2) in the quartic monomial basis:

~~~
16 32 24  8 1
 8 20 18  7 1
 4 12 13  6 1
 2  7  9  5 1
 1  4  6  4 1
~~~

The reciprocal eigenvalues of A^2 give the exact integral factorization already established in #667:

$$
\chi_T(X)=(X-1)(X^2-7X+1)(X^2-47X+1),
\quad\det T=1,
$$

and therefore

$$
\boxed{\chi_T(16)=-1076625=-3^3\,5^3\,11\,29.}
$$

Exact order pairs (ord_p(16), ord_p(T)):

- p=2: (nonunit,3); p=3: (1,2); p=5: (1,5) — inherited #667.
- p=7: (3,4), joint order 12; p=11: (5,5), joint order 5.
- p=29: (7,7), **an additional spectral coincidence control**. Prime 29 also occurs in the original source denominators; it is not an out-of-source prime.

Modulo 11, ell_11=(4,2,10,10,1) satisfies ell_11*T=16 ell_11. Thus ell_11*T^n*e0=4*16^n mod 11, a genuine homogeneous finite-field intertwiner. Modulo 29 the corresponding primitive row is ell_29=(4,6,14,20,1), another genuine intertwiner. Modulo 7 there is no eigenvalue 16. The underlying square-root orientation has 2^3=+1 mod 7 but 2^5=-1 mod 11 while 16^5=+1. This is an exact orientation double-cover, not pi-digit randomness.

**Nonlift theorem (one digit only):** rank_F11(T^T-16I)=4 and v_11(det(16I-T))=1. Smith reduction therefore has one elementary divisor of valuation one and four units; every solution ell*T=16ell mod 121 reduces to zero mod 11. No primitive ell_11 can lift with this **fixed eigenvalue 16** modulo 121. This does not exclude a moving 11-adic eigenvalue or a nonautonomous/injected observer.

#666 independently supplies a *source-filter* evaluation H(A^{-1})=[[8,1],[1,7]], determinant 55=5*11. The source-derived local precision defect and the new T/16 homogeneous spectral coincidence have not been identified as a single BBP-to-real-phase conjugacy. The p=29 control prevents overinterpreting the spectral match.

## JOL-03: Exact p-primary rational source transport (paper-proved)

For reduced q=a/b, let p^k || b; define pr_p(q)=(a*(b/p^k)^(-1) mod p^k)/p^k in Q/Z, or zero if p does not divide b. The canonical group decomposition satisfies q=Σ_p pr_p(q) mod Z, and therefore

$$
\operatorname{pr}_p(U_{n+1})
=16\operatorname{pr}_p(U_n)+\operatorname{pr}_p(r(n+1))
\quad\text{in }\mathbb Q/\mathbb Z.
$$

It is an exact decomposition of the original **rational** state, not of the irrational completed value U_n+T_n. Active prime powers must be tracked: a p-level coincidence cannot be applied at a p^2 source pole. These local waves are not probabilistically independent. Averaging their products requires an authenticated signed joint/cofactor estimate.

## JOL-04: A rational holonomy-to-R0 sufficient theorem (paper-proved, missing premise OPEN)

Here the inherited word "holonomy" names a source-corrected lag residual. No
connection, closed geometric transport path, or curvature theorem is asserted.

For fixed positive integer lag ell set R_(n,ell)=Σ_{j=1}^ell 16^(ell-j) r(n+j). Then

$$
U_{n+\ell}-U_n-R_{n,\ell}=(16^\ell-1)U_n.
$$

For nonzero integer h, K=h(16^ell-1), and B>=1, form the **fully rational** norm

$$
H_{B;\ell,h}=\frac1B\sum_{n=B}^{2B-1}
\left\|h\,(U_{n+\ell}-U_n-R_{n,\ell})\right\|_{\mathbb T}^{\,2}
=\frac1B\sum_{n=B}^{2B-1}\|KU_n\|_{\mathbb T}^2.
$$

Using (i) ||Kt||_T<=|K| ||t||_T, (ii) 1-cos(2pi t)>=8||t||_T^2, (iii) the authentic positive tail T_n<r(n+1)/15, (iv) r(n) decreasing via its positive moment representation, and (v) |e(s+t)-e(s)|<=2pi|t|, we obtain for the **actual zero-seeded** W_B(1):

$$
\boxed{1-\Re W_B(1)\ \ge\
\frac{8H_{B;\ell,h}}{h^2(16^\ell-1)^2}
-\frac{2\pi}{15}r(B+1).}
$$

Thus a proved liminf_B H_(B;ell,h)>0 for any **fixed predeclared** ell,h would prove R0. This is a stronger sufficient hypothesis, not a source-derived bound, not an equivalence, and not full normality. No all-B lower bound has been proved.

At p=7, an ell=3 homogeneous loop kills its simple p-part; at p=11, ell=5 kills its simple part. Adjacent lag ell+1 restores a nonzero multiplier mod these primes, subject to higher-pole depth. Comparing return/escape pairs is a way to test the **cofactor**, not a shortcut to independent clock statistics.

## JOL-05: Holonomy has an exact fifteen-point gauge kernel (paper-proved)

Since gcd_{ell>=1}(16^ell-1)=15, the signed character bank containing all lags with h=1 has kernel precisely the circle-fixed subgroup (1/15)Z/Z. An unanchored bank therefore cannot distinguish phase zero from 1/15. Squared-distance energies have additional reflection ambiguity u versus -u, so this kernel statement is not their complete identifiability statement. Absolute authenticated source/phase observations are necessary to identify that distinction. Real Fourier indices h=7 and h=11 separate points because 8*7-5*11=1, giving e(u)=e(7u)^8 e(11u)^(-5). Their two separate means do not determine the mean of e(u); signed joint information is needed. These **real frequency indices** are not the p-adic 7/11 source-clock projections; conflating them would manufacture a source map.

The exact phasor source twist and its Jacobian are seed-blind: the hostile same-forcing seed s=-pi/16 has an exactly locked completed orbit but violates the original U_0=0 boundary. The abstract completed radix orbit fixed at1/15 has zero lag energy while satisfying R0. For the same-forcing seed1/15-pi/16, the raw rational-source analogue is U_n=16^n/15-T_n; its lag energy tends to zero, rather than being identically zero at finite time. Fibonacci observer rank, unimodular volume, and local matches alone cannot prove signed real cancellation.

## JOL-06: Preregistered proof offensive

**Proposed fixed cross-channel probes:** (ell,h)=(4,11) aimed at 7-adic memory, and (6,7) aimed at 11-adic memory, **after** evaluating source p-power depths and their respective cofactor cancellation. The outstanding target is a uniform all-late-shell lower bound for H_(B;ell,h), or preferably the weaker Main XXVI terminal rational norm, derived from the authentic terminal numerator/CRT winding. Holdouts must be beyond prior tested ranges; finite positives do not prove a liminf.

**Follow-up correction:** these two multipliers have gcd 255, so their own
signed bank has a 255-point blind subgroup, larger than the full all-lags kernel.
The implemented preregistration keeps their modes as diagnostics and explicitly
includes the absolute authenticated h=1 character. The historical prime labels
do not establish that these two lags are arithmetically superior.

**Hostile cases:** s=-pi/16 wrong-seed same-forcing lock; rational alias; 1/15 fixed phase; sparse factorial irrational with cold shells; p=29 homogenous spectral false-positive; higher p-power poles; and PR #667's mixed 2/3-adic finite-history shadow. Retain raw signed cofactor phases and chronological source, never replace a full product average by product of averages.

**Evidence:** the follow-up audit replayed both inherited stdlib scripts, checking characteristic polynomial and rank/order, 11/29 eigenrows, original Fraction BBP recurrence, p-primary transport, fifteen-point character kernel, and finite rational lag inequalities. The executed commands and current validation scope are recorded in [VALIDATION](five_channel/VALIDATION.md); no unrecorded earlier run is needed as evidence. **R0, all-mode Weyl cancellation, π normality, Collatz, and RH: OPEN.**

## Repository crosswalk

- #657: signed descent, window tomography and source-gauge controls.
- #663: rational Borwein/Haar criterion for full normality.
- #664: actual prime survival, CRT compatible terminal words and unresolved integer winding.
- #665: memory-preserving null operations.
- #666: source filter H(A^{-1}), 5/11 determinant and causal/cyclic boundaries.
- #667: T=Sym^4(A^2), 2/3/5 prime-power orders and information-loss controls.

Do not merge unreviewed sibling branches. Source arithmetic and observer algebra are closed local edges; **the missing edge is still a uniform signed estimate in the authenticated source frame**. A faithful local moving frame may remain locked forever.

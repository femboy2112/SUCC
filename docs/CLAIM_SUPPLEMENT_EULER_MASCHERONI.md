# Euler--Mascheroni successor, character, and completed-Li claims

**Namespace:** EMS-01--28. **Baseline main:**
`e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**PI NORMALITY PROVED: NO. RH PROVED: NO.**

This additive research supplement changes no historical claim. Classical
identities, elementary paper proofs, exact finite certificates, numerical
diagnostics, and unproved asymptotic obligations have separate authority.
The full analytic claims below are not Lean-kernel certificates. Internal
same-model review is not independent external refereeing. Academic priority
of the new-to-project assembly remains unverified.

## Source and notation

$G(s)=\zeta(s)-1/(s-1)$, with its removable value $G(1)=\gamma$.
$G(s,a)=\zeta(s,a)-1/(s-1)$ for $a>0$.
$B_N(s,a)=\sum_{0\le k<N}(k+a)^{-s}-\int_1^Nx^{-s}\,dx$.
The original BBP orbit is $U_0=0$, $U_n=16U_{n-1}+r_1(n)$, where
$r_s(n)=4(8n-7)^{-s}-2(8n-4)^{-s}-(8n-3)^{-s}-(8n-2)^{-s}$.
Changing $s$ changes the forcing unless $s=1$.
$e(x)=\exp(2\pi i x)$; every pi asymptotic statement concerns each fixed
integer $h\ne0$ and all sufficiently large source horizons.
Li coefficients use the actual completed $\xi$ and the standard Stieltjes
sign/factorial convention.

Proof keys: [S: successor/refinement](../research/2026-10-24/EULER_MASCHERONI_SUCCESSOR_REFINEMENT.md),
[B: BBP regulator](../research/2026-10-24/EULER_MASCHERONI_BBP_REGULATOR.md),
[C: character Tauberian](../research/2026-10-24/EULER_MASCHERONI_CHARACTER_TAUBERIAN.md),
[L: completed Li](../research/2026-10-24/EULER_MASCHERONI_COMPLETED_LI.md),
[R: synthesis and crosswalk](../research/2026-10-24/EULER_MASCHERONI_SYNTHESIS.md),
[F: finite receipt](../research/2026-10-24/euler_mascheroni_validation/probe_receipt.json).

| ID | Claim, domain, and quantifiers | Authority | Proof, control, and limit |
|---|---|---|---|
| EMS-01 | For real $r>1$, the user's sum is $G(r)$; $G$ extends entirely and its Taylor jet at one is the Stieltjes hierarchy | CLASSICAL | S §1, DLMF 25.2. Scalar identity supplies no source-character cancellation. |
| EMS-02 | For every finite $N\ge1$, the paired-sum correction is $(N^{1-r}-r^{-N})/(r-1)$; the compensated remainder is bounded by $|s|N^{-\Re s}/\Re s$ for $\Re s>0$, and by $1/N$ for real $s\ge1$ | PROVED PAPER; EXACT FINITE | S §2. Both boundary terms and the removable value $N-\log N$ are retained; missing-boundary mutant rejected. |
| EMS-03 | Arbitrary simultaneous $N\to\infty,r\downarrow1$ need not preserve gamma: $N=m^m,r=1+1/m$ gives $\gamma-1$ | REFUTED unrestricted cofinal inference; PROVED counterexample | S Proposition 2.3. This is a full limit proof, not a finite numerical observation. |
| EMS-04 | For $a>0$, all finite successor endpoints and normalized integer residue refinements of $B_N(s,a)$ obey the displayed exact laws | PROVED PAPER; EXACT FINITE | S §4. Finite source reindexing; tests include prime and composite multipliers, omitted residues, and endpoint mutants. |
| EMS-05 | The affine maps $x\mapsto p^{s-1}x+(p^{s-1}-1)/(s-1)$ compose as $\mathcal A_p\mathcal A_q=\mathcal A_{pq}$; at $s=1$ their anomaly is $\log p$ | PROVED PAPER; CLASSICAL ingredients | S Proposition 4.3, exact finite controls. Refinement is not a new independent Euler factor. |
| EMS-06 | $G(1,1/4)-G(1,3/4)=\pi$; the original BBP formula is a specific shifted Lerch combination at $s=1,z=1/16$ | CLASSICAL; EXACT SOURCE IDENTIFICATION | S §5 and B §2. Common gamma cancels in the reflection difference; an independent Machin bracket calibrates finite intervals. |
| EMS-07 | On $\Re s>0$, $G(s)/s$ is the Laplace transform of $1-\{e^y\}$; its sum kernels are positive Gram kernels | PROVED PAPER from CLASSICAL summation | S §6; exact finite positive and null Gram controls. No identification with completed signed Weil. |
| EMS-08 | The positive measure $(1-\{e^y\})e^{-y}dy$ has moments $m_j=j!\sum_{k\le j}\gamma_k/k!$, bounded by $j!$, and its full moment sequence determines it | PROVED PAPER | S §7, explicit exponential-moment/transform uniqueness proof. Full infinite data are essential. |
| EMS-09 | For any fixed $M\ge0$, explicit positive Legendre perturbations preserve moments $0$ through $M$ and change the next moment | PROVED PAPER; EXACT FINITE | S §8; F includes orders 0,1,3,6. Counterfeit changes the source; it does not preserve every derivative simultaneously. |
| EMS-10 | The normalized Dirichlet and geometric clocks at $1+\varepsilon$ have total variation tending to one as $\varepsilon\downarrow0$ | PROVED PAPER; FINITE LOWER CERTIFICATE | C Proposition 1; event $n\le\lceil\varepsilon^{-2}\rceil$; F certifies TV $>4/5$ at $\varepsilon=1/64$. |
| EMS-11 | Holomorphy of a bounded-coefficient Dirichlet series near $s=1$ alone does not force its ordinary coefficient mean to vanish | REFUTED implication | C Proposition 2; $a_n=n^{it}$ has an off-axis boundary pole and nonvanishing mean. The counterfeit is not BBP. |
| EMS-12 | For every bounded complex sequence, its ordinary mean tends to zero iff both harmonic time windows $(N,2N]$ and $(N,3N]$ tend to zero | PROVED PAPER; REFORMULATION | C Theorem 3; exact dilation cocycle, dense multiplicative subgroup, dominated convergence. No selected-source cancellation is established. |
| EMS-13 | One harmonic time dilation does not suffice | REFUTED implication; PROVED counterexample | C Proposition 4: dyadic log-periodic signs have doubling windows $O(1/N)$ and a subsequence mean $2\sqrt2-3\ne0$. |
| EMS-14 | For original $U_0=0$ and each integer $h$, the harmonic source-to-pi error is bounded by $33|h|/(896N^2)$ at dilation2 and $11|h|/(252N^2)$ at dilation3 | PROVED PAPER; EXACT FINITE envelopes | C §5; unchanged four-pole tail. All-mode/all-horizon cancellation remains required. |
| EMS-15 | The difference of the actual-source and pi-orbit character Dirichlet series continues holomorphically to $\Re s>-1$, with the stated compact-half-plane tail | PROVED PAPER | C Proposition 8; coefficient difference $O_h(n^{-2})$. Preserves the boundary question, does not remove its singularities. |
| EMS-16 | Continuous boundary values of the character Dirichlet series on the entire line $\Re s=1$ suffice for ordinary cancellation | CLASSICAL CONDITIONAL Tauberian bridge | C §7; apply Wiener--Ikehara to nonnegative coefficients $1+\Re a_n$ and $1+\Im a_n$ with conjugate modes. Actual boundary premise unproved. |
| EMS-17 | Four actual $h=1$ BBP harmonic windows at $N=32,128$, dilations2,3, have the recorded exact rational enclosures; the doubling magnitude increases between these horizons | VERIFIED FINITE; REFUTED monotone-decay inference | C §8 and F; Machin/Taylor intervals and disjoint squared-modulus intervals. No asymptotic conclusion. |
| EMS-18 | Finite Lerch residue partitions, with both $z^j$ and $z^p$, preserve all original BBP source indices | PROVED PAPER; EXACT FINITE | B equations (1)--(3), tests of independent interleavings and dropped factors. Only $s=1,z=1/16$ is the original pi sum. |
| EMS-19 | For every real $s>0,N\ge1$, the unregulated four-ray tail lies between $(15/8)(8N+6)^{-s}$ and $(15/8)(8N-7)^{-s}$ | PROVED PAPER | B §3; positive three-difference decomposition and integral comparison. Rational code specializes to integer exponents. |
| EMS-20 | The balanced Hurwitz continuation has $B(0)=15/8$ though every literal finite $s=0$ sum is zero; if $s\downarrow0$, $N\to\infty$ and $s\log N\to c\in[0,\infty]$, the cofinal prefix limit is $(15/8)(1-e^{-c})$ | PROVED PAPER; finite endpoint controls | B §4; exact tail squeeze, including $c=\infty$. $s=1/m,N=2^m$ gives $15/16$, not a pi statistic. |
| EMS-21 | The Stieltjes jet transports through the formal logarithm to the actual completed Li coefficients with all Gamma/pole/pi terms retained | CLASSICAL map; PROVED finite recurrence | L Propositions 2--4. Fixed Archimedean gamma and coupled gamma mutation are explicitly distinct; omitted-completion controls fail. |
| EMS-22 | Integer successor sums with monotone tails and rational log/pi/zeta enclosures certify positive $\lambda_1,\lambda_2,\lambda_3$ at cutoff512 | VERIFIED RATIONAL FINITE | L Propositions 1--4 and §5, F. Calibration of three known coefficients; no all-degree positivity result. |
| EMS-23 | For every $m\ge2$, an explicit entire symmetric deformation preserves the first $m-1$ Li coefficients yet has zeros at $1/4,3/4$; its added term cannot come from an ordinary absolutely convergent Dirichlet series | PROVED PAPER; EXACT finite polynomial controls | L Propositions 5--6. Preserves the completed analytic finite observations but provably changes arithmetic source; not an RH counterexample. |
| EMS-24 | Centered fractional-part dilation has Mellin transform $(\theta-\theta^s)\zeta(s)/s$ for $0<\theta\le1,\Re s>0$, with explicit value and gamma-containing derivative at one | CLASSICAL; PROVED crosswalk | R §7 and Balazard--Saias. The associated $L^2$ closure is the classical RH-equivalent obligation, still open. |
| EMS-25 | All actual BBP character time windows vanish; all completed Li coefficients have the required sign; Nyman closure or original signed Weil positivity holds | OPEN / UNVERIFIED | The targets are stated, not assumed. No finite certificate, counterfeit, positive gamma kernel, or change of coordinate discharges them. |
| EMS-26 | With actual completion fixed, replacing $G$ by $B_N$ changes the $n$th Li coefficient by at most $(20/7)n5^{n-1}N^{-3/4}$; the centered $B_N-(1/2)N^{-s}$ improves this to $(135/392)n5^{n-1}N^{-7/4}$, for every $N,n\ge1$ | PROVED PAPER | L Proposition 7 and Corollary 7.1: finite-cell representation, common convex disk, logarithm segment estimate, Cauchy and binomial transfer; centered primitive prompted by pinned PR285. Sufficient cutoff budgets only, not optimal/necessary complexity bounds or sign theorems. |
| EMS-27 | For a genuine finite Euler product, $0\le\zeta(1+\varepsilon)-P_X(1+\varepsilon)\le X^{-\varepsilon}/\varepsilon$; the stated cofinal condition suffices to recover gamma after pole subtraction | PROVED elementary bound; prior-chat / PR285 continuation | R §8; EAB-07--08 at pinned sibling head. Fixed prime cutoff fails; no necessity or new Euler-product theorem claimed. |
| EMS-28 | A 70-dps huge-cutoff Hurwitz diagnostic returned0 at $m=400$; 220dps gave approximately0.948528; the new guard rejects the inadequate precision | OBSERVED NUMERICAL FAILURE; REPAIRED diagnostic | B §6 and preserved failure receipt. Neither number is an interval certificate; theorem (EMS-20) is proved independently. |

## Next falsification opportunities

For the finite interfaces, delete a boundary, residue, regulator power,
completion term, or sign and require the existing exact controls to fail.
For a proposed pi estimate, test it on the original zero-initial source,
retain every signed term, and confront the certified nonmonotone windows
and one-scale counterfeit. For a proposed RH implication, preserve actual
Dirichlet-source data and fixed completion, and expose the uniform
degree/horizon bound. A declaration of all-degree positivity or an
RH-equivalent closure is an unpaid premise until proved.

See the [synthesis](../research/2026-10-24/EULER_MASCHERONI_SYNTHESIS.md) for
the comparison with all recent sibling drafts and the strictly smaller
first-saving targets. The [validation record](../research/2026-10-24/EULER_MASCHERONI_VALIDATION.md)
distinguishes the full test run from paper-proof authority.

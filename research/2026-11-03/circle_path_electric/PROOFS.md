# Operation CIRCLE PATH × ELECTRIC — natural extension, exact Fourier selection, and BBP branch energy

**2026-11-03.** New strictly additive draft child of SUCC PR #487 at pinned commit `5f69d87d8bddde4f7136229289bc9ebde430c5f0`. Preregistration was separately committed before running the declared original holdouts at `2772bf00fef7b5a43df302560766d0547beee6a1`. All original four signed Mellin denominators and the literal `U_0=0` remain unchanged. This file claims paper proofs and exact finite checks, NOT a new Lean proof, physical Feynman dynamics, electrical lightning explanation, real Weyl decay, or base-16 normality of pi.

## Contract and source map

Original **unwrapped** state: `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`. Original real circle phase: `x_n={U_n}`. Every `r(n)` and `U_n` has **odd reduced denominator** (combine the original even denominators into the inherited odd-denominator normal form from #476), hence each is 2-integral. Never substitute `{U_n}` for the unwrapped 2-adic state without reinstating integer carries. The authentic BBP completion is `X_n=16^n(pi/16)=U_n+T_n`, with positive `T_n=O(n^-2)` inherited from #474/#487.

The path category and transfer operator below are the classical expanding `×16` map on the CIRCLE. The source-marked affine arrows `F_n(x)=16x+r(n+1)` form a **different, nonautonomous path category**. The spatial cylinder tree of the actual empirical `x_n` is a valid observable tree, but is NOT automatically the chronological path tree of the unforced `×16` system: forcing and Gamma correction must be retained for an interconnection.

## CE-01 — Unique finite odd-denominator predecessor and the missing real-limit section (CLASSICAL + ORIGINAL SOURCE)

Let `C_M=(1/M)Z/Z`, with M a positive ODD integer. The map `T(x)=16x mod1` is a group automorphism of `C_M` since gcd(16,M)=1. For `z=a/M∈C_M`, written in [0,1), its SIXTEEN circle predecessors are

`x_j=(z+j)/16=(a+jM)/(16M)`, `0<=j<16`.

A predecessor belongs to the odd-denominator subgroup if and only if `16 | a+jM`, since any surviving power of 2 in the reduced denominator is forbidden. Because M is odd, this has a UNIQUE solution

`j_*(z) = -a * (M^-1 mod16) mod16`.

Thus the original source's **affine** arrow `F_n(x)=16x+r(n+1)` has exactly one rational odd-denominator predecessor at every rational y for which `(y-r(n+1)) mod1` has odd reduced denominator. On an ACTUAL source transition `y={U_(n+1)}` this odd predecessor equals `{U_n}` and `j_* = floor(16{U_n})`. This is a proof on every source time, not only a finite test.

The odd-rational inverse does NOT extend continuously to the ordinary real circle. For `k>=1`, `y_k=1/(16k-1)->0` in R/Z, but its unique odd predecessor is `k/(16k-1)->1/16`; meanwhile the predecessor of 0 is 0. Consequently **the arithmetic finite-stage inverse and the real-circle completion do not commute**.

The original `M_N=lcm_{1<=j<=N}den(r(j))` is odd, and all actual source transitions live in its finite cyclic carrier at horizon N. The selected inverse branch is canonical as *2-integrality*, not a preference for a low-complexity or aesthetically pleasing lift. Canonical finite selection does not imply real equidistribution.

## CE-02 — The natural extension is a genuine solenoid (CLASSICAL)

For the AUTONOMOUS map T on the real circle, its natural extension is

`Sigma_16 = {(x_0,x_{-1},...): 16*x_{-j-1}=x_{-j} mod1}`, an inverse-limit compact group.

The shift is invertible; projection onto x_0 forgets the prehistory. Its fiber over x_0 is a torsor for `Z_16 ≅ Z_2` as compact totally disconnected topological groups (16-adic and 2-adic topologies agree). The odd-rational inverse defines a source-specific algebraic selection of a single prehistory on the dense odd-torsion subgroup, but CE-01 shows this selection is NOT continuous in the real-circle metric. The source-forced nonautonomous arrows need their own time labels and are not silently declared a solenoid automorphism.

References: https://ncatlab.org/nlab/show/solenoid ; Nekrashevych lecture notes https://people.tamu.edu/~nekrash/teaching/15S/part3.pdf . The construction is classical; no source-selected Haar follows.

## CE-03 — A precise Feynman-SHAPED transfer operator, and its total-averaging trap (CLASSICAL)

For any fixed REAL circle forcing r, define the normalized Perron-Frobenius operator

`(L_r f)(y)=(1/16) Σ_(j=0)^15 f((y-r+j)/16)`.

For every integer harmonic h, direct geometric-series algebra gives

`L_r e_h(y) = 0` when `16 ∤ h`, and `L_r e_h(y)=e_(h/16)(y-r)` when `16|h`.

For the unforced map, `L_0^K e_h = 0` unless `16^K|h`, in which case `L_0^K e_h=e_(h/16^K)`. **Every fixed nonzero harmonic is killed after finite depth.** This does NOT mean any specified trajectory, including the actual BBP trajectory, is Haar. The operator integrates UNIFORMLY OVER ALL inverse branches, not one realized branch. Nor are these positive transfer weights quantum amplitudes.

The selected inverse can nonetheless be reconstructed EXACTLY from 16 Fourier character sectors:

`1_(j=j*) = (1/16) Σ_(q=0)^15 exp(2πi q(j-j*)/16)`.

Consequently the arithmetic-selected inverse operator equals the sum of all 16 Fourier-sector transfer operators, with source-selected weights depending on `j*(z)`; the ordinary uniform branch transfer keeps only q=0. Replacing those coefficients by equal probabilities erases the arithmetic provenance one is trying to prove something about. This is a finite character-sum analogue of a path-amplitude decomposition, NOT a derived physical Feynman integral.

**Exact hostile control:** `x=1/5` is fixed by `×16`, since `16≡1 mod5`. Its unique odd-denominator backward branch is j=3 forever. This selected trajectory is NONNORMAL, while the uniform inverse operator nevertheless kills low Fourier modes. Likewise the SAME ORIGINAL BBP FORCING with different completed initial condition `1/5` (initial U0*=1/5-π/16, preserving four poles but not the marked source) is coherent modulo1 as n→∞ and still has all classical inverse-branch structure. Equal branch interference is NOT original-source cancellation.

Reference: Chen & Volkmer, *On transfer operators on the circle with trigonometric weights*, https://ems.press/content/serial-article-files/37299 .

## CE-04 — Exact electrical-current decomposition of ORIGINAL collision energy (NEW TYPED RESTATEMENT, ALL FINITE EPOCHS)

For any positive integer A, let the genuine original selected empirical measure be

`mu_A=(1/A) Σ_(n=A)^(2A-1) δ_{ {U_n} }`.

For each word `w∈{0,...,15}^k`, define `mu_A(w)` as the mass in the base16 half-open cylinder `I_w=[index(w)/16^k,(index(w)+1)/16^k)`. The consistency law `mu_A(w)=Σ_j mu_A(wj)` is EXACT conservation of current on the rooted 16-ary cylinder tree. This is an **observation tree of real fractions**, not a claim that the source temporal arrow selects every spatial refinement.

Define the normalized collision energy at depth k

`E_k(A)=16^k Σ_(|w|=k) mu_A(w)^2`.

Expand squares and use `Σ_j mu_A(wj)=mu_A(w)`:

`E_(k+1)-E_k=16^(k+1) Σ_(|w|=k) Σ_(j=0)^15 (mu_A(wj)-mu_A(w)/16)^2 >=0`. `(CE-1)`

Since E0=1, an EXACT telescoping gives

`E_K(A)-1=Σ_(k=0)^(K-1) 16^(k+1) Σ_(|w|=k) Σ_j(mu_A(wj)-mu_A(w)/16)^2`. `(CE-2)`

This is a nonnegative orthogonal refinement/dissipation identity (martingale difference / Cauchy-Schwarz). It is independent of any normality hypothesis, and applies to the ACTUAL original source phase sample.

At mesh `m=16^K`, E_K is precisely SUCC #476's real-circle bin collision energy `E_(A,m)=(m/A²)Σ_r count_r²`. Parent #476 proved for ANY growing even mesh m_A<=A that `E_(A,m_A)=o(log m_A)` on all dyadic epochs implies base16 π normality, provided the original selected source. We may choose `K_A=floor(log_16 log A)` for sufficiently large A, so `16^K ≍log A` and `log m_A=K_A log16`. Under this CHOICE, the STILL-OPEN sufficient hypothesis becomes

`Σ_(k<K_A)16^(k+1)Σ_(w,j)(mu_A(wj)-mu_A(w)/16)^2=o(K_A)`. `(CE-3)`

This is exactly equivalent to the original mesh energy hypothesis, NOT a newly proved near-pair saving. The next proof must derive genuine source-selected bounds on the **branch imbalances**, possibly via original carries, old-prime cofactors and Gamma, without assuming equal split currents. An artificial Haar path ensemble always satisfies this and is not evidence about π.

**Finite exact held-out original data** at levels k=0,1,2,3:

```
A      E0          E1           E2          E3
96     1          347/288      11/3        136/3
192    1          599/576      9/4         68/3
384    1          607/576      491/288     71/6
```

These rational energy entries were recomputed from the exact original recurrence and recorded in FINITE_RECEIPT.json; probe.py verifies them independently of the prose. They are not extrapolated to an all-time bound. Finite level-3 m=4096 is undersampled at these horizons. No all-horizon inference.

## CE-05 — A genuine electrical resistance, an exact 2-adic dual, and the limit of the lightning analogy (CLASSICAL)

Give each edge of the homogeneous infinite 16-ary tree unit electrical resistance. By symmetry the unit root current splits into current `16^-k` along each edge at depth k. Its total Thomson energy is

`R_eff=Σ_(k>=1)16^k*(16^-k)^2=Σ_(k>=1)16^-k=1/15`.

This is the effective electrical resistance from the root to infinity (also obtained from the series/parallel law `R=(1+R)/16`). In the DIFFERENT **2-adic** completion, the divergent REAL series `Σ_(k>=0)16^k` converges and equals `-1/15`. Both values share the radix `16` and factor `16−1=3*5`, but they are different observables in different topologies; the ± sign is not a new physical conservation law. All bases b>1 admit this algebra. Real lightning breakdown would also require a source-dependent conductivity/breakdown law; the equilibrium equal-current tree cannot select the original BBP path.

References: Lyons & Peres *Probability on Trees and Networks* https://rdlyons.pages.iu.edu/prbtree/ ; Thomson/Dirichlet variational principles https://link.springer.com/chapter/10.1007/978-3-030-27968-4_2 .

## CE-06 — Independent finite probes, controls and next falsifier

Exact original-source held-out epochs A=96,192,384 and phase/branch indices n=97,193,385,769 are declared in GitHub PREREGISTRATION prior to evaluation. The tests reconstruct the original fractions by both direct Q/Z Fraction recurrence and a wholly separate common-odd-denominator **integer modulus** recurrence. At each true arrow, only one of 16 inverse branches has odd denominator and its label equals the original predecessor's leading hexadecimal cylinder. Full 16-character DFT orthogonality is checked by an exact `Z[X]/(X^8+1)` coefficient oracle, not float complex approximations. Energy CE-1 is checked by an independent explicit 16-child square expansion; positive/negative synthetic controls are included.

**Hostile controls:** full 16-branch Haar remains identically fine for the fixed nonnormal x=1/5; branch-selection section is discontinuous in real topology; point-mass flow has E_K=16^K, while uniform synthetic 16^K samples have E_K=1 at their declared stage. A changed BBP initial seed can retain its forcing and fail source mixing. No source-derived signed Weyl savings, novel quantum speedup, observed lightning mechanism, exact π digit distribution or universal proof is asserted.

**Next verdict-changing probe** (NOT an identity): express the true original source's depth-K_A cylinder branch imbalance in terms of time-adjacent forced branch digits and its **complete original p-free cofactor + signed Gamma boundary flux**, then prove a quantitative cancellation/sparsity estimate o(K_A). Synthetic uniform path weights, source-averaged Galois phases, source-independent branch entropy, or same-forcing wrong-seed invariants are false proof lamps.

### Ledger

- CE-01: disclosed classical 16-branch/unique odd-inverse formula; actual source specialization exact all times.
- CE-02: classical solenoid natural extension, mathematical type separate from time-inhomogeneous forced source.
- CE-03: classical Fourier transfer operator and exact arithmetic 16-sector projection; uniform-to-selected inference refuted by 1/5 periodic control.
- CE-04: disclosed all-finite current splitting / orthogonal collision energy identity; source-selected o(K_A) hypothesis still UNVERIFIED.
- CE-05: classical electric resistance and 2-adic sums, unrelated proof channels with generic radix root.
- CE-06: finite tests observed at their exact scopes, not universal verification.
- PI NORMALITY, RH, physical QM and real electrical light-speed claims: OPEN / not claimed.

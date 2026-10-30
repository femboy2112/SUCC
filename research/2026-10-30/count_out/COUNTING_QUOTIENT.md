# Operation Count-Out — quotienting self-counting without deleting the source or selected seed

**Date:** 2026-10-30. **Authority:** DRAFT mathematical research, intended as a child of SUCC Noether/radix Ward PR #404 at exact head `419cf7c280e7be11542ecbd6edef6c70fa7050e5`, itself descended from #402/#397 and merged Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. Nothing changes in the original four signed BBP poles, selected `U_0=0`, archived theorems, production, existing branches, workflows or main. **π base-16 normality, RH remain open.**

## 0. Author's steelman: "SUCC counting through itself is just counting; quotient out counting to see what's left"

An internally self-modeling observer must distinguish universal counting, path multiplicities, source-dependent geometry and *selected* realized information. Counting the number of ways a path could have been visited is not itself evidence that the actual selected arithmetic orbit is equidistributed. Make this assertion mathematically sharp in three **distinct** quotients, testing what each preserves:

1. **Time-counting / twisted coboundary quotient:** remove the universal affine radix-16 expansion from the forced recurrence by its unique bounded future source correction; identify the remaining selected boundary charge.
2. **Finite-path permutation quotient:** remove the universal binomial orbit multiplicity from SUCC's shared-source Bernoulli virtual field, retaining source labels and non-counting chronology in a separate fiber.
3. **Haar seed-counting moment subtraction:** subtract the completely universal 34th-moment counting baseline from #404 and calculate the exact first source-dependent signed residual and its all-N asymptotic.

These three are NOT equivalent operations and may not be silently conflated or treated as physical symmetries. A quotient that destroys actually witnessed carry/digit data violates the user's no-discard operational contract. Every quotient must name its target property and preservation proof.

## CQ-01: the affine time dynamics really IS pure counting after a bounded cohomological correction — EXACT

Use the unchanged original signed four-pole source
\[
r_n=R(8n-7),\quad R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\quad U_{n+1}(s)=16U_n(s)+r_{n+1}.
\]
Define the original future Green tail
\[
T_n=\sum_{j\ge1}16^{-j}r_{n+j}>0,\quad T_0=\sum_{j\ge1}16^{-j}r_j=\pi/16.
\]
The sum is absolutely convergent and T_n tends to 0. The *twisted-coboundary* equation and its precise source-to-counting conjugacy are
\[
\boxed{r_{n+1}=16T_n-T_{n+1}},\qquad
\boxed{V_n:=U_n+T_n\quad\Longrightarrow\quad V_{n+1}=16V_n}.\tag{CQ1}
\]
Thus for every real seed s,
\[
\boxed{U_n(s)=16^n(s+\pi/16)-T_n}.\tag{CQ2}
\]
**Uniqueness:** Any bounded real solution B_n of `16B_n-B_(n+1)=r_(n+1)` differs from T_n by a homogeneous solution C16^n; boundedness forces C=0. This is a bounded **mathematical coordinate corrector**, not a claim that an actual finite observer physically stores an exact infinite real. If one demands *both* boundedness and strict preservation of the marked initial coordinate B_0=0, this gauge removal is impossible because the unique bounded corrector has B_0=π/16>0. Allowing an unbounded corrector B_n=-U_n(0) instead removes the forcing without moving U_0 but explicitly violates the bounded-corrector condition. That is an exact **relative boundary obstruction**: the source information has moved into the global selected initial value, not been destroyed.

**The boundedness/boundary/forcing trilemma (exact):** If we refuse to move the marked initial condition, we may instead use the *past-generated* counterterm `B_n=-U_n(0)`, with `B_0=0` and `B_(n+1)=16B_n-r_(n+1)`. Then `U_n(s)+B_n=16^ns`, so source forcing is again removed while the zero seed remains at zero. But `|B_n|=16^n(π/16)-T_n` grows exponentially. Therefore there is **no correction simultaneously satisfying** (i) bounded time coordinate, (ii) unchanged original zero boundary, and (iii) complete removal of the forcing. We can have any two, not all three. This is a mathematical precision/transport tradeoff, NOT a theorem that a physical observer must store exponentially many independent random bits. A finite observer may compute successive values of B_n with increasing resources; the unique bounded future correction uses the global source law and is not a finite causal memory state unless approximated with a certified truncation.

On the circle, `y_n={V_n}={16^n(s+π/16)}`. Let `x_n={U_n}`, `eta_n=floor(x_n+T_n)`, `d_(n+1)=floor(16 y_n)` and `kappa_(n+1)=floor(16x_n+r_(n+1))`. Then the exact **integer seam/carry cocycle** is
\[
\boxed{\kappa_{n+1}=d_{n+1}+16\eta_n-\eta_{n+1}}.\tag{CQ3}
\]
Removing this twisted counting seam is lossless ONLY if eta and the radix branch metadata are retained. The coherent same-forcing counterseed `s_*=-π/16` has y_n=0 for all n yet the original positive source is unchanged. So removing the local counting evolution does NOT establish π normality; it isolates the still-unproved arithmetic property of the selected global boundary α=π/16.

**A finite EXACT anti-epicycle probe:** for finite horizon M, use truncated `T_n^(M)=Σ_(j=1)^(M−n)16^−j r_(n+j)`, with T_M^(M)=0. Every finite identity above is exact for n<M using α_M=s+T_0^(M). For artificial coherent seed s=−T_0^(M), the last carry at terminal n=M is **16** rather than 15 because the truncation forcibly makes T_M zero. The genuine infinite future-tail s*=−π/16 has strictly positive T_n and carry 15 at every step. Thus *cutting off the future* can fabricate a terminal carry defect: preserving the boundary and source passport is load bearing.

This exact future-tail conjugacy and integer seam are inherited from prior SUCC PRs #390/#396/#400; the bounded-marked quotient perspective and initial-boundary incompatibility are specialized here, not claimed independent discovery of the formula.

## CQ-02: universal combinatorial path counting is a legitimate quotient for source likelihood, not for realized history — EXACT

Under the authentic source `μ_(a_n)(dx)=exp(−a_nx)Q(x)dx/R(a_n)`, `a_n=8n−7`, consider three **declared** source-retained panels of n Bernoulli probes, all conditional-i.i.d. with success `p(x)=1−exp(−8x)`. Let the full actually observed binary word be `ω∈{0,1}^{3n}` and grade `s=|ω|`. A single EXACT word has probability
\[
\boxed{b_{n,s}=\frac{1}{R(a_n)}\sum_{j=0}^s(-1)^j{\binom{s}{j}}
R\big(a_n+8(3n-s+j)\big)}.\tag{CQ4}
\]
This depends on ω ONLY through its number of ones. The symmetric group S_(3n) acts transitively on the words of grade s, with orbit size `binom(3n,s)`. Hence
\[
\boxed{P(S=s)={\binom{3n}{s}}b_{n,s},\qquad
P(\omega\mid S=s)=1/\binom{3n}{s}.}\tag{CQ5}
\]
The *counting-only factor* `binom(3n,s)` is universal and can be divided out if the question only concerns source likelihood or latent X. A positive **Oily–Macaroni** reweighting D_s of the total grade does NOT change `P(ω|S=s)` because its factor cancels conditionally. The same is true for any Gamma-matched positive-source fake using the identical conditional-i.i.d. observation grammar.

**No-discard/crucible:** A signed observation `F(ω)` is legitimately computable solely from the quotient s iff it is invariant under the S_(3n) permutations. SUCC's actual three-time intermediate carry map is **not** invariant. At n=3, the virtual triple grades (1,0,0),(0,1,0),(0,0,1) all have s=1 yet the authentic selected original carries are `(3,3,3)`, `(4,3,3)`, `(4,4,3)` respectively. Each grade pattern has exactly three underlying words, so given s=1 the three carry-history classes each have probability 1/3 under this declared observer, independent of Q and of grade-only Oily weighting.

Thus the honest lossless decomposition is
\[
\text{word}\ \longleftrightarrow\ (s,\text{rank within the }\binom{3n}{s}\text{-element fiber}),
\]
with conditional chronology entropy `log_2 binom(3n,s)` for the witnessed full word, as long as the observation contract actually includes that word. A merely grade-only instrument never witnessed the detailed chronology and does not owe a fictional record. With a source-atom mark D∈{3,4,5}, the quotient can retain its rational posterior `P(D|S=s)`; the detailed word remains uniform within the fiber conditional on S and D. This is a **source-positive** distinction, not a π-digit law.

## CQ-03: subtracting the universal 34th-moment counting background yields a genuine source-dependent residue — EXACT ALL N

Let `e(x)=exp(2πix)`, integer h≠0, and
\[
W_N(s;h)=\sum_{n=1}^N e(hU_n(s)),\quad
M_{N,17}(h)=\int_0^1|W_N(s;h)|^{34}ds.
\]
Parent PR #404 proves the complete radix-16 17-equal-length collision classification:
\[
M_{N,17}=D_{N,17}+2\sum_{2\le p<q\le N}a_{pq}\cos(2πh(r_q-r_p)),
\]
where `D_(N,17)=Σ_(m1+...+mN=17) (17!/(Πm_i!))²`, and `a_pq=17` if q=p+1 and 289 otherwise. Define the **pure-counting baseline** by setting all coherent collision phases to 1:
\[
M_{N,17}^{\rm count}=D_{N,17}+2\sum_{p<q}a_{pq}.
\]
The **quotient defect** after subtracting this universal counting baseline is the nonnegative quantity
\[
\boxed{\mathfrak D_{N,h}:=M_{N,17}^{\rm count}-M_{N,17}
=2\sum_{2\le p<q\le N}a_{pq}[1-\cos(2πh(r_q-r_p))].}\tag{CQ6}
\]
No Fourier cancellation or normality assumption enters.

**Exact O(N) reduction, with no huge floating-point moment subtraction.** Put `m=N−1` and define three finite source series
\[
A_{N,h}=\sum_{p=2}^N[1-\cos(2πh r_p)],\quad
S_{N,h}=\sum_{p=2}^N\sin(2πh r_p),\quad
B_{N,h}=\sum_{p=2}^{N-1}[1-\cos(2πh(r_{p+1}-r_p))].
\]
Set `Z=Σ_(p=2)^N exp(2πi h r_p)=m−A+iS`. The elementary identity `Σ_(p<q)cos(arg(z_q/z_p))=(|Z|²−m)/2` yields
\[
\boxed{\mathfrak D_{N,h}
=578(N-1)A_{N,h}-289(A_{N,h}^2+S_{N,h}^2)-544 B_{N,h}.}\tag{CQ7}
\]
This is an exact full source identity requiring only O(N) real arithmetic. It isolates the **source dephasing** residual that universal radix counting hides beneath the huge moment `D_(N,17)=Θ(N^17)`.

## CQ-04: the quotient defect has a universal-in-N source-specific linear law with an explicit constant — PROVED FOR EACH FIXED h

Because `0<r_n≤15/(8n-7)^2`, the following series converge absolutely for each fixed nonzero integer h:
\[
A_h=\sum_{p\ge2}[1-\cos(2πh r_p)]>0,\quad
S_h=\sum_{p\ge2}\sin(2πh r_p),\quad
B_h=\sum_{p\ge2}[1-\cos(2πh(r_{p+1}-r_p))].
\]
The sums satisfy `A_h−A_(N,h)=O_h(N^−3)`, `S_h−S_(N,h)=O_h(N^−1)`, `B_h−B_(N,h)=O_h(N^−3)`. Therefore CQ7 yields the **stronger-than-previous-round theorem**:
\[
\boxed{\mathfrak D_{N,h}=578N A_h+C_h+O_h(N^{-1}),}\tag{CQ8}
\]
\[
\boxed{C_h=-578A_h-289(A_h^2+S_h^2)-544B_h.}\tag{CQ9}
\]
No rates are uniform over h growing with N. A_h>0 for each h≠0 because all sufficiently large `0<|h|r_p<1` so at least one (indeed all sufficiently late) phases is nontrivial.

**Real high-precision independent source-holdout, h=1:** `A_1=0.36236676355054...` (tail < 4.52×10^−14), `S_1≈1.497553814441517...`, `B_1≈0.157417231288605...`, `C_1≈−981.1623446123` (conservative error < 10^−9), coefficient `578 A_1≈209.447989332...`. The A_1 truncated series at p≤20000 has the elementary certified tail <`4.52×10^−14` using `1−cos x≤x²/2` and `r_p≤15/(8p−7)^2`; do not quote more proven decimals than this error permits. A true O(N) residual does not imply the original selected N-term signed sum is o(N).

## CQ-05: the *harmonic/Gamma* structure emerges from subtracting harmonic pole counting

The exact original source unweighted pole sum is finite because its coefficients sum to zero:
\[
\boxed{S_R:=\sum_{n\ge1}r_n
=-\frac18\big[4\psi(1/8)-2\psi(1/2)-\psi(5/8)-\psi(3/4)\big],}\tag{CQ10}
\]
where `ψ=Γ'/Γ` is the digamma function. The Euler–Mascheroni constant terms cancel in this **particular** linear combination (sum of signed coefficients zero). This is a classical digamma summation specialized to the exact original four poles, not a new gamma theorem.

The same counting/reindexing identity appearing in earlier SUCC #400 yields the exact source-specific Green-memory budget
\[
\boxed{\sum_{n\ge1}T_n=(S_R-\pi)/15=0.0162969977338265\ldots.}\tag{CQ11}
\]
So summing the source poles in their native clock versus summing their geometric BBP-weighted contributions differs by a **finite, source-specific memory remainder**. This is a particularly faithful mathematical instance of the author's harmonic/Gamma/Oily "counting of counting then quotient the overhead" intuition.

The sine series has a rapidly convergent digamma-corrected evaluation:
\[
S_h=2πh(S_R-r_1)+\sum_{p\ge2}[\sin(2πh r_p)-2πh r_p],\qquad r_1=47/15,
\]
where the correction summand is `O_h(p^-6)`. This produces an independently calculable signed remainder without assuming digit normality. It is still independent of absolute seed because the 34th moment is Haar-averaged.

## CQ-06: three exact limits of the quotient, and why none is normality by itself

1. **Bounded-corrector quotient:** the source vanishes from local affine evolution but survives as the global selected boundary `α=s+π/16`. The same forcing with coherent `s*=−π/16` gives α=0 and nonnormal pure digits. The admissible mathematical bounded-coordinate change does NOT preserve U_0=0 as the new zero coordinate.
2. **Permutation/grade quotient:** the source likelihood collapses to total grade and source-mark proportions; realized carry/phase chronology is NOT invariant and cannot be erased by the quotient without losing observational information. Grade-only Oily weighting changes no conditional permutation-fiber distribution.
3. **Haar Ward counting subtraction:** the first residual \mathfrak D_{N,h} is source-specific and nonnegative with a sharp linear asymptotic, but it **remains seed-blind** because integrating over all s is translation invariant. There is no selected Weyl saving. Other sources with the same forcing can share the quotient; the exact original and coherent counterseed agree on its value for all N.

An even more severe no-go: the preimage-averaging Perron–Frobenius operator of `T_16(x)={16x}` is
\[
(\mathcal L f)(x)=\frac1{16}\sum_{j=0}^{15}f((x+j)/16).
\]
For Fourier `e_h(x)=exp(2πihx)`, `L e_h=0` whenever 16∤h. Yet the **individual coherent selected orbit** α=0 has `e_h(T_16^n 0)=1` for every n. The operator has removed *branch counting* by averaging over sixteen preimages, but that averaging destroys the exceptional selected orbit. This is a direct counterexample to proving normality by applying only an unconditional universal counting transfer operator. (Classical transfer-operator context: https://marshareb.github.io/Perron-Frobenius-Operator/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC8306100/ .)

Finally #404's shrinking seed cylinder `I_N=[0,16^-N]` gives a source-independent bound `sup_(s∈I_N)|W_N(s;h)-W_N(0;h)|≤32π|h|/15`. Thus the locally normalized **second** moment satisfies
\[
\boxed{\frac1{N^2|I_N|}\int_{I_N}|W_N(s;h)|²\,ds
=\left|\frac{W_N(0;h)}N\right|²+O_h(1/N).}\tag{CQ12}
\]
This is a valid selected-seed preserving *criterion*, but not a new saving: it is equivalent to the original Weyl problem. Dividing out global counting and retaining selection restores the exact original missing difficulty.

## Verdict and next discriminating instrument

**DISCLOSED/classical:** unique bounded future-tail conjugacy and nonzero fixed-boundary obstruction; exact three-panel group-orbit counting factor and chronology loss; new exact O(N) first 34th-moment counting-subtracted source defect and sharp `578 N A_h+C_h+O_h(1/N)` asymptotic; original digamma/Gamma–Green source-memory identity; transfer-operator null counterexample and selected shrinking-cylinder second-moment equivalence. Novelty asserted only *within the current SUCC program*, not academic priority.

**REFUTED as implications:** self-counting quotient automatically chooses zero seed; Oily grade normalization adds order-sensitive knowledge; source-only Haar moments, nonzero dephasing energy or conservation laws establish π normality; transfer-operator Haar averaging preserves all selected trajectories.

**UNVERIFIED:** an original-source-and-marked-zero-boundary signed nonproduct carry/phase estimate that survives counting subtraction, predicts behavior on unseen expanding windows and yields a genuine selected o(N) estimate (or the stronger O_h(N^(1−δ_h)) bound); any physical spacetime interpretation and RH. The latest sister arithmetic program #403/#405 proves genuine logarithmic selected saving but not positive density; no source-only or quotient identity here supersedes it.

**Next falsifier:** Define a path-conditional (not Haar-seed-averaged) source/carry/phase observable with (i) counting quotient and lossless fiber record, (ii) exact seed-local window I_N, (iii) full original four signed poles and selected U_0=0, (iv) real/p-adic CRT common-basis transport, and (v) a source-locked bound that distinguishes the original zero-seed orbit from coherent `s*=−π/16`, wrong Γ-matched/higher-jet-matched sources and nonnormal periodic controls but passes genuine normal Stoneham 3/5 cases. A result only equivalent to `W_N(0;h)=o(N)` earns no promotion.

**Execution authority:** focused exact stdlib Fraction checks, independently authored SymPy/mpmath 60-digit source oracle, rigorous tail bound for displayed A_1, exact source Git hashes, receipts. Full root SUCC gates, hosted CI, Lean and external peer review have NOT been run on this additive research branch. Do not merge blindly.

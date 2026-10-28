# SUCC Inside-Out — Typed Lambda Calculus, Source-Selected Inverse Branches and a Conditional Fourier Gate

**Date:** 2026-10-26. **Integration parent:** `research/oily-macaroni-totient-third-shadow-2026-10-26` at `a8c7c85b7a1900d422090f1757c174e7aac69f44` (draft PR #310), already stacked through draft #309 onto #306. Original Main XI ancestor `6dd80730c3575d91f746546a25da5aedbd2e2737`. **Research-stage; not main; π base-16 normality and RH OPEN.** This document proves classical functional/finite-Fourier identities and new-to-project exact source interfaces, and isolates the open arithmetic estimate. No new published mathematical priority or physical virtual-particle claim.

## 0. The author's intuition, steelmanned

> Turn the mathematical fields inside out: regard values as operations and operations as values. The same arithmetic reality can be described as recursive evolution of a point, pullback of an observable, a collection of possible inverse paths, or a source-indexed distribution on those paths. Their meaning may converge without their formulas looking similar. Keep the source-selected path and ask why the mathematical potential of alternatives should constrain the one realized orbit.

**Strongest defensible construction:** use (i) the finite-set exponential/curry adjunction (typed λ calculus), (ii) Koopman pullback of observables along authentic BBP successor, (iii) its Haar-conditional Perron–Frobenius preimage transfer, and (iv) exact source-witness data distinguishing one realized predecessor from 16 equally weighted possible predecessors. Compare with the auxiliary Möbius/Oily–Macaroni packet grade law. Produce an exact selected-phase inequality whose unproved hypothesis is exposed and tested.

**Not allowed:** replacing one realized preimage with 16 uniformly sampled ones, replacing a source-indexed law by a coincident scalar, or claiming that root-of-unity orthogonality proves selected π digits are normal.

## 1. Immutable arithmetic source

For ordinary positive integers, retain without modification

$$
 r(n)=\frac{4}{8n-7}-\frac{2}{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
 U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

The real-circle observable is $x_n=\{U_n\}\in\mathbb R/\mathbb Z$. The authentic exact Green-tail theorem, already in main, gives

$$\left|\sum_{n=1}^N e(h16^{n-1}\pi)-\sum_{n=1}^N e(hU_n)\right|<\frac{119}{648}|h|,$$

where $e(t)=e^{2\pi i t}$. The only target is

$$\forall h\ne0:\quad A_N(h)=\frac1N\sum_{n=1}^N e(hU_n)\longrightarrow0.$$

The same source integral has $r(n)>0$, and the original positive moment kernel $P(t)=(1-t)B(t)$, $B(t)\le15$ on $[0,1]$, implies

$$\sum_{n\ge1}r(n)=\int_0^1\frac{P(t)}{1-t^8}\,dt\le15.$$

This summability is used only for an explicit approximate-invariance budget. It does **not** itself imply cancellation.

## 2. Values as operations: an honest finite internal language

On finite sets, the evaluation arrow $\mathrm{ev}:Y^X\times X\to Y$ and currying establish

$$\operatorname{Hom}(A\times X,Y)\cong\operatorname{Hom}(A,Y^X).$$

The implementation **reuses** `beck_chevalley_source.FiniteMap` and `finite_map`; it does not create a competing category or generic lambda interpreter. A bounded `ChurchIterator(n)` interprets a natural number as $n$ applications of a declared finite endomorphism. An unbounded/untyped lambda interpreter would bring no arithmetic theorem.

The BBP recurrence is *nonautonomous*. One Church numeral applied to an arbitrary fixed affine operation on the circle cannot be substituted for the actual sequence of source operations $T_n(x)=16x+r(n+1)$; the source tape $n\mapsto r(n+1)$ is a first-class component.

## 3. Operator inversion and the exact root-of-unity theorem

At authentic source time $n$, define $T_n(x)=16x+r(n+1)\pmod1$. On Fourier characters $\chi_h(x)=e(hx)$, Koopman pullback is

$$\boxed{\mathcal K_n\chi_h=e(hr(n+1))\chi_{16h}.}$$

Relative to Haar measure, the 16-to-one normalized inverse transfer is

$$\mathcal P_nf(y)=\frac1{16}\sum_{j=0}^{15}f\left(\frac{\{y-r(n+1)\}+j}{16}\right).$$

The source shift is retained, and an elementary character sum proves

$$\boxed{\mathcal P_n\chi_h=\begin{cases}0,&16\nmid h,\\e(-(h/16)r(n+1))\chi_{h/16},&16\mid h.\end{cases}}$$

Consequently, **on finite Fourier polynomials**,

$$\boxed{\mathcal P_n\mathcal K_n=I,\qquad \mathcal K_n\mathcal P_n=\Pi_{16\mathbb Z},}$$

where $\Pi_{16\mathbb Z}$ deletes every Fourier mode not divisible by 16. The same formulas extend on appropriate $L^2$ spaces by standard continuity. This is classical; exact finite rational root-of-unity arithmetic is implemented in $\mathbb Q[\zeta_{16}]\cong\mathbb Q[X]/(X^8+1)$.

**Crucial representation firewall:** formal basis symbols in the group algebra $\mathbb Q[\mathbb Q/\mathbb Z]$ do not automatically satisfy cyclotomic cancellation. To certify $\sum_{j=0}^{15}\zeta_{16}^{hj}=0$, quotient by the cyclotomic relation; `Cyclo16` uses eight exact rational coordinates. A formal sum that evaluates to zero as a complex character is not necessarily zero as a formal source-witness sum.

**No-go:** $\mathcal P_n$ uses an *equal-weight inverse ensemble*. The authentic orbit is an actual single source-selected history. Equality of the two would assume a conditional-uniformity law, which is the missing input. For the pure map $x\mapsto16x$, Haar and the fixed Dirac mass at zero are both invariant, but the latter has nonvanishing Fourier coefficients. Hence operator commutation, positivity and approximate invariance do not select Haar.

## 4. The authentic inverse branch carries the literal integer carry

For the realized $x_n$, define the digit and future remainder **exactly**:

$$j_n=\lfloor16x_n\rfloor\in\{0,\dots,15\},\qquad t_n=\{16x_n\}=\{x_{n+1}-r(n+1)\}.$$

Then

$$\boxed{x_n=\frac{j_n+t_n}{16},\qquad e(hU_n)=e\left(\frac{h t_n}{16}\right)\zeta_{16}^{h j_n}.}$$

The real integer carry is not silently replaced by $j_n$:

$$\boxed{c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor=j_n+\lfloor t_n+r(n+1)\rfloor.}$$

The testable `BranchWitness` retains $j_n$, $t_n$, original rational forcing, literal carry, and the common source-forcing conductor through $n+1$. Authenticity requires the **entire zero-selected original recurrence**, not a string label. Any changed seed/forcing fails that check.

The $j_n$ values are **not** the graded packet labels $J$ of PR #310. Their relationship is an outstanding map to construct, not an identification to declare.

## 5. Finite conditional χ² and the first certified selected-Weyl inequality

Fix a horizon $N$ and an integer $M\ge1$. Bin each $t_n$ into $I_b=[b/M,(b+1)/M)$, $b=0,\dots,M-1$. Define integer cell counts

$$n_{bj}=\#\{1\le n\le N:\; t_n\in I_b,\;j_n=j\},\qquad n_b=\sum_{j=0}^{15}n_{bj}.$$

For $n_b>0$, the empirical conditional distribution is $w_{bj}=n_{bj}/n_b$. Let $u_j=1/16$ be the **comparison Haar branch law**, not an asserted authentic law. Define the exact rational defect

$$\boxed{\Delta_{N,M}=\sum_{b:n_b>0}\frac{n_b}{N}\sum_{j=0}^{15}\frac{(w_{bj}-1/16)^2}{1/16}
=\frac{16}{N}\sum_{b:n_b>0}\sum_j\frac{(n_{bj}-n_b/16)^2}{n_b}.}$$

No complex approximations or source oracle are used to evaluate $\Delta$. Its range is $0\le\Delta\le15$, where 0 means uniform branch distribution in every occupied tail cell. The exact conditional cyclotomic spectrum is

$$F_b(h)=\sum_j w_{bj}\zeta_{16}^{hj},\qquad E_{N,M}(h)=\sum_b\frac{n_b}{N}|F_b(h)|^2.$$

By finite Fourier Parseval,

$$\boxed{\sum_{h=1}^{15}E_{N,M}(h)=\Delta_{N,M}.}$$

Choose midpoint $\tau_b=(b+1/2)/M$. On $I_b$, $|t-\tau_b|\le1/(2M)$, so using $|e(a)-e(b)|\le2\pi|a-b|$:

$$\left|A_N(h)-\sum_b\frac{n_b}{N}e(h\tau_b/16)F_b(h)\right|\le\frac{\pi|h|}{16M}.$$

For $16\nmid h$, uniform reference character $\sum_j u_j\zeta^{hj}=0$; conditional Cauchy–Schwarz gives $|F_b(h)|\le\sqrt{\chi^2(w_b\|u)}$. A second Cauchy–Schwarz therefore proves

$$\boxed{|A_N(h)|\le\sqrt{E_{N,M}(h)}+\frac{\pi|h|}{16M}
\le\sqrt{\Delta_{N,M}}+\frac{\pi|h|}{16M}\quad(16\nmid h).}$$

**This inequality is finite, fully explicit, source selected and valid for every rational history.** The code returns an **outward rational** upper bound replacing the irrational square root by an exact integer-isqrt enclosure and $\pi<22/7$. It has not proved that either energy is small.

### Explicit Z/16 → Z/2 shadow

For $h=8$, $\zeta_{16}^{8j}=(-1)^j$, and the mode energy itself becomes an exact rational:

$$\boxed{E_{N,M}(8)=\sum_{b:n_b>0}\frac{(n_b^{\rm even}-n_b^{\rm odd})^2}{N n_b}.}$$

This is a particularly clean finite version of the author's earlier $0\to\mathbb Z/16\to\mathbb Z/2\to0$ intuition, while retaining actual BBP selection and future conditioning. **Parity balancing within the future fibers** is what is needed for this character; parity counts alone are not enough.

## 6. The source's almost-invariance pays for every 16-divisible mode

The recurrence gives

$$e(16hU_n)=e(hU_{n+1})e(-h r(n+1)).$$

Sum from $n=1$ to $N$, telescope the endpoints, and use $\sum_{n\ge1}r(n)\le15$:

$$\boxed{|A_N(16h)-A_N(h)|\le\frac{2+30\pi|h|}{N}
<\frac{2+660|h|/7}{N}.}$$

Hence for $h=16^k m$, $16\nmid m$, iterating the prior bound yields the **all-frequency source-selected certificate**

$$\boxed{|A_N(h)|\le\sqrt{\Delta_{N,M}}+\frac{\pi|m|}{16M}
+\frac1N\sum_{i=0}^{k-1}(2+30\pi|16^i m|).}$$

The implementation uses strict rational outer bounds, so it certifies each finite original rational orbit without a numerical π oracle. This is a *conditional estimate*; the hard part of showing $\Delta_{N,M}$ decays is separate.

## 7. Exact reformulation of π normality — NOT a proof

**Theorem (classical ergodic criterion, new SUCC interface).** For the original zero-initialized four-pole BBP source, the following are equivalent:

1. π is normal in base 16.
2. The original selected rational states $x_n=\{U_n\}$ are equidistributed on the real circle.
3. There exists an integer schedule $M_N\to\infty$ for which $\Delta_{N,M_N}\to0$.

**(3)⇒(2):** For fixed $h$ with $16\nmid h$, apply §5. For any other fixed nonzero h, strip its finite power of 16 using §6. Weyl's criterion gives equidistribution.

**(2)⇒(3):** For every fixed $M$, each source cell $(b,j)$ is an interval of length $1/(16M)$ in the observed $x_n$ circle. Equidistribution implies $n_{bj}/N\to1/(16M)$, whence $\Delta_{N,M}\to0$. Choose thresholds $N_M$ so the defect is $<1/M$ for all $N\ge N_M$, then take an arbitrarily slowly growing diagonal schedule $M_N$. This is a legitimate existence argument **assuming equidistribution**, not a practical predefined rate.

The equivalence is honest but circular as a *proof program*. **A new source-specific, independently established $\Delta_{N,M_N}=o(1)$ estimate for an explicit admissible growing schedule would prove π normality.** This is the actual arithmetic debt, now expressed as an inverse-branch conditional mixing estimate instead of an unexplained Fourier sum.

A stronger possible target is to estimate the selected mode energy $E_{N,M}(h)$ for each primitive fixed h, not the full χ²; that is a weaker, more phase-sensitive condition. The code exposes its exact $\mathbb Q(\zeta_{16})$ representation, but no smallness theorem.

## 8. Why the Oily–Macaroni packet law does not fill the missing slot

The exact PR #310 endpoint grade distribution $w_J=(J+1)/2^{J+2}$, **folded modulo 16**, has rational weights

$$p_j=\sum_{m\ge0}w_{j+16m}=
\frac1{2^{j+2}}\left[\frac{j+1}{1-2^{-16}}+\frac{16\,2^{-16}}{(1-2^{-16})^2}\right].$$

Its inverse-branch character, using $z=\zeta_{16}^h$, is exactly

$$\boxed{\sum_{j=0}^{15}p_jz^j=\frac1{(2-z)^2}\ne0.}$$

More sharply, for every $|z|=1$, $1/9\le|1/(2-z)^2|\le1$. The exact χ² value at modulus 16 is

$$\Delta_{\rm packet}=16\sum_jp_j^2-1=\frac{75912489607}{38653526025}\approx1.9639214688>0.$$

After conditioning to **primitive dyadic grades** (odd $J$), we obtain

$$\boxed{F_{\rm prim}(h)=\frac{9\zeta_{16}^h}{(4-\zeta_{16}^{2h})^2},\quad F_{\rm prim}(8)=-1,}$$

and the conditional packet χ² increases to

$$\Delta_{\rm prim}=\frac{65968750207}{11930100625}\approx5.5296055147.$$

**This is a mathematical no-go for silently replacing source-selected inverse branches by the positive Oily–Macaroni packet grade law**: it preserves nontrivial Fourier characters and can even maximize the parity character. It does not refute the usefulness of the packet log/Gamma third-order shadow as a separate source observable; it forbids treating its auxiliary randomness as selected digit-branch randomness without a genuine coupling theorem.

## 9. Hostile counterexamples and finite receipts

- **Exact changed seed:** the same original forcing with $V_0=-\pi/16$ yields $V_n=-T_n\to0$, so its normalized Fourier sums tend to one. Source forcing, positive Gamma measures, atomic BBP coefficients, Oily packet weights and uniform inverse-character algebra are unchanged. The new selected-history verifier rejects an altered rational seed; no finite rational sample is claimed to represent $-\pi/16$ exactly.
- **Haar preimage ensemble vs selected point:** pure $x\mapsto16x$ admits an invariant Dirac mass at the zero fixed point. The uniform inverse ensemble annihilates all non-16 frequencies, but the Dirac orbit has $A_N(h)=1$. This is an unconditional obstruction to inferring selected mixing from a transfer-operator spectral identity alone.
- **Uniform digit marginal but nonuniform conditional branch:** put 16 equally weighted states $x_j=(j+t_j)/16$, with $t_j=0$ for even j and $t_j=1/2$ for odd j. Then $\Delta_{16,1}=0$, but $A_{16}(8)=(1-i)/2\ne0$ and $\Delta_{16,2}=1$. These are synthetic diagnostic states, not a valid authentic BBP trajectory.
- **Source grade ≠ inverse digit:** the Oily packet $p_j$ gives $\Delta_{\rm packet}>0$; primitive conditioning gives a full surviving parity mode $F_{\rm prim}(8)=-1$. Different arithmetic carriers, same modulo-16 label; replacing one with the other is an invalid type coercion.
- **Finite source snapshots:** observed exact defects for the authentic rational orbit decrease on some tested $(N,M)$; such finite samples cannot prove the all-$N$ asymptotic. At $(N,M)=(128,4),(256,4),(512,8)$ the exact parity energies are respectively $1211/40128$, $71243/4493440$, and $154897/31105152$. These are observations, not extrapolated theorems.
- **All-zero character and 16-divisible modes:** $h=0$ never has cancellation and is explicitly rejected; modes divisible by 16 must be handled with the nonautonomous source shift budget, never with the primitive-root annihilation identity.

## 10. Mathematical next cut for Astra Ultra

The new conditional digit/tail criterion places **source-selection** into a finite exact statistic, but doesn't create smallness. A genuine next theorem must, for the authentic zero-seeded four-pole orbit, prove one of:

A. $\Delta_{N,M_N}=o(1)$ for an explicitly justified growing $M_N$, using the **actual BBP source**, its signed Gaussian atoms, conductor growth, zero anchor and carries; OR

B. For every fixed $16\nmid h$, $E_{N,M_N}(h)=o(1)$ (a weaker, selected-mode target), with $M_N\to\infty$ and all errors; OR

C. Another source-authenticated signed Weyl saving with independently proved implication to the original orbit.

Study conditional primitive lifts under the full two-atom source, not only their marginal counts. The short path to a falsifiable estimate is the exact $h=8$ parity energy, then $h=4$ Gaussian quarter-turn and other cyclotomic modes. Compare against changed-seed, matched-moment, carry-preserving and Oily packet-weight controls. Exploit the difference between the two 4-step signs $G^4=-I/4$, $H^4=+I/4$ without pretending it forces absolute branch uniformity. The exact source keeps the fourth-order cross-digit Walsh terms; one-digit parity alone does not complete normality.

Any success must be an **inequality** independent of having already assumed equidistribution. A category diagram, lambda term, commuting-square certificate or maximal-entropy phrase is not sufficient without proof of the source's entropy/mixing estimate.

## 11. Validation and authority

- Production: `observational_succ/lambda_source_duality.py`, using existing native FiniteMap, exact BBP `authentic_r`, and rational source histories.
- Tests: `tests/test_lambda_source_duality.py` — typed curry/uncurry, Church iterations, actual BBP source/history, cyclotomic character algebra, finite chi-squared and selected-Weyl certificates, exact Parseval, parity/CRT controls, changed-seed rejection.
- Probe/receipt: `scripts/lambda_source_duality_probe.py` and `research/2026-10-26/LAMBDA_SOURCE_DUALITY_RECEIPT.json`, exact deterministic JSON with source-module hash, finite history statistics and rejection tests.
- Authoritative proof **paper/classical** for the analytic bounds and equivalence; tests certify exact finite instances. No Lean declaration for the new infinite statement, no claim of RH/π proof or academic originality.
- Local targeted verification uses inspected minimal shims for `FiniteMap` and `authentic_r`; this is NOT native hosted CI. Full source-provenance and hosted exact-head CI must be separately checked. Preserve source originals and attach review only to the research branch.

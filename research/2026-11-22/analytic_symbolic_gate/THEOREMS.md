# The authentic BBP source-to-digit analytic obstruction and the critical Diophantine ceiling

**22 November 2026 · SUCC additive research continuation of draft #685.** This dossier answers a deliberately stricter question: can we prove a nontrivial property of **the single literal-zero-seeded BBP trajectory**, not simply repackage R0, and can we exhibit a known nonnormal control for which it fails? **Yes** for the natural-boundary/source-filter no-go and the quantitative periodic-shadow exclusion. **No** for a signed all-shell bound; R0 and π base-16 normality remain OPEN. Mathematical priority is NOT claimed: classical inputs are explicitly credited, and the deductions are a new-to-SUCC integration.

## Source, types, and imported claims

The target is the original four-pole source, without modification:

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Write `c_n=16^{-n}r(n)`, `x=\sum_{n>=1}c_n=π/16` **by the classical BBP formula**, `θ_n={16^n x}`, and `x=0.d_1d_2\dots` in canonical base 16. No homogenizing seed is silently changed. A real number's irrationality exponent is `μ(x)`; rational multiplication by a fixed nonzero rational preserves that exponent.

External claims, with DIFFERENT provenance statuses:

- **CLASSICAL:** Pólya–Carlson theorem: an integer-coefficient power series of exact radius 1 is either rational or has the unit circle as a natural boundary. (Pólya 1922 / Carlson 1921; see Gerhold, 2005, or modern expositions.)
- **PEER-REVIEWED IMPORT:** D. Zeilberger and W. Zudilin, *The irrationality measure of π is at most 7.103205334137...*, Moscow Journal of Combinatorics and Number Theory 9 (2020), 407–419, DOI `10.2140/moscow.2020.9.407`. The endpoint is a bound, not a claim that the exact exponent is known from that paper.
- **PEER-REVIEWED IMPORT:** The generalized Kempner/Fredholm constants `β_b=Σ_{k>=0}b^{-2^k}`, integer `b≥2`, have irrationality exponent **2**, as summarized in *Continued fractions and irrationality exponents for modified Engel and Pierce series*, Monatshefte für Mathematik 190 (2019), §4 (with earlier primary literature attributed there). We DO NOT claim an in-repository proof of this deep exponent theorem.
- **2026 NOT INDEPENDENTLY REFEREED HERE:** OpenAI, *The irrationality exponent of π is 2*, 24 Sep 2026, released with claimed Lean formalization (`https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026`; `https://github.com/openai/math/blob/main/lean/docs/017.md`). Treat the exponent-two sharpened corollary **CONDITIONAL ON THAT EXTERNAL CLAIM** pending independent specialist verification and scope review. SUCC's unconditional theorem uses the 2020 peer-reviewed bound instead. None of the present tests rebuilds the external Lean artifact.

## AZG-01 — Source analyticity has room beyond the unit circle (INHERITED CLASSICAL; SOURCE SELECTED)

Let `F(z)=Σ_(n>=1)c_n z^n`. The exact signed Mellin polynomial

\[
Q(t)=4-2t^3-t^4-t^5=(1-t)(4+4t+4t^2+2t^3+t^4)
\]

satisfies `r(n)=∫_0^1 t^(8n−8) Q(t) dt`, with `r(n)>0` and `r(n)~15/(64n²)`. Thus the series `F` has exact radius of convergence 16, is analytic on `|z|<16`, and `F(1)=x`. The source complex-frequency transform `F(e^{iω})` is therefore analytic through a complex neighborhood of every point of the unit circle. This reproduces earlier #675/#677 source analytic structure, and is not itself a fresh arithmetic normality estimate.

## AZG-02 — The **actual zero-seeded π digit journal** has a natural boundary (PROVED PAPER from classical imports)

Let

\[
D(z)=\sum_{n\ge1}d_nz^{n-1},\qquad d_n\in\{0,1,\ldots,15\}.
\]

**Theorem.** The radius of convergence of `D` is 1, and **every point** of `|z|=1` obstructs analytic continuation of `D`.

**Proof.** Irrationality of `x=π/16` implies its hexadecimal digit string cannot be eventually periodic; in particular infinitely many digits are nonzero, so the radius of `D` is exactly 1 (boundedness supplies radius at least 1). By Pólya–Carlson, either `D` is rational or has the unit circle as a natural boundary. If `D` were rational, its bounded integer coefficients would satisfy a fixed linear recurrence for all large n. A length-k vector of consecutive digits belongs to a finite alphabet; the recurrence makes the next digit a deterministic function of this vector. Some state eventually repeats, forcing the entire tail eventually periodic. That would make x rational, contradiction. Thus `D` is not rational and has a natural boundary. QED.

**Collatz continuation.** The classical Bernstein–Lagarias 2-adic parity conjugacy in SUCC #681 constructs from these same hexadecimal digits a binary parity stream `ε_0,ε_1,...` with `d_(n+1)=Σ_(j=0)^3 2^j ε_(4n+j)`. Its generating series `E(z)=Σ_(k>=0) ε_k z^k` likewise has the unit circle as a natural boundary: an eventually periodic parity stream would make the four-bit digit stream eventually periodic, contradicting irrationality. This is a property of the *selected symbolic 2-adic companion*, not positive-integer Collatz convergence.

**Scope firewall:** every irrational base-16 expansion enjoys the same natural-boundary deduction, including many nonnormal ones. The theorem DOES distinguish the authentic zero-seeded π trajectory from the exactly locked same-forcing wrong seed (`s=-π/16`), whose digit generating function is zero. It is not a proof of π-normality.

## AZG-03 — No fixed finite-dimensional stationary linear source-to-digit filter (PROVED PAPER; NEGATIVE INSTRUMENT THEOREM)

**Theorem.** There exist no rational functions `R(z)`, `P(z)` with

\[
D(z)=R(z)F(z)+P(z)
\]

as holomorphic germs at zero (allowing removable singularities in the product). More generally there is no fixed finite-dimensional stationary constant-coefficient linear time-invariant source-response realization whose input is the exponentially weighted `c_n` journal and whose output is the exact `d_n` sequence, with only a finite-dimensional homogeneous transient.

**Proof.** The right side extends meromorphically to `|z|<16`, apart from finitely many poles of rational `R,P`. Hence it admits analytic continuation across some open arc of `|z|=1`, avoiding those finitely many poles. AZG-02 says `D` has **no** such arc. Contradiction. Finite-dimensional LTI transfer functions and finite-dimensional homogeneous transients are rational/meromorphic of exactly the proscribed type. Moreover, `D` and the selected parity series `E` are **not D-finite**: a solution of a linear ODE with polynomial coefficients has only finitely many possible finite singularities (zeros of its leading coefficient), contradicting a natural boundary. QED.

**Allowed alternatives:** a nonlinear digit threshold, an infinite-dimensional or time-varying observer, an unbounded-precision carry gate, and correctly source-authenticated feedback are not excluded. A *finite* Fourier basis change of the smooth source journal cannot by itself be the missing statistical estimate. This is a structural failure certificate for proposals that simply identify source-time Fourier modes with real-phase Weyl modes.

**Gaussian caution:** multiplying all digit coefficients by `exp(-λn²/2)`, λ>0, yields an entire function and an unbounded inverse. Such smoothing hides the natural boundary observationally without deleting source coefficients. This extends the existing source-seam Gaussian caution to the **actual digit journal** and does not imply mixing.

## AZG-04 — Quantitative exclusion of excessively long periodic shadows (PROVED CONDITIONAL ON PEER-REVIEWED DIOPHANTINE INPUT)

Fix `ν>μ(π)`. There exists `N_ν` such that the following holds for **all** nonnegative integers n, positive integers p and lengths L whenever `n+p≥N_ν`: if hexadecimal digits `d_(n+1),...,d_(n+L)` agree with a periodic repetition of a block of length p, then

\[
\boxed{L\le(\nu-1)n+\nu p+1.}
\]

**Proof.** Form a rational `y` from the first n hexadecimal digits, followed by indefinite repetition of the p-digit block: if A and W denote the prefix and block integers,

\[
y=\frac{A(16^p-1)+W}{16^n(16^p-1)}=\frac{P}{Q},\quad Q=16^n(16^p-1).
\]

The two numbers share their first `n+L` digits. Thus `|x-y|≤16^{-(n+L)}`. But `π=16x`, so the imported irrationality-exponent bound, at sufficiently large Q, implies

\[
|x-y|=\tfrac1{16}|\pi-16P/Q|\ge\tfrac1{16}Q^{-\nu} \ge16^{-1-\nu(n+p)}.
\]

Combining gives `n+L≤1+ν(n+p)`, hence the inequality. Choosing `N_ν` so `Q≥Q_ν` is valid because `Q≥(15/16)16^(n+p)`. QED.

**Unconditional explicit import:** the peer-reviewed bound `μ(π)≤7.103205334137...` permits any `ν>7.103205334137...`, e.g. ν=7.104. Then, eventually,

\[
\boxed{L\le6.104n+7.104p+1.}
\]

**Sharpened conditional 2026 claim:** if the advertised, independently unreviewed here `μ(π)=2` is accepted with its stated scope, then for any ε>0, eventually,

\[
L\le(1+\epsilon)n+(2+\epsilon)p+1.
\]

Neither statement implies R0: a whole shell of B near-zero digits begins at n≈B and has length L≈B—exactly the *critical scale* that exponent 2 still allows. No fixed universal `c/q²` constant, computable cutoff N, or independent reconstruction of the 2026 Lean theorem is asserted.

**Discriminating nonnormal control:** `β_!=Σ_{k>=2}16^{-k!}` has zero digits between consecutive factorial positions, with runs starting at n=k! and length `L=(k+1)!−k!−1`. For any fixed finite ν this eventually violates the bound above (take p=1 and all-zero block). The control is irrational and nonnormal, with infinite irrationality exponent; the exact same conclusion does **not** hold for it. Its failure is certified symbolically, not by sample digits.

## AZG-05 — The *optimal* irrationality exponent still permits complete R0 failure (IMPORT + NEW EXPLICIT R0 BOUND)

Let

\[
\beta=\sum_{k\ge0}16^{-2^k}\in(0,1).
\]

**Imported published theorem:** `μ(β)=2`, see the generalized Kempner constant reference above. Its hexadecimal digits equal 1 precisely at positions `1,2,4,8,...` and 0 elsewhere, so it is manifestly nonnormal.

**New exact elementary R0 estimate.** Set `B=2^k`, k≥1. For every integer `B≤n<2B`, all powers `2^j≤n` contribute integers to `16^nβ`, and the next surviving one is at position `2B`. Therefore

\[
0<\theta_n=\{16^n\beta\}=\sum_{j:2^j>n}16^{n-2^j}\le\frac{16}{15}16^{n-2B}.
\]

Use `1−cos(2πt)≤2π²t²` and sum a finite geometric series:

\[
\begin{aligned}
\mathcal A_B(\beta)&=\frac1B\sum_{n=B}^{2B-1}\bigl(1-\cos(2\pi\theta_n)\bigr)\\
&\le\frac{2\pi^2}{B}\left(\frac{16}{15}\right)^2\sum_{m=1}^{B}16^{-2m}\\
&\le\boxed{\frac{512\pi^2}{225\cdot255}\frac1B}\longrightarrow0.
\end{aligned}
\]

**Consequently, even the ideal global irrationality measure `μ=2` is NOT sufficient for R0.** The same beta has a natural-boundary digit generating function by AZG-02's classical argument. This kills *both* shortcuts: (i) natural-boundary/infinite stationary Fourier complexity ⇒ R0, and (ii) optimal irrationality exponent ⇒ R0. It also shows why a threshold strictly stronger than the universal Diophantine exponent is needed at the actual source-selected radix scales.

## AZG-06 — Source-selected signed coupling is the **remaining** live proof target (OPEN, not a restatement presented as proof)

The exact zero-seeded `x=π/16` inherits the already proved SUCC #685 two-carry decomposition

\[
d_n=b_n+e_n+\delta_n-16\delta_{n-1},\qquad
\mathcal A_B\ge H_B^{\rm raw}-2D_B-O(1/\log B).
\]

The forcing-kick error `e_n` is paid. What is **not** paid is a source-specific signed estimate on the ordinary raw quarter-sector distribution relative to the future-tail crossings. It must use *actual original zero-seeded* source/prime/cofactor/carry information, be insensitive to no fitted phase shell, and fail appropriately on rational locked and Kempner-type nonnormal controls.

This dossier removes an entire tempting class of false approaches (fixed finite stationary analytic/Fourier filters and general irrationality-measure bounds), and proves nontrivial zero-seed complexity/repetition statements, but gives **no positive all-B original-source R0 constant**. The direct bridge from exact source-root / 2-adic / 3-adic Fourier bookkeeping to a signed real-phase all-shell inequality remains UNVERIFIED. The imported classic theorems and existing SUCC results are not misreported as new discoveries.

## Claim status

- **DISCLOSED within imported classical hypotheses:** AZG-01–04; AZG-05's elementary shell estimate. Imported exponent of β is peer-reviewed and must not be confused with our own computation.
- **CORROBORATED ONLY AS EXTERNAL CLAIM, NOT VERIFIED HERE:** OpenAI's 2026 π-exponent-two paper + released Lean formalization; conditional sharpened cap only.
- **REFUTED with explicit controls:** fixed finite rational transfer from smooth BBP source to actual digit journal; natural boundary ⇒ R0; irrationality exponent 2 ⇒ R0; eventual bounded digit repetition for factorial-Liouville; statistical mixing from Fourier basis changes.
- **UNVERIFIED / OPEN:** signed source-selected anti-locking on all late integer shells, π base-16 normality, general positive-integer Collatz, RH. No physical superfluid/quantum energy claims.

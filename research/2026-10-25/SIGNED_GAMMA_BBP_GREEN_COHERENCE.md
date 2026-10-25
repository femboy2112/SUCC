# Signed Gamma–BBP coherence and the Green-tail orbit bridge

**Date:** 2026-10-25. **Research branch:** `research/signed-gamma-bbp-green-orbit-2026-10-25`. **Pinned parent:** `research/gamma-zero-one-moment-bridge-2026-10-25@c87cc007a72c1754bc20bd399d12b20831d6baeb` (draft #292), itself stacked on the Contextual Zero and Coherent Zero foundations. **Original arithmetic source:** Coherent Main X four-pole BBP recurrence `U_0=0`, `U_{n+1}=16U_n+r(n+1)`. This dossier uses previously documented classical positive moment, digamma, Weyl and BBP facts. These are **new-to-the-repository compositions of classical mathematical arguments**, not a claim of independent scholarly priority. No archive or historical provenance is rewritten. **π normality and RH remain OPEN.**

## 1. Source passport and the mathematical claim

We retain the exact signed four-pole forcing and no substitute:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}>0,\qquad n\ge1.
\]

On the positive unit carrier, put

\[
\delta(x)=\frac1x-\log\left(1+\frac1x\right),\quad
W(t)=\int_0^1(1-t^u)\,du=(1-t)C(t),\quad
P(t)=(1-t)(t^2+2)(t^2+2t+2).
\]

The already verified Gamma/BBP bridge gives the genuine Hausdorff moments

\[
g_k=\delta(8k+1)=\int_0^1t^{8k}W(t)dt,\qquad
b_k=r(k+1)=\int_0^1t^{8k}P(t)dt,\quad k\ge0.
\]

The density ratio \(D(t)=P(t)/W(t)=B(t)/C(t)\) is continuous and **strictly increasing** from 4 to 30 on \([0,1]\). The physical analogy of a virtual field is only an analogy: these are rigorous **source-typed positive measures, transitions and signed residuals**, not a model of actual quantum virtual particles.

## 2. SGO-01–03: a ZERO-ANCHORED SIGNED INTERACTION, at every moment

Let \(a_k=b_k/g_k\). For each natural \(k\), define a finite signed measure

\[
\boxed{d\sigma_k(t)=t^{8k}\big(P(t)-a_kW(t)\big)dt.}
\]

It has exactly zero total mass. Since \(4<a_k<30\), strict monotonicity of \(D(t)\) implies that the signed density crosses zero exactly once: negative at small \(t\), positive near 1. Hence for every strictly increasing continuous \(f\) for which the pairings exist,

\[
\int_0^1f(t)\,d\sigma_k(t)>0.
\]

**Proof:** Normalize \(t^{8k}W(t)dt\) to a probability law \(\mu_k\). Then the pairing is
\(g_k\operatorname{Cov}_{\mu_k}(D,f)\). Its covariance is half the double integral
\(\frac12\iint(D(t)-D(s))(f(t)-f(s))d\mu_k(t)d\mu_k(s)\), strictly positive since both functions are increasing on an interval with full support. This **does not** work for arbitrary complex oscillatory Fourier phases, which are not ordered functions.

Taking \(f(t)=t^{8j}\), for every integer \(j\ge1\), yields the **strict all-index two-source determinant law**

\[
\boxed{b_{k+j}g_k-b_kg_{k+j}>0,
\quad b_{k+j}-a_kg_{k+j}>0.}
\]

Equivalently \(4<a_0<a_1<\cdots<30\). These inequalities are more than positive Hankel Grams: they orient the **source-difference** after a zero-mass calibration, and every higher moment detects it.

The reference \(k=0\) is explicit:
\[
g_0=1-\log2,\qquad b_0=47/15,\qquad
\boxed{a_0=\frac{47/15}{1-\log2}.}
\]

This is the correct use of the additive/logarithmic **unit distinction**—\(\log2\neq1\). Applying the increasing resolvent test function \(f_z(t)=(1-zt^8)^{-1}\), \(0<z<1\), gives

\[
\boxed{\mathcal R_{B,k}(z)-a_k\mathcal R_{G,k}(z)>0,}
\quad\mathcal R_{B,k}(z)=\sum_{j\ge0}z^jb_{k+j},
\quad\mathcal R_{G,k}(z)=\sum_{j\ge0}z^jg_{k+j}.
\]

In particular, since the authentic BBP formula identifies \(\mathcal R_{B,0}(1/16)=\pi\),

\[
\boxed{\pi>\frac{47/15}{1-\log2}
\sum_{j=0}^\infty\frac{\delta(8j+1)}{16^j}.}
\]

The strict difference is approximately 0.0045208596933030558. The executable paper-compatible instrument constructs **outward exact rational** brackets using no floating-point input; depth 12 bounds the difference with width below \(6\cdot10^{-18}\). A true finite signed-memory excess also follows: with \(M_B=\sum_{n\ge1}T_n^B\), \(M_G=\sum_{n\ge1}T_n^G\), and the same positive geometric Green kernel,

\[
\boxed{M_B-a_0M_G=\frac1{15}\sum_{j\ge1}(1-16^{-j})(b_j-a_0g_j)>0.}
\]

The first term alone gives an exact rational lower bound, since \((1-16^{-1})/15=1/16\).

## 3. SGO-04: Euler–Mascheroni is exactly eight SUCC^8 sectors

The full real-positive Euler field at the unit origin is \(\gamma=\sum_{n\ge1}\delta(n)\). Split it into eight residue sectors on the **same natural successor source**:

\[
\boxed{\gamma=\sum_{a=1}^{8}\Gamma_a,\qquad
\Gamma_a=\sum_{k=0}^{\infty}\delta(8k+a)>0.}
\]

This is a completely legitimate cofinal partition of an absolutely convergent positive series: all eight stages together cover every finite integer **exactly once**, without a mysterious limit interchange. Each sector uses the same operator \(M:f(t)\mapsto t^8f(t)\) but a different cyclic density \(t^{a-1}W(t)dt\). The authentic BBP forcing uses **the a=1 sector** with an additional, bounded, strictly increasing source reweighting \(P/W\).

Classical gamma/digamma recurrences give an analytic closed form for each positive sector:

\[
\boxed{\Gamma_a=
\log\Gamma\left(\frac{a+1}{8}\right)-
\log\Gamma\left(\frac{a}{8}\right)-
\frac18\psi\left(\frac a8\right).}
\]

Summing telescopes the Gamma log terms; the digamma multiplication identity
\(\sum_{a=1}^8\psi(a/8)=8\psi(1)-8\log8\) then returns \(\gamma\) exactly. Independently, the moment integral gives
\(
\gamma=\int_0^1W(t)\sum_{a=1}^8t^{a-1}/(1-t^8)\,dt=\int_0^1C(t)dt.
\)

Every \(\Gamma_a\) now has a finite rational outward interval with an explicit upper bound on the omitted stage tail. The existing GZB/EAB finite gamma errors retain their declared chart and are not replaced by a numerically fitted value.

## 4. SGO-05–08: the authenticated forward/backward Green zero-pair

Set \(\alpha=\sum_{j\ge1}16^{-j}r(j)=\pi/16\) (authentic BBP identity). The finite forward integer/rational recurrence is

\[
U_0=0,\qquad U_{n+1}=16U_n+r(n+1).
\]

Define its **genuine future Green correction**

\[
\boxed{T_n=\sum_{j\ge1}16^{-j}r(n+j)>0.}
\]

It obeys the opposite directed recursion

\[
\boxed{16T_n-T_{n+1}=r(n+1).}
\]

The two zero-identities are complementary:

\[
\begin{aligned}
U_{n+1}-16U_n-r(n+1)&=0,\\
16T_n-T_{n+1}-r(n+1)&=0.
\end{aligned}
\]

Subtracting them cancels the same actual forcing in opposite coordinates:

\[
\boxed{(U_{n+1}+T_{n+1})-16(U_n+T_n)=0.}
\]

The boundary at infinity **selects the correct solution**. Any difference between two bounded solutions of \(16T_n-T_{n+1}=r(n+1)\) obeys \(d_{n+1}=16d_n\), so must vanish. Then \(U_n+T_n=16^n\alpha=16^{n-1}\pi\) for every integer n≥0. The *full future source* determines T, but every T_n has explicit **finite, exact rational** brackets from positivity and decreasing r. Moreover the finite cutoffs obey the very same balancing identity without ever taking infinity:

\[
\boxed{16T_{n,D}-T_{n+1,D-1}=r(n+1),}
\]

where \(T_{n,D}=\sum_{j=1}^D16^{-j}r(n+j)\), \(D\ge1\). Matching D with D−1 across the boundary is essential; naively using equal cutoffs leaves an uncancelled source term. This is a precise example of why SUCC's carrier and boundary-cost metadata are indispensable.

**General l¹ theorem (elementary, not dependent on π).** For radix b>1 and any absolutely summable scalar forcing \(r_m\), the Green operator
\(T_n=\sum_{j\ge1}b^{-j}r_{n+j}\) has \(\sum_{n\ge1}|T_n|\le\frac{1}{b-1}\sum_{m\ge2}|r_m|\). The forward/backward identities and bounded uniqueness follow as above. The new source-specific theorem below is a strict finite-error application of this classical bounded convolution operator.

## 5. SGO-09: a UNIFORM-IN-ORBIT-LENGTH signed Weyl transfer theorem

Let \(e(x)=\exp(2\pi i x)\). Coherent Main X's normality target uses
\(S_N(h,\pi)=\sum_{n=1}^Ne(h16^{n-1}\pi)\) for each fixed nonzero integer h. Define the **same actual source's rational orbit sum**
\(\widehat S_N(h)=\sum_{n=1}^Ne(hU_n)\). The forward/backward identity yields
\(16^{n-1}\pi=U_n+T_n\). Since \(|e(x+t)-e(x)|\le2\pi|t|\),

\[
|S_N(h,\pi)-\widehat S_N(h)|\le2\pi|h|\sum_{n=1}^NT_n.
\]

The source's positivity and its endpoint-zero factor give a **global, exact finite error cap**. Indeed

\[
\sum_{n\ge1}T_n=\frac1{15}\sum_{m\ge2}(1-16^{1-m})r(m).
\]

The genuine BBP polynomial factorization gives
\(r(m)\le15/[(8m-7)(8m-6)]\le15/(8m-7)^2\). Monotone integral comparison gives

\[
\sum_{m\ge2}\frac1{(8m-7)^2}\le\frac1{9^2}+\int_2^\infty\frac{dx}{(8x-7)^2}
=\frac{17}{648}.
\]

Therefore \(\sum_{n\ge1}T_n\le17/648\). Using the classical \(2\pi<7\), we obtain the all-horizon bound

\[
\boxed{\forall N\ge1,\quad
|S_N(h,\pi)-\widehat S_N(h)|<\frac{119}{648}|h|.}
\]

In particular, the *normalized* difference is less than \(119|h|/(648N)\), tending to zero at a certified rate. The unwrapped rational orbit \(U_n\) is **not an independently sampled surrogate**: it is precisely the original deterministic authentic recurrence and initial condition. Therefore

\[
\boxed{
\pi\text{ is base-16 normal}
\quad\Longleftrightarrow\quad
\widehat S_N(h)=o(N)\ \text{for every fixed }h\in\mathbb Z\setminus\{0\}.
}
\]

The equality of normality targets is classical Weyl criterion plus the proved bounded discrepancy. **This is not a proof that either sum actually cancels.** It moves the unbounded time-dependence from the smooth π phase into an **exact rational/cyclotomic arithmetic source** with a finite, uniform error cost. Unlike a fixed rational approximation to π, the source-native \(U_n\) changes with n and preserves the authentic BBP integer lift.

The all-horizon bound is not just a sampled-numerical fit. An executable independent Fraction replay computes arbitrary finite Green-tail intervals and a tighter aggregate bound, e.g. with 32 exact source states and 12 Green-depth stages, \(\sum_nT_n\) is bounded above by a rational approximately 0.0163085484 (versus the universal 17/648≈0.02623457). Thus at h=1 the universal signed Weyl error cap can be sharpened from 0.183642 to about 0.114160; divide by N for the normalized estimate.

**Observer-class caveat:** the analogous statement holds for any fixed 1-periodic Lipschitz function with its Lipschitz constant. The base-16 **digit indicator is discontinuous**, so an unproved assertion that its per-cell disagreements obey the same Lipschitz bound would be false. The inherited Hypothesis-A collision/source-cell machinery addresses such boundaries separately. Fourier/Weyl testing is legal because its observables are continuous and Lipschitz.

## 6. SGO-10–12: controls, nonidentification and the remaining frontier

- **Independent source oracle:** the new exact rational forward recursion equals the original signed four-pole formula, Main X natural-BBP `exact_forcing`, and Main X integer-carrier `forcing_pair`. Host integration is separate from an isolated local shim.
- **Independent π holdout:** a rational Machin arctangent series tests the complex phase transport on finite horizons; it supplies **no construction input** to the proof formula. The finite bound was derived from the authenticated source and \(2\pi<7\).
- **Precision calibration:** an initial 120-digit mpmath comparison falsely rejected an extremely tight rational interval at high moment index because the interval width was beyond working precision. Raising this holdout to 260 digits passes. The actual certificate remained exact Fraction throughout; no test run was silently hidden.
- **Synthetic nonnormal control:** two rational atoms at t=1/2 and t=3/4 with increasing relative densities 17 and 47/2 have strictly positive *all* shifted cross-determinants yet a **rational** resolvent at z=1/16, whose base-16 expansion is eventually periodic. The pair does not match authentic Euler/BBP source data; it refutes the shortcut from *shape of signed moment ordering* to normality.
- **Summable-amplitude no-go:** any absolutely summable scalar sequence w_n has \(|\sum_{n\le N}w_ne(hU_n)|\le\sum_n|w_n|=O(1)\), regardless of the orbit. Thus positive/negative **summable correction amplitudes alone cannot cause an N-scale Fourier cancellation theorem**. The missing target is a new nontrivial bound for \(\widehat S_N(h)\) itself, using the true signed integer-lift recurrence, prime/cyclotomic source, or a complete transfer principle.
- **No Weil/RH inference:** the signed measure built here is a *difference of two positive moment sources*, **not** the original signed completed Weil distribution or Suzuki quadratic form. The new source is a mathematical observer/field instrument, not a QFT assertion.

## 7. Verification, source authority, and next discriminating probe

New code: `observational_succ/gamma_bbp_signed_coherence.py`; exact tests: `tests/test_gamma_bbp_signed_coherence.py` and `tests/test_gamma_bbp_signed_integration.py`; JSON rational replay: `scripts/gamma_bbp_signed_coherence_probe.py --verify`; scoped claims: `docs/CLAIM_SUPPLEMENT_SIGNED_GAMMA_BBP.md`. **Locally observed Python 3.13.5: 27 new focused exact/numerical test cases pass**, plus 25 inherited GZB focused tests for **52 total**. The original `bbp_natural_carrier` and `integer_bbp_carrier` files were *locally represented by explicitly labelled shims*. Live full-repo integration and all AGENTS.md checks are a separate GitHub CI gate. A separate independently implemented complete factorial check covered **1,452 finite signed-force radices (b=2,3,4,16; lengths 1..5; coefficients -1,0,1)** with no mismatches, and **390 strict gamma/BBP cross-moment pairs** also passed. These calibrate, but do not replace, the all-index proofs. The script prints outward-quantized rational enclosures so Python's decimal-digit serialization limits do not compromise exact computations or generate huge JSON.

Sources: [NIST DLMF §5.5 (digamma recurrence)](https://dlmf.nist.gov/5.5); [Bailey–Borwein–Plouffe original paper, NASA archive](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19970009337.pdf); the inherited SUCC π Gearbox Atlas, π Frontier Contract, EAB/CZR/CZB/GZB source labels. No nontrivial zeros, π digit strings, fake-independent prime 6 or physical vacuum observations enter the proof construction.

**Next verdict-changing proof:** On the rational arithmetic recurrence U_(n+1)=16U_n+r(n+1), obtain a nontrivial signed estimate \(\widehat S_N(h)=o(N)\), or the corresponding highest-order four-bit Walsh correlation, *with exact source/phase provenance and a uniform all-N bound*. The new theorem removes one entire analytic boundary-transfer debt; it does not discharge the signed arithmetic cancellation debt. **π NORMALITY OPEN. RH OPEN.**

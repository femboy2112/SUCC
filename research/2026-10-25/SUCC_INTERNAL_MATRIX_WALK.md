# SUCC internal matrix walk — arithmetic successor, Fourier carrier, and retained source curvature

**Research date:** October 25, 2026. **Parent:** `femboy2112/SUCC` research branch `research/signed-gamma-bbp-green-orbit-2026-10-25@fd45a98e9206496fa1486761db5a7389713559f8` (draft PR #293), preserving the Contextual Zero, Gamma Zero/One and Green-tail lineage. **Source passport:** original Coherent Main X signed four-pole BBP recurrence

\[
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad
r(m)=\frac4{8m-7}-\frac2{8m-4}-\frac1{8m-3}-\frac1{8m-2}.
\]

No original arithmetic source, Weil/Suzuki functional, or physical observation was modified or inferred. This implements the author's precise proposal: the *external* operation is one arithmetic SUCC, but the *internal* state retains a source-typed matrix of representations and its evolution. Everything below is classical Fourier/Gram/Fejér and explicit rational BBP identities, in a new-to-SUCC combination. Independent scholarly novelty **UNVERIFIED**. **π normality and RH remain OPEN.**

## 1. Exact rational circle group algebra is the internal coefficient carrier

The source state is rational for every finite n. Write \(e(q)=\exp(2\pi iq)\) formally for \(q\in\mathbb Q/\mathbb Z\), and work initially in the *free group algebra* \(\mathbb Q[\mathbb Q/\mathbb Z]\):

\[
e(q_1)e(q_2)=e(q_1+q_2),\quad e(q)^*=e(-q),\quad e(0)=1.
\]

This is a **symbolic finite arithmetic** type, not floating complex approximation and not a ring in which all root-of-unity cyclotomic relations have already been imposed. Example: \(e(0)+e(1/2)\) is formally nonzero even though its complex evaluation equals 0. The *existing* SUCC `finite_fourier_carrier.CyclotomicElement` supplies a separate exact evaluation quotient for bounded common denominator. This distinction is load-bearing: exact formal equality is sufficient for every certificate in this module, but it is not a complete decision procedure for equality of complex cyclotomic values. A growing common conductor can exceed finite budgets.

All populated Gram entries and source phase angles below are exact `Fraction` or these symbolic group algebra polynomials, with no π input.

## 2. One SUCC increments an entire matrix by rank one

For a fixed integer base frequency \(h\neq0\) and finite width \(H\ge2\), define an internal observer vector

\[
v_n=(1,e(hU_n),e(2hU_n),\dots,e((H-1)hU_n))^\top.
\]

Let \(G_N=\sum_{n=1}^N v_nv_n^*\), and \(A_N=G_N/N\). The exact, source-labelled update is

\[
\boxed{G_{N+1}=G_N+v_{N+1}v_{N+1}^*,\qquad
A_{N+1}=\frac{N A_N+v_{N+1}v_{N+1}^*}{N+1}.}
\]

The matrix is Hermitian positive semidefinite under the true character representation, its diagonal entries are 1, and its rank is at most \(\min(N,H)\). Crucially the exact entry
\((A_N)_{k\ell}=N^{-1}\sum_{n=1}^N e((k-\ell)hU_n)\) is Toeplitz. The selected Weyl coefficient is an **off-diagonal matrix element**, not an inaccessible oracle.

### IMW-01: precise spectral-purity / Fourier identity

\[
\boxed{\operatorname{tr}(A_N^2)-H
=2\sum_{j=1}^{H-1}(H-j)\left|\frac1N\sum_{n=1}^N e(jhU_n)\right|^2.}
\]

**Proof:** expand the trace \(\sum_{k,\ell}|(A_N)_{k\ell}|^2\); all H diagonal terms are exactly 1; pairs with \(|k-\ell|=j\) occur \(2(H-j)\) times. This equality holds **symbolically in the original Q[Q/Z] algebra**, and can be evaluated in any compatible cyclotomic field without approximation. **Rank floor:** \(\operatorname{tr}(A_N^2)\ge H^2/\min(N,H)\), since a positive H×H matrix of trace H and rank r has \(\sum\lambda_i^2\ge H^2/r\). Finite observer dimensionality intrinsically limits perfect uniformity at early horizons.

**Concrete conditional sufficiency:** if some \(H_N\to\infty\) satisfies \(\operatorname{tr}(A_{N,H_N}^2)=H_N+o(H_N)\) on the authentic h=1 trajectory, every **fixed** nonzero character vanishes by the exact identity and Weyl's criterion establishes base-16 normality. This is a real growing internal-matrix proof gate, *not* a proved estimate; using width \(H_N\gg N\) is impossible under the rank floor. It's another representation of the still-open signed source concentration problem, not an escape from it.

### IMW-02: the derivative of the matrix's spectral energy is a Fejér overlap

Put \(P_N=\operatorname{tr}(A_N^2)\), and let \(q_N=v_{N+1}^*A_Nv_{N+1}\). Rank-one algebra yields

\[
\boxed{P_{N+1}=\frac{N^2P_N+2Nq_N+H^2}{(N+1)^2}.}
\]

Moreover

\[
\boxed{q_N=\frac1N\sum_{m=1}^N
\left|\sum_{k=0}^{H-1}e\bigl(kh(U_{N+1}-U_m)\bigr)\right|^2.}
\]

This is exactly a Fejér-type nonnegative kernel of **pairwise trajectory differences**. It shows where new information enters as the observer walks: the time derivative of its internal spectral purity is determined by actual authenticated relative phases. No tick-marked reference angle is needed, and no stochastic independence is presumed. The implementation checks both routes as *exact group-algebra identities* rather than merely matching numerical traces.

## 3. A second, geometric-frequency matrix makes the source twist explicit

On the true circle, the nonautonomous step is \(F_n(x)=16x+r(n+1)\pmod1\). For a Fourier character \(e(hx)\), Koopman pullback obeys

\[
\boxed{K_ne(hx)=e(hr(n+1))\,e(16hx).}
\]

Thus on the natural frequency ladder \(h,16h,16^2h,\dots\), each \(K_n\) is a unilateral weighted shift with phase \(\omega_{n,k}=e(h16^k r(n+1))\). A **fixed single-step** weighted shift with unimodular weights is diagonally gauge-equivalent to the plain shift: \(g_0=0,\ g_{k+1}=g_k+h16^k r(n+1)\), \(D_n^*K_nD_n=S\). Its bare eigen/singular spectrum alone is therefore source-blind. Furthermore finite compression to the first H channels leaves an outgoing **unit-norm boundary channel**: operator-norm truncation cannot be claimed to converge simply because the observer uses a larger finite matrix. Exact source information remains in phase labels, cross-time comparisons, the initial state and the escaping high-frequency channel. The natural geometric-frequency Gram is not Toeplitz in its index, and is separately computed instead of mislabelled as one.

### IMW-03: mixed SUCC-time/FUCC-frequency curvature is a source Pascal jet

Retain the **unwrapped rational phase** \(\theta_{n,k}=h16^k r(n+1)\). The finite mixed difference is

\[
\boxed{\Delta_n\Delta_k\theta_{n,k}=15h16^k\bigl(r(n+2)-r(n+1)\bigr).}
\]

More generally for all integers \(a,b\ge0\):

\[
\boxed{\Delta_k^a\Delta_n^b\theta_{n,k}
=15^a16^k h\Delta_n^br(n+1),\qquad
(-1)^b\Delta_n^br(n+1)>0\ (b>0).}
\]

The sign theorem comes from the **unchanged original four-pole positive moment density** \(r(n+1)=\int_0^1t^{8n}P(t)dt\), \(P(t)=(1-t)(t^2+2)(t^2+2t+2)>0\) on \([0,1)\). Then

\[
(-1)^b\Delta_n^br(n+1)=\int_0^1t^{8n}(1-t^8)^bP(t)dt>0.
\]

This is the exact interface to SUCC's Pascal/Lucas differentiated-source machinery. The rational phase *lift* has a definite sign; reducing modulo one may wrap and destroy that order. The plaquette is invariant under **separable additive chart changes** \(\theta\mapsto\theta+a(n)+b(k)\), but is **not asserted** to be invariant under arbitrary time/frequency-dependent gauge transformations. Neither positivity of these lifted jets nor single-step unitary equivalence proves π normality.

## 4. IMW-04: a provable NONUNIFORM frequency window — the actual obstruction to naive finite-to-infinite transport

The authentic BBP source has

\[
r(n+1)=\frac{120n^2+151n+47}{(2n+1)(4n+3)(8n+1)(8n+5)}.
\]

For every n≥1, straightforward positive-denominator rational algebra gives

\[
\boxed{0<\frac{15}{64}-n^2r(n+1)<\frac7{5n}.}
\]

The left difference is exactly

\[
\frac{5696n^3+7672n^2+2910n+225}
{64(2n+1)(4n+3)(8n+1)(8n+5)},
\]

which is positive. After clearing positive denominators, the upper inequality has polynomial numerator
\(200896n^4+420392n^3+304426n^2+85787n+6720\) over \(320n(2n+1)(4n+3)(8n+1)(8n+5)\), again positive.

Let \(n=4^j\), take the *moving frequency channel* \(k=j\), and observe \(16^j=n^2\). Hence

\[
\boxed{e(16^jr(4^j+1))\longrightarrow e(15/64)\neq1.}
\]

Meanwhile for every **fixed k**, \(e(16^kr(n+1))\to1\). So \(K_n\to S\) strongly on each fixed finite-frequency vector, but \(\|K_n-S\|\not\to0\): the source twists remain macroscopic in a frequency band migrating toward infinity as time advances. This is a **source-specific theorem that two carrier limits do not commute**, not just a generalized warning about infinite-dimensional operators.

### IMW-05: differentiating the matrix moves the critical band from n² to n³

The adjacent forcing difference has

\[
\lim_{n\to\infty}n^3\bigl(r(n+1)-r(n+2)\bigr)=15/32.
\]

In fact rational denominator-clearing proves for every n≥1

\[
\boxed{0<15/32-n^3[r(n+1)-r(n+2)]<3/n.}
\]

The left defect has numerator
\(3(3424256n^7+20586496n^6+49593600n^5+61599296n^4+42266944n^3+15796980n^2+2888640n+184275)\), all positive, over the positive denominator \(32(2n+1)(2n+3)(4n+3)(4n+7)(8n+1)(8n+5)(8n+9)(8n+13)\). After clearing denominators, \(3/n\) minus that difference has another polynomial with **all positive coefficients**, independently derived with SymPy and recorded in local mathematics checks.

Thus with \(n=16^j\) and \(k=3j\), the *time-differenced high-frequency phase* converges to the nontrivial source angle:

\[
\boxed{e(16^{3j}[r(16^j+1)-r(16^j+2)])\to e(15/32)\neq1.}
\]

**Consequence:** measuring the internal matrix's change as SUCC walks really can expose source data invisible at any fixed Fourier depth. The critical frequency scales of the phase and its first time derivative differ (n² and n³). These are precisely defined moving horizons, not a proof that the corresponding phases cancel.

## 5. IMW-06: four-bit Walsh is the *same* matrix-geometry problem in a different basis

Let \(d_n=\lfloor16\{U_n\}\rfloor\) for an explicitly **rational-source** observation; these are not assumed equal to the true π digits without Green-tail boundary certificates. For the 4 binary digits of \(d_n\), write \(w_m(d)=(-1)^{\operatorname{popcount}(m\wedge d)}\) for m=0,...,15, and \(\widehat p_m=N^{-1}\sum_{n≤N}w_m(d_n)\). Then Walsh orthogonality gives the exact finite Parseval law

\[
\boxed{16\sum_{d=0}^{15}p_d^2=\sum_{m=0}^{15}\widehat p_m^2
=1+\sum_{m=1}^{15}\widehat p_m^2.}
\]

This is the same source-labelled **spectral purity/collision** object in the Walsh rather than circle-character basis; the existing `pascal_carry_interferometry.walsh_moments` and `dynamic_fourier_tower.exact_fourier_restriction` are cross-validated by native-host integration tests. The highest-order Walsh term is *essential*: a uniform distribution on the eight even-parity four-bit digits has **all** Walsh masks 1–14 equal to zero, while mask 15 equals 1 and collision energy equals 2. Hence lower-order interactions are not a source-independent proof shortcut. The same law generalizes to L-digit windows (dimension 16^L) with the usual computational and source-index costs.

## 6. What would now be sufficient—and what is still open

A concrete source-authentic theorem that SUCC's evolving matrix spectral excess obeys

\[
\boxed{\operatorname{tr}(A_{N,H_N}^2)-H_N=o(H_N)
\quad\text{for some }H_N\to\infty}
\]

would imply \(N^{-1}S_N^U(h)\to0\) for every fixed h≠0 and therefore π's base-16 normality by the already certified SGO Green-tail/Wasserstein transport. **No such bound has been proved.** The equation identifies an internal-matrix target, not a new source-specific estimate. The Fejér innovation q_N, exact source Pascal phase curvature, and moving n²/n³ frequency band are the new instruments with which to attack it. Standard positivity/rank/orthogonality by themselves are insufficient, as the fixed-point countermodel demonstrates.

The exact Fourier matrix witness does not replace the original Weil/Suzuki source, use nontrivial zero positions, or establish RH. **π NORMALITY: OPEN. RH: OPEN.**

## 7. Implementation, replay and authority

- `observational_succ/succ_internal_matrix_walk.py`: exact arithmetic original forcing and state, formal rational character ring, rank-one Gram SUCC, exact purity and Fejér innovation, Koopman phases/gauges, all-order mixed difference, moving-frequency rational certificates, Walsh collision transform, separately budgeted native cyclotomic quotient.
- `tests/test_succ_internal_matrix_walk.py`: 23 exact/Q-targeted local test groups and numerical mpmath diagnostics *labelled as diagnostics*.
- `tests/test_succ_internal_matrix_integration.py`: source passport comparisons to authentic `bbp_natural_carrier`, `integer_bbp_carrier`, `pi_joint_prime_carrier`, `gamma_bbp_signed_coherence`, `pascal_carry_interferometry`, and `dynamic_fourier_tower`; **native full GitHub CI is the authority for these tests**.
- `scripts/succ_internal_matrix_probe.py --verify`: source-labelled JSON report using Fraction reductions and optional high-precision display.
- `docs/CLAIM_SUPPLEMENT_SUCC_INTERNAL_MATRIX.md`: scoped IMW-01–11 claim ledger, with source/limit firewalls.

### Local validation

23/23 targeted pure-matrix tests passed (local Python 3.13); an independent exhaustive calibration over 780 source-agnostic rational phase histories (5 admissible phase values, horizons 1 through 4) checked the exact purity/Fourier identity; native integrations are separated from local isolated tests and will be checked on the actual GitHub PR head. Independent SymPy rational polynomial reduction confirmed the stated n²/n³ error inequalities; direct rational comparisons verified all sample finite moving windows. No claim of formal Lean analysis, independent academic novelty, or proof of π normality is made.

**Next discriminating round:** (i) Obtain actual source-selected *Fejér innovation decay* that controls the evolving purity rather than just reexpressing it; (ii) couple the critical n²/n³ high band to the exact arithmetic odd-conductor, Pascal/Lucas, four-bit Walsh and CRT operations, respecting their source maps; (iii) test fake-origin and matched-positive-moment countermodels where all fixed finite corners appear benign. Do not silently replace time averages by generic Haar/spatial averages, or convert strong convergence of Koopman matrices into operator-norm convergence.

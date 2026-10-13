# Dynamic/diagonal Fourier for ObsSUCC: incomplete observers and virtual zeros

**Date:** 2026-10-12. **Status:** classical finite Pontryagin/Fourier and complex analysis reorganized into source-relative ObsSUCC proof objects; exact rational checks for finite instances; analytic proofs below. **No RH proof, zero-location oracle, new Fourier theory, physically observed information, or claim of academic priority.**

**User hypothesis.** Standard Fourier transformation starts with an entire globally specified function. SUCC starts from a shared carrier whose *observers* have only evolving, partial source access. Can Fourier be made natural across the observational ladder? Can an off-critical zero from a permissible alternative Archimedean completion represent a "virtual" or not-yet-eliminated possibility rather than a zero of actual zeta?

**Parent source:** `femboy2112/SUCC` draft PR #31 at `04c04f715ed08db91ab531897047420a7299e15a`, built upon dual-observer PRs #26–#29. This is an **additive research branch**. All true-prime/FUCC source signatures, correct Euler product domains, Gamma and Weil-sign firewalls remain in force.

## 1. The two kinds of virtuality must not be conflated

1. **Epistemic completion zero.** Let \(\mathscr A_n\) be the set of global analytic completions still compatible with observer E's *actual* stage-\(n\) evidence. A complex point \(s\) is a *possibly virtual zero* when \(\exists F\in\mathscr A_n:F(s)=0\). It is **forced by evidence** only when \(\forall F\in\mathscr A_n:F(s)=0\). An off-critical zero of one possible \(F\) is **not** a zero of canonical \(\xi\). A zero of a model-dependent multiplier \(C_F\) need not even be absent from \(\xi\): we cannot assert noncoincidence with unknown true zeros.
2. **Observational Fourier null.** An actual nonzero fine source vector \(f\) can be annihilated by a coarser observational map \(T\), even while its **full** Fourier transform is nonzero. This is a false *observer null*, not an analytic zero of \(\xi\).

The two are connected by the problem of **source-relative sufficiency**: finite reports may fail to distinguish the canonical global theory from another globally consistent theory or from a hidden local mode. Merely sharing a source identifier does not authenticate physical data.

## 2. DF1: Exact diagonal Fourier square along a genuine finite quotient (CLASSICAL / PROVED)

Let \(M=kN\), \(N\ge2\). Work on \(G=\mathbb Z/M\mathbb Z\) and \(H=\mathbb Z/N\mathbb Z\), with their standard characters. The source map \(q:G\twoheadrightarrow H\) is reduction modulo \(N\). For a finitely supported complex-valued signal \(f:G\to\mathbb C\), define **raw** observational fiber pushforward

\[
(A_qf)(h)=\sum_{g\equiv h\pmod N}f(g).
\]

Use unnormalized Fourier transforms \(\widehat f_M(j)=\sum_{x\bmod M} f(x)e^{2\pi ijx/M}\), and similarly for \(N\). The dual injection is \(q^*:r\mapsto kr\pmod M\). Then

\[
\boxed{\widehat{A_qf}_N(r)=\widehat f_M(kr)\quad(0\le r<N).}\tag{DF1}
\]

**Proof:** substitute \(A_qf\), interchange two *finite* sums, and use \(e^{2\pi ir(x\bmod N)/N}=e^{2\pi i(kr)x/M}\). No spectral completeness at the *observer* level is assumed. The complete fine Fourier transform exists as a mathematical reference, but E receives only its restricted dual subgroup. The code checks this equality **exactly in rational cyclotomic fields** using the pre-existing `finite_fourier_carrier` and the canonical map \(\zeta_N\mapsto\zeta_M^k\).

For \(M\to N\to L\) with divisibility, both raw pushes and dual inclusions compose strictly. Thus the coarsening and refinement diagrams **really commute**. At prime-power clocks \(p^r\to p^s\), the source checker also verifies that \(p\) is a genuine prime and rejects incorrect local-place signatures. This gives a *projectively natural finite Fourier observation system*, not a reconstructed Archimedean local factor.

## 3. DF2: The Fourier information-debt identity (CLASSICAL / PROVED)

Let \(T_q=k^{-1/2}A_q\) map Euclidean \(\ell^2(G)\) into \(\ell^2(H)\). Then \(T_qT_q^*=I_H\) and \(P_q=T_q^*T_q\) is the orthogonal projection onto functions constant on fibers of \(q\). The **unseen spectral energy** is

\[
\boxed{D_q(f)=\|f\|_2^2-\|T_qf\|_2^2=\|(I-P_q)f\|_2^2
=\frac1M\sum_{j\notin k\mathbb Z/M}|\widehat f_M(j)|^2\ge0.}\tag{DF2}
\]

**Proof:** \(P_qf\) equals the mean of \(f\) over its fiber. The Pythagorean theorem gives the first two equalities. Apply finite character orthogonality / Parseval and DF1 for the last. The exact implementation uses unnormalized rational fiber sums and a rational energy factor \(1/k\), hence computes **exact Fractions**, never approximated \(\sqrt{k}\) or complex roots. For the spectral proof it multiplies cyclotomic coefficients by their exact conjugates and sums the *whole omitted character set*, which has rational total energy.

**Decisive hidden-mode control:** at \(M=4,N=2\), \(f=(1,0,-1,0)\) and \(g=0\) both report \((0,0)\) coarsely, although \(\|f-g\|_2^2=2\). The Fourier spectrum of \(f\) lives entirely in odd characters invisible to \(q^*\widehat H\). No finite observer seeing only \(A_qf\) can know its actual hidden debt without source premises; the number \(D_q(f)\) in a software audit uses a **privileged full-source test vector**.

## 4. DF3: No double counting across nested E-towers (CLASSICAL / PROVED)

For any sequence \(M_0\to M_1\to\cdots\to M_d\) of cyclic quotient clocks, the stage losses are nonnegative and telescope:

\[
\boxed{\|f\|^2-\|T_{M_0\to M_d}f\|^2
=\sum_{j=1}^d\left(\|T_{M_0\to M_{j-1}}f\|^2-
\|T_{M_0\to M_j}f\|^2\right).}\tag{DF3}
\]

The *same* source and source version must be used. Different carriers, destructive updates, uncharged resampling and nonnested experimental menus do not inherit the identity. In a three-level 8→4→2 system with \(f=(1,0,0,0,0,0,0,0)\), the exact energies are \((1,1/2,1/4)\), and the stage debts are \((1/2,1/4)\). This is the source of the operational description "a Fourier transform that builds as the observer refines": it is not a novel transform on an unknown function, but a strictly commuting **tower of incomplete readouts** of the same mathematical signal.

## 5. DF4: The source-to-claim transport criterion (CLASSICAL / PROVED)

Let \(\ell_a(f)=\langle a,f\rangle\) be a real linear original-source target. Then

\[
\boxed{|\ell_a(f)-\ell_a(P_qf)|^2
\le\|(I-P_q)a\|^2\,D_q(f).}\tag{DF4}
\]

This is Cauchy–Schwarz on the orthogonal complement of the observer's visible subspace. In particular **the target factors through all coarse observations if and only if \(a=P_qa\)**, regardless of how much source energy is hidden. The general nonlinear analogue is the already-established SUCC claim-constancy-on-source-fibers theorem (SC1).

**Hostile unbounded-operator control:** for integer \(n\), take \(f_n=(1/n,0,-1/n,0)\), and \(a_n=(n^2,0,-n^2,0)\). Every coarse observation is zero and \(D(f_n)=2/n^2\to0\), yet the missed claim is \(\ell_{a_n}(f_n)=2n\to\infty\). Therefore small Fourier debt **does not imply** stable analytic or arithmetic claims when the observation-to-target operator norm grows without bound. A genuine Mellin continuation needs appropriate common operator-domain bounds or a Schwartz/test-function topology stronger than this local \(\ell^2\) proxy.

## 6. VZ1: A *source-class* interpretation of the prior off-line zeros (CLASSICAL EXAMPLE / PROVED)

Let \(G_a(x)=e^{-\pi a x^2}\), and for \(\epsilon\ge0\) define

\[
\boxed{f_\epsilon(x)=\frac{G_1(x)+\epsilon G_{16}(x)+\frac\epsilon4G_{1/16}(x)}{1+\frac54\epsilon}.}\tag{VZ1a}
\]

Every \(f_\epsilon\) is positive, even, Schwartz, normalized by \(f_\epsilon(0)=\int f_\epsilon=1\), and exactly Fourier-self-dual under the standard real transform (\(G_{16}\leftrightarrow\frac14G_{1/16}\)). Keeping the **unmodified genuine finite Euler factors**, the real Mellin factor differs from the standard Gamma factor by

\[
\boxed{C_\epsilon(s)=\frac{1+\epsilon(4^{-s}+4^{s-1})}{1+5\epsilon/4},\quad
C_\epsilon(s)=C_\epsilon(1-s),\quad C_\epsilon(0)=C_\epsilon(1)=1.}\tag{VZ1b}
\]

Thus \(\xi_\epsilon(s)=C_\epsilon(s)\xi(s)\) is a *different completed analytic function* compatible with the restricted observer signature "finite Euler factors, real positive/selfdual Schwartz, normalized poles, symmetric FE." The actual \(\xi\) and \(\zeta\) are **not modified**. The extra multiplier zeros are genuine zeros **of the alternative analytic function**, but are **virtual relative to a receiver that has not identified which admissible Archimedean source is canonical**. We do not assert that these locations are not also zeros of canonical \(\xi\) without proving it.

Setting \(t=4^{s-1/2}\), the exact multiplier equation for \(\epsilon>0\) is

\[
\boxed{t^2+\frac2\epsilon t+1=0.}\tag{VZ1c}
\]

All conclusions follow from rational inequalities and the quadratic formula; there is **no input of an unknown zeta zero**.

| Source coefficient \(\epsilon\) | Location of *extra multiplier* zeros |
| --- | --- |
| \(0\) | No multiplier zeros: \(C_0\equiv1\) |
| \(0<\epsilon<4/5\) | Outside the **closed** critical strip |
| \(\epsilon=4/5\) | On its boundaries, real parts 0 and 1 |
| \(4/5<\epsilon<1\) | **Inside the open strip, off the critical line** |
| \(\epsilon=1\) | Double zeros on the critical line |
| \(\epsilon>1\) | Zeros on the critical line (simple) |

**Proof of the sharp strip threshold.** For \(0<\epsilon<1\) the two roots are negative and reciprocal, with larger modulus \(R>1\) satisfying \(R+R^{-1}=2/\epsilon\). Since \(\Re s=1/2\pm\log R/\log4\), both lie inside the open strip iff \(R<2\), equivalent to \(2/\epsilon<5/2\), i.e. \(\epsilon>4/5\). At \(\epsilon\ge1\), the roots have modulus one; at \(\epsilon=1\) they coincide. The earlier DZ9 source is **exactly** \(\epsilon=10/11\), recovering \(t^2+(11/5)t+1=0\) and \(C_\epsilon(2)=413/188\).

**A second exact strip check:** for \(0\le\Re s\le1\),
\(|4^{-s}+4^{s-1}|\le4^{-\Re s}+4^{\Re s-1}\le5/4\). Consequently for \(\epsilon<4/5\), \(|\epsilon(4^{-s}+4^{s-1})|<1\), making \(C_\epsilon(s)\) provably nonzero throughout the *entire closed strip*. This is a zero-free statement **only about the auxiliary multiplier \(C_\epsilon\)**.

## 7. VZ2: Why virtual zeros can vanish under SOURCE refinement without violating Hurwitz (CLASSICAL / PROVED)

The family \(C_\epsilon\to1\) locally uniformly on \(\mathbb C\) as \(\epsilon\to0^+\). Indeed, for any compact \(K\), the two exponentials are bounded on \(K\), and \(C_\epsilon-1\) is \(O_K(\epsilon)\). The multiplier roots satisfy \(R(\epsilon)\to\infty\), so their real parts tend to \(+\infty\) or \(-\infty\); eventually none remain in the critical strip. **Zeros cannot simply disappear within a fixed compact region under this analytic convergence.** This is precisely consistent with Hurwitz/Rouché: if a nonzero analytic limit has no zeros on the boundary of a compact Jordan region, then approximants eventually have the same zero count there.

When multiplying by canonical \(\xi\), \(C_\epsilon\xi\to\xi\) locally uniformly. Existing \(\xi\)-zeros are unaffected; only the additional model-dependent zeros can escape. The no-extra-zero statement for \(C_\epsilon\) never purports to establish a zero-free strip for \(\xi\).

**Interpretive repair:** The "virtual" is an **epistemic alternative model**, not a nonexistent analytic root, a vacuum fluctuation, or a physical/quantum virtual particle. A subjective model update \(\mathscr A_{n+1}\subseteq\mathscr A_n\) can eliminate a model that carried the root. A sequence of actual analytic alternatives can also move its auxiliary roots out of any compact. These are different phenomena.

## 8. VZ3: Exact model-selection from an additional Mellin probe (PROVED, CONDITIONAL)

Within **this one-parameter family**, the exact second Mellin multiplier is

\[
C_\epsilon(2)=\frac{1+(65/16)\epsilon}{1+(5/4)\epsilon},\qquad
\boxed{\epsilon=\frac{16(C_\epsilon(2)-1)}{65-20C_\epsilon(2)}}.\tag{VZ3a}
\]

The map is injective on every finite \(\epsilon\ge0\); an additional **source-authenticated exact** measurement of \(C(2)\) collapses the observer's parameter interval to one value. \(C(2)=1\) selects the standard Gaussian \(\epsilon=0\) in this restricted family. This is not a selection of the standard test function from every conceivable selfdual Schwartz function, nor a way to measure the real Gamma factor using only finite Euler coefficients. Numeric noise, sample cost and source identification need further work.

**Stronger positive-cone rigidity.** The individually normalized selfdual Gaussian pair
\[
 f_r(x)=\frac{G_{r^2}(x)+r^{-1}G_{r^{-2}}(x)}{1+r^{-1}},\quad r>0
\]
obeys the striking *exact* identity
\[
\boxed{C_r(2)-1=r+r^{-1}-2=\frac{(r-1)^2}{r}\ge0.}\tag{VZ3b}
\]

Therefore any finite **nonnegative convex mixture** \(\sum_j w_j f_{r_j}\), \(w_j\ge0\), \(\sum w_j=1\), has
\[
C(2)-1=\sum_j w_j\frac{(r_j-1)^2}{r_j},
\]
and \(C(2)=1\) **if and only if** every positive-weight summand is the canonical \(G_1\) (\(r_j=1\)). This proves conditional source rigidity on a substantially larger cone than VZ1. Positivity of mixing weights is load-bearing; no uniqueness is claimed for all positive self-Fourier Schwartz functions or for the whole adelic Schwartz–Bruhat space. This is a nonnegative **moment gap**, not the completed Weil positivity required for RH.

## 9. What would genuinely make this an RH tool?

A candidate bridge must be compatible with the **actual** finite-prime test family \(\mathcal S(\mathbb A_\mathbb Q)\), the true Archimedean Gamma local functional, correct Haar selfduality and additive characters, the multiplicative/Mellin action, and rigorous analytic continuation. It must provide:

1. A **source-derived law** choosing or identifying the Archimedean test-function distribution (not assuming it from the functional equation).
2. A compatible source-indexed **test-function/projective Fourier functor** with quantitative tails, including the correct support and conductor controls at every genuine prime (especially \(p=2\)), and correct domain/norm transport to the real Mellin functional.
3. A theorem that bounds \(\sup_{s\in K}|F_n(s)-F(s)|\) from *actual observed source evidence* and justified operator norms. Only then can Rouché/Hurwitz transfer local zero counts. An uncited \(L^2\)-energy inequality on finite clocks is not enough, as DF4 proves.
4. The distinct **RH-strength source-derived positive completed Weil/Suzuki form**, with the exact test-function domain, pole/Gamma terms and half-density, no nontrivial-zero inputs, and matched genuine-character versus non-Euler controls. The present nonnegative Fourier debt or Gaussian moment gap does **not** imply Weil positivity.

**Moonshot mathematical candidate:** construct a diagram of source-aware filtered adelic test-function spaces \((\mathcal S_n,\mathcal F_n,\mathcal L_n)\), where finite Fourier transformations and their dual maps commute, \(\mathcal L_n\) are certified local Mellin distributions, and the analytic comparison \(\|\mathcal L_n-\mathcal L\|_{K}\le\varepsilon_n\to0\) is independently established in a topology that controls zeros. Test that proof against \(\epsilon\)-deformed real Gaussians, fake composite Euler factors, nonunit FUCC, missing prime-place escape and changing underlying carriers.

## 10. Evidence and repro

- `observational_succ/dynamic_fourier_tower.py`: exact cyclotomic quotient Fourier squares, rational whole-spectrum deficit, source-versioned composition, original-source claim budget, and unbounded-claim counterexample.
- `observational_succ/virtual_mellin_zeros.py`: exact rational multiplier/source signatures, threshold classification, source-relative admissibility, exact C(2) source selection, and positive Gaussian-mixture rigidity.
- `tests/test_dynamic_fourier_tower.py`, `tests/test_virtual_mellin_zeros.py`: exhaustive small rational clocks, cross-quotient composition, false Euler/place and forged signature controls, boundary thresholds, and source family mutation.
- `scripts/dynamic_fourier_virtual_zeros_probe.py`: reproducible exact JSON summary, saved as `research/2026-10-12/DYNAMIC_FOURIER_VIRTUAL_ZEROS_RECEIPT.json`. No floating-zero computations or zero reading.

**Independent/external theory:** finite quotient duality: [Encyclopedia of Mathematics, Pontryagin duality](https://encyclopediaofmath.org/wiki/Pontryagin_duality); analytic zero stability: [Encyclopedia of Mathematics, Hurwitz theorem](https://encyclopediaofmath.org/index.php?title=Hurwitz_theorem); nonstationary Fourier already exists in signal processing: [Dörfler et al., nonstationary Gabor frames](https://pmc.ncbi.nlm.nih.gov/articles/PMC3257872/). This is an SUCC source/proof discipline for classical constructions, not a claim to have invented time-varying Fourier analysis. The original source geometry is Tate's classical adelic Fourier/Mellin framework as pinned in `DIAGONAL_ADELIC_ZETA_SOURCE.md`.

## 11. DF5: True dynamical Fourier requires a state-change descent square (CLASSICAL / PROVED LOCAL)

The quotient tower above changes the **observer**, not the carrier. The user's stronger "dynamical Fourier" question also permits SUCC/instrument actions that transform the fine carrier itself. Fix the source signal space \(X=\mathbb Q^M\), the coarse report space \(Y=\mathbb Q^N\), and the surjective fiber-sum map \(A:X\to Y\). Let \(U:X\to X\) be a *declared, possibly noncommuting* linear intervention, with no assumption that it is a genuine quantum or empirical instrument. Ask whether there exists an update \(V:Y\to Y\) making the **actual source/observation square** commute:

\[
\begin{array}{ccc}
X&\xrightarrow{U}&X\\
\downarrow A&&\downarrow A\\
Y&\xrightarrow{V}&Y.
\end{array}
\]

**Theorem DF5 (lawful source-changing descent).** Since \(A\) is surjective,
\[
\boxed{\exists!V:\ AU=VA\quad\iff\quad U(\ker A)\subseteq\ker A.}\tag{DF5}
\]

**Proof:** If \(AU=VA\), then for \(k\in\ker A\), \(AUk=VAk=0\). Conversely, if \(U(\ker A)\subseteq\ker A\), define \(V(Ax)=AUx\). If \(Ax=Ax'\), then \(x-x'\in\ker A\), so \(AUx=AUx'\); thus \(V\) is well-defined. Surjectivity makes it unique. For the residue-fiber map, \(\ker A\) is generated by **differences of basis vectors within each fiber**. Checking their images under \(AU\) is a complete finite linear-algebraic certificate.

**Positive source controls:** authentic SUCC shifts \(x\mapsto x+d\) and clock-unit FUCC permutations respect reduction \(\mathbb Z/M\to\mathbb Z/N\); their induced coarse dynamics are unique and the Fourier diagram inherits their dual covariance. This identity holds also for nonprime unit multipliers: **Euler provenance is an independent gate**, as before.

**Decisive noncommuting / state-changing negative control:** on \(\mathbb Q^4\to\mathbb Q^2\), let \(U=I+E_{0,2}\), the invertible shear adding coordinate 2 into coordinate 0. Then \(h=(-1,0,1,0)\) has \(Ah=0\), but \(AUh=(1,0)\ne0\). The coarse observer sees zero before the intervention and a nonzero result after it. **There is no coarse-only update \(V\)** reproducing the true fine dynamics. The source had an invisible possibility that became distinguishable *because a lawful change of carrier mixed the hidden and visible directions*.

This is a particularly concrete form of what "dynamical Fourier" must handle: it cannot consist solely of advancing the clock or decreasing projection debt. It needs a **verified Beck–Chevalley-style intervention/observation square** or a certified defect witnessing why the square does not descend. When it fails, the correct result is *UNRESOLVED/REQUIRES FINE SOURCE*, not a forged coarse theorem. The source-checker emits an exact hidden vector and post-action visible discrepancy.

All this is classical quotient-module linear algebra; it is new-to-project source/proof plumbing, not a discovery of quantum entanglement, dynamical gravity, or RH geometry.

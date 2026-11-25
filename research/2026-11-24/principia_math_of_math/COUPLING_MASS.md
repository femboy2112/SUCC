# Principia — source-coupled mass and higher-order interaction preservation

**Date:** 2026-11-24 · draft SUCC PR #690 · supplementary to CAUSAL_MEMORY.md T15–T20. **Foundational motivation:** the user's “memory of observations AND causal coupling” must retain enough signed and higher-order information to reconstruct the target mathematics, not merely the cardinality of an observational fiber.

**Scope:** classical, finite, exact arithmetic. This document derives the unique coefficients a legal quotient must preserve for linear, bilinear and arbitrary finite multilinear mathematical observables. It does not reconstruct the automorphic theta/Petersson pairing of the published RH proof.

## T21 — unique linear and bilinear source pushforward (CLASSICAL / PROVED)

Let \(I\) be a finite set of original source-labelled paths, \(q:I\to C\) a map to observed equivalence classes, and \(R\) a commutative ring; the native implementation uses \(R=\mathbb Q\). Let \(a_i\in R\) be signed weights and \(K_{ij}\in R\) a **complete** matrix of original path-pair coefficients.

For class-constant tests \(f,g:C\to R\), define
\[
L(f)=\sum_{i\in I}a_i f(q(i)),
\qquad
B(f,g)=\sum_{i,j\in I}K_{ij}f(q(i))g(q(j)).
\]

There are UNIQUE coefficients on the quotient that reproduce these values on *every* such test:
\[
\boxed{\bar a_c=\sum_{q(i)=c}a_i,\qquad
\bar K_{cd}=\sum_{\substack{q(i)=c\\q(j)=d}}K_{ij}.}
\]
Then
\[
L(f)=\sum_c\bar a_c f(c),\qquad
B(f,g)=\sum_{c,d}\bar K_{cd}f(c)g(d).
\]

**Proof:** group each finite sum by the quotient fibers. Uniqueness follows by using indicator/basis tests \(f=1_{\{c\}}\) for \(L\), and \(f=1_{\{c\}},g=1_{\{d\}}\) for \(B\). This is the exact finite fiber-summation or pushforward construction; it is not a new historical theorem in category theory. The incidence matrix \(Q\), \(Q_{ic}=1_{q(i)=c}\), gives
\[
\boxed{\bar a=Q^{\mathsf T}a,\qquad
\bar K=Q^{\mathsf T}KQ.}
\]
The second equality is a **congruence**, not an independent diagonal rescaling. If \(K\succeq0\) on a real source space, then \(\bar K\succeq0\), but source positivity does not imply it equals the *completed Weil/Petersson form* or that discarded features were class-constant.

**Necessary qualification:** if a required test distinguishes two paths within the same class, it does **not descend** to a function \(C\to R\). Refine the quotient or retain extra source data. No finite pushforward theorem licenses collapsing a target-required distinction merely because its present readout is zero.

## T22 — actual arithmetic mass survives Gaussian-theta compression

The source is the existing true Gaussian integer theta lattice \(\mathbb Z[i]\); source paths are *actual lattice points* on a fixed norm shell. At norm \(2\), the four elements \(\lambda=\pm1\pm i\) satisfy \(\lambda^4=-4\) each. Thus
\[
H_4(2)=\sum_{N(\lambda)=2}\lambda^4=-16,
\quad
\boxed{|H_4(2)|^2=256.}
\]
If compression retains only the four diagonal path energies, it instead gets
\[
\sum_{\lambda}|\lambda^4|^2=4\cdot16=64.
\]
The missing \(192\) comes from **cross-path pairings**. No new arithmetic was inserted: the kernel is the outer product \(K_{\lambda\mu}=\lambda^4\overline{\mu^4}\), and the exact pushforward retains every term of the genuine same-source square.

A second, opposite mutation exposes manufactured mass: the norm-two second holomorphic derivative has four purely imaginary contributions \(\lambda^2=\pm2i\), summing to zero. For its imaginary channel \(a_\lambda\in\{\pm2\}\),
\[
\sum a_\lambda=0,\quad
\left(\sum a_\lambda\right)^2=0,
\quad\text{but}\quad
\sum a_\lambda^2=16.
\]
If source coupling is dropped, cancellation vanishes and a **false positive** quadratic “mass” appears. The norm-three Gaussian shell has *no points*, so its coefficients vanish for a different reason; CAUSAL_MEMORY.md T20 supplies the legal higher-jet discriminator.

**Verdict:** source coupling carries exactly the quantity the finite bilinear mathematical target requires. This is a scoped, exact answer to the “missing analytic mass” intuition: it identifies *where information can be lost*. It is **not** a new RH inequality, nor a claim that the automorphic Petersson norm is this elementary theta-shell square.

## T23 — any fixed finite coupling order can miss a higher relation

The bilinear result does **not** establish that pairwise coupling universally suffices. For any \(r\ge2\), let
\[
E_r=\{x\in\{0,1\}^r:\textstyle\sum_jx_j\equiv0\pmod2\},\quad
O_r=\{x\in\{0,1\}^r:\textstyle\sum_jx_j\equiv1\pmod2\}.
\]
For every proper coordinate subset \(J\subsetneq\{1,\ldots,r\}\), and every assigned bit pattern on \(J\), *both* \(E_r\) and \(O_r\) have exactly \(2^{r-|J|-1}\) compatible assignments. Thus **all proper marginal counting measures agree**, including all pairwise ones when \(r\ge3\).

But the full parity character
\[
\chi(x)=(-1)^{\sum_{j=1}^r x_j}
\]
satisfies
\[
\boxed{\sum_{x\in E_r}\chi(x)=2^{r-1},
\qquad
\sum_{x\in O_r}\chi(x)=-2^{r-1}.}
\]

**Proof:** fixing fewer than \(r\) bits leaves at least one free bit, and each parity imposes one independent linear equation over \(\mathbb F_2\). Its remaining solutions number \(2^{r-|J|-1}\). The parity character is constant \(+1\) on \(E_r\) and \(-1\) on \(O_r\). QED.

This is a decisive **NO-GO** for an unqualified assertion that any fixed-order observer moments or pairwise data identify an arbitrary source coupling at all ranks. It does not deny that low-order observations can suffice in a *restricted* source class with additional laws.

## T24 — all finite arities have the same typed pushforward (CLASSICAL / PROVED)

For \(r\ge1\) and a source-labelled \(r\)-tensor \(K^{(r)}:I^r\to R\), pushforward along \(q:I\to C\) by
\[
\boxed{
\bar K^{(r)}_{c_1,\ldots,c_r}
=\sum_{\substack{q(i_1)=c_1\\\vdots\\q(i_r)=c_r}}
 K^{(r)}_{i_1,\ldots,i_r}.
}
\]
It is the **unique** quotient tensor that preserves all multilinear contractions with class-constant test functions \(f_1,\ldots,f_r\). The proof is the same finite regrouping as T21; uniqueness uses the \(r\) indicator/basis tests. The native implementation supports *sparse* finite tensors, exact rational coefficients, checked index dimensions, and source/quotient transport. It does not compute or claim the existence of every infinite-order analytic kernel.

**Completion frontier:** a proof requiring infinitely many arities or an infinite carrier needs a declared topology, compatibility/limit maps, and convergence/Fubini or operator-norm bounds. The finite tensor construction does not supply those properties for free. This is directly relevant to SUCC's infinite null-differential tower: exact finite stage compatibility is necessary, not sufficient, for a global theorem.

## T25 — source-weighted coupling meets causal-memory quotients

CAUSAL_MEMORY.md T15/T16 supplies the **current original-world/state coupling** \(\Gamma_h\) and a source-checked, coarsest target/future behavioral quotient of its marked states. A weighted mathematical source adds coefficients \(a_w\) and a full kernel \(K_{ww'}\). On the *surviving original worlds*, the native bridge
\[
\Gamma_h\quad\longrightarrow\quad
\bigl(\text{class}(w),a_w,K_{ww'}\bigr)
\quad\longrightarrow\quad
(\bar a,\bar K)
\]
restrains the original source **without introducing Bayesian renormalization** of signed arithmetic weights. The original transcript and source fingerprint remain attached. The resulting compressed quantities are checked by the independent source-fiber sums of T21.

A sharp negative control: two worlds with exactly identical future/target behavior form **one** behavioral class. Weights \((1,-1)\) and outer-product pairing compress to \((0,0)\); weights \((1,1)\) compress to linear mass \(2\), quadratic mass \(4\). **The behavioral quotient is identical**, while the source-weighted mathematical quantities differ. Therefore no unweighted behavioral quotient can certify analytic mass across arbitrary arithmetic sources; the relevant coefficient/pairing passport is load-bearing.

This is precisely the separation demanded by Principia: **source identity, observational indistinguishability, causal memory, target sufficiency, and quantitative capacity are distinct structures**. The behavior quotient need not be discarded; it must be *enriched with whichever quantitative source data the mathematical target requires*.

## Falsification and verification

- **DISCLOSED classical:** T21 and T24 finite pushforward identities and uniqueness; T23 parity obstruction; T25 composition of source-memory relation with the exact weighted quotient.
- **SOURCE-EXACT:** Gaussian theta fourth-jet quadratic \(256\) versus diagonal \(64\), second-jet cancellation \(0\) versus diagonal \(16\).
- **OBSERVED local:** ten two-point kernel tests, four general finite tensor/source-memory tests, and **180** independently generated exact rational kernel systems checked using a separate SymPy matrix implementation. Parity source controls cover ranks \(2,\ldots,7\) and every proper coordinate projection. All native code/tests reside in observational_succ/principia_coupling_mass.py, tests/test_principia_coupling_mass.py, tests/test_principia_higher_coupling.py and independent_coupling_mass_oracle.py.
- **UNVERIFIED:** a source-faithful, *actual automorphic theta-lift/Petersson pairing* and all RH global estimates M4–M10; compatibility of finite tensor stages with any specific analytic completion. No independent RH proof is claimed.

### Next probe that could change the verdict

Use the **actual source-defined automorphic period/lift map** as a carrier, declare the exact coefficient and pairing kernel on its lawful theta-lift paths, and test whether the proposed Principia quotient preserves every integral-minor valuation, rank and Archimedean period norm needed by (M). If all observable zeros and all low-order interactions agree while a required higher signed/lattice coupling differs, the compression must be refined. If the exact native realization preserves the required source tensors and quantitative completions, that is a genuine mathematical reconstruction milestone—not merely a translated theorem name.

**Provenance:** Principia Books III/IV, SUCC source-null and context-zero archives, CAUSAL_MEMORY.md, CM_THETA_TWO_PLACE.md, and established elementary category/linear-algebra source pushforwards. Same-project algorithms and SymPy checks are distinct methods but not independent scholarly witnesses.

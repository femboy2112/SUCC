# Multiplicative orientation Gram: divisor vs interval completions of FUCC and the log-source obstruction

**Date:** 2026-10-18. **Base:** draft Connes PR #169, originally at 9924e7783a5ef3657a48c735b5a730f76a971973, itself based on research/direct-quotient-pontryagin-transfer-2026-10-17@c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d. **Authority:** elementary mathematical proofs below; exact independent integer/Fraction probes. The GCD/Smith/Euler-totient positivity phenomenon, valuation-tree negative type, and interval covariance are classical mathematics. The comparison is new-to-SUCC research packaging, not claimed academic priority. **RH PROVED: NO.**

## Motivation: don't mistake an arbitrary positive matrix for one from multiplication on Z_{>0}

The previous local Connes bridge proved exact rational off-identity p-adic fixed-point coefficients and showed the *necessity* of distinguishing single-place idèle scaling from diagonal rational gauge. Its arbitrary-contact negative Gram mutation correctly refuted orientation **by itself** as a universal PSD theorem, but did not probe positivity arising from actual FUCC multiplication and unique factorization. The present note strengthens that test with two genuinely multiplication-covariant all-finite-set PSD Gram kernels and a nontrivial negative-type logarithmic generator.

## MOG-01. Two canonical normalized positive Gram kernels (CLASSICAL/PROVED)

For m,n≥1 let

\[
K_D(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}},\qquad
K_A(m,n)=\frac{\min(m,n)}{\sqrt{mn}}.
\]

There are two independent **Gram factorizations**, both using canonical norm-one vectors:

\[
D_n(d)=\frac{\sqrt{\varphi(d)}}{\sqrt n}\,\mathbf1_{d\mid n}\in\ell^2(\mathbb N),\quad
A_n(x)=\frac{\mathbf1_{0<x\le n}}{\sqrt n}\in L^2(\mathbb R_{>0}).
\]

The classical identity \(\sum_{d\mid r}\varphi(d)=r\), applied to r=gcd(m,n), proves
\(\langle D_m,D_n\rangle=K_D(m,n)\); indicator overlap length proves
\(\langle A_m,A_n\rangle=K_A(m,n)\). Both vectors have norm one. Hence **for every finite set of labels, every complex coefficient vector**, both kernels are PSD without assuming RH or testing any zeros. Equivalently the unnormalized exact integer matrices have distinct incidence sums of squares:

\[
\sum_{i,j}\bar c_i\,\gcd(n_i,n_j)c_j
=\sum_{d\ge1}\varphi(d)\left|\sum_{i:d\mid n_i}c_i\right|^2,
\]

\[
\sum_{i,j}\bar c_i\,\min(n_i,n_j)c_j
=\int_0^\infty\left|\sum_{i:x\le n_i}c_i\right|^2dx.
\]

Both normalized matrices are positive diagonal congruences of the respective unnormalized ones.

### FUCC equivariance and agreement along every jet

For every integer a,m,n≥1,
\(K_D(am,an)=K_D(m,n)\) and \(K_A(am,an)=K_A(m,n)\). If \(m\mid n\) or \(n\mid m\), then gcd(m,n)=min(m,n), so **all comparable FUCC pairs** agree. In particular \(K_D(1,p^k)=K_A(1,p^k)=p^{-k/2}\), matching the squared half-density coefficient of the earlier independent local Connes C_p(p^k)=p^{-k/2} construction.

The normalization \(1/\sqrt n\) is forced if one demands that each original feature vector, with squared raw norm n, be of norm one; this is a true all-finite-set PSD mechanism. It does **not** uniquely choose a representation of the full arithmetic source.


### Actual multiplication-isometry representations on one Hilbert space

Both feature families may be placed in the SAME \(\ell^2(\mathbb N)\): replace the real interval \((0,n]\) by its unit cells \(1\le j\le n\), so \(A_n(j)=n^{-1/2}\mathbf1_{j\le n}\). The arithmetic family \(D_n(d)=\sqrt{\varphi(d)/n}\mathbf1_{d\mid n}\) likewise lives in \(\ell^2(\mathbb N)\). **Both spans are dense:** for the interval features \(\sqrt n A_n-\sqrt{n-1}A_{n-1}=e_n\) (with \(A_0=0\)); for divisor features, induct on n since \(D_n(n)=\sqrt{\varphi(n)/n}>0\) and every other supporting coordinate divides n and is smaller.

Their common Gram invariance proves that for each \(a\in\mathbb N_{>0}\), the assignments
\[
T_a^D D_n=D_{an},\qquad T_a^A A_n=A_{an}
\]
are well-defined isometries on the dense spans: a vanishing linear combination stays zero because its norm is unchanged. They extend uniquely to isometries on \(\ell^2(\mathbb N)\), and \(T_aT_b=T_{ab}\) on dense generators, hence everywhere. **Thus we have two legitimate representations of the SAME multiplicative semigroup by isometries on the SAME Hilbert space, with the SAME normalized unit vector \(D_1=A_1=e_1\).** They are not generally the literal basis shift \(e_n\mapsto e_{an}\).

No unitary can intertwine both representations while fixing \(e_1\), because it would preserve all cyclic orbit inner products. But
\[
\langle T_2^De_1,T_3^De_1\rangle=1/\sqrt6,\qquad
\langle T_2^Ae_1,T_3^Ae_1\rangle=2/\sqrt6.
\]
This is a rigorous **vacuum-preserving representation inequivalence**: the choice of multiplication action and orientation is not alone sufficient to force the *specific* global covariance. It is stronger than merely inventing two PSD matrices.

## MOG-02. A real gluing defect, not merely an artificial negative toy (PROVED)

For incomparable m,n, gcd(m,n)<min(m,n). Thus \(K_A(m,n)-K_D(m,n)>0\), although the two kernels share identical diagonal entries. Already on labels (2,3),

\[
(K_A-K_D)|_{\{2,3\}}
=\frac1{\sqrt6}\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

with one positive and one negative eigenvalue. Both input matrices are PSD; their difference is indefinite. Consequently they are **not** related by an isometry preserving their labeled feature vectors, nor by an everywhere-positive correction. More generally any nonzero Hermitian matrix with zero diagonal cannot be PSD (Cauchy–Schwarz or the 2×2 principal minor). The convex continuum
\(K_\theta=(1-\theta)K_D+\theta K_A\), \(0\le\theta\le1\), is PSD, normalized, multiplication-invariant, and agrees on every comparable pair—yet its cross-prime pair (2,3) varies with θ. This is an exact *non-uniqueness under prime-jet-only observations* countermodel.

Hence the SUCC/FUCC source must specify cross-prime data, topology, and the correct trace/test transport. One-dimensional prime-jet covariance and positivity are not enough to identify the global arithmetic form.

## MOG-03. Natural logarithmic prime energy and conditional positivity (CLASSICAL/PROVED)

Write \(v_p(n)\) for the exponent of p dividing n and set
\[
d_D(m,n)=\sum_p|v_p(m)-v_p(n)|\log p
=\log\frac{mn}{\gcd(m,n)^2}.
\]
This is the weighted \(\ell^1\) valuation metric, nonnegative and multiplication invariant. Then \(K_D(m,n)=e^{-d_D(m,n)/2}\).

The *unrestricted* PSD kernel
\[
G(m,n)=\log\gcd(m,n)
=\sum_{p,k\ge1}(\log p)\,\mathbf1_{p^k\mid m}\mathbf1_{p^k\mid n}
\]
has the exact positive quadratic
\[
\sum_{i,j}\bar c_i\,G(n_i,n_j)c_j
=\sum_{p,k\ge1}(\log p)\left|\sum_{i:p^k\mid n_i}c_i\right|^2\ge0.
\]
Each finite test contains only finitely many contributing primes and powers, so there are no convergence assumptions.

Since \(\log K_D(m,n)=G(m,n)-(\log m+\log n)/2=-d_D(m,n)/2\), for every **zero-sum** finitely supported vector \(c\) the row/column terms vanish, and
\[
\boxed{
-\frac12\sum_{i,j}\bar c_i c_j\,d_D(n_i,n_j)
=\sum_{p,k\ge1}(\log p)\left|\sum_{i:p^k\mid n_i}c_i\right|^2\ge0.
}
\]
Thus d_D is conditionally negative definite and **log K_D is conditionally positive definite**: its off-diagonal entries are negative, yet its quadratic is nonnegative on the natural zero-sum difference subspace. This is a source-derived sum of squares, not a tautological GNS factorization of the completed Weil form. The zero-sum condition here is not asserted to equal the Mellin/pole-vanishing test conditions in Weil's criterion.

### Exact prime-power amplitude

Along a genuine p-ladder,
\(K_D(1,p^k)=p^{-k/2}\) and \(d_D(p^k,p^{k+1})=\log p\). Consequently
\[
d_D(p^k,p^{k+1})K_D(1,p^k)
=\frac{\log p}{\sqrt{p^k}}
=\frac{\Lambda(p^k)}{\sqrt{p^k}}.
\]
This recovers the **magnitude** of the correct von Mangoldt weight from one prime-FUCC step and the normalized carrier overlap. At n=6, the single-prime-stratum projection excludes an illegitimate log(6) prime jet. The required signed Weil distribution, the Gamma/poles/contact, and the measure of its complete test space are **not** reconstructed by this product identity.

## MOG-04. The real-log-topology discontinuity (PROVED)

There is a sharp distinction between the two otherwise compatible PSD completions. The real-log chart sends n+1 over n to
\(t_n=\log((n+1)/n)\to0\). But because gcd(n,n+1)=1,

\[
K_D(n,n+1)=\frac1{\sqrt{n(n+1)}}\to0,
\qquad
K_A(n,n+1)=\sqrt{\frac n{n+1}}\to1.
\]

On \(\mathbb Q_{>0}^\times\), the multiplication-invariant divisor kernel is a positive-definite function \(F_D(a/b)=1/\sqrt{ab}\) for coprime positive a,b. The sequence \((n+1)/n\to1\) in the **ordinary real** topology, but \(F_D((n+1)/n)\to0\ne F_D(1)=1\). Therefore **there is no continuous positive-definite function on the real additive log-line whose restriction to log Q_{>0} equals F_D**. Conversely \(K_A(m,n)=e^{-|\log(m/n)|/2}\) has this real-log continuity.

This does NOT preclude an adelic or other topology retaining prime valuations; it refutes an unqualified one-dimensional Archimedean-continuity identification of the bare divisor kernel. SUCC's unit-successor \(n\mapsto n+1\) supplies a decisive source-differentiating probe: near-neighbors are close in real-log chart but arithmetically coprime.


## MOG-08. Literal positive-integer multiplication shifts: the strong orientation test (PROVED)

The preceding two kernels are genuinely multiplicative Gram constructions. To remove any ambiguity, work directly on \(\ell^2(\mathbb N)\) with the original basis \(e_n\) and **literal** FUCC multiplication:
\[
V_p e_n=e_{pn},\quad V_p^*V_p=I.
\]
The self-adjoint multiplication adjacency \(H_p=V_p+V_p^*\) has compression on the two basis states \(e_1,e_p\) equal to
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
with eigenvalues \(+1,-1\) and quadratic values \(+2,-2\) on \(e_1\pm e_p\). Thus even an operator **literally built from multiplication on positive integers** is not automatically PSD.

However, the half-density-oriented multiplication factor
\[
A_p=(I-p^{-1/2}V_p)^*(I-p^{-1/2}V_p)
=(1+p^{-1})I-p^{-1/2}(V_p+V_p^*)
\]
is necessarily PSD. Its \(e_1,e_p\) compression has diagonal \(1+1/p\) and *negative* off-diagonal entries \(-1/\sqrt p\), while its eigenvalues are \((1\pm p^{-1/2})^2>0\). This precisely realizes the legitimate version of the hypothesis that normalized coefficients may be negative while the quadratic form is positive for structural reasons. Unlike a tautological GNS representation of the unknown Weil form, these are explicitly given original prime-multiplication operators.

The energy generator \(H e_n=(\log n)e_n\) satisfies \([H,V_p]=(\log p)V_p\) on the finite-support core, providing a second original-source route to the fundamental prime-clock \(\log p\) without reading zeros. This commutator is a classical equality and cannot alone fix Weil's contact/Gamma terms.

## MOG-09. The Möbius finite-Euler factor is positive, but the critical vacuum blows up (PROVED)

For a finite genuine prime set \(P\), put \(N_P=\prod_{p\in P}p\) and define
\[
B_P=\prod_{p\in P}(I-p^{-1/2}V_p)
=\sum_{d\mid N_P}\frac{\mu(d)}{\sqrt d}\,V_d.
\]
All factors commute because distinct prime multipliers commute. \(B_P^*B_P\) is PSD on ALL of \(\ell^2(\mathbb N)\), including arbitrary signed input vectors; Möbius signs are allowed. On the cyclic vacuum \(e_1\),
\[
B_Pe_1=\sum_{d\mid N_P}\frac{\mu(d)}{\sqrt d}\,e_d,\qquad
\|B_Pe_1\|^2=\sum_{d\mid N_P}\frac{\mu(d)^2}{d}
=\prod_{p\in P}\left(1+\frac1p\right).
\]
These identities are exact, independent of numerical prime tests.

As \(P\) exhausts all primes, Euler's divergence \(\sum_p1/p=\infty\) implies \(\prod_p(1+1/p)=\infty\). Therefore **the unnormalized product cannot converge strongly at half-density, already on e1**, even though every finite factorization is PSD. This is a concrete failure of the inference “all finite multiplicative orientation stages are positive, therefore the global half-density operator exists.” The known convergence boundary comes from elementary harmonic analysis / Euler sums, not RH.

Even dividing \(B_Pe_1\) by its growing norm cannot supply a nonzero strong vacuum: the normalized vectors all have norm 1 but converge weakly to zero, since each fixed \(e_n\) coefficient tends to zero and finitely supported tests are dense. They therefore have no strong limit. A nontrivial global object requires a different completion, renormalization or space, with source-justified test/trace pairing; it cannot be imposed by wishful passage to infinity.

The direct source test enumerates finite squarefree divisors with exact Möbius signs and amplitude-square 1/d, independently checking the exact rational product formula. The one-prime test checks the true multiplication-shift negative direction and the positive factored alternative. For \(P=\{2,3,5\}\), the exact norm square is \(12/5\). Composite 6 is explicitly rejected as a fake prime place. No global Weil positivity, trace class, canonical principal value, or RH result is inferred.

## MOG-05. Weil/Suzuki/Connes transfer remains a separate, falsifiable obligation (UNVERIFIED)

The positive source kernels act on finitely supported coefficient sequences indexed by integers, not automatically on the full Schwartz–Bruhat/Weil test space. The already-authenticated full completed Weil source contains **signed prime-power impulses plus the one real Gamma, pole/contact**, and the claimed equality
\[
B_{\rm source}(f,g)=W(f*\widetilde g)
\stackrel{?}{=}\langle Jf,Jg\rangle_{\mathcal H_{\rm mult}}
\]
for one declared source-built map J on ALL admissible tests is unproved. If J is defined only by declaring the Gram of W positive, the construction is circular; if J discards cross-prime or identity/contact information, the equality can fail while both auxiliary kernels stay PSD. The 2/3 contrast, successor near-neighbor discontinuity, and 6 false-prime mutation are mandatory probes.

This package sharpens the earlier draft Connes interface. The next serious gate is a **source-typed all-place test-transport map** between SUCC/FUCC (with both successor and prime actions) and the canonical Connes scaling trace, preserving exact contact and the original Weil functional. A bridge that matches only p^k amplitudes but not the (2,3), (n,n+1), Gamma or pole terms fails. A full source-equal noncircular positive factorization would be RH-level progress, not an implication from the elementary lemmas here.

### Exact executable receipts / independence

- observational_succ/multiplicative_orientation_gram.py: separate integer factorization, totient divisor sums, interval indicator quadratics, explicit signed valuation energies and zero-sum mutation, symbolic log-prime weights without floating transcendental tests.
- tests/test_multiplicative_orientation_gram.py: independent exact source/feature evaluations, cross-prime indefinite difference, chain invariance, discontinuous near-neighbors, fake p=6 projection and wrong-domain mutants; independent cross-oracle to observational_succ/connes_oriented_scaling.py.
- Python tests are finite calibration of stated proved identities, not their proof. An isolated local run passed ten purely arithmetic groups; an additional integration cross-oracle needs the authentic previous branch module, so only CI on the **exact final GitHub head** can certify integrated execution. Record its actual status rather than assuming success.

**Citations / provenance:** Smith's classical GCD matrix determinant (1876) and later GCD Gram theory; Connes–Consani *Weil positivity and Trace formula: the archimedean place*, arXiv:2006.13771 (restricted Sonin-compressed scaling positivity); prior SUCC O1–O8 dossier research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md and COT-01–08. **New academic priority NOT asserted. RH PROVED: NO.**


## MOG-10. Repairing the completion diagnosis: p+1 is a genuine local projective normalization (PROVED finite; CLASSICAL infinite extension)

The earlier MOG-09 no-go is **strictly representation-relative**: it rules out the *unnormalized* Euler vacuum product as a strong vector in the standard \(\ell^2(\mathbb N)\) with fixed prime-empty reference. It neither forbids normalized compatible states, an infinite tensor-product/GNS Hilbert space, nor a different analytically regularized limit. Calling it a global “failure of completion” without this qualification would be misleading.

### Arithmetic algebra, local geometry and chosen orientation

For every genuine prime p,
\[
1+\frac1p=\frac{p+1}{p}=
\frac{\#\mathbb P^1(\mathbb F_p)}{\#\mathbb A^1(\mathbb F_p)}.
\]
Indeed \(\mathbb P^1(\mathbb F_p)=\mathbb F_p\cup\{\infty\}\) has exactly p+1 directions. The Bruhat–Tits tree for \(\mathrm{PGL}_2(\mathbb Q_p)\) is \((p+1)\)-regular: upon selecting one end at infinity, each vertex has one edge toward the end and p edges away. This is a genuine classical geometric **correspondence of multiplicities**, not an identification of Connes' \(\mathrm{GL}_1\) idèle-class dynamical system with a \(\mathrm{PGL}_2\) tree.

In the Hilbert space with basis \(\{|a\rangle:a\in\mathbb F_p\}\cup\{|\infty\rangle\}\), group affine directions as
\[
|\mathrm{aff}_p\rangle=p^{-1/2}\sum_{a\in\mathbb F_p}|a\rangle.
\]
Then the exact signed unit vector
\[
\boxed{
|\psi_p^-\rangle=
\frac{\sum_a|a\rangle-|\infty\rangle}{\sqrt{p+1}}
=\sqrt{\frac{p}{p+1}}|\mathrm{aff}_p\rangle
-\frac1{\sqrt{p+1}}|\infty\rangle
=\frac{|\mathrm{aff}_p\rangle-p^{-1/2}|\infty\rangle}
{\sqrt{1+p^{-1}}}
}
\]
is exactly the normalized local Möbius **vacuum-sector** factor (under the explicit 2-sector identification). Its squared weights are p/(p+1) and 1/(p+1), reflecting p versus 1. The local sign \(-1\) is a declared Möbius phase, **not** derived from the combinatorial counting or from the choice of an end: replacing it by \(+1\) leaves all squared weights unchanged. A source-sensitive interferometric/trace test would have to distinguish those two alternatives. The two-sector identification does NOT itself intertwine the full FUCC shift \(V_p\) on every valuation level.

### Compatible finite cylinders give a legitimate global normalized state

For any finite genuine prime set F, define the two-sector tensor vector \(\Psi_F=\bigotimes_{p\in F}\psi_p^-\), of exact norm one. For a subset S⊆F, put d=∏_{p∈S}p and \(Z_F=\prod_{p\in F}(1+1/p)\); its coefficient has squared magnitude
\[
\boxed{\mathbb P_F(S)=\frac{1}{d\,Z_F}
=\prod_{p\in S}\frac1{p+1}\prod_{p\in F\setminus S}\frac p{p+1}},
\qquad\mathrm{phase}=\mu(d).
\]
These cylinder distributions are **exactly projectively compatible**: marginalizing from G to F⊆G returns \(\mathbb P_F\), since each omitted prime's probabilities sum to 1. In fact the stronger *density matrix* compatibility also holds:
\[
\mathrm{Tr}_{G\setminus F}(|\Psi_G\rangle\langle\Psi_G|)
=|\Psi_F\rangle\langle\Psi_F|.
\]
Thus the finite vectors define a normalized pure product state on the quasi-local tensor algebra, and its GNS/incomplete tensor-product Hilbert representation exists. This is a **legitimate alternative global completion**. It is not a claim that the vacuum lies in the initial \(\ell^2(\mathbb N)\) representation. The associated classical Kolmogorov product measure on \(\{0,1\}^{\mathbb P}\) has independent inclusion probabilities \(q_p=1/(p+1)\).

Since \(\sum_p1/(p+1)=\infty\) (it differs from \(\sum_p1/p\) by a convergent sum), the second Borel–Cantelli lemma gives infinitely many included primes almost surely. Thus this global **probability carrier is supported on infinite prime subsets**, not on finite natural-number labels. That explicitly records the cost of changing from \(\ell^2(\mathbb N)\) to the new completed carrier. In the old representation, the normalized \(\Psi_F\) embedded with empty unobserved primes still converges weakly to zero, not strongly: every fixed finite-squarefree label's probability tends to zero. There is no contradiction between these statements.

### A second, analytically normalized global answer: distinct from the product state

For Re(s)>1, independently of the above probabilistic Hilbert completion,
\[
Z(s)=\prod_p(1+p^{-s})
=\frac{\zeta(s)}{\zeta(2s)}
=\sum_{\substack{n\ge1\\n\text{ squarefree}}}n^{-s}.
\]
At its boundary, the **global analytic residue** is
\[
\boxed{\lim_{s\to1^+}(s-1)Z(s)=\frac1{\zeta(2)}=\frac6{\pi^2}.}
\]
This analytically normalized quantity is not the unnormalized infinite vector, nor a replacement for its local projective cylinder state. Under a prime cutoff x, a different renormalization is \(\prod_{p\le x}(1+1/p)/\log x\to (6/\pi^2)e^\gamma\) by the classical Mertens theorem: the differing \(e^\gamma\) reflects the normalization scheme. **Normalization is essential but its value is not source-free or automatically unique.**

For the standard completed zeta, \(\Gamma_{\mathbb R}(1)=\pi^{-1/2}\Gamma(1/2)=1\); it does not itself cancel the pole at s=1. The analytic pole cancellation uses \(s-1\), and \(\xi(s)=\frac12s(s-1)\Gamma_{\mathbb R}(s)\zeta(s)\) incorporates that global correction. The **projective point** \(\infty\in\mathbb P^1(\mathbb F_p)\), the **boundary end** of the local Bruhat–Tits tree, and the **Archimedean place** of \(\mathbb Q\) are three different mathematical objects; equal wording must not collapse them.

### Research verdict and next falsifiers

This repairs the misleading global-no-completion inference while preserving the correctly proved old-\(\ell^2\) no-go. We now have two rigorous completion mechanisms (quasi-local normalized product state; analytic s→1 residue), a natural local p:1 orientation geometry, and an exact sign mutation. **Neither state is shown to carry Connes' global trace, Tate's original all-place Schwartz–Bruhat distribution, Suzuki's screw form, or Weil positivity.**

The next discriminating instruments should test:
1. A source-derived, representation-theoretic map from the local \(\mathrm{PGL}_2\) p+1 projective/Hecke sector to the actual \(\mathrm{GL}_1\) idèle dilation, preserving the phase and full prime-power orbit weight, not just the 0/1 valuation vacuum.
2. Both ± signs under phase-sensitive tests; probabilities alone cannot select the arithmetic Möbius sign.
3. The exact Archimedean Gamma/pole/contact with a declared normalization scheme, including test-space topology, gamma tails and all primes, before asserting a Connes/Weil trace identity.

**References:** classical Bruhat–Tits tree construction and p+1 valency, e.g. [J. Raimbault, PGL2 tree and Hecke operators](https://perso.math.univ-toulouse.fr/jraimbau/2016/04/25/arbre-du-groupe-pgl2-et-operateurs-de-hecke/); squarefree Dirichlet Euler product e.g. [D. Burde, Analytic Number Theory notes, §3.2](https://homepage.univie.ac.at/dietrich.burde/papers/burde_81_annt_course.pdf). All-P cylinder extension/Borel–Cantelli, Mertens' product theorem, and Γ identities are attributed classical inputs. Claims originate in project synthesis, not asserted academic priority. **RH PROVED: NO.**

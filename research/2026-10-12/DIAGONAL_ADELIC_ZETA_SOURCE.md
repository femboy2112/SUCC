# Diagonal \(\mathbb Q\), two arithmetic observer systems, and source-derived zeta completion

**Date:** 2026-10-12. **Branch:** `research/diagonal-adelic-zeta-source-reciprocity-2026-10-12`, based on the dual-boundary SUCC draft PR #29 (`dc109306a8b55611f6217e956f6a1b8de543d001`). **Scope:** Exact rational arithmetic / finite cyclotomic Fourier proofs / classical analytic derivation; source declarations and numerical tests are NOT external authentication. **RH, physical entanglement, completed Weil positivity, and academic novelty are not claimed.**

**Maintainer's new proposal:** Build the primary SUCC carrier from what the finite and Archimedean observers actually share, then make their paths along provably correlated dimensions commute at shared boundary observations, with a view to reconstructing \(\zeta\) and its completion without reading zeros.

**Steelman and mathematical repair.** The canonical *common arithmetic source* is \(\mathbb Q\). It embeds diagonally into the restricted adele ring
\[
\mathbb A_{\mathbb Q}=\mathbb R\times\prod_{p}'\mathbb Q_p,
\quad \iota(q)=(q;q,q,\ldots),\quad
\mathbb A_{\mathbb Q}/\mathbb Q\text{ compact}.
\]
The completed places are **not literally the same topological space** and do not carry a single canonical probability law by virtue of sharing \(\mathbb Q\). For each \(q\in\mathbb Q\), however, their source images and normalized local characters obey checkable global constraints. ``Diagonal'' describes an actual ring morphism. The following results show exactly what is reconstructed, what is only a prescribed local test function, and what can escape between finite and full completion.

## DZ1: multiplicative SUCC/FUCC reciprocity on the genuine source (CLASSICAL; exact finite proof)

For \(q\in\mathbb Q^\times\), let \(v_p(q)\) be its authentic prime valuation, \(|q|_p=p^{-v_p(q)}\), and \(|q|_\infty\) its real absolute value. Writing \(q=\pm\prod p^{v_p(q)}\) gives
\[
\boxed{|q|_\infty\prod_p|q|_p=1.}\tag{DZ1}
\]
All but finitely many factors are 1. \(S_d(q)=q+d\), \(V_m(q)=mq\) preserve the source's embedding, and for \(m\ne0\):
\[
\boxed{V_m\circ S_d=S_{md}\circ V_m,\qquad
\iota_v\circ S_d=S_d^{(v)}\circ\iota_v,\quad
\iota_v\circ V_m=V_m^{(v)}\circ\iota_v.}\tag{DZ1b}
\]
The commuting equalities are true for **composites too**. Authenticity of a prime FUCC multiplier is an independent source check, not derived from commutativity. At a finite \(\mathbb Z/p^k\) clock, reducing \(q\in\mathbb Q_p\) as a **ring** is defined only when \(q\in\mathbb Z_p\). Multiplication by a nonunit acts as an endomorphism but does not define an invertible Fourier coordinate permutation. A nonintegral input cannot be forced into a \(\mathbb Z_p/p^k\mathbb Z_p\) ring quotient without extra scaling/precision data.

**Countermodels:** \(q,-q\) have identical finite valuations, so the product formula does not reconstruct sign; fake \(p=6\) must fail as a place; zero has no finite multiplicative valuation.

## DZ2: additive character compatibility and canonical phase reconstruction (CLASSICAL; exactly checked)

For \(q\in\mathbb Q\) and a prime \(p\), let \(\{q\}_p\in[0,1)\cap\mathbb Z[1/p]\) represent its class in \(\mathbb Q_p/\mathbb Z_p\). If \(v_p(q)=-k<0\), compute it explicitly as \(r/p^k\) with \(r\equiv p^kq\pmod{p^k}\). Otherwise \(\{q\}_p=0\). This is a well-defined group homomorphism to \(\mathbb Q/\mathbb Z\) after quotienting by integers, NOT an ordinary real-number additive homomorphism of chosen representatives.

Define \(\psi_\infty(q)=e^{-2\pi i q}\) and \(\psi_p(q)=e^{2\pi i\{q\}_p}\). Then
\[
\boxed{\sum_p\{q\}_p-q\in\mathbb Z,\qquad
\psi_\infty(q)\prod_p\psi_p(q)=1.}\tag{DZ2}
\]
**Proof without assuming the result:** write \(q=a/b\) in lowest terms, \(b=\prod_p p^{k_p}\). For each prime divisor \(p\mid b\), choose \(r_p\in\{0,\dots,p^{k_p}-1\}\) so that \(q-r_p/p^{k_p}\in\mathbb Z_p\). For all \(p\nmid b\), \(q\in\mathbb Z_p\) and the fractional part is 0. Therefore \(q-\sum_{p\mid b}r_p/p^{k_p}\) is \(p\)-integral for every prime, hence an integer; the last implication follows from unique factorization of reduced rational denominators. Exponentiation proves DZ2.

At \(q=1/6\), the two nonzero finite phases are \(1/2\) and \(2/3\), so \(1/2+2/3-1/6=1\). Omitting either local factor breaks this diagonal cancellation. But at every integer \(q\), **all these additive characters are individually 1**; the global character identity alone is NOT a faithful encoding of \(\mathbb Q\). Nor does it reconstruct real topology or the Gamma factor.

This is the correct *coherent arithmetic pairing* from which the adele Fourier transform is built. It is **not physical quantum entanglement**: no tensor product of quantum states, violation of a Bell inequality, or nonseparable density operator has been produced.

## DZ3: a finite dual-observer recovery theorem with exact resource threshold (CLASSICAL; exact finite proof)

Let \(C_H\) contain reduced rationals \(q=a/b\), with \(|a|,b\le H\), \(b>0\), and denominators prime to each selected \(p\in P\). Two candidates \(a/b,c/d\in C_H\) matching in every \(\mathbb Z/p^{k_p}\) obey \(p^{k_p}\mid(ad-bc)\). By coprimality of the moduli,
\[
M:=\prod_{p\in P}p^{k_p}\mid ad-bc,\qquad
|ad-bc|\le2H^2.
\]
Consequently,
\[
\boxed{M>2H^2\implies\text{the finite prime-observer reports uniquely identify every }q\in C_H.}\tag{DZ3}
\]
If an independently justified Archimedean observer bounds \(|q-r|\le\epsilon\), use \(|ad-bc|\le \epsilon H^2\); the smaller sufficient threshold is \(M>\epsilon H^2\). These are **uniform** over the declared finite-height source class. They do not assume the answer. The bound is sufficient, not always sharp; the implementation also independently enumerates actual small fibers.

A finite E/E'' handoff is implemented with exact source-class tables, one finite readout per selected true-prime clock, an independent rational real interval, and a compatible-source intersection. An original-source claim is PROVED only if constant on the nonempty joint fiber. A false version, forged prime or precision, contradictory reports, and hidden true-source shortcut are rejected. The single final E ``macro-SUCC'' is a counted epistemic act, not free measurement, transmission or computation.

## DZ4: receding unobserved-place obstruction / full adelic discreteness (CLASSICAL; new-to-project witness)

Do two observers converging in \(\mathbb R\) and *each of finitely many* \(\mathbb Q_p\) necessarily converge in the true global source topology? **No.** For a finite nonempty prime set \(P\), put
\[
M_n=\prod_{p\in P}p^n,\qquad
q_n=\frac{M_n}{M_n^2+1}.
\]
Then \(q_n\ne0\), \(|q_n|_\infty<1/M_n\to0\), and for each \(p\in P\), \(v_p(q_n)=n\), so \(|q_n|_p=p^{-n}\to0\). But its denominator \(M_n^2+1\) is prime to every selected \(p\); **all compensating denominator primes lie outside the observation family**:
\[
\boxed{\prod_{p\notin P}|q_n|_p=M_n^2+1\longrightarrow\infty.}\tag{DZ4}
\]
This rules out convergence of the diagonal source sequence to zero in the **full restricted adele topology**. Indeed, \(\mathbb Q\subset\mathbb A_{\mathbb Q}\) is discrete: the open neighborhood \((-1,1)\times\prod_p\mathbb Z_p\) intersects the diagonal \(\mathbb Q\) only at zero. The sequence fails its eventually-all-primes integrality gate; this is a topology issue, not a failure of DZ1.

This is the strongest falsifier of the naive assertion ``two infinite limits agree, therefore their global objects are identified.'' Finite products and full restricted products are not interchangeable; missing finite places can absorb the mismatch. It also gives a concrete arithmetic counterpart to our older *receding-escape* / unobserved-holonomy examples.

## DZ5: exact finite Fourier SUCC/FUCC duality (CLASSICAL, computational source control)

For any finite cyclic \(C_N=\mathbb Z/N\mathbb Z\) and a declared rational-valued function \(f\), let \(\zeta_N\) be a formal primitive root in the exact cyclotomic field \(\mathbb Q[X]/\Phi_N(X)\). Set
\[
\widehat f(k)=\sum_{x\in C_N} f(x)\zeta_N^{kx}.
\]
The classical orthogonality relation \(\sum_k\zeta_N^{k(x-y)}=N\,1_{x=y}\) gives exact inversion. Translation \(T_df(x)=f(x-d)\) and unit dilation \(D_mf(x)=f(m^{-1}x)\) satisfy
\[
\boxed{\widehat{T_df}(k)=\zeta_N^{kd}\widehat f(k),\qquad
\widehat{D_mf}(k)=\widehat f(mk),\quad \gcd(m,N)=1.}\tag{DZ5}
\]
The implementation uses exact rational cyclotomic polynomial division, not complex rounding, and independently tests character orthogonality, inverse, and the two commuting squares for many moduli. **Fake multiplier 6 is behaviorally legal modulo 5 but is rejected when an authentic prime-FUCC source is required.** This calibrates the Fourier duality on finite SUCC clocks; a compatible *all-place* test-function and Haar-measure construction still requires Tate's harmonic analysis.

## DZ6: where genuine completed zeta enters (CLASSICAL TATE/RIEMANN CONSTRUCTION)

**Previously missing ingredient identified precisely:** completing \(\mathbb Q\) as an adelic source is not enough to specify a zeta function. We must declare Schwartz–Bruhat test functions and compatible Haar measures.

Take the standard factorized source test function
\[
\Phi(x)=e^{-\pi x_\infty^2}\prod_p\mathbf 1_{\mathbb Z_p}(x_p).
\]
Normalize the real multiplicative measure as \(d^\times x=dx/|x|\), and each finite multiplicative Haar measure by \(\mathrm{vol}(\mathbb Z_p^\times)=1\). The local Mellin integrals are, for \(\Re s>0\),
\[
\begin{aligned}
Z_\infty(s)&=\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\frac{dx}{|x|}
=\pi^{-s/2}\Gamma(s/2),\\
Z_p(s)&=\int_{\mathbb Q_p^\times}\mathbf1_{\mathbb Z_p}(x)|x|_p^s d^\times x
=\sum_{k\ge0}p^{-ks}=\frac1{1-p^{-s}}.
\end{aligned}
\]
For \(\Re s>1\), absolute convergence and the Euler product yield
\[
\boxed{Z_\infty(s)\prod_p Z_p(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)=:\Lambda(s).}\tag{DZ6}
\]
All **prime factors and Gamma** are now realized as local contributions of a *single declared source test function*. This is the classical mechanism of Tate's thesis. It is mathematically stronger than analogizing prime clocks with a superconductor, but **the Archimedean Gaussian was a chosen, normalized test function**, not derived uniquely from integer prime-factor data. Source-specific replacement tests are mandatory.

The finite tool certifies local Euler factors at integer \(s\ge2\). A finite prime product \(P_M(2)=\prod_{p\le M}(1-p^{-2})^{-1}\) has the exact bound
\[
\boxed{P_M(2)\le\zeta(2)\le P_M(2)\frac{M+1}{M}.}\tag{DZ6a}
\]
**Proof:** omitted primes are a subset of integers \(n>M\), and \(\prod_{n=M+1}^L(1-n^{-2})^{-1}=((M+1)/M)\,(L/(L+1))\). For \(s\ge2\), each omitted factor is no larger than at \(s=2\). A separate, exact Machin-arctangent interval for \(\pi\) combines with DZ6a to enclose \(\Lambda(2)=\zeta(2)/\pi\) by two rational numbers. There is no numerical ``analytic continuation certificate'' disguised as a Fraction result.

## DZ7: the Fourier / theta commuting law produces the functional equation (CLASSICAL ANALYTIC PROOF)

The standard additive adele character is trivial on the diagonal \(\mathbb Q\) (DZ2). With self-dual Haar normalizations, the Gaussian is its own real Fourier transform and \(\mathbf1_{\mathbb Z_p}\) is its own local Fourier transform. Thus \(\Phi\) is an admissible self-dual adelic test function. Poisson summation on \(\mathbb Q\subset\mathbb A_{\mathbb Q}\), restricted to the real dilation \(\sqrt t\), yields the Jacobi identity
\[
\boxed{\theta(t)=t^{-1/2}\theta(1/t),\qquad
\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}.}\tag{DZ7a}
\]
This is where the two *dual* observer descriptions actually meet, via Fourier transform—not by unproved equality of infinite knowledge states.

For \(\Re s>1\), Mellin inversion of each positive Fourier heat term gives
\[
\Lambda(s)=\frac12\int_0^\infty(\theta(t)-1)t^{s/2-1}\,dt.
\]
Separate \((0,1)\) and \((1,\infty)\), use DZ7a, and change \(t\mapsto1/t\) in the first piece:
\[
\boxed{
\Lambda(s)=\frac1{s-1}-\frac1s+\frac12\int_1^\infty(\theta(t)-1)
\left(t^{s/2-1}+t^{(1-s)/2-1}\right)dt.}\tag{DZ7b}
\]
The integral converges uniformly on compact subsets of \(s\in\mathbb C\) because \(\theta(t)-1\) decays exponentially. It defines an entire function, so DZ7b meromorphically continues \(\Lambda\) with only possible simple poles at \(0,1\) and is manifestly invariant under \(s\mapsto1-s\). Therefore
\[
\boxed{\Lambda(s)=\Lambda(1-s),\qquad
\xi(s)=\tfrac12s(s-1)\Lambda(s)=\xi(1-s).}\tag{DZ7c}
\]
These are *established theorems*, not novel SUCC/RH claims. Numerical theta checks in the code are clearly labelled NONCERTIFICATES; the proof is the analytic Poisson/Mellin argument. The Gauss factor at real infinity is essential. A mutated source deleting the prime \(2\) while retaining the same completion multiplies \(\Lambda(s)\) by \(1-2^{-s}\), whose value is \(3/4\) at \(s=2\), but \(-1\) at \(s=-1\). This destroys the unmodified reflection law. Such a test rejects Euler-blind mimicry and does not read unknown zeros.

## What has actually advanced? (precise status)

**Constructed and checked:** one rational SUCC/FUCC source with finite and real place labels; exact multiplicative and additive reciprocity; finite-precision/finite-height reconstruction with a source-specific resource certificate; a hostile *true* convergence example exposing escape through missing primes; explicit finite Fourier functor on cyclic clocks; exact local Euler integral factors and rigorous \(s=2\) numerical enclosures; dual-receipt common-source verification. The analytic Fourier/Poisson proof connects the source to the known completed zeta functional equation, with no zero positions supplied.

**Classical prior art:** adele diagonal and its product/additive formulas; weak approximation and discreteness; Fourier analysis on finite abelian groups; rational reconstruction/CRT; Tate's thesis; Poisson/Jacobi/Mellin functional equation. **Novel-to-project:** the unified typed ObsSUCC proof receipts, exact inverse clock/FUCC source signature gates, two-sided finite recovery and escaped-prime compensator. No claims of mathematical priority or proof of RH.

**Not earned and not silently inferred:** deriving the real Gaussian *uniquely* from finite primes; actual L(s,χ) with verified conductor/epsilon/Gamma source character beyond trivial \(\zeta\); nontrivial zero-free regions; globally positive Weil form; a local-to-global positivity or arithmetic polarization; physically verified measurements; noncommuting physical entanglement; impossible quantum observer status; finite universal proof of Gaussian moat existence; analytic continuation by termwise Euler factors outside \(\Re s>1\).

## Next real RH-strength theorem targets

1. **Source-typed adelic Schwartz/Fourier functor.** Construct compatible inverse/direct limits of genuine local Bruhat test-function spaces, measure/phase normalization at \(2\), an independently verified global Schwartz source, and an exact finite approximation theorem for the Poisson/mellin duality with rigorous tail and domain control. The p-integral restriction and phase convention must survive every base-change square.
2. **Matched controls beyond zeta.** Reproduce genuine Dirichlet/Hecke L-factors with conductors, nontrivial characters, Gauss sums, Gamma parity and epsilon factors; falsify with a fake composite Euler impulse and matched non-Euler Davenport–Heilbronn-style source while using no unknown zeros as inputs. Merely having a functional equation is insufficient to force an Euler product.
3. **RH-hard identification.** Construct a noncircular completed arithmetic distribution or cohomological polarization from the original prime/Arch data, identify it with the full Weil/Suzuki test-domain form, and prove its **global** positivity. This is the proof-strength obstruction, not the already-known \(s\leftrightarrow1-s\) symmetry.
4. **Finite-to-global source-support accounting.** Quantify exactly when an observer tower's local modulus, height bound, conductor and trusted archival information prevent the missing-prime escape in DZ4. The full restricted-adele topology, rather than an arbitrary finite product topology, is load-bearing.
5. **Independent mechanization.** Formalize DZ1–DZ5, local Euler tail and rigorous \(\pi\) brackets in Lean/mathlib or an independent proof checker. Existing Python Fractions plus tests are not Lean proofs.

## External mathematics / source provenance

- [Keith Conrad, *The Character Group of Q*](https://math.stanford.edu/~conrad/154Page/handouts/characterQ.pdf): standard additive characters and rational diagonal annihilator.
- [Ngô, *Valuations of the Field of Rational Numbers*](https://math.uchicago.edu/~ngo/number.pdf): diagonal \(\mathbb Q\) discrete and cocompact in adeles.
- [Terence Tao, *Tate's proof of the functional equation*](https://terrytao.wordpress.com/2008/07/27/tates-proof-of-the-functional-equation/): additive Fourier/Poisson, adelic Gaussian, local Gamma and global zeta reflection.
- [ETH Zurich, *Fourier Analysis on Number Fields: An Exposition of Tate's Thesis*](https://www.research-collection.ethz.ch/items/3f1edd24-b9df-4ad8-8314-cbd0cb50ee84): self-dual Haar, local zeta factors, global functional equation and Riemann–Roch.
- [OpenAI Gaussian moat manuscript, pinned](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf): distinct application; all-D existence remains imported and is NOT proved here.

**Crucial negative statement:** No pointwise phase cancellation, Fourier covariance, independent positive kernel, or completed functional equation by itself implies RH. The missing Weil identification and positivity problem remains openly unresolved.

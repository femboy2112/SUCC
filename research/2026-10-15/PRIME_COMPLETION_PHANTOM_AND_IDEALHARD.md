# Prime-completion obstructions: phantom affine fixed point and Haar-null IdealHard source

**Research checkpoint:** 2026-10-15, child Tate/effective branch stacked on Classical PR #115. These are classical facts and newly combined **SUCC source-interface examples**, not claims of mathematical priority. The user-originated Simple/IdealHard/Fucked terminology is **relative to source class, probes, target and computation**.

## PC1 — the forbidden zero is a completed multiplicative fixed point

Take original positive-integer source \(S=\mathbb N_{\ge1}\), successor \(S(n)=n+1\), multiplication \(V_m(n)=mn\) for \(m\ge2\). Its faithful multiplicative-unit-centered chart is \(x=n-1\), so

\[
V_m^{\mathrm{chart}}(x)=mx+(m-1).
\]

For **each genuine prime p**, the finite source report is \(q_r(n)=n\bmod p^r\); in x-chart \(q_r^x(x)=x\bmod p^r\). For every stage \(r\ge1\), the genuine source \(n_r=p^r\) gives \(x_r=p^r-1\equiv-1\pmod{p^r}\). These stage witnesses are *different* positive integers; do not invent a single positive source satisfying all congruences. The compatible inverse-limit report is the point \(x_*=-1\in\mathbb Z_p\), equivalently \(n_*=0\in\mathbb Z_p\), which is **not in the original source**.

**Stronger invariant:** for every \(m\ge2\),

\[
V_m^{\mathrm{chart}}(-1)=m(-1)+(m-1)=-1.
\]

In the completed carrier this is a common fixed point. On the original positive source, \(V_m(n)=n\) would imply \((m-1)n=0\), impossible for \(m\ge2,n\ge1\). The global completed fixed point is therefore **a mathematically valid p-adic point but a phantom relative to the original source**. At stage r the original witness \(n=p^r\) and phantom \(n=0\) have identical residue observation and multiplication output modulo \(p^r\), but they are not the same original-source state.

The completion of positive integers with respect to these residue quotients is \(\mathbb Z_p\), with new points. Existence in that topological completion does **not** authenticate them as realized addresses on the original positive-integer carrier.

**Countermodel target:** "there exists a positive original n fixed by V_2" is false; "there exists a p-adic completed n fixed by V_2" is true. The source class is load-bearing. A new authorized non-modular source test or model-class restriction can distinguish the original-world question; this is not an intrinsic FuckedSpace label for all representations.

## PC2 — embed the classical DNR/Kleene tree into a genuine Z_2 prime-clock tower

Use the explicit computable binary tree \(T\subseteq2^{<\omega}\) from `effective_field_gates.py`. Let \(T_r=T\cap2^r\) and map \(\sigma\) to the 2-adic residue \(a_\sigma=\sum_{j<r}\sigma_j2^j\bmod2^r\). Define the clopen cylinder set

\[
C_r=\bigcup_{\sigma\in T_r}(a_\sigma+2^r\mathbb Z_2).
\]

Every \(C_r\) is a **genuine subset of the actual local ring \(\mathbb Z_2\)**; for fixed r its indicator \(f_r=1_{C_r}\) belongs to the authentic Schwartz–Bruhat window \(V_{0,r}\) of \(\mathbb Q_2\). Each finite r admits exact construction. Because T is prefix-closed, \(C_{r+1}\subseteq C_r\); because every level is nonempty, every C_r is nonempty. Compactness of \(\mathbb Z_2\) proves

\[
K=\bigcap_{r\ge0}C_r\ne\varnothing.
\]

This K is exactly the digit embedding of infinite paths through T. It contains **no computable 2-adic element**: an algorithm computing a 2-adic point to arbitrary precision would output its binary digits, giving a computable path in T, contradicting the diagonal theorem. This does NOT mean \(\mathbb Z_2\) itself lacks computable elements (0 is one); the obstruction lies in the declared closed source constraint K.

**Source class:** the *genuine source* is now the nonempty compact K, not the original full \(\mathbb Z_2\). A finite program may describe K effectively as an intersection of computable clopen sets; that is a computable *name of a closed set*, **not** an algorithm to select a member of it. The target/execution request must be named before calling this IdealHard.

## PC3 — Hilbert \(L^2\) observations lose the nonempty closed source

At level r, let \(k_r\) count indices \(e<r\) whose self-program has halted within r steps. The diagonal constraints fix exactly these k_r bits and leave the others free, independently; therefore

\[
|T_r|=2^{r-k_r},\qquad
\mu_{\mathrm{Haar}}(C_r)=\frac{|T_r|}{2^r}=2^{-k_r}.
\]

There are **infinitely many** distinct indices of immediately halting programs: take `HALT` followed by any number of unreachable `HALT` instructions. The selected explicit Cantor-cons encoding assigns distinct indices. For any integer L, choose L distinct such indices and take r larger than all of them; then all L are among the first r and have halted within r steps, so \(k_r\ge L\). Consequently \(k_r\to\infty\), hence

\[
\mu_{\mathrm{Haar}}(K)=\lim_{r\to\infty}\mu(C_r)=0.
\]

Let \(f_r=1_{C_r}\in L^2(\mathbb Z_2,\mu_{\mathrm{Haar}})\), extended by zero to \(L^2(\mathbb Q_2,dx)\) with \(\mu(\mathbb Z_2)=1\). The exact finite-window Haar energy is

\[
\|f_r\|_2^2=\int f_r\,d\mu=2^{-k_r}\longrightarrow0.
\]

Thus \(f_r\to0\) **strongly in L²**, even though \(K=\bigcap C_r\) is a **nonempty original closed source constraint with no computable points**. For each finite r, the exact Tate-normalized additive Fourier transform satisfies Parseval, so \(\|\widehat f_r\|_2^2=2^{-k_r}\to0\) as well.

This is not a mathematical inconsistency: \(L^2\) identifies functions differing on null sets, and indicator of the nonempty null set K is the zero vector a.e. The **source-set topology** and **ambient Hilbert representation** answer different questions. No positive Hilbert covariance or Fourier isometry can by itself reconstruct a global set's nonempty support once it is Haar-null. To preserve such witnesses one needs a different target topology, source-labeled state, distributional/evaluation interface, or qualified measure class—not an automatic claim that the Hilbert space is defective.

**This is the strongest new bridge for the other SUCC finite-to-global sessions:** source-topological realization and \(L^2\) norm convergence can deliver opposite-looking but simultaneously correct reports. This is a rigorous witness for why "measure-normalized completion" is not enough to identify *all* topological/global source properties.

## PC4 — exact computational scope and hostile controls

- `phantom_zero_stage(p,r,m)`: genuine prime, positive precision, nontrivial m; authentic finite positive \(n=p^r\), affine chart, and no original fixed point. Exhaustive finite controls over \(p=2,3,5,7\), \(r=1,2,3\), \(m=2,3,6,11\).
- `idealhard_2adic_stage(r)`: explicit all-residue check for \(0\le r\le7\) against the *independent* bitwise tree oracle. Computes exact admissible counts, forced positions, and rational Haar mass.
- `idealhard_2adic_packet(r)`: genuine \(V_{0,r}\) Schwartz–Bruhat function; exact cyclotomic Fourier and Plancherel; no numerical rounding.
- `padded_immediate_halt_indices(k)`: distinct syntactic HALT-padding witnesses; needed for the infinite Haar-null proof, not a fitted low-level coincidence.
- `tests/test_prime_completion_obstructions.py`: 6 targeted methods, independent enumeration, exact p-adic residue checks, energy identity, forbidden diagonal-bit mutation, invalid prime/precision controls. **Finite tests do not prove PC2–PC3's unbounded quantifiers**; classical diagonal, compactness and measure-continuity proofs do.

## PC5 — dependency and falsification boundary

This construction relies on a **classically universal** two-counter enumeration, decidable bounded simulation, source constraint C_r as actually defined, normalized *real* Haar on \(\mathbb Z_2\), and compactness. There is no claim of an algorithm computing a point of K, no empirical p-adic physical observer, and no source-derived Weil sign, completed zeta functional equation, or RH proof.

For any proposed global SUCC bridge, demand independent declarations of its **source image**, its **inverse-limit object**, and its **observable topology**. Tests should include: the phantom \(n=0\) source mutation, computable-tree nonselection, the Haar-null but nonempty K example, and a positive control where a finite-state source has a genuine computable fixed-point/witness.

Next: an explicitly typed natural transformation from **source-support/set-valued inverse limits** to analytic/distributional Tate test spaces, with a proof of which source observables survive in \(L^2\) and which necessarily live in stronger spaces. No circular positivity assumption permitted.

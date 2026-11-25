# Principia CM laboratory — one authentic Gaussian theta object, its inert-prime jets and real Gaussian size

**Date:** 2026-11-24. **Parent:** Principia Genesis draft #690 (same research branch), anchored to SUCC Main XXVI and its source/path/knowledge/null contracts. **Verdict:** genuine, fully classical CM-theta *illustration* with new native-to-SUCC reconstructions; this is **NOT** the automorphic theta-lift period map in the Alpöge–Claude RH proof. No RH implication or academic-priority claim.

## 0. Recover the object before adding a language

The concrete reference is the simplest example in Michael Rubinstein et al.'s *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, **version 2**, 22 November 2026, Part I §I.4.1 and Part III §III.12:
https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf .

§III.12 explicitly calls the lemniscate **an illustration not used in the Lean proof**. Its purpose here is to recover a genuine theorem-bearing CM source without claiming that its cheap theta kernel already supplies the full arithmetic multiplicity of (M).

The source is the Gaussian integer lattice \(\mathbb Z[i]\), its norm \(N(a+bi)=a^2+b^2\), and its theta function
\[
\Theta(z,t)=\sum_{\lambda\in\mathbb Z[i]}
\exp(-\pi t|\lambda|^2+z\lambda),\qquad t>0.
\]
At \(t=1\), this is exactly the Gaussian theta \(\Theta(z)\) of the cited illustration. Gaussian domination proves entire dependence on \(z\), and all its derivatives can be taken term by term.

For each nonnegative \(n,r\), define an **integer** holomorphic moment shell
\[
H_r(n)=\sum_{\substack{\lambda=a+bi\in\mathbb Z[i]\\ a^2+b^2=n}}\lambda^r\in\mathbb Z[i].
\]
Complex conjugation shows it is real and hence integral. Rotation \(\lambda\mapsto i\lambda\) shows \(H_r(n)=0\) for every \(n>0\) unless \(4\mid r\). The full analytic relation is
\[
\partial_z^r\Theta(0,t)
=\sum_{n\ge0}H_r(n)e^{-\pi t n}.
\]
The source carries both the **integral arithmetic** Hasse/coefficient readout and the **Archimedean Gaussian** analytic readout. The latter must not be identified with the former without transporting the \(q\)-weights.

## T9. Inert-prime coefficient transport is an exact source theorem

Let \(p\equiv3\pmod4\) be an actual rational prime. Since \(-1\) is not a square modulo \(p\), \(p\mid a^2+b^2\) implies \(p\mid a\) and \(p\mid b\): if \(b\not\equiv0\), then \((a/b)^2=-1\pmod p\), a contradiction, and similarly for \(a\). Therefore, for every \(n\ge0\), scaling Gaussian integers by \(p\) is a bijection between norm-\(n\) points and norm-\(p^2n\) points. Hence
\[
\boxed{H_r(p^2n)=p^r H_r(n)}
\]
for every derivative order \(r\ge0\) (with the convention \(0^0=1\) for \(r=0,n=0\)). This is a genuine local source-derived divisibility gain for the *holomorphic* theta shell, not an arbitrary arithmetic assignment. At split primes such as \(p=5\) the claim is false: \(3+4i\) has norm \(25\) and is not divisible by \(5\) in \(\mathbb Z[i]\).

The important precision: this is an identity of **individual norm shells**, not a statement that the complete complex analytic number \(\Theta^{(r)}(0,1)\) is an integer or p-adically integral.

## T10. Exact nonzero CM theta jet map, rank and p-adic minor

The ramified Gaussian factor \(2=-i(1+i)^2\) gives exactly four Gaussian integers of norm \(2^j\): the units times \((1+i)^j\). Since \((1+i)^4=-4\),
\[
H_{4r}(2^j)=4(-4)^{rj}.
\]
For inert \(p\), form the actual coefficient matrix
\[
M_{rj}=H_{4r}(p^2 2^j)
=4p^{4r}((-4)^j)^r,\qquad 0\le r,j<k.
\]
Each row is an **actual theta holomorphic derivative shell**; each column is an **actual, distinct source norm**. There are no fitted input values. This is a finite mathematical period-*coefficient* map, NOT the automorphic theta-period map of the RH Lean proof.

With \(x_j=(-4)^j\), ordinary Vandermonde factorization gives
\[
\boxed{\det M=4^k p^{2k(k-1)}
\prod_{0\le i<j<k}(x_j-x_i)\ne0.}
\]
Therefore the exact rank is \(k\), and \(v_p(\det M)\ge2k(k-1)\). The arithmetic growth is a *genuine proven valuation of one nonzero integer determinant* selected by the same actual theta source, not the multiplication-support depth of a basis vector. Extra valuations arising from the Vandermonde differences remain source-accounted.

At \(p=3,k=2\),
\[
M=\begin{pmatrix}4&4\\324&-1296\end{pmatrix},
\quad \det M=-6480,\quad v_3(\det M)=4.
\]
This gives a fully source-generated two-dimensional arithmetic knowledge map with no rank aliasing.

## T11. SAME map, REAL Gaussian norm, with its normalization cost paid

Choose \(q=e^{-\pi t}\in(0,1)\). For finite exact tests, \(q=1/2\) is a legal analytic \(t=\log2/\pi\). Define the **actual Gaussian weighted** matrix
\[
W=M\operatorname{diag}(q^{p^22^0},\ldots,q^{p^22^{k-1}}).
\]
Its entries are the selected terms of the very same \(\partial_z^{4r}\Theta(0,t)\) used above. Let \(n_j=p^22^j\). All of the following are exact:
\[
\det W=q^{\sum_j n_j}\det M,\quad
\|W_{r,*}\|_2^2=\sum_j M_{rj}^2q^{2n_j},
\]
and Hadamard gives
\[
\boxed{|\det M|^2\,q^{2\sum_j n_j}
\le\prod_{r=0}^{k-1}\sum_j M_{rj}^2q^{2n_j}.}
\]
The **unweighted integral determinant** is bounded by the weighted analytic row norms only after paying the explicit reciprocal factor \(q^{-\sum n_j}\). Dropping this factor would be an invalid p-adic/real comparison, precisely the kind of source-map or analytic-mass error Principia is designed to expose.

There is also a **whole-theta, not just finite-window**, real Gaussian squared-energy bound. For every \(r\ge0\), the Gaussian representation count satisfies \(r_2(n)\le4(n+1)\) for \(n\ge1\), so
\[
|H_{4r}(n)|\le r_2(n)n^{2r}\le4(n+1)n^{2r}.
\]
Inert transport then bounds the full \(p^2\)-supported shell energy
\[
\begin{aligned}
\mathcal E_{p,r}(q)
&=\sum_{n\ge1}|H_{4r}(p^2n)|^2q^{2p^2n}\\
&\le64p^{8r}\sum_{n\ge1}n^{4r+2}x^n\\
&\le\boxed{64p^{8r}(4r+2)!\frac{x}{(1-x)^{4r+3}}},\quad x=q^{2p^2}.
\end{aligned}
\]
The last inequality follows from \(n^s\le s!\binom{n+s-1}s\) and the exact binomial generating function \(\sum_{n\ge1}\binom{n+s-1}sx^n=x/(1-x)^{s+1}\). All values at rational \(q\) can be verified by integer/Fraction arithmetic; no floating approximations or unstated Gaussian tails are required.

**Crucial distinction:** this is a useful *valid joint local/real construction*, but its elementary Gaussian upper bound is very loose and the explicit normalization costs are not shown to be small. It does **not** supply an RH-strength global inequality or a positive saving after normalization.

## T12. The same CM geometry reconstructs the lemniscatic period jets

Consider the genus-one curve \(E:y^2=1-x^4\), based at \((0,1)\), with invariant holomorphic differential \(dx/y\). Its automorphism \((x,y)\mapsto(ix,y)\) exhibits CM by \(\mathbb Z[i]\). The inverse of
\[
z=\int_0^x\frac{du}{\sqrt{1-u^4}}
\]
is the lemniscate sine \(\operatorname{sl}(z)\). By differentiation,
\[
\operatorname{sl}''=-2\operatorname{sl}^3,\quad
\operatorname{sl}(0)=0,\ \operatorname{sl}'(0)=1.
\]
Thus its Hurwitz jets \(A_n=\operatorname{sl}^{(n)}(0)\) obey an exact integer recurrence involving multinomial coefficients, giving
\[
A_1=1,\quad A_5=-12,\quad A_9=3024,\quad
A_{13}=-4390848,\quad A_{17}=21224560896.
\]
All are proved *integers* by induction. The curve is nonsingular at every odd prime. Its Hasse invariant in this quartic model is the coefficient
\([x^{p-1}](1-x^4)^{(p-1)/2}\bmod p\), which vanishes for \(p\equiv3\pmod4\) and is nonzero for \(p\equiv1\pmod4\). The standard Hasse-invariant criterion (an imported classical theorem) then identifies the good inert-prime reduction as supersingular, with formal-group height two. It does not identify the curve's formal logarithm with SUCC's auxiliary Honda logarithm without an **integral coordinate change and its unit factors**.

For the theta/period bridge, define
\[
\bar\omega=2\int_0^1(1-x^4)^{-1/2}dx.
\]
The classical Jacobi/Weierstrass identity **proved for this illustration** in Rubinstein et al., version 2, §III.12, is
\[
\Theta(z,1)/T_0=\sigma(u)^2\wp(u),\quad
u=\frac{\bar\omega z}{2\pi},\
T_0=\Theta(0,1)=\frac{\sqrt2\,\bar\omega}{\pi},
\quad(g_2,g_3)=(4,0).
\]
The analytic theta-to-period identity is an **imported, cited theorem**, NOT independently proved in this round. What is reconstructed natively is its **entire rational Taylor coefficient recursion**.

Write \(x=u^4\) and \(u^2\wp(u)=A(x)=1+\sum_{k\ge1}a_k x^k\).
Since \(\wp''=6\wp^2-2\), coefficient comparison gives
\[
\boxed{
\bigl((4k-2)(4k-3)-12\bigr)a_k
=6\sum_{j=1}^{k-1}a_j a_{k-j}-2[k=1].
}
\]
Also \((\log\sigma)''=-\wp\) and \(\sigma(u)/u\to1\) yield
\[
\frac{\sigma(u)^2\wp(u)}{1}
=A(x)\exp\left(-2\sum_{k\ge1}
\frac{a_kx^k}{(4k)(4k-1)}\right)=\sum_{k\ge0} f_k x^k.
\]
The normalized theta derivatives follow **without sampling their values**:
\[
\boxed{
r_k=\frac{T_{4k}}{T_0(\bar\omega/\pi)^{4k}}
=\frac{(4k)!}{2^{4k}}f_k.
}
\]
The native Fraction recurrence produces
\[
r_1=1/4,\quad r_2=17/16,\quad r_3=-111/64,\quad
r_4=12513/256,\quad r_5=-146079/1024,
\]
matching the external guide. It gives \(4^kr_k\in\mathbb Z\) for every checked \(k\le30\). **Universal** integrality of \(4^kr_k\) is a theorem of the cited §III.12, not proven from the displayed recurrence here.

Most significantly, at \(k=30\) the **exact native recurrence**, not a fitted decimal, gives
\[
v_3(r_{30})=14<45=\frac{120\cdot3}{3^2-1}.
\]
This is the published simple-theta **negative control**. A Gaussian-sized theta with the right CM lattice/period symmetry can still **fail** the RH proof's required full local multiplicity. That failure is not repaired by pointing to the correct source or adding formally duplicate paths.

## T13. A source-sensitive Honda sign gate: first *actual* local coordinate defect

There is a concrete, falsifiable difference between the auxiliary *positive* height-two Honda logarithm of Principia T8, \(\ell_{H,+}(T)=T+T^{p^2}/p+\cdots\), and the *actual lemniscate formal logarithm*
\[
\ell_E(T)=\int_0^T\frac{dx}{\sqrt{1-x^4}}
=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(4j+1)}T^{4j+1}.
\]
The latter is derived directly from the curve \(y^2=1-x^4\), not fitted to a desired p-adic valuation. At \(p=3\), \([T^9]\ell_E=1/24\), while the positive model has coefficient \(1/3\).

If a strict coordinate \(h(T)=T+\cdots\) satisfies \(\ell_{H,+}(h(T))=\ell_E(T)\), then the first potentially nonintegral comparison coefficient is
\[
\boxed{[T^9]h=\frac1{24}-\frac13=-\frac7{24},
\quad v_3([T^9]h)=-1.}
\]
Thus this **specific positive-sign** candidate fails the p-integral coordinate requirement, already at the first p-square jet. Merely naming both source germs “height two” cannot establish their integral compatibility.

Try the opposite signed candidate \(\ell_{H,-}(T)=T-T^9/3+\cdots\). The first coefficient becomes
\[
\boxed{[T^9]h=\frac1{24}+\frac13=\frac38,
\quad v_3([T^9]h)=1.}
\]
This is a *first-coordinate positive control*, **not a full integral isomorphism**. For the checked inert primes \(3,7,11,19,23\), exact binomial arithmetic produces \(v_p([T^{p^2}]h_+)=-1\) and \(v_p([T^{p^2}]h_-)=1\). The finite observations are diagnostics, not a proof of that valuation formula for all inert primes or of a globally integral formal-group coordinate.

**Interpretation in Principia:** an apparently equivalent abstract local jet may fail to transport through the specific **integral** source map. The sign/unit data of Frobenius are not optional. This moves the M3→M4 obstruction from “integrality is a missing keyword” to an explicit first-degree, exact-rational, source-sensitive test.

The actual automorphic CM-theta integrality theorem still requires much more: the complete formal-coordinate map, proper period and conductor normalization, and persistence under all theta lifts.

## T14. Effective analytic completion is an actual theorem, not an infinite-time experiment

The theta shell construction itself supplies a rigorously controlled finite-to-analytic limit. Fix \(r\ge0\), \(q=e^{-\pi t}\in(0,1)\), and source truncation \(N\ge0\). Put
\[
S_{r,N}(q)=\sum_{n=0}^N H_{4r}(n)q^n,\qquad
n_0=N+1.
\]
As above, \(|H_{4r}(n)|\le4(n+1)n^{2r}\) for \(n\ge1\).
The ratio of two successive terms in this positive majorant is
\[
q\,\frac{n+2}{n+1}\left(\frac{n+1}{n}\right)^{2r},
\]
which is decreasing in \(n\ge1\). If
\[
R=q\,\frac{n_0+2}{n_0+1}\left(\frac{n_0+1}{n_0}\right)^{2r}<1,
\]
then the **entire infinite theta derivative** has a certified tail:
\[
\boxed{
\left|\partial_z^{4r}\Theta(0,t)-S_{r,N}(q)\right|
\le \frac{4(n_0+1)n_0^{2r}q^{n_0}}{1-R}.
}
\]

**Proof:** compare the omitted absolutely convergent source series to the displayed positive majorant and dominate the latter by the geometric series with initial term \(4(n_0+1)n_0^{2r}q^{n_0}\) and ratio \(R\). Nothing is inferred from a finite number of observations alone; the global tail theorem follows from the actual Gaussian source law.

The code evaluates the bound and rational-\(q\) partials using exact Fraction arithmetic; it refuses cutoffs where \(R\ge1\). At the paper's \(t=1\), classical \(\pi>3\) and the rational Taylor lower bound \(e^3>20\) imply \(q=e^{-\pi}<1/20\), so the same monotone rational formula at \(q=1/20\) is a **rigorous majorant** for the omitted tail there, even though the exact finite \(q=e^{-\pi}\) sum is transcendental.

This supplies Principia's source-faithful *completion* arrow on a genuine analytic CM source. It does not imply an all-order theta-period integrality theorem or RH.

## 3. Mathematical acceptance and source mapping

The branch now carries three genuinely different interfaces, and no two are silently identified:

| Source interface | Actually constructed and proved | Remaining map |
| --- | --- | --- |
| Finite shell \(H_{4r}(n)\) | Same \(\mathbb Z[i]\) theta source, inert p-adic transport, nonzero matrix determinant, real Gaussian row energies, explicit normalization cost | To the actual automorphic period-map kernels used in the proof |
| Lemniscate curve \(y^2=1-x^4\) | Exact Hurwitz jets, CM automorphism, Hasse-invariant inert vanishing; classical height-two criterion | A *certified integral* comparison to the RH formal-logarithm coordinates |
| Period-normalized theta derivatives \(r_k\) | Exact rational recurrence obtained from \(\wp,\sigma\), assuming the classical theta-period identification; precise p=3 failure | Actual theta-lift integrality and stronger valuation in its correct coordinate/weight module |

The finite integer matrix in T10 is not a Petersson-period map. Its norm is an honest Gaussian coefficient metric, not the automorphic Rallis/Petersson norm. The mathematical similarity is **scoped**.

## 4. Hostile controls and next verdict-changing theorem

- **Split prime:** p=5 admits \(3+4i\) of norm 25, invalidating inert transport.
- **Composite fake:** 15 cannot be substituted as a source prime merely because \(15\equiv3\bmod4\).
- **Holomorphic versus radial:** \(H_4(2)=-16\), whereas \(\sum_{N(\lambda)=2}N(\lambda)^2=16\); \(q\,d/dq\) and \(\partial_z\) are distinct.
- **Duplicate observer:** repeated columns give determinant zero despite multiple labels.
- **Unpaid real normalization:** replacing the unweighted arithmetic determinant by the Gaussian-weighted determinant loses the \(q^{\sum n_j}\) factor.
- **Bad p=2:** the lemniscate quartic has bad reduction; its Hasse test is not admitted.
- **Unjustified standard Honda form:** supersingularity/height two does not supply the required explicit integral coordinate isomorphism or theta-kernel integrality.
- **Simple-theta failure:** \(v_3(r_{30})=14\), not the target 45. This is a refutation of the cheap local-to-global substitution, not of the published RH theorem.

**Next theorem (UNVERIFIED):** construct a *source-normalized integral morphism* from the actual CM theta-lift kernel and its formal local coordinates into a genuine period/lattice representation, preserving both a nonzero minor's p-adic valuations and its real Petersson/period norms. Specify how its denominators, conductor, Galois action and invariant measure are paid. A test that only matches Gaussian theta moments or creates a formally large valuation without the same real object fails.

## Validation and prior art

- Native exact source engine: observational_succ/principia_cm_theta.py.
- Exact period coefficient engine: observational_succ/principia_cm_period.py.
- Focused tests: tests/test_principia_cm_theta.py; includes 18 cases and numerous parameterized exact matrix checks.
- Independent SymPy/mPMath oracle: research/2026-11-24/principia_math_of_math/independent_cm_theta_oracle.py. The 20 independent SymPy determinant/weighted-norm and Gaussian shell cases and five exact formal inversion checks are arithmetic; the numerical \(T_0,\bar\omega,r_1,r_2,r_3\) comparison is a diagnostic, not an outward-rounded proof of the theta-period theorem.
- External original: Rubinstein et al., 22 Nov 2026 guide, §I.3–I.4 and §III.12; standard Gaussian integer arithmetic, Jacobi theta/elliptic functions, Hasse invariant criterion.

This round **constructs a genuine CM theta finite-shell two-place mathematical object**; it does not construct the exact automorphic theta-period object required by RH. Source names, coordinate labels and rank arguments are no substitute for that missing theorem.

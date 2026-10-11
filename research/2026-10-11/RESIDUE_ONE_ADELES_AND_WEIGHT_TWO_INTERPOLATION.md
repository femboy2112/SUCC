# Residue-one Euler units, finite-place limits and the missing Archimedean scale

**Date:** 2026-10-11. **Maintainer's originating hypothesis:** At \(s=-1\), the Euler product is indexed by genuine primes \(p\) and the prime-local factor \(1-p\) has residue 1 modulo its own prime. Perhaps collecting infinitely many such normalized finite places constructs what should be interpreted as the “Archimedean prime valuation,” perhaps with an emerging new prime. Preserve the intuition while enforcing the distinction between finite-place local units, the global product formula, and the genuine Gamma completion.

**Mathematical status:** proved-local elementary number theory; classical compact-group/topological argument; separately established Kubota–Leopoldt interpolation and Tate adelic Fourier/Poisson constructions; exact rational software controls. The general proposed identification with RH/holographic entropy remains **UNVERIFIED**. This note is freestanding ObsSUCC research stacked above draft PR #15.

**Original mathematical sources:** Rodrigues Jacinto–Williams, *An introduction to \(p\)-adic \(L\)-functions*, Essential Number Theory 4 (2025), 101–216, [DOI 10.2140/ent.2025.4.101](https://doi.org/10.2140/ent.2025.4.101) and [arXiv:2309.15692](https://arxiv.org/abs/2309.15692); [Lean blueprint](https://cbirkbeck.github.io/AINTLIB-blueprints/padic/Overview-and-roadmap/Part-I-___-The-Kubota___Leopoldt-p-adic-L-function/); [Tate's thesis, local](https://web.stanford.edu/~dkim04/blog/tate-thesis-1/) and [global](https://web.stanford.edu/~dkim04/blog/tate-thesis-2/), expository lecture notes on the classical construction; NIST [DLMF 25.2](https://dlmf.nist.gov/25.2) and [25.4](https://dlmf.nist.gov/25.4). The interpolation and Tate results are IMPORTED theorems; finite program values do not independently construct them.

## 1. Strong positive fact: each local Euler series really converges \(p\)-adically

Fix an ACTUAL prime \(p\). The Euler factor continued to \(s=-1\) is
\[
E_p(-1)=\frac1{1-p}.
\]
This is not merely a formal rational continuation. In the local field \(\mathbb Q_p\), \(|p|_p=1/p<1\), hence
\[
\boxed{E_p(-1)=\sum_{k=0}^\infty p^k\quad\text{converges in }\mathbb Q_p.}
\]
The finite-\(K\) residual error is EXACTLY
\[
\frac1{1-p}-\sum_{k=0}^{K-1}p^k=\frac{p^K}{1-p},
\qquad
v_p(\mathrm{error})=K,\quad
|\mathrm{error}|_p=p^{-K}.
\]
Therefore
\[
\boxed{E_p(-1)\in1+p\mathbb Z_p,\quad
E_p(-1)\equiv1\pmod p,\quad |E_p(-1)|_p=1.}
\]
This gives a genuine local source-supported residue-one SUCC jet with continuously increasing p-adic precision. It is *not* the same scalar-valued convergence as the usual complex Euler factor series, which diverges at \(-1\). Different \(\mathbb Q_p\) are different completions; local convergences cannot be naively multiplied as complex scalars.

Negative controls: for composite \(q=6\), the algebra \(1/(1-q)=1+q+\cdots\) can still make sense at primes dividing q, but q is not an independent Euler prime place of \(\zeta\); the code refuses to label 6 a prime. Moreover both \((1-p)^{-1}\) and \((1-p^2)^{-1}\) are **different elements with the same residue one modulo \(p\)** and unit absolute value. Thus the residue alone discards even local information.

## 2. Exact adelic place vector and why unit residues cannot recover infinity by ordinary multiplication

All the local units form a legitimate finite-idelic unit tuple
\[
u=(u_p)_p\in\prod_p(1+p\mathbb Z_p)\subseteq
\widehat{\mathbb Z}^{\times},\quad u_p=(1-p)^{-1}.
\]
The compact product \(U=\prod_p(1+p\mathbb Z_p)\) stores MUCH more than just the mod-p residues; all those residues are 1, yet the full units vary with p.

The normalized idelic modulus for an idele \(x=(x_\infty,x_2,x_3,\ldots)\) is
\[
\|x\|=|x_\infty|_\infty\prod_p |x_p|_p.
\]
For this NON-DIAGONAL local Euler tuple \(u_p\), all finite norms equal 1. Attaching any real nonzero \(x_\infty\) gives
\[
\boxed{\|(x_\infty,u_p)_p\|=|x_\infty|.}
\]
The finite-place residue-one data alone do not pick an \(x_\infty\) or \(|x_\infty|\). If one additionally **imposes norm-one as a condition on the idele**, it forces only \(|x_\infty|=1\), not \(-1/12\) or the Gamma factor.

The standard product formula \(|r|_\infty\prod_p|r|_p=1\) applies to a SINGLE rational \(r\in\mathbb Q^\times\) embedded **diagonally** at all places. The Euler tuple \(u_p=1/(1-p)\) is not the diagonal embedding of one rational number. In particular, for the actual rational special value \(r=-1/12\),
\[
|r|_\infty=\frac1{12},\quad
|r|_2=4,\quad |r|_3=3,\quad
\prod_v|r|_v=\frac1{12}\times4\times3=1.
\]
The nonunit \(2\)- and \(3\)-adic valuations of \(-1/12\) do **not** arise as the per-place norms of \(E_p(-1)\), all of which equal 1.

### 2a. Strong no-go for a naive “continuous multiplicative Archimedean valuation”

Suppose one seeks a continuous group homomorphism
\[
A:U=\prod_p(1+p\mathbb Z_p)\rightarrow\mathbb R_{>0}
\]
that derives a nontrivial Archimedean magnitude using only multiplication of the residue-one unit group.

**Theorem (CLASSICAL elementary topology):** \(A\) is trivial.

**Proof:** Each \(1+p\mathbb Z_p\) is a compact multiplicative subgroup of \(\mathbb Z_p^\times\), so \(U\) is compact in the product topology (Tychonoff). Its continuous image \(A(U)\) is a compact subgroup of \((\mathbb R_{>0},\times)\). Applying \(\log\), its image is a compact additive subgroup of \((\mathbb R,+)\); the only such subgroup is \(\{0\}\), since any nonzero real additive element generates an unbounded subgroup. Thus \(A(U)=\{1\}\).

**Scope:** The theorem rules out THIS specific continuous multiplicative extraction, NOT a nonlinear functional, a family depending on a complex spectral parameter \(s\), a distributional/regularized trace, a Fourier/Poisson normalization or an analytic continuation. Indeed, the Tate/Gamma theory requires more than the residue-one group.

## 3. When every FINITE place sees 1 but the Archimedean place sees escape

A particularly faithful toy for the maintainer's imagery is
\[
N_m=m!+1.
\]
For any fixed prime \(p\) and any exponent \(k\), eventually \(p^k\mid m!\), so
\[
\boxed{N_m\to1\text{ in every }\mathbb Q_p,\qquad N_m\to+\infty\text{ in }\mathbb R.}
\]
In fact \(N_m\to1\) in the entire profinite ring \(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\), while the diagonal sequence does NOT converge in the whole adelic ring because its Archimedean component diverges.

This is a rigorous **finite-versus-infinite-place topology separation**. It makes the intuition more precise than saying a prime at infinity materializes: an *existing sequence of ordinary integers* approaches the same finite value at every fixed p while diverging at infinity.

Every prime divisor \(q\) of \(N_m\) is strictly larger than \(m\) (otherwise q divides both \(m!\) and \(N_m\), forcing q|1). This is Euclid's new-prime-SUPPORT argument, not a guarantee that \(N_m\) itself is prime:
\[
4!+1=25=5^2,\quad5!+1=121=11^2,\quad6!+1=721=7\cdot103.
\]

If an ORDINARY fixed integer \(n>1\) were congruent to 1 modulo literally every prime \(p\), take a prime \(p>n-1\); then p cannot divide n-1, contradiction. The only integer with residue 1 at every prime is \(n=1\), which is not prime. An **infinite limiting family** and an **actual finite integer at the limit** are different mathematical objects. In the profinite completion, all the finite residue conditions pick a compact structure, not an “Archimedean prime.”

## 4. A positive local-to-global special-value identity: p-adic zeta interpolation

The actual Kubota–Leopoldt construction gives a stronger and subtler connection than the unit norm product alone.

Its analytic \(p\)-adic zeta functions interpolate the classical Bernoulli/zeta special values after deleting the Euler factor at p. In the **weight-indexed branch convention**
\[
\zeta_{p,i}(1-k)=(1-p^{k-1})\zeta(1-k),
\quad k\equiv i\pmod{p-1},
\]
where the branch indexing and parity conventions must be declared. At weight \(k=2\), with the matching branch \(i\equiv2\pmod{p-1}\), we obtain for odd p
\[
\boxed{\zeta_{p,\mathrm{wt}\,2}(-1)=(1-p)\zeta(-1)=\frac{p-1}{12}.}
\]
Consequently, as an equality of rational special values in \(\mathbb Q_p\),
\[
\boxed{E_p(-1)\,\zeta_{p,\mathrm{wt}\,2}(-1)=-\frac1{12}.}
\]

**CAUTION ABOUT BRANCHES:** Do not write this as an equality for one universally untwisted scalar function called \(\zeta_p(-1)\) without stating the analytic branch. For example, in the convention above weight 2 belongs to residue class 2 modulo 4 at p=5, but residue class 0 modulo 2 at p=3. The authors' alternative indexing \(\zeta_{p,i}(-k)\) may shift i by one. The source cited above makes the actual Teichmüller/weight decomposition explicit.

The construction of the analytic p-adic L-function depends on Kummer congruences and p-adic measures. The code merely checks that the rational **interpolation identity**, taken as a CLASSICAL ASSUMPTION, normalizes correctly at the specified weight. It does NOT derive or construct the p-adic function from local geometric residues, nor independently infer \(\zeta(-1)\).

**This is arguably the maintainer's strongest mathematical candidate:** each prime has its own locally analytic object, the Euler correction is exactly \(1-p\), and the same rational special value appears across all the appropriate analytic branches. That is a genuine local-to-global interpolation phenomenon, yet it is *not* a limit of ordinary products of the residue-one values.

## 5. Tate's thesis gives the actual Gamma-at-infinity bridge

In Tate's local-global theory, the local zeta integral for the characteristic function \(\mathbf1_{\mathbb Z_p}\) and unramified \(|x|_p^s\) has finite-place factor
\[
Z_p(\mathbf1_{\mathbb Z_p},s)=(1-p^{-s})^{-1}
\]
for its complex convergence domain, and its meromorphic continuation is the local Euler factor. The real Gaussian \(e^{-\pi x^2}\) at infinity contributes
\[
Z_\infty(e^{-\pi x^2},s)=\pi^{-s/2}\Gamma(s/2)
\]
with a standard choice of multiplicative Haar normalization. Global Poisson summation on the adeles produces the functional equation.

The **p-adic** convergence of \(\sum p^k\) at s=-1 is a *different target coefficient topology* from the \(\mathbb C\)-valued local zeta integral for complex s; the meromorphic continuation does not become an ordinary convergent complex Euler product there.

Tate's construction also uses full Schwartz–Bruhat test functions, Fourier transforms, characters, Haar measures, a global diagonal arithmetic lattice and correctly normalized completed factors. The \(\Gamma\)-factor is not shown to arise from a continuous group homomorphism of residue-one units alone. This identifies specific additional structures required for the SUCC/FUCC proposal.

## 6. What should be developed next

The new result suggests a concrete research program:

1. Treat local SUCC/FUCC prime-jet structures as typed \(p\)-adic fields and explicit local geometric series; retain their full \(p\)-adic units and valuations, not only residue 1.
2. Build a common **weight/parameter-indexed** local interpolation system. Use the correct Teichmüller branch and Kummer congruence conditions, rather than assuming all primes' branches are interchangeable.
3. Attempt a functorial bridge from these local source functions to an adelic Fourier/Poisson family with the real/Gamma contribution. Prove every square, including topology, Haar normalization, character, source and frame domains. Existing Tate/Kubota–Leopoldt theory is primary comparison, not novelty.
4. Use fake-composite 6, missing-prime 2, unit-residue collisions and wrong analytic branch as mandatory negative controls.
5. For RH, only a source-derived full completed Weil positivity certificate on a legitimate test-function space would justify a new implication. Negative special values, rational product formulas and p-adic unit residues do not by themselves constrain all nontrivial zeros.

**Claim statuses proposed for ledger:** O139 local Q_p geometric convergence; O140 nondiagonal unit tuple and Arch magnitude underdetermination; O141 continuous compact-unit-to-real multiplicative no-go; O142 factorial+one finite/Arch divergent topology and new prime support; O143 all-prime residue-one integer \(\Rightarrow n=1\), not primality; O144 diagonal rational product formula versus local unit tuple; O145 p-adic zeta weight-two interpolation with branch; O146 Tate local/real zeta integral compatibility via global Poisson (external); O147 no RH/holographic theorem.

**Verdict:** The maintainer correctly identifies a *nontrivial p-adically convergent local structure* at every Euler prime with residue 1 and a genuine finite-versus-Archimedean tension. This does not produce a new Archimedean prime or determine a real valuation by multiplying p-adic unit norms. The most promising rigorous follow-through is the combination of **p-adic L-function interpolation and Tate's global adelic Fourier/Gamma normalization**, with source-sensitive, branch-aware proof-support transport.

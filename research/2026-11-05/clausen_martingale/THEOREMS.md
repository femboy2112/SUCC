# Operation CLAUSEN CUT × RANDOMIZED ARROWS × SELECTED BBP PRESSURE

**Draft paper mathematics, 2026-11-05.** Strict add-only child of SUCC #514 at SHA \`4243b6c5dda90d49969c62f99b3f3aae73300ebe\`. The authentic signed original four-pole forcing \(r_o(n)\), literal \(U_0=0\), full unwrapped carries, source manifests, historical Lean/proof contracts, production/workflows/license/main remain untouched. None of the following proves base-16 normality of π or a source-selected lower bound on its Vandermonde determinant.

The user's concrete question is whether source-conditioned/categorical **randomized arrows** can transport SUCC's exactly neutral and tightly concentrated Haar-seed Fekete energy into the authenticated **zero seed**. The answer is a new-to-SUCC *exact cut/deformation theorem*, a SHARP \(A^{2/3}\) source-independent mean-neutrality boundary, and a Gaussian randomized-arrow digit-block falsifier. This narrows the source-selected proof obligation, but does not pay it.

## CM-00: randomized arrows do not create structure from a true zero object by themselves

Define \(\mathbf{FinStoch}_*\) as follows: an object is a finite set X with a chosen basepoint \(x_0\). A morphism \((X,x_0)\to(Y,y_0)\) is a row-stochastic matrix \(K(y|x)\) with entries in \([0,1]\) such that the entire row at the basepoint is the Dirac distribution \(\delta_{y_0}\). Composition is ordinary stochastic matrix multiplication; the basepoint condition is preserved. (This is a **declared** subcategory of ordinary finite stochastic kernels, not a claim about every Markov category.)

The pointed singleton \(*\) is BOTH initial and terminal: from \(*\) into Y there is exactly one permitted stochastic arrow, the Dirac row at \(y_0\), and from any X into \(*\) the only row-stochastic matrix is the all-ones column. Hence \(*\) is an actual zero object in this category. Its endomorphism is uniquely the identity. It is also the tensor unit for the usual product-of-systems monoidal structure.

**Source-creation no-go.** A composable sequence of pointed stochastic arrows \(K_n:X\to X\) satisfies \(K_n(x_0)=\delta_{x_0}\) at every step. Therefore a process initialized at the pure basepoint \(\delta_{x_0}\) stays there for all times: **randomized arrows preserving the zero object cannot spontaneously produce a nonzero state from pure zero.**

The repair is explicit and source-labelled. Supply a second pointed SOURCE object S with non-basepoint \(s_1\). A pointed stochastic transition \(T:X\times S\to X\) must send the overall basepoint \((x_0,s_0)\) to \(x_0\), but it MAY map \((x_0,s_1)\) to a nontrivial distribution. For example \(X=S=\{0,1\}\) with basepoint 0, choose \(T(\cdot|0,0)=\delta_0\), \(T(\cdot|0,1)=(1/2,1/2)\), and \(T(\cdot|1,s)=\delta_1\). This preserves the categorical zero and still allows nontrivial branching when a source has been actualized.

**Connection to authentic SUCC:** the bare scalar \(U_0=0\) is a zero STATE, not itself the category's zero object. The original forcing \(r_o(n)\) is source input, so the affine arrow \(U_{n+1}=16U_n+r_o(n+1)\) is not required to preserve the basepoint. Similarly the unit-pair \(a=b=1\) is a NONZERO object of the kernel of subtraction, not the zero object. This distinguishes (1) categorical zero, (2) observed relational zero, (3) source injection, and (4) conditional randomized realization. It does not give a physical vacuum theory or a source-selected Weyl bound.

## CM-01: an exact Clausen/Bloch–Wigner boundary primitive for the authentic source

Let \(e(x)=e^{2\pi ix}\), and let \(g(t)=\log|1-e(t)|^2=2\log(2|\sin\pi t|)\). This function is 1-periodic, integrable, with \(\int_0^1g(t)dt=0\). Define its continuous periodic primitive
\[
\boxed{L(t)=\int_0^t g(v)\,dv
=-\frac1\pi\mathrm{Cl}_2(2\pi t)
=-\frac1\pi\Im\operatorname{Li}_2(e(t)).}\tag{CM1}
\]
All equalities follow from the absolutely convergent Fourier series of the primitive; the unit-circle identity is the classical Clausen/Bloch–Wigner dilogarithm, not new physics.

For ANY deterministic forcing \(r_n\), put \(U_n(s)=u_n+16^n s\), \(u_n=U_n(0)\). For integers A≥2, \(i<j\) in \([A,2A)\), define \(q_{ij}=16^j-16^i>0,\ \alpha_{ij}=u_j-u_i\) and the original #513 Fekete energy
\[
E_A(s)=A^{-2}\sum_{A\le i<j<2A}g(\alpha_{ij}+q_{ij}s).
\tag{CM2}
\]
Let an arbitrary K-digit hexadecimal cylinder be \(C_{K,d}=[d16^{-K},(d+1)16^{-K})\), \(0\le d<16^K\), and equip it with normalized Lebesgue measure \(\mu_{K,d}\). With \(s_0=d16^{-K}\), \(Q_{ij}=q_{ij}16^{-K}\), exact substitution \(v=q_{ij}s\) gives
\[
\boxed{
M_{ij}(K,d):=\mathbb E_{\mu_{K,d}}g(\alpha_{ij}+q_{ij}s)
=\frac{L(\alpha_{ij}+q_{ij}s_0+Q_{ij})
      -L(\alpha_{ij}+q_{ij}s_0)}{Q_{ij}}.}\tag{CM3}
\]
There are no numerical π digits here. For the authentic original BBP source, every \(u_n\in\mathbb Q\), and all arguments are RATIONAL, hence \(e(\text{argument})\) are roots of unity. This is an exact cyclotomic Clausen/dilogarithm boundary evaluation. It is not a sign or size estimate for the selected embedding.

## CM-02: all source/seed cross-cut interactions have O(A^-2) neutral pressure

For \(A\le K\le2A\), classify each orbit pair by its source-time relationship to the digit-resolution cut K.

- **Future–future**, \(K\le i<j\): \(Q_{ij}\in\mathbb Z\), so \(M_{ij}=0\) EXACTLY, for every source and cylinder word d.
- **Past–future**, \(i<K\le j\): write \(a=K-i\ge1,\ b=j-K\ge0\), \(\delta=16^{-a}\), \(Q=16^b-\delta\). The integer-period part cancels, leaving the short **signed boundary flux**
\[
\boxed{M_{ij}(K,d)=
-\frac1{16^b-\delta}
\int_{\beta_{ij}-\delta}^{\beta_{ij}}g(v)\,dv,\quad
\beta_{ij}=\alpha_{ij}+q_{ij}s_0.}\tag{CM4}
\]

### Uniform log-arc lemma

For every circular arc J of length \(0<\delta\le1/16\),
\[
\boxed{\left|\int_J g(t)dt\right|
\le 2\delta[1+\log(1/\delta)].}\tag{CM5}
\]
Proof: \(g(t)\le\log4\), and writing \(d(t)=\|t\|_{\mathbb R/\mathbb Z}\), the elementary inequality \(\sin(\pi d)\ge2d\) implies \((-g(t))_+\le[-2\log(4d(t))]_+\). The latter is radially decreasing from its singularity and its integral over ANY arc of length δ is maximized by the centered arc. Its centered integral is \(2\delta[1-\log(2\delta)]\le2\delta[1+\log(1/\delta)]\). The positive part contributes at most δlog4, smaller than the same bound. Thus CM5 controls the absolute signed integral, including arcs through a logarithmic singularity.

Since \(Q\ge(15/16)16^b\),
\[
|M_{ij}|\le\frac{32}{15}\,16^{-a-b}(1+a\log16).
\]
Sum over all possible a≥1 and b≥0 (this only enlarges the actual finite source-pair set); use \(\sum_{a≥1}16^{-a}=1/15\), \(\sum_{a≥1}a16^{-a}=16/225\), and \(\sum_{b≥0}16^{-b}=16/15\). Therefore
\[
\boxed{
\left|\frac1{A^2}\sum_{A\le i<K\le j<2A} M_{ij}(K,d)\right|
\le\frac{C_\times}{A^2},\
C_\times=\frac{512}{225}\left(\frac1{15}+
\frac{16\log16}{225}\right)
\approx0.60035648024865754.}\tag{CM6}
\]
**The bound is source-independent, uniform in ALL K and ALL cylinder digits d.** This is a source-time/seed-causality screening theorem, not an assumption that channels are statistically independent.

## CM-03: an exact past–past pressure bound and the sharp source-uniform A^(2/3) neutrality range

Let \(t=K-A\in[0,A]\). The only unscreened interactions lie at \(A\le i<j<K\) (both chronologically actualized before the digit cutoff). In this case \(Q_{ij}=16^{j-K}(1-16^{i-j})\in(0,1/16)\), so CM5 gives
\[
|M_{ij}|\le2[1+\log(1/Q_{ij})]
\le 2[1+(K-j)\log16+\log(16/15)].
\]
Summing j from A+1 to K-1, with j−A earlier i, and using
\[
\sum_{u=1}^{t-1}u=\frac{t(t-1)}2,\qquad
\sum_{u=1}^{t-1}u(t-u)=\frac{t(t-1)(t+1)}6,
\]
we obtain, **for any deterministic forcing and every K-digit seed prefix**:
\[
\boxed{
|\mathbb E_{\mu_{K,d}}E_A(s)|
\le\frac{
C_\times+t(t-1)[1+\log(16/15)]
+\frac{\log16}{3}t(t-1)(t+1)
}{A^2}.}\tag{CM7}
\]
At \(K\le A\), the exact value is zero, because every q_ij16^-K is an integer. At \(K=A+1\), no past–past pair exists, and the conditional absolute expectation is at most \(C_\times/A^2\).

**New universal conclusion:**
\[
\boxed{K_A-A=o(A^{2/3})
\quad\Longrightarrow\quad
\sup_{\text{source}}\sup_{0\le d<16^{K_A}}
|\mathbb E[E_A\mid C_{K_A,d}]|\to0.}\tag{CM8}
\]
The sup means *all deterministic forcing sequences, even modified/no forcing*, for the declared mathematical seed model. It says NOTHING pointwise about any chosen seed after infinite resolution. This is an exact suppression of conditional **mean** pressure through an information-depth layer.

### Sharpness against the honest unforced-zero baseline

Take r_n≡0, so u_n=0 and the source-selected seed zero is the fixed orbit. For \(A<K=A+t\le2A\), each past–past pair has α=0 and \(Q=16^{j-K}(1-16^{i-j})\). Using \(\sin\pi x=\pi x+O(x^3)\) for 0<x≤1/16,
\[
Q^{-1}\int_0^Qg(v)dv=
2\log(2\pi Q)-2+O(Q^2).
\]
Summing the exact logarithm of Q over the past–past triangular region and applying CM6 to cross-boundary terms yields UNIFORMLY for 1≤t≤A,
\[
\boxed{
\mathbb E_{\mu_{A+t,0}}E_A(s)=
-\frac{\log16}{3}\frac{t(t-1)(t+1)}{A^2}
+O\left(\frac{t^2+1}{A^2}\right).}\tag{CM9}
\]
Thus at \(t=\lfloor cA^{2/3}\rfloor\) with fixed c>0,
\[
\boxed{\mathbb E_{\mu_{A+t,0}}E_A(s)
\to-\frac{\log16}{3}c^3<0.}\tag{CM10}
\]
**The \(A^{2/3}\) exponent is optimal as a UNIVERSAL neutrality guarantee.** The original BBP source may behave differently, and its actual selected Fekete lower bound remains OPEN.

## CM-04: conditioning is a radix-16 random-arrow martingale, not a typicality oracle

Let Haar-uniform S∈[0,1), and let \(\mathcal F_K\) be the sigma-field of its first K base-16 digits. The integrable finite-energy random variable \(E_A(S)\) has conditional expectations \(\mathcal P_{A,K}(S)=\mathbb E[E_A(S)|\mathcal F_K]\), a genuine martingale in K:
\[
\mathbb E[\mathcal P_{A,K+1}|\mathcal F_K]=\mathcal P_{A,K},\quad
\mathcal P_{A,K}=0\quad(K\le A).
\]
By parent #514, \(\mathrm{Var}\,E_A(S)\le4.808/A^2\), and L² conditional expectation is a contraction. Yet on a prescribed infinite zero branch, the conditional limit may be exceptional: with r≡0, \(E_A(0)=-\infty\) for every A because all phase points collide. CM9 shows that negative pressure appears as we condition deeper into that one branch, although the full Haar-seed energy is centered and concentrated.

**No unrestricted interchange** is licensed between the information-resolution limit K→∞ and the chronological limit A→∞. The new CM8/CM10 identify a SHARP source-uniform onset scale for the conditional mean, not a source-specific theorem at the selected seed.

## CM-05: the Gaussian randomized-arrow analogy has a quantitative NON-normal digit falsifier

In the standard measure-theoretic Markov category, a stochastic arrow is a Markov kernel. For \(0<\rho<1\), the Gaussian autoregressive kernel
\[
\mathsf K(x,dy)=\mathcal N(\rho x,1-\rho^2)(dy)
\]
has stationary marginal \(\gamma=N(0,1)\), is ergodic and is time-reversible as a stationary Gaussian process. Apply its marginal CDF to the real observations:
\[
V_n=\Phi(X_n)\in(0,1),\quad V_n\sim\mathrm{Unif}(0,1).
\]
The stationary ergodic theorem gives, for almost every randomized arrow history, uniform **empirical one-time** distribution of \(V_n\). This is distinct from base-16 normality of a single number and from a digit sequence with independent block frequencies.

Define a **digit string** \(D_n=\lfloor16V_n\rfloor\in\{0,\ldots,15\}\). Each single digit is uniform. However for \(\rho=1/2\), \(D_n\ge8\iff X_n\ge0\) (up to null boundary events). Isotropic Gaussian orthant geometry gives
\[
\boxed{
\Pr(D_n\ge8,D_{n+1}\ge8)
=\frac14+\frac{\arcsin(\rho)}{2\pi}
=\frac13\quad(\rho=\tfrac12),}\tag{CM11}
\]
rather than the \(1/4\) required by a normal base-16 digit sequence (64 of the 256 two-digit blocks). Ergodicity forces the realized upper-half consecutive-pair frequency to **1/3 almost surely**. Thus **the Gaussian randomized-arrow digit string is NOT base-16 normal, despite uniform one-time marginals and a.e. real-observation equidistribution**. This is a decisive positive/negative distinction relevant to the user's "normal coded" metaphor.

The two threshold signs have joint masses \(\Pr(++)=\Pr(--)=1/3\), \(\Pr(+-)=\Pr(-+)=1/6\). Their mutual information is
\[
\boxed{
I_{\rm sign}=\frac23\log\frac43+\frac13\log\frac23
\approx0.0566330122651\ {\rm nats}>0.}\tag{CM12}
\]
The 16-symbol process has at least this much adjacent mutual information (the sign is a deterministic coarsening), so its entropy rate is at most \(\log16-I_{\rm sign}<\log16\). A randomized categorical arrow can maintain a **nonzero realized source coupling** without being normal-coded in the stronger digit-block sense.

The continuous Gaussian-field Casimir/plate interaction from #514 has an exact information interpretation:
\[
\boxed{
I(X_0;X_d)=-\frac12\log(1-\rho^{2d})
=-F_{\rm int}(d).}\tag{CM13}
\]
Both equalities follow from the 2×2 Gaussian covariance determinant and Gaussian differential entropy. This is a source/measurement category statement, not physical vacuum energy or an observed π digit process.

## CM-06: an important source-selected rational-seed equivalence (not a normality proof)

The original SUCC positive tail identity gives
\[
U_n(s)=16^n(\pi/16+s)-T_n,\qquad T_n=O(n^{-2}).
\]
For each fixed integer h, the total chord-error between e(hU_n(s)) and e(h16^n(\pi/16+s)) is bounded by \(2\pi|h|\sum_{n≥1}T_n<\infty\). Thus the source sequence U_n(s) is equidistributed mod1 **iff** \(\pi/16+s\) is normal base16 (classical Wall/Weyl).
Normality in an integer base is invariant under adding ANY rational number (Wall's theorem), so
\[
\boxed{
\text{normality of the zero-seed BBP orbit}
\iff
\text{normality of the SAME forcing orbit for ANY fixed rational seed }s.}\tag{CM14}
\]
For terminating base-16 rational s with denominator a power of 16, the two circle orbits are LITERALLY identical after finite time; for other rational s the difference phase is eventually periodic. This gives freedom to choose an alternate rational boundary in a future proof, **but does not establish that any one is normal**. The coherent counterseed \(s_*=-\pi/16\) is irrational and has completed zero phase, so the rational-seed theorem does not exclude it from the larger real-seed family.

## Verdict and next discrimination

CM1–CM14 are paper derivations from classical harmonic analysis/Markov-category/ergodic facts and original SUCC source. Their globally novel priority is NOT claimed; finite preregistered tests are calibrations and not a proof of source-selected π normality.

**STRONGEST NEW-TO-SUCC RESULT:** in every radix-16 source/cylinder, causal cut-crossing logarithmic determinant pressure is O(A^-2), and the seed-conditional field stays mean-neutral until the SHARP universal \(A^{2/3}\) pointing layer. An exact cyclotomic Clausen boundary expression identifies the remaining past–past arithmetic terms. Gaussian random arrows illustrate why uniform marginals, ergodic sampling, causal coupling, and normal digit blocks are genuinely different properties.

The original literal-zero-seed lower bound \(E_A(0)\ge-o(1)\), original fixed-h Weyl decay, original critical maximal-sharp-subinterval rate, base-16 π normality, and RH remain OPEN. A verdict-changing new inequality must control the ACTUAL centered original source/carry values \(\alpha_{ij}\) in the past–past Clausen sum. Merely switching to a random-arrow category or averaging over seeds cannot supply it.

### Classical sources / inheritance

- Tobias Fritz, *A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics*, Advances in Mathematics 370 (2020), 107239, https://doi.org/10.1016/j.aim.2020.107239 .
- GNU Scientific Library, Clausen function \(\mathrm{Cl}_2\) and dilogarithm: https://gsl.ampl.com/ref/clausen.html .
- Wall normality preservation under rational addition, restated in *Descriptive Complexity in Cantor Series*, J. Symbolic Logic: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A6DA9405DFB7D81 .
- Original SUCC #514 (seed ensemble, exact radix period, Fekete variance); #513 (determinant→Weyl); #505 (same forcing coherent wrong seed). These all share the original BBP source genealogy.

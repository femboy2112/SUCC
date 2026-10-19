# Factorial Borwein arithmetic hologram: stable cardinal reconstruction and authentic prime-clock gates

**Date:** 2026-10-19. **Branch:** \`research/factorial-borwein-holographic-clock-2026-10-19\`, pinned child of \`research/borwein-delta-prime-clock-2026-10-19\` at \`414efb07f396af4a8d15ffed9fe36d6567fda95a\` (parent draft PR #189). **Scope:** new-to-SUCC realization of classical uniform-convolution, Legendre, Fourier and cardinal-interpolation mathematics. **Academic novelty unverified. ABC OPEN; RH OPEN; signed completed Weil/Suzuki S4 OPEN.** No source-archive files were modified.

## 0. Actual inputs versus analogy

The prior SUCC \`borwein_prime_clock.py\` constructs Borwein uniform-sum CDFs, true prime-clock delta gates, and exact finite gated walks. This **child** does not replicate those. It constructs an \`N!\`-dependent Borwein embedding \`I_N : ell^2(Z) -> L^2(R)\` whose integer samples **erase N**, while variance and higher local Fourier moments recover the genuine prime-power window structure.

Three different meanings of "factorial" are kept separate:
- **Arithmetic Legendre occupation:** \`v_p(N!)=sum_{j>=1}floor(N/p^j)\`.
- **Simplex volume:** a finite uniform-sum / Borwein leakage contains \`1/m!\` from inclusion-exclusion geometry (already derived in parent PR #189).
- **Poissonized SUCC:** \`e^{t(S-I)}=e^{-t}sum t^k S^k/k!\` with \`1/k!\` from ordered event times.

They are compatible interfaces, not one undifferentiated normalization. A sinc width is **not** a prime-residue measurement. Clock residues must be authenticated separately on the integer source.

## 1. Construction and uniform-width theorem (PROVED LOCAL, classical ingredients)

For each positive integer N define
\[
J_N=\{(p,k):p\text{ prime},\ 2\le k\le v_p(N!)\},\quad h_{p,k}=\frac1{2p^k},\quad
S_N=\sum_{(p,k)\in J_N}\frac1{p^k}.
\]
Set \`U_h(x)=1_{[-h,h]}(x)/(2h)\` as a probability density and
\[
\boxed{B_N=U_{1/2}*\mathop{*}_{(p,k)\in J_N}U_{h_{p,k}}.}
\]
For N<=3 this is the central box (endpoints assigned half values); for N>=4 it is a continuous compactly supported nonnegative density. Its Fourier transform is
\[
\boxed{\widehat B_N(\xi)=\operatorname{sinc}(\xi/2)
\prod_{(p,k)\in J_N}\operatorname{sinc}(\xi/(2p^k)).}
\]
Using the *infinite* sum of all repeated-prime power reciprocal widths,
\[
0\le S_N\le\sum_{p}\sum_{k\ge2}p^{-k}
=\sum_p\frac1{p(p-1)}
<\sum_{\substack{m\ge2\\m\ne4}}\frac1{m(m-1)}
=\frac{11}{12}<1.
\]
(The missing integer 4 makes the inequality uniform and strict.)

Put \`r_N=(1-S_N)/2\` and \`R_N=(1+S_N)/2\`. Then
\[
\boxed{r_N>1/24,\quad R_N<23/24,\quad B_N(x)=1\ (|x|\le r_N),
\quad B_N(x)=0\ (|x|\ge R_N).}
\]
**Proof:** all added uniform jumps have total absolute displacement at most \`S_N/2\`; averaging the unit-height base box leaves its interior \`|x|<=1/2-S_N/2\` exactly unchanged and the support stays within \`1/2+S_N/2<1\`. At support boundaries the density vanishes for N>=4. No prime distribution theorem is needed.

The original Borwein–Borwein sinc paper gives the classical Fourier/convolution basis: D. Borwein and J.M. Borwein (2001), *Some Remarkable Properties of Sinc and Related Integrals*, Ramanujan Journal 5, 73–89, Theorem 1:
https://gwern.net/doc/math/humor/2001-borwein.pdf .
This paper does **not** contain or establish our specific factorial arithmetic indexing or any claim of novelty for it.

## 2. A uniformly stable source–target–source hologram (PROVED LOCAL)

**Theorem FBH-01.** For N>=4:
\[
\boxed{B_N(m)=\mathbf1_{m=0}\quad(m\in\mathbb Z),}
\qquad
\boxed{\sum_{m\in\mathbb Z} B_N(x-m)=1\quad(x\in\mathbb R).}
\]
The first is immediate from the radius bounds. For the second, integer translates of \`U_{1/2}\` partition unity a.e.; convolve this identity with the probability density of all the smaller jumps. The result is continuous for N>=4, so the identity holds pointwise. For N<=3 the half-value endpoint convention gives the same partition.

For a finitely supported integer sequence \`c\`, put
\[
(I_Nc)(x)=\sum_{m\in\mathbb Z}c_m B_N(x-m),\qquad
(Rf)(m)=f(m)\quad (f\in\operatorname{ran}I_N).
\]
Then \`R I_N = identity\`, with exact cardinal recovery. Crucially, this isn't merely algebraic:
\[
\boxed{
(1-S_N)\|c\|_{\ell^2}^2
\le \|I_Nc\|_{L^2(\mathbb R)}^2
\le\|c\|_{\ell^2}^2,\qquad
1-S_N>1/12.
}
\]
**Lower proof:** on each disjoint core \`[m-r_N,m+r_N]\`, \`B_N(x-m)=1\` and all other integer translates vanish almost everywhere. Integration gives \`2r_N|c_m|^2\` at each site. **Upper proof:** the nonnegative partition weights sum to one; Jensen gives \`|I_Nc(x)|^2<=sum_m B_N(x-m)|c_m|^2\`; integrate, using \`int B_N=1\`. Density of finite sequences extends this to all \`ell^2(Z)\`. \`R\` is bounded on **the range only**, with norm at most \`(1-S_N)^(-1/2)\`; no bounded point-sampling of arbitrary L2 functions is claimed.

For N>=4, all kernels also agree on the **half-integer** lattice:
\[
B_N(1/2)=B_N(-1/2)=1/2,\qquad B_N(m+1/2)=0
\quad\text{if }|m+1/2|\ge3/2.
\]
This follows by symmetry and the total smaller-jump support contained in \`(-1/2,1/2)\`. A fixed integer or half-integer sampling instrument **cannot tell N apart**. This is a rigorous probe-gap, not intrinsic identity of the continuous kernels.

## 3. Exact nonorthogonal Hilbert Gram geometry (PROVED LOCAL)

Let \`g_j=int_R B_N(x)B_N(x-j)dx=(B_N*B_N)(j)\`. Support gives \`g_j=0\` for \`|j|>=2\`, while positivity of convolution on the interior gives \`g_1>0\` for N>=4. Partition unity implies \`g_0+2g_1=1\`.

Consequently
\[
\|I_Nc\|_2^2=g_0\sum_m|c_m|^2+
2g_1\operatorname{Re}\sum_m c_m\overline{c_{m+1}}.
\]
The Fourier Gram symbol is \`g_0+2g_1 cos(theta)\`, with \`g_0-2g_1>=1-S_N>1/12\`. The lifts are **cardinal but not orthogonal in L2(R)**. This corrects a tempting identification with orthonormal Hilbert bases or an automatic positive signed Weil form.

Two exact independent inclusion-exclusion Gram witnesses:
\[
(g_0,g_1)_{N=4}=(871/960,\ 89/1920),\qquad
g_0-2g_1=391/480;
\]
\[
(g_0-2g_1)_{N=6}
=45340537298096683/56873575734312960.
\]
The complete fractions are recorded by \`scripts/factorial_borwein_hologram_probe.py\`. The CDF oracle uses the parent PR #189 algorithm; the Gram PDF is independently implemented from the generalized Irwin–Hall signed subset formula.

## 4. Exact prime/composite spectral injection (PROVED LOCAL)

\[
V_N:=\operatorname{Var}(B_N)
=\frac1{12}\left(1+\sum_{(p,k)\in J_N}p^{-2k}\right).
\]
Hence
\[
\boxed{V_N-V_{N-1}=\frac1{12}
\sum_{\substack{p\text{ prime},\,k\ge2\\
v_p((N-1)!)<k\le v_p(N!)}}p^{-2k},}
\quad N\ge2.
\]
The sum is nonnegative and
\[
\boxed{V_N=V_{N-1}\iff N\text{ prime},\quad N\ge2.}
\]
**Proof:** if N is prime, the only new factorial prime occupancy is its first appearance \`v_N(N!)=1\`, excluded from \`J_N\`. If N is composite, it has some prime divisor \`p<N\`, and \`v_p((N-1)!)>=1\` because p itself occurs in the preceding factorial. Its new occupancy at step N therefore creates at least one \`k>=2\` window, making the increment positive.

Exact examples:
\[
V_4-V_3=5/768,\quad V_5-V_4=0,\quad
V_6-V_5=337/248832,\quad V_7-V_6=0.
\]
This is **not a computational shortcut to primality**: constructing the source windows already uses genuine primes and Legendre valuations. It is an exact arithmetic/spectral transport identity.

## 5. Spectrum retains the widths that the samples erase (PROVED LOCAL)

Near \`xi=0\`, all \`sinc\` factors are positive and
\[
\boxed{
\log\widehat B_N(\xi)
=-\sum_{r\ge1}\frac{\zeta(2r)}{r\pi^{2r}}
\left(\frac1{2^{2r}}+\sum_{(p,k)\in J_N}(2p^k)^{-2r}\right)\xi^{2r}.
}
\]
The expansion follows from Euler's product for sine; coefficients never vanish. Therefore the full analytic germ yields the power sums of the **finite multiset of squared uniform half-widths**. Newton's identities reconstruct the monic polynomial \`prod_j(z-h_j²)\`, hence all prime-power widths, with their multiplicities. This is exact finite moment recovery **with a declared Fourier probe**, not knowledge extracted from the integer samples alone.

An adversarial example:
\[
B_4(3/10)=B_5(3/10)=1,\qquad
B_6(3/10)=B_7(3/10)=30922061/31104000<1.
\]
But even the off-grid point \`1/10\` lies in the common plateau and **cannot** distinguish \`B_4\` from \`B_6\`. No blanket one-probe identification claim survives.

## 6. Infinite factorial limit with an effective uniform bound (PROVED LOCAL)

The infinite random series of independent centered uniforms with half-widths \`1/(2p^k)\` for every genuine \`p\` and \`k>=2\` converges **absolutely** because the sum of those half-widths is finite. Convolve its law with \`U_(1/2)\` to define \`B_infty\`. It has the same plateau/supported cardinal properties.

For N>=4, the fixed window \`U_(1/8)\` is always present. Write \`B_N=U_(1/8)*G_N\` where \`0<=G_N<=1\` because the base \`U_(1/2)\` has height one. Thus \`B_N\` is 4-Lipschitz uniformly in N. The sum of omitted *twice-half-widths* is at most
\[
E_N=
\sum_{p\le N}\frac{1}{p^{v_p(N!)}(p-1)}
+\frac1N.
\]
For p<=N, the term is the exact geometric tail; for p>N, bound \`sum_p 1/[p(p-1)]\` by the telescoping integer tail \`1/N\`.
A direct coupling of common uniforms therefore yields
\[
\boxed{\|B_\infty-B_N\|_\infty\le 2E_N,\qquad E_N\to0.}
\]
The limit follows by domination of the summable prime-power width series, not by numerical extrapolation. \`infinite_tail_budget(N)\` computes the finite rational certificate. This controls the **kernel limit**, not the number-theoretic tails required to prove ABC.

## 7. Source-clock lift, factorial Poisson SUCC, and two negative controls

Define \`P_{p,r}\` on integer coefficients by source-authenticated residue \`m mod p=r\`, and \`S c(m)=c(m-1)\`. On the image of \`I_N\`, the lifted action \`I_N P_{p,r} R\` is idempotent, while \`I_N S R\` intertwines with real translation by 1. For different N,M, \`I_M R I_N=I_M\`; the transition **changes off-lattice geometry but preserves all integer source values**. This is a flat source-certificate transport, not a claim that all continuous kernels are equal.

For any set of genuine prime-clock gates \`A\`, \`t>=0\`, source n and integer M>=0,
\[
P_{M,A}(t,n)=\sum_{k=0}^M\frac{t^k}{k!}\mathbf1_{n+k\in A},
\quad
\left|e^{-t}P_{M,A}-\Pr(n+\mathrm{Pois}(t)\in A)\right|
\le \frac{t^{M+1}}{(M+1)!}.
\]
The bound follows from \`Pr(Pois(t)>=M+1)<=E[binom(Pois(t),M+1)]=t^(M+1)/(M+1)!\`. \`poisson_wheel_polynomial\` returns the exact rational polynomial and certified tail, retaining actual \`p,r\` orientation including negative SUCC sites.

**Hostile mutation #1: first prime occupations destroy the cardinal delta.** Replace the repeated widths by first-occupation widths for p=2,3,5. Their sum \`1/2+1/3+1/5=31/30>1\`. For \`U_(1/2)*U_(1/4)*U_(1/6)*U_(1/10)\`, the *false* integer delta has
\[
\boxed{B_{\mathrm{mutated}}(1)=1/43200>0.}
\]
Exact independent CDF calculation. Thus the restriction to repeated occupations is load-bearing, not ornamental.

**Hostile mutation #2: stochastic/Hilbert positivity is not Weil positivity.** Every \`B_N\` is a nonnegative probability kernel, and its translate Gram is PSD (indeed coercive). The signed completed Suzuki/Weil form involves the genuine Gamma, pole, conductor, and prime-power source signs. No map identifying these objects has been proved. The RH-equivalent obstruction \`S4\` stays OPEN.

## 8. Reproduce, falsify, and carry forward

- Module: \`observational_succ/factorial_borwein_hologram.py\` (exact Fractions, authentic p, bounded analytic subset sums).
- Tests: \`tests/test_factorial_borwein_hologram.py\`; **13 tests** with independent factorial valuation, prime/nonprime, 2-implementations of spline/CDF, exact Gram, half-grid nonidentification, source gates, and first-occupation mutation.
- Probe: \`python -m scripts.factorial_borwein_hologram_probe\`.
- CI: \`.github/workflows/factorial-borwein-hologram.yml\` in Python 3.10/3.13. Local standalone Python 3.13 used a mathematical surrogate of upstream Borwein CDF; actual parent integration must be established by hosted CI before claiming complete compatibility.
- Algebra/probability statuses: **PROVED LOCAL** from displayed proofs; **TESTED MODEL** for the executable rational certificates; **UNVERIFIED** for Lean, academic priority, ABC/RH implications, and growing-modulus prime-tuple correlations.

**Next verdict-changing probe:** couple \`(I_{N_a},I_{N_b},I_{N_c})\` to authentic primitive \`a+b=c\` cancellation **with the shared residue moduli explicitly transported across all three slots**, then test whether any derived family inequality outperforms the established Bernert–Browning–Lichtman–Teräväinen 2026 ABC exceptional-set benchmark. A width/cumulant fit without such source-authenticated arithmetic and an independent holdout is not a new ABC theorem.


## 9. Prime-wheel spectral mixing: factorial normalization is NOT uniform in growing W (CLASSICAL, PROVED LOCAL)

Fix a wheel \`W>=2\`, a nonempty residue set \`A\subset Z/WZ\`, and the declared SUCC orientation \`n->n+1\`. The factorial-normalized Poisson clock function is
\[
F_{W,A}(t,n)=\frac{W}{|A|}e^{-t}
\sum_{k=0}^{\infty}\frac{t^k}{k!}\mathbf1_{n+k\bmod W\in A}.
\]
Discrete Fourier orthogonality gives the **exact** spectral representation
\[
F_{W,A}(t,n)
=\frac1{|A|}\sum_{j=0}^{W-1}
\widehat{\mathbf1_A}(j)
e^{2\pi i jn/W}\,
\exp\{t(e^{2\pi ij/W}-1)\},
\quad
\widehat{\mathbf1_A}(j)=\sum_{r\in A}e^{-2\pi ijr/W}.
\]
The \`j=0\` term is exactly 1. Nonzero modes decay at rates \`1-cos(2*pi*j/W)\`; the slowest rate is
\[
\boxed{\Delta_W=1-\cos(2\pi/W)=2\sin^2(\pi/W),\qquad
8/W^2\le\Delta_W\le2\pi^2/W^2.}
\]
The bounds follow from \`2u/pi<=sin(u)<=u\` for \`u in [0,pi/2]\`.

In particular, for the Poisson SUCC displacement on \`Z/WZ\`, a first Fourier character is a normalized bounded test with mean zero under uniform Haar, so the total-variation distance to uniform satisfies
\[
\boxed{
\tfrac12 e^{-t\Delta_W}
\le \mathrm{TV}(\operatorname{Pois}(t)\bmod W,\mathrm{Haar}_W)
\le\min\!\bigl(1,\tfrac{W-1}{2}e^{-t\Delta_W}\bigr).
}
\]
The upper bound is Fourier inversion and triangle inequality; the lower bound tests \`exp(2*pi*i n/W)\` against the difference of measures. **Consequently, no fixed time t makes prime wheels mix uniformly as W grows**. The relaxation scale is at least order \`W²\`; using a factorial denominator \`k!\` does not erase an expanding CRT period. For W=870870, the slow Fourier rate is about \`2.6e-11\`, illustrative only; the inequality itself is exact.

**What this rules out:** extracting growing-wheel prime independence or a uniform ABC \`K_eps\` simply by Poissonizing the SUCC clock. Green–Tao's transference needs pseudorandom majorants and control of arithmetic linear forms, not merely a finite-wheel heat kernel. No RH/Weil positivity statement follows.

## 10. Validation correction

The first hosted CI attempt completed **8/8 parent tests and 13/13 child tests on both Python 3.10 and 3.13**, but failed *after the tests* because the receipt script was run as \`python scripts/...\` without the repository root on \`sys.path\`. The workflow was corrected to
\`python -m scripts.factorial_borwein_hologram_probe\` and then **passed** on both interpreters. This is a repository-execution import-path correction, not a mathematical patch. The directly reproducible checkout commands are:

\`\`\`sh
python -m unittest discover -s tests -p 'test_borwein_prime_clock.py' -v
python -m unittest discover -s tests -p 'test_factorial_borwein_hologram.py' -v
python -m scripts.factorial_borwein_hologram_probe
\`\`\`

The remaining full existing SUCC validation status is controlled by its independent workflow, not inferred from the focused proof-access gate.

# Operation Zero–One — SUCC formal endpoint characters and the original BBP logarithmic seam

**2026-10-27 · additive research child of PR #335, pinned parent aa270c4ed733e8220d02748c3cf8a83047e8258b.** The original four signed BBP poles, U_0=0, archival proof contracts, research history and main are NOT modified. **π base-16 normality and RH remain OPEN.** Mathematical claims are scoped; no scholarly-priority claims for classical formal completions, Gauss digamma values or Habiro rings.

## ZO-0. Literal p=0/1 degenerates; the correctly typed objects are formal q-neighborhoods

The ordinary inverse-limit formula applied literally gives

$$
\varprojlim_k\mathbb Z/1^k\mathbb Z=0,\qquad
\varprojlim_k\mathbb Z/0^k\mathbb Z=\mathbb Z\ \text{with the discrete topology}.
$$

No nontrivial prime-like locally compact field or canonical integer-digit character follows. The faithful reinterpretation uses the polynomial successor parameter q and the two **different ideal-adic completions**

$$
\mathcal O_0=\mathbb Q[[q]],\qquad
\mathcal O_1=\mathbb Q[[q-1]].
$$

For a polynomial f, a depth-K 0-character is

$$
\chi_{0,K,\theta}(f)=
e\left(\sum_{j<K}\theta_j[q^j]f\right),
$$

and a depth-J 1-character is

$$
\chi_{1,J,\eta}(f)=
e\left(\sum_{j<J}\eta_j[s^j]f(1-s)\right),\qquad s=1-q.
$$

Take rational weights for exact character phases, or real weights for real-linear coefficient functionals; e(x)=exp(2πix). These are explicit continuous finite-jet **additive characters**, not a claimed complete Pontryagin-dual classification.

There is no continuous identity extension from the q=0 completion to the q=1 completion: q^N tends formally to zero at 0 but q^N≡1 mod(q−1). Conversely, (1−q)^N tends to zero at 1 but has constant coefficient 1 at 0. A genuine source-specific analytic transport must pay for this incompatibility.

## ZO-1. An exact analytic bridge: the authentic BBP source as one function

Keep the original signed four-pole forcing

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$

Define

$$
\boxed{G(q)=\sum_{n\ge1}r(n)q^{n-1}}
$$

for |q|<1. The exact rational Mellin kernel is

$$
P(x)=4-2x^3-x^4-x^5=(1-x)(x^2+2)(x^2+2x+2),
$$

and geometric summation gives

$$
\boxed{G(q)=\int_0^1\frac{P(x)}{1-qx^8}\,dx.}
$$

The original BBP identity is **exactly**

$$
\boxed{G(1/16)=\pi.}
$$

Since P(x)≥0 on [0,1], P(1)=0 and P'(1)=−15, the positive source coefficients are absolutely summable and

$$
r(n)=\frac{15}{64n^2}+O(n^{-3}).
$$

The q=0 coefficients are the entire causal source history, the q=1 boundary is a finite source mass, and q=1/16 is the real selected value. These are **three distinct operations on a common authentic analytic source**.

A suitable joint host is the Banach source class

$$
\mathcal W^{(1)}
=\left\{
G(q)=c\frac{\mathrm{Li}_2(q)}q+\sum_{n\ge1}b_nq^{n-1}:
\sum_{n\ge1}n|b_n|<\infty\right\}
$$

with norm |c|+Σ n|b_n|. For the original BBP source, c=15/64 and b_n=r(n)−c/n²=O(n⁻³). In this **stronger analytic norm**, finite 0-jets, the q=1 value, the renormalized q=1 slope, and interior evaluation at β=1/16 are all continuous additive functionals. Their exponentials are SUCC-compatible boundary/interior characters.

They are NOT continuous in the purely formal endpoint topologies alone. For any N, the polynomial (16^N/2)q^N vanishes to formal order N at q=0 but evaluates to **1/2 at β**, so its selected character is always −1. At the 1-endpoint, use (1/2)(16/15)^N(1−q)^N: it vanishes to formal order N at 1 yet also evaluates to 1/2 at β.

Thus extra analytic growth control is not optional.

## ZO-2. Authentic logarithmic q=1 germ, exact Euler–Mascheroni cancellation

Put s=1−q, c=15/64. The endpoint q=1 is finite, but the derivative diverges logarithmically:

$$
\boxed{
G(1-s)=R-cs\log(1/s)-d\,s+O(s^2\log(1/s)),
\qquad s\downarrow0.
}
$$

Its genuine total source mass is

$$
R=G(1)=\frac{\pi}{4}+\frac{5\sqrt2\pi}{16}
+\frac{5\log2}{8}+\frac{5\sqrt2\log(1+\sqrt2)}8.
$$

The exact finite renormalized slope is

$$
\boxed{
d=\frac{15}{64}+\frac{19\log2}{32}
-\frac{(5+9\sqrt2)\pi}{128}
-\frac{9\sqrt2}{64}\log(1+\sqrt2)
=0.03554037004791627\ldots.
}
$$

**Derivation, not curve fitting:** let b_n=r(n)−c/n². Since Σ n|b_n|<∞,

$$
d=c(1-\zeta(2))+\sum_{n\ge1}(n-1)b_n
=c+\sum_{n\ge1}\left((n-1)r(n)-\frac cn\right).
$$

This follows from the classical Li₂ singular expansion at 1, including the O(s²log(1/s)) remainder.

Write r(n)=Σ_i A_i/(n−a_i) for

$$
(a_i)=(7/8,1/2,3/8,1/4),\quad
(A_i)=(1/2,-1/4,-1/8,-1/8).
$$

Then (n−1)r(n)=Σ_i C_i/(n−a_i) with

$$
(C_i)=(-1/16,1/8,5/64,3/32),\qquad \sum_i C_i=c.
$$

The digamma identity
Σ_{n≥1}(1/(n−a)−1/n)=−γ−ψ(1−a) gives

$$
\boxed{d=c-\sum_iC_i[\gamma+\psi(1-a_i)].}
$$

Gauss's rational digamma theorem reduces this to the displayed π/logarithm expression. All explicit Euler–Mascheroni constants **cancel** because ΣC_i=c. Gamma is involved in the harmonic coordinate conversion; gamma alone does NOT prove normality.

**Exact rational certificate.** Set D(n)=(2n−1)(4n−1)(8n−7)(8n−3). Direct polynomial algebra proves that for every n≥2,

$$
0<r(n)-c/n^2\le1/n^3.
$$

Indeed 64n²D(n)(r(n)−c/n²) equals
F(n)=9664n³−9656n²+3090n−315. With n=t+2:

$$
F(t+2)=9664t^3+48328t^2+80434t+44553,
$$

$$
64D(t+2)-(t+2)F(t+2)
=23104t^4+128952t^3+261694t^2+225811t+68142.
$$

Both are positive for t≥0. Consequently for N≥2 the rational approximation

$$
d_N=c+\sum_{n=1}^N\left[(n-1)r(n)-c/n\right]
$$

obeys the certified universal error

$$
\boxed{|d-d_N|\le(1+c)/N.}
$$

The q=1 germ is **not an ordinary Taylor series**, since its leading singular coefficient is c s log s. It belongs to an additive log-germ space A(s)+B(s)log s, with A/B analytic near s=0; under products allow polynomial powers of log s. Its first finite data are a₀=R, a₁=−d, b₁=c, hence characters can independently observe R, c and d without falsely declaring a finite ordinary derivative.

## ZO-3. Strong all-depth obstruction to finite endpoint-character normality proofs

For **arbitrary** integers K≥1 and J≥2, construct

$$
\boxed{
M_{K,J}(q)=1-\frac{16^{K+J}}{15^J}q^K(1-q)^J,
\qquad \widetilde G(q)=M_{K,J}(q)G(q).
}
$$

The rational polynomial multiplier satisfies

$$
M_{K,J}(1/16)=0,\qquad
M_{K,J}\equiv1\pmod{q^K},\qquad
M_{K,J}\equiv1\pmod{(q-1)^J}.
$$

Therefore the altered source has the same first K authentic q=0 coefficient observations and the same q=1 log-germ observations below order J, including G(1)=R and c when J≥2. Every altered coefficient remains rational with odd denominator. Its true zero-seeded recurrence is

$$
\widetilde U_0=0,\quad
\widetilde U_{n+1}=16\widetilde U_n+\widetilde r(n+1),
\quad \widetilde r(n)=[q^{n-1}]\widetilde G(q).
$$

But its selected real value is **zero**:

$$
\widetilde G(1/16)=0.
$$

Since \widetilde r(n)=O(n⁻²), the exact Green identity gives \widetilde U_n=−\widetilde T_n→0, and therefore for every fixed h≠0,

$$
\boxed{\lim_{N\to\infty}\frac1N\sum_{n=1}^Ne(h\widetilde U_n)=1.}
$$

This is an **explicit nonnormal changed-source countermodel**, NOT a counterexample to the *original fixed four-pole BBP source*.

More severely, after n>K+J the altered source is exactly a rational finite difference

$$
\widetilde r_\infty(x)
=r(x)-C\sum_{j=0}^J(-1)^j{J\choose j}r(x-K-j),
\quad C=\frac{16^{K+J}}{15^J}.
$$

It is **a 2-adic isometry** on Z₂. Proof: original r is a 2-adic isometry, all its shifted terms are 1-Lipschitz, and v₂(C)=4(K+J)≥4. Hence \widetilde r_\infty(x)=r(x)+16g(x) with g 1-Lipschitz; strong ultrametric dominance preserves the exact distance.

For every k≥1 and n≥k+K+J the actual rational zero-seeded mutant obeys

$$
\widetilde U_n\equiv
\sum_{j=0}^{k-1}16^j\widetilde r_\infty(n-j)
\pmod{16^k}.
$$

The right side is itself a 2-adic isometry in n. Consequently **every consecutive block of 16^k source times after the transient visits each state residue exactly once**, for every depth k. Yet the real phases converge to 1.

Further, \widetilde r(n)=r(n)+O(n^{-J-2}) and is eventually positive. No global early-time positivity claim is made.

**REFUTED:** fixed finite 0-jets + fixed finite logarithmic 1-jets + eventual complete 2-adic source-clock Haar + zero initial condition ⇒ selected real-circle normality.

The universal counterexample family proves that an all-level source-rigidity statement, not simply finite endpoints, is load-bearing.

## ZO-4. What remains genuinely open

The positive result is a compatible **analytic** character host spanning q=0, the logarithmic q=1 endpoint and the source-selected interior q=1/16. The negative result demonstrates exactly what such a host does NOT buy: it does not control signed real Weyl sums for the actual expanding BBP orbit.

A real π-normality advance must produce source-specific signed cancellation for

$$
\sum_{n=1}^Ne(hU_n)=o(N),\qquad h\in\mathbb Z\setminus\{0\},
$$

while rejecting every K/J source counterfeit above and the nonnormal 2-adic-isometric PR #320 controls. Preserving the authentic full four signed poles and the actual zero-selector is indispensable.

Potential next discriminators:
- Construct a source-specific all-level analytic/odd-prime carry observable which changes under the multiplier countermodels, and derive a new quantitative signed Weyl saving.
- Explore cyclotomic q=1 gluing (Habiro) only with its type restrictions: q is invertible in the Habiro ring but **not** in the q=0 formal ring, so no naive q-preserving ring map can identify them.
- Separate Gamma, Euler–Mascheroni and Oily–Macaroni grade normalization from invariant source-phase information; changing the finite logarithmic reference must not alter a claimed normality theorem.
- Test whether multi-prime / Mellin transfer operators provide a *verified* real cancellation mechanism beyond character reconstruction.

## Authority and reproducibility

**Paper-proved in this research round:** exact original Mellin kernel, Banach analytic bridge, formal character definitions, logarithmic 1-germ coefficient and d formula, exact rational slope budget, pure-formal discontinuity, all-K/J counterfeit with eventual all-level 2-adic residue Haar. **CLASSICAL provenance:** adic completion, Li₂ singularity, digamma/Gauss, Wiener algebra, Habiro completion. **OPEN:** π normality and any new authentic selected signed Weyl saving.

The accompanying full isolated standard-library implementation and tests were executed locally: 15 tests collected, **14 PASS, one native SUCC import SKIP**; a standalone exact rational probe checked 256 source Mellin identities, 25 endpoint counterfeit pairs, 294 isometry cases and 22 formal-evaluation witnesses. The depth-1/depth-2 complete 16/256 state clocks were verified. Independent 65-digit numeric integral tests corroborated G(1/16)=π and the germ slope. These finite checks are not universal proof certificates. Full native SUCC suite, provenance, CI and Lean have not been run in this research session.

Primary mathematical sources:
- Ideal-adic completions: https://encyclopediaofmath.org/wiki/Adic_topology
- Series completions: https://www.math.ucla.edu/~sharifi/notes/algnum-ch05.html
- Classical Gauss digamma theorem: https://mathworld.wolfram.com/GausssDigammaTheorem.html
- Li₂ singular expansions: https://rivoal.perso.math.cnrs.fr/articles/inversepolylog.pdf
- Habiro ring and q invertibility: https://link.springer.com/article/10.1007/s00029-024-00990-y

**No main merge, release, publication or source rewrite authorized.**
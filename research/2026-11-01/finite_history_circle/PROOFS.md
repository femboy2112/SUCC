# Constant-curvature → finite-source history → moving-scale BBP phase transport

**Research-only, 2026-11-01.** Exact underlying original signed four-pole forcing and selected `U0=0`. Parent SUCC Main XVIII and stacked research PR #447 supply the original BBP identity and recursive circle length law; PRs #440/#446/#445 supply the positive source, Wilson commutator, and exact phase-echo. **π base-16 normality and RH are OPEN.** Algebraic reconstructions here are paper proofs with independent finite exact programs, not a new Lean theorem or peer-reviewed finding.

## CH-01. Constant signed curvature is a complete *geometric* evolution rule with initial frame

For a unit-speed plane curve γ(s) with oriented Frenet tangent T(s), normal N(s), and constant signed extrinsic curvature κ≠0,

`T'=κN`, `N'=-κT`, `γ'=T`.

Thus `(T(s),N(s))` is the rotation by `κ(s−s0)` of its initial frame. Integration determines γ(s) uniquely from position, tangent, signed κ. It is a circle of radius `1/|κ|`. This is the classical fundamental theorem of plane curves, not a SUCC novel geometric proof, and has NO implication that a separate arithmetic driving term r(n) is known. Pure intrinsic curvature of the one-dimensional circle is zero; this is extrinsic signed curvature. Previous PR438's time-frequency line bundle has a separate two-form curvature.

The circle-recursive quotient Π_k from PR447 uses positive-root branch and upper orientation; it is an *inscribed-length* sequence satisfying `0<π−Π_k<8/(3·4^k)`. For original BBP the exact integer circle cocycle is `z_n=z_(n-1)^16 e(r(n))`. The ×16 constant derivative is universal; source rotations r(n), their order, and the literal seed are *extra data*.

## CH-02. Seven exact original-source observations determine all futures *in a restricted rational source family*

Define the declared class

`R_(2,4)={A(x)/D(x): deg A<=2, deg D<=4, D not zero at observed x}`, with D normalized monic for parameter recovery.

Authentic rational source (write capital A,D for integral polynomials):

`A(x)=120x²−89x+16`,
`D(x)=(2x−1)(4x−1)(8x−7)(8x−3)=512x⁴−1024x³+712x²−206x+21`,
`r(x)=A(x)/D(x)`.

Suppose f=A1/D1,g=A2/D2 are in R_(2,4), finite at seven distinct positive integer nodes x_j, and `f(x_j)=g(x_j)` for all seven. Then `A1D2−A2D1` is a polynomial of degree at most `2+4=6` vanishing at seven points; hence it vanishes identically. Therefore f=g as rational functions. No positivity or curvature assertion is used in this uniqueness argument.

**Constructive exact identification:** normalize `Dtilde=x⁴+b3x³+b2x²+b1x+b0` and `Atilde=a2x²+a1x+a0`, write each measured `r_j` as a linear equation

`a0+a1*x_j+a2*x_j² −r_j(b0+b1*x_j+b2*x_j²+b3*x_j³)=r_j*x_j⁴`.

The 7×7 rational system has the unique original solution

`(a0,a1,a2)=(1/32,−89/512,15/64)`,
`(b0,b1,b2,b3)=(21/512,−103/256,89/64,−2)`.

Uniqueness of representation at the original source follows from `gcd(A,D)=1` (their resultant is nonzero, `−7372800`) and the monic degree-four normalization. An independent fraction-free determinant/Cramer's-rule algorithm reconstructs the SAME source from arbitrary distinct seven-node samples including shifted windows 35..41. Seven distinct exact source values plus known model class and zero seed thus determine every r(n), and by the literal recurrence every future exact unwrapped U_n.

**No numerical stability claim**: identification from noisy or finite-precision data is a different inverse problem. We did not infer the rational `(2,4)` degree class from a circle.

## CH-03. Seven is SHARP in this class; a positive six-observation counterfeit

Define the integer polynomials

`P6(x)=2560x²+27261099545x−10222908432`,
`Q6(x)=9(12923803584x³−21109033272x²+10286815366x−1497394413)`.

Exact polynomial arithmetic proves

`P6(x)D(x)−A(x)Q6(x)=1310720 * product_(j=1)^6(x−j)`.

Let ε=10^(-8), and form the type-(2,4) rational source

`r_ε(x)=[A(x)+εP6(x)/1310720]/[D(x)+εQ6(x)/1310720]`.

For all six x=1,..,6, it has EXACTLY the same values as the authentic r, while for x=7 it differs by a strictly positive rational number:

`r_ε(7)-r(7)=104857600/12101122644582669027899751`.

The mutant is strictly positive for every REAL x≥1, not merely finite test samples. Indeed `A(x)>=31x²`, `D(x)>=15x⁴`, and

`|P6(x)/1310720|<30000x²`, `|Q6(x)/1310720|<320000x³`, for x≥1.

Thus the perturbed numerator is `>(31−0.0003)x²>0`, and the denominator is `>(15−0.0032)x⁴>0`. At infinity the source remains decaying as x^(-2). This explicitly refutes prediction from six samples **even with global positivity and the same coarse type (2,4)**. It does not preserve the exact original four pole positions, so is not a counterexample to a theorem with all four poles authenticated. The same six initial zero-seeded U_n and circle phases are identical; the seventh differs.

## CH-04. Circle-phase tomography: exact residues and irreversible branch labels

Let `z_n=e(U_n)`, with e(x)=exp(2πix). For every n≥1,

`z_n/z_(n-1)^16=e(r(n))`.

Because authentic `0<r(n)<1` for n≥2 (positive decreasing Hausdorff source and `r(2)=106/819<1`), the first eight complex circle observations z1..z8 uniquely determine the rational source values r2..r8 by choosing the unique representative in (0,1). Seven such samples recover the ENTIRE rational source using CH-02, even without unwrapping r1.

**Stronger with declared zero boundary and first-step branch:** if `z0=1`, `U0=0`, and source prior `3<r(1)<4` is authenticated, then z1 determines `r1=3+arg(z1)/(2π)` with the argument chosen in [0,2π); z2..z7 determine r2..r7. Therefore just z1..z7 determine all future. The (3,4) lift is an assumption; unit phases alone do not supply it, and the visible y0=e(U0) does not uniquely specify the real unwrapped U0 without the declared literal boundary.

For any known source and next circle output y, the previous seed solutions are

`x_j=(y-r(n)+j)/16 mod1`, `j=0,..,15`.

They are **exactly 16 distinct preimages**, so after N stages the same final output has 16^N distinct starting circle states. If each branch is assigned *uniform prior* the conditional branch information is `log2(16)=4` bits per predecessor step; this is an INFORMATION-THEORETIC model, not intrinsic entropy production or heat. For example all initial seeds `s=j/16` with j=0,..,15 give exactly the same positive-time circle observations for the original source: `16^n s` is an integer for n≥1. The initial label (or unwrapped path history) is not recoverable from all later phases alone.

The source-free expanding map and rotations have angular derivative 16. Neither this derivative, constant extrinsic circle curvature, nor Haar-invariance decides the statistical normality of the selected orbit.

## CH-05. Exact mixed geometric-length / source-Wilson future predictor

Inherited BBP identity, with original source and literal zero boundary:

`U_n=16^(n−1)π−T_n`,
`T_n=Σ_(m>=1)16^(-m)r(n+m)`.

Define `d_j=15(r(j)−r(j+1))` as the genuine adjacent ordered affine Wilson displacement (PR446). Source decay and finite summation by parts give the EXACT finite formula, for n≥0,J≥1,

`T_(n,J)=Σ_(m=1)^J16^(-m)r(n+m)`
`        = 1/225 Σ_(k=1)^J (1−16^(-k))d_(n+k)`
`          +(1−16^(-J))/15 * r(n+J+1)`.

The **last boundary term is required**. Drop it and the finite-history predictor is false. The strictly positive unobserved tail has the certified all-horizon bound

`0<T_n−T_(n,J)<16^(-J)/[64(n+J)^2]`.

Let Π_k be the independent pure circle chord quotient from PR447, and choose the finite source-faithful predictor

`U~_(n;N,L,J)=16^(n−1)*Π_(2N+L)−T_(n,J)`, `1<=n<=N`.

This is literally (finite geometric length) minus (finite source-Wilson future curvature with boundary). None of its inputs require any digits of π: the circle recursion uses positive square roots of rationals, and all future source values are computable exactly from the seven-sample reconstruction in CH-02. The identity between infinite geometric π and the BBP series is an IMPORTED classical BBP theorem, not an independent new implication of constant circle curvature.

## CH-06. NEW arbitrarily precise whole-horizon signed Weyl and quantum echo transport

For each N≥1 and any desired INTEGER power p≥1, let L be the least nonnegative integer with `4^L>=N^p`, and J the least positive integer with `16^J>=N^p`. Then k=2N+L circle bisections, J=O(p logN) future-source steps.

Original known geometric error: `0<π−Π_k<8/(3*4^k)`. Multiplying by 16^(n−1), summing n=1..N and paying the exact source tail yields

`Σ_(n=1)^N |U_n−U~_n|`
` < (8/(45*4^L))(1−16^(−N)) + 16^(−J)/(64J)`.

The last term follows from `Σ_(n>=1)(n+J)^(-2)<1/J`. Since `|e(hx)−e(hy)|<=2π|h||x−y|` and `2π<44/7`, **for all N≥1, integer nonzero h, p≥1**:

`|Σ_(n<=N)e(hU_n)−Σ_(n<=N)e(hU~_n)|`
`< (44/7)|h| * [(8/(45*4^L))(1−16^(−N))+16^(−J)/(64J)]`
`<= (44/7)|h| * (8/45+1/64) * N^(−p)`.

**THIS CONTROLS THE UNNORMALIZED FULL N-TERM WEYL SUM**, not merely its mean. It is deterministic TRANSPORT, NOT a newly proved bound on the size of either sum.

From PR445 the exact original echo is `E_(n,h)=e(hU_n)I`. Define controlled diagonal echo `V_N=⊕_(n=1)^N E_(n,h)`, and its fully finite predicted echo `V~_N=⊕ e(hU~_n)I`. Their operator-norm error is bounded by the maximum scalar phase error:

`||V_N−V~_N|| <= max_n |e(hU_n)−e(hU~_n)|`
` < (44/7)|h| [1/(6*4^L)+16^(−J)/(64J²)]`
` <= (44/7)|h| (1/6+1/64) N^(−p)`.

So the **entire** N-branch phase-echo unitary admits arbitrary polynomial-rate approximation from k=2N+O(p logN) circle refinements, the finite Wilson curvature and exact seven-sample source model. It remains a mathematical coherent-control model; no practical gate-count/energy bound or quantum speedup is claimed.

For any fixed p, the signed Fejér-lag bilinear correlations also transport with a paid O_h(N^-p) absolute full-sum error (by the phase-sum/Gram identities and |z|<=1), but NO source-selected cancellation is derived. In particular the coherent altered-seed q=1/5 cannot be assigned this circle-linked zero-seed error budget; its state includes `16^n(q−π/16)`.

## CH-07. Hostile sources, orientation and target firewall

1. **Six-observation counterfeit** (CH-03): same source class, globally positive, same first six states and phases, different seventh and future. Exact polynomial receipt provided. Thus `six past => unique future` is REFUTED under this class.
2. **No rational class assumption:** prior PR446 supplies strictly positive Hausdorff moment sources matching arbitrarily many finite observations but with different completed orbits. Universal `finite past => unique future` is REFUTED.
3. **Unobserved backward branches:** 16^N seeds can match a final phase; even infinite positive-time phases cannot distinguish seed shifts j/16. The literal zero anchor is extra boundary data.
4. **Unselected source/circle correspondence:** geometric circle π and its uniform curvature apply to any source, including forcing zero or changed-seed coherent q=1/5. No normality follows from circle geometry or deterministic source identification.
5. **Authentic four poles are only authenticated within a model prior or from the already-known full expression**. Six mutant adds new rational poles. Exact finite rational source recovery is NOT proof that the four poles arise uniquely from universal geometry.
6. **Phase versus statistics:** the finite projector reproduces the exact selected signed phases with arbitrarily small total error but does not establish `S_N(h)=o(N)`. Source-selected asymptotic phase correlation is a separate open gate.

**Verdict:** DISCLOSED within the stated classical/rational source/geometry domain: seven-source identification, phase tomography with branch, inverse 16-fold history, all-horizon finite geometric-Wilson projector and arbitrarily small absolute full-echo error. REFUTED: source-free reconstruction or constant curvature alone implies a selected π normality proof. OPEN: a source-derived signed asymptotic estimate or new source-to-circle law not using the inherited BBP π identity.

## Classical source attribution

- Plane Frenet curvature reconstruction: M. Ghomi, Georgia Tech, *Fundamental theorem for planar curves*, https://ghomi.math.gatech.edu/Classes/Math426/LectureNotes3.pdf .
- Rational function degree constraints and extrapolation are standard interpolation; our seven-node argument is self-contained. NIST, *Rational Function Models*, https://www.itl.nist.gov/div898/handbook/pmd/section8/pmd812b.htm .
- Circle expanding map entropy/covariance: A. Erchenko, *Flexibility of Lyapunov exponents for expanding circle maps*, https://www.aimsciences.org/article/doi/10.3934/dcds.2019098 . Our branch-count argument is elementary and does not import entropy-rigidity claims.
- Source and previous original SUCC work: Main XVIII, PR #437 (four-pole source and positive Beta mutants), #438 (Zak band), #440 (finite unit atoms), #442 (four-punctured sphere), #445 (phase echo), #446 (ordered Wilson curvature), #447 (circle/diameter recursive quotient and bracket).

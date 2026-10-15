# HILBERT–WEIL ATLAS: finite-to-complete carrier with authentic signed Suzuki source

**Date:** 2026-10-14 (America/New_York). **Parent source:** `femboy2112/SUCC` `main` pinned at `03db44203147a7b28d445bb9f970fa71360e78c4` (Phoenix II, PRs #57–99 integrated). **Source-authenticated module:** `observational_succ/source_weil_hierarchy.py`, exact Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. **Mathematical provenance:** Suzuki *Weil's quadratic form via the screw function* arXiv:2606.09096v3 (2026); Suzuki–Yoshida Weil criterion; Connes–Consani *Weil positivity and Trace formula, the archimedean place* arXiv:2006.13771; Connes–Consani–Marcolli *The Weil proof and the geometry of the adeles class space* arXiv:math/0703392; Hilbert space-filling curve (classical); compact self-adjoint spectral theory, Haar/Martingale convergence and operator Schur complements (classical).

**Scope:** The source is the **original** rational/integer SUCC+FUCC, original prime powers with von Mangoldt weights, *one* real Gamma and original contact/pole terms. The 2D Hilbert curve is a new **observation order and dyadic finite-to-continuum mathematical instrument**, not another p-adic place, a physical infinity, an adelic space, a new Archimedean completion, or a source of the Weil sign. **RH PROVED: NO.** All exact carrier constructions and operator inequalities below are classical consequences under their explicit hypotheses; independent scholarly novelty remains unreviewed.

## 0. Audit and ranked next-stage plan

Phoenix II merged PRs #57–99 into `main` `03db4420`: full suite 3350 Python tests green, main GitHub Actions 3.10/3.13 succeeded. The signed finite-source hierarchy (#85), actual Gamma positive-tail result (#85), full 30-moment-null positivity (#86), canonical 30-low/15+15 Schur reduction (#96), and exact zero-shift range condition (#99) are integrated. The unproved bridge is **the actual low/high cross-resolvent sign at λ↓0**, and its extension to all a.

The two newly created but not yet committed Hilbert research branches `research/hilbert-carrier-completion-2026-10-14` and `research/hilbert-curve-cube-zeno-certificates-2026-10-14` both referenced the identical fresh main head during intake. This branch is separate and source-pinned; do not overwrite them or main.

**Priority / acceptance gates:**

1. **H1 (this round)**: implement the dyadic Hilbert atlas with exact source-aware area, finite-prefix, refinement and path checks; prove measure/Hilbert-space limit with quantified errors. Require a negative-source control that falsifies sign from finite positive cells.
2. **H2 (this round)**: plug the Hilbert pair-cell order into Suzuki's original signed compact screw kernel, rather than replacing the original source. Preserve **all signed prime/Gamma/contact/pole terms** and a rigorous all-state operator norm error via the immutable source module.
3. **H3 (this round)**: combine the genuine infinite-dimensional 30-moment positive complement with dyadic step refinement to produce an unconditional **shifted** cross-resolvent upper bound for every λ>0 on a=1/2; quantify its λ-cost and explicitly refuse the unshifted inference.
4. **H4 (next)**: generate *tight*, source-true low/cross Legendre interaction entries without the uniform cell Lipschitz wall; exploit parity, first-prime wavefront tiles and the positive Gamma tail one-sided. Test against fake-composite6, wrong half-density, non-Euler L and missing pole.
5. **H5 (next)**: a Connes/Suzuki comparison capsule with exact trace/test-function maps, self-dual Haar, conductor and true Euler, and a source-respecting interpolation from the compact signed operator to the candidate cohomological/adelic trace pairing. Unless the completed Weil form is **identified on its full domain**, no unrelated positive graph/Hilbert covariance may replace it.
6. **H6 (moonshot)**: prove either all-a Suzuki/Weil positivity from a source-derived shorted matrix with zero-shift range control, or find a source-authentic strict negative witness. All finite scans, Hilbert ordering and isolated critical-line zeros are insufficient alone.

## HW-1 — exact Hilbert refinement, genuine mathematical continuum

At depth n≥0, `H_n` enumerates every grid tile of side `2^-n` in the unit square, visiting each of the `4^n` tiles exactly once and successively crossing a shared side. Parent tile of child visit indices `4j,4j+1,4j+2,4j+3` is the tile indexed by `j` at depth n−1. This uses the classical Hilbert orientation specified in the module; the finite claim is proved by induction using quarter rotations and reversals, and independently exhaustively checked through depth 6.

Put `h_n(t)` equal to the **tile center** whose Hilbert index contains `t∈[j/4^n,(j+1)/4^n)`. The parent property nests all later containing closed tiles. Their diameters are `sqrt(2)2^-n`, hence there is a unique pointwise limit `h(t)`. Adjacent indices have adjacent cells. If `|t-s|≤4^-n`, both limiting points are in the same or adjacent squares, giving a distance at most `sqrt(5)2^-n`. Choose n with `4^-(n+1)<|t-s|≤4^-n` to obtain the classical Hölder-1/2 estimate `|h(t)-h(s)|≤2sqrt(5)|t-s|^1/2` (and continuity at interval endpoints). This is a continuous surjection onto the square; all dyadic tile interiors have preimage a time interval of length `4^-n` up to null boundary sets.

Consequently `h_*Leb_[0,1]=Leb_[0,1]^2`: for each dyadic square of area `4^-n`, the preimage has time mass exactly `4^-n`; extend from dyadic rectangles by uniqueness of Borel measures. Thus pullback `Uf=f∘h` gives an **isometric embedding** `L²(square)→L²(interval)`. Do **not** assert a canonical arithmetic-place isomorphism, a unitary Fourier rotation, an actualized infinite SUCC operation, or a proof that f is a physical report.

Let `F_n` be the sigma field on `[0,1]` generated by its `4^n` Hilbert visit intervals. On a true Lipschitz `f` on the square, the conditional average of `Uf` on any block differs from `Uf` pointwise by at most `sqrt(2)L_f 2^-n`, so `||Uf−E[Uf|F_n]||₂≤sqrt(2)L_f2^-n`. For all `f∈L²` without regularity, standard martingale/dense-function theory still gives L² convergence but **no universal numeric rate**. This is a legitimate source-independent `finite observer→completed mathematical observable` theorem.

## HW-2 — exact one-dimensional traversal of a **signed** double integral

For a coordinatewise-Lipschitz `f:[0,1]^2→R`, with independently established `|f(x,y)-f(x',y')|≤L_x|x-x'|+L_y|y-y'|`, the Hilbert-midpoint quadrature

`Q_n(f)=4^-n Σ_(j=0)^(4^n-1) f((i_j+1/2)2^-n,(k_j+1/2)2^-n)`

satisfies **for every n** `|∫square f − Q_n(f)|≤(L_x+L_y)2^(-n-1)` by integrating the midpoint inequality cell by cell. Neither positivity nor signed cancellations are assumed. The order is useful for nested patch traversal and streaming source receipts; the numerical value equals ordinary full-grid midpoint quadrature. A permutation of *pair-cell read order* cannot alter the sign/spectrum of the source operator. Any claim of improved spectral sign solely from Hilbert ordering is REFUTED.

When `f(x,y)=g_a(2a(x-y))u(x)conj(u(y))`, this quadrature is valid only if an appropriate pointwise regularity budget is proved for u (e.g. Lipschitz). For arbitrary L² test states, one must instead use Suzuki's **operator-norm** source error. Do not substitute a pointwise midpoint estimate for a signed all-test Weil form bound.

## HW-3 — authentic source/Suzuki interface (new-to-SUCC implementation)

On `H=L²_0(-a,a)`, let `G_a=P_0 (g_a*·)P_0` be the original compact signed Suzuki operator, `g_a` exactly Suzuki's original prime/Gamma/contact/pole screw function. Let `E_n` be orthogonal projection onto mean-zero dyadic step functions on `N=2^n` subintervals; `E_n→I` strongly. The genuine pinned source module supplies `G_(a,J,N)` whose range lies in `E_n H` and a **certified norm error**. For every `u∈H`, `|<u,(G-G_JN)u>|≤ε_JN||u||²`.

The inherited authentic Gamma complement is positive. Distinguish the two source errors:

`T_J=||G−G_J|| ≤ 2/(4J+1)^2 + 16/(4J+1)^3`, `T_J≽0` (positive OU tail),
`E_sp=||G_J−G_JN|| ≤ 2a[(2a/N) L_J(a)+η_JN]` (true spatial/source interval budget).

Therefore `epsilon_JN=T_J+E_sp` bounds `||G-G_JN||`. The order over 2D pairs is chosen by the finite Hilbert curve, but **every** signed pair contributes exactly once. 

The code's source-only observer requires the immutable module blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, verifies its `stage` fields, rejects floats, requires mean-zero cell vectors, and reports **only** a single-state signed Rayleigh interval. Even when its lower endpoint is positive, it refuses to infer `G≥0`.

For the complete signed source, Hilbert enumerating `G_JN` gives **no better fundamental error constant** than the inherited grid certificate. It exposes a useful refined geometry and adaptive order, not a new free proof of RH.

## HW-4 — source prime-wavefront threshold geometry has only O(N) ambiguous cells

For an authenticated prime power `q=p^k`, the signed Suzuki hinge contribution to `g_a` is `c_q (|x−y|−log q)_+`, with `c_q=log p/sqrt q`. For a dyadic tile `Q_ij` in the *pair* square `[-a,a]^2`, exact rational interval geometry gives the range of `|x−y|`. Using a certified interval `[ℓ_-,ℓ_+]` for `log q`, classify tiles as inactive (certainly below threshold), active (certainly above), or threshold-ambiguous.

If `ℓ_+−ℓ_-<h/2` for cell width `h=2a/N`, in each fixed x column the uncertain y lies in one of two strips around `y=x±ℓ`, each spanning at most `h+(ℓ_+−ℓ_-)<1.5h` vertically. Each hits at most four closed grid rows, so the number of ambiguous cells is at most `8N`, **not** `N²`. This is a classical grid-intersection fact now applied to the *actual* source hinge; it does **not** apply to the smooth Gamma/contact/pole contributions, which remain global. For `a=1/2`, the exact true-prime-2 counts at N=4,8,16,32,64 are 6,10,18,38,78; the parent source log-2 phase is certified rationally. Fake composite `6` is source-rejected. Genuine `4=2²` is a real prime power but remains outside the first window (no activation).

The dyadic Hilbert observer can therefore **concentrate adaptive source precision** on true prime threshold cells. This is a potential computational gain at high resolution; a global sum of all smooth kernel interactions remains necessary, so an O(N) *total* Weil operator algorithm has NOT been established.

## HW-5 — original positive high space + Hilbert refinement: a shifted Schur gate

**Source premise (integrated AMW-06B/SM-01):** at `a=1/2` the authentic signed G is **strictly positive relative to** the inverse Neumann K on the 30-moment-null high space `H_30`:

`<Gu,u> ≥ κ<Ku,u>`, `κ=369/10000`, `u∈H_30`.

Let `L_30` be the span of the 30 mean-zero Legendre functions and define `L_n=closure(L_30+E_n H)` (finite-dimensional; exact orthogonal projection Π_n). Then `H_n=L_n^⊥⊂H_30`; hence the high operator `D_n=Q_nGQ_n≥0`, `Q_n=I−Π_n`. In contrast, **plain dyadic E_n^⊥ is not known positive**; the 30-mode augmentation is essential.

Because `G_JN` is supported entirely on the dyadic step subspace `E_nH`, `G_JN Q_n=0`. Thus the true cross block obeys:

`||B_n||=||Π_n GQ_n|| ≤ ||(G−G_JN)Q_n|| ≤ ε_JN`.

For every λ>0, the true high resolvent `(D_n+λI)^−1` exists and is bounded above by `1/λ`. Therefore the complete **source-true shifted cross-penalty** satisfies the operator inequality

`0≤B_n(D_n+λI)^−1B_n* ≤ (ε_JN²/λ) I_(L_n)`.

**THIS is the proof-bearing payoff:** a source-indexed finite-to-complete coupling certificate valid for *all states* in the declared low space, not just a positive finite matrix. It requires the authentic Gamma/prime/pole operator-norm envelope and the independently proved 30-moment high sign. For any fixed λ>0, increasing J, N and arithmetic precision can drive the right-hand side to zero, but this says **nothing** about λ=0 without a new uniform relative inverse/cross theorem. Source implementation uses `T_J+E_sp`, the stronger one-sided authentic Gamma tail, and exposes its exact rational squared/λ cost.

This method trades a fixed 30-dimensional low Schur for a growing `30+(N−1)` dimensional low sector. It is **not** a certified positivity result for that low sector and does not imply convergence of the unshifted 30×30 Feshbach matrix. For large N, proving low-block sign, controlling interval cancellation and the λ→0 inverse remain decisive. Prior #96 direct Legendre integration is probably the preferable path for a truly small low matrix.

## HW-6 — no free prime-causal refinement: a rigid commutator obstruction

The natural dyadic parent of a Hilbert visit index at level n+1 is `floor(j/4)`. Multiplying that **index** by p modulo `4^(n+1)` fails to descend to multiplication on parent indices: at n+1=2, `j=2,p=3`, parent of child `(3·2 mod16)=6` is 1, while multiplying parent `floor(2/4)=0` yields 0. Although p=3 is a *unit* modulo 16, its transport is NOT Hilbert-refinement-natural. p=2 is even noninjective, image size 8 rather than 16. Multiplying a Hilbert visit index is **not** the original arithmetic `V_p` acting on the integer carrier; this negative control prevents an invented prime coupling.

**Strong vs norm prime transport.** Let `P_n` be the dyadic spatial projection on I=(-1/2,1/2), `T_ℓ f(x)=f(x+ℓ)` cut off on I with the **genuine** length `ℓ=log2`. Since `ℓ/|I|=log2` is not a dyadic rational, its binary expansion is not eventually constant. Hence for infinitely many n the fractional part `θ_n={2^n log2}` lies in `[1/4,3/4]` (every non-eventually constant binary sequence has infinitely many adjacent unequal bits). For each such n choose two separated *interior-overlap* dyadic cells and the normalized mean-zero difference of their indicators; both cells remain inside the original interval under the shift. Projection of each translated indicator onto step cells loses squared norm `2 θ_n(1−θ_n)≥3/8`, and the disjoint pair witnesses the same loss. Therefore

`limsup_(n→∞) ||[P_n,T_ℓ]|| ≥ sqrt(3/8)`.

This is a genuine operator-norm obstruction on the original log-prime shift, while `P_n→I` strongly implies `P_nT_ℓ−T_ℓP_n→0` strongly for each fixed L² vector (with appropriate mean-zero compression). The obstruction is not physical superluminal motion or a proof that prime arithmetic resists all representations; it is a strict consequence of **this declared dyadic observer architecture**.

**Key contrast:** the *complete Suzuki screw kernel* G is compact, and `||G−E_nGE_n||→0`. Since `E_nGE_n` commutes with E_n, the offdiagonal block identity yields `||[E_n,G]||≤||G−E_nGE_n||→0`. For any authenticated finite source approximation `G_JN`, it is bounded by `ε_JN`. Thus **analytic smoothing** produces an operator-norm-compatible Hilbert observation even while the bare arithmetic shift does not. That is a real law connecting arithmetic and analytic carriers without conflating them.

## HW-7 — no-free-Weil-sign theorem in exactly the same pair geometry

For any fixed level n let `N=2^n`, `L=2a`. Consider the **source-independent** smooth even difference kernel

`k_n(x−y)=−(2/L) cos(2π N(x−y)/L)` on I².

The corresponding compact self-adjoint operator has eigenvalues -1 on the normalized `cos(2πN(x+a)/L)` and `sin(2πN(x+a)/L)` vectors, and zero on their orthogonal complement. Both vectors have mean zero. But their integral over *each level-n dyadic interval* is zero (one complete oscillatory period per interval), so **the entire level-n step compression of this negative operator is identically zero**, even though it is an even smooth translation-invariant kernel. The test module supplies a fully rational discrete alternating-Toeplitz counterpart on level-(n+1) cells with eigenvalue -1 and zero coarser compression.

This refutes any inference from finite Hilbert-cell zero/positive matrices to universal signed positivity. The constructed `k_n` is **not the authentic prime/Gamma Suzuki source** and therefore is not an RH counterexample. Its high frequency also violates any fixed uniform kernel modulus as n grows, showing precisely why a *source-derived* regularity/error bound is indispensable.

## HW-8 — Connes comparison: what the Hilbert atlas can and cannot transport

Connes's adele-class trace formula and the Connes–Consani/Marcolli Weil-positivity pairing are based on multiplicative scaling, Fourier/Haar normalization, and the authentic global arithmetic source. Connes–Consani's 2020 archimedean analysis uses compressed scaling operators, Sonin spaces and prolate spheroidal/Toeplitz control. Suzuki's 2026 finite-interval screw operator is a different but source-related realization of the completed Weil form. These are substantial classical programs; their global RH-strength positivity remains unproved.

A Hilbert space-filling traversal creates a **faithful integration and approximation order on a 2D pair kernel** when the original measure and source are preserved. It does not establish an equivalence between adelic test-function categories and dyadic cells; no self-dual Haar, idele class action, Mellin/trace functionals or representation of the original signed Weil distribution is produced merely by a Peano/Hilbert path. For a Connes-flavored future arrow we need typed original source, exact character and conductor, trace/Fourier identity, correct test domain, and a source-identified sign-bearing map. A positive Gram of the Hilbert cell adjacency graph is a **wrong positive object** unless shown to match that pairing.

A practical direction is to use Hilbert-prefix ordering **only as storage and adaptive quadrature** for Suzuki's genuine 2D continuous signed kernel, while retaining Legendre/parity and Toeplitz structures for spectral algebra. The Hilbert permutation itself can destroy obvious Toeplitz banding, so do not use its geometry as a substitute for the true operator basis.

## Handoff / outcome table

| Object | Mathematical result | Research status |
|---|---|---|
| Hilbert finite path / dyadic stage / measure limit | Exact path, law, Hölder/martingale, area error | CLASSICAL + PROVED LOCAL tests |
| First genuine prime-2 hinge | Source-authenticated wavefront tags, O(N) ambiguous band | PROVED LOCAL (source test budget) |
| Source Hilbert operator readout | **Original** signed full Suzuki finite matrix, source-verified norm error | PROVED LOCAL, integrated original-source CI needed |
| Dyadic+moment low/high | Genuine first-window high D≥κK; **shifted** cross penalty ≤ε²/λ | PROVED CONDITIONAL on established source theorems; no low sign |
| Prime shift/Hilbert non-equivariance | Exact noncommuting prefix and fixed-log-prime norm commutator | CLASSICAL / PROVED LOCAL |
| Hidden negative smooth kernel | Every finite Hilbert observer can miss a negative direction | PROVED LOCAL countermodel, NOT original source |
| Connes adelic→Suzuki full signed functor | Correct test/Haar/trace/positive correspondence | UNVERIFIED, central next theorem |
| Unshifted λ=0 & all radii | Source-derived true Weil positivity or real counterexample | RH-EQUIVALENT / OPEN |

**Reproduce:** `python -m unittest discover -s tests -p 'test_hilbert_weil_atlas.py' -v`, `python scripts/hilbert_weil_atlas_probe.py --verify research/2026-10-14/HILBERT_WEIL_ATLAS_RECEIPT.json`, and the dedicated Python 3.10/3.13 workflow; original-source adapter tests run only in the complete actual repository with exact pinned source code. Entire-workflow and other Lean packages are separate checks. All numerical outputs are exact rational calculations or explicitly labeled illustrative source stages; no nontrivial zeta zeros are inputs. Independent scholarly priority unverified; **RH PROVED: NO**.

## HW-9b — naive finite trace does not produce Connes's genuine prime distribution

For the true prime power n=2 and its source log-translation ℓ=log2, let `P_N` be the usual N-step spatial projection on `I=(-1/2,1/2)`. In the normalized cell basis, the diagonal matrix coefficient of the compressed translation `P_N T_ℓ P_N` is `max(0,(h−ℓ)/h)`, where h=1/N: the overlap of a cell with itself shifted by ℓ, divided by h. For `N≥2`, `ℓ>h`, so **every diagonal entry is zero**, and `Tr(P_N T_ℓ P_N)=0`; nevertheless `ℓ<1`, so the translation itself has a nonzero offdiagonal action. It contributes the genuine prime-2 term to the original Weil form for test states supported on the overlap strips.

The finite Hilbert order is just a permutation of these kernel-pair cells, so it cannot repair the trace blindness. Connes's periodic-orbit/adele-class trace, and the distinct Sonin compressed scaling trace, require a different trace/cyclic/cohomological test functional, not the naive finite `Tr(P_NT_ℓP_N)`. This is a concrete **no-free-Connes-trace result** from an authentic arithmetic phase, not a refutation of Connes's theorem or of trace formulas.

## HW-10 — a genuine improvement: the unshifted Suzuki **range condition** follows from source regularity and the 30-moment high theorem

**Theorem HW-10 (PROVED CONDITIONAL ON THE ALREADY VERIFIED AUTHENTIC AMW-06B THEOREM).** On `I=(-1/2,1/2)` let `H=L²_0(I)`, `G` be Suzuki's **actual** original signed compact screw-kernel operator, `K=(-Δ_N)^−1` the inverse-Neumann positive operator on mean-zero H, `P` the orthogonal projection onto 30 **orthonormal** nonconstant Legendre polynomials, and `Q=I−P`. Set `A=PGP`, `B=PGQ`, `D=QGQ`. The source-authentic high theorem establishes `D≥κ QKQ`, `κ=369/10000`. Then:

1. `G:H→H¹(I)∩H` is bounded, with rigorous elementary source bounds `||g'||_(L¹(-1,1))<24`, `sup_(|t|≤1)|g(t)|<12`, hence `||G||_(L²→L²)<12` and `||(Gx)'||₂<24||x||₂`.
2. The entire 30-dimensional cross image `B*P H` is contained in `H¹(I)∩QH`, which embeds into the range of `D^(1/2)`; **the original zero-shift Douglas/range gate is automatically satisfied**.
3. The unshifted finite quadratic matrix `R_0 = lim_(λ↓0) B(D+λI)^−1 B*` exists entrywise and in norm (low dimension 30), with the **fully source-derived conservative bound**

   `0≤R_0≤[(10000/369)·11556²] I_(P H)`.                          (HW10)

4. The exact remaining sign question becomes `A−R_0≥0` on the 30-dimensional low space; both matrices are well-defined but **this sign is not yet proved**. RH remains open even if this fixed `a=1/2` sign is eventually certified, since every interval radius must also be covered.

**Proof of (1), all source terms retained.** In terms of `t=|x-y|≤1`, the original even screw source on `t≥0` is

`g(t)=−8(cosh(t/2)−1)+(C/2)t−Σ_(j≥0) (1−e^(−α_j t))/α_j² + c_2(t−log2)_+`,

where `α_j=2j+1/2`, `C=γ+π/2+3log2+logπ`, and `c_2=log2/sqrt2`. **No other prime power is active on |t|≤1.** The sum converges uniformly by `Σ1/α_j²<∞`, and its derivative series converges in L¹(0,1) because, by Tonelli,

`Σ_j ∫_0^1 e^(−α_jt)/α_j dt=Σ_j(1−e^(−α_j))/α_j²≤Σ_j4/(4j+1)²≤5`.

The last bound follows from the decreasing integral test `4[1+∫_0^∞(4x+1)^−2dx]=5`. The remaining derivative contributions satisfy

`∫_0^1 4sinh(t/2)dt=8(cosh(1/2)−1)<2`, `C/2<4`, and `∫_0^1 c_2 1_(t>log2)dt<1`.

Here `cosh(1/2)<5/4` follows by `(2j)!≥2^j`; `C<8` follows from elementary `γ<1, π<4, log2<1, logπ<2`. Summing gives `∫_0^1|g'(t)|dt<12`, hence by evenness `||g'||_(L¹(-1,1))<24`. Since `g(0)=0`, `|g(t)|<12` throughout the support difference window. Young's convolution bound, followed by orthogonal projection to meanzero, establishes (1). The fact `g'` behaves logarithmically at t=0 does NOT invalidate its W^{1,1} regularity; it only rules out an unjustified uniform pointwise-Lipschitz claim for the infinite Gamma source.

**Proof of (2), including the projection cost.** The orthonormal low Legendre basis on I is `e_j(x)=sqrt(2j+1)P_j(2x)`, j=1,...,30. The classical exact Legendre identity `∫_(-1)^1 (P_j')²dx=j(j+1)` gives

`Σ_(j=1)^30 ||e_j'||₂² = Σ_(j=1)^30 2(2j+1)j(j+1)=922560<961²`.

For every H¹ function f, the derivative of its finite L² Legendre projection satisfies `||(Pf)'||₂≤961||f||₂`. With `w=B*x=QGx`, x∈PH,

`||w'||₂≤||(Gx)'||₂+||(PGx)'||₂<(24+961·12)||x||₂=11556||x||₂`.

Since `w∈H¹(I)∩H`, the Neumann spectral theorem gives `w∈Ran(K^(1/2))` and `||K^(-1/2)w||₂=||w'||₂`. For every y∈QH,

`|<w,y>|=|<K^(-1/2)w,K^(1/2)y>|≤||w'||₂ <Ky,y>^(1/2)≤κ^(-1/2)||w'||₂ <Dy,y>^(1/2)`.

By the Riesz representation theorem on `Ran(D^(1/2))` (or the classical Douglas factorization lemma), this proves `w∈Ran(D^(1/2))` and `||D^(-1/2)w||₂≤κ^(-1/2)||w'||₂`. The spectral theorem then implies for every λ>0

`<w,(D+λI)^(-1)w>≤||D^(-1/2)w||²≤(10000/369)11556²||x||²`.

Taking λ↓0 gives the finite positive semidefinite matrix `R_0` with this bound, and the shorted-operator criterion gives the equivalence `G≥0 ⇔ A−R_0≥0`. The proof never inverts compact D as a **bounded** operator, never omits the original negative pole/contact/prime contributions, and never reads any ζ zero. QED.

**Verdict:** This pays one genuinely consequential mathematical debt from the integrated ST-5/Feshbach frontier: *existence* and an explicit if crude source-certified uniform bound for the unshifted cross-resolvent at `a=1/2`. The subsequent **signed 30×30 low matrix** remains unknown, and the elementary `11556` bound is too conservative to force that sign. This is not a general all-a positivity theorem, Hilbert-space miracle, proof of RH or new result in abstract block-operator theory. The source-specific application is new to SUCC; independent scholarly novelty is not established.

## HW-11 — quantified diagonal finite-to-global *shifted* resource schedule

At `a=1/2`, suppose the original source interval evaluator is allowed arbitrarily high justified rational precision, with center-kernel rounding radius `η_{J,N}≤N^−2` (this is an *engineering hypothesis* satisfied by sufficiently accurate rational evaluation, not a claim that the current finite software supports unbounded N). Set for integer n≥1

`J=N=2^n`, `λ=1/N`, `h=1/N`.

The inherited original source Lipschitz envelope for truncated g_J is `L_J=9+2Σ_(j<J)(4j+1)^−1`. Elementary harmonic estimates give `L_J≤11+(1+log J)/2<(23+n)/2` since `log2<1`. The positive Gamma tail satisfies `τ_J^+≤1/(8J²)+1/(4J³)`. Thus the full original source-norm error obeys the purely rational explicit envelope

`ε_(J,N)≤ ([(23+n)/2]+2/N)/N`.

Using the authentic high-space sign on `H_n=(L_30+E_nH)^⊥`, the true shifted coupling penalty is at most

`ε_(J,N)²/λ≤(1/N)([(23+n)/2]+2/N)² → 0`.               (HW11)

**This is a constructive cofinal proof shape** for the *shifted cross term*: choose both actual dyadic observer resolution and genuine Gamma-source truncation, with separately paid rational rounding precision. It does NOT prove that the growing low matrix has nonnegative sign or the λ=0 30-moment shorted matrix. It does not provide a finite terminating observer or a current executable 2^n×2^n original stage for arbitrary n. The Python method returns exact rational budgets with `software_supports_this_level` explicitly false beyond the inherited stage limits. The existence of this schedule and HW-10's uniform resolvent finiteness are complementary facts: the former is constructive shifted error; the latter establishes the actual unshifted range on fixed 30 low modes.

## HW-12 — the next proof-bearing Moonshot, now reduced further

**At a=1/2, range is no longer the missing theorem.** With the genuine original positive high sector and the source-regularity argument, define the canonical 30×30 shorted matrix

`S_0=A−R_0`, `R_0(i,j)=<D^(-1/2)QG e_i,D^(-1/2)QG e_j>`.

The remaining finite-dimensional *sign* problem is to source-certify this R_0 sharply enough to compare with the already source-derived Legendre low A; the brute upper bound `~3.6×10^9` will not be sign-decisive. An optimal next analytic strategy is to construct **genuine high-compression energy bases for K** and a source-correct variational upper bound for the shorting matrix, using the actual g' and original source cancellation instead of separate worst-case norms. This must include both odd and even parity 15×15 blocks, and never replace D by K as an equality. Source-positive Gamma omitted modes should be handled by Loewner shorting, not symmetric error taxes.

The most promising Connes comparison is **not** Hilbert-grid adjacency positivity: identify a genuine scale-action trace or Sonin/prolate Toeplitz projection whose signed arithmetic distribution is *proved equal* to the same R_0 or its complement on the full test domain. Without such an identity, Connes-like Hilbert-space positivity is a different mathematical object. Verify prime-2 wavefront, fake6, non-Euler L, Gamma phase/contact and dyadic norm-vs-strong controls before any sign promotion.

## HW-13 — a genuinely finite-parameter sufficient sign test via source Γ derivative Gram

The HW-10 scalar `11556` bound is very conservative. An actual source-dependent upper bound of the shorted matrix is obtained by replacing it with **derivative interactions of the 30 low modes**.

For each genuine truncated source `g_J` define `G_J` (original prime powers, original contact, two poles, first J authentic Gamma modes, nothing fitted) and `Q=I−P` with P the 30-mode Legendre projection. On the 30-dimensional low space define the **positive derivative Gram**

`T_J(i,j)=∫_I (QG_J e_i)'(x) overline[(QG_J e_j)'(x)] dx`.

This is *not* the Weil form; it is a computable **upper error-energy instrument for the source-identified cross resolvent**. From the authentic positive Γ mode tail, with `d=4J+1`,

`τ'_J = ||g−g_J||∞ ≤ 1/d+4/d²`,
`||(g−g_J)'||_(L¹(-1,1)) ≤ 2τ'_J`.

The second inequality is Tonelli on the omitted gamma rungs, as in HW-10. By the already established Legendre derivative projector bound and Young's inequality,

`||(Q(G−G_J)x)'||₂ ≤ (2+961)τ'_J||x||₂ = δ_J||x||₂`, `δ_J=963(1/d+4/d²)`.

For every η>0, the ordinary Hilbert-space Young inequality implies the full **finite-dimensional Loewner upper bound**

`0≤ R_0 ≼ κ^−1 [(1+η)T_J + (1+η^−1)δ_J² I_30]`.              (HW13a)

Because the omitted original Gamma operator is PSD, the true low block obeys `A≽A_J=P G_J P`. Combining with the unshifted Schur equivalence yields the completely source-compatible **SUFFICIENT sign gate**

`A_J − κ^−1 [(1+η)T_J +(1+η^−1)δ_J² I_30] ≽0`               (HW13b)

`⇒ G_(a=1/2)≽0` for every state in the entire mean-zero Hilbert space.

**This inequality is not established for the authentic source.** All expressions are legitimate source-first objects and a finite J would suffice if they obeyed the displayed inequality, but the bound might be too crude and could fail even if G itself is positive. No sign is manufactured by the positive derivative Gram: it is explicitly SUBTRACTED. The next discriminating experiment is to build `T_J` with independent exact polynomial-exponential integrals from the pinned source `suzuki_legendre_source.py` and run rational LDL on the two 15×15 parity blocks, checking both real source and deliberate mutants. A failed sufficient test is only **inconclusive**, not a negative Weil witness.

This gives an alternative to directly approximating the compact high inverse, while paying the true H¹ source cost explicitly. It is the strongest concrete SUCC-to-Weil mathematical bridge from this round.

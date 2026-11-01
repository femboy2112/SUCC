# SUCC: arctangent reciprocal chart, four-sheeted source lift, and perpendicular Fourier carrier

**Research only; 2026-11-01.** Exact original four signed BBP poles and literal `U_0=0` from Main XVIII. Stacked on draft PR #448. Most instruments are classical: Möbius maps, finite Fourier transforms, Pontryagin duality, solenoids, and finite character orthogonality. We specialize them to the authentic rational source and characterize their actual obstruction. **No proof of base-16 normality of π, RH, or quantum speedup. No false physical sphere-to-Fourier identification.** Paper proofs are accompanied by source-specific exact Fraction and cyclotomic tests, not newly formalized Lean kernel results.

## F0 — The source, its three types, and the basic rule

Use the ORIGINAL forcing, for integers `n>=1`:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{A(n)}{D(n)},\quad
A(x)=120x^2-89x+16,\ D(x)=(2x-1)(4x-1)(8x-7)(8x-3).
\]
\[
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad z_n=e(U_n),\quad e(t)=e^{2\pi it}.
\]

Distinguish (i) source `r` as a **2-adic input-index function**, (ii) `U_n` as the **unwrapped rational chronological state**, and (iii) `z_n` as a **real-circle phase**. The circle map at time `n` is `F_n(z)=e(r(n)) z^16`. These are different objects and require explicit arrows between them. The prior selected normality gate is `S_N(h)=sum_(n<=N)e(hU_n)=o(N)` for EACH fixed integer h !=0. Neither a fixed invariant measure nor complete dyadic Haar sums discharge that gate.

## F1 — Source r is an isometry of Z_2, with a full finite residue permutation

Every coefficient of `D(x)` is an integer and `D(x)` is odd for every x in Z_2, so `r` is a regular rational function over Z_2. Reduce the numerator and denominator modulo 2 as polynomials: `A(x)=x (mod2)`, `D(x)=1 (mod2)`. The polynomial

\[
H(x,y)=\frac{A(x)D(y)-A(y)D(x)}{x-y}\in\mathbb Z[x,y]
\]

exists by divisibility by `x-y`; reducing the defining relation mod 2 gives `H(x,y)=1 (mod2)` identically. Therefore

\[
\frac{r(x)-r(y)}{x-y}=\frac{H(x,y)}{D(x)D(y)}\in\mathbb Z_2^\times,
\quad \boxed{v_2(r(x)-r(y))=v_2(x-y)}
\]

for every distinct x,y in Z_2. Thus r induces an **exact isometric permutation** on each `Z/16^a`, a>=1. This dyadic isometry was already identified in SUCC main-family research; this round independently rederives it and adds its exact Fourier selection rules. The finite probe exhaustively replays levels 16,256,4096,65536. These runs corroborate; the H-mod-2 argument proves ALL levels.

## F2 — Exact base-16 two-channel spectral transformation (SOURCE-SPECIFIC)

At every integer n, the explicit mod-16 source law is

\[
\boxed{\rho(n)=r(n)\bmod16=-n+2(n\bmod2)\bmod16.}
\]

This is established for ALL Z_2 inputs because the rational map has odd denominator and is compatible with congruence mod 16; the 16 exact residue cases exhaust the input classes.

Set `zeta=exp(2pi i/16)`, and define the Fourier-change kernel for the source **permutation** `rho` by

\[
K_{k,\ell}^{(1)}=\frac1{16}\sum_{n=0}^{15}\zeta^{\ell n-k\rho(n)}.
\]

Split the sum into even/odd n. The eight-term sum of even powers vanishes unless `ell+k=0 (mod8)`. If `ell=-k (mod16)`, the even and odd parts have factors `1` and `zeta^(-2k)`; if `ell=8-k (mod16)` the odd part changes sign. Hence the **full exact 16×16 matrix** is

\[
\boxed{K_{k,\ell}^{(1)}=
\begin{cases}
(1+\zeta^{-2k})/2,&\ell\equiv-k\pmod{16},\\
(1-\zeta^{-2k})/2,&\ell\equiv8-k\pmod{16},\\
0,&\text{otherwise}.
\end{cases}}
\]

It is unitary because it represents a genuine permutation after Fourier conjugation. No complex floating arithmetic is needed: `Z[zeta16]=Z[X]/(X^8+1)` and all 256 entries have been evaluated exactly in its eight-coordinate integral basis with two independent algorithms. **This is Fourier conjugation of SOURCE as a 2-adic time-index map, not yet the odd-denominator Fourier evolution of the selected real-circle state.**

## F3 — NEW all-resolution spectral confinement: two derivative classes

Differentiate the original rational source with respect to its index variable. Let `N(x)=A'(x)D(x)-A(x)D'(x)`. Direct integer-polynomial expansion yields

\[
N(x)-(11+4x(x-1))D(x)^2\equiv 8x(x+1)\pmod{16},
\]

where the congruence is coefficientwise. Since `x(x+1)` is divisible by 2 on **every** x in Z_2 and `D(x)` is a unit,

\[
\boxed{r'(x)\equiv11+4x(x-1)\pmod{16}
=\begin{cases}11,&x\equiv0,1\pmod4,\\3,&x\equiv2,3\pmod4.\end{cases}}
\]

For a>=2 set `Q=16^a`, `L=16^(a-1)`, and group the source Fourier kernel

\[
K_{k,\ell}^{(a)}=\frac1Q\sum_{n\bmod Q} e\left((\ell n-kr(n))/Q\right)
\]

into blocks `n=b+L t`, `t=0..15`. Because `2(a-1)>=a` and source denominators are 2-adic units, the exact rational Taylor congruence is

\[
r(b+Lt)\equiv r(b)+Lt\,r'(b)\pmod Q.
\]

The inner 16-point character sum is **zero** unless `ell-k r'(b)=0 (mod16)`. The only available derivatives mod16 are 3 and 11, so the FULL source-specific all-level conclusion is

\[
\boxed{K_{k,\ell}^{(a)}=0\ \text{unless}\ 
\ell\equiv3k\ \text{or}\ \ell\equiv11k\pmod{16},\quad a\ge2.}
\]

This is a necessary support restriction, NOT a claim that every permitted entry is nonzero or a new real-circle signed estimate. It is independent of initial seed and survives a coherent same-forcing nonnormal orbit. A positive extra-pole mutant `r(n)+1/(2n+1)` demonstrably changes the precise base-16 Fourier matrix; original source rigidity matters.

## F4 — The arctangent identity gives a genuine Möbius sphere rotation

For principal real branches and t!=0,

\[
\arctan(t)+\arctan(1/t)=\operatorname{sgn}(t)\pi/2.
\]

The local sign is branch information. On the projective coordinate `[a:b]` with t=a/b, reciprocal inversion is the globally defined Möbius involution `J([a:b])=[b:a]`, including 0<->infinity. The Cayley map 

\[
C([a:b])=\frac{b+ia}{b-ia}
\]

satisfies the rational identity `C(J t)=-C(t)^(-1)` without any arctangent branch choices. The matrix `i sigma_x=[[0,i],[i,0]]` lies in SU(2) (determinant 1 and unitary) and acts on CP^1 by the Möbius map `t->1/t`, a 180-degree rotation of the Riemann sphere. Its restriction to the real projective equator reverses its angular orientation: for `eta=2dt/(1+t^2)`, `J*eta=-eta`.

The EXACT circle conjugacy for the original source step is

\[
\boxed{J F_n J^{-1}=F_n^\vee,\quad F_n^\vee(z)=e(1/2-r(n))z^{16}.}
\]

The chiral source and boundary are **not** the same original source/seed:

\[
r^\vee(n)=1/2-r(n),\quad U_0^\vee=1/2.
\]

The actual unwrapped recurrence yields

\[
\boxed{U_n^\vee=1/2-U_n+8(16^n-1)/15.}
\]

The last term is an integer carry; it is essential to unwrapped history and absent after reduction modulo 1. Thus, for every fixed integer h,

\[
\boxed{S_N^\vee(h)=(-1)^h\overline{S_N(h)},\quad |S_N^\vee(h)|=|S_N(h)|.}
\]

More strongly, if both chirality variables are observed jointly, their empirical Fourier coefficient is

\[
\boxed{\widehat\mu_N^{joint}(h,k)=(-1)^k\frac{S_N(h-k)}N.}
\]

The diagonal `h=k` is always exactly `(-1)^h`. **This produces an exact chiral correlation, not an independent Fourier witness.** The signed real Fejer/lag statistic is unchanged under the dual (each lag is complex conjugated). The dual source has an even denominator and cannot be inserted unmodified into SUCC's original 2-adic integral source-permutation functor.

## F5 — Four inverse branches become ONE coherent inverse on the full solenoid

Use the 16-solenoid inverse limit, the classical compact group

\[
\Sigma_{16}=\{(x_j)_{j\ge0}\in(\mathbb R/\mathbb Z)^{\mathbb N}:16x_{j+1}=x_j\}.
\]

Its Pontryagin dual is `Z[1/16]` with character `chi_(m/16^j)(x)=e(m x_j)`. The multiplication by 4 endomorphism `p=[4]` on the ordinary circle is 4-to-1, but on the COMPLETE inverse limit it is an AUTOMORPHISM:

\[
\boxed{([4]^{-1}x)_j=4x_{j+1}.}
\]

Both compositions [4][4]^-1 and [4]^-1[4] are the identity, by the bonding law. This is a genuine repair of a pathway gap, not a fictitious inverse of the original 4-fold cover. The finite-stage map still has four branches and no global continuous section on the base circle.

Each original `r(n)` has odd denominator q. Define its canonical odd-torsion solenoid lift by

\[
\boxed{\iota(p/q)_j=\frac{p(16^{-j}\bmod q)}q\pmod1,\quad q\text{ odd}.}
\]

Since 16 is invertible modulo odd q, the lift is unique among q-torsion points above the given base circle phase, and is additive across compatible denominators. The genuine chronological source update on the solenoid is

\[
\widetilde F_n(x)=[16]x+\iota(r(n)).
\]

Define the FOURTH-root transported successor

\[
\widetilde G_n(x)=[16]x+[4]^{-1}\iota(r(n)).
\]

Then the exact naturality / covering square is

\[
\boxed{[4]\widetilde G_n=\widetilde F_n[4].}
\]

That is the correctly typed solution: **the operation and source label must BOTH be transported**. Demanding `[4] F_n=F_n [4]` with the same source violates the scalar source shift in general. A map can descend to a quotient under one condition and lift through a cover under another; these are not interchangeable assertions. The functors must remember source labels and branch histories.

## F6 — Chiral inversion is a natural equivalence only after choosing its branch tower

The base-circle half-turn `1/2` has many lifts in the solenoid. Choose the explicit compatible tower

\[
\tau_j=1/(2\cdot16^j),\quad [16]\tau_{j+1}=\tau_j.
\]

Define the affine involution on the full solenoid `J_tau(x)=tau-x`. Then

\[
\boxed{J_\tau\widetilde F_nJ_\tau^{-1}(x)
=[16]x+(1-[16])\tau-\iota(r(n)).}
\]

The zeroth coordinate is exactly the arctan reciprocal dual `x->16x+(1/2-r(n))` modulo 1. At fractional dual characters `m/16^j`, the half-turn tower contributes `e(m/(2*16^j))`; changing the tower while preserving `tau_0=1/2` alters these fractional phases. Thus the **whole branch history remains observable** in the full Fourier dual even when all base-circle observations agree. Exact finite towers were checked using odd-torsion states and a second lift differing by a nonzero kernel element.

## F7 — The finite register must be doubled AS A TORSOR, not by naïve ×16

Let Q be an odd common source denominator up to a chosen finite horizon. The original circle phases live in the odd-torsion subgroup `A=(1/Q)Z/Z`. Its reciprocal chart lives in the disjoint coset `B=1/2-A`. They partition the even-clock set `(1/(2Q))Z/Z` into TWO Q-point torsors.

In integer coordinates modulo 2Q, the original sector consists of even labels x and the dual sector of odd labels. Put `b=Q*r(n) modQ`. The exact source-labelled map is

\[
P_n(x)=\begin{cases}
16x+2b\pmod{2Q},&x\text{ even},\\
16x+Q-2b\pmod{2Q},&x\text{ odd}.
\end{cases}
\]

Each restriction is a PERMUTATION because `gcd(16,Q)=1`; the full two-sector operation is also a permutation and intertwines the involution `J_Q(x)=Q-x`. It represents two differently labelled but canonically conjugate SUCC species in one finite Hilbert space, with exact history. This is NOT equal to the naive map `x->16x+b` on all `Z/(2Q)`: the latter is NOT invertible, since `gcd(16,2Q)=2`.

Let `DFT_(2Q)` be the unitary negative-exponent discrete Fourier transform. Character orthogonality gives `DFT_(2Q)^2|x>=|-x>`. If `S_Q` shifts positions by half a clock, then

\[
\boxed{J_Q=S_Q\,DFT_{2Q}^{2}.}
\]

**This is the exact connection between arctan inversion and a perpendicular Fourier frame:** a **half-turn translation plus two Fourier quarter-rotations**, on a properly augmented and source-labelled carrier. A single DFT is NOT generally a pointwise rotation of an ordinary sphere: on a Q-dimensional quantum register it acts on CP^(Q-1), not CP^1 except Q=2. The sphere inversion is a separate SU(2) projective rotation; the two constructions agree on this specific involution only after typing the finite carrier correctly.

On the original odd-Q source register, the *single* DFT also provides the honest Fourier state map for the chronological permutation `P_n|x>=|16x+Q*r(n)>`:

\[
\boxed{DFT_Q P_n DFT_Q^{-1}|p>
=e\left(-\frac{p\,16^{-1}(Qr(n))}{Q}\right)|16^{-1}p\bmod Q>.}
\]

This is a true reversible change of polarization, preserving every source-defined complex amplitude. It is **different** from F2/F3's time-index source permutation Fourier matrix. Confusing those two Fourier transforms would commit a source-map type error.

## F8 — Arctan reciprocity also supplies the exact invariant geometric measure

The projective tangent coordinate `t=tan(pi x)` maps the circle Haar measure `dx` to the standard Cauchy measure on the real chart,

\[
\boxed{d\nu(t)=dt/[\pi(1+t^2)]}.
\]

The reciprocal substitution `t->1/t` preserves this measure: `dt/(1+t^2)` is transformed into the same UNSIGNED volume form, whereas the oriented angular one-form changes sign. This is exactly the analytic content of the arctan reciprocal identity. The source rotation map `(t+a)/(1-at)` preserves this Cauchy measure, and the 16-fold projective circle map preserves its probability pushforward (the angular form pulls back by 16 on each branch).

The Cauchy distribution is therefore a common invariant probability measure for EVERY time-indexed circle map `F_n` including the authentic source, and for its chiral dual. But a source-invariant measure does NOT imply that the deterministic selected orbit is generic for it. The exact same forcing with completed q=1/5 yields `U_n(q)=16^n/5-T_n`, whose circle phase converges to e(1/5), so its tangent orbit converges to `tan(pi/5)` rather than equidistributing under ν.

The **correct** selected π normality criterion can equally be stated: the empirical projective-tangent measures of `t_n=tan(pi U_n)` converge weakly to ν. This is exactly equivalent to the original Weyl criterion by the projective circle homeomorphism. It does not constitute a new signed saving.

## F9 — A strict cross-place obstruction: no continuous 2-adic-time → real-circle source map

One could be tempted to take the dyadic isometry F1 and directly reinterpret its eigenmodes as source rotations on the real projective circle. The actual source defeats that proposed continuous extension.

Take integer times `n_j=1+16^j`. Then `n_j->1` in Z_2, while as **real** numbers `n_j->infinity` and the original positive forcing satisfies `r(n_j)->0`. But `r(1)=47/15`, so

\[
\boxed{e(r(n_j))\longrightarrow1\ne e(47/15).}
\]

Thus the map from positive integers `n->e(r(n))` admits **no continuous extension** from their 2-adic closure Z_2 into the ordinary real circle that retains the original archimedean character values. The original source is entirely well-defined in BOTH completions; the obstruction is transporting their topologies and phases with an unsupported common basis. This is an actual access/source-map defect, not an impossibility of a larger adelic/graph carrier retaining both coordinates. A repaired categorical diagram must keep a separate real-archimedean source label, rather than identifying 2-adic Fourier orthogonality with real-circle BBP cancellation.

## F10 — Machin is a geometrically independent arctan chart, not a BBP source theorem

Exact multiplication of Gaussian integers gives the identity

\[
\boxed{(5+i)^4=476+480i=2(1+i)(239+i).}
\]

Taking arguments with explicitly checked first-quadrant branch yields the **classical Machin identity**

\[
\boxed{\pi=16\arctan(1/5)-4\arctan(1/239).}
\]

This provides a completely independent *angle/geometry* calibration of the original π constant, and arctan reciprocity may exchange its large and small tangent charts while paying ±π/2 branches. For each truncation of the positive-x alternating arctan series, the first omitted term gives a rational outward interval for π. The artifact implements two independent exact Fraction versions and uses these intervals as a finite cross-check for the authentic BBP truncation.

The Gaussian integer factorization and tangent reciprocity do not select the ORIGINAL four-pole BBP r(n), nor do they prove base-16 normality. They ARE valuable as a provenance-independent geometric angle oracle to test source–circle conversion without an externally entered decimal π.

## F11 — Verdict, independence and falsification

- **Disclosed / classical (source-specialized):** F1 dyadic isometry, F2 base16 exact two-mode cyclotomic kernel, F3 all-level derivative-based Fourier support, F4 projective arctan involution and chiral source/carry, F5 exact solenoid [4]-inverse and source-specified square, F6 branch-history dependence, F7 finite chiral torsor and Fourier-square identity, F8 Cauchy measure invariance, F9 no real-continuous Z2 source-phase extension, F10 Gaussian-integer Machin identity. The all-level proofs are algebra/analysis, not finite exhaustive numerical extrapolation.
- **Proved negative controls:** no independent selected information in the chiral dual Weyl sum; naive ×16 not unitary on a full even conductor; source shift not invariant under a bare four-cover; no global 2-adic/real continuity; source-agnostic Haar or Cauchy stationarity cannot establish selected π normality; projective SU2 inversion is not a general DFT of a 16-state register.
- **Observed finite:** exact 16/256/4096/65536 source permutations; all 256 base16 cyclotomic matrix entries; modular Taylor and Cauchy identities, full finite solenoid towers, chiral torsor permutation, the independent Gaussian identity and rational Machin/BBP bracket.
- **OPEN:** original zero-seeded, all-horizon signed Weyl saving `sum_(n<=N)e(h U_n)=o(N)` for each fixed h!=0, or a new authenticated mixed source/archimedean Fejer condition. Nothing above pays that debt. Fourier-support sparsity applies to **source as function of 2-adic input index**, not to the target actual selected real-circle sequence.
- **Next falsification:** construct a SOURCE- and ZERO-BOUNDARY-dependent cross-completion coupling between actual real-circle lags and permitted dyadic Fourier mode pairs, with a non-vacuous signed inequality that fails for same-forcing q=1/5. A mere recast through solenoids, chiral conjugation, the invariant Cauchy law, or the Machin constant cannot pass.

## Explicit classical provenance

- Standard arctan branch identity: Stanford trigonometry reference https://stanford.edu/~shervine/teaching/cme-102/trigonometry/ and NIST DLMF §4.23 https://dlmf.nist.gov/4.23.
- `16`-solenoid and its dual `Z[1/16]`: Proposition 1.2 in https://cs.du.edu/~frederic/research/1110.6227.pdf; inverse limits and homotopy discussed in the mathematical literature, e.g. https://ncatlab.org/nlab/show/solenoid.
- Fourier as 90-degree rotation of CANONICAL phase space, not arbitrary spatial sphere: Lopez–Dodin 2019, https://www.osti.gov/pages/servlets/purl/1573502; https://collaborate.princeton.edu/en/publications/pseudo-differential-representation-of-the-metaplectic-transform-a/.
- Classical Machin identity and derivation https://www.math.brown.edu/reschwar/M10/machin.pdf.
- SUCC inherited sources: Main XVIII `AGENTS.md`, `docs/CATEGORICAL_OBSERVER_ATLAS.md`, `observational_succ/operational_yoneda_descent.py`, sibling PR #437 source four poles, stacked #438–#448. The original four-pole identity is imported and never changed. These dependencies are NOT external corroboration of new formula claims.

## F12 — MAJOR SOURCE/GEOMETRY TRANSPORT: the original four-pole BBP period IS a circle angle modulo an exact zero-boundary coboundary

This result addresses the missing **source-authentication** for the circle/path quotient discussed in PRs #447–#448. Rather than assuming the BBP identity as an input, start only with its literal original four rational poles and derive the geometric π period by direct integral calculus.

The partial-fraction identity

\[
r(n)=\int_0^1 t^{8(n-1)} P(t)\,dt,
\quad P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2)
\]

is exact for every integer n>=1. By Tonelli, since the positive integrand converges uniformly on the compact domain for the 16^-n weighting, its completed BBP source is

\[
\alpha:=\sum_{n=1}^{\infty}16^{-n}r(n)
=\int_0^1\frac{P(t)}{16-t^8}\,dt
=\int_0^1\frac{1-t}{(2-t^2)(t^2-2t+2)}\,dt.
\]

Factorization used above is **exact**:

\[
16-t^8=(2-t^2)(2+t^2)(t^2-2t+2)(t^2+2t+2).
\]

Put `u=t-1` and let `eta(u)=2du/(1+u²)` be the canonical oriented angular one-form of the unit circle on its real projective rational chart. On the original integration segment `0<=t<=1` define the smooth real logarithmic potential

\[
G(t)=\frac18\log\frac{2-t^2}{t^2-2t+2}.
\]

The key **source-attested differential identity**, checked by independent symbolic factorization and exact Fraction samples, is

\[
\boxed{
\frac{P(t)}{16-t^8}\,dt
=\frac18\eta(t-1)+dG(t)
=\frac{dt}{4[1+(t-1)^2]}+dG(t).
}
\]

Crucially the ORIGINAL source factorization enforces the EXACT BOUNDARY CANCELLATION

\[
G(0)=\frac18\log(2/2)=0,
\qquad G(1)=\frac18\log(1/1)=0.
\]

Thus the relative de Rham classes agree on the oriented interval with fixed boundary:

\[
\boxed{[\omega_{BBP}]=\frac18[\eta(t-1)]\quad\text{in }H^1_{dR}([0,1],\{0,1\}).}
\]

Evaluating the genuine quarter-circle angular increment, without importing the BBP-to-π identity,

\[
\boxed{\alpha=\frac18\int_{-1}^0\frac{2\,du}{1+u^2}=\frac18\frac\pi2=\frac\pi{16}.}
\]

Equivalently, **the literal four-pole BBP series identity** `π=16 Σ 16^-n r(n)` follows directly from (1) four-pole partial fractions, (2) exact Mellin/geometric summation, and (3) a circular quarter-turn period. This is a new explicit source-to-circle *decomposition* for SUCC; it is not claimed as an academically novel way to prove an established BBP identity. The logarithmic coboundary is generally NONZERO at interior t, so the mathematical paths are not locally identical; their **relative period** is identical because the endpoints annihilate its contribution.

**Finite chronological identity and exact future:** Let `alpha_N=Σ_(n=1)^N 16^-n r(n)` and `T_N=Σ_(j>=1)16^-j r(N+j)`. The exact geometric series gives

\[
\alpha_N=\int_0^1\frac{P(t)}{16-t^8}\left[1-(t^8/16)^N\right]dt
=\underbrace{\frac18\int_{-1}^{0}\eta}_{\alpha}
-16^{-N}T_N.
\]

Thus, using only the original arithmetic recurrence,

\[
\boxed{U_N=16^N\alpha_N=\frac{16^N}{8}\int_{-1}^0\eta -T_N
=16^{N-1}\pi-T_N.}
\]

This is a **genuine, precisely typed finite arithmetic ↔ circle-angle boundary transport**. It is the missing geometric interpretation of the future correction developed in #446–#448. It does NOT give signed Weyl cancellation; the phases still have to be summed at all horizons.

**Hostile source mutation:** Modify the original positive Mellin density by `P_epsilon(t)=P(t)+epsilon*t^7(1-t)^8`, epsilon>0. Then the source is altered by the original positive Beta test mutant `b_n=epsilon B(8n,9)`, retains a literal zero seed and strict positivity but adds poles beyond the original four. Its completed source period changes by

\[
\Delta\alpha=\epsilon\int_0^1\frac{t^7(1-t)^8}{16-t^8}dt,
\quad \boxed{\frac{\epsilon B(8,9)}{16}<\Delta\alpha<\frac{\epsilon B(8,9)}{15}},
\quad B(8,9)=1/102960.
\]

The extra density cannot be silently called the SAME geometric quarter-turn: its relative period changes by a certified positive amount. The exact source poles and density are doing theorem work.

## F13 — Source sphere and completed angular sphere are not Möbius-equivalent: Mellin completion is the indispensable arrow

The four source-index rational poles of r(z) are `(7/8,1/2,3/8,1/4)` with ordered cross ratio `lambda_source=8/5` and elliptic-cover invariant `j_source=470596/225`, already independently established in PR #442.

The **reduced COMPLETED Mellin differential** of F12 has four other simple t-plane poles at

\[
(\sqrt2,-\sqrt2,1+i,1-i).
\]

They are a harmonic configuration: the SAME cross-ratio convention gives `lambda_completed=-1` and

\[
\boxed{j_{completed}=1728\ne\frac{470596}{225}=j_{source}.}
\]

This is an exact SymPy rational/surd symbolic certificate. The `j=1728` cross-ratio configuration has the familiar order-four complex symmetry after taking its double cover, but the BBP differential has LOGARITHMIC poles and is NOT automatically a holomorphic elliptic period; do not promote this to a new elliptic normality theorem.

**Obstruction:** A single Möbius rotation of the original four-punctured source Riemann sphere cannot map its four source punctures to the completed t-plane four punctures. The unordered four-point j-invariant is preserved under all such transformations, and the invariants differ. It follows that the source-to-angle identification CANNOT arise from an unsupported direct rigid/projective rotation of one fixed four-punctured sphere.

**Repair:** F12 supplies a concrete, legitimate NON-MÖBIUS arrow: exact Mellin summation changes the variable and rational pole geometry, then relative de Rham projection kills the endpoint-exact logarithmic term. F4/F6 supply a DIFFERENT lawful Möbius/inverse-limit chart equivalence for the final circle and its chiral companion, with full branch histories retained. The source sphere, completed Mellin t-sphere, projective circle, dyadic source spectrum and odd real-circle quantum register are distinct typed objects linked by actual derived maps. This is precisely the categorical distinction that earlier 2D snapshots concealed.

This does not evade the normality gate. The relative period is known and source-selected, yet a single period supplies no theorem about the distribution of its repeated ×16 orbit. A future genuinely new signed bound must exploit the **local time/history data** of the relative-period transport rather than only the period equality.

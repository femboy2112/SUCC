# ONE OBJECT II — SOURCE-CANCELLED HILBERT–ZENO × TATE–WEIL–SUZUKI ZERO-SHIFT CERTIFICATES

**15 October 2026 · mathematical checkpoint; RH OPEN.**

**Pinned parent:** draft [PR #106](https://github.com/femboy2112/SUCC/pull/106), head `04b6d8ede12c58afe4a244b11297663c33260de1` (includes exact Tate-source PR #103 head `940f0a47ef25b8b553c2f0b45032b37e68c23b02`, genuine Weil↔Suzuki completion/contact, Connes local clock). Separate related siblings: [#107](https://github.com/femboy2112/SUCC/pull/107), head `dfceb9ca17cd1a54738a809185939fb31347c39d` (source-authentic finite-J low Legendre derivative-energy enclosures), [#104](https://github.com/femboy2112/SUCC/pull/104), head `88eca261bae1381b83d018163d0945c3434a3385` (zero-shift Douglas range existence); [#105](https://github.com/femboy2112/SUCC/pull/105), head `2da47bd86c63225aae3d64279d789ea1a805b428` (exact original signed finite-J cell integrals). All descend from Phoenix II `main@03db44203147a7b28d445bb9f970fa71360e78c4` but neither sibling's code is silently imported into this PR. The **original immutable signed Suzuki source module** `observational_succ/source_weil_hierarchy.py` has Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. No main edits, no external RH push, no physical source attestation, no zero lists.

## 0. The actual proof debt: not another positive kernel

Tate fixes local additive Fourier, multiplicative Mellin, character/conductor/parity, one Archimedean Gamma and the functional-equation normalization. PR #106 establishes exact *finite-stage* completed Weil distribution ↔ twice-integrated Suzuki screw kernel with a contact correction. The Connes/Consani local finite-clock trace computes a fixed-point factor away from scaling identity, while the contact principal-value at identity and **global adelic trace** remain independent, UNSOLVED identifications. None of these already-established arrows supplies the global sign.

On the genuine first-prime interval `a=1/2`, Suzuki works with

\[
H=L^2_0(-a,a),\quad G=G_a=G_a^*\text{ with kernel }g(|x-y|),\quad
K=V^*V=(-\Delta_N)^{-1},\quad (Vu)(x)=\int_{-a}^{x}u(t)\,dt.
\]

Here the derivative source vectors satisfy `\int u=0`, hence `Vu` has zero boundary values. On the 30 true Legendre modes `F=span{P_1(x/a),...,P_{30}(x/a)}` (normalized in H), let `P` project onto F and `Q=I-P`. Decompose **the original signed** operator

\[
G=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\qquad
D=QGQ\succeq\kappa QKQ,\quad \kappa=369/10000.
\]

The high-sector positive lower bound comes from **the authentic complete Weil source** AMW-06B in PR #86, transported into Suzuki derivative coordinates by PR #96; it is `κK`, **not** a fictitious `κI`. This is an imported mathematical theorem with its hypotheses, not independently formalized here. PR #99 isolates the Douglas range and zero-shift shorting gate; PR #104 already proves source-specific *existence* of the zero-shift Gram. **The novel local results below sharpen its constants and introduce a trial-residual two-sided source certificate.**

## 1. Exact full-source derivative identity (PROVED / classical special functions + original arithmetic)

On `0<r<1`, excluding the one true prime-2 threshold `b=log 2`, the original infinite-rung screw kernel is

\[
\begin{aligned}
g(r)={}&-4(e^{r/2}+e^{-r/2}-2)
+\tfrac12 C_G r
+\frac{\log2}{\sqrt2}(r-\log2)_+\\
&-4\sum_{j=0}^{\infty}
 \frac{1-e^{-(4j+1)r/2}}{(4j+1)^2},\qquad
C_G=\gamma+\frac\pi2+3\log2+\log\pi.
\end{aligned}
\]

This is **the actual PR85 original zeta source** (not a fabricated positive bath). The Gamma rungs can be differentiated at each `r>0` by dominated geometric summation, giving

\[
\boxed{
g'(r)=-4\sinh(r/2)+\frac{C_G}{2}
+\frac{\log2}{\sqrt2}{\bf1}_{r>\log2}
-\operatorname{artanh}(e^{-r/2})-\arctan(e^{-r/2}).
}\tag{OS2-1}
\]

Proof of the Gamma identity: for `z=e^{-r/2}` with `0<z<1`, the odd-index generating functions give
`atanh(z)+atan(z)=2 Σ_{j>=0} z^(4j+1)/(4j+1)`. The source is even in `r`, so its weak derivative is odd. The logarithmic singularity at `r=0` is integrable, including its square. Prime 3 does **not** enter on `|r|<=1`, since `log3>1`; 4 is a legitimate power of 2 but its threshold `log4>1`, while 6 is not a prime-power atom at all.

**External-sourcing status:** finite Tate/Suzuki contact from #106 and the original immutable Weil kernel from #85 determine the identity. These identities are classical; priority is not claimed.

## 2. A rigorous source cancellation enclosure (NEW SOURCE-EXECUTABLE CERTIFICATE)

The original Gamma derivative and the prime/Archimedean/pole/contact terms nearly cancel. The pure-`Fraction` code `observational_succ/signed_gprime_enclosure.py` proves **without any floating-point samples, zeta zeros or numerical integrals**:

\[
\boxed{
\frac14<\|g'\|_{L^1(-1,1)}<\frac{11}{40},\qquad
\|g'\|_{L^2(-1,1)}^2<\frac4{25}.
}\tag{OS2-2}
\]

**Proof algorithm and why it is rigorous:**

1. Evaluate `C_G`, `log2`, `pi`, `log pi`, `sqrt2`, `exp`, `atan` and `atanh` in *outward directed rational intervals*: positive Taylor geometric tails for exp/log/atanh, Machin's alternating arctangent for pi, reduced-argument alternating arctangent for `atan`, Euler–Maclaurin harmonic remainder for gamma, and integer-isqrt enclosures for `sqrt2`. These are exact rational deductions under the classical analytic remainder lemmas; not an empirical approximation to the source.
2. On each rational cell `[j/4096,(j+1)/4096]`, `j>=1`, the pole derivative `-4sinh(r/2)` decreases, while the Gamma derivative `-atanh(e^-r/2)-atan(e^-r/2)` increases. Therefore separate endpoint extrema + the rational contact interval + the strictly source-identified step at `log2` give an enclosure **for every real r in the cell**. The wavefront-overlapping cell uses the full interval `[0, log2/sqrt2]` for its prime step rather than pretending a jump is smooth.
3. The cell containing `r=0` is **never sampled**. The analytic inequalities `1-e^-r/2 >=r/(r+2)>=r/3`, `atan(z)<1`, and `atanh(e^-r/2)<=0.5log(6/r)` give an elementary pointwise upper. Its exact `L¹` integral is `delta [C+0.5(log(6/delta)+1)]`, and its `L²` square integral is `delta(B²+B+1/2)` after setting `B=C+0.5log(6/delta)`, with `delta=1/4096`.
4. Summing directed upper bounds of `|g'|` and `|g'|²` times **exact** cell widths, using oddness, gives the strict rational claims (OS2-2). For a lower positive witness, use `min(abs(lo),abs(hi))` on cells whose entire interval excludes zero, and sum these exact lower bounds. The entire proof checks every cell, not a finite numerical fit of `g`.

A standalone 55-digit mpmath integration (held as **NUMERIC DIAGNOSTIC**) returns approximately `||g'||_1≈0.2634744210` and `||g'||_2≈0.3452714870`; the numerical values are **not the proof**. The outward interval code certifies the reported inequalities without using mpmath. Deliberately removing the true 2-jump or changing the contact alters the cell derivative profile, and source-type checks reject that mutation as authentic. The code is isolated from source-less `A5`/Hilbert positive-Gram toys.

This is the **first clear, operator-useful source cancellation** we have obtained from the *complete original* first-window Weil data. It is not an RH proof, but improves the previous #104 generic triangle upper by orders of magnitude.

## 3. Zero-shift Feshbach range and a substantially sharper bound (PROVED given authentic high theorem)

The original screw kernel has `g∈W^{1,1}(-1,1)∩H¹(-1,1)`. Young's convolution inequality on the unit window gives, for every `f∈H`,

\[
\boxed{\|(Gf)'\|_2\le\|g'\|_{L^1(-1,1)}\|f\|_2
<\tfrac{11}{40}\|f\|_2.}\tag{OS2-3}
\]

**Key optimization:** For a high vector `h∈QH` and low vector `x∈F`,
`<B*x,h>=<Gx,h>`; do NOT differentiate `QGx`, which adds artificial large derivatives of the 30-mode projection. Instead integrate by parts directly in the *original* source:

\[
\langle Gx,h\rangle=-\langle (Gx)', Vh\rangle,
\quad \langle Dh,h\rangle\ge\kappa\|Vh\|².
\]

The variational formula for the positive high shorting produces

\[
\boxed{
0\preceq R_0:=\lim_{\lambda\downarrow0}B(D+\lambda I)^{-1}B^*
\prec\frac{(11/40)^2}{\kappa}I_F
=\frac{3025}{1476}I_F\quad(\approx2.04946 I_F).
}\tag{OS2-4}
\]

All low vectors are unit-normalized in `L²_0`. This is an **unconditional result for the original Suzuki model conditional only on the already-proved first-window `D>=κK` source theorem and the classical Weil-to-Suzuki identity**, not a sign assumption. PR #104 had a valid but much coarser `~3.6e9` trial range constant after differentiating `QGx`, while the newer parallel #107 proves source-low derivative enclosures but still lists `||g' ||_1<26` as its global bound. A naive whole-kernel triangle bound gives `4840000/369≈13116`. The above proof keeps the correct high/low source orthogonality and exploits the authentic cancellation; no unauthorized `κI` gap or inverse of compact `D` is used.

Existence and finiteness of `R0` follow from its increasing positive resolvent quadratic forms being uniformly bounded; the low space is finite-dimensional. The Douglas range inclusion is equivalently recovered from the same bounded functional. This **does not** show `A-R0>=0`. Indeed the bound `~2.05` is still far above the delicate first-window low-mode sign scale.

## 4. NEW true zero-shift **trial-residual** two-sided Schur enclosure (PROVED functional-analysis lemma)

Let `F=P H` (30 dimensions), `H_hi=QH`, `A=PGP`, `B=PGQ`, `D=QGQ`. For **any bounded linear finite-column trial map** `U:F->QH`, with columns in the declared source high carrier, set

\[
\begin{aligned}
L_U&=BU+U^*B^*-U^*DU,\\
R_U(x)&=G(x-Ux)\in H^1(-a,a),\\
C_U(x,y)&=\langle (R_Ux)',(R_Uy)'\rangle_{L²}.
\end{aligned}
\]

By shifting the variational supremum defining `R0` by `Ux`, and using the **same original antiderivative** `V`, source inequality `D>=κ V*V`, and integration by parts,

\[
\boxed{
L_U\preceq R_0\preceq L_U+\kappa^{-1}C_U,
\qquad
A-L_U-\kappa^{-1}C_U\preceq S_0:=A-R_0\preceq A-L_U.
}\tag{OS2-5}
\]

**Proof:** for `x∈F` and `h=Ux+z∈QH`, expand `2Re<B*x,h>-<Dh,h>` into `<L_Ux,x> + 2Re<G(x-Ux),z>-<Dz,z>`. Integration by parts yields `|<G(x-Ux),z>|≤||(G(x-Ux))'||·||Vz||`; the high positivity gives `−<Dz,z>≤−κ||Vz||²`. Optimize scalar `t=||Vz||` to obtain the quadratic residual penalty `κ^-1||(G(x-Ux))'||²`. Taking `z=0` gives the opposite bound. No inverse `D^-1` is used, and the result includes **all** signed correlations of the original Weil source through `G`.

**A direct finite-input acceptance criterion:** Construct original-source, outward-rational enclosures for the 30×30 matrices `A`, `L_U`, and `C_U` on the true Legendre split. If the certified lower matrix `A−L_U−κ^-1 C_U` is PSD, then **the full original completed Weil form is positive on the complete first-prime window**, not just sampled vectors. If the certified upper `A−L_U` is negative on an original-source vector, it proves a strict original negative witness (which would refute RH after provenance audit). Failure of either finite test is **UNRESOLVED**, not RH evidence.

**Synthetic exact demonstration (not authentic zeta):** In dimension one low and two high, with
`K=diag(1/4,1/9)`, `D=diag(1/2,1/3)`, `B=(1/4,1/6)`, `κ=1/2`, `R0=5/24`, `A=R0+1/120`, the zero trial gives `S_lower=-47/60` and cannot certify sign. The lawful high trial `U=(1/2,1/2)` exactly solves `DU=B*`, makes `C_U=0` and certifies `S0=1/120>0`. Arbitrary finite intermediate rational trials give exact two-sided bounds with a residual width falling quadratically with trial-error. Replacing `A` by `R0−1/120` yields an **exact negative Schur witness**, preventing the verifier from manufacturing universal positivity. The tests check both sign directions and reject unverified high positivity, singular inverse-Neumann metrics and float/bool source laundering.

**Major remaining debt:** this PR has **not** computed the actual source `U`, `A`, `L_U` and `C_U` at rank 30 or proved a uniform decreasing original-source residual schedule. PR #96 gives efficient direct original low Legendre entries, PR #105 gives original exact signed finite cell integrals, and parallel PR #107 supplies finite-J source low Legendre derivative-energy interval machinery, but none automatically supplies certified **projected high-trial** derivative residual matrices on the full high continuum.

## 5. Hilbert fractal now controls the original FULL signed operator in the right topology (PROVED on first window)

Let `E_N` be conditional expectation onto mean-zero dyadic cell-constant functions of the **original** interval `(-1/2,1/2)` with `N=2^d` equal cells. The **original full** signed screw kernel on the product square is `K_G(x,y)=g(x-y)`. By (OS2-2) and the exact two-axis conditional-expectation/Poincaré inequality,

\[
\|K_G- E_N^x E_N^y K_G\|_{L²([-1/2,1/2]^2)}
\le h(\|\partial_x K_G\|_2+\|\partial_y K_G\|_2)
<\frac{4}{5N},\quad h=1/N.
\]

The same bound holds in **Hilbert–Schmidt and operator norm** after mean-zero compression. A Hilbert path is simply a dyadic permutation of these N² square cells: it preserves all cell weights, signed energy and the operator norm, and supplies a finite successor ordering with source-compatible nested refinements. **Space filling itself does not create positivity.**

Use PR #105's *independently constructed exact original-source finite-J block CELL INTEGRALS*, rather than invalid midpoint sampling of a logarithmically singular derivative. With the original infinite-contact source `g_J` from PR85 and its proved uniform omitted-Gamma bound `tau_J=1/(4J+1)+4/(4J+1)^2`, obtain the improved two-axis Zeno theorem

\[
\boxed{
\|G-E_NG_JE_N\|_{\rm op}
<\frac4{5N}+\frac1{4J+1}+\frac4{(4J+1)^2}.
}\tag{OS2-6}
\]

At `N=J=1024` the exact rational upper is `<0.001026`; at `N=J=16384`, `<0.000065`. The analytic theorem is for all positive N,J; the present Python bounds do not assert physical measurements or actually construct the 16384×16384 matrix. In contrast to the older midpoint `h L_J` bound growing like `log J/N`, the **full-source Sobolev** estimate gives `O(1/N)` spatial error independent of Gamma truncation. This is the Hilbert/Weil use-case, not an aesthetic scan or an invented operator isomorphism from arbitrary 1D orderings.

**Critical limitation:** (OS2-6) is an L²/compact-operator certificate, NOT a convergence estimate for unbounded `D^-1`, the zero-shift shorted matrix, or the Connes scale-trace distribution. The derivative residual in (OS2-5) requires its own source-correct interval quadrature and error proof. The next source theorem must explicitly connect those two moduli.

## 6. Why Tate, Connes and source stamps matter

The source identity predicate in `parent_original_source_contract` reads (i) the exact PR85 original source-module Git blob through `suzuki_legendre_source._pinned_source`; (ii) `TateWeilProfile.canonical('zeta')` with conductor 1, even parity, root +1, completed poles and half-density 1/2; (iii) the exact finite real contact increment from PR106. The branch cannot silently apply the resulting source sign to the odd conductor-3 `chi_{−3}` profile. A genuine prime-power impulse is not a primitive composite-6 place.

The Connes local `Z/p^r` fixed-point trace is a distinct model: identity scaling is singular, and local off-identity values cannot determine the principal-value/contact distribution. The exact global Tate↔Connes semi-local trace equivalence with the full signed Weil functional, and the operator realization of the entire spectral/shorted form, remain **UNVERIFIED**. Connes–Consani (arXiv:2006.13771) prove an Archimedean Sonin-trace comparison with *support and Fourier-moment restrictions*; transplanting that restricted sign to the original all-prime completed Weil form is unauthorized.

### Negative-controls contract

- Change the contact `C_G` or omit the authentic p=2 jump: the certified cancellation argument no longer describes the original source, even if a numerical plot looks similar.
- Substitute a positive helper Gram: the entire signed Weil normalization is lost.
- Treat `Hilbert` cell reordering as an isometry of Sobolev derivative energies or source-prime multiplicative actions: forbidden; our theorem controls Hilbert square *area* only.
- Use `κI` instead of `κK` on high: forbidden; the low/high source metric is inverse-Neumann.
- Treat local ζ/χ conductor data interchangeably, introduce a fake primitive composite 6, or omit pole/contact: forbidden.
- Claim that low-moment sign from a synthetic rational block carries to original source: forbidden.
- Claim a finite `(N,J)` bound gives positivity without sign margin: forbidden.
- Make the original source positive by defining a new Sobolev/Connes Hilbert feature space: circular unless **all** original signed source entries match.

## 7. Results, verification and next falsification

**Locally executed:** source-neutral Fraction algebra and interval proof suite, source signed scalar/derivative controls, Hilbert dyadic geometry, complete negative toy controls. A separate mpmath derivative integration is only an independent **numerical holdout**. Exact source `TateWeilProfile` and original SHA-bound adapter are exercised only after checking out the full GitHub ancestor; the isolated overlay transparently reports those tests as skipped. The dedicated CI must run and fail closed if the real parent module is missing/modified. No Lean kernel proofs or physical observer validation claimed.

**Immediate next falsifier/proof step:** Build a small but *actual* source Legendre low/15+15 block with analytic original finite-J element enclosures (PR #96 and parallel #107). Choose high-source trial columns `U` from true Legendre modes 31..M, compute `L_U` and the derivative Gram `C_U` using the exact `g'` interval machinery and rigorous two-axis quadrature with a matched resolution schedule, then test `A−L_U−κ^-1 C_U`. If the bound refuses sign, inspect its genuine deficit and construct a less wasteful high preconditioner instead of assuming RH. If a strict original negative direction is found, cross-check the explicit formula, one Gamma/contact/poles, source prime tape and domain independently before reporting. Finally expand a from 1/2 and construct a source-uniform exhaustion theorem: all-a positivity is RH-hard.

**RH PROVED: NO.** One cannot claim this branch leaves only a minor technical step; it makes the remaining obligations more exact and substantially improves cancellation/error constants, which is genuine progress.

### Primary mathematical sources and related review

- Masatoshi Suzuki, *Weil's quadratic form via the screw function* (2026), arXiv:2606.09096v3, §1 and §7.7; the full spectral realization is conjectural.
- Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771, Theorem 1; **only the stated support/moment space**.
- Tate's thesis and standard Schwartz–Bruhat local/global zeta functional equation with self-dual Haar measures (external classical normalization).
- SUCC pinned sources PR #85, #86, #96, #99, #103, #104, #105, #106; all statuses and exact SHA inputs recorded at opening.

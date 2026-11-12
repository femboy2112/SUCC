# π base-16 normality — Main XXV frontier

Maintained 2026-11-12. **Source-selected signed cancellation, original-zero
hexadecimal parity balance and parity words, π base-16 normality, completed Weil
positivity, and RH remain OPEN.** Main XXIV consolidates the source, identity and
observer machinery; it supplies no missing statistical estimate. Main XXV adds the
exact ladder of signed statements below the canonical target, thresholds for its rungs
in the canonical units, the necessary Diophantine cost of any saving, and a settled
restricted-exponent probe (§9); it also supplies no estimate. The Main XXV
[audit](SUCC_MAIN_XXV_INTEGRATION_AUDIT_2026-11-12.md),
[manifest](SUCC_MAIN_XXV_INTEGRATION_MANIFEST_2026-11-12.json) and
[claim supplement](CLAIM_SUPPLEMENT_MAIN_XXV.md) record this integration; the
[Main XXIV entrypoint](archive/PI_NORMALITY_FRONTIER_MAIN_XXIV_2026-11-12.md) is preserved
byte for byte. The Main XXIV
[audit](SUCC_MAIN_XXIV_INTEGRATION_AUDIT_2026-11-11.md),
[manifest](SUCC_MAIN_XXIV_INTEGRATION_MANIFEST_2026-11-11.json), and
[claim supplement](CLAIM_SUPPLEMENT_MAIN_XXIV.md) record exact integration and
validation authority. The [Main XXIII entrypoint](archive/PI_NORMALITY_FRONTIER_MAIN_XXIII_2026-11-11.md)
is preserved byte for byte, including earlier sufficient criteria and references.

## 1. Source → exact carrier → authenticated origin

For integer $`n\ge1`$, retain the source and literal zero seed:

```math
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
```

Set $`x=\pi/16`$, $`P_n=\sum_{j=1}^n16^{-j}r(j)`$, and
$`T_n=\sum_{j\ge1}16^{-j}r(n+j)`$. The classical BBP evaluation and exact recurrence give

```math
U_n(0)=16^nP_n,\qquad U_n(0)+T_n=16^nx=16^{n-1}\pi,
\qquad 0<T_n<\frac{r(n+1)}{15}.
```

The [rational source](../observational_succ/duck_bbp.py),
[integer carrier](../observational_succ/integer_bbp_carrier.py), and
[selected orbit](../observational_succ/selected_orbit.py) retain their distinct coordinates.
For $`C_n=\lfloor U_n\rfloor`$, the literal carry is
$`\kappa_n=C_n-16C_{n-1}`$; retain carry 16 before any reduction.
The critical-carry bit in `selected_orbit` is a different observable. Original
imports are authenticated by the [frozen provenance manifest](../provenance/IMPORT_MANIFEST.json).

For seeds in the declared symbolic module $`s=a+bx`$, $`a,b\in\mathbb Q`$,

```math
U_n(s)=16^n(s+P_n),\qquad
Z_n:=16^{-n}U_n(s)-P_n=s,\qquad U_n(s)+T_n=16^n(x+s).
```

The [zero-anchor kernel](../research/2026-11-10/circle_line_lr_observer/zero_anchor_identity/THEOREMS.md)
checks exact coordinates, using imported π irrationality for uniqueness. The coherent
seed $`s=-x`$ produces a zero completed orbit but has recovered seed $`(0,-1)`$.
The rational shift $`1/16`$ aliases later phases but has seed $`(1/16,0)`$.
Authentication distinguishes both. Later circle statistics cannot distinguish the
rational alias; this is a loss of information, not a failed statistical test.
Equality in this module does not decide equality of arbitrary computable reals.

## 2. Claim status and authority

| Claim | Required treatment | Supporting domain / boundary |
|---|---|---|
| Exact four-pole BBP recurrence | **Established source contract** | Original coefficients, rational clock and literal $`U_0=0`$; [source contract](PI_FRONTIER_CONTRACT.md) |
| Geometric and BBP π identification | **Classical identity with source provenance** | Euclidean arclength and classical BBP evaluation; finite overlap of names alone is insufficient |
| Finite L/R observer productivity | **Proved within declared hypotheses** | Correct shrinking intervals and imported irrationality; unbounded integer registers |
| Complete Dedekind-cut reconstruction | **Proved within declared category** | Labelled rational probes; strict/closed and order/action distinctions retained |
| Finite-height Farey exclusion | **Proved within declared domain** | Every integer $`H\ge1`$, source-selected irrational in the initial Farey bracket |
| Symbolic zero-seed recovery | **Exact algebraic identity** | $`\mathbb Q+\mathbb Qx`$, with imported irrationality for coordinate uniqueness |
| Certified finite Weyl/Haar observations | **Finite mathematical certificates** | Exact rational intervals, paid approximation errors and branch guards |
| Source-selected signed cancellation | **OPEN** | All-large-epoch signed estimate for the actual source and zero seed is missing |
| Ladder of signed rungs, thresholds, saving–exponent law (§9) | **Proved within declared hypotheses** | Every real number, hence every seed; same-model paper proofs with one independent audit each; exact carry lemmas kernel-checked |
| R0: `limsup Re W_(B,1) < 1` (binary digit changes of π have positive lower shell density) | **OPEN** | The weakest open signed statement; its necessary restricted Diophantine exponent `< 1` is itself open for π |
| Original-zero parity balance | **OPEN** | Conditional prime balance does not bound the real complementary contrast |
| π base-16 normality | **OPEN** | Requires the all-nonzero-mode Weyl criterion below |
| Completed Weil positivity sufficient for RH | **OPEN** | Universal positivity on the valid completed test-function domain remains unproved; the classical criterion is retained |
| Riemann hypothesis | **OPEN** | Independent completed prime–Archimedean program |

“Proved” here refers to the stated paper derivations or classical imports. Finite
implementation checks and scoped Lean identities carry their own authority. No
full compiler, signed estimate or infinite theorem becomes kernel-verified by
passing native tests. Exact candidate receipts belong to the integration audit.

## 3. Identity → computational observers

Strict original-source intervals

```math
P_L<x<P_L+\frac{r(L+1)}{15\,16^L}
```

define a unique real and a computable rational cut. The
[irrational-cut formulation](../research/2026-11-10/cursed_categories_dedekind_yoneda/CUT_YONEDA_THEOREMS.md)
uses $`F_x(q)=\{*\}`$ iff $`q<x`$ on $`\mathbb Q_{\le}^{op}`$.
The [real restricted nerve](../research/2026-11-10/cursed_categorical_computation/round_iii_dedekind/DEDEKIND_YONEDA.md)
uses $`q\le x`$. They agree for irrational targets and differ at rational endpoints.
Each specified embedding is fully faithful; equivalence is onto its stated essential
image. Rational affine/projective action groupoids are separate categories.
The category of rational witnesses has its labelled colimit in the real completion,
not generally in the rational category.

The [geometric observer](../research/2026-11-10/circle_line_lr_observer/README.md)
derives rational beta and rotation sources from the Euclidean circle/line metric.
Stern–Brocot endpoint matrices $`E=\left(\begin{smallmatrix}a&c\\b&d\end{smallmatrix}\right)`$
have determinant -1; L/R updates multiply on the right by determinant-one shears.
Residual charts swap the generator convention. The conic lift respects projective
scalar classes and retains the rational metric-distortion cocycle. Geometric radians
are distinct from Fourier arguments measured in turns.

Productivity follows under imported irrationality. [Aperiodic cycle rejection](../research/2026-11-10/aperiodic_circle_observer/README.md)
additionally imports nonquadraticity; its quantitative uniform budget imports the
named transcendence measure. A strictly decreasing interval potential alone does
not imply nonperiodic output, as the retained quadratic periodic control shows.
[Height shields](../research/2026-11-10/circle_line_lr_observer/height_shield/HEIGHT_SHIELD_THEOREMS.md)
give, for each $`H`$, a finite Farey certificate and rational $`\delta_H>0`$ satisfying
$`|\pi-p/q|>\delta_H`$ for **all** reduced rationals with $`1\le q\le H`$.
Coherent finite cut restrictions reconstruct the full cut mathematically; no infinite
physical computation is asserted.

The [canonical typed compiler](../research/2026-11-10/zero_anchored_lambda_haar/COMPILER.md)
and [alternative implementation](../research/2026-11-10/zero_anchored_lambda_haar/README_ALTERNATIVE_589.md)
preserve rational source states and capture-free finite reductions. Tail contraction
is in source/observer depth. Statistical contraction is in temporal sample length
and remains OPEN. Cross-front checks cover the rational restriction of the symbolic
seed kernel; a full irrational-module-to-typed-compiler reflection theorem is
**UNVERIFIED**. Exhausted computation returns UNKNOWN/UNRESOLVED.

## 4. The canonical signed target and the Basel bridge

Let $`e(t)=\exp(2\pi i t)`$, with $`t`$ measured in turns, and $`Y_n=16^nx`$.

```math
W_{N,h}=\frac1N\sum_{n=0}^{N-1}e(hY_n),
\qquad \forall h\in\mathbb Z\setminus\{0\}:\quad W_{N,h}\longrightarrow0.
```

This all-mode criterion is equivalent to π base-16 normality. The
[Basel–Tauberian theorem](../research/2026-11-10/basel_crt_omega_phasebridge/SIGNED_BASEL_TAUBERIAN.md)
provides an exact equivalent gate. Define, for integers $`A\ge1`$,

```math
F_h(A;0)=\sum_{n=A}^{\infty}\frac{e(hY_n)}{n^2},\qquad
\omega_A=\sum_{n=A}^{2A-1}n^{-2},\qquad
B_A(h)=\frac{F_h(A;0)-F_h(2A;0)}{\omega_A}.
```

For bounded phases, signed summation by parts gives

```math
\frac1A\sum_{n=A}^{2A-1}e(hY_n)\to0
\quad\Longleftrightarrow\quad A F_h(A;0)\to0
\quad\Longleftrightarrow\quad B_A(h)\to0.
```

The original chronological two-/three-block Ω-Haar commutators supply an exact
six-frame directed-trace realization of $`F_h`$ for $`A\ge11`$, retaining the real
phase and Archimedean weight $`n^{-2}`$. Unphased Basel energy only gives
$`|F_h(A;0)|=O(1/A)`$. The needed **signed** saving is $`o(1/A)`$ for every fixed
nonzero mode. The [handoff](MAIN_XXIV_HANDOFF.md) states its quantifiers and a
weighted correlation lemma worth attacking.

The [zero-seed microscope](../research/2026-11-10/zero_seed_microscope/MICROSCOPE_THEOREMS.md)
separately measures energy over seed cylinders. Coarse depth $`K=o(N)`$ decays for
any source, even a nonnormal control. At $`K=N-o(N)`$, its energy criterion recovers
the pointwise Weyl obligation. The fixed-depth signed fingerprint is established;
its deep cumulative signed estimate is OPEN.

## 5. Sixteen-child Haar and the signed chronological CDF overlap

Put $`z_n=\{Y_n\}`$, $`\mu_N=N^{-1}\sum_{n<N}\delta_{z_n}`$ and

```math
T(z)=\{16z\},\qquad B_a(y)=\frac{a+y}{16},\qquad
C\nu=\frac1{16}\sum_{a=0}^{15}(B_a)_*\nu,\qquad Q\nu=C T_*\nu.
```

Here $`Q`$ replaces the leading digit uniformly **while retaining the full future
phase**. All sixteen children are required. It is also the average of the sixteen
translations by $`a/16`$ modulo one. $`C`$ contracts ordinary interval Wasserstein
distance by $`1/16`$; $`Q`$ is idempotent and is not a strict contraction.
Binary conditional Haar, prime-local Haar and seed-cylinder Haar are distinct tools.

With ordinary interval cost $`|u-v|`$ on $`[0,1]`$, set
$`H_\nu(t)=F_\nu(t)-F_{Q\nu}(t)`$ and $`D(\nu)=\int_0^1|H_\nu(t)|\,dt`$.
For adjacent temporal blocks of length $`M`$, use $`\mu^-_M`$ on clocks $`0\le n<M`$
and $`\mu^+_M`$ on $`M\le n<2M`$, and write $`H_\pm=H_{\mu^\pm_M}`$.
The [exact signed identity](../research/2026-11-10/zero_anchored_lambda_haar/CONSTRUCTION.md) is

```math
\Omega_M=\int_0^1\min(|H_-(t)|,|H_+(t)|)
\mathbf1_{H_-(t)H_+(t)<0}\,dt,\qquad
D_{2M}=\frac{D(\mu^-_M)+D(\mu^+_M)}2-\Omega_M.
```

This is a decomposition, not a proved all-$`M`$ overlap gain. A sufficient route would
control both the late-block defect and overlap with independently bounded vanishing
errors. Odd lengths require the weighted version: $`p=L/N`$, $`q=(N-L)/N`$,
$`L=\lfloor N/2\rfloor`$, and
$`D_N=pD_-+qD_+-2\int\min(p|H_-|,q|H_+|)\mathbf1_{H_-H_+<0}`$.
Dyadic observations alone do not pay all integer lengths.

For consecutive orbit laws, the proved endpoint-corrected reconstruction gives

```math
W_1(\mu_N,\lambda)\le\frac{16}{15}D_N+
\frac{|z_N-z_0|}{15N}.
```

The [finite backend](../research/2026-11-10/zero_anchored_lambda_haar/BACKEND_PROOFS.md)
certifies each phase inside one hexadecimal cell. At grid denominator $`q=16^k`$,
its absolute defect error is at most $`2/q`$ and overlap error at most $`4/q`$.
The [identity kernel](../research/2026-11-10/circle_line_lr_observer/zero_anchor_identity/THEOREMS.md)
also supplies rational-midpoint bounds: if each phase interval stays in one digit
chart with midpoint error $`\epsilon_n`$, then
$`|D_N-\widehat D_N|\le2N^{-1}\sum\epsilon_n`$; combine the two half-block and
whole-block errors through the displayed overlap identity. Global interval-Lipschitz
translation across a branch seam is false. Neither backend silently changes to the
circle geodesic metric. Finite exact overlap, improved precision and source-tail
contraction provide no asymptotic signed saving.

## 6. Parity, prime marginals and joining obstructions

Preserve the #572 source-clock sign
$`s_n=(-1)^{\lfloor U_n+T_n\rfloor}`$. For $`n\ge2`$ this is the parity of the
$`(n-1)`$st fractional hexadecimal digit. Its full CRT factorization is

```math
s_n=(-1)^{n+\sum_m k_{m,n}+\ell_n+\varepsilon_n}=a_nb_n,
\qquad a_n=(-1)^{k_{p_A,n}}.
```

The complement $`b_n`$ retains all other prime powers, global winding, the clock and
the real-tail boundary. In contrast, $`f(t)=(-1)^{\lfloor16\{t\}\rfloor}`$ satisfies
$`f(U_n+T_n)=s_{n+1}`$. The corresponding epoch means differ by
$`(s_{2A}-s_A)/A`$, at most $`2/A`$. Discrete digit parity is the digit-group
$`h=8`$ character, not the single smooth real character $`e(8t)`$.

With both prime-sign fibers populated, the
[two-fiber identity](../research/2026-11-09/aphex_two_fiber_haar/PROOFS.md) is

```math
\beta_A^*=\frac{u_+(A)-u_-(A)}2,\qquad
\mathbb E_A[s]=\beta_A^*+m_At_A,\qquad
|\mathbb E_A[s]-\beta_A^*|\le|m_A|.
```

Here $`u_\pm=\mathbb E_A[b\mid a=\pm1]`$, $`m_A=\mathbb E_A[a]`$ and
$`t_A=(u_++u_-)/2`$. The balanced-prime estimate remains conditional on its stated
PNT/AP, exponential-sum and completion hypotheses; the fixed-Gram statement requires
$`p\nmid h`$. It pays the prime marginal, not $`u_+-u_-\to0`$.
The [odd-eight route](../research/2026-11-09/cayley_source_observer/BOUNDARY_PROOFS.md)
plus its boundary payments is sufficient for fair parity words and is weaker than
full normality. Its source-selected premise remains OPEN.

The [3/2 ratio fiber](../research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/RATIO_FIBER_TORUS.md)
retains exact prime ratios and complete real winding. The
[2→3 joining dossier](../research/2026-11-10/basel_crt_omega_phasebridge/ratio_fiber_joinings/README.md)
constructs individually normal/Haar marginals with locked, nonproduct joint laws,
and a nonproduct joining with a selected mixed coefficient zero. Neither two Haar
marginals nor one vanishing mixed mode implies independence. A bound on this distinct
mixed fiber alone would not imply ordinary Weyl decay.

## 7. Hostile controls a proof must survive

| Control | What it rules out |
|---|---|
| Coherent same-forcing $`s=-x`$ | Source-blind decay: completed phase is zero, $`A F_h(A;s)\to1`$, $`D_N=15/32`$, $`\Omega_M=0`$ |
| Rational shift $`1/16`$ | Later phases do not authenticate a seed; reject it through $`Z_n`$ |
| Epoch-dependent p-integral PPP-08 | Identical selected prime history can have $`b=a`$, contrast 2, parity 1 and zero fitted loss |
| Factorial-sparse computable irrational | Productivity, Farey separation and complete cut identity coexist with nonnormal digits |
| Rational periodic orbits | Exact source-style computations and Fourier transport can preserve a non-Haar law |
| Positive additional-pole and matched-moment mutants | Finite samples, positive moments and bounded fixed points do not identify the original four-pole source |
| Correct local prime marginals, incorrect full winding | Prime Haar does not determine the real/CRT complement |
| Normal locked 2→3 orbits; nonproduct mixed-zero joining | Marginal uniformity and one mixed mode do not identify joint laws |
| False universal Haar contraction | Retained quantization/discrepancy controls forbid the claimed too-small remainder |
| Hexadecimal branch seams and omitted carries | Interval transport needs a common chart and complete integer lift |

The [Main XXIII archive](archive/PI_NORMALITY_FRONTIER_MAIN_XXIII_2026-11-11.md)
retains the earlier collision floors, Fejér, Galois, prime-clock, Gamma and carry
criteria with their exact references. Those tools remain available under their
original hypotheses. The [Gaussian-circle/primitive-character front](../research/2026-11-10/gaussian_circle_long_lag/README.md) supplies a
separate conditional anticlustering route; no source-attested long-lag saving is
silently imported from a geometric model.

## 8. Completed Weil remains a separate open program

The [completed prime–Archimedean packet](../research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/WEIL_PACKET_PROOFS.md)
keeps genuine prime powers, the involution $`f^\sharp(x)=x^{-1}f(1/x)`$, valid smooth
test domains and Gamma/pole terms. Ordinary positive Hilbert overlap and the signed
completed Weil quadratic form are different objects. Positivity, even when supplied
conditionally by RH, gives no source-selected off-diagonal overlap decay.
Fake composite and matched non-Euler controls remain mandatory; no nontrivial zero
positions are construction inputs. **Universal completed Weil positivity and RH
remain OPEN.** See the [RH handoff](RH_HANDOFF.md),
[typed Gamma table](MAIN_XXII_GAMMA_OBSERVABLES.md), and
[Main XXIII tool atlas](MAIN_XXIII_TOOL_ATLAS.md).

## 9. Main XXV: the ladder below the canonical target

The statements of this section hold for **every real number** `ξ` (so for every seed and
every source completing to it). They prove nothing about π's statistics. Proofs,
falsifiers and audits: [innovation × arithmetic decoupling](../research/2026-11-11/innovation_arithmetic_decoupling/README.md)
(IAD, SWT, ZSC) and [frontier rungs](../research/2026-11-12/frontier_rungs/README.md) (LMF, RDT).

**Shell means and limit measures.** With $`z_n=\{16^n\xi\}`$ and integers $`B\ge1`$, put

```math
W_B(h)=\frac1B\sum_{n=B}^{2B-1}e(hz_n),\qquad
\nu_B=\frac1B\sum_{n=B}^{2B-1}\delta_{z_n},\qquad
M(\xi)=\{\text{weak-* limit points of }(\nu_B)\}.
```

$`M(\xi)`$ is nonempty, compact, connected, consists of $`\times16`$-invariant measures and
depends only on the completed point; normality is $`M(\xi)=\{\lambda\}`$ (LMF-01). A real
saving at mode $`h`$ on all large shells is the exclusion from $`M(\xi)`$ of the invariant
measures on periodic points $`p`$ with $`hp\in\mathbb Z`$ (LMF-02).

**The ladder** (LMF-03; every implication is strict, with explicit witnesses):

| Rung | Signed form | Digit form |
|---|---|---|
| R0 | $`\limsup_B\operatorname{Re}W_B(1)<1`$ | binary digit changes have positive lower shell density |
| R1 | $`\limsup_B\lvert W_B(1)\rvert<1`$ | no shell limit is a single fixed-point mass |
| (CH) | $`\limsup_B\operatorname{Re}W_B(15)<1`$ | hexadecimal digit changes $`d_n\ne d_{n+1}`$ have positive lower shell density |
| (CH$`_k`$) | $`\limsup_B\operatorname{Re}W_B(16^k-1)<1`$ | $`d_n\ne d_{n+k}`$ with positive lower shell density |
| normality | $`W_B(h)\to0`$ for all $`h\ne0`$ | — |

normality ⟹ (CH$`_k`$) ⟹ (CH) ⟹ R1 ⟹ R0. For the literal zero seed, (CH) is also a statement
about the literal carries $`\kappa_n`$ (ZSC-03). **For π all rungs are OPEN.**

**Thresholds in the canonical units of §5** (LMF-04, LMF-05; interval cost on $`[0,1]`$,
$`D(\nu)=W_1(\nu,Q\nu)`$):

```math
\limsup_B D(\nu_B)<\tfrac14\ \Rightarrow\ \text{R1},\qquad
\limsup_B D(\nu_B)<\tfrac1{60}\ \Rightarrow\ \text{(CH)},\qquad
\limsup_B D(\nu_B)<\tfrac1{4(16^k-1)}\ \Rightarrow\ (\text{CH}_k),
```

and the same with $`W_1(\nu_B,\lambda)`$ in place of $`D(\nu_B)`$; for prefixes,
$`\limsup_ND_N<15/256`$ implies R1 and $`\limsup_ND_N<1/256`$ implies (CH). The constants $`1/4`$
and $`1/60`$ are sharp for shells. The coherent control has $`D=15/32`$. Thresholds are
sufficient conditions; a finite set of shells below a threshold is not evidence.

**Necessary Diophantine cost** (ZSC-01, ZSC-02, LMF-03). A real saving $`\eta`$ at one mode
on all large shells forces

```math
\lVert16^m\xi\rVert\ \ge\ c\,16^{-\frac{2-\eta}{2+\eta}m}\qquad(m\ge m_0),
```

a restricted exponent strictly below 1 at the denominators $`16^m`$. No bound on the
irrationality exponent can supply it ($`v_{16}\le\mu-1`$, $`\mu\ge2`$): an unrefereed claim
$`\mu(\pi)=2`$, even if correct, yields no saving. The refereed record is
$`v_{16}(\pi)\le6.1033`$. The cost is necessary, not sufficient: explicit points have
$`v_{16}=0`$ and no saving. For algebraic irrationals the cost is paid (Ridout, ineffective)
and a positive density of digit changes is still not known.

**Restricted exponents** (RDT). From a linear form $`A\xi-B=I`$ the bound at denominators
$`g\,b^m`$ beats the unrestricted bound of the same form exactly by the $`b`$-adic imbalance
of $`A`$ over $`B`$. Rivoal (2007, import) gives
$`v_{16}(\log(16/15))\le0.8813`$; $`\log(16/15)=\sum_{n\ge1}16^{-n}/n`$ is a proper
zero-seeded element of the seven-dimensional period space $`V`$ of the source class
(ZSC-06), and the local extension to $`15\cdot16^m`$ gives a digit change in every large
shell for that element. For π, the families examined show no gain (observed), and the
effective base of the relevant logarithm series is $`\sqrt2`$ (the BBP point
$`x=(1\pm i)/2`$, $`|x|=2^{-1/2}`$) against the $`\ge12`$ used by the import. Not claimed:
that $`v_{16}(\pi)<1`$ is false.

**Source moduli** (ZSC-06). Sources $`(g,s)`$ with the gauge
$`(g-(16-z^8)h,\ s+\int_0^1h)`$ share the completed point and all phase statistics; seed,
poles, literal carries and seam are not gauge-invariant. In proper form the zero seed says
exactly that $`\pi/16\in V`$. A fixed zero-seeded rational source with positive
$`O(n^{-2})`$ forcing and complete census is coherent on every shell: no transfer using
only those properties can work.

**Kernel authority.** Thirty-three exact statements behind ZSC-02 (locality lemma), ZSC-03
(renewal lemma) and ZSC-06 (null relation) are checked in Lean 4.14.0 against the pinned
mathlib, with nine refuted mutants. No statistical or asymptotic statement is
kernel-checked.

Additional hostile controls a proof must survive: points with $`v_{16}=0`$ on the wrong
side of each rung (LMF-03); the two-digit run point (R1 holds, (CH) fails); the lift $`1`$
of the fixed point $`0`$ on the interval (the error in a provisional threshold of this
round); the null source and the hostile source of ZSC-06.

Resume with the [Main XXV handoff](MAIN_XXV_HANDOFF.md) and, for the full signed theorem,
the [Main XXIV handoff](MAIN_XXIV_HANDOFF.md): prove a genuinely source-derived signed
bound with all integer-epoch and all-mode quantifiers.

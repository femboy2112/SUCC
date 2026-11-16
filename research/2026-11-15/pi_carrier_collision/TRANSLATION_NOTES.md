# Translation and provenance: randomized readout of the selected BBP phase

**2026-11-15. Bounded translator audit; no scholarly priority claim.**

Local parent: `85a14bb68aeae31d3a2796350529fda9a5c39072`, branch
`research/pi-carrier-collision-2026-11-15`. The source and open arithmetic
target are frozen in [HOLE_CONTRACT.md](HOLE_CONTRACT.md). This note owns no
production implementation and does not report a full-suite run.

The concurrent donor [PR #640](https://github.com/femboy2112/SUCC/pull/640)
was read through the GitHub connector at the exact unmerged head
`9dc78d8e999f8c53b5a87c95363b5f99ec21bb4e`. Its theorem file has Git blob
`729338cefc069c9f2d4996540338a50d9bb5a165`; its module has blob
`c594c39dbc02ee26633ba5e1bec69634489f2fe5`. PR metadata reports tests;
those tests were not executed in this audit. The donor was not merged or
silently treated as an ancestor.

## 1. Findings that survive the source boundary

1. A known Gamma phase channel has a nonzero complex multiplier at every
   finite positive depth and finite real frequency. Retaining its clock
   gives samplewise phase compensation. Discarding the clock gives an
   unbiased inverse with a calculable variance penalty. This is a
   measurement theorem, not an arithmetic cancellation theorem.
2. The principal's proposed integer two-tap echo retains the selected BBP
   phase exactly. Independent Gamma–Poisson tap indices can generate a
   well-conditioned finite readout frame, provided the original forcing
   nodes have the stated separation. The exact matrix concentration
   theorem and its constants are given below.
3. Such frame conditioning holds for every phase vector, including the
   same-forcing coherent counterseed. It authenticates stable recovery,
   not normality. The observed signed outputs remain necessary.
4. The inherited global branch coercivity theorem already supplies an
   eventual positive detection probability of order `1/m` on an octave-
   style block `(m,8m]`. Fresh repeated trials amplify this to high
   probability with order `m` trials. The resource growth is the reason
   this does not prove the still-open fixed relative saving R0.
5. The Gamma–Poisson law is classical and already appears in SUCC. Its use
   as an explicitly chosen detector law is legitimate. Identifying it
   with an unrelated original source joint law is already refuted in the
   archive.

## 2. Repository ancestry that must be credited

| Source inspected | Inherited result | Boundary for this round |
| --- | --- | --- |
| [PI_NORMALITY_FRONTIER.md](../../../docs/PI_NORMALITY_FRONTIER.md), especially §§1–6 and 9 | The actual signed rungs R0, R1, CH and normality; strict separation of the rungs; source-zero selection | Their signed estimates remain OPEN. A detector is not the estimate it observes. |
| [PI_FRONTIER_CONTRACT.md](../../../docs/PI_FRONTIER_CONTRACT.md) | Literal four-pole recurrence, zero anchor, Green-tail transfer, collision and spectral gates, selected-likelihood warnings | A phase-free Gram or a comparison law does not replace selected phases. |
| [SIGNED_GAMMA_BBP_GREEN_COHERENCE.md](../../2026-10-25/SIGNED_GAMMA_BBP_GREEN_COHERENCE.md) | The original raw/completed Weyl sums differ by a bounded fixed-frequency error | The completion transports the signed target; it does not supply decay. |
| [OILY_LOG_CLOCK_HILBERT_TRANSPORT.md](../../2026-10-26/OILY_LOG_CLOCK_HILBERT_TRANSPORT.md), LOC-3–4 | An existing source-to-Hilbert signed transport with an explicit all-frequency `O(N^(-1/3))` comparison error | Even a faithful quantitative transport may leave precisely the original signed saving unpaid. |
| [GLOBAL_BRANCH_COERCIVITY.md](../../2026-10-27/GLOBAL_BRANCH_COERCIVITY.md), GB-1 and GB-12 | Eventual fixed absolute loss on `(m,8m]`; logarithmic absolute loss for prefixes; original zero selector is essential | No numerical global onset was extracted. Relative loss tends to zero in the proved prefix bound. |
| [FOUR_POLE_ATOMIC_SUBSTRATE.md](../../2026-10-26/FOUR_POLE_ATOMIC_SUBSTRATE.md), §9, “A Gamma–Poisson identity does not authenticate a joint law” | The original grade/latent limit has mixed moment `4`, while the auxiliary Gamma–Poisson coupling has mixed moment `6` | Equality of marginal transforms does not authenticate a conditional source law. |
| [UNIVERSAL_N_PASCAL_GAMMA_ZETA.md](../../2026-10-30/universal_n_carrier/UNIVERSAL_N_PASCAL_GAMMA_ZETA.md), UN-03 | A separately declared Bernoulli count probe on the authentic latent variable has a Gamma–Poisson limit | This probe is different from the original fixed Oily grade. The observation law must be stated. |
| [gamma_volume/THEOREMS.md](../../2026-11-14/gamma_volume/THEOREMS.md), GV-04 | Exact Gamma subordination and negative-binomial coefficient semigroup, including a finite-tail certificate | The mixing identity is inherited. A new echo/frame interface must preserve the arithmetic source and its orientation. |
| [Donor #640 theorem file](https://github.com/femboy2112/SUCC/blob/9dc78d8e999f8c53b5a87c95363b5f99ec21bb4e/research/2026-11-14/haar_gamma_entanglement/THEOREMS.md), HGE-02–07 | Inverse propensity identity, hidden complex Bell-sector coherence, Gamma phase attenuation, complementary quadratures, recorded conditioning and no-signalling | The declared two-qubit source is not the arithmetic BBP carrier. The reusable character identity needs an explicit classical source map. |

The original source is

\[
 U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Write `e(x)=exp(2πix)` and `z_n=e(hU_n)`, with fixed nonzero integer `h`.
For an arbitrary initial seed `s`, the same recurrence is denoted `U_n(s)`.
The selected phase is `s=0`; statements valid for every seed cannot by
themselves distinguish that selection.

## 3. Exact donor translation and a quantitative inverse

### 3.1 What the donor actually establishes

HGE-04 acts on the separately declared two-qubit sector

\[
 \rho_\gamma=\tfrac12(|00\rangle\langle00|+|11\rangle\langle11|
 +\gamma|00\rangle\langle11|+\bar\gamma|11\rangle\langle00|),
 \qquad |\gamma|\le1.
\]

The one-sided phase `diag(1,exp(iωt))` maps its coherence to
`γ exp(-iωt)`. Averaging `t~Gamma(α,rate 1)` gives
`γ(1+iω)^(-α)`. HGE-03 fixes the readout signs:
`<XX>=Re γ`, `<XY>=-Im γ`. At `α=2,ω=1`, the multiplier is `-i/2`:
the zero XX quadrature is a phase rotation, not zero complex coherence.
An opposite phase on the other subsystem preserves this marked sector.

The inverse below is algebraic inference on a declared signal. It is not
a completely positive inverse channel on arbitrary quantum states, nor a
physical entanglement-distillation protocol. The donor's source and
instrument separation should be retained verbatim in substance.

### 3.2 A classical source-preserving version

**Domain.** Let `α>0`, `λ>0`, `ω` real, and let a known source signal satisfy
`|z|=1`. Independently choose `T~Gamma(α,rate λ)` and observe the complex
report `Y=z exp(-iωT)`. Euler's integral gives, on the principal branch,

\[
 m=\mathbb E e^{-i\omega T}=(1+i\omega/\lambda)^{-\alpha},\qquad
 |m|=(1+(\omega/\lambda)^2)^{-\alpha/2}>0,
 \quad \arg m=-\alpha\arctan(\omega/\lambda)\pmod{2\pi}.
\]

The principal power is unambiguous because `1+iω/λ` lies in the open right
half-plane. If the clock is measured as a shift of a circle coordinate in
`e(hx)`, then `ω=2πh`; the factors of `2π` must not be dropped. At depth
zero the limiting law is `δ_0` and `m=1`. Negative depth is outside this
probability model.

**Recorded clock.** `exp(iωT)Y=z` samplewise. If only a clock estimate
`T_hat` with `|T_hat-T|≤d` is retained, then

\[
 |e^{i\omega\widehat T}Y-z|\le\min(2,|\omega|d).
\]

A separate source-coordinate error `|U_hat-U|≤ε` contributes at most
`min(2,2π|h|ε)`. These are deterministic continuity bounds, not a claim
that the necessary sensor precision is automatically available.

**Discarded clock.** `Y/m` is unbiased for `z`, with exact complex variance

\[
 \mathbb E|Y/m-z|^2=|m|^{-2}-1.
\]

For `N` deterministic phases, one fresh independent clock per phase gives
an unbiased estimator of `W_N=N^(-1)Σz_n` with mean squared error
`(|m|^(-2)-1)/N`. If each trial instead chooses a fresh uniform index
from a fixed block of `B` phases, the one-trial variance is
`|m|^(-2)-|W_B|^2`, and `M` independent trials divide it by `M`.

For either independent bounded-report construction, applying the scalar
bounded-variable inequality separately to the two quadratures gives

\[
 \Pr(|\widehat W-W|\ge\epsilon)
 \le4\exp[-M|m|^2\epsilon^2/4].
\]

The constants here are deliberately conservative. With a calibrated
multiplier estimate `m_hat≠0` and an observed averaged report `y_hat`
satisfying `|y_hat-mW|≤ε`, the deterministic inverse error is

\[
 |y_{\rm hat}/m_{\rm hat}-W|
 \le\frac{\epsilon+|m_{\rm hat}-m|}{|m_{\rm hat}|},\qquad |W|\le1.
\]

For parameters growing with the horizon, clock-discarding consistency
requires control of this inverse condition number. In the one-clock-per-
point model, `N|m_N|^2→∞` is a sufficient condition for mean square
consistency. If `|m_N|→0`, the locked sequence `z_n=1` has attenuated mean
`m_N→0` despite possessing no arithmetic cancellation at all.

### 3.3 Adaptive sampling remains a calibrated observation problem

On a fixed finite block of `B` source phases, let the next index `I_j` have
positive history-predictable probabilities `π_j(i)`. A fresh clock,
conditionally independent of the selected source phase, yields

\[
 X_j=\frac{z_{I_j}e^{-i\omega T_j}}{B\pi_j(I_j)m},\qquad
 \mathbb E[X_j\mid\mathcal F_{j-1}]=W_B.
\]

Thus `Σ(X_j-W_B)` is a complex martingale for this declared experiment.
Its conditional second moment is exactly

\[
 \mathbb E[|X_j|^2\mid\mathcal F_{j-1}]
 =\frac1{B^2|m|^2}\sum_i\frac1{\pi_j(i)}.
\]

For full complex unit-modulus phase reports with equal query costs, uniform
sampling minimizes this second moment by Cauchy–Schwarz. Attraction-based
sampling does not create a variance gain for this particular target merely
by revisiting preferred phases. Different costs, available information or
scalar targets would be different designs. Zero support loses general
identifiability, and copied observations do not constitute fresh
martingale differences. Time-uniform confidence claims need an actual
martingale bound, not a fixed-sample interval inspected repeatedly.

## 4. Audit of the principal's Gamma–Poisson echo frame

This section checks the announced mathematical interface. It is not an
audit of a production implementation that did not yet exist when these
calculations were made.

### 4.1 Integer taps preserve the target

Let `K` be a nonnegative integer random tap, independent of the fixed
arithmetic source. The exact two-tap identity is

\[
 e((h-16K)U_n+KU_{n+1})
 =z_n e(Kr(n+1)).
\]

Both tap coefficients are integers, so the echo is a well-defined
character of the two circle observations. A raw real Gamma variable is
not an integer tap; Poissonization is a separately specified way to
obtain one. The identity holds for every seed, while retaining its phase
when `h≠0`. Setting `h=0` deletes that phase.

Declare `T~Gamma(2,scale Λ)` and `K|T~Poisson(T)`, with `Λ>0`. Then

\[
 \mathbb E z^K=[1+\Lambda(1-z)]^{-2},\quad |z|\le1,
 \qquad\Pr(K=k)=(k+1)p^2q^k,
 \quad p=\frac1{1+\Lambda},\ q=\frac\Lambda{1+\Lambda}.
\]

This is an externally chosen probe law. It is not asserted to be the
intrinsic joint law of the original BBP arithmetic trajectory or the
original Oily grade. The provenance distinction in §2 is load-bearing.

### 4.2 Population Gram and separation

For distinct known nodes `t_1,...,t_B` in a real interval of length at most
`1/2`, suppose `|t_n-t_m|≥d|n-m|` after their monotone ordering, with
`d>0`. Set the row vector `v(K)=(e(Kt_1),...,e(Kt_B))` and
`G=E[v(K)^*v(K)]`. Then

\[
 G_{nm}=[1+\Lambda(1-e(t_m-t_n))]^{-2},\qquad G_{nn}=1.
\]

For `Δ=t_m-t_n`, direct expansion gives

\[
 |G_{nm}|=\frac1{1+4\Lambda(1+\Lambda)\sin^2(\pi\Delta)}
 \le\frac1{1+16\Lambda(1+\Lambda)d^2|n-m|^2}.
\]

The last inequality uses `|Δ|≤1/2`; separation must be measured on the
circle if that hypothesis is removed. Summing the off-diagonal row and
using `Σj^(-2)=π²/6` gives

\[
 \|G-I\|_{\rm op}\le\eta_0
 :=\frac{\pi^2}{48\Lambda(1+\Lambda)d^2}
 <\frac1{4\Lambda(1+\Lambda)d^2}.
\]

Any upper bound `η<1` therefore yields
`(1-η)I≤G≤(1+η)I`. The original nodes proposed by the principal are
`t_n=r(n+1)` on a finite shell. Establishing their uniform `d` is a
source-specific elementary calculation, not supplied by matrix
concentration. Their scale `d` of order `B^(-3)` calls for `Λ` of order
`B^3` at fixed frame margin. No conclusion about signed `z_n` was used.

### 4.3 Fresh sampled rows: exact application of matrix Chernoff

Take `s` independent copies of `K` and put `F_{jn}=e(K_jt_n)/sqrt(s)`.
Whiten the rank-one summand:

\[
 X_j=G^{-1/2}v(K_j)^*v(K_j)G^{-1/2},\qquad
 \mathbb E X_j=I,\qquad
 0\le X_j\le\frac{B}{1-\eta}I.
\]

The last bound follows from `||v||²=B` and the lower bound on `G`.
Tropp's matrix Chernoff theorem, followed by the elementary scalar
estimates for its exponential brackets, gives, for `0<ε<1`,

\[
 \Pr\!\left(
 \left\|\frac1s\sum_jX_j-I\right\|_{\rm op}>\epsilon
 \right)
 \le2B\exp\!\left[-\frac{s\epsilon^2(1-\eta)}{3B}\right].
\]

Consequently, for `0<δ<1`, it suffices that

\[
 s\ge\frac{3B}{(1-\eta)\epsilon^2}\log\frac{2B}{\delta}
\]

to obtain, with probability at least `1-δ`,

\[
 (1-\epsilon)G\le F^*F\le(1+\epsilon)G,
 \qquad
 \kappa(F)\le
 \sqrt{\frac{(1+\epsilon)(1+\eta)}{(1-\epsilon)(1-\eta)}}.
\]

This applies to complex Hermitian rank-one matrices. Independence is
across sampled rows, not across the `B` coordinates of a row. Unbounded
`K` is permitted because row norm is always `sqrt(B)`. Reusing one clock
`s` times has rank at most one and is a decisive negative control for
`B>1`.

If complex observations are `y=Fz+e`, least squares gives

\[
 \|\widehat z-z\|_2
 \le\frac{\|e\|_2}{\sqrt{(1-\epsilon)(1-\eta)}},\qquad
 |B^{-1}\mathbf1^*(\widehat z-z)|
 \le\frac{\|e\|_2}{\sqrt{B(1-\epsilon)(1-\eta)}}.
\]

If the instrument instead reports `B^(-1)Σ_n z_ne(K_jt_n)`, its raw
readout errors must be multiplied by `B/sqrt(s)` before using the above
normalization. Conditioning does not remove that measurement cost.
Complex quadratures, not just squared magnitudes of reports, are the
input of this linear inverse. An intensity-only instrument is a different
phase-retrieval problem.

### 4.4 Finite tap and precision budgets

For integer `M≥0`, summing the geometric tail gives the exact formula

\[
 \Pr(K>M)=q^{M+1}[1+(M+1)p].
\]

The probability that any of `s` independent taps exceeds `M` is at most
`s` times this quantity. A simpler sufficient bound follows from
`E[(1+1/(2Λ))^K]=4`:

\[
 \Pr(\max_jK_j\ge M)
 \le4s(1+1/(2\Lambda))^{-M}.
\]

This bounds an event for the original probe distribution. Truncating or
rerolling large taps changes the distribution and its population Gram;
that change requires an additional error estimate.

If the two source coordinates are measured separately with absolute
errors `ε_n,ε_(n+1)`, the echo's complex error is at most

\[
 \min\{2,\ 2\pi[(|h|+16K)\epsilon_n+K\epsilon_{n+1}]\}.
\]

A common error propagated through an exactly imposed recurrence can have
different cancellation; it must not be substituted for independent sensor
errors. The number of sampled rows, maximum frequency, source-coordinate
precision and coherent-sum readout cost are separate resources.

### 4.5 Why this is not artificial evidence for normality

The source-labelled row is `v(K) diag(z_1,...,z_B)`. Its population Gram
is a unitary diagonal conjugate of `G`, with exactly the same spectrum.
The frame is therefore equally conditioned for locked phases, periodic
phases, and the genuine same-forcing counterseed `U_n(-π/16)=-T_n`.
That is expected for a stable observation interface. It is fatal to an
inference from frame conditioning alone to signed phase cancellation.

Forgetting `K` discards the calibrated design labels required by this
inverse. Averaging such unlabelled outputs can attenuate every source.
No amplification claim may treat that attenuation as evidence that the
original `B^(-1)Σz_n` was small. Likewise the zero-seed identity must be
authenticated separately: late circle phases cannot distinguish the
rational alias seed `1/16` from zero, although the unwrapped seed extractor
can.

## 5. A genuine weaker detector from inherited signed arithmetic

The source-selected GB-12 theorem supplies an integer `m_2≥4096` such that

\[
 \left|\sum_{n=m+1}^{8m}e(hU_n)\right|<7m-\frac1{14}
 \quad(m\ge m_2,\ 1\le|h|\le m^2/64).
\]

Its proof uses the published irrationality bound `μ(π)<15/2`, the original
four-pole recurrence and the zero initial condition. The inherited proof
does not provide a numerical value of `m_2`. The following is an elementary
probabilistic corollary, not an improved arithmetic estimate.

Choose a fresh uniform `I` from `{m+1,...,8m}` and then a fresh independent
coin whose conditional hit probability is

\[
 p_I=\frac{1-\cos(2\pi hU_I)}2.
\]

The mean hit probability satisfies

\[
 \bar p_m=
 \frac{7m-\operatorname{Re}\sum_{n=m+1}^{8m}e(hU_n)}{14m}
 >\frac1{196m}.
\]

Thus `M` independent trials miss with probability at most
`exp(-M/(196m))`. For any `0<δ<1`,

\[
 M=\left\lceil196m\log(1/\delta)\right\rceil
\]

suffices for detection probability at least `1-δ`, at every scale within
the theorem's domain. This experiment assumes access to the declared coin
probability, through exact source computation or a certified readout and
coin implementation. Finite precision changes that probability and must
be charged.

The same-forcing counterseed has `U_n=-T_n` with
`0<T_n<1/(64n²)`. Since `1-cos x≤x²/2`, its mean hit probability obeys

\[
 \bar p_m^{\rm counter}
 \le\frac{\pi^2h^2}{4096(m+1)^4}.
\]

By a union bound its probability of any hit in `M` trials is at most
`Mπ²h²/[4096(m+1)^4]`. For fixed `h,δ` and the above linear trial budget
this tends to zero as `m^(-3)`. A completely locked zero phase gives no
hits. A periodic nonnormal phase can give many hits, so this test rejects
coherence and is not a general normality discriminator.

R0 would instead supply a fixed positive per-trial rate on every
sufficiently large dyadic shell, allowing a scale-independent trial
budget for fixed confidence. That premise is not proved here. Copying one
successful report does not implement repeated independent trials. The
unknown onset must also remain visible in any executable budget.

## 6. Orthogonal routes and where their arithmetic obligation remains

| Candidate detector | Exact useful output | Remaining obligation |
| --- | --- | --- |
| Adaptive inverse propensity / martingale | An unbiased estimator of a fixed selected finite-block statistic, and confidence bounds under actual boundedness/variance assumptions | A finite confidence interval does not prove the statistic's all-scale bound. |
| Twisted transfer operator | A contractive norm can bound selected signed sums if the source belongs to its controlled class and all boundary functionals are controlled | A spectral statement for a reference distribution does not place the fixed π orbit in that class. The source membership is often the hidden original problem. |
| Positive kernel, Riesz-style product or collision majorant | A valid exact upper/lower comparison after retaining the selected phase, scale and normalization | Positivity or small randomized ensemble mean is not a source-specific signed saving. The existing prescribed collision gates in the frontier remain open. |
| Gamma echo frame | Stable finite recovery of the original source phase vector from labelled complex reports | Recovering the vector does not establish an asymptotic signed estimate for it. |
| GB-12 repeated hit test | High-probability detection with a growing trial budget and a genuine zero-source versus counterseed separation | A uniform positive relative hit density remains an additional arithmetic premise. |

No new Riesz-product or transfer-operator theorem is asserted here. The
bounded search did not identify a source-faithful estimate beyond the
explicit weaker GB-12 corollary. Bailey–Crandall already expresses the
normality issue through a zero-initial rationally perturbed expanding
map. Rephrasing that orbit as a random experiment does not discharge its
equidistribution hypothesis.

## 7. Live primary-source audit

The following sources were opened during this round. Formula applications
and error bounds in §§3–5 are derived above; they are not attributed as
new theorems to these authors.

| Primary / official source | Verified location and supported claim |
| --- | --- |
| [NIST DLMF §5.9.1](https://dlmf.nist.gov/5.9#E1) | Euler integral with `Re ν>0`, `μ>0`, `Re z>0`, principal fractional powers. Setting `μ=1`, `ν=α`, `z=λ+iω` proves the Gamma multiplier. This is an official reference, not a novelty source. |
| [Joel Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*, arXiv:1004.4389v7](https://arxiv.org/pdf/1004.4389) | Theorem 1.1 and Corollary 5.2: independent positive semidefinite self-adjoint summands, a uniform eigenvalue bound, multiplicative upper/lower tails. Remark 5.4 explicitly applies the theorem to independent vectors in `C^m` and their rank-one Gram summands. These are the exact hypotheses used in §4.3. |
| [Bailey–Borwein–Plouffe, *On the Rapid Computation of Various Polylogarithmic Constants*](https://www.davidhbailey.com/dhbpapers/digits.pdf) | Theorem 1, equation (1.2), PDF p.3: the original four coefficients and denominators in the base-16 π series. This authenticates the source formula, not its digit statistics. |
| [Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf) | Hypothesis A, PDF p.2: zero-initial rational-polynomial perturbations of an expanding radix map; the finite-attractor/equidistribution alternative is a hypothesis. Theorem 3.1, PDF pp.9–10, separately proves the rationality/finite-attractor equivalence under its stated rational-function conditions. |
| [Howard–Ramdas–McAuliffe–Sekhon, *Time-uniform, nonparametric, nonasymptotic confidence sequences*](https://arxiv.org/pdf/1810.08240) | Introduction, equation (1): simultaneous coverage over all observation times; the surrounding discussion explains why repeatedly inspecting fixed-sample intervals is not that guarantee. This supports the sequential-inference boundary, not an asserted bound for an unspecified adaptive experiment. |
| [Horvitz–Thompson, *A Generalization of Sampling Without Replacement from a Finite Universe*](https://doi.org/10.1080/01621459.1952.10483446) | Publisher metadata and abstract verified: unequal-probability finite sampling and unbiased variance estimation. Full article text was not used here; the elementary conditional expectation in §3.3 is proved directly. |
| [Zeilberger–Zudilin, corrected author manuscript](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/pimeasNew.pdf) and [version record](https://arxiv.org/abs/1912.06345) | The published bound `μ(π)≤7.103205334137…<15/2` supplies more than the coarse input needed by inherited GB-12. The arXiv record explicitly identifies v2's corrected Lemma 2. This note does not claim this is the current best bound; later search results are not needed for the implication. |

For the principal's own citation verification, retrieval references from
this audit were: DLMF `turn98view2`; Tropp `turn99view0`, `turn100view0–2`;
BBP `turn99view1`; Bailey–Crandall `turn98view0`, `turn100view3`; Howard et
al. `turn98view1`; Horvitz–Thompson publisher `turn102search5`;
Zeilberger–Zudilin `turn106view0`, `turn105view0`. These tool reference
labels are retrieval aids, not evidence additional to their underlying
sources.

## 8. Bounded verdict and next falsification

**Disclosed within the stated models:** Gamma character/inverse identities;
the source-retaining integer echo; the separated-node population Gram
bound; the finite independent-row Chernoff application; the GB-12 hit-test
corollary. The frame section is conditional on the separately certified
source node gap and declared complex readout access. No new source
distribution, physical interaction or quantum resource is inferred.

**Still open:** any new all-scale selected signed saving, R0, π base-16
normality and a physical BBP-to-quantum instrument identification.

**Priority:** Gamma transforms, negative-binomial mixing, inverse
probability weighting, Chernoff concentration and repeated-trial
amplification are classical. The repo already contains each relevant
structural ingredient listed in §2. The candidate addition is a concrete
source-faithful finite echo/frame interface with explicit resource and
error accounting; scholarly novelty has not been established.

**Next discriminating controls:** apply the same labelled frame to the
genuine zero-seeded source, the same-forcing counterseed and a locked
phase vector. All should preserve the predicted conditioning, while the
recovered signed outputs remain different. Delete the clock labels,
reuse one clock as multiple rows, omit one quadrature, reverse the
character orientation, or change a BBP channel. Each mutation should
break the specific claimed interface or trigger its declared error,
rather than being accepted as apparent arithmetic cancellation.

## 9. Independent finite audit and bounded paper review

The standalone [independent_audit.py](independent_audit.py) imports no SUCC
production module. Its replay is

```sh
python research/2026-11-15/pi_carrier_collision/independent_audit.py \
  --output research/2026-11-15/pi_carrier_collision/receipts/translator_independent.json
```

The saved [raw receipt](receipts/translator_independent.json) reports
**6,622 exact finite checks, PASS**, using Python 3.12.14. It records actual
version data, script/input hashes, all declared case bounds and exact
rational census probabilities. The elapsed-time field is diagnostic; no
floating-point mathematical comparison is used. The receipt explicitly
lists the inherited universal inputs that this script does not re-prove.

The controls comprise 800 rational budget configurations; five complete
binomial count censuses with plus probabilities `1/2,2/3,3/4,1/4,7/8` and
row counts `43,64,86,86,171`; copied-row rank failure; four exact Hadamard
normalization controls; 198 Gamma multiplier comparisons between repeated
rational division and binomial expansion; 594 Gamma semigroup fixtures;
312 negative-binomial tail and character enclosures; four exact rational
population Grams checked by principal minors; 480 literal source echo
identities; deleted-channel argument controls; and rational GB-12 dose
accounting at five declared scales. Its GB cases retain the condition
`m≥m_2`; selecting `m=4096` in a budget fixture does not certify the unknown
arithmetic onset.

Script SHA-256:
`2ea8dfcd55402b5334e8d9739f30b5a8c1acae7bfe0cc685980489b063c1f521`.
Initial raw receipt SHA-256:
`ba7c1f3919beaa02147046fb69b51c4261a94b111dac29a71e1db6a6e207befc`.
A rerun changes the elapsed-time field and therefore may change the receipt
hash while preserving the exact mathematics.

The production module
`observational_succ/random_probe_frames.py`, SHA-256
`6f0a90443e7b201c56422dd9c55bd07082b45d52c40d5440c6fa03f7a1c2a047`,
and its tests, SHA-256
`c5b5379ed2aedb5785a9475f918a08bd72f00a3d583887f80af2ffcf5719bdff`,
were read without editing. **Static bounded PASS:** the independent-row
model, whitening constant, binary logarithm ceiling, rational failure
bound, Gram versus matrix condition numbers, and both RMS noise factors
agree with the derivations above. This is not a claim to have executed
their unit tests; the independent script is the run reported here.

The initial paper review read PC-01–10 at theorem SHA-256
`6040127220b34084f1d401d2ebb4b0e619c7b078bae52a8e55272690fdbc121b`.
The assigned mathematical regions PC-03, PC-04, PC-06 and PC-09 passed:
external Gamma law versus original Oily law; complex Gram orientation;
independent-row Chernoff; the summable `1/[B(B+1)]` all-scale failure
allocation; the `1/B_0` union tail without cross-scale independence;
temporal Haar versus source-coordinate Haar; phase-sensitive reference
difference; the inherited constant `1/(196m)`; and the fixed-`h`
`O_h(log(m)/m^3)` counterseed false-hit bound.

Three wording clarifications were returned to the principal: explicitly
fix `η≤1/4,ε=1/2` when the all-scale event refers to the numerical frame
bounds `(3/8,15/8)`; state that the raw response vector must be divided by
`sqrt(s)` when writing it as `Ac/B`; and specify `h=1` when calling the
reference-difference statistic equivalent to R0. For a general fixed
integer `h`, a positive lower bound still implies R0 through
`1-cos(hθ)≤h²(1-cos θ)`, but the equivalence is to its own oriented
mode statistic. These requests do not change the validated equations.

**Refreshed bounded paper PASS.** The principal incorporated all three
clarifications. The reviewed theorem file now has SHA-256
`0552a45d0b2a6d3fe8537b13ea06d5e07d5984339f3a8e9cc745a7ea70a97334`:
PC-04 explicitly fixes the recommended `η,ε`; PC-06 defines the scaled
response and least-squares estimator; and its R0 equivalence explicitly
uses `h=1`. No unresolved defect remains in the assigned PC-03/04/06/09
validity review. This refresh is a paper read, not an additional experiment
or an independent source of evidence beyond the derivations and receipt
already described.

**Final uniform-margin refresh — bounded PASS.** The current theorem file
has SHA-256
`03938f2d19125d214ad2e517982365d4f73f33fe8a264a6ef3278741d3021e1b`.
PC-06 now explicitly assumes a family with `η≤η_*<1` for its across-scale
R0 equivalence, and retains `h=1`. This supplies exactly the needed
uniform constants: `A_B≥a>0` implies
`B D_B≥2(1-η_*)a`, while `B D_B≥b>0` implies
`A_B≥b/[2(1+η_*)]`. The finite-scale identities and the other reviewed
conclusions are unchanged. This was a narrow paper read; no experiments
were rerun and no production file was changed.

# Observer-headed causal Yoneda pinbed — GPS geometry, source gluing, and correction codes

**20 November 2026. Research-only additive extension of SUCC's original pinbed.** Based on the authenticated Main XXVI source, the original Fourier–Yoneda pinbed, driven two-tone pinbed, learning pinbed, Principia's causal quotients, and draft #671's source-acquisition theorem. Proof status is scoped **paper mathematics / classical algebra**, with exact test receipts kept separately. No external physical GPS data, nonclassical physics, pi normality, R0, or new scholarly-priority claim. The original four-pole BBP forcing and literal `U_0=0` remain untouched.

## Model and steelman

A **head** is a declared observer role `(source_id, preparation, clock, frame, allowed probes, memory, noise budget, cost)`. A shaft is a lawful source-to-head causal path, not a metaphysical physical wire. Every report retains provenance, clock, source normalization, signed phase/reference if used, and whether it was actually acquired. The bed is the **joint compatibility problem** for source states with all reports, not a fictitious global sensor. Distinct heads need not be independent random variables; they must refer to one authenticated source under known transports. Shared-source errors and unknown gauge can defeat apparent redundancy.

**Steelman:** the GPS/code analogy predicts that individually incomplete heads may collectively determine a carrier-relative target. Redundant calibrated heads may detect or correct readout faults, while geometry controls stability. Distinguish (1) consistent global source realization; (2) uniqueness of the declared target; (3) conditioning/precision; (4) fault tolerance; (5) actual instrument acquisition and source adequacy; (6) eventual/infinite dynamical statistics.

Let `V=F^k`, with field `F=Q`, `R` or `C` as specified. Head i returns `y_i=P_i x` (scalar for explicit code results); retain a known invertible chart `C_i` so raw local report is `z_i=C_i P_i x`. For a finite collected head/path menu, stack normalized observations into `H=[P_1; ...; P_m]`. Under a lawful forward action word `w`, the corresponding row is `P_i A_w`; all such rows may be added with their clock and cost. A target is a linear map `F:V→Z` (call it `L` if confusing with the base field). A nonlinear carrier is not assumed to obey these linear formulas: it requires its own global laws or a justified local Jacobian chart.

## OHY-01 — Joint observer-gluing and target descent (CLASSICAL, PROVED)

For finite field-linear head maps, a given tuple `y` is a **lawful global source transcript** iff `y∈im H`. Let `Λ` have rows forming a basis of `ker(H^T)` (transpose, not conjugate; these are algebraic linear relations). Then

`y∈im H  iff  Λ y=0`.

The equations `Λ y=0` are exact **syndrome / compatibility** checks. If they fail, no source in the declared linear class explains all readings, but the failure does **not** identify which head, which source promise, or which calibration is wrong.

If `y` is realizable, the target `F x` is uniquely determined across all compatible states iff

`ker H ⊆ ker F  iff  rank([H;F])=rank H`.

**Proof:** `H x=H x'` iff `x−x'∈ker H`; target equality on each fiber is precisely the kernel inclusion. For syndrome, finite-dimensional annihilator duality says `(ker H^T)^⊥=im H`. A linear report on `im H` is a family of source-compatible sections, not automatically a full Yoneda nerve of the whole carrier. If Hom-based lawful probe objects are dense in a source category and the required preparations are available, the restricted Yoneda functor can be fully faithful. A finite linear `H` alone proves only target descent for the declared quotient.

**Adversarial:** nine identical copies of `P=[1,0]` do not recover target `[0,1]`. Increasing head count without independent causal directions changes neither kernel nor target truth.

## OHY-02 — More than the sum of individually informative heads (EXACT finite synergy)

For a uniformly random pair of independent bits `a,b`, let the target be `b` and two calibrated heads report `O1=a`, `O2=a XOR b`.

`I(b;O1)=I(b;O2)=0`, while `I(b;O1,O2)=1 bit`.

**Proof:** each individual report is a fair bit independent of `b`; their parity equals `b` exactly. In algebraic notation their maps are independent rows `[1,0]` and `[1,1]` over `F_2`, jointly rank two. This is **conditional/synergistic access to already source-encoded information**, not creation of entropy or energy. If the second head actually reports `a` again, the gain vanishes. The shared source label and causal correspondence are load-bearing. Neither statistical independence nor a quantum effect is needed.

For an arbitrary target `F`, *new* head `P` is useful exactly when `rank([H;P])>rank(H)` for source-state recovery, or when adding it repairs `ker H⊆ker F` for the specific target. Algebraic rank improvement and target information are distinct.

## OHY-03 — GPS local geometry, clock bias, and quantitative accuracy (CLASSICAL)

In a standard idealized one-way pseudorange model, satellite positions `s_i∈R^d` are known, the receiver has unknown position `x∈R^d` and unknown clock bias `b∈R`, and

`ρ_i(x,b)=||x−s_i||+b`.

At a noncollision operating point, its Jacobian row is `g_i=[(x−s_i)^T/||x−s_i||,1]`, a row in `R^{d+1}`. Thus at least `d+1` scalar satellites/heads are necessary for full **local first-order** position-plus-clock identification; sufficiency requires `rank G=d+1`. In 3D this is at least **four** generic satellites. The nonlinear model may also have global ambiguities: rank alone is only local.

For the linearized model `y=Gθ+ε` with full column rank, least squares gives `θhat=G†y` and

`||θhat−θ||_2 ≤ ||ε||_2/σ_min(G)`.

For independent equal-variance zero-mean errors `σ²` in the correctly calibrated linearized model, `Cov(θhat−θ)=σ²(G^T G)^{-1}`. More satellites do not guarantee accuracy if they are geometrically clustered, ill-conditioned or carry correlated bias. Unknown offsets/gains must be added to the state and calibration cost; they cannot be assumed away.

**Exact 2D witness:** rows `[u_ix,u_iy,1]` for unit directions `(1,0),(0,1),(−1,0),(0,−1),(3/5,4/5)`. Every three rows are invertible because a straight line meets the unit circle in at most two distinct points. Thus these five heads encode three unknowns with distance three (OHY-04). The independent numeric audit records `σ_min≈1.4142` for this well-spread geometry but `≈0.0005286` for five tightly clustered *distinct* rational unit directions; their geometry has >2600 times worse least favorable sensitivity. This is a **synthetic local instrument**, not a physical GPS field result.

## OHY-04 — Target-relative observer error-correcting code (CLASSICAL, PROVED)

For `m` scalar heads, define the **target separation distance**

`d_F(H)=min_{v: Fv≠0} wt(Hv)`, where `wt` is the number of *heads* with nonzero output. If some such `v` lies in `ker H`, then `d_F=0`.

If `d_F>e`, losing any `e` **known** heads (erasures) cannot make two different target values indistinguishable. Conversely if `d_F≤e`, some erasure set does. If `d_F>2t`, arbitrary corruptions of at most `t` unknown scalar head outputs can be corrected *at the target level*. Conversely if `d_F≤2t`, there are two different target values with overlapping Hamming balls of radius `t`, so universal correction is impossible.

**Proof:** for distinct target values, report vectors differ in at least `d_F` head coordinates. A set of `e<d_F` deleted coordinates leaves at least one disagreement. For errors, a single received tuple at Hamming distance `≤t` from both codewords would imply their distance `≤2t`. When `d_F≤2t`, split the difference support into two sets of size at most `t` to construct an ambiguous received tuple. The same argument gives exact necessity. This is a statement for **noise-free exact field readings with bounded numbers of fully adversarial head errors**, not finite-precision real sensors. Distinguish errors from erasures, deterministic covariance, and shared source-class violations.

If `H` is `m×k` and **full spark** (every selection of `k` rows has rank `k`), with target `F=identity`, the corresponding linear observation code has distance `m−k+1`. Proof: no nonzero `v` can vanish on `k` rows; any `k−1` rows have nontrivial kernel, so equality is attained. It detects up to `d−1` arbitrary faults, corrects `⌊(d−1)/2⌋` unknown faults, and tolerates `d−1` known erasures. A parity-check basis spans the left nullspace of H. Error positions can be located only when the code has sufficient distance; a nonzero syndrome alone merely detects inconsistency.

**Precision firewall:** for arbitrarily small real-valued differences, discrete Hamming distance does not yield a positive Euclidean minimum separation. For `ker H⊆ker F`, `F=F H†H`; the natural estimator `F H†y` has error `≤||F H†|| ||ε||` under bounded additive noise, and this is the minimax error on an unrestricted source space with Euclidean-ball noise. Proof of sharpness: choose a unit `u∈im H` approaching the norm of `F H†`, sources `±δ H†u` and errors `∓δ u`, both reporting zero. Any estimator must miss one target by at least `δ||F H†||`. A finite exact code may be hopelessly poorly conditioned.

## OHY-05 — The original two-tone pinbed was already a parity-check code (PROVED connection)

For each nonzero Fourier harmonic, the original SUCC two-tone pinbed has calibrated gain vector `g_h=(G_a(h),G_a(h−1))` and a single true complex coefficient `m_h`. Lawful paired readings satisfy `y=(g_0m_h,g_1m_h)`, hence

`g_1 y_0 − g_0 y_1=0`.

This is **exactly a syndrome/parity-check identity**; the prior pinbed calls it the cross-channel syzygy. For two nonzero gains the `[2,1,2]` scalar code can detect one arbitrary inconsistent channel but **cannot correct** an unknown one. With a third independently calibrated nonzero harmonic gain, the `[3,1,3]` code can correct one arbitrary corrupt complex reading in the exact model. If one gain vanishes, the distance can fall to two. Existing two-tone real-probability law realization additionally requires the appropriate infinitely many Toeplitz positivity constraints; per-harmonic code correction does not by itself prove a lawful probability distribution.

The new fixture uses rational gains `(2,3,5)` for exact arithmetic rather than pretending a particular physical aperture provides these gains at every h.

## OHY-06 — **BBP seven-head correction theorem** (NEW-TO-SUCC assembly, sharp conditional on inherited SA-02)

In the **declared** five-real-parameter source family, define

`r_c(j)=Σ_{a=1}^4 c_a/(8j−β_a)`, with `β=(7,4,3,2)`;
`U_0=s`, `U_n=16U_(n−1)+r_c(n)`;
`θ=(s,c_1,c_2,c_3,c_4)∈R^5`.

For each clock t the exact unwrapped head row is

`R_t=(16^t, Σ_{j=1}^t 16^{t−j}/(8j−7), Σ_{j=1}^t16^{t−j}/(8j−4), Σ_{j=1}^t16^{t−j}/(8j−3), Σ_{j=1}^t16^{t−j}/(8j−2))`.

Thus `U_t=R_t θ`. The arbitrary-five-clock theorem [#671, SA-02](https://github.com/femboy2112/SUCC/blob/73bbe2bfd603dc3ffc06375366b200ab5a429737/research/2026-11-19/causal_generator_reconstruction/SOURCE_ACQUISITION.md) proves **any five distinct nonnegative clock rows have nonzero determinant** (indeed positive in ordered form), using a block-Cauchy expansion. Import this **declared-family** theorem, not a claim about every other causal source.

**Corollary:** any `m≥5` distinct exact unwrapped clock heads form a full-spark observation code of length `m`, dimension five and minimum Hamming distance

`d=m−4`.

In particular, **seven** distinct heads have `[7,5,3]` and correct **one** arbitrary corrupted scalar report, detect up to two, or tolerate **two known erasures**, without modifying the original source. These readings can be collected sequentially from one forward trajectory and retained in memory; seven simultaneous independent physical copies are *not* required. The theorem assumes that the true state lies in the source family, all other clock/head labels are correct, and at most the declared number of scalar readings are wrong. Faults in the source law, clock alignment, charts, or shared reference are not protected.

**Proof:** SA-02 implies full spark; OHY-04 gives exact distance and error/erasure bounds. Independent SymPy reconstruction verifies all 21 five-clock minors for clocks `1,...,7`, and an independent exact decoder recovers `(0,4,−2,−1,−1)` after one corrupted report. The imported arbitrary-clock theorem supplies the universal statement; finite checks calibrate the implementation, not the theorem's quantifiers.

**Resource and authority:** original BBP's `s=0`, signed coefficients and recurrence are already given by the source contract, so these extra heads are a **redundant verification/error correction experiment against admitted parameter rivals**, not additional arithmetic information required to define π. Exact scalar readings are an ideal oracle. The inherited condition number for five consecutive late clocks can grow as `Θ(N^7)` in raw units. No source-mixing inequality or π-normality estimate follows from recovering its five source parameters.

## OHY-07 — Causal communication must carry its frame and anchor (PROVED gauge boundary)

Let head i return `z_i=C_i P_i x`, with known invertible frame `C_i`. Then each head can be normalized to `P_i x`, and the joint rank/syndrome/precision calculations apply with actual transported noise bounds. An **unknown** independent phase reference at each head cannot be normalized for free: two reports `z_i=e(θ+α_i)` with arbitrary uncalibrated `α_i` fit *every* θ, regardless of how many such heads are added. Thus redundant reports needn't supply new source information.

On a rooted directed graph with mutually coherent forward path comparisons, a phase connection is recovered up to vertex gauge from `|E|−|V|+1` chord holonomies (inherited [#671 PG-01](https://github.com/femboy2112/SUCC/blob/73bbe2bfd603dc3ffc06375366b200ab5a429737/research/2026-11-19/causal_generator_reconstruction/PATH_GEOMETRY.md)). A comparison of two forward paths to a common endpoint is a valid algebraic holonomy without physical reversal of time. An **absolute seed/endpoint phase** needs its own source anchor. More independent path comparisons can create syndrome-like consistency checks, but only with a declared acquisition protocol, known coherent references and a corrected source map.

## OHY-08 — A thousand heads sharing the same quotient cannot reveal its erased history (EXACT BBP no-go)

For the unchanged BBP forcing, two seeds differing by `δs=16^(−N)` have unwrapped state difference `16^(t−N)`, an integer at every `t≥N`. Thus all circle phases at every such time are identical under **every** circle Fourier character and any passive circle pinbed, even with arbitrarily many heads, all future time windows or complete phase tomography. Yet their unwrapped seed and earlier historical records differ. For `N=1`, the shift is `1/16` and the alias holds for all clocks `t≥1`.

A head with lawful unwrapped state/seed access, or one retaining relevant early-time memory, can distinguish them. This is an access/provenance difference, not a force that collective voting repairs. It is inherited from [learning pinbed LO-02](https://github.com/femboy2112/SUCC/blob/main/research/2026-11-07/pinbed_yoneda_oscillators/LEARNING_OBSERVER.md). These late-circle-aliased histories **do have the same normality status**; seed identification is distinct from the signed normality target.

For each fixed finite terminal `M`, setting a different seed `s_M=−P_M` gives an identically locked **finite completed** BBP orbit `U_n(s_M)+T_n^[M]=0` for `n≤M`, even with every authentic forcing value and every source-time head intact. This altered seed is recoverable by the unwrapped five-parameter observer. The genuine fixed infinite counterseed `s=−π/16` likewise differs from `s=0`; it remains a *source-blind inference* killer, not a rival to the authenticated initial-value problem.

## OHY-09 — Source-class promise and shared-error adversaries (EXACT boundary)

For any finite collection of clock heads ending at `M`, alter only an out-of-family forcing at `M+1`. Every earlier report remains exactly the same, and the later state differs. No finite full-rank report bank, no matter how redundant, authenticates an unrestricted future carrier. This is the inherited delayed-witness obstruction.

Likewise, a common unknown clock offset, incorrect nominal satellite positions, or shared faulty phase reference can produce mutually consistent but wrong reports. Pure algebraic redundancy does not turn a shared defect into multiple independent checks. The relevant source passport, instrument calibration, clock and frame data are part of the report type.

## OHY-10 — The objective+subjective pinbed's remaining π truth debt (UNVERIFIED)

For the *authenticated* original four signed poles and literal `U_0=0`, the exact completed phase is `Y_n=U_n+T_n=16^n π/16`, and the real orbit's normality still requires `W_B(h)→0` for each nonzero integer h. R0 requires a positive all-late-shell Gaussian displacement/hexadecimal-domain-wall density (refer to #672 and #662). The observer-headed pinbed can determine the parameter source, detect or correct faulty readouts, preserve source anchors, and compare calibrated frame-relative spectra. **It does not force a positive all-shell signed phase response.**

A new witness must use the independently source-derived p-primary/cofactor or carry chronology, retain the zero seed and complex phase, and prove a bound applicable to all sufficiently late shells while failing on correctly labeled locked controls. Extra heads that merely re-encode the same zero-defect recurrence or same source-time Fourier spectrum do not supply an independent signed inequality. The differential and mixed head correlations are the most concrete new probe candidates; the target-bearing signed correlation is still unpaid.

## Claim boundaries and independent tests

- **Mathematical exactness:** OHY-01/03/04/05/06/07/08/09 are elementary, inherited, or exact within explicit models. OHY-02 uses a uniform-bit source for the information calculations; this is not a statement about physical mutual information in arbitrary systems.
- **Nonclassical carrier:** a GPS/code-like joint observer can be realized entirely classically. Evidence for uniquely nonclassical physics would require separate operational inequalities/experiments.
- **Formalization:** these are paper proofs and exact test receipts; no new Lean proof, peer referee, or actual sensor tests. The full root suite is not claimed.
- **Next falsifier:** preregister the original-zero BBP source/head bank plus source-tail/carry heads, compare signed **source-coherent** head syndromes against the unchanged forcing with wrong seed, source mutants, clock misalignment and matched finite terminals. Test whether a genuinely new bound survives held-out late shells; finite passes alone never establish R0.

# Operation Γ16 — the source-preserving 16×16 BBP matrix, q-Gamma blocking and full-tail Yoneda lift

**Date:** 2026-11-09. **Branch scope:** additive research child of #565 at `35a664c19e91ab5bd11678c82566ce88336e0309`. The original signed source, literal `U_0=0`, archive/provenance, formal kernels, workflows, sibling branches and main are frozen. **π base-16 normality remains OPEN.** New-to-SUCC assembly and finite checks are not a claim of worldwide novelty or refereed proof. The critical classical q-Gamma input is [NIST DLMF §5.18, equation 5.18.7](https://dlmf.nist.gov/5.18.E7).

## Ontology: three matrices that must NOT be conflated

1. **Scalar empirical pair matrix** `M^(N) in R^(16×16)`, with nonnegative entries summing to 1, calculated from actual two-digit observations. It has 256 scalar entries and discards every third-or-later digit.
2. **The unitary Fourier/finite Weyl matrix** `F_16`, a basis-change on the **16-dimensional digit space**, `F_(u,a)=16^(-1/2) exp(-2πiua/16)`. It is independent of π and BBP. The transformed scalar pair matrix is `\hat M=16 F M F^T`, not `F M F^*` because the *joint law* has two forward Fourier character coordinates. `F M F^*` is instead appropriate when conjugating a linear operator, such as the row-stochastic conditional transition `P`.
3. **Full carrier's 16×16 matrix of measures** `\mathfrak M_(a,b)`, each cell a nonnegative measure on the *entire residual future tail*. This is injective and actually reconstructs the whole state law. It is not equivalent to 256 scalar masses unless one assumes extra future-independence.

The phrase *BBP–Gamma matrix* is shorthand for the **composition of** (i) the source-specific BBP Laplace/q-Gamma **blocking** cocycle, (ii) the finite Fourier/Weyl **interference** basis, and (iii) the full-tail **realization** map. It is **not** an identity between Euler Γ and a 16×16 matrix, and not yet a normality theorem.

## GM16-01 — exact cyclic 16×16 observation matrix, spectral transformation (PROVED)

Let `d_1,...,d_N∈{0,...,15}` be any finite hexadecimal word, `N≥2`, and extend cyclically only for counting. Put

\[
C_{ab}=\#\{1\le n\le N:d_n=a,\ d_{n+1}=b\},\qquad M_{ab}=C_{ab}/N,
\]

with `d_(N+1)=d_1`. Then `\sum_b C_(a,b)=\sum_b C_(b,a)` (exact de Bruijn flow balance), and `\sum_{a,b} M_{ab}=1`. Let `\zeta=\exp(2πi/16)` and `F_{u,a}=\zeta^{-ua}/4`. The unitary DFT satisfies

\[
\boxed{\widehat M_{uv}=\sum_{a,b}\zeta^{-ua-vb} M_{ab}=(16F M F^{\mathsf T})_{uv}.}\tag{GM1}
\]

Every pair law is recovered by Fourier inversion; its Haar reference has `M_ab=1/256`, thus `\hat M_00=1` and every other coefficient 0. Plancherel gives, *exactly as an identity*,

\[
\boxed{E_2(N)=256\sum_{a,b}(M_{ab}-1/256)^2=\sum_{(u,v)\ne(0,0)}|\hat M_{uv}|^2.}\tag{GM2}
\]

The **16 digit characters** split into cyclotomic orders `1,2,4,8,16` of dimensions `1,1,2,4,8`; their tensor pairs account for all 256 matrix modes. These correspond to SUCC #559's primitive Fourier sectors. This is a change of basis, **not** a source-selected bound.

The finite Fourier matrix is the conventional discrete Heisenberg/Weyl quarter-turn: with `T|a>=|a+1>`, `Z|a>=\zeta^a|a>`, we have `F T F^(-1)=Z^(-1)`, `F Z F^(-1)=T`, `F²|a>=|-a>`, `F^4=I`. This is not a field-\(\mathbb F_{16}\) Fourier operator; the digit group is **\(\mathbb Z/16\mathbb Z\)**, which is not the additive group of \(\mathbb F_{16}\). No prime-field Gauss bound transfers merely by renaming the group.

## GM16-02 — exact split into preferred-basis locking and relative-phase resonance (PROVED)

Let `S` simultaneously increment both digit coordinates mod16. The 16-shift twirl

\[
(\Pi M)_{ab}=\tfrac1{16}\sum_{t=0}^{15}M_{a+t,b+t}=
\frac{Q_{b-a}}{16N},\qquad Q_j=\sum_a C_{a,a+j},
\]

is an **orthogonal projection** in Frobenius inner product onto the subspace invariant under this common digit translation. Its Fourier transform retains precisely characters with `u+v≡0 mod16`.

Therefore, without any probabilistic input,

\[
\boxed{E_2=E_{\rm basis}+E_{\rm relative}},\qquad
E_{\rm basis}=256\|M-\Pi M\|_F^2,
\quad E_{\rm relative}=256\|\Pi M-J/256\|_F^2.\tag{GM3}
\]

Both are **exact rational count invariants**:

\[
\boxed{E_{\rm relative}=\frac{16\sum_j Q_j^2-N^2}{N^2},\qquad
E_{\rm basis}=\frac{\sum_{a,b}(16C_{ab}-Q_{b-a})^2}{N^2}.}\tag{GM4}
\]

The single-digit energy `E_1` lies entirely in the basis sector, so `0≤E_1≤E_basis`. The relative sector detects a **digit-difference preference even when no digit is a preferred origin**. An exact period-16 rotation `0123456789ABCDEF` gives `(E_1,E_basis,E_relative)=(0,0,15)`: *no preferred digit basis does NOT imply Haar*. Equalizing only the relative sector likewise does not control basis-locking.

This makes the user's “basis point on the circle” distinction rigorous: it is a **proper subspace** of the obstruction, not the entire obstruction.

## GM16-03 — the 16×16 joint law is insufficient; the 16×16 future-tail matrix is fully faithful (PROVED + COUNTEREXAMPLE)

For a Borel probability μ on `[0,1)` let `d_1(x)=floor(16x)`, `d_2(x)=floor(16{16x})`, `T(x)={16x}`, `B_a(y)=(a+y)/16`. Define a 16×16 **matrix of finite positive measures** on the residual circle:

\[
\boxed{\mathfrak M_{ab}^{\mu}(D)
=\mu\{x:d_1(x)=a,\ d_2(x)=b,\ T^2x\in D\}.}\tag{GM5}
\]

Then

\[
\boxed{\mu=\sum_{a,b}(B_a\circ B_b)_*\mathfrak M_{ab}^{\mu},\qquad
T^2_*\mu=\sum_{a,b}\mathfrak M_{ab}^{\mu}.}\tag{GM6}
\]

**Proof:** `x=B_(d1(x)) B_(d2(x))(T²x)` exactly under the declared half-open radix convention. Each x belongs to one digit cell; integrate a test function and sum. Conversely **every** collection of nonnegative finite cell measures of total mass1 realizes exactly one μ by GM6; thus this is a genuine representation isomorphism on the declared spaces. The scalar matrix is merely `M_ab=\mathfrak M_ab(whole circle)` and forgets the tail test functions.

If μ is T-invariant, then **conditional first-digit Haar given the entire future tail** is the measure-valued row relation

\[
\boxed{\mathfrak M_{ab}=\frac1{16}\sum_c\mathfrak M_{cb}
\quad\text{as measures, for every }a,b.}\tag{GM7}
\]

It is equivalent to SUCC #565's `Qμ=μ` and, together with T-stationarity, implies μ=Haar. This is an *inherited* qualitative implication expressed at a new matrix-of-measures interface. The original-zero estimate needed to verify GM7 along empirical π histories remains OPEN.

**Decisive alias:** a periodic de Bruijn word of order2 has **every pair exactly once**, hence its scalar matrix is EXACTLY `J/256`, its row kernel is EXACTLY `J/16`, and all 255 non-DC scalar pair Fourier modes vanish. But its three-word energy is `E_3=15`; its `\mathfrak M_ab` measures are each an atom of mass1/256 at a particular periodic future, not Haar tail mass. This is a *source-free* counterexample to “a Haar 16×16 scalar matrix implies normality.”

**Topology firewall:** on a finite empirical atomic orbit whose atoms have no shifts by nonzero a/16 in the same orbit (e.g. this periodic de Bruijn orbit, or any irrational ×16 orbit), `||μ_N-Qμ_N||_(TV-mass)=15/8` for every N—even when the point has normal digits. Consequently, **do not demand total-variation convergence of empirical measures to Qμ_N**. Use SUCC #565's interval Wasserstein/weak finite smooth Fourier pin metrics, which are compatible with empirical approximation. Exact measure-valued equality is a limiting-law statement, not a finite-atom TV proof gate.

## GM16-04 — two-digit sampling has two genuine chronological frames (PROVED)

For even N, split pair starts into even and odd indices (zero-based indices of **fractional digits of π**). Let `M_even,M_odd` be their respective normalized 16×16 matrices, with N/2 samples each, and `M_all=(M_even+M_odd)/2`. Then by polarization,

\[
\boxed{\frac{E_2^{\rm even}+E_2^{\rm odd}}2
=E_2^{\rm all}+64\|M_{\rm even}-M_{\rm odd}\|_F^2.}\tag{GM8}
\]

**Subtle source-origin detail:** the BBP `U_0=0` completion is `α=π/16`, whose hexadecimal digits start with **3** followed by the fractional digits `243F...` of π. Radix-256 *blocking of α* begins `(3,2)` at k=0 and then `(d_2,d_3),(d_4,d_5),...` at k≥1. Thus the original grouped **source** `U_(2k)` agrees with the **odd zero-based** starts in the archived fractional-π digit prefix after the initial `(3,2)` pair. The other frame is a once-shifted carrier. Replacing all-start pair statistics by one selected frame without a parity/phase budget is an unlicensed arrow.

This positive phase-frame energy is **not** conserved physical energy or new cancellation. It quantifies the representation cost of choosing one radix-256 clock instead of averaging both.

## GM16-05 — authentic source + exact two-step Fourier lattice (PROVED FINITE FORMULA; SIGNED ASYMPTOTIC OPEN)

Keep the original four signed poles and `U_0=0`:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
x_n=\{16x_{n-1}+r(n)\}.
\]

For n≥2, `0<r(n)<1`. Define the literal carry character `F_(r,h)(x)=exp(2πih floor(16x+r)/16)`, with h mod16; if h=0 it is identically1. By SUCC #564 FLP-03 (already proved), for h≠0,

\[
\hat F_{r,h}(m)=c_h(m)\,e(mr/16),\quad
c_h(m)=\frac{16(1-e(-h/16))}{2\pi i m}\mathbf1_{m\equiv h\ (16)},\quad m\ne0.
\]

Put `r=r(n)`, `s=r(n+1)`, `x=x_(n-1)`. The **actual** consecutive real carry-character product is `F_(r,u)(x) F_(s,v)(16x+r mod1)`. Finite Fejér expansions of common aperture H multiply to a completely explicit **two-dimensional source-twisted Fourier lattice**:

\[
\boxed{\sum_{\substack{|m|,|\ell|<H\\m\equiv u\ (16),\ \ell\equiv v\ (16)}}
\bigl(1-|m|/H\bigr)\bigl(1-|\ell|/H\bigr)c_u(m)c_v(\ell)
 e((m+16\ell)x)\,e\!\left(\frac{mr+\ell s}{16}+\ell r\right).}\tag{GM9}
\]

For zero character include only its m=0 coefficient=1 (and analogously for ℓ). **This is exactly the desired twist → two-character interference → source-twist → realized digit-pair readout.** The arithmetic frequency is `m+16ℓ`, not an arbitrary fitted phase. The source-specific twist factorizes further across SUCC #552's three positive channels because `r=Σ_i r_i`.

For the sharp discontinuous carry characters, replacing the true pair by this finite lattice costs at most the **sum of the two individual FLP-04 Fejér boundary errors** (because both exact characters and their positive-Fejér means lie in the unit disk). On any epoch, this yields explicit moving-boundary occupation counts plus `O(1/(Hε))`. The original-zero bound on these counts and *signed* Fourier sums is UNVERIFIED. Fixed or `H=o(A²)` modes become insensitive to the direct `r(n)=O(A^-2)` source twist; this is not a source-independent normality proof.

## GM16-06 — TRUE Gamma link: exact q-Gamma blocking of the original positive source (PROVED; classical q-Gamma input)

From SUCC's frozen four poles, in Laplace variables with `a_n=8n-7`,

\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}
=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x})>0,
\quad r(n)=\int_0^\infty e^{-a_n x}Q(x)dx.
\]

For any fixed integer g≥1, **the inherited exact g-step radix regrouping** is `R_g(k)=Σ_(j=1)^g 16^(g-j)r(g(k-1)+j)`, and `U_(gk)=16^g U_(g(k-1))+R_g(k)`. Put `a_g(k)=8g(k-1)+1` and `t=e^{-8x}`. Termwise integration proves the *new source-typed Laplace expression*

\[
\boxed{R_g(k)=\int_0^\infty e^{-a_g(k)x}Q_g(x)dx,\quad
Q_g(x)=Q(x)\,\mathcal B_g(e^{-8x}),\quad
\mathcal B_g(t)=\sum_{j=0}^{g-1}16^{g-1-j}t^j.}\tag{GM10}
\]

**Recursion and composition** are polynomial identities, valid for every t:

\[
\boxed{\mathcal B_{g+h}(t)=16^h\mathcal B_g(t)+t^g\mathcal B_h(t),\qquad
\mathcal B_{gh}(t)=\mathcal B_g(t)\sum_{j=0}^{h-1}16^{g(h-1-j)}t^{gj}.}\tag{GM11}
\]

These follow by partitioning/reindexing the finite geometric series; this proves exact associativity of nested digit blocking. At `t=1`, `\mathcal B_g(1)=(16^g-1)/15`; the **endpoint jets** are

\[
\boxed{Q_g'(0)=16^g-1,\qquad
Q_g''(0)=-59\mathcal B_g(1)-240\sum_{j=0}^{g-1}j16^{g-1-j}.}\tag{GM12}
\]

In particular `Q_1'(0)=15,Q_1''(0)=-59`; `Q_2'(0)=255,Q_2''(0)=-1243`. Positivity and the simple endpoint zero survive for every fixed finite g. For a→∞, the normalized positive Laplace density `e^(-ax)Q_g(x)dx / ∫ e^(-ax)Q_g(x)dx` under the scaled variable `Y=aX` tends to the classical **Gamma(2,1)** density `y e^(-y)dy`. This is the same endpoint-rank mechanism already observed in SUCC's Gamma work; blocking preserves its rank but not the higher jet constants.

Here is a *literal* link to the **classical q-Gamma function**. With `q_x=e^{-8x}/16 in (0,1/16]`, the q-integer `[g]_q=(1-q^g)/(1-q)` satisfies the classical [DLMF 5.18.7](https://dlmf.nist.gov/5.18.E7) recurrence `Γ_q(g+1)=[g]_qΓ_q(g)`. Therefore

\[
\boxed{\mathcal B_g(e^{-8x})=16^{g-1}[g]_{q_x}
=16^{g-1}\frac{\Gamma_{q_x}(g+1)}{\Gamma_{q_x}(g)}.}\tag{GM13}
\]

This is **exact**, but note the crucial difference between the two appearances of Gamma: `q_x≤1/16` and does *not* approach1 in the endpoint scaling, so the Gamma(2) law and the q-Gamma quotient are **not the same limit**. The q-Gamma factor is universal to radix blocking of *any* Laplace source, including a two-pole counterfeit. It cannot select the π forcing or zero seed alone. The four-pole source-specific fingerprint remains in Q(x), its three components and its higher jets.

## GM16-07 — the original BBP gauge identifies the source time, not genericity (INHERITED; CHECKED FINITELY)

Let `α=Σ_(j≥1)16^-j r(j)=π/16` (classical BBP). `U_n+T_n=16^nα` exactly and `T_n=(r(n+1)+T_(n+1))/16`. Thus translations `H_n:x↦x+T_n (mod1)` obey the exact affine cocycle intertwining

\[
\boxed{H_{n+1}\circ(x↦16x+r(n+1))=(x↦16x)\circ H_n.}\tag{GM14}
\]

The **actual** completed digit observations at n≥1 are the digits of `z_n={16^nα}`; `z_1={π}` gives the first fractional digit 2. This is the source-anchored natural equivalence previously developed in SUCC. It preserves the singleton zero-seed path and π; it does *not* make that point generic for Haar or imply normality by a change of representation.

## GM16-08 — honest negative controls (PROVED)

1. **Period-16 digit cycle:** simultaneous digit-shift invariance (no preferred basis) holds exactly, but the relative pair energy is15 and the orbit is nonnormal.
2. **de Bruijn(16,2) cycle:** pair matrix literally equals Haar, but E3=15 and the full tail measures are point-supported. A scalar 16×16 matrix cannot decide normality.
3. **Positive full-support mixing Markov chain:** `P=(I/2)+(J/32)` has stationary uniform single-digit law and is irreducible/aperiodic with gap1/2, but its pair relative energy is 15/4 and its pair law is non-Haar. A random-reference mixing theorem does not establish the authentic deterministic BBP origin.
4. **Every source-twisted Haar reference is identically Haar at two digits:** for any two fixed rational source shifts r,s∈[0,1), a Haar-distributed x maps under `x↦(floor(16x+r) mod16, {16x+r})` to `(Unif16, Haar)` independently. Applying `floor(16y+s) mod16` makes all 256 pair probabilities exactly1/256. This is true for arbitrary forcing, including counterfeits. The script certifies it by independent exact rational threshold interval integration; it is not a statement about the original zero-selected orbit.
5. **Same-forcing coherent wrong seed:** seed `s*=−π/16` gives completed α=0 and a constant symbol, yet every source Laplace blocking identity, q-Gamma quotient, positive three-channel geometry and affine gauge law still holds. Thus analytic source transformations alone cannot distinguish selected normality.
6. **Finite empirical TV trap:** even a normal irrational ×16 orbit has `||μ_N-Qμ_N||_(TV-mass)=15/8` for each finite N, because its sampled points and nontrivial 1/16 rotations are disjoint; this cannot be used as a convergence target. The source-anchored SUCC interval W1 and finite smoothed Fourier observers are appropriate weaker probes.

## GM16-09 — finite, exact observations on ALREADY CERTIFIED π digits (OBSERVED; NOT NEW HOLDOUT)

The input is the same **40,960** hexadecimal fractional digits previously generated from original zero-seeded BBP by draft #561, then reused in #565. `sha256(data + newline)=c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527`. No new digits are generated, no new independent oracle is claimed. All counts below are exact integer/rational; complex Fourier and plotted colors are diagnostic.

All-start 16×16 pair counts: `N=40960`, Haar expected cell count **160**, observed cell range **129..189**, exact scalar energy

\[
\boxed{E_2=\frac{981}{163840}\approx0.00598755,\qquad
E_1=\frac{7629}{52428800}.}\tag{GM15}
\]

The basis/relative split is

\[
\boxed{E_{\rm basis}=\frac{284071}{52428800},\qquad
E_{\rm relative}=\frac{29849}{52428800}.}\tag{GM16}
\]

Approximately **90.49%** of the observed two-digit discrepancy lies in the basis-sensitive component and **9.51%** in digit-relative resonance. These are two independent *mathematical subspaces*, not probabilistically independent energy sources or evidence that one must decay faster.

Two zero-based chronological stroboscopic frames at same N give

\[
E_2^{\rm even}=\frac{9281}{819200},\quad
E_2^{\rm odd}=\frac{10249}{819200},\quad
\text{frame split}=\frac{243}{40960}.
\]

The exact identity GM8 holds. The stage-labelled #554 prime clock gives another exact four-stage variance decomposition on the actual real completed-digit matrix, not a new signed saving: for epoch `A=2048,p=4937` the source births cut the epoch at `(2048,2469,3086,3703,4096)`. Stage variation is positive by elementary variance decomposition even for fake sources and arbitrary partitions, so only a *signed source-selected correlation with the real complementary phase* can advance normality. The 16 same-histogram shuffle controls and a periodic/de Bruijn control are retained in the separate finite receipt.

## GM16-10 — precise unproved theorem and proof-burden accounting

The matrix of full-tail measures and its Fourier basis define a lawful observer representation. A genuine π normality proof could establish, **for all sufficiently large original-zero epochs, every fixed future tail test from a convergence-determining family and every nontrivial first-digit character**, asymptotic vanishing of the source-anchored signed conditional modes. That is the #565 conditional Haar symmetry defect, in source-typed matrix form. **This is a reformulation and currently remains unproved.**

The particularly tempting shortcut “q-Gamma blocking ⇒ scalar pair Haar ⇒ π normality” has TWO independent refutations: the source q-Gamma factor also holds for coherent wrong seeds, and a periodic order-two de Bruijn path has scalar pair Haar without global normality. Every claimed result must retain the original four poles, zero seed, actual time frame and future-tail probes; no averaged Haar reference may stand in for the selected orbit.

**Claims:** matrix transport, twirl energy, full-tail reconstruction, source blocked-Laplace/q-Gamma relation, correct start phase and finite probes PROVED as specified; model and prior classical inputs explicitly credited; original zero-seed all-epoch decay, q-Gamma-to-Haar inference and normality **OPEN/REFUTED as scoped**.

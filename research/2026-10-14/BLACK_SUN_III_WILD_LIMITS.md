# BLACK SUN III — Tame towers and wild limits: the Alexander correspondence, the Baez-Duarte distance instrument, and the two-mode reduction

**Campaign round 3:** 2026-10-14 (night). **Branch:** `research/black-sun-iii-wild-limits-2026-10-14` (child of Black Sun II `1dc31da`). **RH PROVED: NO.** No zero positions used as inputs. This round takes the operator's wild-embedding intuition (J.W. Alexander's horned sphere) seriously, states precisely where it is load-bearing for SUCC and where it is only analogy, and builds two new instruments plus the main-line two-mode reduction.

## 0. The intuition, stated precisely

Alexander's horned sphere (1924): a topological 2-sphere embedded in S³ constructed as an infinite composition of "horn-pushing" stages. **Every finite stage is tame** (locally flat, with simply-connected complement); **the limit is wild** (complement not simply connected). The wildness is invisible to every finite local observation; it is detected only by a *global loop* threading the horns. The wild points form a Cantor set — a limit object par excellence.

The operator's hypothesis: *"what globally is a sphere, from our local finite perspective is the local projection of an infinitely intertwisting embedding."* SUCC has two towers with exactly this architecture, and the correspondence is more than poetry in both:

| Alexander | The window tower (Weil) | The dilation tower (NBD/BD) |
|---|---|---|
| finite construction stages | windows (−a,a): finitely many prime atoms (n < e^{2a}) | spans V_k = span{γ_2,…,γ_{k+1}}: finite-dimensional |
| each stage tame | Q_a computable spectrum (round 1–2) | Gram matrices exact, solvable |
| the limit object | the completed Weil form over all windows | the closure of ∪V_k |
| the limit question | Q_a ≥ 0 for ALL a (⟺ RH) | γ ∈ closure (⟺ RH, BD's strengthening) |
| horn loops | negative directions / near-null modes | a nonzero f ⊥ every γ_l |
| Cantor wild set | the zero-set geometry (via BM density, round 1) | the zero-set aggregate mass |
| detection needs global data | ∀a quantifier; finite Gram evidence void (IH-01) | d_k > 0 at every finite stage; only d_k → 0 decides |

**The honest disanalogy:** Alexander constructs a specific embedding whose wildness he *proves*; SUCC's towers have limit questions whose answers (RH-equivalent) are unknown. The correspondence supplies architecture, not proofs. What it *does* supply rigorously: (i) the discipline that finite-stage evidence can never settle the limit question (this is the repo's IH-01/FSW-4 no-go family, now with a geometric home), and (ii) the shape of any witness — always a global object orthogonal to all finite stages.

## 1. BS-III-2 (PROVED LOCAL): the source-to-tower transport is TAME

For every A > 0, the windowed-form family {Q_a : a ≤ A} determines the source Λ(n)/√n for every 2 ≤ n < e^{2A} exactly, and is completely blind to mutations at n ≥ e^{2A}. The recovery is explicit: for each atom n₀ < e^{2A}, a smooth test function with support isolating ±log n₀ from all other atoms (locally finite separation) extracts the weight exactly (E38.1's mechanism, restated for the coverage tower). **Consequence:** the tower of finite stages is a *faithful inverse system* on sources — no wildness hides in the transport. The difficulty of RH lives exclusively in (a) the SIGN of each stage's form (a hard but finite spectral question at each a — my round-1/2 spectra) and (b) the universal quantifier over a. The "wildness" is precisely the ∀, not any hidden identification failure. (Exact finite verification: `source_recovery_check`.)

This sharpens the SUCC question *where the wildness is*: it is a quantifier/limit phenomenon (density, positivity-at-every-scale, closure), never an information phenomenon. Finite observers are not deluded about the object; they are deluded only if they mistake finite-stage evidence (d_k > 0 at all k probed; λ₀(a) unresolved at 1e−4) for limit knowledge.

## 2. BS-III-1 (classical + exact implementation): the Baez-Duarte distance instrument

The Nyman–Beurling criterion and Baez-Duarte's strengthening (EXTERNAL THEOREMS): in the Bagchi-weighted space 𝓗 = ℓ²(ℕ, 1/(n(n+1))), with γ_l = ({{n/l}})_{n≥1} and γ = (1,1,…), **RH ⟺ γ lies in the closed span of {γ_l}**. The distance sequence

\[
d_k = \mathrm{dist}\big(\gamma,\ \mathrm{span}\{\gamma_2,\dots,\gamma_{k+1}\}\big),\qquad \|\gamma\|^2 = 1 \text{ exactly},
\]

is computed here with **closed-form Gram entries**: ⟨γ_l, γ_m⟩ = ∑_n {n/l}{n/m}/(n(n+1)) reduces, by the periodicity of {n/l}{n/m} modulo lcm(l,m) and the telescoping weight ∑[1/(jL+r) − 1/(jL+r+1)] = (1/L)[ψ((r+1)/L) − ψ(r/L)], to finite digamma-at-rationals expressions (themselves Gauss-closed forms). The ⟨γ, γ_l⟩ entries likewise; e.g. ⟨γ, γ_₂⟩ = (log 2)/2 exactly (verified to 30 digits). Note γ₁ = {{n/1}} ≡ 0 — the first dilation vector is identically zero; the effective family starts at γ₂.

**Instrument validation:** the closed forms match direct summation within tails (`test_gram_closed_vs_direct`); and the sequence reproduces the published Baez-Duarte table (d₁ = 0.553943, d₂ = 0.309431, d₃ = 0.256811, d₄ = 0.190575, d₅ = 0.190284, d₆ = 0.156168 — regression-locked to 6 digits).

**The horn reading (TESTED MODEL):** d_k > 0 at every finite stage — the horns never fully retract at any finite k (each finite-dimensional projection leaves a positive residual: the limit question is whether the horns retract *in the limit*, which is RH). The measured decay is slow (d₁₂ = 0.140980): under RH, d_k → 0 with a rate governed by the zero aggregate (classical analysis: the Mellin side relates d_k² to zero contributions); the observed ~1/√k-ish decay is consistent with the classical numerics and with no finite stage being decisive. **The BD sequence is the cleanest quantitative "wildness meter" in the whole program: every entry is exact finite arithmetic, and the limit question is precisely RH.**

The correspondence with my window spectra (rounds 1–2): the BD distances d_k and the window eigenvalues λ₀(a) are two meters of the same limit object (both RH-equivalent); the near-null window modes (Shannon count 4a) and the slow BD decay are the same "horns remaining" measured in two geometries. A quantitative bridge between them (e.g., an inequality linking d_k to window margins at a = (log k)/2-type scales) is open and recorded as a target.

## 3. BS-III-3 (TESTED MODEL): the two-mode reduction — groundwork for the phase-sharp certificate

At a = 1/2 (first window, prime-2 only), the completed Weil form's restriction to the span of the two lowest eigenmodes (computed at M = 1200):

- **The 2×2 effective matrix is diagonal at machine precision in the eigenbasis**: entries (−1.5e−6, +1.8e−4): the two near-null eigenvalues of the full operator.
- **A-part vs prime-part split per mode:** even-mode direction: A-part +0.0119, prime-part −0.0119; odd-mode direction: A-part −0.1600, prime-part +0.1601. The prime-2 atom compensates the archimedean form mode-by-mode (the odd mode's rescue +0.160 is the phase-rescue of round 2 seen in the reduced matrix).
- **Complement margin: λ₂ = +0.018.** The third and higher modes are comfortably positive.

**The reduction hypothesis** (round 2's next lemma, now with data): all difficulty is confined to the 2-dimensional span; the certificate program is: (i) interval-arithmetic positivity of the 2×2 (the 1e−4-scale objects — hard but finite), plus (ii) a rigorous complement bound λ ≥ 0.018-margin (the +0.018 margin is two orders above the noise floor: tractable by profile-weighted estimates). Failure of (i) at the 1e−6 scale would be a first-window counterexample candidate requiring the full hostile-verification protocol.

## 4. Status ledger

| ID | Statement | Status | Test |
|---|---|---|---|
| BS-III-1 | BD distance instrument: closed-form Gram (digamma at rationals), γ₁ = 0, b₂ = (log2)/2, d_k sequence = published table | PROVED LOCAL (implementation) + EXTERNAL THEOREMS (criterion) | test_black_sun_wild.py (7 tests) |
| BS-III-2 | Tame-tower faithfulness: finite stages see exactly n < e^{2A}; full tower determines the source | PROVED LOCAL | test_visibility, test_recovered_weight |
| BS-III-3 | Two-mode reduction at a = 1/2: 2×2 diagonal, per-mode A/prime compensation, complement margin +0.018 | TESTED MODEL | test_reduction_structure |
| Alexander correspondence | the architecture table (§0); disanalogy stated | STUDY (no claim) | — |

## 5. Boundary

Nothing here proves RH. The BD criterion is classical (Nyman/Beurling/Baez-Duarte/Bagchi — cited, not re-proved); what is new in-repo is the exact closed-form instrument (digamma reduction), the γ₁ = 0 bookkeeping, the regression-locked published-table match, and the placement in the wild-limit architecture. The two-mode numbers are float64 at M = 1000–1400. The Alexander material is a study section: every mathematical statement in it is either classical (cited) or labeled by its status above.

## 6. Next lemmas (both concrete)

1. **The BD-rate bridge:** relate d_k's decay rate to the windowed spectra (an inequality connecting the two meters) — even a one-sided bound would let window computations bound BD distances or vice versa, unifying the two RH-meters.
2. **The two-mode interval certificate:** IA-positivity of the 2×2 + profile-weighted complement bound (λ₂ = 0.018-margin), producing the first *certified* first-window positivity statement (or the first certified counterexample candidate).

**Source receipts:** parent `1dc31da` (PR #87); this branch `research/black-sun-iii-wild-limits-2026-10-14`; classical sources: Alexander (1924), Nyman (1950), Beurling (1955), Baez-Duarte arXiv:math/0202141 + strengthening paper, Bagchi arXiv:math/0607733 (Bagchi-weighted formulation); BM density (round 1 usage). Main untouched.
# BLACK SUN IV — The Zeno reconstruction: schedules, remaining distances, and the four-constant fight

**Campaign round 4:** 2026-10-14 (night). **Branch:** `research/black-sun-iv-zeno-completion-2026-10-14` (child of Black Sun III `1031b21`). **RH PROVED: NO.** No zero positions used as construction inputs. Sibling intake: the Alexander swarm PRs #88–90, #92 read; the branch `research/zeno-finite-global-proof-calculus-2026-10-14` (a parallel session's reservation, no Zeno commits at intake time) is noted — this round is the concrete instruments lane (schedules, floors, budgets) and complements any calculus treatment.

## 0. The thesis: finite→global proofs are Zeno completions, and SUCC's program is a Zeno audit

Zeno's dichotomy, resolved: a countable task sequence completes when there is a **summable schedule**. The general shape of every finite-to-global truth proof:

\[
\text{complete ambient space} + \text{convergent finite stages} + \text{a-priori error schedule} \;\Longrightarrow\; \text{a certified global limit}.
\]

The operator's question — *would reconstructing Zeno in SUCC help the finite→global problem?* — has a precise answer, and this round delivers it as an **audit**: every limit structure in the program either HAS an explicit Zeno schedule (and is therefore harmless: finitely certifiable to any ε) or DOESN'T (and is exactly where the open problems live). The audit's punchline: **exactly one sum in the Weil program lacks a schedule — the elementary window margin — and that gap is the entire content of the IdealHard contract.**

## 1. BS-IV-1 (PROVED LOCAL): Zeno's completion theorem and the rung schedule

**Theorem (abstract form).** Let (M,d) be complete, x_n ∈ M with d(x_n,x_{n+1}) ≤ r_n, Σr_n < ∞. Then x_∞ = lim x_n exists with d(x_n, x_∞) ≤ Σ_{k≥n}r_k, and for every ε the stage n(ε) = min{n: tail_n ≤ ε} certifies the global object within ε. (Standard proof; the content is always the SCHEDULE.)

**Instance (the Gamma rungs).** The completed Weil archimedean part is the Zeno sum of its rungs with the exact schedule (CW-10/11 constants, re-derived and 25–40-digit-verified in round 1):

\[
\varepsilon_J = \max\Big\{\frac{9}{8a_J^2}+\frac{1}{2a_J^3},\ \frac{1}{2a_J^2}+\frac{2}{a_J^3}\Big\},\qquad a_J = 2J+\tfrac12,\qquad \varepsilon_J = O(J^{-2}).
\]

**J(ε) = ⌈Θ(ε^{−1/2})⌉** (verified: J(10⁻⁴)=53, J(10⁻⁶)=531, J(10⁻⁸)=5304, each certifying ε_J ≤ ε). Empirical check on piecewise-linear test functions: measured truncation errors (1.5×10⁻³ at J=6, 4.6×10⁻⁴ at J=17) respect the a-priori schedule (7.5×10⁻³, 9.6×10⁻⁴) with a ~5× safety factor. **The infinite-rung completed form is finitely certifiable to any precision: the archimedean completion is Zeno-harmless.**

## 2. BS-IV-2 (PROVED LOCAL): the Gamma kernel IS a Zeno sum; the paradox point is the kernel singularity

**Identity (exact, verified to 40 digits).**
\[
k_G(t) = \sum_{j\ge0} e^{-(2j+\frac12)|t|} = \frac{e^{-|t|/2}}{1-e^{-2|t|}},
\]
a geometric series with ratio q(t) = e^{−2|t|}: **converges iff t ≠ 0, diverges at t = 0** — Zeno's paradox point. At the paradox point the J-partial self-sums grow like ½log J (measured: 3.25, 3.96, 4.30 at J = 10, 40, 80).

**The identification (the round's structural claim).** The paradox point t = 0 is:
- the kernel's 1/(2|t|) singularity — the source of every technical difficulty (the barrier, the E_G domain subtleties);
- **the observer's own location** (the self-pairing h(0) = ‖v‖² term — the observer cannot step away from itself);
- the round-3 wild point.

**The repair (why this is not a paradox).** The contact subtraction D_h(x) = h(x)+h(−x)−2e^{−x/2}h(0) = O(x) (proved: symmetric first-derivative cancellation) is exactly the Zeno repair: subtracting the observer's divergent self-sum makes the whole summed pairing converge. The completed Weil distribution is the *repaired* Zeno sum: the identity is exact once the self-term is handled (round 1's 25-digit verification of the full identity, including the mandatory [2a,∞) contact tail). **Zeno's paradox is not an obstacle in the completed form — it is managed, and the management is the contact structure.**

## 3. BS-IV-3 (PROVED LOCAL): the arrow — the Baez-Duarte distances as Zeno's remaining distance

The BD distances d_k (round 3's exact instrument) are Zeno's **remaining distance** of the dilation task: each new γ_l is a step of the arrow toward the closure.

**(a) Monotone:** d_{k+1} ≤ d_k (nested spans; measured: strictly decreasing through k=12).

**(b) The unconditional floor (new, one-line proof).**
\[
\boxed{d_k^2 \;\ge\; \frac{1}{L_k(L_k+1)},\qquad L_k = \mathrm{lcm}(2,3,\dots,k+1).}
\]
*Proof:* at coordinate n = L_k, every generator satisfies {L_k/l} = 0 (l | L_k), so every span element vanishes there, while γ(L_k) = 1; the squared distance is at least the coordinate weight 1/(L_k(L_k+1)). ∎ (Verified exactly for k = 1..10; the floor is valid but weak — by design: it is what is true with zero hypotheses.)

**(c) The slower-than-Zeno phenomenon.** Since log L_k = ψ(L_k-Chebyshev) ~ k (classical), the floor decays **geometrically**: the arrow is guaranteed to advance at most exponentially fast. The *measured* advance is **polynomial-slow** (~k^{−1/2}-ish: d_k√k ≈ 0.44 → 0.49 over k = 8..12): the dilation steps overlap wastefully; the arrow of this problem is far slower than Zeno's geometric arrow. The gap between the guaranteed-maximum speed (e^{−k/2}) and the observed speed (k^{−1/2}) is itself a datum: it says the γ_l are far from orthogonal steps — the "waste" is the arithmetic structure of the dilations.

**(d) Arrival is RH.** d_k → 0 ⟺ RH (Baez-Duarte/Bagchi, classical): **the arrow arrives iff RH.** Combined with (b): the arrow can never arrive at any finite stage (unconditionally), and its arrival is precisely the conjecture. This is the cleanest Zeno statement in the whole program: *the task list is infinite, each step is exact finite arithmetic, the remaining distance is monotone with an explicit unconditional floor, and the completion question is exactly RH.*

## 4. BS-IV-4 (PROVED LOCAL bookkeeping): the four-constant fight at the first window

The first-window positivity question (round 2's next lemma) is now seen to be a fight between four constants of the same scale:

| constant | value | status |
|---|---|---|
| zero-side budget B (cos-bell, a=1/2) | **1.09×10⁻³** | explicit bound, computed with no zero positions (classical counting law + the CLASSICAL-VERIFIED initial-segment fact: no nontrivial zeros with height < 14, used only as a certification bound) |
| window margin λ₀(a) | ∈ (−3×10⁻⁴, +3×10⁻⁴) unresolved; λ₀(0.36) = +8.5×10⁻⁴ | float64 Rayleigh–Ritz at resolution 3×10⁻⁶ |
| contact bookkeeping error scale | 2 log 2 = 1.386 | the fatal normalization trap scale (round 1's control) |
| resolution floor | 3×10⁻⁶ | discretization |

**The audit's verdict.** The zero-side budget (1.09e−3) and the elementary margins (≈ ±3e−4) are the same scale: neither dominates. So the Zeno-completion of window positivity requires BOTH: (i) an explicit schedule for the elementary margin — **the missing sum**: this is exactly the IH-2′/IdealHard gap (round 1 §5, round 2 §5) — and (ii) the zero-side budget above, which is now explicit. The first-window question is thus *reduced to a single unscheduled inequality at the 10⁻³ scale*; every other ingredient (contact constants, rung schedules, zero budget, resolution floor) is explicit. This is the sharpest available statement of where the finite→global problem actually stops being Zeno.

**The classical zero-free regions give no schedule.** With the de la Vallée Poussin region Re ≥ 1 − c/log T, the (β−½) factors in the zero budget are bounded by ½ − c/log T, and the budget over the full height range is O(‖v̂‖²·log-weight) = O(1)·‖v‖² — useless against 10⁻⁴ margins. Only the classical initial-segment fact (no zeros below height 14) brings the budget to the 10⁻³ scale. **Known zero-free regions cannot schedule the window margins; the required schedule is RH-grade.**

## 5. The Zeno audit table (the round's synthesis)

| SUCC limit structure | Zeno schedule | paradox point | repair | status |
|---|---|---|---|---|
| Gamma rungs → completed archimedean form | ε_J = O(J⁻²), J(ε) = Θ(ε^{−1/2}) | t = 0 self-sum | contact subtraction D_h = O(x) | **SCHEDULED (proved)** |
| prime atoms per fixed test | finite support: no Zeno needed | none | — | trivial |
| factorial-prime defect D_N → 1−γ | rate ⟺ zero-free quality (round 1 dictionary) | none | — | **SCHEDULED ⟺ strip quality** |
| ψ(x)/x → 1, A(x) − log x → const | O(x^{−δ}) ⟺ zero-free strip | β = 1 pole | Euler-constant bookkeeping | **SCHEDULED ⟺ strip** |
| dilation arrow d_k → 0 | *unknown rate; unconditional floor e^{−Θ(k)}; measured ~ k^{−1/2}* | never arrives finitely | — | **UNSCHEDULED: rate ⟺ RH** |
| window margins λ₀(a) ≥ 0 ∀a | **NO KNOWN SCHEDULE** | the 10⁻³-scale fight (§4) | IH-2′ | **UNSCHEDULED: the gap** |
| 2-adic Collatz chart | inverse limit: complete (ℤ₂) | none (profinite completion) | — | complete |

**The audit answers the operator's question.** Would reconstructing Zeno help? It helps *diagnostically*: it separates the scheduled sums (harmless, all the convergence machinery of rounds 1–3) from the two unscheduled ones (the arrow's rate; the window margin schedule) — and both unscheduled sums are RH-equivalent information. The finite→global problem in this program is *exactly* the absence of a Zeno schedule for the window margins, now isolated at the 10⁻³ scale with every other constant explicit. A proof of RH by this route IS a Zeno schedule; the reconstruction shows what such a schedule must be worth.

## 6. Status ledger and boundary

| ID | Statement | Status | Test |
|---|---|---|---|
| BS-IV-1 | Zeno completion theorem (abstract) + rung schedule J(ε) = Θ(ε^{−1/2}), verified | PROVED LOCAL + TESTED MODEL | test_schedule_* |
| BS-IV-2 | kernel = geometric Zeno sum (40-digit identity); paradox point t=0 diverges; the contact = the repair | PROVED LOCAL | test_identity, test_paradox_point |
| BS-IV-3 | arrow theorem: monotone; unconditional floor d_k² ≥ 1/(L_k(L_k+1)) (one-line proof); geometric floor vs polynomial-slow advance; arrival ⟺ RH (classical) | PROVED LOCAL (floor, monotonicity) + TESTED MODEL (rates) + classical (⟺RH) | test_floor_proof, test_measured_above_floor, test_floor_geometric |
| BS-IV-4 | zero-side budget 1.09e−3 (cos-bell, a=½, explicit constants, position-free); the four-constant table; classical regions give no schedule | PROVED LOCAL (bookkeeping) | test_budget_* |

**Boundary:** nothing proves RH. The floor theorem is small but unconditional and new-in-repo (novelty UNVERIFIED); the budget uses the classical initial-segment zero-free fact strictly as a certification bound (no positions feed any construction). The audit table's "unscheduled" verdicts are the honest state of the art, not new obstructions beyond round 2's no-go.

## 7. Next lemma (the audit's demand)

The Zeno audit isolates the task: **produce a schedule for the elementary window margin** — an explicit function g(a) with λ₀(a) ≥ g(a) ≥ −B(a) (the zero budget of §4) — or prove none exists within a natural class. The two-mode reduction (round 3) plus the interval arithmetic program is the concrete route: the 2×2's positivity at the 10⁻⁴ scale against the budget 1.09×10⁻³ is the single fight to win.

**Source receipts:** parent `1031b21` (PR #91); classical: Zeno (as resolved by the geometric series), Chebyshev ψ ∼ lcm (PNT), von Mangoldt N(T), de la Vallée Poussin region, the classical first-zero initial segment (verified computation, used as bound only); Baez-Duarte/Bagchi (arrival ⟺ RH). Main untouched.
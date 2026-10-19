# SUCC Academic Main V — Research Frontier (Thinker-Dome campaign)

**Pinned to** `integration/succ-academic-main-v-2026-10-19` (→ `main` on merge).
**Governing principle.** Local freedom is not global validity; a categorical construction is not
an original-source realization; an analytic representation is not an arithmetic proof. SUCC's job is
to make those bridges explicit, compositional and certifiable.

**Firewall (load-bearing, unchanged).** RH PROVED: **NO**. ABC **OPEN**. The authentic signed Suzuki
`S₄ = A₄ − R₄` sign is **OPEN (AMBIGUOUS)**. No positive analytic/Hilbert Gram is the signed completed
Weil form. No nontrivial zeta-zero ordinate is a construction input. `Λ(p^k)=log p`; one real archimedean
Γ; correct pole/contact, half-density/Haar, valid test-function domains. The #181 and #182 prime-two
inverse estimates are **alternatives** for the same Schur residual — **never summed** without a new
common operator inequality. A new inequality without an executable source-attested error budget (exact
rational / sound interval) is not a completed result. A green test suite is not a proof.

Each moonshot is an **independent** track on its own non-main branch with a draft PR; failure of one
does not invalidate the others. Each names base modules in the integrated tree, the smallest decisive
lemma, and its falsification opportunity.

---

## Moonshot A — Source-indexed Beck–Chevalley theorem  (priority: VERY HIGH)

**Goal.** Promote #188's constructive relational descent + existential-support adjunction to a precise
base-change theorem. For a cartesian square of source/observation carriers S'→S, O'→O with projections
q,q', investigate the constructive equivalence `g*(∃_q F) ≅ ∃_{q'}(g'* F)`. Prove it first for a genuine
set-theoretic pullback with **exact witness transport and no unrestricted choice**; then weaken the
cartesian hypothesis and build the **smallest counterexample** where base change fails; then add
original-source semantics (when does a mathematical pullback preserve a *lawful realization certificate*,
not merely a formal existential relation?).

**Base in tree.** `observational_succ/meta_choice_descent.py` (existential support, MayReport adjunction,
fiber invariance), `formal/MetaChoiceRelationalDescent.lean` (`may_report_left_adjunction`,
`support_transport_iff_fiber_invariance_choice_free`, `existential_pushforward_composes` — all verified
choice-free), plus SUCC clock quotients `rad_ris_transport.py` / `prime_phase_clocks.py` for the exact
finite example.

**Smallest next lemma.** The cartesian Beck–Chevalley iso for a finite set-theoretic pullback of SUCC
clock quotients, witness-transport explicit, Lean-checked choice-free; **plus** one non-cartesian square
where `g*(∃_q F) ≠ ∃_{q'}(g'* F)`.

**Firewall.** Do **not** claim a new Beck–Chevalley theorem (it is classical). The novelty, if any, is in
the **source-indexed adequacy conditions and operational interface** — and the realization-certificate
firewall (a preserved formal existential is not a preserved lawful realization).

---

## Moonshot B — Minimum-cost global obstruction repair  (priority: VERY HIGH)

**Goal.** Extend #188's F₂ parity-transport system. For edge constraints `t_e`, vertex assignments `x_v`,
repair costs `w_e`, study `C_* = min_x Σ_{e=(u,v)} w_e·1[x_u⊕x_v ≠ t_e]`; prove its exact relation to
weighted parity satisfaction, and for all-flip unit-weight graphs derive `C_* = |E| − MaxCut(G)`. Connect
to signed-graph frustration / Ising ground states / weighted Max-2-LIN; classify restricted graph families
with cheap exact algorithms vs. the general NP-hard case.

**Base in tree.** `observational_succ/meta_choice_descent.py` (the odd-loop obstruction, exact F₂ cochain
solver, `odd_triangle_has_no_global_section`), `formal/MetaChoiceRelationalDescent.lean`.

**Smallest next lemma.** Exact `C_* = |E| − MaxCut(G)` for all-flip unit-weight graphs, with a replayable
optimality certificate on a bounded family (e.g. all graphs ≤ 6 vertices) — exact integer costs.

**Critical nuance / firewall.** Computational complexity is **not** noncomputability — an NP-hard but
finitely computable graph problem is not an `IdealHardField`. Distinguish: repairing the model vs. adding
a probe vs. changing a transport interface vs. **illegally altering an original source law** (the last is
not a lawful SUCC repair). A probe may *reveal* an obstruction without *repairing* it.

---

## Moonshot C — Prime-clock-to-hologram naturality  (priority: HIGH)

**Goal.** Unify the categorical arithmetic spine (#184–186), Borwein machinery (#189–190), and descent
metatheory (#188). For the factorial Borwein embedding `I_N` and its source-recovering sampler `R_N` on
**precisely declared domains**, study `R_N I_N = id`, `T_{M←N} = I_M R_N`, and prove the composition law
`T_{L←M} T_{M←N} = T_{L←N}`. Transport authentic integer residue projections and SUCC shifts; require
correct phase orientation (covariance of residue projectors under `n ↦ n+1`). Construct a
**nonrecoverability counterexample**: continuous off-lattice information not recoverable from integer
samples alone.

**Base in tree.** `observational_succ/factorial_borwein_hologram.py` (I_N/R_N, range-only reconstruction),
`borwein_prime_clock.py`, `rad_ris_transport.py`, `prime_phase_clocks.py`, `green_tao_clock_ap.py`.

**Smallest next lemma.** The exact-domain composition law `T_{L←M} T_{M←N} = T_{L←N}` on the sampling
range, with the residue-projector `n↦n+1` covariance verified exactly; plus one off-lattice
nonrecoverability witness.

**Firewall.** `R_N I_N = id` holds **only on the range of `I_N`** — never globalized to point evaluation
on arbitrary L². Keep Borwein simplex factorials, Poisson jump-time factorials, and `v_p(N!)` distinct.
The goal is a coherent transport calculus, not an attractive diagram.

---

## Moonshot D — Primitive ABC triple correlations beyond the local Haar model  (priority: HIGH)

**Goal.** Pass from #187's correct local profinite p-adic valuation distributions to a **uniform** statement
over genuine integer triples `a+b=c`. Investigate, for a nontrivial `t>1/3`,
`Σ_{a+b=c≤X,(a,b)=1} ris(abc)^t ≤ C_t X²`. Begin at **t = 2/5** (not an unbounded sweep). Prove it or build
a genuine asymptotic counterexample, using prime-power divisor decompositions, CRT, Fourier orthogonality,
sieve estimates. If it holds, derive the actual improvement to the elementary exceptional-triple estimate
and compare quantitatively to the published `3/5+ε` benchmark.

**Base in tree.** `observational_succ/abc_clock_families.py` (conditional-Haar laws ABC-CLK-01/09, the
`ris^θ` moment bound ABC-CLK-02, the `X^(8/5−…)` baseline ABC-CLK-03, modular additive count ABC-CLK-13).

**Smallest next lemma.** Either a proof of the `t=2/5` bound with a source-attested constant `C_{2/5}`, or
a genuine asymptotic counterexample (extreme imbalance, deep prime powers, moving moduli) breaking it.

**Firewall.** Do **not** promote local independence to global independence. Do **not** claim an
academically competitive ABC result merely because the elementary bound improves — the honest target is a
**family-specific** result whose source-sensitive information survives a coarse moment estimate, or a
rigorous no-go theorem explaining why uniformity fails. ABC stays OPEN.

---

## Moonshot E — RH-facing source identification, without shortcutting the sign  (priority: SPECULATIVE, separate branch)

**Goal.** Ask whether the new source-certified categorical/analytic transport language helps formulate the
precise missing map between genuine SUCC/FUCC arithmetic constructions and the signed completed
Weil/Suzuki form. Demand genuine prime-power inputs, correct archimedean Γ / pole / conductor, correct
half-density and test-function domains, equality on a specified test space, independent fake-source and
non-Euler controls, and — if positivity is claimed — a proof of positivity for the **actual signed form**.

**Base in tree.** `observational_succ/certified_four_schur_trial.py` (CFS, exact two-sided Loewner
enclosure of S₄, sign CERTIFIED AMBIGUOUS), `suzuki_moment_schur.py`, `tate_suzuki_shorting.py`, and the
Academic Main IV continuation instruments (`nonvanishing_transport.py`, `prime_two_directional_holdout.py`).

**Firewall.** Do **not** infer RH from analogy, positive smoothing, finite prime windows, or a generic
Hilbert embedding. The original signed Schur `S₄` obstruction stays unresolved unless a genuinely new
certified source-specific result changes it. This is a research invitation, **not** authorization to
relabel an old conditional equivalence as a proof. The binding lever remains a sharper even-parity `κ′`
against the `1/κ = 50` amplification.

---

## Cross-cutting discipline (§7)

One principal integration writer; ≤ 2–3 concurrent **read-only** bounded audit workers; no competing full
suites. Discover any optimized rational comparator numerically, then **re-certify exactly** (Fraction /
sound interval; a float is never a certificate). Non-main branches, draft PRs, precise claim statuses per
`AGENTS.md`. No merge / tag / license / external publication without maintainer authorization; do not alter
the YEAN repository without separate authorization. Do not claim independent verification when multiple
tests share one implementation or fitted dataset.

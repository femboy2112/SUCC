# Academic Main IV — Continuation Frontier (post-merge research targets)

**Pinned to validated `main` = `4de8657`** (Operation SUCC Academic Main IV merge commit).
**Firewall (unchanged, load-bearing):** RH PROVED: **NO**. Signed four-mode Schur sign
`S₄ = A₄ − R₄` is **OPEN (AMBIGUOUS)**. No positive Hilbert covariance is the completed Weil
form; no nontrivial zeta-zero ordinate is a construction input; `Λ(p^k)=log p`; one real Archimedean
Γ; both poles/contact; half-density/Haar; valid test-function domains. A new inequality without an
executable source-attested error budget (exact rational / sound interval, with provenance) is not a
completed result.

This branch (`research/academic-main-iv-continuation-targets-2026-10-18`) opens three **independent**
tracks — failure of one must not invalidate the others. Each target names its base modules in the
integrated tree, the smallest decisive lemma, and its falsification opportunity.

---

## Target A — Source-indexed nonvanishing compactness (finite→global transport)

**Goal.** Formalize a *general* finite-to-global operator-transport criterion: given a family of
finite-section source operators with (i) **uniform boundedness**, (ii) **compatible defining
equations** across sections, and (iii) a **persistent fixed nonzero matrix coefficient** (a rank-one
or finite-rank witness that does not vanish in the limit), conclude a nonvanishing global transported
coefficient. State it as a theorem with explicit hypotheses and quantifiers, not a diagram.

**Base in tree.** `observational_succ/infinite_gamma_carleman.py` (noncompact Carleman boundary,
H¹₀ tail), `observational_succ/gamma_fredholm_completion.py`, `observational_succ/clamped_k_residual_bridge.py`;
Lean `formal/InfiniteGammaGeometric.lean`. Operator-theory audit no-go to respect: **strong operator
convergence need not imply norm convergence; a compact kernel has no fixed positive spectral gap in
infinite dimensions** — so the "persistent coefficient" must be a *matrix-coefficient* survival, not a
spectral-gap survival.

**Hostile boundary example (required control).** The **atomic–Haar** classification (#178 Institute,
`observational_succ/institute_atomic_haar.py`): a case where the transport criterion *fails* because
the fixed coefficient is annihilated in the atomic limit. A criterion that does not correctly refuse
the atomic–Haar boundary is overclaimed.

**Smallest next lemma.** A finite, source-attested witness that a specific rank-one coefficient of the
authentic Suzuki finite section survives the J→∞ limit with a rigorous remainder bound — or a
counterexample built from the atomic–Haar family.

**Falsification.** Exhibit a uniformly bounded, equation-compatible section family whose fixed nonzero
coefficient nonetheless transports to zero (the atomic–Haar shape is the prime suspect).

---

## Target B — Information repair plus online control (combined Pareto theorem)

**Goal.** A single Pareto theorem trading off (a) **retained information**, (b) **lawful acquisition
cost**, and (c) **future causal realizability**, admitting **destructive probes** and **imperfect
information**. Clearly separate what is a classical recovery (rate-distortion, online-learning regret,
feedback-capacity results) from any genuine SUCC extension.

**Base in tree.** `formal/round2/PublicBelief.lean` (nondeterministic public-belief safety),
`formal/round2/ResidueTransfer.lean`, `formal/FutureSafeForgetting.lean` (future-safe quotient),
`observational_succ/future_safe_quotient.py`, `observational_succ/lawful_history_gluing.py`; the
Institute Round II forward-only obstruction (INS-15..22). Foundations audit caution: the existing
"safety"/"descent"/"gluing" results are finite-model or Lean-kernel *local* — the Pareto frontier must
state its quantifiers and not promote a finite construction to a universal claim.

**Smallest next lemma.** For a single destructive-probe channel with one imperfect observation, the
exact three-way Pareto boundary point (retained bits, acquisition cost, realizability) as an exact
rational, with the classical special case (lossless, free, realizable) recovered as a corner.

**Falsification.** A channel where a claimed Pareto-improving repair violates future causal
realizability (an acquisition that cannot be scheduled without seeing the future).

---

## Target C — Original prime-two normalized directional inverse

**Goal.** Fix the source-valid **high comparator B** from the **prime-two mismatch of #181**
(`round2-signed`; exact rational, SHA-pinned source-high-budget audit in
`research/2026-10-18/ROUND2_FULL_PRIME_J8.json` / `J24.json`), then rigorously explore **#182's
finite-rank directional inverse methods** (`scripts/directional_source_inverse_probe.py`,
`observational_succ/source_residual_phase_savings.py`) in the **B-normalized high Hilbert/form
metric**. Validate domains, positivity, source coupling, interval errors, and **fresh high-mode
holdouts**.

**BINDING CONSTRAINT (from the Academic Main IV integration audit).** #181's prime-two saving
`C ⪰ w₀(I − A_b)` and #182's directional correction `C ⪰ Z G⁻¹ Z*` are **both lower bounds on the
same operator excess `C = D − κI`** — competing *upper* bounds on the identical Schur residual.
**Do NOT add them.** `C⪰X` and `C⪰Y` do not give `C⪰X+Y`; no common operator inequality licensing the
sum exists. Any combination must either (i) take the better single enclosure, or (ii) first PROVE a
genuine common operator inequality `C ⪰ f(X,Y)` with `f` sharper than `max`, with its own source-attested
error budget. Summing is a double-count and is refuted in advance.

**Smallest next lemma.** In the B-normalized metric, the exact (rational/interval) minimum-eigenvalue
of #181's `new_lower` on a **fresh** high-mode holdout not used to fit B — confirming or breaking the
claim that the first-window lower stays non-PSD (current status: `new_lower_PSD: False`, strict
positive saving but S₄ sign uncertified). This is the single number that would move the S₄ verdict.

**Falsification.** A fresh high-mode holdout where the B-normalized directional inverse makes the
first-window lower PSD **and** the result survives an independent-metric recomputation — which would
be a genuine (still first-window, still not all-radii, still not RH) positivity event worth escalating.

---

## Cross-cutting discipline

- One coordinator; delegate independent **read-only** audits; never run multiple full suites
  concurrently.
- Discover any optimized rational `U`/comparator numerically, then **re-certify exactly**.
- Status vocabulary per `AGENTS.md`; verify `p=2`-only activation from the support law; reuse the
  SHA-pinned frozen source (`ba075348…`), never re-derive the signed-Weil budget silently.
- A certified positive S₄ first-window margin is a first-window theorem, **not RH**.
- Non-main branch, draft PR, no merge / tag / license / external publication without maintainer
  authorization; do not alter the YEAN repository without separate authorization.

---

## Delivered this round (2026-10-18) — first exact instrument per track

All three are exact (Fraction / sound interval; float is never a certificate), carry `RH_proved:False`,
use no zeta-zero ordinate input, and were independently re-verified by the coordinator. **RH stays OPEN;
S₄ sign stays OPEN (AMBIGUOUS).**

- **A — `observational_succ/nonvanishing_transport.py`** (`tests/test_nonvanishing_transport.py`, 17 ok).
  Transport criterion + diagonal Γ heat-kernel witness: rank-one `c_J` strictly increases
  `c₁₆≈1.5515 → c₃₂≈1.5727 → c₆₄≈1.5804`, exact Cauchy remainders `≤0.173/0.036/0.0056`, structural
  floor `c_∞ ≥ exp(−1/256) > 0`. Atomic–Haar hostile control correctly **REFUSED** (coefficient → 0).
  **VERIFIED-EXACT-MODEL + HOSTILE-CONTROL-REFUSED.** OPEN: non-diagonal Suzuki OU persistence (hyp iii).

- **B — `observational_succ/repair_control_pareto.py`** (`tests/test_repair_control_pareto.py`, 11 ok).
  Exact 3-way Pareto frontier (retained-info / cost / fidelity): 7 non-dominated rational vertices;
  classical corner `(33/50,0,1)` recovered and verified unreachable at zero cost; acausal + premature
  falsifiers rejected. **VERIFIED-EXACT-MODEL** (corner CLASSICAL). Caveat: order-2 (Gini) info measure,
  not Shannon; static schedules.

- **C — `observational_succ/prime_two_directional_holdout.py`** (`tests/test_prime_two_directional_holdout.py`, 16 ok).
  Fresh holdout (B fit J8/M80, eval J24/M192): B-normalized corrected lower is **negative-definite both
  sectors** (det>0 ∧ trace<0, exact) → `fresh_holdout_flips_S4_sign=False`, **S₄ OPEN**. Never-sum rule
  enforced in code (`better_single_enclosure` / `reject_double_count`). **VERIFIED-EXACT-MODEL**; refutes
  only "a fresh holdout flips the first-window sign". Binding constraint still the `1/κ=50` amplification
  / sharper even-parity `κ′`.

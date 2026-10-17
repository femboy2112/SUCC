# SUCC post-Academic-Main-II proof frontier (2026-10-16)

**Status:** research frontier / dependency graph. Establishes targets; proves nothing new by itself.
**RH PROVED: NO.** Companion to
[`ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md`](ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md) and
[`SUCC_FUCC_TATE_WEIL_NEXT_CAMPAIGN.md`](SUCC_FUCC_TATE_WEIL_NEXT_CAMPAIGN.md).

Prioritized by **mathematical leverage × falsifiability × reuse**. Speculative moonshots are marked
`[MOONSHOT]`; already-refuted routes are marked `[DEAD]` with their receipt so they are not re-walked.

## Dependency graph (what blocks what)

```
                       [certified two-sided enclosure of S_4]  (DONE this round, VERIFIED EXACT MODEL)
                                        |
                 +----------------------+----------------------+
                 |                                             |
   (F-I.a) sharper high-sector κ                  (F-I.b) §3C certified tail modulus
   (a better theorem than D_4 ⪰ K/50)             (certified high-Legendre decay)
                 |   \                                   /   |
                 |    \-------- both needed -------------/    |   (either alone is NOT sufficient:
                 v            for a certified-positive S_4        §5 shows 1/κ amplification binds)
        [decisive sign of S_4 at a=1/2]  ---- first-window only, NOT RH ----+
                 |                                                           |
                 v                                                          v
        (F-I.c) all-radius generalization  ----------------------------> [RH-equivalent] OPEN
                                                                          FIREWALL. RH PROVED: NO.

 independent tracks (meaningful regardless of the S_4 sign):
   F-II  SUCC×FUCC categorical arithmetic  (V_p S = S^p V_p braid, carries, group completion)
   F-III finite-observer resonance horizon (effective finite Weil-negative witness complexity)
   F-IV  proof-producing SUCC×YEAN         (exact rational Gram/Schur -> checkable kernel; uses the
                                            CLAIM_NAMESPACE_REGISTRY FQIDs as stable proof keys)
   F-V   observer / proof-access           (SUCC-λ, E-ladder consensus, causal gluing, trilemma)
```

---

## FRONTIER I — Source-derived Weil positivity (the `S_4` sign and its all-radius lift)

* **Established inputs.** Certified two-sided enclosure `A_4−L_U−50T_{r_U} ⪯ S_4 ⪯ A_4−L_U`
  (`certified_four_schur_trial`); `A_4 ≻ 0` (certified `J=64`); `D_4 ⪰ K/50` (WB4); `‖g′‖₁<11/40`.
* **Classical dependencies.** Schur/Feshbach shorting, Loewner order, Douglas range, Legendre
  transform, Haynsworth quotient; completed-ξ explicit formula (CTW-08) for the source.
* **Missing theorem.** Either (a) a high-sector coercivity `κ' ≫ 1/50` sharp enough that
  `A_4 − L_U − (1/κ')T_{r_U} ⪰ 0` for an attainable `U`, or (b) a residual theorem avoiding the full
  `1/κ` factor. §5 shows **(b-tail alone is insufficient)**: even the tight continuum residual leaves
  the lower bracket negative-definite, so `κ` (not Young slack) is binding.
* **Hypotheses / domain.** `a = 1/2`, mean-zero `L²₀`, prime-2-only support; `U` finite rational
  parity-respecting; `K = V*V`.
* **Adversarial counterexample / control.** The §6 exact no-go: a large coercivity on a decoupled
  high direction does **not** rescue a Schur negative driven by a near-null intermediate direction —
  so a bigger `κ` must act on the **coupled** sector, not merely exist. Also `[DEAD]` "high ⇒ full"
  (REFUTED, DAG firewall) and "positive Gram ⇒ signed-form positive" (REFUTED, O12 / CTW-12).
* **Reproducible procedure.** `scripts/certified_four_schur_trial_probe.py`; sweep `κ'` candidates
  from `arithmetic_resolvent_probe` sharper caps (odd `405.../891…`, even `107.../127…`).
* **Predicted observable that discriminates.** If `κ` is binding, the certified lower-bracket
  min-eig scales ≈ linearly in `κ`; if the §3C tail is binding, it scales with the diagnostic
  finite-mode Gram gap. (This round: the former — tight residual still negative.)
* **Possible proof certificate.** Exact rational PSD (LDL) of the lower bracket per parity block.
* **Cost.** Low for the certified sweep (seconds–minutes, `J ≤ 64`); the `κ'` theorem is hard analysis.
* **Independent branches.** `F-I.a` (coercivity) and `F-I.b` (tail modulus) proceed independently;
  both feed the sign.
* **Smallest result that moves the verdict.** A certified `κ' > (11/40)² / λ_min(A_4−L_U)` on the
  **even** parity block (the tightest block, margin ≈`9.25·10⁻⁸`) for one attainable rational `U` → `POSITIVE_CERTIFIED`
  on that block.

## FRONTIER II — SUCC × FUCC categorical arithmetic `[partly MOONSHOT]`

* **Established inputs.** Factorial→Gamma moment lift + prime-FUCC Tate–Mellin transport
  (#145/#146, `factorial_gamma_fucc`, `tate_mellin_prime_transport`); carrier reconstructions (EC).
* **Classical dependencies.** Group completion `B(N)→Z`, `p`-adic valuation/carries, Mellin–Gamma.
* **Missing theorem.** A coherent braid `V_p S = S^p V_p` with its higher coherence (which diagrams
  commute strictly vs only up to a noninvertible correspondence/quotient). Which structures transport
  strictly across additive↔multiplicative carriers.
* **Hypotheses / domain.** Finite carriers first; colimit only with an explicit density + uniform
  bound (cf. Proof-Teeth completion arrow — strong convergence but `‖I−Pn‖=1`).
* **Adversarial control.** A diagram that is *visually* a transport but fails a coherence law at the
  level of actual maps (AGENTS.md item 9); a carry that breaks strict preservation.
* **Reproducible procedure.** Exact finite SUCC/FUCC affine-law checks; small categorical models.
* **Predicted observable.** A universal property (initiality/terminality) that pins the Gamma
  transport, vs merely a numerically-matching reconstruction.
* **Possible proof certificate.** Exact affine SUCC/FUCC identities + a finite commuting-diagram check.
* **Cost.** Low–medium (finite algebra). **Independent of the `S_4` sign.**
* **Smallest result.** One strictly-preserved braid relation with a finite exact witness and one
  explicit obstruction where only a noninvertible comparison exists.

## FRONTIER III — Finite-observer resonance horizon `[MOONSHOT]`

* **Question.** If an RH counterexample were astronomically deep, what smallest finite arithmetic /
  spectral witness must it force, and how much observation detects it?
* **Established inputs.** Finite Weil-negative test machinery (`gaussian_weil_certificates`, log2/log5
  bump witnesses, `W<−19/75`); Li-coefficient / inverse-Mellin transport.
* **Classical dependencies.** Weil explicit formula, Li's criterion, prime-counting error terms.
* **Missing theorem.** An effective bound: existence → **effective construction** → **computable upper
  bound** on first-witness complexity. Distinguish existence, construction, computable bound,
  heuristic, and an intrinsic finite-observer obstruction.
* **Adversarial control.** A fake composite source (no prime-6 atom) that mimics the cheap finite
  positivity but differs at the first genuine hinge — the observability discriminator.
* **Reproducible procedure.** Finite log-prime-clock sampling + exact bump-test sweeps.
* **Predicted observable.** A finite "resonance horizon" `N*(a)` beyond which no new sign information
  appears at radius `a`.
* **Possible proof certificate.** An exact finite witness + a proven aliasing/undersampling bound.
* **Cost.** Medium. **Independent of `S_4`.** **Smallest result:** a proven finite resonance horizon
  for one radius, even without RH.

## FRONTIER IV — Proof-producing SUCC × YEAN

* **Established inputs.** Exact rational Gram/Schur/PSD certificates everywhere in this stack; the new
  `CLAIM_NAMESPACE_REGISTRY.json` + `claim_namespaces.fqid(...)` giving **stable unique FQIDs**
  (`PH.PROF-01`, `PH.PFH-01`, …) usable as kernel/Lean identifiers; YEAN proof-kernel branches (YX).
* **Classical dependencies.** Lean/kernel checking of finite linear algebra (rational PSD, Schur
  enclosure); provenance/normalization passports.
* **Missing theorem.** A precise certificate pipeline: exact-Python PSD/Schur → a small independently
  checking kernel, with the assumptions separating **finite formal proofs** from **infinite analytic
  theorems** made explicit (a Lean proof of a finite matrix does **not** formalize the analytic Suzuki
  theorem).
* **Adversarial control.** A finite PSD certificate that is *true* but whose analytic lift is
  unproved — the pipeline must refuse to over-claim.
* **Reproducible procedure.** Emit the certified parity-block LDL of a bracket as a rational
  certificate keyed by FQID; check in-kernel.
* **Predicted observable.** A kernel-checked rational PSD certificate whose FQID resolves uniquely via
  the registry (collision-guarded by `test_claim_namespace_collisions`).
* **Cost.** Medium; YEAN work needs a separate coordinated branch + version pins (do **not** touch the
  YEAN repo from here). **Smallest result:** one bracket's PSD certificate kernel-checked end to end.

## FRONTIER V — Observer / proof-access mathematics

* **Established inputs.** SUCC-λ observation calculus, E-ladder consensus, collective observers
  (#139/#143/#144, consensus now clean — no `KeyError:'kind'`), causal gluing, Simple/IdealHard/
  Fucked/Unresolved trilemma (SCF).
* **Classical dependencies.** Finite-intersection-property gluing (nonconstructive), inverse limits,
  Haar/finite-cyclic structure.
* **Missing theorem.** A useful statement of **when** collaborating observers (or a new lawful source
  construction) reveal a distinction inaccessible to any earlier single observational interface —
  without identifying physical realization with mathematical existence.
* **Adversarial control.** The phantom source-map no-go (`∀N∃z` vs `¬∃z∀N`); noncompact escape →
  empty limit; a cooperative policy that gains nothing a single observer lacked.
* **Reproducible procedure.** `collective_*` probes; exact finite consensus/pool algebra.
* **Predicted observable.** A finite instance where a two-observer join strictly decides a property no
  single interface can.
* **Cost.** Low–medium. **Independent of `S_4`.** **Smallest result:** one exact finite join-reveals-
  distinction instance with a matched single-observer impossibility.

---

## Priority ranking (leverage × falsifiability × reuse)

1. **F-I.a (sharper `κ`)** — highest leverage; this round proved it is the binding constraint on `S_4`.
2. **F-I.b (§3C certified tail modulus)** — necessary for a tight certified lower bracket; reusable.
3. **F-IV (SUCC×YEAN certificate pipeline)** — turns every exact Gram/Schur result into a checkable
   artifact; compounds across the whole stack.
4. **F-II / F-III / F-V** — independent of the sign, each with a small falsifiable first result.

The one-line verdict mover: **a certified high-sector coercivity `κ'` acting on the even (tightest)
parity block, large enough to beat `(11/40)²/λ_min`, for one attainable rational `U`.**

# Next campaign — reusable prompt (post-CertifiedTrial)

Directly reusable seed for the next Claude/Codex/DeepSeek research round, pinned to the exact
resulting code and proven state of branch
`research/original-four-schur-certified-trial-2026-10-16`. **RH PROVED: NO.**

---

**Mission.** The certified two-sided Loewner enclosure of the original four-mode Suzuki/Weil Schur
complement `S_4 = A_4 − R_4` at `a = 1/2` is built and verdict is **CERTIFIED AMBIGUOUS**
(`observational_succ/certified_four_schur_trial.py`). This round proved the binding constraint is the
**`1/κ = 50` amplification** of the residual energy, not estimate conservatism: at the numerically
optimal high response `U`, the tight residual bracket `A_4 − L_U − (1/κ)C_quot` is itself
negative-definite. Your job is to attack the **one verdict-moving lever** and the one enabling lemma.

**Primary target (F-I.a — leverage).** Prove a **sharper high-sector coercivity**
`D_4 ⪰ κ' Q_4 K Q_4` with `κ' ≫ 1/50`, acting on the sector the low space actually couples to —
specifically beating `κ' > (11/40)² / λ_min(A_4 − L_U)` on the **even** parity block (the tightest
block of `A_4`, certified margin ≈ `9.25·10⁻⁸` unnormalized at `J = 64`). Candidate starting points:
the sharper `R_0` caps already computed by `scripts/arithmetic_resolvent_probe.py` (odd
`405333569368851711757618861801/891024077979000000000000000000`, even
`107959895025855318145227769087/127289153997000000000000000000`); the 30-mode coercivity
`κ_30 = 369/10000` — but note the exact no-go in `observational_succ/four_thirty_schur_transport.py`:
`κ_30` does **not** transport through the signed modes-5..30 shorting, so a larger `κ` must act on the
coupled four-mode complement, not merely exist higher up.

**Enabling lemma (F-I.b — §3C modulus).** Prove a **certified high-Legendre-coefficient decay /
effective derivative-Gram tail modulus** for the source response `G Vx`, so the finite-mode residual
Gram diagnostic in `certified_four_schur_trial._finite_mode_residual_gram_diagnostic` becomes a
rigorous **upper** bound on `T_{r_U}` (the kinks of `g′` — the prime-2 hinge step and the `|r|`
corner — suggest an `H^{1/2}`-type `O(1/M)` modulus). Necessary for a tight certified lower bracket;
by this round's finding it is **not sufficient** alone — you still need F-I.a.

**Discipline (hard).** Reuse the pinned source (`source_weil_hierarchy`, blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`); `Λ(p^k)=log p`, `Λ(4)=Λ(8)=log2`, no composite-6 atom,
`n^{-1/2}` half-density, one real `Γ_ℝ`, both poles, contact, `K = V*V`, `K^{-1} = −Δ_N`. Verify the
`a=1/2` prime-2-only activation from `authenticated_prime_wavefront`, never a hard-coded cutoff.
Exact rational / sound interval only — mpmath is **discovery**, never a certificate. Separate
candidate `U` discovery from proof: discover numerically, re-certify with `CertifiedTrial`. No
nontrivial zeta-zero coordinates as inputs. A certified positive `S_4` is a **first-window** theorem,
not RH; a certified negative direction demands hostile independent verification with an exact rational
witness. Non-main branch, draft PR, no merge without authorization.

**Verdict gate.** Run `scripts/certified_four_schur_trial_probe.py`; a `κ'` is decisive iff
`CertifiedTrial` returns `POSITIVE_CERTIFIED` (exact LDL of the lower bracket, both parity blocks) for
an attainable rational `U` — or `NEGATIVE_CERTIFIED` with a surviving exact witness.

**Parallel independent tracks (meaningful regardless of the `S_4` sign).** F-II SUCC×FUCC categorical
braid `V_p S = S^p V_p`; F-III finite-observer resonance horizon; F-IV SUCC×YEAN certificate pipeline
(use `claim_namespaces.fqid(...)` FQIDs as stable kernel keys); F-V observer/proof-access
join-reveals-distinction. See
[`SUCC_POST_MAIN_II_PROOF_FRONTIER.md`](SUCC_POST_MAIN_II_PROOF_FRONTIER.md).

**Deliverables.** Certified `κ'` theorem or a precise no-go; certified §3C tail modulus or named wall;
updated `CertifiedTrial` verdict; comparison table vs this round's enclosure; draft PR; A–G report.

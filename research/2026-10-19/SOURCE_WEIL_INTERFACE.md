# Source → Signed Completed Weil/Suzuki Interface (Moonshot E)

**Campaign.** SUCC Academic Main V — Thinker-Dome, Moonshot E (SPECULATIVE,
most firewall-sensitive track).
**Branch.** `research/amv-moonshot-e-rh-source-2026-10-19` (base `origin/main` = `455600a`).
**Artifacts.** `observational_succ/source_weil_interface.py`,
`tests/test_source_weil_interface.py`, this document.
**Status of the deliverable.** **RESEARCH INVITATION + firewall scaffold.** It is
**NOT** a proof, **NOT** a new theorem, and **NOT** a relabeling of an old
conditional equivalence. It FORMULATES a precise open obligation and makes a
claimed identification *mechanically refuse to certify* until that obligation is
discharged.

---

## 0. Firewall (load-bearing, verbatim)

> RH PROVED: **NO**. Signed `S₄ = A₄ − R₄` sign **OPEN (CERTIFIED AMBIGUOUS)**.
> Do NOT infer RH from analogy, positive smoothing, finite prime windows, or a
> generic Hilbert embedding. A positive covariance/Gram is **NOT** the completed
> Weil form. **No** nontrivial zeta-zero ordinate as a construction input.
> #181/#182 inverses are **alternatives, NEVER summed**. Exact arithmetic only.

---

## 1. The target object (CLASSICAL)

Let `φ` be an admissible test function on a specified finite test space. The
*completed Weil explicit-formula distribution* for `ζ_Q` is the **indefinite**
quadratic form

```
W(φ) = A_∞(φ)  +  P(φ)  +  C_G(φ)  −  Σ_{p prime, k≥1} (log p) · φ̂(k·log p)      (★)
```

- `A_∞(φ)` — the **one** real archimedean Γ-factor term (digamma/Γ′/Γ);
- `P(φ)` — the pole term (the `s = 0, 1` poles of the completed ξ);
- `C_G(φ)` — the contact/conductor constant term (`−ψ(1/4) + log π`, conductor 1);
- the **prime sum** carries `Λ(p^k) = log p` and enters with a **minus sign**.

**Status: CLASSICAL** (Weil 1952; Suzuki's half-density normalization at
`a = 1/2`). The minus sign is the whole point: `W` is **not** a positive
Gram/covariance. *Weil positivity* — `W(φ) ≥ 0` for all admissible `φ` — is
**equivalent to RH** and is **OPEN**.

---

## 2. The typed obligation (what an identification must supply)

An *identification* is a claim that a genuine SUCC/FUCC arithmetic construction
realizes `(★)`. The interface `certify_source_to_weil(offer)` treats this as a
typed obligation and refuses to certify unless **every** item below is supplied.

### 2.1 Required inputs (each must be present and genuine)

| # | Obligation (key) | Requirement | Primitive it is checked against |
|---|---|---|---|
| 1 | `genuine_prime_power_inputs` | prime-power tape `= ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2))`, each place a genuine prime, `Λ(p^k)=log p` | `source_weil_hierarchy.AUTHENTIC_TAPE`, `tate_suzuki_shorting.prime_power_parent / is_genuine_prime` |
| 2 | `archimedean_gamma_present` | exactly one real Γ factor | `TateSourcePassport.real_gamma_count == 1` |
| 3 | `completed_pole_and_contact` | pole term **and** contact `C_G` term present | `source_weil_hierarchy.contact_iv` (reproduced, not assumed) |
| 4 | `conductor_one` | conductor `= 1` | `TateSourcePassport.conductor == 1` |
| 5 | `half_density_haar` | half-density `1/2`, self-dual Gaussian scale `1` (Tate Haar) | `TateSourcePassport.half_density == 1/2`, `gaussian_scale == 1` |
| 6 | `valid_test_function_domain` | finite, in-domain, mean-zero; **no** zero-ordinate input | finite `test_space_id`, empty `zero_ordinate_inputs` |
| 7 | `fake_source_control_rejected` | a matched **fake-composite** control supplied and refused by the construction | §4(b) |
| 8 | `non_euler_control_rejected` | a matched **non-Euler** control supplied and refused | §4(c) |

### 2.2 The exact equality on the specified finite test space (OPEN)

> **Specified test space.** `F₄ = span{ P₁(2t), …, P₄(2t) }` (the four even/odd
> Legendre derivative carriers) in `L²₀(−1/2, 1/2)` at `a = 1/2`, with the single
> active prime atom `p = 2` (`authenticated_prime_wavefront(1/2) = ((2,2),)`).
> Interface id: `F4_legendre_derivative_carrier_a_half_p2`.

> **Obligation `signed_source_to_weil_morphism_equality` (CARDINAL, OPEN).**
> Prove that for **every** `φ ∈ F₄`, the SUCC-constructed signed quadratic value
> `Q_SUCC(φ)` equals `W(φ)` of `(★)` — matching the archimedean, pole, contact
> **and signed prime** channels term-by-term, as **exact rationals / sound
> intervals**, with an executable source-attested error budget. This is the
> *signed source→Weil morphism*. **It is not supplied by any currently available
> construction.**

### 2.3 The positivity obligation (CARDINAL, OPEN — only if positivity is claimed)

> **Obligation `signed_form_positivity_proof_for_actual_form`.** If positivity is
> claimed, supply a proof of positivity for the **actual signed form** `(★)` —
> **not** for a positive surrogate Gram/covariance. The current best construction
> yields the certified Schur complement `S₄ = A₄ − R₄` whose sign is **CERTIFIED
> AMBIGUOUS** (`certified_four_schur_trial.CertifiedTrial`, verdict `AMBIGUOUS`).
> Hence this obligation is **OPEN**.

### 2.4 Why the two cardinal obligations are structurally undischargeable here

Both are **proofs over an infinite admissible class / operator positivity**, not
data. The interface exposes only boolean *claim* flags for them; asserting such a
flag is recorded as a **rejected input** (“a boolean is not a proof”), never as a
discharge. Consequently `certify_source_to_weil` **can never return
`identified: True`** on anything available — `identified` is hardcoded `False` and
`signed_source_to_weil_morphism_equality` is appended to `missing_obligations`
unconditionally. (Tested: source scan for any `identified = True` literal;
adversarial battery; maximally-compliant offer.)

---

## 3. What the interface returns

```
{ identified: False,                       # structural; no code path sets True
  missing_obligations: [ … ],              # includes the cardinal OPEN item(s)
  rejected_inputs: [ {input, reason}, … ], # firewall refusals
  satisfied_obligations: [ … ],
  open_obligation: "<morphism + S₄ sign, in words>",
  s4_sign: "OPEN (CERTIFIED AMBIGUOUS)",
  RH_proved: False, exact_arithmetic_only: True, firewall: {…} }
```

**Fed the actual current best source construction** (`genuine_source_offer()`,
which wires `verify_original_suzuki_source`, `TateSourcePassport`,
`authenticated_prime_wavefront(1/2)` and `reconfirm_s4_ambiguous`):

- `identified = False`;
- `rejected_inputs = ()` (the honest genuine offer passes every reject gate);
- `satisfied_obligations` = obligations **1–8**;
- `missing_obligations = (signed_source_to_weil_morphism_equality,
  signed_form_positivity_proof_for_actual_form)` — i.e. the signed source→Weil
  morphism **and** the `S₄` sign, both OPEN.

---

## 4. Negative controls (each constructed explicitly; each REJECTED)

| | Control (constructor) | Rejected input | Reason |
|---|---|---|---|
| a | `control_positive_gram_as_signed_form` | `offered_form` | a PSD Gram/covariance is not the **indefinite** `(★)` |
| b | `control_fake_composite_lambda6` | `prime_power_tape` | `6 = 2·3` is not a prime power (`prime_power_parent(6) is None`); `Λ` lives only on prime powers |
| c | `control_non_euler_matched` | `euler_product` | a matched source without genuine Euler factorization is not the arithmetic source |
| d | `control_zeta_zero_ordinate_input` | `zero_ordinate_inputs` | a nontrivial zeta-zero ordinate is a **forbidden** construction input (numeric ordinates are refused at the door; only a forbidden *token* can even be offered) |
| e | `control_finite_window_as_all_height` | `positivity_scope` | all-height positivity on finite-window evidence; a finite prime window is not all height |

All five yield `identified: False` with the stated rejection. (Tested.)

---

## 5. The `summed_inverse_guard` (#181/#182)

`#181` (`full_prime_resolvent`, “full prime-two inverse for the original signed
Schur bound”) and `#182` (Theorem Forge II source repair) are **alternative**
Loewner-lower enclosures of the **same** prime-two Schur residual. Summing them
double-counts one residual and yields an **unsound** Loewner inequality.

- `summed_inverse_guard(a, b, operation="sum")` → **raises** (refused for two
  alternatives of the same residual; lawful only under a NEW, separately proved
  common operator inequality);
- `summed_inverse_guard(a, b, operation="select_better")` → returns the single
  better enclosure (largest `loewner_lower_min_eig`).

The estimate scalars are **exact Fractions** (floats refused). The illustrative
stand-in values are both negative-definite (no actual negative source energy is
established); they exercise the guard’s algebra, not a numeric bound claim.

---

## 6. Claim ledger rows (this deliverable)

| ID | Claim | Domain / quantifiers | Status | Receipt | Next falsification |
|---|---|---|---|---|---|
| SWI-E1 | `certify_source_to_weil` never returns `identified: True` on available inputs | all `SourceWeilOffer` | **CERTIFIED (structural)** | source scan + adversarial battery (`tests/test_source_weil_interface.py`) | exhibit an offer that flips `identified` |
| SWI-E2 | the five negative controls are each rejected with the specified input | the 5 constructed controls | **CERTIFIED** | `NegativeControlTests` | a control that slips an identification through |
| SWI-E3 | the actual current best construction → `identified: False`, missing = {morphism, positivity}, 0 rejects | `genuine_source_offer()` | **OBSERVED** | `GenuineConstructionTests` | a construction discharging either cardinal obligation |
| SWI-E4 | `#181/#182` prime-two inverses are never summed | `summed_inverse_guard` | **CERTIFIED (firewall)** | `SummedInverseGuardTests` | a proved common operator inequality that licenses a sum |
| SWI-E5 | signed source→Weil morphism equality on `F₄` | `∀ φ ∈ F₄` | **OPEN (research invitation)** | §2.2 | construct `Q_SUCC` and match `(★)` term-by-term, exactly |
| SWI-E6 | `S₄ = A₄ − R₄` sign | `a = 1/2`, four-mode | **OPEN (CERTIFIED AMBIGUOUS)** | `reconfirm_s4_ambiguous` reuses CFS | a certified sign (either direction) with an exact witness |

**Adversarial countermodels retained.** (i) A positive Gram looks like a form but
is the wrong (definite) object — §4(a). (ii) A finite prime window looks like “all
primes” but is not all height — §4(e). (iii) A matched non-Euler / fake-composite
source reproduces low moments without the arithmetic — §4(b,c). (iv) A zeta-zero
ordinate would trivially “close” the loop and is therefore forbidden — §4(d).

---

## 7. The exact open obligation (the invitation)

> **OPEN.** Construct the signed source→Weil morphism: an exact proof that the
> SUCC-constructed signed completed form equals the Weil/Suzuki distribution
> `(★)` on the specified finite test space `F₄`, with an executable
> source-attested error budget — **and**, to claim positivity, a proof of
> positivity for the **actual signed form** `(★)`. The certified Schur complement
> `S₄ = A₄ − R₄` sign remains **AMBIGUOUS**. **Both remain OPEN.** Nothing in this
> deliverable moves RH; it only makes the missing map precise and refuses every
> shortcut around it.

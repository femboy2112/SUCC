# Front B claim ledger (Main XX, 2026-11-05)

Every row has a domain, a status, a receipt, and the next falsification opportunity. Nothing here promotes π normality.

Mapping to the `docs/METHOD.md` ledger vocabulary:
- PROVED → PROVED LOCAL (paper proof within the stated domain)
- PROVED-CONDITIONAL and EQUIVALENT-REFORMULATION → PROVED LOCAL, with the hypothesis stated, **no status promotion**
- CERTIFIED-FINITE → TESTED MODEL (exact certified finite range)
- OPEN → HYPOTHESIS / open target

These are same-model results with hostile same-model review (`hostile_review/REVIEW.md`). They are not independently refereed.

| ID | Statement (short) | Domain / hypotheses | Status | Receipt | Next falsifier |
|---|---|---|---|---|---|
| CB-1 | `b_{n,m,k}=1[S_m(n+k)≤x_{n+d}<S_d(n)]`, `δ=S_d(n)−S_m(n+k)` | any seed; forcing positive on `(n,n+d]`; `S_d(n)<1` | **PROVED** (exact case analysis) | PROOFS.md §CB-1; `tests/test_selected_orbit.py` (definition path = window path on every admissible triple at A=64,173; seed 1/5; one-pole mutant); two independent oracles: 591,175 admissible cases, 0 mismatches; first inadmissible depth fails as expected (`numerics/VALIDATION.md` §2) | any exact mismatch at an admissible triple |
| CB-1g | gauge form `b=1[16^mT_{n+k}≤z_{n+d}<16^dT_n]`, `z_j={16^j(s+π/16)}` | `16^dT_n≤1` | **PROVED** | PROOFS.md; rigorous `T_n` enclosures; 118,235 admissible cases, 0 mismatches by two z-routes, min endpoint margin 1.07e-5 (`numerics/VALIDATION.md` §3) | mismatch with `16^dT_n` near 1 |
| CB-1c | coherent seed `α=0` ⇒ `b≡0` on every admissible triple | `s_*=−π/16` | **PROVED** (corollary; reproves #521 CT-03 on the same domain — an earlier "generalises" claim was REFUTED by hostile review) | PROOFS.md Cor. 2; hostile_review/REVIEW.md | — |
| CB-0 | admissibility law: admissible ⟺ `A≥2^{2d−3}` ⟺ `c_A(d)≤1` ⟺ CT-03 domain | original forcing | **CERTIFIED-FINITE** for `2≤d≤200` (0 exceptions); OPEN beyond (asymptotic margin `≈1.125/2^{2d−3}`) | `admissibility_law.py` (Lean-backed `duck_bbp` enclosures); refuter `p5_domain.py` | a `d>200` exception |
| CB-1e | Haar-seed carry moments (#521 CT-05/06) carry no selected-seed information | Haar seed ensemble | **PROVED** (corollary) | PROOFS.md Cor. 4 + #522 HS-06 | — |
| CB-2 | (H1) frequency existence ∧ (H2) lattice smallness ⟹ `ν`=Haar; under (H1) `J`-smallness ⟺ normality | any seed | **PROVED-CONDITIONAL** (a conditional equivalence; not π progress) | PROOFS.md §CB-2 (Lemmas 2.1–2.4) | a non-Haar `ν` with `Ψ(c)=Ψ(c16^{-k})` ∀c,k |
| CB-2′ | (LS) log-scale local stationarity ∧ (H2\*) ⟹ normal | any seed | **PROVED-CONDITIONAL** | PROOFS.md §CB-2′ | a stationary (LS) non-normal orbit with `J→0` |
| CB-3 | a same-forcing non-normal seed has `sup_admissible|J|→0` | a.s. realisation of the lattice-calibrated Bernoulli digit model | **PROVED** (refutes "J-family ⟹ normality") | PROOFS.md §CB-3; construction check: residual 9e-60, `p_0=1/16` exactly; exact `max|E J|≤2.7e-7`; non-normality witness `f1−f2=0.0098±0.0007` vs iid null `0.0002±0.0005` at N=262144 (`numerics/FINITE_RECEIPT.json`, `numerics/data/cb3.json`); refuter `p4_cb3.py` | a lattice threshold escaping calibration |
| CB-4 | normal ⟺ (LS) ∧ (H2\*); both conjuncts strictly weaker | any seed | **EQUIVALENT-REFORMULATION** (proved; not progress) | CB-2′ + CB-3 + non-uniform Bernoulli generic point | — |
| CB-5 | second-order selected carry statistic `J2_{A,ℓ}=A^{-1}Σ[b_nb_{n+ℓ}−Leb(I_n∩T^{-ℓ}I_{n+ℓ})]` separates CB-3 from Haar **in exact expectation** (`E J2≈1.44e-5`, constant in A for ℓ=1), while first-order `J` does not | CB-3 measure, A≤2^17, three representative triples, ℓ≤3 | **OBSERVED-FINITE** (exact expectations; not resolvable by a single sequence at A≤2^17 — needs A~10^9 by the measured noise ≈0.47/√A) | `numerics/data/j2.json`, `numerics/VALIDATION.md` §6 | a calibrated second-order countermodel (CB-6 conjecture) |
| CB-6 | hierarchy conjecture: for every finite order q, some non-normal same-forcing seed has every selected carry statistic of order ≤q vanish | — | **CONJECTURE** | CB-3 is q=1; CB-5 shows q=1 calibration does not reach q=2 | build the q=2 Markov lattice-calibrated model |
| CB-OPEN-1 | `J_{A,m,k}(0)→0` for the zero seed | zero seed | **OPEN** | finite exact values change sign across epochs (e.g. A=173 (4,1): −3.724e-2; A=691 (5,1): +1.622e-3; A=4096 (6,1): −2.203e-3) — OBSERVED-FINITE, `numerics/data/trueseed.json` | — |
| CB-OPEN-2 | (LS) or frequency existence for the zero seed | zero seed | **OPEN** | — | stationarity statistic Λ_A (NEXT.md) |
| — | π base-16 normality; fixed-h Weyl `S_N(h)=o(N)`; `Q_{1/2}(μ_A)→0`; RH | — | **OPEN** | — | — |

**Corpse kept.** Favourite before the crucible: "the critical carry innovation family `J_{A,m,k}(0)→0` transports to fixed-h Weyl". It is **REFUTED as an unconditional transport** by CB-3: the J-family can vanish on a non-normal orbit of the same forcing. **Corrected formulation:** CB-2/CB-2′. These are conditional on stationarity, and the stationarity they need is itself open for π.

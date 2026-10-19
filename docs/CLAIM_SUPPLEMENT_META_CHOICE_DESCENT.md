# Claim supplement — source-certified generative choice and descent (MCD)

**Date:** 2026-10-19. **Parent:** `main@4de865766d53ea448555386d98f3e88e3ec605b6`.  
**Full definitions, paper proofs, controls and academic references:** [SUCC metatheory manuscript](../research/2026-10-19/SUCC_META_GENERATIVE_CHOICE_DESCENT.md).  
**Scope:** witnessed construction, relational quotient transport, exact finite `F_2` graph cocycles. No general topos compiler, physical source authentication, or RH result is claimed.

| ID | Statement | Status and evidence | Countermodel, boundary, next gate |
| --- | --- | --- | --- |
| MCD-01 | Witnessed dependent choice `(Πx Σy R) → Σf Πx R` by projection | CLASSICAL / CONSTRUCTIVE TYPE-THEORETIC | Does not extract data from arbitrary `Prop`-level `∀x∃y` |
| MCD-02 | In elementary topos, every epi splitting entails Boolean internal logic | CLASSICAL — Diaconescu 1975 | REFUTES unrestricted internal AC alongside globally non-Boolean logic; do not conflate local witnesses |
| MCD-03 | Source support compatible on `q`-fibers iff some `Prop`-valued successor relation descends; no surjectivity/AC required | PROVED PAPER; Lean declarations added, kernel gate to check | Not a deterministic witness selector; `support_transition_exists_choice_free`, `support_transport_iff_fiber_invariance_choice_free` |
| MCD-04 | Fiber-invariant May/CommonPossible coincide at all reports even for nonsurjective `q` | REFUTED (unreachable report: empty may, vacuously true common) | Corrected on image; `exact_envelopes_on_image_choice_free`, `empty_observation_fiber_separates_envelopes` |
| MCD-05 | Local edge satisfiability implies a global transport section | REFUTED — three 1-flips around a triangle | Closed walk parity = 1; no global solution despite each edge having witnesses |
| MCD-06 | For finite undirected `F_2` multigraph, global assignment iff edge cochain is coboundary iff all closed-walk parity vanishes; when flat, `2^c` sections | CLASSICAL PROVED PAPER; exact solver/oracle added | Graph cohomology only, not arbitrary sheaf cohomology; finite tests require CI |
| MCD-07 | Formal local compatibility / sheafification produces an original-source realizer automatically | REFUTED; prior NG-Q0/NG-INF counterexamples | Realization is a separate source-adequacy gate |
| MCD-08 | Concrete Grothendieck site `(C_S,J_S)`, source adequate sheaves, and functorial base change for general SUCC | UNVERIFIED HYPOTHESIS | Prove smallness, composition, cover stability/transitivity, source comparison and actual realization |
| MCD-09 | The SUCC synthesis yields a genuinely novel arithmetic theorem / Weil positivity / RH | UNVERIFIED; RH OPEN | Require new original-source typed morphism, authentic signed Weil proof, fake-source controls, independent verification |

## Executable receipts

- Formal: `formal/EODCS_RelationalChoice.lean` (Lean 4.14.0, preexisting file, additive new theorems only).
- Finite model: `observational_succ/meta_choice_descent.py`.
- Hostile oracle: `tests/test_eodcs_meta_choice_descent.py` (729 labeled 4-vertex simple graphs; 16 exact assignments per graph; plus mutation controls).
- Deterministic report: `python scripts/meta_choice_descent_probe.py`.
- CI: `.github/workflows/eodcs-lean.yml` and `.github/workflows/eodcs-tests.yml` should discover the modified Lean file and new `test_eodcs_*.py` on PR.

**Truth firewall:** no observation of physical sources is claimed. Logical soundness of the paper statements does not certify a repository compilation until CI succeeds. Distinct algorithms sharing a source contract are crosschecks, not independent empirical provenance. This round never modifies the original Weil positivity/Schur frontier.

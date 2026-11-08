# Harmonic–Pisot boundary research (2026-11-07)

**Scope:** A precise harmonic-feedback boundary model, its Euler–Mascheroni finite part, exact Pisot/Galois source memory, and an adversarial anti-normality theorem.

- [THEOREMS.md](THEOREMS.md): HPB-01 through HPB-05, proofs, explicit threshold, analytical tail bounds, and source/type firewalls.
- [NEXT.md](NEXT.md): exact source-map checks, fixed-h signed-gate follow-ups, pass/fail/ambiguous probe criteria.
- [CIRCLE_WINDOW.md](CIRCLE_WINDOW.md): constant geometric aperture vs actual reachability, Fourier-complete golden observation windows, locked-phase countermodels, and a uniquely self-calibrating golden half-width.
- [Original focused tests](../../../tests/test_harmonic_pisot_boundary.py): ten standard-library finite exact/numeric controls.
- [Aperture-focused controls](../../../tests/test_harmonic_pisot_circle_window.py): seven additional standard-library tests, including rational masking, golden visibility and moving-frame controls.

**Parent:** main@d32342d375f44ddf62221ad6aff2f534abdc0a03. **Only additive research/tests.** Related *draft* work: [Pisot/Gamma gluing #470](https://github.com/femboy2112/SUCC/pull/470), [Golden observer #471](https://github.com/femboy2112/SUCC/pull/471), [Holographic triangle #534](https://github.com/femboy2112/SUCC/pull/534), [Quadratic Pisot–Tate #537](https://github.com/femboy2112/SUCC/pull/537). Entry gate: [pi normality frontier](../../../docs/PI_NORMALITY_FRONTIER.md).

**Key mathematical verdict:** finite weighted phase-defect energy gives a finite critical boundary and forces the first Weyl average to **1**, not **0**. This model explains historical residue under phase-locking but is **not** a pi-normality proof instrument without a fundamentally different, sign-sensitive source-specific step. Pi normality and RH remain open.

Focused replay:

    python -m unittest discover -s tests -p 'test_harmonic_pisot_boundary.py' -v

Run the full AGENTS.md gates before merging. No merging, tagging, release, formal theorem promotion, or source modifications in this change.

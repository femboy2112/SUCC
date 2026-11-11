# Signed 3/2 prime ratio: true two-to-three Haar joinings and source-selected finite probe

**2026-11-10. Research-only child of draft SUCC #588 (`896c9ff3ceec5eb062a72cf5fc9230b6f80e2467`), which is stacked on #585 → #584.** Read `PROOFS.md` for complete definitions, quantifiers, derivations, countermodels and the unproved next theorem.

## Outcome

- **Genuine 2→3 coupling defect (DISCLOSED):** Two explicit invariant joinings of `T²×T³` on the two-torus have Haar marginals, but their `h=8` diagonal Fourier coefficients have opposite real signs with magnitude at least `cos(π/16)>0.9807`. The joining is built from a 2-digit block embedded into a 3-digit block with a signed modulo-16 twist. This is a two-time joint-correlation effect, not a Wilson-loop holonomy or a zeta-zero theorem.
- **Normal orbits with locked fiber (DISCLOSED):** An independent-root digit construction on the arithmetic graph `f(n)=floor(3n/2)` gives, almost surely, fully normal base-16 digit sequences while their 3/2 fiber remains nearly +1 or −1 at *every* epoch. A variance/O(N log N) and square Borel–Cantelli argument is included; finite pseudorandom digits are not mistaken for normality certification.
- **Periodic false positive (DISCLOSED):** `α=1/9` is nonnormal, yet the single `h=8` ratio-fiber mean decays as `O(1/A)` by an exact 3-adic cyclotomic cancellation. Thus single-mode ratio cancellation and base-16 normality are incomparable on the space of real phase parameters.
- **Irrationality anti-locking, not cancellation (DISCLOSED):** the recurrence `K_(ell+2)=4352 K_(ell+1)−1048576 K_ell` yields a universal limsup distance ≥`1/1052929` from integers for all irrational α and nonzero h; sparse-digit irrational controls nevertheless have fiber mean approaching 1 on a subsequence.
- **Source-selected evidence (FINITE):** exact rational BBP and separate rational trigonometric enclosures for the *literal zero-seed π orbit* at fresh epochs `A=263,521,1031`, `h=8`. Finite values differ from the engineered model joinings but yield no asymptotic saving.
- **Source-resolution identity:** an exact sinc kernel quantifies when averaging a phase interval destroys mixed correlation versus when a source prefix resolves the selected π point.

**Verdict:** We have characterized a strong, real 2/3 prime–Archimedean *joining obstruction*. Proving original-zero cancellation on the single 3/2 fiber would be a source-specific result stronger than ordinary normality, but even that result alone would not prove π normality. The primary all-mode signed Basel/Weyl gate from #585 remains OPEN. No RH⇒π normality result; no claims of novel priority.

## Local verification

```sh
cd research/2026-11-10/basel_crt_omega_phasebridge/ratio_fiber_joinings
python -W error -m unittest -q test_ratio_fullblast.py
python certified_fiber.py 263
python certified_fiber.py 521
python certified_fiber.py 1031
```

13 focused tests passed locally. All new files reside under this additive research subtree. No source/seed/provenance/Lean/workflow/main changes, no ~13k CI wait. Read `CLAIM_LEDGER.md` and `VALIDATION.md` for truth and execution boundaries.

# Validation receipt: additive cursed-cut research, not whole-repository CI

Date: 2026-11-10. Python 3.13.5. Local standalone workspace in a tool container (not a full SUCC checkout). Focused command:

```sh
python -W error -m unittest -v test_cut_graph.py test_cursed_rounds.py
python -m compileall -q cut_graph.py test_cut_graph.py test_cursed_rounds.py
```

**Final local outcome: 14/14 focused tests passed; compileall passed.** Source and tests are pure Python stdlib (`Fraction`, `math.isqrt`, `unittest`), run without decimal pi, mpmath, or a network download. This does not establish existing SUCC imports, 13k+ native tests, hosted GitHub checks, or Lean.

Test scope:

1. All four signed poles equal a separate three-positive-difference rational decomposition, r(n)>0 and r(n+1)<r(n).
2. Authenticated pi/16 rational prefix strict nesting through depth 39 and width contraction.
3. Integer-`isqrt` dyadic sqrt(2) interval strictness for depths 1..23.
4. Rational cut queries and `UNKNOWN` on a rational boundary query under budget exhaustion.
5. Rational affine naturality: query reindexing, exact composition, reject zero scale.
6. Certified original-source hexadecimal digits `3243F6A8885A308D`, prefixes and the integer carry recurrence.
7. Coherent rational wrong seed +1/16: first digit changes and later digits alias.
8. Stern–Brocot paths and determinant-one Farey matrices for pi/16 and sqrt(2).
9. Divisibility incidence zeta/Möbius inverse checked on all comparable divisor pairs for 12, 30, 60, and 180.
10. Two distinct irrational affine transforms of sqrt(2) match every selected finite rational probe while differing at base-16 precision two.
11. Rank-two six-cell commutator of two idempotents: exact cubic relation and skew symmetry.
12. Positive oriented source-wavelet area tested over eight exact rational clocks.
13. Idempotent first-digit projection `Q delta_0` has exact non-Haar Wasserstein distance `1/32`.
14. Divisor-category `gcd` restriction is right adjoint to inclusion and composes coherently.

Retained initial local failures: first test used a **false** positive-channel decomposition `6/[a(a+3)]+1/[(a+3)(a+4)]+1/[(a+4)(a+5)]`, which failed already at n=1 (`47/15 != 19/12`). Replaced by the **correct** identity `6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)]`. Also repaired an out-of-range access to digit index 16 in a 16-digit prefix loop. Both bugs were in new local tests, not changes to the immutable source; after repair all focused tests passed. These failed attempts do not count as independent validations.

File SHA-256 (locally, before publication):

```text
cut_graph.py       02d247c8a51507d7561b7dd0096b7af8065c741a8747179b491b54ebe0b36c9d
test_cut_graph.py  f8112c7c4c665dfefd305e9d586a450b22f3c14922afbc38db71f088dfe6e51d
test_cursed_rounds.py 4e01c40d2f2ef350aad51c2a7e07147a5b0f2d1f56402618d0d3b605c288cbf7
```

**Release and integration:** Additive research draft only. Never merge to main, tag, release, rewrite frozen files, or bypass repo mandatory gates based on this receipt. At integration, compare new files byte-for-byte, rerun focused suite against the repository environment and original `observational_succ.duck_bbp`, then run AGENTS.md full required commands once on the integration candidate if a maintainer decides the candidate is merge-ready. No full suite or hosted CI is claimed here.

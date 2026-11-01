# Operation Main XVIII — validation

**Research-status.** All validation was run on the integration head in an isolated worktree with a
**compliant** interpreter. No mathematical status is promoted.

## 1. Environment (the prior full-run failure was environment, not mathematics)

The earlier Astra full-run failure was an outdated `mpmath` (1.2.1, below the declared `>=1.3`) plus a
missing editable install — a configuration issue, recorded by the author in
`research/2026-10-31/signed_lag_fireworks/receipts/baseline/baseline_termination.json` and not counted
as a pass. For Main XVIII a compliant environment was built before any lengthy run:

- `python -m venv --system-site-packages` + `pip install -e '.[test]'` from the worktree.
- Resulting versions: **mpmath 1.4.1** (satisfies `>=1.3,<2`), numpy 2.5.0, sympy 1.12, scipy 1.18.0.
- The editable install resolves `import observational_succ` even in a subprocess whose `sys.path[0]`
  is `scripts/` — so the Main XVII `meta_choice_descent` subprocess artifact does **not** recur here.
- `observational_succ` resolves to the worktree tree; the worktree was clean apart from the
  integration's own additive files.

## 2. Mandatory AGENTS.md gates

| gate | result |
|---|---|
| `python scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, `source_commit ba075348`, 72 items, 17 byte-identical archives, rc=0 |
| `python scripts/observer_foundations_probe.py` | rc=0; firewall flags unchanged (`finite_survival_claims_are_universal_proofs: false`, delayed-prefix-19 refuted) |
| `python scripts/ordinal_succ_report_probe.py` | rc=0; `positive_definiteness_proved: false` (unchanged) |
| `python -m unittest discover -s tests -p 'test_*.py'` | **Ran 10253 tests in 1048.8s — OK, rc=0** (zero failures, zero errors, zero known artifacts) |

The full count decomposes as Main XVII's 10025 + 228 new Main XVIII tests (Cluster A 11, Cluster B 77,
Cluster C 140) = **10253**. The single Main XVII env-only artifact is gone under the compliant editable
install.

## 3. Math-memory layer

| check | result |
|---|---|
| `python scripts/verify_math_memory_graph.py` | PASS, 51 typed nodes / 60 typed edges, rc=0 (proofs not independently checked, by design) |
| `python scripts/build_math_memory.py --check` | rc=0 after the catalog was **regenerated last** (with the pre-existing GS-4/GS-5 legacy-prefix warnings carried from `main`, not errors) |

The catalog (`docs/math_memory/CLAIM_CATALOG.json`) is a by-path discovery index that records each
research `*.md`/`*.lean` by sha256; it certifies no proof (`not_a_proof_checker: true`). It was
regenerated after all document edits so it captures the new `research/2026-10-31/` dirs and this
dossier. Because unregistered rows are keyed by path, the new research-dir prefixes (CT/TWTH/CP/HP/TD)
produce **no machine-level claim-ID collision** and the 15 namespace-collision tests stay green.

## 4. Focused cluster tests + module-isolation reconciliation

| group | tests | result |
|---|---:|---|
| Cluster A `test_counterfactual_triangle_carrier.py` | 11 | OK |
| Cluster B (`two_three_joint_carrier`, `pascal_crossprime_conjugacy`, `half_power_horizon`, `multiplace_bbp_difference`) | 77 | OK |
| Cluster C (`carrier_path_measure`, `edge_seed_tomography`, `seed_superposition`, `selected_lag_tomography`, `signed_lag_fireworks_{arithmetic,audit,boundary,sharpness,transport}`) | 140 | OK |
| **All 228 new tests, single process, FORWARD order** | 228 | OK |
| **All 228 new tests, single process, REVERSE order** | 228 | OK |

The forward/reverse single-process runs confirm the `independent_oracle` module-name-collision fix:
every oracle/module is loaded by a unique `spec_from_file_location` name, no bare
`import independent_oracle` exists anywhere, so test order does not matter.

## 5. Committed receipts (reproduced, not trusted blindly)

The Cluster C reviewer re-ran the committed probes with the compliant interpreter and matched the
stored receipts exactly: `signed_lag_fireworks/probe.py` → `finite_receipt.json`;
`run_boundary_receipt.py` → `boundary_receipt.json`; `run_sharpness_receipt.py` →
`sharpness_receipt.json`; `arithmetic.py` → `arithmetic_receipt.json`; `receipts/SHA256.json` 0
mismatches. An independent 40-digit recomputation of the signed scores fell inside the stored
intervals. `RESULTS.md` discloses that the `K=17` Weyl upper bound exceeds 1 (vacuous) and that fresh
positive signed scores occur at several `h` — correctly forbidding any universal finite inequality.

## 6. Invariants and proof authority

- `observational_succ/`, `formal/`, `scripts/`, `provenance/`, `.github/`, `ci.yml`, the frozen BBP
  source dossier, `IMPORT_MANIFEST.json` (`source_commit ba075348`), `U_0=0`, and the four signed
  poles are **byte-identical to `main`** (Lean and CI are confirmatory, not re-proved).
- **No Lean declaration was added or kernel-checked** this round; the cluster paper proofs are labeled
  "paper proof, NOT Lean kernel" and are not promoted to formal authority.
- The hosted CI conclusion on the exact final integration head is recorded on the integration PR.

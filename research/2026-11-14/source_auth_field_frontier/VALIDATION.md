# Validation — Source Authentication × Field-Class Frontier

**2026-11-14, isolated runtime, Python 3.13.5.** These are locally executed results from the accompanying code. They do not constitute an independent physical experiment, theorem-prover certification, or full-root SUCC suite pass.

## Executed commands

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python research/2026-11-14/source_auth_field_frontier/independent_oracle.py
PYTHONPATH=. python research/2026-11-14/source_auth_field_frontier/run_live_holdout.py \
    --sessions-per-model 12 --horizon 20 \
    --out research/2026-11-14/source_auth_field_frontier/receipts/holdout_sessions.json
```

- **58/58 local tests PASS:** the 31 inherited PR #628 `test_recursive_observer.py` tests and 27 newly authored `test_source_authentication.py` tests. Exact rational `Fraction` computations and real subprocess I/O.
- **Independent raw-path oracle PASS:** 1,562 distinct action/outcome/model trace checks (through length 4), comparing a separately encoded source-process probability rule against exact RFO joint filters. An independent adaptive-policy null martingale replay checks **42** depth-six endpoints. Exact null e-martingale census passed for each depth **0–7**, including Ville threshold 4.
- **Executed contact:** 24 separate Python subprocess instances (12 registered P, 12 Q), each 20 actions, **480 actual legal interventions/readouts**. Each session precommitted to a 128-byte tape + hidden model tag before first action. The full revealed tapes, public actions/outcomes, model predictions, evidence process, original-state posteriors, internal and client external timings and credits are in `receipts/holdout_sessions.json.gz` (deterministic gzip, `gzip -dk` to unpack). Every session passed an independent replay verifying commitment, source script digest, hidden transitions and state, observer policy, cost, posterior, likelihood and proper scores.
- **Exact source process digest:** `738d3e77d617262411f950c03947d81de78edbcacbdb1d0ae39d1e425232d162` (SHA-256 of the exercised `source_process.py` file). This digest is bound to source code bytes, not OS executable provenance.

### Observed holdout diagnostics (not theoretical certainties)

| Registered source | Sessions | Terminal E≥4 | Ever E≥4 | Ever E≥20 | Independently charged credits | Mean Brier P forecast | Mean Brier Q forecast |
|---|---:|---:|---:|---:|---:|---:|---:|
| Alternative P (read accuracy 3/4) | 12 | 8 | 8 | 6 | 558 | 0.4031049 | 0.5000000 |
| Null Q (read accuracy 1/2) | 12 | 1 | 2 | 1 | 504 | 0.5995422 | 0.5000000 |

The mean scores are per binary **scored** probe, excluding `flip` actions with a single deterministic outcome (P: 234 scored observations, Q: 216). The predeclared models and policy were not fitted to these 24 sessions. These realized counts do **not** estimate a universal false-positive rate or prove the ideal stochastic law of OS RNG. The mathematically valid sequential type-I bound is a conditional theorem under the null model, not an empirical calibration from twelve trials.

### Hostile mutations actually checked

- Source `peek` action is rejected rather than revealing the hidden bit.
- Tampered tape, revealed model tag, published source digest, outcome or cost are rejected by the independent replay.
- Modified observer posterior, chosen action, or evidence ratio is rejected separately from source I/O replay.
- A reset action reports the **pre-reset** source; post-state-only likelihood factorization must fail.
- A hindsight-selected alternative to a fair-coin null makes `E_Q[e] = 2`, invalidating naive post-hoc calibration.
- Two hidden models with different state counts but identical observable predictions pass finite predictive-span equality; ontology does not descend.
- A hidden tag remains unobservable over every allowed read/flip word, by source-level induction; a finite sample of words is only an executable control.
- A sequence of delayed finite mutants defeats any fixed unbounded-class observation horizon; a known complexity bound would change the verdict.
- Field-report constructor rejects explicit contradictory evidence and refuses to accept numeric values as boolean proof certificates.

## Exact authority boundary

**DISCLOSED (inside specified finite model):** algebraic Bayesian conditioning, fixed-cost policy execution, exact registered-action martingale calibration, rational path checks, target nonidentifiability/finite delay/CRT phantom paper arguments.

**OBSERVED:** 24 finite executed local source programs and successful after-reveal replay. Source executable and observer are in one Linux container: this is not a physically separated or malicious-actor-resistant external experiment. Hash commitments assume binding; `secrets.token_bytes` is OS supplied; independence and ideal uniformity are assumptions, not proven properties of this one random source.

**UNVERIFIED:** external physical source map, timing/energy source law, complete side-channel modeling, universal model class, any RH/pi/GR or quantum conclusion. No new Lean certificate or external blind referee.

**Not executed:** the full checkout's mandatory `scripts/verify_provenance.py`, full repository test discovery, `scripts/observer_foundations_probe.py`, and `scripts/ordinal_succ_report_probe.py` at the new branch head. Run on GitHub CI before integration and inspect the exact final SHA. Existing GitHub results from older commits are not this branch's validation.

## Reproduction, file integrity

`receipts/holdout_sessions.json.gz` stores the entire 24-session trace: it is not a summary-only reconstruction. The independent auditor can verify it after decompression. `receipts/holdout_summary.json` contains digest, counts, score totals and source SHA. `FILE_HASHES.json` lists content digests for new files; remote Git blob IDs must be checked against generated local digests after pushing. The complete Python3.13 source and tests are runnable without external dependencies (outside the inherited `recursive_observer.py`).

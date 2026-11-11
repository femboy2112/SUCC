# Innovation × arithmetic decoupling (2026-11-11)

**Research branch, additive to Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`. Not merged.**
**π base-16 normality, the source-selected signed estimate, original-zero parity balance and RH
remain OPEN.** This round set out to find a source-dependent signed estimate. It did not find one.
It found exactly why the proposed innovation/history mechanism cannot supply one, what any such
estimate is forced to imply, and one unconditional estimate for the seed-independent factor.

## The question

Can the temporal innovations `Δ_ℓ(n) = U_(n+ℓ) - 16^ℓ U_n` of the authenticated four-pole BBP
recurrence be shown to decorrelate from their inherited arithmetic history strongly enough to give
a nontrivial Archimedean cancellation estimate?

## The answer, in five sentences

1. The innovation factor alone **does** cancel, with explicit constants, in the lag window
   `(2+δ)log_16 B ≤ ℓ ≤ (3-δ)log_16 B`, uniformly on subintervals and on clock progressions
   (IAD-04) — but this is a statement about the forcing only and holds for every seed.
2. The history factor **contains the conjugate innovation exactly** (`A = C·conj(Z)·e(-hτ)`,
   IAD-05), so "decoupling" is literally the completed lag correlation; no filtration can make it
   easier, and the coherent seed has the same innovations and correlation 1.
3. No finite-horizon prime-to-real transfer that omits even one place can work: for every odd
   prime `q` and every shell there is a rational seed identical to the true source at all other
   places, to any finite precision, whose completed orbit is coherent on that whole shell (IAD-07).
   (The seed depends on the shell; purely asymptotic transfers are not excluded by this.)
4. Any estimate with a fixed saving on all large shells, for one mode or one lag, forces
   `‖16^B·π/16‖ ≥ c·B·16^(-B)` — the base-16 Diophantine exponent of π at most 1 without ε-loss —
   where the refereed record is 6.1033 (IAD-08); so the target is at least that hard.
5. On the maintainer's Scott-domain thesis: the order cannot see normality but **does transport
   it** — across the finite/analytic weld (π is normal iff the rational source's literal
   carry stream has uniform block frequencies over `{0,…,15}`, SWT-04) and across schedules whenever the functional is antitone (SWT-05), which is
   why the handoff's Fejér schedule is free (IAD-02).

## Files

| File | Content |
|---|---|
| [THEOREMS.md](THEOREMS.md) | IAD-01 … IAD-09 with complete derivations and quantifiers |
| [SCOTT_TRANSPORT.md](SCOTT_TRANSPORT.md) | SWT-00 … SWT-06: what the Scott order transports and where it stops |
| [OBSTRUCTIONS.md](OBSTRUCTIONS.md) | Ten failed mechanisms with receipts, and the four invariances that kill them |
| [PREREGISTRATION.md](PREREGISTRATION.md) | Checks and predictions, committed before any holdout probe existed |
| [PROBES.md](PROBES.md) | What was run, on what, and what came out (raw data in `RESULTS_*.json`) |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Established / conditional / open, each with its falsifier |
| [NEXT.md](NEXT.md) | The single next obligation (WALL-16) and the next verdict-changing probe |
| [SOURCE_MAP.md](SOURCE_MAP.md) | Frozen source, reused internal results, literature with verification status |
| [VALIDATION.md](VALIDATION.md) | Exact commands, commits and outcomes; audit record |
| `iad_core.py` | Exact rational kernel (reuses the frozen forcing) |
| `probe_analytic.py`, `probe_arithmetic.py` | Reproducible probes |
| `test_iad_analytic.py`, `test_iad_arithmetic.py` | Unit tests with mutation controls |

## Reproduce

From the repository root, with the test dependencies of `pyproject.toml` installed:

```sh
export PYTHONPATH="$PWD"
python -m unittest discover -s research/2026-11-11/innovation_arithmetic_decoupling -p 'test_*.py'
python research/2026-11-11/innovation_arithmetic_decoupling/probe_analytic.py
python research/2026-11-11/innovation_arithmetic_decoupling/probe_arithmetic.py
```

The probes rewrite `RESULTS_analytic.json` and `RESULTS_arithmetic.json` deterministically and
exit non-zero if any theorem-grade check fails.

## Scope and boundaries

- All proofs are local, same-model work with a same-model adversarial audit. No external
  refereeing and no Lean verification is claimed.
- Finite probes test instruments and theorem instances. They change the status of no open claim.
- No frozen source, provenance manifest, historical default or existing dossier is modified.

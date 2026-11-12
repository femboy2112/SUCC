# Frontier rungs — limit faces, canonical thresholds and restricted exponents

Round 3 of the innovation × arithmetic programme (2026-11-12), on top of
[`research/2026-11-11/innovation_arithmetic_decoupling/`](../../2026-11-11/innovation_arithmetic_decoupling/README.md)
(IAD, SWT, ZSC) and Main XXIV.

**π base-16 normality, the source-selected signed estimate, (CH), R1 and R0 are OPEN.** This round
proves no estimate for the zero-seeded source. It identifies the rungs of the signed ladder
exactly, measures them in the canonical Main XXIV units, settles the restricted-exponent probe
named by the previous round, and gives kernel authority to the exact carry lemmas.

Frozen source, unchanged: `r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)`, `U_0 = 0`,
`U_n = 16U_(n-1) + r(n)`, `C_n = ⌊U_n⌋`, `κ_n = C_n - 16C_(n-1)`, completed point `π/16`.

## What the round answers

1. **What is the weakest open signed statement?** Not (CH), as the previous round said. It is
   **R0**: `limsup_B Re W_B(1) < 1`, the real part of the canonical target at its first mode;
   equivalently the binary digits of π change with positive lower shell density; equivalently
   `δ_0` is not a weak-* limit of shell measures (LMF-03). Above it: R1 (no single fixed-point
   delta), R2 = (CH), (CH_k), a saving at every mode, positive entropy, normality — each the
   exclusion of an explicit set of invariant measures, each implication strict.
2. **How far from the canonical target is each rung?** For shell measures:
   `limsup W_1(ν_B, λ) < 1/4` or `limsup D(ν_B) < 1/4` implies R1 and R0; below `1/60` implies
   (CH); below `1/(4(16^k − 1))` implies (CH_k); normality is `→ 0`. Prefix forms: `D_N < 15/256`
   and `D_N < 1/256` (LMF-04, LMF-05). `1/4` and `1/60` are sharp for shells.
3. **Is a restricted exponent below 1 known anywhere in the period class `V`?** Yes, by import:
   Rivoal (2007) gives `v_16(log(16/15)) ≤ 0.8813`, and `log(16/15) = Σ 16^(-n)/n` is a proper
   zero-seeded element of `V`. Extended locally to the denominators `15·16^m`, this gives **L2**
   (a digit change in every large shell) for that element (RDT-07). (CH) for it is OPEN. For
   `log 2` a tilted Legendre family gives `v_2(log 2) ≤ 2.3814`, below the unrestricted record
   `2.5746` and far above 1 (RDT-05; no novelty claimed).
4. **Why does that mechanism not reach π?** A restricted gain is exactly a `b`-adic imbalance
   between the two coefficients of a linear form (RDT-01/02). For `log(16/15)` and `log 2` the
   argument of the logarithm is a non-unit at 2; for the π-line it is a root of unity, the
   effective base is `√2` (RDT-08), and in the convergent Gaussian families examined the imbalance
   sits on the constant term (RDT-06). Not claimed: that `v_16(π) < 1` is false.
5. **What has kernel authority?** Thirty-three exact statements behind ZSC-02, ZSC-03 and ZSC-06
   (`lean/`), with nine refuted mutants. Nothing statistical or asymptotic.

The analysis, with the rabbit holes followed and the next obligation, is in
[FRONTIER_ANALYSIS.md](FRONTIER_ANALYSIS.md).

## Files

| File | Content |
|---|---|
| [FRONTIER_ANALYSIS.md](FRONTIER_ANALYSIS.md) | Where the frontier stands, what each rabbit hole returned, the next obligation (R0; test object `log(16/15)`) |
| [LIMIT_FACES.md](LIMIT_FACES.md) | LMF-01 … LMF-06: limit set of shell measures, face dictionary, ladder with witnesses, thresholds in `W_1`, `D` and Basel units |
| [RESTRICTED_EXPONENT.md](RESTRICTED_EXPONENT.md) | RDT-01 … RDT-08: restricted transference lemma, continued-fraction dictionary, silence of BBP partial sums, `log 2`, π, the Rivoal import and its extension, effective base |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Every statement with status, authority and falsifier |
| [SOURCE_MAP.md](SOURCE_MAP.md) | Literature with verification grades; corrections of earlier recollections; unrefereed 2026 claims (not imported) |
| [PREREGISTRATION_RUNGS.md](PREREGISTRATION_RUNGS.md) | Shells, predictions and mutation controls, committed before the probe existed |
| [VALIDATION.md](VALIDATION.md) | Audits (what each found), runs, deviations, what was not done |
| `faces_core.py`, `test_faces.py`, `probe_rungs.py`, `RESULTS_rungs.json` | Exact evaluators, tests and the preregistered probe for LMF |
| `rde_core.py`, `test_rde.py`, `RESULTS_rde.json` | Exact evaluators, tests and exploration record for RDT |
| [`lean/`](lean/README.md) | Lean 4 source, check script with paired mutant controls, receipt |

## Reproduce

```sh
PYTHONPATH=$PWD python -W error -m unittest discover -s research/2026-11-12/frontier_rungs -p 'test_*.py'
PYTHONPATH=$PWD python -W error research/2026-11-12/frontier_rungs/probe_rungs.py   # rewrites RESULTS_rungs.json identically
python scripts/main_xxv_research_gate.py --out <directory outside the checkout>      # both dossiers, all probes
```

## Authority

Paper proofs by one model, each theorem file audited once by a separate read-only instance of the
same model family with its own code; repairs made after those audits were not audited again. The
Lean check is kernel authority for the listed exact lemmas only. Literature statements were read by
a helper (citation check, not refereeing). No external review. No claim of novelty.

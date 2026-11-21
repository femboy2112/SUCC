# Validation — zero-seed two-carry differential

**Authoring date:** 2026-11-21. **Source:** original four-pole SUCC Main XXVI, literal `U0=0`; the Pi identity is the inherited classical BBP theorem. This document records exact runs and their scope, not a new formal proof or referee certificate.

## Executed local verification (research directory)

```sh
PYTHONPATH=. python -m unittest -v test_two_carry_seam.py
python independent_audit.py
python -m compileall -q two_carry_seam.py test_two_carry_seam.py independent_audit.py
python -m two_carry_seam
```

- Focused stdlib suite: **21/21 methods pass**, process exit 0; saved `focused_unittest.log`. The initial two *test-expectation sign errors* were caught and corrected before the final run; no incorrect source formula or unreported mathematical positivity claim remains. A negative-control assertion for a slowly sparse digit word was also corrected from an overstrong finite numerical threshold: the **asymptotic** density proof uses diverging gaps, not a false small-N frequency claim.
- Standalone SymPy/fractions audit: **1766 exact assertions PASS**, process exit 0; saved `independent_audit.py`, `independent_audit.log`, and machine-readable `independent_audit_receipt.json`. It implements the source through the independent compact rational numerator/denominator formula, direct Mellin monomial integration, direct modular powers for selected BBP clocks, 12 positive Hankel minors, six prime-square original-vs-mutant fingerprints, 4,096 independent raw-state recurrences, and rational changed-seed positive controls. This is an independent **implementation path sharing the same mathematical premises**, not independent scholarly certification of the all-n theorem.
- `compileall`: process exit 0.
- Exact original seed replay: 16,000 rational Fraction clocks, all source-kick counters `e_n=0`, all strict source-tail upper bounds certify `delta_n=0`, no unresolved intervals, certified 16,000 hexadecimal digits via signed coboundary. `exact_16000_receipt.json` preserves the first/last 32-digit strings, exact predeclared quarter-shell counts, and `SHA256` of the complete digit string. The digit sequence itself is not used to infer an infinite asymptotic property.
- Predeclared finite shell quarter response: B=128 hits66, B=512 hits262, B=2048 hits1017, B=8000 hits3940. These bound the **actual** R0 energy `A_B` *from below at those finite B only*, because `1−cos(2πtheta)>=1` for phases in `(1/4,3/4)`.

## Exact mathematical statements and their limits

- Full quantifiers for `TCD-01` complete monotonicity/Hankel positivity, `TCD-02` signed integer coboundary, `TCD-03` all-seed cooldown, and `TCD-04` opposite orientations are proved in `THEOREMS.md`. Their proof authority is the written mathematics, not the size of the finite sample.
- The almost-sure eventual digit-transfer theorem `TCD-05` is a **seed-ensemble** theorem using Haar and the first Borel-Cantelli lemma. It does **not** apply to the fixed seed s=0 merely because the first 16,000 selected clocks pass.
- `TCD-07` gives a changed-seed sparse-word nonnormal model with tail carry eventually zero and forcing carry density zero, showing neither condition alone or together implies R0. The locked exact counterseed s=-pi/16 has delta_n=1 at every clock, a direct negative control for any seed-uniform completion-carry claim.
- The completed Collatz parity companion `TCD-09` is a **constructed Z2 journal** via the inherited classical Bernstein–Lagarias conjugacy; 64,000 certified parity bits are 4 bits per certified hexadecimal digit. This says nothing about an ordinary positive integer's entire trajectory.

## Not run or claimed

Full inherited SUCC ~14k+ test suite, `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`, hosted CI, Lean, external independent referee, source-selected R0 all-B theorem, π normality, Collatz conjecture, RH, or physical information-energy conservation. No source file, protected archive, ledger, workflow, or main was altered.

## Falsification matrix

| Instrument | Expected result | Negative control |
|---|---|---|
| Source forcing kick | e event resets raw phase below r(n), delaying next kick | Rational changed seed forcing e=1 at a chosen clock |
| Completion tail carry | delta event has opposite raw orientation, true phase < T_n | s=-x has delta=1 forever; rational changed seed forces delta=1 at chosen clock |
| Signed digit relation | d=b+e+delta−16delta_prev **as integers** | Deliberately omit −16 term: wrong-seed locked control fails immediately |
| Moment signature | every finite signed difference and Hankel minor strictly positive | H factor/moment algebra mutation rejected by source fingerprints |
| R0 from rare carries | **must not follow** | explicit 0/1 sparse word with gaps ~log n: delta eventually0, e density0, R0 fails |
| π-normality claim | **OPEN** | fixed zero seed and every late integer B still require new signed estimate |

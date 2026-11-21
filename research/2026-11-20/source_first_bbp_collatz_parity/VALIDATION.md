# Validation, independent finite audit, and exact scope

## Executed local commands (on byte-identical local files)

All commands executed in `/mnt/data/source_first_collatz_join`:

```sh
python -m unittest discover -s . -p 'test_*.py' -v
python independent_sympy_audit.py
python -m compileall -q source_first_parity.py test_source_first_parity.py independent_sympy_audit.py
```

**Actual results:** 21/21 stdlib exact focused tests PASS (exit zero); a separate SymPy/mpmath implementation PASS with **424 counted assertions**, including 11 certified first-pole prime-square events `p=7,...,43`, actual signed source-vs-swapped block signs, 2-adic finite quotient idempotents, factor resultants/projectors, and an independent 360-decimal-digit π evaluation. `compileall` PASS. Raw outputs: [`focused_unittest.log`](focused_unittest.log), [`independent_audit.log`](independent_audit.log), [`audit_receipt.json`](audit_receipt.json). The SHA256 manifest covers exactly the research files, including logs and this validation note, excluding only the manifest itself.

**Source-specific selected orbit checks:** `source_parity_bit` with the original four poles and rigorous BBP rational tail directly certifies each of the first 48 chronological Collatz parities without supplying any hexadecimal digit to its oracle. The assembled parity address `0xA5888A6F3423` and finite Collatz residue `0x138D4B466283` agree with SUCC #681 and independent high-precision π plus separately coded reversed inverse branches. This is a checked finite source-consequence, not independent proof of the classical BBP identity or an asymptotic distribution theorem.

**Signed counterfactual:** every tested prime p=7,11,13,17,19,23,29,31,37,41,43 has a rational interval `1/64<=delta<1/4`. The exact source carry classifier and independent high-precision calculation agree on the signed two-hex block comparison. `p=19` has a negative block-order sign despite positive imaginary interferometric orientation. Explicit reversed signs, prime-source mutation, even-vs-odd source, root-pole collapse, and quarter-XOR-not-necessary controls are retained.

## Independent routes and limitations

- **First path:** stdlib `Fraction`, original four-pole rational source, exact monotonic/positive source-tail and integer carry bounds, exact shortcut Collatz replay. Theorems prove the universal statements algebraically; tests calibrate specific clocks.
- **Second path:** separate SymPy exact source and factor algebra, finite rational source perturbations, 360-digit `mpmath` π oracle *without reading the stdlib source's computed digited values*, reverse Collatz parity inversion, and exhaustive F2[t]/t^4 idempotent enumeration. These programs share elementary mathematical premises, **not independent proof families**.
- **Not run or claimed:** full root SUCC >14k test suite; required SUCC provenance, foundations, ordinal scripts; hosted CI/Actions; Lean; formalization of new theorems; external referee; complete all-shell phase/carry theorem; positive-integer Collatz; physical slit measurement.
- **No promotion:** All claims remain research-paper or exact finite receipts. SFC-04/05 compare to a deliberately altered chronological source. Their positive signed response is **not** an anti-lock statement about a single unchanged source. The root H and binary parity are *not* claimed to be related by a freely integral 2-adic projector.

## Reproduction and hash control

Re-run the two Python test commands. Verify every file in `SHA256SUMS.txt` via `sha256sum -c SHA256SUMS.txt`. GitHub blob SHA checks after publication will separately verify remote bytes, not replace these checks. Original SUCC forcing, zero seed, frozen imports and all sibling Collatz repo files remain unmodified.

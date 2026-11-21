# Operation PRIME-PARITY INTERFEROMETER: source-first BBP → Collatz

**Draft isolated SUCC research · 2026-11-20.** Planned stacked child of [SUCC #681](https://github.com/femboy2112/SUCC/pull/681). The immutable BBP source (four poles, zero seed, exact future tail) is not modified. Sister repositories [femboy2112/collatz](https://github.com/femboy2112/collatz) and [femboy2112/collatz-proof](https://github.com/femboy2112/collatz-proof) were **inspected read-only**, including their actual governance and live frontier, not overwritten or promoted.

## What we achieved

1. **Source-specific 2-adic obstruction (new to this SUCC dossier):** original mask `H=(t²+2)(t²+2t+2)` has `Res=8`. Its two source-Haar factor projectors split over Q_2, but no nontrivial integral t-equivariant projector exists over Z_2. In the natural companion basis the rational projector costs **exactly two bits** of 2-adic precision, even though the two factors split integrally at every odd prime. This is the actual missing gluing bill for a naive root-port→Collatz-bit claim.
2. **Direct signed source-to-parity oracle:** each Collatz parity bit for the constructed π shadow is the sign of a source-selected Fourier sine `sin(2π·2^(3-j)·16^n·(π/16))`. Original BBP rational intervals certify one bit at a time *without first decoding its hexadecimal digit*. This is source-first computationally, **not** mathematically more informative than the complete BBP value.
3. **Actual source-root quarter chart ↔ two Collatz parity bits:** the quarter boundaries at 1/4 and 3/4 are exactly the threshold locations for the XOR of the **last two** bits in each 4-bit Collatz parity block; event frequency would suffice for SUCC's weakest open R0 rung. No event-density theorem is proved.
4. **Signed causal prime-square response:** swapping the two *actual* adjacent BBP inputs at the clock immediately preceding `p²`'s first pole generates a source-computable signed imaginary phase cross-response at a log-prime forward delay, uniformly ≥`sin(π/32)`. Thus **at least one of the next eight Collatz parity bits differs**, independent of decoding either word. This is a **counterfactual changed-source** theorem, not π-normality.
5. **GPS-style carry resolution:** one authentic source-derived carry comparison determines the **lexicographic sign** of the two changed hexadecimal blocks, without constructing either block. At `p=19` the sign is negative; others among checked small primes are often positive—an exact, falsifying example against treating positive oriented phase difference as universally positive digit-order difference.
6. **2→3 arithmetic reciprocity:** for any positive integer in the sourced Collatz binary cylinder, the next accelerated odd return modulo 3 is `(-1)^v` where `v` is the gap to its next odd parity. This connects the selected BBP parity word to the **verified conditional reciprocity** in the user's older Collatz repo, without inventing a continuous Z_2→Z_3 field morphism.

## Entry points

- [`THEOREMS.md`](THEOREMS.md) — proofs, hypotheses, quantifiers, signed formulas, mathematical firewall.
- [`source_first_parity.py`](source_first_parity.py) — exact rational source-first parity, signed swap delay, carry oracle, finite Collatz cylinder.
- [`test_source_first_parity.py`](test_source_first_parity.py) — focused stdlib tests, including positive and hostile controls.
- [`independent_sympy_audit.py`](independent_sympy_audit.py) — independent SymPy/350+ digit mpmath path for finite arithmetic calibration.
- [`VALIDATION.md`](VALIDATION.md), [`audit_receipt.json`](audit_receipt.json) — executed commands and scope.
- [`SOURCE_MAP.md`](SOURCE_MAP.md) — exact source file/claim mapping for SUCC and both external Collatz repositories.
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) — proved / conditional / blocked, including concrete refutations.
- [`NEXT.md`](NEXT.md) — next source-selected signed unperturbed-orbit experiment.

**Research verdict:** A genuinely new-to-this-dossier source-specific cross-observer *counterfactual* signed phase/Collatz response has been proved; a root-port integral-lift obstruction is explicit; a finite original-zero parity bit oracle is executable. **The unchanged π orbit's R0 and base-16 normality, general Collatz, RH, and physical energy claims remain OPEN.** No inherited 14k+ root suite, hosted CI, Lean proof, external referee, or publication approval is claimed.

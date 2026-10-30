# Operation Selected Boundary: arithmetic phase slips, not source-only Gamma

**Draft research-only, child of SUCC PR #401.** This package asks whether the authentic BBP zero boundary and original four signed poles impose an all-horizon constraint on selected character coherence.

## Strongest result

Fix nonzero integer h. Define `E_n=1-cos(2*pi*h*(U_(n+1)-U_n))`, and `S_N=sum_(n=1)^N exp(2*pi*i*h*U_n)` with the original rational BBP `U_0=0`. Using the exact four-pole Green-tail comparison and the published Zeilberger–Zudilin irrationality-exponent bound for π, we derive, for every sufficiently large A:

`max_(A<=n<8A) E_n >= 1-cos(pi/10)`.

Therefore `sum_(n<N) E_n >= ((1-cos(pi/10))/log8)*log N-O_h(1)` and

`|S_N(h)| <= N - ((1-cos(pi/10))/(4log8))*log N+O_h(1)`.

**This is a genuinely nontrivial all-horizon signed saving** over the trivial upper bound N, but is far smaller than `o(N)` and does not prove normality. The selected coherent seed `s*=-pi/16` has finite total energy under the **same** forcing, so this theorem really uses the arithmetic identity of the selected endpoint. It also holds for fixed rational translations of that seed; it is not unique source identification.

## Main files

- `THEOREMS.md`: exact scope, the source-tail bound, the no-wrap Diophantine argument, the logarithmic energy and signed-sum deductions, and hostile controls.
- `CLAIMS.md`: epistemic and quantitative claim ledger.
- `selected_boundary.py`, `test_selected_boundary.py`: exact Fraction source/phase probes, no π digits needed for finite tests.
- `independent_oracle.py`: independently unrolled Fraction recurrence + rational Machin π enclosures and selected slip window checks.
- `ASTRA_ULTRA_FANOUT.md`: multi-agent original proof-search handoff.
- `VALIDATION.md`, `focused_tests.log`, `independent_oracle_receipt.json`, `initial_oracle_failure.log`, `SOURCE_MANIFEST.json`: raw receipts and provenance.

## Known blockers and relation to the Gamma program

The original Gamma cocycle, positive Pascal triangle, all-prime transports and selected real BBP recurrence remain separate typed maps. The new theorem exploits a classical Diophantine property of **π itself** plus the summably small source Green-tail: not a new Gamma/Gross–Koblitz-to-real cofiber theorem. Under the established irrationality exponent bound the guaranteed window length is 7A, while SC-06 first-prime periods have length at most approximately 2A. Thus the theorem does not settle even one SC-06 window uniformly.

No historical source, `main`, Lean contract, or existing PR is modified. New proof is locally paper-derived; publication/priority and hosted checks not claimed.

# Prime Fixed Points × Twisted Arithmetic Cylinder × Goldbach

**2026-11-12 · additive SUCC research · draft, not a solution of binary Goldbach.**

## Result in one paragraph

Construct a coassociative reduced factorization coproduct `Delta` on the integer-labelled Hilbert basis. Its primitive states are exactly `1` and the primes. Embed it in a graded supercharge `Q`; the number-sector compression of `[Q*,Q]` is the nonnegative divisor-count operator `A=Delta*Delta`, with the same kernel. A simpler prime-factor grading `B=(Omega-1)_+` has the same fixed points and obeys the **exact prime-birth commutator** `[B,V_p]=V_p(I-P_vac)` for genuine primes `p`. A terminating, product-preserving category of states `(remaining integer, extracted prime context)` has a finite-program observer which enumerates all prime fixed points over unbounded SUCC successor time. For midpoint `n`, the grade `h_n(d)=B(n-d)+B(n+d)` is zero precisely for prime pairs. Angular averaging on a circle annihilates all nonzero grades; across the unbounded midpoint axis this forms an arithmetic cylinder. A parity-compatible back-and-forth walk `W_2` has measurable commutator `[H_n,W_2]`. **Goldbach remains precisely the missing claim that its grade-zero sector is nonempty at every midpoint.** Chen's theorem imports a genuine bound `min h_n<=1` for sufficiently large `n`; the jump from 1 to 0 is not proven.

## Navigation

- [THEOREMS.md](THEOREMS.md) — exact domains, categorical functor, coassociativity, commutator formulas, cylinder, Chen bridge, and obstructions.
- [CLAIMS.md](CLAIMS.md) — scope and truth/authority ledger with countermodels and next probes.
- [prime_cylinder.py](prime_cylinder.py) — standard-library-only exact finite implementation (no floating phases).
- [test_prime_cylinder.py](test_prime_cylinder.py) — nine test families, two distinct primality routes, source mutations, coassociativity, pure gauge.
- [PROBE_RESULTS.json](PROBE_RESULTS.json), [VALIDATION.md](VALIDATION.md) — exact finite receipts and execution scope.
- [../prime_interferometer_legacy](../prime_interferometer_legacy/RESEARCH_NOTE.md) — the earlier split-complex, Hilbert, Haar and CRT–Haar witness-certificate package, kept separate from the new cylinder construction.

## Source contracts and dependencies

- This is additive research. No frozen BBP four-pole recurrence, seed, provenance manifest, RH claim, π-normality claim, Lean file, CI configuration, or `main` integration is modified.
- The *same* Fourier/Haar calculus appears in SUCC's zero-anchored Lambda–Haar compiler, but the BBP selected orbit and these prime-pair amplitudes are different mathematical sources. No accidental implication between Goldbach, RH or π normality is asserted.
- Classical reference for the near-Goldbach boundary: Chen's theorem; see [2022 explicit published version](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/an-explicit-version-of-chens-theorem/2E6F5B87A198E00561CF2C21D147346A) and [exposition of Chen's original proof](https://www.numdam.org/article/AST_1975__24-25__281_0.pdf). The explicit paper obtains a threshold `2n > exp(36)`, but our claim only needs `n` sufficiently large.
- Circle method background: [Helfgott's ternary Goldbach exposition](https://www.mpim-bonn.mpg.de/webfm_send/210).
- Related bosonic Fock number grading is standard; no priority claim for arithmetic Fock encodings or reduced divisor coproducts.

## Minimal reproduction

```sh
cd research/2026-11-12/prime_fixedpoint_cylinder
python -m unittest -v test_prime_cylinder
python prime_cylinder.py > /tmp/prime_cylinder_report.json
```

All finite statements are scoped. No CPU experiment can establish universal Goldbach.

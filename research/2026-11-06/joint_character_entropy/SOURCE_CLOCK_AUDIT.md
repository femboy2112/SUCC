# JC-08 — source-coefficient clock audit (2026-11-06)

**OBSERVED-FINITE / PROVED LOCAL algebra, not a normality result.** This additive audit executes the previously committed `SOURCE_CLOCK_PREREG.md` at the exact pre-measurement branch head `a0289b84295b4fdef3a7f3678d6c3cfdd5ea881c`. It does not change the old `pole_clock`, any prior measurement, `main`, the original BBP source or `U_0=0`.

## Error located and repaired (without erasing history)

The first JC-05 demonstration used `pole_clock(n,7) = (8(n+1)-7) mod 7 = (n+1) mod 7`. This is a genuine **index-only** period-7 auxiliary tape, not a fingerprint of the original four signed coefficients. Its reversible Mealy and entropy theorems remain valid, but earlier descriptive wording suggesting coefficient authentication is too strong. The old instrument remains as the fixed baseline.

For source time `j=n+1>=1` define the exact original four-pole forcing

`r(j) = 4/(8j-7) - 2/(8j-4) - 1/(8j-3) - 1/(8j-2)`;

`D(j)=(2j-1)(4j-1)(8j-7)(8j-3)`;

`A(j)=D(j)r(j)=120j^2-89j+16`;

and the **source-coefficient-sensitive period-7 clock** `sigma_n=A(n+1) mod 7`.
The identity `D*r=A` is algebraic, independently checked by exact Fraction arithmetic on 200 original indices. Because `A` is an integer polynomial, its clock is period 7. It responds to the predeclared mutation `4→5` in the first signed BBP term: its cleared numerator changes by `(2j−1)(4j−1)(8j−3)`. Original first period = `[5,3,3,5,2,1,2]`; mutant first period = `[6,3,3,5,1,4,6]`; first divergence at n=0. The old index-only clock's first period is `[1,2,3,4,5,6,0]`.

A period-7 clock, however, **does not uniquely authenticate a rational source**: replacing `A(j)` by `A(j)+7K(j)` for any integer polynomial `K` preserves its complete clock. Actual source authentication requires the full exact four-pole rational source and zero seed as separate evidence. The entropy budget changes neither `Q=16` nor clock alphabet size `7`, so the finite `log112` constant in J19 remains valid.

## Exact reversible policy and finite outcomes

The existing encoder was kept fixed, without tuning: `c_n=(d_n+q_n+sigma_n) mod16`, `q_{n+1}=(q_n+3d_n+2sigma_n) mod16`, `q_0=0`. Decoder: `d_n=(c_n−sigma_n−q_n) mod16`. Exact tests show forward/reverse replay for both original and mutant coefficient clocks, and rejection when an original encoded history is decoded using the wrong mutant clock. This verifies reversible arithmetic **given the tape**; it does not verify the physical/ontological model of an observer.

After the source clock was preregistered, the already-certified literal-zero BBP completed digit stream was measured for finite sample lengths N=384,768,1536. All displayed entropy deficits are floating diagnostic values of exact block counts; they are not rigorous Fourier bounds.

| N | k | Input Δ | Index-only Δ | Coefficient-clock Δ | Mutant-clock Δ | Coeff vs input | Coeff vs index |
|---:|---:|---:|---:|---:|---:|---|---|
|384|1|0.011460304|0.021974065|0.013019768|0.021485489|worse|better|
|384|2|0.356757456|0.401056731|0.338133887|0.398277616|better|better|
|768|1|0.010008271|0.010563497|0.008049241|0.011870684|better|better|
|768|2|0.170236277|0.193622962|0.161683259|0.174405112|better|better|
|1536|1|0.003862131|0.005392143|0.005180901|0.005401634|worse|better|
|1536|2|0.081273554|0.090773699|0.088049197|0.078783462|worse|better|

The coefficient clock improves finite k=1 and k=2 deficit relative to the original index-only clock in **all six predeclared comparisons**, but improves relative to the actual input in only **three of six**. These results are finite and **not** an asymptotic sign estimate. Their favorable comparison to the old clock is not a proof of a useful arithmetic cancellation; choosing a clock by comparing held-out deficits after measuring them would invalidate future holdout status. No such retuning was performed.

## Validation and adversarial scope

- Original registered source-clock hypothesis: `SOURCE_CLOCK_PREREG.md` (Git blob `083a9ce7a977c9626b836e737cd465bb7f0cc5a6`) at `a0289b84295b4fdef3a7f3678d6c3cfdd5ea881c`, before these finite measurements.
- `python -m unittest discover -v -s . -p 'test_*.py'`: **33/33** passed in this follow-up sandbox; `python -m compileall -q .` passed.
- Additional original exact arithmetic tests: source cleared identity for j in 1..200 plus j=1007; mutant cleared numerator, period-7 property, full transcript reverse-replay and wrong-clock rejection.
- Replayed independently derived rational Machin/BBP oracle and original previously committed finite holdout scripts; no changes to their results.
- Raw table: `SOURCE_CLOCK_AUDIT_RAW.json`; test log: `SOURCE_CLOCK_AUDIT_TEST_LOG.txt`; deterministic file hashes and parent: `SOURCE_CLOCK_AUDIT_RECEIPT.json`.
- The **full native SUCC suite**, root scripts, formal Lean and exact-head hosted CI were not executed for this follow-up. No status upgrade on π normality, selected signed Weyl, or RH.

**Steelman → crucible → verdict.** Source-coefficient labels can guide a bounded observer. The first period-7 index label lacked coefficient content; the corrected polynomial residue is genuinely coefficient-sensitive, but only within the declared mutant class. The selected infinite signed cancellation remains **OPEN**. The verdict-changing future measurement is a *new, preregistered* source-selected estimate that outperforms the trivial J19 bound while rejecting coherent periodic completions, without leaking an external normality tape or choosing a clock from the tested output.

# BBP Pole-Shift Crucible — exact tests, symbolic witness, known results and open boundary

**Date:** 2026-11-17. Companion to [BBP_POLE_SHIFT_CRUCIBLE.md](BBP_POLE_SHIFT_CRUCIBLE.md). The deliverable is a verified **source-specific rational-coboundary obstruction** and rigorously distinguished hostile controls, not a new π-normality theorem.

## Executed standard-library rational tests

Two locally authored Python files were run:

~~~sh
python -m unittest -v /mnt/data/test_bbp_pole_telescope_oracle.py
python -m unittest -v /mnt/data/test_cold_run_horizon.py
~~~

**Results:** 10 PASS and 7 PASS respectively, **17/17 total**, with 0 failures/errors. Source files on the research PR were fetched back from GitHub and have Git blob SHA-1 values identical to the exact tested copies:

| File | Byte count | Exact matched Git blob SHA |
|---|---:|---|
| [BBP pole/residue and causal-rank controls](../../../tests/test_bbp_pole_telescope_oracle.py) | 5,654 | 93aede9276dd6f966c9dff1055652dd6e00d3c63 |
| [Cold-run/Kempner controls](../../../tests/test_cold_run_horizon.py) | 3,427 | 205bfdb4097f7aa39cc0c1dfbe464d787cf424ee |

Tests include original four distinct integer-shift poles, nonvanishing residues, exact finite rational telescope to locked endpoint 1/2, positive decreasing alternative forcing, same 15/(64n²) asymptotic on finite rational calibration points, vanished shifted-pair weighted residues, rank-one full endpoint-probe Jacobian, indistinguishable terminal impulse histories, exact recovery from a complete causal clock history, sparse zero-seed source and vanishing cold-shell proxy, 1/17 threshold and explicit Kempner near-critical shell windows. The universal theorems are proved in the note rather than inferred from finite tests.

## Independently executed SymPy pole-residue audit

A distinct symbolic derivation used the SymPy residue operation at all four actual original poles and all four alternative-source poles, the symbolic limit for leading terms, and symbolic simplification for the telescoping identity.

**Exact original source pole/residue pairs:**

~~~text
(7/8, 1/2)
(1/2, -1/4)
(3/8, -1/8)
(1/4, -1/8)
~~~

**Exact alternative locked source pole/residue pairs:**

~~~text
(7/8, 2)
(-1/8, -1/8)
(3/4, -2)
(-1/4, 1/8)
~~~

Each alternative orbit's weighted residue equals zero exactly:
\(2+16(-1/8)=0\) and \(-2+16(1/8)=0\). Each original orbit has one isolated nonzero residue and fails the necessary weighted-residue criterion. Both source leading coefficients satisfy
\(\lim_{n\to\infty}n^2r(n)=15/64\) exactly; the alternative identity simplifies to zero:
\(r_{\rm tel}(n)-16a(n)+a(n+1)=0\).

This independent implementation uses the same four authentic coefficients but verifies a **different symbolic decomposition**, so it is a computational cross-check, not a blind arithmetic source witness. The proof that a rational source-telescope cannot exist is the infinite finite-pole support argument in the manuscript.

## Finite direct completed-phase diagnostic for the Kempner hostile example

A separately written mpmath calculation at 380 decimal working digits evaluated the partial infinite-base-16 Kempner endpoint \(\sum_{j=0}^{12}16^{-2^j}\) (the omitted tail is negligible at the stated B) and directly computed \(A_B=1-\Re W_B\) at critical dyadic shells:

| B | Observed phase energy (numerical, not certified interval) | Proven upper bound 32π/(225B) |
|---:|---:|---:|
| 2 | 0.03821197554109443 | 0.2234021442552742 |
| 4 | 0.01910570749295756 | 0.1117010721276371 |
| 8 | 0.009552853744340364 | 0.05585053606381855 |
| 16 | 0.004776426872170182 | 0.02792526803190927 |
| 32 | 0.002388213436085091 | 0.01396263401595464 |
| 64 | 0.001194106718042545 | 0.006981317007977318 |
| 128 | 0.00059705335902127 | 0.00349065850398866 |

The universal counterexample follows from the exact lacunary tail inequality (BPC12), **not** this numerical calculation. The bad-approximability statement is an externally established infinite continued-fraction result of Shallit, not checked by this finite experiment.

## Source-map / external claim discipline

- **PROVED PAPER + exact finite implementation:** the original BBP forcing has nonzero weighted residues in four integer-shift pole orbits, ruling out a rational clock-form solution to \(r(n)=16h(n)-h(n+1)\); nevertheless its actual nonrational future tail satisfies that equation on integer clocks.
- **PROVED PAPER + exact finite controls:** positivity, monotonicity, rational telescope and source-zero lock in an *alternative* four-pole forcing with the same leading asymptotic.
- **PROVED PAPER + exact finite controls:** terminal observation rank-one response versus full-rank clock history, including causal impulse ambiguity.
- **PROVED PAPER + exact finite controls:** sharp 1/17 cold-run bound and κ-base-16 R0 failure along dyadic shells; its bounded partial quotients come from cited published literature.
- **EXTERNAL CONDITIONAL:** OpenAI's September 2026 preprint and associated Lean scope report claim μ(π)=2; external machine check has been reported, but independent paper-level mathematical referee and semantic audit remain incomplete. The conditional consequence \(v_{16}(\pi)\le1\) is not R0. Do not promote this external preprint without tracking its provenance.
- **UNVERIFIED:** the missing source-selected quantitative link from uncancelled pole orbit residues to *positive density* of separated integer windings on each late BBP shell.
- **OPEN:** \(R_B(0)\ge\delta>0\) eventually, R0, and base-16 π normality.

**Not executed on this new head:** full root SUCC mandatory gates, Main XXIV/XXV/XXVI integration suites, Lean kernel certification of the new result, independent mathematical peer review, and completion of hosted GitHub CI. The complete 14,577-test prior receipt belongs to an **earlier exact commit** and is not recycled as a pass on this head.

## Next falsifiable research advance

Freeze a source-specific arithmetic inequality linking the four noncanceling weighted pole residues to the *original zero-selected integer winding* at U_(2B), rather than to a rational-clock antiderivative. The next proof must produce \(\epsilon,\theta>0\) such that at least \(\theta B\) terminal backward directions have torus distance ≥ε for every sufficiently late B. Show why no variant with the same null seed, same leading asymptotic, but shift-paired poles can satisfy the proposed source hypothesis; simultaneously reject the slowly escaping badly approximable Kempner source, coherent wrong seed, and terminal/history aliases. Until this quantitative bridge is proved, π normality is not established.

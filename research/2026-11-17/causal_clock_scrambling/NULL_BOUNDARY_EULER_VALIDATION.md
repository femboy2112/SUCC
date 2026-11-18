# BBP Null-Boundary Cocycle — exact validation and limits

**Date:** 2026-11-17. Companion to [NULL_BOUNDARY_EULER_COCYCLE.md](NULL_BOUNDARY_EULER_COCYCLE.md). Original forcing is the literal signed four-pole BBP \(r(n)\), and the actual source seed remains \(U_0=0\). All nonzero seed values are labelled *counterfactual interventions*. Nothing here proves R0 or base-16 normality.

## Focused exact tests, byte-matched committed artifact

Executed locally after replacing an initially tautological derivative check with an **independently computed formal power-series coefficient recurrence**:

~~~sh
python -m unittest discover -s /mnt/data -p 'test_bbp_null_boundary_product.py' -v
~~~

**9 tests PASSED, 0 errors, 0 failures.** The tested local file and the branch copy [tests/test_bbp_null_boundary_product.py](../../../tests/test_bbp_null_boundary_product.py) have the **same complete Git blob SHA**:

~~~text
716775b25e126d9c726ad2b2f02764731d916597
~~~

The byte identity was checked after a harmless differing trailing blank line was repaired in the local executable copy; the initial different hashes are not cited as proof of a pass on the remote bytes. The final test passes were run on the exact code published in the final blob.

The tests cover: original \(r(1)=47/15\), \(P_1=47/240\), exact source recurrence and finite endpoint sums; the direct N-factor product for several genuinely different nonnegative seeds; the exact zero at the first transfer factor, the nonzero suffix and their composition; higher jets computed from the **independent formal equation** \((P_N+s)G_N(s)=s\); dual-number first-jet coefficient multiplication; finite negative-seed singular denominators; a different **perfectly locked zero-seeded forcing** with the same null-boundary and nonzero-jet pattern; and the exact first-jet decomposition \(1/P_N=(1/P_1)(P_1/P_N)\).

## Independent symbolic verification

A separate SymPy implementation started with \(G(s)=s/(s+P)\) for an indeterminate positive real \(P\), and verified for each \(1\le k\le5\) that

\[
\left.\partial_s^k G(s)\right|_{s=0}
=(-1)^{k-1}k!/P^k
\]

by independent symbolic differentiation and simplification. All five symbolic differences were **exactly zero**. It also verified that

\[
\frac{s}{s+P_1}\frac{s+P_1}{s+P}
=\frac{s}{s+P}
\]

as a rational identity with independent indeterminates \(s,P_1,P\).

This confirms algebraic formulas, not any random digit distribution.

## Separate 75-digit completed-endpoint diagnostic

A direct 75-digit mpmath computation of the genuine BBP weighted source sum, at \(N=1,2,4,8,16,32\), compared the zero-seed nonzero suffix \(P_1/P_N\) to \(47/(15\pi)\), and the first derivative \(1/P_N\) to \(16/\pi\). Representative suffix absolute differences:

| N | Numeric \(\left|P_1/P_N-47/(15\pi)\right|\) |
|---:|---:|
| 1 | 0.002629023291 |
| 2 | 0.00005403276481 |
| 4 | 6.223181815e−8 |
| 8 | 2.604972733e−13 |
| 16 | 1.593987978e−23 |
| 32 | 2.21730998e−43 |

These values are **not certified interval calculations**; the infinite limit is justified by the classical BBP source identity and the convergence of the positive weighted sum.

## No-go scope and next actual arithmetic probe

- The individual factors are only defined where each \(U_{n+1}(s)\ne0\); the rational simplification does not silently extend the original raw product through singular intermediate states. The positive seed regime \(s\ge0\) is safe, and analytic jets near \(s=0\) are safe because \(P_N\ge P_1>0\).
- The product \(G_\infty(0)=0\) has nontrivial first response \(16/\pi\), a **source-dependent scalar endpoint**, not a source-selected signed Weyl density.
- An alternative null-seeded forcing \(f(1)=16,f(n>1)=0\) has exactly locked completed phase, yet \(G_\infty(0)=0\) and \(G'_\infty(0)=1\ne0\). This decisively refutes the inference “zero boundary plus coherent suffix implies orbit escape.”
- Prime Euler factors \(1-p\) at \(s=-1\) are all nonzero for actual primes \(p\ge2\); BBP's first chronological source factor is exactly zero. The similarity of multiplicative *forms* is not a prime-to-clock source-identification theorem.
- **Not claimed on this exact PR head:** full SUCC repository unittest suite, root AGENTS provenance/observer/ordinal gates, Lean kernel formalization, a physical vacuum probe, completed GitHub hosted checks, R0, or π normality.

**Verdict-changing step:** supply an independent, source-authenticated *chronological* response coupling all four BBP poles to selected zero-seed carry/winding, with a universal late-shell estimate that excludes the locked and sparse countermodels. More derivatives of the endpoint-only function \(s/(s+\pi/16)\) do not by themselves pay that arithmetic debt.

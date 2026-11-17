# Movable Boundary Order-Lift — exact executed validation receipt

**Date:** 2026-11-16. Scope: [theorem note MBO-01–08](MOVABLE_BOUNDARY_ORDER_LIFT.md). No claim of stochastic π digits, physical observer coupling, proof of R0, full normality, RH or independent theorem priority.

## Executed focused code

The locally authored Python standard-library test script was run before publication using Python unittest verbose on the source at /mnt/data/test_boundary_order_lift.py.

**Result: 11/11 PASS; 0 failures; 0 errors.** The tested script has Git blob SHA-1:

~~~text
0568f278a2e3285f9c7acad2f2f83c1f4c9556a2
~~~

This equals GitHub's fetched blob SHA for the committed [tests/test_boundary_order_lift.py](../../../tests/test_boundary_order_lift.py). The code uses exact Fraction values in all finite C4 joint distributions, pair/triple products and original BBP arithmetic; its Shannon-information endpoint calculation at p=0,1 additionally uses Python floating log2, with an exact analytic derivation in the main note.

Tests covered: four possible C4 source phases, four intervention strengths p, exact equality of complete single-channel laws, conditional mean-zero, exact second-order pZ, intervention contrast, fully independent p=0 null, full reconstruction at p=1, single-channel unit-variance false positive, third-order source syndrome with all pair marginals blind, source recurrence/gauge-integer tests, strict finite forcing monotonicity, new second-order speed-envelope and old-envelope comparison, finite R0 margins and finite-prior mutual-information endpoints.

## Independent symbolic audit of coupling

A separately implemented SymPy version symbolically enumerated all 4×4 shared/independent mask combinations for each Z in {1,i,-1,-i}, with an **indeterminate** real coupling variable p.

Results: all four source phases satisfied exactly:

~~~text
full marginal A = uniform C4
full marginal B = uniform C4
cross moment E[conj(A)*B] = p*Z
derivative d/dp = Z
~~~

These are exact symbolic rational-polynomial calculations. This is an independent *implementation* of the same conditional toy law, not an independent physical observation.

The main theorem's arbitrary phase Z in the circle requires **continuous Haar** masks. The finite C4 audit has deliberately narrower scope: C4 marginals are guaranteed source-independent only for the four C4 source phases.

## Independent finite BBP arithmetic comparison

Another exact Fraction script reconstructed the authenticated original BBP recurrence, computed the old speed envelope and the new second-order envelope, and checked that the new envelope strictly exceeds the old at every listed shell:

| B | Old speed certificate | Improved source-pair certificate | Exact strict improvement |
|---:|---:|---:|---|
| 16 | 1.115511010778806 | 1.118497925016514 | PASS |
| 32 | 1.419544018700512 | 1.420255787319224 | PASS |
| 64 | 1.457849048509468 | 1.458084570487634 | PASS |
| 128 | 1.335706813143393 | 1.335759884755608 | PASS |
| 256 | 1.332030683976077 | 1.332044339267756 | PASS |

Displayed decimals are for readability. The strict comparisons used **entire exact rational Fractions**. Both implementations share the original four signed poles and cannot independently authenticate the imported BBP π endpoint. These clocks were previously explored and are not an unseen holdout.

## What is established versus unpaid

- **PROVED PAPER/CLASSICAL:** independent Haar masks erase each individual source-dependent marginal; a tunable shared mask produces pZ in the second-order cross moment; sample mean-square error is (1-p²)/(Np²); triple masks exhibit genuinely third-order-only source dependence.
- **PROVED PAPER/SOURCE-CONDITIONED:** original BBP forced phase difference, strict monotonicity of the original positive Mellin forcing, 0<T_(n+1)<T_n<r(n+1)/15, and corrected objective step bound.
- **OBSERVED FINITE EXACT:** the new rational relative-speed envelope strictly improves the earlier original-source bound at B=16,32,64,128,256.
- **NOT RUN/NOT CLAIMED:** root repository provenance gate, full root unittest suite, observer foundations and ordinal report scripts, Main XXIV/XXV/XXVI integration replays, Lean kernel proof, independent blind mathematical referee, or hosted CI success on the final draft head.
- **UNVERIFIED:** an independently available physical or computational instrument that genuinely couples to the original zero-seeded BBP timeline and yields fresh source-specific conditional phase information not already encoded by the rational recurrence.
- **OPEN:** a positive source-selected lower bound for the newly sharpened speed certificate on **every** sufficiently late integer shell; hence R0, base-16 π-normality and RH remain open.

**Verdict-changing probe:** declare an accessible source-connected intervention that changes the *conditional joint law* without changing the first-order marginals, register its signed response and distinguish it from the identical-marginal independent-mask null. Then derive a zero-seed/four-pole/odd-denominator-sensitive all-shell correlation inequality that survives counterfeit and coboundary controls.

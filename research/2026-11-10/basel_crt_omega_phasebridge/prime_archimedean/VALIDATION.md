# Reproduction, controls, and CI firewall

## Local focused run

Run on Python 3.13 (stdlib only):

```sh
python -W error -m unittest -v test_prime_weil_probe.py
```

**Executed locally on 2026-11-10:** 21 tests passed after repairing an incorrect expected sign in the synthetic two-fiber test; the initial failure and repair are disclosed. The mutation of the 2m/6m fiber reverses the ×2 correlation but **preserves** the ×3 correlation, because both endpoints of each ×3 edge receive the same flip. The original incorrect expectation had the ×3 sign reversed; that was a test-specification defect, not a theorem.

The suite checks: factorization and prime-power classifier; all edges absent for one dyadic epoch; four exact 2/3-diamond edges and no q=6 primitive edge; rational unphased and negative-fiber coefficients; 20 exact flat Wilson loops and a nonflat *mixed finite difference*; Möbius convolution reconstruction across 150 integers; all-prime-power Λ defect coefficients; literal BBP four-pole positivity and rational completed prefixes; the 12-term exact **source-selected phase** sign and mixed-6 certificates; bad precision horizons rejected.

The code does not evaluate nontrivial zeta zeros, calculate the analytic Weil form numerically, or claim independent interval certification of any other sine/cosine. The certified sign theorem uses rational phase subintervals plus elementary quadrant inequalities. It does not turn finite agreement into an asymptotic theorem.

## Source contracts and exclusion

- Original four-pole `R(j)` preserved; real `P_∞=π/16`, literal `U_0=0` and all real carries retained.
- Parent #585 / Main XXIII #584 stack; no source mutations, `main` write, Lean changes, archive changes, workflows or release.
- Original source finite-horizon wrong seed `−P_L` and coherent infinite wrong seed `−π/16` are **separate controls**.
- Weil formula includes every `Λ(p^k)` and completed `Γ/pole` contribution. RH positivity is used only as a conditional interpretation.
- No original full ~13,000 SUCC tests were executed in this round. The parent integration branch's independent required native CI gates remain required before any main merge.

**Independent review needed:** Check normalization `f^♯(x)=x^(-1)f(1/x)`, Mellin shift, smooth packet isolation, multiplicative prime-edge coefficients, and rational quadrants against the canonical `π/16` BBP source. Then attempt an actual source-locked off-diagonal Weil-to-Basel estimate on **new** non-dyadic holdout epochs. No claim of novel academic priority.

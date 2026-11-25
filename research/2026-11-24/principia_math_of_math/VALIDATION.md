# Principia Genesis — cumulative validation and source receipts

**Date:** 2026-11-24. Research branch: research/principia-math-of-mathematics-2026-11-24. Pinned parent main: 81be6b897ae980b801a3b9de9e22ef81e8360bfb. **Status:** local mathematical/prototype validation. Not a complete SUCC worktree or original RH proof rebuild.

## Latest coupled-mass and higher-order rounds — exact receipts

After the earlier 67-test causal-memory round, the source-shaped Python 3.13.5 overlay was extended with exact signed bilinear and arbitrary finite-arity coupling pushforwards and the source-memory-to-weighted-kernel bridge.

Executed:

    PYTHONPATH=. python -m unittest discover -s tests -p 'test_principia_*.py' -q

Observed:

    ----------------------------------------------------------------------
    Ran 81 tests in 0.065s

    OK

**81/81 cumulative passing:** previous 67 plus ten exact coupled-mass and four higher-order tensor/source-memory tests. The higher-order controls cover rank 2–7 binary parity families and every proper-coordinate marginal. All authentic Gaussian arithmetic input comes from the existing exact Z[i] source; no fitted theta moments.

Additional independent validation:

    PYTHONPATH=. python independent_coupling_mass_oracle.py

Observed:

    COUPLING_MASS_INDEPENDENT_SYMPY_PASS 180 source systems, 4 actual CM shell checks

The independent SymPy implementation computes an incidence matrix Q on 180 deterministic fresh signed rational source systems and confirms the native results against Q^T a and Q^T K Q. It also tests arbitrary class-constant features and actual Gaussian norm-shell source coefficients. **Algorithmically independent, but not an external referee.** Prior 84-source causal-memory all-word brute-force oracle still passed.

New current Git blobs matched the exact files executed in the local overlay:

| Source | Exact uploaded blob SHA-1 |
| --- | --- |
| observational_succ/principia_coupling_mass.py | f41310e8ea2e59b6a50002c6acdb205cea156e02 |
| tests/test_principia_coupling_mass.py | 4f17937c995b33241d66ec2b96f0887c31491a8d |
| tests/test_principia_higher_coupling.py | 05635230fa9d6922e1fb92619925b32dad25b78b |
| research/2026-11-24/principia_math_of_math/independent_coupling_mass_oracle.py | 973b1ec944cc24ebefd9f4c0059136656b0e9d3d |

All four blob IDs match the tested sources. **Mandatory full-SUCC root tests, hosted CI, the full Lean repository and independent peer review have NOT been executed.** The universal finite mathematical claims are supported by derivations in COUPLING_MASS.md, not inferred from finitely many samples.

## Prior causal-memory round — exact local and independent-source receipts

**Executed after the prior CM round** in the same isolated Python 3.13.5 source-shaped overlay:

    PYTHONPATH=. python -m unittest discover -s tests -p 'test_principia_*.py' -q

Observed:

    ----------------------------------------------------------------------
    Ran 67 tests in 0.053s

    OK

The cumulative 67 consist of the previous **51** and **16** new methods from tests/test_principia_causal_memory.py. New controls verify the original-world/current-state memory update, forged/source-mutated histories, coarsest finite future-target congruence, independent pair-distinguishability, source-sensitive future-null versus a silent preparation, exact source-world coupling versus marginal readouts, reset/no-reset operational access, all-branches policy verification, and genuine Gaussian theta null mechanisms.

Independent research oracle:

    PYTHONPATH=. python independent_causal_memory_oracle.py

Observed:

    CAUSAL_MEMORY_INDEPENDENT_BRUTE_FORCE_PASS 84 fresh carriers, all <=N-1 words

This oracle uses Random(20261124), generates 84 fresh deterministic mathematical source laws, enumerates all legal words through N−1 where N is the reachable marked-state count, compares their exact future response signatures against the native Moore quotient, independently replays four observed actions per source, and audits any finite produced target-identification policy. **Same researcher/model provenance**; algorithmically different checks, not an external blind referee. Compiler checks for the new Python files also passed.

Exact newly uploaded GitHub source blobs checked against Git hash-object on the actually executed files:

| New file | Git blob SHA-1 |
| --- | --- |
| observational_succ/principia_causal_memory.py | 917a14de44fb46fdd6cf7c23385d4a5778975fe2 |
| tests/test_principia_causal_memory.py | b81aa69e4029670fe905a8440cca1bf8f47c7158 |
| research/2026-11-24/principia_math_of_math/independent_causal_memory_oracle.py | 9cbd47e2a3fd2c0d698ee3e2f8c8c48f35064850 |

All three new executable blobs MATCH. The CAUSAL_MEMORY.md mathematical proofs are classical paper derivations, not Lean kernel certifications. The **full SUCC root AGENTS.md gates, hosted GitHub CI, and original RH Lean build remain NOT RUN** in this environment.

## Executed source-shaped overlay

All core Principia files from this draft were assembled in an isolated Python 3.13.5 source-shaped overlay. The following **was actually run** after adding the CM theta, period-normalized jets, sign-coordinate and analytic-completion branches:

    PYTHONPATH=. python -m unittest discover -s tests -p 'test_principia_*.py' -q

Observed:

    ----------------------------------------------------------------------
    Ran 51 tests in 0.041s

    OK

The 51 cases comprise the inherited **32** Principia Genesis focused tests (path/source, integer null-height, exact knowledge-volume and height-two formal resolvent) and **19** additional CM-theta/lemniscate cases. The new cases include numerous nested parameter combinations over inert primes 3, 7, 11; rank 1–4; independent nonzero integer minors; exact p-valuation floors; real Gaussian weighted-Hadamard and full-energy majorants; elliptic sine Hurwitz jets; the quartic Hasse invariant; the normalized \(\sigma^2\wp\) period-jet recurrence; simple-theta \(v_3(r_{30})=14<45\); the p=3 positive/negative Honda sign; signed Honda coordinate through degree 40; and exact rational finite-to-infinite holomorphic theta tail bounds.

The hostile tests reject split/composite fake primes, source/normalization swaps, duplicate zero minors, radical/holomorphic derivative confusion, invalid heat weights, and inadmissible theta-tail cutoffs. Nonintegral and wrong-prime defects remain explicit failures.

Also run:

    python -m compileall -q observational_succ/principia_* tests/test_principia_*.py

Observed: exit code 0.

## Independent analytic/arithmetic source checks

A separate SymPy oracle was executed on the local candidate:

    PYTHONPATH=. python research/2026-11-24/principia_math_of_math/independent_cm_theta_oracle.py

Observed:

    SYMPY_INDEPENDENT_CM_THETA_CERTIFICATES_PASS 20
    SYMPY_INDEPENDENT_LEMNISCATE_INVERSION_PASS 5
    NUMERICAL_CM_PERIOD_THETA_CHECK_PASS (not an interval proof) 1.18034059901609623

The **20** SymPy checks independently recompute the Gaussian integer shell moments (using complex algebraic powers), the integer determinant and the Gaussian-weighted determinant for different inert primes and ranks. The **five** exact lemniscate controls compute the inverse elliptic integral by independent formal power-series reversion, rather than using the differentiated ODE source.

The last check computes \(\Theta(0,1)\), the lemniscatic period \(\bar\omega\), and normalized theta derivatives \(r_1,r_2,r_3\) by independent 80-digit mpmath series/integrals and matches the classical period formulas. It is a **numerical diagnostic**, not an independently proved analytic theorem, nor a claimed interval arithmetic certificate. The termwise and finite-to-analytic theta-tail theorem is separately proved in CM_THETA_TWO_PLACE.md T14 using an explicit rational majorant.

Prior focused independent Genesis controls (unchanged from the previous version of this draft): **360** SymPy polynomial factorization/height cases, **100** SymPy knowledge-rank cases and **4** formal-inverse comparisons. They are prior recorded executions, not rerun here.

## Exact source identity checked

The following **three current branch blobs were fetched and compared to Git SHA-1 of the exactly tested local source files**:

| Source file | Current Git blob SHA-1 |
| --- | --- |
| observational_succ/principia_cm_theta.py | be249b7ff12caace9a75acfd197f5bcdcca9aa83 |
| observational_succ/principia_cm_period.py | 2e26924d05859923a1736225e27f8a7f8b9720df |
| tests/test_principia_cm_theta.py | 2657b449dc425a2d6ebc9e9fc8222150f0d67e17 |

**All three match the executed local files.** The separately uploaded independent_cm_theta_oracle.py is an optional research script with mathematically equivalent execution statements but was not byte-identical to the local oracle; it is **not** claimed as an exact-source-matched run. An independent agent should rerun it on the branch before promoting its receipt.

Prior Genesis executable blobs and checks are recorded in the previous version of this validation file / original #690 PR body.

## Mathematical proof authority and boundaries

T9–T11 and T14 in CM_THETA_TWO_PLACE.md supply complete elementary classical arguments for the Gaussian CM source shell transport, Vandermonde nonzero minor and valuation, same-map Gaussian norm and fully paid normalization cost, and analytic source completion. T12 supplies exact ODE and rational Taylor recurrences, **conditional on a cited classical theta/Weierstrass period identity** proved in the public November 22 exposition; that identity was not independently proved here. T13 proves p=3 degree-nine sign mismatch and checks additional finite inert-prime cases; **the full integral coordinate equivalence is unverified**.

The full automorphic CM theta-kernel integrality, repeated theta lifts, real Petersson/Rallis norm, conductor/Galois and trace-formula estimates, the weighted main inequality (M), and a complete native SUCC mathematical reconstruction of RH are **not proved here**. The paper's lemniscate is an illustration **not used** in the external Lean proof; the present finite-shell matrix is not its automorphic theta-period map.

## Mandatory SUCC gates NOT run

The parent repository AGENTS.md requires, before merging or promoting an inherited theorem:

    python scripts/verify_provenance.py
    python -m unittest discover -s tests -p 'test_*.py'
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py

These were **not run** on a complete checkout; neither remote GitHub Actions nor a Lean build nor independent external peer review was executed during this round. Finite simulation is not a universal proof. The cited mathematical derivations, not the numeric examples, support the elementary universal claims.

## Next falsifier

Reconstruct an *actual* theta-lift kernel from the published RH proof in its integral CM formal-group coordinate and prove that its period-normalized nonzero lattice minors have simultaneous local valuations and independent real bounds; check trace/rank, conductor factors, and source-specific Frobenius units. Failure to provide that **same** source map is an access/pathway gap, not a reason to rename a different CM theta map as the proof's own.

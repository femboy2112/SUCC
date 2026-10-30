# Validation — primitive carrier / Gamma completion / CRT digit bridge

## Authority and source passport

- Local research date: **2026-10-29 America/New_York**.
- Exact pinned parent: `femboy2112/SUCC@e02933591e7b7486376acb9847e00fd01d9ae498`, research draft PR #383. It inherits the full four-pole source, original marked `U0=0`, #367 convolution, #373 inertial minimal preparation, #379 Gamma tiling and #381 opposing observers. No direct integration of sibling #372.
- Original source used unchanged: `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`. Exact comparison at 150 clocks independently checks original numerator `120n²−89n+16` and denominator `(2n−1)(4n−1)(8n−7)(8n−3)`; resultant/discriminant 2,3,5.
- Original archived files, workflows, production code, registries, claim namespace and `main` are not modified. This is an additive research child branch. Source-manifest Git blob pins below the folder reference parent head, not recomputed content from public search.

## Actual locally executed gates

| Command (from isolated folder) | Actual result | Authority boundary |
|---|---|---|
| `python minimal_pole_gamma.py` | `MINIMAL_POLE_GAMMA_EXACT_PASS` 100 rational clock/product checks | Exact source model, not full SUCC |
| `python fermat_unit_bridge.py` | `FERMAT_CRT_UNIT_BRIDGE_PASS`, 64 multiplicative products, distinct U255/U256 | Classical finite groups |
| `python -m unittest discover -s . -p 'test_*.py' -v` | **24/24 PASS**, 0 skips | Exactly these new research methods |
| `python independent_oracle.py` | **904 independent exact SymPy/Fraction assertions PASS** | Imports neither research production module; universal claims still paper proofs |
| `python numerical_holdouts.py` | **22 at 90 dps PASS**, including native Gamma product & Oily logarithmic phase no-go observations | High precision is not an interval certificate |
| `python certified_interval.py` | **RATIONAL_K_H_CERTIFICATE_PASS** | Fraction + positive `atanh` remainders + analytic tail; rigorous all-N interval |
| `python -m compileall -q .` | Pass | Syntax only |
| `git ls-remote https://github.com/femboy2112/SUCC.git HEAD` | **FAIL**, local DNS cannot resolve `github.com` | Root repo not cloned; not counted as mathematical failure |

All actual outputs are preserved in `receipts/`. An initial focused test expectation and an independent-oracle algebraic comparison bug were corrected, and the false failures are recorded in `receipts/INITIAL_HARNESS_CORRECTION.md`; **never claim a continuously green initial run**. No original BBP source or implementation was altered to resolve those harness errors.

## Universal paper proofs versus finite evidence

- `MC-01` through `MC-03`: algebraic numerator/root-product ratio and the *all-positive-integer-weights* cost minimization; source positivity via Laplace kernel and Gamma(2) transform limit. No computer enumeration is required for the universal bounds.
- `MC-06` through `MC-09`: exact rational unit-step logarithm; all-index strict harmonic comparison `1/(15n)<eta_n<1/(15n)+7/(180n²)`; exact Γ recurrence; the **rigorous** tail `0<K∞−K_N<7/(180N)`. The executable interval uses rational positive atanh series and a mathematically proved remainder, not a floating-point convergence claim.
- `MC-11`/`MC-11b`: explicit U15/U16 group isomorphism, exact all-256-entry Gram identity `BB*=8I`, invertibility for **every** single digit function, and explicit U255/U256 non-isomorphism. None is a source-derived digit time-evolution law.
- `MC-13`: original polynomial/resultant and discriminant certified by independent symbolic elimination; primes 2,3,5 are exceptional **for this rational map**, not a proved causal mechanism for π-normality.
- `MC-14`: proof of the universal signed reweighting `O(log N/N)` no-go and `c`-phase coherent-limit modulus `1/sqrt(1+(c/15)^2)`. This includes the explicit real same-forcing coherent seed `−π/16`, not a synthetic changed-source artifact.

## Numeric illustrations (not general proof certificates)

```
Gamma log completion C_gamma = 0.0906871865238264538858771685077976541...
Euler/harmonic finite part K_H = 0.0522061421970575965121096958356374920...
Oily packet contrast lambda-gamma = 0.0408183238483619875980747442832356867...
Gamma-vs-golden contrast 15*K_H-(lambda-gamma) = 0.7422738091075019600...
Source-only phase twist c=15, N=20000: |mean|≈0.70714722916761581
Analytically proved coherent limit modulus at c=15: exactly 1/sqrt(2)
```

**Rigorous interval, not float-only:** `receipts/K_H_CERTIFICATE.json` stores exact numerator/denominator rational endpoints at N=128 with four positive atanh terms. As displayed only, `0.052036743511030673 < K_H < 0.05234056295547751`. Its tail is proved for all unseen n>N; 90-dps mpmath only corroborates.

## Claims not made / integration gates

- The conditional minimum-cost primitive positive integer four-pole model is NOT proved to be the unique physically necessary or the shortest universal algorithmic description of the BBP source. It recovers an existing authentic source under explicit axioms.
- The Fermat/CRT, Euler–Gamma and golden/Oily connections are individually exact with **typed interfaces**; no canonical physical source-to-signed-carry functor is derived.
- The complete 16-state hybrid character basis is an invertible finite observation. It cannot prove either the one-digit or all-block equidistribution of the selected π digits.
- **π base-16 normality, RH, new signed o(N) Weyl estimates, Lean proofs and external academic novelty remain OPEN / UNVERIFIED.**
- Full root repository `python scripts/verify_provenance.py`, `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py`, full math-memory graph/catalog and exact-head hosted CI were NOT run in this isolated local checkout. Check the new draft PR's actual hosted runs and do not promote status without source/CI revalidation.

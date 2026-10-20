# PSD — Portable Sundial prime-clock / rational SUCC claim supplement

**Date:** 2026-10-19. **Parent:** Academic Main V at `455600a2e013895c36238a3a97e0f470fd7ba197`.  
**Full definitions, proofs, countermodels, tool contracts:** [research dossier](../research/2026-10-19/PORTABLE_PRIME_SUNDIAL.md).  
**Global status:** elementary classical arithmetic, independently tested finite model; no physical time/source authentication and no established academic priority. **ABC/RH OPEN; signed S4 OPEN.**

| ID | Quantified source-typed statement | Status | Crucible / boundary |
|---|---|---|---|
| PSD-01 | All positive integer frames `(a,b;u,v)`: independent k,l updates commute; mixed finite ratio difference is `-uv/[B_l(B_l+v)]` | CLASSICAL / PROVED PAPER | Nonzero report coupling is not noncommuting source dynamics |
| PSD-02 | On diagonal n, `D=ub-va` is invariant; exact drift `F_(n+1)-F_n=D/[B_n(B_n+v)]`, offset `F_n-u/v=-D/(vB_n)` | CLASSICAL / PROVED PAPER | Exact sign tests; D may be negative or zero |
| PSD-03 | `gcd(A_n,B_n)` divides `D` for all n, so nonzero D bounds every common prime valuation | CLASSICAL / PROVED PAPER | D=0 stationary family refutes finite bound without condition |
| PSD-04 | If D=0 and `g=gcd(u,v)`, `gcd(A_n,B_n)=t+ng` for the unique t determined by `a=t(u/g),b=t(v/g)` | CLASSICAL / PROVED PAPER | Unbounded cancellation with stationary ratio |
| PSD-05 | For genuine p,r, solvability of `a+nu=0 mod p^r` iff `p^min(r,v_p(u))|a`; solution is one p-power class | CLASSICAL / PROVED PAPER | Noninvertible or empty clocks handled exactly |
| PSD-06 | If p does not divide uv, `p^r|gcd(A_n,B_n)` for some n iff `p^r|D` | CLASSICAL / PROVED PAPER | D divisible p is not sufficient when p divides a unit |
| PSD-07 | For genuine prime-power wheel W coprime uv, phase `l0-k0=-D/(uv) mod W` glues and an explicit k,l realizes both zero clocks | CLASSICAL / PROVED PAPER | Finite CRT only; no source/primality/physical time inference |
| PSD-08 | For nonzero D, largest divisor M of `|D|` coprime uv divides some diagonal gcd | CLASSICAL / PROVED PAPER | Explicit (a,b;u,v)=(1,20;3,5), M=11,n=7 |
| PSD-09 | RAD-anchored units: each later radical is original RAD times primes born outside support; RIS quotient updates exactly | CLASSICAL / PROVED PAPER | 12/18 → 24/30; prime 5 newly appears only in denominator |
| PSD-10 | Homogeneous full-frame scale preserves rational path; independent rebase shifts phase by h-j; reduction-only quotient can erase future | CLASSICAL / PROVED PAPER | 1/2=2/4 but unit-one next 2/3 vs 3/5 |
| PSD-11 | The finite prime sundial gives original-source authenticated or physical time data, or determines a full adelic clock | UNVERIFIED / NOT CLAIMED | Source labels are declared; finite phases cannot infer an actual carrier |
| PSD-12 | The sundial yields an improved ABC exceptional-set exponent or authentic signed Weil positivity/RH | UNVERIFIED / NOT CLAIMED | Requires genuine primitive-triple uniform correlations and source-to-Weil equality |
| PSD-13 | Three exact rational reports at (0,0),(1,0),(0,1) reconstruct (a/b,u/b,v/b), hence all reports, and classify frames up to one positive rational homothety | CLASSICAL / PROVED PAPER; TESTED FINITE | Ratios do not authenticate original source or integer scale |
| PSD-14 | Every proper subset of the *canonical* three probes admits nonhomothetic countermodels; even all rational reports leave absolute p-adic occupations ambiguous | CLASSICAL / PROVED PAPER; TESTED FINITE | Three explicit omitted-probe pairs plus homogeneous scaling; no universal adaptive-probe minimality claimed |

**Reproduction:** `python -m unittest discover -s tests -p 'test_portable_prime_sundial.py' -v`, `python -m scripts.portable_prime_sundial_probe`.

**Frozen finite receipt:** [PORTABLE_SUNDIAL_FINITE_RECEIPT.json](../research/2026-10-19/PORTABLE_SUNDIAL_FINITE_RECEIPT.json) — 256 declared frames, 1,024 p-power reads, 306 satisfiable diagonal windows, exact three-shadow reconstruction/source-scale aliases, and nonunit/RAD-birth/stationary negative controls. These tests calibrate a finite grammar, not a universal theorem.

**Dependency trace:** `observational_succ/rad_ris_transport.py` (genuine RAD/RIS/factor oracle), `prime_phase_clocks.py` (distinct prior clock program), `formal/EODCS_CausalDescent.lean` and `formal/MetaChoiceRelationalDescent.lean` (observation descent), Academic Main V provenance. All old modules are imported/read, not rewritten. No original Weil identity or zero ordinate is used.

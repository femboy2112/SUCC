# Periodic-tail enclosure — claim supplement (PTE series)

**Research branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`, stacked on bootstrap `11781889a3822d8f2602716fdc12f80755f1b399`; main ancestor `6e0d88f1b235b85188393bbcd64ac0436cb71a70`. **RH PROVED: no.** No zero locations are construction inputs.

| ID | Exact statement/scope | Status | Evidence and next falsifier |
|---|---|---|---|
| PTE-01 | For finite exact-rational residue-clock family `F(k)=Σa_n(k mod n)/n`, `L=lcm(moduli)`, the global squared `L²(w)` error `E=Σ|1-F(k)|²/(k(k+1))` satisfies `P_K + m/(K+1) <= E <= P_K + M/(K+1)` with `m,M` the exact min/max of `|1-F(k)|²` over `1..L`. | PROVED LOCAL | Exact periodicity + telescoping `Σ_{k>K}1/(k(k+1))=1/(K+1)`; `observational_succ/periodic_tail_enclosure.py`, `tests/test_periodic_tail_enclosure.py` (8 assertions), brackets `1-ln 2` independently. |
| PTE-02 | The enclosure strictly sharpens the prior ZCR-07 bound `(1+Σ|a_n|)²/(K+1)`, since `M < (1+Σ|a_n|)²` for every nonempty family, and supplies a positive lower bound generically. | PROVED LOCAL | `|r_n(k)| <= (n-1)/n < 1`; exact ratios 36/529 (ZCR-04 family) and 1/9 (single clock). |
| PTE-03 | The sharp enclosure is itself a *global* L² convergence proof (uniform in the coefficient family) toward a zero error, or a source-faithful instrument that distinguishes Euler from non-Euler sources. | UNVERIFIED / NOT CLAIMED | The enclosure width `(M-m)/(K+1)->0` at fixed `L`, but `L` grows with the family and ZCR-06 gives only `1/L² -> 0`; it is a convergent *finite* certificate, not a global Nyman bound (N05). Periodicity uses only `r_n`, so it is source-blind by design. |

**No priority claim** for residue clocks, periodicity, or telescoping; these are elementary. The novel artifact is the exact two-sided periodic enclosure that strictly improves the existing finite certificate and the executable receipt for it.

Validation (run, do not pre-claim):

```sh
python3 -m unittest tests.test_periodic_tail_enclosure -v
python3 scripts/verify_succ_property_graph.py
```

**Next verdict changer:** refining the tail into the exactly-computable synchronized `jL` cells plus a residual, to push the lower bound from `m/(K+1)` toward `1/L²` plus a computable residual term — still a finite certificate, but a sharper one.

| TS-01 | With `c_r=|1−F(r)|²` (`c_L=1` exact), `m'=min_{r<L}c_r`, `M'=max_{r<L}c_r`, `B=Σ_{jL>K}1/(jL(jL+1))`: `P_K+B+m'(1/(K+1)−B) ≤ E ≤ P_K+B+M'(1/(K+1)−B)`. Lower bound strictly sharper than PTE-01 always; upper strictly sharper when `M'≠1`; 65× tighter in the blackout-dominated regime (a₂=2 brackets 1−ln 2). | PROVED LOCAL | `observational_succ/tail_split_enclosure.py`, `tests/test_tail_split_enclosure.py` (9 assertions); exact residue split + telescoping; independent 4000-cell direct-sum check. |

| MS-01 | For integer `s≥2` the bounded functional `L_s` gives `‖e‖ ≥ |L_s(e)|/‖L_s‖` with `L_s(1)=1/s`, `L_s(r_n)=(ζ(s)/s)(1/n−n^{−s})`, `‖L_s‖²` a rational series. Unconditional, zero-independent, analytic — complements the conditional ZCR-03 and the combinatorial PTE-01/TS-01. | PROVED LOCAL | `observational_succ/mellin_lower_bound.py`, `tests/test_mellin_lower_bound.py` (6 assertions); rigorous rational interval enclosures of `ζ(s)` and `‖L_s‖²`; valid lower bound on `√(1−ln2)` case. |

# Front A countermodels and controls (with receipts)

Each entry rules out only the hypothesis set it names. **None of them is the zero-seed orbit, and none shows that π is nonnormal.**

## Countermodels

| # | Countermodel | What it kills | Receipt | Status |
|---|---|---|---|---|
| CM-A1 | Phase-locked calibrated i.i.d.-digit seed under the same forcing (front B CB-3; rederived independently here) | FL (every constant `C`) and FL-q: `𝒥_A→0` while `limsup Q_{1/2}(μ_A)>0`. Hence any forcing-uniform carry→Clausen transfer is impossible. | Front B CB-3 Lemmas 3.1–3.5, audited in PROOFS §A2: constant ≤2.134; second IFT direction `w=e_1-e_2` with `γ_w>=0.366` | PROVED (paper); not built numerically |
| CM-A2 | Stochastically smaller i.i.d. digits with `p_0=1/16` (e.g. `u+ε(e_1-e_15)`), taken at a generic seed | FL-1: one-sided carries plus frequency existence do not imply Haar. Every 16-shell carries ≥ its Lebesgue mass. | Coupling proof (FA-4). Exact check `F_p(j/256)>=j/256` (min 0). `\|ν^(1)\|=0.01188` | PROVED; exact finite check |
| CM-A3 | Single-lattice calibrated i.i.d. digits (paper only) | Lattice-only carry gates under stationarity: silence on `c_*16^Z` with `ν≠Haar` | FA-11(d) (IFT). FA-11(c): the zero set of `J_∞(·,1)` has empty interior for every non-uniform `p` | PROVED (paper); numerical build is assigned to another agent |
| CM-A4 | Coherent seed `s*=-π/16` | Any Clausen or carry statement that ignores the seed: `Q→log2`, and `J=-avg δ≈-c(1-16^-k)/2` | FA-6 enclosures; exact rational `J` | PROVED + OBSERVED |
| CM-A5 | Periodic completions `k/(16^p-1)` near `π/16` | Statements based only on forcing plus nearness of the seed: `Q→Q(ν_α)>0` by the closed form | FA-7, 20 enclosures inside the proved band | PROVED + OBSERVED |
| CM-A6 | Dyadic-only epochs | "liminf over `A=2^j` suffices" in FA-2: the final partial block is uncontrolled | Logical (PROOFS FA-2 proof) | PROVED (gap, if the subsequence is used) |

## Controls (not countermodels)

| # | Control | What it shows | Receipt |
|---|---|---|---|
| C1 | Rational seed `1/5` | A rotation: `\|c_A\|`, `Q` and `J` statistics are identical. Not a nonnormal contrast. | Exact orbit identity for `n<=2112`; identical enclosures |
| C2 | Numerator mutant `4→3` | Fixed-h Clausen values sit in the same Haar-iid band, so the instrument is not source-selective | FA-9 |

## Not achieved

- No invariant family was found with `Q_{1/2}/sup|J_∞|→∞`. The linear-rate question (FL quantitative) is OPEN, neither refuted nor proved.

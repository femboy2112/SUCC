# Front A — next falsification opportunities

**Where things stand.**
- #520's finite-cut Clausen inequality is the fixed-h Weyl gate, written up to an explicit `O(1/A)` (FA-1/FA-2).
- The carry family `J` is a complete gate only together with log-scale stationarity (FA-5, front B CB-2′/CB-4). Without stationarity, same-forcing seeds silence every carry while staying nonnormal (CB-3).
- So the debt has been moved, not paid.

## 1. One seed-selective target (smallest unpaid piece)

**(LS-lite).** For the zero seed, prove that the kernel distance `D(μ_{[aA,bA)}, μ_{[A,2A)})` tends to 0 for `1<=a<b<=8`.
- This is weaker than frequency existence.
- By FA-5 it reduces normality to the carry gate.
- It is still OPEN, and no mechanism for it is known.
- **Falsifier.** It is **not** implied by forcing alone: CB-3 seeds violate it. Any proof must use exact zero-seed rationality or another seed-selective input. Check every proposal against CB-3 first.

## 2. Quantitative transfer (FL-quant, OPEN)

- **Question.** Among ×16-invariant `ν`, is `Q_{1/2}(ν)<=C·sup_{c<=c_*}|Ψ_ν(c)-Ψ_ν(c/16)|`?
- **Hostile test.** Look for families of i.i.d. or Markov digit measures whose carry functional degenerates faster than the Clausen energy. Use FA-11(c): Bernoulli zero sets are nowhere dense, so `sup_c|J_∞|>0`.
- **Constraint.** Do not build the lattice-calibrated Bernoulli numerically here; that belongs to the sibling agent.

## 3. Fresh finite holdouts (OBSERVED only)

- **Epochs.** Preregister new epochs, e.g. `A∈{1500,2048}`.
- **Repeat.** Rerun the `A·Q_{1/2}` and `sqrt(A)|J|` anomaly falsifiers (`>6` and `>4`).
- **Interpretation.** A pass changes no status. A fail would be a reportable anomaly, not a disproof.

## Not to do

- Do not claim `liminf_A Q_{1/2}(μ_A)=0` as easier "progress". It already implies that every hex word occurs in π infinitely often, which is open.
- Do not iterate RENORM-1 hoping for monotone energy. It only gives `Q_r>=Q_{r^16}/16-O(1/A)`.

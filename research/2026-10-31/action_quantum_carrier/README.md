# Operation ACTION QUANTUM — A source-typed primitive-SUCC phase carrier

**Status:** Research-only child of SUCC PR #440 on exact parent commit `7833a238012bb8e70ff363a3bcf6d60354ecb795`; integrated Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`. All files additive. No change to original four BBP poles, `U_0=0`, canonical proof contracts, production, or Lean. π normality, RH, physical quantization and physical GR/SR are **OPEN / NOT CLAIMED**.

## Why this package exists

Hypothesis: within an observable carrier, one primitive SUCC translation gives a minimum *relative phase resolution* analogous to an effective hbar; refinement adds finer SUCCs. An energy/momentum-style covariance should mediate translation/dilation frames instead of declaring them to commute.

**Mathematical repair:** the general carrier invariant is the exact Weyl bicharacter `omega(a,chi)=chi(a)`; the finite cyclic radix-16 special case has a phase mesh `2pi/16^r` that refines by 16. No universal scalar hbar exists for all finite carriers (quadratic Pisot four-state noncyclic counterexample). The correct position/momentum covariance is reciprocal symplectic scaling `(x,p)->(mx,p/m)`, not a consequence of SR's energy-momentum equation.

## Delivered results

- Finite, exact 16-branch isometries `J_(r,a)|x>=|16x+a>` with a complete carry seam and exact clock/shift phase transport.
- Original **signed four-pole** BBP rational forcing and zero state represented in these 2-adic clocks with **explicit source-authenticated** digit + carry at every tested level and an all-level paper proof.
- Source map firewall: no finite (or continuous 2-adic) clock-only representation can reconstruct `exp(2pi i x)` on odd-denominator rationals. Exact witness `0` vs `16^r/3` has equal local residue and real phase chord `sqrt(3)`.
- Finite support uncertainty `|supp f| |supp fhat| >= |A|`: rigorously carrier-relative, no physical minimum-length assertion.
- Exact coarse-stride kinetic (and polynomial dispersion) intertwining across each branch, plus a **negative** result for naive native fine-step operators.
- **Original BBP canonical action:** exact real phase-plane map `(x,p)->(16x+r(n+1),p/16)` preserves the symplectic form and gives `A_n=x_n p_n=Σ_(j<=n)16^(-j)r(j)->π/16` for the literal zero seed. The source cocycle and seed boundary are both explicit. This is a mathematical action pairing, not physical quantum action.
- Actual Pisot arithmetic: `beta=2+sqrt2` has two first-level digits; `beta² L=2L`, so the second level is `(Z/2)^2` of order four, possessing no primitive 4th-root Weyl phase. This demands a full colored-character pairing.

## Start here

- [PROOFS.md](PROOFS.md): all statements, derivations and countermodels.
- [CLAIMS.md](CLAIMS.md): typed local claim ledger and evidence grade.
- [SOURCE_MAP.md](SOURCE_MAP.md): exact maps, what is forgotten and which phase does not descend.
- [NEXT.md](NEXT.md): signed-π attack with calibrated controls; no placebo structural promotions.
- [VALIDATION.md](VALIDATION.md): commands and exact finite receipts.
- [FINITE_RECEIPT.json](FINITE_RECEIPT.json): small machine-checkable exact source digits, action prefixes, phase meshes and Pisot/no-factor witnesses.
- [action_quantum.py](action_quantum.py): rational/source, group branch, Pisot, symplectic and finite kinetic exact library.
- [independent_oracle.py](independent_oracle.py): alternative exact source and graph/field calculations.
- `tests/test_action_quantum_carrier.py`: 35 root-discoverable exact tests with exhaustive small carriers.

No new probability of truth, quantum system, speedup or sourced π normality theorem is implied.

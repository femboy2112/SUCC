# BBP form choice, prime-local causal transport, and signed Gaussian compensation

**20 November 2026 · additive, research-only stacked draft.** Parent: [Gaussian Causal Yoneda PR #672](https://github.com/femboy2112/SUCC/pull/672), head `833afa532c61cf30c64c11a5a72490e823c91095`; original Main XXVI `81be6b897ae980b801a3b9de9e22ef81e8360bfb`. This work does not alter BBP forcing, `U_0=0`, the archived source, imports, production code, or any other agent's branches. **R0, base-16 pi normality, RH, and physical source-back-action remain open.**

## The proposed interpretation, faithfully separated into testable claims

An embedded observer chooses a mathematical form, such as BBP's radix-16 and signed rational poles. A physical implementation of that choice may perform work, measure the source through a particular algebra, and create new interactions if it controls an intervenable source. The mathematical *form* can generate additional positive **observer-defect energy** under noncommuting observation/advance operations, yet a correctly compensated description of the *same completed phase* has source-independent invariants. A representation need not physically inject energy into the mathematical number it represents.

The sharper possibility: original BBP prime-power events, measured in their own `p`-adic arithmetic, carry source-specific information that a leading Gaussian energy shadow omits. Their **signed, ordered coupling with the complete real cofactor and zero-seed anchor** might supply an R0 certificate. A genuine uniform cofactor nontracking bound has not been proved.

## Results

| Label | Theorem / obstruction | Precise conclusion |
| --- | --- | --- |
| ACT-01 | Arithmetic places versus expansion | `|16|_infinity=16`, `|16|_2=1/16`, odd places unit; rational product formula exact, no thermodynamic interpretation |
| ACT-02 | Original pole-square local/real contrast | at `n=(p²+7)/8`, `v_p(r(n))=-2`, `p²r(n)=4 (mod p)` but `p⁴r(n)->15`; matched-jet mutant residue 5, same real leading jet |
| ACT-03 | Gaussian form-order defect | Positive, phase-independent `L²` defect from smoothing before versus after radix advance; disappears under exact `lambda -> 256 lambda` transport |
| ACT-04 | Finite BBP source/boundary square | All finite-terminal compensation identities exact in `Q`; counterseed `-P_M` makes the **entire finite terminal** perfectly locked with unchanged forcing |
| ACT-05 | Indispensable signed Gaussian interference | Completed displacement = source energy + boundary energy + signed cross term; for locked terminal cross cancels all positive components exactly |
| ACT-06 | CRT prime-primary factorization | Every `q in Q/Z` decomposes exactly into canonically labelled p-primary fractions; complex characters multiply, not their positive energies |
| ACT-07 | Cofactor tracking is R0, not a proof | For any selected prime set, the signed inverse-tracking gap is exactly the original phase displacement; arbitrary prime refactorization changes the ledger, not its invariant sum |
| ACT-08 | Prime-square pulse sparsity obstruction | Bounded witnesses supported for `O(log B)` ticks after pole-square events have `o(1)` shell means; positive R0 density needs wider nonlocal effects or a different source channel |
| ACT-09 | Feedback requires action | A model-dependent carrier change needs a responsive causal instrument/intervention; Gaussian norm discrepancy alone does not imply physical energy transfer |
| ACT-10 | Matched-jet mutation | `Q* = Q+(1-t)^2` preserves `Q(1),Q'(1)`, leading real source energy, but changes p-square residue and the inherited auxiliary source filter |
| ACT-11 | Remaining signed witness obligation | The source-authenticated all-shell prime/cofactor correlation lower bound is **UNVERIFIED**; its already established conditional implication to R0 is retained from #672 |

**Strongest new cross-view insight:** for prime-square clocks, the original forcing has a spectacular `p`-adic valuation but a *much smaller* real amplitude due to the four-pole cancellation; a matched-jet mutant has essentially the same real Gaussian energy and a different exact prime-local residue. That is a concrete instance in which distinct observers require distinct source labels to recover the arithmetic process. However those prime-square clocks are sparse: detecting their short-lived local energy cannot by itself prove anti-locking on every late shell.

## Exact source contract

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
Let `x=pi/16`, `P_M=sum_{j=1}^M 16^-j r(j)`, and `T_n=sum_{j>=1}16^-j r(n+j)`; the original completed orbit is `Y_n=U_n+T_n=16^n x`. At finite terminal `M`, the *exact rational* compensator is `T_n^[M]=sum_{j=n+1}^M 16^(n-j)r(j)`. Never substitute an ensemble, changed forcing, co-moving complex mask, or an unanchored seed as the authentic orbit.

## Fast entrypoints

- [THEOREMS.md](THEOREMS.md) — complete definitions, proofs, no-go receipts, domain boundaries.
- [NEXT.md](NEXT.md) — preregistered signed cofactor assault and expected falsifiers.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md) — separated claims and statuses.
- [PROVENANCE.md](PROVENANCE.md) — exact dependencies, ancestral provenance and non-independence.
- [adic_transduction.py](adic_transduction.py) — pure stdlib exact rational instruments and declared Gaussian observables.
- [test_adic_transduction.py](test_adic_transduction.py) — positive, negative, null, mutation, and moving-frame controls.
- [independent_sympy_audit.py](independent_sympy_audit.py) — independently constructed symbolic source and source-mutation calculations.
- [VALIDATION.md](VALIDATION.md) — actual execution receipts and what was not run.

To reproduce from this directory:

```sh
python -m unittest -v test_adic_transduction
python independent_sympy_audit.py   # Requires SymPy; not required by production SUCC
```

No claim of original academic priority. Classical ingredients (CRT, product formula, Fourier/Parseval, Gaussian heat semigroup, causal feedback) are explicitly separated from the new-to-this-dossier BBP assembly and source-valid finite calculations.

# Validation receipt — exact bounded calculations; paper proofs separately scoped

**Parent/source:** exact #460 head b99518cf93048d87c7cfecd43587bf95dc502c87, stacked on #459 and verified Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. Only additive research files under this directory. The original source, selected seed, historical theorem contracts and production remain untouched.

## 1. Executed finite exact checks

Local command before uploading exact byte-matching source:
\[
\texttt{python macrolag\_exact\_probe.py}
\]
**7/7 unittest methods PASS**, no skips, 0.085 seconds observed. The two source implementations (four signed terms vs combined rational polynomial) agree for n=1..179. The probe checks independent source-birth and residue predictions on many original and coherent-shadow time pairs; exact control tests verify U0=0, \(\widetilde r>0\), its explicit changed forcing, and p-adic valuations of both shared and newborn prime families.

A separate broader exact Fraction stress check inspected **193743 original** and **29766 shadow** p-valuation instances over finite small/mid-range time pairs; zero mismatches. These are not independent mathematical proofs, and the unbounded results use classical PNT-AP.

## 2. Original *real* selected phase interval certificates

The exact oracle is interval.py. Its **uploaded Git blob is identical to the locally tested byte content** (after a path-only portability change and a post-change p4013 replay). Source Git blobs independently verified by fetching them back:
- macrolag_exact_probe.py: c3e32519d373a2bd60f2e1180a07fbf5fb7680fe
- interval.py: 8f5133b735b60668f2a0e6365fa5ad0ef43c91f7
- independent_float_oracle.py: 4223f08c8dcc95109b9ca7a65c45c17970ba73b7

A Machin rational interval encloses pi with no decimal pi digits. Exact U_n mod1 reduction precedes 2^19-mesh phase floor. Exact rational degree-20 Taylor evaluation and the global per-component error bound
\[
\epsilon=10^{-9}+(22/7)^{21}/21!+(44/7)2^{-19}+(\pi_{\rm high}-\pi_{\rm low})
\]
give the outward L1 normalized bound
\[
\frac1L\left|\sum e(hU_n)\right|
\le\frac{|R_{\rm integer}|+|I_{\rm integer}|}{10^9L}+2\epsilon,
\]
then round *up* to the next 10^-9. Here the real/imag integer sums are integer truncations of **rational** polynomials, not approximate sines from a floating library.

Predeclared batch p=4013,4021,4093 and h=1,3,5,7: all **12/12** certified \(\ell_1<1/8\).
Stricter predeclared batch p=10037,10061,10069 and h=1,3,5,7: all **12/12** certified \(\ell_1<1/16\).
Every result and its exact outward numerator is in FINITE_WINDOWS.json. The largest of the 24 is 0.042229173 (p=4021,h=5), so the first batch satisfies 1/16 too **only as a post hoc stronger observation**.

For all these cases the coherent positive changed-source control has \(|\widetilde W_p(h)|/L>0.999997\) from the exact all-p inequality, not a float extrapolation. The same-four-pole changed irrational counterseed is likewise coherent.

**Failed-attempt provenance:** The initial combined >10000 interval run was killed after completing p10037; all three selected p cases were then rerun individually and passed. The mathematical oracle was unchanged during those 3 runs. The subsequent portability-only output-path update changed no calculations; a p4013 local replay confirmed the same rounded bounds. The preselection and experiments came from one model session, not blind external witnesses.

## 3. Float-only second source family

Run:
\[
\texttt{python independent\_float\_oracle.py}
\]
This separately constructs U_n from the **literal four signed fractions**, then evaluates trig with standard double precision. All 24 numerically reported complex moduli lie below their rigorous L1 upper bounds. This is a cross-implementation sanity check only. It is not an independently calibrated error interval or external referee.

## 4. Reproduction

From the repository root:
~~~sh
python research/2026-11-02/macrolag_prime_witness/macrolag_exact_probe.py
python research/2026-11-02/macrolag_prime_witness/independent_float_oracle.py
# Full 4000-range rational interval batch (writes local FINITE_WINDOWS_RAW_4000.json)
python research/2026-11-02/macrolag_prime_witness/interval.py
# To check individual >10000 preregistered cases:
PYTHONPATH=research/2026-11-02/macrolag_prime_witness python -c "from interval import produce; from fractions import Fraction; print(produce(10037,(1,3,5,7),Fraction(1,16)))"
# Repeat previous command with p=10061 and p=10069.
~~~
Large exact upper fractions printed by produce can be outward-ceiled to a 10^9 denominator and compared to FINITE_WINDOWS.json. No code performs a covert pi-digit lookup.

## 5. Not run; cannot claim

The complete native SUCC >11k suite, root AGENTS.md provenance/foundations/ordinal probes, hosted exact-head GitHub Actions CI, new Lean theorem certification, independent blind referee and all-scale signed Weyl saving are **NOT RUN / NOT ESTABLISHED** here. The local environment cannot directly clone GitHub due DNS. The paper derivations rely on PNT-AP, and finite script checks do not promote those proofs to formal or independently peer-reviewed authority.

# ST — authentic signed Weil H¹ zero-side tail (scope-controlled claims)

Source ancestor: draft PR #82, exact SHA `bb5b6f96f78df0d9472a60441501024e0e2b904e`; its original-theta contour is already completed and receipt-pinned. Original Weil equality is a **CLASSICAL IMPORT**, not a theorem manufactured by arithmetic simulations. Details: [dossier](../research/2026-10-14/SIGNED_WEIL_H1_SPECTRAL_TAIL.md). **RH PROVED: NO.** Academic priority and Lean proof are not claimed.

| ID | Exact claim, limitation | Status |
|---|---|---|
| ST-01 | Authentic theta continuation yields `|F(z)|<=3(1+|z|)^(|z|/2+2)` for `|z|>=1`. Jensen + `F(0)>59/120` yield all-zero count `N_abs(T)<7T log(4T)` for `T>=2`, multiplicity and off-line zeros included. | PROVED LOCAL (classical Jensen) |
| ST-02 | Dyadic source zero count bounds `sum_(|gamma|>T)1/gamma² <=28 log(16T)/T` without enumerating or locating zeros. | PROVED LOCAL |
| ST-03 | Authentic signed Weil spectral remainder satisfies `|Q_>T(v,w)| <=70 a e^a log(16T)/T ||v||H¹ ||w||H¹` for all `v,w∈H₀¹(-a,a)`, `T>=2`, no RH. Finite zero-side truncations converge in form/operator norm H¹→H^-1. Does NOT mean Suzuki's unbounded L² operator truncations converge in operator norm. | PROVED LOCAL (classical Weil source identity) |
| ST-04 | Source-hash-verified simple critical first pair is a genuine rank≤2 positive component; unknown other low zeros remain SIGNED, high remainder bounded by ST-03. | PROVED LOCAL / source receipt imported |
| ST-05 | A bounded-H¹ concentrated triangle has no sixth classical derivative but is covered by ST-03: smooth C⁷ technique's scope failure does not prove no H¹-tail theorem. | PROVED exact H¹ geometry / negative control |
| ST-06 | Toy signed finite Hilbert forms with same positive first coordinate and zero high tail have opposite global signs. Not arithmetic zeta or proof of an off-critical true zero. | PROVED finite countermodel |
| ST-07 | All-height positivity of every source-certified finite spectral truncation, or a corresponding all-test sign source inequality, is not shown. | UNVERIFIED / RH-hard |

| ST-08 | Completed-Weil PR #71 signed Gamma approximation CW-11 and ST-03 signed spectral tail imply two-chart operator/form bound `||Q̃_J^arith-Q_≤T^spec||H¹→H^-1 ≤ ε_J+70ae^a log(16T)/T`, `ε_J=max(9/(8A²)+1/(2A³),1/(2A²)+2/A³)`, A=2J+1/2. Both charts retain the original source; the spectral low chart is not algorithmically populated without independent contour certificates. | PROVED LOCAL via classical triangle inequality / imported authentic PR #71 CW-11; zero-sign UNVERIFIED |
**No imported zero coordinates:** The theta contour produces a known first pair by a source-certified computation, not by supplying a zeta-zero list. The independent signed tail construction uses none. Every original prime-power, Gamma/contact, pole and half-density term is retained in the **pre-existing** Weil distribution. Zero-side continuation uses the external classical equality, not generic covariance.

**Reproduce:** `python -m unittest discover -s tests -p 'test_signed_weil_h1_tail.py' -v` and `python scripts/signed_weil_h1_tail_probe.py --verify research/2026-10-14/SIGNED_WEIL_H1_TAIL_RECEIPT.json`; optional independent numerical diagnostic only. `main` remains unchanged.

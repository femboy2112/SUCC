# Borwein Quantitative Kernel Bridge — exact execution receipt and falsification ledger

**2026-11-17.** Research-only, stacked on draft SUCC PR #657. No source/history/main mutation, merge, release or claim to have proved π normality.

## Source / worktree receipt

- Inherited committed original-source Borwein theorem: [BORWEIN_SWEPT_IMPULSE_BBP.md](BORWEIN_SWEPT_IMPULSE_BBP.md) on research branch research/defect-window-tomography-2026-11-16 at base commit 7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf.
- New isolated implementation: [observational_succ/borwein_quantitative_certificate.py](../../../observational_succ/borwein_quantitative_certificate.py), 6,228 exact tested bytes; Git blob SHA **21168fe02d90365ff537ece2af6c302240bd772d**, SHA-256 **14a8fef9c885d934a2cfb13a6690a8c7e0897bf9174a617db172ffc0d170e28a**.
- New isolated tests: [tests/test_borwein_quantitative_certificate.py](../../../tests/test_borwein_quantitative_certificate.py), Git blob SHA **93f8eff792c53d6e7af11592bfc564a89f52909c**, SHA-256 **58e3b421270a096e0b0e9e57f9d1a5adf0351a6f6b6fb54d7d3fc0935a899c28**.
- The exact remote Git blob SHAs were checked against locally executed copies after fixing an initially incorrect test import and replacing an inert tuple-return with an **actual rational upper-bound function**. No unexecuted source revision was counted as passing.

## Focused exact tests

Executed with PYTHONPATH pointing at the model's test workspace:

~~~sh
python -m unittest discover -s /mnt/data -p 'test_borwein*.py' -q
~~~

**24 tests passed, zero failures/errors**: 15 in the new quantitative module and 9 in the previously committed two-pulse Borwein focused suite. This is **not** the full repository-wide unittest/AGENTS gate.

Controls include:
1. Literal authenticated signed four-pole BBP forcing, zero seed, exact Fraction recurrence and terminal endpoint source.
2. Symbolic exact one-atom \(\mathcal V=335872/304434045\), source-independent translation invariance, zero-phase and nonunit fixed-phase locked adversaries.
3. Two **different implementations** of the exact rational \(\mathcal V\): piecewise quadratic integral versus pairwise rational autocorrelation K evaluated at differences of source phases; equality at several synthetic and original-source shells.
4. A separate 3,000-point Riemann quadrature diagnostic agrees with the exact polynomial integral within \(10^{-6}\) for selected independent phase configurations. This check is numerical, not the proof.
5. An independent direct trigonometric evaluation at harmonics h=1,...,127 confirms the **paper-proved** rational Fourier floor \(2205/(139876h^2)\).
6. Source-rational explicit interval-discrepancy and Weyl-bound functions reject false square-root certificates; the exact full-interval discrepancy implementation correctly handles duplicates (16 identical phases: discrepancy 1). An earlier inadequate endpoint-scan diagnostic was replaced *before* reporting tests.
7. Original source future-tail-certified digit-word extraction: for B=32,64,128, and every tested k=1,2,3,4, all B clocks have **zero boundary ambiguities** under the exact source tail. The test verifies full counts, not their expected limiting frequency.
8. A stopped/locked orbit keeps \(\mathcal V_B=335872/304434045\) for all B, whereas finite equally spaced rational grids have strictly smaller energy and approach the Haar state as they refine.

## Finite source-rational energy samples

Every entry is computed from the **literal original** rational U_(2B), and is thus an exact rational value; decimal views are not used for proof.

| Shell B | Exact rational \(\mathcal V_B\), decimal display | \(\sqrt{\mathcal V_B}\), decimal display | Exact source-torus interval discrepancy of rational shadow |
|---:|---:|---:|---:|
| 4 | 0.00018379480029718 | 0.013557094095 | 0.5078158963 |
| 8 | 0.00010024353552966 | 0.010012169372 | 0.3851655573 |
| 16 | 0.00013394290597516 | 0.011573370554 | 0.3703075423 |
| 32 | 0.00000989211400697 | 0.003145173128 | 0.1707468438 |
| 64 | 0.00000547677362073 | 0.002340250760 | 0.1072147263 |

The \(\mathcal V_B\) sequence is **not monotone even on these samples** (B=16 > B=8). No \(\mathcal V_B\to0\) or source-implied spectral estimate is inferred.

## Mathematical proof chain (not a finite-run extrapolation)

- **Exact rational quadrature:** finite swept kernel is piecewise quadratic with rational source breakpoints; integrate its square piecewise, giving Fraction \(\mathcal V_B\in\mathbb Q\).
- **Signed-energy identity:** Parseval gives \(\mathcal V_B=\sum_{h\ne0}|\widehat L(h)|^2|\widehat \mu_B(h)|^2\). The weights are strictly positive by the prior all-harmonic two-pulse theorem.
- **Explicit Fourier lower bound:** reverse triangle inequality plus \(3<\pi<22/7\) yields \(|\widehat L(h)|>2205/(139876 h^2)\) for every h≠0, not merely the tested 127 modes.
- **Exact source tail:** inherited BBP identity gives \(\sup_\alpha|J_B-\widehat J_B|<\epsilon_B=16r(2B+1)/(7225B)\), and the L2 reverse triangle inequality gives \(|\sqrt{V_B^{true}}-\sqrt{\mathcal V_B}|\le\epsilon_B\).
- **Explicit interval-digit bound:** for any integer H≥1, the Erdős–Turán inequality \(D_B\le3/(H+1)+3\sum_{h=1}^H|W_B(h)|/h\) and the source spectral bound give \(D_B\le3/(H+1)+(69938/735)H(H+1)(\sqrt{\mathcal V_B}+\epsilon_B)\).
- **Normality equivalence:** \(\mathcal V_B\to0\) iff every nonzero radix Weyl mode tends to zero, hence (by Weyl's criterion) iff \(\pi\) is base-16 normal. **An equivalence is not its desired asymptotic conclusion.**

## Red flags and next independently falsifiable advance

- The general Erdős–Turán bound can exceed 1 at the measured small B; do **not** claim the new finite digit-discrepancy bound is presently competitive with direct counts. Its significance is the valid universal, calculable implication from future source estimates.
- An arbitrary finite digit cylinder can have normal and nonnormal completions. Nothing in 24 passing local tests converts finite observations to a universal theorem.
- A *changed* source with a zero numerical seed can be perfectly locked; the original complete four-pole passport is essential.
- The input rectangles/Dirac impulses are observer kernels, not independent stochastic data injected into the BBP source.
- The exact \(\mathcal V_B\) functional is a positive characteristic-kernel metric; its asymptotic decay for the original arithmetic source is **UNVERIFIED**.
- A collaborator proving \(\mathcal V_B\to0\) with an authentic signed carry/cofactor/Gamma argument and surviving locked-source controls would close the base-16 normality objective. Merely defining \(\mathcal V_B\) does not.

**Not run:** full repository unittest suite, provenance/observer/ordinal gates, Lean, full hosted CI for this head, blind referee check. **Status of R0, full base-16 π normality, RH: OPEN.**

**External theorem context:** [Bailey–Crandall, On the Random Character of Fundamental Constant Expansions](https://doi.org/10.1080/10586458.2001.10504441); [Erdős–Turán with explicit constants](https://androma.org/theorems/9093); [prior signed Borwein kernel](BORWEIN_SWEPT_IMPULSE_BBP.md). These do not supply the new original-source all-shell bound.

# Exact SUCC History Ledger: source, realized branch, predictive ensemble

This is the reproducible bookkeeping contract for PR #521's history-first child. It is a mathematical epistemic instrument, not a probability that π is normal or a physical quantum field.

## 1. What constitutes authenticated evidence

The objective **relative to this mathematical model** is the literal original four-pole signed rational history
\[
r_o(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_{n+1}=16U_n+r_o(n+1).
\]
For each n retain the exact Fraction value U_n, the independently computed collapsed rational source formula, the fractional state x_n={U_n}, and literal carry c_(n+1)=floor(16x_n+r_o(n+1)). Never reconstruct the source from fitted π digits. The finite chronological records H_(N+1) restrict to H_N by forgetting the last step.

## 2. Source-labelled m-digit observation after k future steps

For m,k≥1, compute from the exact history
\[
S_k(n)=\sum_{j=1}^k16^{k-j}r_o(n+j),\
a=\lfloor16^{m+k}x_n\rfloor,\
\theta=\{16^{m+k}x_n\},\
q+\delta=16^m S_k(n)
\]
with q integer, 0≤δ<1. The realized branch and output cell are
\[
b=\mathbf1_{\theta+\delta\ge1},\qquad
w=(a+q+b)\bmod16^m.
\]
**All these are exact arithmetic records.** For every row, independently confirm w=floor(16^m{U_(n+k)}), the exact recurrence and the source/carry contract.

The two possible model-predicted cells are (a+q) and (a+q+1) modulo16^m. Only after explicitly assuming a *uniform unknown remainder* θ do they receive probabilities 1−δ and δ. They are not probabilities of the actual already realized branch.

## 3. Epistemic forecasts use the real conditional state

A probability ensemble is extra data representing incomplete observations or competing source hypotheses. Push its complete conditional remainder distribution through the true source map; condition on actual observations; do NOT independently re-uniformize the current cell after each step. The exact toy model's total variation error 1/2, and the original-source finite error about 0.216168, falsify the re-uniformization shortcut.

For a finite observed epoch, the innovation of the declared model is
\[
J_(A,m,k)=A^{-1}\sum_{A\le n<2A}(b_(n,m,k)-\delta_(n,m,k)).
\]
This is a deterministic diagnostic, not a proof of convergence to zero or a sequence of statistically independent trials. A complete exact source+seed history has a point-mass posterior; any nontrivial ensemble must state its deliberate ignorance.

## 4. Observation-selection experiment, run under preregistration

[DECISION_PROTOCOL.md](DECISION_PROTOCOL.md) defines a source-only expected binary-entropy score and selects (m,k) before the selected original branch is examined.

| Epoch A | Chosen m,k | Realized branch count | Sum of forecast probabilities |
|---:|---|---:|---:|
| 211 | 2,3 | 39 | 38.8326342 |
| 419 | 2,3 | 15 | 19.5509667 |
| 829 | 3,3 | 153 | 158.0880546 |

At all three epochs the same-original-forcing coherent but nonnormal seed received a *smaller* finite Brier score than the true zero seed. Optimizing subjective predictive fit does not authenticate source selection or certify normality.

For future tests, preregister new source times, candidate observer depths and source mutants, predicted differences and the intended verdict before reading their selected history. Preserve raw and source-adjusted views separately. The [finite receipt](FINITE_RECEIPT.json) is for reproducibility and provenance.

## 5. The unpaid theorem

The exact source history is a sufficient statistic for its own deterministic recurrence, but this is NOT a theorem about its infinite-time empirical distribution. A verdict-changing new result must prove an original zero-seeded signed or unsigned bound such as the fixed-radius Clausen condition Q_(1/2)(mu_A)→0, uniformly bounded all-depth cell pressure, or fixed-h Weyl decay, with full quantifiers and adversarial coherent/periodic controls. A strong forecast with no such arithmetic inequality is a useful engineering observation, not a normality proof.

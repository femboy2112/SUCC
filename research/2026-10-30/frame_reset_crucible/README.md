# SUCC — Frame-Reset Crucible: normal hexadecimal paths and observer choice

**Date:** 2026-10-30. **Status:** draft, independent research-only branch based on `main@e18ba565ca540adb7edf3292f5593929e76d91c5`. This is a calibration of the Main XVI operational triangle and the unmerged spacetime/dual-triangle research #390–#393; those drafts are read-only references, not silently integrated. Main, the original BBP four signed poles, `U_0=0`, original archives, historical claims, production code, and workflow configuration are unchanged.

## Why this control is different

Calibrate the same selection / observed-endpoint / `T(x)={16x}` frame reset on **both** demonstrably normal and demonstrably nonnormal deterministic base-16 systems:

- **Normal arithmetic controls:** `alpha_(16,3)=sum_(k>=1) 1/(3^k 16^(3^k))` and `alpha_(16,5)` are Stoneham constants, known base-16 normal by Bailey–Crandall 2002. We give a self-contained finite-stage **bounded-hot-spot** proof specialized to their original source. Their rational source stages have exactly six and twenty traversals of explicitly specified residue classes, respectively.
- **Nonnormal same-grammar control:** `alpha_(16,2)` has exactly one nonzero hexadecimal digit at position `2^k+ceil(k/4)` for every k, with value `2^(4ceil(k/4)-k)`; its nonzero-digit frequency is zero.
- **Normal but computable control:** the base-16 Champernowne concatenation; an observer using its known digit algorithm can selectively inspect only zero positions.
- **Locally perfect but nonnormal:** an exactly uniform two-digit de Bruijn cycle repeated forever; all one-digit conditional next-symbol counts are perfectly fair but most three-digit words never occur.
- **Biased reset fixed point:** any full-support i.i.d. digit law is unchanged by conditioning on a word then recentering; Haar is not selected by mere reset invariance.
- **Original π frontier:** `z_n={U_n(0)}` is an exact rational carrier with `U_n=16U_(n-1)+r(n)`, `r(n)=R(8n-7)` and the known source-tail bound. No corresponding **uniform conductor-coverage certificate** has been proved for those rational phases.

## What the genuine arithmetic certificate is

For every circular interval I, integer N>c and c in {3,5}, let `A_N^c(I)` count visits of the **true** pure orbit `{16^n alpha_(16,c)}`, 0<=n<N. Then

```
A_N^c(I) <= c*N*|I| + 3*c*(c-1)*floor(log_c(N-1)) + c.
```

The proof bounds the genuine orbit against exact source rational surrogates, with no fitted numerical π-like digit frequencies. Every weak empirical limit is T-invariant and dominated by c times Haar; the Fourier Riemann–Lebesgue lemma forces the limit to be Haar. This reproduces a known normality theorem with a source-specific quantitative construction. See [RESEARCH.md](RESEARCH.md).

**The missing π bridge is now typed:** construct a similarly uniform *source-authenticated arithmetic coverage certificate* for the rational BBP carrier `U_n(0)`; a positive posterior, golden/Gamma mark, exact phase reconstruction, and one-step reset cannot substitute for this. This is a sufficient target, **not a known necessary mechanism**.

## Explicit human T-action / choice object

`T(x)={16x}` is the arithmetic shift. The observer can choose a measurable cylinder/partition and recenter after observing a word w via

```
R_w(mu) = (T^|w|)_*( mu restricted to C_w / mu(C_w) ).
```

The arithmetic digit is determined by the actual number; an observer's **choice of instrument** and the **conditional update of the observer's law** are separate operations. For Haar, `R_w(Haar)=Haar` for each fixed w; for normal deterministic sequences this holds for *fixed-word empirical conditionals in the limit*, not at every finite time or under every adaptive policy. For a full-support biased i.i.d. measure, every reset holds too, without normality. We classify those fixed points in RESEARCH.md.

## Run locally

```bash
cd research/2026-10-30/frame_reset_crucible
python -m unittest -v test_frame_reset.py
python independent_oracle.py
python -m compileall -q frame_reset.py test_frame_reset.py independent_oracle.py
```

The exact local test/oracle receipts are in [VALIDATION.md](VALIDATION.md). **Do not infer π normality or RH.** The locally proved source criterion is intended as a falsifiable template for the next SUCC round, not an assertion that BBP already satisfies it.

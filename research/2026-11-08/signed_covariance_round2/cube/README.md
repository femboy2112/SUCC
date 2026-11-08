# Cube front: an exact depth boundary and a wider Fourier budget

The new [paper proofs](THEOREMS.md) give the exact local-source identity

`||a||_(U^d)^(2^d)=D_(m,d-1)+mean_(nondegenerate preceding shifts)|S(c)|^2`,

where the mean retains normalization m^(-(d-1)). Thus the bound is
`D+(1-D)delta^2`, with D=1-(1-1/m)^(d-1). It is uniform in every nonzero
source coefficient. The selected prime clock's cyclic cube norm tends to zero
**if and only if** 2^d=o(log p). This is an instrument threshold, not a
necessary condition for full real Weyl decay or arbitrary polynomial twists.

At depth two this also proves the fourth-moment bound
`sum |ahat_k|^4 <= V_p=1/m+(1-1/m)delta^2`. The leakage into any s selected
Fourier modes is at most `(s V_p)^(1/4)`. Hence the existing complement-tail
criterion now needs `s*(1/m+delta^2)->0`, in place of
`s*(1/m+delta)->0`, with the **same** approximation residual. This improves
the sufficient support budget; it does not establish that the original
complement has a suitable tail. CQ4 additionally gives a nonlinear cube-atom
predictor certificate, explicitly charging coefficient variation and error.

The coherent complement B=conjugate(a) keeps correlation one while every
proved local cube bound holds. It defeats any inference from local high-order
uniformity alone to the original signed covariance. No original-zero upper
estimate is proved. **Pi base-16 normality: OPEN. RH: OPEN.**

## Executed checks and dependence

The [protocol](PROTOCOL.md) and its fourth-moment supplement were pushed
before their respective checks. [receipt.json](receipt.json) retains all
formal root-of-unity coefficient histograms and exact rational values:

- 66 cube cases, comprising 1,950,022 literal cube instances, agree with an
  independently indexed final-shift square expansion; 11,382 preceding
  shift tuples give the exact degeneration count.
- 18 fourth-moment cases, comprising 46,434 Fourier index triples, agree
  with the depth-two cube histograms. This reuses the same sources through
  a different representation, not a new independent dataset.
- 212 unwrapped-source/authentication checks retain the original four poles.
- 24 exact Gaussian-rational multilinear cases check Gowers--Cauchy--Schwarz
  and the dual-atom convention; 48 Fourier support checks include the sharp
  complete flat-spectrum case.
- Seven focused unit tests pass, including zero frequency, full source
  authentication, bilinear pairing, and wrong-conjugation rejection.
- [PEER_REVIEW.json](PEER_REVIEW.json) pins the scoped paper review of CH1--6
  and H1--6. The separately reproducible peer oracle checks 266 Gram cases,
  64 triangular-weight cases, and 24 chronological word laws. All pass.

The algebra checks do not prove BK/PNT or the classical finite-field imports.
The proof reviews share the same model and baseline; no external scholarly
certification is claimed. No Lean statement was added by this front.

From the repository root, reproduce with standard-library Python:

```sh
python3 -m unittest discover -s research/2026-11-08/signed_covariance_round2/cube -p 'test_*.py'
python3 research/2026-11-08/signed_covariance_round2/cube/cube_oracle.py --output /tmp/succ-cube-replay.json
python3 research/2026-11-08/signed_covariance_round2/cube/peer_review.py --output /tmp/succ-cube-peer-replay.json
```

The parent source is pinned to `1990b05117d84b33094c8e0f53f7d19b60f48060`.
The next discriminating theorem is a source-derived upper bound for the
original complementary Fourier tail, or for the signed residual when this
stronger prediction condition fails.

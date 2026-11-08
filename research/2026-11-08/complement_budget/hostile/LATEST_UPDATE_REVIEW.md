# Final fetched dependency update: three-channel source Gram

Read-only audit at exact branch tip
`efcb9985d0a240ea6d5c580de97445e57f5d12b7`, branch
`research/four-pole-three-channel-poisson-matrix-2026-11-08`.
Main remains `43a607818907120d4cdab73d240f5b4d7700b63f`.

Inspected the actual `research/2026-11-08/four_pole_three_channel/PROOFS.md`,
its claim ledger and `observational_succ/three_channel_source.py` with
`git show`. No branch content was imported, merged, modified or executed.
This is a proof/dependency relevance audit, not a full code or CI review.

**Verdict: useful source geometry; neither PR8 approximation error nor its
retained resonance is bounded by this update.**

- FP3-01 gives the exact anchored positive decomposition already compatible
  with our forcing bounds. Its source-dependent endpoint jets are15 and-59.
- FP3-02 constructs a genuine full-rank positive source Gram. The displayed
  leading determinant constants check algebraically: the degree1/2/3
  coefficient determinant is-10 and the factorial moment determinant is576,
  giving57600, then115200 after multiplying the component weights. These
  are rank/conditioning facts without the selected BBP phases.
- FP3-03 correctly distinguishes the universal Gamma(2) Poisson minimum1/9
  from the four-pole fingerprint. Its two-pole control prevents identifying
  those quantities merely by counting channels.
- FP3-04 explicitly retains the unresolved signed covariance. Its proposed
  phase-bearing matrix requires normalization and a further arithmetic
  estimate. The implementation's `signed_covariance` takes both actual phase
  histories as inputs; it does not derive the complement from the Gram.

The normalization warning has a direct quantitative check. Since
`0<=1-exp(-d*x)<=d*x`, the weighted Gram has

`trace G_weighted(a) <= 2 sum_d w_d d²/a³ = 118/a³`.

It is positive semidefinite, so its operator norm is at most that trace.
For the proposed matrix
`K_A=mean_n z_n G_weighted(8n-7)`, with **any** unit phases z_n, triangle
inequality gives

`||K_A|| <= 118/(8A-7)^3`.

Thus decay of that unnormalized matrix occurs even for z_n identically1
and for the coherent same-forcing control. This calculation verifies the
branch's stated warning; it does not refute the proposed normalized,
chronology-sensitive research direction. A normalized reconstruction and
an independent source-selected signed bound are still required.

The separately fetched branch
`research/theta-gamma-extruded-triangle-dual-interference-2026-11-08` points
exactly to `43a607818907120d4cdab73d240f5b4d7700b63f`, with no new diff to
main at inspection. No unpublished theorem is inferred from its name.

No change to the current proof chain follows from either fetched update:
original-zero signed covariance decay remains OPEN, and its established
implications lead to Weyl decay and then normality. Pi normality and RH
remain OPEN.

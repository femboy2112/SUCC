# Final-fetch audit: chronological three-channel prime tomography

Read-only remote pin:
`origin/research/prime-three-channel-phase-tomography-2026-11-08`
at **`34403d5c5d0ae9f37cb78e3c9d68c1e55c11a627`**.
The two newest commits are `9440dc724d6ef4ea490e3718fbe338c412b9d5c6`
(implementation) and the pinned head (tests), above the previously inspected
`efcb9985d0a240ea6d5c580de97445e57f5d12b7` three-channel branch.

Inspected actual `observational_succ/three_channel_prime_tomography.py`,
`tests/test_three_channel_prime_tomography.py`, the source decomposition,
and `research/2026-11-08/four_pole_three_channel/{PROOFS,CLAIM_LEDGER,NEXT,README}.md`
at that exact pin. This was a source/proof inspection; **no tests were run**
and no files on that branch were changed. At this pin the new prime module
has docstrings and exact test specifications, but the paper proof and claim
ledger still describe FP3-01–05 rather than a new numbered tomography theorem.
Do not silently treat those older paper proofs as coverage of every new API.

## What the new construction actually retains

It splits the authentic forcing into the three zero-seeded channel orbits
with marks `(d,w)=(3,2),(4,1),(5,1)`. For `p=8k+1` it retains four distinct
p-birth events inside each simple-pole shell. In the first shell their
normalized channel vectors are exactly

```
(2,1,1), (3/2,1,1), (3/2,4/5,1), (3/2,4/5,5/6).
```

Their scalar sums are the earlier four-pulse coefficients
`4,7/2,33/10,47/15`. The event durations are `3k,k,k,3k`, plus the explicitly
retained last endpoint. The code records the complete local character
histogram rather than dropping these chronological labels. The claimed
simple-pole domain `r<k` ends exactly before the first p² birth;
`first+k*p=(p²+7)/8`, so this scope is materially important.

The new normalized local phase Gram has first-shell conditional limit

```
[[1,0,0], [0,1,1/2], [0,1/2,1]],
```

when the subgroup's nonzero character discrepancy tends to zero. The1/2
comes from equal second and third channel marks in the first two stages,
whose durations total4k. This is a genuine retained local correlation,
not an unnormalized matrix decaying because channel masses shrink. The
module's `subgroup_delta` and Gram evaluations are expressly floating
diagnostics; its residue and histogram paths use exact modular arithmetic.
The inspection checks the formulas and boundaries, not execution results.

## Connections to this round, with domains kept separate

**MQ2:** Both constructions show why *labeled* measurements retain information
lost by scalar energy summaries. MQ2 is the complete mixed-quadratic intensity
chart of the actual folded complement B, whose inverse transform recovers
off-diagonal products of B. This new3×3 Gram consists of selected pairwise
characters of three **local p-primary channel phases**. It is neither that
complete chart nor a reconstruction of the complementary phases. No
identification of the two carriers is justified merely by the word tomography.

**QCO5:** A complex-linear coefficient selector that commutes with the
single prime-clock shift still has invariant outputs proportional to W.
The new chronological birth-stage labels offer a concrete place where a
future source rule could break that equivariance. QCO5 does not automatically
apply to every Gram, nonlinear construction, or stage-dependent rule. The
new branch has not supplied a source-selected signed estimate for such a
rule, so neither an automatic no-go nor an automatic escape is established.

**Remaining complement debt:** Its exact p-primary genealogy can help choose
an anchored representation or test source mutants, including mutants that
match the first two Gamma jets. It still leaves the real complementary
phase unconstrained. The new tests explicitly preserve two relevant controls:
a rational p-unit seed changes real phase while leaving these local residues
unchanged, and a complementary phase chosen as the local phase's conjugate
makes the full product identically1. The latter is correctly labeled a
coherent observer control, not the authentic zero source.

**Verdict:** useful additional chronology and local multichannel arithmetic;
no new original-zero signed covariance decay estimate is present at this
pin. The most relevant next connection is a stage-labeled source-derived
coefficient rule with an independently bounded real complement, retaining
the phase frame and paying the residual/commutator terms. Pi base16
normality and RH remain **OPEN**.

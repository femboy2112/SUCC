# Proof Teeth: exact SUCC / YEAN formal boundary

SUCC research PR: https://github.com/femboy2112/SUCC/pull/134
YEAN research PR: https://github.com/femboy2112/yean/pull/135

The formal result is pinned to YEAN
`bf49477d9758e17070e9603526ead3e3e11122a1`, on
`research/succ-proof-teeth-kernel-2026-10-15`, whose parent is
`f58cdf5147e96148aa82481c0a37ea53d21247cf`. It extends the existing paired
research lineage, not main. SUCC's child starts at
`0f86ba2478a72bf90cf33a4ee192cb2265d992dd`.

There are **62 new kernel-checked theorems**: 14 in AffineWord, 20 in TwoPoint,
and 28 in FiniteRetract. The audit also records 25 new definitions and 14 existing
YEAN declarations. Exact statements and per-declaration axioms, rather than this
summary, determine the formal claim:

- [Lean modules and theorem-family report](https://github.com/femboy2112/yean/blob/bf49477d9758e17070e9603526ead3e3e11122a1/research/proof_teeth_2026-10-15/SWARM_B_REPORT.md).
- [All exact types and `#print axioms`](https://github.com/femboy2112/yean/blob/bf49477d9758e17070e9603526ead3e3e11122a1/research/proof_teeth_2026-10-15/receipts/axioms-and-types.txt).
- [Compiler commands and exit codes](https://github.com/femboy2112/yean/blob/bf49477d9758e17070e9603526ead3e3e11122a1/research/proof_teeth_2026-10-15/receipts/commands.json).
- [Transitive dependency, source and axiom manifest](https://github.com/femboy2112/yean/blob/bf49477d9758e17070e9603526ead3e3e11122a1/research/proof_teeth_2026-10-15/receipts/manifest.json).

The successful runner freshly compiled 21 local modules serially with Lean
4.29.1, commit f72c35b3f637c8c6571d353742168ab66cc22c00. Its final audit uses
`-j1 -M2304 -t0`. Pinned external packages and prebuilt artifacts are read-only;
they were hashed and imported proof terms checked at trust level zero, not all
rebuilt from source. The principal separately rechecked 3,245 source hashes and
49 successful command-log hashes; see
[the reconciliation receipt](../research/2026-10-15/proof_teeth_receipts/yean-principal-reconciliation.json).

The axiom budget is `propext`, `Quot.sound`, and, in the rational finite-sum
lane, `Classical.choice`. Some counterexamples require no axioms. No custom
axiom, `sorry`, `admit`, or `native_decide` is present. This is Lean/Mathlib
verification; it is not an extension of the separate Rust T0 calculus.

| SUCC construction | Actual Lean result | Remaining comparison obligation |
|---|---|---|
| SUCC/FUCC action words | Semiring affine composition and chronological append; positive natural slope under PrimeWord | Runtime source ID/epoch, budget exceptions, prime admission and serialization are outside the model |
| Two-point basis | Affine equality over a ring, including ZMod n; irredundancy with Nontrivial; checked word equality and witness | Arbitrary unknown functions and physical experiments are not affine by declaration |
| Integer-to-residue reduction | Normalization/evaluation reduction and formal natural-source alias counterexample | Residue equality cannot certify natural equality |
| Coimage compiler | Existing MemeSufficientArtifact factor_iff reused; affine report instance | Total ambient decoder requires extra existence hypotheses; Empty/Unit counterexample retained |
| Quotient retract | Actual rational finite sums, cyclic chart x mod n, average-pullback, self-adjoint projector, Pythagoras | Rational counting bilinear form is not itself the complex Haar Fourier theorem |
| Fourier/cyclotomic inclusion | **NOT formalized in this round** | Remains PAPER_PROVED with exact cyclotomic instances in SUCC |
| Profinite Hilbert / signed Schur | **NOT formalized in this round** | Paper analytic domains and classical imports remain explicit |

The formal cyclic chart is `(r,t) ↦ r+n*t` in Fin(k*n). Retraction needs k>0;
nontriviality needs n>0 and k>1. A nontrivial projector is not an invertible
route. Existing GeneratingBasis, MemeHomMatrix coherence, MemeProjectorRigidity,
SplitCodec and MemeRouteLeafSort authorities were inspected and freshly compiled;
their solved claims were not replaced by new conjectures.

Reproduce in the paired checkout:

```sh
python3 tools/check_succ_proof_teeth.py --dependencies /home/leah/YEAN/.lake/packages --rust
```

Use the corresponding pinned populated package directory on another machine.
Rust 1.85.1 passed all 63 relevant existing tests with
`cargo test --locked --all-targets`. There is no verified Python-to-Lean extraction
adapter and no proof that a JSON capsule authenticates a physical source.

Current-head YEAN CI is infrastructure-unverified: run 38836487441 at bf49477
failed before any step, with the account payments/spending-limit annotation
recorded in [the live CI receipt](../research/2026-10-15/proof_teeth_receipts/yean-current-head-ci.json).
The local inherited Markdown-math gate also fails on two unchanged prior research
notes; that is a separate real baseline defect. Text validation passed. Full
Ouroboros/make-check workflows were not executed in this round.

The next formal step is a source-pinned syntax adapter followed by the exact
Fourier dual injection and cyclotomic embedding. Do not promote the complete
analytic capsule because a rational algebraic sublemma compiled. RH PROVED: NO.

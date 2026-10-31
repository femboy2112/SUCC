# Read-only sibling cross-review — PR #432 edge/seed tomography vs PR #433 superposition

**2026-10-31.** Audited draft [PR #432](https://github.com/femboy2112/SUCC/pull/432), at pinned head `d3907a7937b10dbf51f3926e0dd3460d5ff12353`, including `edge_seed_tomography/PROOFS.md`, `SOURCE_MAP.md`, `NEXT.md` and `CLAIMS.md`. This child [PR #433](https://github.com/femboy2112/SUCC/pull/433) is independently stacked on green-tested PR #431 at `cf23b8cfc39f56935c432ed764adf0a33efb0d7e`, **not on #432**. No imported modifications or shared-source evidence counted as independent proof.

## Exact provenance and research scopes

- **Already in PR #404:** second through thirty-second balanced even moments under full seed Haar and the first 17-factor carry relation. **Already in PR #431:** original-source relative positive path resistance, gauge-gradient flatness, and same-forcing coherent seed firewall. They are not newly discovered by either sibling.
- **Already in PR #432 (ESM-07/08):** exact *second/fourth* balanced moments for late modes in aligned radix-16 seed cylinders and seed-point localization weakness (ESM-10). Our SS-01/04/11/12 have overlapping analytic provenance; DO NOT count them as independent witnesses.
- **Distinct new-to-project scope of PR #433:** the complete conditional moment hierarchy **for each r=1,...,16** on every base-16 seed cylinder's tail, finite dyadic path-ensemble rank-one phase Gram collapse and 16-adic late-time alias, an exact point-evaluation gradient-energy cost, and quantitative late-time coherent source 17-factor resonance. These are extensions/controls, not a π proof.
- **Distinct useful PR #432 results:** original selected BBP edge-normality is exactly equivalent to π base-16 normality (ESM-01/03, equivalence only); the complete finite counterfactual intensity remembers every complex pair-phase ratio (ESM-04); the classical (73,9,1) cyclic difference set gives alias-free 73-point DFT tomography for nine frequencies of radix 16 and h coprime to 73, with only a global phase ambiguity (ESM-05/06). PR #432 also adds rational horizon-dependent coherent changed seeds `s_K`, a new hostile holdout.

## Finite tomography horizon theorem (CLASSICAL / elementary, finite scoped)

For N ordered BBP time modes 16^n, all N(N−1) nonzero oriented integer differences 16^n−16^m (n≠m) are distinct, as PR #432 proves by 16-adic valuation. An alias-free cyclic Fourier detector must assign distinct residues to those labels **plus zero**, so necessarily

```
modulus >= N*(N-1)+1
```

This lower bound is necessary, not sufficient for the existence of a good modulus. At N=9, p=73 achieves the bound exactly: the residues `D={16^n mod73:1<=n<=9}` have all 72 nonzero ordered differences exactly once (classical projective-plane / difference-set construction in PR #432). But ord_73(16)=9, so the 10th time mode has the same residue as the first; p=73 fails at N=10, independent of source phases. Further, at p=73 any h divisible by 73 causes all h-weighted difference labels to alias.

**No fixed cyclic finite grid can remain alias-free at arbitrarily long horizons.** For modulus q, the list 16^n mod q has a repeated value among its first q+1 entries by pigeonhole; recurrence by multiplication 16 then repeats forever after that point (or is already zero in a nonunit chart). A correct tomography program must grow or adapt modulus with N and re-check *all* oriented labels. This generalizes our dyadic-only alias theorem SS-09 and does not refute PR #432's finite alias-free design.

**Two independent local regression guards:** `test_24` recomputes the integer (73,9,1) difference-set labels without importing PR #432 code and rejects extension to N=10 and h divisible by73. `test_25` exhausts fixed-modulus repetitions for 2,16,17,19,73,127,256,257,1201 and juxtaposes true continuous-cylinder phase mean zero with dyadic-grid alias onset. The tests use exact integer arithmetic and are calibration, not independent external proof of normality.

## Coherent, source-attested proof harness

Use **PR #431** as the typed carrier and resistance/path-measure interface; **PR #432** as finite phase-pair tomography and alternate edge-normality gate; **PR #433** as conditional-moment, anti-alias and point-evaluation-cost firewall. Always keep the true source's four signed poles and `U0=0`, real tail `T_n`, and actual-vs-virtual flag. Include three hostile holdouts: altered coherent infinite seed `s*=-π/16`, PR #432's rational near-coherent finite prefixes `s_K`, and PR #431's arbitrary q-Pascal phase-by-fiat. Any proposed all-horizon bound that applies to `s*` cannot prove normality.

**OPEN verdict-changing theorem:** source-derived signed off-diagonal sum `|S_N(h;0)|^2=o(N^2)` for every fixed integer h≠0, with complete time/frequency coverage, independent source/seed and transport verification. Recovering that exact sum from finite measurements is not a bound on its value. π normality and RH remain OPEN.

**Status:** classical exact alias/no-go (proved local); shared model-moment source (not independent); selected original real phase saving (UNVERIFIED). Draft only; no merge or publication.

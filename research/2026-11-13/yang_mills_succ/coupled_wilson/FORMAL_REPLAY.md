# Bounded formal replay — 2026-11-13

**Verdict: observed successful bounded replay; the Yang–Mills construction theorem was not reproduced here.** The distinction is essential. We ran the upstream integrity check, compiled one original proof-generation module, tested a valid and an invalid transport, and kernel-checked a new finite rational counterexample certificate. We did not compile `YangMills.jointExistence`, `YMReview.Acceptance.combined_acceptance`, `YMReview.OPE.constructed`, their dependency closure, or the Comparator review suite.

## Pins and actual execution

| Input | Verified identity |
|---|---|
| Assessment repository | `yang-mills-group/YM`, commit `55ba9fc36293b3f4d52c6b1f813169a0be76ee98` |
| Submitted source | October 28 import corresponding to `openai/yang-mills` commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464` |
| Compiler | Lean 4.32.0, commit `8c9756b28d64dab099da31a4c09229a9e6a2ef35`, official Linux x86_64 release |
| Downloaded release archive SHA-256 | `fca846f3588724a38ad19ee40292c67cb7438d7555903372e3308eef795ba516` |
| Original module | `submissions/openai-20261028/submission/YM/UVExtension/Orchard/Barrel.lean` |
| Original module SHA-256, before and after | `e3b65f4eb934fe60668bfe6642abe6314cfcc73a90efe22cc7cd3378e9c50912` |

The archive checksum was obtained from the official [Lean 4.32.0 release metadata](https://api.github.com/repos/leanprover/lean4/releases/tags/v4.32.0) and matched the downloaded archive. No global installation, dependency upgrade, remote installer, or `lake update` was used. The imported source was not changed.

The executed portable command was:

```sh
python3 scripts/yang_mills_bounded_replay.py \
  --upstream /workspace/scratch/af4759a8623f/YM-audit \
  --lean /workspace/scratch/af4759a8623f/ym-replay/lean-4.32.0-linux/bin/lean \
  --toolchain-archive /workspace/scratch/af4759a8623f/ym-replay/lean-4.32.0-linux.tar.zst \
  --output /workspace/scratch/af4759a8623f/ym-replay/final-run-v2
```

Substitute local checkout/toolchain/output paths to rerun. The script checks the pinned assessment HEAD, compiler version/commit, source hash, and optionally the release archive checksum. It does not obtain missing dependencies automatically. Exact commands, working directories, fixture hashes, return codes, standard output and errors are preserved in [bounded_replay.json](replay_receipts/bounded_replay.json). Full upstream integrity details are also preserved in [upstream_integrity.json](replay_receipts/upstream_integrity.json).

## What passed

1. **Upstream integrity, before and after:** 9,508 submitted files and 43 review modules match the package manifests. Four original OS declarations match the separately sourced declarations after the documented normalization. This is provenance and text correspondence; the full upstream OS projects were not jointly compiled.
2. **One original module compiled:** `Orchard/Barrel.lean` implements the `vintage` command, replacing a referenced constant by its explicitly supplied `Vintage` variant in a proof term and type, then asking Lean to check the resulting declaration. This is proof-transport infrastructure, not the Yang–Mills theorem.
3. **Positive transport:** an original definition with value 7 and a replacement definition also with value 7 transport a proof of equality to 7. The generated theorem compiles. `#print axioms` reports no axioms for this example.
4. **Hostile transport:** changing only the replacement value to 8 is rejected with `(kernel) declaration type mismatch`. Source syntax alone cannot authorize that change of semantics.
5. **New rational certificate:** [WilsonTaylorNegative.lean](formal/WilsonTaylorNegative.lean) compiles with `-DwarningAsError=true`. It computes all nine entries of the proposed reflected Gram matrix from the supplied rational moment table, verifies its negative direction, and proves the matrix is not positive semidefinite.
6. **Hostile sign control:** changing the claimed value from `-71/512` to `+71/512` is rejected. The negative-control log may show `sorryAx` in the failed declaration's diagnostic continuation; that file is required to fail and is not a certified result.

The new finite certificate uses `decide +kernel`, not `native_decide`. Its five printed theorem dependencies are restricted to `propext`, `Classical.choice`, and `Quot.sound`. This is a second implementation of finite arithmetic, not an independent mathematical witness for the analytic identification of the Gram matrix.

## Exact scope of the new certificate

Let the supplied moment functional be

\[
m_0=1,\quad m_2=\tfrac14,\quad m_4=\tfrac18,\quad
m_6=\tfrac5{64},\qquad m_1=m_3=m_5=0.
\]

Apply the product functional \(L(x^a y^b)=m_a m_b\) to

\[
G_{ij}=L\!\left(x^i y^j
\left[1+2(x+y)+2(x+y)^2+(x+y)^3+\tfrac14(x+y)^4\right]\right),
\qquad 0\leq i,j\leq2.
\]

Lean checks

\[
G=\begin{pmatrix}
69/32&13/16&179/256\\
13/16&5/16&1/4\\
179/256&1/4&113/512
\end{pmatrix},\quad
v=(-4,5,5),\quad v^\top Gv=-71/512,
\]

and \(G_{00}>0\), \(v^\top Gv/G_{00}=-71/1104\), and \(\neg(\forall v,\ v^\top Gv\geq0)\).

The analytic identification of \(m_n\) with moments of the real coordinate of normalized Haar \(SU(2)\), and of the polynomial with the squared Taylor amplitude, is supplied by the accompanying mathematical derivation. Those analytic facts are not formalized in this Lean file. No theorem about a continuum limit or mass gap follows from the finite certificate.

## Failures and limits retained

- The first compilation attempt used the output directory as Lean's source root while compiling an external source path. Lean rejected that path; the dependent fixture imports then failed. [initial-root-error.json](replay_receipts/initial-root-error.json) retains this setup error. The successful runner compiles the original file from its own source root and writes its build output elsewhere.
- Ordinary `decide` did not unfold Lean's deliberately irreducible rational operations. Replacing it with `decide +kernel` enabled kernel reduction; no native evaluation or additional axiom was introduced.
- An exploratory `leanchecker --help` invocation returned exit 137 without output. It provides no successful secondary check and is excluded from all pass claims. Its termination cause was not established.
- The full upstream rerun documentation estimates about three hours and 52 GiB for dependency/build products, plus tools and temporary storage. The local environment initially had about 57 GiB free and 9 GiB available RAM. We did not start that full build. The unexecuted remainder is a resource/scope limitation, not a reported proof failure.
- The portable upstream runner uses `fake-landrun.sh`, including on Linux, and no external kernel. Reading that runner is not equivalent to executing its Comparator and negative-control targets; we did not execute those targets.

## Next falsifying probe

Run the complete pinned upstream build, all 43 review modules, the 13 endpoint axiom checks, and the three Comparator targets with their negative controls in a sufficiently provisioned environment. Preserve the tool pins and source imports. A full pass would support reproduction of the *stated formal endpoints*; it would still not add a mass-gap or infinite-volume-uniqueness theorem to those endpoints.

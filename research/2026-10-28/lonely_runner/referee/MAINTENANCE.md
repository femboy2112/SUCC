# Evidence layout and parent-diff audit

The child branch starts at PR #351 head
`27af9600ddd8acacea7a1822921083821c5dbf6e`, whose main ancestor is
`b763ba8ef375fbac221e29e4396989a635a6ef36`. Live remote heads and all six
parent workflows were checked before edits. A fresh worktree isolates this
campaign from the original branch and all other research worktrees.

The parent diff has 306 paths and 10,726,894 bytes in the changed files.
Byte-identical file groups account for 3,847,309 redundant bytes, principally
repeated n95 certificates and replay logs. These copies bind distinct past
execution observations. They are preserved: relocating or deleting them would
invalidate historical receipts and is unnecessary to review the mathematics.
The complete path/hash/size inventory is retained in the baseline validation
directory, alongside the exact commands and starting Git state.

This child isolates new generated census evidence in
`receipts/census-21-30/`. Deterministic gzip retains full raw JSON bytes;
its index binds both compressed and uncompressed SHA-256 values. Replaying
the census regenerates the original raw JSON and compares it after decompression.
This is lossless storage, not omission of rejected cases or a weaker receipt.
The independent Fraction path remains separate from the primary implementation.

The inherited 80-file source manifest remains unchanged. A child manifest
pins new sources separately, preventing unrelated historical status changes.
The generated mathematical catalog is rebuilt because new dossiers exist;
its raw indexing status confers no mathematical authority. New runtime and
hosted observations after the final commit live outside the worktree so that
validation can remain tied to an immutable source commit.

The unshifted growth manuscript is separate from the parent's local-rule
manuscript. No original BBP source, frozen archive, release metadata, license,
other research branch, or main commit is changed by this campaign.

## Rendered manuscript

`MANUSCRIPT.pdf` is a nine-page rendering of `MANUSCRIPT.md`, visually
inspected locally. Reproduce the mathematical content with:

```sh
pandoc research/2026-10-28/lonely_runner/referee/MANUSCRIPT.md \
  -f markdown+tex_math_single_backslash -s --pdf-engine=pdflatex \
  -o /tmp/lonely-runner-manuscript.pdf
```

PDF metadata includes the build time; byte identity is not a reproduction
requirement. Both the committed Markdown and rendered PDF have source pins.

# Preserved failures and repairs

## First conductor-2 stage assertion

The initial approximate-grid calibration asserted that every truncated
Stoneham c=2 stage position `n=2^j,...,2^(j+1)-1` is already zero modulo one.
The exact test refuted it at j=5: the newest term begins at 1/32, then 1/2,
then zero. The correct statement retains `ceil(j/4)` transient radix steps;
the zero cell has multiplicity `2^j-ceil(j/4)`, which still diverges.

Raw failed runs are `focused_tests-with-grids.log` and
`approximate_grid_failed.log`, with command metadata. The latter was emitted
under the original path `approximate_grid_receipt.json`; after the failure
it was moved byte-for-byte to a `.log` path because it is traceback text,
not JSON. `command_receipts.grids.json` preserves the original launch output
path and unchanged SHA256 `55709acb6901be231fa6fcebe63f1a26156de826a448a9f8f324b3d0e547cad5`.
This paragraph is the explicit relocation mapping. The corrected probe
is written to `approximate_grid_receipt-corrected.json`; the old failure is
not overwritten. This is a faulty calibration assertion, not a change to
the authentic BBP source or a normality theorem.

## Analytic method failures

All 18 attempted Fourier-completion absolute-value bounds were >=L on the
declared windows; their exact Fourier identity remains valid. Fresh SC-06
energy observations all exceeded the trial threshold, but no uniform proof
was obtained. The finite approximate-grid search excludes its declared
q/error/window class only. The all-seed energy minimization theorem is an
obstruction to source-only coercivity, not a theorem about zero-seed saving.

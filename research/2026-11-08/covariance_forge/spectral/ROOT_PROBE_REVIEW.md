# Review of the root's signed sparse-spectrum interval probe

Reviewed `../run_spectral_probe.py` and `../intervals.py` as they stood when
`PROVENANCE.json` recorded their SHA256 hashes. This is a separate same-model
source review, not an independent numerical replay or external referee.

The sparse residual certificate is valid. Its true value is the folded
complement norm squared minus the sum of its s largest Fourier-bin energies.
The sum of the s largest **upper endpoints** bounds every s-element true sum
from above, and the sum of the s largest **lower endpoints** bounds the true
maximum from below. Combining these with the norm enclosure gives the stated
residual interval; comparison with1/4 correctly tests L2 error at most1/2.

The DFT convention is consistent: both transforms use e(-kr/m), so the signed
bilinear reconstruction is `sum_k a_hat[k] b_hat[-k]`. Conjugating either factor
or using the same index would change the observable. Cycle folding uses
n=A+r+jm and retains the common local phase. Original and changed-seed
complement factors multiply their declared local phase to the intended real
phase. The source-pair construction includes p in its preserved prime set.

Integer interval multiplication, squaring, and division round outward. Exact
quadrant transport places the phase argument inside (-1,1), and the Taylor
remainders 1/28! for cosine and1/29! for sine are valid there. Rectangle
independence can widen bounds, but does not invalidate them.

The direct-mean and reconstructed-mean overlap assertions are useful
consistency checks. They alone do not prove the Fourier identity; the exact
DFT derivation in CFS-4 supplies that identity. Finite sparse-fit successes or
failures do not establish the required asymptotic rates, and even a genuine
fit must pay the prime-leakage factor.

No substantive defect was found in this scoped source review. Larger runtime
results remain the root's separately recorded evidence.

# Complementary cylinder and Stoneham review

Same-model separate derivation and implementation; no external referee.
Reviewed exact SHA256 is retained in `receipts/cylinders-review-final.log`.

C1a passes: at A=2 the source-corrected radius is strictly <1/17. Neighboring
good states therefore share their multiplication-by-15 fixed-point center.
For center0, the 0/15 digit seam requires its separate side-preservation
argument; the dossier includes it. Each bad position touches at most two
internal edges, giving C≤2K, including L=1.

C1b passes: a constant word of length L+2 lies within 16^−(L+2) of its fixed
point, and its last tested state is within 16^−3. The displayed 15/4096 plus
tail bound is strict already at A=2. The finite-word lower endpoint and the
one-sided approach to its upper endpoint are retained by the separate probe.
C1c's two lost boundary positions are necessary for this counting proof:
all other slip positions require a change among their next two edges. This
yields K≤2C+2, not a zero-boundary exclusion.

C2 passes: 0.overline(01)_16 has distance1/17 from its next state; frequency17
makes all completed characters equal. Its positive lag-slip density therefore
cannot supply finite-band decay. The irrational changed seed is correctly typed.

C3 passes: the last incomplete Stoneham stage has multiplicity at most c(c−1),
not merely an expectation. The grid has q=c^(p−1) points, with a translation;
Fourier orthogonality handles that translation, and the exact worst-case sum
is bounded by q+H. The sum over all completed/partial stage grids is <cN.
The early c states and the positive future-tail budget are both explicitly
accounted for. The all-horizon bound and limsup≤c conclusion therefore follow
under the written H=O(N^(1/3)) scaling. This uses actual Stoneham arithmetic,
not the bare fact of normality. It does not transfer the conductor law to BBP.

Fresh separate checks: 16,984 transition configurations with alternate lawful
source-error endpoints, 768 constant-word positions, 100 period01 positions,
2,048 exact Fourier-grid inequalities, and six full Stoneham stages.
`cylinders_review.py` imports none of the front's code. These are finite checks
of the paper arguments, not new universal proof authority.

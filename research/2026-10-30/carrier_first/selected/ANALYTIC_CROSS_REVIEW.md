# Separate reconstruction of analytic A01--A03

This is a same-model cross-review, not an independent referee certificate.
The reviewed analytic dossier's SHA256 is recorded in
`receipts/analytic-crosscheck.log`. No analytic implementation was imported.

For A01, the four source moments are the moments of the positive density
shown in that dossier, and its resolvent at 16 is exactly the original BBP
boundary. The orthogonality proof of the Markov error identity is valid:
the divided difference of p_d has degree d-1 in x, so multiplying it by
p_d(x) has zero integral. Strict bounds follow because the measure has
positive density on (0,1). The center needs moments through 2d-1; its
norm-based error certificate needs the additional moment 2d. This distinction
is explicit in the final statement and must be preserved.

For A02, the monic shifted Chebyshev comparator has supremum norm
2^(1-2d). Its squared norm is at most (47/15) 2^(2-4d), while every
factor in p_d(16) exceeds 15. Dividing by 15 p_d(16)^2 gives exactly
188/(225*3600^d). The phase multiplication factor 16^n and its effect on
required d are paid. This is a precision transport theorem, not a Weyl
cancellation estimate; its coarse constant need not beat direct truncation
at every small d.

For A03, Gaussian interpolation and orthogonality prove positive weights
and agreement through degree 2d-1. The rational annihilating polynomial
gives rational future moments despite irrational node locations. The
first missed moment differs by h_d, and the finite measure's completed
boundary R_d(16) is rational. The accumulated tail is

    integral x/[(1-x)(16-x)] dmu_d
      = [R_d(1)-16R_d(16)]/15.

For h equal to the denominator of R_d(16), the integer completed phase
drops out, leaving the stated O_d(1) loss from perfect coherence. This h
depends on d. The finite moment matrix has rank d, which also proves the
minimal number of atoms in such an exact positive matching source. These
changed sources cannot inherit the authentic four-pole label.

The separate exact d=1 check uses mass 47/15, node 530/12831 and rational
boundary 201019/1023830. A 40-term rational BBP enclosure lies strictly
inside the A01 interval, the first two source values agree, and the third
deficit equals the exact squared norm. All 64 checked fake path states
satisfy the rational-boundary/Green-tail formula. The general proofs above
do not follow from those finite checks; they have separate mathematical
derivations.

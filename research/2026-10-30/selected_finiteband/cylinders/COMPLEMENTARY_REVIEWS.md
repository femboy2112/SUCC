# Complementary proof reconstruction

These checks are by another same-model agent in the same research context.
They are useful independent derivations/implementations, not an external
referee or independent proof authority. Exact reviewed hashes are in receipts.

## Kernel K01/K02

Reconstructed K01 directly from the Hilbert coefficient sum, independently
confirming sum_h h^2(1-|h|/H)=H(H^2-1)/6 and the diameter sqrt(2H), using
nonnegativity of Fejer. Integrating min(A,B/x^2) gives 2sqrt(AB), whose square
is pi H sqrt(H^2-1)/(8sqrt(3)); the stated C_* is correct.

Checked the source bound from the three positive reciprocal differences and
the Green series. Seven fresh rational source cases and five fresh frequency
moments pass in `kernel_review.py`, alongside symbolic constant checks.

For K02, independently reconstructed the pair-vector expansion
E=H-2A/N+||V||^2/N^2 and the resulting error bracket after taking square roots.
The n^-4 majorant, cutoff at n~sqrt(H), finite-N tail integral and the regime
N/sqrt(H)->infinity all have the required powers. Tonelli's nonnegative
cosine-defect representation reduces the Mellin integral to
sqrt(pi)/16 times 2 integral_0^1(1-u)sqrt(4pi u) du = pi/15.
The value and general coefficient 8pi sqrt(A)/15 check out. This establishes
sharp source-uniform transport order using a changed coherent seed; it says
nothing about sharpness at the selected zero seed. No defect found.

## Arithmetic AQ01–AQ04

Reconstructed the positive measure from the three reciprocal differences:
its 1/64 scaling, interval support, mass 1/64 and geometric moment formula
are correct. The functions F_1,...,F_M,1,b,...,b^J are linearly independent
by successively inspecting double poles 0,-1,...,-(M-1).

The noncompact cubature argument is sound: absolute integrability permits
finite compact approximations, rational support nodes are dense, and a
supporting functional vanishing at the moment vector must vanish on a whole
interval of positive density. Thus the vector is interior to the cone's
closure. Full-dimensional convex cones share their interior with their
closure, paying the exact-membership step. Minimizing the number of positive
weights makes the columns independent, giving at most M+J+1 nodes; rational
columns and target make the unique weights rational.

The order-J Taylor remainder bound (J+2)t^(J+1) for (1+t)^-2 is valid on
the whole positive half-line. It therefore controls the unbounded support
without a compact-support assumption. The telescoping Green identity and
zero-boundary recurrence give the rational completed constant. The error
bound in AQ03 needs only one common upper bound, since both tails are
nonnegative; no missing factor two occurs.

The minimum node count follows from the squared vanishing polynomial of
degree 2s. Full-moment identification should transfer an exponential moment
to an arbitrary positive rival by monotone convergence before invoking
analyticity; that clarification was sent to the arithmetic author and added.
The complete four-pole family is correctly separated from the larger
positive double-pole mutant family.

`arithmetic_review.py` uses a geometric-shift recurrence (rather than the
producer's Eulerian recurrence or oracle's Laplace series) for six moments,
rechecks three holdouts, and constructs a fresh exact two-node M=1,J=0 witness
using endpoints 1/8 and 3/4 with no numerical optimization. The next source
value differs, so the witness is explicitly a changed source. No defect found.

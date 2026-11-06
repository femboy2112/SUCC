# Finite Mellin interpolation holdout

Derived the error integral before running these checks. At N=1,3,9,13
construct the truncated angular impulse blocks by multiplying the recurrence
u_j=u_{j-1}-u_{j-2}/2, with u_0=u_1=2, reflect and divide by 4. Compute
every Dirichlet-polynomial value at 0,-1,...,-8N by exact arithmetic.
The oracle is half the Euler numbers from the reciprocal cosh series.
Expect exact agreement through 8N−1 and first difference
beta(−8N)−B_N(−8N)=(8N)!/(2*16^N). Independently compute the selected
state via the authenticated eight partial fractions and check its exact
scale at s=1. This is local ordering evidence only.

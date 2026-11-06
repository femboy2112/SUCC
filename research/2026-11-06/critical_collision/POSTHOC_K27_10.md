# Post-hoc strengthening of exact finite continuum-radius upper caps (NOT BLIND)

The preregistered N4096 holdout used K=3. After observing all N=128,256,512,1024,2048,4096 records, the stored integer counts were independently rechecked against the STRONGER rational threshold K=27/10=2.7. This selection is POST-HOC, **not a preregistered holdout**, and no all-N statement follows.

For every stored grid r_j with next r_(j+1)≤4r_j/3, the exact integer test

    40*(A_N(r_j)−N)*den(r_j) <= 81*N²*num(r_j)

passed for all 132 stored radii across all six N. This is exactly (A_N(r_j)−N)/(N² r_j) ≤ 81/40 = 2.025. By monotonicity of A_N and the grid ratio, for every REAL δ∈[1/(N+1),1/2] at each listed N:

    A_N(δ) ≤ N + (27/10) N² δ.

Maximum sampled ratios (float display ONLY; the predicate is exact rational):
N=128 1.986883907; 256 2.001418024; 512 2.006168962; 1024 2.007693169; 2048 1.999184343; 4096 1.999706887.

One must not relabel these six post-hoc strengthened finite certificates as ∀N. The original K=3 prediction at N4096 was predeclared and passed; the improved K=27/10 is exploratory reanalysis. All-horizon original-source collision bound and π normality remain OPEN.

Reproduce from exact raw counts in RADIUS_CERTIFICATES.json and HOLDOUT_N4096.json; use Fraction, not floats, for tests.

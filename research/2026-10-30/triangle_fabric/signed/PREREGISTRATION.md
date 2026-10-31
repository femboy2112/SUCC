# Signed-front hypotheses and controls, before exact execution

Parent405 `6cf5050ff2cfd92e7a0c8876da5233be6ff117f5`; research branch
`research/triangle-categorical-fabric-2026-10-30`. No source changes.

1. **SF-01:** for N>=0,M>=1 the rational moment Gram system for BBP weight
   `(1-z)^M w(z)` defines a monic orthogonal p_N. The filter
   `F=1-(z-1)^M p_N(z)/(15^M p_N(16))` is positive on [0,1], annihilates16,
   reproduces source values1..N and the first M kernel derivatives.
   Pass: all symbolic equalities and source-relative inequalities hold.
   Fail: any exact residual or violated exact inequality. Finite passage
   corroborates the paper theorem; it does not establish its quantifiers.
2. **SF-02:** the corresponding zero-seed selected boundary is rational;
   its error below π has sign (-1)^M. Pass: algebraic rational telescoping
   and rigorous BBP intervals order these approximants correctly. Numerical
   quadrature alone is ambiguous.
3. **SF-03:** convex mixing of an even/odd pair allows an explicit dyadic
   boundary with the same prefix and arbitrarily many jets. Its zero-seed
   orbit is eventually a decaying rational tail modulo1; all fixed-h means
   tend1 and lag energy is summable. This refutes a NORMALITY certificate
   using only positivity, rank/finite jets, a finite exact zero-boundary
   prefix and arbitrarily small source-relative error. It does not refute
   the authentic four-pole source, which these mutants do not preserve.
4. **SF-04:** same-source finite scalar/Gamma geometry cannot provide
   fixed-h selected cancellation. Existing coherent irrational seed and
   rational alias controls must retain their correct types.

Declared exact training cases `(N,M)`:
(0,1),(0,2),(1,1),(1,2),(2,3),(3,2),(4,4).
Declared fresh holdouts: (5,3),(7,4),(8,5),(11,6).
For every case: orthogonality, F16, source indices1..max(32,2N+4), jets0..M+2,
256 rational z-grid points, and telescoping indices0..48.
Dyadic pairs: N=0,2,5,8 with minimum jet depths2,4,4,6 respectively.
Separate oracle will reconstruct p_N by determinant/Gram-Schmidt using the
three-positive-term source, not import the main polynomial solver.
Control: F=1 authentic must fail annihilation; source-altered coefficient
ratio and zero source are not silently treated as authentic.

Mathematical independence: separate code paths are computational checks;
same-model agents are not independent referees. No scholarly priority claim.

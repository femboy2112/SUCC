# Independent arithmetic review of CFS-1, CFS-2 and CFS-7

Reviewed `../spectral/THEOREMS.md`, SHA256
`4557a77ca42d0dc876c79adca40df3202b2db2edf7046ae10c719afd469e666b`.
This read occurred only after root explicitly opened the cross-review round.
The arithmetic bearing did not develop these results. The review is a paper
derivation and hostile boundary audit; it is not a Lean certificate or a new
independent verification of the imported BK theorem.

**Verdict: the three stated inequalities survive.**

- CFS-1: expanding the normalized DFT square gives exactly 1/m times the
  sum of the m cyclic autocorrelations. The zero shift contributes 1/m;
  all remaining shifts have nonzero coefficient xi(g^d-1), since g has
  exact order m. BK therefore yields 1/m+(1-1/m)delta with the stated
  normalization. There is no independence premise or dropped sign.
- CFS-2: the Dirichlet estimate is min(1,1/(2m||t||)). The nearest m-grid
  point is at distance at most 1/(2m), so the other points at index distance
  j have denominator at least 2j-1. At most two points occur at each
  distance, giving the conservative 1+2 harmonic-sum bound. Repeated complete
  cycles add a normalized geometric factor of modulus at most one. The
  interval comparison uses the same unit-modulus sequence; the source
  prime boundary is not crossed while claiming a clean-cycle formula.
- CFS-7: the finite Gram bound has prefactor (m+H-1)/(mH). Multiplying its
  off-diagonal weights, whose sum is (H-1)/2, gives the valid estimate
  2/H+2 max|correlation|. For x_j<=1 and t=1/H<=1,
  (x_j+t)^2<=2x_(j+1)+4t+t^2<=5(x_(j+1)+t). Iterating yields exactly
  the exponent 5^(2^d-1). This constant is loose but valid.

The last point's main potential failure was wraparound. Here every difference
is applied after zero extension, so the surviving support is exactly
0<=r<m-sum h_i. On that interval its phase coefficient is
xi product(g^(h_i)-1), nonzero because 0<h_i<m. The dth polynomial difference
is constant, and restoring the missing complete-cycle terms costs at most
sum h_i/m. Both the endpoint cost and the condition d(H-1)<m are necessary
in this argument and are present. Applying a cyclic polynomial difference
instead would be invalid: for example P(r)=r^2/7 on m=4 has a wrap difference
at r=3 differing from the usual polynomial difference by -16/7.

H=floor(sqrt(m)) satisfies the finite restrictions eventually for each fixed
d. The uniformity in real polynomial coefficients survives translating each
complete cycle. The final normalized interval comparison is valid for any
unit-modulus sequence, so it also preserves this uniformity.

The scope boundary is essential: these are correlations of one original
p-local factor against prescribed temporal model classes. An arbitrary
history-dependent complementary phase is outside those classes unless an
actual approximation/complexity estimate is supplied. The arithmetic
terminal-support counterfamily retains the same local factor while forcing
the full signed average, and hence covariance, toward one. It supplies a
hostile control for any attempt to omit that complementary-phase premise.

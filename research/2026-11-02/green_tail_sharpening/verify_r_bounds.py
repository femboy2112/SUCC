"""Verify sharp two-sided bounds on r(n)."""
from fractions import Fraction
def r(n): return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

# (1) r(n) > 15/(64 n^2) for all n>=1
assert all(r(n) > Fraction(15, 64*n*n) for n in range(1, 2000))
# (2) r(n) < 15/(64 (n-1)^2) for n>=2
assert all(r(n) < Fraction(15, 64*(n-1)*(n-1)) for n in range(2, 2000))
# (3) r(n) > 15/(64n^2) + 151/(512 n^3) (positive-term series)
assert all(r(n) > Fraction(15,64*n*n)+Fraction(151,512*n**3) for n in range(1, 2000))
# (4) theta(n) = n^4 (r(n) - 15/(64n^2) - 151/(512n^3)) < 19999/7680, decreasing
theta = [n**4*(r(n)-Fraction(15,64*n*n)-Fraction(151,512*n**3)) for n in range(1,300)]
assert all(t <= Fraction(19999,7680) for t in theta)
assert all(theta[i] > theta[i+1] for i in range(len(theta)-1))
# (5) asymptotic coeffs
assert abs(float(3000**4*(r(3000)-Fraction(15,64*3000*3000)-Fraction(151,512*3000**3))) - 1209/4096) < 0.01
print("r(n) two-sided bounds: ALL PASS")
print("  r(n) > 15/(64n^2)  [sharp lower]")
print("  r(n) < 15/(64(n-1)^2)  [upper, n>=2]")
print("  r(n) = 15/(64n^2)+151/(512n^3)+theta(n), 0<theta<19999/(7680 n^4)")

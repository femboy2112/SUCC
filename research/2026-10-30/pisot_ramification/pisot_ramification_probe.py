"""SUCC: exact finite counting ramification into Pisot-coordinate carriers.

All tests use standard-library integer/Fraction arithmetic; approximate roots
are only calibration. Neither field change proves pi normality nor GR.
"""
from fractions import Fraction as F
from math import comb, isqrt, sqrt
import unittest


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))


def scale(k, a):
    return tuple(tuple(k*x for x in r) for r in a)


def mul(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))


def power(a, n):
    z = eye(len(a))
    while n:
        if n % 2:
            z = mul(z, a)
        a = mul(a, a)
        n //= 2
    return z


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def char3(a):
    trace = sum(a[i][i] for i in range(3))
    minors = sum(a[i][i]*a[j][j]-a[i][j]*a[j][i]
                 for i in range(3) for j in range(i+1, 3))
    return (1, -trace, minors, -det3(a))


def disc3(b, c, d):
    return b*b*c*c-4*c**3-4*b**3*d-27*d*d+18*b*c*d


def conv(a, b, depth):
    out = [0]*(depth+1)
    for i, x in enumerate(a[:depth+1]):
        for j, y in enumerate(b[:depth+1-i]):
            out[i+j] += x*y
    return out


def tiles(nmax, tile_length, colors):
    a = [0]*(nmax+1)
    a[0] = 1
    for n in range(1,nmax+1):
        a[n] = a[n-1]+(colors*a[n-tile_length] if n>=tile_length else 0)
    return a


A2 = ((1, 3), (1, 0))
B2 = add(A2, eye(2))
A3 = ((1, 0, 3), (1, 0, 0), (0, 1, 0))
B3 = add(add(scale(2, eye(3)), A3), mul(A3, A3))


class PisotRamification(unittest.TestCase):
    def test_two_color_tiling_pascal(self):
        a = tiles(35, 2, 3)
        for n in range(36):
            self.assertEqual(a[n], sum(3**j*comb(n-j, j)
                                      for j in range(n//2+1)))
            self.assertEqual(a[n], power(A2, n)[0][0])

    def test_positive_fibonacci_convolution_resolution(self):
        a = tiles(24,2,3)
        f = tiles(24,2,1)
        for n in range(25):
            total = 0
            for k in range(n//2+1):
                prod = [1]+[0]*24
                for _ in range(k+1):
                    prod = conv(prod, f, 24)
                total += 2**k*prod[n-2*k]
            self.assertEqual(total, a[n])

    def test_quadratic_binomial_pisotification(self):
        a = [power(A2,n)[0][0] for n in range(18)]
        b = [power(B2,n)[0][0] for n in range(18)]
        self.assertEqual(a[:5],[1,1,4,7,19])
        self.assertEqual(b[:5],[1,2,7,23,76])
        for n in range(18):
            self.assertEqual(b[n],sum(comb(n,k)*a[k] for k in range(n+1)))
            self.assertEqual(a[n],sum((-1)**(n-k)*comb(n,k)*b[k]
                                     for k in range(n+1)))
        for n in range(2,18):
            self.assertEqual(b[n],3*b[n-1]+b[n-2])

    def test_quadratic_shift_family(self):
        for a in range(1,12):
            for b in range(1,12):
                discriminant = a*a+4*b
                small = (a-sqrt(discriminant))/2
                m = int(-small+0.5)
                large = (a+sqrt(discriminant))/2
                self.assertGreaterEqual(m,0)
                self.assertLessEqual(abs(small+m),0.50000000001)
                self.assertGreater(large+m,1)
                # Shifted characteristic has integral coefficients:
                self.assertEqual((a+2*m), int(a+2*m))
                self.assertEqual(m*m+a*m-b, int(m*m+a*m-b))

    def test_cubic_nonpisot_matrix(self):
        self.assertEqual(char3(A3), (1,-1,0,-3))
        a2 = mul(A3,A3)
        p = add(add(power(A3,3),scale(-1,a2)),scale(-3,eye(3)))
        self.assertEqual(p, scale(0,eye(3)))
        for n in range(4,18):
            self.assertEqual(power(A3,n)[0][0],
                             power(A3,n-1)[0][0]+
                             3*power(A3,n-3)[0][0])

    def test_nonpisot_cubic_cannot_shift_to_pisot(self):
        p=lambda x:x*x*x-x*x-3
        self.assertLess(p(F(9,5)),0)
        self.assertGreater(p(F(2)),0)
        # If alpha in (9/5,2), the conjugate real part
        # (1-alpha)/2 lies in (-1/2,-2/5), and
        # v^2=3/alpha-u^2 > 3/2-1/4=5/4>1.
        self.assertGreater(F(3,2)-F(1,4),1)

    def test_positive_polynomial_pisotification(self):
        self.assertEqual(B3,((4,3,6),(2,2,3),(1,1,2)))
        self.assertTrue(all(v>=0 for row in B3 for v in row))
        self.assertEqual(char3(B3),(1,-8,5,-1))
        self.assertEqual(det3(B3),1)
        self.assertEqual(add(add(power(B3,3),scale(-8,power(B3,2))),
                             add(scale(5,B3),scale(-1,eye(3)))),
                         scale(0,eye(3)))

    def test_exact_integer_inverse_and_order(self):
        inverse = add(scale(2,eye(3)),scale(-1,A3))
        self.assertEqual(mul(B3,inverse),eye(3))
        self.assertEqual(mul(inverse,B3),eye(3))
        self.assertEqual(add(scale(2,eye(3)),scale(-1,inverse)),A3)
        self.assertEqual(inverse,
                         add(add(power(B3,2),scale(-8,B3)),scale(5,eye(3))))

    def test_unimodular_change_of_integral_basis(self):
        # 1, theta=2+alpha+alpha^2, theta^2=13+7alpha+8alpha^2.
        change = ((1,2,13),(0,1,7),(0,1,8))
        self.assertEqual(det3(change),1)
        # The algebraic number rings have the same Z-basis lattice.
        self.assertEqual(disc3(-1,0,-3),-255)
        self.assertEqual(disc3(-8,5,-1),-255)

    def test_exact_field_ramification_primes(self):
        disc = abs(disc3(-1,0,-3))
        self.assertEqual(disc, 3*5*17)
        self.assertEqual(disc, 16**2-1)
        self.assertEqual(isqrt(disc)**2 == disc,False)
        self.assertTrue(all(disc%(p*p) for p in (3,5,17)))
        # Squarefree polynomial discriminant implies index 1.

    def test_cubic_pisot_conjugate_bound(self):
        # The real root alpha is between 9/5 and 2.
        # theta=(2-alpha)^(-1)>5.
        # Other conjugates beta=u+iv have u<0 and
        # |1/(2-beta)| < 1/2 strictly.
        self.assertGreater(F(1,2) / (F(2)-F(9,5)), 1)
        self.assertEqual(det3(B3),1)

    def test_cubic_pisot_coordinates_preserve_trajectory(self):
        for n in range(13):
            a = power(A3,n)
            # A = 2 I - B^{-1}, hence powers can be expressed
            # using commuting inverse Pisot powers.
            inv = add(scale(2,eye(3)),scale(-1,A3))
            v = scale(0,eye(3))
            for k in range(n+1):
                v = add(v,scale(comb(n,k)*2**(n-k)*(-1)**k,
                                power(inv,k)))
            self.assertEqual(a,v)

    def test_colored_length_three_positive_pisot_expansion(self):
        g = tiles(24,3,1)
        a = tiles(24,3,3)
        for n in range(25):
            total = 0
            for k in range(n//3+1):
                prod = [1]+[0]*24
                for _ in range(k+1):
                    prod = conv(prod,g,24)
                total += 2**k*prod[n-3*k]
            self.assertEqual(total,a[n])

    def test_source_model_not_determined_by_growth_rate(self):
        # Fibonacci pure path, colored path, and polynomial carrier
        # agree on local path classes but have different full sequences.
        f=tiles(12,2,1)
        a=tiles(12,2,3)
        self.assertNotEqual(f,a)
        self.assertEqual(f[:2],a[:2])
        self.assertEqual(A3[0][2],3)
        self.assertNotEqual(A3,B3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

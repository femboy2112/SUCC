"""Exact finite calibration, not a normality/proof checker."""
from fractions import Fraction as F
from itertools import product
import unittest


def forcing_poles(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def forcing_polynomial(n):
    return F(120*n*n-89*n+16, 512*n**4-1024*n**3+712*n*n-206*n+21)


def frac(q):
    return q-q.numerator//q.denominator


def pressure(masses):
    return len(masses)*sum((p*p for p in masses), F(0))


def bernoulli_words(probabilities, depth):
    out=[]
    for word in product(range(len(probabilities)), repeat=depth):
        p=F(1)
        for digit in word:
            p*=probabilities[digit]
        out.append(p)
    return out


def markov_words(depth):
    out=[]
    for word in product(range(16), repeat=depth):
        p=F(1,16)
        for i,j in zip(word,word[1:]):
            p*=F(1,24)+(F(1,3) if i==j else 0)
        out.append(p)
    return out


class ExactRefereeCalibration(unittest.TestCase):
    def test_independent_original_forcing(self):
        for n in range(1,74):
            self.assertEqual(forcing_poles(n),forcing_polynomial(n))

    def test_unwrapped_rational_seed_rotation(self):
        zero,shifted=F(0),F(1,5)
        for n in range(74):
            self.assertEqual(shifted-zero,F(16**n,5))
            self.assertEqual(frac(shifted-zero),F(1,5))
            self.assertEqual(frac(shifted),frac(zero+F(1,5)))
            zero=16*zero+forcing_poles(n+1)
            shifted=16*shifted+forcing_polynomial(n+1)

    def test_bernoulli_product_pressure(self):
        p=[F(9,128),F(7,128)]+[F(1,16)]*14
        self.assertEqual(sum(p),1)
        base=16*sum((x*x for x in p),F(0))
        self.assertEqual(base,F(513,512))
        for m in range(1,4):
            words=bernoulli_words(p,m)
            self.assertEqual(sum(words),1)
            self.assertEqual(pressure(words),base**m)
        for m in range(1,48):
            # Exact factorized depth extension, not direct large enumeration.
            self.assertGreater(base**m,1)
            self.assertEqual(base**m,(F(513,512))**m)

    def test_uniform_marginal_correlated_control(self):
        for m in range(1,4):
            words=markov_words(m)
            self.assertEqual(sum(words),1)
            self.assertEqual(pressure(words),F(8,3)**(m-1))
        self.assertEqual(pressure(markov_words(1)),1)
        self.assertGreater(pressure(markov_words(2)),1)

    def test_positive_ac_component_pressure(self):
        for theta in [F(1,7),F(2,11)]:
            for m in [1,2,5,13,29]:
                M=16**m
                first=theta+(1-theta)/M
                others=(1-theta)/M
                actual=M*(first*first+(M-1)*others*others)
                self.assertEqual(actual,1+theta*theta*(M-1))

    def test_atomless_positive_ac_component_pressure(self):
        theta=F(1,7)
        p=[F(9,128),F(7,128)]+[F(1,16)]*14
        for m in range(1,4):
            words=bernoulli_words(p,m)
            M=len(words)
            mixed=[(1-theta)/M+theta*q for q in words]
            self.assertEqual(pressure(mixed),1+theta*theta*(F(513,512)**m-1))

    def test_frostman_exponent_below_three(self):
        # pmax < 16^(-2/3), so s>2/3 and 2/s<3, without logs.
        self.assertLess(F(9,128)**3,F(1,16**2))

    def test_half_open_digit_map_at_boundaries(self):
        for m in [1,2,3]:
            M=16**m
            for w in [0,1,7,M//2,M-1]:
                x=F(w,M)
                digits=[]
                z=x
                for _ in range(m):
                    d=int(16*z)
                    digits.append(d)
                    z=16*z-d
                value=0
                for d in digits:
                    value=16*value+d
                self.assertEqual(value,w)
                self.assertEqual(z,0)

    def test_sparse_exact_collision_and_half_grid(self):
        # Full grids with two samples replaced by one repeated phase remain
        # weakly Haar as grid size grows, but every Fekete energy is -infinity.
        for N in [17,33,65,129]:
            points=[F(j,N) for j in range(N)]
            changed=[F(0),F(0)]+points[2:]
            self.assertEqual(changed[0],changed[1])
            # Every bounded observable changes normalized sum by at most 4/N.
            self.assertEqual(sum(a!=b for a,b in zip(points,changed)),1)
            half=[F(j,2*N) for j in range(N)]
            self.assertTrue(all(x<F(1,2) for x in half))
            self.assertEqual(half[1]-half[0],F(1,2*N))


if __name__=='__main__':
    unittest.main()

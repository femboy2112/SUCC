"""Exact-Fraction / high-precision Decimal controls for SUCC no-discard/Oily claims.

Research-only: native source comparisons and a declared auxiliary sensor.
Does not sample actual hexadecimal pi digits or prove their normality.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from math import comb
import unittest

C = (4, -2, -1, -1)
T = (0, 3, 4, 5)
GAMMA = D("0.57721566490153286060651209008240243104215933593992")


def rational_source(a):
    a = F(a)
    return sum((F(c) / (a + t) for c, t in zip(C, T)), F(0))


def fake_source(a):
    a = F(a)
    return F(15) / (a * a)


def dfrac(x):
    return D(x.numerator) / D(x.denominator)


def oily(s):
    lam = (D(5).sqrt() - 1) / 2
    return sum((D(1) / k for k in range(1, s + 2)), D(0)) - GAMMA - lam ** (s + 2)


def z_oily():
    lam = (D(5).sqrt() - 1) / 2
    return 1 - GAMMA + D(3).ln() - (1 + 3 * lam) ** (-2)


def log_pole_square(a):
    a = D(a)
    return -sum((D(c * d) * (a + u + v).ln()
                 for c, u in zip(C, T) for d, v in zip(C, T)), D(0))


def chi2_source(a):
    a = F(a)
    return log_pole_square(a) / (D(a.numerator)**2 * dfrac(rational_source(a))**2) - 1


def chi2_upper(a):
    a = D(a)
    c = D(59) / 30
    if not a > 2*c:
        raise ValueError("source lower-normalizer bound requires a>59/15")
    return 6*c*c / (a*a*(1-2*c/a)**2)


def grade_mass(n, s, fake=False):
    a = F(8*n-7)
    R = fake_source if fake else rational_source
    kernel = sum(((-1)**i * comb(s,i) * R(a+8*(2*n-s+i))
                  for i in range(s+1)), F(0))
    return comb(2*n, s) * kernel / R(a)


def tilted_grade(n, fake=False):
    p = [dfrac(grade_mass(n,s,fake)) for s in range(2*n+1)]
    z = sum((x*oily(s) for s,x in enumerate(p)), D(0))
    return [x*oily(s)/z for s,x in enumerate(p)]


class OilyNoDiscardTests(unittest.TestCase):
    def test_rational_four_pole(self):
        for a in range(1,100):
            self.assertEqual(
                rational_source(a),
                F(15*a*a+121*a+240,a*(a+3)*(a+4)*(a+5)))
            self.assertGreater(rational_source(a),0)

    def test_exact_pole_logarithm(self):
        with localcontext() as ctx:
            ctx.prec = 75
            for a in (9,17,49,81):
                L = log_pole_square(a)
                b = D(a)
                nine = (16*(b+3).ln()+8*(b+4).ln()+8*(b+5).ln()
                        -16*b.ln()-4*(b+6).ln()-4*(b+7).ln()
                        -5*(b+8).ln()-2*(b+9).ln()-(b+10).ln())
                self.assertLess(abs(L-nine),D("1e-65"))
                self.assertGreater(L,0)

    def test_chi2_global_bound_and_jet(self):
        with localcontext() as ctx:
            ctx.prec = 75
            for a in (9,17,25,81,257,1024):
                self.assertGreater(chi2_source(a),0)
                self.assertLess(chi2_source(a),chi2_upper(a))
            target = D(3481)/450
            self.assertLess(abs(D(4096)**2*chi2_source(4096)-target),
                            D("0.07"))

    def test_oily_normalizer(self):
        with localcontext() as ctx:
            ctx.prec = 70
            lam = (D(5).sqrt()-1)/2
            self.assertGreater(lam-GAMMA,0)
            total = D(0)
            for s in range(160):
                ps = D((s+1)*2**s)/D(3)**(s+2)
                total += ps*oily(s)
            self.assertLess(abs(total-z_oily()),D("1e-20"))

    def test_history_split_unchanged(self):
        for n in (2,3,5,8):
            for s in range(2*n+1):
                probs = [F(comb(n,j)*comb(n,s-j),comb(2*n,s))
                         for j in range(max(0,s-n),min(s,n)+1)]
                self.assertEqual(sum(probs,F(0)),1)
                # A grade-only positive Oily tilt cancels from all ratios.

    def test_oily_kl_under_global_bound(self):
        with localcontext() as ctx:
            ctx.prec = 75
            om = (D(5).sqrt()-1)/2 - GAMMA
            for n in (3,5,8,12):
                original = tilted_grade(n)
                fake = tilted_grade(n, True)
                self.assertLess(abs(sum(original)-1),D("1e-55"))
                KL = sum((p*(p/q).ln() for p,q in zip(original,fake)),D(0))
                upper = chi2_upper(8*n-7)*(
                    (1+(D(2*n+1)).ln())/om)**3
                self.assertGreater(KL,0)
                self.assertLess(KL,upper)

    def test_oily_mean_grade_and_history_cost(self):
        with localcontext() as ctx:
            ctx.prec = 65
            lam=(D(5).sqrt()-1)/2
            Z=z_oily()
            exact = (6-4*GAMMA+4*D(3).ln()-4*(1+3*lam)**(-3))/Z
            mean=sum((D(s*(s+1)*2**s)*oily(s)/
                      (D(3)**(s+2)*Z) for s in range(160)),D(0))
            self.assertLess(abs(mean-exact),D("1e-19"))
            self.assertLess(abs(exact-D("5.6580417264381389589")),D("1e-15"))
            for n in (4,8,12):
                probs=tilted_grade(n)
                h=sum((p * (D(comb(2*n,s)).ln()/D(2).ln())
                       for s,p in enumerate(probs)),D(0))
                self.assertGreater(h,0)
                self.assertLess(h,2*n)

    def test_high_grade_code_length(self):
        with localcontext() as ctx:
            ctx.prec = 65
            Z=z_oily()
            for s in (5,10,20,50,100):
                for j in (0,s//2,s):
                    W=D((s+1)*comb(s,j))*oily(s)/(D(3)**(s+2)*Z)
                    bits = -W.ln()/D(2).ln()
                    lower = (D(s)*(D(3)/2).ln()+2*D(3).ln()
                             -D(s+1).ln()-(1+D(s+1).ln()).ln()
                             +Z.ln())/D(2).ln()
                    self.assertGreater(bits+ D("1e-40"),lower)


if __name__ == "__main__":
    unittest.main(verbosity=2)

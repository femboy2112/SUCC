from fractions import Fraction as Q
import unittest

from pr_resonance import classify, clock, eligible, evaluate, order16, reduce_on_clock, select_prime, source_xi


class TestPrimeResonance(unittest.TestCase):
    def test_orders_against_independent_walk(self):
        for p in (17,41,73,137,281,4201,4217,4337):
            value, m = 16 % p, 1
            while value != 1:
                value = value * 16 % p
                m += 1
            self.assertEqual(order16(p), m)

    def test_alias_requires_quotient_reduction(self):
        for p in (17,41,73,137):
            for xi in (1,3):
                m = order16(p)
                c = pow(xi, m, p)
                polynomial = [7-c, -3] + [0]*(m-2) + [1]
                result = classify(polynomial, p, xi, h=3)
                self.assertTrue(result['resonant'])
                self.assertEqual(result['remainder'], [7 % p])
                self.assertEqual({(3*x+evaluate(polynomial,x,p)) % p for x in clock(p,xi)}, {7%p})

    def test_nonconstant_remainder_cannot_be_constant_on_clock(self):
        for p in (17,41,73,137):
            for xi in (1,3):
                m = order16(p)
                for D in range(1,min(m,6)):
                    polynomial = [2,5]+[1]*(D-1)
                    remainder=reduce_on_clock(polynomial,p,xi)
                    values={evaluate(remainder,x,p) for x in clock(p,xi)}
                    self.assertGreater(len(values),1)
                    self.assertLess(len(remainder)-1,m)

    def test_selector_absence_and_first_birth(self):
        self.assertIsNone(select_prime(1050))
        self.assertEqual(select_prime(1051),4201)
        self.assertTrue(eligible(4201))
        self.assertFalse(eligible(2017))
        self.assertFalse(eligible(4209))

    def test_literal_source_and_mutant(self):
        for p in (17,41,137):
            L=(p-1)//4
            state=Q(0)
            mutant=Q(0)
            checked=0
            for n in range(1,2*L+1):
                terms=[(4,7),(-2,4),(-1,3),(-1,2)]
                state=16*state+sum((Q(c,8*n-pole) for c,pole in terms),Q(0))
                mutant=16*mutant+Q(5,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
                if n>=L+1:
                    def principal(u):
                        d=u.denominator; pe=1
                        while d%p==0:d//=p;pe*=p
                        return Q(u.numerator*pow(d,-1,pe)%pe,pe)
                    expected=Q(source_xi(p)*pow(16,n-L-1,p)%p,p)
                    self.assertEqual(principal(state),expected)
                    self.assertNotEqual(principal(mutant),expected)
                    checked+=1
            self.assertEqual(checked,L)

    def test_invalid_inputs_and_zero_character(self):
        for args in (([1],15,1),([1],17,0),([1.0],17,1)):
            with self.assertRaises(ValueError):reduce_on_clock(*args)
        with self.assertRaises(ValueError):select_prime(True)
        self.assertTrue(classify([3],17,1,h=17)['resonant'])
        self.assertEqual(classify([0,-1],17,1)['constant_phase_numerator'],0)


if __name__=='__main__':
    unittest.main()

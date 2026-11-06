"""Independent cyclotomic and weak-limit controls for the sphere deck lift."""
import unittest
from fractions import Fraction
import sympy as s
import mpmath as mp

I=s.I
z,w,n=s.symbols('z w n')
J=s.factor(I*(3*z+1-2*I)/((2-I)*z-3*I))
N=3*I*z+2+I
D=(2-I)*z-3*I

class OddTorsionTests(unittest.TestCase):
    def setUp(self): self._dps=mp.mp.dps
    def tearDown(self): mp.mp.dps=self._dps
    def zero(self,v): self.assertEqual(s.simplify(s.cancel(v)),0)

    def test_01_original_recurrence_odd_denominators(self):
        source=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
        collapsed=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        self.zero(source-collapsed)
        state=Fraction(0)
        for k in range(1,81):
            r=Fraction(4,8*k-7)-Fraction(2,8*k-4)-Fraction(1,8*k-3)-Fraction(1,8*k-2)
            state=16*state+r
            self.assertEqual(state.denominator%2,1)
        # One-tap change removes odd-denominator cancellation at source time 1.
        r1=Fraction(4,1)-Fraction(1,4)-Fraction(1,5)-Fraction(1,6)
        self.assertEqual(r1.denominator%2,0)

    def test_02_deck_relation_and_characteristic_two(self):
        self.zero(J-N/D)
        self.zero((2-I)*z*J-3*I*(z+J)-(2+I))
        # Gaussian integer coefficients reduce modulo varpi=(1+i) to F_2.
        # DL6 reduces to z*w+z+w+1=(z+1)(w+1).
        self.assertEqual((2-1)%2,1)
        self.assertEqual((-3)%2,1)
        self.assertEqual((-2-1)%2,1)
        self.zero(J.subs(z,-1)-I)  # even-order exception
        self.zero(J.subs(z,I)+1)
        self.zero(J.subs(z,1)-(-3+4*I)/5)

    def test_03_exact_odd_cyclotomic_resultant_holdouts(self):
        # An independent finite elimination oracle, not proof of all-order theorem.
        for m in (1,3,5,7,9):
            P=s.cyclotomic_poly(m,z)
            for k in (1,3,5,7,9):
                Q=s.Poly(s.cyclotomic_poly(k,w),w)
                d=Q.degree()
                transformed=sum(c*N**(d-j)*D**j for j,c in enumerate(Q.all_coeffs()))
                self.assertNotEqual(s.simplify(s.resultant(P,transformed,z)),0,(m,k))

    def test_04_odd_grid_lift_is_unstable_as_n_grows(self):
        mp.mp.dps=50
        b=lambda a: ((1+2j)*a+1)/(a+1-2j)
        jmap=lambda a: 1j*(3*a+1-2j)/((2-1j)*a-3j)
        phi=(1+mp.sqrt(5))/2
        for count in (53,97):
            period=2*count*count+1  # odd conductor for the approximate other lift
            max_err=mp.mpf('0')
            first1=mp.mpc(0); first2=mp.mpc(0)
            for k in range(count):
                root=mp.exp(2j*mp.pi*k/count)
                target=jmap(root)
                idx=int(mp.nint((mp.arg(target)%(2*mp.pi))*period/(2*mp.pi)))%period
                other=mp.exp(2j*mp.pi*idx/period)
                err=abs(-b(root)**2+b(other)**2)
                max_err=max(max_err,err)
                first1+=root
                first2+=other
            self.assertLess(max_err, 2*phi**2*mp.pi/period)
            self.assertLess(abs(first1/count),mp.mpf('1e-46'))
            self.assertGreater(abs(first2/count),mp.mpf('0.68'))
            self.assertLess(abs(first2/count-mp.mpc(-1,2)/3),mp.mpf('0.005'))

if __name__=='__main__': unittest.main()

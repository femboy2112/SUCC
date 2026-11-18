"""Sharp radix16 cold-run obstruction and a badly approximable R0 countermodel.

The infinite continued-fraction/badly-approximable theorem for the Kempner
family is cited in the paper note, not inferred from these finite tests.
"""
from fractions import Fraction as F
import unittest

B=16
DELTA=F(1,17)


def torus(x):
    t=F(x)%1
    return min(t,1-t)


def kempner_partial(max_j):
    return sum((F(1,B**(2**j)) for j in range(max_j+1)),F(0))


def kempner_future_sum(j,max_j):
    """Sum fractional phases over [2**j,2**(j+1)) of finite future markers."""
    first=2**j
    geom=F(B**(2*first)-B**first,B-1)
    return geom*sum((F(1,B**(2**k)) for k in range(j+1,max_j+1)),F(0))


def signed_near_zero(t):
    t=F(t)%1
    return t if t<=F(1,2) else t-1


class ColdRunHorizonTests(unittest.TestCase):
    def test_expansion_has_sharp_nonwrapping_threshold(self):
        for x in [F(0),F(1,128),F(-1,128),F(1,300),F(-1,300)]:
            y=signed_near_zero(x)
            if abs(y)<DELTA and torus(16*x)<DELTA:
                self.assertEqual(signed_near_zero(16*x),16*y)
        self.assertEqual(torus(F(1,17)),DELTA)
        self.assertEqual(torus(F(16,17)),DELTA)
        self.assertEqual((16*F(1,17))%1,F(16,17))
        self.assertEqual((16*F(16,17))%1,F(1,17))

    def test_finite_cold_run_forces_exponential_initial_closeness(self):
        for m in (2,4,8,16):
            x=F(1,16**m*100)  # intentionally tiny before its departure
            run=[]; y=x
            for _ in range(m):
                if torus(y)>=DELTA:break
                run.append(torus(y));y=(16*y)%1
            L=len(run)
            self.assertGreaterEqual(L,1)
            self.assertLess(run[0],DELTA/16**(L-1))

    def test_kempner_exact_fractional_phases_during_zero_shell(self):
        for j in range(2,8):
            m=2**j
            x=kempner_partial(j+5)
            for n in range(m,2*m-1):
                self.assertLess(torus(16**n*x),DELTA)
            self.assertGreater(torus(16**(2*m-1)*x),DELTA)

    def test_kempner_critical_shell_mass_uniformly_bounded(self):
        for j in range(1,8):
            S=kempner_future_sum(j,j+5)
            self.assertGreater(S,0)
            self.assertLess(S,F(16,225))
            m=2**j
            self.assertLess(S/m,F(16,225*m))

    def test_sparse_zero_seed_recurrence_has_correct_endpoint(self):
        for m in (2,4,8,16,32):
            u=F(0)
            for n in range(1,m+1):
                u=16*u+(1 if n&(n-1)==0 else 0)
            expected=sum((F(1,16**(2**j)) for j in range(m.bit_length()) if 2**j<=m),F(0))
            self.assertEqual(F(u,16**m),expected)

    def test_one_cold_run_does_not_imply_all_late_shells_cold(self):
        # x=1/(16**m*100) begins arbitrarily near zero but eventually wraps.
        for m in (1,3,6):
            x=F(1,16**m*100)
            self.assertLess(torus(x),DELTA)
            self.assertGreater(torus(16**m*x),0)
            self.assertNotEqual((16**m*x)%1,0)

    def test_no_exact_repetition_for_sparse_irrational_form_is_not_finite_proof(self):
        # Finite prefixes of the sparse expansion are rational. Infinite
        # nonperiodicity and irrationality follow from the exact digit support.
        for j in (2,4,6):
            x=kempner_partial(j)
            self.assertEqual((16**(2**j)*x)%1,0)
            self.assertGreater(kempner_partial(j+1)-x,0)


if __name__=='__main__':unittest.main()

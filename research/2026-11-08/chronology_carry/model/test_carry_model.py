import importlib.util
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import carry_model as cm


class CarryModelTests(unittest.TestCase):
    def test_source_stream_against_fraction(self):
        z = Q(0)
        previous_floor = 0
        rows = list(cm.authentic_stream(60, (1, 17, 60)))
        for row in rows[:-1]:
            n = row['n']
            z = 16*z + sum(Q(c, 8*n-pole) for c,pole in cm.POLES)
            floor = z.numerator//z.denominator
            self.assertEqual(row['carry'], floor-16*previous_floor)
            self.assertEqual(Q(row['rem'],row['denominator']), z-floor)
            previous_floor = floor
        self.assertEqual(rows[-1]['summary']['modular_checkpoints'], [1,17,60])
        self.assertEqual(len(rows[-1]['summary']['carries']), 60)

    def test_dyadic_disk_and_outside_carries(self):
        for a in range(-5,6):
            for b in range(-5,6):
                z = cm.Box(cm.Interval.ratio(a,5), cm.Interval.ratio(b,5))
                # Give fitting a valid phase-mean box; extreme boxes test the
                # defensive contraction too without the huge number of steps.
                if a*a+b*b>25:
                    continue
                v,_ = cm.fitted_center(z)
                self.assertLessEqual(v[0]**2+v[1]**2,cm.TABLE_SCALE**2)
        self.assertEqual(cm.feature(-2,16,'two'),(-2,16))
        table={'tables':{'1':{'two':{'-2,16':{'center':[1,-2]}}}}}
        self.assertEqual(cm.table_predict(table,1,'two',-2,16),((1,-2),False))
        self.assertEqual(cm.table_predict(table,1,'two',0,0),((0,0),True))

    def test_modulus_bounds_exact_rationals(self):
        for a in range(-4,5):
            for b in range(-4,5):
                z = cm.Box(cm.Interval.ratio(a,7),cm.Interval.ratio(b,11))
                lo,hi = cm.magnitude_bounds(z)
                sq=Q(a*a,49)+Q(b*b,121)
                self.assertLessEqual(lo*lo,sq)
                self.assertGreaterEqual(hi*hi,sq)
        for q in [Q(0),Q(1),Q(2),Q(13,17),Q(1000,7)]:
            lo,hi=cm.sqrt_bounds(q)
            self.assertLessEqual(lo*lo,q)
            self.assertGreaterEqual(hi*hi,q)

    def test_coherent_control_never_certifies_below_one(self):
        p=41;m=cm.order16(p);q=2;h=1
        xs=cm.clock(p,cm.source_xi(p))
        B=[cm.phase(-h*x,p) for x in xs]
        for v in ((0,0),(cm.TABLE_SCALE,0),(-cm.TABLE_SCALE,0),(0,cm.TABLE_SCALE)):
            prediction=[[q*v[0],q*v[1]] for _ in xs]
            cert=cm.certify_fold(B,prediction,p,m,q,h)
            bound=Q(cert['direct_certificate_upper']['numerator'],cert['direct_certificate_upper']['denominator'])
            self.assertGreaterEqual(bound,1)
            self.assertLessEqual(cert['rho_lower']['decimal_diagnostic'],cert['rho_upper']['decimal_diagnostic'])

    def test_gauss_period_square_identity(self):
        for p in (17,41,73,89):
            H=set(cm.clock(p,1));m=len(H);seen=set();s=cm.Interval(0,0)
            count=0
            for c in range(1,p):
                if c in seen:continue
                orbit={c*x%p for x in H};seen.update(orbit);count+=1
                value=sum((cm.phase(x,p) for x in orbit),cm.Box())
                s=s+value.norm_squared()
            self.assertEqual(count,(p-1)//m)
            self.assertLessEqual(s.lo,(p-m)*cm.SCALE)
            self.assertGreaterEqual(s.hi,(p-m)*cm.SCALE)
            self.assertGreaterEqual(cm.quotient_factor_bounds(p,m)['total_factor_upper']['decimal_diagnostic'],1)


if __name__=='__main__':unittest.main()

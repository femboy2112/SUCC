"""Independent identities and exact/interval control tests for the cut probe."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    'final_pin_regularized_cut', Path(__file__).with_name('regularized_cut.py'))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
iv = m.iv


def bounds(x):
    return tuple(map(m.dyadic_endpoint, x._mpi_))


def overlap(x, y):
    a, b = bounds(x)
    c, d = bounds(y)
    return max(a, c) <= min(b, d)


def fourier_mean(alpha, Q, r, H=120):
    total = iv.mpf(0)
    for h in range(1, H+1):
        z = iv.pi*h*m.point(Q)
        total -= 2*m.point(r**h)/h*iv.cos(2*iv.pi*h*m.point(alpha)+z)*iv.sin(z)/z
    err = m.point(2*r**(H+1)/((H+1)*(1-r)))
    return total+iv.mpf([-err.b, err.b])


class RegularizedCutTests(unittest.TestCase):
    def test_original_source_and_literal_carries(self):
        values, _ = m.exact_states(41)
        # Independent summation form, not the iterative chronological path.
        for n in range(42):
            expected = sum((16**(n-k)*(
                F(4,8*k-7)-F(2,8*k-4)-F(1,8*k-3)-F(1,8*k-2))
                for k in range(1,n+1)), F())
            self.assertEqual(values[n], (expected, expected))

    def test_mutant_and_rational_seed_are_not_original(self):
        original, _ = m.exact_states(12)
        rational, _ = m.exact_states(12, F(1,5))
        mutant, _ = m.exact_states(12, mutant=True)
        for n in range(13):
            self.assertEqual(rational[n][0]-original[n][0], F(16**n,5))
        self.assertNotEqual(mutant[12][0], original[12][0])

    def test_short_mean_against_independent_fourier_integral(self):
        for alpha in (F(0), F(1,7), F(19,20)):
            for Q in (F(1,16), F(7,4096)):
                observed = m.average_short((alpha,alpha), Q, F(1,2))
                self.assertTrue(overlap(observed, fourier_mean(alpha,Q,F(1,2))))

    def test_cross_boundary_sign_and_integer_period(self):
        states = [(F(0),F(0))]*6
        observed = m.pair_mean(1,2,2,states,F(1,2))
        oracle = fourier_mean(F(0),F(15,16),F(1,2))
        self.assertTrue(overlap(observed,oracle))
        self.assertGreater(bounds(observed)[0],0)
        self.assertEqual(bounds(m.pair_mean(2,3,2,states,F(1,2))),(F(0),F(0)))

    def test_root_grid_energy_product_identity(self):
        A=11
        states=[(F(n,A),F(n,A)) for n in range(2*A)]
        for r in (F(1,2),F(3,4)):
            ri=m.point(r)
            exact=(iv.log(1-ri**A)-iv.log(1-ri))/A
            self.assertTrue(overlap(m.energy(A,states,r),exact))

    def test_all_coincident_energy(self):
        A=13
        states=[(F(0),F(0))]*(2*A)
        exact=m.point(F(A-1,A))*iv.log(iv.mpf(1)/2)
        self.assertTrue(overlap(m.energy(A,states,F(1,2)),exact))

    def test_green_enclosure_is_nested(self):
        for n in (0,17,53):
            a,b=m.green(n,12)
            c,d=m.green(n,24)
            self.assertLess(a,c)
            self.assertLess(d,b)
        self.assertEqual((16**5-1)%m.periodic_beta().denominator,0)
        self.assertEqual((16**5*m.periodic_beta()-m.periodic_beta())%1,0)

    def test_finite_cut_transport_control(self):
        A=9
        states,_=m.exact_states(2*A-1)
        r=F(1,2)
        E=m.energy(A,states,r)
        P=sum(m.pressure(A,2*A,states,r).values())
        lip=4*iv.pi*m.point(r)/(1-m.point(r))
        self.assertLess(max(abs(v) for v in bounds(P-E)),bounds(lip/(30*A))[1])


if __name__=='__main__':
    unittest.main()

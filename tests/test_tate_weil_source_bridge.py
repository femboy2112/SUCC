"""Tate source fingerprints / completed log derivatives, with negative controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.tate_weil_source_bridge import (
    TateWeilBridgeError, TateWeilProfile,
    finite_log_derivative_tape, finite_completed_log_derivative,
    analytic_source_tail_bound,
)


class TateWeilProfileTests(unittest.TestCase):
    def test_exact_profiles_and_ramified_gauss(self):
        z = TateWeilProfile.canonical('zeta')
        c = TateWeilProfile.canonical('chi_minus_3')
        self.assertEqual((z.conductor,z.parity,z.root_number,z.has_completed_poles,z.half_density), (1,0,1,True,Q(1,2)))
        self.assertEqual((c.conductor,c.parity,c.root_number,c.has_completed_poles,c.half_density), (3,1,1,False,Q(1,2)))
        self.assertIsNone(z.local_ramified_gauss())
        self.assertEqual(c.local_ramified_gauss().norm(), 3)

    def test_altered_pole_phase_conductor_parity_and_half_density_rejected(self):
        correct = TateWeilProfile.canonical('chi_minus_3')
        for index, bad in [(0,1),(1,0),(2,-1),(3,True),(4,Q(1))]:
            params=[correct.conductor,correct.parity,correct.root_number,correct.has_completed_poles,correct.half_density]
            params[index] = bad
            with self.subTest(index=index), self.assertRaises(TateWeilBridgeError):
                TateWeilProfile(correct.kind,*params)
        with self.assertRaises(TateWeilBridgeError):
            TateWeilProfile.canonical('fake6')
        with self.assertRaises(TateWeilBridgeError):
            TateWeilProfile('zeta',True,0,1,True,Q(1,2))

    def test_source_atoms_are_only_authentic_prime_powers(self):
        z=TateWeilProfile.canonical('zeta')
        c=TateWeilProfile.canonical('chi_minus_3')
        self.assertEqual(finite_log_derivative_tape(12,z), ((2,2,1),(3,3,1),(4,2,1),(5,5,1),(7,7,1),(8,2,1),(9,3,1),(11,11,1)))
        self.assertEqual(finite_log_derivative_tape(12,c), ((2,2,-1),(4,2,1),(5,5,-1),(7,7,1),(8,2,-1),(11,11,-1)))
        self.assertNotIn(6, (n for n,_,_ in finite_log_derivative_tape(100,c)))
        for bad in (None,'zeta'):
            with self.assertRaises(TateWeilBridgeError):
                finite_log_derivative_tape(12,bad)
        for bad in (0,1,6.5,True):
            with self.assertRaises(TateWeilBridgeError):
                finite_log_derivative_tape(bad,z)

    def test_independent_original_zeta_log_derivative(self):
        from observational_succ.completed_weil_transport import independent_xi_logderivative
        import mpmath as mp
        prof=TateWeilProfile.canonical('zeta')
        for s in (mp.mpc('2.5','0.5'),mp.mpc('3','1.25')):
            N=1200
            actual=finite_completed_log_derivative(s,N,prof,70)
            oracle=independent_xi_logderivative(s)
            upper=analytic_source_tail_bound(s.real,N,prof)
            self.assertLess(abs(actual-oracle),upper)
            self.assertLess(abs(actual-oracle),mp.mpf('0.002'))

    def test_independent_primitive_chi3_log_derivative(self):
        import mpmath as mp
        prof=TateWeilProfile.canonical('chi_minus_3')
        for s in (mp.mpc('2.5','0.3'),mp.mpc('3','1.5')):
            N=1200
            actual=finite_completed_log_derivative(s,N,prof,70)
            mp.mp.dps=70
            L=lambda z:mp.power(3,-z)*(mp.zeta(z,mp.mpf(1)/3)-mp.zeta(z,mp.mpf(2)/3))
            oracle=mp.log(3/mp.pi)+mp.digamma((s+1)/2)+2*mp.diff(L,s)/L(s)
            upper=analytic_source_tail_bound(s.real,N,prof)
            self.assertLess(abs(actual-oracle),upper)
            self.assertLess(abs(actual-oracle),mp.mpf('0.002'))
            # Directly mutating conductor/parity erases an O(1) Gamma signature.
            wrong=actual+mp.digamma(s/2)-mp.digamma((s+1)/2)
            self.assertGreater(abs(wrong-oracle),upper)

    def test_no_fake_positivity_and_source_domain(self):
        z=TateWeilProfile.canonical('zeta')
        c=TateWeilProfile.canonical('chi_minus_3')
        self.assertEqual(finite_log_derivative_tape(2,c),((2,2,-1),))
        for profile in (z,c):
            for s in (1,0,0.75,-2):
                with self.assertRaises(TateWeilBridgeError):
                    finite_completed_log_derivative(s,100,profile)
        with self.assertRaises(TateWeilBridgeError):
            analytic_source_tail_bound(2,2,c)

if __name__ == '__main__':
    unittest.main()

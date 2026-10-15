"""Exact spectral-mode tests and source-countermodel mutation controls."""
import itertools
import math
import unittest
from fractions import Fraction as Q
from observational_succ.scalar_circle_spectral import (
    CircleScalar,SpectralSourceError,poisson_theta_direct,poisson_theta_dual,
    massless_zeta_tail_bound,
)


class TestPhysicalStyleCircleCarrier(unittest.TestCase):
    def test_periodic_mode_source(self):
        w=CircleScalar('toy',0,Q(2),Q(3))
        self.assertEqual(tuple(w.eigenvalue(n) for n in range(-3,4)),
                         (Q(29),Q(14),Q(5),Q(2),Q(5),Q(14),Q(29)))

    def test_massless_zeta2s_equals_mode_sum_at_every_finite_cutoff(self):
        zero=CircleScalar('toy',0,Q(0),Q(1,3))
        for s,n in itertools.product((1,2,3),(1,2,3,8,15)):
            self.assertEqual(zero.truncated_spectral_zeta(s,n,nonzero_modes_only=True),
                             zero.massless_dirichlet_truncation(s,n))

    def test_zero_mode_mutant_must_not_be_hidden(self):
        zero=CircleScalar('toy',0,Q(0),Q(1))
        with self.assertRaises(SpectralSourceError):
            zero.truncated_spectral_zeta(2,8)
        self.assertEqual(zero.truncated_spectral_zeta(2,0,nonzero_modes_only=True),Q(0))
        massive=CircleScalar('toy',0,Q(1),Q(1))
        self.assertEqual(massive.truncated_spectral_zeta(1,0),Q(1))

    def test_massive_mode_weights_fail_multiplicativity_exactly(self):
        for m,a in itertools.product((Q(0),Q(1,2),Q(1),Q(3),Q(17,5)),
                                     (Q(1),Q(2),Q(1,3))):
            world=CircleScalar('toy',0,m,a)
            c=m/a
            self.assertEqual(world.multiplicative_two_three_defect(),
                             -Q(24)*c/(1+c)**2)
            if m>0:
                self.assertLess(world.multiplicative_two_three_defect(),0)
            else:
                self.assertEqual(world.multiplicative_two_three_defect(),0)

    def test_massive_world_cannot_forge_massless_zeta_claim(self):
        m=CircleScalar('toy',0,Q(1),Q(1))
        with self.assertRaises(SpectralSourceError):
            m.massless_dirichlet_truncation(2,5)
        zero=CircleScalar('toy',0,Q(0),Q(1))
        self.assertNotEqual(m.truncated_spectral_zeta(2,5,nonzero_modes_only=True),
                            zero.truncated_spectral_zeta(2,5,nonzero_modes_only=True))

    def test_high_energy_mass_can_be_arbitrarily_hard_to_resolve_relatively(self):
        mass=CircleScalar('toy',0,Q(7),Q(3))
        for n in (1,2,3,7,31,100,1000):
            self.assertEqual(mass.relative_mass_perturbation(n),Q(7,3*n*n))
        self.assertLess(mass.relative_mass_perturbation(1000),Q(1,100000))

    def test_zeta_tail_includes_actual_known_value(self):
        zero=CircleScalar('toy',0,Q(0),Q(1))
        # Numerical independent benchmark pi^2/3 = 2*zeta(2); the rigorous
        # tail bound is checked against the benchmark, not treated as proof.
        for N in (5,25,100):
            truncated=zero.truncated_spectral_zeta(1,N,nonzero_modes_only=True)
            error=massless_zeta_tail_bound(1,N)
            self.assertLess(float(truncated),math.pi**2/3)
            self.assertGreater(float(truncated+error),math.pi**2/3)
        with self.assertRaises(SpectralSourceError):
            massless_zeta_tail_bound(1,0)

    def test_heat_kernel_poisson_duality_numeric_crosscheck(self):
        # Analytic Poisson identity is proved separately; these are diagnostics.
        for t,alpha,N in ((1.0,1.0,12),(0.5,1.0,15),(2.0,1.0,12),
                          (0.25,2.0,18),(1.0,0.5,18)):
            self.assertAlmostEqual(poisson_theta_direct(t,alpha,N),
                                   poisson_theta_dual(t,alpha,N),places=12)
        self.assertNotEqual(poisson_theta_direct(1.,1.,1),
                            poisson_theta_dual(1.,1.,1))

    def test_malformed_source_guard(self):
        with self.assertRaises(SpectralSourceError):
            CircleScalar('x',0,Q(0),Q(0))
        with self.assertRaises(SpectralSourceError):
            CircleScalar('x',0,0.1,Q(1))
        with self.assertRaises(SpectralSourceError):
            CircleScalar('x',-1,Q(1),Q(1))


if __name__=='__main__':
    unittest.main()

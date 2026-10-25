"""Exact rational controls and separate numerical diagnostics for EAB claims.

The classical identities (DLMF, Basel, Tate/Poisson, PNT) are paper imports.
Finite sampling does not prove an analytic theorem, RH, or pi normality.
"""
from __future__ import annotations

import math
import unittest
from fractions import Fraction as Q

from observational_succ.generalized_euler_adelic import (
    GeneralizedEulerError, analytically_continued_zero_power,
    cell_certificate, cell_defect_exact, clock_gamma_diagnostic, clock_jump,
    cofinal_prime_schedule, continued_gamma, euler_product_exact,
    finite_hurwitz_mesh, finite_succ_defect, hurwitz_mesh_limit,
    literal_zero_power, positive_type_hostile_zero, prime_euler_diagnostic,
    primes_through, theta_balanced_completed, theta_balanced_integral,
    pi_squared_from_cells, certified_pi_hex_prefix,
    symmetric_functional_equation_mutant,
)


class GeneralizedEulerAdelicTests(unittest.TestCase):
    def test_rational_cells_and_exact_bounds(self):
        self.assertEqual(cell_defect_exact(2,1),Q(1,2))
        self.assertEqual(cell_defect_exact(2,2),Q(1,12))
        self.assertEqual(cell_defect_exact(2,3),Q(1,36))
        self.assertEqual(cell_defect_exact(0,19),Q(0))
        with self.assertRaises(GeneralizedEulerError):
            cell_defect_exact(1,1)
        for power in (2,3,4,5):
            older=None
            for cutoff in (1,2,4,7,16,32):
                cert=cell_certificate(power,cutoff)
                self.assertGreater(cert.lower,0)
                self.assertLess(cert.lower,cert.upper)
                self.assertEqual(cert.upper-cert.lower,Q(1,2*cutoff**power))
                if older is not None:
                    self.assertGreater(cert.lower,older.lower)
                    self.assertLess(cert.upper,older.upper)
                older=cert

    def test_exact_zero_power_mutation_and_domain(self):
        for n in (1,2,7,113):
            self.assertEqual(literal_zero_power(n),1)
        self.assertEqual(analytically_continued_zero_power(),Q(1,2))
        self.assertNotEqual(literal_zero_power(10),analytically_continued_zero_power())
        with self.assertRaises(GeneralizedEulerError):
            cell_certificate(1,3)
        with self.assertRaises(GeneralizedEulerError):
            cell_certificate(3,0)

    def test_original_succ_complex_half_plane_and_one(self):
        import mpmath as mp
        with mp.workdps(60):
            for s in (mp.mpf('0.4'),mp.mpf('1'),mp.mpf('1.5'),mp.mpc('0.8','0.3')):
                n=300
                observed=finite_succ_defect(s,n,65)
                analytic=continued_gamma(s,65)
                remainder=observed-analytic-mp.power(n,-s)/2
                # Rigorous centered-sawtooth tail bound from integrating cells.
                ceiling=(abs(s*(s+1))/4*
                         (n**(-mp.re(s)-2)+n**(-mp.re(s)-1)/(mp.re(s)+1)))
                self.assertLess(abs(remainder),ceiling)
            self.assertLess(abs(continued_gamma(1,65)-mp.euler),mp.mpf('1e-58'))
            self.assertLess(abs(continued_gamma(0,65)-mp.mpf('0.5')),mp.mpf('1e-58'))

    def test_hurwitz_gauge_deformation(self):
        import mpmath as mp
        with mp.workdps(60):
            self.assertLess(abs(hurwitz_mesh_limit(1,1,1,65)-mp.euler),mp.mpf('1e-55'))
            self.assertLess(abs(hurwitz_mesh_limit(1,1,2,65)-mp.euler/2),mp.mpf('1e-55'))
            self.assertLess(abs(hurwitz_mesh_limit(1,2,1,65)-(mp.euler-1+mp.log(2))),
                            mp.mpf('1e-55'))
            self.assertGreater(abs(hurwitz_mesh_limit(1,2,1,65)-mp.euler),mp.mpf('0.2'))
            for s in (mp.mpf('0.75'),mp.mpf('1'),mp.mpc('1.3','0.2')):
                finite=finite_hurwitz_mesh(s,2,mp.mpf('1.25'),500,65)
                complete=hurwitz_mesh_limit(s,2,mp.mpf('1.25'),65)
                self.assertLess(abs(finite-complete),mp.mpf('0.08'))
            with self.assertRaises(GeneralizedEulerError):
                hurwitz_mesh_limit(1,0,1)
            with self.assertRaises(GeneralizedEulerError):
                finite_hurwitz_mesh(1,1,0,50)

    def test_prime_source_not_composite_and_exact_tail(self):
        self.assertEqual(primes_through(13),(2,3,5,7,11,13))
        self.assertEqual(euler_product_exact(2,5),Q(25,16))
        self.assertEqual(euler_product_exact(2,5,fake_composite=6),Q(45,28))
        with self.assertRaises(GeneralizedEulerError):
            euler_product_exact(2,5,fake_composite=5)
        import mpmath as mp
        for power in (2,3,4):
            with mp.workdps(65):
                for cutoff in (5,10,30):
                    P=euler_product_exact(power,cutoff)
                    pf=mp.mpf(P.numerator)/P.denominator
                    missing=mp.zeta(power)-pf
                    bound=mp.power(cutoff,1-power)/(power-1)
                    self.assertGreater(missing,0)
                    self.assertLess(missing,bound)

    def test_cofinal_diagonal_has_rigorous_symbolic_cutoff(self):
        import mpmath as mp
        for q in (2,3,4,5,6):
            d=cofinal_prime_schedule(q)
            self.assertEqual(d.cutoff,q**(2*q))
            self.assertEqual(d.epsilon,Q(1,q))
            self.assertEqual(d.proved_absolute_euler_error_leq,Q(1,q))
        with mp.workdps(50):
            for q in (2,3,4):
                d=cofinal_prime_schedule(q)
                s=1+mp.mpf(1)/q
                P=prime_euler_diagnostic(s,d.cutoff,50)
                missing=mp.re(mp.zeta(s)-P)
                self.assertGreater(missing,0)
                self.assertLess(missing,mp.mpf(1)/q)
            with self.assertRaises(GeneralizedEulerError):
                prime_euler_diagnostic(1,7)

    def test_prime_limit_noncommutes_with_pole_subtraction(self):
        import mpmath as mp
        with mp.workdps(60):
            values=[]
            for q in (10,20,40,80):
                z=1+mp.mpf(1)/q
                values.append(mp.re(prime_euler_diagnostic(z,7,65)-q))
            self.assertTrue(all(values[i]>values[i+1] for i in range(3)))
            self.assertLess(values[-1],-70)
            self.assertLess(abs(continued_gamma(1,65)-mp.euler),mp.mpf('1e-55'))

    def test_theta_entire_self_dual_completion_diagnostic(self):
        import mpmath as mp
        with mp.workdps(50):
            for s in (mp.mpf('2'),mp.mpf('1'),mp.mpf('0'),mp.mpc('.42','.31')):
                direct=theta_balanced_integral(s,8,65)
                completed=theta_balanced_completed(s,65)
                reflected=theta_balanced_integral(1-s,8,65)
                self.assertLess(abs(direct-completed),mp.mpf('1e-45'))
                self.assertLess(abs(direct-reflected),mp.mpf('1e-45'))
            self.assertGreater(theta_balanced_integral(mp.mpf('0.5'),8,65).real,0)
            self.assertLess(abs(theta_balanced_completed(1,65)-
                (1+mp.euler/2-mp.log(2*mp.sqrt(mp.pi)))),mp.mpf('1e-45'))

    def test_positive_definite_does_not_force_zero_location(self):
        import mpmath as mp
        with mp.workdps(60):
            probe=positive_type_hostile_zero(65)
            self.assertGreater(abs(mp.im(probe['zero'])),1)
            self.assertLess(abs(probe['residual']),mp.mpf('1e-55'))
            for x in (0,mp.pi/2,mp.pi,2*mp.pi):
                self.assertGreater(2+mp.cos(x),0)
            # Exact Gram: 2+cos(t-u)=2+cos(t)cos(u)+sin(t)sin(u).

    def test_pi_base16_prefix_certified_from_rational_succ_cells(self):
        self.assertEqual(certified_pi_hex_prefix(10,1),"3.2")
        self.assertEqual(certified_pi_hex_prefix(50,3),"3.243")
        self.assertIsNone(certified_pi_hex_prefix(50,4))
        self.assertEqual(certified_pi_hex_prefix(300,4),"3.243F")
        lo,hi=pi_squared_from_cells(50)
        self.assertGreater(lo,Q(9))
        self.assertEqual(hi-lo,Q(3,50**2))
        with self.assertRaises(GeneralizedEulerError):
            certified_pi_hex_prefix(50,0)

    def test_even_functional_equation_is_not_authentic_prime_source(self):
        for s in (Q(0),Q(1,4),Q(1,2),Q(2,3),Q(1),Q(2)):
            self.assertEqual(symmetric_functional_equation_mutant(s),
                             symmetric_functional_equation_mutant(1-s))
        self.assertEqual(symmetric_functional_equation_mutant(Q(0)),1)
        self.assertEqual(symmetric_functional_equation_mutant(Q(1)),1)
        self.assertNotEqual(symmetric_functional_equation_mutant(Q(2)),1)
        with self.assertRaises(GeneralizedEulerError):
            symmetric_functional_equation_mutant(0.5)

    def test_prime_power_clock_crossover(self):
        for primepower,prime in ((2,2),(3,3),(4,2),(8,2),(9,3),
                                 (16,2),(25,5),(27,3),(49,7),(64,2)):
            self.assertEqual(clock_jump(primepower),prime)
        for nonpower in (6,10,12,14,15,18,20,30):
            self.assertEqual(clock_jump(nonpower),1)
        self.assertLess(abs(clock_gamma_diagnostic(200)-0.5772156649015329),0.15)


if __name__=="__main__":
    unittest.main()

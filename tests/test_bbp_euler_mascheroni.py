"""Exact rational and independent analytic tests for BBP Euler–Mascheroni jets."""
from __future__ import annotations

import math
import unittest
from fractions import Fraction as F

from observational_succ.bbp_euler_mascheroni import (
    POLES, forcing, block_source, blocking_coefficients, block_laplace_mass,
    source_endpoint_jets, mellin_first_jet_coefficient, bbp_gamma_log_argument,
    bbp_gamma_deformation, blocked_free_energy, prime_factorization, valuation,
    log_linear_prime_coefficients, mellin_gamma_correction, q_lambert_partial,
    q_lambert_tail_bound, divisor_count, divisor_lambert_partial,
    multiplicative_order_16, q_block_polynomial,
)
from observational_succ.duck_bbp import forcing as frozen_forcing


class BBPEulerMascheroni(unittest.TestCase):
    def test_frozen_four_signed_poles(self):
        for n in range(1,301):
            self.assertEqual(forcing(n), frozen_forcing(n))
            self.assertGreater(forcing(n), 0)

    def test_original_source_four_pole_jet(self):
        self.assertEqual(sum(w for d,w in POLES), 0)
        self.assertEqual(-sum(w*d for d,w in POLES),15)
        self.assertEqual(sum(w*d*d for d,w in POLES),-59)
        self.assertEqual(-sum(w*d**3 for d,w in POLES),243)

    def test_laplace_block_equals_true_source(self):
        for g in (1,2,3,4,5,8,12):
            for k in (1,2,3,10):
                a=8*g*(k-1)+1
                self.assertEqual(block_laplace_mass(g,a),block_source(g,k))

    def test_block_grouping_two_levels(self):
        for g,h,k in ((2,3,1),(3,2,4),(4,3,2),(1,8,5)):
            step=block_source(g*h,k)
            regroup=sum((16**(g*(h-j))*block_source(g,h*(k-1)+j)
                        for j in range(1,h+1)),F())
            self.assertEqual(step,regroup)

    def test_block_polynomial_q_factor_and_composition(self):
        for g in (1,2,3,5,8):
            for t in (F(0),F(1,2),F(1)):
                B=q_block_polynomial(g,t)
                self.assertEqual(B,F(16**g-t**g,16-t))
                self.assertEqual(B,16**(g-1)*sum((F(t,16)**j for j in range(g)),F()))
        for g,h,t in ((2,3,F(1,4)),(3,4,F(1)),(7,2,F(1,2))):
            self.assertEqual(q_block_polynomial(g+h,t),16**h*q_block_polynomial(g,t)+t**g*q_block_polynomial(h,t))

    def test_exact_endpoint_jets_independent_exponential_oracle(self):
        for g in (1,2,3,5,8,16):
            deriv1=sum(16**(g-1-j)*sum(-w*(8*j+d) for d,w in POLES)
                       for j in range(g))
            deriv2=sum(16**(g-1-j)*sum(w*(8*j+d)**2 for d,w in POLES)
                       for j in range(g))
            self.assertEqual(source_endpoint_jets(g),(deriv1,deriv2))
            self.assertEqual(deriv1,16**g-1)

    def test_source_specific_first_mellin_jet(self):
        self.assertEqual(mellin_first_jet_coefficient(1),F(59,30))
        self.assertEqual(mellin_first_jet_coefficient(2),F(1243,510))
        for g in (1,2,3,5,8,12,16):
            self.assertEqual(mellin_first_jet_coefficient(g),F(5,2)-F(8*g,16**g-1))
            self.assertLess(mellin_first_jet_coefficient(g),F(5,2))

    def test_mellin_closed_rational_prime_logs(self):
        self.assertEqual(log_linear_prime_coefficients(1,1),{
            2:-F(35,94),3:-F(5,94),5:-F(3,47)})
        for g in (1,2,8):
            co=log_linear_prime_coefficients(g,1)
            self.assertTrue(co)
            self.assertTrue(all(c!=0 for c in co.values()))
            value=1+sum(float(c)*math.log(p) for p,c in co.items())
            self.assertAlmostEqual(value,mellin_gamma_correction(g,1),places=10)
        self.assertIn(31,log_linear_prime_coefficients(8,1))
        self.assertNotIn(31,log_linear_prime_coefficients(7,1))
        R=block_source(8)
        self.assertEqual(log_linear_prime_coefficients(8,1)[31],-F(1,62)/R)

    def test_mellin_first_jet_against_independent_quad(self):
        # High-precision quadrature is independent of logarithm-of-rationals oracle.
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest('mpmath not installed; rational tests still execute')
        with mp.workdps(45):
            for g,a in ((1,17),(2,30),(8,40)):
                aa=mp.mpf(a)
                f=lambda y: mp.exp(-y)*(4-2*mp.exp(-3*y/aa)-mp.exp(-4*y/aa)-mp.exp(-5*y/aa))*sum(mp.mpf(16)**(g-1-j)*mp.exp(-8*j*y/aa) for j in range(g))
                mass=mp.quad(f,[0,1,3,10,40,160])
                logmass=mp.quad(lambda y:f(y)*mp.log(y),[0,1,3,10,40,160])
                measured=1-(logmass/mass)-mp.euler
                self.assertLess(abs(measured-mellin_gamma_correction(g,a)),mp.mpf('1e-11'))

    def test_source_finite_part_formula_and_growing_block_bound(self):
        gamma=0.5772156649015328606
        for g in (1,2,3,5,8):
            C=bbp_gamma_log_argument(g)
            v=blocked_free_energy(g,256)
            want=math.log(float(C))+2*math.log(g)-2*gamma
            self.assertLess(abs(v-want),0.03)
        self.assertEqual(bbp_gamma_log_argument(1),F(3008,225))
        vals=[bbp_gamma_log_argument(g) for g in range(1,12)]
        self.assertTrue(all(vals[j]>vals[j+1] for j in range(len(vals)-1)))
        self.assertTrue(all(bbp_gamma_deformation(g)<0 for g in (1,2,5,8)))

    def test_bbp_27_and_31_are_real_denominator_births(self):
        self.assertEqual(forcing(7),F(5273,911547))
        self.assertEqual(forcing(8),F(776,179645))
        self.assertEqual(valuation(forcing(7),3),-3)
        self.assertEqual(valuation(forcing(8),31),-1)
        for n in range(1,7):self.assertGreaterEqual(valuation(forcing(n),3),-2)
        for n in range(1,8):self.assertGreaterEqual(valuation(forcing(n),31),0)
        self.assertEqual(valuation(block_source(8),3),-3)
        self.assertEqual(valuation(block_source(8),31),-1)
        self.assertEqual(valuation(bbp_gamma_log_argument(8),3),-4)
        self.assertEqual(valuation(bbp_gamma_log_argument(8),31),-1)

    def test_complete_block_eight_rational_and_prime_factors(self):
        self.assertEqual(block_source(8),F(130649266880774398385420101096,154923473562396513975))
        self.assertEqual(bbp_gamma_log_argument(8),
                         F(8361553080369561496666886470144,665391252178290169344635447625))
        fac=prime_factorization(bbp_gamma_log_argument(8).denominator)
        self.assertEqual(fac[3],4)
        self.assertEqual(fac[31],1)
        self.assertIn(257,fac)
        self.assertIn(65537,fac)

    def test_critical_other_prime_clocks_not_confused(self):
        self.assertEqual(multiplicative_order_16(31),5)
        self.assertEqual(multiplicative_order_16(27),9)
        self.assertEqual(multiplicative_order_16(3),1)
        for n in range(1,5):self.assertNotEqual(pow(16,n,31),1)
        for n in range(1,9):self.assertNotEqual(pow(16,n,27),1)

    def test_q_euler_vs_its_actual_derivative(self):
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest('mpmath not installed')
        with mp.workdps(50):
            q=mp.mpf(1)/16
            val=mp.log(1-q)+mp.log(16)*sum(mp.mpf(1)/(mp.power(16,n)-1) for n in range(1,45))
            independent=-mp.diff(lambda z:mp.log(mp.qgamma(z,q)),1)
            self.assertLess(abs(val-independent),mp.mpf('1e-45'))
            self.assertLess(abs(val-mp.mpf('0.1318958182223980194674209652162561372746504')),mp.mpf('1e-40'))

    def test_lambert_tail_rational_cert(self):
        for m in (1,2,4,8,16):
            prefix=q_lambert_partial(m)
            post=q_lambert_partial(m+25)-prefix
            self.assertGreater(post,0)
            self.assertLess(post,q_lambert_tail_bound(m))

    def test_divisor_lambert_product_identity_finite(self):
        for M in (1,3,5,15,25,31):
            exact=sum((sum((F(1,16**(n*j)) for j in range(1,M//n+1)),F())
                       for n in range(1,M+1)),F())
            self.assertEqual(exact,divisor_lambert_partial(M))
        self.assertEqual(divisor_count(27),4)
        self.assertEqual(divisor_count(31),2)
        self.assertEqual(divisor_count(16),5)

    def test_qgamma_universal_versus_source_mellin(self):
        # A two-pole source Q*=1-exp(-x) has the SAME q blocking multiplier,
        # but normalized Mellin first jet differs by exactly 44/30 at g=1.
        for g in (1,2,5,8):
            coeff=blocking_coefficients(g)
            s0=sum(coeff);s1=sum(j*x for j,x in enumerate(coeff))
            two_pole=F(s0+16*s1,2*s0)
            self.assertEqual(mellin_first_jet_coefficient(g)-two_pole,F(22,15))
            self.assertEqual(q_block_polynomial(g,F(1,2)),
                             sum((coeff[j]*F(1,2)**j for j in range(g)),F()))

    def test_exact_receipt_replay(self):
        import importlib.util
        import json
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        source=root/"research/2026-11-09/bbp_euler_mascheroni/experiment.py"
        spec=importlib.util.spec_from_file_location("bbp_euler_exact_receipt",source)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        recorded=json.loads((source.parent/"FINITE_RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(module.exact_receipt(),recorded)

    def test_invalid_ranges(self):
        for fn,args in ((forcing,(0,)),(block_source,(0,)),
                        (block_laplace_mass,(2,0)),(source_endpoint_jets,(-1,)),
                        (bbp_gamma_log_argument,(0,)),(q_lambert_partial,(-1,)),
                        (multiplicative_order_16,(32,)),(log_linear_prime_coefficients,(1,0))):
            with self.assertRaises(ValueError):fn(*args)

if __name__=='__main__':unittest.main()

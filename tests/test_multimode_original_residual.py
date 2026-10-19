"""Exact original four-Schur high multimode response, with negative controls."""
import unittest
from fractions import Fraction as F
from observational_succ import multimode_original_residual as M
from observational_succ import original_continuum_residual as R
from observational_succ import clamped_k_residual_bridge as B


class ExactSourceClampedHighBasis(unittest.TestCase):
    def test_basis_geometric_endpoint_and_low_moment_constraints(self):
        for i in (1,2,3,4):
            for j in (0,1,2):
                p=M.correction_primitive(i,j)
                h=p["primitive"]
                self.assertTrue(all(B.value(x,y)==0 for x in (h,B.derivative(h))
                                    for y in (-F(1,2),F(1,2))))
                self.assertTrue(all(B.integral_product(B.derivative(h),B.legendre(k))==0
                                    for k in (1,2,3,4)))
                self.assertGreater(R.norm_squared(h),0)
                self.assertEqual(p["indices"][0][0]+2,p["indices"][1][0])

    def test_independent_exact_spd_inverse_model(self):
        self.assertEqual(M._solve_spd_exact(((F(2),F(1)),(F(1),F(3))),
                    (F(1),F(2))),(F(1,5),F(3,5)))
        with self.assertRaises(M.MultiResidualError):
            M._solve_spd_exact(((1,2),(2,1)),(1,1))
        with self.assertRaises(M.MultiResidualError):
            M._solve_spd_exact(((1,1),(1,1)),(1,1))

    def test_all_high_response_traces_stay_original_clamped(self):
        for i in range(1,5):
            basis=[M.correction_primitive(i,t) for t in (0,1,2)]
            h,c=M._construct_h(i,(F(1,8),-F(1,7),F(1,12)),basis)
            self.assertEqual(B.value(h,F(1,2)),0)
            self.assertEqual(B.value(B.derivative(h),-F(1,2)),0)
            self.assertEqual(c[0][0],i)
            self.assertEqual(c[0][1],1)

    def test_untyped_modes_not_silently_introduced(self):
        for i,n in ((0,1),(5,1),(1,5),(True,0),(2,-1)):
            with self.assertRaises(M.MultiResidualError):
                M.correction_primitive(i,n)
        with self.assertRaises(M.MultiResidualError):
            M.original_multimode_source_schur(count=0)
        with self.assertRaises(M.MultiResidualError):
            M.original_multimode_source_schur(count=1,J=0)
        with self.assertRaises(M.MultiResidualError):
            M.original_multimode_source_schur(count=1,eta=0)


class RealFrozenSuzukiSource(unittest.TestCase):
    def test_source_authentic_entire_continuum_high_with_two_correctors(self):
        x=M.original_multimode_source_schur(count=2,J=8,M=80,eta=F(1,4))
        self.assertEqual(x["source_sha"],R.SOURCE_SHA)
        self.assertEqual(x["original_first_prime_wavefront"],((2,2),))
        self.assertTrue(x["frozen_source_signed_contact_poles_and_prime2"])
        self.assertTrue(x["actual_full_continuum_L2_residual_certified"])
        self.assertTrue(x["all_original_high_Q4_boundary_traces_valid"])
        self.assertFalse(x["RH_proved"])
        for sector,block in x["parity_schur_blocks"].items():
            self.assertEqual(len(block["optimal_clamped_correction_coefficients"]),2)
            self.assertEqual(len(block["optimal_clamped_correction_coefficients"][0]),2)
            self.assertTrue(all(F(v)>=0 for v in block["real_Gamma_tail_errors"]))
            self.assertFalse(x["original_first_window_S4_certified_positive"]
                         and not all(z["S4_lower_PSD_certified"]
                             for z in x["parity_schur_blocks"].values()))


if __name__=="__main__":
    unittest.main()

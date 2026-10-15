"""Exact rational Suzuki low-block interaction tests, original-source if installed.

Pure polynomial tests are independent of transcendentals. The only routines
allowed to certify original Gamma/prime/pole intervals replay the pinned
#85 file hash. A locally missing parent is an explicit scoped skip; in CI
there is a FAIL-CLOSED mandatory source step with the parent present.
"""
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_moment_schur import SchurSourceError,low_inverse_neumann,low_gram
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial, poly_add, poly_mul, poly_eval, poly_integral,
    poly_derivative,poly_primitive_zero_at_left, exp_antiderivative_poly,
    source_ou_pair_affine, poly_two_variable_cross,
    prime_hinge_integral_polynomial, authentic_full_low_entry,
    authentic_direct_low_matrix, authentic_gamma_low_entry,
    authentic_pole_low_entry,authentic_first_prime_low_entry,
    source_low_entry_gamma_prime_contact,
)


class AuthenticLegendreLowTests(unittest.TestCase):
    a=Q(1,2)
    def test_exact_legendre_polynomials(self):
        assert legendre_polynomial(1,self.a)==(0,2)
        assert legendre_polynomial(2,self.a)==(-Q(1,2),0,6)
        assert legendre_polynomial(3,self.a)==(0,-3,0,20)

    def test_parity_and_orthogonality(self):
        for i in range(31):
            p=legendre_polynomial(i,self.a)
            assert all((j-i)%2==0 or v==0 for j,v in enumerate(p))
            assert poly_eval(p,self.a)==1 and poly_eval(p,-self.a)==(-1)**i
        for i in range(1,8):
            for j in range(1,8):
                val=poly_integral(poly_mul(legendre_polynomial(i,self.a),legendre_polynomial(j,self.a)),-self.a,self.a)
                assert val==(Q(1,2*i+1) if i==j else 0)

    def test_poly_primitive_correct_boundary(self):
        for k in range(1,10):
            p=legendre_polynomial(k,self.a)
            f=poly_primitive_zero_at_left(p,self.a)
            assert poly_eval(f,-self.a)==poly_eval(f,self.a)==0
            assert poly_derivative(f)==p

    def test_ou_affine_known_exact_values(self):
        assert source_ou_pair_affine(1,1,self.a,Q(1,2))==(Q(364,3),Q(-200))
        assert source_ou_pair_affine(1,3,self.a,Q(1,2))==(Q(29720),Q(-49000))
        assert source_ou_pair_affine(2,2,self.a,Q(1,2))==(-Q(90276,5),Q(29768))

    def test_ou_affine_source_is_symmetric(self):
        for alpha in (Q(1,2),Q(5,2),Q(17,2)):
            for i in range(1,6):
                for j in range(i,6):
                    assert source_ou_pair_affine(i,j,self.a,alpha)==source_ou_pair_affine(j,i,self.a,alpha)

    def test_ou_parity_kills_opposite_chart(self):
        for i in range(1,8):
            for j in range(1,8):
                if (i+j)%2:
                    assert source_ou_pair_affine(i,j,self.a,Q(7,2))==(0,0)

    def test_exponential_poly_antiderivative(self):
        for alpha in (Q(1,2),Q(5,2)):
            for sign in (-1,1):
                for i in range(1,6):
                    p=legendre_polynomial(i,self.a)
                    f=exp_antiderivative_poly(p,alpha,sign)
                    assert poly_add(poly_derivative(f),f,sign*alpha)==p

    def test_cross_polynomial_zero_at_endpoint(self):
        for i in range(1,9):
            for j in range(1,9):
                rho=poly_two_variable_cross(i,j,self.a)
                assert poly_eval(rho,2*self.a)==0
                assert poly_eval(rho,0)==(Q(2,2*i+1) if i==j else 0)

    def test_cross_polynomial_symmetry(self):
        for i in range(1,7):
            for j in range(i,7):
                assert poly_two_variable_cross(i,j,self.a)==poly_two_variable_cross(j,i,self.a)

    def test_cross_polynomial_reflection(self):
        for i in range(1,7):
            for j in range(1,7):
                if (i+j)%2: assert all(c==0 for c in poly_two_variable_cross(i,j,self.a))

    def test_contact_exact_Neumann_identity(self):
        # ∫_0^(2a) t*rho(t)dt = ∫∫ |x-y|P_i(x)P_j(y)dxdy = -2K_ij.
        K=low_inverse_neumann(self.a,10)
        for i in range(1,11):
            for j in range(1,11):
                rho=poly_two_variable_cross(i,j,self.a)
                dist=poly_integral(poly_mul((0,1),rho),0,2*self.a)
                assert dist==-2*K[i-1][j-1],(i,j,dist,K[i-1][j-1])

    def test_hinge_integral_polynomial_vanishes_at_source_threshold(self):
        for i in range(1,8):
            for j in range(1,8):
                p=prime_hinge_integral_polynomial(i,j,self.a)
                assert poly_eval(p,2*self.a)==0
                assert poly_eval(poly_derivative(p),2*self.a)==0

    def test_hinge_polynomial_constant_equals_contact(self):
        K=low_inverse_neumann(self.a,8)
        for i in range(1,9):
            for j in range(1,9):
                p=prime_hinge_integral_polynomial(i,j,self.a)
                assert p[0]==-2*K[i-1][j-1]

    def test_hinge_polynomial_exact_source_control(self):
        assert prime_hinge_integral_polynomial(1,1,self.a)==(-Q(1,15),0,Q(1,3),-Q(1,3),0,Q(1,15))
        assert all(t==0 for t in prime_hinge_integral_polynomial(1,2,self.a))

    def test_hinge_polynomial_integral_at_fake_phase(self):
        for b in (Q(1,3),Q(1,2),Q(2,3)):
            for i,j in ((1,1),(1,3),(2,2),(2,4)):
                rho=poly_two_variable_cross(i,j,self.a)
                direct=poly_integral(poly_mul((-b,1),rho),b,2*self.a)
                assert poly_eval(prime_hinge_integral_polynomial(i,j,self.a),b)==direct

    def test_hinge_polynomial_integral_is_negative_on_true_L1(self):
        # The exact true first-prime hinge has negative sign on u=P1,
        # before the authentic coefficient log2/sqrt2 enters.
        p=prime_hinge_integral_polynomial(1,1,self.a)
        assert poly_eval(p,Q(2,3))<0 and poly_eval(p,Q(7,10))<0

    def test_illegal_legs_and_typed_floats(self):
        with self.assertRaises(SchurSourceError):legendre_polynomial(41,self.a)
        with self.assertRaises(SchurSourceError):legendre_polynomial(1,.5)
        with self.assertRaises(SchurSourceError):source_ou_pair_affine(1,1,self.a,0)
        with self.assertRaises(SchurSourceError):source_ou_pair_affine(1,1,self.a,.5)
        with self.assertRaises(SchurSourceError):prime_hinge_integral_polynomial(1,1,Q(0))

    def test_parent_failure_or_source_interval(self):
        try:
            x=authentic_full_low_entry(1,1,self.a,2)
        except SchurSourceError as exc:
            assert 'pinned parent #85' in str(exc)
            self.skipTest('pinned source #85 not mounted in isolated overlay')
        else:
            assert x.lo<x.hi and x.hi<1
            assert x.lo>-10

    def test_odd_source_entry_must_authenticate_too(self):
        try:
            x=authentic_full_low_entry(1,2,self.a,2)
        except SchurSourceError as exc:
            assert 'pinned parent #85' in str(exc)
        else:
            assert x.lo==x.hi==0

    def test_actual_original_full_matrix_when_checked_out(self):
        try:
            m=authentic_direct_low_matrix(rank=3,J=2)
        except SchurSourceError as exc:
            if 'pinned parent #85' not in str(exc):raise
            self.skipTest('pinned #85 source required; fail-closed integration CI')
        else:
            assert m['source']=='AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3'
            assert m['omitted_gamma_tail_positive'] and not m['RH_proved']
            mat=m['interval_matrix']
            assert len(mat)==3
            assert mat[0][1].lo==mat[0][1].hi==0
            assert mat[0][2].lo==mat[2][0].lo
            assert mat[0][0].lo<mat[0][0].hi

    def test_source_J_invalid_budget_fail_closed(self):
        with self.assertRaises(SchurSourceError):authentic_gamma_low_entry(1,1,self.a,65)


if __name__=='__main__':unittest.main()

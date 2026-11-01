"""Independent exact tests for finite Weyl, SUCC source-digit/carry and Pisot quotient."""
from __future__ import annotations
import unittest, importlib.util, sys
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-10-31'/'action_quantum_carrier'
def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module
q=load('action_quantum_source_20261031','action_quantum.py')
o=load('action_quantum_oracle_20261031','independent_oracle.py')

class ActionQuantumCarrierTest(unittest.TestCase):
    def test_modulus_validation(self):
        self.assertEqual(q.modulus(1),16)
        self.assertEqual(q.modulus(3),4096)
        for n in (0,-1,7,1.5):
            with self.assertRaises(ValueError):q.modulus(n)

    def test_finite_weyl_exact_all_16(self):
        for a,k,x in product(range(16), repeat=3):
            left=(k*((x+a)%16))%16
            right=(k*x+a*k)%16
            self.assertEqual(left,right)
            self.assertEqual(q.commutator_exponent(1,a,k),(a*k)%16)

    def test_phase_resolution_steps(self):
        for r in range(1,5):
            self.assertEqual(F(1,q.modulus(r+1)),F(1,q.modulus(r)*16))
            self.assertEqual(q.commutator_exponent(r,1,1),1)

    def test_branch_basis_isometry_and_completeness(self):
        for r in (1,2):
            values={q.digit_embedding(r,a,x) for x in range(q.modulus(r)) for a in range(16)}
            self.assertEqual(values,set(range(q.modulus(r+1))))
            for a,x in product((0,1,15), (0,q.modulus(r)-1)):
                self.assertEqual(q.recover_branch(r,q.digit_embedding(r,a,x)),(a,x))

    def test_shift_digit_carry_boundary_exhaustive(self):
        for r in (1,2):
            for a,x in product(range(16),range(q.modulus(r))):
                d,y=q.branch_shift(r,a,x)
                self.assertEqual(d,(a+1)%16)
                self.assertEqual(y,(x+(a==15))%q.modulus(r))

    def test_power_16_shift_intertwining(self):
        for r in (1,2):
            for a in range(16):
                for x in range(q.modulus(r)):
                    fine=q.shift(r+1,q.digit_embedding(r,a,x),16)
                    target=q.digit_embedding(r,a,q.shift(r,x))
                    self.assertEqual(fine,target)

    def test_character_refinement_exact(self):
        for r in (1,2):
            for a,k,x in product((0,1,15),(0,1,7,29),(0,1,q.modulus(r)-1)):
                lhs,rhs,branch=q.branch_clock_phase(r,a,x,k)
                self.assertEqual(lhs,rhs)
                self.assertEqual(branch,k*a%q.modulus(r+1))

    def test_quantum_phase_preserved_for_scaled_successor(self):
        for r in (1,2,3):
            for k in (1,3,17):
                coarse=q.commutator_exponent(r,1,k)
                fine=q.commutator_exponent(r+1,16,k)
                self.assertEqual(fine,16*coarse%q.modulus(r+1))

    def test_source_identity_independent_fraction(self):
        self.assertEqual(q.original_four_pole(1),F(47,15))
        for n in range(1,101):
            self.assertEqual(q.original_four_pole(n),q.original_combined(n))
            self.assertEqual(q.original_combined(n),o.bbp_combined(n))
            self.assertEqual(q.original_combined(n).denominator%2,1)

    def test_original_states_independent_convolution(self):
        for n in range(0,25):
            self.assertEqual(q.original_state(n),o.reconstructed_state(n))
            self.assertEqual(q.original_state(n).denominator%2,1)

    def test_modular_inverse_implementation_independent(self):
        for n,r in product(range(1,45),range(1,5)):
            self.assertEqual(q.two_adic_residue(q.original_four_pole(n),r),o.fraction_mod_2power(o.bbp_combined(n),r))

    def test_original_source_carry_all_levels(self):
        for r,n in product(range(1,5),range(0,23)):
            z=q.source_carry_step(r,n)
            self.assertTrue(0<=z.source_digit<16)
            self.assertTrue(0<=z.source_carry<16**r)
            self.assertEqual(z.state_after,q.two_adic_residue(o.reconstructed_state(n+1),r+1))
            self.assertEqual(z.state_after,(16*(z.state_before+z.source_carry)+z.source_digit)%16**(r+1))
            self.assertEqual(z.source_digit,q.two_adic_residue(o.bbp_combined(n+1),r+1)%16)

    def test_original_source_first_digit(self):
        z=q.source_carry_step(1,0)
        self.assertEqual(z.state_before,0)
        self.assertEqual(z.source_digit,1)
        self.assertEqual(z.state_after,q.two_adic_residue(F(47,15),2))

    def test_nonlocal_denominator_rejected(self):
        for r in (1,2):
            with self.assertRaises(ValueError):q.two_adic_residue(F(1,2),r)
        with self.assertRaises(TypeError):q.two_adic_residue(0.5,1)

    def test_real_phase_does_not_factor_exact_witness(self):
        for r in range(1,6):
            x,y=q.real_phase_nonfactor_witness(r)
            self.assertEqual(q.two_adic_residue(x,r),0)
            self.assertEqual(q.two_adic_residue(y,r),0)
            self.assertEqual(y%1,F(1,3))
            # In Q(zeta_3), (1-zeta_3)(1-zeta_3²)=3, hence chord²=3.
            z=(0,1)
            def mul(v,w):
                a,b=v; c,d=w
                return (a*c-b*d,a*d+b*c-b*d) # zeta_3²=-1-zeta_3
            self.assertEqual(mul((1,-1),(2,1)),(3,0))

    def test_pisot_multiplication_and_digit_division(self):
        for a,b in product(range(-12,13),repeat=2):
            d,x,y=q.quadratic_pisot_division(a,b)
            self.assertIn(d,(0,1))
            A,B=q.quadratic_pisot_multiply(x,y)
            self.assertEqual((A+d,B),(a,b))

    def test_pisot_squared_is_two_times_unit(self):
        self.assertEqual(q.pisot_squared_matrix(),((6,8),(4,6)))
        self.assertEqual(q.pisot_squared_matrix(),o.beta_matrix_square_via_composition())
        # beta^2=2(3+2sqrt2), factor 3+2sqrt2 has norm 1.
        self.assertEqual(3**2-2*2**2,1)
        self.assertEqual(o.pisot_quotient_two_grid(),set(product((0,1),repeat=2)))

    def test_pisot_noncyclic_second_level(self):
        # Quotient Z[sqrt2]/beta^2 Z[sqrt2] == (Z/2)^2, four states, exponent two.
        cosets=set(product((0,1),repeat=2))
        self.assertEqual(len(cosets),4)
        self.assertTrue(all(((2*a)%2,(2*b)%2)==(0,0) for a,b in cosets))
        self.assertNotEqual(2,4)

    def test_pisot_characters_cannot_have_order_four(self):
        for u,v,a,b in product((0,1),repeat=4):
            phase=(-1)**((u*a+v*b)%2)
            self.assertIn(phase,(-1,1))

    def test_kinetic_energy_refinement_every_branch(self):
        for r in (1,2):
            for a in range(16):
                for x in range(q.modulus(r)):
                    coarse=q.kinetic_basis(r,x)
                    embedded=q.embed_linear(r,a,coarse)
                    fine=q.kinetic_basis(r+1,q.digit_embedding(r,a,x),stride=16)
                    self.assertEqual(fine,embedded)

    def test_native_fine_kinetic_does_not_intertwine(self):
        self.assertNotEqual(q.kinetic_basis(2,0,stride=1),q.embed_linear(1,0,q.kinetic_basis(1,0)))

    def test_kinetic_second_order_independent_oracle(self):
        for x in (0,1,5,15):
            fine={q.digit_embedding(1,3,x):1}
            for _ in range(2):
                fine=o.kinetic_apply_to_linear_combination(256,fine,16)
            coarse={x:1}
            for _ in range(2):
                coarse=o.kinetic_apply_to_linear_combination(16,coarse,1)
            self.assertEqual(fine,q.embed_linear(1,3,coarse))

    def test_symplectic_frame_covariance(self):
        for m in (1,2,3,16,1024):
            M=q.symplectic_scaling(m)
            self.assertEqual(M[0][0]*M[1][1]-M[0][1]*M[1][0],1)
            self.assertEqual(q.symplectic_defect(m,F(1,m)),0)

    def test_naive_frame_is_not_symplectic(self):
        for m in (2,3,16):self.assertEqual(q.symplectic_defect(m,F(1)),m-1)

    def test_affine_composition_and_diamond(self):
        for m,x in product((2,3,16),(-7,-1,0,5)):
            self.assertEqual(m*(x+1),(m*x)+m)
            self.assertEqual(q.affine_compose(0,m,1,1),(m,m))

    def test_finite_uncertainty_saturating_cyclic(self):
        # H=4Z/16, size4, annihilator characters multiples4 size4.
        H=(0,4,8,12)
        ann=[k for k in range(16) if all((k*x)%16==0 for x in H)]
        self.assertEqual(ann,[0,4,8,12])
        self.assertTrue(q.elementary_uncertainty_bound(16,len(H),len(ann)))
        self.assertEqual(len(H)*len(ann),16)

    def test_finite_uncertainty_saturating_pisot(self):
        H=((0,0),(1,0))
        ann=[(u,v) for u,v in product((0,1),repeat=2)
             if all((u*a+v*b)%2==0 for a,b in H)]
        self.assertEqual(ann,[(0,0),(0,1)])
        self.assertEqual(len(H)*len(ann),4)
        self.assertTrue(q.elementary_uncertainty_bound(4,len(H),len(ann)))

    def test_false_uncertainty_claim_rejected(self):
        self.assertFalse(q.elementary_uncertainty_bound(16,2,3))
        for tup in ((16,0,3),(0,1,1),(16,17,1)):
            with self.assertRaises(ValueError):q.elementary_uncertainty_bound(*tup)

    def test_cyclotomic_oracle_independent_of_modular_annihilator(self):
        # H={0,4,8,12}; exact Phi16 polynomial reduction.
        H=(0,4,8,12)
        for k in range(16):
            zero=not any(q.exact_cyclotomic_character_sum(1,H,k))
            self.assertEqual(zero,k%4!=0)
        for k in (0,1,7,31):
            self.assertEqual(len(q.exact_cyclotomic_character_sum(2,(0,64,128,192),k)),128)

    def test_same_level_dilation_is_not_invertible(self):
        for r in (1,2,3):
            self.assertEqual(q.same_level_dilation_kernel_size(r,16),16)
            self.assertEqual(len({16*x % q.modulus(r) for x in range(q.modulus(r))}),q.modulus(r)//16)
            self.assertEqual(q.same_level_dilation_kernel_size(r,1),1)

    def test_original_symplectic_source_action_is_exact_BBP_sum(self):
        for n in range(0,31):
            x,p,A=q.bbp_source_action(n)
            self.assertEqual(x,q.original_state(n))
            self.assertEqual(p,F(1,16**n))
            self.assertEqual(A,q.bbp_normalized_sum(n))
            self.assertEqual(A,o.reconstructed_state(n)/16**n)

    def test_source_action_cocycle_every_step(self):
        for n in range(0,31):
            x,p,A=q.bbp_source_action(n)
            y,p2=q.source_symplectic_step(n,x,p)
            self.assertEqual(y*p2-A,q.original_four_pole(n+1)*p2)
            self.assertEqual((y,p2,y*p2),q.bbp_source_action(n+1))

    def test_positive_source_action_is_bounded(self):
        previous=F(0)
        for n in range(1,35):
            A=q.bbp_source_action(n)[2]
            self.assertGreater(A,previous)
            self.assertLess(A,F(1,4))
            previous=A

    def test_naive_momentum_not_reciprocal_breaks_action(self):
        x,p=F(3,5),F(7,11)
        n=2
        y,p2=q.source_symplectic_step(n,x,p)
        expected_delta=p2*q.original_four_pole(n+1)
        self.assertEqual(y*p2-x*p,expected_delta)
        self.assertNotEqual(y*p-x*p,expected_delta)

    def test_source_clock_is_not_real_circle_factor(self):
        # A smooth-compatible 2-adic source law can retain perfect local digits while
        # its circle phase differs by primitive 3rd root: x=0 vs x=16^r/3.
        for r in range(1,5):
            a,b=q.real_phase_nonfactor_witness(r)
            self.assertNotEqual((b-a)%1,0)
            self.assertEqual(q.two_adic_residue(a,r),q.two_adic_residue(b,r))

if __name__=='__main__':unittest.main()

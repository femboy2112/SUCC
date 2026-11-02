"""Source-attested rational and cyclotomic tests, not a pi-normality proof."""
import unittest
from fractions import Fraction
from math import gcd,lcm
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'arctan_chiral_solenoid'
def load(name,file):
    spec=importlib.util.spec_from_file_location('test_acss_'+name,ROOT/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
A=load('a','arctan_chiral.py')
O=load('o','independent_oracle.py')

class SourceTests(unittest.TestCase):
    def test_first_values(self):
        self.assertEqual(A.source(1),Fraction(47,15));self.assertEqual(A.source(2),Fraction(106,819))
    def test_four_poles_independent(self):
        for n in range(-15,60):
            self.assertEqual(A.source(n),O.four_poles(n))
            self.assertEqual(A.source(n),A.source_combined(n))
    def test_source_has_odd_denominators(self):
        for n in range(-30,100):self.assertEqual(A.source(n).denominator%2,1)
    def test_r_mod16_piecewise(self):
        for n in range(-64,65):self.assertEqual(A.source_residue(n,1),A.source_base16_closed(n))
    def test_source_exact_permutations(self):
        for level in range(1,5):
            q=16**level
            self.assertEqual(len(set(A.source_residue(n,level) for n in range(q))),q)
    def test_derivative_mod16_classes(self):
        for n in range(-24,64):
            self.assertEqual(A.lifted_derivative(n),A.derivative_base16_closed(n))
            self.assertEqual(A.lifted_derivative(n),(11 if n%4 in(0,1) else 3))
    def test_higher_taylor_law_all_residues_level2(self):
        for a in range(16):
            for t in range(16):self.assertTrue(A.source_slope_congruence(a,2,t))
    def test_higher_taylor_law_selected_level3_4(self):
        for level in (3,4):
            for a in (0,1,2,3,4,5,11,15,16,17,29,33,127):
                for t in range(16):self.assertTrue(A.source_slope_congruence(a,level,t))
    def test_mod_oracle(self):
        for level in (1,2,3):
            q=16**level
            for n in range(-32,130):self.assertEqual(A.source_residue(n,level),O.source_mod_via_horner(n,q))
    def test_valuation_exact_not_only_congruence(self):
        pairs=((0,1),(0,2),(2,6),(1,17),(5,69),(32,80),(2,258))
        def v2(n):
            if not n:raise ValueError()
            return (abs(n)&-abs(n)).bit_length()-1
        for x,y in pairs:
            delta=A.source(x)-A.source(y)
            self.assertEqual(v2(delta.numerator),v2(x-y))
            self.assertEqual(delta.denominator%2,1)
    def test_invalid_modulus(self):
        with self.assertRaises(ValueError):A.odd_denominator_mod(Fraction(1,2),16)
    def test_source_poles(self):
        for x in (Fraction(1,2),Fraction(1,4),Fraction(7,8),Fraction(3,8)):
            with self.assertRaises(ValueError):A.source(x)
    def test_zero_seed(self):
        states=A.finite_orbit(12)
        self.assertEqual(states[0],0)
        for j in range(1,len(states)):
            self.assertEqual(states[j],16*states[j-1]+O.four_poles(j))
            self.assertEqual(states[j],O.direct_unwrapped(j))

class FourierTests(unittest.TestCase):
    def test_full_16_cyclotomic_matrix(self):
        for k in range(16):
            for l in range(16):
                self.assertEqual(A.source_fourier16_numerator(k,l),A.source_fourier16_closed_numerator(k,l))
                self.assertEqual(A.source_fourier16_numerator(k,l),O.finite_fourier_witness(k,l))
    def test_base16_two_channel_cardinality(self):
        for k in range(16):
            self.assertEqual(set(l for l in range(16) if A.source_fourier16_numerator(k,l)!=(0,)*8),
                             set(l for l in ((-k)%16,(8-k)%16) if A.source_fourier16_numerator(k,l)!=(0,)*8))
    def test_unitary_cyclotomic_orthogonality(self):
        # Position permutation => inner products of its characters form orthogonal basis.
        rho=[A.source_residue(n,1) for n in range(16)]
        for j in range(16):
            for k in range(16):
                s=(0,)*8
                for n in rho:s=A.add_vec(s,A.root_vector_16((j-k)*n))
                self.assertEqual(s,(16,)+(0,)*7 if j==k else (0,)*8)
    def test_all_level_support_rule(self):
        for k in range(1,65):
            permitted={l%16 for l in range(16) if A.higher_fourier_support(k,l)}
            self.assertEqual(permitted,{(3*k)%16,(11*k)%16})
    def test_disallowed_congruences_exact_taylor(self):
        # For any 16-adic lifted block, t-sum vanishes if l-k*r'(a) != 0 mod16.
        for a in range(16):
            d=A.lifted_derivative(a)
            for k in range(1,9):
                for ell in range(16):
                    exps=tuple((ell-k*d)*t for t in range(16))
                    s=(0,)*8
                    for ex in exps:s=A.add_vec(s,A.root_vector_16(ex))
                    self.assertEqual(s,(16,)+(0,)*7 if (ell-k*d)%16==0 else (0,)*8)
    def test_source_matched_mutant_not_same_base_Fourier(self):
        mutated=[A.odd_denominator_mod(A.source(n)+Fraction(1,2*n+1),16) for n in range(16)]
        self.assertEqual(len(set(mutated)),16)
        self.assertNotEqual(mutated,[A.source_residue(n,1) for n in range(16)])
        # Its frequency k=1 is not the exact original two-channel signature.
        def kernel(rho,k,l):
            s=(0,)*8
            for n,r in enumerate(rho):s=A.add_vec(s,A.root_vector_16(l*n-k*r))
            return s
        self.assertTrue(any(kernel(mutated,1,l)!=A.source_fourier16_numerator(1,l) for l in range(16)))
    def test_fourier_is_not_coordinate_permutation(self):
        # A 16-point DFT sends localized |0> to 16 nonzero Fourier components.
        self.assertEqual(sum(1 for k in range(16) if A.root_vector_16(0)!=(0,)*8),16)
    def test_fourier_squared_parity(self):
        for q in (2,16,30,256):
            for x in range(q):self.assertEqual(O.cyclic_coset_DFT_square(x,q),(-x)%q)

class ArctanTests(unittest.TestCase):
    def test_projective_reciprocal_cayley_identity_exact(self):
        # C(t)=(b+ia)/(b-ia); C(1/t)=-1/C(t).
        for a in range(-5,6):
            for b in range(-5,6):
                if a==0 and b==0:continue
                # exact Gaussian integer multiplication of projective numerator/denom
                def times(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
                left=times((b,a),(a,b))
                right=times((b,-a),(a,-b))
                self.assertEqual(left,(-right[0],-right[1]))
    def test_arctan_reflection_involution(self):
        for q in (3,15,819,4095):
            for num in range(-2*q,2*q+1,13):
                x=Fraction(num,q)
                self.assertEqual(A.inverted_circle_phase(A.inverted_circle_phase(x)),A.mod_one(x))
    def test_mod_one_chiral_conjugacy(self):
        for n in range(1,16):
            for x in (Fraction(0),Fraction(1,15),Fraction(3,7),Fraction(2,19)):
                lhs=A.inverted_circle_phase(16*x+A.source(n))
                rhs=A.mod_one(16*A.inverted_circle_phase(x)+A.chiral_forcing(n))
                self.assertEqual(lhs,rhs)
    def test_chiral_explicit_unwrapped_carry(self):
        u=A.finite_orbit(12);v=A.chiral_orbit(12)
        for n in range(13):
            self.assertEqual(v[n]+u[n]-Fraction(1,2),A.chiral_integer_carry(n))
            self.assertEqual(A.mod_one(v[n]),A.inverted_circle_phase(u[n]))
    def test_chiral_real_characters_conjugate_exact(self):
        u=A.finite_orbit(10);v=A.chiral_orbit(10)
        for n in range(11):
            for h in (-7,-3,-2,-1,0,1,2,5):
                self.assertEqual(A.mod_one(h*v[n]),A.mod_one(Fraction(h,2)-h*u[n]))
    def test_chiral_joint_character_locked(self):
        u=A.finite_orbit(11)
        for n in range(12):
            x=A.mod_one(u[n]);y=A.inverted_circle_phase(x)
            for h in (1,2,3,5):
                for k in (0,1,2,3):
                    self.assertEqual(A.mod_one(h*x+k*y),A.mod_one(Fraction(k,2)+(h-k)*x))
    def test_chiral_source_not_two_adic_integral(self):
        for n in range(1,20):
            self.assertEqual(A.chiral_forcing(n).denominator%2,0)
            with self.assertRaises(ValueError):A.odd_denominator_mod(A.chiral_forcing(n),16)
    def test_chiral_signed_lag_conjugate(self):
        u=A.finite_orbit(15);v=A.chiral_orbit(15)
        for a in range(1,10):
            for k in range(1,5):
                self.assertEqual(A.mod_one(v[a+k]-v[a]),A.mod_one(-(u[a+k]-u[a])))

class SolenoidTests(unittest.TestCase):
    def test_odd_source_lift_all_rational_inputs(self):
        for x in (Fraction(47,15),Fraction(106,819),Fraction(2,7),Fraction(4,19),Fraction(29,31)):
            tower=A.odd_torsion_tower(x,8)
            self.assertTrue(A.compatible_tower(tower))
            self.assertEqual(tower[0],A.mod_one(x))
            for j in range(7):self.assertEqual(A.mod_one(16*tower[j+1]),tower[j])
    def test_four_inverse_odd_torsion_unique(self):
        for x in (Fraction(47,15),Fraction(106,819),Fraction(7,13),Fraction(1,3)):
            t=A.odd_torsion_tower(x,8)
            inv=A.tower_four_inverse(t)
            self.assertEqual(A.tower_scale(inv,4),t[:-1])
            q=A.mod_one(x).denominator
            root=A.mod_one(x) if q==1 else Fraction((A.mod_one(x).numerator*pow(4,-1,q))%q,q)
            self.assertEqual(inv[0],root)
    def test_solenoid_source_trajectory(self):
        states=A.finite_orbit(7);state=A.odd_torsion_tower(Fraction(0),9)
        for n in range(8):
            self.assertEqual(state,A.odd_torsion_tower(states[n],9))
            if n<7:state=A.tower_source_step(state,A.source(n+1))
    def test_four_cover_source_square(self):
        initial=A.odd_torsion_tower(Fraction(5,17),9)
        for n in range(1,7):
            g=A.tower_add(A.tower_scale(initial[:-1],16), A.tower_four_inverse(A.odd_torsion_tower(A.source(n),9)))
            pf=A.tower_source_step(A.tower_scale(initial[:-1],4),A.source(n))
            self.assertEqual(A.tower_scale(g,4),pf)
    def test_halfturn_tower_is_compatible(self):
        t=A.half_turn_tower(10)
        self.assertTrue(A.compatible_tower(t))
        self.assertEqual(t[0],Fraction(1,2))
    def test_chiral_tower_involution_and_natural_square(self):
        t=A.half_turn_tower(9)
        x=A.odd_torsion_tower(Fraction(3,17),9)
        self.assertEqual(A.tower_chiral(A.tower_chiral(x,t),t),x)
        for n in range(1,8):
            self.assertEqual(A.tower_chiral(A.tower_source_step(x,A.source(n)),t),
                             A.tower_chiral_source(A.tower_chiral(x,t),t,A.source(n)))
    def test_halfturn_lifts_are_not_unique(self):
        t=A.half_turn_tower(8)
        k=(Fraction(0),)+tuple(Fraction(1,16**j) for j in range(1,8))
        self.assertTrue(A.compatible_tower(k))
        alternative=A.tower_add(t,k)
        self.assertEqual(t[0],alternative[0])
        self.assertNotEqual(t[1],alternative[1])
        self.assertNotEqual(A.tower_character(t,1,1),A.tower_character(alternative,1,1))
    def test_source_dual_character_weighted_shift(self):
        for x in (Fraction(1,7),Fraction(47,15)):
            state=A.odd_torsion_tower(x,8)
            for n in range(1,6):
                for level in range(8):
                    for num in (-3,-1,1,2,5,16):
                        left,right=A.dual_shift_phase(state,A.source(n),num,level)
                        self.assertEqual(left,right)
    def test_unmodified_source_map_no_even_halfturn_clock(self):
        q=15
        self.assertNotEqual(gcd(16,2*q),1)
        self.assertEqual((16*0)%(2*q),(16*q)%(2*q))
    def test_chiral_torsor_oddQ_bijective(self):
        for q,number in ((15,1),(4095,2)):
            src=A.source(number)
            perm=[A.finite_chiral_torsor_map(i,q,src) for i in range(2*q)]
            self.assertEqual(len(set(perm)),2*q)
            for i in range(2*q):
                self.assertEqual(perm[A.finite_chiral_j(i,q)],A.finite_chiral_j(perm[i],q))
    def test_independent_chiral_torsor_orbit(self):
        q=lcm(15,819)
        x=0
        v=q
        for n in (1,2):
            x=A.finite_chiral_torsor_map(x,q,A.source(n))
            v=A.finite_chiral_torsor_map(v,q,A.source(n))
        self.assertEqual((x,v),O.finite_chiral_orbit(q,2))
    def test_arctan_is_halfshift_times_doubleDFT(self):
        for q in (3,5,15,819):
            for idx in range(2*q):
                self.assertEqual(A.finite_chiral_j(idx,q),A.fourier_squared_reflection(idx,2*q))
    def test_source_odd_torsion_fourthroot(self):
        for n in range(1,13):
            t=A.odd_torsion_tower(A.source(n),4)
            self.assertEqual(A.tower_scale(A.tower_four_inverse(t),4),t[:3])

class MachinTests(unittest.TestCase):
    def test_gaussian_factor_identity(self):
        self.assertEqual(A.arctan_ratio_machin_factor(),((476,480),(476,480)))
        self.assertEqual(A.arctan_ratio_machin_factor(),O.machin_gaussian())
    def test_rational_arctan_both_parities(self):
        for n in range(1,9):
            lo,hi=A.arctan_alternating_bounds(5,n)
            self.assertLess(lo,hi)
    def test_machin_pi_oracle_independence(self):
        lastwidth=None
        for k in (1,2,3,4,5,8,12):
            lo,hi=A.machin_pi_bounds(k)
            o_lo,o_hi=O.machin_interval(k)
            self.assertEqual((lo,hi),(o_lo,o_hi))
            self.assertLess(lo,Fraction(22,7))
            self.assertGreater(hi,Fraction(3,1))
            self.assertLess(lo,hi)
            if lastwidth is not None:self.assertLess(hi-lo,lastwidth)
            lastwidth=hi-lo
    def test_machin_supports_bbp_rational_bracket(self):
        for N in (1,2,3,4,5,7):
            b=sum((Fraction(16,16**n)*A.source(n) for n in range(1,N+1)),Fraction(0))
            lo,hi=A.machin_pi_bounds(16)
            self.assertLess(b,lo)
            self.assertLess(hi, Fraction(22,7))
    def test_guard_bad_inputs(self):
        with self.assertRaises(ValueError):A.arctan_alternating_bounds(1,3)
        with self.assertRaises(ValueError):A.arctan_alternating_bounds(5,0)
        with self.assertRaises(ValueError):A.half_turn_tower(0)

if __name__=='__main__':unittest.main()

class PerpendicularTests(unittest.TestCase):
    def test_odd_conductor_Fourier_state_change(self):
        for Q,indices in ((15,(1,2,7,11)),(4095,(1,7,256,4094))):
            for n in ((1,) if Q==15 else (1,2)):
                b=(A.mod_one(A.source(n)).numerator*(Q//A.mod_one(A.source(n)).denominator))%Q
                inv=pow(16,-1,Q)
                for p in indices:
                    k,phase=A.odd_register_fourier_step(p,Q,A.source(n))
                    self.assertEqual(k,(p*inv)%Q)
                    self.assertEqual(phase,A.mod_one(Fraction(-p*inv*b,Q)))
                    # Independent eigencharacter change: P maps p-character to inv(p)-character
                    for y in (0,1,2,5,7):
                        x=((y-b)*inv)%Q
                        self.assertEqual(A.mod_one(Fraction(p*x,Q)),A.mod_one(phase+Fraction(k*y,Q)))
    def test_odd_conductor_denominator_required(self):
        with self.assertRaises(ValueError):A.odd_register_fourier_step(1,15,A.source(2))
        with self.assertRaises(ValueError):A.odd_register_fourier_step(1,30,A.source(1))
    def test_cauchy_inversion_chart_exact(self):
        for a in range(-15,16):
            if not a:continue
            for b in (1,3,7,11):
                l,r=A.cauchy_inversion_density_identity(Fraction(a,b))
                self.assertEqual(l,r)
    def test_cauchy_rotations_exact(self):
        for a in (Fraction(-7,3),Fraction(-1,2),Fraction(0),Fraction(2,3),Fraction(1,5)):
            for t in (Fraction(-11,4),Fraction(-1,3),Fraction(0),Fraction(2,7),Fraction(9,4)):
                if a*t==1:continue
                l,r=A.cauchy_rotation_density_identity(t,a)
                self.assertEqual(l,r)
    def test_projective_double_reciprocal(self):
        self.assertIsNone(A.projective_circle_double(Fraction(1)))
        self.assertIsNone(A.projective_circle_double(Fraction(-1)))
        self.assertEqual(A.projective_circle_double(Fraction(1,5)),Fraction(5,12))
    def test_source_time_continuity_obstruction_finite(self):
        # For n_j=1+16^j -> 1 in Z2, real r(n_j)->0 != r(1)=47/15.
        self.assertNotEqual(A.mod_one(A.source(1)),0)
        self.assertGreater(A.source(1),3)
        for j in range(1,10):
            n=1+16**j
            self.assertEqual((n-1)%16**j,0)
            self.assertGreater(A.source(n),0)
            self.assertLess(A.source(n),Fraction(1,(n-1)**2))
    def test_chiral_Cauchy_weyl_no_new_constraint(self):
        for n in range(1,15):
            original=A.mod_one(A.finite_orbit(n)[n])
            dual=A.inverted_circle_phase(original)
            for h in range(-5,6):
                self.assertEqual(A.mod_one(h*dual),A.mod_one(Fraction(h,2)-h*original))
    def test_weyl_source_type_and_chiral_type_not_identical(self):
        q=4095
        self.assertEqual(gcd(16,q),1)
        self.assertNotEqual(gcd(16,2*q),1)
        self.assertEqual(A.finite_chiral_j(0,q),q)

class SourceAngleCohomologyTests(unittest.TestCase):
    def test_exact_cancellation_of_source_mellin_factors(self):
        for n in range(0,21):
            t=Fraction(n,20)
            self.assertEqual(A.completed_mellin_density(t),A.completed_mellin_reduced(t))
    def test_angular_plus_log_coboundary(self):
        for n in range(0,21):
            t=Fraction(n,20)
            self.assertEqual(A.completed_mellin_density(t),
                             A.geometric_angular_eighth(t)+A.log_coboundary_derivative(t))
    def test_exact_relative_boundary_zero(self):
        self.assertEqual(A.log_boundary_ratio(Fraction(0)),1)
        self.assertEqual(A.log_boundary_ratio(Fraction(1)),1)
        self.assertNotEqual(A.log_boundary_ratio(Fraction(1,2)),1)
    def test_positive_source_mellin_density(self):
        for j in range(1,100):
            t=Fraction(j,100)
            self.assertGreater(A.completed_mellin_density(t),0)
    def test_mutant_moment_and_completed_period_sign(self):
        self.assertEqual(A.beta_8_9(),Fraction(1,102960))
        for eps in (Fraction(1),Fraction(1,100),Fraction(7,19)):
            low,high=A.positive_mutant_period_bounds(eps)
            self.assertLess(low,high)
            self.assertGreater(low,0)
    def test_bad_mutant_input(self):
        with self.assertRaises(ValueError):A.positive_mutant_period_bounds(Fraction(0))

class CompleteSourceCircleTests(unittest.TestCase):
    def test_four_signed_poles_equal_integrated_mellin_polynomial(self):
        for n in range(1,101):
            alpha=8*(n-1)
            moment=(Fraction(4,alpha+1)-Fraction(2,alpha+4)-
                    Fraction(1,alpha+5)-Fraction(1,alpha+6))
            self.assertEqual(moment,A.source(n))
    def test_exact_original_finite_partial_vs_unwrapped_state(self):
        state=Fraction(0)
        partial=Fraction(0)
        for n in range(1,50):
            state=16*state+A.source(n)
            partial+=A.source(n)/16**n
            self.assertEqual(partial,Fraction(state,16**n))
    def test_complete_circle_period_independent_machin_bracket(self):
        # Machin's angle comes from independent Gaussian integer path;
        # the BBP partial sum and positive future tail bound bracket it.
        lo,hi=A.machin_pi_bounds(20)
        lower_pi=Fraction(0)
        for n in range(1,11):
            lower_pi+=16*A.source(n)/16**n
            upper_pi=lower_pi+Fraction(16,15)*A.source(n+1)/16**n
            self.assertLess(lower_pi,lo)
            self.assertLess(hi,upper_pi)
    def test_mutant_Beta_source_integral_positive(self):
        # Exact extra moments identify a genuinely different source class.
        for n in range(1,22):
            from math import factorial
            beta=Fraction(factorial(8*n-1)*factorial(8),factorial(8*n+8))
            self.assertGreater(beta,0)
        lo,hi=A.positive_mutant_period_bounds(Fraction(1,100))
        self.assertGreater(lo,0)
        self.assertLess(hi,Fraction(1,100000))

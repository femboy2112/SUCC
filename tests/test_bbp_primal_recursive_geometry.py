"""Exact adversarial audit: first-prime BBP recursion, 3-adic pole split and CRT join.

This suite uses the immutable PR #321 source module and authoritative forcing.
Tests establish finite claims; the dossier supplies the universal 2-adic/
3-adic proofs. No test is a claim of pi normality or independence.
"""
import unittest
from fractions import Fraction as Q
from random import Random

from observational_succ import bbp_primal_recursive_geometry as p
from observational_succ import bbp_binwindow_conjugacy as base
from observational_succ.succ_internal_matrix_walk import authentic_r


class SourceAndBinaryGates(unittest.TestCase):
    def test_original_four_poles_and_canceled_source_independently(self):
        for n in range(1,201):
            self.assertEqual(Q(p.source_numerator(n),p.source_denominator(n)), authentic_r(n))
            self.assertEqual(base.canceled_source_extension(n),authentic_r(n))

    def test_high_index_modular_adapter_against_exact_four_poles(self):
        for n in (1_000_001, 2**20+3, 2**31+7):
            self.assertEqual(Q(p.source_numerator(n),p.source_denominator(n)), authentic_r(n))
            for bits in (12,20,24,32):
                self.assertEqual(p.binary_code(n,bits),
                                 p.binary_code(n % (1<<bits),bits))

    def test_first_binary_gates(self):
        self.assertEqual(tuple(p.shear_anf_masks(j) for j in range(4)),
                         ((),(),(2,),(2,4,6)))
        for n in range(160):
            self.assertEqual(p.binary_code(n,1),n%2)
            self.assertEqual(p.binary_code(n,2),n%4)
            self.assertEqual(p.shear_bit(2,n%4),(n>>1)&1)
            self.assertEqual(p.shear_bit(3,n%8),int(bool(n&2 or n&4)))

    def test_first_hex_reflection_and_not_global_involution(self):
        for n in range(96):
            val=p.first_hex_reflection(n)
            self.assertEqual(val,(2*(n&1)-n)%16)
            self.assertEqual((2*(val&1)-val)%16,n%16)
        # Explicit hostile extension: the mod16 involution FAILS mod32.
        self.assertEqual(p.binary_code(2,5),30)
        self.assertEqual(p.binary_code(30,5),18)
        self.assertNotEqual(p.binary_code(p.binary_code(2,5),5),2)

    def test_first_hex_state_successor_two_operations(self):
        for x in range(16):
            expected=(x+1 if x%2==0 else x-3)%16
            self.assertEqual(p.conjugated_successor(x,4),expected)

    def test_next_nontrivial_boolean_anf(self):
        self.assertEqual(p.shear_anf_masks(4),(2,3,6,8,10,12,14))
        for j in range(7):
            masks=p.shear_anf_masks(j)
            for lower in range(1<<j):
                self.assertEqual(p.evaluate_anf(masks,lower),p.shear_bit(j,lower))

    def test_input_type_firewall(self):
        for bad in (True,1.0,"3",-1):
            with self.assertRaises(ValueError):p.binary_code(bad,4)
        with self.assertRaises(ValueError):p.shear_bit(2,4)
        with self.assertRaises(ValueError):p.binary_inverse_from_gates(16,4)
        with self.assertRaises(ValueError):p.shear_truth_table(10)
        with self.assertRaises(ValueError):p.ternary_trident(0)

    def test_exact_state_modular_crosschecks_no_digit_oracle(self):
        for n in range(0,65):
            state=base.authentic_state(n)
            for bits in (1,2,3,4,5,6,8,12):
                expected=base.two_adic_mod(state,(bits+3)//4)%(1<<bits)
                self.assertEqual(p.binary_code(n,bits),expected)

    def test_recursion_permutations_and_inverse_all_outputs(self):
        for bits in range(1,9):
            cert=p.binary_recursion_receipt(bits)
            self.assertTrue(cert["inverse_is_bit_recursive"])
            self.assertEqual(cert["states"],1<<bits)
            self.assertFalse(cert["normality_proved"])

    def test_inverse_lift_large_inputs_and_all_digits(self):
        rg=Random(712161)
        for bits in (9,11,13,17,23,32):
            mask=(1<<bits)-1
            for _ in range(24):
                n=rg.randrange(min(1<<bits,500_000))
                y=p.binary_code(n,bits)
                self.assertEqual(p.binary_inverse_from_gates(y,bits),n&mask)
                shifted=n+(1<<bits)*rg.randint(0,10)
                if shifted<1_000_000:
                    self.assertEqual(p.binary_code(shifted,bits),y)

    def test_large_2adic_inverse_without_fake_source_extension(self):
        rng=Random(99891)
        for bits in (21,24,28,32):
            for target in (0,1,(1<<bits)-1,*[rng.getrandbits(bits) for _ in range(16)]):
                n=p.binary_inverse_from_gates(target,bits)
                self.assertLess(n,1<<bits)
                self.assertEqual(p.binary_code(n,bits),target)
                self.assertEqual(p.binary_code(n+(1<<bits)*5,bits),target)

    def test_modular_source_evaluator_matches_parent_in_overlap(self):
        from fractions import Fraction as Q
        for n in (0,1,2,31,999,65535,999999):
            for bits in (5,16,24,32):
                m=1<<bits
                v=0
                for s in range((bits+3)//4):
                    t=n-s
                    v=(v+16**s*(120*t*t-89*t+16)*pow((2*t-1)*(4*t-1)*(8*t-7)*(8*t-3),-1,m))%m
                self.assertEqual(p.binary_code(n,bits),v)

    def test_odometer_conjugacy(self):
        for bits in (3,4,6):
            m=1<<bits
            state=0
            seen=set()
            for n in range(m):
                self.assertNotIn(state,seen)
                seen.add(state)
                self.assertEqual(state,p.binary_code(n,bits))
                state=p.conjugated_successor(state,bits)
            self.assertEqual(state,0)
            self.assertEqual(len(seen),m)

    def test_perturbation_rejects_nonisometry(self):
        # A fake function may agree at the first 16 digits but merge two
        # residues at the next level. A finite mod16 check is insufficient.
        fake=lambda n:(p.binary_code(n,5)&15)
        self.assertEqual(len({fake(n) for n in range(16)}),16)
        self.assertLess(len({fake(n) for n in range(32)}),32)


class ThreeAdicSource(unittest.TestCase):
    def test_numerator_three_adic_isometry_all_finite_levels(self):
        for k in range(1,8):
            m=3**k
            self.assertEqual(len({p.regularized_ternary_code(n,k) for n in range(m)}),m)
        for a in range(-20,21):
            for b in range(-20,21):
                if a==b:continue
                self.assertEqual(p.v3_integer(p.source_numerator(a)-p.source_numerator(b)),
                                 p.v3_integer(a-b))

    def test_ternary_hensel_inverse(self):
        for depth in range(1,6):
            m=3**depth
            for y in range(m):
                n=p.ternary_inverse_from_lifts(y,depth)
                self.assertEqual(p.source_numerator(n)%m,y)
                self.assertEqual(p.ternary_inverse_from_lifts(p.source_numerator(n)%m,depth),n)

    def test_source_forms_root_mod3_coincidence_then_split(self):
        self.assertEqual(p.ternary_trident(1)["roots"],(2,2,2))
        self.assertEqual(p.ternary_trident(1)["descriptive_ratio"],9)
        self.assertEqual(p.ternary_trident(2)["roots"],(8,5,2))
        self.assertEqual(p.ternary_trident(2)["descriptive_ratio"],0)
        for k in range(2,10):
            t=p.ternary_trident(k)
            self.assertEqual({r%9 for r in t["roots"]},{2,5,8})
            self.assertEqual(t["coincidence_count"],0)

    def test_residue_zero_does_not_remove_local_three_adic_poles(self):
        r=p.source_pole_residues()
        self.assertEqual(dict(r["poles"]),
                         {Q(1,2):Q(-1,4),Q(1,4):Q(-1,8),
                          Q(7,8):Q(1,2),Q(3,8):Q(-1,8)})
        self.assertEqual(r["sum_of_finite_residues"],0)
        self.assertTrue(r["local_poles_remain"])

    def test_four_poles_and_one_numerator_root(self):
        names=("numerator","two_n_minus_one","four_n_minus_one",
               "eight_n_minus_seven","eight_n_minus_three")
        for name in names:
            for k in (1,2,3,4,6):
                a=p.pole_root_mod_three(name,k)
                self.assertGreaterEqual(a,0)
                self.assertLess(a,3**k)
        # Denominator roots occupy *every* mod-3 time class.
        classes={p.pole_root_mod_three(n,1) for n in names[1:]}
        self.assertEqual(classes,{0,1,2})

    def test_poles_genuine_not_cancelled_by_source_numerator(self):
        poles=(Q(1,2),Q(1,4),Q(7,8),Q(3,8))
        checks=(Q(3,2),Q(5,4),Q(30),Q(-1,2))
        for a,want in zip(poles,checks):
            self.assertEqual(120*a*a-89*a+16,want)
            self.assertNotEqual(want,0)

    def test_3_adic_backward_window_divergence_every_center(self):
        # Every center in Z3 can approach the 3/8 pole in reverse ages.
        for center in (-31,-7,0,1,18):
            ages=[]
            for k in range(1,10):
                r=p.backward_three_adic_divergence(k,center)
                ages.append(r["positive_age"])
                self.assertLessEqual(r["weighted_term_valuation"],-k)
                self.assertFalse(r["convergent_three_adic_past"])
            self.assertEqual(ages,sorted(set(ages)))

    def test_r_not_globally_Z3_integral_or_3adic_contraction(self):
        for n in (1,2,3,4,5,6,7,9,11):
            f=base.canceled_source_extension(n)
            self.assertLess(p.v3_fraction(f.numerator,f.denominator),0)
        # Genuine integral islands near numerator zero DO exist.
        n=p.pole_root_mod_three("numerator",4)
        f=base.canceled_source_extension(n)
        self.assertGreaterEqual(p.v3_fraction(f.numerator,f.denominator),1)


class JointPrimeClock(unittest.TestCase):
    def test_genuine_all_pair_permutations_small_and_medium(self):
        for k,l in ((1,1),(1,2),(2,1),(2,2)):
            result=p.crt_period_certificate(k,l)
            self.assertEqual(result.unique_pairs,16**k*3**l)
            self.assertTrue(result.full_bijection_checked)
            self.assertFalse(result.zero_selected_real_pi_normality_proved)
            self.assertEqual(result.zero_anchor_two,0)
            self.assertEqual(result.zero_anchor_three,16%3**l)

    def test_constructive_CRT_inverse_arbitrary_pairs(self):
        rg=Random(95007)
        for k,l in ((1,4),(2,3),(3,3),(4,2)):
            m=16**k*3**l
            for _ in range(30):
                n=rg.randrange(m)
                pair=p.crt_time_to_source_pair(n,k,l)
                self.assertEqual(p.crt_source_pair_to_time(*pair,k,l),n)
                # One full period returns the same pair.
                self.assertEqual(p.crt_time_to_source_pair(n+m,k,l),pair)

    def test_source_tags_distinguish_3adic_numerator_from_real_state(self):
        n=1
        self.assertEqual(p.crt_time_to_source_pair(n,1,1),
                         (base.two_adic_mod(base.authentic_state(n),1),p.source_numerator(n)%3))
        self.assertNotEqual(p.source_numerator(n),base.authentic_state(n))
        flags=p.source_status_flags()
        self.assertFalse(flags['2adic_state_equals_3adic_numerator'])
        self.assertFalse(flags['real_pi_base16_normality_proved'])
        self.assertFalse(flags['3adic_unweighted_infinite_past_converges'])

    def test_hostile_real_nonnormal_zero_seedy_control_survives(self):
        # PR #320's exact zero-seeded positive forcing counterfeit.
        T=lambda n:Q(n+1,(2*n+1)*(4*n+1)*(8*n+1))
        for n in range(1,15):
            x=16**n-T(n)
            self.assertEqual(x%1,1-T(n))
            self.assertTrue(T(n)>0)
            self.assertLess(T(n),Q(1,2*n))

    def test_negative_promotion_receipt(self):
        flags=p.source_status_flags()
        self.assertTrue(flags['2adic_triangular_permutation'])
        self.assertTrue(flags['finite_CRT_primal_clock'])
        self.assertFalse(flags['RH_proved'])
        self.assertFalse(flags['real_pi_base16_normality_proved'])


if __name__=='__main__':
    unittest.main()

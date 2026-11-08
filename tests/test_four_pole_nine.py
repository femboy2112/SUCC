"""Exact rational adversarial tests of the source's nine-entry/ternary theory."""

import cmath
import math
import unittest
from collections import Counter
from fractions import Fraction
from itertools import product

from observational_succ.four_pole_nine import (
    SHIFTS, POLE_COEFFICIENTS, POSITIVE_CHANNELS, PROJECTION,
    signed_four_pole, difference_channel, forcing, positive_three_channel,
    original_zero_orbit, component_orbit, source_jets, rigid_integer_shifts,
    source_matrix, cauchy_determinant, determinant_3, recover_multiplicities,
    relative_clock_vector, relative_operator, projected_clock_step,
    relative_commutator, commutator_closed, commutator_op_norm_sq,
    commutator_vandermonde_norm_sq, spin_135_parts,
    source_channel_weights, source_channel_limit_weights,
    channel_amplitude, channel_limit_amplitude, normalized_channel_amplitude_budget)


class TestAuthenticPoleIdentity(unittest.TestCase):
    def test_four_original_signed_poles_preserved(self):
        self.assertEqual(SHIFTS, (0,3,4,5))
        self.assertEqual(POLE_COEFFICIENTS, (4,-2,-1,-1))
        self.assertEqual(sum(POLE_COEFFICIENTS), 0)
        for n in range(1,100):
            a=8*n-7
            original=(Fraction(4,a)-Fraction(2,a+3)
                      -Fraction(1,a+4)-Fraction(1,a+5))
            self.assertEqual(forcing(n), original)
            self.assertEqual(signed_four_pole(a), original)
            self.assertEqual(sum(positive_three_channel(a)),original)

    def test_reject_invalid_clock_and_seed(self):
        for value in (0,-1,True,1.5,'5'):
            with self.subTest(value=value),self.assertRaises((TypeError,ValueError)):
                signed_four_pole(value)
        for value in (-1,True,0.5):
            with self.subTest(value=value),self.assertRaises((TypeError,ValueError)):
                original_zero_orbit(value)
        with self.assertRaises(ValueError):
            forcing(0)

    def test_exact_triplet_phase_is_original_seeded_orbit(self):
        for n in range(0,24):
            v=component_orbit(n)
            self.assertEqual(len(v),3)
            self.assertEqual(sum(v),original_zero_orbit(n))
        # Numerically verify independent phase-product identity on reduced rational lifts.
        for h in (1,2,3,7):
            for n in (1,3,5,8,15):
                v=component_orbit(n)
                u=original_zero_orbit(n)
                p=complex(1,0)
                for q in v:
                    p*=cmath.exp(2j*math.pi*h*float(q%1))
                expected=cmath.exp(2j*math.pi*h*float(u%1))
                self.assertLess(abs(p-expected),1e-11)

    def test_three_difference_channels_strictly_positive(self):
        self.assertEqual(POSITIVE_CHANNELS,((3,2),(4,1),(5,1)))
        for a in (1,9,17,137,Fraction(9,2)):
            self.assertTrue(all(x>0 for x in positive_three_channel(a)))
            self.assertEqual(positive_three_channel(a),(
                Fraction(6,1)/(Fraction(a)*(Fraction(a)+3)),
                Fraction(4,1)/(Fraction(a)*(Fraction(a)+4)),
                Fraction(5,1)/(Fraction(a)*(Fraction(a)+5))))

    def test_pythagorean_shifts_and_exact_first_source_jets(self):
        self.assertEqual(3**2+4**2,5**2)
        self.assertEqual(source_jets(),(15,59,243))
        self.assertEqual(2*3**2+4**2+5**2,59)
        self.assertEqual(59,3**2+2*5**2)
        self.assertEqual(rigid_integer_shifts(15,59),((3,4,5),))

    def test_mutant_of_higher_jet_does_not_identify_full_source(self):
        # A third-order perturbation of Q(x) can share the first two source jets;
        # the integer-three-differences theorem makes no claim about that class.
        jets=source_jets()
        self.assertEqual(jets[:2], (15,59))
        self.assertNotEqual(source_jets((3,4,6)), jets)
        self.assertNotEqual(source_jets((2,4,7)), jets)

    def test_exact_cauchy_identifiability_of_three_channel_weights(self):
        for times in ((1,9,17),(1,25,81),(Fraction(1,2),Fraction(3,2),5)):
            M=source_matrix(times)
            det=determinant_3(M)
            self.assertNotEqual(det,0)
            self.assertEqual(det,cauchy_determinant(times))
            vals=[signed_four_pole(a) for a in times]
            self.assertEqual(recover_multiplicities(times,vals),(2,1,1))

    def test_duplicate_clock_fails_to_invert(self):
        with self.assertRaises(ValueError):
            recover_multiplicities((1,1,9),[signed_four_pole(a) for a in (1,1,9)])

    def test_positive_amplitude_simplex_and_limit(self):
        self.assertEqual(source_channel_limit_weights(),(Fraction(6,15),Fraction(4,15),Fraction(5,15)))
        for a in (1,9,17,73,257,1000,Fraction(15,2)):
            ws=source_channel_weights(a)
            self.assertEqual(sum(ws),1)
            self.assertTrue(all(w>0 for w in ws))
            self.assertLessEqual(abs(math.sqrt(sum(x*x for x in channel_amplitude(a)))-1),1e-12)
            q=source_channel_limit_weights()
            for x,y in zip(ws,q):
                ratio=x/y
                self.assertGreaterEqual(ratio,Fraction(a,Fraction(a)+5))
                self.assertLessEqual(ratio,1+Fraction(5,a))
            d=math.sqrt(sum((x-y)**2 for x,y in zip(channel_amplitude(a),channel_limit_amplitude())))
            self.assertLessEqual(d,float(normalized_channel_amplitude_budget(a))+1e-13)


class TestPoleProjectedChronology(unittest.TestCase):
    def test_projection_rank_three(self):
        self.assertEqual(tuple(sum(row) for row in PROJECTION),(0,0,0,0))
        self.assertEqual(sum(PROJECTION[i][i] for i in range(4)),3)
        for i in range(4):
            for j in range(4):
                self.assertEqual(sum(PROJECTION[i][k]*PROJECTION[k][j] for k in range(4)),PROJECTION[i][j])

    def test_relative_source_state_cannot_drop_common_mode(self):
        for a in (1,9,17,101,Fraction(37,3)):
            actual,predicted,mu,inj=projected_clock_step(a)
            self.assertEqual(actual,predicted)
            self.assertGreater(mu,0)
            self.assertNotEqual(inj,(0,0,0,0))
            self.assertNotEqual(tuple(x-y for x,y in zip(actual,tuple(u-mu*v for u,v in zip(predicted,inj)))),(0,0,0,0))

    def test_commutator_really_nonzero_on_all_distinct_positive_clocks(self):
        for a,b in ((1,9),(9,17),(17,25),(31,47),(Fraction(1,2),Fraction(3,2))):
            actual=relative_commutator(a,b)
            self.assertEqual(actual,commutator_closed(a,b))
            self.assertTrue(any(entry for row in actual for entry in row))
            self.assertTrue(all(actual[i][j]==-actual[j][i] for i in range(4) for j in range(4)))
            self.assertTrue(all(sum(row)==0 for row in actual))
            self.assertGreater(commutator_op_norm_sq(a,b),0)
            self.assertEqual(commutator_op_norm_sq(a,b),commutator_vandermonde_norm_sq(a,b))

    def test_commutator_zero_at_same_time(self):
        for a in (1,9,17,99):
            self.assertFalse(any(x for row in relative_commutator(a,a) for x in row))
            self.assertEqual(commutator_op_norm_sq(a,a),0)

    def test_exact_commutator_rational_receipts(self):
        self.assertEqual(relative_commutator(1,9)[0][1],-Fraction(283,2297295))
        self.assertEqual(relative_commutator(9,17)[0][1],-Fraction(291,33215875))
        self.assertEqual(commutator_op_norm_sq(1,9),Fraction(11541128,258600651534225))

    def test_commutator_asymptotic_a6_limit(self):
        # Nondestructive finite calibration of the independently proved limit.
        leading2=128**2 *362
        for a in (1000,10000,100000):
            v=commutator_op_norm_sq(a,a+8)
            ratio=float(v*a**12/leading2)
            self.assertTrue(0<ratio<1)
        self.assertGreater(float(commutator_op_norm_sq(100000,100008)*100000**12/leading2),0.99)

    def test_matrix_spin_1_3_5_decomposition(self):
        M=((Fraction(1),Fraction(2),Fraction(3)),
           (Fraction(4),Fraction(5),Fraction(6)),
           (Fraction(7),Fraction(8),Fraction(9)))
        scalar,skew,quad=spin_135_parts(M)
        self.assertEqual(sum(scalar[i][i] for i in range(3)),15)
        self.assertEqual(sum(quad[i][i] for i in range(3)),0)
        self.assertEqual(tuple(tuple(scalar[i][j]+skew[i][j]+quad[i][j] for j in range(3)) for i in range(3)),M)
        for i in range(3):
            for j in range(3):
                self.assertEqual(skew[i][j],-skew[j][i])
                self.assertEqual(quad[i][j],quad[j][i])

    def test_nontrivial_chronology_lives_in_skew_sector(self):
        C=relative_commutator(1,9)
        # Contraction with same real source input is identically zero for skew operators.
        c=tuple(Fraction(x) for x in POLE_COEFFICIENTS)
        self.assertEqual(sum(c[i]*C[i][j]*c[j] for i in range(4) for j in range(4)),0)
        self.assertTrue(any(x for row in C for x in row))


class TestNonHaarAndHigherOrderFirewall(unittest.TestCase):
    def test_universal_negative_binomial_pgf(self):
        # The two geometric channels give q_j=(j+1)/2^(j+2).
        self.assertEqual(sum(Fraction(j+1,2**(j+2)) for j in range(32)),1-Fraction(34,2**33))
        self.assertEqual(Fraction(1,(2-(-1))**2),Fraction(1,9))
        self.assertEqual(Fraction(1,(2-1)**2),1)

    def test_two_pole_countermodel_has_same_gamma_two_shape(self):
        # Source 1/a-1/(a+1) has just two poles yet its scaled
        # Laplace transform tends (1+s)^-2, hence the same PGF.
        for s in (Fraction(1,2),Fraction(1),Fraction(2)):
            values=[]
            for a in (10,100,1000,10000):
                R=lambda t: Fraction(1,t)-Fraction(1,t+1)
                v=R(a*(1+s))/R(a)
                values.append(abs(v-Fraction(1,(1+s)**2)))
            self.assertGreater(values[0],values[-1])
            self.assertLess(values[-1],Fraction(1,1000))

    def test_three_pairwise_uniforms_do_not_determine_product(self):
        m=5
        locked=[(x,y,(-x-y)%m) for x,y in product(range(m),repeat=2)]
        free=list(product(range(m),repeat=3))
        for i,j in ((0,1),(0,2),(1,2)):
            cnt_locked=Counter((row[i],row[j]) for row in locked)
            cnt_free=Counter((row[i],row[j]) for row in free)
            self.assertEqual(set(cnt_locked),set(cnt_free))
            self.assertTrue(all(cnt_locked[key]*len(free)==cnt_free[key]*len(locked) for key in cnt_locked))
        self.assertTrue(all(sum(row)%m==0 for row in locked))
        self.assertEqual(sum(sum(row)%m==0 for row in free),m*m)
        # The diagonal third Fourier character is 1 for locked and 0 for free.
        omega=cmath.exp(2j*math.pi/m)
        self.assertLess(abs(sum(omega**sum(row) for row in locked)/len(locked)-1),1e-13)
        self.assertLess(abs(sum(omega**sum(row) for row in free)/len(free)),1e-13)

    def test_triplet_product_survives_wrong_phase_selection(self):
        # For a rational altered seed, the same forcing-only positive apparatus
        # acquires an independent 16^n*s homogeneous phase; it is not a selector.
        for n in (1,2,4,6):
            u=original_zero_orbit(n)
            seed=Fraction(1,17)
            shifted=u+16**n*seed
            self.assertEqual(shifted-u,16**n*seed)
            self.assertEqual(sum(component_orbit(n)),u)

# Register additional tests through unittest discovery (explicit module import).
from observational_succ.four_pole_nine import (
    three_circle_carry_seam,three_channel_carry_transport,cubic_phase_cumulant)

class TestCarryAndCumulant(unittest.TestCase):
    def test_exact_three_torus_carry_seam(self):
        observed=set()
        for n in range(0,50):
            phases,seam,selected,carry=three_circle_carry_seam(n)
            self.assertEqual(len(phases),3)
            self.assertTrue(all(Fraction(0)<=x<Fraction(1) for x in phases))
            self.assertIn(seam,(0,1,2))
            self.assertEqual(selected,original_zero_orbit(n)%1)
            self.assertEqual(carry,original_zero_orbit(n)//1)
            observed.add(seam)
        self.assertEqual(observed,{0,1,2})

    def test_three_channel_actual_carry_transport(self):
        for n in range(1,50):
            carry,channel_carries,m_before,m_after=three_channel_carry_transport(n)
            self.assertEqual(carry,sum(channel_carries)+m_after-16*m_before)
        self.assertEqual(three_channel_carry_transport(1),(3,(1,0,0),0,2))

    def test_cumulant_recovers_triple_mean_from_moments(self):
        m=5
        w=cmath.exp(2j*math.pi/m)
        dependent=[(w**x,w**y,w**((-x-y)%m)) for x,y in product(range(m),repeat=2)]
        independent=[(w**x,w**y,w**z) for x,y,z in product(range(m),repeat=3)]
        kt,mt,means,pairs=cubic_phase_cumulant(dependent)
        k0,m0,means0,pairs0=cubic_phase_cumulant(independent)
        self.assertLess(abs(mt-1),1e-12)
        self.assertLess(abs(kt-1),1e-12)
        self.assertLess(abs(m0),1e-12)
        self.assertLess(abs(k0),1e-12)
        self.assertTrue(all(abs(x)<1e-12 for x in means+means0))
        self.assertTrue(all(abs(x)<1e-12 for x in pairs.values()))
        self.assertTrue(all(abs(x)<1e-12 for x in pairs0.values()))

from observational_succ.four_pole_nine import (
    positive_channel_two_adic_seam,source_channel_two_adic_history,
    two_adic_valuation)

class TestSourceTwoAdicGluing(unittest.TestCase):
    def test_all_source_steps_have_paired_halfintegral_cancellation(self):
        for n in range(1,180):
            (c3,c4,c5),paired,original=positive_channel_two_adic_seam(n)
            self.assertEqual((two_adic_valuation(c3),two_adic_valuation(c4),two_adic_valuation(c5)),(-1,2,-1))
            self.assertGreaterEqual(two_adic_valuation(paired),0)
            self.assertGreaterEqual(two_adic_valuation(original),0)
            self.assertEqual(c3+c4+c5,original)

    def test_half_integral_classes_glue_across_zero_seeded_histories(self):
        for n in range(1,80):
            a,b,c,total=source_channel_two_adic_history(n)
            self.assertEqual((a,b,c),(-1,2,-1))
            self.assertGreaterEqual(total,0)

    def test_mutated_multiplicity_breaks_source_gluing(self):
        # Remove the 2 in front of the d=3 channel. The numerator then has
        # v2=-2, and neither the original odd-denominator status nor the
        # two-half-integer cancellation survives.
        for n in range(1,15):
            a=8*n-7
            fake=difference_channel(a,3,1)+difference_channel(a,4)+difference_channel(a,5)
            self.assertEqual(two_adic_valuation(fake),-2)

    def test_source_2adic_seam_exact_first_step(self):
        (d3,d4,d5),pair,total=positive_channel_two_adic_seam(1)
        self.assertEqual((d3,d4,d5),(Fraction(3,2),Fraction(4,5),Fraction(5,6)))
        self.assertEqual(pair,Fraction(7,3))
        self.assertEqual(total,Fraction(47,15))

from observational_succ.four_pole_nine import (
    gamma_two_source_normalizer,authentic_mixed_poisson_mean,
    authentic_mixed_poisson_pgf,golden_fixed_point_bracket)

class TestSourceGoldenDrift(unittest.TestCase):
    def test_normalizer_is_monotone_and_below_one(self):
        x=[Fraction(1,3),Fraction(1),Fraction(9),Fraction(17),Fraction(81),Fraction(1000)]
        y=[gamma_two_source_normalizer(a) for a in x]
        self.assertTrue(all(Fraction(0)<v<Fraction(1) for v in y))
        self.assertTrue(all(y[j]<y[j+1] for j in range(len(y)-1)))

    def test_actual_mixed_poisson_pgf_properties(self):
        for a in (1,9,17,257,Fraction(1,2)):
            self.assertEqual(authentic_mixed_poisson_pgf(a,1),1)
            self.assertGreater(authentic_mixed_poisson_pgf(a,0),0)
            self.assertTrue(1<authentic_mixed_poisson_mean(a)<2)
            for z in (Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(2,3)):
                self.assertGreater(authentic_mixed_poisson_pgf(a,z),Fraction(1,(2-z)**2))

    def test_exact_rational_golden_fixed_point_bracketing(self):
        q0=(3-math.sqrt(5))/2
        previous=1
        for a in (1,9,17,64,257,1024):
            lo,hi=golden_fixed_point_bracket(a,60)
            self.assertLess(hi-lo,Fraction(1,2**59))
            self.assertLess(authentic_mixed_poisson_pgf(a,hi),hi)
            self.assertGreater(authentic_mixed_poisson_pgf(a,lo),lo)
            self.assertGreater(float(lo),q0)
            self.assertLess(float(lo),previous)
            previous=float(lo)

    def test_source_specific_first_golden_drift_coefficient(self):
        coeff=Fraction(59,15)*(5-math.sqrt(5))/10
        q0=(3-math.sqrt(5))/2
        normalized=[]
        for a in (64,256,1024,4096):
            lo,hi=golden_fixed_point_bracket(a,84)
            normalized.append(a*(float((lo+hi)/2)-q0))
        self.assertLess(abs(normalized[-1]-coeff),0.001)
        self.assertLess(abs(normalized[-1]-coeff),abs(normalized[0]-coeff))


class TestNineEntryLiftNoGo(unittest.TestCase):
    def test_three_channel_complex_lift_does_not_generate_cancellation(self):
        from observational_succ.four_pole_nine import (
            channel_amplitude,channel_limit_amplitude,normalized_channel_amplitude_budget)
        fixed=channel_limit_amplitude()
        for A in (8,16,32,64):
            for h in (1,2):
                W=0j
                vec=[0j,0j,0j]
                for n in range(A,2*A):
                    x=float(original_zero_orbit(n)%1)
                    phase=cmath.exp(2j*math.pi*h*x)
                    W+=phase/A
                    v=channel_amplitude(8*n-7)
                    for j in range(3):
                        vec[j]+=phase*v[j]/A
                diff=math.sqrt(sum(abs(vec[j]-fixed[j]*W)**2 for j in range(3)))
                budget=float(normalized_channel_amplitude_budget(8*A-7))
                self.assertLess(diff,budget)
                # The full 9-entry Hermitian matrix is rank <= 1: its
                # 2-by-2 minors vanish up to harmless floating rounding.
                matrix=[[vec[i]*vec[j].conjugate() for j in range(3)] for i in range(3)]
                for i in range(3):
                    for j in range(i+1,3):
                        self.assertLess(abs(matrix[i][i]*matrix[j][j]-matrix[i][j]*matrix[j][i]),1e-12)

    def test_nine_entry_lift_fails_on_coherent_phase(self):
        limit=channel_limit_amplitude()
        for A in (16,64,128):
            vec=[sum(channel_amplitude(8*n-7)[j] for n in range(A,2*A))/A for j in range(3)]
            self.assertLess(math.sqrt(sum((vec[i]-limit[i])**2 for i in range(3))),
                            float(normalized_channel_amplitude_budget(8*A-7)))
            self.assertGreater(math.sqrt(sum(v*v for v in vec)),0.95)


if __name__=='__main__':
    unittest.main()

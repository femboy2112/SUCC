"""Exact adversarial cyclotomic SUCC origin-frame and BBP source tests."""
import unittest
from fractions import Fraction as Q
from math import gcd,lcm,comb

from observational_succ.cyclotomic_gauge_frames import (
    cyclotomic_value, multiplicative_order, least_clock_modulus,
    effective_frame_period, gauge_chart_step, literal_chart_symmetry,
    relative_path, arc_distance, cyclotomic_frame_character,
    twirl_entry, twirl_mask, twirl_matrix, fusion_mask,
    period_class_sizes, lag_index_pairs, harmonic_depth,
    phase_modulation_samples, positive_energy_signature,
    direct_symbolic_lag_terms, twirled_laurent_terms,
    discrete_fourier_probe, forced_lag_rational_phases,
    bbp_signed_lag_budget, bbp_energy_budget,
    mobius, exact_period_point_count, cyclic_necklace_count,
    certified_origin_energy_interval,
)
from observational_succ.pi_source_genesis import forced_states
from observational_succ.bbp_source_memory import forcing


class GaugeSemantics(unittest.TestCase):
    def test_circle_origin_is_conjugacy_not_universal_commutation(self):
        for base in (2,3,16):
            for origin in (Q(),Q(1,7),Q(1,base-1)):
                for x in (Q(3,10),Q(2,7),Q(1,2)):
                    chart = (x-origin)%1
                    self.assertEqual(gauge_chart_step(base,origin,chart),
                                     (base*x-origin)%1)
            self.assertTrue(literal_chart_symmetry(base,Q(1,base-1)))
        self.assertFalse(literal_chart_symmetry(16,Q(1,7)))
        self.assertTrue(literal_chart_symmetry(16,Q(1,15)))
        self.assertEqual(sum(literal_chart_symmetry(16,Q(k,15))
                             for k in range(15)),15)

    def test_actual_translated_paths_are_not_same_physical_orbit(self):
        for n in range(12):
            d=relative_path(16,Q(1,3)+Q(1,7),Q(1,3),n)
            self.assertEqual(d,pow(16,n,7)*Q(1,7)%1)
            self.assertEqual(d,relative_path(16,Q(1,7),Q(),n))
            self.assertLessEqual(arc_distance(d),Q(1,2))
        self.assertEqual(relative_path(16,Q(1,3),Q(),12),Q(1,3))
        self.assertEqual(relative_path(16,Q(1,17),Q(),1),Q(16,17))
        self.assertEqual(relative_path(16,Q(1,17),Q(),2),Q(1,17))

    def test_bbp_forcing_is_covariant_under_chart_translation(self):
        origin=Q(2,7)
        states=forced_states(12)
        for n in range(12):
            z=(states[n]-origin)%1
            next_chart=(16*z+15*origin+forcing(n+1))%1
            self.assertEqual(next_chart,(states[n+1]-origin)%1)
        # Taking the same forcing but CHANGING INITIAL y0 creates a
        # different selected physical orbit, not simply a chart.
        altered=forced_states(3,initial=origin)
        self.assertNotEqual(altered[1],(states[1]-origin)%1)

    def test_parameter_guards(self):
        for bad in (True,1.0,-1):
            with self.assertRaises(ValueError):
                cyclotomic_value(16,bad)
        with self.assertRaises(ValueError):
            multiplicative_order(16,16)


class CyclotomicClockArithmetic(unittest.TestCase):
    def test_exact_integer_cyclotomic_factorization(self):
        known={1:15,2:17,3:273,4:257,5:69905,6:241}
        for d,v in known.items():
            self.assertEqual(cyclotomic_value(16,d),v)
            product=1
            for e in range(1,d+1):
                if d%e==0:
                    product*=cyclotomic_value(16,e)
            self.assertEqual(product,16**d-1)
        self.assertEqual(gcd(15,273),3)
        self.assertEqual(15*273,16**3-1)
        # Distinct cyclotomic evaluations are NOT automatically coprime!
        self.assertNotEqual(lcm(15,273),16**3-1)

    def test_minimal_period_clocks_against_independent_order(self):
        minimal={1:3,2:17,3:7,4:257,5:11,6:119,7:29}
        for d,q in minimal.items():
            self.assertEqual(least_clock_modulus(16,d,1000),q)
            self.assertEqual(multiplicative_order(16,q),d)
            self.assertEqual((16**d-1)%q,0)
            for k in range(2,q):
                if gcd(k,16)==1:
                    self.assertNotEqual(multiplicative_order(16,k),d)
        self.assertEqual(119,7*17)
        self.assertEqual(lcm(multiplicative_order(16,7),
                             multiplicative_order(16,17)),6)
        self.assertNotEqual(cyclotomic_value(16,6)%119,0)
        with self.assertRaises(ValueError):
            least_clock_modulus(16,8,1000)

    def test_character_orthogonality_and_frequency_aliases(self):
        for q,d in ((7,3),(11,5),(17,2),(119,6)):
            for h in (1,2,3,7):
                eff=effective_frame_period(16,q,h)
                for j in range(14):
                    for k in range(14):
                        self.assertEqual(twirl_entry(16,q,h,j,k),
                                         int((j-k)%eff==0))
                self.assertEqual(twirl_entry(16,q,h,0,d),1)
        self.assertEqual(effective_frame_period(16,7,7),1)
        self.assertEqual(effective_frame_period(16,7,0),1)
        self.assertEqual(tuple(cyclotomic_frame_character(16,7,1,j)
                               for j in range(6)),(1,2,4,1,2,4))

    def test_tensor_fusion_and_non_coprime_compatibility(self):
        for n in (1,4,10,14):
            self.assertTrue(fusion_mask(16,7,17,1,n))
            self.assertTrue(fusion_mask(16,15,273,1,n))
        self.assertEqual(twirl_mask(16,119,1,14),
                         tuple(tuple(int((i-j)%6==0) for j in range(14))
                               for i in range(14)))
        A=tuple(tuple(i*13+j for j in range(14)) for i in range(14))
        t7=twirl_matrix(A,16,7,1)
        t17=twirl_matrix(t7,16,17,1)
        self.assertEqual(t17,twirl_matrix(A,16,119,1))
        self.assertEqual(t17,twirl_matrix(t17,16,119,1))
        with self.assertRaises(ValueError):
            twirl_matrix(((1,2,3),(4,5,6)),16,7,1)

    def test_periodic_point_necklace_counts(self):
        self.assertEqual((mobius(1),mobius(4),mobius(6)),(1,0,1))
        self.assertEqual(exact_period_point_count(16,1),15)
        self.assertEqual(exact_period_point_count(16,2),240)
        self.assertEqual(exact_period_point_count(16,3),4080)
        self.assertEqual(cyclic_necklace_count(16,3),1360)
        for d in range(1,7):
            self.assertEqual(sum(exact_period_point_count(16,e)
                                 for e in range(1,d+1) if d%e==0),16**d-1)


class SignedLagReconstruction(unittest.TestCase):
    def test_complete_root_frame_gram_partition(self):
        for q,d in ((7,3),(11,5),(17,2),(119,6)):
            n=21
            mask=twirl_mask(16,q,1,n)
            for i in range(n):
                for j in range(n):
                    self.assertEqual(mask[i][j],int(i%d==j%d))
            self.assertEqual(sum(mask[i][i] for i in range(n)),n)

    def test_symbolic_laurent_positive_and_negative_phase_memory(self):
        for period in (1,2,3,5,9):
            for n in (0,1,3,8,17):
                L=harmonic_depth(n,period)
                coeff=twirled_laurent_terms(n,period)
                self.assertEqual(sorted(coeff),list(range(-L,L+1)))
                self.assertEqual(coeff[0],tuple((j,j) for j in range(n)))
                for ell in range(1,L+1):
                    self.assertEqual(coeff[ell],
                                     tuple((j+ell*period,j)
                                           for j in range(n-ell*period)))
                    self.assertEqual(coeff[-ell],
                                     tuple((k,j) for j,k in coeff[ell]))
                    self.assertEqual(discrete_fourier_probe(n,period,ell),
                                     coeff[ell])
                if L:
                    with self.assertRaises(ValueError):
                        discrete_fourier_probe(n,period,L,2*L)

    def test_dft_has_minimum_alias_free_sample_count(self):
        n,d=10,3
        self.assertEqual(harmonic_depth(n,d),3)
        self.assertEqual(phase_modulation_samples(n,d),7)
        self.assertEqual(len(discrete_fourier_probe(n,d,1)),7)
        self.assertEqual(len(discrete_fourier_probe(n,d,2)),4)
        self.assertEqual(len(discrete_fourier_probe(n,d,3)),1)
        self.assertEqual(len(discrete_fourier_probe(n,d,0)),10)

    def test_hair_haar_variance_requires_nonzero_character(self):
        for period in (1,2,3,5,12):
            for n in range(2,15):
                stats=positive_energy_signature(n,period,1)
                pairs=[(j,k) for k in range(n) for j in range(k+1,n)
                       if (j-k)%period==0]
                diffs={16**j-16**k for j,k in pairs}
                self.assertEqual(len(diffs),len(pairs))
                self.assertEqual(stats["pairs"],len(pairs))
                self.assertEqual(stats["haar_variance"],2*len(pairs))
                self.assertEqual(stats["fixed_point_energy"],
                                 n+2*len(pairs))
        with self.assertRaises(ValueError):
            positive_energy_signature(9,3,0)

    def test_frame_oversampling_fakes_subquadratic_normality(self):
        for n in (8,16,64):
            d=n
            stats=positive_energy_signature(n,d)
            self.assertEqual(stats["fixed_point_energy"],n)
            self.assertEqual(stats["haar_variance"],0)
            self.assertEqual(stats["harmonic_depth"],0)
            self.assertEqual(Q(stats["fixed_point_energy"],n*n),Q(1,n))
        # Even orbit x=0 or 1/3 (both nonnormal base 16) has
        # normalized E -> 0 along d_N=N. It is a FALSE normality probe.

    def test_true_bbp_signed_source_phase_transport(self):
        n,d=10,3
        phases=forced_lag_rational_phases(n,d,1,1)
        self.assertEqual(len(phases),n-d)
        y=forced_states(n)
        self.assertEqual(phases,
                         tuple((y[j+d+1]-y[j+1])%1 for j in range(n-d)))
        self.assertEqual(len(forced_lag_rational_phases(n,d,4,1)),0)
        for ell in (1,2,3):
            bound=bbp_signed_lag_budget(n,d,ell,1)
            self.assertTrue(Q(0)<bound<=Q(2,15))
        self.assertEqual(bbp_energy_budget(n,d,1),
                         2*sum(bbp_signed_lag_budget(n,d,ell,1)
                               for ell in range(1,4)))
        self.assertEqual(bbp_energy_budget(6,7,1),Q())

    def test_certified_pi_signed_energy_not_artificial_hair(self):
        n,d=7,3
        b=certified_origin_energy_interval(1,n,d,source="bbp")
        m=certified_origin_energy_interval(1,n,d,source="machin")
        f=certified_origin_energy_interval(1,n,d,source="forced")
        self.assertLessEqual(b[0],b[1])
        self.assertLessEqual(m[0],m[1])
        self.assertLessEqual(f[0],f[1])
        self.assertLessEqual(max(b[0],m[0]),min(b[1],m[1]))
        # New genuinely pi-selected FINITE certificate, paid by TWO
        # independent source enclosures (BBP and Machin), NOT a limit.
        lower,upper=Q(199199,50000),Q(498,125)
        for source_interval in (b,m):
            self.assertGreater(source_interval[0],lower)
            self.assertLess(source_interval[1],upper)
        self.assertEqual(positive_energy_signature(7,3)["fixed_point_energy"],17)
        bound=bbp_energy_budget(n,d)
        self.assertLessEqual(max(Q(),b[0]-f[1],f[0]-b[1]),bound)
        self.assertEqual(certified_origin_energy_interval(0,10,3),
                         (Q(34),Q(34)))
        with self.assertRaises(ValueError):
            certified_origin_energy_interval(1,7,3,source="invented")


if __name__=="__main__":
    unittest.main()

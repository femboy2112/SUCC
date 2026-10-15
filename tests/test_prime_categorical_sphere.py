"""Source-typed exact rational crucible for the prime categorical sphere prototype.

Mathematical proofs are in the dossier. Tests check independent finite oracles
and hostile mutations, never nontrivial zeta-zero locations.
"""
import unittest
from fractions import Fraction as Q
from math import comb, gcd, pi

from observational_succ.prime_categorical_sphere import (
    SphereError, is_prime, source_prime, factorization, valuation, base_p_carries,
    pascal_source, pascal_local_cancellation, fixed_precision_obstruction,
    gamma_chart, gamma_mode, gamma_prime_transport, chi4,
    gamma_bath_weight, gamma_dilation_certificate, sieve_coefficient,
    sieve_certificate, original_suzuki_chart_transport, ou_gram_dyadic,
    ldlt_positive, heat_bath_dyadic_interval, categorical_sphere_faces,
    sphere_homology_receipt, prime_phase_equator_action, chiral_mode_symbol,
    chiral_symbol_interval, chiral_diagonal_interval, chiral_finite_gram,
    gamma_chiral_identity_receipt, chiral_Hminus1_certificate,
    affine_gamma_source_intertwiner, chiral_markov_model_certificate,
    poisson_unit_mean_tail_bound, finite_markov_sphere_energy,
    two_hemisphere_gaussian_fourier, receipt,
)


class PrimeSphereTests(unittest.TestCase):
    def test_01_true_primality_negative_six(self):
        self.assertEqual([p for p in range(2,50) if is_prime(p)],
                         [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
        for n in (4,6,9,21,25,49):
            with self.assertRaises(SphereError):source_prime(n)
        for bad in (1,0,-3,2.0,True):
            with self.assertRaises(SphereError):source_prime(bad)

    def test_02_source_prime_factor_oracle(self):
        for n in range(1,300):
            factors=factorization(n)
            val=1
            for p,k in factors.items():
                self.assertTrue(is_prime(p))
                self.assertEqual(valuation(n,p),k)
                val*=p**k
            self.assertEqual(val,n)

    def test_03_all_small_pascal_carries(self):
        for n in range(0,34):
            for k in range(n+1):
                d=pascal_source(n,k)
                self.assertEqual(d['binomial'],comb(n,k))
                self.assertEqual(d['probability'],Q(comb(n,k),2**n))
                self.assertTrue(d['source_product_formula_exact'])
                for p in range(2,n+1):
                    if is_prime(p):
                        self.assertEqual(base_p_carries(k,n-k,p),
                                         valuation(comb(n,k),p))

    def test_04_large_binomial_source_no_practical_proof_omega(self):
        d=pascal_source(256,128)
        self.assertGreater(d['binomial'].bit_length(),250)
        self.assertIn(2,d['Kummer_prime_carries'])
        self.assertTrue(d['source_product_formula_exact'])

    def test_05_pascal_local_cancellation_phase_is_necessary(self):
        x=pascal_local_cancellation(2,1,2)
        self.assertEqual(x['parent_valuations'],(0,0))
        self.assertEqual(x['child_valuation'],1)
        self.assertEqual(x['cancellation_excess'],1)
        self.assertTrue(x['needs_residue_phase'])
        y=pascal_local_cancellation(6,3,5)
        self.assertGreaterEqual(y['child_valuation'],min(y['parent_valuations']))

    def test_06_precision_ghosts_all_primes(self):
        for p in (2,3,5,7):
            for r in range(1,9):
                d=fixed_precision_obstruction(p,r)
                self.assertEqual(d['sum_valuations'],(r,r+1))
                self.assertEqual(d['second_parent']%p**r,
                                 d['aliased_parent']%p**r)

    def test_07_gamma_sector_unique_chart(self):
        for n in range(1,1200):
            e,r,j=gamma_chart(n)
            self.assertEqual(gamma_mode(e,r,j),n)
            self.assertEqual(r,(n//(2**e))%4)
            self.assertEqual(gamma_bath_weight(n),Q(4,n*n))

    def test_08_gamma_prime_actual_transport(self):
        for e in range(3):
            for r in (1,3):
                for j in range(9):
                    for p in (2,3,5,7,11,13):
                        d=gamma_prime_transport(e,r,j,p)
                        self.assertEqual(gamma_mode(*d['to']),p*gamma_mode(e,r,j))
                        self.assertEqual(d['orientation_character'],chi4(p))

    def test_09_gamma_prime_composition_diamond(self):
        for r in (1,3):
            for j in range(7):
                for p,q in ((2,3),(3,5),(5,7),(2,11),(3,13)):
                    pq=gamma_prime_transport(*gamma_prime_transport(0,r,j,p)['to'],q)['to']
                    qp=gamma_prime_transport(*gamma_prime_transport(0,r,j,q)['to'],p)['to']
                    self.assertEqual(pq,qp)
                    self.assertEqual(gamma_mode(*pq),p*q*(4*j+r))

    def test_10_gamma_half_density_dilation(self):
        for n in (1,2,3,5,7,13,17,25):
            for p in (2,3,5,7):
                c=gamma_dilation_certificate(n,p)
                self.assertEqual(c['renormalized_kernel_weight'],
                                 c['target_kernel_weight'])
                self.assertEqual(c['alpha_target'],p*c['alpha_source'])
                self.assertTrue(c['true_half_density_transport'])

    def test_11_gamma_original_plus_exit(self):
        for p in (2,3,5,7,11,13):
            d=original_suzuki_chart_transport(p,201)
            self.assertEqual(d['original_chart_invariant'],p%4==1)
            self.assertTrue(d['source_complete_mode_inclusion_verified'])
            self.assertEqual(d['spectral_indices_in_target'],
                             [p*n for n in range(1,202) if n%4==1 and p*n<=201])

    def test_12_source_authenticated_euler_sieves(self):
        for primes in ((2,), (3,), (2,3),(2,3,5),(3,5,7),(5,13)):
            d=sieve_certificate(primes,80)
            m=1
            for p in primes:m*=p
            self.assertIsNone(d['first_negative'])
            self.assertTrue(d['genuine_Euler_primitive_source'])
            for n,c in d['coefficients'].items():
                self.assertEqual(c,int(gcd(n,m)==1))

    def test_13_overlapping_sieve_negative_control(self):
        s=sieve_certificate((2,6),40,require_primes=False)
        self.assertEqual(s['coefficients'][6],-1)
        self.assertEqual(s['first_negative'],6)
        self.assertFalse(s['all_resolvent_weights_positive_or_zero'])
        t=sieve_certificate((2,2),20,require_primes=False)
        self.assertEqual(t['coefficients'][2],-1)
        with self.assertRaises(SphereError):sieve_certificate((2,6),40)
        with self.assertRaises(SphereError):sieve_certificate((3,3),40)

    def test_14_coprime_composites_not_euler(self):
        t=sieve_certificate((4,9),80,require_primes=False)
        self.assertTrue(t['all_resolvent_weights_positive_or_zero'])
        self.assertFalse(t['genuine_Euler_primitive_source'])
        with self.assertRaises(SphereError):sieve_certificate((4,9),80)

    def test_15_actual_ou_kernel_rational_lattice(self):
        # At x_j=2*j*log(2), alpha=n/2 => e^-alpha|x_i-x_j|=2^(-n|i-j|).
        for chart in ('all','suzuki','companion'):
            for P in ((),(2,),(2,3)):
                g=ou_gram_dyadic(21,P,4,chart)
                self.assertEqual(g[0][0],g[-1][-1])
                self.assertEqual(g[0][1],g[1][2])
                self.assertTrue(all(d>0 for d in ldlt_positive(g)))

    def test_16_heat_gamma_dyadic_finite_interval(self):
        lo1,hi1=heat_bath_dyadic_interval(5)
        lo2,hi2=heat_bath_dyadic_interval(9)
        self.assertLessEqual(lo1,lo2)
        self.assertGreaterEqual(hi1,hi2)
        self.assertEqual(lo1,Q(4,2)+Q(4,5*2**25))
        self.assertLess(hi2-lo2,Q(1,10**10))

    def test_17_heat_companion_is_another_source(self):
        a,b=heat_bath_dyadic_interval(9,1,'suzuki')
        c,d=heat_bath_dyadic_interval(9,1,'companion')
        self.assertGreater(a,d)
        self.assertGreater(b,c)
        with self.assertRaises(SphereError):heat_bath_dyadic_interval(7,1,'fake')

    def test_18_toy_sphere_homology_and_boundary_squared_zero(self):
        g=categorical_sphere_faces()
        d=sphere_homology_receipt()
        self.assertEqual((d['V'],d['E'],d['F']),(6,12,8))
        self.assertEqual(d['Euler_characteristic'],2)
        self.assertEqual(d['Betti_Q'],(1,0,1))
        self.assertEqual(len(set(g['faces'])),8)
        self.assertFalse(d['arithmetic_source_realization_of_all_sphere_faces'])

    def test_19_odd_prime_spherical_degree_is_chi4(self):
        for p in (3,5,7,11,13,17,19,23,29):
            d=prime_phase_equator_action(p)
            self.assertEqual(d['degree_on_toy_S2'],chi4(p))
            self.assertTrue(d['top_homology_action_verified_on_integer_chains'])
            self.assertEqual(d['equator_permutation'],tuple(p*j%4 for j in range(4)))
        self.assertIsNone(prime_phase_equator_action(2)['degree_on_toy_S2'])

    def test_20_prime_equator_composition_orientation(self):
        for p,q in ((3,5),(3,7),(5,13),(7,11)):
            f=prime_phase_equator_action(p)['equator_permutation']
            g=prime_phase_equator_action(q)['equator_permutation']
            self.assertEqual(tuple(f[g[j]] for j in range(4)),
                             tuple((p*q*j)%4 for j in range(4)))
            self.assertEqual(chi4(p*q),chi4(p)*chi4(q))

    def test_21_chiral_modes_exact_fourier_rational(self):
        for xi in (Q(0),Q(1,3),Q(2),Q(9,4)):
            for n in (1,3,5,7,9,11):
                self.assertEqual(chiral_mode_symbol(n,xi),
                                 Q(4,n)/(Q(n*n,4)+xi*xi))
            for j in range(8):
                self.assertGreater(chiral_mode_symbol(4*j+1,xi),
                                   chiral_mode_symbol(4*j+3,xi))

    def test_22_chiral_positive_rational_intervals(self):
        for xi in (Q(0),Q(1,2),Q(2),Q(7,3),Q(10)):
            oldlo,oldhi=chiral_symbol_interval(xi,1)
            self.assertGreater(oldlo,0)
            for pairs in (2,3,5,9,15):
                lo,hi=chiral_symbol_interval(xi,pairs)
                self.assertGreaterEqual(lo,oldlo)
                self.assertLessEqual(hi,oldhi)
                oldlo,oldhi=lo,hi

    def test_23_chiral_fourier_zero_known_dirichlet_beta_identity(self):
        lo,hi=chiral_symbol_interval(0,35)
        expected=pi**3/2
        self.assertLess(float(lo),expected)
        self.assertGreater(float(hi),expected)
        self.assertLess(float(hi-lo),Q(1,15000))
        # Numeric pi is an independent calibration only, NOT proof authority.

    def test_24_chiral_catalan_normalization(self):
        lo,hi=chiral_diagonal_interval(80)
        try:
            import mpmath as mp
            mp.mp.dps=50
            expected=4*mp.catalan
            self.assertLess(mp.mpf(lo.numerator)/lo.denominator,expected)
            self.assertGreater(mp.mpf(hi.numerator)/hi.denominator,expected)
        except ImportError:
            self.assertTrue(Q(3)<lo<hi<Q(4))
        self.assertGreater(lo,0)

    def test_25_source_correct_signed_gamma_difference_is_PSD(self):
        for maxodd in (7,15,31,63):
            M=chiral_finite_gram(maxodd,5)
            self.assertTrue(all(v>0 for v in ldlt_positive(M)))
        self.assertTrue(gamma_chiral_identity_receipt()['suzuki_plus_minus_operator_PSD'])

    def test_26_chiral_bath_is_not_weil_positive(self):
        d=gamma_chiral_identity_receipt()
        self.assertFalse(d['full_suzuki_operator_sign_proved'])
        self.assertFalse(d['spectral_gap_uniform_in_frequency'])
        self.assertFalse(d['RH_proved'])

    def test_29_global_chiral_Hminus1_coercivity_rational_controls(self):
        for xi in (Q(0),Q(1,10),Q(1,2),Q(1),Q(2),Q(10),Q(100)):
            x=chiral_Hminus1_certificate(xi,10)
            self.assertTrue(x['source_analytic_global_bound_proved_in_dossier'])
            self.assertFalse(x['full_Weil_positivity'])
            self.assertLess(Q(x['Hminus1_lower']),Q(x['partial_interval'][0]))
            self.assertLess(Q(x['partial_interval'][1]),Q(x['Hminus1_upper']))

    def test_30_literal_integer_to_full_Gamma_mode_functor(self):
        for n in range(1,75):
            for p in (2,3,5,7,11):
                d=affine_gamma_source_intertwiner(n,p)
                self.assertEqual(d['succ_label'],Q(n+1,2))
                self.assertEqual(d['prime_dilation_label'],Q(p*n,2))
                self.assertEqual(d['affine_braid_left'],d['affine_braid_right'])
                self.assertTrue(d['integer_SUCC_and_FUCC_source_laws_preserved'])
                self.assertFalse(d['operator_intertwiner_constructed'])
        with self.assertRaises(SphereError):affine_gamma_source_intertwiner(3,6)

    def test_31_chiral_markov_dirichlet_form_and_finite_compiler(self):
        model=chiral_markov_model_certificate()
        self.assertEqual(model['jump_variance'],'pi^2')
        self.assertEqual(model['signed_chiral_differentiated_operator'],'pi*(I-P)')
        self.assertFalse(model['full_original_Weil_operator'])
        for v in ((Q(0),)*4,(Q(1),)*4,(Q(0),Q(1),Q(2),Q(3)),
                  (Q(-1,4),Q(1,7),Q(2,9),Q(-1,3))):
            energy=finite_markov_sphere_energy(v)
            self.assertEqual(Q(energy['quadratic']),Q(energy['edge_energy']))
            self.assertGreaterEqual(Q(energy['quadratic']),0)
            self.assertFalse(energy['same_kernel_as_continuum_sech'])
        old=Q(10)
        for K in range(0,12):
            new=poisson_unit_mean_tail_bound(K)
            self.assertLess(new,old)
            old=new

    def test_32_two_law_cones_share_one_real_Fourier_apex(self):
        for xi in (Q(0),Q(1,4),Q(1,2),Q(1)):
            old_gap=None
            for N in (8,16,32,64,128,256):
                d=two_hemisphere_gaussian_fourier(N,xi)
                self.assertLessEqual(d['Pascal_Fourier_lower'],
                                     d['common_Gaussian']+1e-14)
                self.assertLessEqual(d['common_Gaussian'],
                                     d['Gamma_chiral_Fourier_upper']+1e-14)
                gap=d['Gamma_chiral_Fourier_upper']-d['Pascal_Fourier_lower']
                if old_gap is not None:self.assertLessEqual(gap,old_gap+1e-14)
                old_gap=gap
            self.assertLess(old_gap,0.01)
        with self.assertRaises(SphereError):
            two_hemisphere_gaussian_fourier(2,Q(2))

    def test_27_full_receipt_has_no_zeros_and_no_ghost_sphere(self):
        d=receipt()
        self.assertTrue(d['no_nontrivial_zero_inputs'])
        self.assertFalse(d['RH_proved'])
        self.assertFalse(d['toy_sphere']['arithmetic_source_realization_of_all_sphere_faces'])
        self.assertEqual(d['sieve_overlap_2_6']['coefficients'][6],-1)

    def test_28_bad_source_inputs_refused(self):
        for bad in (0,-1,0.3,True):
            with self.assertRaises(SphereError):gamma_chart(bad)
        with self.assertRaises(SphereError):gamma_mode(0,2,0)
        with self.assertRaises(SphereError):gamma_prime_transport(0,1,0,6)
        with self.assertRaises(SphereError):chiral_symbol_interval(0.1)
        with self.assertRaises(SphereError):sieve_coefficient(0,(2,))


if __name__=='__main__':unittest.main()

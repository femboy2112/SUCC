"""Exact finite source/FUCC mathematics with fail-closed authentic adapter."""
from __future__ import annotations

from fractions import Fraction as F
import unittest

from observational_succ import finite_gamma_fucc_fredholm as A


class FredholmAlgebraTests(unittest.TestCase):
    def test_gamma_prefix_exact_8(self):
        self.assertGreater(A.gamma_scalar_prefix(8), F(25,4))
        self.assertEqual(A.gamma_scalar_prefix(8),F(63349408,10094175))

    def test_real_source_threshold_8(self):
        d=A.source_baseline_threshold(8,32)
        self.assertGreater(F(d['positive_swap_baseline_gap_strictly_greater']),F(3,8))
        self.assertLess(F(d['number_of_negative_Gamma_prefix_modes_strictly_less_than']),21)
        self.assertTrue(d['positive_compact_cell_lower_available'])
        self.assertFalse(d['full_source_sign_proved'])

    def test_threshold_bad_budget(self):
        for j,n in [(7,32),(8,1),(8,False),(1,500)]:
            with self.assertRaises(A.FredholmError):A.source_baseline_threshold(j,n)

    def test_cubic_over_all_first_prime_integer_shifts(self):
        for n in range(5,20):
            for shift in range(n//2+1,n):
                if not n/2 < shift: continue
                A.first_prime_partial_swap(n,shift)

    def test_wrong_first_prime_shift_rejected(self):
        for shift in [0,2,4,8]:
            with self.assertRaises(A.FredholmError):A.first_prime_partial_swap(8,shift)

    def test_exact_unshifted_inverse(self):
        swap=A.first_prime_partial_swap(4,3)
        inv=A.exact_swap_inverse(swap,F(2),F(1))
        self.assertEqual(inv[0][0],F(2,3))
        self.assertEqual(inv[0][3],F(1,3))
        self.assertEqual(inv[1][1],F(1,2))

    def test_swap_spectral_channels(self):
        swap=A.first_prime_partial_swap(8,5)
        e=[F(0)]*8;e[0]=e[5]=1
        o=[F(0)]*8;o[0]=1;o[5]=-1
        ce=[F(0)]*8;ce[3]=1
        self.assertEqual(A.apply(swap,e),tuple(e))
        self.assertEqual(A.apply(swap,o),tuple(-v for v in o))
        self.assertEqual(A.apply(swap,ce),tuple(F(0) for _ in ce))

    def test_cell_projection_destroys_exact_cubic(self):
        a=A.cell_compressed_shift(4,F(3,5))
        self.assertNotEqual(A.mul(A.mul(a,a),a),a)
        with self.assertRaises(A.FredholmError):A.exact_swap_inverse(a,2,F(1,4))

    def test_source_nonrational_phase_not_laundered(self):
        with self.assertRaises(A.FredholmError):A.cell_compressed_shift(8,F(1,2))
        with self.assertRaises(A.FredholmError):A.cell_compressed_shift(8,F(1))
        with self.assertRaises(A.FredholmError):A.cell_compressed_shift(8,0.7)

    def test_gamma_not_made_from_fake_FUCC(self):
        self.assertFalse(A.source_baseline_threshold(8,32)['RH_proved'])
        self.assertEqual(A.gamma_scalar_prefix(1),4)
        self.assertEqual(A.gamma_scalar_prefix(2),F(24,5))

    def test_exact_finite_positive_Fredholm(self):
        swap=A.first_prime_partial_swap(4,3)
        model=A.finite_gamma_fredholm_model(swap,1,F(1,2),A.scale(A.eye(4),F(3,4)),(1,0,0,1),(0,0,0,0))
        self.assertTrue(model['full_signed_positive'])
        self.assertTrue(model['compact_Birman_Schwinger_positive'])

    def test_exact_finite_negative_no_pole(self):
        swap=A.first_prime_partial_swap(4,3)
        model=A.finite_gamma_fredholm_model(swap,1,F(1,2),A.scale(A.eye(4),F(3,4)),(0,0,0,0),(0,0,0,0))
        self.assertFalse(model['full_signed_positive'])
        self.assertFalse(model['compact_Birman_Schwinger_positive'])

    def test_exact_negative_odd_pole(self):
        swap=A.first_prime_partial_swap(4,3)
        model=A.finite_gamma_fredholm_model(swap,2,F(1,2),A.scale(A.eye(4),F(1,2)),(0,0,0,0),(0,1,0,0))
        self.assertFalse(model['full_signed_positive'])

    def test_finite_spurious_RH_claim_rejected(self):
        swap=A.first_prime_partial_swap(4,3)
        model=A.finite_gamma_fredholm_model(swap,1,F(1,2),A.scale(A.eye(4),F(1,4)),(1,0,0,1),(0,0,0,0))
        self.assertFalse(model['RH_proved'])
        self.assertFalse(model['original_source_sign_proved'])

    def test_true_gamma_kernel_required_PSD(self):
        swap=A.first_prime_partial_swap(4,3)
        fake=A.scale(A.eye(4),F(-1))
        with self.assertRaises(A.FredholmError):A.finite_gamma_fredholm_model(swap,2,F(1,2),fake,(0,0,0,0),(0,0,0,0))

    def test_negative_wrong_cubic(self):
        swap=A.first_prime_partial_swap(4,3)
        bad=A.add(swap,A.eye(4),F(1,2))
        with self.assertRaises(A.FredholmError):A.finite_gamma_fredholm_model(bad,2,F(1,2),A.eye(4),(0,0,0,0),(0,0,0,0))

    def test_fraction_exp_encloses_basic_known_values(self):
        for x in [F(0),F(1,8),F(1,2),F(1),F(3,2),F(2),F(6)]:
            v=A.exp_minus_interval(x)
            self.assertGreater(v.lo,0)
            self.assertLessEqual(v.lo,v.hi)
            if x==0:self.assertEqual(v.lo,1)
            if x<=1:
                self.assertLessEqual(v.hi, 1/(1+x)+F(1,10**20))
                self.assertGreaterEqual(v.lo,1-x)

    def test_ou_cell_closed_forms(self):
        for offset in range(5):
            t=A.ou_cell_integral(F(1,2),F(1,4),offset)
            self.assertGreater(t.lo,0)
            self.assertLessEqual(t.lo,t.hi)
        self.assertLess(A.ou_cell_integral(F(1,2),F(1,4),4).hi,
                        A.ou_cell_integral(F(1,2),F(1,4),1).lo)

    def test_ou_cell_matrix_positive_trace_upper(self):
        m=A.gamma_cell_interval_matrix(2,4)
        lo=sum((m[i][i].lo for i in range(4)),F())
        hi=sum((m[i][i].hi for i in range(4)),F())
        self.assertTrue(0<lo<hi<2)
        self.assertEqual(m[0][1],m[2][3])

    def test_outward_exponential_mutant_rejected(self):
        with self.assertRaises(A.FredholmError):A.ou_cell_integral(F(1),F(1,4),1,lambda x:(F(0),F(1)))
        with self.assertRaises(A.FredholmError):A.exp_minus_interval(F(-1))
        with self.assertRaises(A.FredholmError):A.exp_minus_interval(F(65))

    def test_exact_small_matrix_rational_inverse(self):
        m=((F(2),F(1)),(F(1),F(2)))
        self.assertEqual(A.mul(m,A.inverse(m)),A.eye(2))
        self.assertTrue(A.psd(m))
        self.assertFalse(A.psd(((F(1),F(2)),(F(2),F(1)))))

    def test_float_bool_refused(self):
        for x in [True,1.0,False]:
            with self.assertRaises(A.FredholmError):A.q(x)


class AuthenticSourceTests(unittest.TestCase):
    def _has_source(self):
        try:
            from observational_succ import source_weil_hierarchy  # noqa: F401
            return True
        except ImportError:
            return False

    def test_full_signed_source_gamma8_to64_p1(self):
        if not self._has_source():self.skipTest('isolated environment without authentic SUCC modules')
        out=A.source_authenticated_fredholm_packet(8,8)
        self.assertEqual(out['source_sha'],'0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertTrue(out['P1_positive_after_true_64_modes_but_negative_with_8'])
        self.assertFalse(out['original_Schur_sign_proved'])

    def test_true_gamma_cell_and_trace(self):
        if not self._has_source():self.skipTest('isolated environment without authentic SUCC modules')
        out=A.source_authenticated_fredholm_packet(8,8)
        self.assertLess(F(out['gamma_compact_cell_matrix_trace_interval'][1]),8)
        self.assertLess(F(out['negative_index_trace_upper_rational']),20)

    def test_four_mode_Archimedean_source_clock_filtration(self):
        if not self._has_source():self.skipTest('isolated environment without authentic SUCC modules')
        out=A.source_original_four_mode_gamma_clock()
        pairs=tuple((z['true_original_low_mode'],z['first_strictly_positive_gamma_rungs']) for z in out['genuine_four_mode_first_positive_clock'])
        self.assertEqual(pairs,((1,19),(2,10),(3,20),(4,7)))
        self.assertEqual(out['source_sha'],'0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertFalse(out['original_full_Schur_sign_proved'])

    def test_actual_four_low_J63_to_J64_first_PD(self):
        if not self._has_source():self.skipTest('isolated environment without authentic SUCC modules')
        out=A.source_original_four_mode_PD_transition()
        self.assertEqual(out['first_strict_positive_four_low_gram_gamma_J'],64)
        self.assertEqual(out['negative_63_rung_original_rational_test'],(0,24,0,-25))
        self.assertLess(F(out['negative_63_rung_test_energy_strict_upper']),0)
        self.assertTrue(out['four_low_A4_positive_CERTIFIED'])
        self.assertFalse(out['four_low_S4_positive_CERTIFIED'])

    def test_true_source_only_prime2(self):
        if not self._has_source():self.skipTest('isolated environment without authentic SUCC modules')
        from observational_succ import source_weil_hierarchy as src
        self.assertEqual(src.authenticated_prime_wavefront(F(1,2)),((2,2),))
        self.assertIsNone(src.real_prime_power(6))


if __name__=='__main__':unittest.main()

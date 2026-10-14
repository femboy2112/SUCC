"""True prime/Gamma/pole Suzuki hierarchy: rational proof and hostile gates."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q

from observational_succ import source_weil_hierarchy as h


class SourceRationalTests(unittest.TestCase):
    def test_original_prime_power_tape(self):
        self.assertEqual(h.AUTHENTIC_TAPE,((2,2),(3,3),(4,2),(5,5),(7,7),(8,2)))
        self.assertTrue(h.assert_original_source_tape())
        for tape in (
            ((2,2),(3,3),(4,2),(5,5),(6,6),(7,7),(8,2)),
            ((2,2),(4,2),(5,5),(7,7),(8,2)),
            ((2,2),(3,3),(4,2),(5,5),(7,7),(8,3))
        ):
            with self.assertRaises(h.WeilHierarchyError):
                h.assert_original_source_tape(tape)

    def test_pi_interval(self):
        p=h.pi_iv()
        self.assertLess(p.lo,Q(22,7))
        self.assertGreater(p.hi,Q(3))
        self.assertLess(p.hi-p.lo,Q(1,10**23))
        self.assertGreater(p.lo,Q(3141592653589793,10**15))
        self.assertLess(p.hi,Q(3141592653589794,10**15))

    def test_gamma_contact(self):
        e=h.gamma_iv();contact=h.contact_iv()
        self.assertGreater(e.lo,Q(57,100))
        self.assertLess(e.hi,Q(58,100))
        self.assertLess(e.hi-e.lo,Q(1,10**10))
        self.assertGreater(contact.lo,Q(5))
        self.assertLess(contact.hi,Q(6))

    def test_logs_and_exp_reciprocity(self):
        from math import log,exp
        for x in (Q(1,4),Q(1,2),Q(2),Q(3),Q(4),Q(8),Q(13,7)):
            interval=h.log_iv(x)
            # independent float is a diagnostic, not a proof premise
            self.assertLessEqual(float(interval.lo),log(float(x))+1e-12)
            self.assertGreaterEqual(float(interval.hi),log(float(x))-1e-12)
            self.assertLess(interval.hi-interval.lo,Q(1,10**22))
        for x in (Q(0),Q(1,4),Q(1),Q(3),Q(9),Q(33)):
            a=h.exp_pos(x);b=h.exp_neg(x)
            self.assertLessEqual(float(a.lo),exp(float(x))*(1+1e-12))
            self.assertGreaterEqual(float(a.hi),exp(float(x))*(1-1e-12))
            self.assertLessEqual(float((a*b).lo),1+1e-12)
            self.assertGreaterEqual(float((a*b).hi),1-1e-12)

    def test_exact_source_zero_origin(self):
        for j in (1,3,8):
            x=h.screw_interval(Q(),j)
            self.assertTrue(x.lo<=0<=x.hi)
            self.assertLess(x.hi-x.lo,Q(1,10**20))

    def test_signed_source_against_independent_parent(self):
        try:import mpmath as mp
        except ImportError:self.skipTest('research mpmath optional')
        from observational_succ.gaussian_weil_certificates import signed_suzuki_g
        mp.mp.dps=70
        for r in (Q(1,8),Q(1,2),Q(3,4),Q(1),Q(2)):
            for J in (1,4,12):
                certified=h.screw_interval(r,J)
                original=signed_suzuki_g(mp.mpf(r.numerator)/r.denominator,J,dps=70)
                lo=mp.mpf(certified.lo.numerator)/certified.lo.denominator
                hi=mp.mpf(certified.hi.numerator)/certified.hi.denominator
                self.assertLessEqual(lo,original)
                self.assertGreaterEqual(hi,original)

    def test_mutation_types(self):
        for fn in (
            lambda:h.log_iv(Q(0)),
            lambda:h.exp_pos(Q(-1)),
            lambda:h.screw_interval(Q(11,5),3),
            lambda:h.screw_interval(Q(1,2),0),
            lambda:h.screw_interval(0.5,3),
            lambda:h.stage(Q(2),4,4),
            lambda:h.stage(Q(1,2),4,1)
        ):
            with self.assertRaises(h.WeilHierarchyError):fn()


    def test_cache_source_type_alias_does_not_launder_float(self):
        # Before the fix, lru_cache hashed Fraction(1,2) == float(.5) and
        # returned the exact result without invoking its source type gate.
        h.log_iv(Q(1,2));h.exp_pos(Q(1,2))
        h.screw_interval(Q(1,2),3);h.stage(Q(1,2),3,3)
        for bad in (
            lambda:h.log_iv(0.5),
            lambda:h.exp_pos(0.5),
            lambda:h.screw_interval(0.5,3),
            lambda:h.stage(0.5,3,3),
        ):
            with self.assertRaises(h.WeilHierarchyError):bad()

    def test_sqrt_inverse(self):
        x=h.sqrt_inverse(2)
        self.assertLessEqual(x.lo*x.lo*2,1)
        self.assertGreaterEqual(x.hi*x.hi*2,1)
        self.assertLess(x.hi-x.lo,Q(1,10**20))


class SignedOperatorProofTests(unittest.TestCase):
    def test_rational_analytic_limit(self):
        a=Q(1,2)
        errors=[h.continuous_error(a,J,J*J) for J in (2,4,8,16)]
        self.assertTrue(all(x>y>0 for x,y in zip(errors,errors[1:])))
        self.assertLess(h.gamma_tail(50),h.gamma_tail(5))

    def test_source_stage_finite(self):
        st=h.stage(Q(1,2),4,4)
        self.assertEqual(st.source,'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3')
        self.assertFalse(st.nontrivial_zeros_used)
        self.assertTrue(st.norm_error>h.continuous_error(st.a,st.J,st.N))
        self.assertEqual(len(st.center),4)
        self.assertTrue(all(st.center[i][j]==st.center[j][i]
                            for i in range(4) for j in range(4)))

    def test_exact_gram_shift_bounds(self):
        st=h.stage(Q(1,2),5,5)
        d=h.certified_upper_negative_depth(st,iterations=6)
        self.assertTrue(d>=0)
        self.assertTrue(h.ldl_positive(h._contrast_quadratic(st.center,d)) or d==0)
        low,high=h.depth_enclosure(st,iterations=6)
        self.assertTrue(0<=low<=high)
        self.assertGreaterEqual(high,st.norm_error)

    def test_forged_source_matrix_rejected(self):
        st=h.stage(Q(1,2),2,3)
        for mutant in (
            replace(st,source='DECLARED_TOY'),
            replace(st,norm_error=Q()),
            replace(st,center=tuple(tuple(Q() for _ in row) for row in st.center))
        ):
            with self.assertRaises(h.WeilHierarchyError):
                h.depth_enclosure(mutant,iterations=3)

    def test_strict_PD_indefinite_controls(self):
        self.assertTrue(h.ldl_positive(((Q(2),Q(1)),(Q(1),Q(2)))))
        self.assertFalse(h.ldl_positive(((Q(1),Q(2)),(Q(2),Q(1)))))
        self.assertFalse(h.ldl_positive(((Q(0),),)))
        with self.assertRaises(h.WeilHierarchyError):
            h.ldl_positive(((Q(1),Q(2)),(Q(1),Q(2))))

    def test_small_interval_hierarchy_separate_source(self):
        a=Q(1,4)
        lower=h.continuous_error(a,4,24)
        self.assertGreater(lower,0)
        self.assertLess(h.continuous_error(a,8,64),lower)
        self.assertLess(h.continuous_error(a,16,256),
                        h.continuous_error(a,8,64))

    def test_halting_bound_and_finite_blindness(self):
        for T in (None,1,4,9,21):
            for N in (1,2,4,10):
                seen,err=h.simple_rank_one_negative(N,T)
                true=Q(0) if T is None else -Q(1,2**T)
                self.assertLessEqual(abs(seen-true),err)
        self.assertEqual(h.simple_rank_one_negative(4,9),(Q(),Q(1,16)))
        self.assertEqual(h.simple_rank_one_negative(9,9),(-Q(1,512),Q(1,512)))

    def test_no_floating_certificate(self):
        with self.assertRaises(h.WeilHierarchyError):
            h.stage(0.5,3,3)
        with self.assertRaises(h.WeilHierarchyError):
            h.simple_rank_one_negative(2,3.0)




class HigherOrderSignTests(unittest.TestCase):
    def test_pairwise_positive_threeway_negative(self):
        u=(Q(1),Q(1),Q(-2))
        M=tuple(tuple(Q(i==j)-Q(1,5)*u[i]*u[j] for j in range(3))
                for i in range(3))
        for i in range(3):
            for j in range(i+1,3):
                v=tuple(int(k==i)-int(k==j) for k in range(3))
                self.assertGreater(h.exact_rayleigh(M,v),0)
        self.assertEqual(h.exact_rayleigh(M,u),Q(-1,5))
        minimum,vector=h.finite_multiway_search(M,amplitude=1)
        self.assertLessEqual(minimum,Q(-1,5))
        self.assertEqual(sum(vector),0)
        self.assertGreaterEqual(max(abs(x) for x in vector),1)

    def test_actual_multiway_search_has_source_gate(self):
        st=h.stage(Q(1,2),3,3)
        out=h.authenticated_multiway_witness(st,amplitude=1)
        self.assertEqual(len(out["vector"]),3)
        self.assertFalse(out["certified_global_positive"])
        self.assertFalse(out["nontrivial_zero_input"])
        self.assertEqual(out["source_upper_rayleigh"],
                         out["rational_center_rayleigh"]+st.norm_error)

    def test_forged_multiway_source_rejected(self):
        st=h.stage(Q(1,2),3,3)
        with self.assertRaises(h.WeilHierarchyError):
            h.authenticated_multiway_witness(replace(st,norm_error=0))


    def test_equality_launders_float_matrix_zero_without_strict_schema(self):
        st=h.stage(Q(1,2),4,4)
        rows=[list(r) for r in st.center]
        self.assertEqual(rows[0][0],Q(0))
        rows[0][0]=0.0
        fake=replace(st,center=tuple(tuple(r) for r in rows))
        # Standard dataclass equality is not a proof of exact element types.
        self.assertEqual(fake,st)
        with self.assertRaises(h.WeilHierarchyError):
            h.depth_enclosure(fake,iterations=3)

    def test_float_in_exact_spectral_probes_rejected(self):
        for fn in (
            lambda:h.ldl_positive(((1.0,),)),
            lambda:h.exact_rayleigh(((1.0,0,0),(0,1,0),(0,0,1)),(1,-1,0)),
        ):
            with self.assertRaises(h.WeilHierarchyError):fn()

    def test_invalid_multidirection(self):
        M=((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1)))
        with self.assertRaises(h.WeilHierarchyError):
            h.exact_rayleigh(M,(1,1,1))
        with self.assertRaises(h.WeilHierarchyError):
            h.finite_multiway_search(M,amplitude=0)




class SourceWavefrontTests(unittest.TestCase):
    def test_authentic_radius_prime_activation(self):
        self.assertEqual(h.authenticated_prime_wavefront(Q(1,4)),())
        self.assertEqual(h.authenticated_prime_wavefront(Q(1,2)),((2,2),))
        self.assertEqual(h.authenticated_prime_wavefront(Q(1)),((2,2),(3,3),(4,2),(5,5),(7,7)))
        self.assertNotIn((6,6),h.authenticated_prime_wavefront(Q(1)))

    def test_wavefront_source_and_radius_gates(self):
        with self.assertRaises(h.WeilHierarchyError):
            h.authenticated_prime_wavefront(Q(0))
        with self.assertRaises(h.WeilHierarchyError):
            h.authenticated_prime_wavefront(Q(5,4))
        with self.assertRaises(h.WeilHierarchyError):
            h.authenticated_prime_wavefront(0.5)




class CoupledResolutionTests(unittest.TestCase):
    def test_more_true_gamma_can_worsen_error_bound(self):
        self.assertGreater(h.gamma_refinement_delta(Q(1,2),16,24),0)
        self.assertLess(h.gamma_refinement_delta(Q(1,2),16,64),0)
        self.assertLess(h.gamma_tail(17),h.gamma_tail(16))

    def test_exact_first_improving_grid(self):
        self.assertEqual(h.minimum_improving_resolution(Q(1,2),12),23)
        for J in (2,4,8,12,16,20):
            N=h.minimum_improving_resolution(Q(1,2),J)
            self.assertLess(h.gamma_refinement_delta(Q(1,2),J,N),0)
            if N>2:
                self.assertGreaterEqual(h.gamma_refinement_delta(Q(1,2),J,N-1),0)

    def test_invalid_grid_boundaries(self):
        with self.assertRaises(h.WeilHierarchyError):
            h.minimum_improving_resolution(Q(0),8)
        with self.assertRaises(h.WeilHierarchyError):
            h.gamma_refinement_delta(Q(1,2),16,1)
        with self.assertRaises(h.WeilHierarchyError):
            h.gamma_refinement_delta(0.5,16,24)




class GammaDiamondTests(unittest.TestCase):
    def test_positive_tail_is_second_order(self):
        for J in (1,2,3,4,8,16,32,64,128):
            t=h.authentic_positive_gamma_tail_norm(J)
            self.assertGreater(t,0)
            self.assertLess(t,h.gamma_tail(J))
        for J in range(1,20):
            self.assertGreater(h.authentic_positive_gamma_tail_norm(J),
                               h.authentic_positive_gamma_tail_norm(J+1))

    def test_true_gamma_modes_increase_loewner_clock_energy(self):
        indices=(-1,0,1)
        for weights in ((1,-2,1),(1,0,-1),(1,-1,0)):
            energies=[h.monotone_gamma_mode_rayleigh(indices,weights,j)
                      for j in (1,2,3,4,5)]
            self.assertTrue(all(b>a>0 for a,b in zip(energies,energies[1:])))

    def test_source_spectrum_asymmetric_bounds_sharper(self):
        st=h.stage(Q(1,2),4,4)
        output=h.original_source_one_sided(st,iterations=6,amplitude=1)
        self.assertEqual(output["source"],'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3')
        self.assertLess(output["spatial_interval_norm_error"],st.norm_error)
        old=h.certified_upper_negative_depth(st,iterations=6)+st.norm_error
        self.assertLess(output["upper_negative_depth"],old)
        self.assertGreaterEqual(output["upper_negative_depth"],
                                output["lower_negative_depth"])
        self.assertFalse(output["rh_proved"])
        self.assertLess(output["positive_gamma_tail_norm_upper"],h.gamma_tail(st.J))

    def test_true_gamma_tail_positive_without_source_mutation(self):
        st=h.stage(Q(1,2),4,3)
        out=h.original_source_one_sided(st,iterations=4,amplitude=1)
        self.assertEqual(out["spatial_interval_norm_error"]+
                         2*st.a*h.gamma_tail(st.J),st.norm_error)

    def test_forged_stage_rejected_for_one_sided_sign(self):
        st=h.stage(Q(1,2),3,3)
        with self.assertRaises(h.WeilHierarchyError):
            h.original_source_one_sided(replace(st,source="fake-Gamma"))
        with self.assertRaises(h.WeilHierarchyError):
            h.original_source_one_sided(replace(st,norm_error=Q()))


if __name__=='__main__':
    unittest.main()

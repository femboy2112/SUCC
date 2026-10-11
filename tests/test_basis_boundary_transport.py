"""Exact source/probe and negative controls for basis-indexed SUCC transport."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import json
import unittest

from observational_succ.basis_boundary_transport import (
    BasisTransportError, SharedBasis, BasisState, SparseDelta,
    CertifiedEqualFamily, FrameActionBasis,
    encode_sparse_delta, decode_sparse_delta, encode_action_path,
    decode_action_path, Root6, boundary_evaluations,
    boundary_decode_bandlimited, finite_boundary_demo,
    radial_mode_samples, decode_radial_modes, round_root6_samples,
    zero_only_line_counterexample,
)


class BasisIndexedTransportTests(unittest.TestCase):
    def setUp(self):
        self.basis=SharedBasis(6)
        self.start=BasisState.from_sparse(self.basis,{1:2,2:7,4:3})
        self.delta=SparseDelta((1,4,5),(Q(1),Q(1),Q(1)))
        self.end=self.start.update(self.delta,self.basis)
        self.family=CertifiedEqualFamily(
            (1,4,5),tuple(SparseDelta((1,4,5),(v,v,v))
                           for v in (Q(0),Q(1),Q(2))),
        )

    def test_exact_user_example_reconstructs_relative_state_not_a_snapshot(self):
        packet=encode_sparse_delta(self.end,self.start,self.basis,self.delta)
        d=json.loads(packet)
        self.assertEqual(d["directions"],[1,4,5])
        self.assertEqual(d["values"],["1","1","1"])
        self.assertEqual(d["mode"],"unrestricted")
        self.assertNotIn("current_state",d)
        self.assertNotIn("full_state",d)
        self.assertEqual(decode_sparse_delta(self.start,packet,self.basis),self.end)
        self.assertEqual(self.end.coefficients,
                         (Q(3),Q(7),Q(0),Q(4),Q(1),Q(0)))
        self.assertNotEqual(self.end,self.start)

    def test_empty_delta_and_exact_composition_are_identity_and_associative(self):
        unit=SparseDelta((),())
        self.assertEqual(self.start.update(unit,self.basis),self.start)
        left=SparseDelta((1,4),(Q(1,2),Q(2)))
        right=SparseDelta((4,5),(Q(-1),Q(3)))
        combined=left.add(right,self.basis)
        self.assertEqual(combined.indices,(1,4,5))
        self.assertEqual(combined.values,(Q(1,2),Q(1),Q(3)))
        self.assertEqual(self.start.update(left,self.basis).update(right,self.basis),
                         self.start.update(combined,self.basis))
        self.assertEqual(left.add(right,self.basis),right.add(left,self.basis))
        self.assertEqual(self.start.update(unit,self.basis),
                         decode_sparse_delta(self.start,
                            encode_sparse_delta(self.start,self.start,self.basis,unit),
                            self.basis))

    def test_very_small_shared_basis_different_source_position_same_tuple(self):
        a=BasisState.from_sparse(self.basis,{1:1})
        b=BasisState.from_sparse(self.basis,{1:100})
        a1=a.update(self.delta,self.basis)
        b1=b.update(self.delta,self.basis)
        self.assertNotEqual(a1,b1)
        packet=encode_sparse_delta(a1,a,self.basis,self.delta)
        with self.assertRaises(BasisTransportError):
            decode_sparse_delta(b,packet,self.basis)
        self.assertEqual(decode_sparse_delta(a,packet,self.basis),a1)

    def test_wrong_basis_version_or_wrong_direction_is_rejected(self):
        packet=encode_sparse_delta(self.end,self.start,self.basis,self.delta)
        other=SharedBasis(6,"changed-meaning-v2")
        with self.assertRaises(BasisTransportError):
            decode_sparse_delta(self.start,packet,other)
        # The new version can encode its *own* packet; the old decoder
        # correctly refuses it. No tool can infer external language meaning
        # from matching dimensions alone.
        valid_other=encode_sparse_delta(self.end,self.start,other,self.delta)
        with self.assertRaises(BasisTransportError):
            decode_sparse_delta(self.start,valid_other,self.basis)
        bad=json.loads(packet)
        for change in (
            lambda d:d.update(anchor="stale"),
            lambda d:d.update(end="forged"),
            lambda d:d.update(basis="not-this-dictionary"),
            lambda d:d.update(directions=[1,4,6]),
            lambda d:d.update(directions=[1,4,4]),
            lambda d:d.update(directions=[1,4,True]),
            lambda d:d.update(values=["1","2","1"]),
            lambda d:d.update(values=["1","1"]),
            lambda d:d.update(values=["not a fraction","1","1"]),
            lambda d:d.update(mode="unsupported"),
        ):
            mutated=json.loads(json.dumps(bad))
            change(mutated)
            with self.subTest(mutated=mutated):
                with self.assertRaises(BasisTransportError):
                    decode_sparse_delta(self.start,json.dumps(mutated).encode(),self.basis)
        with self.assertRaises(BasisTransportError):
            SparseDelta((1,1),(Q(1),Q(1)))
        with self.assertRaises(BasisTransportError):
            SparseDelta((True,),(Q(1),))
        with self.assertRaises(BasisTransportError):
            self.start.update(SparseDelta((7,),(Q(1),)),self.basis)

    def test_certified_source_law_compresses_values_not_bare_indices(self):
        packet=encode_sparse_delta(self.end,self.start,self.basis,self.delta,self.family)
        d=json.loads(packet)
        self.assertEqual(d["directions"],[1,4,5])
        self.assertEqual(d["values"],["1"])
        self.assertEqual(d["mode"],"equal-coefficients")
        self.assertEqual(decode_sparse_delta(self.start,packet,self.basis,self.family),
                         self.end)
        with self.assertRaises(BasisTransportError):
            decode_sparse_delta(self.start,packet,self.basis)
        with self.assertRaises(BasisTransportError):
            decode_sparse_delta(
                self.start,packet,self.basis,
                CertifiedEqualFamily(
                    (1,4,5),(SparseDelta((1,4,5),(Q(3),Q(3),Q(3))),)))
        wrong=SparseDelta((1,4,5),(Q(1),Q(1),Q(2)))
        with self.assertRaises(BasisTransportError):
            encode_sparse_delta(self.start.update(wrong,self.basis),
                                self.start,self.basis,wrong,self.family)

    def test_invalid_fake_source_lemma_cannot_license_value_compression(self):
        wrong=SparseDelta((1,4,5),(Q(1),Q(1),Q(2)))
        unsound=CertifiedEqualFamily((1,4,5),(self.delta,wrong))
        with self.assertRaises(BasisTransportError):
            unsound.verify(self.basis)
        with self.assertRaises(BasisTransportError):
            encode_sparse_delta(self.end,self.start,self.basis,self.delta,unsound)
        valid=encode_sparse_delta(self.end,self.start,self.basis,self.delta,self.family)
        altered=json.loads(valid)
        altered["values"]=["2"]
        with self.assertRaises(BasisTransportError):
            decode_sparse_delta(self.start,json.dumps(altered).encode(),
                                self.basis,self.family)

    def test_frame_actions_are_order_sensitive_even_with_same_coordinate_multiset(self):
        ops=FrameActionBasis()
        a=((1,Q(1)),(4,Q(1)),(5,Q(1)))
        b=((4,Q(1)),(1,Q(1)),(5,Q(1)))
        self.assertEqual(ops.apply(0,a),Q(3))
        self.assertEqual(ops.apply(0,b),Q(2))
        self.assertNotEqual(ops.apply(0,a),ops.apply(0,b))
        encoded=encode_action_path(0,a,ops)
        self.assertEqual(json.loads(encoded)["steps"],
                         [[1,"1"],[4,"1"],[5,"1"]])
        self.assertEqual(decode_action_path(0,encoded,ops),Q(3))
        with self.assertRaises(BasisTransportError):
            decode_action_path(2,encoded,ops)
        wrong=json.loads(encoded)
        wrong["steps"]=[[4,"1"],[1,"1"],[5,"1"]]
        with self.assertRaises(BasisTransportError):
            decode_action_path(0,json.dumps(wrong).encode(),ops)
        with self.assertRaises(BasisTransportError):
            ops.apply(0,((2,Q(1)),))

    def test_group_law_and_root6_dft_orthogonality_independently(self):
        z=Root6(0,1)
        one=Root6(1)
        self.assertEqual(z.power(0),one)
        self.assertEqual(z.power(6),one)
        self.assertEqual(z*z,z-one)
        self.assertEqual(z.conjugate()*z,one)
        self.assertEqual(z.power(-1),z.conjugate())
        for n in range(-12,13):
            total=Root6()
            for j in range(6):
                total=total+z.power(j*n)
            self.assertEqual(total,Root6(6 if n%6==0 else 0))
        for m in range(6):
            coefficients=tuple(Q(1) if j==m else Q(0) for j in range(6))
            self.assertEqual(
                boundary_decode_bandlimited(boundary_evaluations(coefficients)),
                coefficients)

    def test_exact_degree_five_boundary_recovery_on_independent_polynomials(self):
        for entries in product((-1,0,1),repeat=4):
            coeff=tuple(Q(x) for x in (*entries,0,0))
            data=boundary_evaluations(coeff)
            self.assertEqual(boundary_decode_bandlimited(data),coeff)
        for sign in (-3,-1,0,1,3):
            coeff=tuple(Q(sign*j) for j in range(6))
            self.assertEqual(
                boundary_decode_bandlimited(boundary_evaluations(coeff)),coeff)

    def test_unbounded_modes_alias_even_all_six_boundary_samples(self):
        zero=boundary_evaluations(())
        hidden=boundary_evaluations((Q(-1),)+(Q(0),)*5+(Q(1),))
        self.assertEqual(zero,hidden)
        self.assertNotEqual((Q(-1),)+(Q(0),)*5+(Q(1),),(Q(0),)*7)
        self.assertEqual(
            boundary_evaluations((Q(0),Q(1))),
            boundary_evaluations((Q(0),)*7+(Q(1),)))
        with self.assertRaises(BasisTransportError):
            boundary_decode_bandlimited(zero[:5])
        with self.assertRaises(BasisTransportError):
            boundary_decode_bandlimited((Root6(0,1),)*6)

    def test_radial_recovery_exact_but_finite_precision_hides_high_mode(self):
        high=(Q(0),)*5+(Q(1),)
        at_r=radial_mode_samples(high,Q(1,2))
        self.assertEqual(decode_radial_modes(at_r,Q(1,2)),high)
        self.assertEqual(
            round_root6_samples(at_r,Q(1,8)),
            round_root6_samples(radial_mode_samples((Q(0),)*6,Q(1,2)),Q(1,8)),
        )
        self.assertNotEqual(at_r,radial_mode_samples((Q(0),)*6,Q(1,2)))
        self.assertEqual(
            decode_radial_modes(round_root6_samples(at_r,Q(1,8)),Q(1,2)),
            (Q(0),)*6,
        )
        self.assertEqual(Q(1,2)**5,Q(1,32))
        with self.assertRaises(BasisTransportError):
            radial_mode_samples(high,Q(0))
        with self.assertRaises(BasisTransportError):
            radial_mode_samples(high,Q(2))
        with self.assertRaises(BasisTransportError):
            decode_radial_modes(at_r,Q(0))
        with self.assertRaises(BasisTransportError):
            round_root6_samples(at_r,Q(0))

    def test_many_exact_radial_inverse_controls_different_source_modes(self):
        radii=(Q(1),Q(3,4),Q(1,2),Q(1,4))
        for coefficients in product((-1,0,1),repeat=3):
            full=tuple(Q(x) for x in (*coefficients,0,0,0))
            for r in radii:
                observed=radial_mode_samples(full,r)
                self.assertEqual(decode_radial_modes(observed,r),full)

    def test_critical_line_zeros_only_cannot_suffice_for_global_reconstruction(self):
        r=zero_only_line_counterexample()
        self.assertEqual(r["status"],"SYMMETRIC_ENTIRE_POLYNOMIAL_LINE_ZERO_NONUNIQUENESS")
        self.assertEqual(r["line_zeros_in_both"],["1/2-i","1/2+i"])
        self.assertEqual(r["extra_offline_zeros_in_one"],["1/4","3/4"])
        self.assertTrue(r["both_respect_s_to_one_minus_s"])
        self.assertTrue(r["both_respect_reality_conjugation"])
        self.assertFalse(r["line_zero_locations_alone_determine_global_entire_function"])
        self.assertTrue(r["full_exact_line_function_values_have_identity_theorem_uniqueness"])
        self.assertFalse(r["either_function_is_true_riemann_xi"])
        self.assertFalse(r["RH_disproved_or_proved"])

    def test_fixed_support_message_lower_bound_under_ordinary_full_basis(self):
        # Exactly three unknown support positions among six => 20 cases.
        # For an exact fixed-length code shared decoder needs >= 5 bits.
        from math import comb
        self.assertEqual(comb(6,3),20)
        self.assertEqual((comb(6,3)-1).bit_length(),5)
        self.assertLess(2**4,comb(6,3))
        self.assertGreaterEqual(2**5,comb(6,3))

    def test_explicit_status_does_not_claim_physical_gravity_or_rh(self):
        r=finite_boundary_demo()
        self.assertEqual(r["status"],"EXACT_SHARED_BASIS_RELATIVE_BOUNDARY_TRANSPORT")
        self.assertEqual(r["source_packet_directions"],[1,4,5])
        self.assertEqual(r["source_packet_values"],[1,1,1])
        self.assertEqual(r["proof_context_value_codes_before"],3)
        self.assertEqual(r["proof_context_value_codes_after"],1)
        self.assertEqual(r["noncommutative_ordered_path_endpoints"],[3,2])
        self.assertTrue(r["boundary_exact_bandlimited_reconstruction"])
        self.assertTrue(r["boundary_unrestricted_high_mode_alias_exists"])
        self.assertTrue(r["radial_exact_high_mode_reconstruction"])
        self.assertTrue(r["finite_precision_root_six_samples_hide_mode_five"])
        self.assertTrue(r["critical_line_zero_only_incomplete_for_symmetric_polynomial_family"])
        self.assertFalse(r["true_xi_line_zero_locations_claimed_complete"])
        self.assertFalse(r["gravity_holographic_correspondence_proved"])
        self.assertFalse(r["total_message_bit_optimality_claimed"])
        self.assertFalse(r["RH_claimed"])


if __name__=="__main__":
    unittest.main()

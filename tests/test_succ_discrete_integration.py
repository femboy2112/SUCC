"""Hostile exact controls for SUCC as discrete integration in a shared basis.

The finite-difference prefix scan reconstructs every actual intermediate step.
Finite jets predict later steps ONLY when a separately justified recurrence /
polynomial source law is a binding part of the admitted source family.
Changing coordinate frames needs a covariant difference and ordered connection.
"""
import json
from fractions import Fraction as Q
from itertools import product
from dataclasses import replace
from math import comb
import unittest

from observational_succ.basis_boundary_transport import (
    BasisState, SharedBasis, SparseDelta,
)
from observational_succ.succ_discrete_integration import (
    DiscreteSuccError, ScanResult, RationalFrame, AffineStep,
    PolynomialJetSourceFamily, finite_difference_states,
    parallel_prefix_differences, encode_step_differences,
    decode_step_differences, difference_jet_from_samples,
    finite_newton_reconstruct_samples,
    newton_evaluate, encode_newton_jet, decode_newton_jet,
    covariant_step, parallel_prefix_affine, succ_derivative_demo,
    covariant_initial_jet_from_local_samples, covariant_newton_evaluate,
    finite_covariant_newton_reconstruct_samples, certified_covariant_newton_path,
)


def setup_basis():
    basis=SharedBasis(3)
    initial=BasisState.from_sparse(basis,{1:2,2:4})
    return basis,initial


class SuccDiscreteIntegrationTests(unittest.TestCase):
    def test_anchor_plus_first_differences_reconstruct_each_intermediate_frame(self):
        basis,initial=setup_basis()
        steps=(
            SparseDelta((1,3),(Q(1),Q(2))),
            SparseDelta((1,2),(Q(-2),Q(1))),
            SparseDelta((2,3),(Q(3),Q(-2))),
            SparseDelta((1,),(Q(4),)),
        )
        states=finite_difference_states(initial,steps,basis)
        self.assertEqual(
            [tuple(int(x) for x in s.coefficients) for s in states],
            [(2,4,0),(3,4,2),(1,5,2),(1,8,0),(5,8,0)])
        packet=encode_step_differences(states[-1],initial,basis,steps)
        data=json.loads(packet)
        self.assertEqual(data["kind"],"source-relative-succ-differences-v1")
        self.assertNotIn("full_history",data)
        self.assertNotIn("full_state",data)
        self.assertEqual(len(data["steps"]),4)
        receipt=decode_step_differences(initial,packet,basis)
        self.assertEqual(receipt.states,states)
        self.assertEqual(receipt.parallelizable_dependency_depth,2)
        self.assertFalse(receipt.actual_parallel_execution_performed)

    def test_same_net_delta_does_not_determine_internal_succ_path(self):
        basis=SharedBasis(1)
        start=BasisState.from_sparse(basis,{})
        plus_then_minus=(
            SparseDelta((1,),(Q(1),)), SparseDelta((1,),(Q(-1),)))
        minus_then_plus=(
            SparseDelta((1,),(Q(-1),)), SparseDelta((1,),(Q(1),)))
        left=finite_difference_states(start,plus_then_minus,basis)
        right=finite_difference_states(start,minus_then_plus,basis)
        self.assertEqual(left[-1],right[-1])
        self.assertNotEqual(left[1],right[1])
        self.assertNotEqual(
            encode_step_differences(left[-1],start,basis,plus_then_minus),
            encode_step_differences(right[-1],start,basis,minus_then_plus),
        )

    def test_associative_prefix_scan_all_small_binary_sequences(self):
        basis=SharedBasis(2)
        origin=BasisState.from_sparse(basis,{1:3,2:-2})
        cases=0
        for n in range(6):
            for choices in product((-1,0,1), repeat=n):
                step=tuple(SparseDelta((1,2),(Q(v),Q(1-v))) for v in choices)
                serial=finite_difference_states(origin,step,basis)
                scan=parallel_prefix_differences(origin,step,basis)
                self.assertEqual(serial,scan.states)
                self.assertEqual(scan.parallelizable_dependency_depth,
                                 max(0,n-1).bit_length())
                self.assertFalse(scan.actual_parallel_execution_performed)
                cases+=1
        self.assertEqual(cases,364)

    def test_zero_steps_and_canonical_sparse_derivative_controls(self):
        basis,start=setup_basis()
        zero=SparseDelta((),())
        trace=finite_difference_states(start,(zero,),basis)
        self.assertEqual(trace,(start,start))
        self.assertEqual(parallel_prefix_differences(start,(),basis).states,(start,))
        packet=encode_step_differences(start,start,basis,())
        self.assertEqual(decode_step_differences(start,packet,basis).states,(start,))
        with self.assertRaises(DiscreteSuccError):
            encode_step_differences(
                BasisState.from_sparse(basis,{1:999}),start,basis,(zero,))

    def test_stale_basis_anchor_wrong_endpoint_wrong_increment_fail_closed(self):
        basis,start=setup_basis()
        seq=(SparseDelta((1,3),(Q(1),Q(2))),)
        end=finite_difference_states(start,seq,basis)[-1]
        packet=encode_step_differences(end,start,basis,seq)
        data=json.loads(packet)
        for key,val in [
            ("basis","different"),("anchor","bad"),("end","fake")]:
            altered=dict(data)
            altered[key]=val
            with self.subTest(key=key):
                with self.assertRaises(DiscreteSuccError):
                    decode_step_differences(start,json.dumps(altered).encode(),basis)
        changed=json.loads(packet)
        changed["steps"][0]["values"][0]="-999"
        with self.assertRaises(DiscreteSuccError):
            decode_step_differences(start,json.dumps(changed).encode(),basis)
        changed=json.loads(packet)
        changed["steps"][0]["directions"]=[1,1]
        with self.assertRaises(Exception):
            decode_step_differences(start,json.dumps(changed).encode(),basis)
        changed=json.loads(packet)
        changed["steps"][0]["values"]=["1/1","2"]
        with self.assertRaises(DiscreteSuccError):
            decode_step_differences(start,json.dumps(changed).encode(),basis)
        other=SharedBasis(3,"different-law-meaning-v2")
        with self.assertRaises(DiscreteSuccError):
            decode_step_differences(start,packet,other)
        with self.assertRaises(DiscreteSuccError):
            decode_step_differences(start,b"not-json",basis)

    def test_full_finite_newton_jet_inverts_arbitrary_observed_sequences(self):
        # No polynomial source premise is required WITHIN the known finite
        # sample horizon. That premise becomes necessary for extrapolation
        # beyond it using a truncated jet.
        b=SharedBasis(1)
        count=0
        for n in range(1,7):
            for values in product((-1,0,1),repeat=n):
                samples=tuple(BasisState((Q(v),)) for v in values)
                reconstructed=finite_newton_reconstruct_samples(samples,b)
                self.assertEqual(reconstructed,samples)
                count+=1
        self.assertEqual(count,1092)
        b2=SharedBasis(2)
        w=(BasisState((Q(1),Q(2))),
           BasisState((Q(9),Q(-4))),
           BasisState((Q(-2),Q(11))),
           BasisState((Q(200),Q(0))),
           BasisState((Q(3),Q(-13))))
        self.assertEqual(finite_newton_reconstruct_samples(w,b2),w)

    def test_quadratic_newton_forward_difference_identity(self):
        basis=SharedBasis(1)
        start=BasisState.from_sparse(basis,{})
        states=tuple(BasisState((Q(n*n),)) for n in range(3))
        jet=difference_jet_from_samples(states,basis)
        self.assertEqual(jet,((Q(0),),(Q(1),),(Q(2),)))
        for n in range(30):
            self.assertEqual(newton_evaluate(start,jet[1:],n,basis),
                             BasisState((Q(n*n),)))
        self.assertEqual(newton_evaluate(start,(),7,basis),start)

    def test_cubic_newton_jet_recovers_all_states_without_long_delta_list(self):
        basis=SharedBasis(1)
        start=BasisState((Q(0),))
        d1=(Q(1),)
        d2=(Q(6),)
        d3=(Q(6),)
        law=PolynomialJetSourceFamily(basis.fingerprint,3,((d1,d2,d3),))
        samples=tuple(BasisState((Q(n**3),)) for n in range(4))
        jet=difference_jet_from_samples(samples,basis)
        self.assertEqual(jet[1:],(d1,d2,d3))
        packet=encode_newton_jet(start,basis,samples,law,100)
        states=decode_newton_jet(start,packet,basis,law)
        self.assertEqual(len(states),101)
        self.assertEqual(states[20],BasisState((Q(8000),)))
        self.assertEqual(states[-1],BasisState((Q(1000000),)))
        self.assertEqual(len(json.loads(packet)["jets"]),3)
        self.assertNotIn("all-steps",json.loads(packet))

    def test_source_law_is_necessary_for_global_inference_from_initial_jet(self):
        basis=SharedBasis(1)
        origin=BasisState((Q(0),))
        samples=(origin,origin,origin)
        jet=difference_jet_from_samples(samples,basis)
        self.assertEqual(jet[1:],((Q(0),),(Q(0),)))
        polynomial_prediction=newton_evaluate(origin,jet[1:],3,basis)
        alternative_next=BasisState((Q(1),))
        self.assertNotEqual(polynomial_prediction,alternative_next)
        # Both paths share the EXACT same first 3 samples, but one source
        # violates Delta^3 x_n=0 at n=0. Prefix observations alone cannot
        # turn polynomial interpolation into a global recurrence theorem.
        law=PolynomialJetSourceFamily(basis.fingerprint,2,
                                      (((Q(0),),(Q(0),)),))
        packet=encode_newton_jet(origin,basis,samples,law,3)
        reconstructed=decode_newton_jet(origin,packet,basis,law)
        self.assertEqual(reconstructed[-1],origin)
        self.assertNotEqual(reconstructed[-1],alternative_next)

    def test_forged_newton_family_and_stale_anchor_rejected(self):
        basis=SharedBasis(1)
        origin=BasisState((Q(0),))
        samples=(origin,BasisState((Q(1),)),BasisState((Q(4),)))
        good=PolynomialJetSourceFamily(basis.fingerprint,2,
                                       (((Q(1),),(Q(2),)),))
        bad=PolynomialJetSourceFamily(basis.fingerprint,2,
                                      (((Q(0),),(Q(0),)),))
        pkt=encode_newton_jet(origin,basis,samples,good,7)
        with self.assertRaises(DiscreteSuccError):
            decode_newton_jet(origin,pkt,basis,bad)
        with self.assertRaises(DiscreteSuccError):
            encode_newton_jet(origin,basis,samples,bad,7)
        changed=json.loads(pkt)
        changed["jets"]=[["9"],["2"]]
        with self.assertRaises(DiscreteSuccError):
            decode_newton_jet(origin,json.dumps(changed).encode(),basis,good)
        changed=json.loads(pkt)
        changed["anchor"]="WRONG"
        with self.assertRaises(DiscreteSuccError):
            decode_newton_jet(origin,json.dumps(changed).encode(),basis,good)
        other=SharedBasis(1,"other-version")
        with self.assertRaises(DiscreteSuccError):
            decode_newton_jet(origin,pkt,other,good)
        with self.assertRaises(DiscreteSuccError):
            good.verify(other)
        with self.assertRaises(DiscreteSuccError):
            decode_newton_jet(origin,pkt.replace(b"newton",b"NEWTON"),basis,good)

    def test_invertible_rational_frame_exact_algebra_and_singular_rejection(self):
        A=RationalFrame(((Q(2),Q(1)),(Q(1),Q(1))))
        identity=RationalFrame.identity(2)
        self.assertEqual(A.compose(A.inverse()),identity)
        self.assertEqual(A.inverse().compose(A),identity)
        B=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        v=(Q(3),Q(5))
        self.assertEqual(A.compose(B).act(v),A.act(B.act(v)))
        with self.assertRaises(DiscreteSuccError):
            RationalFrame(((Q(1),Q(2)),(Q(2),Q(4)))).inverse()
        with self.assertRaises(DiscreteSuccError):
            RationalFrame(((Q(1),Q(2)),))
        with self.assertRaises(DiscreteSuccError):
            A.compose(RationalFrame.identity(3))

    def test_naive_local_delta_is_wrong_under_changing_basis(self):
        identity=RationalFrame.identity(2)
        switched=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        x=(Q(2),Q(3))
        y0=identity.act(x)
        y1=switched.act(x)
        naive=tuple(b-a for a,b in zip(y0,y1))
        self.assertNotEqual(naive,(Q(0),Q(0)))
        step=covariant_step(identity,switched,(Q(0),Q(0)))
        self.assertEqual(step.delta,(Q(0),Q(0)))
        self.assertEqual(step.act(y0),y1)
        # The frame change is captured by transport U, not a physical
        # vector-state increment. This prevents falsely treating a
        # coordinate rotation as a newly observed material change.

    def test_covariant_discrete_derivative_square_commutes(self):
        F0=RationalFrame.identity(2)
        F1=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        F2=RationalFrame(((Q(1),Q(1)),(Q(0),Q(1))))
        x0=(Q(2),Q(3))
        d0=(Q(1),Q(0))
        d1=(Q(0),Q(2))
        x1=(Q(3),Q(3))
        x2=(Q(3),Q(5))
        a=covariant_step(F0,F1,d0)
        b=covariant_step(F1,F2,d1)
        scan=parallel_prefix_affine(F0.act(x0),(a,b))
        self.assertEqual(scan.values,(F0.act(x0),F1.act(x1),F2.act(x2)))
        self.assertEqual(scan.dependency_layers,1)
        self.assertFalse(scan.actual_parallel_execution_performed)
        self.assertEqual(b.compose(a).act(F0.act(x0)),F2.act(x2))

    def test_arbitrary_finite_trajectory_has_exact_covariant_newton_inverse(self):
        b=SharedBasis(2)
        I=RationalFrame.identity(2)
        S=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        H=RationalFrame(((Q(1),Q(1)),(Q(0),Q(1))))
        frames=(I,S,H,S,I)
        canonical=((Q(2),Q(3)),(Q(-1),Q(11)),(Q(0),Q(0)),
                   (Q(7),Q(-4)),(Q(0),Q(100)))
        local=tuple(frame.act(v) for frame,v in zip(frames,canonical))
        self.assertEqual(finite_covariant_newton_reconstruct_samples(frames,local),local)
        jet=covariant_initial_jet_from_local_samples(frames,local)
        self.assertEqual(jet[0],local[0])
        for n in range(len(frames)):
            self.assertEqual(
                covariant_newton_evaluate(jet[0],jet[1:],
                                          frames[0],frames[n],n),
                local[n])
        self.assertEqual(len(jet),len(local))
        # This is an exact observed-horizon identity even though the
        # canonical sequence has no quadratic recurrence.

    def test_certified_newton_jet_reconstructs_many_moving_frames_in_one_macro_message(self):
        b=SharedBasis(2)
        I=RationalFrame.identity(2)
        S=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        H=RationalFrame(((Q(1),Q(1)),(Q(0),Q(1))))
        frames=tuple((S,H,I)[n%3] for n in range(13))
        d1=(Q(1),Q(0))
        d2=(Q(1),Q(2))
        law=PolynomialJetSourceFamily(b.fingerprint,2,((d1,d2),))
        base=(Q(2),Q(3))
        def global_state(n):
            return (base[0]+Q(n)*d1[0]+Q(comb(n,2))*d2[0],
                    base[1]+Q(n)*d1[1]+Q(comb(n,2))*d2[1])
        local=tuple(F.act(global_state(n)) for n,F in enumerate(frames))
        received=certified_covariant_newton_path(b,frames,local[:3],law)
        self.assertEqual(received,local)
        self.assertEqual(len(received),13)
        jet=covariant_initial_jet_from_local_samples(frames[:3],local[:3])
        self.assertEqual(tuple(frames[0].inverse().act(v) for v in jet[1:]),
                         (d1,d2))
        self.assertEqual(covariant_newton_evaluate(
                             jet[0],jet[1:],frames[0],frames[10],10),
                         local[10])
        bad=PolynomialJetSourceFamily(b.fingerprint,2,
                                      (((Q(1),Q(1)),(Q(0),Q(0))),))
        with self.assertRaises(DiscreteSuccError):
            certified_covariant_newton_path(b,frames,local[:3],bad)

    def test_covariant_truncated_jet_still_cannot_predict_unrestricted_future(self):
        b=SharedBasis(2)
        I=RationalFrame.identity(2)
        S=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        frames=(I,S,I,S)
        canonical=( (Q(0),Q(0)),(Q(0),Q(0)),(Q(0),Q(0)),(Q(5),Q(-3)) )
        local=tuple(F.act(v) for F,v in zip(frames,canonical))
        jet=covariant_initial_jet_from_local_samples(frames[:3],local[:3])
        predicted=covariant_newton_evaluate(jet[0],jet[1:],
                                            frames[0],frames[3],3)
        self.assertNotEqual(predicted,local[3])
        self.assertEqual(predicted,(Q(0),Q(0)))
        # All four actual states *can* be reconstructed by a full finite
        # third-order jet, without inventing a quadratic global source law.
        self.assertEqual(finite_covariant_newton_reconstruct_samples(frames,local),
                         local)
        singular=RationalFrame(((Q(1),Q(2)),(Q(2),Q(4))))
        with self.assertRaises(DiscreteSuccError):
            finite_covariant_newton_reconstruct_samples(
                (I,singular),local[:2])

    def test_global_frames_induce_flat_closed_loop_transport_not_holonomy(self):
        I=RationalFrame.identity(2)
        S=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        H=RationalFrame(((Q(1),Q(1)),(Q(0),Q(1))))
        frames=(I,S,H,I)
        zero=(Q(0),Q(0))
        steps=tuple(covariant_step(frames[i],frames[i+1],zero)
                    for i in range(len(frames)-1))
        total=steps[2].compose(steps[1]).compose(steps[0])
        self.assertEqual(total.transport,I)
        self.assertEqual(total.delta,zero)
        self.assertEqual(parallel_prefix_affine((Q(2),Q(3)),steps).values[-1],
                         (Q(2),Q(3)))

    def test_ordered_noncommutative_affine_succ_and_scan(self):
        I=RationalFrame.identity(2)
        swap=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        translate=AffineStep(I,(Q(1),Q(0)))
        rotate=AffineStep(swap,(Q(0),Q(0)))
        start=(Q(0),Q(0))
        forward=parallel_prefix_affine(start,(translate,rotate))
        reversed_order=parallel_prefix_affine(start,(rotate,translate))
        self.assertEqual(forward.values[-1],(Q(0),Q(1)))
        self.assertEqual(reversed_order.values[-1],(Q(1),Q(0)))
        self.assertNotEqual(forward.values[-1],reversed_order.values[-1])
        self.assertEqual(rotate.compose(translate).act(start),(Q(0),Q(1)))
        self.assertEqual(translate.compose(rotate).act(start),(Q(1),Q(0)))

    def test_all_short_affine_paths_match_serial_order_and_prefix(self):
        I=RationalFrame.identity(2)
        S=RationalFrame(((Q(0),Q(1)),(Q(1),Q(0))))
        H=RationalFrame(((Q(1),Q(1)),(Q(0),Q(1))))
        library=(
            AffineStep(I,(Q(1),Q(0))),
            AffineStep(S,(Q(0),Q(0))),
            AffineStep(H,(Q(0),Q(-1))),
        )
        count=0
        for n in range(5):
            for actions in product(library,repeat=n):
                trace=parallel_prefix_affine((Q(2),Q(3)),tuple(actions))
                curr=(Q(2),Q(3))
                manual=[curr]
                for a in actions:
                    curr=a.act(curr)
                    manual.append(curr)
                self.assertEqual(trace.values,tuple(manual))
                self.assertEqual(trace.dependency_layers,max(0,n-1).bit_length())
                count+=1
        self.assertEqual(count,121)

    def test_circuit_parallel_depth_is_not_physical_one_step(self):
        basis=SharedBasis(1)
        origin=BasisState((Q(0),))
        increments=tuple(SparseDelta((1,),(Q(1),)) for _ in range(64))
        additive=parallel_prefix_differences(origin,increments,basis)
        self.assertEqual(len(additive.states),65)
        self.assertEqual(additive.states[-1],BasisState((Q(64),)))
        self.assertEqual(additive.parallelizable_dependency_depth,6)
        self.assertFalse(additive.actual_parallel_execution_performed)
        I=RationalFrame.identity(1)
        affine=parallel_prefix_affine((Q(0),),
                                     tuple(AffineStep(I,(Q(1),)) for _ in range(64)))
        self.assertEqual(affine.values[-1],(Q(64),))
        self.assertEqual(affine.dependency_layers,6)
        self.assertFalse(affine.actual_parallel_execution_performed)

    def test_reference_receipt_keeps_scope_boundaries(self):
        d=succ_derivative_demo()
        self.assertEqual(d["status"],"EXACT_DISCRETE_SUCC_DERIVATIVE_INTEGRATION")
        self.assertTrue(d["initial_condition_is_receiver_anchored"])
        self.assertEqual(d["ordinary_difference_steps"],4)
        self.assertTrue(d["all_intermediate_succ_states_reconstructed"])
        self.assertTrue(d["unconditional_newton_inversion_of_all_observed_finite_steps"])
        self.assertEqual(d["additive_prefix_parallel_dependency_layers"],2)
        self.assertEqual(d["polynomial_degree_law"],2)
        self.assertEqual(d["polynomial_reconstructed_states"],25)
        self.assertEqual(d["polynomial_jet_directions_count"],2)
        self.assertTrue(d["covariant_frame_transport_square_commutes"])
        self.assertFalse(d["law_premise_proved_from_finite_samples_alone"])
        self.assertFalse(d["additive_prefix_executed_on_actual_parallel_hardware"])
        self.assertFalse(d["affine_prefix_actually_parallel_executed"])
        self.assertFalse(d["real_world_source_measurement_authenticated"])
        self.assertFalse(d["RH_claimed"])


if __name__=="__main__":
    unittest.main()

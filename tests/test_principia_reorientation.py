"""Finite and unbounded reorientation from source-relative local observations."""
import unittest
from dataclasses import replace
from observational_succ.principia_causal_memory import carrier, initial_memory, step_memory
from observational_succ.principia_reorientation import (
    ReorientationTask, ReorientationError, OrientationPolicy,
    solve, verify_policy, reorient_from_anywhere, ring_with_beacon,
    ring_with_unknown_heading, homogeneous_ring,
    ordered_coupling, target_set, successors,
    trace_zigzag, zigzag_moves, find_line_beacon,
    certify_gauge_obstruction, verify_gauge_obstruction,
    reflected_ring_gauge, homogeneous_ring_gauge,
)


def load_machine():
    states=('s0','s1','l0','l1','read0','read1')
    c=carrier('causal-localization-preparation',('w0','w1'),states,
              ('noop','read','load'),('s0','s1'),
              ('0','0','0','0','0','1'),('start0','start1'),
              (states,
               ('read0','read0','read0','read1','read0','read1'),
               ('l0','l1','l0','l1','read0','read1')),
              costs=(0,1,0))
    return ReorientationTask(c,('s0','s1','l0','l1','read0','read1'),'initial')


class FiniteBalanceTests(unittest.TestCase):
    def test_known_direction_beacon_recovers_position_from_anywhere(self):
        for n in (4,5,7,9):
            task=ring_with_beacon(n)
            res=reorient_from_anywhere(task)
            self.assertEqual({y for y,_ in res},{'beacon','dark'})
            self.assertTrue(all(x.rank is not None for _,x in res))
            self.assertEqual(dict(res)['beacon'].rank,0)
            self.assertEqual(dict(res)['dark'].rank,n-2)
            for y,cert in res:
                self.assertEqual(verify_policy(task,initial_memory(task.carrier,y),cert),cert.rank)

    def test_remembered_path_recovers_original_position(self):
        task=ring_with_beacon(7)
        original=replace(task,mode='initial')
        for y,cert in reorient_from_anywhere(original):
            self.assertIsNotNone(cert.rank)
            verify_policy(original,initial_memory(original.carrier,y),cert)
        self.assertEqual(dict(reorient_from_anywhere(original))['dark'].rank,5)

    def test_homogeneous_environment_is_not_locating_even_with_compass(self):
        task=homogeneous_ring(7)
        y,cert=reorient_from_anywhere(task)[0]
        self.assertEqual(y,'dark')
        self.assertIsNone(cert.policy)
        self.assertIsNone(cert.rank)
        self.assertEqual(cert.winning_beliefs,0)

    def test_reset_recovers_current_position_not_original_identity(self):
        current=homogeneous_ring(6,reset=True,mode='current')
        original=homogeneous_ring(6,reset=True,mode='initial')
        a=reorient_from_anywhere(current)[0][1]
        b=reorient_from_anywhere(original)[0][1]
        self.assertEqual(a.rank,1)
        self.assertEqual(a.policy.action,'reset')
        self.assertIsNone(b.rank)
        m=initial_memory(current.carrier,'dark')
        m=step_memory(current.carrier,m,'reset','dark')
        self.assertEqual(len(m.coupling),6)
        self.assertEqual({q for _,q in m.coupling},{'x0'})
        self.assertEqual(len({w for w,_ in m.coupling}),6)

    def test_direction_ambiguity_is_a_real_gauge_barrier(self):
        task=ring_with_unknown_heading(5,side_marker=False,coordinate='pose')
        for y,cert in reorient_from_anywhere(task):
            self.assertIsNone(cert.rank,(y,cert.rank))
        # The positions of the same indistinguishable pose pairs are not unique.
        c=task.carrier
        for origin in ('0:+1','0:-1'):
            self.assertEqual(c.outputs[c.states.index(origin)],'beacon')

    def test_source_marker_restores_orientation(self):
        for n in (5,7):
            task=ring_with_unknown_heading(n,side_marker=True,coordinate='pose')
            res=reorient_from_anywhere(task)
            self.assertEqual({y for y,_ in res},{'beacon','dark','eastmark'})
            for y,cert in res:
                self.assertIsNotNone(cert.rank, (n,y))
                verify_policy(task,initial_memory(task.carrier,y),cert)

    def test_position_target_can_be_recovered_without_absolute_heading(self):
        task=ring_with_unknown_heading(5,side_marker=False,coordinate='position')
        for y,cert in reorient_from_anywhere(task):
            self.assertIsNotNone(cert.rank, y)
        self.assertEqual(dict(reorient_from_anywhere(task))['beacon'].rank,0)

    def test_good_direction_is_decreasing_worst_case_rank_not_just_fewer_worlds(self):
        task=load_machine()
        m=initial_memory(task.carrier,'0')
        root=solve(task,m)
        self.assertEqual(root.rank,2)
        self.assertEqual(root.policy.action,'load')
        self.assertEqual(verify_policy(task,m,root),2)
        after=step_memory(task.carrier,m,'load','0')
        next_cert=solve(task,after)
        self.assertEqual(next_cert.rank,1)
        self.assertEqual(len(m.coupling),len(after.coupling))
        self.assertEqual(len({w for w,_ in m.coupling}),2)
        self.assertEqual(len({w for w,_ in after.coupling}),2)

    def test_source_and_observation_mismatch_does_not_manufacture_state(self):
        task=ring_with_beacon(6)
        m=initial_memory(task.carrier,'beacon')
        with self.assertRaises(Exception):
            step_memory(task.carrier,m,'forward','beacon')
        forged=replace(m,source='not-the-declared-world')
        with self.assertRaises(ReorientationError):solve(task,forged)

    def test_bad_policy_rejected(self):
        task=ring_with_beacon(5)
        m=initial_memory(task.carrier,'dark')
        cert=solve(task,m)
        self.assertEqual(cert.rank,3)
        forged=replace(cert,rank=1)
        with self.assertRaises(ReorientationError):verify_policy(task,m,forged)
        forged=replace(cert,policy=OrientationPolicy(None,'x0'))
        with self.assertRaises(ReorientationError):verify_policy(task,m,forged)
        forged=replace(cert,source='wrong-source')
        with self.assertRaises(ReorientationError):verify_policy(task,m,forged)

    def test_reflection_automorphism_is_a_positive_no_go_certificate(self):
        task=ring_with_unknown_heading(5,side_marker=False,coordinate='pose')
        cert=certify_gauge_obstruction(task,reflected_ring_gauge(5))
        self.assertEqual(verify_gauge_obstruction(task,cert),cert)
        self.assertNotEqual(cert.witness[0],cert.witness[1])
        with self.assertRaises(ReorientationError):
            verify_gauge_obstruction(task,replace(cert,source='forged'))

    def test_a_real_landmark_falsifies_the_reflection_automorphism(self):
        task=ring_with_unknown_heading(5,side_marker=True,coordinate='pose')
        with self.assertRaises(ReorientationError):
            certify_gauge_obstruction(task,reflected_ring_gauge(5))

    def test_homogeneous_ring_has_rotation_symmetry_except_after_reset(self):
        task=homogeneous_ring(5,reset=False)
        cert=certify_gauge_obstruction(task,homogeneous_ring_gauge(5))
        self.assertEqual(verify_gauge_obstruction(task,cert),cert)
        with self.assertRaises(ReorientationError):
            certify_gauge_obstruction(homogeneous_ring(5,reset=True),homogeneous_ring_gauge(5))

    def test_symmetry_does_not_refute_a_gauge_invariant_target(self):
        task=ring_with_unknown_heading(5,side_marker=False,coordinate='distance')
        with self.assertRaises(ReorientationError):
            certify_gauge_obstruction(task,reflected_ring_gauge(5))
        self.assertTrue(all(cert.rank is not None for _,cert in reorient_from_anywhere(task)))

    def test_no_go_is_not_forged_policy_certificate(self):
        task=homogeneous_ring(4)
        m=initial_memory(task.carrier,'dark')
        cert=solve(task,m)
        self.assertIsNone(cert.rank)
        self.assertIsNone(verify_policy(task,m,cert))
        # A claimed negative certificate is verified by a separate full solver,
        # not just the positive-policy verifier: see independent oracle.


class InfiniteReorientationTests(unittest.TestCase):
    def test_exhaustive_but_no_uniform_finite_horizon(self):
        for radius in range(1,9):
            trace=trace_zigzag(radius)
            self.assertEqual(len(trace)-1,2*radius*radius+radius)
            self.assertEqual(trace[-1],-radius)
            self.assertEqual(set(range(-radius,radius+1))-set(trace),set())
            self.assertEqual(len(tuple(zigzag_moves(radius))),len(trace)-1)
        for x in range(-12,13):
            response=find_line_beacon(x,radius=max(abs(x),1))
            self.assertEqual(response[0],x)
            self.assertEqual(response[2],0)
            self.assertLessEqual(response[1],2*abs(x)**2+abs(x))

    def test_too_short_search_has_no_entitlement_to_success(self):
        self.assertIsNone(find_line_beacon(100,radius=5))
        self.assertIsNone(find_line_beacon(-100,radius=5))
        with self.assertRaises(ReorientationError):tuple(zigzag_moves(-1))
        with self.assertRaises(ReorientationError):find_line_beacon(1.5,radius=2)


if __name__=='__main__':unittest.main()

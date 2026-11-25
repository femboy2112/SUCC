"""No omniscient feel compass: spectral *fiber* tracks every possible self."""
import unittest
from dataclasses import replace
from observational_succ.principia_causal_memory import initial_memory,step_memory
from observational_succ.principia_reorientation import homogeneous_ring,ring_with_beacon
from observational_succ.principia_dual_compass import make_appraisal,CompassError,dft4,shift4
from observational_succ.principia_self_coupling_fourier import (
    make_chart,self_coupled_fiber,verify_self_coupled_fiber,
)

class SelfCouplingFourierTests(unittest.TestCase):
    def test_unknown_origin_keeps_all_candidate_spatial_phases(self):
        task=homogeneous_ring(4)
        c=task.carrier
        chart=make_chart(c,(0,1,2,3))
        scale=make_appraisal(c,{'forward':0},{'dark':0})
        m=initial_memory(c,'dark')
        fiber=self_coupled_fiber(c,m,chart,scale)
        self.assertEqual(len(fiber.entries),4)
        self.assertEqual(set(entry.spatial_trace for entry in fiber.entries),
                         {(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)})
        self.assertEqual(len({entry.modes for entry in fiber.entries}),4)
        # All four candidates have identical spectral *power*, but distinct phase.
        self.assertEqual(len({tuple(x.squared_abs() for x in entry.modes)
                              for entry in fiber.entries}),1)
        self.assertEqual(verify_self_coupled_fiber(c,m,chart,scale,fiber),fiber)

    def test_more_movement_cannot_recover_unknown_absolute_phase(self):
        task=homogeneous_ring(4)
        c=task.carrier
        chart=make_chart(c,(0,1,2,3))
        scale=make_appraisal(c,{'forward':1},{'dark':0})
        m=initial_memory(c,'dark')
        for _ in range(7):m=step_memory(c,m,'forward','dark')
        f=self_coupled_fiber(c,m,chart,scale)
        self.assertEqual(len(f.entries),4)
        self.assertEqual(len(set(x.spatial_trace for x in f.entries)),4)
        self.assertEqual(len({x.modes for x in f.entries}),4)
        self.assertEqual(len({tuple(z.squared_abs() for z in x.modes) for x in f.entries}),1)
        # A full self-model contains four possible self states, not a magic compass.

    def test_landmark_filters_self_phase_candidates_by_actual_observation(self):
        task=ring_with_beacon(4)
        c=task.carrier
        chart=make_chart(c,(0,1,2,3))
        scale=make_appraisal(c,{'forward':0,'stay':0},{'dark':0,'beacon':1})
        m=initial_memory(c,'beacon')
        f=self_coupled_fiber(c,m,chart,scale)
        self.assertEqual(len(f.entries),1)
        self.assertEqual(f.entries[0].original_world,'x0')
        self.assertEqual(f.entries[0].spatial_trace,(1,0,0,0))
        self.assertEqual(verify_self_coupled_fiber(c,m,chart,scale,f),f)

    def test_same_beacon_environment_after_one_step_filters_hidden_phase(self):
        task=ring_with_beacon(4)
        c=task.carrier
        chart=make_chart(c,(0,1,2,3))
        scale=make_appraisal(c,{'forward':0,'stay':0},{'dark':0,'beacon':1})
        m=initial_memory(c,'dark')
        self.assertEqual(len(self_coupled_fiber(c,m,chart,scale).entries),3)
        m=step_memory(c,m,'forward','beacon')
        f=self_coupled_fiber(c,m,chart,scale)
        self.assertEqual(len(f.entries),1)
        self.assertEqual(f.entries[0].original_world,'x3')
        self.assertEqual(f.entries[0].current_state,'x0')

    def test_chart_rotation_transports_spectra_covariantly_not_absolute_phase(self):
        task=homogeneous_ring(4)
        c=task.carrier
        scale=make_appraisal(c,{'forward':0},{'dark':0})
        m=initial_memory(c,'dark')
        x=self_coupled_fiber(c,m,make_chart(c,(0,1,2,3)),scale)
        y=self_coupled_fiber(c,m,make_chart(c,(1,2,3,0)),scale)
        self.assertNotEqual(x.source,y.source)
        for a,b in zip(x.entries,y.entries):
            self.assertEqual(b.spatial_trace,shift4(a.spatial_trace,1))
            self.assertEqual(b.modes,dft4(b.spatial_trace))
            self.assertEqual(tuple(z.squared_abs() for z in a.modes),
                             tuple(z.squared_abs() for z in b.modes))

    def test_forged_one_candidate_truth_or_wrong_chart_is_refused(self):
        task=homogeneous_ring(4)
        c=task.carrier
        chart=make_chart(c,(0,1,2,3))
        scale=make_appraisal(c,{'forward':0},{'dark':0})
        m=initial_memory(c,'dark')
        f=self_coupled_fiber(c,m,chart,scale)
        with self.assertRaises(CompassError):
            verify_self_coupled_fiber(c,m,chart,scale,replace(f,entries=f.entries[:1]))
        with self.assertRaises(CompassError):
            verify_self_coupled_fiber(c,m,make_chart(c,(1,2,3,0)),scale,f)
        with self.assertRaises(CompassError):
            make_chart(c,(0,1,2))

if __name__=='__main__':unittest.main()

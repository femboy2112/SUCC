"""Exact tests and adversarial controls for conditional observable choice."""
import itertools
import random
import unittest
from fractions import Fraction as Q

from observational_succ.equivariant_choice import (
    FiniteActionQuotient, constraint_matrix, delta_section,
    finite_swap_model, incompatible_predecessors_model,
    minimal_merging_model, transient_cycle_model,
    verify_point_section, point_section, verify_kernel,
    uniform_fiber_kernel, stochastic_section, verify_farkas,
    max_covariance_defect, actions_generate_finite_group,
    stabilizer_fixed_section, lax_fiber_transport, translation_window_defect,
    FiniteMarkovQuotient, markov_stochastic_section, verify_markov_kernel,
)


class EquivariantChoiceTests(unittest.TestCase):
    def test_every_equivariant_quotient_has_lax_set_valued_lift(self):
        for m in (minimal_merging_model(), incompatible_predecessors_model(),
                  transient_cycle_model(), finite_swap_model()):
            self.assertTrue(lax_fiber_transport(m))
        m = minimal_merging_model()
        t, u = m.source_actions[0], m.report_actions[0]
        # The inclusion is strict for the u source fibre: {b} subset {b,c}.
        self.assertEqual({t[x] for x in m.fibers[0]}, {1})
        self.assertEqual(set(m.fibers[u[0]]), {1, 2})

    def test_integer_shift_approximate_probability_but_never_exact(self):
        for n in (0,1,2,3,5,11,50):
            self.assertEqual(translation_window_defect(n), Q(1, 2*n+1))
        self.assertGreater(translation_window_defect(50), Q(0))
        self.assertLess(translation_window_defect(50), translation_window_defect(5))
        with self.assertRaises(ValueError):
            translation_window_defect(-1)

    def test_one_edge_mutation_repairs_exact_section(self):
        broken=minimal_merging_model()
        # Only the b transition changes: b->b rather than b->c.
        repaired=FiniteActionQuotient((0,1,1),2,((1,1,2),),((1,1),))
        self.assertIsNone(stochastic_section(broken))
        self.assertEqual(point_section(repaired),(0,1))
        self.assertTrue(verify_kernel(repaired,stochastic_section(repaired)))

    def test_one_extra_identity_probe_repairs_current_state_only(self):
        # Refinement by a readout revealing b/c is an ASSUMED new instrument.
        coarse=minimal_merging_model()
        refined=FiniteActionQuotient((0,1,2),3,coarse.source_actions,((1,2,2),))
        self.assertIsNone(stochastic_section(coarse))
        self.assertEqual(point_section(refined),(0,1,2))
        self.assertTrue(verify_kernel(refined,stochastic_section(refined)))

    def test_minimal_one_action_no_stochastic_section(self):
        m = minimal_merging_model()
        self.assertEqual(m.fibers, ((0,), (1, 2)))
        self.assertIsNone(point_section(m))
        self.assertIsNone(stochastic_section(m))
        self.assertFalse(verify_kernel(m, uniform_fiber_kernel(m)))
        # Arbitrary selection (a,b) exists but fails T equivariance.
        self.assertFalse(verify_point_section(m, (0, 1)))
        self.assertFalse(verify_point_section(m, (0, 2)))

    def test_three_state_no_go_farkas_exact_certificate(self):
        m = minimal_merging_model()
        A, b, cols, labels = constraint_matrix(m)
        self.assertEqual(cols, ((0, 0), (1, 1), (1, 2)))
        y = [Q(0)] * len(b)
        y[labels.index(('normal', 0))] = -1
        y[labels.index(('action', 0, 0, 1))] = 1
        y[labels.index(('action', 0, 1, 1))] = -1
        self.assertTrue(verify_farkas(A, b, tuple(y)))
        self.assertFalse(verify_farkas(A, b, tuple(-w for w in y)))
        self.assertFalse(verify_farkas(A, b, tuple(Q(0) for _ in y)))

    def test_four_state_history_merge_no_stochastic_section(self):
        m = incompatible_predecessors_model()
        self.assertIsNone(point_section(m))
        self.assertIsNone(stochastic_section(m))
        self.assertEqual(m.fibers, ((0,), (1,), (2, 3)))

    def test_quantitative_gap_achieves_exact_half_tv(self):
        m = minimal_merging_model()
        for p_num in range(21):
            p = Q(p_num, 20)
            k = ((Q(1), Q(0), Q(0)), (Q(0), p, Q(1)-p))
            self.assertEqual(max_covariance_defect(m, k), max(p, Q(1)-p))
            self.assertGreaterEqual(max_covariance_defect(m, k), Q(1, 2))
        self.assertEqual(max_covariance_defect(
            m, ((Q(1), Q(0), Q(0)), (Q(0), Q(1,2), Q(1,2)))), Q(1,2))

    def test_two_point_swap_stochastic_but_not_deterministic(self):
        m = finite_swap_model()
        self.assertTrue(m.is_group_generated())
        self.assertIsNone(point_section(m))
        self.assertIsNone(stabilizer_fixed_section(m))
        k = stochastic_section(m)
        self.assertEqual(k, ((Q(1,2), Q(1,2)),))
        self.assertTrue(verify_kernel(m,k))

    def test_nongroup_transient_cycle_stochastic_not_deterministic(self):
        m = transient_cycle_model()
        self.assertFalse(m.is_group_generated())
        self.assertIsNone(point_section(m))
        self.assertFalse(verify_kernel(m, uniform_fiber_kernel(m)))
        self.assertEqual(stochastic_section(m), ((Q(1,2), Q(1,2), Q(0)),))

    def test_group_nontrivial_report_action_section_exists(self):
        # C2 swaps both reports. Stabilisers trivial: a source section exists.
        m = FiniteActionQuotient((0,0,1,1),2,((2,3,0,1),),((1,0),))
        self.assertTrue(m.is_group_generated())
        self.assertEqual(len(actions_generate_finite_group(m)), 2)
        s = stabilizer_fixed_section(m)
        self.assertIsNotNone(s)
        self.assertTrue(verify_point_section(m,s))
        self.assertTrue(verify_kernel(m, uniform_fiber_kernel(m)))

    def test_group_nontrivial_Y_action_stabilizer_blocks_point(self):
        # A 4-cycle on X acts by a 2-cycle on Y, but its square swaps
        # the two hidden source states in each fibre.
        m=FiniteActionQuotient((0,0,1,1),2,((2,3,1,0),),((1,0),))
        self.assertTrue(m.is_group_generated())
        self.assertEqual(len(actions_generate_finite_group(m)),4)
        self.assertIsNone(point_section(m))
        self.assertIsNone(stabilizer_fixed_section(m))
        self.assertTrue(verify_kernel(m,uniform_fiber_kernel(m)))

    def test_finite_group_invariant_probability_simplex(self):
        # C2 swaps 0,1, leaves 2 fixed; invariants are convex mixtures
        # of delta_2 and uniform_{0,1}, rather than a unique posterior.
        m=FiniteActionQuotient((0,0,0),1,((1,0,2),),((0,),))
        self.assertEqual(stabilizer_fixed_section(m),(2,))
        for t in (Q(0),Q(1,4),Q(1,2),Q(1)):
            k=((t/2,t/2,Q(1)-t),)
            self.assertTrue(verify_kernel(m,k))

    def test_group_fiber_uniform_always_equivariant(self):
        rng = random.Random(8033)
        cases=0
        for nx in (2,3,4,5):
            for _ in range(90):
                ny=rng.randint(1,nx)
                q=list(range(ny))+[rng.randrange(ny) for _ in range(nx-ny)]
                rng.shuffle(q)
                # choose a random permutation tX preserving q-fibre cardinalities,
                # by taking identity on Y and swapping inside each fibre.
                t=list(range(nx))
                for yy in range(ny):
                    ids=[i for i,x in enumerate(q) if x==yy]
                    dst=ids[:]
                    rng.shuffle(dst)
                    for i,j in zip(ids,dst):t[i]=j
                m=FiniteActionQuotient(tuple(q),ny,(tuple(t),),(tuple(range(ny)),))
                self.assertTrue(verify_kernel(m,uniform_fiber_kernel(m)))
                self.assertEqual(point_section(m) is not None,
                                 stabilizer_fixed_section(m) is not None)
                cases+=1
        self.assertEqual(cases, 360)

    def test_all_two_state_single_action_models_have_stochastic_lifts(self):
        count=0
        for ny in (1,2):
            for q in itertools.product(range(ny), repeat=2):
                if set(q)!=set(range(ny)): continue
                for t in itertools.product(range(2),repeat=2):
                    for u in itertools.product(range(ny),repeat=ny):
                        if all(q[t[x]]==u[q[x]] for x in range(2)):
                            m=FiniteActionQuotient(q,ny,(t,),(u,))
                            k=stochastic_section(m)
                            self.assertIsNotNone(k)
                            self.assertTrue(verify_kernel(m,k))
                            count+=1
        self.assertEqual(count, 12)

    def test_exhaustive_three_state_one_action_census(self):
        count=0
        no_prob=0
        bad_examples=[]
        for ny in (1,2,3):
            for q in itertools.product(range(ny), repeat=3):
                if set(q)!=set(range(ny)): continue
                for t in itertools.product(range(3),repeat=3):
                    for u in itertools.product(range(ny),repeat=ny):
                        if all(q[t[x]]==u[q[x]] for x in range(3)):
                            m=FiniteActionQuotient(q,ny,(t,),(u,))
                            k=stochastic_section(m)
                            if k is None:
                                no_prob+=1
                                bad_examples.append((q,t,u))
                            else:
                                self.assertTrue(verify_kernel(m,k))
                            count+=1
        self.assertEqual(count,279)
        self.assertEqual(no_prob,24)
        self.assertIn(((0,1,1),(1,2,2),(1,1)),bad_examples)

    def test_stochastic_source_positive_markov_lift(self):
        # Source a stochastically splits into absorbing b,c. The observed
        # deterministic process u->w is genuine, and a stochastic lift exists.
        h=Q(1,2)
        m=FiniteMarkovQuotient((0,1,1),2,
            ((Q(0),h,h),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1))),
            ((Q(0),Q(1)),(Q(0),Q(1))))
        k=markov_stochastic_section(m)
        self.assertIsNotNone(k)
        self.assertEqual(k, ((Q(1),Q(0),Q(0)),(Q(0),h,h)))
        self.assertTrue(verify_markov_kernel(m,k))

    def test_stochastic_source_negative_markov_lift(self):
        # Identical observed process u->w, but b is transient: the required
        # source lift cannot be invariant after entering w.
        h=Q(1,2)
        m=FiniteMarkovQuotient((0,1,1),2,
            ((Q(0),h,h),(Q(0),Q(0),Q(1)),(Q(0),Q(0),Q(1))),
            ((Q(0),Q(1)),(Q(0),Q(1))))
        self.assertIsNone(markov_stochastic_section(m))

    def test_stochastic_source_forward_lumpability_is_required(self):
        with self.assertRaises(ValueError):
            FiniteMarkovQuotient((0,1,1),2,
               ((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(1),Q(0),Q(0))),
               ((Q(1),Q(0)),(Q(0),Q(1))))

    def test_two_generator_two_state_no_stochastic_section(self):
        m=FiniteActionQuotient((0,0),1,((0,0),(1,1)),((0,),(0,)))
        self.assertIsNone(point_section(m))
        self.assertIsNone(stochastic_section(m))
        # Each generator individually allows a fixed point, both simultaneously don't.
        for t in ((0,0),(1,1)):
            reduced=FiniteActionQuotient((0,0),1,(t,),((0,),))
            self.assertIsNotNone(stochastic_section(reduced))

    def test_invalid_equivariance_detected(self):
        with self.assertRaises(ValueError):
            FiniteActionQuotient((0,1,1),2,((0,0,0),),((1,1),))
        with self.assertRaises(ValueError):
            FiniteActionQuotient((0,0),2,((1,0),),((0,1),))

    def test_large_solver_refuses_unverified_infeasibility(self):
        m=FiniteActionQuotient(tuple(range(17)),17,(tuple(range(17)),),(tuple(range(17)),))
        with self.assertRaises(ValueError):
            stochastic_section(m, max_variables=15)

    def test_probes_history_not_recoverable_from_current_only(self):
        # Source histories a->c and b->c, fully differentiated before activation.
        initial_histories=('a_c','b_c')
        now={'a_c':'c','b_c':'c'}
        self.assertEqual(len(set(now.values())),1)
        # Adding archived origin transcript distinguishes without source disturbance.
        archive={'a_c':'a','b_c':'b'}
        self.assertEqual(len(set(archive.values())),2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

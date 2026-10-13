"""Independent exact controls for all six Cambrian physics/logic assignments."""
from fractions import Fraction as Q
import random
import unittest

from observational_succ.cambrian_f_closure import (
    ClosureError, BlockSystem, add, dot, finite_closure_obstruction, fluid_high_high_witness,
    finite_query_rival, identity, iszero, leray, mat, mm, mv, power, scalar_hankel_rank,
    quantum_backaction_witness, rational_null_rays, null_probe_constraint_rank,
    maxwell_symbol_square, attention_policy_step, attention_witness, tr,
)
from observational_succ.quantum_records import Instrument, QuantumRecordError


def scalar_system(A=0, B=1, C=1, D=Q(1, 2), E=1, H=0):
    return BlockSystem(*(((q,),) for q in (A, B, C, D, E, H)))


def full_block(system):
    return tuple(tuple(a)+tuple(b) for a,b in zip(system.A,system.B)) + \
           tuple(tuple(c)+tuple(d) for c,d in zip(system.C,system.D))


class ClosureAndMemoryTests(unittest.TestCase):
    def test_exact_memory_matches_independent_full_block_powers(self):
        rng = random.Random(2026101332)
        for _ in range(32):
            r, h, m = rng.randrange(1,4), rng.randrange(1,5), rng.randrange(1,3)
            matrix = lambda a,b: tuple(tuple(Q(rng.randrange(-3,4), rng.randrange(1,5))
                                                  for _ in range(b)) for _ in range(a))
            s = BlockSystem(matrix(r,r),matrix(r,h),matrix(h,r),matrix(h,h),
                            matrix(r,m),matrix(h,m))
            x0, z0 = tuple(Q(rng.randrange(-2,3)) for _ in range(r)), \
                     tuple(Q(rng.randrange(-2,3)) for _ in range(h))
            inputs = tuple(tuple(Q(rng.randrange(-2,3)) for _ in range(m)) for _ in range(7))
            xs, zs = s.simulate(x0,z0,inputs)
            f = full_block(s)
            forcing = tuple(tuple(e) for e in s.E) + tuple(tuple(t) for t in s.H)
            for n in range(1,8):
                # Independent unpartitioned variation-of-constants oracle.
                value = mv(power(f,n),x0+z0)
                for j in range(n):
                    value = add(value,mv(mm(power(f,n-1-j),forcing),inputs[j]))
                self.assertEqual(value,xs[n]+zs[n])
                self.assertEqual(s.memory_successor(xs[:n],inputs[:n],z0),xs[n])

    def test_unrestricted_hidden_initial_closure_requires_B_zero(self):
        s = scalar_system(C=0,H=0)
        self.assertTrue(s.closure_certificate()['zero_hidden_initial_closure'])
        self.assertFalse(s.closure_certificate()['all_hidden_initial_closure'])
        self.assertNotEqual(s.step((2,),(0,),(0,))[0],s.step((2,),(1,),(0,))[0])

    def test_zero_B_closes_for_arbitrary_hidden_forcing_and_initials(self):
        s = scalar_system(A=2,B=0,C=7,H=-4,D=3,E=5)
        report = s.closure_certificate()
        self.assertTrue(report['all_hidden_initial_closure'])
        self.assertTrue(report['zero_hidden_initial_closure'])
        xs,_ = s.simulate((3,),(19,),((1,),(-2,),(4,)))
        for n,u in enumerate((1,-2,4)):
            self.assertEqual(xs[n+1],(2*xs[n][0]+5*u,))

    def test_feedback_memory_failure_not_detected_at_initial_step(self):
        s = scalar_system(A=0,B=1,C=1,D=Q(1,3),E=0)
        xs,_ = s.simulate((1,),(0,),((0,),)*3)
        self.assertEqual(xs[1],(0,))
        self.assertEqual(xs[2],(1,))
        self.assertFalse(s.closure_certificate()['zero_hidden_initial_closure'])

    def test_input_memory_failure_with_no_resolved_feedback(self):
        s = scalar_system(C=0,H=2,E=0)
        xs,_ = s.simulate((0,),(0,),((1,),(0,)))
        self.assertEqual(xs,((Q(0),),(Q(0),),(Q(2),)))
        self.assertFalse(s.closure_certificate()['zero_hidden_initial_closure'])

    def test_hidden_nonzero_but_unobservable_excitation_all_kernels_zero(self):
        s = BlockSystem(((2,),),((1,0),),((0,),(1,)),((Q(1,2),0),(0,Q(1,3))),
                        ((1,),),((0,),(2,)))
        self.assertTrue(s.closure_certificate()['zero_hidden_initial_closure'])
        self.assertFalse(s.closure_certificate()['all_hidden_initial_closure'])
        self.assertTrue(all(iszero(s.kernel(k)) for k in range(20)))

    def test_cayley_hamilton_horizon_is_sharp(self):
        for h in (1,2,3,4,7):
            d = tuple(tuple(Q(j == i+1) for j in range(h)) for i in range(h))
            s = BlockSystem(((0,),),(tuple(Q(i == 0) for i in range(h)),),
                            tuple((Q(i == h-1),) for i in range(h)),d,((0,),),
                            tuple((Q(0),) for _ in range(h)))
            self.assertTrue(all(iszero(s.kernel(k)) for k in range(h-1)))
            self.assertEqual(s.kernel(h-1),((Q(1),),))
            xs,_ = s.simulate((1,),tuple(Q(0) for _ in range(h)),((0,),)*(h+1))
            self.assertEqual(xs[-1],(Q(1),))
            self.assertFalse(s.closure_certificate()['zero_hidden_initial_closure'])

    def test_behavioral_equivalence_does_not_determine_hidden_count(self):
        one = scalar_system(A=0,B=1,C=1,D=Q(1,2),E=1)
        twin = BlockSystem(((0,),),((Q(1,2),Q(1,2)),),((1,),(1,)),
                           ((Q(1,2),0),(0,Q(1,2))),((1,),),((0,),(0,)))
        rng = random.Random(320032)
        heldout = tuple((Q(rng.randrange(-4,5),rng.randrange(1,5)),) for _ in range(19))
        self.assertEqual(one.simulate((Q(2,7),),(0,),heldout)[0],
                         twin.simulate((Q(2,7),),(0,0),heldout)[0])
        self.assertEqual(scalar_hankel_rank(twin,4),1)
        self.assertEqual((one.hidden_dimension,twin.hidden_dimension),(1,2))

    def test_two_distinct_rates_have_exact_rank_two_witness(self):
        s = BlockSystem(((0,),),((1,1),),((1,),(1,)),
                        ((Q(1,2),0),(0,Q(1,3))),((0,),),((0,),(0,)))
        a,b,c = (s.kernel(k)[0][0] for k in range(3))
        self.assertEqual(a*c-b*b,Q(1,36))
        self.assertEqual(scalar_hankel_rank(s,3),2)

    def test_wrong_kernel_mutation_fails_a_fresh_input(self):
        s = scalar_system()
        bad = scalar_system(D=Q(3,5))
        inputs = ((Q(0),),(Q(2,7),),(Q(-1,3),),(Q(4,11),))
        self.assertNotEqual(s.simulate((Q(3,8),),(0,),inputs)[0],
                            bad.simulate((Q(3,8),),(0,),inputs)[0])

    def test_general_fiber_closure_positive_and_negative_controls(self):
        states = ((0,0),(0,1),(1,0),(1,1))
        project = lambda s: s[0]
        good = lambda s,a: (1-s[0],s[1])
        bad = lambda s,a: (s[1],s[0])
        self.assertIsNone(finite_closure_obstruction(states,('go',),project,good))
        self.assertIsNotNone(finite_closure_obstruction(states,('go',),project,bad))

    def test_malformed_interfaces_rejected(self):
        with self.assertRaises(ClosureError):
            BlockSystem(((1,2),),((1,),),((1,),),((1,),),((1,),),((1,),))
        with self.assertRaises(ValueError):
            scalar_system(D=0.5)
        with self.assertRaises(ClosureError):
            scalar_system().memory_successor(((1,),),(),(0,))
        with self.assertRaises(ClosureError):
            finite_closure_obstruction((0,1),('a',),lambda x:x,lambda x,a:2)


class QuantumInstrumentTests(unittest.TestCase):
    def test_equal_povm_different_future_exact(self):
        r=quantum_backaction_witness()
        self.assertTrue(r['same_povm'])
        self.assertTrue(r['same_initial_outcome_law'])
        self.assertEqual(r['future_luders_Z'],{'0':Q(0),'1':Q(1)})
        self.assertEqual(r['future_reset_Z'],{'0':Q(1),'1':Q(0)})

    def test_unconditional_trace_distance_squared_contracts(self):
        # For real symmetric trace-zero 2x2 differences, D_trace^2=a^2+b^2.
        states=[]
        for a,b in ((1,0),(0,1),(Q(3,5),Q(4,5)),(Q(5,13),Q(-12,13))):
            states.append(mat(((a*a,a*b),(a*b,b*b))))
        for p in (Q(1,7),Q(3,8),Q(5,11)):
            states.append(mat(((p,0),(0,1-p))))
        distance2=lambda a,b:(a[0][0]-b[0][0])**2+(a[0][1]-b[0][1])**2
        dephase=lambda a:mat(((a[0][0],0),(0,a[1][1])))
        reset=lambda a:mat(((1,0),(0,0)))
        swap=lambda a:mat(((a[1][1],a[1][0]),(a[0][1],a[0][0])))
        for a in states:
            for b in states:
                for channel in (dephase,reset,swap):
                    self.assertLessEqual(distance2(channel(a),channel(b)),distance2(a,b))

    def test_normalized_postselection_is_not_trace_preserving_DPI(self):
        filt=Instrument('cambrian_f_filter',(
            ('kept',mat(((1,0),(0,Q(3,5))))),
            ('other',mat(((0,0),(0,Q(4,5)))))))
        a,b=mat(((0,0),(0,1))),mat(((Q(1,10),0),(0,Q(9,10))))
        _,pa=filt.event(a,'kept'); _,pb=filt.event(b,'kept')
        self.assertEqual(pb[0][0]-pa[0][0],Q(25,106))
        self.assertGreater(pb[0][0]-pa[0][0],b[0][0]-a[0][0])

    def test_invalid_instrument_mutation_rejected(self):
        with self.assertRaises(QuantumRecordError):
            Instrument('cambrian_f_bad',(('0',mat(((1,0),(0,0)))),))


class GeometryAndFluidTests(unittest.TestCase):
    def test_rational_null_rays_leave_exactly_one_metric_scale(self):
        for spatial in (1,2,3,5):
            rk,coords=null_probe_constraint_rank(spatial)
            self.assertEqual(rk,coords-1)
            for v in rational_null_rays(spatial):
                self.assertEqual(-v[0]*v[0]+dot(v[1:],v[1:]),0)
                self.assertEqual(Q(7,3)*(-v[0]*v[0]+dot(v[1:],v[1:])),0)

    def test_clock_normalization_distinguishes_conformal_scale(self):
        v=(Q(1),Q(0),Q(0),Q(0))
        q=-v[0]**2+dot(v[1:],v[1:])
        self.assertNotEqual(q,4*q)
        self.assertEqual((q,4*q),(Q(-1),Q(-4)))

    def test_maxwell_longitudinal_mode_excluded_by_constraints(self):
        xi=(Q(2),Q(3),Q(6)); c=Q(2)
        s,s2=maxwell_symbol_square(xi,c)
        self.assertEqual(mv(s,xi+(Q(0),)*3),(Q(0),)*6)
        self.assertNotEqual(dot(xi,xi),0)  # longitudinal violates div(E)=0
        transverse=(Q(3),Q(-2),Q(0))
        self.assertEqual(dot(xi,transverse),0)
        self.assertEqual(mv(s2,transverse+(Q(0),)*3),
                         tuple(196*x for x in transverse)+(Q(0),)*3)

    def test_incompressible_filter_negative_control_fresh_high_modes(self):
        for n in (2,3,7,13,101):
            r=fluid_high_high_witness(n)
            self.assertTrue(r['incompressible'])
            self.assertTrue(r['resolved_velocity_zero'])
            self.assertEqual(r['leray_advection_sine'],(Q(-1,2),Q(0)))
            self.assertEqual(r['resolved_acceleration_sine'],(Q(1,2),Q(0)))

    def test_independent_exact_fourier_convolution_reconstructs_fluid_stress(self):
        # u modes are REAL Fraction amplitudes; the derivative's formal i is
        # kept as a separate scalar. This implementation doesn't use cos identities.
        for n in (4,11,23):
            k,ell=(n,0),(n,1)
            a,b=(Q(0),Q(1)),(Q(1),Q(-n))
            modes={k:tuple(x/2 for x in a),(-n,0):tuple(x/2 for x in a),
                   ell:tuple(x/2 for x in b),(-n,-1):tuple(x/2 for x in b)}
            q=(0,1); imag=[Q(0),Q(0)]
            for p,up in modes.items():
                for t,ut in modes.items():
                    if tuple(p[j]+t[j] for j in range(2))==q:
                        for j in range(2):
                            imag[j]+=dot(up,t)*ut[j]
            sine=tuple(-2*x for x in imag)
            self.assertEqual(leray(q,sine),fluid_high_high_witness(n)['leray_advection_sine'])

    def test_fluid_zero_control_and_illegal_filter_claims(self):
        self.assertEqual(leray((0,1),(0,0)),(Q(0),Q(0)))
        with self.assertRaises(ClosureError): fluid_high_high_witness(1)
        with self.assertRaises(ClosureError): maxwell_symbol_square((0,0,0),1)


class LogicAndPhenomenologyTests(unittest.TestCase):
    def test_adaptive_finite_queries_leave_computable_single_hole_rival(self):
        # Queries depend on previous reported bits; all-one transcript frozen first.
        queried=[]
        cursor=3
        for n in range(29):
            queried.append(cursor)
            observed=1
            cursor=cursor*2+n+observed
        r=finite_query_rival(queried)
        j=r['rival_zero_at']
        self.assertNotIn(j,queried)
        self.assertTrue(all((0 if n==j else 1)==1 for n in queried))
        rival=lambda n: int(n!=j)
        self.assertEqual(rival(j),0)
        self.assertEqual(rival(j+1),1)
        self.assertFalse(r['universal_certification_from_this_transcript'])

    def test_large_prefix_still_has_computable_next_hole(self):
        self.assertEqual(finite_query_rival(tuple(range(1024)))['rival_zero_at'],1024)

    def test_structural_finite_proof_and_observation_have_distinct_authority(self):
        # Algebra: for arbitrary real n, n^2 >=0. The finite samples below are
        # controls for the encoding, not the universal proof of that fact.
        for n in (Q(-5,7),Q(0),Q(101,3)):
            self.assertGreaterEqual(n*n,0)
        self.assertFalse(finite_query_rival((0,1,2))['universal_certification_from_this_transcript'])

    def test_attention_belief_projection_fails_and_policy_repair_opens_path(self):
        r=attention_witness()
        self.assertIsNotNone(r['belief_only_obstruction'])
        self.assertEqual(r['protected_next'],(0,1))
        self.assertEqual(r['released_then_next'],(1,0))
        self.assertTrue(r['physical_probe_available'])
        self.assertFalse(r['empirical_cognitive_claim'])

    def test_protected_policy_remains_observationally_blind_with_correct_source_map(self):
        for source in (0,1):
            state=(0,1)
            for _ in range(17):
                state=attention_policy_step(state,source_bit=source)
            self.assertEqual(state,(0,1))
        self.assertNotEqual(attention_policy_step((0,0),source_bit=0),
                            attention_policy_step((0,0),source_bit=1))

    def test_invalid_logic_or_attention_types_rejected(self):
        with self.assertRaises(ClosureError): finite_query_rival((0,-1))
        with self.assertRaises(ClosureError): attention_policy_step((0,2))


if __name__=='__main__':
    unittest.main()

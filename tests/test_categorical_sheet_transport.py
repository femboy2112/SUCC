"""Exact finite tests plus universal integer-polynomial identities.

Local execution requires only Python stdlib. Existing project category is
not replaced; its integration adapter has its own separately gated test.
"""
import importlib.util
from pathlib import Path
import sys
import unittest
from fractions import Fraction as F
from itertools import product
from math import gcd
import random
import json

ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'categorical_sheet_transport'
def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
    return m
m=load('succ_categorical_sheet_transport_tested','sheet_transport.py')
p=load('succ_categorical_integer_polynomial_oracle','polynomial_oracle.py')

class SourceTests(unittest.TestCase):
    def test_original_four_poles_oracle(self):
        for n in range(1,81): self.assertEqual(m.source(n),m.source_oracle(n))
    def test_source_first_receipt(self): self.assertEqual(m.source(1),F(47,15))
    def test_source_order(self): self.assertEqual(15*(m.source(1)-m.source(2)),F(12301,273))
    def test_authentic_history(self): self.assertTrue(m.authenticate(m.states(30)))
    def test_changed_seed_rejected(self):
        with self.assertRaises(m.TransportError):m.authenticate(m.states(5,F(1,7)))
    def test_source_mutation_rejected(self):
        h=list(m.states(5));h[4]+=F(1,10**20)
        with self.assertRaises(m.TransportError):m.authenticate(h)
    def test_odd_growing_conductor(self):
        qs=[m.conductor(n) for n in range(1,12)]
        self.assertTrue(all(q%2 for q in qs))
        self.assertTrue(all(b%a==0 for a,b in zip(qs,qs[1:])))
        self.assertEqual(qs[:3],[15,4095,765765])
    def test_convolution_independent(self):
        for n in range(1,15):
            u=sum((16**(n-j)*m.source_oracle(j) for j in range(1,n+1)),F(0))
            self.assertEqual(u,m.states(n)[-1])
    def test_actual_another_one(self):
        x=m.SourceState(0,F(0))
        for n in range(15):
            self.assertEqual(x.value,m.states(n)[-1]);self.assertTrue(x.selected());x=x.successor()
    def test_forged_state(self):
        with self.assertRaises(m.TransportError):m.SourceState(3,F(0))
    def test_float_and_bool_rejected(self):
        for value in (True,0.5,'1/2'):
            with self.assertRaises(m.TransportError):m.R(value)

class CoverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.c=p.certificate(m.A_TERMS,m.B_TERMS,m.CURVE_TERMS)
    def test_universal_dlog(self):self.assertEqual(self.c['dlog_residual'],(0,))
    def test_universal_curve(self):self.assertEqual(self.c['curve_residual'],(0,))
    def test_universal_inverse(self):self.assertEqual(self.c['inverse_residual'],(0,))
    def test_all_positive_time_denominator(self):
        self.assertEqual(self.c['denominator_degree'],18)
        self.assertEqual(len(self.c['shifted_coefficients']),19)
        self.assertTrue(self.c['shifted_positive'])
    def test_identity_mutation_control(self):
        bad=list(m.B_TERMS);i,j,c=bad[0];bad[0]=(i,j,c+1)
        self.assertNotEqual(p.certificate(m.A_TERMS,tuple(bad),m.CURVE_TERMS)['inverse_residual'],(0,))
    def test_delay_integer_reconstruction(self):
        for n in range(1,41):self.assertEqual(m.reconstruct(*m.delay(n)),n)
    def test_delay_rational_holdouts(self):
        for z in (F(11,7),F(1001,10),F(98765,31),F(1234567,999)):
            self.assertEqual(m.reconstruct(*m.delay(z)),z)
    def test_successor_commuting_square(self):
        for z in (F(1),F(17,4),F(301,13),F(1000)):
            self.assertEqual(m.delay_successor(*m.delay(z)),m.delay(z+1))
    def test_composed_successor(self):
        pair=m.delay(F(13,7))
        for k in range(12):
            self.assertEqual(pair,m.delay(F(13,7)+k));pair=m.delay_successor(*pair)
    def test_off_curve_pair_rejected(self):
        u,v=m.delay(2)
        with self.assertRaises(m.TransportError):m.reconstruct(u,v+F(1,100))
    def test_pole_is_not_silently_dropped(self):
        for z in (F(1,2),F(3,8),F(1,4)):
            with self.assertRaises(m.TransportError):m.R(z)
    def test_global_descent_witness(self):
        # Both original values are infinity, yet the successors differ.
        self.assertEqual(m.R(F(3,2)),F(125,1152))
        self.assertEqual(m.R(F(5,4)),F(9,224))
        self.assertNotEqual(m.R(F(3,2)),m.R(F(5,4)))
    def test_real_positive_injectivity_samples(self):
        vals=[m.R(F(k,7)) for k in range(7,71)]
        self.assertTrue(all(a<b for a,b in zip(vals,vals[1:])))
    def test_curve_is_bidegree_four(self):
        self.assertEqual(max(i for i,j,c in m.CURVE_TERMS),4)
        self.assertEqual(max(j for i,j,c in m.CURVE_TERMS),4)

class CompletionTests(unittest.TestCase):
    def test_snapshot_not_stable(self):
        c=m.complete_observer((1,2,3,0),(0,0,1,1))
        self.assertEqual(c['history'][0],(0,0,1,1))
        self.assertEqual(c['labels'],(0,1,2,3))
        self.assertEqual(len(c['history']),2)
    def test_coarse_span_rebranches(self):
        t=(1,2,3,0);o=(0,0,1,1)
        one={(o[x],o[t[x]]) for x in range(4)}
        composed={(a,c) for a,b in one for bb,c in one if b==bb}
        actual={(o[x],o[t[t[x]]]) for x in range(4)}
        self.assertEqual(actual,{(0,1),(1,0)})
        self.assertIn((0,0),composed-actual)
    def test_stable_quotient_needs_no_refinement(self):
        c=m.complete_observer((1,0,3,2),(0,1,0,1))
        self.assertEqual(c['labels'],(0,1,0,1));self.assertEqual(len(c['history']),1)
    def test_unobservable_tag_not_fake_identity(self):
        c=m.complete_observer((1,0,3,2),(9,9,9,9))
        self.assertEqual(c['labels'],(0,0,0,0))
    def test_random_machines_against_pair_orbit_oracle(self):
        rng=random.Random(54891)
        for size in range(2,12):
            for _ in range(8):
                t=tuple(rng.randrange(size) for _ in range(size));o=tuple(rng.randrange(3) for _ in range(size))
                lab=m.complete_observer(t,o)['labels']
                for x,y in product(range(size),repeat=2):
                    a,b=x,y;seen=set();same=True
                    while (a,b) not in seen:
                        if o[a]!=o[b]:same=False;break
                        seen.add((a,b));a,b=t[a],t[b]
                    self.assertEqual(lab[x]==lab[y],same)
    def test_invalid_transition_rejected(self):
        with self.assertRaises(m.TransportError):m.complete_observer((1,2),(0,0))

class FrameTests(unittest.TestCase):
    def test_frame_inverse(self):
        for g in (m.IDENTITY,m.QUARTER_TURN,m.Mobius(2,3,1,2)):
            self.assertTrue(g.compose(g.inverse()).equivalent(m.IDENTITY))
    def test_infinity_chart(self):
        self.assertIsNone(m.QUARTER_TURN(-1));self.assertEqual(m.QUARTER_TURN(None),1)
    def test_marked_successor_covariance(self):
        g=m.QUARTER_TURN;sg=g.conjugate(m.SUCCESSOR)
        for z in (F(0),F(1),F(13,8),None):
            self.assertEqual(sg(g(z)),g(m.SUCCESSOR(z)))
    def test_triple_overlap_cocycle(self):
        a=m.IDENTITY;b=m.QUARTER_TURN;c=m.Mobius(3,1,2,1)
        self.assertTrue(m.frame_change(b,c).compose(m.frame_change(a,b)).equivalent(m.frame_change(a,c)))
    def test_marks_are_transported_not_frozen(self):
        poles=(F(7,8),F(1,2),F(3,8),F(1,4));g=m.QUARTER_TURN
        self.assertNotEqual(set(poles),{g(x) for x in poles})
    def test_singular_frame_rejected(self):
        with self.assertRaises(m.TransportError):m.Mobius(1,2,2,4)

class FourierTests(unittest.TestCase):
    def test_composition_on_every_basis_vector(self):
        for Q in (3,5,9,15):
            a=m.Monomial(Q,2,3,4,1);b=m.Monomial(Q,4,2,1,2)
            for x in range(Q):
                y,pb=b.apply(x);z,pa=a.apply(y)
                self.assertEqual(a.compose(b).apply(x),(z,(pa+pb)%Q))
    def test_inverse_exact(self):
        for Q in (3,5,9,15):
            a=m.Monomial(Q,2,3,4,1)
            self.assertEqual(a.inverse().compose(a),m.Monomial(Q))
    def test_fourier_kernel_orthogonality_exact(self):
        # Fourier kernel sum equals Q at coefficient 0, else zero.
        # Its surviving output/phase is obtained independently of fourier().
        for Q in (3,5,9,15):
            for a in range(1,Q):
                if gcd(a,Q)!=1:continue
                op=m.Monomial(Q,a,2,3,4)
                for x in range(Q):
                    survivors=[y for y in range(Q) if (op.b+a*y-x)%Q==0]
                    self.assertEqual(len(survivors),1);y=survivors[0]
                    self.assertEqual(op.fourier().apply(x),(y,(op.c+op.t*y)%Q))
    def test_fourier_is_functorial(self):
        a=m.Monomial(15,2,3,4,5);b=m.Monomial(15,4,2,1,3)
        self.assertEqual(a.compose(b).fourier(),a.fourier().compose(b.fourier()))
    def test_fourier_square_is_parity_conjugation(self):
        a=m.Monomial(15,2,3,4,5);parity=m.Monomial(15,-1)
        self.assertEqual(a.fourier().fourier(),parity.compose(a).compose(parity))
    def test_fourier_fourth_power(self):
        a=m.Monomial(15,2,3,4,5);b=a
        for _ in range(4):b=b.fourier()
        self.assertEqual(a,b)
    def test_phase_is_not_discarded(self):
        t=m.Monomial(15,t=2);c=m.Monomial(15,b=3)
        comm=c.compose(t).compose(c.inverse()).compose(t.inverse())
        self.assertEqual(comm,m.Monomial(15,c=6))
        self.assertNotEqual(comm,m.Monomial(15))
    def test_phase_echo_authentic(self):
        Q=m.conductor(8)
        for n in range(1,9):
            for h in (-3,1,7):
                expected=(h*Q*m.states(n)[-1]);self.assertEqual(expected.denominator,1)
                self.assertEqual(m.phase_echo(n,h,Q),m.Monomial(Q,c=int(expected)))
    def test_source_frequency_transport(self):
        Q=m.conductor(6)
        for n in range(1,7):
            op=m.propagator(n,Q);fo=op.fourier()
            for k in (0,1,2,11,Q-1):
                y,phase=fo.apply(k)
                self.assertEqual((16**n*y)%Q,k)
                self.assertEqual(phase,int(Q*m.states(n)[-1])*y%Q)
    def test_position_conductor_naturality(self):
        Q=15;QQ=105;op=m.Monomial(Q,16,2,3,4);big=op.embed(QQ);ratio=QQ//Q
        for x in range(Q):
            y,c=op.apply(x);Y,C=big.apply(ratio*x)
            self.assertEqual(Y,ratio*y);self.assertEqual(C,ratio*c)
    def test_fourier_replication_naturality(self):
        # J f(k)=f(k mod Q)/sqrt(m); compare all coefficient addresses/phases.
        Q=15;QQ=105;op=m.Monomial(Q,16,2,3,4);small=op.fourier();big=op.embed(QQ).fourier()
        si=small.inverse();bi=big.inverse()
        for k in range(QQ):
            x,phase=bi.apply(k);xx,p=si.apply(k%Q)
            self.assertEqual(x%Q,xx)
            self.assertEqual(F(phase,QQ)%1,F(p,Q)%1)
    def test_actual_original_source_conductor_naturality(self):
        small=m.source_operator(1,15);big=m.source_operator(1,105)
        for x in range(15):
            y,c=small.apply(x);Y,C=big.apply(7*x)
            self.assertEqual(Y,7*y);self.assertEqual(C,7*c)
    def test_finite_dilation_alias_needs_source_label(self):
        self.assertEqual(m.Monomial(15,16),m.Monomial(15,1))
        self.assertNotEqual(m.Monomial(105,16),m.Monomial(105,1))
    def test_embedding_composition(self):
        op=m.Monomial(15,16,2,3,4)
        self.assertEqual(op.embed(105).embed(1155),op.embed(1155))
    def test_wrong_replication_phase_control(self):
        # Copying translations without multiplying by m breaks I-naturalness.
        op=m.Monomial(15,16,2);wrong=m.Monomial(105,16,2)
        self.assertNotEqual(wrong.apply(0)[0],7*op.apply(0)[0])
    def test_missing_conductor_rejected(self):
        with self.assertRaises(m.TransportError):m.source_operator(2,15)
    def test_even_carrier_rejected(self):
        with self.assertRaises(m.TransportError):m.Monomial(16,16)
    def test_nonunit_is_not_a_unitary(self):
        with self.assertRaises(m.TransportError):m.Monomial(15,3)
    def test_point_evaluation_norm_squares(self):
        # On normalized counting coordinates ell_h(f)=sqrt(Q)f(h): norm^2=Q.
        for Q in (15,105,1155):
            # Rational cylinder witness: phi=Q*1_{k=1} in normalized Haar L2.
            phi=[Q if k==1 else 0 for k in range(Q)]
            squared_norm=sum(F(x*x,Q) for x in phi)
            evaluation_squared=phi[1]**2
            self.assertEqual(evaluation_squared/squared_norm,Q)
            self.assertGreater(evaluation_squared/squared_norm,1)


class GlobalDelayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'GLOBAL_DELAY_CERTIFICATE.json').read_text())
        cls.cert=p.global_certificate(cls.data)
    def test_exact_collision_polynomial(self):self.assertTrue(self.cert['collision_identity'])
    def test_three_frames_separate_all_finite_complex_points(self):self.assertTrue(self.cert['finite_points_separated'])
    def test_infinity_is_separated(self):self.assertTrue(self.cert['infinity_separated'])
    def test_no_collapsed_tangent(self):self.assertTrue(self.cert['immersion'])
    def test_bezout_mutation_control(self):
        data=json.loads(json.dumps(self.data));data['multipliers'][0][0][2]+=1
        self.assertFalse(p.global_certificate(data)['finite_points_separated'])
    def test_projective_rational_decoding_including_poles(self):
        values=[None,F(0),F(7,8),F(1,2),F(3,8),F(1,4),F(-1,2),F(-13,8),F(11,7),F(1000)]
        for z in values:self.assertEqual(m.reconstruct_triple(m.triple_delay(z)),z)
    def test_global_successor_square(self):
        for z in [None,F(0),F(7,8),F(1,2),F(3,8),F(1,4),F(-13,8),F(11,7)]:
            self.assertEqual(m.triple_successor(m.triple_delay(z)),m.triple_delay(None if z is None else z+1))
    def test_third_snapshot_mutation_rejected(self):
        tri=list(m.triple_delay(3));tri[2]+=F(1,10**8)
        with self.assertRaises(m.TransportError):m.reconstruct_triple(tri)
    def test_original_zero_boundary_chart(self):
        self.assertEqual(m.reconstruct(*m.delay(0)),0)
        self.assertEqual(m.reconstruct_triple(m.triple_delay(0)),0)

if __name__=='__main__':unittest.main()

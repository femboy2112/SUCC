"""Focused local exact tests. Run python -m unittest -v test_hopf_source.py.

This is NOT SUCC full CI, Lean, or a proof of π normality.
"""
from __future__ import annotations

import random
import unittest
from fractions import Fraction as F

from observational_succ.hopf_source_exact import (
    H, Sphere4, ONE, ZERO, I, J, K, SOURCE_ID, T, SOURCE_ORIGIN,
    ORIGINAL_TAPS, CHIRAL_EVEN_TAPS, CHIRAL_ODD_TAPS,
    hopf, hopf_left, hopf_right_to_left_odd, hopf_left_to_right_odd,
    t_odd_quaternion_factor, LEFT_FACTOR, RIGHT_FACTOR,
    hopf_decode_given_q2, hopf_two_step_base, t_step, t_iter,
    j_chirality, t2_quaternion_factor, t_power_matrix,
    chiral_readouts, source_tap, source_moment, original_forcing,
    original_numerator_denominator, pole_quaternion, unwrapped_zero_seed,
    paired_unwrapped_zero_seed, consecutive_hopf, source_sphere_chart,
    source_chart_next, source_chart_latitude_next, source_labelled_mixed_hopf,
    source_labelled_decode_poles, coherent_changed_seed_tail_prefix,
    coherent_changed_seed_tail_bound,
)


class QuaternionTests(unittest.TestCase):
    def test_hamilton_relations(self):
        self.assertEqual(I*I,-ONE)
        self.assertEqual(J*J,-ONE)
        self.assertEqual(K*K,-ONE)
        self.assertEqual(I*J,K)
        self.assertEqual(J*I,-K)
        self.assertEqual(J*K,I)
        self.assertEqual(K*I,J)

    def test_division_and_associativity(self):
        a=H(F(1,2), F(1,3),F(-1,4),F(3,5))
        b=H(F(2), F(-5,2),F(1,6),F(7,5))
        c=H(F(-2),F(3),F(1),F(2))
        self.assertEqual(a*(b*c),(a*b)*c)
        self.assertEqual(a*a.inverse(),ONE)
        self.assertEqual(a.inverse()*a,ONE)

    def test_hopf_exact_sphere(self):
        rs=random.Random(919)
        for _ in range(80):
            q1=H(*(F(rs.randint(-12,12),rs.randint(1,17)) for _ in range(4)))
            q2=H(*(F(rs.randint(-12,12),rs.randint(1,17)) for _ in range(4)))
            if q1==ZERO and q2==ZERO: continue
            p=hopf(q1,q2)
            self.assertEqual(p.R.norm2()+p.B**2,1)
        with self.assertRaises(ValueError):hopf(ZERO,ZERO)

    def test_right_gauge_invariance_noncommutative(self):
        q1=H(1,F(2,3),F(-4,5),F(6,7))
        q2=H(F(3,2),F(2,5),1,F(-2,7))
        for u in (I,J,K,H(F(3,5),F(4,5)),H(F(3,5),F(0),F(4,5))):
            self.assertEqual(u.norm2(),1)
            self.assertEqual(hopf(q1,q2),hopf(q1*u,q2*u))

    def test_hermitian_projector_quaternion(self):
        q1=H(1,2,3,4)
        q2=H(2,0,1,-1)
        den=q1.norm2()+q2.norm2()
        p11=H(q1.norm2()/den)
        p12=(q1*q2.conj()).scale(1/den)
        p21=(q2*q1.conj()).scale(1/den)
        p22=H(q2.norm2()/den)
        self.assertEqual(p11*p11+p12*p21,p11)
        self.assertEqual(p11*p12+p12*p22,p12)
        self.assertEqual(p21*p11+p22*p21,p21)
        self.assertEqual(p21*p12+p22*p22,p22)
        p=hopf(q1,q2)
        self.assertEqual(p11,H((1+p.B)/2))
        self.assertEqual(p22,H((1-p.B)/2))
        self.assertEqual(p12,p.R.scale(F(1,2)))


class SUCCSourceExactTests(unittest.TestCase):
    def test_source_fingerprint(self):
        self.assertIn("four-pole",SOURCE_ID)

    def test_T_matches_independent_gaussian_split(self):
        # Independent calculation in Q(i) complex pairs from PR333 source sectors.
        def mul(x,y):return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
        def conj(x):return (x[0],-x[1])
        for x in [H(2),H(1,2,3,-4),H(F(1,7),F(2,3),F(5,11),F(-1,9))]:
            z=(x.a,x.b); w=(x.c,x.d)
            u=((z[0]+w[0])/2,(z[1]-w[1])/2)
            v=((z[0]-w[0])/2,(z[1]+w[1])/2)
            g=(F(1,2),F(1,2))
            a=mul(g,u);b=mul(g,conj(v))
            new=H(a[0]+b[0],a[1]+b[1],a[0]-b[0],-a[1]+b[1])
            self.assertEqual(t_step(x),new)

    def test_operator_4_8_step(self):
        for x in [H(1),H(2,3,5,7),H(F(2,3),F(9,5),F(-3,4),F(11,13))]:
            self.assertEqual(t_iter(x,4),j_chirality(x).scale(F(-1,4)))
            self.assertEqual(t_iter(x,8),x.scale(F(1,16)))

    def test_scaled_orthogonality(self):
        for x in (H(1),I,J,K,H(1,2,3,4),H(F(1,5),F(-2,3),F(3,7),F(7,8))):
            self.assertEqual(t_step(x).norm2(),x.norm2()/2)
            for n in range(12):
                self.assertEqual(t_iter(x,n).norm2(),x.norm2()/2**n)

    def test_wrong_odd_chirality_mutation_is_rejected(self):
        # Counterfeit: replace odd v -> g*conj(v) by v -> g*v.
        def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
        def mutate(x):
            a,b,c,d=tuple(x)
            u=((a+c)/2,(b-d)/2)
            v=((a-c)/2,(b+d)/2)
            g=(F(1,2),F(1,2))
            x1=mul(g,u);y1=mul(g,v)
            return H(x1[0]+y1[0],x1[1]+y1[1],x1[0]-y1[0],-x1[1]+y1[1])
        x=SOURCE_ORIGIN
        wrong=[]
        for _ in range(8):
            wrong.append(source_tap(x));x=mutate(x)
        self.assertNotEqual(tuple(wrong),ORIGINAL_TAPS)
        self.assertNotEqual(mutate(mutate(SOURCE_ORIGIN)),t_iter(SOURCE_ORIGIN,2))

    def test_source_first_shell(self):
        x=SOURCE_ORIGIN
        a=[];even=[];odd=[]
        for _ in range(8):
            a.append(source_tap(x));e,o=chiral_readouts(x)
            even.append(e);odd.append(o);x=t_step(x)
        self.assertEqual(tuple(a),ORIGINAL_TAPS)
        self.assertEqual(tuple(even),CHIRAL_EVEN_TAPS)
        self.assertEqual(tuple(odd),CHIRAL_ODD_TAPS)
        self.assertEqual(sum(even,F(0)),F(15,4))
        self.assertEqual(sum(odd,F(0)),F(-15,4))

    def test_original_four_poles_and_rational_source(self):
        for n in range(1,151):
            self.assertEqual(original_forcing(n),source_moment(n))
            self.assertEqual(original_forcing(n),original_numerator_denominator(n))
            self.assertEqual(chiral_readouts(t_iter(SOURCE_ORIGIN,0))[0],F(4))

    def test_zero_seed_and_channel_gluing(self):
        for n in range(0,50):
            up,down,total=paired_unwrapped_zero_seed(n)
            self.assertEqual(up+down,total)
            self.assertEqual(total,unwrapped_zero_seed(n))
            self.assertEqual(total,F(0) if n==0 else 16*unwrapped_zero_seed(n-1)+original_forcing(n))

    def test_changed_seed_adversarial(self):
        # Positive source/chiral Hopf is unchanged by changing the unwrapped seed.
        for n in range(0,19):
            one_third=unwrapped_zero_seed(n,seed=F(1,3))
            exact=unwrapped_zero_seed(n)
            self.assertEqual(one_third-exact,F(16**n,3))
            self.assertEqual((one_third-exact)%1,F(1,3))

    def test_coherent_changed_seed_future_tail_control(self):
        # Using the proven BBP sum pi/16, the alternative REAL initial seed
        # c=-pi/16 gives U_n=-sum_{k>=1}16^-k r(n+k) ->0, not a normal orbit.
        # Here only finite exact rational partial tails are evaluated.
        for n in range(0,45):
            tail=coherent_changed_seed_tail_prefix(n,30)
            self.assertLess(tail,0)
            self.assertLess(-tail,coherent_changed_seed_tail_bound(n))
            self.assertEqual(coherent_changed_seed_tail_bound(n),F(8,15*(n+1)**2))

    def test_ring_incompatibility(self):
        # (1,0)*(0,1)=0 in CxC, but eta(1,0)*eta(0,1)=j in H.
        self.assertNotEqual(ONE*J,ZERO)


class HopfSourceBridgeTests(unittest.TestCase):
    def test_T_squared_exact_quaternion_factor(self):
        for x in (ONE,I,J,K,H(1,2,3,4),H(F(2,5),F(1,3),F(-8,11),F(5,7))):
            self.assertEqual(t_iter(x,2),t2_quaternion_factor(x))

    def test_odd_step_gauge_fails_explicit(self):
        q1,q2,u=ONE,I,J
        self.assertEqual(hopf(q1,q2),hopf(q1*u,q2*u))
        before=hopf(t_step(q1),t_step(q2))
        after=hopf(t_step(q1*u),t_step(q2*u))
        self.assertNotEqual(before,after)
        self.assertEqual(before,Sphere4(K,F(0)))
        self.assertEqual(after,Sphere4(-K,F(0)))

    def test_odd_step_quaternion_antilinear_exact(self):
        for x in (ONE,I,J,K,H(1,2,3,4),H(F(4,7),F(6,11),F(-9,13),F(1,5))):
            self.assertEqual(t_step(x),t_odd_quaternion_factor(x))
        self.assertEqual(LEFT_FACTOR.norm2(),2)
        self.assertEqual(RIGHT_FACTOR.norm2(),F(1,4))

    def test_left_hopf_gauge_invariance(self):
        q1=H(1,2,-3,4);q2=H(3,5,7,-11)
        for u in (I,J,K,H(F(3,5),F(4,5))):
            self.assertEqual(hopf_left(q1,q2),hopf_left(u*q1,u*q2))

    def test_odd_hopf_gauge_switch_is_exact(self):
        rs=random.Random(20261027)
        for _ in range(80):
            q1=H(*(F(rs.randint(-10,10),rs.randint(1,17)) for _ in range(4)))
            q2=H(*(F(rs.randint(-10,10),rs.randint(1,17)) for _ in range(4)))
            if q1==ZERO and q2==ZERO:continue
            right=hopf(q1,q2)
            left=hopf_left(q1,q2)
            self.assertEqual(hopf_left(t_step(q1),t_step(q2)),hopf_right_to_left_odd(right))
            self.assertEqual(hopf(t_step(q1),t_step(q2)),hopf_left_to_right_odd(left))
            for u in (I,J,K,H(F(3,5),F(4,5))):
                self.assertEqual(hopf_left(t_step(q1*u),t_step(q2*u)),hopf_right_to_left_odd(right))
                self.assertEqual(hopf(t_step(u*q1),t_step(u*q2)),hopf_left_to_right_odd(left))
            self.assertEqual(hopf_left_to_right_odd(hopf_right_to_left_odd(right)),
                             hopf_two_step_base(right))

    def test_odd_chart_transports_even_base_rotation(self):
        x=hopf(H(1,2,3,4),H(7,11,13,17))
        p=x
        for _ in range(4):
            p=hopf_left_to_right_odd(hopf_right_to_left_odd(p))
        self.assertEqual(p,x)

    def test_two_step_gauge_descends_exact(self):
        rs=random.Random(77291)
        for _ in range(60):
            q1=H(*(F(rs.randint(-10,10),rs.randint(1,13)) for _ in range(4)))
            q2=H(*(F(rs.randint(-10,10),rs.randint(1,13)) for _ in range(4)))
            if q1==ZERO and q2==ZERO:continue
            p=hopf(q1,q2)
            self.assertEqual(hopf(t_iter(q1,2),t_iter(q2,2)),hopf_two_step_base(p))
            for u in (I,J,K,H(F(3,5),F(4,5))):
                self.assertEqual(hopf(t_iter(q1*u,2),t_iter(q2*u,2)),hopf_two_step_base(p))

    def test_two_step_order_four(self):
        x=hopf(H(1,2,3,4),H(F(-2,3),F(7,5),F(6,11),F(3,7)))
        z=x
        for _ in range(4):z=hopf_two_step_base(z)
        self.assertEqual(z,x)

    def test_natural_next_state_constant_latitude(self):
        seen=set()
        for n in range(0,40):
            p=consecutive_hopf(n)
            seen.add(p.as_rational5())
            self.assertEqual(p.B,F(1,3))
            self.assertEqual(p,consecutive_hopf(n%8))
        self.assertEqual(len(seen),5)  # selected source b has only five distinct views

    def test_J_mirror_is_equatorial(self):
        for n in range(24):
            x=t_iter(SOURCE_ORIGIN,n)
            self.assertEqual(hopf(x,j_chirality(x)).B,F(0))

    def test_anchored_stereographic_inverse_and_latitude(self):
        for x in (ZERO,ONE,I,J,K,H(1,2,3,4),H(F(4,11),F(-7,13),F(15,19),F(1,17))):
            p=source_sphere_chart(x)
            self.assertEqual(hopf_decode_given_q2(p,ONE),x)
            next_p=source_chart_next(p)
            self.assertEqual(next_p,source_sphere_chart(t_step(x)))
            self.assertEqual(next_p.B,source_chart_latitude_next(p.B))
        self.assertEqual(source_chart_next(Sphere4(ZERO,F(1))),Sphere4(ZERO,F(1)))

    def test_anchored_selected_source_exact_latitudes(self):
        expected={0:F(3,5),1:F(1,3),2:F(0),3:F(-1,3),4:F(-3,5),8:F(-63,65)}
        for n,B in expected.items():
            p=source_sphere_chart(t_iter(SOURCE_ORIGIN,n))
            self.assertEqual(p.B,B)
        for n in range(0,20):
            p=source_sphere_chart(t_iter(SOURCE_ORIGIN,n))
            self.assertEqual(p.B,(F(4,2**n)-1)/(F(4,2**n)+1))

    def test_pole_quartet_stereographic_exact_decode(self):
        for n in range(1,90):
            pole=pole_quaternion(n)
            p=source_sphere_chart(pole)
            self.assertEqual(hopf_decode_given_q2(p,ONE),pole)
            self.assertEqual(sum(tuple(hopf_decode_given_q2(p,ONE)),F(0)),original_forcing(n))
            self.assertGreaterEqual(p.R.norm2(),0)

    def test_source_labelled_mixed_latitudes_and_exact_tomography(self):
        vals=[]
        for n in range(1,45):
            p=source_labelled_mixed_hopf(n)
            poles=source_labelled_decode_poles(n,p)
            self.assertEqual(poles,pole_quaternion(n))
            self.assertEqual(sum(tuple(poles),F(0)),original_forcing(n))
            vals.append(p.B)
        self.assertGreater(vals[0],0)
        self.assertLess(vals[1],0)
        self.assertGreater(vals[11],0)
        self.assertNotEqual(vals[0],vals[1])

    def test_pole_frame_permutation_is_a_noncanonical_choice(self):
        # The scalar original forcing does not determine the quaternion basis.
        for n in (1,3,17):
            q=pole_quaternion(n)
            swapped=H(q.a,q.c,q.b,q.d)
            self.assertEqual(sum(tuple(q),F(0)),sum(tuple(swapped),F(0)))
            self.assertEqual(q.norm2(),swapped.norm2())
            self.assertEqual(source_sphere_chart(q).B,source_sphere_chart(swapped).B)
            self.assertNotEqual(source_sphere_chart(q).R,source_sphere_chart(swapped).R)

    def test_mixed_chiral_time_pairing_is_not_canonical(self):
        n=4
        q=pole_quaternion(n)
        p_declared=source_labelled_mixed_hopf(n)
        p_alternative=hopf(q,t_iter(SOURCE_ORIGIN,n))
        self.assertNotEqual(p_declared.B,p_alternative.B)
        # Both partner states are genuine source states; the pairing itself
        # was an additional choice not specified by the four-pole forcing.

    def test_sign_mutation_latitude_blind_but_full_Hopf_detects(self):
        for n in (1,3,17):
            a=pole_quaternion(n)
            mutant=H(*(abs(v) for v in a))
            x=source_sphere_chart(a)
            y=source_sphere_chart(mutant)
            self.assertEqual(x.B,y.B)
            self.assertNotEqual(x.R,y.R)
            self.assertNotEqual(sum(tuple(a),F(0)),sum(tuple(mutant),F(0)))

    def test_right_gauge_changes_source_coordinates(self):
        n=3
        q1=pole_quaternion(n);q2=t_iter(SOURCE_ORIGIN,n-1)
        x=hopf(q1,q2)
        gauge=J
        self.assertEqual(x,hopf(q1*gauge,q2*gauge))
        self.assertNotEqual(q1,q1*gauge)
        self.assertNotEqual(q2,q2*gauge)
        self.assertEqual(source_labelled_decode_poles(n,x),q1)
        # Discarding the authenticated q2 loses the ability to distinguish them.


if __name__=="__main__":unittest.main(verbosity=2)

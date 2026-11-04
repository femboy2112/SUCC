"""Exact source-faithful E2 stationary observer controls; no pi-normality claims."""
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

PATH=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'stationary_e2_gamma'/'stationary_e_observer.py'
SPEC=importlib.util.spec_from_file_location('succ_stationary_e_observer',PATH)
S=importlib.util.module_from_spec(SPEC)
import sys
sys.modules[SPEC.name]=S
SPEC.loader.exec_module(S)


class ChiralGammaTowers(unittest.TestCase):
    def test_exact_old_e2_eight_taps_and_parity(self):
        self.assertEqual(S.TAPS,(4,0,0,-2,-1,-1,0,0))
        self.assertEqual(S.EVEN,(4,2,0,-1,-1,F(-1,2),0,F(1,4)))
        self.assertEqual(S.ODD,(0,-2,0,-1,0,F(-1,2),0,F(-1,4)))
        self.assertEqual(S.first_shell_invariants(),
            {'even_mass':F(15,4),'odd_mass':F(-15,4),
             'total_mass':F(0),'first_moment':F(-15)})

    def test_exact_e2_four_and_eight_chiral_return(self):
        for vector in ((0,0,0,0),(1,2,3,4),(F(1,7),F(-3,5),F(2,9),F(8,11))):
            v=tuple(map(F,vector))
            w=v
            for _ in range(4):w=S.e2_step(w)
            self.assertEqual(w,tuple(-z/4 for z in S.e2_chirality(v)))
            for _ in range(4):w=S.e2_step(w)
            self.assertEqual(w,tuple(z/16 for z in v))

    def test_e2_gain_equals_gamma_one_unit_fourier_multiplier(self):
        re,im=S.gamma_gain_unit_frequency()
        self.assertEqual((re,im),(F(1,2),F(1,2)))
        self.assertEqual(re*re+im*im,F(1,2))
        def times(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
        x=(re,im)
        for _ in range(3):x=times(x,(re,im))
        self.assertEqual(x,(F(-1,4),F(0)))
        for _ in range(4):x=times(x,(re,im))
        self.assertEqual(x,(F(1,16),F(0)))

    def test_direct_four_poles_and_mellin_e2_shell(self):
        for n in range(1,101):
            self.assertEqual(S.original_r(n),S.miller_beta_r(n))
        self.assertEqual(S.original_r(1),F(47,15))

    def test_chiral_first_order_vanishes_for_actual_combined_source(self):
        inv=S.first_shell_invariants()
        self.assertEqual(inv['total_mass'],0)
        self.assertEqual(-inv['first_moment']/64,F(15,64))
        self.assertEqual(inv['even_mass']/8,F(15,32))
        self.assertEqual(inv['odd_mass']/8,F(-15,32))

    def test_actual_source_field_positive_and_quadratic(self):
        for k in range(11):
            q=F(1,2**k)
            r=S.source_field(q)
            self.assertGreater(r,0)
            self.assertLessEqual(r,F(15,2)*q*q)
            self.assertEqual(r,S.source_field(q,'even')+S.source_field(q,'odd'))
        for q in (F(0),F(1),F(1,2),F(13,17)):
            self.assertEqual(S.source_field(q,'full'),sum(
              (c*q/(8+(j-7)*q) for j,c in enumerate(S.TAPS)),F(0)))

    def test_two_chiral_tails_first_order_oppose(self):
        for k in (10,12,14):
            q=F(1,2**k)
            self.assertLess(abs(S.source_field(q,'even')/q-F(15,32)),F(1,1000))
            self.assertLess(abs(S.source_field(q,'odd')/q+F(15,32)),F(1,1000))
            self.assertLess(abs(S.source_field(q)/q**2-F(15,64)),F(1,1000))

    def test_first_shell_moment_resolvent_polynomial(self):
        # P(t)*[(1-t+t²/2)(1-t²/2)] == 4(1-t)(1-t^8/16)
        def mul(a,b):
            c=[F(0)]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):c[i+j]+=x*y
            return c
        lhs=mul(list(S.TAPS),mul([1,-1,F(1,2)],[1,0,F(-1,2)]))
        rhs=mul([4,-4],[1,0,0,0,0,0,0,0,F(-1,16)])
        self.assertEqual(lhs[:len(rhs)],rhs)
        self.assertTrue(all(v==0 for v in lhs[len(rhs):]))

class StationaryEField(unittest.TestCase):
    def test_compact_q_clock_automatically_replaces_index(self):
        q=F(1)
        for n in range(256):
            self.assertEqual(q,F(1,n+1))
            self.assertEqual(S.source_field(q),S.original_r(n+1))
            self.assertEqual(S.clock_update(q),S.at_grade(q,1))
            q=S.clock_update(q)

    def test_e_accepts_independent_chiral_receipts_in_one_macro_update(self):
        o=S.EObserver()
        u=F(0)
        for n in range(48):
            self.assertEqual(o.q,F(1,n+1))
            self.assertEqual(o.p,F(1,16**n))
            self.assertEqual(o.original_U,u)
            a,b=S.emit(o.q,'even'),S.emit(o.q,'odd')
            self.assertEqual(a.value+b.value,S.original_r(n+1))
            o=o.receive(a,b)
            u=16*u+S.original_r(n+1)
        self.assertEqual(o.original_U,u)

    def test_reject_ghost_mutated_chirality_clock_and_source(self):
        o=S.EObserver()
        a=S.emit(o.q,'even');b=S.emit(o.q,'odd')
        tests=[(b,a),
               (a,S.SourceReceipt(S.SOURCE_TAG,'odd',o.q,b.value+1)),
               (a,S.SourceReceipt('forged source','odd',o.q,b.value)),
               (a,S.SourceReceipt(S.SOURCE_TAG,'odd',F(1,2),b.value)),
               (a,a)]
        for pair in tests:
            with self.assertRaises(ValueError):o.receive(*pair)

    def test_all_exact_prefixes_observer_match_two_independent_formulas(self):
        for n in range(0,31):
            o=S.observer_at(n)
            self.assertEqual(o.alpha,S.source_alpha_B(n))
            self.assertEqual(o.alpha,S.e2_complete(n))
            self.assertEqual(o.a_even,S.e2_channel_complete(n,'even'))
            self.assertEqual(o.a_odd,S.e2_channel_complete(n,'odd'))

    def test_original_zero_seeds_and_coherent_wrong_seed_separate(self):
        o=S.EObserver()
        self.assertEqual(o.original_U,0)
        self.assertEqual(o.alpha,0)
        self.assertEqual(S.static_source_step(F(1,5),0),(F(1,5),F(0)))
        self.assertEqual(S.static_source_step(F(0),0),(F(0),F(0)))
        self.assertNotEqual(F(1,5),0)

    def test_static_koopman_update_equals_actual_rational_phase(self):
        x,q=F(0),F(1)
        o=S.EObserver()
        for _ in range(70):
            self.assertEqual(x,o.circle_phase)
            self.assertEqual(q,o.q)
            x,q=S.static_source_step(x,q)
            o=o.update()

    def test_compact_carrier_does_not_imply_fixed_bit_precision(self):
        a=S.observer_at(8)
        b=S.observer_at(32)
        self.assertGreater(b.q.denominator,a.q.denominator)
        self.assertGreater(b.p.denominator,a.p.denominator)
        self.assertNotEqual(a.alpha,b.alpha)

class GammaBoundaryField(unittest.TestCase):
    def test_exact_finite_gamma_seam(self):
        for q in (F(0),F(1),F(1,2),F(5,17)):
            for B in range(1,15):
                self.assertEqual(S.finite_intertwiner_residual(q,B),
                                 S.finite_intertwiner_expected(q,B))

    def test_genuine_gamma_field_finite_tail_enclosure(self):
        for q in (F(0),F(1),F(1,3),F(5,16)):
            for B in (1,2,4,8,12):
                low=S.tau_partial(q,B)
                high=S.tau_partial(q,B+16)
                self.assertGreaterEqual(high-low,0)
                self.assertLessEqual(high-low,S.tau_remaining_bound(q,B))

    def test_original_all_window_finite_seam_one_static_alpha(self):
        for B in (1,2,8,13,32):
            alpha=S.e2_complete(B)
            for n in range(B+1):
                o=S.observer_at(n)
                self.assertEqual(o.original_U+S.full_finite_seam(n,B),
                                 16**n*alpha)

    def test_static_completed_field_equals_e_receiver_accumulator(self):
        for B in (0,1,2,4,8,16,32):
            self.assertEqual(S.tau_partial(F(1),B),S.observer_at(B).alpha)

    def test_exact_finite_stationary_koopman_character_defect(self):
        for x in (F(0),F(1,5),F(8,13)):
            for q in (F(1),F(1,2),F(2,7)):
                for B in (1,3,9):
                    for h in (1,2,16):
                        lhs=h*(16*x+S.source_field(q)+S.tau_partial(S.clock_update(q),B))
                        rhs=h*16*(x+S.tau_partial(q,B))
                        self.assertEqual(lhs-rhs,h*S.finite_intertwiner_expected(q,B))
                        self.assertEqual((lhs-rhs)%1,(h*S.finite_intertwiner_expected(q,B))%1)

    def test_tau_0_and_original_gamma_tail_budget(self):
        self.assertEqual(S.tau_partial(0,100),0)
        for n in (1,4,8,16):
            q=F(1,n+1)
            self.assertLessEqual(S.tau_partial(q,15),F(1,(8*n+1)*(8*n+2)))
            self.assertGreater(S.tau_partial(q,15),0)

    def test_boundary_source_vanishes_but_harmless_periodic_states_remain(self):
        self.assertEqual(S.source_field(0),0)
        for q in (F(1),F(1,2),F(1,7)):
            self.assertGreater(q-S.clock_update(q),0)
            self.assertEqual(q-S.clock_update(q),q*q/(1+q))
        y=F(1,7)
        for _ in range(3):
            y,_=S.static_source_step(y,0)
        self.assertEqual(y,F(1,7))

    def test_source_specific_mutation_breaks_quadratic_readout(self):
        # Drop ODD lane: 1/n leading term survives, and E refuses the receipt.
        q=F(1,128)
        re=S.source_field(q,'even')
        self.assertGreater(re/q,F(2,5))
        with self.assertRaises(ValueError):
            S.EObserver().receive(S.emit(1,'even'),S.SourceReceipt(S.SOURCE_TAG,'odd',F(1),F(0)))

if __name__=='__main__':unittest.main()

import unittest
import math
from fractions import Fraction as F
from observer_model import (native_birth,controlled_birth,source,tilted,selection,
                            history,selected_history_at_terminal,finite_history_rejection)


class SourceVsObserver(unittest.TestCase):
    def test_uniform_poya_marginal_from_histories(self):
        for j in range(0,9):
            out=[F(0)]*(j+1)
            for w,prob in history(j).items():
                out[sum(w)]+=prob
            self.assertEqual(out,source(j))

    def test_snapshot_postselection_recovers_each_tilt_exactly(self):
        for a in [F(1,9),F(1,4),F(2,3),F(9,10)]:
            for j in range(0,40):
                q,p_accept=selection(a,j)
                self.assertEqual(q,tilted(a,j))
                self.assertEqual(p_accept,sum((a**k for k in range(j+1)),F(0))/F(j+1))

    def test_acceptance_cost_and_linear_rate(self):
        a=F(1,4)
        for j in [10,30,100,300]:
            _,prob=selection(a,j)
            trials=1/prob
            asymptotic=F(1,1)-a
            self.assertGreater(trials,0)
            self.assertLess(abs(trials/F(j+1)-asymptotic),F(1,5000))

    def test_fixed_time_and_persistent_history_share_terminal_marginals(self):
        for a in [F(1,4),F(1,2),F(3,4)]:
            for j in range(0,8):
                q=history(j,a)
                selected,_=selected_history_at_terminal(a,j)
                terminal_q=[F(0)]*(j+1)
                terminal_sel=[F(0)]*(j+1)
                for w in q:
                    terminal_q[sum(w)]+=q[w]
                    terminal_sel[sum(w)]+=selected[w]
                self.assertEqual(terminal_q,tilted(a,j))
                self.assertEqual(terminal_sel,tilted(a,j))

    def test_two_time_posterior_differs_from_persistent_dynamics(self):
        for a in [F(1,9),F(1,4),F(1,2),F(3,4)]:
            selected,_=selected_history_at_terminal(a,2)
            one_time_selected=sum(prob for word,prob in selected.items() if word[0]==1)
            one_time_controlled=tilted(a,1)[1]
            self.assertEqual(one_time_selected, (a+2*a*a)/(2*(1+a+a*a)))
            self.assertEqual(one_time_controlled-one_time_selected,
                a*(1-a)/(2*(1+a)*(1+a+a*a)))
            self.assertGreater(one_time_controlled,one_time_selected)

    def test_unrestricted_finite_history_postselection_can_mimic_control(self):
        a=F(1,4)
        last=F(1)
        for j in range(1,9):
            prob,accept=finite_history_rejection(a,j)
            self.assertTrue(all(0<t<=1 for t in accept.values()))
            self.assertLessEqual(prob,last)
            last=prob

    def test_relabeling_is_invariant_if_both_laws_are_pushed_forward(self):
        a=F(1,4)
        for j in [1,2,4,10]:
            p=source(j)
            q=tilted(a,j)
            revp=p[::-1];revq=q[::-1]
            self.assertTrue(math.isclose(
                sum(float(v)*math.log(float(v/u)) for u,v in zip(p,q)),
                sum(float(v)*math.log(float(v/u)) for u,v in zip(revp,revq)),
                rel_tol=1e-13, abs_tol=1e-13))
            self.assertEqual([q[j-k] for k in range(j+1)],revq)

    def test_noninvertible_observer_coarsening_decreases_kl(self):
        a=F(1,4)
        for j in range(2,15):
            p=source(j);q=tilted(a,j)
            full=sum(float(v)*math.log(float(v/u)) for u,v in zip(p,q))
            p2=[sum(p[::2]),sum(p[1::2])]
            q2=[sum(q[::2]),sum(q[1::2])]
            coarse=sum(float(v)*math.log(float(v/u)) for u,v in zip(p2,q2))
            self.assertLessEqual(coarse,full+1e-13)

    def test_natural_numbers_label_swap_is_not_semiring_automorphism(self):
        flip=lambda n:4 if n==2 else 2 if n==4 else n
        self.assertNotEqual(flip(2*2),flip(2)*flip(2))
        transported_product=lambda x,y:flip(flip(x)*flip(y))
        self.assertEqual(transported_product(4,4),2)

    def test_cost_bias_c_k_equal_k_is_just_a_declared_observer(self):
        a=F(1,4)
        for j in [2,5,8]:
            # A grade-dependent description cost C_o(k)=k, exp(-lambda C)=a**k.
            conditional,rate=selection(a,j)
            self.assertEqual(conditional,tilted(a,j))
            self.assertGreater(rate,0)

    def test_native_law_and_tilted_snapshots_both_normalized(self):
        for j in range(100):
            self.assertEqual(sum(source(j)),F(1))
            self.assertEqual(sum(tilted(F(1,4),j)),F(1))


if __name__=='__main__':
    unittest.main(verbosity=2)

from fractions import Fraction as Q
from itertools import product
import unittest
from observer import (ArithmeticState,source,frac,floor,rational_orbit,word_counts,
 branch_cost,transport_bound,w1_uniform,minimal_states,completed_bbp_word,
 debruijn,periodic_value)


class ObserverTests(unittest.TestCase):
    def test_source_and_history_types_are_enforced(self):
        with self.assertRaises(ValueError):ArithmeticState(source_id='mutant')
        with self.assertRaises(ValueError):ArithmeticState(clock=-1)
        with self.assertRaises(ValueError):ArithmeticState(clock=1)

    def test_actual_lift_and_carry(self):
        s=ArithmeticState();u=Q(0)
        for n in range(1,81):
            s=s.step();u=sum((16**(n-j)*source(j) for j in range(1,n+1)),Q(0))
            self.assertEqual(s.lift,u)
            self.assertEqual(floor(s.lift),sum(16**(n-1-i)*c for i,c in enumerate(s.carries)))
        self.assertEqual(s.carries[0],3)
    def test_future_refinement_exhaustive(self):
        for b,m,L in ((2,1,4),(3,2,3),(16,1,2)):
            seen=set()
            for j in range(b**(m+L-1)):
                x=Q(j,b**(m+L-1))
                seen.add(tuple(floor(b**m*y) for y in rational_orbit(x,L,b)))
            self.assertEqual(len(seen),b**(m+L-1))
    def test_finite_transport_exact(self):
        for b in (2,3,16):
            for den in (7,17,257,263,509,521):
                for N in (1,3,11,41):
                    pts=rational_orbit(Q(1,den),N+5,b)
                    word=tuple(floor(b*x) for x in pts)
                    for k in (0,1,2,4):
                        counts=word_counts(word,N,k,b)
                        self.assertLessEqual(w1_uniform(pts[:N]),transport_bound(counts,k,b))
    def test_constant_control_is_sharp_in_limit(self):
        counts={(0,0):100}
        r=branch_cost(counts)
        self.assertEqual(r['rho'],Q(15,32))
        self.assertEqual(w1_uniform([Q(0)]*100),Q(1,2))
        self.assertAlmostEqual(r['deficiency'],__import__('math').log(16))
    def test_debruijn_false_success_control(self):
        w=debruijn(2,5);N=len(w);word=(w*2)[:N+5]
        self.assertEqual(branch_cost(word_counts(word,N,4,2),2)['rho'],0)
        self.assertGreater(branch_cost(word_counts(word,N,5,2),2)['rho'],0)
        x=periodic_value(w,2)
        self.assertLessEqual(w1_uniform(rational_orbit(x,N,2)),transport_bound(word_counts(word,N,4,2),4,2))
    def test_sampling_floor(self):
        for k in range(6):
            w=debruijn(2,5);counts=word_counts((w*2),32,k,2);r=branch_cost(counts,2)
            self.assertGreaterEqual(r['deficiency']+1e-14,r['sampling_floor'])
        r=branch_cost({(j%16,j):1 for j in range(40)},16)
        self.assertAlmostEqual(r['deficiency'],r['sampling_floor'])
    def test_minimal_states_against_lasso_enumeration(self):
        for N in range(1,8):
            for w in product(range(2),repeat=N):
                choices=[]
                for a in range(N):
                    for p in range(1,N-a+1):
                        if all(w[i]==w[a+(i-a)%p] for i in range(a,N)):
                            choices.append(a+p)
                self.assertEqual(minimal_states(w)[0],min(choices))
    def test_rational_aliases_are_not_normality_falsifiers(self):
        for x in (Q(1,17),Q(1,257)):
            self.assertEqual(rational_orbit(x,30),rational_orbit(x+7,30))
            y=x+Q(5,16**3)
            self.assertEqual(rational_orbit(x,30)[3:],rational_orbit(y,30)[3:])
    def test_original_completed_prefix(self):
        w=completed_bbp_word(32)
        self.assertEqual(''.join(format(x,'X') for x in w[:8]),'243F6A88')


if __name__=='__main__':unittest.main()

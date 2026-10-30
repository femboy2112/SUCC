import unittest
from collections import Counter
from fractions import Fraction
from cylinder_probe import (r,bbp_states,certified_word,word_digits,
                            collision_energy,fkm_debruijn,cyclic_words,bbp_word_census)


def refinement_defect(words,m,N):
    counts=Counter(words)
    q=16**m
    if m==0:
        return Fraction(1)
    parent=Counter(w//16 for w in words)
    delta=Fraction(0)
    for v,p in parent.items():
        for a in range(16):
            pa=counts.get(v*16+a,0)
            delta+=(Fraction(pa,N)-Fraction(p,16*N))**2
    return 16**m*delta


def tent(u,q):
    u = u - (u.numerator//u.denominator)
    d=min(u,1-u)
    return q*(1-q*d) if d < Fraction(1,q) else Fraction(0)


def soft_pair_energy(states,q):
    N=len(states)
    return sum((tent(a-b,q) for a in states for b in states),Fraction(0))/N**2

class CylinderTests(unittest.TestCase):
    def test_source_identity(self):
        for n in [1,2,3,7,17,31]:
            for R in [2,4,6]:
                Tn=sum((r(n+j)/16**j for j in range(1,R+1)),Fraction(0))
                Tnext=sum((r(n+1+j)/16**j for j in range(1,R)),Fraction(0))
                self.assertEqual(16*Tn-r(n+1),Tnext)

    def test_source_positive_and_monotone(self):
        for n in range(1,80):
            self.assertGreater(r(n),0)
            self.assertGreater(r(n),r(n+1))

    def test_exact_certification_of_hex_word(self):
        u=next(bbp_states(1))
        word,R=certified_word(u,1,8)
        self.assertEqual(word,0x243F6A88)
        self.assertGreaterEqual(R,8)

    def test_shift_overlap(self):
        v=list(bbp_states(80))
        for m in [2,3,5]:
            for n in range(1,80):
                word,_=certified_word(v[n-1],n,m)
                word_next,_=certified_word(v[n],n+1,m-1)
                self.assertEqual(word%16**(m-1),word_next)

    def test_known_debruijn_double_control(self):
        cyc=fkm_debruijn(16,2)
        self.assertEqual(len(cyc),256)
        self.assertEqual([collision_energy(cyclic_words(cyc,m),m) for m in range(1,5)],
                         [1,1,16,256])
        self.assertEqual(len(set(cyclic_words(cyc,2))),256)

    def test_all_zero_adversary(self):
        for m in [1,2,3,4]:
            self.assertEqual(collision_energy([0]*128,m),16**m)

    def test_collision_is_pair_count(self):
        w=[0,1,0,2,3,3,3]
        c=Counter(w)
        self.assertEqual(sum(v*v for v in c.values()),sum(a==b for a in w for b in w))

    def test_exact_refinement_energy(self):
        cyc=fkm_debruijn(16,2)
        for m in [1,2,3,4]:
            words=cyclic_words(cyc,m)
            parents=[w//16 for w in words]
            q_m=collision_energy(words,m)
            q_prev=collision_energy(parents,m-1)
            self.assertEqual(q_m-q_prev,refinement_defect(words,m,len(words)))
            self.assertGreaterEqual(q_m,q_prev)

    def test_bbp_census_has_sampling_floor(self):
        res=bbp_word_census(256,3)
        self.assertEqual(res[1]['Q'],'2117/2048')
        self.assertEqual(res[2]['Q'],'31/16')
        self.assertEqual(res[3]['Q'],'17')
        for m in [1,2,3]:
            self.assertGreaterEqual(Fraction(res[m]['Q']),Fraction(16**m,256))

    def test_biased_product_entropy(self):
        p=[Fraction(1,2)]+[Fraction(1,30)]*15
        self.assertEqual(sum(p),1)
        factor=16*sum(x*x for x in p)
        self.assertEqual(factor,Fraction(64,15))
        for m in [1,2,3]:
            self.assertGreater(factor**m,1)

    def test_soft_source_transfer(self):
        N=28
        u=list(bbp_states(N))
        t=[sum((r(n+j)/16**j for j in range(1,9)),Fraction(0)) for n in range(1,N+1)]
        upper=[t_i+r(n+9)/Fraction(15*16**8) for n,t_i in enumerate(t,1)]
        for q in [16,256]:
            e_source=soft_pair_energy(u,q)
            e_approx=soft_pair_energy([a+b for a,b in zip(u,t)],q)
            bound=Fraction(2*q*q,N)*sum(upper)
            self.assertLessEqual(abs(e_source-e_approx),bound)

    def test_tent_kernel_is_lipschitz(self):
        for q in [16,256]:
            for i in range(6):
                x=Fraction(i,100*q)
                for j in range(6):
                    y=Fraction(j,100*q)
                    self.assertLessEqual(abs(tent(x,q)-tent(y,q)),q*q*abs(x-y))


class WalshExtraTests(unittest.TestCase):
    def test_walsh_is_refinement_defect_debruijn(self):
        from cylinder_probe import walsh_defect
        cycle=fkm_debruijn(16,2)
        for m in range(0,4):
            children=cyclic_words(cycle,m+1)
            parents=[w//16 for w in children]
            self.assertEqual(
                walsh_defect(children,m),
                collision_energy(children,m+1)-collision_energy(parents,m)
            )

    def test_walsh_source_selected_bbp(self):
        from cylinder_probe import walsh_defect
        us=list(bbp_states(128))
        for m in range(0,3):
            children=[certified_word(u,n,m+1)[0] for n,u in enumerate(us,1)]
            parents=[w//16 for w in children]
            self.assertEqual(walsh_defect(children,m),
                             collision_energy(children,m+1)-collision_energy(parents,m))

class HaarOverlapCalibration(unittest.TestCase):
    def test_overlapping_word_equality_probability(self):
        from itertools import product
        for base in (2,3):
            for m in range(1,5):
                for shift in range(1,m+2):
                    favorable=0
                    total=0
                    for digits in product(range(base), repeat=m+shift):
                        total+=1
                        favorable+=digits[:m]==digits[shift:shift+m]
                    self.assertEqual(Fraction(favorable,total),Fraction(1,base**m))

    def test_haar_expectation_formula(self):
        N=256
        self.assertEqual(Fraction(1)+(Fraction(16**3-1,N)),Fraction(4351,256))


class HardSoftBridgeTests(unittest.TestCase):
    def test_termwise_coarse_tent_domination(self):
        from fractions import Fraction
        from cylinder_probe import certified_word, bbp_states
        for m in (2,3):
            q=16**m
            coarser=16**(m-1)
            a=[Fraction(k,4000) for k in range(4001)]
            # A deterministic collection across thousands of endpoints, including exact edges.
            for i in range(0,4000,107):
                for j in range(0,4000,113):
                    if (q*a[i]).numerator//(q*a[i]).denominator == (q*a[j]).numerator//(q*a[j]).denominator:
                        self.assertLessEqual(q,Fraction(256,15)*tent(a[i]-a[j],coarser))

    def test_actual_source_hard_to_soft(self):
        from cylinder_probe import bbp_states
        N=32
        states=list(bbp_states(N))
        y_approx=[]
        for n,u in enumerate(states,1):
            y_approx.append(u+sum((r(n+j)/16**j for j in range(1,13)),Fraction(0)))
        for m in (2,3):
            words=[certified_word(states[n-1],n,m)[0] for n in range(1,N+1)]
            hard=collision_energy(words,m)
            soft=soft_pair_energy(y_approx,16**(m-1))
            self.assertLessEqual(hard,Fraction(256,15)*soft)

if __name__=='__main__':
    unittest.main(verbosity=2)

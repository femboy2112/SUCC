import unittest
from fractions import Fraction as F
import arrow_probe as p

class ArrowTests(unittest.TestCase):
    def test_source_authentic(self):
        self.assertEqual(p.source(1),F(47,15))
        self.assertEqual(sum(p.endpoint(17,5)),1)
    def test_conditional_prefix_probabilities(self):
        for x in [F(0),F(1,11),F(3,7),F(10,11),F(1)]:
            for m in [3,4,6]:
                rows=[p.conditional_word(x,w,True) for w in p.all_words(m)]
                self.assertEqual(sum(rows),1)
                self.assertTrue(all(v>=0 for v in rows))
                for k in range(m+1):
                    self.assertEqual(sum(p.conditional_word(x,w,True) for w in p.all_words(m) if w.count('1')==k),
                                     sum(p.conditional_word(x,w,False) for w in p.all_words(m) if w.count('1')==k))
    def test_all_prefix_joint_snapshots(self):
        for a in [17,41]:
            for m in [3,5,7]:
                for k in range(m+1):
                    self.assertEqual(sum(p.word_probability(a,w,True) for w in p.all_words(m) if w.count('1')==k),p.endpoint(a,m)[k])
    def test_hidden_history_split(self):
        for x in [F(1,7),F(2,5),F(8,9)]:
            q01=p.conditional_word(x,'011',True)/(x*(1-x))
            q10=p.conditional_word(x,'101',True)/(x*(1-x))
            self.assertEqual(q10-q01,x*(1-x))
    def test_native_joint_margins(self):
        for a,m,d in [(17,2,2),(41,3,4),(97,5,3)]:
            self.assertEqual(p.margins(p.native_joint(a,m,d)),(p.endpoint(a,m),p.endpoint(a,m+d)))
    def test_tree_reconstruction(self):
        for a in [17,41,97]:
            for m in [1,3,6]:
                self.assertEqual(p.reconstruct_one_step(p.endpoint(a,m),p.endpoint(a,m+1)),p.native_joint(a,m,1))
    def test_cycle_rank(self):
        for m in range(1,7):
            for d in range(1,5):
                support=p.edge_support(m,d)
                kernel=len(support)-p.rank(p.incidence(m,d))
                basis=[[z[i][k] for i,k in support] for z in p.cycle_basis(m,d)]
                self.assertEqual(kernel,m*(d-1))
                self.assertEqual(p.rank(basis),kernel)
    def test_positive_cycle_preserves_margins(self):
        j=p.native_joint(41,3,4);z=p.cycle(3,4,1,3)
        epsilon=min(v for row in j for v in row if v)/2
        changed=p.perturb(j,z,epsilon)
        self.assertTrue(all(v>=0 for row in changed for v in row))
        self.assertNotEqual(j,changed)
        self.assertEqual(p.margins(j),p.margins(changed))
    def test_euler_offset_cancels(self):
        z=p.cycle(3,4,1,3)
        for c in [F(0),F(1,2),F(137,211)]:
            f=[p.harmonic(i)-c for i in range(4)]
            g=[p.harmonic(i)-c for i in range(8)]
            self.assertEqual(p.mixed(z,f,g),F(1,8))
    def test_single_harmonic_probe_blind_direction(self):
        a,b=p.cycle(3,3,0,1),p.cycle(3,3,1,2)
        f=[p.harmonic(i) for i in range(4)]
        g=[p.harmonic(i) for i in range(7)]
        ca,cb=p.mixed(a,f,g),p.mixed(b,f,g)
        z=[[cb*v-ca*w for v,w in zip(ar,br)] for ar,br in zip(a,b)]
        self.assertEqual(p.mixed(z,f,g),0)
        self.assertTrue(any(v for row in z for v in row))
        self.assertEqual(p.margins(z),([0]*4,[0]*7))
    def test_cauchy_reconstruction(self):
        for a,m,d in [(17,2,2),(41,3,2),(97,4,3)]:
            j=p.native_joint(a,m,d)
            measured,restored,gain=p.tomography(j,list(range(1,m+2)),list(range(2,m+d+3)))
            self.assertEqual(restored,j)
            self.assertGreater(gain,1)
    def test_duplicate_probe_rejected(self):
        with self.assertRaises(ValueError):p.inverse(p.cauchy([1,1],[0,1]))


class StrongTriangleControls(unittest.TestCase):
    def test_all_mixed_harmonic_golden_controls(self):
        z,rank=p.matched_arrow_direction(4,4)
        self.assertLess(rank,12)
        self.assertEqual(p.harmonic_golden_moments(z),[0]*7)
        self.assertEqual(p.margins(z),([0]*5,[0]*9))
        for a in [17,97,233]:
            j=p.native_joint(a,4,4)
            epsilon=p.power_moment(a,8,8)/2
            altered=p.perturb(j,z,epsilon)
            self.assertTrue(all(v>=0 for row in altered for v in row))
            self.assertEqual(p.harmonic_golden_moments(j),p.harmonic_golden_moments(altered))
            self.assertNotEqual(j,altered)
    def test_harmonic_resolvent_discriminates_triangle_matched_arrow(self):
        z,_=p.matched_arrow_direction(4,4)
        c=p.cauchy(range(1,6),range(5));d=p.cauchy(range(2,11),range(9))
        observed=p.matmul(p.matmul(c,z),p.transpose(d))
        self.assertTrue(any(v for row in observed for v in row))

if __name__=='__main__':unittest.main()

import json
from pathlib import Path
from fractions import Fraction as F
import unittest
import quadrature as q

HERE=Path(__file__).parent
ROWS=sum((json.loads((HERE/'receipts'/name).read_text())['rows'] for name in ('quadrature-witnesses.json','fresh-quadrature-witnesses.json')),[])

class QuadratureTests(unittest.TestCase):
    def test_original(self):
        self.assertEqual(q.source(1),F(47,15)); self.assertEqual(q.source(2),F(106,819))
    def test_geometric_moments(self):
        self.assertEqual(q.geometric_moment(0),F(1,15))
        self.assertEqual(q.geometric_moment(1),F(16,225))
        self.assertEqual(q.geometric_moment(2),F(272,3375))
    def test_total_mass(self): self.assertEqual(q.green_moment(0),F(1,64))
    def test_positive_exact_witnesses(self):
        for r in ROWS:
            self.assertTrue(q.certify(r['M'],r['J'],list(map(F,r['nodes'])),list(map(F,r['weights']))))
    def test_prefix_all_arithmetic(self):
        for r in ROWS:
            bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights'])); u=F(); v=q.prefix(r['M'])
            self.assertEqual(u,v[0])
            for n in range(1,r['M']+1):
                u=16*u+q.mutant_source(n,bs,ws)
                self.assertEqual(u,v[n])
                self.assertEqual(u,16**n*q.mutant_g(0,bs,ws)-q.mutant_g(n,bs,ws))
                for p in (2,3,5,13,19,73): self.assertEqual(q.primary(u,p),q.primary(v[n],p))
    def test_source_differs_after_matching(self):
        for r in ROWS:
            bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights']))
            self.assertNotEqual(q.mutant_source(r['M']+1,bs,ws),q.source(r['M']+1))
    def test_positive_decay(self):
        for r in ROWS:
            bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights']))
            for n in (1,2,5,19,73,1000):
                self.assertGreater(q.mutant_source(n,bs,ws),0)
                self.assertGreater(q.mutant_source(n,bs,ws),q.mutant_source(n+1,bs,ws))
    def test_green_telescopes(self):
        for r in ROWS:
            bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights']))
            for n,K in ((0,5),(5,3),(23,7)):
                lhs=sum((q.mutant_source(n+j,bs,ws)/16**j for j in range(1,K+1)),F())
                self.assertEqual(lhs,q.mutant_g(n,bs,ws)-q.mutant_g(n+K,bs,ws)/16**K)
    def test_completed_boundary_rational(self):
        for r in ROWS:
            bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights']))
            self.assertEqual(F(r['completed_constant']),16*q.mutant_g(0,bs,ws))
    def test_cancellations(self):
        us=q.prefix(274)
        self.assertTrue(all(q.primary(us[n],19)==0 for n in range(10,17)))
        self.assertNotEqual(q.primary(us[17],19),0)
        self.assertEqual(q.primary(us[274],73),0)
        self.assertEqual(us[4].numerator%73,0)
    def test_mutant_bad_input_rejected(self):
        r=ROWS[0]; bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights'])); ws[0]+=F(1,1000)
        with self.assertRaises(AssertionError): q.certify(r['M'],r['J'],bs,ws)
    def test_g_bound(self):
        for r in ROWS:
            bs=list(map(F,r['nodes'])); ws=list(map(F,r['weights']))
            for n in (0,1,17,127):
                self.assertLessEqual(q.mutant_g(n,bs,ws),F(1,(8*n+1)**2))
                self.assertLessEqual(q.mutant_g(n,bs,ws)-q.mutant_g(n+1,bs,ws),F(16,(8*n+1)**3))
            self.assertLess(sum((q.mutant_g(n,bs,ws) for n in range(1,41)),F()),F(17,648))

if __name__=='__main__': unittest.main(verbosity=2)

from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
import family_audit as fa


def box(a,b=0):
    a,b=Q(a),Q(b)
    return fa.Box(fa.Interval.ratio(a.numerator,a.denominator),fa.Interval.ratio(b.numerator,b.denominator))


class FamilyAuditTests(unittest.TestCase):
    def test_radial_is_exact_dyadic_in_disk(self):
        for a,b in product(range(-8,9),repeat=2):
            v=fa.radial_witness(box(Q(a,11),Q(b,13)))
            self.assertEqual(v.re.lo,v.re.hi)
            self.assertEqual(v.im.lo,v.im.hi)
            self.assertLessEqual(v.re.lo*v.re.lo+v.im.lo*v.im.lo,fa.SCALE*fa.SCALE)

    def test_exact_dual_bound_all_tables(self):
        targets=[box(1),box(0,1),box(-1),box(0,-1),box(Q(3,5),Q(4,5))]
        categories=[['0','0'],['0','1'],['1','1'],['0','1'],['1','0']]
        witnesses=[targets,[fa.radial_witness(v) for v in targets]]
        values=[box(0),box(1),box(-1),box(0,1),box(0,-1),box(Q(3,5),Q(4,5))]
        for witness in witnesses:
            result=fa.dual_certificate(targets,categories,witness)
            r=result['lower_bound'];lower=Q(r['numerator'],r['denominator'])
            self.assertGreater(lower,0)
            for g0,g1 in product(values,repeat=2):
                g={'0':g0,'1':g1}
                actual=Q(0)
                for f,c in zip(targets,categories):
                    pred=(g[c[0]]+g[c[1]]).divide(2)
                    actual+=fa.magnitude_bounds(f-pred)[0]
                self.assertLessEqual(lower,actual/len(targets))

    def test_coherent_constant_family_has_no_positive_floor(self):
        target=[box(1) for _ in range(8)]
        cats=[[str(j%3),str((j+1)%3)] for j in range(8)]
        result=fa.dual_certificate(target,cats,target)
        self.assertEqual(result['lower_bound']['numerator'],0)


if __name__=='__main__':unittest.main()

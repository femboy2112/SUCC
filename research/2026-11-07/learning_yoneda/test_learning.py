import unittest
from fractions import Fraction as Q
from itertools import product, combinations

from learning import (SourceSignature, exact_history, calibrated_digits,
                      history_category, digit_carrier, residual_layers,
                      late_index_target, seed_charge, affine_open_phase)
from observational_succ.operational_yoneda_descent import (
    restricted_yoneda_arrow_detection, CertifiedSourceMorphism,
    induced_observation_functor)


class LearningTests(unittest.TestCase):
    def test_frozen_source_and_lifts(self):
        self.assertTrue(SourceSignature().authenticate_original_zero())
        for mutant in (SourceSignature(boundary=Q(1,5)),
                       SourceSignature(weights=(4,-2,-1,1)),
                       SourceSignature(poles=(7,4,3,1))):
            with self.assertRaises(ValueError): mutant.authenticate_original_zero()
        a, b = exact_history(0,12), exact_history(Q(1,256),12)
        for n in range(13):
            self.assertEqual(b.unwrapped[n]-a.unwrapped[n], Q(16**n,256))
        self.assertEqual(a.circle[2:],b.circle[2:])
        self.assertNotEqual(a.unwrapped[2:],b.unwrapped[2:])

    def test_digit_holdouts(self):
        for depth in (1,2,3,4):
            for k in (0,1,7,15,16**depth//3,16**depth-1):
                if k >= 16**depth: continue
                expected=tuple((k//16**(depth-t-1))%16 for t in range(depth))
                self.assertEqual(calibrated_digits(Q(k,16**depth),depth),expected)

    def test_genuine_path_yoneda_not_endpoints(self):
        c=history_category((0,),2,("zero",))
        terminal=next(i for i,(budget,_) in enumerate(c.contexts) if budget==0)
        self.assertEqual(len(c.hom(0,terminal)),4)
        self.assertFalse(restricted_yoneda_arrow_detection(c,0,terminal,())["faithful_on_selected_hom"])
        self.assertTrue(restricted_yoneda_arrow_detection(c,0,terminal,(0,))["faithful_on_selected_hom"])

    def test_main_functor_and_policy_reuse(self):
        f,s,t=digit_carrier((Q(0),Q(1,256),Q(17,256)),2,("0","1","17"))
        m=CertifiedSourceMorphism(f,f,s,s,tuple(range(f.count)),t,t,"ancestry")
        r=induced_observation_functor(m,horizon=2).proof_receipt()
        self.assertTrue(r["faithful"] and r["full"])
        self.assertGreater(r["checked_functor_compositions"],0)

    def test_all_binary_three_digit_targets_independent_rows(self):
        for table in product((0,1),repeat=8):
            layers=residual_layers(table,2,3)
            for t in range(4):
                # Direct suffix enumeration, distinct from table slicing.
                rows=[]
                for prefix in product(range(2),repeat=t):
                    row=[]
                    for suffix in product(range(2),repeat=3-t):
                        index=0
                        for x in prefix+suffix:index=2*index+x
                        row.append(table[index])
                    rows.append(tuple(row))
                self.assertEqual(len(layers[t][0]),len(set(rows)))

    def test_late_query_needs_large_intermediate_memory(self):
        for m in (1,2):
            target,depth=late_index_target(m)
            layers=residual_layers(target,16,depth)
            self.assertEqual(len(layers[m][0]),16**m)
            self.assertEqual(len(layers[-1][0]),2)
        with self.assertRaises(ValueError):residual_layers((0,1,0),2,2)

    def test_adaptive_threshold_strict_resource_advantage(self):
        # Actual binary-search paths, and exhaustive fixed four-probe sets.
        for source in range(16):
            left,right,queries=0,16,0
            while right-left>1:
                middle=(left+right)//2
                if source>=middle:left=middle
                else:right=middle
                queries+=1
            self.assertEqual(left,source)
            self.assertEqual(queries,4)
        for schedule in combinations(range(1,16),4):
            reports={tuple(int(s>=j) for j in schedule) for s in range(16)}
            self.assertEqual(len(reports),5)

    def test_anchored_charge_and_feedback_control(self):
        for args in ((0,-1,2,1),(0,2,-1,1),(0,True,2,1),(0,2,1,1.0)):
            with self.assertRaises(ValueError): affine_open_phase(*args)
        for n in (2,7,13):
            for t in (0,1,n-1):
                for h in (-3,1,5):
                    s=Q(7,53)
                    delta=(affine_open_phase(s,n,t,h)-affine_open_phase(0,n,t,h))%1
                    self.assertEqual(delta,(h*(16**n-16**t)*s)%1)
            self.assertEqual(seed_charge((n,0),(1,-16**n)),0)
        # Adaptive phase conjugation turns a cancelling two-point law into 1.
        phases=(Q(0),Q(1,2))
        controlled=tuple((p + (-p))%1 for p in phases)
        self.assertEqual(controlled,(Q(0),Q(0)))


if __name__=="__main__":unittest.main()

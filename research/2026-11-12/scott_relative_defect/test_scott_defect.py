"""Exact local checks, independent arithmetic controls, mutation/hostile cases."""
import unittest
from math import isqrt
from scott_defect import (Trace, prime, split, trial_prime, refines, normalize,
                          trace_chain, bounds, defect_bounds, prime_transport,
                          true_omega, split_count, terminal, pair_bounds,
                          goldbach_interval, kleene_step, kleene_prefix)


def sieve(limit):
    a=[True]*(limit+1)
    a[:2]=[False,False]
    for i in range(2,isqrt(limit)+1):
        if a[i]:
            for j in range(i*i,limit+1,i):
                a[j]=False
    return a

class ScottDefectTests(unittest.TestCase):
    def test_alternative_paths_same_normal_form_degree(self):
        sv=sieve(600)
        for n in range(2,601):
            paths=[trace_chain(n,p) for p in ("minimum","balanced","reverse")]
            for hist in paths:
                self.assertEqual(bounds(hist[-1]),(true_omega(n),true_omega(n)))
                self.assertEqual(split_count(hist[-1]),true_omega(n)-1)
                self.assertTrue(terminal(hist[-1]))
                self.assertTrue(all(refines(a,b) for a,b in zip(hist,hist[1:])))
                self.assertEqual(sum(b.kind=="prime" for b in hist),int(sv[n]))

    def test_bounds_monotone_and_sound_during_reduction(self):
        for n in range(2,700):
            for policy in ("minimum","balanced"):
                h=trace_chain(n,policy)
                ranks=[bounds(x) for x in h]
                self.assertTrue(all(l<=true_omega(n)<=u for l,u in ranks))
                self.assertTrue(all(a[0]<=b[0] and a[1]>=b[1]
                                    for a,b in zip(ranks,ranks[1:])))
                self.assertEqual(ranks[-1],(true_omega(n),)*2)

    def test_source_faithful_scott_transport_commutator(self):
        for p in (2,3,5,7,11):
            for n in range(2,180):
                for t in trace_chain(n,"balanced"):
                    transported=prime_transport(p,t)
                    l,u=defect_bounds(t)
                    self.assertEqual(defect_bounds(transported),(l+1,u+1))
                    self.assertEqual(transported.n,p*n)

    def test_information_loss_vs_actual_defect(self):
        self.assertEqual(defect_bounds(Trace(9)),(0,2))
        self.assertEqual(defect_bounds(normalize(9)),(1,1))
        self.assertEqual(defect_bounds(Trace(60)),(0,4))
        self.assertEqual(defect_bounds(normalize(60)),(3,3))
        # An uninspected composite may have lower defect 0: not a prime witness.
        self.assertEqual(pair_bounds(Trace(9),Trace(11)),(0,4))
        self.assertEqual(pair_bounds(normalize(9),normalize(11)),(1,1))
        self.assertEqual(pair_bounds(normalize(7),normalize(13)),(0,0))

    def test_goldbach_count_interval_and_refinement(self):
        sv=sieve(400)
        evidence={}
        for n in range(2,201):
            lo,hi=goldbach_interval(n,evidence)
            actual=sum(sv[n-d] and sv[n+d] for d in range(n-1))
            self.assertLessEqual(lo,actual)
            self.assertGreaterEqual(hi,actual)
        for k in range(2,401):
            evidence[k]=normalize(k,"minimum")
        for n in range(2,201):
            actual=sum(sv[n-d] and sv[n+d] for d in range(n-1))
            self.assertEqual(goldbach_interval(n,evidence),(actual,actual))
        self.assertEqual(goldbach_interval(10,{}),(0,9))
        self.assertEqual(goldbach_interval(10,evidence),(2,2))
        partial={m:Trace(m) for m in range(2,21)}
        lo0,hi0=goldbach_interval(10,partial)
        for k in (9,11,7,13,10):
            partial[k]=normalize(k)
            lo,hi=goldbach_interval(10,partial)
            self.assertGreaterEqual(lo,lo0)
            self.assertLessEqual(hi,hi0)
            lo0,hi0=lo,hi

    def test_horn_operator_inflationary_monotone(self):
        a=frozenset({("seen",2)})
        b=frozenset({("seen",2),("seen",3),("tested",2,1)})
        self.assertLessEqual(a,b)
        self.assertLessEqual(kleene_step(a),kleene_step(b))
        x=frozenset()
        for _ in range(140):
            nxt=kleene_step(x)
            self.assertLessEqual(x,nxt)
            x=nxt
        sv=sieve(100)
        for n in range(2,101):
            if sv[n]:
                self.assertIn(("prime",n),x)
                self.assertFalse(any(f[0]=="composite" and f[1]==n for f in x))
            else:
                self.assertTrue(any(f[0]=="composite" and f[1]==n for f in x))
                self.assertNotIn(("prime",n),x)

    def test_counterfeit_prime_alphabet_no_4k_midpoints(self):
        sv=sieve(500)
        s={p for p in range(2,501) if sv[p] and p%4==1}
        self.assertTrue(s)
        self.assertTrue(all((p+q)%4==2 for p in s for q in s))
        for n in range(2,126):
            if n%2==0:  # 2n divisible by 4
                self.assertEqual(sum((n-d in s and n+d in s) for d in range(n-1)),0)

    def test_mutation_controls(self):
        with self.assertRaises(ValueError): prime(9)
        with self.assertRaises(ValueError): split(Trace(2),Trace(1))
        with self.assertRaises(ValueError): Trace(12,"split",Trace(2),Trace(7))
        self.assertFalse(refines(normalize(12,"minimum"),normalize(12,"balanced")))

if __name__=="__main__": unittest.main()
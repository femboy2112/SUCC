import unittest
from fractions import Fraction as Q
from itertools import combinations
from observational_succ.round2_completion import (alpha, squared_vacuum_overlap,
    crt_intersection, dual_mass, continuity_witness, action_ratios, transpose_test_tables)


class CompletionTests(unittest.TestCase):
    def test_crt_all_pairs(self):
        ps=(2,3,5,7)
        sets=[frozenset(c) for k in range(5) for c in combinations(ps,k)]
        for f in sets:
            for g in sets:
                intersection=crt_intersection(f,g)
                self.assertEqual(intersection,alpha(f|g))
                self.assertEqual(squared_vacuum_overlap(f,g),intersection**2/(alpha(f)*alpha(g)))
                if f<=g:
                    self.assertEqual(squared_vacuum_overlap(f,g),alpha(g)/alpha(f))

    def test_nonnested_mutation(self):
        self.assertNotEqual(squared_vacuum_overlap({2},{3}),alpha({3})/alpha({2}))
        self.assertEqual(squared_vacuum_overlap({2},{3}),Q(1,3))

    def test_fake_prime_rejected(self):
        for p in (0,1,4,9,True,2.0):
            with self.assertRaises(ValueError): alpha({p})

    def test_constant_test_extremizer(self):
        for weights in ([1]*40, [n*n for n in range(1,30)], [Q(n,7) for n in range(1,18)]):
            r=continuity_witness(weights)
            self.assertEqual(r['constant_pairing'],1)
            self.assertEqual(r['norm_squared'],1/dual_mass(weights))
            self.assertEqual(sum(r['atoms']),1)

    def test_harmonic_failure_not_infinity_claim(self):
        ns=(1,2,4,16,256)
        norms=[continuity_witness([1]*n)['norm_squared'] for n in ns]
        self.assertTrue(all(a>b for a,b in zip(norms,norms[1:])))
        self.assertEqual(norms[1],Q(2,3))

    def test_power_shift_norms(self):
        for p in (2,3,5):
            self.assertEqual(action_ratios(lambda n:n**2,p,range(1,40)),((Q(p*p),Q(1,p*p)),)*39)

    def test_summability_does_not_bound_source_shift(self):
        def w(n): return n*n if n%2 else n**4
        for n,(a,b) in zip(range(1,20,2),action_ratios(w,2,range(1,20,2))):
            self.assertEqual(a,16*n*n)
            self.assertEqual(a*b,1)
        self.assertLessEqual(dual_mass([w(n) for n in range(1,100)]),dual_mass([n*n for n in range(1,100)]))

    def test_weighted_adjoint_is_not_original_backward(self):
        p,n=3,7
        ratio=Q((p*n)**2,n*n)
        self.assertEqual(ratio,9)
        self.assertNotEqual(ratio,1)

    def test_transpose_pairings_and_domain(self):
        for p in (2,3,5):
            for q in (2,3,4,7):
                values=tuple(Q(x*x-2,q) for x in range(q))
                pull,cut=transpose_test_tables(p,values)
                self.assertEqual(len(cut),p*q)
                for n in range(1,3*p*q):
                    self.assertEqual(pull[n%q],values[(p*n)%q])
                    if n%p:
                        self.assertEqual(cut[n%(p*q)],0)
                    else:
                        self.assertEqual(cut[n%(p*q)],values[(n//p)%q])
        # Division modulo q loses which of the p lifts was divisible by p.
        _,cut=transpose_test_tables(2,(1,2,3))
        self.assertNotEqual(cut[0],cut[3])
        # Wrong multiplicative orientation is an actual separating test.
        pull,_=transpose_test_tables(2,(0,1,4))
        self.assertNotEqual(pull,(0,1,4))

    def test_invalid_weights(self):
        for w in ([0],[1,-1]):
            with self.assertRaises(ValueError): dual_mass(w)
        with self.assertRaises(ValueError): continuity_witness([])

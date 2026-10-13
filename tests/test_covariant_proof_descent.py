"""Exact source/claim covariance, group holonomy and full pullback testing."""
from itertools import product
import random
import unittest
from observational_succ.covariant_proof_descent import (
    OriginalSourceSquare,FrameHolonomy,FiniteBeckChevalley,
    permutation_inverse,permutation_compose,bit_shears,covariant_proof_demo,DescentError)


class SourceTransportTests(unittest.TestCase):
    def test_reversible_observation_and_source_truth_squares(self):
        m=OriginalSourceSquare('source',(1,0),(0,1),(1,0),(0,1),
                ((0,0),(1,1)),(1,0))
        self.assertTrue(m.observation_square()['commutes'])
        self.assertTrue(m.original_claim_square()['preserved'])
        self.assertEqual(dict(m.decoder()['decoder']),{0:0,1:1})

    def test_noninjective_carrier_can_destroy_original_truth(self):
        m=OriginalSourceSquare('S',(0,0),(0,1),(0,0),(0,1),((0,0),(1,0)))
        self.assertTrue(m.observation_square()['commutes'])
        self.assertFalse(m.original_claim_square()['preserved'])
        self.assertFalse(m.decoder()['factors'])
        self.assertEqual(m.decoder()['collision'],(0,1))

    def test_invertible_carrier_but_forgetful_observation_loses_claim(self):
        m=OriginalSourceSquare('S',(1,0),(0,1),(0,0),(0,1),((0,0),(1,0)))
        self.assertTrue(m.observation_square()['commutes'])
        self.assertTrue(m.original_claim_square()['preserved'])
        self.assertFalse(m.decoder()['factors'])

    def test_commuting_observation_square_not_automatic(self):
        m=OriginalSourceSquare('S',(1,0),(0,1),(0,1),(0,1),((0,0),(1,1)))
        self.assertFalse(m.observation_square()['commutes'])
        self.assertEqual(m.observation_square()['source_witness'],0)
        self.assertTrue(m.decoder()['factors'])

    def test_post_claim_mutation_refused(self):
        m=OriginalSourceSquare('S',(1,0),(0,1),(1,0),(0,1),
                ((0,0),(1,1)),(0,1))
        self.assertFalse(m.original_claim_square()['preserved'])

    def test_observation_transport_not_function_rejected(self):
        with self.assertRaises(DescentError):
            OriginalSourceSquare('S',(0,1),(0,1),(0,1),(0,1),((0,0),(0,1)))

    def test_exact_fiber_formula_exhaustive_two_state(self):
        for U in product(range(2),repeat=2):
            for O in product(range(2),repeat=2):
                for P in product(range(2),repeat=2):
                    m=OriginalSourceSquare('S',U,O,O,P)
                    ground=all(O[U[x]]!=O[U[y]] or P[x]==P[y] for x in range(2) for y in range(2))
                    self.assertEqual(m.decoder()['factors'],ground)


class FiniteFrameGroupTests(unittest.TestCase):
    def test_GL2_shears_are_nonglobal_but_zero_invariant(self):
        h=bit_shears()
        self.assertTrue(h.certificate()['invariant'])
        self.assertEqual(h.certificate()['orbit_partition'],((0,), (1,2,3)))
        self.assertNotEqual(h.transport(('A','B')),h.transport(('B','A')))
        self.assertEqual(h.transport(('A','-A')),tuple(range(4)))

    def test_noninvariant_claim_has_explicit_single_generator_witness(self):
        h=bit_shears()
        k=FrameHolonomy('S',h.generators,('0','1','1','0'))
        report=k.certificate()
        self.assertFalse(report['invariant'])
        x,y=report['source_witness']
        self.assertNotEqual(k.claim[x],k.claim[y])

    def test_full_generator_invariance_for_all_sixteen_binary_claims(self):
        h=bit_shears()
        winners=[]
        for target in product(('0','1'),repeat=4):
            m=FrameHolonomy('S',h.generators,target)
            sound=all(target[i]==target[g[i]] for _,g in m.generators for i in range(4))
            self.assertEqual(m.certificate()['invariant'],sound)
            if sound:winners.append(target)
        self.assertEqual(len(winners),4)

    def test_permutation_inverse_associative_composition(self):
        a=bit_shears().generators[0][1]
        b=bit_shears().generators[1][1]
        self.assertEqual(permutation_compose(a,permutation_inverse(a)),tuple(range(4)))
        self.assertEqual(permutation_compose(a,permutation_compose(b,a)),
                         permutation_compose(permutation_compose(a,b),a))

    def test_frame_group_renaming_missing_generator_rejected(self):
        h=bit_shears()
        with self.assertRaises(DescentError):h.transport(('C',))
        with self.assertRaises(DescentError):h.transport(('-C',))
        with self.assertRaises(DescentError):
            FrameHolonomy('S',(('BAD',(0,0,2,3)),),(0,1,1,1))


class BeckChevalleyTests(unittest.TestCase):
    def test_finite_pullback_positive(self):
        m=FiniteBeckChevalley((0,1,0),(1,0),2,((0,1),(1,0),(2,1)))
        self.assertTrue(m.audit()['pullback'])
        for bits in product((0,1),repeat=3):
            subset=tuple(i for i,b in enumerate(bits) if b)
            self.assertTrue(m.for_predicate(subset)['equal'])

    def test_commuting_proper_relation_does_not_guarantee_base_change(self):
        m=FiniteBeckChevalley((0,1),(0,1),2,((0,0),))
        self.assertFalse(m.audit()['beck_chevalley_for_all_predicates'])
        self.assertFalse(m.for_predicate((1,))['equal'])
        self.assertEqual(m.for_predicate((1,))['g_star_f_image'],(1,))
        self.assertEqual(m.for_predicate((1,))['q_image_p_star'],())

    def test_exhaustive_binary_cospans_and_all_relations(self):
        total=0
        for f in product(range(2),repeat=2):
            for g in product(range(2),repeat=2):
                pb=tuple((i,j) for i in range(2) for j in range(2) if f[i]==g[j])
                for choices in product((False,True),repeat=len(pb)):
                    rel=tuple(pair for pair,include in zip(pb,choices) if include)
                    M=FiniteBeckChevalley(f,g,2,rel)
                    all_equal=all(M.for_predicate(tuple(k for k in range(2) if bits[k]))['equal']
                                  for bits in product((False,True),repeat=2))
                    self.assertEqual(all_equal,M.audit()['pullback'])
                    total+=1
        self.assertEqual(total,82)

    def test_noncommuting_declared_relation_rejected(self):
        with self.assertRaises(DescentError):
            FiniteBeckChevalley((0,1),(0,1),2,((0,1),))

    def test_demo_covers_all_three_gates(self):
        r=covariant_proof_demo()
        self.assertTrue(r['frame_holonomy_noncommutes'])
        self.assertFalse(r['parity_claim_invariant'])
        self.assertTrue(r['commuting_but_incomplete_square_rejected'])


if __name__=='__main__':unittest.main()

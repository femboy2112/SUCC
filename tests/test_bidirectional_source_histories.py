"""Exact adversarial tests for source-faithful, bidirectional histories."""
import unittest
from fractions import Fraction as Q

from observational_succ.bidirectional_source_histories import (
    SourceHistoryError, affine_history_square, compose_at_cut, dual_labelled_messages,
    enumerate_stopped_words, exact, finite_stopped_pascal, genuine_prime,
    interval_law, pascal_cotransition_identity, project_pascal_words,
    source_path_law, valuation_edit_lower_bound, word_probability,
    conditioned_bidirectional_path_law,
)


def branching_source():
    layers=(('a','b'),('c','d'),('e','f'),('g',))
    kernels=(
        {'a':(('first','c',Q(1,3)),('other','c',Q(1,3)),('right','d',Q(1,3))),
         'b':(('zero','d',Q(1)),)},
        {'c':(('up','e',Q(1,4)),('down','f',Q(3,4))),
         'd':(('up','e',Q(2,3)),('down','f',Q(1,3)))},
        {'e':(('finish','g',Q(1)),),'f':(('finish','g',Q(1)),)},
    )
    initial={'a':Q(3,4),'b':Q(1,4)}
    return layers,kernels,initial


class HistoryFidelityTests(unittest.TestCase):
    def test_labeled_paths_retain_parallel_edges_with_equal_endpoints(self):
        layers,kernels,initial=branching_source()
        law=source_path_law(layers,kernels,initial)
        self.assertEqual(sum(law.values(),Q()),Q(1))
        self.assertTrue(any(p[1][0]=='first' for p in law))
        self.assertTrue(any(p[1][0]=='other' for p in law))
        self.assertNotEqual(len(law),len(layers[-1]))

    def test_all_cuts_exact_associativity(self):
        _,kernels,_=branching_source()
        for start in range(4):
            for end in range(start,4):
                for cut in range(start,end+1):
                    for x in kernels[start] if start<len(kernels) else ('g',):
                        self.assertEqual(compose_at_cut(kernels,start,cut,end,x),
                                         interval_law(kernels,start,end,x))

    def test_arithmetic_two_routes_share_source_paths_but_not_clock_receipts(self):
        # 4 microticks, from clock n=2 to p(n+1)=6 for prime p=2.
        kernels=tuple({'x':(('branch_A','x',Q(2+t,5+t)),
                              ('branch_B','x',Q(3,5+t)))} for t in range(4))
        result=affine_history_square(kernels,2,2,'x')
        self.assertTrue(result['routes_agree_on_source_histories'])
        self.assertFalse(result['clock_receipts_identical'])
        self.assertEqual(result['S_then_Vp_clock'],(2,3,6))
        self.assertEqual(result['Vp_then_Sp_clock'],(2,4,5,6))
        self.assertEqual(sum(result['fine_source_law'].values(),Q()),1)
        self.assertEqual(len(result['fine_source_law']),16)

    def test_unequal_observation_records_are_not_identified(self):
        _,kernels,_=branching_source()
        # Different cut points explicitly remain different observational receipts.
        self.assertNotEqual((2,3,6),(2,4,5,6))
        for p in (2,3,5):self.assertEqual(genuine_prime(p),p)
        with self.assertRaises(SourceHistoryError):genuine_prime(4)
        with self.assertRaises(SourceHistoryError):exact(0.2)
        with self.assertRaises(SourceHistoryError):exact(True)
        with self.assertRaises(SourceHistoryError):affine_history_square(kernels,2,4,'a')

    def test_future_conditioned_and_unconditional_reverse_are_distinct(self):
        layers,kernels,initial=branching_source()
        success={'g':Q(1)}
        answer=dual_labelled_messages(layers,kernels,initial,success)
        self.assertEqual(answer['cut_overlaps'],(Q(1),)*4)
        for rev in answer['reverse']:
            for row in rev.values():self.assertEqual(sum(row.values(),Q()),1)
        law=source_path_law(layers,kernels,initial)
        self.assertEqual(sum(law.values(),Q()),answer['Z'])

    def test_nontrivial_success_condition_and_doob_normalization(self):
        layers=(('s',),('x','y'),('ok','bad'))
        kernels=({'s':(('X','x',Q(1,3)),('Y','y',Q(2,3)))},
                 {'x':(('win','ok',Q(3,4)),('lose','bad',Q(1,4))),
                  'y':(('win','ok',Q(1,5)),('lose','bad',Q(4,5)))})
        d=dual_labelled_messages(layers,kernels,{'s':Q(1)},{'ok':Q(1),'bad':Q()})
        self.assertEqual(d['Z'],Q(1,3)*Q(3,4)+Q(2,3)*Q(1,5))
        self.assertTrue(all(v==d['Z'] for v in d['cut_overlaps']))
        for rows in d['doob']:
            for row in rows.values():self.assertEqual(sum(row.values(),Q()),1)
        # Every nonzero source flux is recovered by Bayes reverse.
        for t,rev in enumerate(d['reverse']):
            for y,row in rev.items():
                for (x,label),w in row.items():
                    self.assertEqual(d['alpha'][t+1][y]*w,
                                     d['unconditioned_edge_flux'][t][(x,label,y)])

    def test_forward_backward_entire_conditioned_history_identity(self):
        layers=(('s',),('x','y'),('ok','bad'))
        kernels=({'s':(('X','x',Q(1,3)),('Y','y',Q(2,3)))},
                 {'x':(('win','ok',Q(3,4)),('lose','bad',Q(1,4))),
                  'y':(('win','ok',Q(1,5)),('lose','bad',Q(4,5)))})
        event={'ok':Q(1),'bad':Q()}
        r=conditioned_bidirectional_path_law(layers,kernels,{'s':Q(1)},event)
        self.assertEqual(r['forward_histories'],r['backward_histories'])
        self.assertEqual(sum(r['backward_histories'].values(),Q()),1)
        self.assertEqual(len(r['forward_histories']),2)
        self.assertFalse(r['past_causal_reversal_proved'])
        with self.assertRaises(SourceHistoryError):
            conditioned_bidirectional_path_law(layers,kernels,{'s':Q(1)},
                                                {'ok':Q(),'bad':Q()})

    def test_no_prior_free_reverse_for_many_to_one_transition(self):
        layers=(('a','b'),('z',))
        kernels=({'a':(('a_src','z',Q(1)),),'b':(('b_src','z',Q(1)),)},)
        one=dual_labelled_messages(layers,kernels,{'a':Q(1,4),'b':Q(3,4)},{'z':Q(1)})
        two=dual_labelled_messages(layers,kernels,{'a':Q(3,4),'b':Q(1,4)},{'z':Q(1)})
        self.assertEqual(one['alpha'][-1],two['alpha'][-1])
        self.assertNotEqual(one['reverse'][0]['z'],two['reverse'][0]['z'])
        self.assertEqual(one['reverse'][0]['z'][('a','a_src')],Q(1,4))

    def test_mutant_row_rejected(self):
        layers,kernels,initial=branching_source()
        bad=list(kernels)
        bad[0]={**bad[0], 'a':(('z','c',Q(1,2)),('w','c',Q(1,3)))}
        with self.assertRaises(SourceHistoryError):source_path_law(layers,tuple(bad),initial)
        with self.assertRaises(SourceHistoryError):source_path_law(layers,kernels,{'a':1,'b':1})


class StoppedPascalTests(unittest.TestCase):
    def test_exact_normalization_and_word_law(self):
        for primes,beta,cap in (((2,),2,3),((2,3),2,2),((2,3,5),2,1),((2,3),4,2)):
            m=finite_stopped_pascal(primes,beta,cap)
            independent=enumerate_stopped_words(m)
            self.assertEqual(sum(independent.values(),Q()),1)
            for word,w in independent.items():
                self.assertEqual(word_probability(m,word),w)
            self.assertEqual(sum(m['terminal'].values(),Q()),1)

    def test_prime_deletion_projectivity_exact(self):
        for cap in (1,2):
            full=finite_stopped_pascal((2,3,5),2,cap)
            for sub in ((2,3),(2,5),(3,5),(2,),(5,),()):
                pushed=project_pascal_words(full,sub)
                if sub:
                    expected=enumerate_stopped_words(finite_stopped_pascal(sub,2,cap))
                else:
                    expected={():Q(1)}
                self.assertEqual(pushed,expected)

    def test_substochastic_backward_pascal_with_stop_mass(self):
        m=finite_stopped_pascal((2,3),2,3)
        checks=pascal_cotransition_identity(m)
        self.assertEqual(checks[(0,0)],(Q(1),m['terminal'][(0,0)],1-m['terminal'][(0,0)]))
        self.assertTrue(all(s==stop+future for s,stop,future in checks.values()))
        self.assertTrue(any(stop>0 for s,stop,future in checks.values()))

    def test_rank_normalization_corpse_matches_prior_pr236(self):
        # Rank-1 Gibbs P(first prime = 2) is (1/4)/(1/4+1/9) = 9/13.
        rank1=Q(1,4)/(Q(1,4)+Q(1,9))
        # Rank-2 Gibbs pushed back via alpha_2/2 gives 99/133.
        denom=Q(1,16)+Q(1,36)+Q(1,81)
        pushed=(Q(1,16)+Q(1,72))/denom
        self.assertEqual(rank1,Q(9,13))
        self.assertEqual(pushed,Q(99,133))
        self.assertNotEqual(rank1,pushed)

    def test_invalid_primitive_mutants_and_word_source(self):
        for p in ((2,4),(3,3),(True,3)):
            with self.assertRaises(SourceHistoryError):finite_stopped_pascal(p,2,2)
        m=finite_stopped_pascal((2,3),2,2)
        with self.assertRaises(SourceHistoryError):word_probability(m,(7,))
        with self.assertRaises(SourceHistoryError):finite_stopped_pascal((2,3),1,2)
        with self.assertRaises(SourceHistoryError):finite_stopped_pascal((2,3),2,2.0)


class NonlocalityAndPhysicalBoundaryTests(unittest.TestCase):
    def test_successor_cannot_have_uniformly_bounded_prime_occupation_edits(self):
        for k in (1,2,3,9,40):
            out=valuation_edit_lower_bound(k)
            self.assertEqual(out['min_occupation_L1_edits'],k)
            self.assertEqual(out['before_v2'],k)
            self.assertEqual(out['after_v2'],0)
            self.assertFalse(out['uniform_bounded_prime_edit_S_possible'])
        with self.assertRaises(SourceHistoryError):valuation_edit_lower_bound(0)

    def test_existing_growing_dtn_source_is_compatible(self):
        # Import in the actual repo also tests its dynamic_boundary_inverse API.
        from observational_succ.growing_dtn_history import ConductiveState, field_weighted_subset_process
        base=ConductiveState(('L','R','u','v'),('L','R'),(
            ('L','u',Q(1)),('u','R',Q(1)),('L','v',Q(1)),('v','R',Q(1))))
        candidates={'a':('L','u',Q(1)),'b':('u','v',Q(1)),
                    'c':('L','R',Q(1)),'d':('u','R',Q(1))}
        layers,raw=field_weighted_subset_process(base,candidates,4,Q(1,3))
        kernels=tuple({x:tuple((next(iter(y-x)),y,w) for y,w in row.items())
                       for x,row in K.items()} for K in raw)
        _validate=source_path_law(layers,kernels,{frozenset():Q(1)})
        self.assertEqual(sum(_validate.values(),Q()),1)
        square=affine_history_square(kernels,2,2,frozenset())
        self.assertTrue(square['routes_agree_on_source_histories'])
        self.assertFalse(square['clock_receipts_identical'])
        self.assertEqual(sum(square['fine_source_law'].values(),Q()),1)


if __name__ == '__main__':
    unittest.main()

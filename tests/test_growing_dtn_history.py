"""Exact tests and hostile controls for finite growing Dirichlet networks."""
import unittest
from fractions import Fraction as F
from itertools import permutations
from observational_succ.growing_dtn_history import (
    ConductiveState, GrowthContractError, replay, field_weighted_subset_process,
    exact_forward_backward, prime_clock_square, prime_adjoint_on_basis,
    history_affine_square,
)


def diamond():
    return ConductiveState(('L','R','u','v'),('L','R'),(
        ('L','u',F(1)),('u','R',F(1)),('L','v',F(1)),('v','R',F(1))))


class ExactNetworkTests(unittest.TestCase):
    def test_baseline_equivalent_parallel_paths(self):
        self.assertEqual(diamond().response(),((F(1),F(-1)),(F(-1),F(1))))
        self.assertEqual(diamond().energy((0,1)), F(1))
        self.assertEqual(diamond().potential((0,1))['u'],F(1,2))

    def test_rank_one_matches_direct_schur_all_endpoint_types(self):
        for edge in (('L','R',F(2,3)),('L','u',F(4,3)),
                     ('u','v',F(3,5)),('u','R',F(7))):
            w=diamond().edge_update(*edge)
            self.assertTrue(w['exact_match'])
            self.assertGreaterEqual(w['dirichlet_resistance'],0)
            self.assertGreater(w['rank_one_factor'],0)
            for v in ((0,0),(0,1),(4,-3)):
                q=sum((F(v[i])*w['observed_delta'][i][j]*F(v[j])
                       for i in (0,1) for j in (0,1)),F())
                self.assertGreaterEqual(q,0)

    def test_hidden_edge_invisible_to_complete_boundary_response(self):
        w=diamond().edge_update('u','v',F(7))
        self.assertEqual(w['voltage_drop_vector'],(F(),F()))
        self.assertEqual(w['predicted_delta'],((F(),F()),(F(),F())))
        self.assertNotEqual(w['successor'].edges,diamond().edges)
        self.assertEqual(w['successor'].response(),diamond().response())

    def test_hidden_memory_revealed_by_later_source_intervention(self):
        bare=diamond()
        hidden=bare.with_edge('u','v',F(7))
        self.assertEqual(bare.response(),hidden.response())
        self.assertEqual(bare.with_edge('L','u',1).energy((0,1)),F(7,6))
        self.assertEqual(hidden.with_edge('L','u',1).energy((0,1)),F(49,41))
        self.assertNotEqual(bare.with_edge('L','u',1).response(),
                            hidden.with_edge('L','u',1).response())

    def test_independent_kirchhoff_flux_oracle(self):
        for state in (diamond(),diamond().with_edge('L','u',1),
                      diamond().with_edge('u','v',F(7,3))):
            potentials=state.potential((0,1))
            flux_L=sum((g*(potentials['L']-potentials[b])
                        if a=='L' else g*(potentials['L']-potentials[a])
                        for a,b,g in state.edges if 'L' in (a,b)),F())
            flux_R=sum((g*(potentials['R']-potentials[b])
                        if a=='R' else g*(potentials['R']-potentials[a])
                        for a,b,g in state.edges if 'R' in (a,b)),F())
            self.assertEqual(flux_L,-state.energy((0,1)))
            self.assertEqual(flux_R,state.energy((0,1)))
            self.assertEqual(flux_L+flux_R,0)

    def test_exact_telescoping_all_additive_orderings(self):
        base=diamond()
        events=(('L','u',F(1)),('u','v',F(2,3)),('L','R',F(1,5)))
        ends=[]
        for ordering in permutations(events):
            states=replay(base,ordering)
            ends.append(states[-1].response())
            for j,event in enumerate(ordering):
                update=states[j].edge_update(*event)
                self.assertEqual(update['predicted_delta'],update['observed_delta'])
            summed=tuple(tuple(sum((states[k+1].response()[i][j]-states[k].response()[i][j]
                                    for k in range(len(events))),F())
                               for j in range(2)) for i in range(2))
            actual=tuple(tuple(states[-1].response()[i][j]-base.response()[i][j]
                               for j in range(2)) for i in range(2))
            self.assertEqual(summed,actual)
        self.assertEqual(len(set(ends)),1)

    def test_fixed_edges_terminal_flatness_but_interior_history_differs(self):
        e=('L','u',F(1))
        f=('u','v',F(3))
        x=replay(diamond(),(e,f))
        y=replay(diamond(),(f,e))
        self.assertNotEqual(x[1].response(),y[1].response())
        self.assertEqual(x[-1],y[-1])
        self.assertEqual(x[-1].response(),y[-1].response())
        self.assertNotEqual((e,f),(f,e))

    def test_material_memory_creates_nonzero_order_defect(self):
        x=diamond().with_edge('L','u',F(1))
        a,g_a=diamond().adaptive_edge('u','v',1,(0,1),1)
        route_a=a.with_edge('L','u',F(1))
        route_b,g_b=x.adaptive_edge('u','v',1,(0,1),1)
        self.assertEqual(g_a,F(1))
        self.assertEqual(g_b,F(37,36))
        self.assertNotEqual(route_a.edges,route_b.edges)
        self.assertNotEqual(route_a.response(),route_b.response())
        self.assertLess(route_a.energy((0,1)),route_b.energy((0,1)))

    def test_hostile_validation(self):
        with self.assertRaises(GrowthContractError):diamond().with_edge('u','v',0)
        with self.assertRaises(GrowthContractError):diamond().with_edge('u','v',-1)
        with self.assertRaises(GrowthContractError):diamond().with_edge('u','v',0.1)
        with self.assertRaises(GrowthContractError):diamond().with_edge('bad','v',1)
        with self.assertRaises(GrowthContractError):diamond().potential((1,))
        with self.assertRaises(GrowthContractError):diamond().adaptive_edge('u','v',1,(0,1),-1)
        with self.assertRaises(GrowthContractError):replay(diamond(),[['L','u',1]])


class DirectionalReconciliationTests(unittest.TestCase):
    def data(self):
        labels={'a':('L','u',F(1)),'b':('u','v',F(1)),
                'c':('L','R',F(1))}
        return field_weighted_subset_process(diamond(),labels,2,F(1,3))

    def test_exact_alpha_beta_invariant_and_reverse_bayes(self):
        layers, kernels=self.data()
        start={frozenset():F(1)}
        terminal={x:F('a' in x) for x in layers[-1]}
        r=exact_forward_backward(layers,kernels,start,terminal)
        self.assertEqual(len(r['overlap']),3)
        self.assertEqual(len(set(r['overlap'])),1)
        self.assertGreater(r['event_probability'],0)
        self.assertLess(r['event_probability'],1)
        for t,rev in enumerate(r['bayes_reverse']):
            for y,row in rev.items():
                self.assertEqual(sum(row.values(),F()),F(1))
                for x,val in row.items():
                    self.assertEqual(r['alpha'][t][x]*kernels[t][x].get(y,F()),
                                     r['alpha'][t+1][y]*val)
        for t,cond in enumerate(r['success_conditioned']):
            for x,row in cond.items():
                self.assertEqual(sum(row.values(),F()),F(1))

    def test_conditioned_reverse_same_kernel_on_supported_states(self):
        layers, kernels=self.data()
        r=exact_forward_backward(layers,kernels,{frozenset():F(1)},
                                 {x:F('a' in x) for x in layers[-1]})
        Z=r['event_probability']
        for t, kernel in enumerate(kernels):
            for x,row in r['success_conditioned'][t].items():
                for y, q in row.items():
                    if r['alpha'][t+1][y]*r['beta'][t+1][y]==0:continue
                    at_x=r['alpha'][t][x]*r['beta'][t][x]/Z
                    at_y=r['alpha'][t+1][y]*r['beta'][t+1][y]/Z
                    reverse_under_conditioning=at_x*q/at_y
                    self.assertEqual(reverse_under_conditioning,
                                     r['bayes_reverse'][t][y][x])

    def test_selection_mutation_does_not_forge_success(self):
        layers,kernels=self.data()
        start={frozenset():F(1)}
        no={x:F() for x in layers[-1]}
        self.assertEqual(exact_forward_backward(layers,kernels,start,no)['event_probability'],0)
        terminal={x:F('a' in x) for x in layers[-1]}
        exact=exact_forward_backward(layers,kernels,start,terminal)
        fake=[dict(row) for row in kernels]
        wrong={x:dict(choices) for x,choices in fake[0].items()}
        root=next(iter(wrong))
        first=next(iter(wrong[root]))
        wrong[root][first]+=F(1,13)
        fake[0]=wrong
        with self.assertRaises(GrowthContractError):
            exact_forward_backward(layers,tuple(fake),start,terminal)
        self.assertGreater(exact['event_probability'],0)

    def test_branching_blocks_faithful_clock_only_encoding(self):
        layers,_=self.data()
        # Two distinct one-event states share time n=2; time index cannot
        # encode both original source events injectively.
        self.assertGreater(len(layers[1]),1)
        self.assertEqual({len(x)+1 for x in layers[1]},{2})

    def test_wrong_direction_breaks_pairing(self):
        layers,kernels=self.data()
        start={frozenset():F(1)}
        terminal={x:F('a' in x) for x in layers[-1]}
        r=exact_forward_backward(layers,kernels,start,terminal)
        wrong={x:F() for x in layers[1]}
        self.assertNotEqual(sum((r['alpha'][1][x]*wrong[x] for x in layers[1]),F()),
                            r['event_probability'])

    def test_malformed_transition_rejected(self):
        layers,kernels=self.data()
        with self.assertRaises(GrowthContractError):
            exact_forward_backward(layers,kernels,{frozenset():F(0)}, {})
        with self.assertRaises(GrowthContractError):
            field_weighted_subset_process(diamond(),{'a':('L','u',1)},2)


class AffineClockTests(unittest.TestCase):
    def test_forward_and_adjoint_backward_squares_all_small_primes(self):
        for p in (2,3,5,7,11):
            for n in range(1,51):
                r=prime_clock_square(n,p)
                self.assertTrue(r['equal'])
                self.assertEqual(r['backward_Sstar_Vpstar'],n)
                self.assertEqual(r['backward_Vpstar_Sstar_p'],n)
            for m in range(1,51):
                lhs=prime_adjoint_on_basis(m,p)
                lhs=lhs-1 if lhs is not None and lhs>1 else None
                rhs=m-p if m>p else None
                rhs=prime_adjoint_on_basis(rhs,p) if rhs is not None else None
                self.assertEqual(lhs,rhs)

    def test_same_history_two_affine_routes_equal_endpoint_not_same_records(self):
        states=replay(diamond(),(('L','u',1),('L','R',F(1,2)),('u','v',F(3))))
        square=history_affine_square(states,1,2)
        self.assertTrue(square['terminal_equal'])
        self.assertEqual(square['S_then_Vp_indices'],(1,2,4))
        self.assertEqual(square['Vp_then_Sp_indices'],(1,2,3,4))
        self.assertNotEqual(square['S_then_Vp_responses'],square['Vp_then_Sp_responses'])
        with self.assertRaises(GrowthContractError):history_affine_square(states,2,2)

    def test_backwards_prime_has_kernel_and_is_not_global_inverse(self):
        self.assertIsNone(prime_adjoint_on_basis(5,3))
        self.assertEqual(prime_adjoint_on_basis(6,3),2)
        with self.assertRaises(GrowthContractError):prime_clock_square(2,4)
        with self.assertRaises(GrowthContractError):prime_adjoint_on_basis(3,1)


if __name__=='__main__':
    unittest.main()

import itertools
import random
import unittest
from fractions import Fraction as Q

from observational_succ import (BudgetExceeded, DomainError, Engine, IncompleteObservation,
                           I, Limits, ONE, Scalar, ShadowIndex, ZERO,
                           clock_contract, conditional_mean, conductor_growth,
                           connected_audit, factorization, mixed_probe,
                           run_arithmetic, source_at, structure_birth)


def oracle_paths(n, allowed):
    # Different implementation: recursively enumerate literal ordered paths;
    # production uses a compressed dynamic-programming polynomial/DAG.
    def rec(rem):
        if rem == 1:
            yield ()
        for a in allowed:
            if a <= rem and rem % a == 0:
                for tail in rec(rem//a):
                    yield (a,)+tail
    return tuple(p for p in rec(n) if len(p) >= 2)


def oracle_weight(paths, known):
    total = ZERO
    for path in paths:
        val = ONE
        for x in path: val *= known[x]
        total += val*Q((-1)**(len(path)+1), len(path))
    return total


class ShadowTests(unittest.TestCase):
    def test_6_8_12_trajectories(self):
        e = Engine(arithmetic=True)
        expected = {2: {6:0, 8:Q(1,3), 12:0},
                    3: {6:-1, 8:Q(1,3), 12:1},
                    4: {6:-1, 8:Q(-2,3), 12:0},
                    6: {6:-1, 8:Q(-2,3), 12:-1}}
        for n in range(1, 13):
            e.advance(ONE)
            if n in expected:
                for target, value in expected[n].items():
                    self.assertEqual(Scalar.from_data(e.shadow(target)["weight"]), Scalar.of(value))
            if n in (6,8,12):
                self.assertEqual(Scalar.from_data(e.shadow(n)["source"]["connected"]),
                                 Scalar.of(Q(1,3) if n==8 else 0))
        self.assertEqual(len(e.state["arithmetic"]), 12)

    def test_zero_weight_preserves_paths(self):
        e = run_arithmetic(4)
        info = e.shadow(12, witnesses=True)
        self.assertEqual(Scalar.from_data(info["weight"]), ZERO)
        self.assertEqual(info["occurrences"], 5)
        self.assertFalse(info["observed"])
        self.assertEqual(sorted(info["witnesses"]["paths"]), [[2,2,3],[2,3,2],[3,2,2],[3,4],[4,3]])

    def test_exhaustive_counts_and_weights(self):
        for N in range(1, 13):
            known = {n: source_at(n) for n in range(1,N+1)}
            idx = ShadowIndex(known)
            for target in range(2,49):
                paths = oracle_paths(target, range(2,N+1))
                ent = idx.entry(target)
                self.assertTrue(ent.complete)
                self.assertEqual(ent.occurrences, len(paths), (N,target))
                self.assertEqual(ent.weight, oracle_weight(paths,known), (N,target))

    def test_non_zeta_holdout_coefficients(self):
        rng = random.Random(7121)
        for _ in range(8):
            known = {1: ONE, **{n:Scalar(Q(rng.randint(-2,2),3),Q(rng.randint(-1,1),5)) for n in range(2,10)}}
            idx = ShadowIndex(known)
            for target in [6, 8, 12, 18, 24, 30, 36, 42, 48, 54, 60, 64]:
                self.assertEqual(idx.entry(target).weight, oracle_weight(oracle_paths(target,range(2,10)), known))

    def test_zero_source_coefficient_does_not_delete_combinatorics(self):
        idx = ShadowIndex({1:ONE,2:ZERO,3:ONE})
        self.assertEqual(idx.entry(6).weight,ZERO)
        self.assertEqual(idx.entry(6).occurrences,2)

    def test_source_online_causality(self):
        # Source providers differ only in a future event. No earlier states change.
        left, right = Engine(arithmetic=True), Engine(arithmetic=True)
        for n in range(1,6):
            left.advance(source_at(n))
            right.advance(source_at(n,overrides={6:Scalar('8/7')}))
            self.assertEqual(left.dumps(),right.dumps())
        left.advance(ONE); right.advance(Scalar('8/7'))
        self.assertEqual(left.shadow(6)['source']['status'],'consistent')
        self.assertEqual(right.shadow(6)['source']['status'],'mixed_composite_defect')
        self.assertEqual(Scalar.from_data(right.shadow(6)['source']['connected']),Scalar('1/7'))

    def test_genuine_characters_and_mixture(self):
        for kind in ['zeta','chi5','chi5_bar']:
            idx=ShadowIndex({n:source_at(n,kind) for n in range(1,65)})
            for n in range(2,65): self.assertEqual(connected_audit(idx,n)['status'],'consistent',(kind,n))
        mix=run_arithmetic(6,kind='mixture5')
        self.assertEqual(Scalar.from_data(mix.shadow(6)['source']['connected']),ONE)
        # Exact nonreal conjugate-character mixture: generic kappa=1/3 control.
        a=Scalar(Q(1,2),Q(-1,6))
        known={n:a*source_at(n,'chi5')+(ONE-a)*source_at(n,'chi5_bar') for n in range(1,7)}
        self.assertEqual(ShadowIndex(known).connected(6),Scalar(Q(10,9)))

    def test_unit_and_half_density_and_clock_mutations(self):
        with self.assertRaises(DomainError): ShadowIndex({1:Scalar(2)})
        idx=ShadowIndex({1:ONE,2:Scalar('103/100')})
        self.assertEqual(connected_audit(idx,2)['status'],'nonunit_local_factor')
        self.assertTrue(clock_contract(8,[(2,3)]))
        with self.assertRaises(DomainError): clock_contract(2,[(2,Q(101,100))])
        with self.assertRaises(DomainError): clock_contract(2,[(2,1)],Q(49,100))

    def test_ramification_is_explicit(self):
        idx=ShadowIndex({1:ONE,2:ZERO})
        self.assertEqual(connected_audit(idx,2,1)['status'],'nonunit_local_factor')
        self.assertEqual(connected_audit(idx,2,2)['status'],'consistent')
        idx=ShadowIndex({1:ONE,2:ONE})
        self.assertEqual(connected_audit(idx,2,2)['status'],'ramification_defect')
        e=run_arithmetic(6,kind='chi5')
        self.assertEqual(e.shadow(5)['source']['status'],'consistent')
        with self.assertRaises(TypeError):idx.known[2]=ZERO

    def test_unknown_is_not_observed_zero(self):
        idx=ShadowIndex({1:ONE,2:ONE,6:ONE})
        self.assertEqual(connected_audit(idx,6)['status'],'unobserved_divisors')
        with self.assertRaises(IncompleteObservation): idx.connected(8)

    def test_depth_limit_is_explicit(self):
        idx=ShadowIndex({1:ONE,2:ONE},Limits(max_depth=2))
        e=idx.entry(8)
        self.assertFalse(e.complete)
        self.assertEqual(e.weight,ZERO)
        with self.assertRaises(IncompleteObservation): e.exact_weight()
        with self.assertRaises(IncompleteObservation): ShadowIndex({1:ONE,2:ONE,8:ONE},Limits(max_depth=2)).connected(8)
        with self.assertRaises(BudgetExceeded): idx.entry(65)

    def test_witness_clipping_does_not_clip_exact_aggregate(self):
        idx=ShadowIndex({n:ONE for n in range(1,13)},Limits(max_witnesses=2))
        out=idx.witnesses(12)
        self.assertFalse(out['expansion_complete'])
        self.assertTrue(out['aggregate_complete'])
        self.assertEqual(len(out['paths']),2)

    def test_conductor_clock_and_holdouts(self):
        from math import lcm
        for d in range(1,257):
            b=structure_birth(d)
            self.assertEqual(lcm(*range(1,b+1))%d,0)
            if b>1:self.assertNotEqual(lcm(*range(1,b))%d,0)
        self.assertEqual(conductor_growth(3)['born_conductors'],[3,6])
        self.assertEqual(conductor_growth(6)['innovation_rank'],0)
        self.assertIsNone(conductor_growth(30,max_divisors=1)['born_conductors'])

    def test_joint_probe_arity(self):
        for ps in [(2,3),(2,3,5),(3,5,7)]:
            vals=mixed_probe(ps)
            for r in range(len(ps)):
                for subset in itertools.combinations(ps,r):
                    from math import prod
                    self.assertEqual(set(conditional_mean(vals,prod(subset))),{Q(0)})
            from math import prod
            self.assertEqual(sum(v*v for v in vals)/len(vals),prod(Q(p-1,p*p) for p in ps))
        with self.assertRaises(DomainError): mixed_probe((2,6))
        with self.assertRaises(BudgetExceeded): mixed_probe((2,3,5),Limits(max_probe_cells=6))


if __name__=='__main__':unittest.main()

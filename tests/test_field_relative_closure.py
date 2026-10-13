"""Exact finite observational closure, source consistency, frame invariance."""
import random
import unittest
from dataclasses import replace
from itertools import product

from observational_succ.field_relative_closure import (
    ClosureError, FiniteField, invariant_orbits, minimal_inconsistent_core,
)


def field2():
    states=tuple(product((0,1),repeat=2))
    return FiniteField("real-carrier-declared","v1",states,
                       {"a":tuple(x[0] for x in states),
                        "b":tuple(x[1] for x in states),
                        "constant":(0,)*4},
                       {"xor":tuple(x[0]^x[1] for x in states),
                        "a":tuple(x[0] for x in states),
                        "constant":(7,)*4})

class FieldClosureTests(unittest.TestCase):
    def test_one_probe_original_bit_is_finite_simple(self):
        f=field2();c=f.factor(("a",),"a")
        self.assertTrue(c.proved)
        self.assertTrue(f.verify(c))
        self.assertEqual(len(c.decoder),2)

    def test_one_probe_original_parity_has_real_rival(self):
        f=field2();c=f.factor(("a",),"xor")
        self.assertFalse(c.proved)
        x,y=c.counterexample
        self.assertEqual(f.signature(x,("a",)),f.signature(y,("a",)))
        self.assertNotEqual(x[0]^x[1],y[0]^y[1])
        self.assertTrue(f.verify(c))

    def test_two_probes_prove_original_parity(self):
        f=field2();c=f.factor(("a","b"),"xor")
        self.assertTrue(c.proved)
        self.assertEqual(len(c.decoder),4)
        self.assertTrue(f.verify(c))

    def test_forged_decoder_is_rejected(self):
        f=field2();c=f.factor(("a","b"),"xor")
        fake=replace(c,decoder=c.decoder[1:])
        with self.assertRaisesRegex(ClosureError,"False"):
            f.verify(fake)

    def test_forged_rival_is_rejected(self):
        f=field2();c=f.factor(("a",),"xor")
        with self.assertRaisesRegex(ClosureError,"False"):
            f.verify(replace(c,counterexample=((0,0),(1,1))))

    def test_source_and_basis_are_independent_gates(self):
        f=field2();c=f.factor(("a","b"),"xor")
        for fake in (replace(c,source_id="surrogate"),replace(c,basis_id="v2"),
                     replace(c,source_count=3)):
            with self.assertRaisesRegex(ClosureError,"Wrong source"):
                f.verify(fake)

    def test_finite_rank_first_stage_and_nonretraction(self):
        f=field2();v=f.finite_depth((("a",),("a","b")),"xor")
        self.assertEqual(v['status'],"FINITE_CLOSURE")
        self.assertEqual(v['rank'],1)
        self.assertTrue(f.verify(v['certificate']))
        with self.assertRaisesRegex(ClosureError,"retracted"):
            f.finite_depth((("a","b"),("a",)),"xor")

    def test_finite_horizon_is_not_omega_refutation(self):
        f=field2();v=f.finite_depth((("constant",),("constant","a")),"xor")
        self.assertEqual(v['status'],"UNRESOLVED_FINITE_HORIZON")
        self.assertIsNone(v['rank'])
        self.assertIsNotNone(v['rival'])

    def test_constant_target_factors_through_zero_probes(self):
        f=field2();c=f.factor((),"constant")
        self.assertTrue(c.proved)
        self.assertEqual(c.decoder,(((),7),))

    def test_all_pairwise_even_parity_reports_can_be_globally_impossible(self):
        states=((0,0,0),(0,1,1),(1,0,1),(1,1,0))
        f=FiniteField("even-parity","v1",states,
                      {f"bit{i}":tuple(x[i] for x in states) for i in range(3)},
                      {"target":tuple(x[0] for x in states)})
        records=tuple((f"bit{i}",1) for i in range(3))
        r=f.local_realizability(records)
        self.assertTrue(r['pairwise_realizable'])
        self.assertEqual(r['status'],"NO_GLOBAL_SOURCE_WITNESS")
        core=minimal_inconsistent_core(f,records)
        self.assertEqual(len(core.minimal_records),3)
        self.assertTrue(core.proper_subsets_realizable)

    def test_simple_inconsistent_pair_and_consistent_data(self):
        f=field2()
        core=minimal_inconsistent_core(f,(("a",0),("a",1),("b",0)))
        self.assertEqual(core.minimal_records,(("a",0),("a",1)))
        self.assertIsNone(minimal_inconsistent_core(f,(("a",0),("b",1))))

    def test_resource_cap_does_not_mean_consistency(self):
        f=field2()
        with self.assertRaisesRegex(ClosureError,"exhausted"):
            minimal_inconsistent_core(f,(("a",0),("a",1),("b",1)),max_subsets=1)

    def test_gl2_zero_claim_invariant_original_parity_not(self):
        states=(0,1,2,3)  # bit-pairs 00,01,10,11
        A=(0,1,3,2)  # (a,b)->(a,a xor b)
        B=(0,3,2,1)  # (a,b)->(a xor b,b)
        source_zero=(1,0,0,0)
        original_parity=(0,1,1,0)
        r=invariant_orbits(states,(A,B),source_zero)
        self.assertTrue(r['claim_is_frame_invariant'])
        self.assertEqual(set(r['orbits']),{(0,),(1,2,3)})
        s=invariant_orbits(states,(A,B),original_parity)
        self.assertFalse(s['claim_is_frame_invariant'])
        self.assertIsNotNone(s['generator_violation'])

    def test_nonpermutation_frame_rejected(self):
        with self.assertRaisesRegex(ClosureError,"permutation"):
            invariant_orbits((0,1),((0,0),),(0,1))

    def test_invalid_source_tables_rejected(self):
        f=field2()
        with self.assertRaises(ClosureError):
            FiniteField("x","y",(0,0),{"a":(0,0)},{"t":(0,0)})
        with self.assertRaises(ClosureError):
            f.names(("a","a"))
        with self.assertRaises(ClosureError):
            f.signature((2,2),("a",))

    def test_independent_exhaustive_random_truth_table_oracle(self):
        rng=random.Random(44167)
        for _ in range(420):
            n=rng.randint(2,8)
            m=rng.randint(1,5)
            probes={f"p{i}":tuple(rng.randrange(3) for j in range(n)) for i in range(m)}
            t=tuple(rng.randrange(3) for j in range(n))
            f=FiniteField("seeded-source","v1",tuple(range(n)),probes,{"target":t})
            names=tuple(p for p in probes if rng.randrange(2))
            c=f.factor(names,"target")
            brute=all(t[i]==t[j] or any(probes[p][i]!=probes[p][j] for p in names)
                      for i in range(n) for j in range(i+1,n))
            self.assertEqual(c.proved,brute)
            self.assertTrue(f.verify(c))

if __name__=='__main__':unittest.main()

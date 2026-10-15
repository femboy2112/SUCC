"""Independent exact hostile tests of categorical edge-to-carrier reconstructions.

Finite probes validate selected canonical presentations and source mutations.
Their correctness on *all* integers/all inverse-limit points is established
by the paper's universal-property/CRT proofs, NOT a finite test campaign.
"""
import random
import unittest
from fractions import Fraction as F
from math import gcd, lcm

from observational_succ.edge_carrier_reconstruction import (
    EdgeCarrierError, NatLoop, IntegerLoop, RayPath,
    RationalSpan, SLocalization, GaussianInteger, GaussianRational,
    ProfiniteProgram, finite_clock_collision, finite_prime_partition,
    prime_projector_is_not_integer, carrier_interface_contract,
    finite_cyclic_yoneda,
)


class NatToIntegerEdgeTests(unittest.TestCase):
    def test_free_one_vertex_successor_loop_composition(self):
        for a in range(23):
            for b in range(23):
                self.assertEqual(NatLoop(a).then(NatLoop(b)), NatLoop(a+b))
                self.assertEqual(NatLoop(a).then(NatLoop(b)).group_complete().winding,a+b)
        self.assertEqual(NatLoop(0).then(NatLoop(7)), NatLoop(7))
        for bad in (-1, True, F(1,2), 1.5):
            with self.assertRaises(EdgeCarrierError):
                NatLoop(bad)

    def test_raw_paths_equivalence_not_tuple_equality(self):
        raw=IntegerLoop(9,6)
        alternate=IntegerLoop(7,4)
        self.assertNotEqual(raw,alternate)  # source-event presentations differ
        self.assertTrue(raw.equivalent(alternate))  # quotient morphism is the same
        self.assertEqual(raw.canonical(),IntegerLoop(3))
        self.assertEqual(alternate.canonical(),IntegerLoop(3))
        self.assertFalse(raw.equivalent(IntegerLoop(4)))
        self.assertTrue(raw.then(raw.inverse()).equivalent(IntegerLoop(0)))

    def test_group_laws_and_torsor_origin(self):
        rng=random.Random(17823)
        for _ in range(400):
            x,y,z=(IntegerLoop.from_winding(rng.randint(-35,35)) for _ in range(3))
            self.assertTrue(x.then(y).then(z).equivalent(x.then(y.then(z))))
            self.assertTrue(x.then(y).equivalent(y.then(x)))
            self.assertTrue(x.then(x.inverse()).equivalent(IntegerLoop(0)))
            origin=rng.randint(-20,20)
            self.assertEqual(x.transport(origin),origin+x.winding)
            self.assertEqual(x.then(y).transport(origin), origin+x.winding+y.winding)

    def test_cyclic_target_universal_extension(self):
        for modulus in range(2,15):
            for gen in range(modulus):
                for n in range(-23,24):
                    p=IntegerLoop.from_winding(n)
                    self.assertEqual(p.cyclic_target(modulus,gen),n*gen%modulus)
                    self.assertEqual(p.canonical().cyclic_target(modulus,gen),n*gen%modulus)
                self.assertEqual(IntegerLoop(1,1).cyclic_target(modulus,gen),0)
        with self.assertRaises(EdgeCarrierError):
            IntegerLoop(1).cyclic_target(1,0)

    def test_yoneda_all_natural_endomaps_recover_exactly_all_edges(self):
        for modulus in range(1,7):
            receipt=finite_cyclic_yoneda(modulus)
            self.assertEqual(receipt["candidate_endofunctions"],modulus**modulus)
            self.assertEqual(receipt["naturality_constrained_endofunctions"],modulus)
            self.assertTrue(receipt["natural_transformation_to_arrow_bijection"])
            self.assertFalse(receipt["yoneda_full_faithfulness_generalized_by_samples"])

    def test_naturality_not_just_an_arbitrary_cardinality_match(self):
        modulus=5
        counterfeit=tuple((2*x)%modulus for x in range(modulus))
        self.assertEqual(len(counterfeit),modulus)
        self.assertNotEqual(counterfeit[1],(counterfeit[0]+1)%modulus)
        self.assertEqual(finite_cyclic_yoneda(modulus)["recovered_cyclic_edges"],5)

    def test_a_ray_is_a_tree_not_an_integer_loop_group(self):
        self.assertEqual(RayPath(0,(1,1,-1,-1)).thin_groupoid_arrow(),(0,0))
        self.assertFalse(RayPath(0,(1,1,-1,-1)).nontrivial_based_loop_after_reduction)
        self.assertEqual(RayPath(3,(-1,-1,1,1,1)).end,4)
        self.assertEqual(RayPath(1,(-1,)).then(RayPath(0,(1,))).end,1)
        with self.assertRaises(EdgeCarrierError):
            RayPath(0,(-1,))
        with self.assertRaises(EdgeCarrierError):
            RayPath(0,(1,0))
        with self.assertRaises(EdgeCarrierError):
            RayPath(0,(1,)).then(RayPath(0,(1,)))

    def test_naive_group_completion_of_non_cancellative_monoid_cannot_embed(self):
        # In the idempotent monoid {0,e}, e+e=e. In an abelian
        # group, x+x=x implies x=0. The source map is not injective.
        e_source_distinct_from_zero = True
        e_group_winding = 0  # forced by e+e=e after cancellation
        self.assertTrue(e_source_distinct_from_zero)
        self.assertEqual(e_group_winding,0)


class IntegerToRationalLocalizationTests(unittest.TestCase):
    def test_integer_numerator_comes_from_edge_quotient(self):
        x=RationalSpan.from_edges(IntegerLoop(2,7),NatLoop(15))
        self.assertEqual(x,RationalSpan(-1,3))
        self.assertEqual(x.as_fraction(),F(-1,3))
        with self.assertRaises(EdgeCarrierError):
            RationalSpan.from_edges(IntegerLoop(1),NatLoop(0))
        self.assertEqual(RationalSpan(20,-12),RationalSpan(-5,3))
        self.assertEqual(RationalSpan(0,-7),RationalSpan(0,1))

    def test_fraction_field_laws_independent_fraction_oracle(self):
        rng=random.Random(902)
        for _ in range(600):
            an,ad,bn,bd=(rng.randint(-30,30),rng.randint(1,19),
                         rng.randint(-30,30),rng.randint(1,19))
            x,y=RationalSpan(an,ad),RationalSpan(bn,bd)
            A,B=F(an,ad),F(bn,bd)
            self.assertEqual(x.add(y).as_fraction(),A+B)
            self.assertEqual(x.subtract(y).as_fraction(),A-B)
            self.assertEqual(x.multiply(y).as_fraction(),A*B)
            if bn:
                self.assertEqual(x.divide(y).as_fraction(),A/B)
                self.assertEqual(y.multiply(y.inverse()).as_fraction(),F(1))
            else:
                with self.assertRaises(EdgeCarrierError):
                    y.inverse()
        self.assertEqual(RationalSpan(0).add(RationalSpan(17,5)),RationalSpan(17,5))

    def test_localizations_restrict_denominators_not_numerators(self):
        z=SLocalization(())
        two=z.extend(2)
        two_three=two.extend(3)
        self.assertTrue(z.contains(RationalSpan(-111,1)))
        self.assertFalse(z.contains(RationalSpan(1,2)))
        self.assertTrue(two.contains(RationalSpan(13,2**10)))
        self.assertFalse(two.contains(RationalSpan(1,3)))
        self.assertTrue(two_three.contains(RationalSpan(-11,2**4*3**3)))
        self.assertFalse(two_three.contains(RationalSpan(11,5)))
        self.assertTrue(z.inclusion_preserves(RationalSpan(3),two))
        self.assertTrue(two.inclusion_preserves(RationalSpan(1,8),two_three))
        with self.assertRaises(EdgeCarrierError):
            two.admit(RationalSpan(1,6))
        with self.assertRaises(EdgeCarrierError):
            two.extend(2)
        with self.assertRaises(EdgeCarrierError):
            two.extend(6)
        with self.assertRaises(EdgeCarrierError):
            SLocalization((3,2))
        with self.assertRaises(EdgeCarrierError):
            z.inclusion_preserves(RationalSpan(1,2),
                    SLocalization((2,),"different-source"))

    def test_localization_non_domain_does_not_embed(self):
        # In Z/6Z, 2*3=0, but 3!=0. Inverting 2 kills 3.
        # The ring localization exists but cannot be faithful on Z/6Z.
        self.assertEqual(2*3%6,0)
        self.assertNotEqual(3%6,0)


class GaussianCarrierTests(unittest.TestCase):
    def test_gaussian_ring_relations_and_norm(self):
        i=GaussianInteger.from_pair(0,1)
        one=GaussianInteger.from_pair(1,0)
        negone=GaussianInteger.from_pair(-1,0)
        self.assertEqual(i.multiply(i).pair,negone.pair)
        self.assertEqual(i.multiply(i).multiply(i).multiply(i).pair,one.pair)
        self.assertEqual(i.multiply(i.conjugate()).pair,one.pair)
        rng=random.Random(111)
        for _ in range(280):
            a,b,c,d=(rng.randint(-25,25) for _ in range(4))
            x=GaussianInteger.from_pair(a,b)
            y=GaussianInteger.from_pair(c,d)
            self.assertEqual(x.add(y).pair,(a+c,b+d))
            self.assertEqual(x.multiply(y).pair,(a*c-b*d,a*d+b*c))
            self.assertEqual(x.multiply(y).norm(),x.norm()*y.norm())
            self.assertEqual(x.multiply(x.conjugate()).pair,(x.norm(),0))
            self.assertEqual(x.norm(),a*a+b*b)

    def test_gaussian_ring_is_not_coordinatewise_Z_times_Z_ring(self):
        i=GaussianInteger.from_pair(0,1)
        self.assertEqual(i.multiply(i).pair,(-1,0))
        self.assertNotEqual(i.multiply(i).pair,(0,1)) # coordinatewise square wrong

    def test_Qi_has_exact_inverse_but_not_all_of_C(self):
        z=GaussianRational(RationalSpan(3,2),RationalSpan(4,5))
        one=GaussianRational(RationalSpan(1),RationalSpan(0))
        self.assertEqual(z.multiply(z.inverse()).as_pair(),one.as_pair())
        i=GaussianRational.from_gaussian(GaussianInteger.from_pair(0,1))
        self.assertEqual(i.multiply(i).as_pair(),(F(-1),F(0)))
        zero=GaussianRational(RationalSpan(0),RationalSpan(0))
        with self.assertRaises(EdgeCarrierError):
            zero.inverse()
        # Q(i) consists only of rational coordinate pairs; C also
        # contains sqrt(2), which cannot be rational (parity proof).
        self.assertFalse(any(F(a,b)**2==2
                for a in range(-30,31) for b in range(1,20)))


class ProfiniteCompletionTests(unittest.TestCase):
    def test_integer_embedding_compatible_all_divisibility_edges(self):
        for k in (-97,-1,0,1,97,100000):
            p=ProfiniteProgram.integer(k)
            for n in range(1,45):
                for factor in (1,2,3,7):
                    r=p.bonding(n*factor,n)
                    self.assertTrue(r["ring_bonding_compatible"])
                    self.assertEqual(r["larger_residue"]%n,r["smaller_residue"])
                    self.assertFalse(r["all_points_of_Zhat_finitely_described"])

    def test_CRT_prime_projector_independent_brute_solver(self):
        for p in (2,3,5,7,11):
            e=ProfiniteProgram.projector(p)
            for n in range(1,250):
                a=e.residue(n)
                k=n
                while k%p==0: k//=p
                power=n//k
                self.assertEqual(a%power, 1%power)
                self.assertEqual(a%k,0)
                self.assertEqual(a*a%n,a)
                self.assertTrue(0<=a<n)
                self.assertEqual(e.bonding(n*2,n)["larger_residue"]%n,a)

    def test_partition_of_unity_and_orthogonality(self):
        for n in range(1,260):
            r=finite_prime_partition(n)
            self.assertTrue(r["ring_partition_certified_at_finite_stage"])
            self.assertEqual(r["sum_modulus"],1%n)
            self.assertTrue(all(value==0 for value in r["pairwise_products"].values()))
            self.assertEqual(set(r["prime_places"]),set(r["idempotent_residues"]))
            self.assertFalse(r["all_primes_computed_in_this_finite_stage"])
        a,b=ProfiniteProgram.projector(2),ProfiniteProgram.projector(3)
        for n in range(1,160):
            self.assertEqual(a.multiply(b).residue(n),0)
            self.assertEqual(a.multiply(a).residue(n),a.residue(n))

    def test_new_global_points_not_diagonal_integers(self):
        for p in (2,3,5,7,11):
            r=prime_projector_is_not_integer(p)
            self.assertFalse(r["in_diagonal_Z"])
            self.assertTrue(r["nontrivial"])
            self.assertFalse(r["full_Zhat_reconstructed_by_finitely_many_samples"])

    def test_recursive_ring_operations_commute_with_bonding(self):
        rng=random.Random(41)
        for _ in range(90):
            p=rng.choice((2,3,5))
            q=rng.choice((2,3,5))
            x=ProfiniteProgram.projector(p)
            y=ProfiniteProgram.projector(q)
            z=ProfiniteProgram.integer(rng.randint(-100,100))
            w=x.multiply(y.add(z)).add(y.multiply(z))
            for n in (2,3,4,6,8,9,15,30,48,60,90,120):
                expected=(x.residue(n)*(y.residue(n)+z.residue(n))+
                          y.residue(n)*z.residue(n))%n
                self.assertEqual(w.residue(n),expected)
                self.assertTrue(w.bonding(n*2,n)["ring_bonding_compatible"])

    def test_source_mutations_and_invalid_divisibility_rejected(self):
        x=ProfiniteProgram.integer(3,source_id="one",epoch=2)
        y=ProfiniteProgram.integer(4,source_id="other",epoch=2)
        with self.assertRaises(EdgeCarrierError):
            x.add(y)
        with self.assertRaises(EdgeCarrierError):
            x.multiply(y)
        with self.assertRaises(EdgeCarrierError):
            x.bonding(9,4)
        with self.assertRaises(EdgeCarrierError):
            x.residue(0)
        with self.assertRaises(EdgeCarrierError):
            ProfiniteProgram.projector(6)
        with self.assertRaises(EdgeCarrierError):
            ProfiniteProgram.integer(True)
        with self.assertRaises(EdgeCarrierError):
            ProfiniteProgram("bad-kind")
        with self.assertRaises(EdgeCarrierError):
            finite_prime_partition(0)

    def test_no_uniform_finite_view_identifies_all_integers(self):
        for horizon in (1,2,3,6,10,25,40):
            report=finite_clock_collision(horizon)
            a,b=report["distinct_source_integers"]
            self.assertEqual(a,0)
            self.assertNotEqual(a,b)
            self.assertTrue(all(b%n==a%n for n in range(1,horizon+1)))
            self.assertNotEqual(b%(b+1),0)
            self.assertTrue(report["all_declared_finite_modular_probes_match"])

    def test_edge_contracts_do_not_upgrade_embeddings_to_isomorphisms(self):
        contracts=carrier_interface_contract()
        self.assertEqual(len(contracts),8)
        self.assertEqual(contracts[0]["kind"],"GROUP_COMPLETION_ISOMORPHISM_ON_HOM")
        self.assertEqual(contracts[1]["kind"],"LOCALIZATION_RING_ISOMORPHISM")
        self.assertEqual(contracts[3]["Z_to_Zhat"],"proper dense embedding, NOT ring isomorphism")
        self.assertEqual(contracts[4]["kind"],"METRIC_COMPLETION_FIELD_ISOMORPHISM_CLASSICAL")
        self.assertEqual(contracts[5]["kind"],"LOCALIZATION_ADELIC_RING_ISOMORPHISM_CLASSICAL")
        self.assertEqual(contracts[6]["kind"],"REAL_FINITE_PLACE_PRODUCT_CARRIER_ISOMORPHISM_CLASSICAL")
        self.assertEqual(contracts[7]["kind"],"NOT_YET_EQUIVALENT_UNCOMPLETED")
        self.assertFalse(contracts[5]["all_global_points_have_finite_code"])


if __name__=="__main__":
    unittest.main()

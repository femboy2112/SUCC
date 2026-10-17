"""Exact group-lattice controls for the stronger profinite-index source route."""
import unittest
from fractions import Fraction as F
from observational_succ.profinite_index_genesis import CyclicObserver
from observational_succ.prime_jet_genesis import SourceError


class ProfiniteIndexTests(unittest.TestCase):
    def test_all_maximal_subgroups_derived_without_prime_oracle(self):
        self.assertEqual(CyclicObserver(210).maximal_indices(),(2,3,5,7))
        self.assertEqual(CyclicObserver(30).maximal_indices(),(2,3,5))
        self.assertEqual(CyclicObserver(64).maximal_indices(),(2,))

    def test_haar_measure_is_index_reciprocal(self):
        c=CyclicObserver(210)
        for p in (2,3,5,7):
            self.assertEqual(c.haar_mass(p),F(1,p))
            self.assertTrue(c.certify_clock(p,F(p)))

    def test_fake_composite_six_is_not_primitive(self):
        c=CyclicObserver(210)
        self.assertEqual(c.haar_mass(6),F(1,6))
        self.assertNotIn(6,c.maximal_indices())
        with self.assertRaises(SourceError):
            c.certify_clock(6,6)

    def test_global_power_gauge_killed_by_haar_index(self):
        c=CyclicObserver(210)
        with self.assertRaises(SourceError):
            c.certify_clock(2,4)
        with self.assertRaises(SourceError):
            c.certify_clock(3,F(9,2))

    def test_finite_cofinal_stage_recovers_small_prefix(self):
        c=CyclicObserver(210)
        atoms=c.reconstructed_atoms(10)
        self.assertEqual(atoms,{F(n):F(1) for n in range(1,11)})

    def test_missing_place_hidden_above_source_horizon(self):
        c=CyclicObserver(210)
        atoms=c.reconstructed_atoms(11)
        self.assertNotIn(F(11),atoms)
        self.assertIn(F(10),atoms)

    def test_pro_p_source_never_observes_other_primes(self):
        c=CyclicObserver(64)
        atoms=c.reconstructed_atoms(32)
        self.assertEqual(list(atoms),[F(1),F(2),F(4),F(8),F(16),F(32)])

    def test_unique_subgroup_of_composite_index_is_not_maximal(self):
        c=CyclicObserver(210)
        subgroup=c.subgroup_of_index(6)
        self.assertEqual(len(subgroup),35)
        self.assertTrue(subgroup < c.subgroup_of_index(2))
        self.assertTrue(subgroup < c.subgroup_of_index(3))

    def test_restricted_stage_loses_distinctions(self):
        c=CyclicObserver(30)
        self.assertNotIn(F(7),c.reconstructed_atoms(10))

    def test_type_and_source_gates(self):
        with self.assertRaises(SourceError): CyclicObserver(301)
        with self.assertRaises(SourceError): CyclicObserver(True)
        with self.assertRaises(SourceError): CyclicObserver(10).subgroup_of_index(7)
        with self.assertRaises(SourceError): CyclicObserver(210).certify_clock(2,2.0)


if __name__=='__main__':
    unittest.main()

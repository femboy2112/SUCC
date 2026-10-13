"""Lock the reproducibility receipt without using output as proof of theorem."""
import json
import unittest
from pathlib import Path
from observational_succ.relational_model_genetics import GeneticsError

class ReceiptTests(unittest.TestCase):
    def test_source_output_matches_saved_receipt(self):
        # A proper installed SUCC project contains both top-level scripts and research.
        # This test is also portable when run from a copied research directory.
        root=Path(__file__).resolve().parents[1]
        saved=root/'research/2026-10-12/GENETIC_MODEL_FUSION_RECEIPT.json'
        if not saved.exists():
            self.skipTest('Research receipt absent from copied source-only test tree')
        from observational_succ.relational_model_genetics import bridge_repair_demo
        from observational_succ.evolutionary_bridge_search import genetic_discovery_demo
        from observational_succ.source_coupling_bounds import combine_heuristic_marginals_demo
        from observational_succ.genetic_obstruction_holonomy import obstruction_language_demo
        # External CLI script may be executed separately; basic independent checks here.
        model=bridge_repair_demo()
        genetic=genetic_discovery_demo(5)
        coupling=combine_heuristic_marginals_demo()
        hol=obstruction_language_demo()
        doc=json.loads(saved.read_text())
        self.assertEqual(doc['generated_semantic_bridge'],model['bridge'])
        self.assertEqual(doc['genetic_grammar']['proposed_fitness'],genetic['heuristic_best_fitness'])
        self.assertEqual(doc['marginal_coupling']['possible_intersection_interval'],list(coupling['allowed_intersection']))
        self.assertEqual(doc['nonflat_connection']['holonomy'],hol['holonomy'])
        self.assertFalse(doc['scope']['RH_or_Weil_positivity_proved'])
        self.assertFalse(doc['scope']['physical_source_authenticated'])

if __name__=='__main__': unittest.main()

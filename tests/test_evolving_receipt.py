"""Receipt determinism and Lean table-to-learner binding (not Lean proof claims)."""
from pathlib import Path
import json
import re
import subprocess
import sys
import unittest
from observational_succ.obstruction_discovery_lab import hidden_carrier
from observational_succ.evolving_observer_categories import discover_representation

ROOT = Path(__file__).resolve().parents[1]

class EvolvingReceiptTests(unittest.TestCase):
    def test_fresh_probe_matches_checked_in_receipt(self):
        result = subprocess.run([sys.executable, str(ROOT/'scripts/evolutionary_obstruction_probe.py')],
                                capture_output=True, text=True, check=True, timeout=60)
        self.assertEqual(json.loads(result.stdout), json.loads((ROOT/'research/2026-10-13/EVOLUTIONARY_OBSTRUCTION_RECEIPT.json').read_text()))

    def test_formal_instance_tables_bind_actual_discovery(self):
        src, _ = hidden_carrier(3,271828)
        q=discover_representation(src)
        text=(ROOT/'formal/obstruction_synthesis/DiscoveredInstance.lean').read_text()
        self.assertIn(src.digest,text)
        arrays={name:tuple(int(x.strip()) for x in body.split(','))
                for name,body in re.findall(r'def (\w+)Table : List \(Fin \d+\) := \[([^\]]+)\]',text)}
        self.assertEqual(arrays['project'],q.labels)
        self.assertEqual(arrays['sourceA'],src.actions[0].after)
        self.assertEqual(arrays['sourceB'],src.actions[1].after)
        self.assertEqual(arrays['sourceR'],src.readouts[0].values)
        self.assertEqual(arrays['a'],q.actions[0].after)
        self.assertEqual(arrays['b'],q.actions[1].after)
        self.assertEqual(arrays['r'],q.readouts[0].values)

    def test_holdout_design_and_scope_not_silently_expanded(self):
        spec=json.loads((ROOT/'research/2026-10-13/DISCOVERY_PRECOMMIT.json').read_text())
        self.assertEqual(spec['calibration']['prime'],3)
        self.assertEqual(spec['heldout'],[{'prime':5,'label_seed':314159},{'prime':7,'label_seed':161803}])
        self.assertFalse(spec['calibration']['allow_target_coordinates_to_learner'])
        receipt=json.loads((ROOT/'research/2026-10-13/EVOLUTIONARY_OBSTRUCTION_RECEIPT.json').read_text())
        self.assertFalse(receipt['unrestricted_grammar_invention'])
        self.assertFalse(receipt['python_algorithm_formally_refined_to_lean'])
        self.assertEqual(receipt['old_genetic_failed_seeds'],[0,11,13])

if __name__=='__main__': unittest.main()

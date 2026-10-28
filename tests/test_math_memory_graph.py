"""Hostile mutations of the curator graph, without modifying global history."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from verify_math_memory_graph import validate

class MathMemoryGraphTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
    cls.raw=json.loads((ROOT/"docs/math_memory/RELATION_GRAPH.json").read_text(encoding="utf-8"))

 def test_original_passes(self):self.assertEqual(validate(self.raw),[])

 def test_no_mistaken_theorem_status(self):
    g=copy.deepcopy(self.raw)
    g['nodes'][0]['status']='PROVED MAGICALLY'
    self.assertTrue(any('unknown status' in x for x in validate(g)))

 def test_missing_source_pin_detected(self):
    g=copy.deepcopy(self.raw)
    g['nodes'][0]['provenance']=[]
    self.assertTrue(any('empty provenance' in x for x in validate(g)))

 def test_unresolved_node_link_detected(self):
    g=copy.deepcopy(self.raw)
    g['edges'].append({'source':'MM-T-002','target':'MISSING','relation':'depends_on','evidence':'mutation'})
    self.assertTrue(any('unknown endpoint' in x for x in validate(g)))

 def test_logical_dependency_cycle_detected(self):
    g=copy.deepcopy(self.raw)
    g['edges'].append({'source':'MM-T-005','target':'MM-T-006','relation':'depends_on','evidence':'mutation'})
    self.assertTrue(any('cyclic depends_on' in x for x in validate(g)))

if __name__=='__main__':unittest.main()

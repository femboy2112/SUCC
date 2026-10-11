"""Hostile exact operational distinguishability and semantic information loss."""
import unittest
from fractions import Fraction as Q

from observational_succ.operational_semantics import (
    SemanticChannelError, Evidence, SemanticReadout, total_variation,
    data_processing, qubit_outcome_evidence, measurement_semantic_probe
)
from observational_succ.quantum_records import INITIAL_ZERO, measure_x, measure_z


class SemanticDataProcessingTests(unittest.TestCase):
    def setUp(self):
        self.labels=("a","b")
        self.a=Evidence(self.labels,(Q(1),Q(0)))
        self.b=Evidence(self.labels,(Q(0),Q(1)))

    def test_identity_preserves_exact_distinguishability(self):
        c=data_processing(self.a,self.b,SemanticReadout.identity(self.labels))
        self.assertEqual(c.before,1)
        self.assertEqual(c.after,1)
        self.assertEqual(c.slack,0)
        self.assertTrue(c.theorem_proved_from_channel_axioms)

    def test_complete_forgetting_loses_but_never_rewrites_source(self):
        forget=SemanticReadout(self.labels,("same",),((Q(1),),(Q(1),)))
        c=data_processing(self.a,self.b,forget)
        self.assertEqual(c.before,1)
        self.assertEqual(c.after,0)
        self.assertEqual(c.slack,1)
        self.assertTrue(c.source_distinct)
        self.assertFalse(c.readout_distinct)
        self.assertEqual(self.a.weights,(Q(1),Q(0)))
        self.assertEqual(self.b.weights,(Q(0),Q(1)))

    def test_exact_noisy_channel_and_composition(self):
        p=Q(3,4);q=Q(1,4)
        noisy=SemanticReadout(self.labels,("up","down"),((p,q),(q,p)))
        c=data_processing(self.a,self.b,noisy)
        self.assertEqual(c.after,Q(1,2))
        self.assertEqual(c.slack,Q(1,2))
        erase=SemanticReadout(("up","down"),("label",),((Q(1),),(Q(1),)))
        after=noisy.then(erase)
        self.assertEqual(total_variation(after.pushforward(self.a),
                                         after.pushforward(self.b)),0)
        self.assertEqual(after.pushforward(self.a),
                         erase.pushforward(noisy.pushforward(self.a)))
        with self.assertRaises(SemanticChannelError):
            erase.then(noisy)

    def test_exact_real_qubit_Z_X_observational_difference(self):
        initial_one=((Q(0),Q(0)),(Q(0),Q(1)))
        z0=qubit_outcome_evidence(measure_z(),INITIAL_ZERO)
        z1=qubit_outcome_evidence(measure_z(),initial_one)
        x0=qubit_outcome_evidence(measure_x(),INITIAL_ZERO)
        x1=qubit_outcome_evidence(measure_x(),initial_one)
        self.assertEqual(total_variation(z0,z1),1)
        self.assertEqual(total_variation(x0,x1),0)
        report=measurement_semantic_probe()
        self.assertEqual(report["status"],"EXACT_SEMANTIC_DATA_PROCESSING")
        self.assertEqual(report["Z_outcomes_0_vs_1_TV"],"1")
        self.assertEqual(report["X_outcomes_0_vs_1_TV"],"0")
        self.assertEqual(report["Z_forgotten_TV"],"0")
        self.assertFalse(report["Weil_positivity_claimed"])
        self.assertFalse(report["source_causal_records_erased"])

    def test_refuse_incompatible_or_illegitimate_readouts(self):
        with self.assertRaises(SemanticChannelError):
            Evidence(("a","b"),(0.5,0.5))
        with self.assertRaises(SemanticChannelError):
            Evidence(("a","a"),(Q(1,2),Q(1,2)))
        with self.assertRaises(SemanticChannelError):
            Evidence(("a","b"),(Q(2),Q(-1)))
        with self.assertRaises(SemanticChannelError):
            SemanticReadout(self.labels,("x","y"),((Q(1),Q(0)),(Q(1),Q(1))))
        with self.assertRaises(SemanticChannelError):
            SemanticReadout(self.labels,("x",),((Q(1),),(Q(-1),)))
        with self.assertRaises(SemanticChannelError):
            data_processing(self.a, Evidence(("a","c"),(Q(1),Q(0))),
                            SemanticReadout.identity(self.labels))
        with self.assertRaises(SemanticChannelError):
            SemanticReadout.identity(("a","a"))
        with self.assertRaises(SemanticChannelError):
            Evidence.from_counts(("a","b"),(0,0))
        with self.assertRaises(SemanticChannelError):
            qubit_outcome_evidence("not an instrument",INITIAL_ZERO)


if __name__=="__main__":
    unittest.main()

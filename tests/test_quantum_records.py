"""Exact physical-carrier experiment independent of RH and human cognition."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q

from observational_succ.quantum_records import (
    QuantumRecordError, QuantumObserver, Instrument, Observation,
    INITIAL_ZERO, INITIAL_PLUS, measure_x, measure_z,
    causal_noncommutativity_probe,
)


class RationalQuantumHistoryTests(unittest.TestCase):
    def test_instruments_are_genuine_exact_complete_positive_measurements(self):
        z,x=measure_z(),measure_x()
        self.assertEqual(z.probabilities(INITIAL_ZERO),{"zero":Q(1),"one":Q(0)})
        self.assertEqual(x.probabilities(INITIAL_ZERO),{"plus":Q(1,2),"minus":Q(1,2)})
        self.assertEqual(z.probabilities(INITIAL_PLUS),{"zero":Q(1,2),"one":Q(1,2)})
        p,rho=x.event(INITIAL_ZERO,"plus")
        self.assertEqual(p,Q(1,2))
        self.assertEqual(rho,INITIAL_PLUS)
        with self.assertRaises(QuantumRecordError):
            z.event(INITIAL_ZERO,"one")

    def test_order_sensitive_observations_are_append_only_and_replayable(self):
        z,x=measure_z(),measure_x()
        original=QuantumObserver.initial_state()
        a=original.advance(x,"plus")
        b=a.advance(z,"zero")
        c=original.advance(z,"zero").advance(x,"plus")
        self.assertEqual(original.records,())
        self.assertEqual(original.state,INITIAL_ZERO)
        self.assertEqual(a.state,INITIAL_PLUS)
        self.assertEqual(a.joint_probability,Q(1,2))
        self.assertEqual(b.joint_probability,Q(1,4))
        self.assertEqual(c.joint_probability,Q(1,2))
        self.assertNotEqual(b.records,c.records)
        self.assertNotEqual(b.head,c.head)
        self.assertEqual(b.records[0],a.records[0])
        self.assertEqual(len(b.records),2)
        self.assertEqual(b.records[1].previous_head,b.records[0].head)
        self.assertEqual(len(b.records[-1].head),64)
        self.assertTrue(b.verify({"X":x,"Z":z}))
        self.assertTrue(c.verify({"X":x,"Z":z}))
        self.assertEqual(causal_noncommutativity_probe()["x_then_z_joint"],"1/4")
        self.assertEqual(causal_noncommutativity_probe()["z_then_x_joint"],"1/2")
        self.assertFalse(causal_noncommutativity_probe()["Weil_positivity_claimed"])

    def test_invalid_states_cannot_be_declared_quantum(self):
        with self.assertRaises(QuantumRecordError):
            QuantumObserver.initial_state(((Q(1),Q(2)),(Q(2),Q(0))))
        with self.assertRaises(QuantumRecordError):
            QuantumObserver.initial_state(((Q(1,2),Q(1,3)),(Q(0),Q(1,2))))
        with self.assertRaises(QuantumRecordError):
            QuantumObserver.initial_state(((Q(1),Q(0)),(Q(0),Q(1))))
        with self.assertRaises(QuantumRecordError):
            QuantumObserver.initial_state(((1.0,0),(0,0)))

    def test_noncomplete_instruments_and_duplicate_outcomes_are_rejected(self):
        with self.assertRaises(QuantumRecordError):
            Instrument("Broken",(("zero",((1,0),(0,0))),))
        with self.assertRaises(QuantumRecordError):
            Instrument("Broken",(("zero",((1,0),(0,0))),
                                 ("zero",((0,0),(0,1)))))
        with self.assertRaises(QuantumRecordError):
            Instrument("Broken!",(("zero",((1,0),(0,0))),
                                  ("one",((0,0),(0,1)))))
        with self.assertRaises(QuantumRecordError):
            Instrument("Broken",(("zero",((1.0,0),(0,0))),
                                 ("one",((0,0),(0,1)))))

    def test_history_integrity_is_replay_checked_not_authentication(self):
        z,x=measure_z(),measure_x()
        recorded=QuantumObserver.initial_state().advance(x,"plus").advance(z,"zero")
        self.assertTrue(recorded.verify({"Z":z,"X":x}))
        bad_record=replace(recorded.records[1],conditional_probability=Q(1,3))
        forged=replace(recorded,records=(recorded.records[0],bad_record))
        with self.assertRaises(QuantumRecordError):
            forged.verify({"Z":z,"X":x})
        with self.assertRaises(QuantumRecordError):
            recorded.verify({"X":x})
        with self.assertRaises(QuantumRecordError):
            replace(recorded,joint_probability=Q(2)).verify({"Z":z,"X":x})
        # A cryptographic digest can detect accidental changes if anchored,
        # but a malicious actor can rewrite both data and digest.
        self.assertEqual(len(recorded.head),64)


if __name__=="__main__":
    unittest.main()

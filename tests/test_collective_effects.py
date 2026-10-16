import dataclasses
import unittest

from observational_succ.collective_effects import (
    AnalyticImport, Context, Derive, EffectError, Event, ExactQuadratic, Kind,
    MacroState, Predict, Relay, Replay, miniature_action, run,
)
from observational_succ.source_lambda import (
    AccessGap, App, Atlas, BOOL, Bool, Eq, Forget, Join, Lam, Passport,
    Read, Residue, Select,
)
from observational_succ.consensus_lambda import MiniPort
from observational_succ.miniature_carrier import Carrier, Mini, MiniatureContractError


P = Passport("collective-effects-fixture", 4)


def context():
    return Context(P, (Event("a2", "A", P, 2, 1), Event("b3", "B", P, 3, 2)))


def mini_port(unsafe=False):
    states = ("0", "1")
    parent = Carrier(states, {"flip": {"0": "1", "1": None if unsafe else "0"}},
                     {"0": "zero", "1": "one"}, states, P.source_id)
    mini = Mini(states, {"step": {"0": "1", "1": "0"}},
                {"0": "zero", "1": "one"}, "0", P.source_id)
    return MiniPort("toggle", parent, mini, {s: s for s in states},
                    {"step": ("flip",)}, {"zero": "zero", "one": "one"})


class CollectiveEffectTests(unittest.TestCase):
    def test_complementary_records_require_real_communication(self):
        program = (Replay("a2", "A"), Replay("b3", "B"), Relay(1, "B", "A"),
                   Derive(Join(Read(2), Read(3)), (0, 2), "A"))
        result = run(program, context())
        report = result.artifacts[-1]
        self.assertEqual((report.value.modulus, report.value.value), (6, 5))
        self.assertEqual(report.origins, frozenset(("a2", "b3")))
        self.assertEqual(report.passport, P)
        self.assertEqual(report.kind, Kind.DERIVED)
        self.assertEqual(result.new_physical_measurements, 0)
        self.assertFalse(result.original_source_authenticated)
        with self.assertRaises(EffectError):
            run(program[:2] + (Derive(Join(Read(2), Read(3)), (0, 1), "A"),), context())

    def test_repeated_replay_never_creates_independence(self):
        result = run((Replay("a2", "A"),) * 8, context())
        self.assertEqual(result.referenced_origins, frozenset(("a2",)))
        self.assertEqual(dict(result.grade)[Kind.RECORDED.value], 8)
        self.assertEqual(result.new_physical_measurements, 0)

    def test_transitive_relay_preserves_one_origin(self):
        result = run((Replay("a2", "A"), Relay(0, "A", "B"), Relay(1, "B", "C")), context())
        self.assertEqual(result.artifacts[-1].origins, frozenset(("a2",)))
        self.assertEqual(result.artifacts[-1].parents, (1,))
        self.assertEqual(result.artifacts[-1].kind, Kind.TESTIMONY)

    def test_no_recipient_can_claim_local_read(self):
        with self.assertRaises(EffectError):
            run((Replay("a2", "B"),), context())
        with self.assertRaises(EffectError):
            run((Replay("a2", "A"), Relay(0, "B", "C")), context())

    def test_absent_record_and_future_reference(self):
        with self.assertRaises(AccessGap):
            run((Replay("missing", "A"),), context())
        with self.assertRaises(EffectError):
            run((Relay(0, "A", "B"),), context())

    def test_foreign_source_epoch_and_basis(self):
        for q in (Passport("other", 4), Passport(P.source_id, 5), Passport(P.source_id, 4, "other")):
            c = Context(P, (Event("foreign", "A", q, 2, 0),))
            with self.assertRaises(EffectError):
                run((Replay("foreign", "A"),), c)

    def test_conflicting_event_identity(self):
        with self.assertRaises(EffectError):
            Context(P, (Event("same", "A", P, 2, 0), Event("same", "A", P, 2, 1)))

    def test_inconsistent_frozen_history(self):
        with self.assertRaises((EffectError, ValueError)):
            Context(P, (Event("a", "A", P, 2, 0), Event("b", "B", P, 4, 1)))

    def test_mutually_exclusive_histories(self):
        c = Context(P, (Event("left", "A", P, 2, 1, ("left",)),
                        Event("right", "A", P, 3, 2, ("right",))), ("left",))
        self.assertEqual(run((Replay("left", "A"),), c).artifacts[0].kind, Kind.RECORDED)
        with self.assertRaises(AccessGap):
            run((Replay("left", "A"), Replay("right", "A")), c)

    def test_prefix_compatible_chronology(self):
        c = Context(P, (Event("a", "A", P, 2, 1, ("first",)),
                        Event("b", "A", P, 3, 2, ("first", "second"))), ("first", "second"))
        out = run((Replay("a", "A"), Replay("b", "A"),
                   Derive(Join(Read(2), Read(3)), (0, 1), "A")), c)
        self.assertEqual(out.artifacts[-1].value.value, 5)

    def test_crt_result_does_not_mint_mod6_record(self):
        prefix = (Replay("a2", "A"), Replay("b3", "B"), Relay(1, "B", "A"),
                  Derive(Join(Read(2), Read(3)), (0, 2), "A"))
        with self.assertRaises(AccessGap):
            run(prefix + (Derive(Read(6), (3,), "A"),), context())

    def test_compressed_provenance_is_not_hidden_decoder(self):
        term = Eq(Forget(Read(3)), Residue(3, 0))
        prefix = (Replay("b3", "B"), Derive(term, (0,), "B"), Relay(1, "B", "A"))
        out = run(prefix, context())
        self.assertEqual(out.artifacts[-1].origins, frozenset(("b3",)))
        self.assertFalse(out.artifacts[-1].value)
        self.assertFalse(out.artifacts[-1].readable_events)
        with self.assertRaises(AccessGap):
            run(prefix + (Derive(Read(3), (2,), "A"),), context())

    def test_latent_effect_is_not_an_executed_read(self):
        term = Lam(BOOL, Read(7))
        out = run((Derive(term, (), "A"),), context())
        self.assertEqual(out.artifacts[0].kind, Kind.PROGRAM)
        self.assertFalse(out.referenced_origins)
        with self.assertRaises(EffectError):
            run((Derive(term, (), "A"), Relay(0, "A", "B")), context())
        with self.assertRaises(AccessGap):
            run((Derive(App(term, Bool(True)), (), "A"),), context())

    def test_lazy_branch_unperformed_read_stays_unperformed(self):
        term = Select(Bool(True), Read(2), Read(2))
        result = run((Replay("a2", "A"), Derive(term, (0,), "A")), context())
        self.assertEqual(result.artifacts[-1].origins, frozenset(("a2",)))

    def test_counterfactual_cannot_be_relayed_as_testimony(self):
        prediction = Predict(Read(7), Atlas.from_integer(P, 12, (7,)), "A")
        out = run((prediction,), context())
        self.assertEqual(out.artifacts[0].kind, Kind.PREDICTED)
        self.assertFalse(out.referenced_origins)
        with self.assertRaises(EffectError):
            run((prediction, Relay(0, "A", "B")), context())
        with self.assertRaises(EffectError):
            run((prediction, Derive(Read(7), (0,), "A")), context())

    def test_analytic_debts_survive_transitive_import_and_finite_check(self):
        program = (AnalyticImport("conditional source estimate", ("OPEN_SPECTRAL_TAIL",)),
                   AnalyticImport("derived consequence", (), (0,)),
                   ExactQuadratic(((1, 2), (2, 1)), (1, -1), (1,)))
        out = run(program, context())
        self.assertIn("OPEN_SPECTRAL_TAIL", out.artifacts[-1].obligations)
        self.assertIn("SOURCE_TO_THEOREM_IDENTIFICATION", out.artifacts[-1].obligations)
        self.assertEqual(out.artifacts[-1].kind, Kind.EXACT)
        self.assertFalse(out.global_theorem_proved)

    def test_forged_artifact_is_not_an_instruction(self):
        artifact = run((Replay("a2", "A"),), context()).artifacts[0]
        with self.assertRaises(EffectError):
            run((dataclasses.replace(artifact, origins=frozenset(("invented",))),), context())

    def test_miniature_action_consumes_capability_and_changes_epoch(self):
        state = MacroState(P, P, frozenset(("0", "1")), frozenset(("token",)))
        nxt, receipt = miniature_action(state, mini_port(), "step", "token")
        self.assertEqual(nxt.original, P)
        self.assertEqual(nxt.current.epoch, P.epoch + 1)
        self.assertEqual(nxt.history, ("flip",))
        self.assertFalse(nxt.capabilities)
        self.assertFalse(receipt["physical_action_executed"])
        with self.assertRaises(AccessGap):
            miniature_action(nxt, mini_port(), "step", "token")
        with self.assertRaises(EffectError):
            run((Replay("a2", "A"),), Context(nxt.current, context().events, nxt.history))

    def test_unsafe_or_unavailable_miniature_macro_rejected(self):
        state = MacroState(P, P, frozenset(("0", "1")), frozenset(("token",)))
        with self.assertRaises((EffectError, ValueError, MiniatureContractError)):
            miniature_action(state, mini_port(True), "step", "token")
        with self.assertRaises(EffectError):
            miniature_action(state, mini_port(), "nonexistent", "token")


if __name__ == "__main__":
    unittest.main()

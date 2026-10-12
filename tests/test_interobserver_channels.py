"""Independent exhaustive small-graph controls for finite zero-error channels."""
from itertools import product
import unittest

from observational_succ.interobserver_channels import (
    ExactChannel, InterobserverWorld, ZeroErrorChannelError,
    exact_minimum_channel, chromatic_channel_demo,
)


def brute_chromatic_number(alphabet, edges):
    positions = {v: i for i, v in enumerate(alphabet)}
    for ncolors in range(1, len(alphabet) + 1):
        for assignment in product(range(ncolors), repeat=len(alphabet)):
            if all(assignment[positions[a]] != assignment[positions[b]]
                   for a, b in edges):
                return ncolors
    raise AssertionError("Every finite graph has a proper vertex coloring")


class InterobserverChannelTests(unittest.TestCase):
    def test_path_graph_gives_real_message_savings(self):
        w = InterobserverWorld(
            ("A_at_ab", "B_at_ab", "B_at_bc", "C_at_bc"),
            ("A", "B", "B", "C"),
            ("ab", "ab", "bc", "bc"),
            ("A", "B", "B", "C"),
        )
        ch = exact_minimum_channel(w)
        self.assertEqual(ch.codewords, 2)
        self.assertEqual(ch.fixed_width_bits, 1)
        self.assertEqual(ch.confusability_edges, (("A", "B"), ("B", "C")))
        self.assertEqual(ch.encode("A"), ch.encode("C"))
        self.assertNotEqual(ch.encode("A"), ch.encode("B"))
        for s,v,t in zip(w.sender_views,w.receiver_views,w.targets):
            self.assertEqual(ch.decode(ch.encode(s),v),t)
        self.assertTrue(ch.exhaustive_minimum_proved)
        with self.assertRaises(ZeroErrorChannelError):
            ch.decode(7,"unknown")

    def test_receiver_already_knows_target_no_bits_needed(self):
        w = InterobserverWorld(("A","B"),("a","b"),("a","b"),("a","b"))
        code = exact_minimum_channel(w)
        self.assertEqual(code.codewords, 1)
        self.assertEqual(code.fixed_width_bits, 0)
        self.assertEqual(code.decode(0,"a"),"a")
        self.assertEqual(code.decode(0,"b"),"b")

    def test_no_side_information_must_send_unique_target(self):
        w = InterobserverWorld(("A","B","C"),("a","b","c"),
                               ("same","same","same"),("A","B","C"))
        ch = exact_minimum_channel(w)
        self.assertEqual(ch.codewords, 3)
        self.assertEqual(ch.fixed_width_bits, 2)
        self.assertEqual(len(ch.confusability_edges), 3)

    def test_impossible_even_with_unbounded_messages_when_sender_is_blind(self):
        w = InterobserverWorld(("A","B"),("same","same"),
                               ("same","same"),("A","B"))
        self.assertEqual(w.feasibility_conflicts(),(("same","same"),))
        with self.assertRaises(ZeroErrorChannelError):
            exact_minimum_channel(w)

    def test_five_cycle_reduces_three_bit_identity_to_two_bit_message(self):
        ids = tuple("ABCDE")
        sources, senders, sides, targets = [], [], [], []
        for i in range(5):
            pair = ids[i]+ids[(i+1)%5]
            for who in (ids[i], ids[(i+1)%5]):
                sources.append(f"{pair}_{who}")
                senders.append(who)
                sides.append(pair)
                targets.append(who)
        world = InterobserverWorld(tuple(sources),tuple(senders),
                                   tuple(sides),tuple(targets))
        self.assertEqual(len(world.edges()),5)
        code=exact_minimum_channel(world)
        self.assertEqual(code.codewords,3)
        self.assertEqual(code.fixed_width_bits,2)
        self.assertEqual((len(ids)-1).bit_length(),3)
        self.assertEqual(code.codewords,
                         brute_chromatic_number(code.sender_alphabet,code.confusability_edges))

    def test_independent_exhaustive_three_source_binary_controls(self):
        # 2^3 receiver-view patterns × 2^3 target patterns = 64 world tables.
        # Distinct sender views mean no same-(sender,side) internal conflict.
        trials=0
        for receiver in product(("r0","r1"), repeat=3):
            for target in product(("zero","one"), repeat=3):
                w=InterobserverWorld(("A","B","C"),("a","b","c"),
                                      receiver,target)
                ref=brute_chromatic_number(w.sender_alphabet(),w.edges())
                c=exact_minimum_channel(w)
                self.assertEqual(c.codewords,ref)
                self.assertEqual(c.fixed_width_bits,(ref-1).bit_length())
                for v,s,t in zip(w.receiver_views,w.sender_views,w.targets):
                    self.assertEqual(c.decode(c.encode(s),v),t)
                trials+=1
        self.assertEqual(trials,64)

    def test_invalid_tables_and_demo_claim_boundaries(self):
        with self.assertRaises(ZeroErrorChannelError):
            InterobserverWorld(("A","B"),("a",),("x","x"),("a","b"))
        with self.assertRaises(ZeroErrorChannelError):
            InterobserverWorld(("A","A"),("a","b"),("x","x"),("a","b"))
        with self.assertRaises(ZeroErrorChannelError):
            exact_minimum_channel("nonworld")
        result=chromatic_channel_demo()
        self.assertEqual(result["status"],"EXACT_INTEROBSERVER_ZERO_ERROR_CHANNEL")
        self.assertEqual(result["minimum_fixed_width_bits"],1)
        self.assertEqual(result["naive_sender_id_fixed_width_bits"],2)
        self.assertFalse(result["optimal_variable_length_bits_claimed"])
        self.assertFalse(result["physical_source_authentication_claimed"])


if __name__=="__main__":
    unittest.main()

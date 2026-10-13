"""Finite model/certificate controls; these do not establish actual ontology."""
import unittest
from itertools import product
from observational_succ.carrier_observational_frontier import (
    ControlledCarrier, FrontierError, ontology_alias_model,
    destructive_parity_model,
)


class CarrierFrontierTests(unittest.TestCase):
    def test_permanent_alias_indistinguishable_for_every_word(self):
        m, claim = ontology_alias_model()
        self.assertEqual(m.classes(), (("inside", "outside"),))
        self.assertEqual(m.claim_quotient(claim)["status"], "PERMANENTLY_DARK_UNDER_ACTIONS")
        self.assertEqual(m.adaptive_original_claim(claim)["status"],"NO_UNIFORM_FINITE_POLICY")
        self.assertEqual(m.separating_word("inside", "outside"),None)
        for length in range(5):
            for word in product(m.actions,repeat=length):
                self.assertEqual(m.trace("inside",word),m.trace("outside",word))

    def test_expanding_allowed_instruments_breaks_ontological_alias(self):
        m, claim=ontology_alias_model(allow_separator=True)
        self.assertEqual(len(m.classes()),2)
        self.assertEqual(m.separating_word("inside","outside"),("SEPARATOR",))
        self.assertEqual(m.claim_quotient(claim)["status"],"BEHAVIORALLY_FACTORABLE_ONLY")
        r=m.adaptive_original_claim(claim)
        self.assertEqual(r["status"],"FINITE_WINNING_POLICY")
        self.assertEqual(r["rank"],1)
        self.assertEqual(r["root_action"],"SEPARATOR")

    def test_destructive_parity_refutes_quotient_implies_strategy(self):
        m, claims=destructive_parity_model()
        self.assertEqual(len(m.classes()),4)
        self.assertEqual(m.claim_quotient(claims)["status"],"BEHAVIORALLY_FACTORABLE_ONLY")
        self.assertEqual(m.adaptive_original_claim(claims)["status"],"NO_UNIFORM_FINITE_POLICY")
        for x,y in product(m.states, repeat=2):
            if claims[x]!=claims[y]:
                word=m.separating_word(x,y)
                self.assertIsNotNone(word)
                self.assertNotEqual(m.trace(x,word),m.trace(y,word))
        # First bit read irreversibly erases second source bit.
        self.assertEqual(m.step((0,0),"READ_A"),m.step((0,1),"READ_A"))
        self.assertEqual(m.step((0,0),"READ_B"),m.step((1,0),"READ_B"))

    def test_claim_constant_is_proved_without_a_physical_action(self):
        m, _=ontology_alias_model()
        r=m.adaptive_original_claim({"inside":1,"outside":1})
        self.assertEqual(r["rank"],0)
        self.assertIsNone(r["root_action"])

    def test_non_destructive_two_bit_read_requires_two_queries(self):
        states=tuple((a,b) for a,b in product(range(2),repeat=2))
        transitions={(s,act):(s[0] if act=="A" else s[1],s)
                     for s in states for act in ("A","B")}
        m=ControlledCarrier("true two bit source",states,("A","B"),transitions)
        report=m.adaptive_original_claim({s:s[0]^s[1] for s in states})
        self.assertEqual(report["status"],"FINITE_WINNING_POLICY")
        self.assertEqual(report["rank"],2)

    def test_minimal_distinguishing_words_against_exhaustive_oracle(self):
        for bits in product((0,1),repeat=8):
            # Two states, two actions; 8 independent transition bits encode
            # outputs/next-state of every state/action pair.
            cells=[(0,"a"),(0,"b"),(1,"a"),(1,"b")]
            transitions={k:(bits[2*i],bits[2*i+1]) for i,k in enumerate(cells)}
            m=ControlledCarrier("complete two-state machine",(0,1),("a","b"),transitions)
            word=m.separating_word(0,1)
            brute=next((w for n in range(1,4)
                         for w in product(m.actions,repeat=n)
                         if m.trace(0,w)!=m.trace(1,w)),None)
            self.assertEqual(word,brute)
            self.assertEqual(word is None,len(m.classes())==1)
            self.assertLessEqual(len(m.partitions()),2)

    def test_three_state_delay_then_distinguish(self):
        # Need a two-step word, despite identical first reports.
        states=(0,1,2,3)
        transitions={(s,a):(0, {0:2,1:3,2:2,3:3}[s] if a=="PREP" else s)
                     for s in states for a in ("PREP","READ")}
        for s in states:
            transitions[(s,"READ")]=(int(s==3),s)
        m=ControlledCarrier("delayed",states,("PREP","READ"),transitions)
        self.assertEqual(m.separating_word(0,1),("PREP","READ"))
        self.assertEqual(m.trace(0,("READ",)),m.trace(1,("READ",)))

    def test_minimal_mealy_quotient_retains_all_future_paths(self):
        m,_=ontology_alias_model()
        q=m.minimal_behavior_quotient()
        self.assertEqual(q['minimum_behavior_state_count'],1)
        for length in range(7):
            for word in product(m.actions,repeat=length):
                self.assertEqual(m.trace('inside',word),q['quotient'].trace(0,word))
                self.assertEqual(m.trace('outside',word),q['quotient'].trace(0,word))
        self.assertFalse(q['source_ontology_identified'])

    def test_minimal_mealy_quotient_exhaustive_small_machines(self):
        from random import Random
        rng=Random(20261012)
        for _ in range(500):
            states=(0,1,2)
            actions=('a','b')
            transitions={(x,act):(rng.randrange(2),rng.randrange(3))
                         for x in states for act in actions}
            m=ControlledCarrier('seeded-small',states,actions,transitions)
            q=m.minimal_behavior_quotient()
            where=dict(q['source_to_observable_state'])
            for x,y in product(states,repeat=2):
                oracle=all(m.trace(x,w)==m.trace(y,w) for depth in range(4)
                           for w in product(actions,repeat=depth))
                self.assertEqual(oracle,where[x]==where[y])
            for x in states:
                for depth in range(4):
                    for w in product(actions,repeat=depth):
                        self.assertEqual(m.trace(x,w),q['quotient'].trace(where[x],w))

    def test_reject_incomplete_or_forged_actions(self):
        with self.assertRaises(FrontierError):
            ControlledCarrier("x",(0,1),("x",),{(0,"x"):(0,0)})
        with self.assertRaises(FrontierError):
            ControlledCarrier("x",(0,1),("x",),{(0,"x"):(0,0),(1,"x"):(0,9)})
        m,_=ontology_alias_model()
        with self.assertRaises(FrontierError):
            m.claim_quotient({"inside":0})
        m,_=ontology_alias_model(allow_separator=True)
        with self.assertRaisesRegex(FrontierError,"Resource budget"):
            m.adaptive_original_claim({"inside":0,"outside":1},max_beliefs=1)

    def test_original_source_not_replaced_by_current_carrier_claim(self):
        m,original_parity=destructive_parity_model()
        # Reading a bit yields a new state with one erased bit, but the
        # original source truth is still parity of the ORIGINAL pair.
        b=m.step((1,1),"READ_A")[1]
        self.assertNotEqual(original_parity[(1,1)],b[0]^b[1])
        self.assertEqual(m.adaptive_original_claim(original_parity)["rank"],None)


if __name__=="__main__": unittest.main()

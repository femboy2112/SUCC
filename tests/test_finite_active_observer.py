import unittest
from itertools import product
from observational_succ.finite_active_observer import FiniteInstrument, ProbeContractError


def machine(kind):
    states=("source0","source1","reset")
    actions=("passive","interrogate")
    table={}
    for s in states:
        table[s,"passive"]=("null",s)
        if kind == "invasive":
            table[s,"interrogate"]=("0" if s=="source0" else "1" if s=="source1" else "r", "reset")
        elif kind == "qnd":
            table[s,"interrogate"]=("0" if s=="source0" else "1" if s=="source1" else "r",s)
        elif kind == "invisible":
            table[s,"interrogate"]=("null",s)
    return FiniteInstrument(states,actions,table)


class FiniteActiveTests(unittest.TestCase):
    def test_no_port_closure(self):
        m=machine("invisible")
        self.assertEqual(m.observational_classes(),(("source0","source1","reset"),))
        self.assertIsNone(m.shortest_separator("source0","source1"))

    def test_passive_invisible_active_measured(self):
        m=machine("invasive")
        self.assertEqual(m.observational_classes(("passive",)),(("source0","source1","reset"),))
        self.assertIsNone(m.shortest_separator("source0","source1",("passive",)))
        self.assertEqual(m.shortest_separator("source0","source1"),("interrogate",))
        r=m.separator_receipt("source0","source1")
        self.assertEqual(r["last_outputs"],("0","1"))
        self.assertTrue(r["left_changed"])
        self.assertTrue(r["right_changed"])
        self.assertEqual(m.trace("source0",("interrogate",)),(("0",),"reset"))
        self.assertEqual(m.trace("source1",("interrogate",)),(("1",),"reset"))

    def test_qnd_countermodel(self):
        m=machine("qnd")
        r=m.separator_receipt("source0","source1")
        self.assertTrue(r["separable"])
        self.assertFalse(r["left_changed"])
        self.assertFalse(r["right_changed"])

    def test_two_step_diagnosis(self):
        states=("a","b","c")
        tab={
            ("a","look"):("same","a"),
            ("b","look"):("same","c"),
            ("c","look"):("different","c"),
        }
        m=FiniteInstrument(states,("look",),tab)
        self.assertEqual(m.shortest_separator("a","b"),("look","look"))
        self.assertEqual(m.trace("a",("look","look"))[0],("same","same"))
        self.assertEqual(m.trace("b",("look","look"))[0],("same","different"))

    def test_empty_active_toolkit(self):
        m=machine("invasive")
        self.assertIsNone(m.shortest_separator("source0","source1",()))
        self.assertEqual(m.observational_classes(()),(("source0","source1","reset"),))

    def test_nonempty_classes_agree_with_separators(self):
        m=machine("invasive")
        classes=m.observational_classes()
        for a in m.states:
            for b in m.states:
                same=any(a in cl and b in cl for cl in classes)
                self.assertEqual(m.shortest_separator(a,b) is None,same)

    def test_all_short_word_controls(self):
        m=machine("invisible")
        for n in range(5):
            for w in product(m.actions,repeat=n):
                self.assertEqual(m.trace("source0",w)[0],m.trace("source1",w)[0])

    def test_model_no_magic_adaptive_gain(self):
        m=machine("invasive")
        # All passive histories coincide, so no passive adaptive decision can split.
        for n in range(6):
            self.assertEqual(m.trace("source0",("passive",)*n)[0],
                             m.trace("source1",("passive",)*n)[0])

    def test_exhaustive_two_state_binary_machine_cross_oracles(self):
        # Independent algorithms: partition refinement vs pair-product BFS.
        states=("a","b"); actions=("x","y")
        entries=list(product(("0","1"),states))
        keys=list(product(states,actions))
        count=0
        for selection in product(entries,repeat=len(keys)):
            machine=FiniteInstrument(states,actions,dict(zip(keys,selection)))
            classes=machine.observational_classes()
            same=any("a" in cl and "b" in cl for cl in classes)
            self.assertEqual(machine.shortest_separator("a","b") is None,same)
            count+=1
        self.assertEqual(count,256)

    def test_malformed_machine_rejected(self):
        for arg in [
            {"states":("a","a"),"actions":("read",),"transitions":{("a","read"):("x","a")}},
            {"states":("a","b"),"actions":("read",),"transitions":{("a","read"):("x","b")}},
            {"states":("a",),"actions":("read",),"transitions":{("a","read"):("x","ghost")}},
        ]:
            with self.subTest(arg=arg),self.assertRaises(ProbeContractError):
                FiniteInstrument(**arg)
        with self.assertRaises(ProbeContractError): machine("qnd").trace("ghost",("passive",))
        with self.assertRaises(ProbeContractError): machine("qnd").allowed(("telepathy",))

if __name__ == "__main__":
    unittest.main()

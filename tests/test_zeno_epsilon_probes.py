from fractions import Fraction as F
import unittest

from observational_succ.zeno_certificate import Stamp
from observational_succ.zeno_proof_debt import (
    SourceFibre, ProbeTable, ProofDebtError,
    epsilon_probe_cover, dynamic_protocol_blindness,
)
ST=Stamp("full-mathematical-source",3,"bits","Cantor-prefix")
ALT=Stamp("mismatched-source",3,"bits","Cantor-prefix")


class TestFiniteApproximationCovers(unittest.TestCase):
    def test_eight_bit_cantor_binary_target(self):
        n=8
        states=tuple(format(i,"08b") for i in range(2**n))
        # positive binary coordinate sum, first bit weight 1/2
        targets=tuple(sum((F(int(b),2**(j+1)) for j,b in enumerate(s)),F(0)) for s in states)
        source=SourceFibre(ST,"binary-real-target",states,targets)
        probes=tuple(ProbeTable(ST,f"bit{j}",tuple(s[j] for s in states)) for j in range(n))
        at_sixteenth=epsilon_probe_cover(source,probes,F(1,16))
        self.assertEqual(at_sixteenth["status"],"CERTIFIED_FINITE_EPSILON_COVER")
        self.assertEqual(at_sixteenth["names"],tuple(f"bit{j}" for j in range(4)))
        self.assertEqual(at_sixteenth["maximum_target_width"],F(15,256))
        self.assertFalse(at_sixteenth["physical_joint_executability_verified"])
        self.assertFalse(at_sixteenth["source_law_authenticated_externally"])
        at_quarter=epsilon_probe_cover(source,probes,F(1,4))
        self.assertEqual(at_quarter["names"],("bit0","bit1"))

    def test_minimal_xor_joint(self):
        sources=SourceFibre(ST,"xor",("00","01","10","11"),(0,1,1,0))
        A=ProbeTable(ST,"A",("0","0","1","1"))
        B=ProbeTable(ST,"B",("0","1","0","1"))
        ans=epsilon_probe_cover(sources,(A,B),F(1))
        self.assertEqual(ans["names"],("A","B"))
        self.assertEqual(ans["maximum_target_width"],0)
        refused=epsilon_probe_cover(sources,(A,),F(1))
        self.assertEqual(refused["status"],"ARITY_OR_SOURCE_INFORMATION_OBSTRUCTION")
        self.assertEqual(refused["maximum_target_width"],1)
        self.assertIsNotNone(refused["indistinguishable_target_pair"])

    def test_adaptive_policy_cannot_break_readonly_equivalence(self):
        src=SourceFibre(ST,"left-bit",("00","01","10","11"),(0,1,0,1))
        q=(ProbeTable(ST,"left-only",("0","0","1","1")),)
        blind=dynamic_protocol_blindness(src,q,target_separation=F(0))
        self.assertEqual(blind["status"],"UNAVOIDABLE_READONLY_EPISTEMIC_DEBT")
        self.assertEqual(blind["lower_bound"],1)
        self.assertFalse(blind["unrestricted_other_probes_ruled_out"])

    def test_wrong_epoch_and_missing_source_rows(self):
        src=SourceFibre(ST,"t",("s0","s1"),(0,1))
        for p in (ProbeTable(ALT,"q",("0","1")),ProbeTable(ST,"q",("0",))):
            with self.assertRaises(ProofDebtError):epsilon_probe_cover(src,(p,),F(1))
        with self.assertRaises(ProofDebtError):epsilon_probe_cover(src,(ProbeTable(ST,"q",("0","1")),),F(1),max_charts=0)

    def test_open_epsilon_is_strict(self):
        src=SourceFibre(ST,"t",("x","y"),(0,F(1,2)))
        ans=epsilon_probe_cover(src,(),F(1,2))
        self.assertEqual(ans["status"],"ARITY_OR_SOURCE_INFORMATION_OBSTRUCTION")
        ans2=epsilon_probe_cover(src,(),F(3,4))
        self.assertEqual(ans2["names"],())

    def test_inclusive_target_separation_at_boundary(self):
        src=SourceFibre(ST,"t",("x","y"),(0,F(1,2)))
        p=ProbeTable(ST,"c",("same","same"))
        out=dynamic_protocol_blindness(src,(p,),target_separation=F(1,2))
        self.assertEqual(out["status"],"UNAVOIDABLE_READONLY_EPISTEMIC_DEBT")
        self.assertEqual(out["lower_bound"],F(1,2))

    def test_no_extra_measured_actions_after_adaptive_join(self):
        src=SourceFibre(ST,"t",("x","y","z"),(0,1,2))
        q=ProbeTable(ST,"constant",("same",)*3)
        ans=dynamic_protocol_blindness(src,(q,),target_separation=F(1))
        self.assertEqual(ans["lower_bound"],2)
        self.assertEqual(ans["status"],"UNAVOIDABLE_READONLY_EPISTEMIC_DEBT")
        q2=ProbeTable(ST,"identity",("x","y","z"))
        ans2=dynamic_protocol_blindness(src,(q,q2,),target_separation=F(1))
        self.assertEqual(ans2["status"],"NO_INDEFEASIBLE_PAIR_AT_THIS_CONTRAST")
        self.assertEqual(ans2["lower_bound"],0)


if __name__=='__main__':unittest.main()

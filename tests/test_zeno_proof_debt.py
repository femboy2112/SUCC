"""Independent exact arithmetic controls for the source-indexed Zeno proof debt system."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
import random
import unittest

from observational_succ.zeno_certificate import Stamp
from observational_succ.zeno_proof_debt import (
    AmortizedContract, EvidenceLedger, MovingTarget, ProofDebtError,
    ProofDebtLedger, ProofEvent, SignedEvidence, SourceFibre,
    exact_psd, future_geometric_drift, gamma_tail_bracket,
    gamma_simple_upper, schur_two_zeno_gate, signed_weil_test_gate,
    toy_halting_real, generic_rank_one_operator_stage,
)

STAMP=Stamp("integer-original",12,"standard","mathematical-proof-claims")
BAD=Stamp("fake-six-source",12,"standard","mathematical-proof-claims")


def event(i,birth,discharge,elapsed=0,resource=0,stamp=STAMP,target="fixed"):
    return ProofEvent(stamp,target,i,F(birth),F(discharge),F(elapsed),F(resource),f"receipt-{i}")


def det(A):
    n=len(A)
    if n==0:return F(1)
    if n==1:return A[0][0]
    return sum(((-1)**j)*A[0][j]*det(tuple(tuple(A[i][k] for k in range(n) if k!=j) for i in range(1,n)))
               for j in range(n))


def independent_psd(A):
    n=len(A)
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):
        raise ValueError("independent oracle requires symmetry")
    return all(det(tuple(tuple(A[i][j] for j in indices) for i in indices))>=0
               for size in range(1,n+1) for indices in combinations(range(n),size))


def qval(A,x):
    return sum((A[i][j]*x[i]*x[j] for i in range(len(x)) for j in range(len(x))),F(0))


class TestHistoricalDebt(unittest.TestCase):
    def test_recurrence_and_two_distinct_budgets(self):
        z=ProofDebtLedger(STAMP,"fixed",F(1))
        z=z.append(event(0,F(1,2),F(1,4),F(1,2),3))
        z=z.append(event(1,F(1,4),F(1),F(1,4),5))
        self.assertEqual(z.snapshots(),(F(1),F(5,4),F(1,2)))
        self.assertEqual(z.elapsed,F(3,4))
        self.assertEqual(z.resource,F(8))
        self.assertEqual(z.outstanding,F(1,2))

    def test_born_cannot_discharge_ghost(self):
        with self.assertRaises(ProofDebtError):
            ProofDebtLedger(STAMP,"fixed",F(0)).append(event(0,0,1))

    def test_wrong_source_epoch_and_target_rejected(self):
        for e in (event(0,0,0,stamp=BAD),event(1,0,0),event(0,0,0,target="changed")):
            with self.assertRaises(ProofDebtError):
                ProofDebtLedger(STAMP,"fixed",F(1)).append(e)

    def test_mutable_history_and_duplicate_source_labels_rejected(self):
        with self.assertRaises(ProofDebtError):
            ProofDebtLedger(STAMP,"fixed",1,[])
        with self.assertRaises(ProofDebtError):
            MovingTarget(STAMP,("dup","dup"),(0,1),(0,1))

    def test_time_converges_cost_diverges_control(self):
        z=ProofDebtLedger(STAMP,"fixed",F(1))
        for n in range(12):
            z=z.append(event(n,0,0,F(1,2**(n+1)),F(1)))
        self.assertEqual(z.elapsed,F(4095,4096))
        self.assertEqual(z.resource,12)
        self.assertEqual(z.outstanding,1)
        self.assertEqual(len(z.events),12)


class TestAmortizedProofDebt(unittest.TestCase):
    def test_upper_exact_equal_ratio(self):
        c=AmortizedContract(STAMP,"fixed",F(1),F(1,2),F(1,3),F(1,2),True)
        for n in range(12):
            want=F(1,2)**n+(F(n,3)*F(1,2)**(n-1) if n else 0)
            self.assertEqual(c.exact_upper(n),want)

    def test_independent_recurrence_and_geometric_majorant(self):
        rng=random.Random(20261014)
        for _ in range(150):
            q=F(rng.randrange(10),10)
            r=F(rng.randrange(10),10)
            d0=F(rng.randrange(7),5)
            c0=F(rng.randrange(9),3)
            c=AmortizedContract(STAMP,"fixed",d0,q,c0,r,True)
            K,rho=c.geometric_envelope()
            d=d0
            for n in range(18):
                self.assertEqual(d,c.exact_upper(n))
                self.assertLessEqual(d,K*rho**n)
                d=q*d+c0*r**n

    def test_uniform_future_horizon_source_law(self):
        c=AmortizedContract(STAMP,"fixed",F(1),F(1,2),F(1,4),F(1,3),True)
        n,b=c.horizon(F(1,100))
        K,rho=c.geometric_envelope()
        self.assertLessEqual(b,F(1,100))
        self.assertEqual(b,K*rho**n)
        self.assertGreater(K*rho**(n-1),F(1,100))
        for k in range(n,n+50):
            self.assertLessEqual(c.exact_upper(k),K*rho**k)
            self.assertLessEqual(K*rho**k,F(1,100))

    def test_no_universal_law_no_promotion(self):
        c=AmortizedContract(STAMP,"fixed",1,F(1,2),F(1),F(1,3),False)
        with self.assertRaisesRegex(ProofDebtError,"UNVERIFIED"):
            c.horizon(F(1,1000))

    def test_budget_exhaustion_not_physical_no_go(self):
        c=AmortizedContract(STAMP,"fixed",1,F(99,100),1,F(99,100),True)
        with self.assertRaisesRegex(ProofDebtError,"RESOURCE_BUDGET"):
            c.horizon(F(1,10**50),max_search=3)

    def test_replay_rejects_false_bound(self):
        c=AmortizedContract(STAMP,"fixed",1,F(1,2),0,0,True)
        okay=ProofDebtLedger(STAMP,"fixed",1).append(event(0,0,F(1,2)))
        bad=ProofDebtLedger(STAMP,"fixed",1).append(event(0,0,F(1,4)))
        self.assertTrue(c.replay_observed(okay))
        self.assertFalse(c.replay_observed(bad))

    def test_replay_both_source_and_target(self):
        c=AmortizedContract(STAMP,"fixed",1,F(1,2),0,0,True)
        with self.assertRaises(ProofDebtError):
            c.replay_observed(ProofDebtLedger(BAD,"fixed",1))
        with self.assertRaises(ProofDebtError):
            c.replay_observed(ProofDebtLedger(STAMP,"not-fixed",1))

    def test_perpetual_birth_no_completion(self):
        d=F(0)
        q=F(1,2)
        for _ in range(20):d=q*d+1
        self.assertEqual(d,2-F(1,2**19))
        self.assertGreater(d,F(19,10))

    def test_unsummable_births_can_have_zero_limit(self):
        d=F(0)
        for n in range(200):d=d/2+F(1,n+1)
        self.assertLess(d,F(3,200))
        self.assertGreater(sum((F(1,n) for n in range(1,201)),F(0)),5)


class TestEpistemicDebt(unittest.TestCase):
    def setUp(self):
        self.src=SourceFibre(STAMP,"xor",("00","01","10","11"),(0,1,1,0))

    def test_successor_refines_without_adding_source_states(self):
        s=self.src
        t=s.observe("read-left",("0","0","1","1"),"0",stamp=STAMP)
        self.assertEqual(s.width,1)
        self.assertEqual(t.width,1)
        t=t.observe("read-right",("0","1","0","1"),"1",stamp=STAMP)
        self.assertEqual(t.width,0)
        self.assertEqual(t.range,(1,1))
        self.assertEqual(t.indices(),(1,))
        self.assertEqual(t.history,(("read-left","0"),("read-right","1")))

    def test_failed_history_and_ghost_undone(self):
        with self.assertRaisesRegex(ProofDebtError,"NO_GHOST"):
            self.src.observe("impossible",("0",)*4,"1",stamp=STAMP)
        with self.assertRaises(ProofDebtError):
            self.src.observe("forgery",("0",)*4,"0",stamp=BAD)
        with self.assertRaises(ProofDebtError):
            self.src.observe("partial",("0","1"),"0",stamp=STAMP)

    def test_target_debt_witness(self):
        self.assertEqual(self.src.witness(),("00","01"))
        self.assertEqual(self.src.range,(0,1))

    def test_moving_target_future_premise(self):
        s=MovingTarget(STAMP,("a","b"),(0,F(1,2)),(0,1))
        s=s.step((F(1,8),F(5,8)),F(1,8),stamp=STAMP)
        self.assertEqual(s.stage,1)
        self.assertEqual(s.checks,(F(1,8),))
        with self.assertRaisesRegex(ProofDebtError,"FUTURE"):
            s.guaranteed_limit_range(F(1,4))
        self.assertEqual(s.guaranteed_limit_range(F(1,4),universal_drift_law=True),(-F(1,8),F(7,8)))

    def test_future_drift_and_false_new_sources(self):
        s=MovingTarget(STAMP,("a","b"),(0,1),(0,))
        with self.assertRaisesRegex(ProofDebtError,"GHOST"):
            s.step((0,1),0,stamp=STAMP,survive=(0,1))
        with self.assertRaisesRegex(ProofDebtError,"DRIFT"):
            s.step((F(1,2),1),F(1,10),stamp=STAMP)
        with self.assertRaises(ProofDebtError):
            s.step((0,1),0,stamp=BAD)
        self.assertEqual(future_geometric_drift(1,F(1,2),3),F(1,4))


class TestIntervalsAndUndecidability(unittest.TestCase):
    def test_intersect_nested_certificates(self):
        ledger=EvidenceLedger(STAMP,"signed-form")
        entries=(SignedEvidence(STAMP,"signed-form",0,0,1,"f0"),
                 SignedEvidence(STAMP,"signed-form",1,F(1,4),F(1,2),"f1"),
                 SignedEvidence(STAMP,"signed-form",2,F(1,4),F(1,4),"f2"))
        for ent in entries:ledger=ledger.append(ent)
        self.assertEqual(ledger.interval,(0,F(1,2)))
        self.assertEqual(ledger.sign,"NONNEGATIVE")

    def test_finite_signed_decision_and_zero_boundary(self):
        signs=[]
        for actual in (F(-1,8),F(1,8),F(0)):
            x=EvidenceLedger(STAMP,"signed-form")
            for n in range(10):
                q=F(0) if n<3 else actual
                if n<3 and abs(actual)>F(1,2**n): q=actual
                e=F(1,2**n)+abs(q-actual)
                x=x.append(SignedEvidence(STAMP,"signed-form",n,q,e,f"e{n}"))
            signs.append(x.sign)
        self.assertEqual(signs,["STRICTLY_NEGATIVE","STRICTLY_POSITIVE","UNRESOLVED"])

    def test_false_intervals_source_stale_conflict(self):
        x=EvidenceLedger(STAMP,"f")
        x=x.append(SignedEvidence(STAMP,"f",0,0,1,"premise"))
        for ent in (SignedEvidence(BAD,"f",1,0,1,"wrong-source"),
                    SignedEvidence(STAMP,"f",0,0,1,"stale-stage"),
                    SignedEvidence(STAMP,"g",1,0,1,"wrong-target"),
                    SignedEvidence(STAMP,"f",1,3,F(1,4),"mutant")):
            with self.assertRaises(ProofDebtError):x.append(ent)

    def test_operator_sign_has_effective_norm_error_but_still_undecidable_weak_sign(self):
        for n in range(10):
            never=generic_rank_one_operator_stage(n,None)
            delayed=generic_rank_one_operator_stage(n,50)
            self.assertEqual(never,delayed)
            self.assertEqual(never["norm_error_upper"],F(1,2**(n+2)))
            self.assertTrue(exact_psd(never["matrix"])[0])
            self.assertFalse(never["completed_weil_identification"])
        seen=generic_rank_one_operator_stage(51,50)
        self.assertFalse(exact_psd(seen["matrix"])[0])
        self.assertLess(seen["matrix"][0][0],0)

    def test_effective_halting_toy_prefix_indistinguishability(self):
        for N in range(10):
            none=toy_halting_real(N,None)
            delayed=toy_halting_real(N,N+25)
            self.assertEqual(none,delayed)
            self.assertLessEqual(F(1,2**(N+27)),delayed[1])
        self.assertEqual(toy_halting_real(5,3)[0],-F(1,32))
        self.assertEqual(toy_halting_real(3,3)[0],-F(1,32))


class TestGammaAndOperatorDebt(unittest.TestCase):
    def test_tail_enclosures_independent_finite_partial_lower(self):
        for j in (1,2,5,16,100):
            lo,hi=gamma_tail_bracket(j,20)
            sample=sum((F(16,(4*i+1)**3) for i in range(j,j+300)),F(0))
            self.assertLess(lo,hi)
            self.assertLess(sample,hi)
            self.assertLess(sample+gamma_simple_upper(j+300),hi)
            self.assertEqual(gamma_simple_upper(j),gamma_tail_bracket(j)[1])

    def test_tail_upper_stronger_with_more_exact_rungs(self):
        for j in (1,5,50):
            self.assertGreater(gamma_tail_bracket(j,0)[1],gamma_tail_bracket(j,5)[1])
            self.assertGreater(gamma_tail_bracket(j,5)[1],gamma_tail_bracket(j,50)[1])

    def test_false_gemini_j1_constant_rejected(self):
        self.assertGreater(F(16,5**3),F(1,8))
        self.assertGreater(gamma_tail_bracket(1,5)[0],F(1,8))

    def test_one_sided_weil_sign_gate(self):
        self.assertEqual(signed_weil_test_gate(F(-1,10),1,1,10),"UNRESOLVED_SIGN")
        self.assertEqual(signed_weil_test_gate(F(1,10),F(1,5),1,10),"CERTIFIED_ONE_TEST_NONNEGATIVE")
        self.assertEqual(signed_weil_test_gate(-2,-1,1,10),"CERTIFIED_ONE_TEST_NEGATIVE")
        with self.assertRaises(ProofDebtError):signed_weil_test_gate(2,1,1,2)

    def test_psd_against_independent_all_principal_minors(self):
        rng=random.Random(20261014)
        for n in (1,2,3,4):
            for _ in range(75):
                A=tuple(tuple(F(rng.randrange(-3,4)) for _ in range(n)) for _ in range(n))
                A=tuple(tuple((A[i][j]+A[j][i])/2 for j in range(n)) for i in range(n))
                expected=independent_psd(A)
                ok,w=exact_psd(A)
                self.assertEqual(ok,expected)
                if not ok:
                    self.assertIsNotNone(w)
                    self.assertLess(qval(A,w),0)

    def test_semidefinite_exact_gram_and_pairwise_falsehood(self):
        A=((F(1),F(1)),(F(1),F(1)))
        self.assertEqual(exact_psd(A),(True,None))
        M=((F(1),F(2)),(F(2),F(1)))
        ok,w=exact_psd(M)
        self.assertFalse(ok)
        self.assertLess(qval(M,w),0)

    def test_schur_with_approximation_and_hostile_mutations(self):
        yes=schur_two_zeno_gate(((F(3),),),F(2),F(1,2),F(1,10))
        self.assertTrue(yes["certifies_all_vectors_conditional_on_inputs"])
        self.assertFalse(yes["claimed_authentic_weil_coefficients_verified"])
        no=schur_two_zeno_gate(((F(1,10),),),2,1,F(1,10))
        self.assertFalse(no["certifies_all_vectors_conditional_on_inputs"])
        with self.assertRaises(ProofDebtError):
            schur_two_zeno_gate(((1,),),F(1,10),1,F(1,5))
        with self.assertRaises(ProofDebtError):
            schur_two_zeno_gate(((1.0,),),2,1,0)

    def test_rational_schur_nondiagonal(self):
        test=schur_two_zeno_gate(((3,F(1,4)),(F(1,4),3)),2,F(1,5),F(1,20))
        self.assertTrue(test["certifies_all_vectors_conditional_on_inputs"])
        self.assertTrue(independent_psd(test["adjusted"]))


if __name__=="__main__":
    unittest.main()

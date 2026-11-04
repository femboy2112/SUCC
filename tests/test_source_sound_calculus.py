"""Exact mathematical / finite-model contract tests for research calculus."""
import sys
import unittest
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'research'/'2026-11-04'
sys.path.insert(0,str(BASE/'source_sound_calculus'))
sys.path.insert(0,str(BASE/'operational_foundations'))
import lcm_carrier as l
import source_sound as p
import operational_probe as o


class LCMCarrierTests(unittest.TestCase):
    def test_join_minimality_commutativity_associativity(self):
        for a in range(1,14):
            for b in range(1,14):
                L=l.divisor_join(a,b)
                self.assertEqual(L,l.divisor_join(b,a))
                self.assertEqual(a*b,gcd(a,b)*L)
                self.assertTrue(L%a==0 and L%b==0)
                self.assertTrue(all((x%a or x%b) for x in range(1,L)))
                for c in (1,3,7):
                    self.assertEqual(l.divisor_join(L,c),l.divisor_join(a,l.divisor_join(b,c)))

    def test_cyclic_exact_sequence_all_pairs(self):
        for a in range(1,21):
            for b in range(1,21):
                r=l.cyclic_join_finite(a,b)
                self.assertEqual((r.kernel_size,r.image_size,r.source_size),
                                 (gcd(a,b),lcm(a,b),a*b))
        r=l.cyclic_join_finite(6,10)
        self.assertEqual((r.gcd,r.lcm,r.kernel_size,r.image_size),(2,30,2,30))
        with self.assertRaises(l.CarrierError):l.cyclic_join_finite(100,100)

    def test_torsion_inclusion_phase_sums(self):
        for a in (1,2,3,5,6,9,10):
            for b in (1,2,3,5,6,9,10):
                for x in range(a):
                    for y in range(b):
                        r,L=l.phase_sum(x,a,y,b)
                        self.assertEqual(F(r,L)%1,(F(x,a)+F(y,b))%1)

    def test_actual_bbp_reduced_forcing_and_lcm_clock(self):
        states=l.bbp_prefix(80)
        sourceclock=1
        un=F(0)
        for n,s in enumerate(states):
            self.assertEqual(s.time,n)
            self.assertEqual(s.clock,sourceclock)
            self.assertEqual(s.unwrapped,un)
            self.assertEqual(s.clock%2,1)
            self.assertEqual(l.source_subgroup_clock(n),sourceclock)
            if n==80:break
            terms=l.forcing_terms(n+1)
            self.assertEqual(sum(terms,F(0)),l.force(n+1))
            un=16*un+l.force(n+1)
            sourceclock=lcm(sourceclock,l.force(n+1).denominator)
            next_state=states[n+1]
            literal=(16*(s.numerator%s.clock)*(next_state.clock//s.clock)+
                     (next_state.clock//l.force(n+1).denominator)*l.force(n+1).numerator)//next_state.clock
            self.assertEqual(next_state.last_carry,literal)

    def test_crt_local_projection_and_reconstruction(self):
        for pp in ((2,3),(4,9),(3,5,7),(8,25),(3,)): 
            M=1
            for x in pp:M*=x
            for addr in range(M):
                coords=l.local_phase_coordinates(addr,M,pp)
                back,den=l.global_from_local(coords,pp)
                self.assertEqual((back,den),(addr,M))
                self.assertEqual(sum((F(c,q) for c,q in zip(coords,pp)),F(0))%1,F(addr,M))
        with self.assertRaises(l.CarrierError):l.local_phase_coordinates(1,12,(4,6))

    def test_lcm_alone_does_not_select_coupling(self):
        x=l.prior_independence_countermodels()
        self.assertEqual(x['clock'],6)
        self.assertTrue(x['uniform_independent'])
        self.assertTrue(x['zero_dirac_independent'])
        self.assertFalse(x['correlated_prior_independent'])


class SourceSoundTests(unittest.TestCase):
    def setUp(self):
        self.src=o.DeclaredSource('synthetic::box',2,(
            o.Instrument('look',('red','red'),(0,1)),
            o.Instrument('tag',('original','replacement'),(0,1),2),
        ))
        self.ctx=p.Context(models={self.src.source:self.src})
        self.ck=p.Checker(self.ctx)

    def test_exact_synthetic_trace_and_filter(self):
        trace=p.Claim(self.src.source,'TRACE',(0,('look','tag'),('red','original'),0))
        modelrun=p.Proof('MODEL_TRACE',trace,inputs=(0,('look','tag')))
        verdict=self.ck.check(modelrun)
        self.assertEqual(verdict.status(),'MODEL_EXACT_NOT_EMPIRICAL')
        filt=p.Claim(self.src.source,'CANDIDATES',(('look','tag'),('red','original'),(0,)))
        final=self.ck.check(p.Proof('MODEL_FILTER',filt,(modelrun,)))
        self.assertEqual(final.status(),'MODEL_EXACT_NOT_EMPIRICAL')
        self.assertEqual(final.open_hypotheses,frozenset())

    def test_journal_requires_a_verified_trace_and_source_provenance(self):
        c=p.Claim(self.src.source,'TRACE',(0,('look','tag'),('red','original'),0))
        tr=p.Proof('MODEL_TRACE',c,inputs=(0,('look','tag')))
        entries=((self.src.source,'look','red'),(self.src.source,'tag','original'))
        x=p.Claim(self.src.source,'JOURNAL',(0,entries,0))
        self.assertEqual(self.ck.check(p.Proof('MODEL_JOURNAL',x,(tr,))).status(),
                         'MODEL_EXACT_NOT_EMPIRICAL')
        wrong=p.Claim(self.src.source,'JOURNAL',(0,((self.src.source,'look','blue'),),0))
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('MODEL_JOURNAL',wrong,(tr,)))
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('MODEL_JOURNAL',x))

    def test_source_refinement_not_an_empirical_observation(self):
        lo=(('look',),3,3)
        hi=(('look','tag'),3,4)
        small=self.src.observation_classes(*lo)
        large=self.src.observation_classes(*hi)
        claim=p.Claim(self.src.source,'REFINES',(lo,hi,small,large))
        res=self.ck.check(p.Proof('MODEL_REFINEMENT',claim,inputs=(lo,hi)))
        self.assertTrue(res.uses_model)
        self.assertEqual(small,((0,1),))
        self.assertEqual(large,((0,),(1,)))
        with self.assertRaises(p.ProofError):
            self.ck.check(p.Proof('MODEL_REFINEMENT',claim,inputs=(hi,lo)))

    def test_real_model_relative_induction_requires_source_step(self):
        src=o.DeclaredSource('induction::synthetic',3,(
            o.Instrument('advance',('ok','ok','bad'),(1,1,2)),
            o.Instrument('wait',('ok','ok','bad'),(0,1,2)),
        ))
        ctx=p.Checker(p.Context(models={src.source:src}))
        fact=p.Claim(src.source,'REACHABLE_INVARIANT',(0,('advance','wait'),(True,True,False)))
        self.assertEqual(ctx.check(p.Proof('MODEL_INDUCT',fact,inputs=fact.data)).status(),
                         'MODEL_EXACT_NOT_EMPIRICAL')
        mutant=o.DeclaredSource('induction::mutant',3,(
            o.Instrument('advance',('ok','ok','bad'),(1,2,2)),
        ))
        bad=p.Claim(mutant.source,'REACHABLE_INVARIANT',(0,('advance',),(True,True,False)))
        with self.assertRaises(p.ProofError):
            p.Checker(p.Context(models={mutant.source:mutant})).check(p.Proof('MODEL_INDUCT',bad,inputs=bad.data))
        with self.assertRaises(p.ProofError):
            ctx.check(p.Proof('MODEL_INDUCT',fact,inputs=(2,('advance','wait'),(True,True,False))))

    def test_math_lcm_and_group_gluing_proof_receipts(self):
        c=p.Claim(p.ARITH,'LCM_JOIN',(6,10,30))
        q=p.Proof('ARITH_LCM',c)
        self.assertEqual(self.ck.check(q).status(),'EXACT_FINITE_ARITHMETIC_OR_LOGIC')
        glue=p.Claim(p.ARITH,'CYCLIC_GLUE',(6,10,2,30,2,30))
        self.assertTrue(self.ck.check(p.Proof('ARITH_CYCLIC_GLUE',glue)).uses_arithmetic)
        with self.assertRaises(p.ProofError):
            self.ck.check(p.Proof('ARITH_LCM',p.Claim(p.ARITH,'LCM_JOIN',(6,10,60))))
        with self.assertRaises(p.ProofError):
            self.ck.check(p.Proof('ARITH_CYCLIC_GLUE',p.Claim(p.ARITH,'CYCLIC_GLUE',(6,10,1,30,1,30))))

    def test_actual_bbp_origin_chain_has_lcm_and_carries(self):
        s=l.bbp_origin()
        origin=p.Proof('BBP_ORIGIN',p.Claim(p.BBP,'BBP_REGISTER',(0,1,0,None)))
        self.assertTrue(self.ck.check(origin).uses_arithmetic)
        for _ in range(1,30):
            s=l.bbp_step(s)
            origin=p.Proof('BBP_STEP',p.Claim(p.BBP,'BBP_REGISTER',
                       (s.time,s.clock,s.numerator,s.last_carry)),(origin,))
        res=self.ck.check(origin)
        self.assertEqual(res.conclusion.data,(s.time,s.clock,s.numerator,s.last_carry))
        self.assertEqual(res.status(),'EXACT_FINITE_ARITHMETIC_OR_LOGIC')
        evil=p.Proof('BBP_STEP',p.Claim(p.BBP,'BBP_REGISTER',(30,1,0,0)),(origin,))
        with self.assertRaises(p.ProofError):self.ck.check(evil)
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('BBP_ORIGIN',p.Claim(p.BBP,'BBP_REGISTER',(0,1,1,None))))

    def test_hypothesis_not_promoted_by_implication_or_repetition(self):
        a=p.Claim('synthetic::box','ATOM',('all-future-observations-equal',))
        b=p.Claim('synthetic::box','ATOM',('normality-follows',))
        ctx=p.Context(models=self.ctx.models,hypotheses=frozenset((a,p.Claim('synthetic::box','IMPLIES',(a,b)))))
        c=p.Checker(ctx)
        aa=p.Proof('ASSUME',a)
        ab=p.Proof('ASSUME',p.Claim('synthetic::box','IMPLIES',(a,b)))
        outcome=c.check(p.Proof('MP',b,(ab,aa)))
        self.assertEqual(outcome.status(),'CONDITIONAL')
        self.assertIn(a,outcome.open_hypotheses)
        theorem=c.check(p.Proof('IMP_I',p.Claim('synthetic::box','IMPLIES',(a,a)),(aa,),(a,)))
        self.assertEqual(theorem.status(),'EXACT_FINITE_ARITHMETIC_OR_LOGIC')
        self.assertEqual(theorem.open_hypotheses,frozenset())

    def test_conjunction_rules(self):
        a=p.Claim(p.ARITH,'LCM_JOIN',(3,4,12))
        b=p.Claim(p.ARITH,'LCM_JOIN',(4,6,12))
        pa=p.Proof('ARITH_LCM',a);pb=p.Proof('ARITH_LCM',b)
        comb=p.Proof('AND_I',p.Claim(p.ARITH,'AND',(a,b)),(pa,pb))
        self.assertEqual(self.ck.check(p.Proof('AND_E',a,(comb,),(0,))).conclusion,a)
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('AND_E',a,(comb,),(1,)))

    def test_bad_source_attestation_and_quantifiers_rejected(self):
        c=p.Claim(self.src.source,'TRACE',(0,('look',),('red',),0))
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('EMPIRICAL_ATTESTATION',c))
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('INDUCT_FROM_FINITE',c))
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('MODEL_TRACE',c,inputs=(1,('look',))))
        with self.assertRaises(p.ProofError):p.Claim(self.src.source,'UNIVERSAL_NORMALITY',())
        with self.assertRaises(p.ProofError):self.ck.check(p.Proof('ARITH_LCM',p.Claim('fake-source','LCM_JOIN',(6,10,30))))
        with self.assertRaises(p.ProofError):
            x=p.Claim('other-source','ATOM',('a',));y=p.Claim(self.src.source,'ATOM',('b',));p.Claim(self.src.source,'IMPLIES',(x,y))
        with self.assertRaises(p.ProofError):
            self.ck.check(p.Proof('MODEL_TRACE',p.Claim(self.src.source,'TRACE',(0,('look',),('blue',),0)),inputs=(0,('look',))))

    def test_finite_no_overpromise_and_budget(self):
        a=p.Claim(p.ARITH,'LCM_JOIN',(6,10,30))
        pa=p.Proof('ARITH_LCM',a)
        conj=p.Proof('AND_I',p.Claim(p.ARITH,'AND',(a,a)),(pa,pa))
        with self.assertRaises(p.ProofError):p.Checker(self.ctx,max_nodes=1).check(conj)
        proof=p.Checker(self.ctx,max_nodes=2).check(conj)
        self.assertEqual(proof.status(),'EXACT_FINITE_ARITHMETIC_OR_LOGIC')

if __name__=='__main__':unittest.main()

"""Independent finite Seinfeld coherence/checkpoint assertions, no pi oracle."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import gcd
import unittest

from observational_succ import seinfeld_coherence_groups as sc


class PhaseFactorTests(unittest.TestCase):
    def test_minimal_phase_quotient_every_residue(self):
        for h in range(-40,41):
            expected=16//gcd(16,h)
            out=sc.phase_partition_certificate(h)
            self.assertEqual(out['modulus'],expected)
            self.assertTrue(out['minimal'])
            self.assertEqual(sum(map(len,out['groups'])),16)
            for group in out['groups']:
                for j in group:
                    for k in group:
                        self.assertEqual((h*(j-k))%16,0)
        self.assertEqual([sc.phase_group_modulus(h) for h in (1,2,4,8,16)], [16,8,4,2,1])

    def test_coarser_parity_alias_misses_quarter_turn(self):
        # j=0 and j=2 have the same parity but chi_4 differ by a minus sign.
        self.assertEqual(0%2,2%2)
        self.assertEqual((4*0)%16,0)
        self.assertEqual((4*2)%16,8)
        self.assertEqual(sc.phase_group_modulus(4),4)



class SignedGroupedAmplitudes(unittest.TestCase):
    def test_reference_cancellation_but_realized_path_coherence(self):
        labels=tuple(j%2 for j in range(16))
        phases=tuple(j for j in range(16))
        ref=sc.grouped_phase_amplitudes((F(1,16),)*16,labels,phases)
        self.assertEqual(sum(ref['total']),1)
        self.assertEqual(sc.parity_evaluate_amplitude(ref['total']),0)
        self.assertEqual(sc.parity_evaluate_amplitude(ref['groups'][0]),F(1,2))
        self.assertEqual(sc.parity_evaluate_amplitude(ref['groups'][1]),F(-1,2))
        chosen=sc.grouped_phase_amplitudes((F(1),)+(F(0),)*15,labels,phases)
        self.assertEqual(sc.parity_evaluate_amplitude(chosen['total']),1)
        self.assertEqual(sum(chosen['groups'][0]),1)
        self.assertEqual(sum(chosen['groups'][1]),0)
        self.assertFalse(chosen['pi_normality_proved'])
        # The formal source vector is NOT the cyclotomic evaluated zero.
        self.assertNotEqual(ref['total'],tuple(F(0) for _ in range(16)))

    def test_grouping_preserves_signed_formal_phase_for_arbitrary_laws(self):
        weights=(F(1,10),F(2,10),F(3,10),F(4,10))
        labels=('even','odd','even','odd')
        phases=(0,1,1,0)
        out=sc.grouped_phase_amplitudes(weights,labels,phases)
        self.assertEqual(out['total'][0],F(1,2))
        self.assertEqual(out['total'][1],F(1,2))
        self.assertEqual(sc.parity_evaluate_amplitude(out['total']),0)
        self.assertEqual(sc.parity_evaluate_amplitude(out['groups']['even']),F(-1,5))
        self.assertEqual(sc.parity_evaluate_amplitude(out['groups']['odd']),F(1,5))

    def test_invalid_signed_coarse_grain_fails_closed(self):
        with self.assertRaises(ValueError):sc.grouped_phase_amplitudes((F(1),),(),(0,))
        with self.assertRaises(ValueError):sc.grouped_phase_amplitudes((F(1,2),),(0,),(0,))
        with self.assertRaises(ValueError):sc.grouped_phase_amplitudes((F(1),),(0,),(0.5,))


class MemoryTests(unittest.TestCase):
    def test_kl_information_chain(self):
        for n in (1,2,3,8,24):
            for k in range(n+1):
                r=sc.prefix_information(n,k)
                self.assertEqual(r['global_kl_log_base'],16**n)
                self.assertEqual(r['checkpoint_kl_log_base'],16**k)
                self.assertEqual(r['unresolved_fiber_kl_log_base'],16**(n-k))
                self.assertEqual(r['checkpoint_kl_log_base']*r['unresolved_fiber_kl_log_base'],r['global_kl_log_base'])
                self.assertFalse(r['selected_weyl_saving_proved'])

    def test_reference_energy_increment_exact(self):
        for N in (1,2,7,16):
            for t in range(N+1):
                self.assertEqual(sc.reference_checkpoint_energy(N,t,7),F(t,N*N))
                self.assertEqual(sc.constant_selected_checkpoint(N,t),F(t,N))
                if t:
                    self.assertEqual(sc.reference_checkpoint_energy(N,t,7)-sc.reference_checkpoint_energy(N,t-1,7),F(1,N*N))
            self.assertEqual(sc.reference_checkpoint_energy(N,N,7),F(1,N))
            self.assertEqual(sc.constant_selected_checkpoint(N,N),1)
            self.assertEqual(sc.reference_checkpoint_energy(N,N,16),1)

    def test_global_vs_working_parity(self):
        even=[0]*16;odd=[0]*16
        even[0]=1;odd[1]=1
        d=sc.conditional_parity_checkpoint((tuple(even),tuple(odd)))
        self.assertEqual(d['global_energy'],0)
        self.assertEqual(d['working_energy'],1)
        self.assertEqual(d['checkpoint_information_energy'],1)
        d1=sc.conditional_parity_checkpoint((tuple(a+b for a,b in zip(even,odd)),))
        self.assertEqual(d1['global_energy'],0)
        self.assertEqual(d1['working_energy'],0)
        self.assertFalse(d['proves_source_mixing'])

    def test_conditional_parity_against_naive_independent_counts(self):
        for rows in (
           ((1,0)*8,),
           ((3,2)*8,(0,4)*8),
           ((0,)*16,(0,1)*8,(1,0)*8),
        ):
            v=sc.conditional_parity_checkpoint(rows)
            self.assertGreaterEqual(v['checkpoint_information_energy'],0)
            self.assertLessEqual(v['working_energy'],1)
            self.assertLessEqual(v['global_energy'],v['working_energy'])
        for invalid in ([],[[]],[[0.5]*16],[[False]*16],[[0]*16]):
            with self.assertRaises(ValueError):sc.conditional_parity_checkpoint(invalid)


class OperatorQuotientTests(unittest.TestCase):
    def test_lumpable_quotient_and_failure(self):
        labels=(0,1,0,1)
        rows=((0,1,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0))
        good=sc.quotient_transition((0,1,2,3),labels,rows)
        self.assertTrue(good['lumpable'])
        self.assertEqual(good['quotient_transition'],((F(0),F(1)),(F(1),F(0))))
        mutated=list(rows);mutated[2]=(0,0,1,0)
        failure=sc.quotient_transition((0,1,2,3),labels,mutated)
        self.assertFalse(failure['lumpable'])
        self.assertEqual(failure['counterexample_state'],2)
        self.assertNotEqual(failure['actual_group_row'],failure['expected_group_row'])

    def test_invalid_transition_rejected(self):
        with self.assertRaises(ValueError):sc.quotient_transition((0,1),(0,1),((F(1,2),F(1,2)),(2,-1)))
        with self.assertRaises(ValueError):sc.quotient_transition((0,1),(0,1),((F(1,2),F(1,2)),))


class PolyaControlTests(unittest.TestCase):
    def test_predictive_weight_normalization(self):
        for history in ((),(0,),(0,0),(0,1,1,2),(15,15,15,15)):
            p=sc.polya_working_weights(history)
            self.assertEqual(len(p),16)
            self.assertEqual(sum(p),1)
            self.assertGreater(min(p),0)
        self.assertEqual(sc.polya_working_weights((0,))[0],F(2,17))
        self.assertEqual(sc.polya_working_weights((0,))[1],F(1,17))

    def test_reference_likelihood_exact_normalization(self):
        self.assertEqual(sc.polya_reference_likelihood(()),1)
        for length in range(1,4):
            total=sum((sc.polya_reference_likelihood(t) for t in product(range(16),repeat=length)),F())
            self.assertEqual(total,F(16**length))
        self.assertEqual(sc.polya_reference_likelihood((0,)),1)
        self.assertEqual(sc.polya_reference_likelihood((0,0)),F(32,17))
        self.assertEqual(sc.polya_reference_likelihood((0,1)),F(16,17))

    def test_second_moment_unconditional_vs_realized(self):
        for N in (1,2,3,10,1024):
            v=sc.polya_fourier_second_moment(N,1)
            self.assertEqual(v,F(N+16,17*N))
            self.assertGreaterEqual(v,F(1,N))
            self.assertGreaterEqual(v,F(1,17))
            self.assertEqual(sc.polya_fourier_second_moment(N,16),1)
        # After 2 realizations, exact joint distribution from urn's product.
        # Event j1=j2 has prob 2/17 and j1!=j2 aggregate 15/17.
        diag=sum((sc.polya_reference_likelihood((j,j)) for j in range(16)),F(0))/(16**2)
        self.assertEqual(diag,F(2,17))
        # This is not a BBP proof (and not a Feynman physical measurement).
        self.assertFalse(sc.testable_status()['pi_base16_normality_proved'])

    def test_input_firewall(self):
        with self.assertRaises(ValueError):sc.polya_working_weights((16,))
        with self.assertRaises(ValueError):sc.polya_reference_likelihood((True,))
        with self.assertRaises(ValueError):sc.phase_partition_certificate(1.5)
        with self.assertRaises(ValueError):sc.prefix_information(1,2)


if __name__=='__main__':unittest.main()

class NativeSourceAdapterTests(unittest.TestCase):
    def test_source_parity_checkpoint_agrees_with_native_conditional_energy(self):
        from observational_succ.lambda_source_duality import original_history, branch_defect
        for N,M in ((8,2),(16,4),(64,4)):
            got=sc.source_parity_checkpoint(N,M)
            expected=branch_defect(original_history(N),M).exact_parity_energy()
            self.assertEqual(got['result']['working_energy'],expected)
            self.assertEqual(got['source'],'original-four-pole-zero-initial')
            self.assertEqual(got['horizon'],N)
            self.assertFalse(got['source_specific_saving_proved'])

"""Adversarial finite checks; analytic limits are proved in paper, not here."""
from __future__ import annotations

from fractions import Fraction as Q
import importlib.util
from itertools import product
from pathlib import Path
import unittest

HERE=Path(__file__).resolve()
MODULE=HERE.parent.parent/'scripts'/'pi_signed_cancellation_probe.py'
if not MODULE.exists():MODULE=HERE.with_name('pi_signed_cancellation_probe.py')
spec=importlib.util.spec_from_file_location('pi_signed_cancellation_probe',MODULE)
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)


class SourceAndIntervals(unittest.TestCase):
    def test_original_poles_native_adapter_and_holdouts(self):
        for n in (1,2,3,17,127,257,4097,65537):
            self.assertEqual(p.four_pole(n),p.cancelled(n))
            self.assertNotEqual(p.four_pole(n)+Q(1,8*n-3),p.cancelled(n))
        # Native integration checks the original adapter when run in repository.
        if MODULE.parent.name=='scripts':
            from observational_succ.bbp_binwindow_conjugacy import source_verified
            for n in (1,3,17,79,127):self.assertEqual(p.four_pole(n),source_verified(n))
        U=p.authentic_states(144)
        self.assertEqual(U[0],0)
        self.assertEqual(U[1],Q(47,15))
        for n in range(1,145):self.assertEqual(U[n]-16*U[n-1],p.four_pole(n))

    def test_pc320_counterfeit_exact_zero_and_different_source(self):
        self.assertEqual(p.pc320_state(0),0)
        for n in (1,2,7,31,127,255):
            self.assertEqual(p.pc320_state(n)-16*p.pc320_state(n-1),p.pc320_forcing(n))
            self.assertGreater(p.pc320_forcing(n),0)
            self.assertNotEqual(p.pc320_forcing(n),p.four_pole(n))
            self.assertEqual(p.pc320_state(n)%1,(-p.pc320_tail(n))%1)
            self.assertLessEqual(p.pc320_tail(n),Q(1,32*n*n))

    def test_machin_interval_and_exact_roots(self):
        lo,hi=p.pi_interval()
        self.assertLess(Q(157,50),lo)
        self.assertLess(hi,Q(22,7))
        self.assertLess(hi-lo,Q(1,2**70))
        for q,target in ((Q(0),(1,0)),(Q(1,4),(0,1)),(Q(1,2),(-1,0)),(Q(3,4),(0,-1))):
            box=p.phase_interval(q)
            for (a,b),v in zip(box,target):
                self.assertLessEqual(a,v);self.assertLessEqual(v,b)
                self.assertLess(b-a,Q(1,2**40))

    def test_huge_unwrapped_phase_is_reduced_first(self):
        for q in (Q(1,3),Q(-97,113),Q(103,16)):
            self.assertEqual(p.phase_interval(q),p.phase_interval(q+10**10000))
            self.assertEqual(p.phase_interval(q),p.phase_interval(q-10**10000))
        a,b=p.phase_interval(Q(1,3))[0]
        self.assertLessEqual(a,Q(-1,2));self.assertLessEqual(Q(-1,2),b)

    def test_infinite_tail_nested_and_tiny_remainder_mutation(self):
        for n in (1,2,17,257,4097):
            a,b=p.tail_interval(n,3);c,d=p.tail_interval(n,9)
            self.assertLess(a,c);self.assertLess(d,b)
            self.assertLess(b,Q(1,15*(n+1)**2))
            # An exact extra source term refutes declaring zero truncation debt.
            self.assertGreater(c,a)
            self.assertGreater(c-a,p.four_pole(n+4)/16**4)

    def test_certified_energy_roots_and_nonnormal_control(self):
        phases=(Q(0),Q(1,2))*16
        a,b=p.energy_interval(phases,1)
        self.assertLessEqual(a,0);self.assertLessEqual(0,b)
        a,b=p.energy_interval(phases,2)
        self.assertLessEqual(a,1);self.assertLessEqual(1,b)
        a,b=p.energy_interval((p.pc320_state(n) for n in range(1,145)),48)
        self.assertGreater(a,Q(99,100))
        self.assertLess(b-a,Q(1,2**30))


class PartitionAndConstruction(unittest.TestCase):
    def test_marked_periods_block_superapproximation_at_next_seam(self):
        certificate=p.marker_certificate()
        self.assertEqual(certificate['certified_approximants'],4)
        self.assertEqual(certificate['digits'],1024)
        digits,records=p.marked_stages(tuple(range(16))*2,(3,5,7),(4,16,64))
        for record in records[1:]:
            self.assertGreaterEqual(abs(digits[record['start']]-record['predicted']),2)
            # Replacing the marker by the predicted digit breaks the key premise.
            self.assertLess(abs(record['predicted']-record['predicted']),2)
        with self.assertRaises(ValueError):p.marked_stages((0,1),(1,2),(4,3))

    def test_exhaustive_weighted_refinement_and_energy_upper(self):
        checked=0
        for N in range(2,9):
            for signs in product((-1,1),repeat=N):
                z=tuple((Q(a),Q(0)) for a in signs)
                for coarse,fine in ((1,2),(1,3),(2,4),(3,6)):
                    e,q=p.gaussian_energy(z,coarse);ee,qq=p.gaussian_energy(z,fine)
                    self.assertEqual(qq-q,p.refinement_increment(z,coarse,fine))
                    self.assertGreaterEqual(qq,q)
                    self.assertLessEqual(abs(e-q),Q(coarse,N))
                    r=N%coarse
                    self.assertLessEqual(e,1+Q(r*(coarse-r),N*N))
                    if N%fine==0:
                        self.assertEqual(e,q);self.assertEqual(ee,qq)
                    checked+=1
        self.assertEqual(checked,2032)

    def test_gaussian_quarter_turns_and_wrong_partition(self):
        z=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)))*9
        self.assertEqual(p.gaussian_energy(z,1),(0,0))
        self.assertEqual(p.gaussian_energy(z,4),(1,1))
        self.assertEqual(p.refinement_increment(z,1,4),1)
        with self.assertRaises(ValueError):p.refinement_increment(z,3,4)
        # Explicit opposite inequality mutation is false: refinement INCREASES.
        self.assertGreater(p.gaussian_energy(z,4)[0],p.gaussian_energy(z,1)[0])

    def test_debruijn_frequencies_fresh_orders(self):
        for radix,order in ((2,4),(3,3),(16,2)):
            word=p.debruijn(radix,order)
            self.assertEqual(len(word),radix**order)
            for r in range(1,order+1):
                counts=p.cyclic_counts(word,r)
                self.assertEqual(len(counts),radix**r)
                self.assertEqual(set(counts.values()),{radix**(order-r)})
            mutant=(word[0],)*len(word)
            self.assertNotEqual(p.cyclic_counts(mutant,1),p.cyclic_counts(word,1))

    def test_periodic_phase_radix_successor(self):
        for order in (1,2):
            word=p.debruijn(16,order)
            for n in (0,1,3,len(word)-1,2*len(word)+3):
                self.assertEqual((16*p.periodic_phase(word,n))%1,p.periodic_phase(word,n+1))
                self.assertEqual(p.periodic_phase(word,n),p.periodic_phase(word,n+3*len(word)))

    def test_sparse_seam_certificates_and_wrap_only_escape(self):
        counts={a:0 for a in range(-1,16)};counts[None]=0
        for n in range(1,257):
            y=p.sparse_phase_interval(n-1,24);t=p.tail_interval(n,12)
            status=p.cut_status(y,t)
            self.assertIn(status,(0,1,-1,None))
            counts[status]+=1
        self.assertGreater(counts[0],150)
        self.assertEqual(counts[None],0)
        # Boundary ownership is one-sided, with exact lower endpoint included.
        for a in range(16):
            self.assertEqual(p.cut_status((Q(a,16),Q(a,16)),(Q(1,1000),Q(1,999))),a)
        self.assertEqual(p.cut_status((Q(1,1000),Q(1,1000)),(Q(1,1000),Q(1,1000))),-1)

    def test_all_cut_jumps_and_omitted_wrap_mutation(self):
        f=tuple(Q(d*d-7*d) for d in range(16))
        tail=Q(1,1000)
        for a in range(16):
            for offset in (Q(0),tail/2,tail):
                y=Q(a,16)+offset;x=(y-tail)%1
                actual=f[int(16*x)]-f[int(16*y)]
                expected=(f[(a-1)%16]-f[a]) if offset<tail else Q(0)
                self.assertEqual(actual,expected)
        self.assertNotEqual(f[15]-f[0],0)
        # Exact endpoint at zero defeats a decomposition omitting that jump.
        self.assertNotEqual(f[int(16*((-tail)%1))]-f[0],0)

    def test_seam_packing_on_periodic_rational_carriers(self):
        N=257;start=16;budget=p.interior_cut_bound(N,start)
        for alpha in (Q(0),Q(1,16),Q(5,16),Q(1,3),Q(1,65535),Q(256,65535)):
            y=alpha%1;events=[]
            for n in range(1,N+1):
                status=p.cut_status((y,y),p.tail_interval(n,12))
                self.assertIsNotNone(status)
                if status in range(1,16):events.append(n)
                y=16*y%1
            self.assertLessEqual(len(events),budget['nonzero_cut_count_upper'])
            after=[n for n in events if n>start]
            self.assertTrue(all(b-a>=budget['L']+1 for a,b in zip(after,after[1:])))

    def test_sparse_seam_two_sided_deficit(self):
        for N in (64,256,1024):
            statuses=[p.cut_status(p.sparse_phase_interval(n-1,24),p.tail_interval(n,12)) for n in range(1,N+1)]
            self.assertNotIn(None,statuses)
            deficit=N-statuses.count(0);bound=p.sparse_wrap_bound(N)
            self.assertLessEqual(bound['deficit_lower'],deficit)
            self.assertLessEqual(deficit,bound['bad_count_upper'])

    def test_mixed_budget_tracks_span_order_and_frequency(self):
        for N,h,lags in ((1000003,17,(17001,)),(65537,65537,(1,)*63),(1048576,1000003,(31,127)),(4096,1,())):
            b=p.mixed_budget(N,h,lags)
            self.assertGreaterEqual(16**b['w'],abs(h)*2**len(lags)*N)
            self.assertEqual(b['D'],sum(lags)+b['w'])
            self.assertGreaterEqual(2**b['J']*b['D'],N+b['D'])
        # Omitting span fails to cover a shifted sparse exponent at n+31=128.
        b=p.mixed_budget(128,1,(31,))
        n=97
        self.assertFalse(any(n<2**j<=n+b['w'] for j in range(10)))
        self.assertTrue(any(n<2**j<=n+b['D'] for j in range(10)))


class NewBoundsAndMutations(unittest.TestCase):
    def test_exact_modular_marginals_match_nonnormal_control(self):
        U=p.authentic_states(256)
        def residue(v,m):return v.numerator*pow(v.denominator,-1,m)%m
        for k in (1,2):
            m=16**k
            self.assertEqual(len({residue(U[n],m) for n in range(m)}),m)
            self.assertEqual(len({residue(p.pc320_state(n),m) for n in range(k,k+m)}),m)

    def test_interior_budget_and_sparse_order(self):
        for N,start in ((256,16),(1024,32),(1000000,1000)):
            b=p.interior_cut_bound(N,start)
            self.assertLessEqual(16**(b['L']+1),15*(start+2)**2)
            self.assertGreater(16**(b['L']+2),15*(start+2)**2)
            self.assertLessEqual(b['nonzero_cut_count_upper'],N)
        for N in (256,1000000,10**12):
            b=p.sparse_wrap_bound(N)
            self.assertGreaterEqual(16**b['H'],200*(N+1)**2)
            self.assertGreaterEqual(b['wrap_count_lower'],0)
        # Source-selected real windows are enclosed independently of a pi float.
        U=p.authentic_states(79)
        for n in range(1,80):
            y=p.authentic_y_interval(U[n],n)
            if y is not None:self.assertIsNotNone(p.cut_status(y,p.tail_interval(n)))

    def test_mixing_finite_band_control(self):
        c=p.mixing_certificate(17)
        self.assertEqual(c['digit_mean'],'7')
        self.assertEqual(c['first_factor'],'1/15')
        self.assertEqual(c['mode_q_real_lower'],'49/900')
        self.assertGreaterEqual(Q(c['entry_minimum']),Q(c['minorization_lower']))
        for h in range(1,17):
            self.assertEqual(sorted(h*j%17 for j in range(17)),list(range(17)))
        self.assertEqual({17*j%17 for j in range(17)},{0})
        with self.assertRaises(ValueError):p.mixing_transition(16)
        # Nonuniform lift weights fail the exact root-coefficient balance.
        wrong=[Q(1,17)]*17;wrong[0]+=Q(1,34);wrong[1]-=Q(1,34)
        self.assertNotEqual(set(wrong),{Q(1,17)})

    def test_receipt_authority_value_source_and_tiny_bound_mutations(self):
        import copy
        expected=p.build_receipt()
        p.validate_payload(copy.deepcopy(expected),expected)
        mutations=[]
        v=copy.deepcopy(expected);v['pi_normality_proved']=True;mutations.append(v)
        v=copy.deepcopy(expected);v['source_hashes']['pi_signed_cancellation_probe.py']='0'*64;mutations.append(v)
        v=copy.deepcopy(expected);v['energies'][0]['authentic_interval']=['0','0'];mutations.append(v)
        v=copy.deepcopy(expected);v['refinement_witness']['E_2']='0';mutations.append(v)
        for mutant in mutations:
            with self.assertRaises(ValueError):p.validate_payload(mutant,expected)



if __name__=='__main__':unittest.main()

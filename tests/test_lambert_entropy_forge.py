"""Hostile and calibrated finite tests: Lambert–W coupon clock × SUCC word entropy."""
import math
import random
import unittest
from fractions import Fraction
from collections import Counter
from observational_succ.lambert_entropy_forge import (
    lambert_w_positive_log, lambert_clock, complete_coverage_reference,
    entropy_diagnostics, entropy_amplification_bound, exact_overlap_returns,
    shannon_block_entropy, sparse_insert_positions,
)


class LambertEntropyForgeTests(unittest.TestCase):
    def setUp(self):
        rng=random.Random(20261108)
        self.digits=[rng.randrange(16) for _ in range(384)]

    def test_lambert_equation(self):
        for n in (1,2,16,256,1024,16384,10**12,10**100):
            w=lambert_w_positive_log(math.log(n)+0.5772156649015328606)
            self.assertAlmostEqual(w+math.log(w),math.log(n)+0.5772156649015328606,delta=3e-13)

    def test_clock_is_source_independent_and_integer_floor(self):
        for n in (256,1024,16384,10**9):
            c=lambert_clock(n)
            self.assertLessEqual(c.integer_depth,c.continuous_depth+1e-8)
            self.assertLessEqual(c.integer_types,c.continuous_types*(1+1e-9))
        self.assertEqual(lambert_clock(16384).integer_depth,2)

    def test_coupon_mean_and_missing_at_threshold(self):
        ref=complete_coverage_reference(3)
        self.assertEqual(ref['types'],4096)
        self.assertTrue(36434<ref['mean_complete_draws']<36435)
        self.assertAlmostEqual(ref['continuum_expected_missing'],math.exp(-0.5772156649015329),places=12)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):lambert_clock(-1)
        with self.assertRaises(ValueError):complete_coverage_reference(4)
        with self.assertRaises(ValueError):entropy_diagnostics([],1)
        with self.assertRaises(ValueError):exact_overlap_returns([1],2,1)
        with self.assertRaises(ValueError):sparse_insert_positions(0)

    def test_exact_collision_identity(self):
        for k in (1,2,3):
            d=entropy_diagnostics(self.digits,k)
            self.assertEqual(d['D'],Fraction(d['collision_sum'])-Fraction(len(self.digits)**2,16**k))
            self.assertEqual(d['energy'],Fraction(16**k,len(self.digits)**2)*d['D'])
            self.assertGreaterEqual(d['D'],0)

    def test_uniform_cyclic_balances(self):
        seq=list(range(16))*20
        self.assertEqual(entropy_diagnostics(seq,1)['D'],0)
        self.assertGreater(entropy_diagnostics(seq,2)['D'],0)

    def test_constant_symbol_mass(self):
        s=[0]*100
        for k in (1,2,3):
            v=entropy_diagnostics(s,k)
            self.assertEqual(v['energy'],Fraction(16**k-1,1))
            self.assertEqual(v['renyi_deficit'],math.log(16**k))

    def test_entropic_amplification_random(self):
        for t in (1,2,3):
            for k in (t,t+1,2*t,2*t+1,9):
                row=entropy_amplification_bound(self.digits,t,k)
                self.assertLessEqual(row['proved_lower_bound'],row['renyi_deficit_k']+1e-10)

    def test_entropic_amplification_coherent(self):
        s=[7]*128
        for t,k in ((1,2),(2,5),(3,11)):
            row=entropy_amplification_bound(s,t,k)
            self.assertGreaterEqual(row['renyi_deficit_k'],row['proved_lower_bound']-1e-10)

    def test_exact_lag_collisions(self):
        for depth in (1,2,3):
            r=exact_overlap_returns(self.digits[:60],depth,10)
            self.assertEqual(r['computed_lags_signed_total']+r['residual_lags_signed_total'],
                             Fraction(r['total_matches_unordered'])-Fraction(r['windows']*(r['windows']-1),2*16**depth))

    def test_lag_mutation(self):
        constant=exact_overlap_returns([1]*60,2,10)
        cycle=exact_overlap_returns(list(range(16))*4,2,10)
        self.assertGreater(constant['D'],cycle['D'])

    def test_counts_cyclic_and_linear_are_different(self):
        x=[0,0,0,1,0]
        c=entropy_diagnostics(x,2)
        l=exact_overlap_returns(x,2,4)
        self.assertNotEqual(c['D'],l['D'])

    def test_reference_multinomial_exact(self):
        # Explicit independent words on {0,1}: E[D] = M(1-1/2).
        M=4
        observed=Fraction(0)
        for mask in range(1<<M):
            counts=Counter((mask>>j)&1 for j in range(M))
            observed+=Fraction(sum(z*z for z in counts.values()))-Fraction(M*M,2)
        self.assertEqual(observed/(1<<M),Fraction(M,2))

    def test_reference_overlapping_exact(self):
        # For each shift, k consecutive overlapping words equal with probability 16^-k,
        # checked here in a binary exhaustive model to distinguish shared coordinates.
        b=2;k=3;L=3
        for shift in range(1,L+1):
            n=k+shift
            matching=0
            for bits in range(1<<n):
                a=tuple((bits>>j)&1 for j in range(k))
                c=tuple((bits>>(shift+j))&1 for j in range(k))
                matching+=(a==c)
            self.assertEqual(matching,2**shift)

    def test_sparse_spike_sizes(self):
        for j in (1,2,3,4,5):
            origin,length=sparse_insert_positions(j)
            self.assertGreater(length,0)
            self.assertLess(length,origin)
            if j>=2:
                self.assertEqual(length,math.isqrt(math.isqrt(origin**3)))

    def test_no_fake_complement_from_coverage(self):
        # All 16 symbols present but maximal coherent concentration.
        a=list(range(16))+[0]*100
        r=entropy_diagnostics(a,1)
        self.assertEqual(r['missing'],0)
        self.assertGreater(r['energy'],10)


if __name__=='__main__':
    unittest.main()

class SourceCertificateTests(unittest.TestCase):
    """Source independence tests distinguish bulk integer BBP from the earlier stepwise implementation."""

    @staticmethod
    def _bulk():
        import importlib.util
        from pathlib import Path
        path=Path(__file__).resolve().parents[1]/'research/2026-11-08/lambert_entropy_forge/bbp_bulk_certificate.py'
        spec=importlib.util.spec_from_file_location('bbp_bulk_certificate',path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        return module

    def test_first_hex_digits_without_digit_oracle(self):
        from pathlib import Path
        cert=self._bulk()
        digits,proof=cert.certified_hex(128)
        self.assertTrue(digits.startswith('243F6A8885A308D3'))
        self.assertEqual(len(digits),128)
        self.assertLess(proof['integer_interval_width'],proof['fractional_cell_width'])

    def test_bulk_matches_existing_per_step_source_prefix(self):
        from pathlib import Path
        cert=self._bulk()
        prior=(Path(__file__).resolve().parents[1]/'research/2026-11-08/zero_origin_spectral_flux/CERTIFIED_HEX_16384.txt').read_text().strip()
        digits,proof=cert.certified_hex(16384)
        self.assertEqual(digits,prior)
        self.assertEqual(proof['K'],16384+24)

    def test_genuine_new_frozen_holdout(self):
        from pathlib import Path
        cert=self._bulk()
        n=40960
        row=Path(__file__).resolve().parents[1]/'research/2026-11-08/lambert_entropy_forge/CERTIFIED_HEX_40960.txt'
        self.assertTrue(row.exists())
        digits,proof=cert.certified_hex(n)
        self.assertEqual(digits,row.read_text().strip())
        self.assertEqual(proof['integer_interval_width'],n+25)

    def test_staggered_lambert_depth_crossing(self):
        self.assertEqual(lambert_clock(32768).integer_depth,2)
        self.assertEqual(lambert_clock(36864).integer_depth,3)
        self.assertEqual(lambert_clock(40960).integer_depth,3)

    def test_coverage_40960(self):
        from pathlib import Path
        path=Path(__file__).resolve().parents[1]/'research/2026-11-08/lambert_entropy_forge/CERTIFIED_HEX_40960.txt'
        if not path.exists():self.skipTest('holdout data not mounted')
        s=path.read_text().strip()
        found=set();t=None
        for i in range(len(s)-2):
            found.add(s[i:i+3])
            if len(found)==4096:
                t=i+3;break
        self.assertEqual(t,31816)
        self.assertEqual(len(found),4096)

    def test_exact_source_40960_collision_energy(self):
        from pathlib import Path
        path=Path(__file__).resolve().parents[1]/'research/2026-11-08/lambert_entropy_forge/CERTIFIED_HEX_40960.txt'
        if not path.exists():self.skipTest('holdout data not mounted')
        ds=[int(v,16) for v in path.read_text().strip()]
        r=entropy_diagnostics(ds,3)
        self.assertEqual(r['D'],40850)
        self.assertEqual(r['energy'],Fraction(817,8192))
        self.assertEqual(r['signed_collision_term'],-50)
        self.assertEqual(r['max_count'],23)

    def test_entropy_bias_amplifies_for_periodic_source(self):
        s=list(range(16))*300
        for t in (1,2):
            a=entropy_amplification_bound(s,t,5)
            self.assertLessEqual(a['proved_lower_bound'],a['renyi_deficit_k']+1e-9)
        # One-digit marginal is exactly uniform but 2-block KL deficit is positive.
        self.assertAlmostEqual(entropy_amplification_bound(s,1,5)['shannon_deficit_t'],0,places=12)
        self.assertGreater(entropy_amplification_bound(s,2,5)['shannon_deficit_t'],2)

class DenseCheckpointAndEntropyTests(unittest.TestCase):
    def test_cyclic_checkpoint_transport_exact_bound(self):
        from observational_succ.bbp_word_spectroscopy import word_counts_cyclic
        rng=random.Random(99)
        x=[rng.randrange(16) for _ in range(350)]
        for t in (1,2,3,4):
            for n,m in ((20,21),(128,137),(250,349)):
                a=word_counts_cyclic(x[:n],t)
                b=word_counts_cyclic(x[:m],t)
                lhs=sum(abs(Fraction(a[w],n)-Fraction(b[w],m)) for w in a.keys()|b.keys())
                rhs=Fraction(2*(m-n)+2*(t-1),m)
                self.assertLessEqual(lhs,rhs)

    def test_pinsker_bound_actual_distribution(self):
        from observational_succ.bbp_word_spectroscopy import word_counts_cyclic
        rng=random.Random(20)
        x=[rng.randrange(16) for _ in range(512)]
        for t in (1,2):
            for k in (t,3,5,7):
                row=entropy_amplification_bound(x,t,k)
                count=word_counts_cyclic(x,t)
                B=16**t
                l1=sum(abs(count.get(tuple([(w//16**j)%16 for j in range(t)][::-1]),0)/512-1/B)
                       for w in range(B))
                self.assertLessEqual(l1,row['pinsker_l1_upper']+1e-10)

    def test_max_multiplicity_entropy_bound(self):
        rng=random.Random(600)
        ds=[rng.randrange(16) for _ in range(1024)]
        for k in (1,2,3):
            obs=entropy_diagnostics(ds,k)
            self.assertLessEqual(1+obs['energy'],Fraction(16**k*obs['max_count'],len(ds)))

    def test_integer_minimum_energy_quantization(self):
        rng=random.Random(3)
        for n in (16,25,64,128,300):
            xs=[rng.randrange(16) for _ in range(n)]
            for k in (1,2):
                B=16**k
                r=n%B
                e=entropy_diagnostics(xs,k)['energy']
                self.assertGreaterEqual(e,Fraction(r*(B-r),n*n))

    def test_preregistered_source_receipt_schema(self):
        from pathlib import Path
        import json
        p=Path(__file__).resolve().parents[1]/'research/2026-11-08/lambert_entropy_forge/FINITE_RECEIPT_40960.json'
        self.assertTrue(p.exists())
        x=json.loads(p.read_text())
        self.assertEqual(x['protocol_commit'],'c207e377143818f95ec12957849834e1d3113661')
        self.assertEqual(x['digit_count'],40960)
        self.assertEqual(len(x['shuffled_controls']),16)
        self.assertEqual(x['checkpoints']['40960']['clock']['integer_depth'],3)

class TrimmedCyclicHostileTests(unittest.TestCase):
    def test_cyclic_trim_bound_arbitrary_controls(self):
        from observational_succ.lambert_entropy_forge import trimmed_cyclic_entropy_bound
        rng=random.Random(123)
        for xs in ([0]*100+[rng.randrange(16) for _ in range(1200)],
                   [rng.randrange(16) for _ in range(1300)],
                   list(range(16))*81+[1,2,3,4]):
            for depth,t in ((2,1),(3,1),(3,2)):
                for threshold in (1,3,10):
                    row=trimmed_cyclic_entropy_bound(xs,depth,threshold,t)
                    self.assertGreaterEqual(row['max_allowed_kl']+1e-9,row['kl_full_fixed_depth'])
                    self.assertEqual(row['retained']+row['discarded'],len(xs))

    def test_spike_removed_without_spurious_normality(self):
        from observational_succ.lambert_entropy_forge import trimmed_cyclic_entropy_bound
        rng=random.Random(995)
        xs=[rng.randrange(16) for _ in range(8192)]+[0]*500
        row=trimmed_cyclic_entropy_bound(xs,3,15,1)
        self.assertGreater(row['discarded'],300)
        self.assertLess(float(row['discarded_fraction']),0.1)
        self.assertLess(float(row['collision_excess_retained']),float(row['untrimmed_collision_excess']))
        # This is a finite synthetically spiked sample, not a proof of source normality.

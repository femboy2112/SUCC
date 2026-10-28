"""Independent arithmetic/period/source-oracle checks; no normality assertions."""
from __future__ import annotations

import math
import unittest
from fractions import Fraction as Q
from observational_succ import pi_ternary_handle as h

# OEIS A004602 (integer 10 followed by this fractional base-3 prefix).
OEIS_HEAD = '0102110122220102110021111102212222201'

class ExactTernaryPi(unittest.TestCase):
    def test_sixth_tap_source_dual(self):
        for k in [0,1,4,13,40,121,364,729]:
            linear,quadratic=h.sixth_slot_dual(k)
            self.assertEqual(linear,Q(-2,2*k+1))
            self.assertEqual(quadratic,Q(-2,(2*k+1)**2))
            self.assertEqual(quadratic, -Q(1,2*k+1)*(-linear))

    def test_pole_depth_both_real_ternary_bbp_sources(self):
        for r in range(1,13):
            k=(3**r-1)//2
            self.assertEqual(h.ternary_pole_depth(k),r)
            a,b=h.sixth_slot_dual(k)
            self.assertEqual(a,Q(-2,3**r))
            self.assertEqual(b,Q(-2,3**(2*r)))
        for L in range(1,7):
            dist=h.source_pole_distribution(L)
            self.assertEqual(sum(dist.values()),3**L)
            from collections import Counter
            self.assertEqual(dict(Counter(min(h.ternary_pole_depth(k),L) for k in range(3**L))),dist)

    def test_first_digit_head_four_independent_sources(self):
        digits,certs=h.digit_range(1,len(OEIS_HEAD))
        self.assertEqual(digits,OEIS_HEAD)
        self.assertEqual(len(certs),4)
        self.assertEqual(len({c.floor_lower for c in certs}),1)
        for c in certs:
            self.assertEqual(c.floor_lower,c.floor_upper)
            self.assertEqual(c.as_dict()['certified'],True)

    def test_long_ternary_holdout_multiple_sources(self):
        for digits in (1,3,9,31,63,96,129):
            certs=[h.certify_prefix(digits,s) for s in h.SOURCES]
            self.assertEqual(len({c.prefix for c in certs}),1)
            self.assertTrue(certs[0].prefix.startswith(OEIS_HEAD[:min(len(OEIS_HEAD),digits)]))

    def test_requested_offset_window(self):
        data,certs=h.digit_range(10,27)
        self.assertEqual(data,OEIS_HEAD[9:36])
        self.assertEqual(data,certs[0].prefix[9:36])

    def test_exact_sqrt_floor_algebraic(self):
        for denom in (1,3,5,11,17):
            for num in (0,1,2,9,53,333,789):
                v=Q(num,denom)
                for scale in (1,3,27,243):
                    x=h.floor_scaled_pi(v,scale,'pi-square')
                    self.assertLessEqual(x*x,scale*scale*v)
                    self.assertGreater((x+1)**2,scale*scale*v)
                    y=h.floor_scaled_pi(v,scale,'pi-root3')
                    self.assertLessEqual(3*y*y,scale*scale*v*v)
                    self.assertGreater(3*(y+1)**2,scale*scale*v*v)

    def test_machin_exact_alternating_oracle(self):
        for k in (1,2,3,5,7,12):
            a=h.machin_interval(k)
            b=h.original_bbp_interval(k)
            self.assertLessEqual(a.low,b.high)
            self.assertLessEqual(b.low,a.high)

    def test_ternary_pi2_pisqrt3_against_machin(self):
        for k in (2,4,8,14):
            mx=h.machin_interval(k*3)
            scale=3**(min(25,3*k))
            # Root floor intervals must be compatible, even before digits certify.
            mi=(h.floor_scaled_pi(mx.low,scale,mx.form),h.floor_scaled_pi(mx.high,scale,mx.form))
            for source in ('ternary-pi2','ternary-pisqrt3'):
                interval=h.interval_for(source,k)
                self.assertGreater(interval.low,0)
                ni=(h.floor_scaled_pi(interval.low,scale,interval.form),h.floor_scaled_pi(interval.high,scale,interval.form))
                self.assertLessEqual(ni[0],mi[1]);self.assertLessEqual(mi[0],ni[1])

    def test_source_mutation_rejected(self):
        k=7
        true=h.ternary_pi2_interval(k)
        false=h.bbp_interval(k,coefficients=(244,)+h.TERNARY_PI2[1:],
             degree=2,base=729,prefactor=Q(2,27),source='ternary-pi2',form='pi-square')
        self.assertGreater(false.low,true.high)
        # A sign mutation of the original BBP pole must break agreement.
        signed=h.original_bbp_interval(k)
        mutated=h.bbp_interval(k,coefficients=(4,0,0,-2,-1,1,0,0),
             degree=1,base=16,prefactor=Q(1),source='original-bbp',form='direct')
        self.assertGreater(mutated.low,signed.high)

    def test_certificate_replay_mutations(self):
        import sys
        from pathlib import Path
        sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
        import verify_pi_ternary_certificate as ver
        data,hits=h.digit_range(17,25)
        record={'policy':'source-exact certified ternary digits; NOT BBP-style random access or pi normality',
                'start':17,'count':25,'digits':data,'witnesses':[c.as_dict() for c in hits]}
        self.assertTrue(ver.verify(record)['certified'])
        import json
        def mutant(): return json.loads(json.dumps(record))
        changed=mutant(); changed['digits']='2'+changed['digits'][1:]
        with self.assertRaises(ValueError):ver.verify(changed)
        changed=mutant();changed['witnesses'][0]['exact_lower']='0/1'
        with self.assertRaises(ValueError):ver.verify(changed)
        changed=mutant();changed['witnesses'][0]['terms']+=1
        with self.assertRaises(ValueError):ver.verify(changed)
        changed=mutant();changed['witnesses'][1]['base3_pi']='10.2'
        with self.assertRaises(ValueError):ver.verify(changed)
        changed=mutant();changed['witnesses'][0]['certified']=False
        with self.assertRaises(ValueError):ver.verify(changed)

    def test_heldout_position_1000_without_float(self):
        out = h.certify_prefix(1000, 'ternary-pi2')
        self.assertEqual(out.prefix[-2:], '10')
        self.assertEqual(out.floor_lower,out.floor_upper)

    def test_invalid_inputs_and_budget(self):
        for start,count in [(0,3),(1,0),(-1,1),(4096,2)]:
            with self.assertRaises(ValueError):h.digit_range(start,count)
        with self.assertRaises(ValueError):h.certify_prefix(1,'not-real')
        with self.assertRaises(ValueError):h.ternary_word(3,1)
        with self.assertRaises(ArithmeticError):h.certify_prefix(100,'ternary-pi2',max_terms=1)

if __name__=='__main__':unittest.main()

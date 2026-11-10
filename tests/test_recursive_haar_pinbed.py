"""Exact, source-anchored recursive Haar disintegration controls.

The outcomes are structural theorems and finite observations, never a
claim of base-16 normality for the original zero-seeded BBP orbit.
"""
import hashlib
import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from random import Random

from observational_succ.recursive_haar_pinbed import (
    canonical_law, normalized_atoms, interval_w1, interval_w1_haar,
    shift_law, uniform_inverse_law, digit_averaging_law,
    sharp_recursive_haar_certificate, conditional_first_digit_defect,
    word_l1_uniform, word_energy, recursive_cylinder_certificate,
    periodic_completed_point, periodic_orbit_law, word_counts_cyclic,
    grouped_bbp_forcing, grouped_bbp_orbit,
)
from observational_succ.duck_bbp import forcing, source_tail_budget

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'research/2026-11-09/recursive_haar_pinbed'


def de_bruijn(k, n):
    alphabet=[0]*(k*n)
    result=[]
    def visit(t,p):
        if t>n:
            if n%p==0: result.extend(alphabet[1:p+1])
        else:
            alphabet[t]=alphabet[t-p]
            visit(t+1,p)
            for j in range(alphabet[t-p]+1,k):
                alphabet[t]=j;visit(t+1,t)
    visit(1,1)
    return result


class RecursiveHaar(unittest.TestCase):
    def test_T_C_split_identity(self):
        for data in ((F(0),),(F(1,7),F(4,9)),(F(1,32),F(4,13),F(997,1000))):
            law=canonical_law(data)
            self.assertEqual(shift_law(uniform_inverse_law(law)),law)

    def test_Q_is_two_equivalent_constructions(self):
        for data in ((F(0),),(F(1,17),F(2,5)),(F(1,3),F(7,15),F(11,32))):
            law=canonical_law(data)
            self.assertEqual(digit_averaging_law(law),uniform_inverse_law(shift_law(law)))
            self.assertEqual(digit_averaging_law(digit_averaging_law(law)),digit_averaging_law(law))

    def test_sharp_coherent_source_control(self):
        law=canonical_law([F(0)])
        r=sharp_recursive_haar_certificate(law)
        self.assertEqual(r['symmetry_defect'],F(15,32))
        self.assertEqual(r['stationarity_defect'],0)
        self.assertEqual(r['distance_to_haar'],F(1,2))
        self.assertEqual(r['distance_to_haar'],r['rigidity_upper_bound'])

    def test_sharp_digit_grid_control(self):
        law=canonical_law([F(a,16) for a in range(16)])
        r=sharp_recursive_haar_certificate(law)
        self.assertEqual(r['symmetry_defect'],0)
        self.assertEqual(r['stationarity_defect'],F(15,32))
        self.assertEqual(r['distance_to_haar'],F(1,32))
        self.assertEqual(r['distance_to_haar'],r['rigidity_upper_bound'])

    def test_exact_interval_wasserstein_simple(self):
        self.assertEqual(interval_w1(canonical_law([F(0)]),canonical_law([F(1,2)])),F(1,2))
        self.assertEqual(interval_w1_haar(canonical_law([F(1,2)])),F(1,4))

    def test_C_contraction(self):
        rng=Random(20261109)
        for _ in range(12):
            a=canonical_law([F(rng.randrange(1024),1024) for j in range(7)])
            b=canonical_law([F(rng.randrange(1024),1024) for j in range(6)])
            self.assertLessEqual(interval_w1(uniform_inverse_law(a),uniform_inverse_law(b)),interval_w1(a,b)/16)
            self.assertLessEqual(sharp_recursive_haar_certificate(a)['distance_to_haar'],sharp_recursive_haar_certificate(a)['rigidity_upper_bound'])

    def test_periodic_16_digits_one_digit_uniform_not_two(self):
        seq=list(range(16))*8
        self.assertEqual(conditional_first_digit_defect(seq,0),0)
        self.assertEqual(conditional_first_digit_defect(seq,1),F(15,8))
        self.assertEqual(word_l1_uniform(seq,1),0)
        self.assertEqual(word_l1_uniform(seq,2),F(15,8))
        p=periodic_orbit_law(tuple(range(16)))
        self.assertEqual(shift_law(p),p)
        self.assertNotEqual(digit_averaging_law(p),p)
        self.assertGreater(interval_w1_haar(p),0)

    def test_debruijn_two_digit_uniform_but_third_not(self):
        seq=de_bruijn(16,2)
        self.assertEqual(len(seq),256)
        self.assertEqual(word_l1_uniform(seq,1),0)
        self.assertEqual(word_l1_uniform(seq,2),0)
        self.assertEqual(conditional_first_digit_defect(seq,1),0)
        self.assertEqual(conditional_first_digit_defect(seq,2),F(15,8))
        self.assertEqual(word_l1_uniform(seq,3),F(15,8))

    def test_normality_is_not_implied_by_one_digit_Haar_even_with_mixing(self):
        # Stationary uniform marginal Markov chain, every transition positive,
        # spectral gap 1/2 (full-support exponentially mixing but nonHaar).
        T=[[F(1,32)+(F(1,2) if a==b else 0) for b in range(16)] for a in range(16)]
        self.assertEqual([sum(row) for row in T],[F(1)]*16)
        self.assertEqual([sum(T[a][b] for a in range(16))/16 for b in range(16)], [F(1,16)]*16)
        self.assertEqual(sum(abs(T[a][b]/16-F(1,256)) for a in range(16) for b in range(16)),F(15,16))

    def test_cylinder_all_depths_recursion_monotonicity(self):
        rng=Random(137)
        for data in (list(range(16))*4, [0]*64, [rng.randrange(16) for _ in range(128)]):
            for depth in (1,2,3,4):
                r=recursive_cylinder_certificate(data,depth)
                self.assertLessEqual(r['word_l1'],r['sum_defect_upper'])
                self.assertLessEqual(r['word_l1'],r['single_deep_defect_upper'])
                self.assertLessEqual(r['defects'][-1]**2,r['new_coordinate_energy'])

    def test_energy_identity_direct_integer(self):
        rng=Random(191)
        digits=[rng.randrange(16) for _ in range(72)]
        for j in range(4):
            lo=word_counts_cyclic(digits,j)
            hi=word_counts_cyclic(digits,j+1)
            b=16**j
            count=sum((16*hi.get(a*b+w,0)-v)**2 for w,v in lo.items() for a in range(16))
            self.assertEqual(word_energy(digits,j+1)-word_energy(digits,j),F(16**j*count,16*len(digits)**2))

    def test_original_source_is_same_four_poles(self):
        for n in range(1,110):
            a=8*n-7
            self.assertEqual(forcing(n),4*F(1,a)-2*F(1,a+3)-F(1,a+4)-F(1,a+5))
        for n in range(2,110):
            self.assertLess(forcing(n+1),forcing(n))

    def test_original_source_completed_digits_authenticated(self):
        # RATIONAL original four-pole series and source-tail enclosure only.
        # The BBP=pi identity is a separately imported classical fact.
        terms=48
        alpha=sum((forcing(j)/16**j for j in range(1,terms+1)), F())
        alpha_tail=source_tail_budget(terms)/16**terms
        digits=[]
        for n in range(1,25):
            lo=16**(n+1)*alpha
            hi=lo+16**(n+1)*alpha_tail
            self.assertEqual(lo.numerator//lo.denominator,hi.numerator//hi.denominator)
            digits.append(lo.numerator//lo.denominator%16)
        self.assertEqual(''.join(format(d,'X') for d in digits),'243F6A8885A308D313198A2E')

    def test_completed_source_proxy_quantitative_defect(self):
        terms=84
        alpha=sum((forcing(j)/16**j for j in range(1,terms+1)), F())
        # Proxy is a rational approximation to pi/16; NO claim it is pi.
        phases=[(16**n*alpha)%1 for n in range(1,49)]
        law=canonical_law(phases)
        r=sharp_recursive_haar_certificate(law)
        self.assertLessEqual(r['stationarity_defect'],F(1,len(phases)))
        self.assertGreater(r['symmetry_defect'],0)

    def test_certified_sibling_40960_prefix_and_replay(self):
        data=(FOLDER/'CERTIFIED_HEX_40960.txt').read_text(encoding='ascii').strip()
        self.assertEqual(len(data),40960)
        self.assertEqual(hashlib.sha256((data+'\n').encode('ascii')).hexdigest(),
                         'c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527')
        digits=[int(c,16) for c in data]
        obs=[conditional_first_digit_defect(digits,j) for j in range(5)]
        self.assertEqual(obs,[F(6592,655360),F(40150,655360),F(160022,655360),F(659862,655360),F(1181966,655360)])
        self.assertEqual(word_l1_uniform(digits,1),obs[0])
        self.assertLess(obs[0],obs[1])
        self.assertLess(obs[1],obs[2])

    def test_40960_receipt_replay(self):
        data=(FOLDER/'CERTIFIED_HEX_40960.txt').read_text(encoding='ascii').strip()
        digits=[int(c,16) for c in data]
        actual={
            'source_digit_sha256':hashlib.sha256((data+'\n').encode()).hexdigest(),
            'n':len(digits),
            'defect_numerators_over_16n':[
                int(conditional_first_digit_defect(digits,j)*16*len(digits)) for j in range(5)],
            'word_one_l1_numerator':int(word_l1_uniform(digits,1)*16*len(digits)),
            'periodic_16_one_digit_defect':'0',
            'periodic_16_two_digit_defect':'15/8',
        }
        expected=json.loads((FOLDER/'FINITE_RECEIPT.json').read_text(encoding='utf8'))
        self.assertEqual(actual,expected)

    def test_exact_grouped_two_digit_bbp_is_one_base256_recurrence(self):
        # Independent direct original four-pole iteration, not grouped implementation.
        u=[F()]
        for n in range(1,71):
            a=8*n-7
            u.append(16*u[-1]+4*F(1,a)-2*F(1,a+3)-F(1,a+4)-F(1,a+5))
        for g in (1,2,3,4,5,7):
            grouped=grouped_bbp_orbit(70//g,g)
            self.assertEqual(grouped,tuple(u[g*k] for k in range(70//g+1)))
            for k in range(1, min(8,70//g+1)):
                expected=sum((16**(g-j)*forcing(g*(k-1)+j)
                              for j in range(1,g+1)),F())
                self.assertEqual(grouped_bbp_forcing(k,g),expected)
        self.assertEqual(grouped_bbp_forcing(1,2),16*forcing(1)+forcing(2))

    def test_quantile_transport_agrees_with_cdf_w1_oracle(self):
        # Independent optimal 1D monotone coupling, rather than integrating CDF gaps.
        def quantile_w1(a,b):
            i=j=0
            ra=a[0][1]; rb=b[0][1]
            total=F()
            while i<len(a) and j<len(b):
                amount=min(ra,rb)
                total += amount*abs(a[i][0]-b[j][0])
                ra -= amount; rb -= amount
                if not ra:
                    i += 1
                    if i<len(a):ra=a[i][1]
                if not rb:
                    j += 1
                    if j<len(b):rb=b[j][1]
            self.assertEqual((i,j),(len(a),len(b)))
            return total
        rng=Random(421)
        for _ in range(16):
            a=canonical_law([F(rng.randrange(97),97) for q in range(6)])
            b=canonical_law([F(rng.randrange(97),97) for q in range(9)])
            self.assertEqual(quantile_w1(a,b),interval_w1(a,b))
            self.assertEqual(quantile_w1(a,uniform_inverse_law(b)),interval_w1(a,uniform_inverse_law(b)))

    def test_exact_sixteen_branch_coalescence_cannot_create_Haar(self):
        from observational_succ.recursive_haar_pinbed import shift_law, normalized_atoms
        for y in (F(0),F(5,7),F(41,128)):
            branches=[(F(a+y,16),F(1,16)) for a in range(16)]
            self.assertEqual(shift_law(normalized_atoms(branches)),canonical_law([y]))
            if y==0:
                # All 16 first-digit choices share the same *coherent* future.
                self.assertEqual(sharp_recursive_haar_certificate(canonical_law([y]))['distance_to_haar'],F(1,2))

    def test_conditional_signed_fourier_pins_invert_exact_counts(self):
        from math import pi
        from cmath import exp
        digs=list(range(16))*4
        for j in (0,1,2):
            lo=word_counts_cyclic(digs,j)
            hi=word_counts_cyclic(digs,j+1)
            base=16**j; N=len(digs)
            for w, ct in lo.items():
                p=[F(hi.get(a*base+w,0),N) for a in range(16)]
                G=[sum((complex(p[a])*exp(2j*pi*h*a/16)
                            for a in range(16)),0j) for h in range(1,16)]
                for a in range(16):
                    actual=float(p[a]-F(ct,16*N))
                    rebuilt=sum((exp(-2j*pi*(h+1)*a/16)*G[h]
                                 for h in range(15)),0j)/16
                    self.assertLess(abs(rebuilt-actual),1e-12)

    def test_bad_inputs(self):
        with self.assertRaises(ValueError):canonical_law([])
        with self.assertRaises(ValueError):word_counts_cyclic([16],1)
        with self.assertRaises(ValueError):conditional_first_digit_defect([0],1)
        with self.assertRaises(ValueError):normalized_atoms([(F(0),F(1,2))])
        with self.assertRaises(ValueError):normalized_atoms([(F(1),F(1))])

if __name__=='__main__':unittest.main()

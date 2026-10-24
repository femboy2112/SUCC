"""Independent exact combinatorial and authentic-source Pascal carry tests."""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb
import unittest

from observational_succ.pascal_carry_interferometry import (
    base_p_digits, binomial_valuation, branch_gate_counts,
    even_parity_countermodel, finite_difference, forcing_difference,
    forcing_difference_upper, forcing_pascal_certificate,
    invert_walsh, kummer_carries, lucas_mod_p, pascal_row,
    pascal_source_jet, prime_clock_pascal_gain, signed_jet_remainder_upper,
    signed_shells_from_gates, signed_shells_from_walsh,
    source_pascal_tomography, walsh_moments, walsh_pascal_certificate,
)
from observational_succ.pi_dyadic_prime_transfer import (
    _bbp_forcing, _bbp_states, dyadic_carry_branch_certificate,
)


class PascalPrimeArithmetic(unittest.TestCase):
    def test_pascal_row_sums_and_mod2_popcount(self):
        for n in range(129):
            row=pascal_row(n)
            self.assertEqual(sum(row),1 << n)
            self.assertEqual(sum(c%2 for c in row),1<<n.bit_count())
            self.assertEqual(len(row),n+1)
        self.assertEqual(pascal_row(4),(1,4,6,4,1))

    def test_lucas_independent_direct_modular(self):
        for p in (2,3,5,7,11,13,17):
            for n in range(80):
                for k in range(n+1):
                    self.assertEqual(lucas_mod_p(n,k,p),comb(n,k)%p)
                digits=base_p_digits(n,p)
                self.assertEqual(sum(lucas_mod_p(n,k,p)!=0 for k in range(n+1)),
                                 __import__('math').prod(x+1 for x in digits))

    def test_kummer_against_independent_factorial_valuation(self):
        from math import factorial
        def vp_factorial(n,p):
            s=0
            while n:
                n//=p
                s+=n
            return s
        for p in (2,3,5,7,11,13):
            for n in range(1,80):
                for k in range(n+1):
                    reference=vp_factorial(n,p)-vp_factorial(k,p)-vp_factorial(n-k,p)
                    self.assertEqual(kummer_carries(n,k,p),reference)
                    self.assertEqual(binomial_valuation(n,k,p),reference)

    def test_bad_domains(self):
        for p in (1,4,9):
            with self.assertRaises(ValueError):
                lucas_mod_p(12,6,p)
        with self.assertRaises(ValueError):
            kummer_carries(2,3,2)
        with self.assertRaises(ValueError):
            walsh_moments((1,2,3))


class WalshFourBitTomography(unittest.TestCase):
    def test_all_sixteen_masks_single_and_paired_carry(self):
        import random
        rng=random.Random(10241024)
        candidates=[[1]*16,[16]+[0]*15,
                    [2 if k.bit_count()%2 == 0 else 0 for k in range(16)]]
        candidates += [[rng.randrange(0,30) for _ in range(16)] for _ in range(20)]
        for hist in candidates:
            cert=walsh_pascal_certificate(hist)
            self.assertEqual(tuple(hist),tuple(invert_walsh(walsh_moments(hist))))
            self.assertEqual(cert['shells'],signed_shells_from_gates(cert['gates']))
            self.assertEqual(cert['shells'],signed_shells_from_walsh(cert['walsh_moments']))
            self.assertEqual(sum(cert['pascal_order_contributions']),16*hist[0])
            self.assertEqual(cert['zero_branch_excess'],16*hist[0]-sum(hist))

    def test_three_wise_balanced_fourth_order_counterexample(self):
        evil=even_parity_countermodel()
        self.assertEqual(evil['pascal_order_contributions'],(16,0,0,0,16))
        self.assertEqual(evil['hist'][0],2)
        self.assertEqual(sum(evil['hist']),16)
        self.assertNotEqual(evil['hist'][0],1)
        # Every one-, two-, and three-bit marginal is exactly uniform.
        for mask in range(1,16):
            if mask.bit_count()<4:
                self.assertEqual(evil['walsh_moments'][mask],0)
        # Mutate one observation and ensure the fourth-order contrast changes.
        mutant=list(evil['hist'])
        mutant[0]-=1
        mutant[1]+=1
        self.assertNotEqual(walsh_moments(mutant)[15],16)

    def test_actual_selected_bbp_9_rows_and_negative_first_shell(self):
        for p in (41,97,257):
            for tau in (Q(1,4),Q(1,16),Q(1,64)):
                reference=dyadic_carry_branch_certificate(p,tau)
                current=source_pascal_tomography(p,tau)
                self.assertEqual(tuple(reference['dyadic_nested_counts']),current['branch_counts'])
                self.assertEqual(tuple(reference['ramanujan_shells']),current['primitive_shells'])
                self.assertEqual(reference['branch_histogram'][0],current['zero_branch_count'])
        self.assertEqual(source_pascal_tomography(97,Q(1,16))['primitive_shells'][0],-7)


class PascalBBPSource(unittest.TestCase):
    def test_hausdorff_complete_monotone_forcing_differences(self):
        for n in (1,2,5,13,33,128):
            for k in range(0,9):
                cert=forcing_pascal_certificate(n,k)
                delta=forcing_difference(n,k)
                self.assertEqual(cert['sign'],(-1)**k)
                self.assertGreater((-1)**k*delta,0)
                self.assertLess((-1)**k*delta,forcing_difference_upper(n,k))
                self.assertLessEqual((-1)**k*delta,_bbp_forcing(n))

    def test_source_pascal_jet_integer_fraction(self):
        for n in (0,1,3,7,13,33):
            for k in (1,2,3,4,6):
                result=pascal_source_jet(n,k)
                self.assertTrue(result['identity_verified'])

    def test_initial_selector_3_and_5_aliases_and_p_clock(self):
        # With the identical nonautonomous forcing, an initial c with 15c integer
        # remains a constant c shift for all n. Differences cannot see it.
        for q in (3,5,15):
            ordinary=_bbp_states(12)
            shifted=[Q(1,q)]
            for n in range(1,13):
                shifted.append((16*shifted[-1]+_bbp_forcing(n))%1)
            self.assertTrue(all((shifted[n]-ordinary[n])%1==Q(1,q)
                                for n in range(13)))
            for k in (1,2,3,4):
                self.assertEqual((finite_difference(tuple(shifted),2,k)-
                                  finite_difference(ordinary,2,k))%1,Q(0))
        for p in (3,5,7,11,13,17,41,97):
            for k in (1,2,3,4):
                r=prime_clock_pascal_gain(p,2,k)
                if p in (3,5):
                    self.assertTrue(r['annihilated_all_t'])
                    self.assertEqual(r['residue'],0)
                else:
                    self.assertTrue(r['p_clock_invertible_gain'])
                    self.assertNotEqual(r['residue'],0)

    def test_jet_rational_bound_and_guards(self):
        for p in (41,97,257):
            for tau in (Q(1,4),Q(1,16),Q(1,64)):
                row=source_pascal_tomography(p,tau)
                exact=Q(row['second_order_jet_error_upper'])
                self.assertGreater(exact,0)
                self.assertLess(exact,
                    signed_jet_remainder_upper(row['window_length'],tau,
                    Q(dyadic_carry_branch_certificate(p,tau)['forcing_drift']),2))
        with self.assertRaises(ValueError):
            signed_jet_remainder_upper(3,Q(1,2),Q(1,100))

    def test_taylor_jet_matches_exact_phase_small_finite_probe(self):
        # Non-certified floating diagnostic ONLY: mathematical error bound above
        # is an analytic theorem with exact-rational outward constants.
        from cmath import exp, pi
        from math import factorial
        from observational_succ.pi_dyadic_prime_transfer import _centered
        p=41
        m=(p-1)//8
        a,b=m+1,4*m
        y=_bbp_states(b)
        eps=_bbp_forcing(a+1)-_bbp_forcing(b)
        tau=Q(1,64)
        self.assertLess(eps,tau)
        H=[h for h in range(-7,9) if h!=0]
        source_sum=0j
        count=0
        for s in range(a,b):
            for t in range(a,b):
                delta=_centered(y[t]-y[s]); nxt=_centered(y[t+1]-y[s+1])
                if abs(nxt)>tau:
                    continue
                eta=_bbp_forcing(t+1)-_bbp_forcing(s+1)
                count+=1
                for h in H:
                    z=2*pi*float(Q(h,16)*(eta-nxt))
                    phase=exp(2j*pi*h*float(delta))
                    source_sum+=phase*(1+1j*z-z*z/2)
        cert=dyadic_carry_branch_certificate(p,tau)
        truth=16*cert['zero_centered_branch']-sum(cert['branch_histogram'])
        bound=signed_jet_remainder_upper(b-a,tau,eps,2,count)
        self.assertLess(abs(source_sum.real-truth),float(bound)+1e-8)
        self.assertLess(abs(source_sum.imag),1e-7)


if __name__=='__main__':
    unittest.main()

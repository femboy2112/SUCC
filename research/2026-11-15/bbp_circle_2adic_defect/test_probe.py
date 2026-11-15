"""Exact and independent-formula checks for BBP circle/2-adic research."""
import cmath
import math
import unittest
from fractions import Fraction

from probe import (forcing, forcing_four_poles, mod_fraction, stable_clock,
                   lifted_states, green_bounds, certified_prefix, global_prefix,
                   reverse_digits, seam_delta, bridge, bridge_direct,
                   character_means, critical_depth, shell_receipt)


class BbpSourceTests(unittest.TestCase):
    def test_original_four_poles(self):
        for n in range(1,251):
            self.assertEqual(forcing(n), forcing_four_poles(n))
            self.assertEqual(forcing(n).denominator % 2,1)
            if n >= 2:
                self.assertGreater(forcing(n),0)
                self.assertLess(forcing(n), forcing(n-1))

    def test_forcing_isometry_on_2adic_integer_samples(self):
        q=4096
        for n in range(-9,41):
            for m in range(-9,41):
                self.assertEqual(math.gcd(n-m,q),
                                 math.gcd(mod_fraction(forcing(n),q)-
                                          mod_fraction(forcing(m),q),q))

    def test_completed_padic_clock_is_permutation(self):
        for k in (1,2,3):
            q=16**k
            residues=[stable_clock(n,k) for n in range(q)]
            self.assertEqual(len(set(residues)),q)
            for n in (0,1,7,17,q-1,q+3):
                self.assertEqual(stable_clock(n,k),stable_clock(n+q,k))

    def test_zero_seed_bonds_to_stable_clock(self):
        states=lifted_states(65)
        for k in (1,2,3):
            q=16**k
            for n in range(k,65):
                self.assertEqual(mod_fraction(states[n],q),stable_clock(n,k))
        self.assertEqual(states[0],0)
        self.assertEqual(states[1],Fraction(47,15))

    def test_arithmetic_and_symbolic_2adic_are_distinct(self):
        state=lifted_states(1)[1]
        self.assertEqual(mod_fraction(state,16),1)
        self.assertEqual(reverse_digits((16*(state%1)).numerator//
                                        (16*(state%1)).denominator,1),2)

    def test_source_seed_alias_is_preserved_in_root_passport(self):
        original=lifted_states(15)
        alias=lifted_states(15,Fraction(1,16))
        for n in range(1,16):
            self.assertEqual(alias[n]-original[n],16**(n-1))
            self.assertEqual(alias[n]%1,original[n]%1)
            if n>=2:
                self.assertEqual(mod_fraction(alias[n]-original[n],16**(n-1)),0)
        self.assertNotEqual(alias[0],original[0])


class CircleSymbolicTests(unittest.TestCase):
    def test_digit_reverse_involution(self):
        for k in (1,2):
            for a in range(16**k):
                self.assertEqual(reverse_digits(reverse_digits(a,k),k),a)

    def test_seam_gap_quantization(self):
        for k in (1,2,3):
            q=16**k
            samples=set((0,1,15,16,31,255,256,q-1,q-2,q//2))
            for a in samples:
                if not 0<=a<q:continue
                delta,m=seam_delta(a,k)
                self.assertEqual(delta,(reverse_digits((a+1)%q,k)-
                                        reverse_digits(a,k))%q)
                if a==q-1:
                    self.assertEqual((delta,m),(1,0))
                else:
                    self.assertEqual(math.gcd(delta,q),16**(m-1))

    def test_noncommutation_except_global_seam(self):
        # A real-circle grid increment is not a compatible Z_16 successor.
        self.assertNotEqual(reverse_digits(1,2)%16,reverse_digits(1,1))
        for k in (1,2,3):
            self.assertEqual(seam_delta(16**k-1,k),(1,0))

    def test_original_completed_prefix_matches_global_root(self):
        states=lifted_states(32)
        for n in (1,2,3,7,12,20):
            for k in (1,2,3):
                packet=certified_prefix(states[n],n,k)
                self.assertEqual(packet['completed'],global_prefix(n,k,depth=n+k+18))

    def test_critical_source_seam_witnesses(self):
        states=lifted_states(192)
        actual={8:0,16:3,32:2,64:8,96:4}
        for B,hits in actual.items():
            self.assertEqual(shell_receipt(B,states)['seam_hits'],hits)

    def test_coherent_counterseed_is_all_minus_one_seams(self):
        for B in (8,16,32,64):
            q=16**critical_depth(B)
            for n in range(B,2*B):
                lo,hi=green_bounds(n,2)
                self.assertGreater(lo,0)
                self.assertLess(q*hi,1)
                # U_n(-x)=-T_n, so u=1-T_n and z=0.
                self.assertGreater(q*(1-hi),q-1)
                self.assertLess(q*(1-lo),q)
                self.assertEqual(seam_delta(q-1,critical_depth(B)),(1,0))


class FourierTransportTests(unittest.TestCase):
    def test_bridge_direct_vs_product_formula(self):
        for k, pairs in ((1,((0,0),(1,1),(1,2),(7,4))),
                         (2,((0,0),(1,1),(1,5),(7,4),(13,19)))):
            for h,t in pairs:
                self.assertLess(abs(bridge(h,t,k)-bridge_direct(h,t,k)),2e-11)

    def test_bridge_unitarity(self):
        for k,rows in ((1,(0,1,2,3)),(2,(0,1,7,23))):
            q=16**k
            vectors={h:[bridge(h,t,k) for t in range(q)] for h in rows}
            for h in rows:
                for hh in rows:
                    scalar=sum(vectors[h][t]*vectors[hh][t].conjugate()
                               for t in range(q))
                    self.assertLess(abs(scalar-(1 if h==hh else 0)),2e-10)

    def test_complete_basis_reconstructs_circle_phase(self):
        k=2;q=16**k
        states=lifted_states(25)
        codes=[certified_prefix(states[n],n,k)['completed']
               for n in range(12,24)]
        p=character_means(codes,k)
        for h in (1,2,7,15):
            from_padic=sum(bridge(h,t,k)*p[t] for t in range(q))
            direct=sum(cmath.exp(2j*math.pi*h*a/q) for a in codes)/len(codes)
            self.assertLess(abs(from_padic-direct),5e-11)
            real_estimates=[]
            for n in range(12,24):
                lo,hi=green_bounds(n,7)
                z=float((states[n]%1+(lo+hi)/2)%1)
                real_estimates.append(cmath.exp(2j*math.pi*h*z))
            real_mean=sum(real_estimates)/len(real_estimates)
            self.assertLessEqual(abs(real_mean-direct),2*math.pi*h/q+1e-8)

    def test_signed_seam_identity_with_critical_harmonic(self):
        states=lifted_states(192)
        for B in (16,32,64,96):
            k=critical_depth(B)
            q=16**k
            old=[];new=[];weights=[]
            for n in range(B,2*B):
                pack=certified_prefix(states[n],n,k)
                old.append(pack['uncompleted'])
                new.append(pack['completed'])
                weights.append(pack['increments'])
            for h in (1,q//2):
                delta=sum(cmath.exp(2j*math.pi*h*b/q)-
                          cmath.exp(2j*math.pi*h*a/q)
                          for a,b in zip(old,new))/B
                formula=(cmath.exp(2j*math.pi*h/q)-1)*sum(
                    d*cmath.exp(2j*math.pi*h*a/q)
                    for d,a in zip(weights,old))/B
                self.assertLess(abs(delta-formula),2e-9)

    def test_high_depth_energy_diagonal_floor(self):
        # For q>B, even B distinct points imply sum(nonzero |P_t|²)=q/B-1.
        B,q=16,256
        codes=list(range(B))
        p=character_means(codes,2)
        energy=sum(abs(v)**2 for v in p[1:])
        self.assertAlmostEqual(energy,q/B-1,places=9)


if __name__=='__main__':
    unittest.main(verbosity=2)

class UnprovedOriginControl(unittest.TestCase):
    def test_finite_2adic_origin_vanishes_256_levels_not_a_proof(self):
        # CONJECTURE BC-0, exact observation only. Not a universal theorem.
        self.assertEqual(stable_clock(0,256), 0)
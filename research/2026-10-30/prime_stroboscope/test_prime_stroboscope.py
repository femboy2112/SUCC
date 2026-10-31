"""Independent finite verification of paper identities; NOT a proof of all primes."""
import unittest
from selected_occupancy import certified_counts, certified_bin
from fractions import Fraction as F
from prime_stroboscope import (BBP_COEFFICIENTS, OFFSETS, actual_scaled_residue,
    events, mirror_coefficients, milestone_times, modular_scaled_residue, prefix,
    predicted_strobe_residue, prime, p_primary_decomposition, rational_mod_p,
    source_term, strobe_time, order_16)

PRIMES=[p for p in range(13,190) if prime(p) and p%8 in (1,5)]

class PrimeStroboscopeTests(unittest.TestCase):
    def test_exact_four_pole_source_and_seed(self):
        self.assertEqual(source_term(1), F(47,15))
        self.assertEqual(prefix(0),0)
        self.assertEqual(prefix(1),F(47,15))
        self.assertEqual(prefix(2),16*prefix(1)+source_term(2))

    def test_prime_list_has_both_classes(self):
        self.assertTrue(any(p%8==1 for p in PRIMES))
        self.assertTrue(any(p%8==5 for p in PRIMES))
        self.assertGreater(len(PRIMES),15)

    def test_strobe_native_time_and_range(self):
        for p in PRIMES:
            for k in range(1,min(4,(p+1)//8)):
                N=strobe_time(p,k)
                self.assertEqual(8*N-2,(8*k-2)*p)
                self.assertLess(8*k-2,p)
        for p,k in [(7,1),(11,1),(13,2),(17,3)]:
            with self.assertRaises(ValueError):strobe_time(p,k)

    def test_modular_strobe_all_sampled_primes(self):
        for p in PRIMES:
            for k in range(1,min(5,(p+1)//8)):
                with self.subTest(p=p,k=k):
                    expected=predicted_strobe_residue(p,k)
                    actual=modular_scaled_residue(p,k)
                    self.assertEqual(actual,expected)
                    if p<80 and k<=3:
                        self.assertEqual(actual,actual_scaled_residue(p,k))

    def test_source_pole_involution(self):
        x=(F(4),F(-2),F(-1),F(-1))
        self.assertEqual(mirror_coefficients(x),x)
        self.assertEqual(mirror_coefficients(mirror_coefficients((5,7,2,-3))),tuple(map(F,(5,7,2,-3))))
        for p in PRIMES:
            if p%8==5:
                for k in range(1,min(4,(p+1)//8)):
                    c=(5,7,2,-3)
                    self.assertEqual(modular_scaled_residue(p,k,c), predicted_strobe_residue(p,k,c))
                    if p<55:
                        self.assertEqual(actual_scaled_residue(p,k,c), predicted_strobe_residue(p,k,c))

    def test_mutated_first_pole_fails_self_shadow(self):
        c=(5,-2,-1,-1)
        for p in (13,29,37,53):
            self.assertNotEqual(actual_scaled_residue(p,1,c),rational_mod_p(prefix(1,c),p))
            self.assertEqual(actual_scaled_residue(p,1,c),rational_mod_p(prefix(1,mirror_coefficients(c)),p))

    def test_mutated_fixed_subspace_survives(self):
        c=(4,0,-1,0)
        for p in (13,17,29,37):
            self.assertEqual(actual_scaled_residue(p,1,c),rational_mod_p(prefix(1,c),p))

    def test_four_collision_p_residues(self):
        for p in PRIMES:
            milestones=milestone_times(p)
            seen={}
            u=F()
            for n in range(1,milestones[-1]+1):
                u=16*u+source_term(n)
                if n in milestones:seen[n]=rational_mod_p(p*u,p)
            def red(v):return rational_mod_p(F(v),p)
            self.assertEqual(seen[milestones[0]],4 if p%8==1 else p-1)
            self.assertEqual(seen[milestones[1]],red(F(7,2)))
            self.assertEqual(seen[milestones[2]],red(F(33,10) if p%8==1 else F(-66,5)))
            self.assertEqual(seen[milestones[3]],red(F(47,15)))

    def test_exact_crt_prime_cofiber(self):
        for p in (13,17,29,37,41):
            for k in (1,2):
                if p<=8*k-2:continue
                u=prefix(strobe_time(p,k))
                a,pp,b,D=p_primary_decomposition(u,p)
                self.assertEqual(pp,p)
                self.assertNotEqual(D%p,0)
                self.assertEqual(a,predicted_strobe_residue(p,k))
                self.assertEqual((u-F(a,p)-F(b,D)).denominator,1)
                self.assertNotEqual(a,0)

    def test_exceptional_zero_cofactor(self):
        # At p=73 the fourth rational prefix vanishes modulo p; the p-primary
        # conductor can disappear at that stroboscopic time.
        p,k=73,4
        self.assertEqual(rational_mod_p(prefix(k),p),0)
        N=strobe_time(p,k)
        self.assertEqual(modular_scaled_residue(p,k),0)
        u=prefix(N)
        self.assertNotEqual(u.denominator%p,0)
        self.assertEqual(p_primary_decomposition(u,p)[0],0)

    def test_p_integral_seed_is_invisible_to_primary_shadow(self):
        # p*16^N*s == 0 mod p for p-integral rational seeds.
        for p,k in [(13,1),(17,1),(29,2)]:
            N=strobe_time(p,k)
            for s in (F(0),F(1,3),F(17,15)):
                self.assertEqual(rational_mod_p(p*prefix(N,seed=s),p),predicted_strobe_residue(p,k))

    def test_first_window_contains_complete_local_multiplicative_period(self):
        for p in PRIMES:
            birth,first_four,_,_=milestone_times(p)
            d=order_16(p)
            self.assertEqual((p-1)//4%d,0)
            self.assertGreaterEqual(first_four-birth,d)
            self.assertEqual(pow(16,d,p),1)

    def test_exact_selected_hex_grid_256(self):
        # Certified by rational BBP forcing + analytic positive Green tail;
        # no assumption about pi normality or irrationality measures.
        cert=certified_counts(256,16)
        expected=[17,18,18,15,14,12,16,18,19,24,13,13,14,16,13,16]
        self.assertEqual(cert['ambiguous'],[])
        self.assertEqual(cert['lower'],expected)
        self.assertEqual(cert['upper'],expected)
        self.assertEqual(sum(expected),256)

    def test_refined_grid_preserves_ambiguity(self):
        cert=certified_counts(256,256)
        self.assertEqual(len(cert['ambiguous']),2)
        self.assertEqual([row['n'] for row in cert['ambiguous']],[1,2])
        self.assertEqual(sum(cert['lower']),254)
        self.assertGreaterEqual(sum(cert['upper']),256)

    def test_event_pole_passport(self):
        for p in (13,17,29,41):
            for k in (1,2):
                if p<=8*k-2:continue
                es=events(p,k)
                residues=[j for (_,j,_,_) in es]
                wanted=[8*t+offset for t in range(k) for offset in OFFSETS]
                self.assertEqual(sorted(residues),sorted(wanted))
                self.assertEqual(len(es),4*k)

if __name__=='__main__':unittest.main(verbosity=2)

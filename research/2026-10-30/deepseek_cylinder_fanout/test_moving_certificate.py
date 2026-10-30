import unittest
from fractions import Fraction
from moving_certificate import (
    block_counts,collision_energy,l1_short_block,finite_certificate_bound,
    witness,finite_test_cases,debruijn)

class MovingScaleCertificateTests(unittest.TestCase):
    def test_zero_model(self):
        for m in range(1,5):
            self.assertEqual(collision_energy([0]*64,60,m),16**m)

    def test_debruijn_model(self):
        cyc=debruijn(16,2)
        self.assertEqual(len(cyc),256)
        self.assertEqual(collision_energy(cyc*2,256,2),1)
        self.assertEqual(collision_energy(cyc*2,256,3),16)

    def test_equal_words_formula(self):
        digits=[0,1,2,0,1,2,0,1,2]
        for m in range(1,4):
            n=len(digits)-m+1
            C=block_counts(digits,n,m)
            lhs=sum(C[w]*C[w] for w in C)
            ws=[]
            for j in range(n):
                k=0
                for x in digits[j:j+m]:k=k*16+x
                ws.append(k)
            rhs=sum(x==y for x in ws for y in ws)
            self.assertEqual(lhs,rhs)

    def test_sampling_floor(self):
        for name,d,n,m,k in finite_test_cases():
            self.assertGreaterEqual(collision_energy(d,n,m),Fraction(16**m,n))

    def test_kl_pinsker_certificate_controls(self):
        for name,d,n,m,k in finite_test_cases():
            self.assertTrue(witness(d,n,m,k)['pass'],name)

    def test_actual_l1_control_debruijn(self):
        cyc=debruijn(16,3)
        self.assertEqual(l1_short_block(cyc*2,4096,1),0)
        self.assertEqual(l1_short_block(cyc*2,4096,2),0)

    def test_sampled_energy_is_one_when_debruijn_equal(self):
        for order in (1,2,3):
            cyc=debruijn(16,order)
            self.assertEqual(collision_energy(cyc*2,len(cyc),order),1)

    def test_finite_bound_is_zero_plus_edge_for_exact_uniform(self):
        n,m,k=256,2,1
        self.assertEqual(finite_certificate_bound(Fraction(1),n,m,k),Fraction(2*m,n))

    def test_explicit_bbp_first_256_census(self):
        # Inherited exact certificate from PR407; test this harness on the
        # integer word histogram using parents' certified digit bins.
        # No fake analytic normality inference from a finite prefix.
        from cylinder_probe import bbp_states,certified_word
        us=list(bbp_states(64))
        words=[certified_word(u,n,2)[0] for n,u in enumerate(us,1)]
        d=[w//16 for w in words]+[words[-1]%16]
        self.assertEqual(collision_energy(d,64,2),
                         Fraction(16**2*sum(c*c for c in block_counts(d,64,2).values()),64**2))
        self.assertTrue(witness(d,64,2,1)['pass'])

if __name__ == '__main__':unittest.main(verbosity=2)

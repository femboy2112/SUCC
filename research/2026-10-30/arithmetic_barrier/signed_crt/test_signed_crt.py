import unittest
from fractions import Fraction as F
from math import gcd
from signed_crt import (source,orbit,primary_split,first_period,nearest_complement,
    twist_energy_certificate,trig_interval,pi_interval,char_sum_box,magnitude_interval,
    variation_interval,interaction_interval,coherent_dyadic_control)


class SignedCRTTests(unittest.TestCase):
    def test_independent_unrolled_rational_oracle(self):
        states=orbit(24)
        for n in range(1,25):
            independent=sum((16**(n-j)*(F(4,8*j-7)-F(2,8*j-4)-F(1,8*j-3)-F(1,8*j-2))
                             for j in range(1,n+1)),F())%1
            self.assertEqual(states[n],independent)

    def test_trigonometric_certificates_at_exact_values(self):
        for q,cos,sin in [(F(),1,0),(F(1,4),0,1),(F(1,2),-1,0),(F(3,4),0,-1)]:
            (cl,cu),(sl,su)=trig_interval(q)
            self.assertLessEqual(cl,cos);self.assertLessEqual(cos,cu)
            self.assertLessEqual(sl,sin);self.assertLessEqual(sin,su)
            self.assertLess(cu-cl,F(1,10**14))
        lo,hi=pi_interval()
        self.assertTrue(F(333,106)<lo<hi<F(355,113))

    def test_all_coprime_nearest_complements(self):
        for p in (13,17,29,73):
            for D in (2,11,32,101):
                if gcd(p,D)>1:continue
                for a in range(1,p):
                    b,z=nearest_complement(a,p,D)
                    self.assertNotEqual(z,0)
                    self.assertGreaterEqual(abs(z),F(1,p*D))
                    self.assertLessEqual(abs(z),F(p-1,2*p*D))
                    self.assertEqual(primary_split(F(a,p)+F(b,D),p)[:2],(a,p))

    def test_multi_prime_joint_primary_restoration(self):
        P=13*17*29
        D=2**18
        for a in (1,2,13,17,987,P-1):
            b,z=nearest_complement(a,P,D)
            for p in (13,17,29):
                self.assertEqual(primary_split(F(a,P)+F(b,D),p)[:2],primary_split(F(a,P),p)[:2])
            self.assertLessEqual(abs(z),F(1,2*D))

    def test_actual_full_phase_exceeds_marginal_plus_one(self):
        _,phases,primary,_=first_period(13)
        f=magnitude_interval(char_sum_box(phases,1))
        m=magnitude_interval(char_sum_box(primary,1))
        self.assertGreater(f[0],m[1]+1)

    def test_actual_cofiber_variation_not_constant_four(self):
        _,_,_,cofiber=first_period(29)
        self.assertGreater(variation_interval(cofiber,1)[0],4)

    def test_exact_twist_energy_and_repeated_residue_mutant(self):
        for p in (13,17,29,37,41,73):
            _,phases,_,_=first_period(p)
            cert=twist_energy_certificate(phases,p)
            self.assertEqual(cert['mean_square'],len(phases))
            with self.assertRaises(ValueError):
                twist_energy_certificate(phases+[phases[0]],p)

    def test_primary_split_higher_powers_and_absence(self):
        for q in (F(3,13**2*17),F(7,17),F(23,2**8*13**3),F()):
            a,power,v=primary_split(q,13)
            self.assertEqual((q-F(a,power)-v).denominator,1)
            self.assertNotEqual(v.denominator%13,0)

    def test_p73_k4_cancellation(self):
        n=((4*4-1)*73+1)//4
        q=orbit(n)[-1]
        self.assertEqual(primary_split(q,73)[:2],(0,1))

    def test_dyadic_coherence_preserves_odd_components_and_aliases(self):
        c=coherent_dyadic_control(12,28,5)
        original=orbit(c['depth']+3)
        changed=orbit(c['depth']+3,c['seed'])
        for n in range(len(original)):
            for p in (3,5,13,17,29,73):
                self.assertEqual(primary_split(original[n],p)[:2],primary_split(changed[n],p)[:2])
        self.assertEqual(original[c['depth']:],changed[c['depth']:])
        self.assertLess(interaction_interval(c['changed_phases'])[1],F(1,1000))

    def test_exact_and_eventual_alias_and_constant_twist(self):
        old=orbit(18)
        for seed,after in ((F(1),0),(F(1,16**4),4)):
            new=orbit(18,seed)
            self.assertEqual(new[after:],old[after:])
        twist=orbit(18,F(1,15))
        self.assertTrue(all((b-a)%1==F(1,15) for a,b in zip(old,twist)))

    def test_mutants_not_unique(self):
        for coeff in ((5,-2,-1,-1),(4,0,-1,0)):
            self.assertNotEqual(orbit(9,coefficients=coeff),orbit(9))
        # A p=1 mod8 first birth alone cannot identify these source mutations.
        self.assertEqual(primary_split(orbit(3,coefficients=(4,0,-1,0))[3],17)[0],4)

if __name__=='__main__':unittest.main(verbosity=2)

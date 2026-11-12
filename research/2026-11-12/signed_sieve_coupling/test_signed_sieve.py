import unittest
from fractions import Fraction
from math import isqrt
from signed_sieve import (coeff, haar_pair, icbrt, masks, midpoint_haar,
                          omega_mask, prime_mask, rough_majorant, row,
                          source_mutant, verify_row)


def trialprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


class SignedCarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.P = prime_mask(10001)

    def test_independent_prime_implementations(self):
        for n in range(10001):
            self.assertEqual(bool(self.P[n]), trialprime(n), n)

    def test_cuberoot_exact(self):
        for n in range(30000):
            z = icbrt(n)
            self.assertLessEqual(z**3, n)
            self.assertLess(n, (z+1)**3)

    def test_rough_has_prime_and_composite_partition(self):
        for z in (2,3,5,7,11,19,23,31):
            q,c,s = masks(self.P,z)
            for k in range(2,10001):
                self.assertEqual(q[k],self.P[k]+c[k])
                self.assertEqual(s[k],int(self.P[k])-int(c[k]))
                self.assertIn(s[k],(-1,0,1))

    def test_signed_convolution_and_independent_goldbach_count(self):
        for N in (4,6,8,20,60,100,256,512,1000,2048,4096,8192):
            for z in (2,3,5,7,icbrt(N),isqrt(N)):
                output=row(N,self.P,z)
                expected=sum(1 for k in range(2,N-1) if trialprime(k) and trialprime(N-k))
                self.assertEqual(output['goldbach_ordered'],expected)
                self.assertEqual(output['signed_lower'],expected-output['rough_composite_pairs'])

    def test_liouville_character_cube_root_threshold(self):
        om=omega_mask(10001)
        for N in (8,20,100,256,1000,2048,4096,8192,9999):
            z=icbrt(N)
            q,c,s=masks(self.P,z)
            for k in range(2,N+1):
                if q[k]:
                    self.assertLessEqual(om[k],2)
                    self.assertEqual(s[k], -(-1)**om[k])
            self.assertEqual(verify_row(N,self.P,z),coeff(q,s,N))

    def test_monotone_quadratic_lower_operator_and_exact_flux(self):
        for N in (100,256,512,1000,2048):
            vals=[]
            prev=None
            for z in (2,3,5,7,11,13,17,19,23,31,isqrt(N)):
                q,c,s=masks(self.P,z)
                v=coeff(q,s,N)
                vals.append(v)
                if prev is not None:
                    old=prev
                    e=[int(old[k])-int(c[k]) for k in range(len(c))]
                    self.assertEqual(vals[-1]-vals[-2],2*coeff(e,c,N)+coeff(e,e,N))
                prev=c
            self.assertEqual(sorted(vals),vals)
            self.assertEqual(vals[-1],coeff(self.P,self.P,N))

    def test_exact_haar_identity_signed_multiscale(self):
        for N in (20,100,512,2048):
            r=midpoint_haar(N,self.P,icbrt(N))
            self.assertEqual(r['signed_lower'],row(N,self.P,icbrt(N))['signed_lower'])
            self.assertTrue(r['scale_bands'])
        out,c,b=haar_pair([1,0,1,0],[-1,1,-1,1])
        self.assertEqual(out,-2)
        self.assertEqual(c,Fraction(0))
        self.assertEqual(sum((v for _,v in b),Fraction(0)),Fraction(-2))

    def test_source_mutation_no_multiple_of_four_witnesses(self):
        fake=source_mutant(self.P)
        for N in (8,12,100,512,1000,2048,8192):
            self.assertEqual(coeff(fake,fake,N),0)
            q=rough_majorant(self.P,icbrt(N))
            self.assertTrue(all(fake[k]<=q[k] for k in range(N+1)))
            c=bytearray(q[k]-fake[k] for k in range(len(q)))
            s=[int(fake[k])-int(c[k]) for k in range(len(q))]
            self.assertEqual(coeff(q,s,N),-coeff(c,c,N))
            self.assertLessEqual(coeff(q,s,N),0)

    def test_low_cutoff_can_fail_even_with_real_witnesses(self):
        r=row(8192,self.P,2)
        self.assertEqual(r['goldbach_ordered'],152)
        self.assertEqual(r['signed_lower'],-2042)
        self.assertFalse(r['certifies'])
        r=row(8192,self.P,icbrt(8192))
        self.assertEqual(r['signed_lower'],128)
        self.assertTrue(r['certifies'])

    def test_odd_not_automatically_positive(self):
        # The even Goldbach positivity target must not be promoted to all integers.
        for n in (11,25,101):
            r=row(n,self.P,icbrt(n))
            self.assertLessEqual(r['signed_lower'],r['goldbach_ordered'])

    def test_one_sided_majority_is_same_signed_certificate(self):
        for N in (20,100,512,1000,2048,8192):
            for z in (2,3,5,icbrt(N)):
                r=row(N,self.P,z)
                self.assertEqual(2*r['prime_rough_pairs']-r['rough_pairs'],r['signed_lower'])
                self.assertEqual(r['certifies'],r['prime_rough_pairs']*2>r['rough_pairs'])

    def test_signed_tensor_projector_monotonicity(self):
        # On the tensor basis, K_z(a,b)=+1 if PP, -1 if CC, zero otherwise.
        # Diagonal differences are positive as composite C_z shrinks.
        for z in (2,3,5,7,11,17):
            _,ca,_=masks(self.P,z)
            _,cb,_=masks(self.P,z+1)
            for a in range(2,91):
                for b in range(2,91):
                    ka=int(self.P[a])*int(self.P[b])-int(ca[a])*int(ca[b])
                    kb=int(self.P[a])*int(self.P[b])-int(cb[a])*int(cb[b])
                    self.assertLessEqual(ka,kb)
                    self.assertLessEqual(kb,int(self.P[a])*int(self.P[b]))

    def test_nonuniform_convergence_witness(self):
        # Each finite sieve admits a surviving p^2, so operator-norm defect=1.
        for z in (2,3,5,7,11,19,31):
            p=next(n for n in range(z+1,101) if trialprime(n))
            q,c,_=masks(self.P,z)
            self.assertEqual(self.P[p*p],0)
            self.assertEqual(c[p*p],1)
            # On pair (p*p,p*p), K_z=-1, P tensor P=0.
            self.assertEqual(int(self.P[p*p])*int(self.P[p*p])-int(c[p*p])*int(c[p*p]),-1)

    def test_fixed_cutoffs_fail_for_large_inputs(self):
        # Specific authentic primes: low local resolution cannot certify forever.
        for z,N in ((2,8192),(3,10000),(5,10000)):
            self.assertLess(row(N,self.P,z)['signed_lower'],0)

    def test_global_signed_mass_does_not_force_local_sign(self):
        # Toy P,C with |P|>|C| has total positive signed mass but negative local score.
        P=bytearray(9);P[2]=P[5]=1
        C=bytearray(9);C[3]=1
        self.assertGreater(sum(P)**2-sum(C)**2,0)
        self.assertLess(coeff(P,P,6)-coeff(C,C,6),0)

    def test_missing_small_prime_restoration_is_unsound(self):
        for N in (8,20,100):
            z=5
            q,c,_=masks(self.P,z)
            naive=bytearray(q)
            for p in (2,3,5):naive[p]=0
            self.assertTrue(any(self.P[p] and naive[p]==0 for p in (2,3,5)))
            self.assertTrue(any(q[p] and not naive[p] for p in (2,3,5)))


if __name__ == '__main__':
    unittest.main()

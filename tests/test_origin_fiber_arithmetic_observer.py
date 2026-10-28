import unittest
from fractions import Fraction as F
from observational_succ import origin_fiber_arithmetic_observer as m

class SourceLockCompressionTests(unittest.TestCase):
    def test_divisor_paths(self):
        for n in range(1,301):
            self.assertEqual(len(m.pair_space(n)),m.d(n))
            for a,b in m.pair_space(n):
                self.assertEqual(a*b,n)

    def test_first_channel_jump_exact(self):
        for n in range(1,121):
            w=m.compressed_channel_additive_sq(n)
            self.assertEqual(set(w),{n+b for b in m.divisors(n)})
            self.assertEqual(len(w),m.d(n))
            for b in m.divisors(n):
                self.assertEqual(w[n+b],F(1,m.d(n)*m.d(n+b)))
            self.assertEqual(w[n+1],m.nearest_successor_overlap_sq(n))

    def test_sharp_half_coherence_loss(self):
        self.assertEqual(m.compressed_channel_additive_sqnorm(1),F(1,2))
        for n in range(1,300):
            self.assertLessEqual(m.compressed_channel_additive_sqnorm(n),F(1,2))
            if n>1:
                self.assertLess(m.compressed_channel_additive_sqnorm(n),F(1,2))

    def test_unbounded_repair_factor(self):
        # Along n=2^k the reciprocal nearest-SUCC overlap diverges.
        for k in range(0,20):
            n=2**k
            c2=m.nearest_successor_overlap_sq(n)
            self.assertLessEqual(c2,F(1,k+1))

    def test_prime_compression(self):
        for p in [2,3,5,7]:
            for j in range(18):
                self.assertEqual(m.compressed_channel_prime_overlap_sq(p**j,p),F(j+1,j+2))

    def test_composition_defect(self):
        self.assertEqual(m.simple_nonfunctoriality_defect_sq(),F(5,24))

    def test_su2_algebra_all_weights(self):
        for j in range(0,35):
            for k in range(j+1):
                self.assertEqual(m.su2_raising_lowering_commutator(j,k),2*m.su2_j3(j,k))
                self.assertEqual(m.su2_casimir(j,k),F(j*(j+2),4))

    def test_su2_origin_variance(self):
        for j in range(0,40):
            z=[m.su2_j3(j,k) for k in range(j+1)]
            self.assertEqual(sum(z,F(0)),0)
            self.assertEqual(sum((t*t for t in z),F(0))/F(j+1),m.uniform_split_j3_variance(j))
            self.assertEqual(4*m.uniform_split_j3_variance(j),F(j*(j+2),3))

    def test_coherent_spin_not_singlet(self):
        for j in range(1,25):
            self.assertGreater(m.su2_casimir(j,0),0)

    def test_exact_reaction_to_nonlinear_phase(self):
        import cmath, math
        phase=lambda n:complex(cmath.exp(2j*math.pi*float(n*n%7)/7))
        for n in range(1,15):
            val=m.source_carry_difference_times_sq(n,phase)
            self.assertGreaterEqual(val,0)
            self.assertLessEqual(val,2.01)  # |phase diff|^2<=4; norm sq<=1/2

    def test_invalid(self):
        with self.assertRaises(ValueError):m.divisors(0)
        with self.assertRaises(ValueError):m.su2_j3(1,2)
        with self.assertRaises(ValueError):m.compressed_channel_prime_overlap_sq(2,4)

if __name__=='__main__':unittest.main()

"""Finite exhaustive and hostile exact checks for arithmetic EPR star."""
from fractions import Fraction as F
from itertools import product
import unittest

from observational_succ.arithmetic_epr_star import (
    PAIRS, codeword, dirichlet_samples, dirichlet_reconstruct, prime_shift,
    local_bruhat_tits_neighbors, pair_decode, pair_encode, act_on_boundary,
    encoded_mirror_images, encoded_tfd_support, truncation_mirror_residual_beta2,
    source_chart_braid_defect,
)


class PrimeBridgeExactTests(unittest.TestCase):
    def test_rational_three_sample_analytic_inverse(self):
        for a in product((-2, -1, 0, 1, 2), repeat=3):
            self.assertEqual(dirichlet_reconstruct(dirichlet_samples(a)), tuple(map(F,a)))
            self.assertEqual(dirichlet_samples(prime_shift(a)),
                             dirichlet_samples((0,a[0],a[1])))

    def test_genuine_2adic_first_shell_not_three_arbitrary_nodes(self):
        shells=local_bruhat_tits_neighbors()
        self.assertEqual(len(shells), 3)
        self.assertEqual({len(k) for k in shells}, {2})
        self.assertEqual(set.intersection(*map(set,shells)), {(0,0)})
        self.assertEqual(set.union(*map(set,shells)), set(product(range(2),repeat=2)))

    def test_three_qutrit_code_isometry_and_erasure_KL(self):
        # At amplitude 1/sqrt(3), the vector inner products are support overlap /3.
        words=[set(codeword(i)) for i in range(3)]
        for i,k in product(range(3), repeat=2):
            self.assertEqual(F(len(words[i]&words[k]),3), F(i==k))
        # For each erased leg e, Tr_{other two} |i_L><k_L| = delta_ik I/3.
        for e in range(3):
            others=tuple(x for x in range(3) if x!=e)
            for i,k in product(range(3),repeat=2):
                mat=[[F() for _ in range(3)] for _ in range(3)]
                for a in codeword(i):
                    for b in codeword(k):
                        if all(a[z]==b[z] for z in others):
                            mat[a[e]][b[e]]+=F(1,3)
                self.assertEqual(mat,
                                 [[F(i==k and u==v,3) for v in range(3)] for u in range(3)])

    def test_all_pair_decoders_are_permutations_and_reconstruct(self):
        for pair in PAIRS:
            seen=set()
            for visible in product(range(3),repeat=2):
                result=pair_decode(pair,visible)
                self.assertEqual(pair_encode(*result,pair),visible)
                seen.add(result)
            self.assertEqual(len(seen),9)
            missing=({0,1,2}-set(pair)).pop()
            for i in range(3):
                self.assertEqual({pair_decode(pair,tuple(w[x] for x in pair))
                                  for w in codeword(i)}, {(i,k) for k in range(3)})
                for w in codeword(i):
                    self.assertEqual(pair_decode(pair,tuple(w[x] for x in pair))[1],w[missing])

    def test_bulk_prime_multiplication_reconstructed_from_each_two_leg_region(self):
        for pair in PAIRS:
            for i in range(3):
                for w in codeword(i):
                    mapped=act_on_boundary(w,pair)
                    if i==2:
                        self.assertIsNone(mapped)
                    else:
                        self.assertIn(mapped,codeword(i+1))
                        missing=({0,1,2}-set(pair)).pop()
                        self.assertEqual(mapped[missing],w[missing])
                    rev=act_on_boundary(w,pair,reverse=True)
                    if i==0:
                        self.assertIsNone(rev)
                    else:
                        self.assertIn(rev,codeword(i-1))
                        self.assertEqual(rev[({0,1,2}-set(pair)).pop()],w[({0,1,2}-set(pair)).pop()])

    def test_full_geometrically_encoded_epr_mirror_all_nine_regions(self):
        self.assertEqual(len(encoded_tfd_support()),27)
        for a in PAIRS:
            for b in PAIRS:
                lhs,rhs=encoded_mirror_images(a,b)
                self.assertEqual(lhs,rhs, (a,b))
                self.assertEqual(len(lhs),18)

    def test_bulk_entropy_term_factors_after_exact_erasure_decode(self):
        # rho includes off-diagonal coherence, not just a classical mixture.
        rho=((F(1,2),F(1,4),F()),
             (F(1,4),F(1,2),F()),
             (F(),F(),F()))
        # For each pair, decoded rho_AB must equal rho logical tensor I_3/3.
        for pair in PAIRS:
            missing=({0,1,2}-set(pair)).pop()
            for a,b in product(product(range(3),repeat=2),repeat=2):
                direct=F()
                for i,k in product(range(3),repeat=2):
                    for word_i,word_k in product(codeword(i),codeword(k)):
                        if (tuple(word_i[x] for x in pair)==a and
                            tuple(word_k[x] for x in pair)==b and
                            word_i[missing]==word_k[missing]):
                            direct+=rho[i][k]/3
                i,r=pair_decode(pair,a)
                k,t=pair_decode(pair,b)
                self.assertEqual(direct,rho[i][k]/3 if r==t else 0)

    def test_source_mutation_breaks_mirror_but_not_geometric_code(self):
        # One altered arithmetic coefficient remains an encodable quantum state,
        # but no longer satisfies the specified prime-mirror transport law.
        for a in PAIRS:
            for b in PAIRS:
                lhs,rhs=encoded_mirror_images(a,b,weights=(4,2,2))
                self.assertNotEqual(lhs,rhs)
                self.assertEqual(len(lhs),18)

    def test_truncation_mirror_defect_is_nonzero_and_not_forced_monotone(self):
        self.assertEqual(truncation_mirror_residual_beta2(1),F(1))
        self.assertEqual(truncation_mirror_residual_beta2(2),F(1,5))
        self.assertEqual(truncation_mirror_residual_beta2(3),F(13,49))
        self.assertGreater(truncation_mirror_residual_beta2(3),
                           truncation_mirror_residual_beta2(2))
        self.assertLess(truncation_mirror_residual_beta2(100),F(1,100))
        with self.assertRaises(ValueError):
            truncation_mirror_residual_beta2(5,4)

    def test_source_chart_does_not_preserve_additive_succ_braid(self):
        lhs,rhs=source_chart_braid_defect()
        self.assertEqual(lhs,(F(),F(),F(1)))
        self.assertEqual(rhs,(F(),F(),F()))
        self.assertNotEqual(lhs,rhs)

    def test_invalid_types_fail_closed(self):
        with self.assertRaises(TypeError):dirichlet_samples((1.0,2,3))
        with self.assertRaises(ValueError):pair_decode((0,0),(1,2))
        with self.assertRaises(ValueError):pair_decode((0,1),(4,1))
        with self.assertRaises(ValueError):act_on_boundary((0,0,False),(0,1))


if __name__=='__main__':
    unittest.main()

# The actual three-direction coherence composite, not merely isolated identities.
class CoherentSquareTests(unittest.TestCase):
    def test_arithmetic_analytic_boundary_square_all_three_regions(self):
        for a in ((F(2),F(3),F(5)),(F(1,7),F(-2,9),F(3,11)),(F(),F(),F(1))):
            from observational_succ.arithmetic_epr_star import dirichlet_samples, dirichlet_reconstruct
            recovered=dirichlet_reconstruct(dirichlet_samples(a))
            target=prime_shift(a)
            self.assertEqual(prime_shift(recovered),target)
            for pair in PAIRS:
                physical={}
                for i,amp in enumerate(recovered):
                    for word in codeword(i):
                        mapped=act_on_boundary(word,pair)
                        if mapped is not None:
                            physical[mapped]=physical.get(mapped,F())+amp
                expected={}
                for i,amp in enumerate(target):
                    for word in codeword(i):
                        if amp:
                            expected[word]=expected.get(word,F())+amp
                physical={k:v for k,v in physical.items() if v}
                self.assertEqual(physical,expected)

"""Independent finite controls for the Pascal/Lucas quotient bridge."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest

from observational_succ.pascal_lucas_quotient import (
    address_to_pair, binomial_transform, digit_histogram,
    four_bit_rank_residual, histogram_average, histogram_symmetrization_tv, histogram_zeta_apply,
    lucas_alphabet_size, lucas_residue_apply, lucas_row_support, lucas_total, lucas_unit,
    pair_to_address, uniform_embedding_tv, zeta_apply,
)


class PascalLucasQuotientTests(unittest.TestCase):
    def test_lucas_against_unrelated_integer_binomial_modulo(self):
        for p, depth in ((2,7), (3,4), (5,3), (7,2)):
            for n in range(p**depth):
                self.assertEqual(lucas_row_support(p,n),
                                 sum(comb(n,k) % p != 0 for k in range(n+1)))
                for k in range(n+1):
                    self.assertEqual(lucas_unit(p,n,k), comb(n,k) % p != 0)
                self.assertFalse(lucas_unit(p,n,n+1))

    def test_bijection_full_domain_including_mutant(self):
        for p, depth in ((2,6), (3,3), (5,2)):
            for address in range(lucas_total(p,depth)):
                n,k = address_to_pair(p,depth,address)
                self.assertEqual(pair_to_address(p,depth,n,k),address)
                self.assertTrue(lucas_unit(p,n,k))
            self.assertEqual(lucas_total(p,depth),
                             sum(lucas_row_support(p,n) for n in range(p**depth)))
        with self.assertRaises(ValueError):
            pair_to_address(2,2,0,1)

    def test_weight_two_binomial_and_parity_triangle_exact_same_cells(self):
        for depth in range(9):
            pairs = {address_to_pair(2,depth,a) for a in range(3**depth)}
            self.assertEqual(len(pairs),3**depth)
            self.assertEqual(len(pairs),sum(comb(depth,j)*2**j for j in range(depth+1)))
            for n,k in pairs:
                self.assertEqual(pair_to_address(2,depth,n,k),
                                 sum(((n>>i & 1)+(k>>i & 1))*3**i for i in range(depth)))

    def test_bivariate_partition_polynomial(self):
        for depth in range(6):
            histogram = {}
            for address in range(3**depth):
                n,k = address_to_pair(2,depth,address)
                key = (n.bit_count(),k.bit_count())
                histogram[key] = histogram.get(key,0)+1
            for j in range(depth+1):
                for h in range(j+1):
                    self.assertEqual(histogram[(j,h)],comb(depth,j)*comb(j,h))

    def test_tensor_incidence_direct_subset_summation(self):
        for p,depth in ((2,5),(3,3),(5,2)):
            size=p**depth
            values=tuple(Q((i*13+7)%19-8, 7) for i in range(size))
            output=zeta_apply(p,depth,values)
            for n in range(size):
                self.assertEqual(output[n],sum((values[k] for k in range(size) if lucas_unit(p,n,k)),Q()))

    def test_residue_operator_separates_support_from_prime_phases(self):
        for p,depth in ((2,5),(3,3),(5,2)):
            size = p**depth
            values = tuple(((17*k+2)%13)-6 for k in range(size))
            output = lucas_residue_apply(p,depth,values)
            for n in range(size):
                self.assertEqual(output[n],
                    sum(comb(n,k)*values[k] for k in range(n+1)) % p)
        self.assertEqual(lucas_residue_apply(3,1,(0,1,0))[2],2)
        self.assertEqual(zeta_apply(3,1,(0,1,0))[2],Q(1))

    def test_rank_quotient_intertwines_pascal_successor(self):
        for depth in range(7):
            values=tuple(Q((i*17+11)%23-11,9) for i in range(2**depth))
            left=histogram_average(2,depth,zeta_apply(2,depth,values))
            right=binomial_transform(tuple(histogram_average(2,depth,values)[(depth-j,j)]
                                           for j in range(depth+1)))
            self.assertEqual(tuple(left[(depth-j,j)] for j in range(depth+1)),right)

    def test_multinomial_histogram_quotient_intertwines_all_primes(self):
        for p,depth in ((2,5),(3,3),(5,2)):
            values=tuple(Q((i*19+3)%29-14,11) for i in range(p**depth))
            self.assertEqual(histogram_average(p,depth,zeta_apply(p,depth,values)),
                             histogram_zeta_apply(p,depth,histogram_average(p,depth,values)))

    def test_nonzero_kernel_loses_position_but_preserves_rank(self):
        values=(Q(0),Q(1),Q(-1),Q(0))
        self.assertTrue(all(v==0 for v in histogram_average(2,2,values).values()))
        self.assertTrue(all(v==0 for v in histogram_average(2,2,zeta_apply(2,2,values)).values()))

    def test_symmetric_quotient_does_not_support_succ_three(self):
        # Ternary least-significant-first digits: 01 (3) and 10 (1).
        a,b=address_to_pair(2,2,3),address_to_pair(2,2,1)
        self.assertEqual((a[0].bit_count(),a[1].bit_count()),
                         (b[0].bit_count(),b[1].bit_count()))
        aa,bb=address_to_pair(2,2,4),address_to_pair(2,2,2)
        self.assertNotEqual((aa[0].bit_count(),aa[1].bit_count()),
                            (bb[0].bit_count(),bb[1].bit_count()))

    def test_four_bit_gate_uniform_binary_source_exact_one_sixteenth(self):
        for depth in range(4,11):
            direct = Q(sum((n&15)==0 for n in range(2**depth)), 2**depth)
            self.assertEqual(direct,Q(1,16))
            layer_means={}
            for rank in range(depth+1):
                group=[n for n in range(2**depth) if n.bit_count()==rank]
                layer_means[rank]=Q(sum((n&15)==0 for n in group),len(group))
            loss=sum((Q(1,2**depth)*(Q((n&15)==0)-layer_means[n.bit_count()])**2
                      for n in range(2**depth)),Q())
            self.assertEqual(loss,four_bit_rank_residual(depth))
        self.assertEqual(four_bit_rank_residual(4),Q(0))
        self.assertEqual(four_bit_rank_residual(5),Q(1,40))
        self.assertGreater(four_bit_rank_residual(10),Q(0))

    def test_sharp_source_symmetry_gate_defect_control(self):
        depth=5
        point=[Q(0)]*(2**depth)
        point[16]=Q(1)
        self.assertEqual(histogram_symmetrization_tv(2,depth,tuple(point)),Q(4,5))
        gate=Q(1)  # n=16 has low four digits zero.
        sym_gate=Q(1,5)  # one of five rank-one positions is 16.
        self.assertEqual(abs(gate-sym_gate),Q(4,5))
        uniform=(Q(1,2**depth),)*(2**depth)
        self.assertEqual(histogram_symmetrization_tv(2,depth,uniform),Q(0))

    def test_prime_embedding_exact_total_variation(self):
        for depth in range(6):
            self.assertEqual(uniform_embedding_tv(2,3,depth),1-Q(1,2)**depth)
            self.assertEqual(uniform_embedding_tv(3,5,depth),1-Q(2,5)**depth)
        self.assertEqual(uniform_embedding_tv(2,3,4),Q(15,16))

    def test_tensor_prefix_coherence_for_all_tested_primes(self):
        for p in (2,3,5):
            for depth in range(4):
                n,k=address_to_pair(p,depth,lucas_total(p,depth)-1)
                for a in range(p):
                    for b in range(a+1):
                        addr=pair_to_address(p,depth+1,n+a*p**depth,k+b*p**depth)
                        self.assertEqual(addr,
                                         pair_to_address(p,depth,n,k) +
                                         (a*(a+1)//2+b)*lucas_total(p,depth))

    def test_invalid_domains(self):
        for invalid in (1,4,9,True):
            with self.assertRaises(ValueError):
                lucas_alphabet_size(invalid)
        for call in (lambda: lucas_total(3,-1),
                     lambda: address_to_pair(2,2,9),
                     lambda: pair_to_address(2,2,4,0),
                     lambda: digit_histogram(2,2,4),
                     lambda: zeta_apply(2,2,(1,2)),
                     lambda: histogram_zeta_apply(2,2,{}),
                     lambda: four_bit_rank_residual(3),
                     lambda: uniform_embedding_tv(3,2,1),
                     lambda: binomial_transform((0.3,)),
                     lambda: lucas_unit(2,-1,0)):
            with self.assertRaises(ValueError):
                call()


if __name__ == '__main__':
    unittest.main()

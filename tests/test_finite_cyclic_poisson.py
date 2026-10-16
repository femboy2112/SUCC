"""Finite cyclic Fourier-Poisson independent witnesses and adverse sign checks."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.finite_fourier_carrier import CyclotomicElement
from observational_succ.finite_cyclic_poisson import (
    finite_poisson_coset, exact_cyclic_annihilator,
    wrong_coset_phase_witness,
)
from observational_succ.pontryagin_source_duality import PontryaginSourceError


class CyclicPoissonControls(unittest.TestCase):
    def test_subgroup_annihilator_with_independent_integer_brute_oracle(self):
        for n in range(2,100):
            for d in range(1,n+1):
                if n%d:
                    continue
                r=exact_cyclic_annihilator(n,d)
                self.assertEqual(r["size_product"],n)
                self.assertTrue(r["two_independent_calculations_agree"])
                H=set(r["subgroup"])
                A=set(r["annihilator"])
                self.assertEqual(len(H)*len(A),n)
                self.assertTrue(all(k*x%n==0 for x in H for k in A))

    def test_finite_poisson_reconstructs_exact_original_rational_table(self):
        rng=random.Random(112244)
        for n in range(2,17):
            divs=tuple(d for d in range(1,n+1) if n%d==0)
            for _ in range(8):
                data=tuple(F(rng.randint(-11,11),rng.randint(1,10)) for _ in range(n))
                d=rng.choice(divs)
                a=rng.randint(-20,20)
                receipt=finite_poisson_coset(data,d,a)
                oracle=sum((data[(a+j*d)%n] for j in range(n//d)),F(0))
                self.assertEqual(receipt["direct_source_sum"],oracle)
                self.assertEqual(receipt["dual_sum_exact_polynomial"],
                                 CyclotomicElement.scalar(n,oracle).polynomial)
                self.assertTrue(receipt["finite_poisson_exact"])
                self.assertFalse(receipt["adelic_poisson_proved_by_finite_examples"])

    def test_extremes_h_whole_group_and_singleton(self):
        for n in range(2,25):
            data=tuple(F(x*x-2*x,7) for x in range(n))
            whole=finite_poisson_coset(data,1,5)
            self.assertEqual(whole["subgroup_size"],n)
            self.assertEqual(whole["annihilator_frequencies"],(0,))
            self.assertEqual(whole["direct_source_sum"],sum(data,F(0)))
            singleton=finite_poisson_coset(data,n,-3)
            self.assertEqual(singleton["subgroup_size"],1)
            self.assertEqual(singleton["direct_source_sum"],data[-3%n])

    def test_coset_sign_mutation_fails(self):
        r=wrong_coset_phase_witness()
        self.assertEqual(r["correct_source_sum"],1)
        self.assertTrue(r["sign_mutation_detected"])
        self.assertEqual(r["wrong_sign_Fourier_sum"],(F(0),))

    def test_incompatible_source_shape_and_wrong_subgroup_rejected(self):
        for args in (
            ((1,),1,0), ((1,2,3,4),3,0), ((1,2,3),0,0),
            ((1,2,3),1,True), ((1,2.2),1,0)
        ):
            with self.subTest(args=args),self.assertRaises(PontryaginSourceError):
                finite_poisson_coset(*args)
        with self.assertRaises(PontryaginSourceError):
            finite_poisson_coset((1,2,3),1,0,source_id="")
        with self.assertRaises(PontryaginSourceError):
            exact_cyclic_annihilator(6,4)


if __name__=="__main__":
    unittest.main()

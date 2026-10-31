from fractions import Fraction as Q
from itertools import product, permutations
from math import comb
from unittest import TestCase, main

from carrier_algebra import (Slot, Object, Path, SignedRank, binomial, polarized_product,
    Matrix, ONE, ZERO, matrix_sum, power_coeff_to_newton, newton_eval,
    newton_product, transport, diamond, swap_telescope, endpoint_states,
    bbp_source, affine_matrix, source_order_lift)


class CarrierAlgebraTests(TestCase):
    def test_path_category_and_associativity(self):
        slots = tuple(Slot(str(i), 'RGB'[i%3]) for i in range(7))
        for word in product((0, 1), repeat=7):
            whole = Path(Object(), slots, word)
            a, rest = whole.split(2)
            b, c = rest.split(3)
            self.assertEqual(a.then(b).then(c), a.then(b.then(c)))
            self.assertEqual(a.then(b).then(c), whole)
            self.assertEqual(Path.identity(whole.source).then(whole), whole)
            self.assertEqual(whole.then(Path.identity(whole.target)), whole)

    def test_typed_errors(self):
        s = Slot('x', 'red')
        with self.assertRaises(ValueError): Object((s, s))
        with self.assertRaises(ValueError): Path(Object(), (s,), (2,))
        with self.assertRaises(ValueError): Path(Object(), (s,), (1,)).then(Path.identity(Object()))
        with self.assertRaises(ValueError): SignedRank(-1, 0)

    def test_vandermonde_bijection(self):
        for a, b in product(range(5), repeat=2):
            counts = [0]*(a+b+1)
            for word in product((0, 1), repeat=a+b):
                counts[sum(word)] += 1
            for k in range(a+b+1):
                expected = sum(comb(a,j)*comb(b,k-j) for j in range(a+1) if 0<=k-j<=b)
                self.assertEqual(counts[k], expected)

    def test_signed_completion_representatives(self):
        for p,n,a,b,t in product(range(4), repeat=5):
            x,alias,y = SignedRank(p,n),SignedRank(p+t,n+t),SignedRank(a,b)
            self.assertTrue(x.equivalent(alias))
            self.assertTrue((x*y).equivalent(alias*y))
            self.assertEqual((x*y).value, polarized_product(x.value, y.value))
            self.assertTrue((x+-x).equivalent(SignedRank(0,0)))

    def test_negative_pascal_and_lost_colour(self):
        self.assertEqual(binomial(-1, 1), -1)
        self.assertEqual(binomial(-1, 2), 1)
        self.assertEqual(binomial(4, 2), binomial(1+3, 2))
        self.assertNotEqual(polarized_product(1,3), polarized_product(2,2))
        for a,b,k in product(range(-5,6), range(-5,6), range(7)):
            self.assertEqual(binomial(a+b,k), sum(binomial(a,j)*binomial(b,k-j) for j in range(k+1)))

    def test_matrix_umbral_intertwining(self):
        coeff = tuple(Matrix(i+1, Q(1,i+2), 2-i, i*i) for i in range(7))
        derivative = tuple(coeff[k+1]*(k+1) for k in range(len(coeff)-1))
        a,b = power_coeff_to_newton(coeff),power_coeff_to_newton(derivative)
        for x in range(-8,10):
            self.assertEqual(newton_eval(a,x+1)-newton_eval(a,x),newton_eval(b,x))

    def test_overlap_product_and_noncommutativity(self):
        left=(Matrix(1,2,0,1),Matrix(0,1,1,0),ONE)
        right=(Matrix(1,0,2,1),Matrix(2,1,0,3))
        ordinary = newton_product(left,right)
        for x in range(-7,9):
            self.assertEqual(newton_eval(ordinary,x),newton_eval(left,x)*newton_eval(right,x))
        self.assertNotEqual(newton_product(left,right),newton_product(right,left))
        self.assertEqual(newton_product((ZERO,ONE),(ZERO,ONE)),(ZERO,ONE,ONE*2))
        self.assertEqual(newton_product((ZERO,ONE),(ZERO,ONE),True),(ZERO,ZERO,ONE*2))

    def test_transported_derivation(self):
        a=(ONE,Matrix(1,2,3,4),Matrix(0,2,1,0))
        b=(Matrix(1,0,1,1),ONE,ONE*3)
        star=newton_product(a,b,True)
        lhs=star[1:]
        r1=newton_product(a[1:],b,True)
        r2=newton_product(a,b[1:],True)
        self.assertEqual(lhs,tuple(x+y for x,y in zip(r1,r2)))

    def test_flat_and_nonflat_source_paths(self):
        a,b=Matrix(1,1,0,1),Matrix(1,0,1,1)
        edge=lambda n,k,bit:(a,b)[bit]
        self.assertNotEqual(diamond(edge,0,0),ZERO)
        self.assertNotEqual(transport((0,1),edge),transport((1,0),edge))
        scalar=lambda n,k,bit:ONE*(2 if bit else 3)
        for n in range(8):
            self.assertTrue(all(len(v)==1 for v in endpoint_states(scalar,n).values()))

    def test_reachable_flatness_is_weaker_than_operator_flatness(self):
        a,b=Matrix(1,0,0,2),Matrix(1,1,0,1)
        edge=lambda n,k,bit:(a,b)[bit]
        self.assertNotEqual(diamond(edge,0,0),ZERO)
        for n in range(8):
            self.assertTrue(all(v=={(Q(1),Q(0))} for v in endpoint_states(edge,n).values()))

    def test_swaps_retain_prefix_and_suffix(self):
        edge=lambda n,k,bit:Matrix(n+2,k+1,bit+1,n+k+3) if bit else Matrix(1,n+1,k,2)
        for word in product((0,1),repeat=7):
            sorted_word, defects=swap_telescope(word,edge,start=(2,1))
            self.assertEqual(sorted_word,tuple(sorted(word)))
            self.assertEqual(transport(word,edge,(2,1))-transport(sorted_word,edge,(2,1)),matrix_sum(defects))
        word=(1,1,0,0)
        _,defects=swap_telescope(word,edge)
        self.assertNotEqual(matrix_sum(defects),-diamond(edge,0,0)*4)

    def test_authentic_affine_commutator(self):
        for i,j in product(range(1,13),repeat=2):
            r,s=bbp_source(i),bbp_source(j)
            a,b=affine_matrix(16,r),affine_matrix(16,s)
            self.assertEqual(b*a-a*b,Matrix(0,15*(r-s),0,0))
        for n in range(1,1024):
            self.assertGreater(bbp_source(n),bbp_source(n+1))

    def test_original_order_is_strict_unwrapped_maximizer(self):
        for n in range(2,7):
            original=tuple(range(1,n+1));top=source_order_lift(original)
            for order in permutations(original):
                value=source_order_lift(order)
                if order==original:self.assertEqual(value,top)
                else:self.assertLess(value,top)
                self.assertEqual(source_order_lift(order,Q(7,11))-value,16**n*Q(7,11))

    def test_affine_swap_defect_not_a_circle_separation_bound(self):
        # Positive decreasing sources may give an integer lifted defect.
        a,b=affine_matrix(16,Q(2,15)),affine_matrix(16,Q(1,15))
        self.assertEqual((b*a-a*b).b,1)
        self.assertEqual((b*a).b%1,(a*b).b%1)


if __name__ == '__main__': main()

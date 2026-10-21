"""Hostile exact tests for the circle -> Gamma -> all primes -> digits chain.

These are finite algebraic tests; all-horizon pi normality remains OPEN.
"""
import itertools
import unittest
from collections import Counter
from fractions import Fraction as Q
from math import factorial

from observational_succ.circle_gamma_prime_digits import (
    mode_laplacian_polynomial, eval_polynomial, ordered_succ_gamma_weight,
    pi_heat_mellin_mode_bounds, genuine_prime_smooth_coefficients,
    phase_turn, mixed_prime_turn, factorized_phase_with_mixed_terms,
    rational_digits, cyclic_debruijn_edge_flow, prime_dilation_polygon_defect,
    succ_fucc_mode_covariance, prime_euler_pi_bracket
)
from observational_succ.pi_polygon_normality import polygon_pi_bracket


def independent_machin():
    def atan(q, count=25):
        value = sum(((-1)**j*q**(2*j+1)/(2*j+1)
                     for j in range(count)), Q())
        err = (-1)**count*q**(2*count+1)/(2*count+1)
        return min(value, value+err), max(value, value+err)
    a, b = atan(Q(1,5))
    c, d = atan(Q(1,239))
    return 16*a-4*d, 16*b-4*c


class CircleDiscreteModes(unittest.TestCase):
    def test_exact_polynomial_recurrence_not_just_numeric(self):
        expected = {
            0: (0,),
            1: (1,),
            2: (4,-1),
            3: (9,-6,1),
            4: (16,-20,8,-1),
        }
        for n, coeffs in expected.items():
            self.assertEqual(mode_laplacian_polynomial(n), tuple(map(Q, coeffs)))
        for n in range(1, 30):
            self.assertEqual(eval_polynomial(mode_laplacian_polynomial(n),0),n*n)

    def test_square_hexagon_spectra_and_alias_modes(self):
        self.assertEqual([eval_polynomial(mode_laplacian_polynomial(n),Q(2))
                          for n in range(5)], [0,1,2,1,0])
        self.assertEqual([eval_polynomial(mode_laplacian_polynomial(n),Q(1))
                          for n in range(7)], [0,1,3,4,3,1,0])

    def test_poisson_gamma_factorial_ratio(self):
        for rate in (Q(0), Q(1,5), Q(3,2), Q(5)):
            for n in range(0,15):
                a = ordered_succ_gamma_weight(rate,n)
                b = ordered_succ_gamma_weight(rate,n+1)
                self.assertEqual(a,Q(rate**n,factorial(n)))
                self.assertEqual(b*(n+1),a*rate)
        self.assertEqual(ordered_succ_gamma_weight(Q(2),4),Q(2,3))
        with self.assertRaises(ValueError):
            ordered_succ_gamma_weight(Q(-1),3)
        with self.assertRaises(ValueError):
            ordered_succ_gamma_weight(0.3,4)

    def test_pi_mellin_source_exact_nonzero_and_independent_holdout(self):
        actual = polygon_pi_bracket(12,256)
        machin_lo, machin_hi = independent_machin()
        self.assertLess(actual.lower, machin_lo)
        self.assertGreater(actual.upper, machin_hi)
        for q in range(1,5):
            for n in (1,2,3,7):
                lo, hi = pi_heat_mellin_mode_bounds(n,q,12,256)
                self.assertLess(lo,hi)
                f = Q(factorial(q-1),n**(2*q))
                self.assertLess(lo, f/machin_hi**q)
                self.assertGreater(hi, f/machin_lo**q)
                self.assertEqual(lo,f/actual.upper**q)
                self.assertEqual(hi,f/actual.lower**q)


class PrimeDilationCircleCovariance(unittest.TestCase):
    def test_finite_prime_defect_has_exact_chord_factor(self):
        for p in (2,3,5,7,11):
            for n in range(1,5):
                defect=prime_dilation_polygon_defect(p,n)
                self.assertEqual(defect[0],0)
                self.assertEqual(defect[1],Q(-p*p*(p*p-1)*n**4,12))
                self.assertEqual(eval_polynomial(defect,0),0)
                for x in (Q(1,9),Q(1,4),Q(1),Q(2)):
                    self.assertEqual(
                        eval_polynomial(defect,x),
                        eval_polynomial(mode_laplacian_polynomial(p*n),x)
                        -p*p*eval_polynomial(mode_laplacian_polynomial(n),x))
        self.assertEqual(prime_dilation_polygon_defect(2,1),(Q(0),Q(-1)))
        self.assertEqual(prime_dilation_polygon_defect(3,1),(Q(0),Q(-6),Q(1)))
        for fake in (4,6,9):
            with self.assertRaises(ValueError):
                prime_dilation_polygon_defect(fake,1)

    def test_circle_prime_covariance_and_finite_failure(self):
        for p in (2,3,5,7):
            for n in range(20):
                left,right=succ_fucc_mode_covariance(p,n)
                self.assertEqual(left,right)
                self.assertEqual(left,p*(n+1))
        # At square m=4, chord²=2: lambda_2=2 but 4*lambda_1=4.
        self.assertEqual(eval_polynomial(prime_dilation_polygon_defect(2,1),2),-2)
        # On continuum X=0 the mismatch vanishes, but dividing by X
        # retains a nonzero first-order geometric defect -1.
        self.assertEqual(prime_dilation_polygon_defect(2,1)[1],-1)
        with self.assertRaises(ValueError):
            succ_fucc_mode_covariance(6,1)


class PrimeSystemWithPhases(unittest.TestCase):
    def test_genuine_finite_euler_boxes_keep_all_mixed_primes(self):
        for primes in ((2,3), (2,3,5), (3,5,7)):
            for s,k in itertools.product((2,3),range(3)):
                coeffs = genuine_prime_smooth_coefficients(primes,k,s)
                self.assertEqual(len(coeffs),(k+1)**len(primes))
                self.assertEqual(coeffs[1],1)
                self.assertEqual(
                    sum(coeffs.values(),Q(0)),
                    __import__('math').prod(
                        sum((Q(1,p**(s*j)) for j in range(k+1)),Q(0))
                        for p in primes))
                for n,v in coeffs.items():
                    self.assertEqual(v,Q(1,n**s))
        c=genuine_prime_smooth_coefficients((2,3,5),1,2)
        self.assertEqual(c[30],Q(1,900))
        for fake in ((2,6),(2,2),(1,2),(3,9),(4,),()):
            with self.assertRaises(ValueError):
                genuine_prime_smooth_coefficients(fake,2,2)

    def test_mixed_phase_is_required_and_associative(self):
        for x in (Q(0), Q(1,7), Q(2,11), Q(1,2), Q(-3,13)):
            for a,b,c in itertools.product(range(1,7),repeat=3):
                self.assertEqual(
                    (phase_turn(a*b,x)-phase_turn(a,x)-phase_turn(b,x)
                     -mixed_prime_turn(a,b,x))%1,0)
                self.assertEqual(
                    (mixed_prime_turn(a,b,x)+mixed_prime_turn(a*b,c,x)
                     -mixed_prime_turn(b,c,x)-mixed_prime_turn(a,b*c,x))%1,0)
        self.assertEqual(mixed_prime_turn(2,3,Q(1,7)),Q(2,7))
        result=factorized_phase_with_mixed_terms((2,3),Q(1,7))
        self.assertEqual(result,(6,Q(5,7),Q(3,7),Q(2,7)))
        self.assertNotEqual(result[1],result[2])

    def test_factorization_independence_with_all_mixed_terms(self):
        for factors in ((2,3,5),(2,2,3),(2,3,7),(3,5,11),(2,3,5,7)):
            for x in (Q(0),Q(1,7),Q(1,11),Q(5,13)):
                result=factorized_phase_with_mixed_terms(factors,x)
                for perm in set(itertools.permutations(factors)):
                    other=factorized_phase_with_mixed_terms(perm,x)
                    self.assertEqual(other[0],result[0])
                    self.assertEqual(other[1],result[1])
                    self.assertEqual((other[2]+other[3])%1,result[1])
        with self.assertRaises(ValueError):
            phase_turn(4,0.125)
        with self.assertRaises(ValueError):
            factorized_phase_with_mixed_terms((),Q(0))
        for forged in ((6,), (10,), (1,), (2,6), (2,15)):
            with self.assertRaises(ValueError):
                factorized_phase_with_mixed_terms(forged,Q(1,7))


    def test_base_shift_is_prime_fucc_diagonal_not_all_prime_enumeration(self):
        for b, primes in ((2,(2,)),(6,(2,3)),(10,(2,5))):
            for j in range(8):
                target=b**j
                extracted=1
                for p in primes:
                    v=target
                    k=0
                    while v%p==0:
                        v//=p
                        k+=1
                    extracted*=p**k
                    self.assertEqual(v, target//p**k)
                self.assertEqual(extracted,target)


class FullPrimeToGeometricPiInverse(unittest.TestCase):
    def test_prime_prefix_interval_certifies_same_pi_as_polygon_and_machin(self):
        machin_lo,machin_hi=independent_machin()
        polygon=polygon_pi_bracket(12,256)
        for P in (2,3,5,7,10,29,100,200):
            br=prime_euler_pi_bracket(P,256)
            self.assertEqual(br.cutoff,P)
            self.assertEqual(br.missing_zeta_upper,Q(1,P))
            self.assertLess(br.lower_pi,machin_lo)
            self.assertGreater(br.upper_pi,machin_hi)
            self.assertLess(br.lower_pi,polygon.upper)
            self.assertGreater(br.upper_pi,polygon.lower)
            self.assertLessEqual(br.lower_pi**2,6*br.euler_partial)
            self.assertGreaterEqual(br.upper_pi**2,6*(br.euler_partial+Q(1,P)))
            self.assertTrue(all(p>=2 and all(p%d for d in range(2,int(p**.5)+1))
                                for p in br.genuine_primes))
        self.assertEqual(prime_euler_pi_bracket(3,256).euler_partial,Q(3,2))
        self.assertEqual(prime_euler_pi_bracket(5,256).euler_partial,Q(25,16))
        self.assertGreater(prime_euler_pi_bracket(200,256).lower_pi,
                           prime_euler_pi_bracket(100,256).lower_pi)

    def test_missing_prime_breaks_claimed_full_prefix_tail_bound(self):
        # Fake set {2,5} at cutoff P=5, omitting prime 3:
        # 25/18 + 1/5 < sum_{n=1}^{30} 1/n² < zeta(2).
        # Hence a falsely claimed full-prime interval would miss pi.
        forged = Q(2*2,2*2-1)*Q(5*5,5*5-1)
        self.assertEqual(forged,Q(25,18))
        actual_partial_harmonic=sum((Q(1,n*n) for n in range(1,31)),Q())
        self.assertGreater(actual_partial_harmonic,forged+Q(1,5))
        for invalid in (1,True,5.0,Q(5)):
            with self.assertRaises(ValueError):
                prime_euler_pi_bracket(invalid)


class HierarchicalDigitTransport(unittest.TestCase):
    def test_prime_seven_half_carrier_and_complete_cosets(self):
        # Multiplication-by-2 on all nonzero units of the prime clock 7.
        cycles=((1,2,4),(3,6,5))
        bits=[]
        for cycle in cycles:
            for r in cycle:
                # Euclidean digit recurrence: d=floor(2r/7).
                bits.append((2*r)//7)
        self.assertEqual(tuple(bits),(0,0,1,0,1,1))
        self.assertEqual(Counter(bits),{0:3,1:3})
        # Each 3-cycle has 3 two-block edges and 3 three-block edges.
        combined_edges=Counter()
        triple_edges=Counter()
        for cycle in cycles:
            word=tuple((2*r)//7 for r in cycle)
            two, inc, out = cyclic_debruijn_edge_flow(word,2,2)
            three, _, _ = cyclic_debruijn_edge_flow(word,2,3)
            self.assertEqual(inc,out)
            combined_edges.update(two)
            triple_edges.update(three)
        self.assertEqual(combined_edges,{(0,0):1,(0,1):2,(1,0):2,(1,1):1})
        self.assertEqual(len(triple_edges),6)
        self.assertEqual(set(triple_edges.values()),{1})

    def test_even_when_one_digit_uniform_block_transitions_are_not(self):
        self.assertEqual(rational_digits(Q(1,3),2,12),(0,1)*6)
        edges, incoming, outgoing=cyclic_debruijn_edge_flow((0,1)*50,2,2)
        self.assertEqual(incoming,outgoing)
        self.assertEqual(edges,{(0,1):50,(1,0):50})
        self.assertNotIn((0,0),edges)
        self.assertNotIn((1,1),edges)
        # Zero phase has legitimate circle geometry but biased orbit.
        bad, _, _=cyclic_debruijn_edge_flow(rational_digits(0,2,20),2,2)
        self.assertEqual(bad,{(0,0):20})
        with self.assertRaises(ValueError):
            cyclic_debruijn_edge_flow((0,1.0),2,2)


if __name__=="__main__":
    unittest.main()

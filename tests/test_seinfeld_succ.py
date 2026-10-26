"""Exact independent tests for Seinfeld SUCC; no float or pi digits."""
from __future__ import annotations
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ import seinfeld_succ as S


class ZeroProvenance(unittest.TestCase):
    def test_zero_is_not_missing_formal_structure(self):
        w = S.step_witness(1)
        self.assertNotEqual(w.coefficients(), {})
        self.assertEqual(w.evaluate(S.source_values(1)), 0)
        self.assertEqual(w.evaluate(S.source_values(1,S.counterfeit_forcing)),0)

    def test_telescoping_as_formal_syzygy(self):
        for n in range(4):
            for k in range(1,9):
                left,right=S.telescope_witness(n,k)
                self.assertEqual(left.coefficients(),right.coefficients())
                source=S.source_values(n+k)
                self.assertEqual(left.evaluate(source), Q(0))
                self.assertEqual(right.evaluate(source), Q(0))

    def test_reference_independent_macro_unrolling(self):
        states=S.source_states(20)
        for n in range(3):
            for k in range(1,8):
                corr=sum((16**(k-j)*S.bbp_forcing(n+j) for j in range(1,k+1)),Q())
                self.assertEqual(states[n+k]-16**k*states[n],corr)

    def test_rank_and_anchor_exact(self):
        for n in range(1,10):
            r=S.recurrence_rank_receipt(n)
            self.assertEqual((r['step_rank'],r['with_macro_rank'],r['with_anchor_rank']),
                             (n,n,n+1))

    def test_rank_bad_domain(self):
        with self.assertRaises(S.NullSourceError):S.rational_rank(((1,2),(1,)))
        with self.assertRaises(S.NullSourceError):S.recurrence_rank_receipt(0)

    def test_missing_source_generator_is_error(self):
        with self.assertRaises(S.NullSourceError):S.step_witness(1).evaluate({'U:1':Q(0)})


class BackwardFibers(unittest.TestCase):
    def test_full_circle_has_sixteen_to_the_k_origins(self):
        actual=S.source_states(6)
        for k in range(1,4):
            target=actual[k]%1
            fiber=S.circle_backward_fiber(target,tuple(S.bbp_forcing(j) for j in range(1,k+1)))
            self.assertEqual(len(fiber),16**k)
            self.assertEqual(len(set(fiber)),16**k)
            self.assertIn(Q(),fiber)
            self.assertTrue(all(Q()<=x<1 for x in fiber))
            self.assertEqual(sum(x.denominator%2 for x in fiber),1)

    def test_unique_odd_inverse_all_authentic_steps(self):
        states=S.source_states(45)
        for n in range(1,45):
            y=states[n]%1
            x=S.odd_torsion_inverse(y,S.bbp_forcing(n))
            self.assertEqual(x,states[n-1]%1)
            self.assertEqual((16*x+S.bbp_forcing(n))%1,y)

    def test_unique_odd_history(self):
        states=S.source_states(12)
        forcing=tuple(S.bbp_forcing(j) for j in range(1,13))
        out=S.backward_odd_history(states[-1]%1,forcing)
        self.assertEqual(out,tuple(y%1 for y in states))

    def test_nonnormal_counterfeit_has_unique_odd_inverse_too(self):
        states=S.source_states(35,S.counterfeit_forcing)
        for n in range(1,35):
            self.assertEqual(S.odd_torsion_inverse(states[n]%1,S.counterfeit_forcing(n)),states[n-1]%1)

    def test_inverse_not_circle_continuous(self):
        for k in (1,2,5,100):
            (yminus,xminus),(yplus,xplus)=S.inverse_discontinuity(k)
            self.assertEqual(yminus,Q(1,16*k-1))
            self.assertEqual(xminus,Q(k,16*k-1))
            self.assertEqual(yplus,Q(1,16*k+1))
            self.assertEqual(xplus,Q(15*k+1,16*k+1))
        # All targets tend to 0, but source-specific inverses approach 1/16 or 15/16.

    def test_even_torsion_is_not_a_lawful_odd_source(self):
        with self.assertRaises(S.NullSourceError):S.odd_torsion_inverse(Q(1,2),0)
        with self.assertRaises(S.NullSourceError):S.odd_torsion_inverse(Q(1,7),Q(1,8))


class FrobeniusLifts(unittest.TestCase):
    def test_integral_coefficients(self):
        for p in (2,3,5,7,11,13):
            self.assertTrue(all(comb(p,j)%p==0 for j in range(1,p)))
            x,y=Q(7,11),Q(2,17)
            result=S.frobenius_relation(p,x,y)
            self.assertEqual(result['zero'],0)
            self.assertEqual(result['carry'],((x+y)**p-x**p-y**p)/p)

    def test_genuine_BBP_lift_at_each_prime(self):
        for n in range(1,6):
            for p in (2,3,5,7):
                cert=S.bbp_frobenius_relation(n,p)
                self.assertEqual(cert['zero'],0)
                if p==2:self.assertTrue(cert['p_integral'])
                if n==1 and p in (3,5):self.assertFalse(cert['p_integral'])

    def test_frobenius_not_primitive_composite(self):
        with self.assertRaises(S.NullSourceError):S.frobenius_relation(6,1,1)
        with self.assertRaises(S.NullSourceError):S.frobenius_relation(1,1,1)
        with self.assertRaises(S.NullSourceError):S.frobenius_relation(2,1.0,1)


class HostileSources(unittest.TestCase):
    def test_authenticated_first_four_poles_differ(self):
        self.assertEqual(S.bbp_forcing(1),Q(47,15))
        self.assertEqual(S.counterfeit_forcing(1),Q(527,99))
        self.assertNotEqual(S.bbp_forcing(1),S.counterfeit_forcing(1))

    def test_counterfeit_coherent_but_nonnormal(self):
        values=S.source_states(60,S.counterfeit_forcing)
        self.assertEqual(values[0],0)
        for n, u in enumerate(values):
            self.assertEqual(u,S.counterfeit_closed_state(n))
            self.assertEqual(u.denominator%2,1)
            if n:
                self.assertGreater(S.counterfeit_forcing(n),0)
                self.assertTrue(S.counterfeit_is_confined(n))
                self.assertEqual(S.counterfeit_phase(n),Q(1,3)-S.counterfeit_tail(n))

    def test_same_quadratic_leading_coefficient(self):
        # Rational two-sided asymptotic diagnostic; proof in the paper is algebraic.
        for n in (100,1000,10000):
            target=Q(15,64)
            self.assertLess(abs(n*n*S.bbp_forcing(n)-target), Q(1,40))
            self.assertLess(abs(n*n*S.counterfeit_forcing(n)-target), Q(1,40))

    def test_counterfeit_not_dyadic_isometry(self):
        # n=0 to n=2 has v2(index gap)=1 but v2(source gap)=0.
        self.assertEqual(S.counterfeit_closed_state(2).numerator%2,1)
        self.assertEqual(S.counterfeit_closed_state(2).denominator%2,1)

    def test_negative_control_breaks_false_pi_implication(self):
        # Every finite zero witness and odd inverse is valid for this fake,
        # but its fractional phases are trapped in (1/4,1/3).
        values=S.source_values(12,S.counterfeit_forcing)
        for n in range(1,13):
            self.assertEqual(S.step_witness(n).evaluate(values),0)
            self.assertTrue(S.counterfeit_is_confined(n))


class AffineNullHomology(unittest.TestCase):
    def test_nonempty_chain_is_cycle(self):
        for n in range(1,6):
            for p in (2,3,5,7):
                chain=S.affine_null_loop(n,p)
                self.assertTrue(chain)
                self.assertEqual(S.chain_boundary(chain),{})
                self.assertEqual(sum(chain.values()),1-p)  # route has 2 vs p+1 edges

    def test_zero_boundary_not_zero_holonomy(self):
        chain=S.affine_null_loop(2,3)
        weights={e: Q(e[1]) if e[0]=='S' else Q() for e in chain}
        self.assertEqual(S.chain_holonomy(chain,weights),Q(2-(6+7+8)))
        self.assertNotEqual(S.chain_holonomy(chain,weights),0)

    def test_every_exact_gradient_closes(self):
        for n in range(1,5):
            for p in (2,3,5):
                chain=S.affine_null_loop(n,p)
                endpoint=p*(n+1)
                states=S.source_states(endpoint)
                potential={j:states[j] for j in range(1,endpoint+1)}
                self.assertEqual(S.gradient_transport(chain,potential),0)
                counterfeit=S.source_states(endpoint,S.counterfeit_forcing)
                fake={j:counterfeit[j] for j in range(1,endpoint+1)}
                self.assertEqual(S.gradient_transport(chain,fake),0)

    def test_fake_composite_not_a_prime_generator(self):
        with self.assertRaises(S.NullSourceError):S.affine_null_loop(3,6)
        with self.assertRaises(S.NullSourceError):S.edge_endpoints(('V',3,6))


if __name__=='__main__':
    unittest.main()

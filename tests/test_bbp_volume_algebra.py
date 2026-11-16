"""Exact finite controls for the source-labelled Green/volume compiler."""

from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest

from observational_succ.bbp_volume_algebra import (
    AffineStep, MAX_DEPTH, MAX_HORIZON, RationalLift, Stage, WordPolynomial,
    bbp_channels, bbp_expression, carry_cocycle, evaluate, green_sum, gamma_geometric_sum,
    integer_gamma_weights, lift_moduli, phase_residue, polynomial_lift_matrix,
)


def forcing(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def explicit_word(word, table, n):
    """Independent chain enumeration, not nested recurrence evaluation."""
    if not word:
        return Q(1)
    total = Q(0)
    for indices in product(range(1, n + 1), repeat=len(word)):
        if any(indices[j] < indices[j+1] for j in range(len(indices)-1)):
            continue
        value, parent = Q(1), n
        for stage, index in zip(word, indices):
            value *= stage.radix ** (parent - index)
            for label in stage.factors:
                value *= table[label][index-1]
            parent = index
        total += value
    return total


class GradedGreenTests(unittest.TestCase):
    def setUp(self):
        self.table = {
            "a": tuple(Q((-1)**n*(n+2), n+1) for n in range(7)),
            "b": tuple(Q(n-2, n+3) for n in range(7)),
            "c": tuple(Q(1, 2*n+1) for n in range(7)),
        }

    def test_two_letter_product_has_collision_and_radix_grade(self):
        a, b = WordPolynomial.atom(16, "a"), WordPolynomial.atom(3, "b")
        expected = WordPolynomial((
            ((Stage(48, ("a",)), Stage(3, ("b",))), Q(1)),
            ((Stage(48, ("b",)), Stage(16, ("a",))), Q(1)),
            ((Stage(48, ("a", "b")),), Q(-1)),
        ))
        self.assertEqual(a*b, expected)
        x, y = evaluate(a, self.table, 7), evaluate(b, self.table, 7)
        self.assertEqual(evaluate(a*b, self.table, 7), tuple(u*v for u,v in zip(x,y)))

    def test_nested_word_against_ordered_indices(self):
        word = (Stage(Q(2,3), ("a",)), Stage(5, ("b","c")), Stage(2, ()))
        expr = WordPolynomial(((word,Q(3,7)),))
        row = evaluate(expr, self.table, 7)
        for n in range(8):
            self.assertEqual(row[n], Q(3,7)*explicit_word(word,self.table,n))

    def test_products_of_nested_words(self):
        words = [(), (Stage(2,("a",)),),
                 (Stage(3,("b",)),Stage(Q(1,2),("c",))),
                 (Stage(1,("a","b")),Stage(4,()))]
        for left,right in product(words,repeat=2):
            a,b = WordPolynomial(((left,Q(1)),)),WordPolynomial(((right,Q(1)),))
            x,y = evaluate(a,self.table,7),evaluate(b,self.table,7)
            self.assertEqual(evaluate(a*b,self.table,7),tuple(u*v for u,v in zip(x,y)))

    def test_formal_associativity_commutativity_and_distributivity(self):
        a,b,c = (WordPolynomial.atom(q,label) for q,label in ((2,"a"),(3,"b"),(5,"c")))
        objects = (a,b,c,a*b,WordPolynomial.one())
        for x,y,z in product(objects,repeat=3):
            self.assertEqual((x*y)*z,x*(y*z))
        self.assertEqual(a*b,b*a)
        self.assertEqual(a*(b+c),a*b+a*c)
        self.assertEqual(a*WordPolynomial(),WordPolynomial())

    def test_collection_retains_source_labels(self):
        a,b = WordPolynomial.atom(16,"a"),WordPolynomial.atom(16,"b")
        self.assertEqual(a+a.scale(-1),WordPolynomial())
        self.assertNotEqual(a,b)
        # Equal source rows do not authorize equality of source provenance.
        equal_table = {"a": (Q(1),), "b": (Q(1),)}
        self.assertEqual(evaluate(a,equal_table,1),evaluate(b,equal_table,1))
        self.assertEqual(Stage(2,("b","a")),Stage(2,("a","b")))

    def test_source_identity_without_pi_input(self):
        expected=[Q(0)]
        for n in range(1,49):
            expected.append(16*expected[-1]+forcing(n))
        self.assertEqual(evaluate(bbp_expression(),bbp_channels(48),48),tuple(expected))
        self.assertEqual(expected[:3],[Q(0),Q(47,15),Q(205826,4095)])

    def test_fully_expanded_bbp_powers(self):
        expr=bbp_expression()
        source=evaluate(expr,bbp_channels(9),9)
        for degree in range(5):
            expanded=expr.power(degree)
            self.assertEqual(evaluate(expanded,bbp_channels(9),9),tuple(u**degree for u in source))
        self.assertEqual(len(expr.power(2).terms),26)
        self.assertEqual(len(expr.power(3).terms),164)

    def test_wrong_radix_and_missing_collision_are_detected(self):
        f,g=(Q(1),Q(1)),(Q(1),Q(1))
        x,y=green_sum(f,16),green_sum(g,16)
        correct=[f[n-1]*y[n]+g[n-1]*x[n]-f[n-1]*g[n-1] for n in (1,2)]
        self.assertEqual(green_sum(correct,256)[2],x[2]*y[2])
        self.assertNotEqual(green_sum(correct,16)[2],x[2]*y[2])
        missed=[f[n-1]*y[n]+g[n-1]*x[n] for n in (1,2)]
        self.assertNotEqual(green_sum(missed,256)[1],x[1]*y[1])

    def test_seeded_product_boundary_is_required(self):
        f,g=self.table["a"],self.table["b"]
        x,y=green_sum(f,2,Q(3,5)),green_sum(g,3,Q(-2,7))
        driver=tuple(f[n-1]*y[n]+g[n-1]*x[n]-f[n-1]*g[n-1] for n in range(1,8))
        expected=green_sum(driver,6,Q(-6,35))
        self.assertEqual(expected,tuple(a*b for a,b in zip(x,y)))
        wrong=green_sum(driver,6)
        self.assertEqual(tuple(a-b for a,b in zip(expected,wrong)),tuple(Q(-6,35)*6**n for n in range(8)))

    def test_polynomial_lift_intertwines_affine_action(self):
        for radix,force,u,degree in product((Q(1,3),Q(16)),(Q(-2,7),Q(47,15)),
                                          (Q(-3,2),Q(0),Q(5,11)),range(7)):
            matrix=polynomial_lift_matrix(radix,force,degree)
            current=tuple(u**j for j in range(degree+1))
            result=tuple(sum((a*b for a,b in zip(row,current)),Q(0)) for row in matrix)
            self.assertEqual(result,tuple((radix*u+force)**j for j in range(degree+1)))

    def test_state_second_order_rational_recurrence(self):
        u=evaluate(bbp_expression(),bbp_channels(40),40)
        for n in range(1,40):
            q=forcing(n+1)/forcing(n)
            self.assertEqual(u[n+1]-(16+q)*u[n]+16*q*u[n-1],0)

    def test_power_green_hierarchy(self):
        u=evaluate(bbp_expression(),bbp_channels(12),12)
        for degree in range(1,7):
            driver=tuple(sum(((-1)**(j+1)*comb(degree,j)*forcing(n)**j*u[n]**(degree-j)
                              for j in range(1,degree+1)),Q(0)) for n in range(1,13))
            self.assertEqual(green_sum(driver,16**degree),tuple(x**degree for x in u))

    def test_exact_domains_and_resource_budgets(self):
        for bad in (1.0,True,"1"):
            with self.assertRaises((TypeError,ValueError)):
                Stage(bad,("a",))
            with self.assertRaises((TypeError,ValueError)):
                green_sum((bad,),16)
        with self.assertRaises(ValueError):
            evaluate(WordPolynomial.atom(2,"missing"),self.table,7)
        with self.assertRaises(ValueError):
            evaluate(WordPolynomial.one(),{"a":(Q(1),)},2)
        with self.assertRaises(ValueError):
            bbp_channels(MAX_HORIZON+1)
        with self.assertRaises(ValueError):
            WordPolynomial.atom(2,"a").power(MAX_DEPTH+1)
        with self.assertRaises(ValueError):
            Stage(0,("a",))


class CarryAndGammaTests(unittest.TestCase):
    def test_negative_and_positive_lifts(self):
        for q in (Q(-17,4),Q(-1),Q(0),Q(47,15),Q(11,7)):
            lift=RationalLift.from_rational(q)
            self.assertEqual(lift.value,q)
            self.assertTrue(0 <= lift.fraction < 1)

    def test_original_phase_and_carry_recurrence(self):
        state=RationalLift.from_rational(0)
        carries=[]
        for n in range(1,41):
            old=state
            state,carry=AffineStep(16,forcing(n)).apply(old)
            carries.append(carry)
            self.assertEqual(state.value,16*old.value+forcing(n))
            self.assertEqual(state.integer,16*old.integer+carry)
            for h in (-3,1,5):
                self.assertEqual(phase_residue(state.fraction,h),phase_residue(16*old.fraction+forcing(n),h))
        self.assertEqual(carries[:2],[3,2])

    def test_chronological_composition_and_carry_cocycle(self):
        for theta,b,c,s,t in product((Q(0),Q(1,7),Q(6,7)),(2,16),(3,5),
                                     (Q(-3,4),Q(2,5)),(Q(1,2),Q(7,3))):
            first,second=AffineStep(c,t),AffineStep(b,s)
            initial=RationalLift(4,theta)
            middle,c1=first.apply(initial)
            final,c2=second.apply(middle)
            direct,total=second.after(first).apply(initial)
            self.assertEqual(direct,final)
            self.assertEqual(total,b*c1+c2)
        self.assertNotEqual(AffineStep(16,Q(1,3)).after(AffineStep(16,Q(1,5))),
                            AffineStep(16,Q(1,5)).after(AffineStep(16,Q(1,3))))

    def test_additive_section_two_cocycle(self):
        values=(Q(-8,5),Q(0),Q(1,3),Q(4,5),Q(9,7))
        for a,b,c in product(values,repeat=3):
            self.assertEqual(carry_cocycle(a,b)+carry_cocycle(a+b,c),
                             carry_cocycle(b,c)+carry_cocycle(a,b+c))

    def test_weighted_phase_needs_lift_moduli(self):
        weights=(Q(1,2),Q(2,3),Q(-5,7),Q(4))
        theta=(Q(1,5),Q(2,9),Q(1,11),Q(0))
        for h in (-3,1,2,21):
            moduli=lift_moduli(weights,h)
            base=sum((w*t for w,t in zip(weights,theta)),Q(0))
            for j,q in enumerate(moduli):
                self.assertEqual(phase_residue(base,h),phase_residue(base+weights[j]*q,h))
                if q>1:
                    self.assertNotEqual(phase_residue(base,h),phase_residue(base+weights[j],h))
        self.assertEqual(lift_moduli(weights,0),(1,1,1,1))
        self.assertEqual(phase_residue(Q(0)),Q(0))
        self.assertEqual(phase_residue(Q(1,2)),Q(1,2))

    def test_gamma_composition_keeps_omitted_mass(self):
        for a,b in product(range(1,5),repeat=2):
            x,y,z=integer_gamma_weights(a,18),integer_gamma_weights(b,18),integer_gamma_weights(a+b,18)
            self.assertLess(sum(x),1)
            for n in range(19):
                self.assertEqual(sum((x[j]*y[n-j] for j in range(n+1)),Q(0)),z[n])
        self.assertEqual(integer_gamma_weights(2,4),(Q(1,4),Q(1,4),Q(3,16),Q(1,8),Q(5,64)))

    def test_tempering_rate_and_positive_series_gate(self):
        for shape,rate in product((1,2,5),(Q(1,3),Q(1),Q(16),Q(32))):
            self.assertEqual(gamma_geometric_sum(shape,rate,1),1)
            weights=integer_gamma_weights(shape,10,rate)
            self.assertEqual(weights[0],(rate/(rate+1))**shape)
            for j in range(10):
                self.assertEqual(weights[j+1]/weights[j],Q(j+shape,j+1)/(rate+1))
        self.assertEqual(gamma_geometric_sum(2,16,16),256)
        self.assertEqual(gamma_geometric_sum(3,32,16),Q(32,17)**3)
        for shape,rate in product((1,2,5),(1,7,15)):
            with self.assertRaises(ValueError):
                gamma_geometric_sum(shape,rate,16)
        for rate in (0,-1,True,0.5):
            with self.assertRaises((TypeError,ValueError)):
                integer_gamma_weights(2,4,rate)

    def test_gamma_lift_moduli_grow(self):
        for shape,h in product((1,2,3,7),(1,3,8)):
            weights=integer_gamma_weights(shape,80)
            q=lift_moduli(weights,h)
            for j in range(81):
                self.assertGreaterEqual(q[j],Q(2**(j+shape),h*comb(j+shape-1,j)))
            self.assertGreater(q[-1],2**40)

    def test_raw_forward_bbp_gamma_terms_grow(self):
        u=evaluate(bbp_expression(),bbp_channels(30),30)
        for shape in (1,2,5):
            w=integer_gamma_weights(shape,28)
            terms=[w[j]*u[j+1] for j in range(29)]
            for left,right in zip(terms,terms[1:]):
                self.assertGreater(right,8*left)

    def test_lift_and_gamma_invalid_domains(self):
        for args in ((0,Q(1)),(0,Q(-1,3)),(True,Q(0)),(0,0.5)):
            with self.assertRaises((TypeError,ValueError)):
                RationalLift(*args)
        for radix in (0,-2,True,Q(3,2)):
            with self.assertRaises(ValueError):
                AffineStep(radix,Q(1))
        for shape in (0,-1,True,Q(1,2),17):
            with self.assertRaises(ValueError):
                integer_gamma_weights(shape,3)
        with self.assertRaises(TypeError):
            lift_moduli((0.5,),1)
        with self.assertRaises(TypeError):
            phase_residue(Q(1,3),True)


if __name__ == "__main__":
    unittest.main()

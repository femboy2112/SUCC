"""Exact controls and finite diagnostics for original-source arctan reciprocity.

The tests do not establish the selected all-horizon sine estimate.
"""
from __future__ import annotations
import cmath
import importlib.util
import math
import pathlib
import sys
import unittest
from fractions import Fraction as F

HERE=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'arctan_reciprocity'
spec=importlib.util.spec_from_file_location('succ_arctan_mirror_'+str(id(object())),HERE/'arctan_mirror.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)


def gauss_mul(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def gauss_power(a,n):
    out=F(1),F(0)
    for _ in range(n):out=gauss_mul(out,a)
    return out


def source_fractions(n):
    x=F(0)
    out=[]
    for i in range(1,n+1):
        x=(16*x+m.forcing(i))%1
        out.append(x)
    return out


def finite_phasors(n,h):
    return sum((cmath.exp(2j*math.pi*h*float(x)) for x in source_fractions(n)),0j)/n

class OriginalSource(unittest.TestCase):
    def test_original_four_poles_combined(self):
        for n in range(1,90):self.assertEqual(m.forcing(n),m.forcing_combined(n))

    def test_original_first_terms(self):
        self.assertEqual(m.forcing(1),F(47,15))
        self.assertEqual(m.forcing(2),F(106,819))
        self.assertEqual(m.rational_orbit(1)[0],F(2,15))

    def test_source_tail_r_is_small(self):
        for j in range(1,120):
            self.assertGreater(m.forcing(j+1),0)
            self.assertLess(m.forcing(j+1),F(15,64*j*j))

    def test_source_step_sum_bound(self):
        for n in (1,2,3,8,17,64):
            self.assertLess(m.source_step_sum(n),F(15,32))
            self.assertLessEqual(m.radix_discrepancy_bound(n,3),m.uniform_radix_bound(n,3))

    def test_rational_seed_is_typed(self):
        with self.assertRaises(m.ReciprocityError):m.rational_orbit(2,seed=0.5)

    def test_harmonics_are_typed(self):
        for f in (m.mirror_sine_squared,m.gaussian_commutator_distance_squared):
            with self.assertRaises(m.ReciprocityError):f(0)

    def test_pi_rational_brackets(self):
        a,b=m.pi_bracket(18)
        self.assertLess(a,b)
        self.assertGreater(a,3)
        self.assertLess(b,F(22,7))
        # Never compare ~1e-32 rational intervals to binary64 math.pi.
        self.assertLess(b-a,F(1,10**24))

    def test_source_alpha_brackets(self):
        pl,pu=m.pi_bracket(22)
        for n in range(1,12):
            a,b=m.source_axis_bracket(n)
            self.assertLess(a,pl/16)
            self.assertGreater(b,pu/16)
            self.assertLess(b-a,F(1,64*n*n*16**n))

    def test_source_midpoint_error_budget(self):
        for n in range(1,15):
            self.assertLess(m.axis_midpoint_error(n),F(1,128*n*n*16**n))
            self.assertLess(m.mirror_axis_discrepancy_bound(n,1),F(22,7)*F(1,128*n*n*16**n))

    def test_geometry_path_error_budget(self):
        self.assertEqual(m.geometric_axis_discrepancy_bound(1,1),F(11,5376))
        self.assertLess(m.geometric_axis_discrepancy_bound(5,7),F(1,10**10))


class ReciprocalProjective(unittest.TestCase):
    def test_mobius_involution_integer_matrix(self):
        for a,b in [(0,1),(1,0),(1,1),(-1,1),(2,3),(F(5,7),F(3,17))]:
            c,d=m.projective_rational_mirror(a,b)
            e,f=m.projective_rational_mirror(c,d)
            self.assertEqual(e,681997*a)
            self.assertEqual(f,681997*b)

    def test_exact_rational_source_axis(self):
        x=m.rational_mirror_label()
        self.assertEqual(x['q'],F(106,819))
        self.assertEqual(x['gamma_real'],F(659525,681997))
        self.assertEqual(x['gamma_imag'],F(173628,681997))
        self.assertEqual(x['gamma_real']**2+x['gamma_imag']**2,1)

    def test_rational_reciprocal_rotation(self):
        q=F(106,819)
        for t in [F(1,2),F(-2,3),F(3,7),F(100,3),F(-1,19)]:
            a,b=m.projective_rational_mirror(t,1)
            self.assertEqual(a/b,(q-t)/(1+q*t))
            k=1/t
            tau=-1/q
            self.assertEqual((k+tau)/(1-tau*k),a/b)

    def test_circle_angle_involution(self):
        q=F(106,819)
        beta=math.atan(float(q))/math.pi
        for x in (0.001,0.05,0.12,0.26,0.42,0.75):
            t=math.tan(math.pi*x)
            a,b=m.projective_rational_mirror(F.from_float(t),1)
            lhs=float(a/b)
            expected=math.tan(math.pi*(beta-x))
            self.assertAlmostEqual(lhs,expected,places=10)

    def test_gaussian_integer_powers(self):
        for n in range(0,22):
            self.assertEqual(m.gaussian_integer_power(819,-106,n),gauss_power((819,-106),n))

    def test_source_mirror_not_torsion(self):
        g=m.rational_mirror_label()
        self.assertNotEqual(g['gamma_real'],0)
        self.assertNotEqual(g['gamma_imag'],0)
        # all roots of unity in Q(i) are +-1,+-i, hence gamma is infinite order.
        for sign in [-1,1]:
            self.assertNotEqual((g['gamma_real'],g['gamma_imag']),(F(sign),F(0)))
            self.assertNotEqual((g['gamma_real'],g['gamma_imag']),(F(0),F(sign)))

    def test_exact_gaussian_commutator(self):
        g=m.rational_mirror_label()
        gamma=(g['gamma_real'],g['gamma_imag'])
        for h in (1,2,3,5,7):
            z=gauss_power(gamma,15*h)
            diff2=(z[0]-1)**2+z[1]**2
            self.assertEqual(diff2,m.gaussian_commutator_distance_squared(h))
            self.assertEqual(diff2,4*m.mirror_sine_squared(h))

    def test_integer_signed_projection(self):
        self.assertEqual(m.signed_gaussian_quadrature_coefficients(1),(819,-106))
        self.assertEqual(m.signed_gaussian_quadrature_coefficients(2),(819*819-106*106,-2*819*106))

    def test_rational_mirror_denominators_all_positive(self):
        for h in range(1,40):
            sq=m.mirror_sine_squared(h)
            self.assertGreater(sq,0)
            self.assertLessEqual(sq,1)
            self.assertGreater(m.exact_mirror_gate_coefficient(h)['inverse_denominator_squared'],0)

    def test_rational_axis_source_versus_machin_selected(self):
        # Two different mirror constructions, both irrational, neither automatically stationary.
        for h in (1,2,3,5,7,11):
            x=m.certified_mirror_denominator(h,axis='rotated',terms=21,taylor_terms=20)
            self.assertGreater(x['lower'],0)
            self.assertGreaterEqual(float(x['upper']),abs(math.sin(15*math.pi*h*(0.5+math.pi/16)))-1e-10)


class MirrorNormalityGate(unittest.TestCase):
    def test_exact_radix_error_finite(self):
        for n in (4,8,17,32,61):
            for h in (1,3,5):
                a=finite_phasors(n,h)
                b=finite_phasors(n,16*h)
                self.assertLessEqual(abs(b-a),float(m.radix_discrepancy_bound(n,h))+1e-11)

    def test_one_real_quadrature_bound(self):
        beta=math.atan(106/819)/math.pi
        for n in (5,16,31,64):
            orbit=source_fractions(n)
            for h in (1,3,5):
                z=finite_phasors(n,h)
                b1=sum(math.sin(2*math.pi*h*(float(x)-beta/2)) for x in orbit)/n
                b16=sum(math.sin(2*math.pi*16*h*(float(x)-beta/2)) for x in orbit)/n
                denom=math.sqrt(float(m.mirror_sine_squared(h)))
                bound=(abs(b1)+abs(b16)+float(m.radix_discrepancy_bound(n,h)))/denom
                self.assertLessEqual(abs(z),bound+1e-11)

    def test_complex_reflection_gate_exact_numeric(self):
        gamma=complex(F(659525,681997),F(173628,681997))
        for n in (8,16,32):
            for h in (1,2,3):
                a=finite_phasors(n,h)
                b=finite_phasors(n,16*h)
                d1=a-gamma**h*a.conjugate()
                d16=b-gamma**(16*h)*b.conjugate()
                comm=abs(gamma**(15*h)-1)
                lhs=abs(a)*comm
                rhs=abs(d1)+abs(d16)+2*abs(b-a)
                self.assertLessEqual(lhs,rhs+1e-11)

    def test_phase_antisymmetry_is_exact(self):
        beta=math.atan(106/819)/math.pi
        for n in (11,20):
            for h in (1,3,5):
                a=finite_phasors(n,h)
                defect=a-cmath.exp(2j*math.pi*h*beta)*a.conjugate()
                quadrature=(cmath.exp(-1j*math.pi*h*beta)*a).imag
                self.assertAlmostEqual(abs(defect),2*abs(quadrature),places=12)

    def test_source_derivative_mirror_no_pi_evaluation(self):
        for h in (1,2,3,4):
            a,b=m.signed_gaussian_quadrature_coefficients(h)
            z=finite_phasors(25,h)
            actual=a*z.imag+b*z.real
            ideal=(681997**(h/2))*((cmath.exp(-1j*h*math.atan(106/819))*z).imag)
            self.assertAlmostEqual(actual/681997**(h/2),ideal/681997**(h/2),places=12)

    def test_cantor_countermodel_digits_closed(self):
        S={0,7,8,15}
        self.assertEqual({m.reciprocal_digit_action(d,first=True) for d in S},S)
        self.assertEqual({m.reciprocal_digit_action(d,first=False) for d in S},S)
        self.assertEqual({m.reciprocal_digit_action(m.reciprocal_digit_action(d,first=True),first=True) for d in S},S)
        self.assertEqual({m.reciprocal_digit_action(m.reciprocal_digit_action(d,first=False),first=False) for d in S},S)
        self.assertNotEqual(len(S),16)

    def test_rational_mirror_countermodel_explicit_digits(self):
        # A nonterminating admissible tail prevents the usual base-expansion endpoint ambiguity.
        ds=[0,7,8,15,0,7,8,15]
        t=F(7,15) # infinite repeated digit 7
        x=sum((F(d,16**j) for j,d in enumerate(ds,1)),F(0))+t/F(16**len(ds))
        y=(F(1,2)-x)%1
        mapped=[m.reciprocal_digit_action(d,first=(j==1)) for j,d in enumerate(ds,1)]
        tail=1-t
        yy=sum((F(d,16**j) for j,d in enumerate(mapped,1)),F(0))+tail/F(16**len(ds))
        self.assertEqual(y,yy)

    def test_coherent_nonnormal_real_seed_fails_irrational_reflection(self):
        beta=math.atan(106/819)/math.pi
        # The coherent counterseed is s=1/5-pi/16 (IRRATIONAL), not a finite rational-register seed.
        target=math.sin(2*math.pi*(1/5-beta/2))
        self.assertGreater(abs(target),0.8)

    def test_source_axis_certificate_a_conditional_not_proof(self):
        for n in (16,64,128):
            mdepth=3
            cert=m.predicted_real_quadrature_bound(n,1,mdepth)
            self.assertGreater(cert['denominator_lower'],0)
            self.assertGreater(cert['additive_error'],0)

    def test_failure_domains(self):
        with self.assertRaises(m.ReciprocityError):m.projective_rational_mirror(0,0)
        with self.assertRaises(m.ReciprocityError):m.reciprocal_digit_action(16,first=True)
        with self.assertRaises(m.ReciprocityError):m.certified_mirror_denominator(0)
        with self.assertRaises(m.ReciprocityError):m.certified_mirror_denominator(1,axis='wrong')
        with self.assertRaises(m.ReciprocityError):m.radix_discrepancy_bound(0,1)


class ExistingCategoricalCore(unittest.TestCase):
    def test_parent_pointed_original_source_contract(self):
        """Exact integration with PR #450's original source-gluing code if mounted.

        The test MUST run on a real repo checkout. Standalone partial archive
        records SKIPPED, not a pretend parent pass.
        """
        parent=HERE.parent/'categorical_source_gluing'/'source_gluing.py'
        if not parent.is_file():
            self.skipTest('full parent categorical_source_gluing module not mounted')
        spec2=importlib.util.spec_from_file_location('succ_arctan_parent_'+str(id(object())),parent)
        p=importlib.util.module_from_spec(spec2);sys.modules[spec2.name]=p;spec2.loader.exec_module(p)
        for n in range(1,35):
            self.assertEqual(m.forcing(n),p.source(n))
            self.assertEqual(m.forcing(n),p.source_combined(n))
            self.assertEqual(m.rational_orbit(n)[-1],p.orbit(n)%1)
            self.assertEqual(m.rational_orbit(n)[-1],p.orbit_convolution(n)%1)
        self.assertEqual(m.rational_mirror_label()['q'],p.source(2))

if __name__=='__main__':unittest.main()

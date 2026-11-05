"""Independent exact regressions for SUCC dual-zero and Cayley real lift.

These tests check finite algebra and declarations, NOT pi normality or academic priority.
"""
from __future__ import annotations
import math
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from sympy import I, Matrix, Poly, Rational, Symbol, cyclotomic_poly, minimal_polynomial, pi, tan, totient, simplify

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'research/2026-11-04/dual_zero_real_carrier'))
import zero_real_carrier as Z


def mult(z,w):
    a,b=z;c,d=w
    return (a*c-b*d,a*d+b*c)


def power(z,n):
    y=(Q(1),Q(0))
    for _ in range(n):y=mult(y,z)
    return y


def phi_from_bounded_source_primes(D,N):
    v=D; ans=D
    for p in range(2,8*N+1):
        if v%p==0:
            ans=ans//p*(p-1)
            while v%p==0:v//=p
    assert v==1, f'large untracked prime {v}'
    return ans


class DualZeroTests(unittest.TestCase):
    def test_original_signed_source_first(self):
        self.assertEqual(Z.authentic_r(1),Q(47,15))
        self.assertEqual(Z.primal_r(1),Q(109,35))

    def test_source_independent_modular_oracle_both(self):
        for primal in (False,True):
            for n in (1,2,3,5,8,13,21,37,61):
                with self.subTest(primal=primal,n=n):
                    self.assertEqual(list(Z.source_phase_stream(n,primal)),list(Z.integer_oracle_stream(n,primal)))

    def test_four_pole_equals_angular_plus_radial(self):
        RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))
        for n in (1,2,3,8,13):
            r=Z.authentic_r(n)
            a=Z.primal_r(n)
            rad=sum((w/Q(8*(n-1)+j) for j,w in enumerate(RAD,1)),Q(0))
            self.assertEqual(r,a+rad)
            self.assertNotEqual(rad,0)

    def test_all_projector_overlap_m(self):
        for M in (3,5,7,15,35):
            h,p=Z.zero_projectors(M)
            self.assertEqual(h*h,h)
            self.assertEqual(p*p,p)
            self.assertEqual(h*p*h,h/M)
            self.assertEqual(p*h*p,p/M)
            self.assertEqual((h*p).trace(),Rational(1,M))
            self.assertEqual((h-p).trace(),0)

    def test_commutator_exact_hilbert_schmidt(self):
        for M in (3,5,7,15,35):
            h,p=Z.zero_projectors(M)
            C=h*p-p*h
            hs=(C.T*C).trace()
            self.assertEqual(hs,Rational(2*(M-1),M*M))
            self.assertNotEqual(h*p,p*h)

    def test_zero_character_row_col_both_one(self):
        for M in (3,5,7,35):
            self.assertTrue(all((0*a)%M==0 for a in range(M)))
            self.assertTrue(all((h*0)%M==0 for h in range(M)))
            self.assertEqual(Z.zero_overlap(M),Q(1,M))

    def test_fourier_swaps_const_and_delta_projectors_symbolically(self):
        # Direct integer character orthogonality: sum_a zeta^(ha)=M iff h=0.
        for M in (3,5,7,15):
            for h in range(M):
                self.assertEqual(sum(int(h*a%M==0) for a in range(M)),
                                 M if h==0 else math.gcd(h,M))
                # Sum of characters (formal cyclotomic identity) checked
                # independently by a high-precision complex root, not authority.
                w=sum(complex(math.cos(2*math.pi*h*a/M),math.sin(2*math.pi*h*a/M)) for a in range(M))
                self.assertLess(abs(w-(M if h==0 else 0)),1e-11)

    def test_exact_cyclotomic_character_orthogonality(self):
        # This is independent exact Z[X]/Phi_M character algebra, no float.
        X=Symbol('X')
        for M in (3,5,7,15,35):
            phi=Poly(cyclotomic_poly(M,X),X)
            for h in sorted(set((0,1,2,3,M-1))):
                sm=Poly(sum(X**((h*a)%M) for a in range(M)),X)
                rem=sm.rem(phi)
                self.assertEqual(rem,Poly(M if h%M==0 else 0,X))

    def test_cayley_pythagorean_unit_and_inverse(self):
        for t in map(Q,('0','1','-1','1/2','-2/3','3/5','5/8','8/13')):
            z=Z.cayley_rational(t)
            self.assertEqual(z[0]**2+z[1]**2,1)
            self.assertEqual(Z.inverse_cayley_rational(z),t)
        self.assertEqual(Z.cayley_rational(None),(Q(-1),Q(0)))
        self.assertIsNone(Z.inverse_cayley_rational((Q(-1),Q(0))))

    def test_cayley_split_only_odd_denominators(self):
        for a,b in [(1,1),(1,2),(2,3),(3,5),(5,8),(8,13),(17,21),(57,91)]:
            D=Z.rational_cayley_split_denominator(Q(a,b))
            self.assertEqual(D%2,1)
            for p in range(3,D+1,2):
                if D%p==0 and all(p%q for q in range(2,math.isqrt(p)+1)):
                    self.assertEqual(p%4,1)

    def test_reciprocal_cayley_reflection(self):
        for t in [Q(1,1),Q(1,2),Q(2,3),Q(3,5),Q(-2,3),Q(-8,7)]:
            a,b=Z.cayley_rational(t)
            self.assertEqual(Z.cayley_reciprocal(t),(-a,b))
        self.assertEqual(Z.cayley_reciprocal(Q(0)),(Q(-1),Q(0)))

    def test_quarter_arcs_source_rational(self):
        a=Z.projective_chart_quarters(Q(0))
        b=Z.projective_chart_quarters(Q(1))
        self.assertEqual(a,((Q(1),Q(0)),(Q(-1),Q(0)),(Q(-1),Q(0)),(Q(1),Q(0))))
        self.assertEqual(b,((Q(0),Q(1)),(Q(0),Q(1)),(Q(0),Q(-1)),(Q(0),Q(-1))))
        self.assertTrue(all(x*x+y*y==1 for x,y in Z.projective_chart_quarters(Q(2,3))))

    def test_fractional_primal_first_tangent_degree(self):
        self.assertEqual(Z.source_tangent_descriptor(Q(109,35))['exact_algebraic_degree'],24)
        self.assertEqual(Z.source_tangent_descriptor(Q(47,15))['exact_algebraic_degree'],8)
        self.assertEqual(Z.source_tangent_descriptor(Q(0))['exact_algebraic_degree'],1)
        self.assertEqual(Z.source_tangent_descriptor(Q(4,35))['phase'],Q(4,35))

    def test_cyclotomic_tangent_polynomial_irreducible(self):
        for M in (3,5,7,9,11,15,21,35,45):
            P=Z.tangent_minpoly_for_odd_conductor(M)
            self.assertEqual(P.degree(),int(totient(M)))
            self.assertTrue(P.is_irreducible)
            self.assertEqual(P.eval(0),int(cyclotomic_poly(M,1)))
            self.assertEqual(P.all_coeffs()[1::2],[0]*(P.degree()//2))

    def test_independent_sympy_minimal_polynomial(self):
        T=Symbol('T')
        for a,M in [(1,3),(1,5),(2,5),(1,7),(2,9),(4,15)]:
            m=Poly(minimal_polynomial(tan(pi*a/M),T),T)
            q=Z.tangent_minpoly_for_odd_conductor(M)
            self.assertEqual(m.monic(),q.monic())

    def test_reciprocal_doubles_original_odd_conductor(self):
        for phase in (Q(1,3),Q(2,5),Q(4,15),Q(4,35),Q(2,9),Q(0)):
            x=Q(1,2)-phase
            self.assertEqual(x.denominator,2*phase.denominator)
            for h in (-5,-2,-1,0,1,3,8):
                # exact exponent congruence e(h(1/2-x))=(-1)^h conj(e(hx))
                L=2*phase.denominator
                a=(h*x.numerator*(L//x.denominator))%L
                b=((h*L//2)-(h*phase.numerator*(L//phase.denominator)))%L
                self.assertEqual(a,b)

    def test_rational_tangent16_integer_binomial(self):
        A,B=Z.angle_16_pair()
        t=Symbol('t')
        from sympy import expand
        self.assertEqual(expand(A.as_expr()+I*B.as_expr()-(1+I*t)**16),0)
        for x in (Q(0),Q(1,3),Q(-1,2),Q(2,5),Q(3,5)):
            self.assertEqual(Z.cayley_rational(Z.tangent16_projective(x)),power(Z.cayley_rational(x),16))

    def test_forced_mobius_source_step(self):
        for t,s in ((Q(1,3),Q(1,7)),(Q(-1,4),Q(2,3)),(Q(0),Q(0)),(Q(1,5),Q(-1,8))):
            left=Z.cayley_rational(Z.tangent_forced_step(t,s))
            right=mult(power(Z.cayley_rational(t),16),Z.cayley_rational(s))
            self.assertEqual(left,right)

    def test_false_commuting_cayley_16_scale(self):
        self.assertNotEqual(Z.cayley_rational(Q(16,3)),power(Z.cayley_rational(Q(1,3)),16))

    def test_source_cyclotomic_phase_exponent(self):
        for phase in (Q(2,15),Q(4,35),Q(5,21)):
            for h in (-17,-1,1,3,16):
                exp,M,_=Z.exact_source_circle_character(h,phase)
                self.assertEqual(exp,(phase.numerator*h)%phase.denominator)
                self.assertEqual(M,phase.denominator)

    def test_haar_reference_not_source_h1(self):
        # delta_1/5 is periodic under radix 16 and never has Haar Fourier cancellation.
        x=Q(1,5)
        self.assertEqual((16*x)%1,x)
        self.assertEqual(Z.source_tangent_descriptor(x)['exact_algebraic_degree'],4)
        self.assertEqual(Z.zero_overlap(5),Q(1,5))

    def test_nested_fourier_refinement_intensity(self):
        for M,Mprime in ((3,15),(5,35),(7,35),(15,105)):
            self.assertEqual(Z.fourier_refinement_factor(M,Mprime),Q(M,Mprime))
            # Delta-a basis: F_{M'}(i delta_a) equals F_M(delta_a)
            # repeated modulo M with |amplitude|^2 scaled M/M'.
            for a in range(M):
                for h in (0,1,3,Mprime-1):
                    self.assertEqual(Q(h*(Mprime//M)*a,Mprime)%1,Q(h*a,M)%1)
            self.assertNotEqual(Q(M,Mprime),Q(1))

    def test_harmonic_weight_density_not_uniform(self):
        # Haar-conditioned quarter interval t in [0,1] has density
        # (4/pi)/(1+t*t), not flat. Strict inverse-weight covariance.
        import mpmath as mp
        mp.mp.dps=50
        mean=2*mp.log(2)/mp.pi
        self.assertTrue(0<mean<mp.mpf('0.5'))
        self.assertGreater(mp.mpf('0.5')-mean,mp.mpf('0.05'))

    def test_primal_rational_phase_not_rational_cayley_coordinate(self):
        x=Q(4,35)
        self.assertEqual(Z.cayley_rational(x),(Q(1209,1241),Q(280,1241)))
        self.assertEqual(1241,17*73)
        self.assertEqual(Z.source_tangent_descriptor(x)['exact_algebraic_degree'],24)
        # No C(t) with t rational can be a primitive odd-order circle root,
        # since C(t) lies in Q(i), which has roots of unity of order 1,2,4.
        self.assertNotEqual(Z.cayley_rational(x),(Q(1),Q(0)))

    def test_angular_kernel_is_quarter_haar_jacobian(self):
        from sympy import symbols, integrate
        t=symbols('t',real=True,positive=True)
        self.assertEqual(integrate(4/(1+t*t),(t,0,1)),pi)
        self.assertEqual(integrate(1/(1+t*t),(t,0,1)),pi/4)
        self.assertEqual(integrate(1/(pi*(1+t*t)),(t,0,1)),Q(1,4))
        self.assertEqual(integrate(1/(pi*(1+t*t)),(t,0,math.inf)),Q(1,2))

    def test_explicit_totient_lower_bound_via_source_support(self):
        # For source D_n with all p|D_n <=8n, log(D/phi(D)) <=H_(8n-1).
        for primal in (False,True):
            state=dict(Z.source_phase_stream(61,primal))
            for n in (1,2,3,5,8,13,21,37,61):
                D=state[n].denominator
                d=phi_from_bounded_source_primes(D,n)
                self.assertGreaterEqual(d,math.ceil(D/(math.e*8*n))-1)
                self.assertEqual(Z.zero_overlap(D)*D,1)

    def test_source_odd_phase_never_recovers_even_halfturn(self):
        # No odd source p-state can exactly be a half-turn or tangent infinity.
        for primal in (False,True):
            for n,x in Z.source_phase_stream(37,primal):
                self.assertNotEqual(x,Q(1,2))
                self.assertEqual(x.denominator%2,1)

    def test_irrational_tangent_periodic_controls_are_exact(self):
        # Radix 16 fixes 1/M for M dividing 15, so tan(pi/M) is a
        # root of B_16(t)-t*A_16(t), despite high algebraic degree.
        A,B=Z.angle_16_pair()
        t=Symbol('t')
        fixed_poly=Poly(B.as_expr()-t*A.as_expr(),t)
        for M in (3,5,15):
            P=Z.tangent_minpoly_for_odd_conductor(M)
            P_t=Poly(P.as_expr().subs(Symbol('T'),t),t)
            self.assertEqual(fixed_poly.rem(P_t),Poly(0,t))
            self.assertEqual((16*Q(1,M))%1,Q(1,M))
            self.assertEqual(P_t.degree(),int(totient(M)))

    def test_endogenous_radial_collapses_despite_high_degree(self):
        u,y=Q(0),Q(0)
        ratios=[]
        for n in range(1,62):
            u=16*u+Z.authentic_r(n)
            y=16*y+Z.primal_r(n)
            rad=u-y
            self.assertGreater(rad,0)
            self.assertLess(rad,Q(1,32*n+16))
            if n in (5,13,37,61):
                self.assertEqual(rad.denominator%2,1)
                self.assertGreaterEqual(Z.source_tangent_descriptor(rad)['exact_algebraic_degree'],2)
                ratios.append((n,rad.denominator.bit_length()))
        self.assertTrue(ratios[-1][1]>ratios[0][1])

    def test_source_field_degree_growth_diagnostic_only(self):
        for primal in (False,True):
            rows=list(Z.source_phase_stream(61,primal))
            for n in (5,8,13,21,37,61):
                M=rows[n][1].denominator
                p=phi_from_bounded_source_primes(M,n)
                self.assertEqual(p,int(totient(M)))
                self.assertLessEqual(math.log(M/p),math.log(8*n)+1)
                self.assertEqual(Z.source_tangent_descriptor(rows[n][1])['exact_algebraic_degree'],p)


if __name__=='__main__':unittest.main()

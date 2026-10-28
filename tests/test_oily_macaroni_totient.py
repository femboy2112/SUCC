"""Exact source-grade, Möbius, cyclotomic and third-order log-shadow checks.

Native SUCC branch is PR #309's source-typed packet compiler. This test file
never assumes π normality, any Fourier saving, or that auxiliary packet
characters are the actual selected BBP phases.
"""
import unittest
from fractions import Fraction as Q
from math import gcd, factorial

from observational_succ import oily_macaroni_totient as t


class MobiusTotientExact(unittest.TestCase):
    def test_primitive_probabilities_and_nonmultiplicativity(self):
        expected={1:Q(1),2:Q(4,9),3:Q(29,49),4:Q(4,9),6:Q(416,1323),16:Q(4,9)}
        for q,v in expected.items():
            self.assertEqual(t.primitive_mass(q),v)
            self.assertGreater(v,0)
        self.assertEqual(t.primitive_mass(6)-t.primitive_mass(2)*t.primitive_mass(3),Q(68,1323))
        self.assertEqual(t.mobius(1),1)
        self.assertEqual(t.mobius(4),0)
        self.assertEqual(t.mobius(30),-1)
        self.assertEqual(t.mobius(6),1)
        with self.assertRaises(ValueError):t.primitive_mass(0)
        with self.assertRaises(ValueError):t.primitive_mass(True)

    def test_grade_tail_equals_original_compiler_error(self):
        for depth in range(1,18):
            partial=sum((t.endpoint_weight(j) for j in range(depth)),Q())
            self.assertEqual(1-partial,t.compiler_error(depth))
            self.assertEqual(t.compiler_error(depth),Q(depth+2,2**(depth+1)))

    def test_finite_modular_residue_mass(self):
        for q in (2,3,6,16):
            v=t.primitive_residue_distribution(q,20)
            self.assertEqual(len(v),q)
            partial=sum(v)
            self.assertLessEqual(abs(partial-t.primitive_mass(q)),t.compiler_error(20))
            self.assertEqual(v[0],sum((t.endpoint_weight(j) for j in range(0,20,q)
                                      if gcd(j,q)==1),Q()))
        with self.assertRaises(ValueError):t.primitive_residue_distribution(2,201)

    def test_source_grade_regrouping_countermodel(self):
        # Same original endpoint grade distribution under regrading J' = J//2;
        # primitive parity probability changes. The grading is load-bearing.
        odd_group=sum((t.endpoint_weight(j) for j in range(120)
                       if j%4 in (2,3)),Q())
        # Tail at 120 is nonzero but negligible, so compare with rational
        # exact residue classes via the 4-adic geometric series.
        tt=Q(1,16)
        exact=sum((Q(1,2**(r+2))*((r+1)/(1-tt)+4*tt/(1-tt)**2)
                   for r in (2,3)),Q())
        self.assertEqual(exact,Q(9,25))
        self.assertNotEqual(exact,t.primitive_mass(2))
        self.assertLess(exact-odd_group,t.compiler_error(120))

    def test_exact_twist_and_shadow_polynomial_at_special_points(self):
        for z in (1,-1,1j,-1j):
            self.assertAlmostEqual(t.odd_fourier_limit(z),t.primitive_root_formula(16,z),places=13)
            self.assertAlmostEqual(t.odd_shadow_coefficient(z),t.shadow_limit(16,z),places=12)
        self.assertAlmostEqual(t.odd_shadow_coefficient(1).real,-4/27,places=14)
        self.assertAlmostEqual(abs(t.odd_fourier_limit(1)),4/9,places=14)
        self.assertAlmostEqual(abs(t.odd_fourier_limit(1j)),4/25,places=14)

    def test_cyclotomic_modes_nonzero_uniform(self):
        import cmath
        for k in range(1,7):
            q=1<<k
            self.assertEqual(t.primitive_mass(q),Q(4,9))
            for h in range(min(q,25)):
                z=cmath.exp(2j*cmath.pi*h/q)
                C=t.odd_fourier_limit(z)
                self.assertGreaterEqual(abs(C)+1e-13,4/25)
                self.assertLessEqual(abs(C),4/9+1e-13)
                self.assertAlmostEqual(C,t.primitive_root_formula(q,z),places=12)
                M=sum((complex(cmath.exp(2j*cmath.pi*h*j/q))*t.endpoint_weight(j)
                       for j in range(35) if j%2),0j)
                self.assertLessEqual(abs(M-C),float(t.compiler_error(35))+1e-12)


class AuthenticPacketKernelExact(unittest.TestCase):
    def test_source_kernel_and_polynomial_identity(self):
        for x in (Q(0),Q(1,7),Q(1,2),Q(5,8),Q(9,10),Q(1)):
            u,v=t.packet_u(x),t.packet_v(x)
            self.assertEqual(t.source_kernel(x),(1-x)/(4*(1-u)*(1-v)))
            self.assertEqual(t.conditional_grade_pgf(x,1),1)
            self.assertEqual(t.conditional_odd_character(x,1), x/((1+u)*(1+v)))
            self.assertEqual(t.kernel_odd_unnormalized(x,1),
                             t.source_kernel(x)*t.conditional_odd_character(x,1))
            for depth in (1,2,3,6):
                val=sum((sum(c*x**j for j,c in enumerate(t.packet_polynomial(g)))
                         for g in range(depth)),Q())
                self.assertGreaterEqual(val,0)
                self.assertLessEqual(val,t.source_kernel(x))
                self.assertLessEqual(t.source_kernel(x)-val,
                                     t.compiler_error(depth)*t.source_kernel(x))

    def test_endpoint_jet_controls(self):
        for j in range(0,15):
            p=t.packet_polynomial(j)
            self.assertEqual(sum(p),0)
            self.assertEqual(sum(k*c for k,c in enumerate(p)),-t.endpoint_weight(j))
            self.assertEqual(t.end_grade_first_variation(j),(2-j)*t.endpoint_weight(j))
        self.assertEqual(sum((t.end_grade_first_variation(j) for j in range(45)),Q()),
                         # finite sum is NOT zero; its tail is nonzero
                         sum(((2-j)*t.endpoint_weight(j) for j in range(45)),Q()))

    def test_mobius_divided_difference_and_odd_integrand(self):
        import cmath
        for x in (Q(0),Q(1,4),Q(1,2),Q(9,10),Q(1)):
            for q in (2,3,6,8):
                z=cmath.exp(2j*cmath.pi/q)
                fx=t.conditional_primitive_character(x,q,z)
                trunc=sum((t.endpoint_weight(j)*z**j for j in range(35)
                           if gcd(j,q)==1),0j) if x==1 else None
                if trunc is not None:
                    self.assertLessEqual(abs(fx-trunc),float(t.compiler_error(35))+1e-12)
                if q in (2,8):
                    self.assertAlmostEqual(fx,t.conditional_odd_character(x,z),places=12)
                    self.assertAlmostEqual(t.source_kernel(x)*fx,
                                           t.kernel_odd_unnormalized(x,z),places=12)

    def test_exact_beta_log_moments_independent_quadrature(self):
        import mpmath as mp
        with mp.workdps(60):
            to_mp=lambda q:mp.mpf(q.numerator)/q.denominator
            for n in (1,5):
                for j in range(4):
                    p=t.packet_polynomial(j)
                    mom=t.packet_log_moments(n,j)
                    def density(x):
                        xx=mp.mpf(x)
                        return xx**(8*n)*sum(to_mp(c)*xx**i for i,c in enumerate(p))
                    for k in range(3):
                        actual=mp.quad(lambda x:density(x)*mp.log1p(-x)**k,[0,.5,1])
                        self.assertLess(abs(actual-to_mp(mom[k])),mp.mpf('1e-50'))

    def test_exact_finite_connected_log_shadow(self):
        import mpmath as mp
        for n,depth in ((2,8),(8,12)):
            d=t.finite_primitive_log_covariance(n,depth)
            self.assertGreater(d['normalizer'],0)
            self.assertLess(d['primitive_mass'],1)
            with mp.workdps(50):
                to_mp=lambda q:mp.mpf(q.numerator)/q.denominator
                g=mp.sqrt(5)
                qstar=(3-g)/2
                coeff=to_mp(d['coefficient_constant'])+to_mp(d['coefficient_log'])*(mp.log(8*n)-qstar)
                # INDEPENDENT direct polynomial quadrature, not beta differentiation.
                polys=[t.packet_polynomial(j) for j in range(depth)]
                def m_poly(poly,x):
                    return sum(to_mp(v)*x**i for i,v in enumerate(poly))
                norm=mp.quad(lambda x:x**(8*n)*sum(m_poly(poly,x) for poly in polys),[0,mp.mpf('0.5'),1])
                g0=mp.quad(lambda x:x**(8*n)*sum(m_poly(poly,x) for j,poly in enumerate(polys) if j%2),[0,mp.mpf('0.5'),1])/norm
                f=lambda x:(mp.log(8*n*(1-x))-qstar)**2
                g2=mp.quad(lambda x:x**(8*n)*sum(m_poly(poly,x) for j,poly in enumerate(polys) if j%2)*f(x),[0,mp.mpf('0.5'),1])/norm
                m2=mp.quad(lambda x:x**(8*n)*sum(m_poly(poly,x) for poly in polys)*f(x),[0,mp.mpf('0.5'),1])/norm
                self.assertLess(abs(coeff-(g2-g0*m2)),mp.mpf('1e-40'))

    def test_full_complex_primitive_mellin_integral_and_limit(self):
        import mpmath as mp
        with mp.workdps(48):
            s=mp.mpc('0','0.4')
            q=16;h=1
            z=mp.exp(2j*mp.pi*h/q)
            reference=4*z/(4-z*z)**2 * mp.gamma(2+s)
            # Full complex character of the primitive odd packet and the
            # Gamma-log coordinate has NONZERO boundary value.
            v15=t.primitive_complex_mellin(15,q,h,s,precision=55)
            v80=t.primitive_complex_mellin(80,q,h,s,precision=55)
            self.assertLess(abs(v80-reference),abs(v15-reference))
            self.assertGreater(abs(reference),mp.mpf('0.04'))
            # Independent finite polynomial expansion, no rational-function
            # denominator: grade-by-grade integrate p_j(x) Y^s.
            n=3; depth=17; a=8*n
            val=t.primitive_complex_mellin(n,q,h,s,precision=55)
            numerator=mp.mpc(0)
            normalizer=mp.quad(lambda x:x**a*t.source_kernel(x),[0,.5,1])
            for j in range(depth):
                if not j%2:continue
                p=t.packet_polynomial(j)
                poly=lambda x:sum((mp.mpf(c.numerator)/c.denominator*x**k for k,c in enumerate(p)),mp.mpf(0))
                numerator+=z**j * mp.quad(lambda x:x**a*poly(x)*(a*(1-x))**s,[0,.5,1])
            self.assertLess(abs(numerator/normalizer-val),mp.mpf(t.compiler_error(depth).numerator)/t.compiler_error(depth).denominator)
            with self.assertRaises(ValueError):t.primitive_complex_mellin(1,2,0,-2)

    def test_complex_mellin_shadow_limit_and_gold_cumulant(self):
        import mpmath as mp
        with mp.workdps(48):
            C=lambda z:4*z/(4-z*z)**2
            H=lambda z:4*z*(4-5*z*z)/(4-z*z)**3
            z=mp.exp(mp.pi*1j/8)
            s=mp.mpc('0.25','0.45')
            self.assertLess(abs(t.primitive_root_formula(16,complex(z))-complex(C(z))),mp.mpf('1e-13'))
            self.assertLess(abs(t.shadow_limit(16,complex(z))-complex(H(z))),mp.mpf('1e-13'))
            coeff=s*mp.gamma(2+s)*H(z)
            self.assertTrue(mp.isfinite(abs(coeff)))
            self.assertNotEqual(coeff,0)
            lam=(mp.sqrt(5)-1)/2
            omega=lam-mp.euler
            # The golden center is not a true fully centered third cumulant.
            self.assertLess(abs(2*(1-mp.euler-lam**2)*H(1) - 2*omega*H(1)),mp.mpf('1e-42'))
            self.assertLess(abs(2*(1-mp.euler-(1-mp.euler))*H(1)),mp.mpf('1e-42'))

    def test_direct_full_source_covariance_asymptotics(self):
        import mpmath as mp
        with mp.workdps(38):
            qstar=(3-mp.sqrt(5))/2
            omega=(mp.sqrt(5)-1)/2-mp.euler
            target=(-mp.mpf(8)/27)*omega
            errors=[]
            for n in (16,64,256):
                a=mp.mpf(8*n)
                def rho(y):
                    if not 0<y<a:return mp.mpf(0)
                    x=1-y/a
                    return x**a*t.source_kernel(x)/a
                knots=[mp.mpf(0),1,5,15,min(a,mp.mpf(70))]
                knots=sorted(set(knots))
                norm=mp.quad(rho,knots)
                def E(fn):return mp.quad(lambda y:rho(y)*fn(y),knots)/norm
                odd=lambda y:t.conditional_odd_character(1-y/a,mp.mpf(1))
                V=lambda y:(mp.log(y)-qstar)**2
                cov=E(lambda y:odd(y)*V(y))-E(odd)*E(V)
                errors.append(abs(a*cov-target))
            self.assertLess(errors[2],errors[1])
            self.assertLess(errors[1],errors[0])
            self.assertLess(errors[-1],mp.mpf('0.001'))

    def test_source_phase_transport_error_budget(self):
        for N,depth in ((32,11),(256,21),(4096,40)):
            cert=t.weighted_selected_transport_budget(N,depth)
            self.assertLess(cert['full_packet_mean_error_upper'],Q(1))
            self.assertLess(cert['finite_packet_mean_error_upper'],Q(1))
            self.assertEqual(cert['limit_dyadic_character_modulus_lower'],Q(4,25))
            self.assertFalse(cert['proves_phase_cancellation'])
            self.assertGreaterEqual(cert['finite_packet_mean_error_upper'],
                                    cert['full_packet_mean_error_upper'])

    def test_negative_not_source_selected(self):
        flags=t.parity_shadow_predictions()
        self.assertEqual(flags['first_log_shadow'],Q(-4,27))
        self.assertEqual(flags['third_shadow_multiplier'],Q(-8,27))
        self.assertFalse(flags['source_only_proves_normality'])


if __name__=='__main__':unittest.main()

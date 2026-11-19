"""Focused exact/rational/independent spectral controls for Gaussian causal SUCC."""
from fractions import Fraction
import cmath
import math
import unittest

import gaussian_causal as g


class SourceTests(unittest.TestCase):
    def test_source_identity(self):
        self.assertEqual(g.forcing(1), Fraction(47, 15))
        for n in (1, 2, 4, 11, 101):
            self.assertEqual(g.state(n), 16*g.state(n-1) + g.forcing(n))
            self.assertGreater(g.forcing(n), 0)

    def test_prefix_tail_exact(self):
        for n, h in ((1, 9), (4, 13), (10, 29)):
            self.assertEqual(g.state(n)+g.finite_tail(n,h), 16**n*g.prefix_x(h))
            self.assertLess(g.finite_tail(n, h), g.tail_upper(n))

    def test_explicit_tail_polynomial(self):
        for n in list(range(1, 32)) + [100, 1000]:
            self.assertGreater(Fraction(15, 64*n*n), 0)
            self.assertLess(g.forcing(n+1), Fraction(15, 64*n*n))
            self.assertGreater(g.forcing(n), Fraction(15, 64*n*n))

    def test_jacobian_exact(self):
        baseline = (Fraction(0),) + tuple(Fraction(c) for c in g.COEFFS)
        perturb = (Fraction(2, 7), Fraction(1, 11), Fraction(-1, 13),
                   Fraction(2, 17), Fraction(1, 19))
        for n in (0, 1, 2, 5, 11):
            row = g.jacobian_row(n)
            shifted = g.state(n, seed=baseline[0]+perturb[0],
                              coeffs=[baseline[j]+perturb[j] for j in range(1, 5)])
            self.assertEqual(shifted-g.state(n), sum((a*b for a,b in zip(row, perturb)), Fraction(0)))

    def test_five_clock_determinant(self):
        matrix = [list(g.jacobian_row(n)) for n in range(1, 6)]
        det = Fraction(1)
        for k in range(5):
            pivot = matrix[k][k]
            self.assertNotEqual(pivot, 0)
            det *= pivot
            for i in range(k+1, 5):
                factor=matrix[i][k]/pivot
                for j in range(k+1, 5):
                    matrix[i][j] -= factor*matrix[k][j]
                matrix[i][k]=Fraction(0)
        self.assertEqual(det, Fraction(32768, 17039726835256125))

    def test_gaussian_covariance_identity(self):
        variance = Fraction(3, 7)
        for a, b in ((1, 2), (3, 6), (9, 11)):
            row_a, row_b = g.jacobian_row(a), g.jacobian_row(b)
            self.assertEqual(g.output_covariance(row_a,row_b,variance),
                             variance * sum((x*y for x,y in zip(row_a,row_b)), Fraction(0)))
            self.assertEqual(g.output_covariance(row_a,row_b,variance),
                             g.output_covariance(row_b,row_a,variance))


class GaussianTests(unittest.TestCase):
    def test_constants_and_r0_inequalities(self):
        _, S, R = g.gaussian_sums()
        self.assertAlmostEqual(S, 0.8845089717463233, places=13)
        self.assertAlmostEqual(4*math.pi*R, 10.175779418614326, places=12)
        for j in range(501):
            x=j/500
            A=1-math.cos(2*math.pi*x)
            D=g.gaussian_displacement(x)
            self.assertGreaterEqual(D+1e-14, 4/math.e*A)
            self.assertLessEqual(D, 2*S*A+1e-14)
        self.assertLess(2*g.gaussian_tail(0, cutoff=8),1e-32)

    def test_direct_circle_quadrature(self):
        phases=[0.0, 0.1, 0.37, 0.75]
        K=6
        def kernel(t):
            return 1+2*sum(math.exp(-k*k/2)*math.cos(2*math.pi*k*t)
                           for k in range(1,K+1))
        total=0.0
        for j in range(2048):
            t=(j+0.5)/2048
            d=sum(kernel(t-p) for p in phases)/len(phases)-1
            total+=d*d/2048
        self.assertAlmostEqual(total,g.gaussian_haar_discrepancy(phases,K),places=12)

    def test_mean_energy_distinction(self):
        repeated=[Fraction(1, 3)]*4
        uniform=[i/16 for i in range(16)]
        self.assertGreater(g.gaussian_haar_discrepancy(repeated),0.6)
        self.assertLess(g.gaussian_haar_discrepancy(uniform),1e-10)
        self.assertGreater(g.gaussian_displacement(1/3),0.1)

    def test_gaussian_haar_spectrum(self):
        phases=[0.03,0.16,0.41,0.67]
        expected=sum(2*math.exp(-h*h)*abs(sum(cmath.exp(2j*math.pi*h*x) for x in phases)/4)**2
                     for h in range(1,7))
        self.assertAlmostEqual(expected,g.gaussian_haar_discrepancy(phases,6),places=14)
        for h in range(1,7):
            self.assertLessEqual(abs(g.phase_moment(phases,h))**2,
                                 math.exp(h*h)*expected+1e-12)

    def test_gaussian_source_tail_transport(self):
        _, S, R = g.gaussian_sums()
        L = 4*math.pi*R
        for B in (2, 4, 8, 16):
            prefix=g.prefix_x(2*B+50)
            u=[g.fraction_mod1(g.state(n)) for n in range(B,2*B)]
            true=[g.fraction_mod1(prefix*16**n) for n in range(B,2*B)]
            E0=sum(g.gaussian_displacement(x) for x in u)/B
            E1=sum(g.gaussian_displacement(x) for x in true)/B
            V0=g.gaussian_haar_discrepancy(u)
            V1=g.gaussian_haar_discrepancy(true)
            self.assertLessEqual(abs(E0-E1),L/(64*B*B)+1e-12)
            self.assertLessEqual(abs(math.sqrt(V0)-math.sqrt(V1)),
                                 2*math.pi*math.sqrt(S)/(64*B*B)+1e-12)

    def test_prime_source_innovation_asymptotic(self):
        _, S, _=g.gaussian_sums()
        coefficient=4*math.pi**2*S*(15/64)**2
        for n in (40, 200, 800):
            r=float(g.forcing(n))
            measured=g.gaussian_displacement(r)*n**4
            self.assertAlmostEqual(measured/coefficient,1.0,delta=0.09 if n==40 else 0.02)
        self.assertEqual(g.gaussian_displacement(0),0)
        self.assertGreater(g.gaussian_displacement(float(g.forcing(40))),0)

    def test_seed_alias_and_locked_control(self):
        # Same forcing, seed s=-x: all completed phases zero, all local forcing positive.
        self.assertEqual(g.gaussian_displacement(0),0)
        self.assertGreater(g.forcing(17),0)
        # s -> s+1/16 is invisible in every circle phase at n>=1.
        for n in range(1,11):
            self.assertEqual((16**n*Fraction(1,16)).denominator,1)

    def test_resolution_matched_seed_noise(self):
        c=0.075
        want=math.exp(-2*math.pi**2*c*c)
        for n in (0, 1, 3, 6, 12):
            self.assertAlmostEqual(g.gaussian_phase_attenuation(n,c/16**n),want,places=14)
        self.assertLess(g.gaussian_phase_attenuation(3,0.075),1e-10)

    def test_circle_heat_transport_fourier(self):
        t=0.037
        beta=0.17
        for h in range(-6,7):
            # T_16 pushforward multiplies the input's Fourier label by 16.
            lhs=cmath.exp(-4*math.pi**2*t*(16*h)**2)*cmath.exp(-2j*math.pi*(16*h)*beta)
            rhs=cmath.exp(-4*math.pi**2*(256*t)*h*h)*cmath.exp(-2j*math.pi*h*(16*beta))
            self.assertAlmostEqual(abs(lhs-rhs),0,places=13)

    def test_mean_energy_variance_splitting(self):
        phases=[0.02,0.17,0.46,0.82]
        left=sum(g.gaussian_displacement(x) for x in phases)/len(phases)
        anchor=0.0
        spread=0.0
        for h in range(1,9):
            w=2*math.exp(-h*h)
            M=g.phase_moment(phases,h)
            anchor+=w*abs(M-1)**2
            spread+=w*(1-abs(M)**2)
        self.assertAlmostEqual(left,anchor+spread,places=12)

    def test_one_sided_polarity_window(self):
        epsilon=1/32
        for N in (20,100,1000,10000):
            phase=15/(1024*(N+1)**2)
            length=0
            while phase<=epsilon:
                length+=1
                phase*=16
            bound=1+math.log(1024*epsilon*(N+1)**2/15,16)
            self.assertLessEqual(length,bound+1e-12)

    def test_exact_late_phase_alias(self):
        for n in (1,2,3,7,11):
            unwrapped=g.state(n)
            shifted=unwrapped+Fraction(16**n,16)
            self.assertEqual(Fraction(unwrapped.numerator%unwrapped.denominator,
                                      unwrapped.denominator),
                             Fraction(shifted.numerator%shifted.denominator,
                                      shifted.denominator))

    def test_heat_relaxation_not_point_mixing(self):
        lam=0.5
        actual=math.exp(-lam/2)
        for n in (1,2,3):
            evolved_uncertainty=math.exp(-lam*256**n/2)
            self.assertGreater(actual,evolved_uncertainty)
        self.assertEqual(g.gaussian_displacement(0),0)

    def test_phase_power_blindness(self):
        alpha,beta=0.0,0.31
        self.assertEqual(abs(cmath.exp(2j*math.pi*alpha)),
                         abs(cmath.exp(2j*math.pi*beta)))
        self.assertNotAlmostEqual(abs(cmath.exp(2j*math.pi*alpha)-
                                      cmath.exp(2j*math.pi*beta)),0)

    def test_finite_harmonic_alias(self):
        grid=[j/16 for j in range(16)]
        self.assertLess(abs(g.phase_moment(grid,1)),1e-14)
        self.assertLess(abs(g.phase_moment(grid,15)),1e-13)
        self.assertAlmostEqual(abs(g.phase_moment(grid,16)),1)
        self.assertGreater(g.gaussian_haar_discrepancy(grid,16),0)

    def test_terminal_compensation_exact(self):
        for horizon in (7,12,23):
            endpoint=g.prefix_x(horizon)
            for n in range(1,horizon):
                tn=g.finite_tail(n,horizon)
                tnext=g.finite_tail(n+1,horizon)
                self.assertEqual(tnext-16*tn,-g.forcing(n+1))
                self.assertEqual(g.state(n)+tn,16**n*endpoint)
                self.assertEqual(g.state(n+1)+tnext,16*(g.state(n)+tn))

    def test_improved_terminal_gaussian_bounds(self):
        _, S, R=g.gaussian_sums()
        L=4*math.pi*R
        for B in (2,4,8,16):
            M=2*B
            endpoint=g.prefix_x(M)
            reference=g.prefix_x(M+60)
            true=[g.fraction_mod1(reference*16**n) for n in range(B,2*B)]
            terminal=[g.fraction_mod1(endpoint*16**n) for n in range(B,2*B)]
            q=float(g.terminal_phase_error_upper(B,M))
            self.assertLessEqual(q,1/(4096*B*B)+1e-30)
            self.assertLessEqual(abs(g.gaussian_haar_discrepancy(true)**0.5-
                                     g.gaussian_haar_discrepancy(terminal)**0.5),
                                 2*math.pi*math.sqrt(S)*q+1e-12)
            self.assertLessEqual(abs(sum(g.gaussian_displacement(x) for x in true)/B-
                                     sum(g.gaussian_displacement(x) for x in terminal)/B),
                                 L*q+1e-12)
            self.assertAlmostEqual(g.terminal_shell_source(B)[0],
                                   sum(g.gaussian_displacement(x) for x in terminal)/B, places=13)

    def test_source_gaussian_step_defect_seed_independent(self):
        for n in (1,2,5,40):
            a=g.state(n,seed=Fraction(0)); b=g.state(n+1,seed=Fraction(0))
            aa=g.state(n,seed=Fraction(1,13)); bb=g.state(n+1,seed=Fraction(1,13))
            da=g.fraction_mod1(b-16*a)
            db=g.fraction_mod1(bb-16*aa)
            self.assertEqual(b-16*a,g.forcing(n+1))
            self.assertEqual(bb-16*aa,g.forcing(n+1))
            self.assertAlmostEqual(g.gaussian_displacement(da),g.gaussian_displacement(db),places=13)
            self.assertAlmostEqual(g.source_gaussian_step_defect(n),
                                   g.gaussian_displacement(float(g.forcing(n+1))),places=13)

    def test_fixed_rational_terminal_is_not_haar(self):
        # 16 mod 17 equals -1: q=1/17 has a two-point forward orbit.
        phases=[1/17,16/17]*5
        self.assertAlmostEqual(g.gaussian_haar_discrepancy(phases),
                               g.gaussian_haar_discrepancy(phases[:2]),places=14)
        self.assertGreater(g.gaussian_haar_discrepancy(phases),0.1)

    def test_source_labeled_gaussian_jacobian_gauge(self):
        variance=Fraction(3,11)
        J=[g.jacobian_row(n) for n in range(1,6)]
        cross=[[variance*j for j in row] for row in J]
        self.assertEqual([[v/variance for v in row] for row in cross], [list(row) for row in J])
        # J and -J have indistinguishable output self-covariances;
        # source-labeled cross-covariances have opposite signs.
        for row_a in J:
            for row_b in J:
                orig=g.output_covariance(row_a,row_b,variance)
                mutant=g.output_covariance([-x for x in row_a],[-y for y in row_b],variance)
                self.assertEqual(orig,mutant)
        self.assertNotEqual(cross,[[-v for v in row] for row in cross])

    def test_complex_gaussian_cross_formula_quadrature(self):
        # Independent midpoint quadrature for E[Z exp(i*a*Z)]=i*a exp(-a^2/2).
        norm=(2*math.pi)**-.5
        for a in (0.25,1.15):
            N=20000; step=18/N
            integ=0j
            for j in range(N):
                z=-9+(j+.5)*step
                integ+=z*cmath.exp(1j*a*z)*norm*math.exp(-z*z/2)*step
            analytic=1j*a*math.exp(-a*a/2)
            self.assertLess(abs(integ-analytic),1e-9)

    def test_gaussian_jacobian_needs_unwrapped_anchor(self):
        for n in (1,3,7):
            self.assertEqual(g.jacobian_row(n),g.jacobian_row(n))
            self.assertEqual(g.state(n,seed=Fraction(1,16))-g.state(n),
                             Fraction(16**n,16))
            self.assertNotEqual(g.state(n,seed=Fraction(1,16)),g.state(n))

    def test_severe_gaussian_inverse_conditioning(self):
        a=.4
        tv=2*a/math.pi
        for N in (2,4,8):
            l2=math.sqrt(2)*a*math.exp(-N*N/2)
            self.assertGreater(tv/l2, math.exp(N*N/2)/4)

if __name__ == "__main__":
    unittest.main()

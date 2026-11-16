"""Finite exact checks of the disclosed identities and calibrated false rules."""
from fractions import Fraction as F
from math import comb, factorial, gcd
import unittest

import gamma_phase_probe as p


class SourceContract(unittest.TestCase):
    def test_literal_source_against_combined_polynomial(self):
        for n in list(range(1,70))+[127,256,1024,65537]:
            with self.subTest(n=n):
                expected = F(120*n*n-89*n+16,
                             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
                self.assertEqual(p.forcing(n), expected)

    def test_positive_rate_regrouping(self):
        for n in [1,2,3,8,17,123,10001]:
            self.assertEqual(p.rate_mass(8*n-7),p.forcing(n))

    def test_all_rational_disk_margins(self):
        for a in [F(1,100),F(1,7),F(2,3),1,9,997,F(100000,3)]:
            center,radius,margin=p.forcing_disk(a)
            self.assertGreater(margin,0)
            self.assertEqual(center-radius,p.rate_mass(a))
            self.assertLess(radius,center)

    def test_authentic_boundary_coprime_witnesses(self):
        for numerator in range(1,24):
            for denominator in range(1,12):
                a=F(numerator,denominator)
                x,y=a.numerator,a.denominator
                left,mid,right=x+3*y,x+4*y,x+5*y
                self.assertEqual(gcd(mid,left*right),1)
                self.assertGreater(mid,1)

    def test_dropped_pole_control_is_detected(self):
        for n in [1,11,257]:
            mutant=p.forcing(n)+F(1,8*n-2)
            self.assertNotEqual(mutant,p.rate_mass(8*n-7))

    def test_source_domain(self):
        for x in [0,-1,True,1.0,F(1,2)]:
            with self.assertRaises(ValueError):p.forcing(x)
        for a in [0,-1,True,1.0]:
            with self.assertRaises(ValueError):p.rate_mass(a)


class ModalIdentities(unittest.TestCase):
    def test_laguerre_low_degree(self):
        self.assertEqual(p.laguerre_poly(0),(F(1),))
        self.assertEqual(p.laguerre_poly(1),(F(2),F(-1)))
        self.assertEqual(p.laguerre_poly(2),(F(3),F(-3),F(1,2)))

    def test_exact_orthogonality(self):
        for m in range(13):
            for n in range(13):
                with self.subTest(m=m,n=n):
                    self.assertEqual(p.laguerre_inner(m,n),m+1 if m==n else 0)

    def test_closed_coefficients_against_polynomial_integration(self):
        for omega in [F(-7,3),-1,0,F(1,7),1,F(5,2),11]:
            for m in list(range(13))+[17,23]:
                with self.subTest(omega=omega,m=m):
                    self.assertEqual(p.coefficient_ratio(m,omega),
                                     p.polynomial_coefficient_ratio(m,omega))

    def test_first_coefficient_orientation(self):
        self.assertEqual(p.coefficient_ratio(1,F(3,2)),(F(),F(-3,2)))
        self.assertNotEqual(p.coefficient_ratio(1,2),(F(),F(2)))

    def test_conjugacy(self):
        for m in range(17):
            a,b=p.coefficient_ratio(m,F(7,3))
            self.assertEqual(p.coefficient_ratio(m,F(-7,3)),(a,-b))

    def test_null_frequency_exactly_one_mode(self):
        self.assertEqual(p.relative_mode_weights(0,100),(F(1),)+(F(),)*100)
        self.assertEqual(p.mode_tail_bounds(0,100),(F(),F()))
        self.assertEqual(p.required_mode_cutoff(0,F(1,1000)),0)

    def test_energy_recurrence_vs_independent_coefficients(self):
        for omega in [F(1,3),1,F(7,2),12]:
            values=p.relative_mode_weights(omega,31)
            for m,value in enumerate(values):
                x,y=p.coefficient_ratio(m,omega)
                self.assertEqual(value,(x*x+y*y)/(m+1))

    def test_factorial_mutation_fails(self):
        omega=F(3,2)
        for m in [2,3,7,11]:
            x,y=p.pochhammer(0,-omega,m)
            wrong=(x*x+y*y)/(m+1)  # Deliberately omit (m!)^2.
            self.assertNotEqual(wrong,p.relative_mode_weights(omega,m)[m])

    def test_rational_tail_bounds_order_and_symmetry(self):
        for omega in [F(1,7),F(3,2),3,10,31]:
            for cutoff in [1,2,11,100,1000,100000]:
                lower,upper=p.mode_tail_bounds(omega,cutoff)
                self.assertLessEqual(0,lower)
                self.assertLessEqual(lower,upper)
                self.assertLessEqual(upper,1)
                self.assertEqual((lower,upper),p.mode_tail_bounds(-omega,cutoff))

    def test_nonzero_mode_tail_has_positive_lower_bound(self):
        for omega in [F(1,7),F(3,2),3,10]:
            cutoff=int(omega*omega)+2
            self.assertGreater(p.mode_tail_bounds(omega,cutoff)[0],0)

    def test_sufficient_cutoff_certificate(self):
        for omega in [F(1,3),1,5,10,100]:
            for error in [F(1,2),F(1,10),F(1,1000)]:
                m=p.required_mode_cutoff(omega,error)
                self.assertLessEqual(p.mode_tail_bounds(omega,m)[1],error)
                if m>1:self.assertGreater(p.mode_tail_bounds(omega,m-1)[1],error)

    def test_mode_domain(self):
        for omega in [True,1.0,'1']:
            with self.assertRaises(ValueError):p.relative_mode_weights(omega,2)
        for m in [0,-1,True,1.5]:
            with self.assertRaises(ValueError):p.mode_tail_bounds(1,m)
        for eps in [0,-1,1,2]:
            with self.assertRaises(ValueError):p.required_mode_cutoff(1,eps)


class AuthenticRateLaw(unittest.TestCase):
    def test_exact_moments(self):
        self.assertEqual([p.rate_moment(j) for j in range(5)],
                         [F(1),F(7,2),F(55,3),F(595,4),F(8551,5)])

    def test_moment_independent_unit_cell_clock(self):
        # Independently derive J>=1 moments from sum q^j j^k recurrence,
        # and integrate the five unit cells with multiplicities 4,4,4,2,1.
        q=F(1,16);sums=[]
        for k in range(7):
            sums.append(q/(1-q)*(1+sum((comb(k,l)*sums[l]
                                      for l in range(k)),F())))
        for order in range(7):
            expected=F()
            for degree in range(order+1):
                shift=sum((F(c*((i-6)**(degree+1)-(i-7)**(degree+1)),degree+1)
                           for i,c in enumerate([4,4,4,2,1])),F())
                expected+=comb(order,degree)*8**(order-degree)*sums[order-degree]*shift
            self.assertEqual(expected,p.rate_moment(order))

    def test_tail_identity_vs_original_four_poles(self):
        for n in [0,1,2,17,257]:
            for depth in [0,1,7,19]:
                lo,hi=p.tail_rate_interval(n,depth)
                original=sum((p.forcing(n+j)/16**j for j in range(1,depth+1)),F())
                self.assertEqual(lo,original)
                self.assertGreater(hi,lo)
                next_lo,_=p.tail_rate_interval(n,depth+1)
                self.assertLess(lo,next_lo)
                self.assertLess(next_lo,hi)

    def test_rate_tail_jensen_consistency(self):
        for n in [0,1,7,127]:
            lo,hi=p.tail_rate_interval(n,20)
            self.assertGreater(lo,1/(8*n+F(7,2))**2)
            self.assertLess(hi,F(1,(8*n+1)**2))

    def test_resonance_certified_constant_decreases(self):
        for k in [-3,-1,1,3]:
            vals=[p.resonance_error_bound(n,k,23) for n in [1,4,16,64,256]]
            self.assertTrue(all(a>b for a,b in zip(vals,vals[1:])))
            self.assertEqual(vals,[p.resonance_error_bound(n,-k,23)
                                   for n in [1,4,16,64,256]])

    def test_resonance_domain(self):
        for args in [(0,1,0),(1,0,0),(1,True,0),(1,1,-1),(1,1,0.5)]:
            with self.assertRaises(ValueError):p.resonance_error_bound(*args)


class NonlinearControls(unittest.TestCase):
    def test_integer_circle_character_aliases_every_coin(self):
        for probability in [F(),F(1,7),F(1,2),F(1)]:
            self.assertEqual(p.nonlinear_coin_sample_mean(probability,(1,0)),(1,0))

    def test_half_character_retains_coin_parameter(self):
        for probability in [F(),F(1,7),F(1,2),F(1)]:
            value=p.nonlinear_coin_sample_mean(probability,(-1,0))
            self.assertEqual((1-value[0])/2,probability)

    def test_matching_endpoint_rational_source(self):
        # R0(t)=1-t, x0=1/2. Its completed base-16 orbit is an integer.
        tail=lambda n:F(1,(8*n+1)*(8*n+2))
        u=F()
        for n in range(1,24):
            mutant_forcing=16*tail(n-1)-tail(n)
            self.assertGreater(mutant_forcing,0)
            u=16*u+mutant_forcing
            self.assertEqual(u+tail(n),F(16**n,2))
            self.assertEqual((u+tail(n))%1,0)
        self.assertNotEqual(16*tail(0)-tail(1),p.forcing(1))

    def test_source_seed_control(self):
        # Exact symbolic coordinates in Q + Q*x: U_n(s)+T_n=16^n(x+s).
        for n in range(12):
            original=(F(),F(16**n))
            counterseed=(F(),F(-16**n))
            self.assertEqual(p.gadd(original,counterseed),(F(),F()))


if __name__=='__main__':unittest.main()

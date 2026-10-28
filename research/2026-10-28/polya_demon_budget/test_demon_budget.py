import cmath
import math
import unittest
from fractions import Fraction as Q
from demon_budget import source_law, tilted_law, native_birth, forced_birth, evolve, kl_forward, kl_reverse, fidelity_from_amplitudes


class DemonBudgetExactTests(unittest.TestCase):
    def test_uniform_source_native_transition(self):
        for j in range(40):
            self.assertEqual(evolve(source_law(j),j,native_birth),source_law(j+1))

    def test_changed_kernel_exactly_transports_tilt(self):
        for a in [Q(1,16),Q(1,4),Q(2,3),Q(9,10)]:
            for j in range(40):
                q=tilted_law(a,j)
                rates=lambda j,k:forced_birth(a,j,k)
                self.assertEqual(evolve(q,j,rates),tilted_law(a,j+1))

    def test_changed_kernel_differs_from_source(self):
        for a in [Q(1,16),Q(1,4),Q(2,3)]:
            for j in range(1,22):
                self.assertNotEqual(evolve(tilted_law(a,j),j,native_birth),tilted_law(a,j+1))

    def test_monotone_occupation_and_tight_expectation(self):
        a=Q(1,4)
        for j in range(30):
            q=tilted_law(a,j)
            self.assertLessEqual(sum(k*v for k,v in enumerate(q)), a/(1-a))

    def test_native_beta_martingale(self):
        for j in range(30):
            for k in range(j+1):
                t=native_birth(j,k)
                expectation=(1-t)*Q(k+1,j+3)+t*Q(k+2,j+3)
                self.assertEqual(expectation,Q(k+1,j+2))

    def test_original_endpoint_event_is_null_in_limit(self):
        for j in [0,1,2,7,31,255]:
            self.assertEqual(source_law(j)[0],Q(1,j+1))
            self.assertEqual(source_law(j)[-1],Q(1,j+1))

    def test_fidelity_exact_in_rational_sqrt(self):
        for r in [Q(1,10), Q(1,4),Q(1,2),Q(1),Q(3,2)]:
            for j in range(1,22):
                sm=sum(r**k for k in range(j+1))
                squared=sum(r**(2*k) for k in range(j+1))
                fid=sm**2/((j+1)*squared)
                self.assertEqual(fid,fidelity_from_amplitudes(r,j))
                if r==1:
                    self.assertEqual(fid,1)
                else:
                    self.assertLess(fid,1)
                    closed=(1+r)*(1-r**(j+1))/((j+1)*(1-r)*(1+r**(j+1)))
                    self.assertEqual(fid,closed)

    def test_entropy_asymptotics_both_directions(self):
        a=.25
        j=3000
        h=-math.log(1-a)-a/(1-a)*math.log(a)
        self.assertAlmostEqual(kl_forward(a,j),math.log(j+1)-h,places=11)
        self.assertAlmostEqual(kl_reverse(a,j),j*(-math.log(a))/2-math.log(j+1)-math.log(1-a),places=10)
        self.assertGreater(kl_reverse(a,j),kl_forward(a,j))

    def test_circle_to_line_zero_shift_biased_character(self):
        for p in [2,3,11]:
            L=math.log(p)
            for a in [.25,.5,.8,1.0]:
                for j in [1,2,4,7]:
                    z=sum(a**k for k in range(j+1))
                    for h in range(1,j+1):
                        t=math.pi*h/((j+1)*L)+1j*math.log(a)/(2*L)
                        ch=sum(a**k*cmath.exp(1j*t*(2*k-j)*L) for k in range(j+1))/z
                        self.assertLess(abs(ch),2e-10)
                        self.assertAlmostEqual(t.imag, 0.0 if a==1 else math.log(a)/(2*L),places=12)

    def test_static_biased_source_off_axis_without_dynamics(self):
        L=math.log(2)
        for w in [0.49,0.51,0.6,0.75]:
            z=math.pi/(2*L)+1j*math.log(w/(1-w))/(2*L)
            chi=w*cmath.exp(1j*z*L)+(1-w)*cmath.exp(-1j*z*L)
            self.assertLess(abs(chi),1e-12)
            self.assertNotAlmostEqual(z.imag,0)


if __name__=='__main__':
    unittest.main(verbosity=2)

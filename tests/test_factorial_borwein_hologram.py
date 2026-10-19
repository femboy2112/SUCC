"""Adversarial exact probes of factorial Borwein source preservation."""
from fractions import Fraction as F
from math import factorial, gcd
from observational_succ.borwein_prime_clock import uniform_sum_cdf
import unittest

from observational_succ.factorial_borwein_hologram import (
    FactorialHologramError, legendre_exponent, windows, increment_windows,
    repeated_width_sum, plateau_radius, support_radius, kernel_variance,
    variance_increment, kernel_at, spectral_power_sum, reconstructed_sinc_polynomial,
    interpolant, lifted_prime_gate, poisson_wheel_polynomial,
    infinite_tail_budget, spline_density, exact_continuous_gram, partition_unity_at,
    source_clock_gate,
)


class FactorialHologramTests(unittest.TestCase):
    def test_legendre_vs_factorial_factorization_independently(self):
        for n in range(1,35):
            for p in (2,3,5,7,11,13,17,19,23,29,31):
                value=factorial(n)
                k=0
                while value%p==0:
                    value//=p;k+=1
                self.assertEqual(legendre_exponent(n,p),k)

    def test_window_source_and_reconstruction(self):
        for n in range(1,32):
            ws=windows(n)
            self.assertEqual(len({(w.prime,w.depth) for w in ws}),len(ws))
            self.assertTrue(all(2<=w.depth<=legendre_exponent(n,w.prime) for w in ws))
            before=set((w.prime,w.depth) for w in windows(n-1)) if n>1 else set()
            after=set((w.prime,w.depth) for w in ws)
            self.assertEqual(after-before,set((w.prime,w.depth) for w in increment_windows(n)))
            self.assertLess(repeated_width_sum(n),F(11,12))
            self.assertGreater(plateau_radius(n),F(1,24))
            self.assertLess(support_radius(n),F(1))

    def test_prime_iff_no_spectral_injection(self):
        for n in range(2,61):
            prime = n>=2 and all(n%d for d in range(2,int(n**.5)+1))
            self.assertEqual(variance_increment(n)==0,prime)
            self.assertEqual(bool(increment_windows(n)),not prime)
        self.assertEqual(variance_increment(4),F(5,768))
        self.assertEqual(variance_increment(6),F(337,248832))
        self.assertEqual(kernel_variance(4),kernel_variance(5))
        self.assertEqual(kernel_variance(6),kernel_variance(7))

    def test_lattice_delta_all_horizons(self):
        for n in (1,2,3,4,5,6,7,8,9,10,16,32,128):
            for k in range(-4,5):
                self.assertEqual(kernel_at(n,F(k)),F(int(k==0)))

    def test_exact_off_grid_kernel_and_flatspot_counterexample(self):
        self.assertEqual(kernel_at(4,F(3,10)),F(1))
        self.assertEqual(kernel_at(5,F(3,10)),F(1))
        self.assertEqual(kernel_at(6,F(3,10)),kernel_at(7,F(3,10)))
        self.assertLess(kernel_at(6,F(3,10)),F(1))
        self.assertEqual(kernel_at(4,F(1,10)),kernel_at(6,F(1,10)))
        self.assertEqual(kernel_at(4,F(1,10)),F(1))
        self.assertEqual(kernel_at(6,F(3,10)),kernel_at(6,F(-3,10)))
        for n in (4,6,8,10):
            self.assertEqual(kernel_at(n, F(5)),0)
            self.assertEqual(kernel_at(n,F(0)),1)
        with self.assertRaises(FactorialHologramError):
            kernel_at(12,F(2,5))

    def test_moment_polynomial_reconstructs_exact_multiset(self):
        for n in (1,4,5,6,7,8):
            squares=[F(1,4)]+[w.half_width**2 for w in windows(n)]
            expected=[F(1)]
            for v in squares:
                nxt=[F()]*(len(expected)+1)
                for i,a in enumerate(expected):
                    nxt[i]+=a;nxt[i+1]-=a*v
                expected=nxt
            self.assertEqual(reconstructed_sinc_polynomial(n),tuple(expected))
            self.assertEqual(4*spectral_power_sum(n,1)/3,kernel_variance(n)*4)
        with self.assertRaises(FactorialHologramError):
            reconstructed_sinc_polynomial(60)

    def test_cardinal_interpolant_and_clock_gate_do_not_conflate(self):
        source=((0,F(7,3)),(1,F(2)),(4,F(-5,2)),(8,F(4)),(13,F(1,7)))
        for n in (4,6,8,18):
            for m in range(-3,17):
                self.assertEqual(interpolant(n,source,F(m)),dict(source).get(m,F()))
            for kind in ("one","minus_one","nonzero"):
                for m in range(-3,17):
                    expected=dict(source).get(m,F()) if (m%3=={"one":1,"minus_one":2}.get(kind, m%3 if m%3 else -1)) else F()
                    self.assertEqual(lifted_prime_gate(n,source,3,kind,F(m)),expected)
        self.assertNotEqual(interpolant(4,((0,F(1)),),F(3,10)),
                            interpolant(6,((0,F(1)),),F(3,10)))

    def test_exact_gram_neighbour_overlap_and_riemann_stability(self):
        for n in (4,5,6,7):
            g=exact_continuous_gram(n)
            self.assertEqual(g["diagonal"]+2*g["adjacent"],F(1))
            self.assertGreater(g["adjacent"],F(0))
            self.assertGreaterEqual(g["min_symbol"],g["certified_lower"])
            self.assertGreater(g["certified_lower"],F(1,12))
        self.assertEqual(exact_continuous_gram(4)["adjacent"],F(89,1920))
        self.assertEqual(exact_continuous_gram(4)["diagonal"],F(871,960))
        self.assertEqual(exact_continuous_gram(6)["min_symbol"],
                         F(45340537298096683,56873575734312960))
        with self.assertRaises(FactorialHologramError):
            exact_continuous_gram(8)

    def test_partition_unity_and_half_integer_information_loss(self):
        for n in (1,4,5,6,7,8,9,10):
            for x in (F(-13,10),F(-1),F(-3,10),F(0),F(1,4),
                      F(3,10),F(1,2),F(7,10),F(3,2),F(13,5)):
                self.assertEqual(partition_unity_at(n,x),1)
            self.assertEqual(kernel_at(n,F(1,2)),F(1,2))
            self.assertEqual(kernel_at(n,F(-1,2)),F(1,2))
            self.assertEqual(kernel_at(n,F(3,2)),0)
        self.assertEqual(kernel_at(6,F(3,10)),F(30922061,31104000))

    def test_first_occupation_mutation_breaks_lattice_delta(self):
        # Replacing repeated p^-k windows with support p^-1 windows
        # kills the uniform subcritical budget already at p=2,3,5.
        w=(F(1,4),F(1,6),F(1,10))
        self.assertGreater(2*sum(w),F(1))
        self.assertEqual(uniform_sum_cdf(w,F(3,2))-
                         uniform_sum_cdf(w,F(1,2)),F(1,43200))
        # This positive B(1) is a fully calibrated failure of delta sampling.

    def test_infinite_kernel_effective_uniform_tail(self):
        for n in (4,5,6,7,8,9,10,12,24,48):
            self.assertGreater(infinite_tail_budget(n),0)
        self.assertGreater(infinite_tail_budget(4),infinite_tail_budget(12))
        self.assertGreater(infinite_tail_budget(12),infinite_tail_budget(48))
        for n,m in ((4,6),(6,8),(8,10)):
            for x in (F(-3,4),F(-1,2),F(1,10),F(1,4),F(3,10),F(1,2)):
                self.assertLessEqual(abs(kernel_at(n,x)-kernel_at(m,x)),
                                     2*infinite_tail_budget(n))
        with self.assertRaises(FactorialHologramError):
            spline_density((F(1,2),),F(0))

    def test_clock_gate_mutations(self):
        for args in ((4,((1,F(1)),),4,"one",F(0)),
                     (4,((1,F(1)),),3,"zeros",F(0))):
            with self.assertRaises(FactorialHologramError):
                lifted_prime_gate(*args)
        with self.assertRaises(FactorialHologramError):
            interpolant(4,((1,F(1)),(1,F(2))),F(1))
        with self.assertRaises(FactorialHologramError):
            legendre_exponent(20,4)
        with self.assertRaises(FactorialHologramError):
            kernel_at(True,F(0))
        with self.assertRaises(FactorialHologramError):
            kernel_at(4,.1)
        self.assertTrue(source_clock_gate(-1,7,"minus_one"))
        self.assertFalse(source_clock_gate(-1,7,"one"))
        self.assertEqual(lifted_prime_gate(4,((-1,F(5)),),7,"minus_one",F(-1)),5)
        self.assertEqual(lifted_prime_gate(4,((-1,F(5)),),7,"one",F(-1)),0)
        self.assertEqual(poisson_wheel_polynomial(-3,((2,"nonzero"),),F(0),0),
                         (F(1),F(0)))

    def test_poisson_coefficients_vs_independent_path_count(self):
        gates=((3,"one"),(5,"nonzero"))
        t=F(2,3)
        poly,tail=poisson_wheel_polynomial(0,gates,t,9)
        manual=F()
        for k in range(10):
            if (k%3==1) and k%5:
                manual+=t**k/factorial(k)
        self.assertEqual(poly,manual)
        self.assertEqual(tail,t**10/factorial(10))
        for d in (0,1,3,6,12):
            p,error=poisson_wheel_polynomial(1,((2,"one"),),F(1),d)
            self.assertTrue(0<=p<=sum((F(1,factorial(k)) for k in range(d+1)),F()))
            self.assertEqual(error,F(1,factorial(d+1)))
        for args in ((0,((4,"one"),),F(1),6),
                     (0,((3,"one"),(3,"nonzero")),F(1),3),
                     (0,((3,"one"),),F(-1),3)):
            with self.assertRaises(FactorialHologramError):
                poisson_wheel_polynomial(*args)


if __name__ == "__main__":
    unittest.main()

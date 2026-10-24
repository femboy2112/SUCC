"""Adversarial integer/Fraction witnesses for prime-clock projection theorems."""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_source_memory import forcing, tail_interval
from observational_succ.bbp_cyclotomic_birth import (
    first_window_residues, multiplicative_order_16, source_window_split,
)
from observational_succ.bbp_prime_window_projection import (
    window_parameters, additive_clock_partition, source_complement_window,
    circular_distance, rational_phase_dispersion_bracket,
    exact_source_period_defects, source_defect_variance_upper,
    window_pi_source_shadow_budget, shadow_uniform_budget,
    first_resonant_clock_period, periodic_profile_orthogonality,
    source_periodicity_obstruction,
)


def unit_fraction_phase(x):
    """Float is a NONPROOF numerical regression only; exact x mod 1 first."""
    return cmath.exp(2j*math.pi*float(Q(x)%1))


def direct_complex_dispersion_squared(w,h,d):
    N=len(w);K=N//d
    return sum(
        abs(unit_fraction_phase(h*w[r+i*d])
            -sum((unit_fraction_phase(h*w[r+j*d])
                  for j in range(K)),0j)/K)**2
        for r in range(d) for i in range(K))/N


class PurePrimeClockAlgebra(unittest.TestCase):
    def test_source_index_and_complete_blocks_are_exact(self):
        for p in (17,41,73,89,97,113,137,193):
            m,L,N,B=window_parameters(p)
            self.assertEqual((8*m+1,3*m//L),(p,B))
            self.assertEqual(first_window_residues(p),
                             tuple(4*pow(16,t,p)%p for t in range(N)))
            self.assertEqual(len(source_complement_window(p)),N)
            self.assertGreaterEqual(B,3)

    def test_coset_completion_for_every_divisor_clock(self):
        for p in (17,41,73,89,97,113):
            m,L,N,B=window_parameters(p)
            for d in range(1,N+1):
                if N%d:continue
                profile=periodic_profile_orthogonality(p,d)
                data=additive_clock_partition(p,d)
                self.assertTrue(profile["exact_cover"])
                self.assertEqual(data["gcd"],math.gcd(d,L))
                self.assertEqual(data["suborder"],L//math.gcd(d,L))
                self.assertEqual(data["repetitions"]*data["suborder"],N//d)
                for r in range(d):
                    # Deliberately independent direct period and multiplicity.
                    raw=[4*pow(16,t,p)%p for t in range(r,N,d)]
                    orbit=[4*pow(16,r+d*j,p)%p for j in range(L//math.gcd(L,d))]
                    self.assertEqual(raw,orbit*data["repetitions"])

    def test_does_not_assume_d_divides_L(self):
        m,L,N,B=window_parameters(73)  # L=9, N=27
        self.assertEqual(L,9)
        d=27  # d does NOT divide L yet d|N; class has one time slot
        self.assertEqual(additive_clock_partition(73,d)["suborder"],1)
        self.assertEqual(periodic_profile_orthogonality(73,d)["class_lengths"],
                         (1,)*27)
        with self.assertRaises(ValueError):
            additive_clock_partition(73,5)
        with self.assertRaises(ValueError):
            additive_clock_partition(17,0)

    def test_source_period_competing_clock_control(self):
        for p,d in ((41,3),(73,3),(97,3),(113,3)):
            N=window_parameters(p)[2]
            roots=(0,1,2)
            periodic_amplitudes=[unit_fraction_phase(Q(t%3,3)) for t in range(N)]
            self.assertEqual(len(periodic_amplitudes),N)
            direct=sum(
                unit_fraction_phase(Q(4*pow(16,t,p),p))*periodic_amplitudes[t]
                for t in range(N))/N
            classes=sum(
                periodic_amplitudes[r] *
                sum(unit_fraction_phase(Q(4*pow(16,r+d*j,p),p))
                    for j in range(additive_clock_partition(p,d)["suborder"]))
                /additive_clock_partition(p,d)["suborder"]
                for r in range(d))/d
            self.assertLess(abs(direct-classes),1e-11)

    def test_resonance_requires_long_clock_complexity(self):
        for p in (17,41,73,97,113):
            m,L,N,B=window_parameters(p)
            self.assertEqual(first_resonant_clock_period(p,1),L)
            u=[unit_fraction_phase(Q(4*pow(16,t,p),p)) for t in range(N)]
            v=[unit_fraction_phase(Q(-4*pow(16,t,p),p)) for t in range(N)]
            self.assertLess(abs(sum((a*b for a,b in zip(u,v)),0j)-N),1e-10)
            with self.assertRaises(ValueError):
                first_resonant_clock_period(p,p)
        with self.assertRaises(ValueError):
            window_parameters(21)

    def test_prime_source_inputs_reject_bad_types(self):
        for bad in (True,1.5,-2):
            with self.assertRaises(ValueError):
                window_parameters(bad)
        for bad in (True,1.0):
            with self.assertRaises(ValueError):
                additive_clock_partition(17,bad)


class SourceSelectedProjection(unittest.TestCase):
    def test_rational_lower_bounds_rule_out_exact_periodicity(self):
        for p,d in ((17,1),(17,3),(41,1),(41,3),(73,1),(73,3)):
            lower,upper=rational_phase_dispersion_bracket(p,d)
            self.assertTrue(Q()<lower<=upper<=1)
            actual=direct_complex_dispersion_squared(source_complement_window(p),1,d)
            self.assertLessEqual(float(lower)-1e-12,actual)
            self.assertLessEqual(actual,float(upper)+1e-12)
        self.assertGreater(rational_phase_dispersion_bracket(17,1)[0],Q(1,2))
        self.assertGreater(rational_phase_dispersion_bracket(17,3)[0],Q(1,4))
        self.assertLess(rational_phase_dispersion_bracket(17,3)[1],Q(2,3))
        self.assertGreater(rational_phase_dispersion_bracket(41,1)[0],Q(7,10))
        self.assertGreater(rational_phase_dispersion_bracket(73,1)[0],Q(13,20))

    def test_orthogonal_projection_source_difference_bound(self):
        for p,d in ((17,1),(17,2),(17,3),(41,3),(73,3)):
            w=source_complement_window(p)
            N=len(w)
            local=[unit_fraction_phase(Q(4*pow(16,t,p),p)) for t in range(N)]
            v=[unit_fraction_phase(w[t]) for t in range(N)]
            k=N//d
            avg=[sum(v[r+d*j] for j in range(k))/k for r in range(d)]
            low_period=sum(local[t]*avg[t%d] for t in range(N))/N
            error=sum(local[t]*(v[t]-avg[t%d]) for t in range(N))/N
            actual=sum(local[t]*v[t] for t in range(N))/N
            self.assertLess(abs(actual-(low_period+error)),1e-12)
            D2=sum(abs(v[t]-avg[t%d])**2 for t in range(N))/N
            self.assertLessEqual(abs(error),math.sqrt(D2)+1e-12)
            self.assertLessEqual(D2,float(rational_phase_dispersion_bracket(p,d)[1])+1e-12)
            self.assertLessEqual(D2,float(source_defect_variance_upper(p,d))+1e-12)
            coset_max=max(abs(sum(local[r+d*j] for j in range(k))/k)
                          for r in range(d))
            self.assertLessEqual(abs(low_period),coset_max+1e-12)

    def test_forcing_causal_period_defect_exact(self):
        for p,d in ((17,1),(17,3),(41,1),(41,3),(73,3)):
            w=source_complement_window(p)
            D=exact_source_period_defects(p,d)
            self.assertEqual(len(D),len(w)-d)
            self.assertEqual(D,tuple(
                circular_distance(w[t+d]-w[t]) for t in range(len(w)-d)))
            self.assertGreater(sum(D),0)
            finite=source_periodicity_obstruction(p,d)
            self.assertGreater(finite["forcing_difference"],0)
            self.assertGreater(finite["phase_gap"],0)
            self.assertLessEqual(finite["phase_gap"],
                                 16*finite["first_defect"]+finite["successor_defect"])
            self.assertGreater(max(finite["first_defect"],
                                   finite["successor_defect"]),0)
            self.assertGreater(finite["minimum_maximum_defect"],0)
        with self.assertRaises(ValueError):
            source_periodicity_obstruction(17,6)

    def test_certified_source_window_shadow_error_is_O_inverse_m(self):
        for p in (17,41,73,97,113,137):
            m,L,N,B=window_parameters(p)
            for h in (0,1,-2,5):
                actual_budget=window_pi_source_shadow_budget(p,h)
                outer=shadow_uniform_budget(p,h)
                if h:
                    self.assertTrue(0<actual_budget<outer)
                else:
                    self.assertEqual((actual_budget,outer),(0,0))
                self.assertEqual(
                    actual_budget,
                    Q(44*abs(h),7)*sum(
                        (Q(1,(8*n+1)*(8*n+2))
                         for n in range(m+1,4*m+1)),Q()))
                # the source-Green interval upper truly dominates the
                # tail in each observed slot; no sampled pi input.
                for n in range(m+1,4*m+1):
                    lo,hi=tail_interval(n,4)
                    self.assertLess(hi,Q(1,(8*n+1)*(8*n+2)))

    def test_positive_lower_witness_with_many_signed_controls(self):
        for p,d in ((17,1),(17,3),(41,3),(73,3)):
            data=additive_clock_partition(p,d)
            lower,upper=rational_phase_dispersion_bracket(p,d,h=2)
            self.assertLessEqual(lower,upper)
            w=source_complement_window(p)
            self.assertGreaterEqual(sum(
                circular_distance(2*(w[j+d]-w[j]))
                for j in range(len(w)-d)),0)


if __name__=="__main__":
    unittest.main()

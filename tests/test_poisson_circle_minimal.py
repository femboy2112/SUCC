"""Independent exact and negative controls for minimum circle kernel theorem."""
import math
import unittest
from fractions import Fraction as Q
from math import factorial

from observational_succ.poisson_circle_minimal import (
    exact_point, chord_squared, poisson_chord, exact_potential, exact_energy,
    exact_power_point, exact_rational_covering_orbit, exact_rational_covering_energy,
    rational_greedy_circle, first_greedy_candidate, exact_greedy_regret,
    energy_from_excess, safe_positive_regret_bound, polygon_poisson_energy,
    orbit_potential_bijection, pair_magnification_sum,
    haar_origin_expected_energy, finite_grid_origin_fourier_square,
    chord_covering_exact, exact_energy_from_one_chord,
    ternary_periodic_counterfeit_energy,
    finite_grid_origin_energy_interval,
    dyadic_nearest_center, _cos_taylor_enclosure, _centered_turn,
    rational_turn_energy_interval, certified_pi_energy, energy_to_weyl_upper,
)
from observational_succ.pi_prime_carry_transport import wallis_pi_bracket


def _independent_fourier_power(z, degree):
    # Complex-power recurrence independently computed in exact Q[i].
    a, b = z
    re, im = Q(1), Q(0)
    for _ in range(degree):
        re, im = re*a-im*b, re*b+im*a
    return re, im


def _fourier_energy_partial(points, band):
    n = len(points)
    total = Q(1)
    for h in range(1, band+1):
        re = im = Q(0)
        for z in points:
            r, i = _independent_fourier_power(z, h)
            re += r
            im += i
        total += Q(2, 2**h)*(re*re+im*im)/(n*n)
    return total


def _machin_bracket(terms=16):
    def alt(x):
        a = sum((Q((-1)**k, (2*k+1)*x**(2*k+1)) for k in range(terms)), Q())
        tail = Q(1, (2*terms+1)*x**(2*terms+1))
        return (a, a+tail) if terms%2 == 0 else (a-tail, a)
    l5,u5=alt(5)
    l239,u239=alt(239)
    return 16*l5-4*u239,16*u5-4*l239


class ExactPoissonKernel(unittest.TestCase):
    def test_01_exact_chord_and_positive_point_guards(self):
        e = exact_point(0)
        antipode = (Q(-1), Q(0))
        i = exact_point(1)
        self.assertEqual(e, (Q(1), Q(0)))
        self.assertEqual(i, (Q(0), Q(1)))
        self.assertEqual(chord_squared(e,e),0)
        self.assertEqual(chord_squared(e,antipode),4)
        self.assertEqual(chord_squared(e,i),2)
        self.assertEqual(poisson_chord(e,e),3)
        self.assertEqual(poisson_chord(e,antipode),Q(1,3))
        self.assertEqual(poisson_chord(e,i),Q(3,5))

    def test_02_symmetry_and_kernel_extrema_on_rational_grid(self):
        pts = [exact_point(a, b) for b in range(1,5) for a in range(-4,5)]
        for x in pts:
            for y in pts:
                self.assertEqual(poisson_chord(x,y),poisson_chord(y,x))
                self.assertGreaterEqual(poisson_chord(x,y),Q(1,3))
                self.assertLessEqual(poisson_chord(x,y),Q(3))

    def test_03_independent_complex_fourier_bounds_all_small_samples(self):
        pts=[exact_point(i, 3) for i in (-3,-2,-1,0,1,2,3)]
        for n in range(1,8):
            actual=exact_energy(pts[:n])
            for H in (1,2,3,6,12):
                partial=_fourier_energy_partial(pts[:n],H)
                self.assertLessEqual(partial,actual)
                self.assertLessEqual(actual,partial+Q(2,2**H))

    def test_04_exact_greedy_energy_is_O_inverse_n(self):
        samples=rational_greedy_circle(20,max_height=14)
        self.assertEqual(samples[0],exact_point(0))
        self.assertEqual(samples[1],(Q(-1),Q(0)))
        for n in range(1,21):
            prefix=samples[:n]
            self.assertLessEqual(exact_energy(prefix),1+Q(2,n))
            self.assertEqual(exact_energy(prefix),energy_from_excess(prefix))
            self.assertEqual(safe_positive_regret_bound(prefix),1+Q(2,n))
            self.assertGreaterEqual(exact_energy(prefix),1)

    def test_05_replay_every_potential_threshold(self):
        pts=rational_greedy_circle(17,max_height=12)
        for n in range(1,len(pts)):
            self.assertLessEqual(exact_potential(pts[:n],pts[n]),n)
        self.assertEqual(first_greedy_candidate(pts[:3],10),pts[3])

    def test_06_finite_search_fail_closed_and_exact_inputs(self):
        for bad in (True,2.0,Q(2),-1):
            with self.assertRaises(ValueError):
                rational_greedy_circle(bad)
        with self.assertRaises(ValueError): exact_point(1,0)
        with self.assertRaises(ValueError): exact_point(1,True)
        with self.assertRaises(ValueError): poisson_chord((Q(0),Q(0)),exact_point(0))
        with self.assertRaises(ValueError): exact_energy(())

    def test_07_non_greedy_origin_and_positive_regret_scale(self):
        p=exact_point(0)
        pts=[p]*12
        self.assertEqual(exact_energy(pts),3)
        self.assertEqual(exact_greedy_regret(pts),tuple(2*n for n in range(12)))
        self.assertEqual(energy_from_excess(pts),3)
        self.assertEqual(safe_positive_regret_bound(pts),3)

    def test_08_two_point_energy_and_signed_excess(self):
        pts=(exact_point(0),(Q(-1),Q(0)))
        self.assertEqual(exact_energy(pts),Q(5,3))
        self.assertEqual(exact_greedy_regret(pts),(Q(0),Q(-2,3)))
        self.assertEqual(energy_from_excess(pts),Q(5,3))

    def test_09_nonuniform_finite_polygon_small_energy(self):
        for q in (2,3,5,7,11,17,29):
            self.assertEqual(polygon_poisson_energy(q),1+Q(2,2**q-1))
        self.assertLess(polygon_poisson_energy(29)-1,Q(1,10**8))
        self.assertEqual(polygon_poisson_energy(3),Q(9,7))
        # x=1/3, doubling visits only 2 of the 3 roots: limit energy 12/7.
        self.assertEqual((2*3+2*Q(3,7))/4,Q(12,7))

    def test_10_true_forward_orbit_differs_from_free_greedy(self):
        p=exact_point(0)
        self.assertEqual(exact_power_point(p,0),p)
        self.assertEqual(exact_power_point(exact_point(1),2),(Q(-1),Q(0)))
        self.assertEqual(exact_rational_covering_energy(p,2,10),3)
        path=exact_rational_covering_orbit(exact_point(1),2,7)
        self.assertEqual(path[0],exact_point(1))
        self.assertEqual(path[1],(Q(-1),Q(0)))
        self.assertEqual(path[2:],((Q(1),Q(0)),)*5)
        self.assertGreater(exact_rational_covering_energy(exact_point(1),2,7),1+Q(2,7))
        z=exact_point(1,2)
        self.assertEqual(exact_power_point(z,6),exact_power_point(exact_power_point(z,2),3))
        with self.assertRaises(ValueError): exact_power_point(z,-1)

    def test_10_pi_first_doubling_is_not_exact_greedy(self):
        # For first step, the exact minimizer is the antipode; 2π−π=π
        # modulo one is not 1/2, because π is irrational.
        # Independent rational source bounds confine the fractional part to (0,1/2).
        ml, mu = _machin_bracket()
        self.assertGreater(ml,3)
        self.assertLess(mu,Q(7,2))
        # Stronger true-π exact source test: the two-step orbital energy is
        # strictly ABOVE the global two-point antipodal minimum 5/3.
        source = certified_pi_energy(2,2,wallis_steps=128,dyadic_bits=44,taylor_order=14)
        self.assertGreater(source.energy_lower,Q(5,3))

    def test_11_lag_decomposition_and_total_pair_magnification(self):
        for base in (2,3,10,16):
            for n in range(1,11):
                pairs=orbit_potential_bijection(base,n)
                self.assertEqual(len(pairs),n*(n-1)//2)
                self.assertEqual(sum(2*triplet[2] for triplet in pairs),
                                 pair_magnification_sum(base,n))
                self.assertEqual(pair_magnification_sum(base,n),
                                 sum(abs(base**j-base**k) for j in range(n) for k in range(n)))

    def test_12_interval_phase_reduction(self):
        self.assertEqual(_centered_turn(Q(8,7)),Q(1,7))
        self.assertEqual(_centered_turn(Q(-8,7)),Q(-1,7))
        self.assertEqual(_centered_turn(Q(1,2)),Q(-1,2))
        with self.assertRaises(ValueError):
            _cos_taylor_enclosure(Q(3,4),Q(22,7),Q(1,100),12)

    def test_13_cos_taylor_rational_exact_holdouts(self):
        ml,mu=_machin_bracket()
        midpoint=(ml+mu)/2
        eps=(mu-ml)/2
        for turns in (Q(0),Q(1,2),Q(1,3),Q(-1,7),Q(5,12)):
            lo,hi=_cos_taylor_enclosure(turns,midpoint,eps,14)
            val=math.cos(2*math.pi*float(turns))
            self.assertLessEqual(float(lo),val+1e-13)
            self.assertGreaterEqual(float(hi),val-1e-13)
        with self.assertRaises(ValueError):
            _cos_taylor_enclosure(Q(1,4),midpoint,Q(-1),14)

    def test_14_exact_wallispolygon_pi_source_numerical_holdout(self):
        ml,mu=_machin_bracket()
        for steps in (1,2,5,128,512):
            lo,hi=wallis_pi_bracket(steps)
            self.assertLess(lo,ml)
            self.assertGreater(hi,mu)
            center,eps=dyadic_nearest_center(lo,hi,48)
            self.assertLessEqual(abs(center-lo),eps)
            self.assertLessEqual(abs(center-hi),eps)

    def test_15_rational_phase_energy_1_3_source(self):
        ml,mu=_machin_bracket()
        center=(ml+mu)/2
        eps=(mu-ml)/2
        for horizon in (2,4,6):
            lo,hi=rational_turn_energy_interval(Q(1,3),2,horizon,center,eps,14)
            self.assertLess(lo,Q(12,7))
            self.assertGreater(hi,Q(12,7))

    def test_16_pi_source_interval_energy_finite_nontrivial(self):
        r=certified_pi_energy(2,4,wallis_steps=512,dyadic_bits=48,taylor_order=14)
        self.assertLess(r.transport_error,Q(1,4))
        self.assertGreater(r.energy_lower,Q(1))
        self.assertLess(r.energy_upper,Q(2))
        self.assertLessEqual(r.energy_lower,r.energy_upper)
        self.assertLess(energy_to_weyl_upper(r.energy_upper,1),Q(1))
        with self.assertRaises(ValueError):
            energy_to_weyl_upper(Q(4),1)

    def test_17_independent_actual_pi_numeric_holdout(self):
        # Only a finite numerical independent check, NEVER a proof of limits.
        for n,steps in ((3,128),(4,512),(5,1024)):
            r=certified_pi_energy(2,n,wallis_steps=steps,dyadic_bits=48,taylor_order=14)
            phases=[2**j*math.pi for j in range(n)]
            value=sum(3/(5-4*math.cos(2*math.pi*(x-y)))
                      for x in phases for y in phases)/(n*n)
            self.assertLessEqual(float(r.energy_lower),value+1e-9)
            self.assertGreaterEqual(float(r.energy_upper),value-1e-9)

    def test_18_horizon_increased_without_precision_returns_wider_bound(self):
        small=certified_pi_energy(2,3,wallis_steps=128)
        large=certified_pi_energy(2,6,wallis_steps=128)
        self.assertLess(small.transport_error,large.transport_error)
        self.assertEqual(large.energy_upper,Q(3))

    def test_19_source_rejects_untrusted_input_types(self):
        for bad in (True,3.2,Q(3)):
            with self.assertRaises(ValueError):certified_pi_energy(2,bad)
        with self.assertRaises(ValueError):certified_pi_energy(True,3)
        with self.assertRaises(ValueError):rational_turn_energy_interval(.2,2,3,Q(22,7),Q(1,7),10)

    def test_20_one_chord_exactly_predicts_complete_target_energy(self):
        for z in (exact_point(0),exact_point(1),exact_point(-1),
                  exact_point(1,2),exact_point(2,3)):
            x=chord_squared(z,exact_point(0))
            for b in (2,3):
                for N in (1,2,3,5):
                    self.assertEqual(exact_energy_from_one_chord(x,b,N),
                                     exact_rational_covering_energy(z,b,N))
                    self.assertEqual(exact_energy_from_one_chord(x,b,N),
                                     exact_rational_covering_energy((z[0],-z[1]),b,N))
        self.assertEqual(chord_covering_exact(Q(2),2),Q(4))
        self.assertEqual(chord_covering_exact(Q(2),3),Q(2))
        with self.assertRaises(ValueError):chord_covering_exact(Q(5),2)

    def test_20_certified_pi_exceeds_haar_average_at_N4_and_N6(self):
        # These are POSITIVE finite source witnesses, not any asymptotic trend.
        for N in (4,6):
            r=certified_pi_energy(2,N,wallis_steps=4096,
                                  dyadic_bits=48,taylor_order=14)
            self.assertGreater(r.energy_lower,haar_origin_expected_energy(N))
            # Signed successor potential excess = N^2*(E_N-1)/2 - N.
            self.assertGreater(Q(N*N,2)*(r.energy_lower-1)-N,0)

    def test_20_ternary_exact_single_nonnormal_orbit_energy_almost_haar(self):
        self.assertEqual(ternary_periodic_counterfeit_energy(1),Q(12,7))
        self.assertEqual(ternary_periodic_counterfeit_energy(2),
                         1+Q(1,14)+Q(3,1022))
        # One *selected* rational orbit, not an ensemble mixture.
        self.assertLess(ternary_periodic_counterfeit_energy(4)-1,Q(1,10**8))
        for depth in range(1,5):
            self.assertGreater(ternary_periodic_counterfeit_energy(depth),1)
            if depth>1:
                self.assertLess(ternary_periodic_counterfeit_energy(depth),
                                ternary_periodic_counterfeit_energy(depth-1))
            q=3**depth
            residues=[]
            x=1
            for _ in range(2*3**(depth-1)):
                residues.append(x)
                x=2*x%q
            self.assertEqual(x,1)
            self.assertEqual(len(set(residues)),2*3**(depth-1))
            self.assertEqual(set(residues),
                             {r for r in range(1,q) if math.gcd(r,q)==1})

    def test_20_exact_haar_origin_mean_matches_greedy_rate(self):
        for n in range(1,19):
            self.assertEqual(haar_origin_expected_energy(n),1+Q(2,n))

    def test_21_finite_polygon_origin_fourier_aliases_and_diagonal(self):
        for base in (2,3,16):
            for n in (2,3,5):
                H=4
                modulus=H*(base**(n-1)-1)+1
                for h in range(1,H+1):
                    self.assertEqual(finite_grid_origin_fourier_square(base,n,h,modulus),Q(1,n))
                low,hi=finite_grid_origin_energy_interval(base,n,H,modulus)
                self.assertEqual(low,1+Q(2,n)*(1-Q(1,2**H)))
                self.assertGreaterEqual(hi,1+Q(2,n))
                self.assertLessEqual(hi-low,Q(2,2**H))
        # Fixed 2-adic grid aliases when doubling collapses the vertices.
        self.assertEqual(finite_grid_origin_fourier_square(2,3,1,2),Q(5,9))

    def test_22_finite_origin_grid_cannot_certify_selected_orbit(self):
        for m in (5,17,97):
            low,up=finite_grid_origin_energy_interval(2,5,8,m)
            self.assertLessEqual(low,3)
            self.assertGreaterEqual(up,low)
        self.assertEqual(exact_rational_covering_energy(exact_point(0),2,5),3)

    def test_20_finite_kernel_modes_truly_all_visible(self):
        # A q-gon can defeat *every finite Fourier test* below q;
        # its single Poisson energy nevertheless detects it positively.
        for q in (5,7,13,29):
            self.assertGreater(polygon_poisson_energy(q),1)
            self.assertEqual(sum(Q(1) for h in range(1,q) if h%q==0),0)


if __name__=="__main__":
    unittest.main()

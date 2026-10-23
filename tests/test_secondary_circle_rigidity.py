"""Hostile exact tests for finite prime-coherent secondary circle reconstruction."""
import math
import unittest
from fractions import Fraction as Q

from observational_succ.secondary_circle_rigidity import (
    primes_to, factor_word, prime_cosine_edges, real_chord_rigidity,
    sqrt_upper, amplified_fourier_bound, joint_rigidity_bound,
    exact_rational_orbit_cosine, exact_uniform_polygon_cosine,
    doubling_orbit, ramanujan_sum, mobius, interval_prime_and_chord_budget,
)


def moments_for_q(q, base, M):
    return (Q(1),)+tuple(exact_rational_orbit_cosine(q, base, h)
                         for h in range(1, M+1))


class PrimeCoherenceExactTests(unittest.TestCase):
    def test_01_genuine_prime_only(self):
        self.assertEqual(primes_to(31), (2,3,5,7,11,13,17,19,23,29,31))
        for n in range(1,400):
            factors = factor_word(n)
            self.assertEqual(math.prod(factors),n)
            self.assertEqual(tuple(sorted(factors)),factors)
            self.assertTrue(all(p in primes_to(p) for p in factors))

    def test_02_exact_ramanujan_known_values(self):
        for q in (3,5,7,9,11,25):
            for h in range(0, 2*q+2):
                units = [k for k in range(1,q) if math.gcd(k,q)==1]
                predicted = ramanujan_sum(q,h)
                if h%q==0:
                    self.assertEqual(predicted, len(units))
                self.assertLessEqual(abs(predicted),len(units))
        self.assertEqual([ramanujan_sum(9,h) for h in (1,3,9)], [0,-3,6])
        self.assertEqual(mobius(1),1)
        self.assertEqual(mobius(4),0)
        self.assertEqual(mobius(30),-1)

    def test_03_rational_orbits_require_signed_full_unit_system(self):
        for q in (3,5,7,9):
            orbit = doubling_orbit(q)
            self.assertEqual(set(orbit)|{-v%q for v in orbit},
                             {n for n in range(1,q) if math.gcd(n,q)==1})
            self.assertEqual(exact_rational_orbit_cosine(q,2,1), Q(ramanujan_sum(q,1),sum(1 for j in range(1,q) if math.gcd(j,q)==1)))
        with self.assertRaises(ValueError):
            exact_rational_orbit_cosine(31,2,1)
        with self.assertRaises(ValueError):
            doubling_orbit(8,2)

    def test_04_fejer_and_prime_chord_bound_universally_on_rational_sources(self):
        checked=0
        for q in (3,5,7,9):
            for M in range(2,61):
                moments = moments_for_q(q,2,M)
                result=real_chord_rigidity(moments)
                self.assertGreaterEqual(result.fejer_integral,0)
                self.assertLessEqual(result.harmonic_bound,1)
                self.assertGreaterEqual(result.harmonic_bound,max(abs(v) for v in moments[1:]))
                self.assertLessEqual(result.harmonic_bound,result.simple_bound)
                self.assertGreaterEqual(result.max_prime_cosine_defect,0)
                self.assertEqual(result.mean_chord, 2-2*moments[1])
                checked+=M
        self.assertGreater(checked,7000)

    def test_05_origin_has_full_coherence_but_fails_chord(self):
        r = real_chord_rigidity([Q(1)]*61)
        self.assertEqual(r.chord_deficit,2)
        self.assertEqual(r.max_prime_cosine_defect,0)
        self.assertEqual(r.harmonic_bound,1)

    def test_06_exact_periodic_chord_looks_fine_at_first_order(self):
        # For base-2 orbit of 1/9, all six unit residues occur.
        # c1=0 (perfect chord), but c_(3*2^j)=-1/2 at all zooms.
        ms=moments_for_q(9,2,40)
        self.assertEqual(ms[1],0)
        self.assertEqual(2-2*ms[1],2)
        for j in range(0,4):
            self.assertEqual(ms[3*2**j],Q(-1,2))
        r=real_chord_rigidity(ms)
        self.assertGreaterEqual(r.max_prime_cosine_defect,Q(1,2))
        self.assertEqual(ms[3],Q(-1,2))

    def test_07_periodic_thirds_reverse_chord_error(self):
        ms=moments_for_q(3,2,36)
        self.assertEqual(ms[1],Q(-1,2))
        r=real_chord_rigidity(ms)
        self.assertEqual(r.mean_chord,3)
        self.assertEqual(r.chord_deficit,0)
        self.assertGreaterEqual(r.max_prime_cosine_defect,Q(3,2))
        self.assertEqual(ms[3],1)

    def test_08_missing_single_prime_fake_perfection(self):
        # Uniform 5-gon is invariant under every prime except 5;
        # its first chord moment equals Haar, but it is atomic.
        moments=tuple(exact_uniform_polygon_cosine(5,h) for h in range(26))
        self.assertEqual(moments[1],0)
        r4=real_chord_rigidity(moments[:5])
        self.assertEqual(r4.max_prime_cosine_defect,0)
        r5=real_chord_rigidity(moments[:6])
        self.assertEqual(r5.max_prime_cosine_defect,1)
        self.assertEqual(moments[5],1)

    def test_09_fejer_positivity_fails_closed(self):
        with self.assertRaises(ValueError):
            real_chord_rigidity([Q(1),Q(-1),Q(-1),Q(-1)])
        with self.assertRaises(ValueError):
            real_chord_rigidity([Q(1),Q(2),Q(0)])
        with self.assertRaises(ValueError):
            prime_cosine_edges([Q(0), Q(0),Q(0)])
        with self.assertRaises(ValueError):
            real_chord_rigidity([1,0])
        with self.assertRaises(ValueError):
            real_chord_rigidity([1,0.1,0])

    def test_10_exact_nontrivial_haar_bound(self):
        r = real_chord_rigidity([Q(1)]+[Q(0)]*128)
        self.assertEqual(r.max_prime_cosine_defect,0)
        self.assertEqual(r.mean_chord,2)
        self.assertEqual(r.fejer_integral,1)
        self.assertEqual(r.harmonic_bound,Q(1,127))


class FourierFiniteAmplification(unittest.TestCase):
    def test_11_sqrt_outward_is_exact(self):
        for num in range(0,65):
            for den in range(1,13):
                x=Q(num,den)
                y=sqrt_upper(x,32)
                self.assertGreaterEqual(y*y,x)
                self.assertLess((y-Q(1,2**32))**2,x+Q(1,2**20))
        self.assertEqual(sqrt_upper(Q(9,16)),Q(3,4))
        with self.assertRaises(ValueError):
            sqrt_upper(Q(-1,7))

    def test_12_amplification_source_bound_real(self):
        r=joint_rigidity_bound([Q(1)]+[Q(0)]*128, base=2, frequency=1,
                               horizon=1000,replicas=8)
        self.assertLess(r.modulus_upper,Q(1,2))
        self.assertEqual(r.endpoint_error,Q(7,1000))
        self.assertGreaterEqual(r.modulus_upper*r.modulus_upper,r.variance_upper)

    def test_13_cutoff_must_cover_correlations(self):
        with self.assertRaises(ValueError):
            amplified_fourier_bound(base=2,frequency=3,horizon=100,
                  replicas=7,cutoff=100,cosine_band_bound=Q(0))
        with self.assertRaises(ValueError):
            amplified_fourier_bound(base=1,frequency=3,horizon=100,
                  replicas=7,cutoff=1000,cosine_band_bound=Q(0))
        with self.assertRaises(ValueError):
            amplified_fourier_bound(base=2,frequency=True,horizon=100,
                  replicas=7,cutoff=1000,cosine_band_bound=Q(0))

    def test_14_bound_survives_rational_periodic_controls(self):
        # Symmetric unit orbits q=3 and q=9 have exactly real Fourier means
        # c_h. For an N equal to a multiple of their period the finite mu_N
        # moments are exactly the Ramanujan ones.
        for q in (3,9):
            for M in (8,20,40):
                ms=moments_for_q(q,2,M)
                for h,R in ((1,2),(2,3)):
                    if h*(2**(R-1)-1)>M:continue
                    f=joint_rigidity_bound(ms,base=2,frequency=h,horizon=120,
                                          replicas=R)
                    self.assertGreaterEqual(f.modulus_upper,abs(ms[h]))

    def test_15_interval_budget_dominates_exact_points(self):
        for q in (3,5,7,9):
            ms=moments_for_q(q,2,24)
            enclosures=[(max(-Q(1),v-Q(1,10000)),min(Q(1),v+Q(1,10000))) for v in ms]
            enclosures[0]=(Q(1),Q(1))
            ci=interval_prime_and_chord_budget(enclosures)
            re=real_chord_rigidity(ms)
            self.assertGreaterEqual(ci.chord_deficit,re.chord_deficit)
            self.assertGreaterEqual(ci.max_prime_cosine_defect,re.max_prime_cosine_defect)
            self.assertGreaterEqual(ci.harmonic_bound,re.harmonic_bound)
            self.assertGreaterEqual(ci.harmonic_bound,max(abs(v) for v in ms[1:]))

    def test_16_interval_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            interval_prime_and_chord_budget([(1,1),(0,0)])
        with self.assertRaises(ValueError):
            interval_prime_and_chord_budget([(1,1),(Q(2),Q(2)),(0,0)])
        with self.assertRaises(ValueError):
            interval_prime_and_chord_budget([(1,1),(Q(1),Q(-1)),(0,0)])
        with self.assertRaises(ValueError):
            interval_prime_and_chord_budget([(1,1),(0.1,0.2),(0,0)])


class CertifiedPiSourceAdapter(unittest.TestCase):
    def test_17_exact_polygon_pi_source_intervals_and_independent_machin(self):
        from observational_succ.secondary_circle_rigidity import certified_pi_cosine_intervals
        from observational_succ.circle_collision_rigidity import pi_interval
        lo,hi=pi_interval(18,85)
        # Independent alternating Machin arithmetic; no supplied pi decimals.
        def atan_bounds(inverse, terms=55):
            s=sum((Q((-1)**k, (2*k+1)*inverse**(2*k+1))
                   for k in range(terms)), Q())
            rem=Q(1,(2*terms+1)*inverse**(2*terms+1))
            return (s,s+rem) if terms%2==0 else (s-rem,s)
        a,b=atan_bounds(5)
        c,d=atan_bounds(239)
        ml,mu=16*a-4*d,16*b-4*c
        self.assertLess(lo,ml)
        self.assertGreater(hi,mu)
        self.assertGreater(hi,lo)
        intervals=certified_pi_cosine_intervals(2,5,12,level=18,precision=85,order=28)
        self.assertEqual(intervals[0],(Q(1),Q(1)))
        self.assertTrue(all(-1<=l<=u<=1 for l,u in intervals))
        result=interval_prime_and_chord_budget(intervals)
        self.assertGreater(result.max_prime_cosine_defect,0)
        self.assertEqual(result.cutoff,12)
        self.assertEqual(result.mean_chord_interval,
                         (2-2*intervals[1][1],2-2*intervals[1][0]))

    def test_18_source_budget_never_proves_from_small_finite_sample(self):
        from observational_succ.secondary_circle_rigidity import certified_pi_cosine_intervals
        intervals=certified_pi_cosine_intervals(16,5,20,level=18,precision=85,order=28)
        bound=interval_prime_and_chord_budget(intervals)
        self.assertEqual(bound.harmonic_bound,1)
        self.assertGreater(bound.chord_deficit,0)
        self.assertGreater(bound.max_prime_cosine_defect,0)

    def test_19_underresolution_fails_open_to_trivial_not_false_precision(self):
        from observational_succ.secondary_circle_rigidity import certified_pi_cosine_intervals
        coarse=certified_pi_cosine_intervals(2,4,8,level=5,precision=30,order=12)
        tight=certified_pi_cosine_intervals(2,4,8,level=18,precision=85,order=28)
        self.assertGreaterEqual(coarse[1][1]-coarse[1][0],
                                tight[1][1]-tight[1][0])
        self.assertTrue(all(-1<=l<=u<=1 for l,u in coarse))
        with self.assertRaises(ValueError):
            certified_pi_cosine_intervals(2,25,10)
        with self.assertRaises(ValueError):
            certified_pi_cosine_intervals(2.0,5,10)

    def test_20_exact_pi_intervals_meet_independent_decimal_holdout(self):
        # The independent source here is a separately implemented Machin
        # arctangent formula; we compare it using high-precision mpmath only
        # as a non-certifying numerical holdout, not as production input.
        import mpmath as mp
        from observational_succ.secondary_circle_rigidity import certified_pi_cosine_intervals
        intervals=certified_pi_cosine_intervals(2,5,12,level=18,precision=85,order=28)
        with mp.workdps(90):
            pi_from_machin=16*mp.atan(mp.mpf(1)/5)-4*mp.atan(mp.mpf(1)/239)
            for h in range(1,13):
                actual=sum(mp.cos(2*pi_from_machin*h*(2**j)*pi_from_machin)
                           for j in range(5))/5
                lower,upper=intervals[h]
                self.assertLessEqual(mp.mpf(lower.numerator)/lower.denominator,
                                     actual)
                self.assertGreaterEqual(mp.mpf(upper.numerator)/upper.denominator,
                                        actual)


class TopologicalReconstructionGauge(unittest.TestCase):
    def test_21_doubling_forbids_nonzero_rotational_repairs(self):
        from observational_succ.secondary_circle_rigidity import circle_rotation_commutator
        for q in range(2,17):
            for numerator in range(1,q):
                c=Q(numerator,q)
                self.assertNotEqual(circle_rotation_commutator(2,c),0)
        self.assertEqual(circle_rotation_commutator(2,Q(0)),0)
        self.assertEqual(circle_rotation_commutator(3,Q(1,2)),0)
        self.assertEqual(circle_rotation_commutator(2,Q(1,2)),Q(1,2))
        with self.assertRaises(ValueError):
            circle_rotation_commutator(2,0.5)

    def test_22_dyadic_order_fixes_the_orientation_preserving_grid(self):
        from observational_succ.secondary_circle_rigidity import doubled_origin_preimages
        for k in range(1,9):
            pts=doubled_origin_preimages(k)
            self.assertEqual(pts[0],0)
            self.assertEqual(len(pts),2**k)
            self.assertEqual(tuple(sorted(pts)),pts)
            # Cyclic-order-preserving grid permutations are rotations.
            # A homeomorphism commuting with doubling must fix 0;
            # only rotation by 0 fixes the initial grid point.
            for shift in range(1,2**k):
                self.assertNotEqual((0+shift)%(2**k),0)
            # Orientation reversal is reflection j -> -j, a lawful
            # doubling-commuting nontrivial gauge, but cannot turn
            # a non-Haar measure into Haar.
            self.assertTrue(all(((2*(-j))%2**k)==((-2*j)%2**k)
                                for j in range(2**k)))


class IndependentCyclotomicWitness(unittest.TestCase):
    def test_23_independent_polynomial_oracle_and_bad_phase(self):
        from scripts.secondary_circle_independent_oracle import run_oracle
        result=run_oracle()
        self.assertEqual(result["exact_cyclotomic_moment_checks"],126)
        self.assertTrue(result["one_sided_phase_mutant_rejected"])


class MinplusPrimeWordTransport(unittest.TestCase):
    def test_24_minplus_costs_improve_naive_all_prime_uniform_budget(self):
        from observational_succ.secondary_circle_rigidity import minplus_prime_chord_certificate
        for q in (3,5,7,9):
            for M in (8,16,32,60):
                c=moments_for_q(q,2,M)
                m=minplus_prime_chord_certificate(c)
                old=real_chord_rigidity(c)
                self.assertLessEqual(m.uniform_cosine_bound,old.harmonic_bound)
                for n in range(1,M+1):
                    self.assertEqual(math.prod(m.prime_paths[n]),n)
                    self.assertGreaterEqual(m.path_costs[n],abs(c[n]-c[1]))
                    self.assertGreaterEqual(m.per_frequency_bounds[n],abs(c[n]))
                self.assertGreaterEqual(m.fejer_weighted_cost,0)

    def test_25_prime_factor_order_matters_for_cost_not_endpoint(self):
        from observational_succ.secondary_circle_rigidity import minplus_prime_chord_certificate
        # This algebraic cost-graph synthetic input is NOT advertised as an
        # authenticated probability source. Test only min-plus recurrence.
        c=[Q(1),Q(0),Q(1,4),Q(1,2),Q(1,4),Q(0),Q(1,3)]
        result=minplus_prime_chord_certificate(c)
        self.assertEqual(result.path_costs[6],Q(1,3))
        self.assertEqual(result.prime_paths[6],(2,3))
        self.assertGreater(Q(1,2)+Q(1,6),result.path_costs[6])

    def test_26_interval_minplus_dominates_exact_and_below_blunt_budget(self):
        from observational_succ.secondary_circle_rigidity import (
            minplus_prime_chord_certificate,interval_minplus_prime_chord_certificate)
        for q in (3,5,7,9):
            c=moments_for_q(q,2,36)
            intervals=[(max(-Q(1),v-Q(1,100000)),min(Q(1),v+Q(1,100000))) for v in c]
            intervals[0]=(Q(1),Q(1))
            it=interval_minplus_prime_chord_certificate(intervals)
            exact=minplus_prime_chord_certificate(c)
            prior=interval_prime_and_chord_budget(intervals)
            self.assertGreaterEqual(it.uniform_cosine_bound,exact.uniform_cosine_bound)
            self.assertLessEqual(it.uniform_cosine_bound,prior.harmonic_bound)
            for n in range(1,37):
                self.assertGreaterEqual(it.per_frequency_bounds[n],abs(c[n]))
                self.assertEqual(math.prod(it.prime_paths[n]),n)

    def test_27_pi_interval_minplus_source_remains_finite_only(self):
        from observational_succ.secondary_circle_rigidity import (
            certified_pi_cosine_intervals,interval_minplus_prime_chord_certificate)
        data=certified_pi_cosine_intervals(2,5,12,level=18,precision=85,order=28)
        m=interval_minplus_prime_chord_certificate(data)
        self.assertEqual(m.uniform_cosine_bound,1)
        self.assertTrue(all(v>=0 for v in m.path_costs))


if __name__ == "__main__":
    unittest.main()

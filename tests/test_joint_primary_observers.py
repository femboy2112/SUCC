"""Independent exact oracles and calibrated failures for joint observers."""

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, prod
import unittest

from observational_succ.joint_primary_observers import (
    bbp_joint_primary_certificate, carrier_sampling_obstruction,
    circle_distance, congruence_separation, escaping_prime_history,
    independent_marginal_phase_law, interval_residue_tv, joint_primary_fiber,
    joint_primary_phases, phase_law, primary_fiber_points, primary_phase,
    prime_support, short_arc_crt_control, temporal_mixed_phase_law,
    source_matching_prime_escape,
)
from observational_succ.source_path_projector import character_sum


def direct_primary(x, p):
    """Enumerate the p-power subgroup, selecting the unique p-integral error."""
    part, rest = 1, x.denominator
    while rest % p == 0:
        part *= p
        rest //= p
    matches = [Q(j, part) for j in range(part)
               if (x-Q(j, part)).denominator % p]
    if len(matches) != 1:
        raise AssertionError("primary oracle was not unique")
    return matches[0]


def literal_states(n):
    result = []
    state = Q()
    for j in range(1, n+1):
        forcing = Q(4, 8*j-7)-Q(2, 8*j-4)-Q(1, 8*j-3)-Q(1, 8*j-2)
        state = 16*state+forcing
        result.append(state)
    return tuple(result)


def exact_character(law, modulus):
    return character_sum(modulus,
                         tuple(int(x*modulus) for x, _ in law),
                         tuple(weight for _, weight in law))


class PrimaryReconstruction(unittest.TestCase):
    def test_projection_against_independent_subgroup_search(self):
        for denominator in range(1, 45):
            for numerator in range(-3, 2*denominator+1):
                x = Q(numerator, denominator)
                for p in (2, 3, 5, 7):
                    self.assertEqual(primary_phase(x, p), direct_primary(x, p))

    def test_full_joint_reconstruction_additivity_and_integer_lift_boundary(self):
        for denominator in (15, 21, 45, 77, 105):
            ps = prime_support(denominator)
            for a in range(denominator):
                x = Q(a, denominator)
                self.assertEqual(sum(joint_primary_phases(x, ps), Q()) % 1, x)
                self.assertEqual(joint_primary_phases(x+3, ps),
                                 joint_primary_phases(x, ps))
                for p in ps:
                    self.assertEqual(primary_phase(x+Q(2, denominator), p),
                                     (primary_phase(x, p)+primary_phase(Q(2, denominator), p)) % 1)

    def test_exact_fibers_against_full_carrier_enumeration(self):
        for D in (6, 15, 21, 45, 105):
            ps = prime_support(D)
            for k in range(len(ps)+1):
                for chosen in combinations(ps, k):
                    groups = defaultdict(list)
                    for a in range(D):
                        x = Q(a, D)
                        groups[joint_primary_phases(x, chosen)].append(x)
                    for observed, expected in groups.items():
                        pairs = tuple(zip(chosen, observed))
                        data = joint_primary_fiber(D, pairs)
                        self.assertEqual(primary_fiber_points(D, pairs), tuple(expected))
                        self.assertEqual(data["fiber_size"], len(expected))
                        self.assertEqual(data["complete"], len(expected) == 1)

    def test_sharp_real_radius_against_all_breakpoint_midpoints(self):
        # A piecewise-linear max-distance objective attains its minimum
        # at one of these grid/antipodal crossing midpoints.
        for R in range(1, 40):
            xs = tuple(Q(j, R) for j in range(R))
            oracle = min(max(circle_distance(x-Q(j, 2*R)) for x in xs)
                         for j in range(2*R))
            self.assertEqual(oracle, Q(R-1, 2*R))
            if R > 1:
                self.assertGreaterEqual(oracle, Q(1, 4))

    def test_large_observed_modulus_does_not_make_last_missing_prime_small(self):
        D = 3**20*101
        data = joint_primary_fiber(D, ((3, Q(1, 3**20)),))
        self.assertEqual(data["observed_modulus"], 3**20)
        self.assertEqual(data["optimal_real_radius"], Q(50, 101))
        self.assertGreater(data["optimal_real_radius"], Q(49, 100))

    def test_carrier_empty_observers_and_extraneous_zero_prime(self):
        self.assertEqual(primary_fiber_points(1, ()), (Q(),))
        self.assertEqual(primary_fiber_points(15, ((7, 0),)),
                         tuple(Q(j, 15) for j in range(15)))

    def test_malformed_observers_and_unbounded_expansion_rejected(self):
        calls = (
            lambda: primary_phase(0.5, 3), lambda: primary_phase(1, 4),
            lambda: primary_phase(1, True),
            lambda: joint_primary_phases(Q(1, 15), (3, 3)),
            lambda: joint_primary_fiber(15, ((3, Q(1, 5)),)),
            lambda: joint_primary_fiber(15, ((3, Q(1, 9)),)),
            lambda: primary_fiber_points(20001, ()),
            lambda: joint_primary_fiber(15, ((3,),)),
        )
        for call in calls:
            with self.assertRaises(ValueError):
                call()


class JointTemporalCorrelations(unittest.TestCase):
    def test_genuine_coprime_primary_rows_differ_from_marginal_product(self):
        rows = tuple(joint_primary_phases(x, (3, 5)) for x in (Q(), Q(1, 15)))
        joint = temporal_mixed_phase_law(rows)
        separate = independent_marginal_phase_law(rows)
        self.assertEqual(joint, ((Q(), Q(1, 2)), (Q(1, 15), Q(1, 2))))
        self.assertNotEqual(joint, separate)
        self.assertNotEqual(exact_character(joint, 15), exact_character(separate, 15))

    def test_all_proper_uniform_marginals_do_not_fix_four_way_phase(self):
        # Binary parity law is a general joint-observation control, not
        # a claim that four copies of G_2 are disjoint primary subgroups.
        words = tuple(bits+(sum(bits) % 2,) for bits in product(range(2), repeat=3))
        for omitted in range(4):
            self.assertEqual(len(set(tuple(row[j] for j in range(4) if j != omitted)
                                     for row in words)), 8)
        rows = tuple(tuple(Q(bit, 2) for bit in row) for row in words)
        self.assertEqual(temporal_mixed_phase_law(rows), ((Q(), Q(1)),))
        self.assertEqual(independent_marginal_phase_law(rows),
                         ((Q(), Q(1, 2)), (Q(1, 2), Q(1, 2))))

    def test_factorization_holds_for_an_actual_full_product_sample(self):
        rows = tuple((Q(a, 3), Q(b, 5)) for a, b in product(range(3), range(5)))
        self.assertEqual(temporal_mixed_phase_law(rows), independent_marginal_phase_law(rows))

    def test_modular_interval_tv_against_all_residue_counts(self):
        for q in range(1, 33):
            for length in range(1, 4*q+2):
                counts = Counter(a % q for a in range(length))
                direct = sum((abs(Q(counts[a], length)-Q(1, q))
                              for a in range(q)), Q())/2
                self.assertEqual(interval_residue_tv(length, q), direct)
                self.assertLessEqual(direct, Q(q, 4*length))

    def test_short_arc_all_proper_crt_marginals_independently_enumerated(self):
        for moduli, length in (((5, 7, 11), 97), ((8, 9, 5), 107),
                              ((7, 13, 17), 411)):
            data = short_arc_crt_control(moduli, length)
            for row in data["proper_marginals"]:
                q = row["modulus"]
                counts = Counter(tuple(a % moduli[j] for j in row["indices"])
                                 for a in range(length))
                direct = (sum((abs(Q(count, length)-Q(1, q))
                               for count in counts.values()), Q())
                          + Q(q-len(counts), q))/2
                self.assertEqual(row["TV"], direct)
                self.assertLessEqual(direct, data["all_proper_TV_upper_bound"])
            self.assertEqual(data["full_joint_TV"], 1-Q(length, prod(moduli)))

    def test_joint_law_guards(self):
        for rows in ((), ((),), ((0,), (0, 1)), ((0.5,),)):
            with self.assertRaises(ValueError):
                temporal_mixed_phase_law(rows)
        with self.assertRaises(ValueError):
            short_arc_crt_control((6, 9), 2)
        with self.assertRaises(ValueError):
            short_arc_crt_control((3, 5), 16)


class CarrierResolutionAndHeight(unittest.TestCase):
    def test_full_resolution_tv_and_collision_against_expanded_uniform(self):
        for D in (1, 5, 9, 15):
            for n in (1, 4, 17):
                points = tuple(Q((j*j+2*j) % D, D) for j in range(n))
                data = carrier_sampling_obstruction(points, D)
                counts = Counter(points)
                direct = sum((abs(Q(counts[Q(a, D)], n)-Q(1, D))
                              for a in range(D)), Q())/2
                self.assertEqual(data["total_variation_to_uniform_carrier"], direct)
                self.assertGreaterEqual(direct, data["sample_TV_lower_bound"])
                self.assertGreaterEqual(data["scaled_collision"], data["collision_lower_bound"])

    def test_wrong_carrier_and_empty_samples_rejected(self):
        with self.assertRaises(ValueError):
            carrier_sampling_obstruction((Q(1, 7),), 15)
        with self.assertRaises(ValueError):
            carrier_sampling_obstruction((), 15)

    def test_joint_valuation_grid_against_brute_numerators(self):
        for D, bounds in ((45, ((3, 0), (5, -1))),
                          (35, ((2, 3), (5, 0))),
                          (15, ((3, -2), (7, 1)))):
            result = congruence_separation(D, bounds)
            M = result["numerator_multiple"]
            allowed = []
            for numerator in range(1, 2*M+1):
                x = Q(numerator, D)
                ok = True
                for p, lower in bounds:
                    a, b, valuation = x.numerator, x.denominator, 0
                    while a % p == 0:
                        a //= p
                        valuation += 1
                    while b % p == 0:
                        b //= p
                        valuation -= 1
                    ok &= valuation >= lower
                if ok:
                    allowed.append(x)
            self.assertEqual(allowed[0], result["nonzero_absolute_separation"])
            self.assertEqual(allowed, [Q(M, D), Q(2*M, D)])

    def test_carry_must_be_included_in_the_valuation_condition(self):
        x = Q(16, 15)
        self.assertEqual(x.numerator % 16, 0)
        nearest_residual = x-1
        self.assertEqual(nearest_residual, Q(1, 15))
        self.assertNotEqual(nearest_residual.numerator % 16, 0)
        self.assertEqual(congruence_separation(15, ((2, 4),))["nonzero_absolute_separation"], x)


class MovingPrimeAndAuthenticControls(unittest.TestCase):
    def test_source_matching_escape_preserves_all_authentic_supported_phases(self):
        for C in (Q(1), Q(1, 3)):
            rows = source_matching_prime_escape(C, 40)["rows"]
            for row in rows:
                n, p, q = row["n"], row["prime"], row["new_prime_denominator"]
                self.assertGreater(p, 16*n)
                self.assertLess(p, 32*n)
                self.assertEqual(row["state"].denominator, row["original_denominator"]*q)
                for local in range(2, 8*n+1):
                    if len(prime_support(local)) == 1 and prime_support(local)[0] == local:
                        self.assertEqual(primary_phase(row["state"], local),
                                         primary_phase(row["original_state"], local))
                        self.assertEqual(primary_phase(row["forcing"], local),
                                         primary_phase(row["original_forcing"], local))
                self.assertNotEqual(primary_phase(row["state_difference"], p), 0)
                self.assertLessEqual(row["tail_lower"], row["tail"])
                self.assertLess(row["tail"], row["tail_upper"])
                self.assertLessEqual(row["tail_upper"], row["uniform_tail_upper"])
                if n >= 2:
                    self.assertGreater(row["forcing"], 0)

    def test_source_matching_escape_improves_absolute_local_precision(self):
        rows = source_matching_prime_escape(Q(1, 3), 65)["rows"]
        for row in rows[31:]:
            for p, power in ((2, 3), (3, 1), (5, 1)):
                for name in ("state_difference", "forcing_difference"):
                    value = row[name]
                    self.assertNotEqual(value.denominator % p, 0)
                    self.assertEqual(value.numerator % p**power, 0)

    def test_fixed_pascal_orders_eventually_match_local_valuation(self):
        rows = source_matching_prime_escape(Q(1, 3), 70)["rows"]
        for order, valuation in ((1, 0), (2, 2), (3, 3)):
            for start in (63, 64, 65):
                for original, changed in (("original_state", "state"),
                                          ("original_forcing", "forcing")):
                    a = sum(((-1)**(order-j)*comb(order, j)*rows[start+j-1][original]
                             for j in range(order+1)), Q())
                    b = sum(((-1)**(order-j)*comb(order, j)*rows[start+j-1][changed]
                             for j in range(order+1)), Q())
                    self.assertEqual(a.denominator % 2, 1)
                    self.assertEqual(b.denominator % 2, 1)
                    self.assertEqual(a.numerator % 2**(valuation+1), 2**valuation)
                    self.assertEqual(b.numerator % 2**(valuation+1), 2**valuation)
                    self.assertEqual((a-b).numerator % 2**(valuation+1), 0)

    def test_moving_prime_controls_keep_height_decay_and_eventual_local_zero(self):
        for b, C in ((2, Q(1)), (3, Q(1, 2)), (16, Q(1, 3)), (5, Q(1, 4))):
            data = escaping_prime_history(C, 24, b)
            rows = data["rows"]
            observed = tuple(row["prime"] for row in rows[:4])
            prior = Q()
            for row in rows:
                n = row["n"]
                self.assertEqual(row["state"], b*prior+row["forcing"])
                self.assertEqual(row["state"].denominator, row["denominator"])
                self.assertGreaterEqual(row["denominator"], 32**n)
                self.assertLess(row["denominator"], 2*64**n)
                self.assertLessEqual(row["tail_lower"], row["tail"])
                self.assertLess(row["tail"], row["tail_upper"])
                self.assertLessEqual(row["tail_upper"], row["uniform_tail_upper"])
                self.assertEqual(row["state"].numerator % row["numerator_multiple"], 0)
                if n >= 2:
                    self.assertGreater(row["forcing"], 0)
                if n > 4:
                    self.assertEqual(joint_primary_phases(row["state"], observed), (Q(),)*4)
                prior = row["state"]

    def test_absolute_local_precision_grows_for_every_fixed_prime(self):
        rows = escaping_prime_history(Q(1, 3), 65)["rows"]
        for row in rows[30:]:
            # m_n>=5, so m_n! is divisible by 2^3, 3 and 5.
            for p, power in ((2, 3), (3, 1), (5, 1)):
                self.assertNotEqual(row["state"].denominator % p, 0)
                self.assertEqual(row["state"].numerator % p**power, 0)

    def test_same_fixed_local_limit_and_different_real_clustering_centers(self):
        left = escaping_prime_history(1, 30)["rows"]
        right = escaping_prime_history(Q(1, 3), 30)["rows"]
        for rows, center in ((left, Q()), (right, Q(1, 3))):
            observed = tuple(row["prime"] for row in rows[:4])
            self.assertTrue(all(joint_primary_phases(row["state"], observed) == (Q(),)*4
                                for row in rows[4:]))
            self.assertLess(circle_distance(rows[-1]["phase"]-center), Q(1, 900))
        self.assertGreater(circle_distance(left[-1]["phase"]-right[-1]["phase"]), Q(3, 10))

    def test_authentic_states_against_independent_literal_four_poles(self):
        for n in (1, 3, 7, 17, 31):
            data = bbp_joint_primary_certificate(n)
            literal = literal_states(n)
            self.assertEqual(data["individual_denominators_d_n"],
                             tuple(x.denominator for x in literal))
            self.assertEqual(data["reconstructed_phases"], tuple(x % 1 for x in literal))
            D = data["common_carrier_D_N"]
            self.assertTrue(all(D % x.denominator == 0 for x in literal))
            self.assertGreater(data["sampling_obstruction"]["sample_TV_lower_bound"], Q(1, 2))

    def test_complete_observers_preserve_phase_but_not_lift(self):
        data = bbp_joint_primary_certificate(3)
        source = literal_states(3)
        ps = data["prime_support"]
        self.assertEqual(joint_primary_phases(source[-1]+1, ps), data["source_rows"][-1])
        self.assertNotEqual(source[-1]+1, source[-1])


if __name__ == "__main__":
    unittest.main()

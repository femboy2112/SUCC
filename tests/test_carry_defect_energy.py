"""Independent rational solves, all-center controls, and source mutations."""
from collections import Counter
from fractions import Fraction as Q
import unittest

from observational_succ import carry_defect_energy as c
from observational_succ.pi_succ_character_intervals import fourier_squared_interval


def invert(matrix):
    n = len(matrix)
    rows = [list(row)+[Q(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = rows[i][i]
        rows[i] = [x/pivot for x in rows[i]]
        for j in range(n):
            if i != j:
                factor = rows[j][i]
                rows[j] = [x-factor*y for x, y in zip(rows[j], rows[i])]
    return tuple(tuple(row[n:]) for row in rows)


def trajectory(seed, forcing):
    values = [Q(seed)]
    for r in forcing:
        values.append(16*values[-1]+r)
    return tuple(values)


def circular_cost(phases, center):
    offsets = tuple(c.fractional_part(x-center+Q(1, 2))-Q(1, 2) for x in phases)
    return sum((x*x for x in offsets), Q())


class GreenKernelTests(unittest.TestCase):
    def test_closed_kernel_against_independent_gauss_jordan(self):
        for t in (1, 2, 3, 5, 8, 13):
            matrix = tuple(tuple(Q(257 if i == j else -16 if abs(i-j) == 1 else 0)
                                 for j in range(t)) for i in range(t))
            self.assertEqual(c.green_kernel(t), invert(matrix))

    def test_green_decomposition_and_both_endpoint_coefficients(self):
        for t in (1, 4, 9, 16):
            q = tuple(Q((7*i+3) % 19-9, 37) for i in range(t+1))
            result = c.green_energy(q)
            norm = sum((x*x for x in q), Q())
            a = tuple(q[i+1]-16*q[i] for i in range(t))
            self.assertEqual(result.squared_norm, norm)
            self.assertEqual(norm, result.signed_forcing_energy
                             + result.homogeneous_boundary_energy)
            self.assertEqual(result.weighted_endpoint_remainder,
                             289*norm-17*q[0]**2-272*q[-1]**2
                             -sum((x*x for x in a), Q()))
        # The signed recurrence has an adjacent SUM remainder. A copied
        # adjacent-difference remainder from the unsigned norm proof is false.
        self.assertNotEqual(result.weighted_endpoint_remainder,
                            16*sum(((q[i+1]-q[i])**2 for i in range(t)), Q()))

    def test_outgoing_homogeneous_boundary_cannot_be_erased(self):
        q = tuple(Q(16**i, 10*16**7) for i in range(8))
        result = c.green_energy(q)
        self.assertEqual(result.signed_forcing_energy, 0)
        self.assertGreater(result.homogeneous_boundary_energy, 0)
        self.assertEqual(result.squared_norm, result.homogeneous_boundary_energy)

    def test_signed_cross_terms_cannot_be_replaced_by_absolute_values(self):
        def backward(a):
            q = [Q()]
            for x in reversed(a):
                q.append((q[-1]-x)/16)
            return tuple(reversed(q))
        plus = c.green_energy(backward((Q(1), Q(1)))).signed_forcing_energy
        minus = c.green_energy(backward((Q(1), Q(-1)))).signed_forcing_energy
        self.assertLess(minus, plus)
        self.assertEqual(plus-minus, 4*c.green_kernel(2)[0][1])


class AllCenterTests(unittest.TestCase):
    def test_all_cuts_against_independent_mean_candidate_oracle(self):
        for phases in ((Q(), Q(1, 3), Q(4, 7)),
                       (Q(1, 5), Q(1, 5), Q(7, 8), Q(2, 9)),
                       (Q(), Q(1, 2)), (Q(1, 7),)*4):
            forcing = tuple(phases[i+1]-16*phases[i] for i in range(len(phases)-1))
            cert = c.all_center_certificate(phases, forcing)
            # At a smooth quadratic minimum theta=(sum phases+integer)/L.
            # Include every cut as well, independently of the cut sweep.
            candidates = [c.fractional_part((sum(phases, Q())+j)/len(phases))
                          for j in range(len(phases))]
            candidates += [c.fractional_part(x+Q(1, 2)) for x in phases]
            self.assertEqual(cert.circular_squared_distance,
                             min(circular_cost(phases, x) for x in candidates))
            self.assertEqual(sum((cut.right-cut.left for cut in cert.cuts), Q()), 1)
            for cut in cert.cuts:
                self.assertEqual(cut.minimum_squared_distance,
                                 circular_cost(phases, cut.minimizing_center))

    def test_exact_count_inequality_and_local_cut_updates(self):
        forcing = (Q(),)*15
        cert = c.all_center_certificate(trajectory(Q(1, 255), forcing), forcing)
        self.assertGreater(cert.minimum_nonmodal_count, 0)
        for cut in cert.cuts:
            counts = Counter(cut.integer_branches)
            direct_pairs = sum(x != y for i, x in enumerate(cut.integer_branches)
                               for y in cut.integer_branches[i+1:])
            self.assertEqual(cut.unequal_pairs, direct_pairs)
            self.assertGreaterEqual(2*cut.unequal_pairs,
                                    cert.transitions*cut.nonmodal_count)
            self.assertEqual(cut.nonmodal_count, cert.transitions-max(counts.values()))
        # Distinct phases give a single-state crossing: +1 to its incoming
        # branch and -16 to its outgoing branch, not the opposite signs.
        phases = (Q(1, 11), Q(3, 11), Q(7, 11), Q(10, 11))
        forcing = tuple(phases[i+1]-16*phases[i] for i in range(3))
        cert = c.all_center_certificate(phases, forcing)
        for old, new in zip(cert.cuts, cert.cuts[1:]):
            delta_b = tuple(y-x for x, y in zip(old.lifted_phases, new.lifted_phases))
            self.assertEqual(sum(delta_b), 1)
            self.assertEqual(tuple(y-x for x, y in zip(old.integer_branches,
                                                       new.integer_branches)),
                             tuple(delta_b[i+1]-16*delta_b[i] for i in range(3)))

    def test_original_poles_negative_frequency_and_certified_signed_holdouts(self):
        for start, t, h in ((4, 7, 1), (11, 9, -3), (23, 12, 7)):
            states, forcing = c.authentic_window(start, t)
            c.authenticate_window(states, forcing, start)
            cert = c.all_center_certificate(states, forcing, h)
            for i, r in enumerate(forcing):
                n = start+i+1
                literal = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
                self.assertEqual(r, literal)
            _, upper = fourier_squared_interval(states, h)
            for lower in (cert.modal_loss_lower, cert.pair_loss_lower,
                          cert.quadratic_loss_lower):
                self.assertLessEqual(upper, (1-lower/len(states))**2)
            chosen = min(cert.cuts, key=lambda x: x.minimum_squared_distance)
            offsets = tuple(x-chosen.minimizing_center for x in chosen.lifted_phases)
            self.assertEqual(c.green_energy(offsets).squared_norm,
                             cert.circular_squared_distance)

    def test_changed_seed_and_pole_mutations_have_distinct_failures(self):
        states, forcing = c.authentic_window(9, 6)
        changed = tuple(x+Q(16**i, 7) for i, x in enumerate(states))
        c.all_center_certificate(changed, forcing)  # all recurrences survive
        with self.assertRaises(ValueError):
            c.authenticate_window(changed, forcing, 9)
        mutated = (forcing[0]+Q(1, 13),)+forcing[1:]
        with self.assertRaises(ValueError):
            c.all_center_certificate(states, mutated)
        repaired_states = trajectory(states[0], mutated)
        c.all_center_certificate(repaired_states, mutated)
        with self.assertRaises(ValueError):
            c.authenticate_window(repaired_states, mutated, 9)

    def test_zero_periodic_and_high_harmonic_controls(self):
        forcing = (Q(),)*12
        zero = c.all_center_certificate(trajectory(0, forcing), forcing)
        self.assertEqual(zero.minimum_nonmodal_count, 0)
        self.assertEqual(zero.quadratic_loss_lower, 0)
        periodic_states = trajectory(Q(1, 255), forcing)
        periodic = c.all_center_certificate(periodic_states, forcing, 255)
        self.assertEqual(periodic.minimum_nonmodal_count, 0)
        self.assertEqual(periodic.quadratic_loss_lower, 0)

    def test_quadratic_instrument_ceiling_on_equispaced_phases(self):
        for length in (3, 4, 7, 12):
            phases = tuple(Q(i, length) for i in range(length))
            forcing = tuple(phases[i+1]-16*phases[i] for i in range(length-1))
            cert = c.all_center_certificate(phases, forcing)
            self.assertEqual(cert.circular_squared_distance,
                             Q(length*length-1, 12*length))
            self.assertLess(cert.quadratic_loss_lower, Q(2*length, 3))

    def test_strict_domains(self):
        for call in (lambda: c.green_kernel(True), lambda: c.green_kernel(0),
                     lambda: c.green_kernel(129), lambda: c.green_energy((0.0, 1)),
                     lambda: c.authentic_window(-1, 4),
                     lambda: c.all_center_certificate((0, 0), (0,), False),
                     lambda: c.all_center_certificate((0, 0), (0,), 0)):
            with self.assertRaises(ValueError):
                call()


if __name__ == '__main__':
    unittest.main()

"""Exact adversarial checks for the separate Round-2 paper proofs.

These finite checks do not certify pi normality or execute the normal-carrier
existence construction. All numerical phase comparisons use rational bounds.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
import importlib.util
from math import gcd, isqrt
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


f = module('pi_prime7_source_fiber_probe')
d = module('pi_full_source_delay_probe')
g = module('pi_gaussian_descent_probe')
a = module('pi_prime7_exact_theorem_probe')


class AuthenticSourceAndSignedFibers(unittest.TestCase):
    def test_exact_resultants_and_denominator_reflection(self):
        r = f.source_algebra()
        self.assertEqual(r['resultant_A_D'], -7372800)
        self.assertEqual(r['discriminant_D'], 3774873600)
        self.assertEqual(r['homogeneous_resultant'], -1932735283200)

    def test_zero_seed_matches_native_source_at_fresh_inputs(self):
        from observational_succ.bbp_binwindow_conjugacy import source_verified
        U = f.authentic_states(83)
        self.assertEqual(U[0], 0)
        for n in (1, 2, 19, 37, 83):
            self.assertEqual(U[n] - 16 * U[n-1], source_verified(n))

    def test_authentic_signed_mirror_has_both_signs(self):
        _, pairs = f.geometry(7, 1)
        U = f.authentic_states(55)
        rows = [f.energy_row([f.phase(h*u) for u in U], 7, 1, pairs) for h in (1, 2)]
        self.assertLess(rows[0]['offdiag'][1], 0)
        self.assertGreater(rows[1]['offdiag'][0], 0)

    def test_prime_power_mixed_strata_cannot_be_deleted(self):
        _, pairs = f.geometry(7, 2)
        self.assertTrue(any(r != s and (120*(r+s)-89) % 49 for r, s in pairs))
        row = f.gaussian_identity(7, 2, pairs)
        self.assertNotEqual(Q(row['mixed_strata_offdiag']), 0)
        self.assertEqual(Q(row['C']), Q(row['E']) + Q(row['offdiag']))

    def test_phase_reduction_and_future_tail_remainder(self):
        self.assertEqual(f.phase(Q(17, 29)), f.phase(10**10000 + Q(17, 29)))
        for n in (0, 1, 17, 353):
            lo, hi = f.changed_tail_interval(n)
            longer = sum((f.forcing(n+j) / 16**j for j in range(1, 25)), Q(0))
            self.assertLess(lo, longer)
            self.assertLess(longer, hi)


class FullSourceDelay(unittest.TestCase):
    def test_poles_are_present_in_projective_source(self):
        self.assertEqual([d.source(x, 7, 2) for x in (0, 2, 3, 4)],
                         [(1, f.D(x) * pow(f.A(x), -1, 49) % 49) for x in (0, 2, 3, 4)])
        self.assertEqual(d.collisions(d.collision_groups(7, 1, 1)), 19)
        self.assertNotEqual(19, 13)  # Numerator count is a different statistic.

    def test_two_delay_counterexample_persists_and_three_resolves_it(self):
        for L, pair in ((1, [2, 3]), (2, [24, 30]), (3, [220, 324])):
            groups = d.collision_groups(7, L, 2)
            self.assertEqual([cell for cell in groups if len(cell) > 1], [pair])
            self.assertEqual(d.collisions(d.collision_groups(7, L, 3)), 7**L)

    def test_source_critical_points_and_holdout_charts(self):
        for p, critical in ((7, [1, 5]), (11, [1]), (241, [152])):
            self.assertEqual([x for x in range(p) if d.derivative(x, p) == 0], critical)
            self.assertTrue(all(d.derivative(x, p) or d.derivative(x+1, p) for x in range(p)))
        self.assertEqual(d.source(152, 241, 1), (0, 0))
        self.assertEqual(d.collisions(d.collision_groups(241, 1, 2)), 241)

    def test_signed_exception_identity_with_incomplete_time_blocks(self):
        for N in (1, 8, 53, 101):
            q = 49
            z = a.integer_gaussian_phases(N, 1)
            Z = a.binned_sums(z, q, 'time')
            groups = d.collision_groups(7, 2, 2)
            raw = sum(a.norm(tuple(sum(Z[x][k] for x in cell) for k in range(2))) for cell in groups)
            off = 2 * sum(Z[24][k] * Z[30][k] for k in range(2))
            self.assertEqual(raw, sum(map(a.norm, Z)) + off)


class ArithmeticCalibration(unittest.TestCase):
    def test_cyclotomic_mirror_zero_and_nonzero_first_depth(self):
        rows = a.prime7_character_certificates()
        for row in rows:
            self.assertEqual(row['normalized_fiber_energy'], '3/7' if row['L'] == 1 else '2/7')
            self.assertEqual(row['mirror_cyclotomic_remainder'], {'0': 1} if row['L'] == 1 else {})

    def test_refinement_is_exact_even_for_empty_and_unbalanced_bins(self):
        rows = a.refinement_certificates()
        self.assertEqual(len(rows), 80)
        self.assertTrue(all(Q(row['fine_energy']) - Q(row['coarse_energy']) ==
                            Q(row['child_difference_energy']) >= 0 for row in rows))

    def test_retaining_complete_fibers_controls_the_operator_norm(self):
        rows = a.truncated_kernel_certificates()
        self.assertEqual(len(rows), 12)
        for row in rows:
            self.assertEqual(row['operator_norm'], 2 * row['p']**row['S'])
            self.assertEqual(Q(row['trace_over_q']), 1-Q(1, row['p']**(row['S']+1)))

    def test_globally_canceled_character_has_nondecaying_fiber_energy(self):
        for p, L in ((7, 1), (7, 3), (11, 2), (241, 1)):
            q = p**L
            remainder = a.cyclotomic_remainder([gcd(u, q) for u in range(q)], p, L)
            self.assertEqual(remainder, [q-q//p]+[0]*(len(remainder)-1))

    def test_fiber_energy_need_not_contract_fine_energy(self):
        q = 49
        cells = defaultdict(list)
        for x in range(q):
            cells[f.A(x) % q].append(x)
        largest = max(cells.values(), key=len)
        # Two periods of unit phases realize Z=2 on one fiber and zero elsewhere.
        Z = [2 if x in largest else 0 for x in range(q)]
        fine = sum(v*v for v in Z)
        coarse = sum(sum(Z[x] for x in cell)**2 for cell in cells.values())
        self.assertEqual(coarse, len(largest)*fine)
        self.assertGreater(coarse, fine)

    def test_local_character_cofactor_is_not_optional(self):
        for u in (Q(1, 2), Q(47, 15), Q(-103, 17)):
            for L in (1, 2, 4):
                q = 7**L
                R = u.numerator * pow(u.denominator, -1, q) % q
                K = (u.denominator*R-u.numerator)//q
                self.assertEqual(u/q, Q(R, q)-Q(K, u.denominator))
                self.assertEqual(u, R-Q(q*K, u.denominator))
        self.assertNotEqual(Q(1, 2*7) % 1, Q(4, 7) % 1)


class GaussianDescentAndRealPhase(unittest.TestCase):
    def test_finite_descent_has_an_even_depth_defect(self):
        for m in range(1, 9):
            red, add, conj, psi, E = g.ring(m)
            rational = {red((x, 0)) for x in range(2**((m+1)//2))}
            fixed = {z for z in E if conj(z) == z}
            self.assertEqual(len(fixed), len(rational)*(2 if m % 2 == 0 else 1))
            self.assertEqual({psi(z) for z in rational}, rational)
        red, _, conj, _, _ = g.ring(2)
        self.assertEqual(conj(red((0, 1))), red((0, 1)))
        self.assertNotIn(red((0, 1)), {red((x, 0)) for x in range(2)})

    def test_all_gaussian_cycles_and_transverse_strata(self):
        report = g.run()
        self.assertEqual(report['rows'][-1], dict(m=12, size=4096, rational=64,
                                                fixed=128, cycles=64, cycle_length=64))

    def test_original_zero_state_and_repeated_clock_bins(self):
        U = f.authentic_states(64)
        for m in (2, 5, 8):
            red, _, _, psi, _ = g.ring(m)
            q = 2**((m+1)//2)
            self.assertEqual(psi(red((0, 0))), red((0, 0)))
            for n in range(q):
                self.assertEqual(psi(red((n, 0))), red((U[n].numerator*pow(U[n].denominator, -1, q), 0)))
                self.assertEqual(psi(red((n, 0))), psi(red((n+q, 0))))

    def test_uniform_in_frequency_phase_gap_witness(self):
        for h in (1, 2, 17, 241, 10**9+7, 10**30+37):
            n = isqrt(4*h)
            n += n*n < 4*h
            self.assertLess(Q(47, 4608), h*f.forcing(n))
            self.assertLess(h*f.forcing(n), Q(1, 4))
            self.assertGreater(4*h*f.forcing(n)/34, Q(47, 39168))

    def test_finite_horizon_phase_gap_is_certified(self):
        # m=4 gives rational-clock period 4. Source phases at a=1,b=5 differ.
        re, im = f.phase(f.forcing(1)-f.forcing(5))
        chord_squared = f.add(f.sq((re[0]-1, re[1]-1)), f.sq(im))
        self.assertGreater(chord_squared[0], 0)


if __name__ == '__main__':
    unittest.main()

"""Exact, independently aggregated controls for source collision research."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.pi_source_collision import (
    adversarial_complement, bbp_forcing, bbp_states, carry_collision_check,
    cell_collision, cell_counts, galois_collision_bounds,
    galois_collision_mean, order16, prime_window, small_ball_pairs, tail_upper,
)
from observational_succ.poisson_circle_minimal import (
    exact_energy, exact_point, exact_potential,
)


def brute_pairs(phases, radius):
    return sum(min((x-y) % 1, (y-x) % 1) <= radius
               for x in phases for y in phases)


def atan_bounds(denominator, terms):
    total = sum((Q((-1)**k, (2*k+1)*denominator**(2*k+1))
                 for k in range(terms)), Q(0))
    following = Q((-1)**terms, (2*terms+1)*denominator**(2*terms+1))
    return min(total, total+following), max(total, total+following)


def machin_bounds(terms):
    a, b = atan_bounds(5, terms), atan_bounds(239, terms)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def certified_pi_bins(start, length, cells, terms=120):
    lower, upper = machin_bounds(terms)
    result = []
    for n in range(start, start+length):
        lo = (cells*16**n*lower).__floor__()
        hi = (cells*16**n*upper).__floor__()
        if lo != hi:
            raise ValueError("Machin interval does not resolve this bin")
        result.append(lo % cells)
    return result


class SourceCollisionTests(unittest.TestCase):
    def test_source_initial_state_and_independent_finite_sum(self):
        source = bbp_states(40)
        self.assertEqual(source[0], 0)
        self.assertEqual(source[1], Q(2, 15))
        for n in range(1, 61):
            unified = Q(120*n*n-89*n+16,
                        (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(bbp_forcing(n), unified)
        for n in (1, 2, 7, 19, 40):
            direct = sum((16**(n-j)*bbp_forcing(j)
                          for j in range(1, n+1)), Q(0)) % 1
            self.assertEqual(source[n], direct)

    def test_first_birth_p_free_complement_and_exact_scope(self):
        for p in (17, 41, 73, 97, 113):
            w = prime_window(p)
            self.assertEqual(w.length, 3*(p-1)//8)
            self.assertEqual(w.start % w.period, 0)
            self.assertEqual(w.conjugate(1), w.states)
            self.assertTrue(all(c.denominator % p for c in w.complement))
            multiplicity = Counter(w.local)
            self.assertEqual(len(multiplicity), w.period)
            self.assertEqual(set(multiplicity.values()), {w.length//w.period})
            self.assertEqual(w.tail_bound, Q(1, (p+8)*(p+9)))

    def test_sorted_pair_algorithm_against_exhaustive_oracle(self):
        pool = (Q(0), Q(1, 12), Q(1, 2), Q(11, 12))
        for n in range(1, 5):
            for phases in product(pool, repeat=n):
                for radius in (Q(0), Q(1, 12), Q(1, 6), Q(5, 12)):
                    self.assertEqual(small_ball_pairs(phases, radius),
                                     brute_pairs(phases, radius))

    def test_galois_bounds_full_source_and_independent_pair_grid(self):
        for p in (17, 41, 73):
            w = prime_window(p)
            for radius in (Q(1, 4), Q(1, 16), Q(1, 64)):
                mean = galois_collision_mean(w, radius)
                numerator = 0
                for s in range(w.length):
                    for t in range(w.length):
                        shift = w.complement[s]-w.complement[t]
                        if w.local[s] == w.local[t]:
                            numerator += (p-1)*int(min(shift % 1, -shift % 1) <= radius)
                        else:
                            numerator += sum(min((Q(a,p)+shift) % 1,
                                                 (-Q(a,p)-shift) % 1) <= radius
                                             for a in range(1,p))
                self.assertEqual(mean, Q(numerator, (p-1)*w.length**2))
                lo, hi = galois_collision_bounds(p, radius)
                self.assertLessEqual(lo, mean)
                self.assertLessEqual(mean, hi)

    def test_repeated_phase_mutation_fails(self):
        p, radius = 17, Q(1, 100)
        local = prime_window(p).local
        mean = sum((Q(brute_pairs(tuple((a*u)%1 for u in local), radius),
                             len(local)**2) for a in range(1,p)), Q(0))/(p-1)
        wrong = Q((2*p*radius).__floor__()+1, p-1)
        self.assertEqual(mean, Q(1, 2))
        self.assertEqual(wrong, Q(1, 16))
        self.assertGreater(mean, wrong)

    def test_factor_two_carry_transport_and_sharp_constant(self):
        before, after = (Q(1,8), Q(3,8)), (Q(5,16), Q(7,16))
        check = carry_collision_check(before, after, 4)
        self.assertEqual(check["after"], 2*check["before"])
        self.assertTrue(check["forward_bound"] and check["reverse_bound"])
        self.assertGreater(check["after"], Q(199,100)*check["before"])
        for phases in product((Q(0), Q(7,16), Q(15,16)), repeat=3):
            for changes in product((Q(0), Q(1,32), Q(7,32)), repeat=3):
                shifted = tuple((x+d)%1 for x,d in zip(phases,changes))
                data = carry_collision_check(phases, shifted, 4)
                self.assertTrue(data["forward_bound"] and data["reverse_bound"])

    def test_actual_pi_bins_against_independent_machin_source(self):
        for p in (17, 41, 73, 97):
            w = prime_window(p)
            for cells in (16, 64, 256):
                self.assertLess(w.tail_bound, Q(1,cells))
                bins = certified_pi_bins(w.start, w.length, cells)
                raw_bins = [int(v*cells) for v in w.states]
                self.assertTrue(all((v-u)%cells in (0,1)
                                    for u,v in zip(raw_bins,bins)))
                counts = Counter(bins)
                pi_collision = Q(cells*sum(c*c for c in counts.values()), w.length**2)
                rational_collision = cell_collision(w.states,cells)
                self.assertLessEqual(pi_collision, 2*rational_collision)
                self.assertLessEqual(rational_collision, 2*pi_collision)

    def test_actual_source_tail_bounds_independent_interval(self):
        lo, hi = machin_bounds(120)
        source = bbp_states(48)
        for n in range(1,49):
            real_prefix = sum((16**(n-j)*bbp_forcing(j)
                               for j in range(1,n+1)), Q(0))
            self.assertLess(real_prefix, 16**(n-1)*lo)
            self.assertLess(16**(n-1)*hi-real_prefix, tail_upper(n))
            self.assertEqual(real_prefix % 1, source[n])

    def test_counterfeit_complement_preserves_p_free_but_not_source(self):
        for p in (17,41,97):
            w = prime_window(p)
            cells = 64
            fake = adversarial_complement(p,cells)
            self.assertNotEqual(fake,w.complement)
            self.assertTrue(all(c.denominator % p for c in fake))
            phases = tuple((u+v)%1 for u,v in zip(w.local,fake))
            self.assertEqual(cell_collision(phases,cells), cells)
            self.assertEqual(small_ball_pairs(phases,Q(1,cells)),w.length**2)

    def test_haar_digit_collision_mean_by_exact_word_enumeration(self):
        # Equal overlapping blocks impose m independent equality constraints.
        for base in (2,3):
            for m in (1,2):
                for gap in (1,2,3):
                    words = list(product(range(base),repeat=m+gap))
                    hits = sum(w[:m] == w[gap:gap+m] for w in words)
                    self.assertEqual(Q(hits,len(words)),Q(1,base**m))

    def test_collision_support_and_nonnormal_controls(self):
        for cells in (4,16,64):
            self.assertEqual(cell_collision((Q(1,3),)*20,cells), cells)
        grid = tuple(Q(i,16) for i in range(16))
        self.assertEqual(cell_collision(grid,16),1)
        self.assertEqual(cell_collision(grid,256),16)
        self.assertEqual(cell_collision((Q(0),Q(0),Q(1,2)),8),Q(40,9))

    def test_regret_potential_bound_exact_and_sharp(self):
        pool = tuple(exact_point(t) for t in (0,1,-1))
        for n in (1,2,3):
            for sample in product(pool,repeat=n):
                energy = exact_energy(sample)
                for point in pool:
                    excess = exact_potential(sample,point)/n-1
                    self.assertLessEqual(excess*excess,2*(energy-1))
        self.assertEqual(exact_energy((pool[0],)),3)
        self.assertGreater(Q(4),Q(199,100)*Q(2))

    def test_fail_closed_domains_and_underresolution(self):
        for bad in (True,1.0,-1):
            with self.assertRaises(ValueError): bbp_forcing(bad)
        for p in (2,9,19,25):
            with self.assertRaises(ValueError): prime_window(p)
        for radius in (0.01,Q(1,2),Q(-1,2)):
            with self.assertRaises(ValueError): small_ball_pairs((Q(0),),radius)
        with self.assertRaises(ValueError): cell_counts((),16)
        with self.assertRaises(ValueError): carry_collision_check((Q(0),),(Q(1,2),),4)
        with self.assertRaises(ValueError): prime_window(17).conjugate(0)
        with self.assertRaises(ValueError): certified_pi_bins(20,1,16,terms=1)


if __name__ == "__main__":
    unittest.main()

"""Independent exact checks of the simultaneous-clock source contract."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from math import gcd, prod
import unittest

from observational_succ.pi_prime_clock_conditioning import (
    aligned_complement_control, clock_pair_count, common_prime_window,
    conditional_cell_counts,
)


def independent_state(n):
    # Expanded-source weighted sum, not the production modular state loop.
    # The combined rational function is independently algebraically derived.
    return sum((16**(n-j) * Q(120*j*j-89*j+16,
                            (2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))
                for j in range(1, n+1)), Q(0)) % 1


def distance(x, y):
    d = abs(x-y) % 1
    return min(d, 1-d)


class PrimeClockConditioningTests(unittest.TestCase):
    def test_authenticated_injective_pair(self):
        w = common_prime_window((73, 97))
        self.assertEqual((w.start, w.stop, w.orders, w.period), (13, 36, (9, 12), 36))
        self.assertEqual(w.states, tuple(independent_state(n) for n in range(13, 37)))
        self.assertTrue(all(gcd(x.denominator, 73*97) == 1 for x in w.complement))
        self.assertEqual([len(f) for f in w.fibers()], [1]*24)
        self.assertTrue(all(len(law) == 1 for law in conditional_cell_counts(w, 16)))
        counts = Counter(int(x*16) for x in w.states)
        self.assertEqual(dict(counts), {0:4, 1:2, 2:1, 3:4, 4:3, 7:2,
                                       8:2, 9:2, 10:2, 13:1, 14:1})
        self.assertEqual(sum(distance(x, y) <= Q(1,16) for x in w.states for y in w.states),106)

    def test_preregistered_repeated_fiber_holdout(self):
        # Fixed before this window was computed: noninjective source clocks.
        w = common_prime_window((193, 241))
        self.assertEqual((w.start, w.stop, w.orders, w.period), (31, 96, (24, 6), 24))
        self.assertEqual(w.states, tuple(independent_state(n) for n in range(31, 97)))
        self.assertEqual(sorted(map(len,w.fibers())), [2]*6 + [3]*18)
        for embedding in ((2,3), (192,240), (17,19)):
            shifted = w.conjugate(embedding)
            for fiber in w.fibers():
                # Compare distances themselves, including exact endpoints.
                for i in fiber:
                    for j in fiber:
                        self.assertEqual(distance(w.states[i],w.states[j]),
                                         distance(shifted[i],shifted[j]))
            for cells in (3,16,64):
                before = conditional_cell_counts(w,cells)
                after = conditional_cell_counts(w,cells,embedding)
                for a,b in zip(before,after):
                    ca=sum(count*count for _,count in a)
                    cb=sum(count*count for _,count in b)
                    self.assertLessEqual(ca,2*cb)
                    self.assertLessEqual(cb,2*ca)
                # Independent support certificate for both conditional entropies.
                forward,reverse=defaultdict(set),defaultdict(set)
                for i in range(len(w.states)):
                    a=int(cells*w.states[i]); b=int(cells*shifted[i]); r=w.local[i]
                    forward[r,a].add(b); reverse[r,b].add(a)
                self.assertLessEqual(max(map(len,forward.values())),2)
                self.assertLessEqual(max(map(len,reverse.values())),2)

    def test_clock_pair_formula_incomplete_and_superlong_periods(self):
        for length in range(1,40):
            for period in range(1,45):
                expected=sum((i-j)%period == 0 for i in range(length) for j in range(length))
                self.assertEqual(clock_pair_count(length,period),expected)

    def test_multiclock_alignment_is_explicitly_changed_source(self):
        w=common_prime_window((73,97))
        denominator,fake=aligned_complement_control(w,16)
        self.assertEqual(denominator,226593)
        self.assertEqual(gcd(denominator,prod(w.primes)),1)
        self.assertNotEqual(fake,w.complement)
        aligned=tuple((sum(row,Q(0))+v)%1 for row,v in zip(w.local,fake))
        self.assertTrue(all(Q(0)<=x<Q(1,denominator) for x in aligned))
        self.assertEqual(sum(distance(x,y)<=Q(1,16) for x in aligned for y in aligned),576)
        self.assertTrue(all(gcd(x.denominator,prod(w.primes))==1 for x in fake))

    def test_no_distinct_first_clock_covers_target_window(self):
        values=(17,41,73,89,97,113,137,193,241)
        for p in values:
            u=(p-1)//8
            for q in values:
                v=(q-1)//8
                self.assertEqual(v+1<=u+1 and 4*v>=4*u,p==q)
        with self.assertRaisesRegex(ValueError,"empty intersection"):
            common_prime_window((17,73))

    def test_translation_boundary_factor_is_sharp(self):
        before=(Q(49,100),Q(51,100))
        after=tuple((x+Q(1,4))%1 for x in before)
        c=lambda xs:sum(v*v for v in Counter(int(2*x) for x in xs).values())
        self.assertEqual(c(after),2*c(before))

    def test_rejects_contract_mutations(self):
        for values in ((),(73,73),(9,),(3,),(True,),(73.0,)):
            with self.assertRaises(ValueError):
                common_prime_window(values)
        w=common_prime_window((73,97))
        for embedding in ((),(1,),(0,1),(1,97),(True,1)):
            with self.assertRaises(ValueError):
                w.conjugate(embedding)
        for cells in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                conditional_cell_counts(w,cells)
        for length,period in ((0,1),(1,0),(True,1),(1,1.5)):
            with self.assertRaises(ValueError):
                clock_pair_count(length,period)


if __name__ == "__main__":
    unittest.main()

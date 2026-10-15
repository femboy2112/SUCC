"""BLACK SUN C-track tests: Collatz defect cocycle and valuation dictionary."""
import unittest

from observational_succ.black_sun_collatz import (
    BlackSunCTrackError,
    cycle_equation,
    defect_cocycle,
    iterate_word,
    no_small_cycles,
    p_lattice_coset,
    shortcut_step,
    valuation_dictionary,
    verify_defect_cocycle,
    v_p,
)


class TestDefectCocycle(unittest.TestCase):
    """BS-C1: 2^m T^m(n) = 3^k n + c_eps exactly."""

    def test_cocycle_on_realizing_orbits(self):
        # actual orbits: their parity words must satisfy the identity
        # words generated from the actual orbits (computed, not hand-written)
        cases = []
        for n0, m in ((7, 8), (1, 4), (5, 8), (27, 20)):
            cur = n0
            eps = []
            for _ in range(m):
                eps.append(cur % 2)
                cur = shortcut_step(cur)
            cases.append((n0, eps))
        for n0, eps in cases:
            # verify the word IS the actual parity sequence
            cur = n0
            for j, e in enumerate(eps):
                self.assertEqual(cur % 2, e, f"word mismatch at {j} for n0={n0}")
                cur = shortcut_step(cur)
            self.assertTrue(verify_defect_cocycle(eps, n0))

    def test_cocycle_formula_generic(self):
        # the algebraic identity holds for the FORCED branch composition:
        # 2^m (forced word map)(n) = 3^k n + c_eps, for ANY word and ANY n
        from observational_succ.black_sun_collatz import forced_word_map
        for eps in ([1, 1, 1], [0, 1, 0, 1], [1]*8, [0]*5, [1, 0, 1, 0, 1]):
            m, k, c = defect_cocycle(eps)
            for n in (11, 1, 7, 100):
                cur = forced_word_map(n, eps)   # exact Fraction
                self.assertEqual((2**m)*cur, (3**k)*n + c,
                                 f"word {eps}, n={n}")
                # affine-map identity: coefficients independent of n
        # coefficient extraction: word map is x -> (3^k x + c)/2^m
        m, k, c = defect_cocycle([1, 0, 1, 1, 0, 1])
        self.assertEqual(forced_word_map(2, [1, 0, 1, 1, 0, 1]),
                         (3**k*2 + c)/(2**m))

    def test_trivial_cycle_equation(self):
        # 1 -> 2 -> 1: word (1,0): m=2, k=1, c=1: n(2^2-3) = 1: n=1
        m, k, c = defect_cocycle([1, 0])
        self.assertEqual((m, k, c), (2, 1, 1))
        exists, n = cycle_equation(m, k, c)
        self.assertTrue(exists)
        self.assertEqual(n, 1)


class TestValuationDictionary(unittest.TestCase):
    """BS-C2: v_3(c_eps)=0, v_3(2^m-3^k)=0, so cycle elements are coprime
    to 3; the p>=5 lattice dictionary."""

    def test_no_cycle_element_divisible_by_3(self):
        for eps in ([1, 0], [1, 0, 1, 0], [1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1]):
            d = valuation_dictionary(eps)
            self.assertEqual(d["v3_c"], 0, f"c_eps must be coprime to 3: {eps}")
            if d["D"] and d["D"] > 0:
                self.assertEqual(d["v3_D"], 0)

    def test_all_cycle_candidates_coprime_3(self):
        """Every realizable positive cycle candidate n = c_eps/(2^m-3^k)
        over all words of length <= 16 is coprime to 3 (exact certificate)."""
        for m in range(2, 17):
            for mask in range(2**m):
                eps = [(mask >> j) & 1 for j in range(m)]
                mk, k, c = defect_cocycle(eps)
                D = 2**mk - 3**k
                if D > 0 and c % D == 0:
                    n = c // D
                    self.assertEqual(n % 3, 0 if n == 0 else n % 3,
                                     msg="sanity")
                    if n > 0:
                        self.assertNotEqual(n % 3, 0,
                                            "cycle candidate divisible by 3")

    def test_p_lattice_p5(self):
        d = p_lattice_coset(5)
        self.assertEqual(d["condition"], "1*m == 3*k (mod 4)")

    def test_p_lattice_matches_actual_valuations(self):
        """v_5(2^m - 3^k) >= 1 iff m == 3k mod 4: direct check."""
        for m in range(1, 25):
            for k in range(1, 13):
                D = 2**m - 3**k
                v5 = v_p(D, 5) if D else 0
                self.assertEqual(v5 >= 1, (m - 3*k) % 4 == 0,
                                 f"m={m}, k={k}: v5={v5}")


class TestNoSmallCycles(unittest.TestCase):
    """Exact finite certificate through the defect equation (TESTED MODEL:
    matches the classical verification; validates the cocycle end-to-end)."""

    def test_no_nontrivial_cycles_m_18(self):
        ok, found = no_small_cycles(18)
        self.assertTrue(ok)
        # only the trivial cycle appears (n=1 and n=2 entries)
        self.assertTrue(all(n in (1, 2) for (_, _, n) in found))

    def test_domain_bounds(self):
        with self.assertRaises(BlackSunCTrackError):
            no_small_cycles(0)
        with self.assertRaises(BlackSunCTrackError):
            p_lattice_coset(3)


if __name__ == "__main__":
    unittest.main()
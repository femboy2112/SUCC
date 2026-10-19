"""Independent exact controls, finite exhaustive fixtures, and hostile mutations."""
from fractions import Fraction as F
from math import gcd
import unittest

from observational_succ.abc_clock_families import (
    ABCClockError, ABCTriple, exact_local_clock, finite_envelope,
    prime, prime_factors, prime_progression_lifts, radical, radical_sieve,
    residue_clock_indicator, ris, valuation,
)


class ABCClockTests(unittest.TestCase):
    def test_exact_defect_examples(self):
        for a, b, c, R, H in ((1, 8, 9, 6, 12),
                              (3, 125, 128, 30, 1600),
                              (1, 4374, 4375, 210, 91125)):
            t = ABCTriple(a, b, c)
            self.assertEqual((t.radical, t.ris), (R, H))
            self.assertEqual(t.radical * t.ris, a*b*c)
            self.assertEqual(t.abc_quality_excess(F(0)), F(c, R))
            self.assertEqual(t.is_exceptional(), c > R)

    def test_factorization_agrees_with_naive_independent_radical(self):
        for n in range(1, 1500):
            expected = 1
            for p in range(2, n+1):
                if n % p == 0 and all(p % d for d in range(2, int(p**0.5)+1)):
                    expected *= p
            self.assertEqual(radical(n), expected)
            self.assertEqual(ris(n) * radical(n), n)
        self.assertEqual(prime_factors(1), ())

    def test_invalid_and_composite_place_rejected(self):
        for args in ((3, 6, 9), (3, 5, 9), (0, 1, 1)):
            with self.assertRaises(ABCClockError):
                ABCTriple(*args)
        with self.assertRaises(ABCClockError):
            exact_local_clock(4, 2)
        with self.assertRaises(ABCClockError):
            valuation(18, 9)
        with self.assertRaises(ABCClockError):
            prime_progression_lifts(3, 7, 13)

    def test_clock_signature_occupies_one_slot_per_prime(self):
        t = ABCTriple(1, 8, 9)
        self.assertEqual(t.clock_signature(), ((2, "b", 3), (3, "c", 2)))
        self.assertEqual(t.family_key(), (2, 3, 0, 1, 1))
        for a, b in ((1, 32), (14, 15), (11, 24), (81, 125)):
            t = ABCTriple(a, b, a+b)
            self.assertEqual(len({p for p, _, _ in t.clock_signature()}), t.width)
            self.assertEqual(sum(k-1 for _, _, k in t.clock_signature()), t.depth)

    def test_exact_haar_local_probabilities(self):
        for p in (2, 3, 5, 7):
            for k in (1, 2, 3):
                law = exact_local_clock(p, k)
                self.assertEqual(law["each_slot_at_least_depth"],
                                 F(p, (p+1)*p**k))
                self.assertEqual(law["no_occupied_slot"]+3*law["each_slot_occupied"], 1)
                self.assertEqual(law["each_slot_exact_depth"],
                                 law["each_slot_at_least_depth"]-
                                 exact_local_clock(p, k+1)["each_slot_at_least_depth"])

    def test_local_law_against_residue_enumeration(self):
        # Distinct prime powers, exact integer counts: no simulation or floating error.
        for p, k in ((2, 1), (2, 2), (3, 1), (3, 2), (5, 1)):
            m = p**(k+1)
            allowed = [(a, b) for a in range(m) for b in range(m)
                       if not (a % p == 0 and b % p == 0)]
            den = len(allowed)
            law = exact_local_clock(p, k)
            self.assertEqual(F(sum(a % p and b % p and (a+b) % p != 0
                                   for a, b in allowed), den), law["no_occupied_slot"])
            for which in (lambda a,b:a, lambda a,b:b, lambda a,b:a+b):
                self.assertEqual(F(sum(which(a,b) % p**k == 0 for a,b in allowed), den),
                                 law["each_slot_at_least_depth"])
                self.assertEqual(F(sum(which(a,b) % p**k == 0 and
                                       which(a,b) % p**(k+1) != 0 for a,b in allowed), den),
                                 law["each_slot_exact_depth"])

    def test_exact_character_orthogonality(self):
        for modulus in range(1, 45):
            for a in range(-12, 13):
                for b in range(-6, 7):
                    self.assertEqual(residue_clock_indicator(a,b,modulus),
                                     int((a+b)%modulus == 0))

    def test_green_tao_lifts_squareful_vs_quality(self):
        for p_minus, p_mid, p_plus in ((3,5,7),(5,11,17),(7,19,31),(5,17,29)):
            t0, t1 = prime_progression_lifts(p_minus,p_mid,p_plus)
            d = p_mid-p_minus
            self.assertEqual(t0.ris, 1)
            self.assertEqual(t0.radical, 2*p_minus*p_mid*p_plus)
            self.assertEqual(t1.radical, p_minus*p_mid*p_plus*radical(d))
            self.assertEqual(t1.ris, p_mid*d*d//radical(d))
            self.assertEqual(t1.abc_quality_excess(F(0)),
                             F(p_mid,p_minus*p_plus*radical(d)))
            self.assertFalse(t0.is_exceptional())
            self.assertFalse(t1.is_exceptional())
            self.assertLess(t1.abc_quality_excess(F(0)), F(1,3))
        for args in ((3, 7, 13), (3, 5, 9), (2,3,5)):
            with self.assertRaises(ABCClockError):
                prime_progression_lifts(*args)

    def test_radical_sieve_independent_trial_factors(self):
        r = radical_sieve(1000)
        for n in range(1, 1001):
            self.assertEqual(r[n], radical(n))

    def test_finite_envelope_with_independent_bruteforce(self):
        es = (F(0), F(1,10), F(1,2), F(1))
        data = finite_envelope(85, es)
        independent = {}
        total = 0
        for c in range(3, 86):
            for a in range(1, c//2+1):
                b = c-a
                if gcd(a,b) != 1 or a > b:
                    continue
                total += 1
                R = radical(a*b*c)
                for e in es:
                    v = F(c**e.denominator, R**(e.numerator+e.denominator))
                    independent[e] = max(v, independent.get(e,F(0)))
        self.assertEqual(data["count"], total)
        for e in es:
            self.assertEqual(data["maxima"][e][0], independent[e])
            self.assertEqual(max(v for v, t in data["families"][e].values()), independent[e])
        vals = [data["maxima"][e][0] for e in es]
        for i in range(len(es)-1):
            self.assertGreaterEqual(vals[i]**es[i+1].denominator,
                                    vals[i+1]**es[i].denominator)

    def test_forged_radical_is_detected(self):
        t = ABCTriple(1,4374,4375)
        forged = radical(t.c)  # dropping a,b support spuriously inflates energy
        self.assertNotEqual(forged,t.radical)
        self.assertGreater(F(t.c,forged), F(t.c,t.radical))


if __name__ == "__main__":
    unittest.main()

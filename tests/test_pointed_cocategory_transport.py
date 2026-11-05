"""Exact finite probes for pointed BBP frame transport (research only).

No floating point, no claims of Haar-mixing, pi normality, or physical transport.
A circle phase is represented by its exact rational exponent modulo one.
"""
from fractions import Fraction as Q
import unittest

from observational_succ.bbp_natural_carrier import exact_forcing


def independent_four_pole(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def orbit(count, base=16, forcing=exact_forcing):
    result = [Q(0)]
    for n in range(1, count+1):
        result.append(base*result[-1]+forcing(n))
    return result


def phase(value):
    """Exact representation of exp(2*pi*i*value) as an element of Q/Z."""
    return value % 1


def character(u, n, s, h=1, base=16):
    return phase(h*(u[n]+base**n*s))


def count_vectors(length, total):
    if length == 1:
        yield (total,)
        return
    for c in range(total+1):
        for tail in count_vectors(length-1, total-c):
            yield (c,) + tail


class PointedCocategoryTransportTests(unittest.TestCase):
    def test_original_four_poles_and_unwrapped_origin(self):
        for n in range(1, 16):
            self.assertEqual(exact_forcing(n), independent_four_pole(n))
        self.assertEqual(exact_forcing(1), Q(47, 15))
        self.assertEqual(phase(exact_forcing(1)), Q(2, 15))
        self.assertEqual(orbit(1)[0], 0)

    def test_translation_character_is_exact(self):
        u = orbit(6)
        for n in range(7):
            for h in (-3, 1, 7):
                s, theta = Q(2, 9), Q(3, 11)
                lhs = phase(character(u, n, s+theta, h) - character(u, n, s, h))
                self.assertEqual(lhs, phase(h*16**n*theta))

    def test_anchor_preserves_selected_weyl_character(self):
        u = orbit(7)
        for s in (Q(0), Q(1, 7), Q(2, 9), Q(8, 21)):
            for h in (-3, 1, 2, 7):
                for n in range(8):
                    anchored = phase(character(u, n, s, h)
                                     - 16**n*character(u, 0, s, h))
                    self.assertEqual(anchored, phase(h*u[n]))

    def test_source_link_survives_frame_change(self):
        u = orbit(8)
        for s in (Q(0), Q(1, 7), Q(13, 17)):
            for h in (1, -3, 5):
                for n in range(8):
                    lhs = phase(character(u, n+1, s, h)
                                - 16*character(u, n, s, h))
                    self.assertEqual(lhs, phase(h*exact_forcing(n+1)))

    def test_transport_square_is_flat(self):
        u = orbit(6)
        s, theta = Q(13, 19), Q(3, 11)
        for n in range(6):
            for h in (1, -3):
                lhs = phase(
                    character(u, n+1, s+theta, h)
                    - character(u, n+1, s, h)
                    - 16*(character(u, n, s+theta, h)
                          - character(u, n, s, h))
                )
                self.assertEqual(lhs, 0)

    def test_time_varying_frames_have_declared_defect(self):
        u = orbit(6)
        thetas = [Q(n*n+1, 11+n) for n in range(7)]
        s = Q(2, 7)
        for n in range(6):
            v0 = u[n]+16**n*(s+thetas[n])
            v1 = u[n+1]+16**(n+1)*(s+thetas[n+1])
            self.assertEqual(
                v1-16*v0-exact_forcing(n+1),
                16**(n+1)*(thetas[n+1]-thetas[n]),
            )

    def test_wrong_anchor_exponent_leaks_seed(self):
        u = orbit(5)
        s, n, h = Q(1, 7), 2, 1
        wrong = phase(character(u, n, s, h)
                      - (16**n+1)*character(u, 0, s, h))
        self.assertNotEqual(wrong, phase(h*u[n]))

    def test_source_mutation_changes_link_without_changing_frame_law(self):
        mutant = lambda n: exact_forcing(n)+Q(1, 7)
        u = orbit(4, forcing=mutant)
        s = Q(1, 11)
        for n in range(4):
            link = phase(character(u, n+1, s)-16*character(u, n, s))
            self.assertEqual(link, phase(mutant(n+1)))
            self.assertNotEqual(link, phase(exact_forcing(n+1)))

    def test_first_unbalanced_resonance_has_degree_base_plus_one(self):
        # Orthogonality of characters: an integral contributes precisely when
        # sum_j base**n_j == base**m. Count-vectors enumerate all possibilities
        # exactly, including base=16 without floating point or huge products.
        for base, N in ((2, 4), (3, 4), (4, 4), (16, 4)):
            found = set()
            for counts in count_vectors(N, base):
                frequency = sum(c*base**i for i, c in enumerate(counts))
                for m in range(N):
                    if frequency == base**m:
                        found.add((counts, m))
            expected = {
                (tuple(base if i == m-1 else 0 for i in range(N)), m)
                for m in range(1, N)
            }
            self.assertEqual(found, expected)


    def test_integer_forcing_mutant_is_invisible_to_circle_characters(self):
        # The phase link sees r mod 1, NOT the unwrapped integer carry.
        altered = orbit(4, forcing=lambda n: exact_forcing(n)+1)
        self.assertNotEqual(altered[1], orbit(1)[1])
        s = Q(3, 11)
        for n in range(4):
            link = phase(character(altered, n+1, s)
                         - 16*character(altered, n, s))
            self.assertEqual(link, phase(exact_forcing(n+1)))


if __name__ == "__main__":
    unittest.main()

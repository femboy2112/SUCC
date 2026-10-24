"""Hostile source-only regression for circle/chord/π geometric normality frontier."""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ.circle_collision_rigidity import (
    covering, compose, evaluate, fejer_chord, chord_fourier,
    haar_moment, polygon_moment, prime_carries, carry_product,
    vertex_orbits, replica_count, chord_interval, perimeter_interval,
    pi_interval, aligned_phase, aligned_error, error_constant,
    energy_transport_error, certified_energy, outward_decimal,
)


class ExactCircleAlgebra(unittest.TestCase):
    def test_polynomial_origins(self):
        self.assertEqual(covering(0), (0,))
        self.assertEqual(covering(1), (0, 1))
        self.assertEqual(covering(2), (0, 4, -1))
        self.assertEqual(covering(3), (0, 9, -6, 1))
        self.assertEqual(covering(4), (0, 16, -20, 8, -1))

    def test_covering_composition_complete_small_grid(self):
        for a in range(1, 10):
            for b in range(1, 10):
                self.assertEqual(compose(covering(a), covering(b)),
                                 covering(a*b))

    def test_center_and_antipode_controls(self):
        for n in range(1, 30):
            self.assertEqual(evaluate(covering(n), 0), 0)
            self.assertEqual(evaluate(covering(n), 4),
                             4 if n % 2 else 0)
            self.assertEqual(covering(n)[1], n*n)
        self.assertNotEqual((0, 4, 1), covering(2))

    def test_logistic_circle_quotient(self):
        for u in (Q(0), Q(1, 8), Q(1, 2), Q(3, 4), Q(1)):
            self.assertEqual(evaluate(covering(2), 4*u)/4,
                             4*u*(1-u))

    def test_positive_fejer_chord_polynomial(self):
        self.assertEqual(fejer_chord(1), (Q(2), -Q(1, 2)))
        self.assertEqual(fejer_chord(2), (Q(3), -Q(2), Q(1, 3)))
        self.assertEqual(fejer_chord(3),
                         (Q(4), -Q(5), Q(2), -Q(1, 4)))
        for M in range(1, 10):
            P = fejer_chord(M)
            self.assertEqual(evaluate(P, 0), M+1)
            for i in range(33):
                self.assertGreaterEqual(evaluate(P, Q(i, 8)), 0)

    def test_haar_moments_identically_prime_carries(self):
        for k in range(85):
            self.assertEqual(carry_product(k), math.comb(2*k, k))
            self.assertEqual(haar_moment(k), carry_product(k))
            self.assertEqual(chord_fourier(k)[0], haar_moment(k))
            if k:
                self.assertEqual(sum(chord_fourier(k).values()), 0)
        self.assertEqual(prime_carries(5), {2: 2, 3: 2, 7: 1})

    def test_sharp_finite_polygon_stabilization(self):
        for k in range(1, 19):
            for m in range(k+1, k+6):
                self.assertEqual(polygon_moment(k, m), haar_moment(k))
            if k >= 2:
                self.assertEqual(polygon_moment(k, k),
                                 haar_moment(k) + 2*(-1 if k % 2 else 1))

    def test_selected_orbit_not_polygon_ensemble(self):
        self.assertEqual(vertex_orbits(7, 2),
                         ((0,), (1, 2, 4), (3, 6, 5)))
        self.assertEqual(polygon_moment(1, 7), 2)
        # Re sum_(r in 1,2,4) e(r/7) = -1/2 exactly, since
        # its conjugate is the other nonzero doubling orbit.
        selected = Q(2) - 2*Q(-1, 2)/3
        self.assertEqual(selected, Q(7, 3))
        self.assertNotEqual(selected, polygon_moment(1, 7))
        with self.assertRaises(ValueError):
            vertex_orbits(8, 2)

    def test_finite_fourier_flat_invariant_counterfeit(self):
        # Uniform qth-root measure is invariant under multiplier b if
        # gcd(q,b)=1. It is singular even though moments k<q are Haar.
        for q in (3, 5, 7, 11):
            self.assertEqual(set(v for cyc in vertex_orbits(q, 2)
                                 for v in cyc), set(range(q)))
            for k in range(1, q):
                self.assertEqual(polygon_moment(k, q), haar_moment(k))
                # Fourier coefficient at every 1<=h<=k is zero,
                # so the Fejer energy is exactly 1 despite non-Haar source.
                self.assertEqual(sum(1 if h % q == 0 else 0
                                     for h in range(1, k+1)), 0)

    def test_selected_periodic_orbit_exact_pair_energy(self):
        # x=1/3, b=2: orbit 1/3,2/3, squared chords D=0 or 3.
        N=8
        for M in range(1, 9):
            P=fejer_chord(M)
            via_chords = sum((evaluate(P, Q(0 if (j-k)%2==0 else 3))
                              for j in range(N) for k in range(N)), Q())/N**2
            def amp(h):
                return Q(1) if h % 3 == 0 else -Q(1, 2)
            via_fourier = 1+2*sum((Q(M+1-h, M+1)*amp(h)**2
                                  for h in range(1, M+1)), Q())
            self.assertEqual(via_chords, via_fourier)
            self.assertGreater(via_fourier, 1)

    def test_replica_bound_against_independent_modular_oracle(self):
        for numerator, denom in ((1, 3), (1, 7), (2, 11)):
            for base in (2, 3, 16):
                N,M=50,24
                def A(h):
                    vals=(cmath.exp(2j*math.pi*
                          ((h*numerator*pow(base,j,denom)) % denom)/denom)
                          for j in range(N))
                    return sum(vals)/N
                E=1+2*sum((1-h/(M+1))*abs(A(h))**2
                          for h in range(1, M+1))
                R=replica_count(base, 1, N, M)
                self.assertGreaterEqual(E, 1-1e-10)
                self.assertLessEqual(abs(A(1)), 2*R/N+((E-1)/R)**.5+1e-9)
        with self.assertRaises(ValueError):
            replica_count(2, 0, 50, 24)


class CertifiedPiGeometry(unittest.TestCase):
    def test_square_seed_and_polygon_pi_enclosures(self):
        self.assertEqual(chord_interval(1, 45), (Q(2), Q(2)))
        for n in range(1, 7):
            lo, hi = pi_interval(n, 75)
            self.assertLess(lo, Q(22, 7))
            self.assertGreater(hi, 3)
            self.assertLess(lo, hi)
            plo, _ = perimeter_interval(n, 75)
            self.assertEqual(plo, lo)

    def test_aligned_curvature_correction_source_only(self):
        pil, piu = pi_interval(32, 83)
        for K in (1, 3, 6):
            for j in range(8):
                lo, hi = aligned_phase(j, K, 83)
                self.assertLess(hi, 16**j*pil)
                self.assertLess(16**j*piu-lo, aligned_error(j, K))
        self.assertLess(error_constant(), Q(47))

    def test_exact_pi_pair_energy_witness(self):
        lo, hi = certified_energy(16, 5, 2, digits=72, pi_level=22, order=26)
        self.assertGreater(lo, Q(1541868, 1000000))
        self.assertLess(hi, Q(1541869, 1000000))
        self.assertLess(hi-lo, Q(1, 10**12))
        lo, hi = certified_energy(16, 8, 3, digits=78, pi_level=23, order=26)
        self.assertGreater(lo, Q(1234121, 1000000))
        self.assertLess(hi, Q(1234122, 1000000))
        self.assertLess(hi-lo, Q(1, 10**12))
        self.assertEqual(outward_decimal(lo, hi, 6),
                         (1234121, 1234122, 1000000))

    def test_aligned_geometric_energy_and_transfer(self):
        a, b = certified_energy(16, 8, 3, geometric=True,
                                lookahead=6, digits=78, pi_level=23, order=26)
        c, d = certified_energy(16, 8, 3, digits=78,
                                pi_level=23, order=26)
        self.assertLess(max(abs(a-d), abs(b-c)),
                        energy_transport_error(3, 8, 6))
        self.assertLess(energy_transport_error(3, 8, 6), Q(1, 10**11))

    def test_strict_falsifiers(self):
        with self.assertRaises(ValueError):
            chord_interval(0)
        with self.assertRaises(ValueError):
            certified_energy(16, 2, 1, geometric=True, lookahead=0)
        with self.assertRaises(ValueError):
            certified_energy(10, 2, 1, geometric=True)
        with self.assertRaises(ValueError):
            certified_energy(16, 1, 1)
        with self.assertRaises(ValueError):
            energy_transport_error(0, 3, 1)


class FinitePolygonEnsembleVsSelectedSource(unittest.TestCase):
    def test_exact_ensemble_orthogonality_and_large_polygon(self):
        from observational_succ.circle_collision_rigidity import (
            polygon_ensemble_fourier_square, polygon_ensemble_energy
        )
        # Full root-of-unity ensemble is extremely uniform at finite N,
        # but the fixed point at vertex 0 has |A_h|=1 for every h.
        base, N, M, m = 16, 6, 3, 4**12
        self.assertGreater(m, M*(base**(N-1)-1))
        for h in range(1, M+1):
            self.assertEqual(polygon_ensemble_fourier_square(
                base, h, N, m), Q(1, N))
        self.assertEqual(polygon_ensemble_energy(base, N, M, m),
                         1+Q(M, N))
        self.assertEqual(1+Q(M, N), Q(3, 2))
        self.assertEqual(M+1, 4)  # fixed selected vertex r=0

    def test_periodic_congruence_collisions_beyond_diagonal(self):
        from observational_succ.circle_collision_rigidity import (
            polygon_ensemble_fourier_square, polygon_ensemble_energy
        )
        # b=2 on the 7-gon is a permutation, but finite phase returns
        # still produce off-diagonal pair congruences once time grows.
        for N in (2, 4, 7, 12):
            for h in (1, 2, 3):
                x = polygon_ensemble_fourier_square(2, h, N, 7)
                y = Q(sum(1 for j in range(N) for k in range(N)
                          if (h*(pow(2, j, 7)-pow(2, k, 7)))%7 == 0),
                      N*N)
                self.assertEqual(x, y)
        self.assertGreater(polygon_ensemble_energy(2, 12, 3, 7), 1)
        with self.assertRaises(ValueError):
            polygon_ensemble_energy(2, 0, 2, 7)

    def test_source_ensemble_typicality_cannot_select_vertex_zero(self):
        from observational_succ.circle_collision_rigidity import (
            polygon_ensemble_energy
        )
        N,M,m=12,4,2**50
        self.assertGreater(m, M*(2**(N-1)-1))
        average=polygon_ensemble_energy(2,N,M,m)
        fixed_orbit=M+1
        self.assertEqual(average,1+Q(M,N))
        self.assertGreater(fixed_orbit,average)


    def test_wallis_pi_source_is_identical_to_haar_chord_moments(self):
        from observational_succ.circle_collision_rigidity import (
            wallis_from_circle_moments
        )
        pil, piu = pi_interval(20, 76)
        for k in range(1, 60):
            lo, hi = wallis_from_circle_moments(k)
            self.assertLess(lo, pil)
            self.assertGreater(hi, piu)
            self.assertEqual(lo, Q(2**(4*k+1),
                                   (2*k+1)*carry_product(k)**2))
            self.assertEqual(carry_product(k),
                             polygon_moment(k, k+1))
        with self.assertRaises(ValueError):
            wallis_from_circle_moments(0)


if __name__ == "__main__":
    unittest.main()

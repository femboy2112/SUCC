"""Finite exact probes. Universal claims are proved in RESEARCH.md, not by census."""
from fractions import Fraction as F
from itertools import product
import unittest

from prime_pisot import (
    Quad, charge_successor_jump, dconv, dirichlet_log, divisor_count,
    divisors, extract_primitives, factor, fiber_laplacian, generator_coeffs,
    half_strip_clock_tail, is_prime, local_profile, lucas_trace, mobius,
    omega, polya_laplacian, prime_fidelity, primes_upto, rank, require_prime,
)


class ArithmeticSource(unittest.TestCase):
    def test_unique_factorization_and_divisor_count(self):
        for n in range(1, 321):
            fs = factor(n)
            reconstructed = 1
            for p, e in fs.items():
                reconstructed *= p**e
            ds = [d for d in range(1, n+1) if n % d == 0]
            self.assertEqual(reconstructed, n)
            self.assertEqual(divisors(n), ds)
            self.assertEqual(divisor_count(n), len(ds))
            self.assertEqual(len(ds) == 2, omega(n) == 1)

    def test_prime_channels_reject_composites_and_invalid_inputs(self):
        for n in (1, 4, 6, 9, 12, 25, 49, True, 0, -3, 2.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                require_prime(n)

    def test_local_fidelity_from_actual_path_count(self):
        for n, p in product(range(1, 81), (2, 3, 5, 7)):
            original = [(a, n//a) for a in range(1, n+1) if n % a == 0]
            target = [(a, p*n//a) for a in range(1, p*n+1) if p*n % a == 0]
            image = {(p*a, b) for a, b in original}
            self.assertTrue(image.issubset(set(target)))
            overlap_squared = F(len(image)**2, len(original)*len(target))
            self.assertEqual(prime_fidelity(n, p), overlap_squared)

    def test_unseen_spectator_prime(self):
        menu = (2, 3, 5, 7)
        for n in (1, 2, 12, 49, 60):
            for q in (11, 13, 101):
                self.assertEqual(local_profile(n, menu), local_profile(n*q, menu))
        self.assertEqual(prime_fidelity(2, 2), prime_fidelity(6, 2))
        self.assertNotEqual(omega(2), omega(6))

    def test_prime_creation_charge(self):
        for n, p, q in product(range(1, 31), (2, 3, 5), (2, 3, 5)):
            self.assertEqual(factor(p*n).get(q, 0)-factor(n).get(q, 0), int(p == q))

    def test_successor_charge_is_unbounded_in_both_directions(self):
        for p, k in product((2, 3, 5, 7), range(1, 9)):
            self.assertEqual(charge_successor_jump(p**k-1, p), k)
            self.assertEqual(charge_successor_jump(p**k, p), -k)

    def test_source_affine_braid(self):
        for n, p in product(range(1, 100), (2, 3, 5, 11)):
            self.assertEqual(p*(n+1), p*n+p)


class VirtualEquilibria(unittest.TestCase):
    def test_pcr02_against_accepted_channel_gram(self):
        for m in range(1, 12):
            p = [[F(0) for _ in range(m)] for _ in range(m+1)]
            for k in range(m):
                p[k][k] = F(m-k, m+1)
                p[k+1][k] = F(k+1, m+1)
            gram_loss = [[F(i == j)-F(m+1, m)*sum(p[k][i]*p[k][j] for k in range(m+1))
                          for j in range(m)] for i in range(m)]
            self.assertEqual(polya_laplacian(m), gram_loss)

    def test_every_divisor_fiber_has_a_ground_state(self):
        for n in list(range(1, 41)) + [64, 72, 105, 210]:
            a = fiber_laplacian(n)
            self.assertEqual(len(a), divisor_count(n))
            self.assertTrue(all(sum(row) == 0 for row in a))
            self.assertEqual(rank(a), len(a)-1)

    def test_prime_filter_is_extra_not_emergent(self):
        for n in (1, 2, 3, 4, 6, 9, 12, 25, 30):
            a = fiber_laplacian(n)
            penalty = (omega(n)-1)**2
            b = [[x + (penalty if i == j else 0) for j, x in enumerate(row)]
                 for i, row in enumerate(a)]
            self.assertEqual(len(b)-rank(b), int(is_prime(n)))

    def test_pcr02_quadratic_form(self):
        for m in range(2, 9):
            a = polya_laplacian(m)
            x = [F((-1)**j*(j+1), j+2) for j in range(m)]
            matrix = sum(x[i]*a[i][j]*x[j] for i in range(m) for j in range(m))
            edges = sum(F(j*(m-j), m*(m+1))*(x[j]-x[j-1])**2 for j in range(1, m))
            self.assertEqual(matrix, edges)
            self.assertGreater(matrix, 0)

    def test_local_character_zero_is_inherited_by_composites(self):
        roots = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def local(j, quarter_turns):
            r = [roots[(quarter_turns*(2*k-j)) % 4] for k in range(j+1)]
            return (F(sum(x for x, _ in r), j+1), F(sum(y for _, y in r), j+1))
        self.assertEqual(local(1, 1), (0, 0))
        self.assertEqual(local(2, 1), (F(-1, 3), 0))
        for j in range(1, 9):
            self.assertEqual(local(j, 0), (1, 0))
            # The p factor at quarter-turn is zero even with a q^j spectator.
            self.assertEqual(local(1, 1)[0]*local(j, 0)[0], 0)


class EulerSource(unittest.TestCase):
    def test_formal_log_and_mobius_primitive_extraction(self):
        for nmax in (40, 160, 320):
            a = [F(0)] + [F(1)]*nmax
            logs = dirichlet_log(a)
            prim = extract_primitives(logs)
            for n in range(2, nmax+1):
                fs = factor(n)
                expected = F(1, next(iter(fs.values()))) if len(fs) == 1 else F(0)
                self.assertEqual(logs[n], expected)
                self.assertEqual(prim[n], int(is_prime(n)))

    def test_sieve_generator_and_factorization_implementations_agree(self):
        ps = primes_upto(160)
        self.assertEqual(generator_coeffs(160, ps), [F(0)] + [F(1)]*160)
        self.assertEqual(ps, [n for n in range(2, 161) if is_prime(n)])

    def test_fake_composite_generator_is_detected(self):
        a = generator_coeffs(80, primes_upto(80)+[4])
        self.assertEqual(a[4], 2)
        logs = dirichlet_log(a)
        self.assertEqual(logs[4], F(3, 2))
        self.assertEqual(extract_primitives(logs)[4], 1)

    def test_pair_penalty_changes_source_and_connected_readout(self):
        a = [F(0)] + [F(1, 2)**(omega(n)*(omega(n)-1)//2) for n in range(1, 81)]
        self.assertEqual(a[6], F(1, 2))
        self.assertEqual(dirichlet_log(a)[6], F(-1, 2))

    def test_complete_two_by_two_controls(self):
        cells = {}
        for fake, penalty in product((False, True), repeat=2):
            a = generator_coeffs(80, primes_upto(80)+([4] if fake else []))
            if penalty:
                a = [F(0)] + [a[n]*F(1, 2)**(omega(n)*(omega(n)-1)//2) for n in range(1, 81)]
            cells[fake, penalty] = dirichlet_log(a)[12]
        self.assertEqual(len(cells), 4)
        mixed = cells[True, True]-cells[True, False]-cells[False, True]+cells[False, False]
        self.assertEqual(mixed, F(-3, 8))

    def test_dirichlet_identity_and_invalid_constant(self):
        a = [F(0)] + [F(1)]*20
        unit = [F(0)]*21
        unit[1] = 1
        self.assertEqual(dconv(a, unit), a)
        a[1] = 2
        with self.assertRaises(ValueError):
            dirichlet_log(a)


class PisotSupport(unittest.TestCase):
    def test_exact_companion_trace_recurrence(self):
        for m, k in product((1, 2, 3, 5, 7, 11, 29, 97), range(0, 31)):
            beta = Quad(m, 0, 1)
            self.assertEqual((beta**k).trace(), lucas_trace(m, k))
            self.assertEqual(beta**k + beta.conjugate()**k, Quad(m, lucas_trace(m, k)))

    def test_negative_conjugate_sign_mutant_is_rejected(self):
        for m in (1, 2, 3, 11, 97):
            beta = Quad(m, 0, 1)
            # Independent source-polynomial checks: inverse() itself calls conjugate().
            # Without these, jointly changing both signs fools a shared-oracle test.
            self.assertEqual(beta.conjugate(), Quad(m, m, -1))
            self.assertEqual(beta**-1, beta-m)
            self.assertEqual(beta.conjugate(), -(beta**-1))
            self.assertNotEqual(beta.conjugate(), beta**-1)

    def test_clock_location_bound_without_floating_roots(self):
        for p in primes_upto(300):
            def f(x):
                return x*x-p*x-1
            self.assertEqual(f(F(p)), -1)
            self.assertEqual(f(F(p)+F(1, p)), F(1, p*p))

    def test_normalized_companion_spectrum_and_marked_projector(self):
        for m in (2, 3, 5, 11, 29, 97):
            b = Quad(m, 0, 1)
            c = b**-2
            tr = F(m)/b
            self.assertEqual(tr, 1-c)
            self.assertEqual(-b**-2, -c)
            # Spectral projector polynomial: (T+cI)/(1+c); eigenvalues 1 and 0.
            self.assertEqual((1+c)/(1+c), Quad(m, 1))
            self.assertEqual((-c+c)/(1+c), Quad(m, 0))
            for k in (1, 2, 3, 7, 19):
                self.assertEqual(Quad(m, lucas_trace(m, k))/b**k, 1+(-c)**k)
                self.assertNotEqual(1+(-c)**k, Quad(m, 1))

    def test_positive_markov_realization_and_virtual_difference(self):
        for m in (2, 3, 4, 5, 6, 11, 97):
            b = Quad(m, 0, 1)
            c = b**-2
            pi0, pi1 = 1/(1+c), c/(1+c)
            self.assertEqual(pi0*(1-c)+pi1, pi0)
            self.assertEqual(pi0*c, pi1)
            u, v = Quad(m, 3), Quad(m, -2)
            self.assertEqual(((1-c)*u+c*v)-u, -c*(u-v))
            self.assertEqual(pi0+pi1, Quad(m, 1))

    def test_two_prime_histories_have_exactly_the_same_pisot_clock(self):
        phi = Quad(1, 0, 1)
        b11, b29 = phi**5, phi**7
        self.assertEqual(b11*b11-11*b11-1, Quad(1, 0))
        self.assertEqual(b29*b29-29*b29-1, Quad(1, 0))
        self.assertEqual(b11**7, b29**5)
        self.assertNotEqual(11**7, 29**5)
        self.assertNotEqual(local_profile(11**7, (11, 29)), local_profile(29**5, (11, 29)))

    def test_non_pisot_clock_control_is_nonintegral_rational(self):
        for p in primes_upto(100):
            q = F(p)+F(1, p)
            self.assertEqual(q.denominator, p)
            self.assertGreater(q, p)

    def test_clock_tail_certificate(self):
        self.assertEqual(half_strip_clock_tail(10000, F(18)), F(3, 62500))
        self.assertEqual(half_strip_clock_tail(1000000, F(18)), F(3, 62500000))
        with self.assertRaises(ValueError):
            half_strip_clock_tail(0, F(18))

    def test_inverse_against_polynomial_multiplication(self):
        for m, a, b in product((1, 2, 3, 11), range(-2, 3), range(-2, 3)):
            if a == b == 0:
                continue
            x = Quad(m, a, b)
            self.assertEqual(x*x.inverse(), Quad(m, 1))
            self.assertEqual(x+x.conjugate(), Quad(m, 2*a+m*b))

    def test_quadratic_algebra_domain_controls(self):
        with self.assertRaises(ValueError):
            _ = Quad(2, 1) + Quad(3, 1)
        with self.assertRaises(ZeroDivisionError):
            _ = Quad(2).inverse()
        with self.assertRaises(ValueError):
            _ = Quad(2, 1)**0.5


if __name__ == '__main__':
    unittest.main(verbosity=2)

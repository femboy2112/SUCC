import unittest
from fractions import Fraction as Q
from math import gcd

import finite_weyl as w


def rational_oracle(n):
    numerator = (((((30720*n-63232)*n+45792)*n-13892)*n+1641)*n-48)
    denominator = (4*n-3)*(4*n-1)*(8*n-7)*(8*n-5)*(8*n-3)*(8*n-1)
    return Q(numerator, denominator)


class WeylTests(unittest.TestCase):
    def test_selected_source_and_inverse(self):
        for T in (13, 29, 47):
            M, positions = w.trajectory(T)
            state = Q(0)
            previous = 0
            self.assertEqual(M % 2, 1)
            for n in range(1, T+1):
                increment = rational_oracle(n)
                self.assertEqual(w.forcing(n), increment)
                state = 16*state + increment
                a = w.coordinate(positions[n], M)
                b = w.coordinate(increment, M)
                self.assertEqual(state % 1, Q(a, M))
                self.assertEqual(w.preimage(a, b, M), previous)
                self.assertEqual((16*previous+b) % M, a)
                previous = a
            # Wrong inverse moves the second or a later point to a different predecessor.
            self.assertTrue(any(
                (16*(w.coordinate(positions[n], M)-w.coordinate(w.forcing(n), M))) % M
                != w.coordinate(positions[n-1], M) for n in range(2, T+1)))

    def test_tower_source_and_character(self):
        for T in (13, 29, 47):
            fine, positions = w.trajectory(T)
            for t in range(1, T+1):
                coarse, points = w.trajectory(t)
                ratio, rem = divmod(fine, coarse)
                self.assertEqual(rem, 0)
                for h in (-19, -1, 0, 1, 11, fine):
                    self.assertEqual(
                        {ratio*a: count for a, count in
                         w.empirical_character(points, h, coarse).items()},
                        w.empirical_character(positions[:t+1], h, fine))

    def test_cocycle_and_affine_conjugacy(self):
        for M in (5, 9, 15):
            for x in range(M):
                for u, h, v, k in ((1, 1, 2, 3), (-1, 0, 1, -2), (0, 3, 2, 0)):
                    a, p = w.action((v,k), x, M)
                    b, q = w.action((u,h), a, M)
                    c, r = w.action((u+v,h+k), x, M)
                    self.assertEqual((b, (p+q-r) % M), (c, w.cocycle((u,h),(v,k),M)))
                    for inc in (-4, 0, 7):
                        label, center = w.affine_conjugate((u,h), inc, M)
                        a, p = w.action((u,h), w.preimage(x,inc,M), M)
                        b, q = w.action(label, x, M)
                        self.assertEqual(((16*a+inc) % M, p), (b, (q+center) % M))

    def test_rotation(self):
        for M in (5, 9, 15):
            for x in range(M):
                for y in range(M):
                    for u, h in ((1,2), (-1,0), (0,1)):
                        a, p = w.action((u,h), x, M)
                        # <y|F D|x> vs <y|D(-h,u) F|x>, common 1/sqrt(M).
                        _, q = w.action((-h,u), (y+h) % M, M)
                        self.assertEqual((p+a*y) % M, (q+(y+h)*x) % M)
            # Plus Fourier sends X to Z; opposite sign gives different exponent at y=1.
            self.assertNotEqual(1 % M, -1 % M)

    def test_position_injection_and_frequency_fibers(self):
        for M in (5,9,15):
            for ratio in (3,5):
                N = ratio*M
                self.assertEqual(Q(len(range(0, N, ratio)), N), Q(1,ratio))
                for y in range(N):
                    for x in range(M):
                        # Fourier kernel action F_N J = K F_M, same squared normalization.
                        self.assertEqual(Q(y*ratio*x,N) % 1, Q((y % M)*x,M) % 1)
                        self.assertEqual(Q(1,N), Q(1,ratio)*Q(1,M))
                lifts = [a for a in range(N) if a % M == 1 and M*a % N == 0]
                if gcd(M,ratio) == 1:
                    self.assertEqual(lifts, [w.character_lift(M,N)])
                else:
                    self.assertEqual(lifts, [])
                    with self.assertRaises(ValueError):
                        w.character_lift(M,N)

    def test_defect_reference_as_formal_character_moments(self):
        # B^*B-I-I has coefficients +1 at powers of z = exp(i theta), z^{-1}.
        # Multiplication below is exact in the group ring, for individual source kets.
        for T in (13,29,47):
            M, positions = w.trajectory(T)
            A = (T+1)//2
            epoch = positions[A:2*A]
            from collections import Counter
            for h in (-19,-1,0,1,11,M):
                coeffs = Counter()
                for y in epoch:
                    phase = h*w.coordinate(y,M) % M
                    terms = [(0,0),(1,phase)]
                    for t,a in terms:
                        for s,b in terms:
                            coeffs[s-t,(b-a) % M] += 1
                self.assertEqual(coeffs[0,0], 2*A)
                for sign in (-1,1):
                    self.assertEqual({phase: count for (degree,phase),count in
                                      coeffs.items() if degree == sign},
                                     w.empirical_character(epoch,sign*h,M))
                if h % M == 0:
                    self.assertEqual(w.empirical_character(epoch,h,M),{0:A})

    def test_forced_seed_symmetry_and_fixed_point(self):
        M, states = w.trajectory(47)
        mutated = Q(1,5)
        altered = [mutated]
        for n in range(1,48):
            mutated = (16*mutated+rational_oracle(n)) % 1
            altered.append(mutated)
        for x, y in zip(states, altered):
            self.assertEqual((y-x) % 1, Q(1,5))
        for a in range(len(states)):
            for b in range(len(states)):
                self.assertEqual((altered[a]-altered[b]) % 1, (states[a]-states[b]) % 1)
        self.assertEqual(w.empirical_character([Q(1,5)]*17, 1, 5), {1:17})
        self.assertEqual((16*Q(1,5)) % 1, Q(1,5))
        self.assertNotEqual((16*Q(1,7)) % 1, Q(1,7))


if __name__ == "__main__":
    unittest.main()

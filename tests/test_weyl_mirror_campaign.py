"""Exact regression controls plus explicitly noncertified Fourier diagnostics."""
import importlib.util
import math
import random
import unittest
from fractions import Fraction as F
from pathlib import Path
P = Path(__file__).resolve().parents[1]/'research/2026-11-02/weyl_mirror_campaign/weyl_mirror.py'
S = importlib.util.spec_from_file_location('wm', P)
w = importlib.util.module_from_spec(S)
S.loader.exec_module(w)


class ExactSource(unittest.TestCase):
    def test_four_poles_odd_form_and_polynomial(self):
        for n in range(1, 200):
            polynomial = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(w.source(n), w.odd_source(n))
            self.assertEqual(w.source(n), polynomial)
            self.assertEqual(w.source(n).denominator % 2, 1)

    def test_integer_lift_against_fraction_recurrence(self):
        D, xs = w.odd_modular_lift(256)
        self.assertEqual(D % 2, 1)
        self.assertEqual([F(x, D) for x in xs], w.fraction_phases(256))

    def test_parent_selfscale_receipts(self):
        D, xs = w.odd_modular_lift(511)
        for A, wanted in {8:14, 16:34, 32:52, 64:110, 128:220, 256:504}.items():
            counts, E = w.energy(xs[A-1:2*A-1], D, A)
            self.assertEqual(sum(c*c for c in counts), wanted)
            self.assertEqual(E, F(wanted, A))

    def test_even_poles_are_not_dropped(self):
        self.assertNotEqual(w.source(2), F(4,9)-F(1,13))

    def test_common_reflection_forcing_contradiction(self):
        self.assertEqual(2*(w.source(2)-w.source(3)), F(133558,765765))
        self.assertNotEqual((2*(w.source(2)-w.source(3))) % 1, 0)

    def test_moving_zero_seed_reflection_fixes_trajectory(self):
        beta = F(0)
        for n, u in enumerate(w.fraction_phases(80), 1):
            beta = (16*beta+2*w.source(n)) % 1
            self.assertEqual(beta, (2*u) % 1)
            self.assertEqual((beta-u) % 1, u)

    def test_exact_antiphase_and_tuned_mirror_impossible(self):
        xs = w.fraction_phases(50)
        for x in xs:
            for y in xs:
                self.assertNotEqual((x+y) % 1, F(1,16))
                for h in (1,3,16):
                    self.assertNotEqual((h*(x-y)) % 1, F(1,2))


class GeometryAndCouplings(unittest.TestCase):
    def test_rotations_and_reflections_of_power_map(self):
        for k in range(15):
            beta = F(k,15)
            for x in (F(1,7), F(13,89)):
                self.assertEqual((beta-16*x) % 1, (16*(beta-x)) % 1)
                self.assertEqual((16*x+beta) % 1, (16*(x+beta)) % 1)

    def test_tuned_mirror_twisted_square(self):
        for x in (F(0),F(1,5),F(17,257)):
            self.assertEqual((16*(F(1,16)-x)) % 1, (-16*x) % 1)
            self.assertEqual((F(1,16)+x) % 1, (F(1,16)-(-x)) % 1)

    def test_conjugates_do_not_cancel(self):
        self.assertAlmostEqual(w.weyl_float([F(1,6),F(5,6)],1).real, .5)
        self.assertAlmostEqual(w.weyl_float([F(1,6),F(5,6)],1).imag, 0)

    def test_uniform_centralizer_measure_is_not_haar(self):
        xs = [F(k,15) for k in range(15)]
        self.assertEqual([(16*x) % 1 for x in xs], xs)
        self.assertAlmostEqual(abs(w.weyl_float(xs,15)),1)
        self.assertGreater(w.mirror_wasserstein(list(range(15)),15),0)

    def test_mirror_sorted_transport_matches_cdf_oracle(self):
        rng = random.Random(160032)
        for D in (17,81,256):
            for N in (1,3,17,32):
                xs = [rng.randrange(D) for _ in range(N)]
                for beta in (F(0),F(1,2),F(1,16)):
                    ps = [F(x,D) for x in xs]
                    ys = [(beta-x) % 1 for x in ps]
                    self.assertEqual(w.mirror_wasserstein(xs,D,beta), w.cdf_wasserstein(ps,ys))

    def test_mirror_character_transport(self):
        D, xs = w.odd_modular_lift(100)
        W = w.mirror_wasserstein(xs,D)
        ps = [F(x,D) for x in xs]
        for h in (1,3,7,16):
            z = w.weyl_float(ps,h)
            factor = complex(math.cos(2*math.pi*h/16),math.sin(2*math.pi*h/16))
            self.assertLessEqual(abs(z-factor*z.conjugate()),2*math.pi*h*float(W)+1e-12)

    def test_antiphase_feasible_certificate(self):
        rng = random.Random(20261103)
        for D in (15,17,128):
            for N in (1,2,3,16):
                xs = [rng.randrange(D) for _ in range(N)]
                for h in (1,2,5):
                    cost = w.antiphase_matching_cost(xs,D,h)
                    z = w.weyl_float([F(x,D) for x in xs],h)
                    self.assertLessEqual(abs(z),float(w.antiphase_weyl_ceiling(cost))+1e-12)

    def test_positive_null_negative_controls(self):
        self.assertEqual(w.antiphase_matching_cost([0,1],2),0)
        self.assertEqual(w.antiphase_matching_cost([1]*10,5),F(1,2))
        self.assertEqual(w.mirror_wasserstein([1]*10,5),F(53,80))
        self.assertEqual(w.mirror_wasserstein([0]*10,1,F(0)),0)
        self.assertEqual(w.mirror_wasserstein([0]*10,1),F(1,16))

    def test_primitive_frequency_and_uniform_determinant(self):
        for h in range(1,1025):
            g,v = w.primitive_frequency(h)
            self.assertEqual(g*16**v,h)
            self.assertNotEqual(g % 16,0)
            self.assertGreaterEqual(abs(math.sin(math.pi*(g % 32)/16)),1/8)

    def test_actual_source_ward_and_mirror_ceiling(self):
        for N in (16,64,128):
            D,xs = w.odd_modular_lift(N)
            ps = [F(x,D) for x in xs]
            W = w.mirror_wasserstein(xs,D)
            for h in (1,3,16,32):
                self.assertLessEqual(abs(w.weyl_float(ps,16*h)-w.weyl_float(ps,h)),
                                     (2+165*h/56)/N+1e-12)
                self.assertLessEqual(abs(w.weyl_float(ps,h)),
                                     float(w.mirror_weyl_ceiling(W,N,h))+1e-12)


class HereditaryFejer(unittest.TestCase):
    def test_subset_kernel_energy_is_monotone(self):
        rng = random.Random(1664)
        ps = [F(rng.randrange(257),257) for _ in range(32)]
        for m in (4,16,32):
            full = len(ps)**2*w.fejer_float(ps,m)
            for selected in (ps[:9],ps[::2],ps[5:28]):
                self.assertLessEqual(len(selected)**2*w.fejer_float(selected,m),full+1e-9)

    def test_psd_without_pointwise_positivity_is_insufficient(self):
        ps = [F(0)]*8 + [F(1,2)]*8
        full = abs(16*w.weyl_float(ps,1))**2
        partial = abs(8*w.weyl_float(ps[:8],1))**2
        self.assertLess(full,1e-20)
        self.assertGreater(partial,63)

    def test_uniform_partial_epoch_ladder_bound(self):
        for alpha in (F(1,5),F(1,7),F(17,257)):
            A,m = 64,64
            x = (16**A*alpha) % 1
            ps = []
            for _ in range(A):
                ps.append(x)
                x = (16*x) % 1
            Q = w.fejer_float(ps,m)
            K = w.ladder_count(m,1)
            ceiling = math.sqrt(Q/K)+2*K/A
            for L in range(1,A+1):
                self.assertLessEqual(abs(L*w.weyl_float(ps[:L],1))/A,ceiling+1e-12)

    def test_general_mesh_tail_transport(self):
        for A in (16,32,64):
            D,xs = w.odd_modular_lift(2*A-1)
            ps = [F(x,D) for x in xs[A-1:2*A-1]]
            moved = [x+F(1,64*n*n) for x,n in zip(ps,range(A,2*A))]
            for m in (4,8,A):
                q0,q1 = w.fejer_float(ps,m),w.fejer_float(moved,m)
                delta = abs(math.sqrt(max(0,q0-1))-math.sqrt(max(0,q1-1)))
                self.assertLessEqual(delta,w.tail_norm_bound_float(A,m)+1e-12)

    def test_slow_mesh_growth_not_power_growth(self):
        for j in range(1,200):
            A = 1 << j
            m = w.slow_mesh(A)
            self.assertTrue(2 <= m <= A)
            self.assertEqual(m & (m-1),0)
            if j >= 2:
                self.assertTrue(j/2 < m <= j)
        self.assertEqual(w.slow_mesh(1 << 16),16)

    def test_rational_enclosures_and_invalid_inputs(self):
        x = F(1,3)
        r = w.rational_interval(x)
        self.assertLessEqual(F(r['lower_numerator'],r['denominator']),x)
        self.assertGreaterEqual(F(r['upper_numerator'],r['denominator']),x)
        for f in (lambda:w.slow_mesh(3),lambda:w.source(0),lambda:w.primitive_frequency(0),
                  lambda:w.mirror_wasserstein([],1),lambda:w.energy([0],1,1)):
            with self.assertRaises(ValueError):
                f()


if __name__ == '__main__':
    unittest.main()

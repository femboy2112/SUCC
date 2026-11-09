"""Exact regression controls: spatial 2-adic Haar != chronological pi Haar."""
from __future__ import annotations
from fractions import Fraction
import unittest
from observational_succ import bbp_spatial_haar_lift as m
from observational_succ.duck_bbp import forcing


class TestOriginalBBPHaarLift(unittest.TestCase):
    def test_original_four_signed_poles(self):
        for n in range(1,100):
            self.assertEqual(forcing(n),
                Fraction(4,8*n-7)-Fraction(2,8*n-4)
                -Fraction(1,8*n-3)-Fraction(1,8*n-2))

    def test_explicit_first_digit_full_cycle(self):
        states=m.source_spatial_states(513,16)
        self.assertEqual(len(set(states[:16])),16)
        for n in range(514):
            self.assertEqual(states[n],m.first_spatial_digit(n))

    def test_derivative_from_unreduced_four_poles(self):
        for a in range(64):
            d=(-Fraction(32,(8*a-7)**2)+Fraction(1,(2*a-1)**2)
                +Fraction(8,(8*a-3)**2)+Fraction(2,(4*a-1)**2))
            value=d.numerator*pow(d.denominator,-1,16)%16
            self.assertEqual(value,m.derivative_slope(a))
            self.assertEqual(value,11 if a%4 in (0,1) else 3)

    def test_256_spatial_states_and_direct_one_to_two_map(self):
        states=m.source_spatial_states(256,256)
        self.assertEqual(len(set(states[:256])),256)
        pairs=set()
        for a in range(16):
            for t in range(16):
                n=a+16*t
                actual=(states[n]%16,states[n]//16)
                self.assertEqual(states[n],m.affine_lift(a,t,1,states[a]))
                self.assertEqual(actual,
                    m.two_spatial_digits_from_first(m.first_spatial_digit(a),t))
                pairs.add(actual)
        self.assertEqual(len(pairs),256)

    def test_4096_level_and_all_16_children(self):
        states=m.source_spatial_states(4096,4096)
        self.assertEqual(len(set(states[:4096])),4096)
        for a in range(256):
            self.assertEqual({states[a+256*t]//256 for t in range(16)},
                             set(range(16)))
            for t in range(16):
                self.assertEqual(states[a+256*t],
                                 m.affine_lift(a,t,2,states[a]))

    def test_first_spatial_time_nibbles_are_not_two_digit_haar(self):
        seq=''.join("0123456789ABCDEF"[m.first_spatial_digit(n)]
                    for n in range(16))
        tab=m.word_counts(seq,cyclic=True)
        er,ec,e2,mixed=m.two_digit_energies(tab)
        self.assertEqual((er,ec,e2,mixed),(0,0,15,15))
        for d in range(16):
            self.assertEqual(tab[d][m.next_temporal_spatial_digit(d)],1)
            self.assertEqual(sum(tab[d]),1)

    def test_mixed_225_mode_decomposition_linear_and_cyclic(self):
        src="0123456789ABCDEF0011223344556677"
        for cyclic in (False,True):
            er,ec,e2,mixed=m.two_digit_energies(m.word_counts(src,cyclic))
            self.assertEqual(er+ec+mixed,e2)
            self.assertGreaterEqual(mixed,0)
            if cyclic:self.assertEqual(er,ec)

    def test_real_pi_two_digit_words_paid_source_tail(self):
        prefix=m.bulk_pi_hex_digits(96)
        self.assertTrue(prefix.startswith("243F6A8885A308D313198A2E03707344"))
        states=m.complete_source_states(96)
        for n in range(1,95):
            self.assertEqual(m.completed_real_word(n,2,12,states),
                             int(prefix[n-1:n+1],16))

    def test_wrong_seed_not_padic_real_identity(self):
        # A rational s=1/5 dies mod256 by time n=2 but stays a 1/5 turn real.
        for n in range(2,35):
            self.assertEqual((16**n*pow(5,-1,256))%256,0)
            self.assertEqual(Fraction(16**n,5)%1,Fraction(1,5))

    def test_two_guard_source_certificate(self):
        a=m.bulk_pi_hex_digits(512,24)
        b=m.bulk_pi_hex_digits(512,32)
        self.assertEqual(a,b)

    def test_wrong_input_rejection(self):
        with self.assertRaises(ValueError):m.two_spatial_digits_from_first(0,16)
        with self.assertRaises(ValueError):m.modular_source(3,19)
        with self.assertRaises(ValueError):m.next_temporal_spatial_digit(16)


if __name__ == "__main__":
    unittest.main()

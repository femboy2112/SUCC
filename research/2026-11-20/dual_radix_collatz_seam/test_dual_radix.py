"""Reproducible exact elementary checks; no tests certify general Collatz/pi."""
from fractions import Fraction
import random
import unittest
from dual_radix import (
    journal, repeated_digit, valuation, mirror_register, digit_step,
    two_adic_reversal, real_fractional_prefix, readout_235,
    collatz_shortcut, collatz_odd_accelerated, five_suffix_decompose,
    bbp_forcing, bbp_prefix, two_adic_digit_shift, two_adic_word, defect_first_mismatch
)

class DualRadixTests(unittest.TestCase):
    def test_q_clocks(self):
        for n in range(1,45):
            J=journal(n)
            self.assertEqual(15*J+1,16**n)
            for q,d in ((3,5),(5,3),(15,1)):
                N=repeated_digit(d,n)
                self.assertEqual(q*N+1, 16**n)
                self.assertEqual(hex(N)[2:],format(d,'x')*n)
                self.assertEqual(valuation(q*N+1,2),4*n)
                self.assertEqual(Fraction(d,15),Fraction(1,q))

    def test_full_collatz_time(self):
        for n in range(1,15):
            x=repeated_digit(5,n)
            self.assertEqual(collatz_odd_accelerated(x),1)
            for i in range(4*n):
                x=collatz_shortcut(x)
                if i<4*n-1:
                    self.assertNotEqual(x,1)
            self.assertEqual(x,1)

    def test_peel_five_suffix(self):
        for k in range(1,8):
            for prefix in (0,1,2,3,5,8,11,37,1023):
                x=16**k*prefix+repeated_digit(5,k)
                self.assertEqual(3*x+1,16**k*(3*prefix+1))
                self.assertEqual(valuation(3*x+1,2),4*k+valuation(3*prefix+1,2))
                y=x
                for _ in range(4*k):
                    y=collatz_shortcut(y)
                self.assertEqual(y,3*prefix+1)
                self.assertEqual(five_suffix_decompose(x,k),(prefix,True))

    def test_unique_digit_residue(self):
        for k in range(1,4):
            for n in range(16**k):
                self.assertEqual((3*n+1) % (16**k)==0,
                                 n==repeated_digit(5,k))

    def test_mirror(self):
        for n in range(1,15):
            J=journal(n)
            A=5*J; B=10*J
            self.assertEqual(mirror_register(A,n),B)
            self.assertEqual(3*B+2,2*16**n)
            self.assertEqual((3*B+1)%2,1)
            self.assertEqual(mirror_register(3*J,n),12*J)

    def test_3_5_valuation_clocks(self):
        for m in range(1,25):
            for n in range(m):
                Jm,Jn=journal(m),journal(n)
                for p in (3,5):
                    self.assertEqual(valuation(Jm-Jn,p),valuation(m-n,p))
                    self.assertEqual(valuation(5*(Jm-Jn),p),valuation(m-n,p)+(p==5))
                    self.assertEqual(valuation(3*(Jm-Jn),p),valuation(m-n,p)+(p==3))

    def test_2adic_root(self):
        for n in range(1,80):
            A=repeated_digit(5,n)
            self.assertEqual(valuation(3*A+1,2),4*n)
            self.assertEqual(collatz_odd_accelerated(A),1)
            self.assertEqual(collatz_odd_accelerated(A+2*16**n),7)
            self.assertEqual(valuation((A+2*16**n)-A,2),4*n+1)

    def test_dual_completions(self):
        random.seed(124)
        for n in range(1,45):
            d=tuple(random.randrange(16) for _ in range(n))
            rev=two_adic_reversal(d)
            dr=tuple(15-j for j in d)
            self.assertEqual(rev+two_adic_reversal(dr),16**n-1)
            self.assertEqual(real_fractional_prefix(d)+real_fractional_prefix(dr),1-Fraction(1,16**n))
            # Prefix of 2-adic shadow is stable in all later windows.
            self.assertEqual(two_adic_reversal(d+(4,9)) % 16**n,rev)

    def test_journal_source_and_checksum(self):
        random.seed(127)
        D=0
        for _ in range(2000):
            digit=random.randrange(16)
            E=digit_step(D,digit)
            self.assertEqual(readout_235(D%15,E%3,E%5,E%2),digit)
            self.assertEqual(E%3,(D%3+digit)%3)
            self.assertEqual(E%5,(D%5+digit)%5)
            D=E% (16**25)  # exact finite test with declared truncated memory

    def test_parity_is_load_bearing(self):
        D=0
        for d in (0,15):
            E=digit_step(D,d)
            self.assertEqual((E%3,E%5),(0,0))
            self.assertEqual(readout_235(0,E%3,E%5,E%2),d)

    def test_two_adic_shift_word_and_fixed_points(self):
        for d in (1,3,5,10,12,14):
            for k in range(1,23):
                M=16**k
                register=repeated_digit(d,k)
                self.assertEqual(register,(-d*pow(15,-1,M))%M)
                self.assertEqual(Fraction(d,15)*15,d)
                x=register
                for j in range(k):
                    found,x=two_adic_digit_shift(x)
                    self.assertEqual(found,d)
                self.assertEqual(x,0)
        source=(3,2,4,3,15,6,10,8)
        y=two_adic_reversal(source)
        for j in range(len(source)):
            self.assertEqual(two_adic_word(y,j,1),source[j])
        self.assertEqual(two_adic_word(y,2,3),4+3*16+15*256)
        self.assertNotEqual(two_adic_word(y,0,1),5)  # pi not constant-5

    def test_first_mismatch_exact_2adic_valuation(self):
        for q in (3,5,15):
            d=15//q
            for k in range(0,12):
                for next_digit in range(16):
                    if next_digit==d:
                        continue
                    ds=(d,)*k+(next_digit,9,7,11)
                    pred=defect_first_mismatch(ds,q)
                    self.assertEqual(pred,4*k+valuation(next_digit-d,2))
                    y=two_adic_reversal(ds)
                    self.assertEqual(valuation(q*y+1,2),pred)
            self.assertIsNone(defect_first_mismatch((d,)*8,q))
        pi=bbp_prefix(12,12)
        self.assertEqual(defect_first_mismatch(pi,5),4)
        self.assertEqual(defect_first_mismatch(pi,3),1)

    def test_digit_block_valuation_criterion(self):
        for q in (3,5,15):
            d=15//q
            for k in (1,2,3):
                for tail in range(16**k):
                    self.assertEqual((q*tail+1)%(16**k)==0,
                                     tail==repeated_digit(d,k))

    def test_mirror_wave_16_channel_naturality(self):
        # Exact rational evaluation of U R = R_tilde U for a nontrivial f.
        f=lambda t: (7*t**3 - 3*t**2 + 2*t + Fraction(1,9))
        for d in range(16):
            for r in (Fraction(1,11),Fraction(3,7),Fraction(9,10)):
                lhs=f(1-Fraction(d+r,16))/4
                rhs=f(Fraction(15-d+(1-r),16))/4
                self.assertEqual(lhs,rhs)

    def test_collatz_not_complement_conjugate(self):
        self.assertEqual(collatz_shortcut(5),8)
        self.assertEqual(collatz_shortcut(10),5)
        self.assertNotEqual(collatz_shortcut(10),mirror_register(8,1))

    def test_fixed_clock_horizon_versus_diagonal(self):
        for n in range(3,31):
            A=repeated_digit(5,n)
            for t in range(1,12):
                if t<4*n:
                    x=A
                    for _ in range(t):
                        x=collatz_shortcut(x)
                    self.assertEqual(x,2**(4*n-t))
            x=A
            for _ in range(4*n):
                x=collatz_shortcut(x)
            self.assertEqual(x,1)

    def test_bbp_first12(self):
        ds=bbp_prefix(12,12)
        self.assertEqual(''.join(format(d,'X') for d in ds),'3243F6A8885A')
        self.assertEqual(ds[:2],(3,2))
        self.assertEqual(two_adic_reversal(ds),int('A5888A6F3423',16))
        self.assertNotEqual(ds[:2],(3,3))  # not the 1/5 fixed orbit

    def test_bbp_source_original(self):
        for n in range(1,55):
            r=bbp_forcing(n)
            self.assertEqual(r,(Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))))

    def test_bad_inputs(self):
        for args in ((-1,), (0.5,)):
            with self.assertRaises(ValueError):journal(*args)
        with self.assertRaises(ValueError):repeated_digit(16,2)
        with self.assertRaises(ValueError):bbp_prefix(13,12)
        with self.assertRaises(ValueError):collatz_odd_accelerated(2)

if __name__=='__main__':
    unittest.main()

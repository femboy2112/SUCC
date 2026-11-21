"""Focused exact arithmetic tests for source-first parity, prime swap, and ring gates."""
import unittest
from fractions import Fraction as F
from math import isqrt
from source_first_parity import (
    forcing,bbp_partial,bbp_interval,source_parity_bit,source_parity_address,
    inverse_parity_mod,shortcut,parity_address,swapped_source_defect,
    prime_square_order_clock,signed_prime_swap,signed_carry_from_source,
    two_hex_block_from_source,two_hex_block_swapped,odd_return_residues_from_parity,source_quarter_haar,
)


class SourceFirstParityTests(unittest.TestCase):
    def test_original_forcing_conductor(self):
        for j in range(1,60):
            self.assertEqual(forcing(j),F(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3)))

    def test_source_monotonic(self):
        for j in range(1,150):
            self.assertGreater(forcing(j),forcing(j+1))
            self.assertGreater(swapped_source_defect(j),swapped_source_defect(j+1))

    def test_prefix_tail_and_zero_seed(self):
        for n in range(0,26):
            a,b=bbp_interval(n)
            self.assertLess(a,b)
            self.assertEqual(a,bbp_partial(n))
            self.assertGreaterEqual(a,0)
            self.assertLess(b,1)

    def test_rademacher_bits_from_original_source(self):
        expected="3243F6A8885A"
        for clock,digit in enumerate(expected):
            val=int(digit,16)
            for bit in range(4):
                eps,terms,(low,high)=source_parity_bit(clock,bit)
                self.assertEqual(eps,(val>>bit)&1)
                self.assertEqual(low.numerator//low.denominator,high.numerator//high.denominator)
                self.assertGreaterEqual(terms,clock)

    def test_source_first_48_bit_collatz_state(self):
        addr,terms=source_parity_address(12)
        self.assertEqual(addr,0xA5888A6F3423)
        seed=inverse_parity_mod(addr,48)
        self.assertEqual(seed,0x138D4B466283)
        self.assertEqual(parity_address(seed,48),addr)
        self.assertGreater(terms,0)

    def test_q4_is_involution_only_at_four_bits(self):
        tab=[parity_address(a,4) for a in range(16)]
        self.assertEqual(len(set(tab)),16)
        self.assertEqual([tab[tab[a]] for a in range(16)],list(range(16)))
        self.assertEqual([(a,tab[a]) for a in range(16) if a!=tab[a]],[(1,5),(2,10),(5,1),(9,13),(10,2),(13,9)])

    def test_four_step_cylinder_precisely_recovers_parity(self):
        for word in range(16):
            a=inverse_parity_mod(word,4)
            self.assertEqual(parity_address(a,4),word)

    def test_source_quarter_haar_predecoded(self):
        for n,ch in enumerate("3243F6A8885A"):
            hit,terms=source_quarter_haar(n)
            digit=int(ch,16)
            self.assertEqual(hit,int(4<=digit<12))
            self.assertGreaterEqual(terms,n)

    def test_pole_prime_clock_gate(self):
        self.assertEqual(prime_square_order_clock(7),6)
        self.assertEqual(prime_square_order_clock(11),15)
        self.assertEqual(prime_square_order_clock(13),21)
        for p in [9,15,21,25,27]:
            with self.assertRaises(ValueError):prime_square_order_clock(p)

    def test_prime_defect_small_and_positive(self):
        for p in [7,11,13,17,19,23,29,31,37,41,43,47]:
            j=prime_square_order_clock(p)
            D=swapped_source_defect(j)
            self.assertTrue(0<D<F(1,4))
            self.assertTrue(F(1,64)<=signed_prime_swap(p)[2]<F(1,4))

    def test_minimal_delay_and_exact_phase_quotient(self):
        for p in [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]:
            j,d,delta=signed_prime_swap(p)
            self.assertEqual(delta,16**d*swapped_source_defect(j))
            if d>0:self.assertLess(delta/16,F(1,64))
            self.assertGreaterEqual(delta,F(1,64))
            self.assertLess(delta,F(1,4))

    def test_signed_carry_direct_source_no_hex(self):
        for p in [7,11,13,17,19,23]:
            sign,terms,clock,delta=signed_carry_from_source(p)
            self.assertIn(sign,[-1,1])
            self.assertTrue(F(1,64)<=delta<F(1,4))
            # Independent two-digit decoding is used as a hostile witness only.
            for m in range(terms,terms+25):
                try:
                    base=two_hex_block_from_source(clock,m)
                    swap=two_hex_block_swapped(clock,prime_square_order_clock(p),m)
                    break
                except ValueError:
                    continue
            else:raise AssertionError('terminal precision never certified paired blocks')
            self.assertNotEqual(base,swap)
            self.assertEqual((base>swap)*2-1,sign)

    def test_unsigned_parity_response_eight_bits(self):
        for p in [7,11,13,17,19]:
            j,d,_=signed_prime_swap(p)
            clock=j+1+d
            for m in range(clock+2,clock+33):
                try:
                    base=two_hex_block_from_source(clock,m)
                    swap=two_hex_block_swapped(clock,j,m)
                    break
                except ValueError:continue
            self.assertNotEqual(base,swap)
            distance=(base ^ swap).bit_count()
            self.assertGreaterEqual(distance,1)
            self.assertGreaterEqual(4*distance,4)  # squared signed parity difference

    def test_collatz_mod3_reciprocity_from_original_source_signs(self):
        addr,_=source_parity_address(12)
        seed=inverse_parity_mod(addr,48)
        records=odd_return_residues_from_parity(addr,48)
        self.assertGreater(len(records),5)
        for pos,gap,residue in records:
            state=seed
            for _ in range(pos):state=shortcut(state)
            self.assertEqual(state%2,1)
            self.assertEqual((3*state+1)//2**gap%3,residue)
            self.assertEqual(((3*state+1)//2**gap)%2,1)

    def test_3adic_prediction_does_not_need_seed_in_congruence_class(self):
        addr,_=source_parity_address(12)
        base=inverse_parity_mod(addr,48)
        for u in range(1,6):
            a=base+u*(1<<48)
            self.assertEqual(parity_address(a,48),addr)
            for position,gap,residue in odd_return_residues_from_parity(addr,48):
                state=a
                for _ in range(position):state=shortcut(state)
                oddout=(3*state+1)//(1<<gap)
                self.assertEqual(oddout%3,residue)

    def test_lag_and_prime_square_source_marks(self):
        for p in [7,11,13,17,19,23]:
            j=prime_square_order_clock(p)
            r=forcing(j+1)
            # Rational p-primary 4/p^2: all other denominators are p-units.
            self.assertNotEqual((r-F(4,p*p)).denominator % p, 0)
            normalized=r*p*p
            self.assertNotEqual(normalized.denominator % p, 0)
            self.assertEqual(normalized.numerator * pow(normalized.denominator,-1,p) % p, 4)

    def test_negative_signed_carry_p19_and_positive_p11(self):
        self.assertEqual(signed_carry_from_source(19)[0],-1)
        self.assertEqual(signed_carry_from_source(11)[0],+1)

    def test_root_factor_idempotents_collapse_mod2(self):
        # F_2[t]/t^4: every element is a four-bit polynomial.
        idempotents=[]
        for v in range(16):
            sq=(v&1)|(((v>>1)&1)<<2)
            if sq==v:idempotents.append(v)
        self.assertEqual(idempotents,[0,1])

    def test_matched_jet_mutant_primary_mark_changes_4_to_5(self):
        for p in [7,11,13,17,19,23]:
            j=(p*p+7)//8
            d=F(2,(8*j-7)*(8*j-6)*(8*j-5))
            normalized=d*p*p
            self.assertNotEqual(normalized.denominator%p,0)
            self.assertEqual(normalized.numerator*pow(normalized.denominator,-1,p)%p,1)
            self.assertEqual(((forcing(j)+d)*p*p).numerator*pow(((forcing(j)+d)*p*p).denominator,-1,p)%p,5)

    def test_quarter_xor_is_not_necessary_for_r0(self):
        theta=F(1,15)     # exactly fixed by multiplication by 16 modulo 1
        self.assertEqual((16*theta)%1,theta)
        d=(16*theta).numerator//(16*theta).denominator
        self.assertEqual(d,1)
        self.assertNotEqual(theta,0)  # thus 1-cos(2*pi*theta)>0
        self.assertEqual(((d>>2)^(d>>3))&1,0)

    def test_disallowed_inputs(self):
        for a,b in [(-1,0),(0,-1),(0,4),(1,15)]:
            with self.assertRaises(ValueError):source_parity_bit(a,b)
        with self.assertRaises(ValueError):signed_prime_swap(25)

if __name__ == '__main__':
    unittest.main(verbosity=2)

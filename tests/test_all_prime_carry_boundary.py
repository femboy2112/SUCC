"""Exact full-CRT boundary tests; independent rational four-pole and integer oracles."""
from fractions import Fraction
from math import lcm
import unittest

from observational_succ.all_prime_carry_boundary import (
    original_carry_ledger, carry_ledger, carry_interval, carry_at_address,
    partial_prime_carry_count, crt_phase_address, consecutive_carry_counts,
    original_digit_at_carry, completed_digit_from_tail,
    two_adic_integral_residue, cross_place_integer_carry,
)
from observational_succ.adelic_additive_gluing import orbit_states, additive_prime_parts
from observational_succ.duck_bbp import forcing


def four_poles(n):
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def independent_integer_orbit(horizon):
    q,num=1,0
    out=[(Fraction(),0)]
    for n in range(1,horizon+1):
        f=four_poles(n)
        Q=lcm(q,f.denominator)
        incoming=(Q//f.denominator)*f.numerator
        literal=(16*(Q//q)*(num%q)+incoming)//Q
        num=16*(Q//q)*num+incoming
        q=Q
        out.append((Fraction(num,q),literal))
    return out


class OriginalFullPrimeCarryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states=orbit_states(32)
        cls.independent=independent_integer_orbit(32)

    def test_frozen_four_poles_independent(self):
        for n in range(1,33):
            self.assertEqual(forcing(n),four_poles(n))
            self.assertEqual(self.states[n],self.independent[n][0])

    def test_all_primes_all_prime_powers_holdout_17_32(self):
        for n in range(17,33):
            ledger=original_carry_ledger(n,states=self.states)
            self.assertEqual(ledger.literal_carry,self.independent[n][1])
            self.assertEqual(ledger.reconstructed_carry,ledger.literal_carry)
            self.assertEqual(ledger.following,self.states[n])
            self.assertEqual(ledger.conductor,lcm(self.states[n-1].denominator,forcing(n).denominator))
            self.assertEqual(len(ledger.rows),len(set(r.prime for r in ledger.rows)))
            self.assertEqual(ledger.conductor,__import__('math').prod(r.power for r in ledger.rows))
            self.assertEqual(sum((r.prior for r in ledger.rows),Fraction())%1,self.states[n-1]%1)
            self.assertEqual(sum((r.next for r in ledger.rows),Fraction())%1,self.states[n]%1)
            self.assertTrue(any(r.inherited_without_forcing for r in ledger.rows))

    def test_all_32_source_carries_including_late_zero(self):
        for n in range(1,33):
            x=original_carry_ledger(n,states=self.states)
            self.assertEqual(x.literal_carry,self.independent[n][1])
        self.assertEqual(original_carry_ledger(14,states=self.states).literal_carry,0)
        self.assertEqual(original_carry_ledger(32,states=self.states).literal_carry,4)

    def test_5_is_inherited_without_input_at_time_2(self):
        ledger=original_carry_ledger(2,states=self.states)
        rows={r.prime:r for r in ledger.rows}
        self.assertEqual(ledger.conductor,4095)
        self.assertEqual([r.prime for r in ledger.rows],[3,5,7,13])
        self.assertEqual(rows[5].prior,Fraction(4,5))
        self.assertEqual(rows[5].forcing,Fraction(0))
        self.assertEqual(rows[5].local_winding,12)
        self.assertTrue(rows[5].inherited_without_forcing)
        self.assertEqual(ledger.literal_carry,2)
        self.assertEqual((ledger.source_integer_offset,ledger.local_winding_sum,
                          ledger.next_global_winding-16*ledger.prior_global_winding),(-2,18,-14))
        self.assertNotEqual(ledger.source_integer_offset+ledger.local_winding_sum,ledger.literal_carry)

    def test_same_three_adic_residue_different_inherited_five_residue(self):
        # The genuine n=2 precursor has 1/3 and 4/5 local additive fractions.
        # Varying p=5 only is a synthetic reference state, NOT the actual zero seed.
        carries=[]
        for j in range(5):
            x=(Fraction(1,3)+Fraction(j,5))%1
            carries.append(carry_ledger(x,forcing(2),13).literal_carry)
        self.assertEqual(carries,[5,8,11,15,2])

    def test_prime_power_not_just_prime(self):
        ledger=original_carry_ledger(2,states=self.states)
        p3=ledger.rows[0]
        self.assertEqual(p3.power,9)
        self.assertEqual(p3.forcing,Fraction(7,9))
        self.assertNotEqual((p3.forcing*3).denominator,1)
        self.assertEqual(p3.local_winding,6)

    def test_zero_and_sixteen_carries_not_reduced_mod_sixteen(self):
        Q=819
        x=Fraction(Q-1,Q)
        L=carry_ledger(x,forcing(2),13)
        self.assertEqual(L.literal_carry,16)
        self.assertNotEqual(L.literal_carry%16,L.literal_carry)

    def test_first_source_step_has_large_forcing_and_nontrivial_global_wrap(self):
        L=original_carry_ledger(1,states=self.states)
        self.assertEqual(L.forcing,Fraction(47,15))
        self.assertEqual(L.literal_carry,3)
        self.assertEqual(L.source_integer_offset,2)
        self.assertEqual(L.next_global_winding,1)

    def test_completed_digit_certified_for_all_32_source_steps(self):
        for n in range(1,33):
            digit,literal,hotspot=original_digit_at_carry(n,depth=12,states=self.states)
            self.assertEqual(hotspot,0)  # finite observations, NOT universal no-hotspot theorem
            self.assertEqual(digit,literal%16)
            # A second independent finite BBP partial and analytic tail enclosure.
            horizon=n+16
            alpha=sum((four_poles(j)/16**j for j in range(1,horizon+1)),Fraction())
            lower=16**n*alpha
            upper=lower+Fraction(16**n,15*16**horizon)*four_poles(horizon+1)
            self.assertEqual(lower.numerator//lower.denominator,
                             upper.numerator//upper.denominator)
            self.assertEqual(digit,(lower.numerator//lower.denominator)%16)

    def test_hotspot_and_16_wrap_need_full_boundary(self):
        r=forcing(2)
        T=Fraction(1,1000)
        for boundary,expected_carry,expected_digit in ((1,0,1),(16,15,0)):
            previous=(Fraction(boundary)-r-T/2)/16
            literal=carry_ledger(previous,r,13).literal_carry
            self.assertEqual(literal,expected_carry)
            recovered,correction=completed_digit_from_tail(16*previous+r,T,T,literal)
            self.assertEqual((recovered,correction),(expected_digit,1))
        with self.assertRaises(ArithmeticError):
            completed_digit_from_tail(Fraction(1999,2000),Fraction(1,10000),Fraction(1,1000),0)

    def test_integral_two_adic_carrier_separate_from_additive_fractional_character(self):
        for n in range(1,33):
            prev=self.states[n-1]
            following=self.states[n]
            result= cross_place_integer_carry(prev,forcing(n),bits=8)
            self.assertEqual(result[0],self.independent[n][1])
            self.assertEqual(result[1],two_adic_integral_residue(following,8))
            self.assertEqual(result[2],int(following)//1%256)
        self.assertEqual(two_adic_integral_residue(Fraction(47,15),8),
                         (47*pow(15,-1,256))%256)
        self.assertNotEqual(two_adic_integral_residue(Fraction(47,15),8),0)

    def test_five_bits_distinguish_carry_zero_and_sixteen(self):
        r=forcing(2)
        Q=819
        x=Fraction(Q-1,Q)
        self.assertEqual(cross_place_integer_carry(x,r,5)[0],16)
        with self.assertRaises(ValueError):
            cross_place_integer_carry(x,r,4)

    def test_source_mutant_rejected(self):
        with self.assertRaises(ValueError):
            bad=list(self.states)
            bad[17]+=Fraction(1,123)
            original_carry_ledger(17,states=tuple(bad))


class CRTBoundaryReferenceTests(unittest.TestCase):
    def test_complete_literal_carry_alphabet(self):
        Q,r=4095,forcing(2)
        counts=consecutive_carry_counts(Q,r)
        self.assertEqual(sum(counts.values()),Q)
        self.assertEqual(min(counts),0)
        self.assertEqual(max(counts),16)
        for k,c in counts.items():
            lo,hi=carry_interval(Q,r,k)
            self.assertEqual(c,hi-lo)
            for m in range(lo,hi):
                self.assertEqual(carry_at_address(Q,r,m),k)

    def test_all_complementary_residues_for_every_interior_carry(self):
        Q,r=4095,forcing(2)
        # p=3^2 separately; p=3^2 and p=5 together; both have L>=17.
        for selected in ((9,),(9,5)):
            M=__import__('math').prod(selected)
            L=Q//M
            self.assertGreaterEqual(L,17)
            for residue in range(M):
                for carry in range(1,16):
                    count, completions=partial_prime_carry_count(Q,r,selected,residue,carry)
                    self.assertEqual(completions,L)
                    self.assertGreaterEqual(count,1)
                    self.assertLess(abs(Fraction(count)-Fraction(L,16)),Fraction(1)+Fraction(1,M))

    def test_reference_counts_are_not_source_carry_statistics(self):
        Q,r=4095,forcing(2)
        actual=original_carry_ledger(2)
        count, L=partial_prime_carry_count(Q,r,(9,),0,2)
        self.assertGreater(count,0)
        self.assertNotEqual(Fraction(count,L),Fraction(int(actual.literal_carry==2)))

    def test_crt_complete_address_and_incomplete_rejection(self):
        for m in range(15):
            self.assertEqual(crt_phase_address(15,{3:m%3,5:m%5}),m)
        with self.assertRaises(ValueError):
            crt_phase_address(15,{3:1})
        with self.assertRaises(ValueError):
            crt_phase_address(15,{3:1,5:1,15:1})

    def test_two_prime_carry_boundary_has_genuine_mixed_rank_three(self):
        # Original n=2 forcing; 15 is the exact previous reduced denominator.
        # This 3x5 matrix is the FULL CRT REFERENCE, not 15 actual BBP times.
        matrix=[]
        for a in range(3):
            row=[]
            for b in range(5):
                m=crt_phase_address(15,{3:a,5:b})
                row.append(int(carry_at_address(15,forcing(2),m)>=8))
            matrix.append(row)
        self.assertEqual([row[:3] for row in matrix],[[0,0,1],[1,0,0],[0,1,0]])
        def det3(M):
            return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
                    -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                    +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
        self.assertEqual(det3([row[:3] for row in matrix]),1)

    def test_carry_slice_count_exact_against_bruteforce(self):
        for Q in (15,45,105):
            for k in range(-1,19):
                lo,hi=carry_interval(Q,forcing(2),k)
                self.assertEqual(hi-lo,sum(carry_at_address(Q,forcing(2),m)==k for m in range(Q)))
                for M in (1,3,5):
                    if Q%M: continue
                    for c in range(M):
                        n,L=partial_prime_carry_count(Q,forcing(2),(M,) if M>1 else (),c,k)
                        self.assertEqual(L,Q//M)
                        self.assertEqual(n,sum(m%M==c and carry_at_address(Q,forcing(2),m)==k for m in range(Q)))

    def test_invalid_scale_and_boundary(self):
        with self.assertRaises(ValueError):
            carry_interval(0,forcing(2),5)  # zero conductor invalid
        with self.assertRaises(ValueError):
            partial_prime_carry_count(4095,forcing(2),(9,9),0,5)
        with self.assertRaises(ValueError):
            partial_prime_carry_count(4095,forcing(2),(7,),7,5)

if __name__=='__main__':
    unittest.main()

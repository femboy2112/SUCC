from __future__ import annotations
import math
import unittest
from fractions import Fraction
from observational_succ.pi_rational_base_carry import (
    base_pair, rational_base_digits, rational_base_value, prefix_from_residue,
    residue_from_prefix, pascal_additive_terms, bbp_forcing,
    bbp_source_states, bbp_newton_coefficient, successor_pascal_source,
    binary_source_carry_stat,
)


def valuation2(q: Fraction) -> int:
    def v(n):
        n = abs(n)
        j = 0
        while n and n % 2 == 0:
            j += 1
            n //= 2
        return j
    return v(q.numerator) - v(q.denominator)


class RationalBaseCarryTests(unittest.TestCase):
    def test_canonical_examples(self):
        self.assertEqual(rational_base_digits(11,11,10),tuple(range(11)))
        self.assertEqual(rational_base_digits(3,3,2),(0,1,2))
        self.assertEqual(rational_base_digits(0,11,10),())
        for p,q in [(3,2),(11,10),(7,3),(5,2)]:
            for N in range(200):
                d=rational_base_digits(N,p,q)
                self.assertEqual(rational_base_value(d,p,q),N)
                if N:self.assertNotEqual(d[-1],0)

    def test_exact_last_digits_mod_p_power_bijection(self):
        for p,q,L in [(3,2,4),(11,10,3),(7,3,3)]:
            mod=p**L
            words=set()
            for n in range(mod):
                word=prefix_from_residue(n,p,q,L)
                self.assertEqual(residue_from_prefix(word,p,q),n)
                self.assertEqual(prefix_from_residue(n+7*mod,p,q,L),word)
                words.add(word)
            self.assertEqual(len(words),mod)

    def test_pascal_additive_presentation(self):
        for p,q in ((3,2),(11,10),(5,4)):
            for n in range(1,100):
                d=rational_base_digits(n,p,q)
                self.assertEqual(sum(pascal_additive_terms(d,p,q),Fraction()),Fraction(n))
        with self.assertRaises(ValueError): pascal_additive_terms((1,2),7,3)

    def test_source_lift_recurrence_independent(self):
        y,C=bbp_source_states(80)
        U=Fraction()
        for n in range(1,81):
            U=16*U+bbp_forcing(n)
            self.assertEqual(U,C[n]+y[n])
            self.assertTrue(0<=y[n]<1)
        self.assertEqual(U.denominator%2,1)

    def test_newton_against_independent_binomial(self):
        U=[Fraction()]
        for n in range(1,42):U.append(16*U[-1]+bbp_forcing(n))
        for k in range(1,42):
            oracle=sum(((-1)**(k-j)*math.comb(k,j)*U[j] for j in range(k+1)),Fraction())
            self.assertEqual(bbp_newton_coefficient(k),oracle)

    def test_sharp_dyadic_val_for_decimal_pascal(self):
        for k in range(1,80):
            x=successor_pascal_source(k,10)
            self.assertEqual(valuation2(x),3*k-k.bit_count()-1)

    def test_operator_transport_equals_binomial_on_base_eleven(self):
        U=[Fraction()]
        for n in range(1,26):U.append(16*U[-1]+bbp_forcing(n))
        # H11=(I+2E)/3. Delta_k H11^j U0 = (H11-I)^k U0.
        for k in range(1,14):
            h=[]
            for j in range(k+1):
                h.append(sum((Fraction(math.comb(j,t)*2**t,3**j)*U[t]
                            for t in range(j+1)),Fraction()))
            result=sum(((-1)**(k-j)*math.comb(k,j)*h[j]
                        for j in range(k+1)), Fraction())
            self.assertEqual(result,successor_pascal_source(k,10))

    def test_uniform_residue_source_probe_exact(self):
        y,_=bbp_source_states(70)
        row=binary_source_carry_stat(y,range(18,69),11)
        self.assertEqual(row['size'],51)
        self.assertEqual(sum(row['residue']),51)
        self.assertEqual(sum(row['sixteen_cells']),51)
        self.assertEqual(row['residue_tv'],Fraction(82,561))
        self.assertEqual(row['joint_vs_product_tv'],Fraction(1658,2601))

    def test_prime11_clock_index_two(self):
        for L in range(1,5):
            m=11**L
            t=5*11**(L-1)
            self.assertEqual(pow(16,t,m),1)
            self.assertEqual((10*11**(L-1))//t,2)
            self.assertNotEqual(pow(16,t//11,m),1) if L>1 else self.assertNotEqual(pow(16,1,m),1)

    def test_source_carry_history_cocycle(self):
        y,C=bbp_source_states(90)
        local=[]
        for n in range(1,91):
            z=16*y[n-1]+bbp_forcing(n)
            local.append(z.numerator//z.denominator)
            for m in (11,121,17):
                self.assertEqual(sum(16**(n-1-j)*local[j] for j in range(n))%m,C[n]%m)

    def test_real_selected_joint_carry_gate_exact(self):
        from observational_succ.pi_rational_base_carry import centered_phase
        p=137;m=(p-1)//8
        y,C=bbp_source_states(4*m+1)
        E=[0,0];Z=[0,0]
        rr={n:bbp_forcing(n) for n in range(m+2,4*m+2)}
        for s in range(m+1,4*m+1):
            for t in range(m+1,4*m+1):
                dplus=centered_phase(y[t+1]-y[s+1])
                if abs(dplus)>Fraction(1,4):continue
                delta=centered_phase(y[t]-y[s])
                k=16*delta+rr[t+1]-rr[s+1]-dplus
                self.assertEqual(k.denominator,1)
                label=int(C[s]%11==C[t]%11)
                E[label]+=1
                Z[label]+=int(k==0)
        self.assertEqual(E,[1108,187]);self.assertEqual(Z,[64,57])

    def test_consecutive_integer_digit_word_general(self):
        for p in range(2,30):
            self.assertEqual(rational_base_digits(p,p,p-1),tuple(range(p)))

    def test_invalid_domains(self):
        for pair in [(10,10),(0,1),(12,8),(True,5),(4,0)]:
            with self.assertRaises(ValueError):base_pair(*pair)
        for action in [lambda:rational_base_digits(-1,11,10),
                       lambda:prefix_from_residue(3,11,10,-1),
                       lambda:residue_from_prefix((11,),11,10),
                       lambda:rational_base_value((11,),11,10),
                       lambda:bbp_forcing(0),
                       lambda:bbp_newton_coefficient(-1),
                       lambda:successor_pascal_source(2,16),
                       lambda:binary_source_carry_stat((Fraction(),),range(0),1)]:
            with self.assertRaises(ValueError): action()

if __name__=='__main__':unittest.main()

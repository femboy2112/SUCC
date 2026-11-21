"""Scoped exact regression tests for digit/routing seam; no pi normality claims."""
from fractions import Fraction
import cmath
import math
import unittest
from digit_remainder import (
    digit_remainder,reverse_branch,four_binary_stages,source_forcing,
    bbp_x_interval,certified_prefix,step_with_memory,original_state,
    walsh_row,norm_of_input_piecewise_constant,branch_norm,walsh_norm, original_root_arc_coordinates
)

class TestDigitRemainder(unittest.TestCase):
    def test_grid_bijection(self):
        for q in (7,16,17,31,64,127,257):
            for p in range(q):
                x=Fraction(p,q)
                d,t=digit_remainder(x)
                self.assertTrue(0<=d<=15 and 0<=t<1)
                self.assertEqual(reverse_branch(d,t),x)

    def test_wrap_at_threshold(self):
        for k in range(16):
            self.assertEqual(digit_remainder(Fraction(k,16)),(k,Fraction(0)))
        self.assertEqual(digit_remainder(Fraction(15,16)+Fraction(1,32)),(15,Fraction(1,2)))

    def test_four_binary_stages(self):
        for q in (9,16,31,101,257):
            for p in range(q):
                x=Fraction(p,q)
                bits,d,res=four_binary_stages(x)
                self.assertEqual(digit_remainder(x),(d,res))
                self.assertTrue(all(bit in (0,1) for bit in bits))
                self.assertEqual(d,8*bits[0]+4*bits[1]+2*bits[2]+bits[3])

    def test_memory_invariant(self):
        for q in (7,17,31,101):
            for p in range(q):
                x=Fraction(p,q)
                m,length,r=0,0,x
                for _ in range(6):
                    m,length,r=step_with_memory(m,length,r)
                    self.assertEqual(original_state(m,length,r),x)

    def test_source_exact_poles(self):
        self.assertEqual(source_forcing(1),Fraction(47,15))
        for n in range(1,70):
            self.assertGreater(source_forcing(n),source_forcing(n+1))
            self.assertGreater(source_forcing(n),0)

    def test_bbp_certified_digits(self):
        digits=certified_prefix(12,12)
        self.assertEqual(''.join(format(d,'X') for d in digits),'3243F6A8885A')
        xlo,xhi=bbp_x_interval(12)
        self.assertLess(xlo,xhi)
        self.assertLess(xhi-xlo,Fraction(1,16**12))

    def test_unproven_short_source_not_claimed(self):
        with self.assertRaises(ValueError):
            certified_prefix(12,3)

    def test_seed_matters(self):
        lo,hi=bbp_x_interval(12)
        self.assertEqual(digit_remainder(Fraction(0)),(0,Fraction(0)))
        self.assertEqual(digit_remainder(lo)[0],3)
        self.assertEqual(digit_remainder(hi)[0],3)
        # The wrong seed s=-pi/16 gives the perfectly locked completed 0;
        # source-only interferometer data do not detect that seed alteration.

    def test_hilbert_branch_isometry_exact(self):
        for shift in range(5):
            a=tuple(Fraction((d+shift)**2-11, d+2) for d in range(16))
            original=norm_of_input_piecewise_constant(a)
            self.assertEqual(original,branch_norm(a))
            self.assertEqual(original,walsh_norm(a))

    def test_walsh_orthogonality(self):
        for k in range(16):
            for l in range(16):
                val=sum(((-1 if ((k & d).bit_count()&1) else 1)*
                         (-1 if ((l & d).bit_count()&1) else 1) for d in range(16)))
                self.assertEqual(val,16 if k==l else 0)

    def test_distribution_conditional(self):
        # Uniform density f=1 yields equal branch energies, but a deterministic
        # point or a nonuniform f need not have equal digit probabilities.
        uniform=tuple(Fraction(1) for _ in range(16))
        self.assertEqual(branch_norm(uniform),1)
        self.assertEqual(tuple((c/4)**2 for c in uniform),(Fraction(1,16),)*16)
        pointlike=tuple(Fraction(4 if d==3 else 0) for d in range(16))
        self.assertEqual(branch_norm(pointlike),1)
        self.assertEqual(sum((Fraction(c,4)**2 for c in pointlike if c)),1)

    def test_hilbert_norm_identity_for_general_test(self):
        # Parseval in a 16-branch exact rational subspace.
        a=tuple(Fraction((-1)**d*(d+1),d+2) for d in range(16))
        self.assertEqual(sum((walsh_row(k,a)**2 for k in range(16)),Fraction()),
                         16*sum((v*v for v in a),Fraction()))

    def test_phasor_digit_transmission(self):
        # The exact algebraic identity is a lift identity; these complex checks
        # merely calibrate signs, not a source-selected Weyl estimate.
        for q in (7,17,43):
            for p in range(q):
                x=Fraction(p,q)
                d,res=digit_remainder(x)
                for h in (1,3,15):
                    lhs=cmath.exp(2j*math.pi*h*float(x))
                    rhs=cmath.exp(2j*math.pi*h*d/16)*cmath.exp(2j*math.pi*h*float(res)/16)
                    self.assertLess(abs(lhs-rhs),3e-14)

    def test_plain_mirror_two_cycle(self):
        L=Fraction(7,3)
        for s in (Fraction(0),Fraction(1,3),Fraction(5,6),L):
            self.assertEqual(L-(L-s),s)
        # BBP begins 3,2,4,3, not a length-two stationary mirror orbit.
        self.assertEqual(certified_prefix(4,8),(3,2,4,3))

    def test_authentic_H_roots_on_digit_seams(self):
        # Chart: upper endpoint 0, left interior roots 1/4 and 3/4,
        # lower endpoint 1 (which is EXCLUDED from the half-open digit domain).
        roots=original_root_arc_coordinates()
        self.assertEqual(roots,(Fraction(0),Fraction(1,4),Fraction(3,4),Fraction(1)))
        self.assertEqual(tuple(16*x for x in roots),(0,4,12,16))
        self.assertEqual(digit_remainder(roots[1]),(4,Fraction(0)))
        self.assertEqual(digit_remainder(roots[2]),(12,Fraction(0)))
        with self.assertRaises(ValueError):digit_remainder(roots[3])
        for x in roots[1:3]:
            delta=Fraction(1,10000)
            self.assertNotEqual(digit_remainder(x-delta)[0],digit_remainder(x+delta)[0])

    def test_validation_guards(self):
        with self.assertRaises(ValueError):digit_remainder(Fraction(-1,10))
        with self.assertRaises(ValueError):digit_remainder(Fraction(1))
        with self.assertRaises(ValueError):reverse_branch(16,Fraction(0))
        with self.assertRaises(ValueError):reverse_branch(1,Fraction(1))
        with self.assertRaises(ValueError):walsh_row(16,tuple([Fraction(0)]*16))
        with self.assertRaises(ValueError):bbp_x_interval(-1)

if __name__=='__main__':
    unittest.main()

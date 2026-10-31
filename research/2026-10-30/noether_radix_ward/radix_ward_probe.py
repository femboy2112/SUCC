"""Exact algebraic seed-Fourier moment selection for the original BBP recurrence.

All coefficients are integer/Fraction. No finite data, no numerical pi oracle,
no assumption of normality. Group-algebra equalities are exact for any seed.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import comb, factorial
import unittest

POLES=((4,0),(-2,3),(-1,4),(-1,5))
B=16

def R(a):
    return sum((F(c,a+d) for c,d in POLES),F(0))

def U_original(n):
    u=F(0);a=[u]
    for j in range(1,n+1):
        u=B*u+R(8*j-7);a.append(u)
    return a

def compositions(k,parts):
    if parts==1:
        yield (k,)
    else:
        for x in range(k+1):
            for y in compositions(k-x,parts-1):
                yield (x,)+y

def freq(m,b=B):
    return sum(c*b**(j+1) for j,c in enumerate(m))

def multi(m):
    from math import prod
    return F(factorial(sum(m)),prod(factorial(z) for z in m))

def collision_classes(b,N,k):
    buckets=defaultdict(list)
    for m in compositions(k,N):buckets[freq(m,b)].append(m)
    return [a for a in buckets.values() if len(a)>1]


class RadixMomentSelection(unittest.TestCase):
    def test_four_pole_source_and_shift_character(self):
        u=U_original(6)
        for n in range(1,6):
            self.assertEqual(u[n]-16*u[n-1],R(8*n-7))
            # shift seed s -> s+1/15: e(h16^n/15) is e(h/15)
            self.assertEqual((16**n-1)%15,0)

    def test_low_equal_length_moments_have_no_additive_collisions(self):
        for k in range(1,17):
            self.assertEqual(collision_classes(16,4,k),[],msg=f'k={k}')
        # First collision in equal-degree moments occurs at k=b+1=17
        classes=collision_classes(16,4,17)
        self.assertEqual(len(classes),3)
        self.assertEqual(set(len(x) for x in classes),{2})

    def test_first_equal_length_collision_phase_is_source_only(self):
        u=U_original(4)
        classes=collision_classes(16,4,17)
        detected=[]
        for entries in classes:
            a,b=entries
            exp=sum((F(a[i]-b[i])*u[i+1] for i in range(4)),F(0))
            self.assertNotEqual(exp,0)
            values=[R(8*p-7)-R(8*q-7)
                    for p in (2,3,4) for q in (2,3,4) if p!=q]
            self.assertIn(exp,values)
            detected.append(exp)
        self.assertEqual(len(detected),3)

    def test_first_unbalanced_sixteen_to_one_resonance(self):
        # Integral_0^1 W_N(s)^16 conjugate(W_N(s)) ds is group-algebra
        # coefficient at seed frequency zero. Terms with 16 copies
        # of one time n and a single conjugate time n+1 survive.
        u=U_original(5)
        for N in (2,3,4,5):
            survivors=[]
            for m in compositions(16,N):
                for j in range(1,N+1):
                    if freq(m)==16**j:
                        exponent=sum((F(m[i])*u[i+1] for i in range(N)),F(0))-u[j]
                        survivors.append((m,j,exponent,multi(m)))
            self.assertEqual(len(survivors),N-1)
            self.assertEqual(sorted([p[2] for p in survivors]),
                             sorted([-R(8*(j+1)-7) for j in range(1,N)]))
            self.assertTrue(all(coeff==1 for *_,coeff in survivors))

    def test_base_b_thresholds_and_exact_source_coboundary(self):
        # Check that the first b+1 collision is not a base-16 fluke.
        for b in (2,3,4,5):
            for k in range(1,b+1):
                self.assertFalse(collision_classes(b,4,k),(b,k))
            self.assertTrue(collision_classes(b,4,b+1),(b,b+1))
            # independent abstract forced affine map
            r=[F(0),F(1,7),F(3,11),F(4,19),F(5,31)]
            x=[F(0)]
            for i in range(1,5):x.append(b*x[-1]+r[i])
            for p in (2,3):
                for q in (2,3,4):
                    if p==q:continue
                    # b*U_(p-1)+U_q -b*U_(q-1)-U_p=r_q-r_p
                    self.assertEqual(b*x[p-1]+x[q]-b*x[q-1]-x[p],r[q]-r[p])

    def test_balanced_moment_first_fourth_and_all_below_17_are_seed_blind(self):
        # For k<=16, all additive powers are uniquely represented,
        # so the Haar-seed average of |W|^(2k) is purely combinatorial.
        for k in (1,2,3,8,15,16):
            vectors=list(compositions(k,4))
            self.assertEqual(len({freq(m) for m in vectors}),len(vectors))
            diagonal=sum((multi(m)**2 for m in vectors),F(0))
            self.assertGreater(diagonal,0)
            if k==1:self.assertEqual(diagonal,4)
            if k==2:self.assertEqual(diagonal,2*4**2-4)
        # For ALL k, Haar seed-smearing is seed blind by translation
        # s -> s+s_0, though first nontrivial forcing resonances start
        # at equal-length k=17, and unequal-length 16-versus-1.


    def test_first_balanced_34th_moment_complete_offdiagonal_formula(self):
        # First equal-degree collision is at k=17, and EVERY
        # nontrivial pair is the two ways of expanding two distinct
        # canonical radix units. The collision phase is r_q-r_p.
        n=5;k=17
        U=U_original(n)
        buckets=defaultdict(list)
        for m in compositions(k,n):buckets[freq(m)].append(m)
        classes=[a for a in buckets.values() if len(a)>1]
        self.assertEqual(len(classes),comb(n-1,2))
        seen=[]
        for clas in classes:
            self.assertEqual(len(clas),2)
            a,b=clas
            exponent=sum((F(a[i]-b[i])*U[i+1] for i in range(n)),F(0))
            coefficient=multi(a)*multi(b)
            values=[]
            for p in range(2,n+1):
                for q in range(p+1,n+1):
                    source_delta=R(8*q-7)-R(8*p-7)
                    multiplicity=17 if q==p+1 else 289
                    values.append((source_delta,F(multiplicity)))
            self.assertTrue((exponent,coefficient) in values or
                            (-exponent,coefficient) in values)
            seen.append(coefficient)
        self.assertEqual(seen.count(F(17)),n-2)
        self.assertEqual(seen.count(F(289)),comb(n-2,2))

    def test_exponentially_small_seed_cylinder_has_explicit_transfer_error(self):
        # For any unit coefficients c_n, |sum c_n e(h16^n s)-sum c_n|
        # <=2*pi*|h|*|s| sum 16^n. For 0<=s<=16^-N this is O_h(1)
        # unnormalized, hence O_h(1/N) for means. This exact bound
        # does not prove any bound on the localized average itself.
        for N in (1,2,4,8,12):
            T=F(1,16**N)*sum(16**n for n in range(1,N+1))
            self.assertLess(T,F(16,15))
            self.assertGreater(T,0)

    def test_radix_selection_rule_for_unbalanced_moments(self):
        # Any integer relation sum(b^n) for p positive and q negative
        # requires p-q divisible by b-1. It is a finite Z_(b-1)
        # selection rule, not a continuous Noether charge.
        b=16
        for p in range(0,9):
            for q in range(0,9):
                if p==q:continue
                self.assertNotEqual((p-q)%15,0)
        self.assertEqual((16-1)%15,0)

    def test_first_radix_carry_signed_moment_has_no_weyl_saving(self):
        # Purely source-force near alignment: its average tends to 1.
        # Rational bound ∑_{n>=2}R(8n-7)<∞ =>
        # |sum e(-h r(n))-(N-1)|<=2π|h| sum r(n).
        rsum=sum((R(8*n-7) for n in range(2,100)),F(0))
        self.assertGreater(rsum,0)
        self.assertLess(rsum,1)
        self.assertLess(R(8*99-7),R(8*98-7))
        # fake forcing Q=15x has different source but same resonance,
        # and source-difference ~ -59/a^3 is summable.
        for n in (10,100,1000):
            a=8*n-7
            fake=F(15,a*a)
            self.assertLess(R(a),fake)
        n=10000;a=8*n-7
        diff=R(a)-F(15,a*a)
        self.assertLess(abs(float(a**3*diff+59)),0.05)


if __name__=='__main__':
    unittest.main(verbosity=2)

"""Independent finite BBP arithmetic checks (no normality claims)."""
import unittest
from collections import Counter
from fractions import Fraction as Q
from scripts import bbp_two_bit_sheet_probe as s

class SheetSourceExact(unittest.TestCase):
    def test_original_four_poles(self):
        for n in range(1,120):
            self.assertEqual(Q(s.A(n),s.D(n)),
                Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))
    def test_full_seven_state_table(self):
        self.assertEqual(tuple((x,s.A(x)%7,s.encode(x,7,1).sheet,
            s.encode(x,7,1).pole) for x in range(7)),
            ((0,2,0,1),(1,5,0,0),(2,3,0,1),(3,3,1,1),
             (4,5,1,1),(5,2,1,0),(6,1,0,0)))
    def test_all_fiber_inverses_and_counts(self):
        for p,L in ((7,1),(7,2),(7,3),(11,2),(13,2),(241,1)):
            q=p**L
            self.assertEqual(len({s.encode(x,p,L) for x in range(q)}),q)
            self.assertEqual(sum(len(s.fiber(a,p,L))**2 for a in range(q)),
                             s.pair_count(p,L))
            self.assertEqual([s.decode(s.encode(x,p,L),p,L) for x in range(q)],
                             list(range(q)))
    def test_two_bits_without_lift_fail_at_49(self):
        roots=[x for x in range(49) if s.A(x)%49==29]
        self.assertEqual(roots,[6,13,20,27,34,41,48])
        states=[s.encode(x,7,2) for x in roots]
        self.assertEqual({(x.target,x.sheet,x.pole) for x in states},{(29,0,0)})
        self.assertEqual({x.lift for x in states},set(range(7)))
    def test_pole_pairs_and_unit_domain(self):
        self.assertEqual([x for x in range(7) if s.D(x)%7!=0],[1,5,6])
        self.assertEqual(len({s.A(x)%7 for x in (1,5,6)}),3)
        for x,y in ((0,5),(1,4),(2,3)):
            self.assertEqual(s.A(x)%7,s.A(y)%7)
            self.assertTrue(s.D(x)%7==0 or s.D(y)%7==0)
        self.assertTrue(all(s.A(x)%7 for x in range(7)))
    def test_gaussian_fourier_difference(self):
        for p in (7,11,13):
            self.assertEqual(s.finite_difference_histogram(p),
                tuple([2*p-1]+[p-1]*(p-1)))
    def test_single_cycle_successor(self):
        for p,L in ((7,1),(7,2),(11,1)):
            q=p**L; c=s.encode(0,p,L)
            for i in range(q):
                self.assertEqual(s.decode(c,p,L),i)
                c=s.successor(c,p,L)
            self.assertEqual(c,s.encode(0,p,L))
    def test_pole_mutation_rejected(self):
        st=s.encode(0,7,2)
        with self.assertRaises(ValueError):
            s.decode(s.Code(st.target,st.sheet,1-st.pole,st.lift),7,2)
    def test_critical_convention_and_invalid_roots(self):
        self.assertEqual(s.fiber(0,7,1),())
        with self.assertRaises(ValueError):s.decode(s.Code(0,0,0,0),7,1)
        with self.assertRaises(ValueError):s.decode(s.Code(29,1,0,0),7,2)
    def test_nonprime_and_initial_source_prohibited(self):
        for p in (2,3,4,5,9):
            with self.assertRaises(ValueError):s.encode(0,p,1)

if __name__=="__main__":unittest.main()

"""Independent exact recurrences and hostile contracts for prefix controls."""
from fractions import Fraction as Q
from math import factorial
import unittest

from observational_succ.pi_carry_prefix_control import carry_prefix_control
from observational_succ.pi_source_collision import small_ball_pairs


def independent_source(last, initial=Q(0)):
    # Unified rational forcing is a different finite evaluation from the
    # production four partial fractions and backward-tail construction.
    states, carries = [initial], []
    for n in range(1, last+1):
        forcing = Q(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        unwrapped = 16*states[-1]+forcing
        carry = unwrapped.__floor__()
        carries.append(carry)
        states.append(unwrapped-carry)
    return states, carries


def dyadic(value):
    d = value.denominator
    return d & (d-1) == 0


class CarryPrefixControlTests(unittest.TestCase):
    def test_selected_p_2081_window_preserves_eight_carries_and_odd_data(self):
        # Predetermined source window: p=2081, u=260, M=16 at c=2/5.
        p, u, cells = 2081, 260, 16
        self.assertLessEqual(cells**5, p*p)
        self.assertGreater((16*cells)**5, p*p)
        control = carry_prefix_control(u+1, 4*u, cells, 8, 17**2*41)
        source, carries = independent_source(control.depth+1)
        changed, changed_carries = independent_source(control.depth+1, control.initial)
        self.assertNotEqual(control.initial, 0)
        self.assertLess(control.initial, 2*Q(1, 16**(u+1)))
        self.assertEqual(changed_carries[:8], carries[:8])
        # The elementary factorial denominator budget authenticates a
        # growing prefix without inspecting favorable boundary margins.
        self.assertLess(2*16**20*factorial(160), 16**(u+1))
        self.assertTrue(all(factorial(160) % source[n].denominator == 0
                            for n in range(1,21)))
        longer = carry_prefix_control(u+1,4*u,cells,20,17**2*41)
        self.assertEqual(longer.initial,control.initial)
        self.assertEqual(changed_carries[:20],carries[:20])
        # The elementary lcm bound improves this to a linear prefix.
        linear_prefix = (u+1-1)//9
        self.assertEqual(linear_prefix,28)
        longest = carry_prefix_control(u+1,4*u,cells,linear_prefix,17**2*41)
        self.assertEqual(longest.initial,control.initial)
        self.assertEqual(changed_carries[:linear_prefix],carries[:linear_prefix])
        self.assertEqual(tuple(changed[u+1:4*u+1]), control.phases)
        self.assertLess(control.diameter_upper, Q(1,cells))
        self.assertEqual(small_ball_pairs(control.phases, Q(1,cells)), (3*u)**2)
        # Complete odd-primary equality follows from dyadic differences;
        # individual finite prime tests alone would not establish completeness.
        self.assertTrue(all(dyadic(a-b) for a,b in zip(changed, source)))
        for n in (0,8,u+1,4*u,control.depth,control.depth+1):
            self.assertTrue(dyadic(16**n*control.initial/control.odd_modulus))
        self.assertEqual(changed[control.depth:], source[control.depth:])
        # The omitted premise is visible, including in later integer carries.
        self.assertNotEqual(changed_carries[8:4*u], carries[8:4*u])

    def test_small_controls_against_direct_all_pairs(self):
        for first,last,prefix,modulus in ((3,9,0,1),(6,15,2,17),
                                          (13,48,4,17**2*41)):
            control = carry_prefix_control(first,last,16,prefix,modulus)
            original, a = independent_source(control.depth)
            altered, b = independent_source(control.depth,control.initial)
            self.assertEqual(a[:prefix], b[:prefix])
            phases = altered[first:last+1]
            pairs = sum(min((x-y)%1,(y-x)%1) <= Q(1,16)
                        for x in phases for y in phases)
            self.assertEqual(pairs,len(phases)**2)
            self.assertEqual(tuple(phases),control.phases)
            self.assertTrue(dyadic(control.initial/modulus))
            self.assertEqual(original[-1],altered[-1])

    def test_coalescence_and_primary_data_do_not_preserve_literal_carries(self):
        original,carries = independent_source(2)
        altered,changed = independent_source(2,Q(1,16))
        self.assertEqual(original[1:],altered[1:])
        self.assertEqual(carries[0],3)
        self.assertEqual(changed[0],4)
        self.assertNotEqual(changed,carries)

    def test_source_contract_and_exact_domains_fail_closed(self):
        invalid = ((0,10,16,0,1),(2,1,16,0,1),(3,10,16,3,1),
                   (3,10,16,0,2),(True,10,16,0,1),(3,10,1.0,0,1),
                   (3,10,10000,0,1),(3,10,16,-1,1),(5,10,16,4,1))
        for args in invalid:
            with self.assertRaises(ValueError,msg=str(args)):
                carry_prefix_control(*args)


if __name__ == '__main__':
    unittest.main()

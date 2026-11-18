"""Exact source-anchored null seed and observation-quotient controls.

The null-source input is defined relative to a fixed forcing and a transported
origin; zero injected seed does not mean random/normal BBP digits.
"""
import unittest
from fractions import Fraction as F


def forcing(n):
    if n < 1:
        raise ValueError('source clock must be >=1')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def source_path(n, seed=F(0), source=forcing):
    state=F(seed)
    path=[state]
    for j in range(1,n+1):
        state=16*state+source(j)
        path.append(state)
    return path


def forced_path(n, source=forcing):
    return source_path(n,F(0),source)


def seed_certificate(n,state,source=forcing):
    return (F(state)-forced_path(n,source)[n])/16**n

class NullSeedSourceAnchorTests(unittest.TestCase):
    def test_original_zero_selected_full_recurrence(self):
        path=source_path(48)
        self.assertEqual(path[0],0)
        for n in range(1,49):
            self.assertEqual(path[n],16*path[n-1]+forcing(n))
            self.assertEqual(seed_certificate(n,path[n]),0)
            direct=sum((forcing(j)*16**(n-j) for j in range(1,n+1)),F(0))
            self.assertEqual(path[n],direct)

    def test_all_seed_invariants_constant(self):
        base=source_path(30)
        for seed in (F(0),F(3,7),-F(1,13),F(7,16**5)):
            path=source_path(30,seed)
            for n in range(31):
                self.assertEqual(seed_certificate(n,path[n]),seed)
                self.assertEqual(path[n]-base[n],16**n*seed)

    def test_seed_translation_natural_with_successor(self):
        for n in range(1,19):
            for s in (F(1,17),F(-3,8),F(0)):
                u=source_path(n)[n]
                rhs=16*(u+16**n*s)+forcing(n+1)
                lhs=16*u+forcing(n+1)+16**(n+1)*s
                self.assertEqual(lhs,rhs)

    def test_chart_shift_can_change_numerical_zero_but_not_transported_excess(self):
        s=F(0)
        b=lambda n:F(2*n*n+3)
        shifted_path=[u+b(n) for n,u in enumerate(source_path(26,s))]
        shifted_forcing=lambda n:forcing(n)+b(n)-16*b(n-1)
        shifted_ref=source_path(26,b(0),shifted_forcing)
        self.assertEqual(shifted_ref,shifted_path)
        for n in range(27):
            # The numerical state at clock zero is nonzero in the new chart,
            # but the source reference origin transforms with it.
            self.assertEqual(shifted_path[n]-shifted_ref[n],0)
            self.assertEqual(seed_certificate(n,shifted_path[n],shifted_forcing),b(0))
            self.assertEqual(seed_certificate(n,shifted_path[n],shifted_forcing)-b(0),0)

    def test_changed_seed_remains_changed_after_gauge_transport(self):
        b=lambda n:F(n*n+1,3)
        for seed in (F(1,5),F(-7,13)):
            path=source_path(17,seed)
            shifted_forcing=lambda n:forcing(n)+b(n)-16*b(n-1)
            for n in range(18):
                chart_u=path[n]+b(n)
                excess=seed_certificate(n,chart_u,shifted_forcing)-b(0)
                self.assertEqual(excess,seed)

    def test_phase_alias_is_not_source_invariant(self):
        for m in (1,3,7):
            s=F(3,16**m)
            z=source_path(m+5,s)
            base=source_path(m+5)
            for n in range(m,m+6):
                self.assertEqual((z[n]-base[n])%1,0)
                self.assertEqual(seed_certificate(n,z[n]),s)

    def test_zero_seed_does_not_force_randomness_for_arbitrary_forcing(self):
        zero_forcing=lambda n:F(0)
        integer_forcing=lambda n:F(1)
        for source in (zero_forcing,integer_forcing):
            path=source_path(12,F(0),source)
            self.assertTrue(all(seed_certificate(n,path[n],source)==0 for n in range(13)))
            self.assertTrue(all((u%1)==0 for u in path))

    def test_coarse_classical_projection_can_hide_future_state(self):
        # Deterministic carrier (a,h) -> (h,a), readout P(a,h)=a.
        # Two actual states with P=0 but different next P values.
        step=lambda state:(state[1],state[0])
        a,b=(F(0),F(1)),(F(0),F(2))
        self.assertEqual(a[0],b[0])
        self.assertNotEqual(step(a)[0],step(b)[0])
        self.assertEqual(step(step(a)),a)
        self.assertEqual(step(step(b)),b)

    def test_seed_derivative_does_not_add_forcing_facts(self):
        # k-th seed variation of U_n is zero for all k>=2, and
        # the first derivative is 16**n for any forcing.
        for n in (0,1,4,17):
            base=source_path(n)[n]
            step=F(1,123)
            first=(source_path(n,step)[n]-base)/step
            self.assertEqual(first,16**n)
            second=source_path(n,step)[n]-2*base+source_path(n,-step)[n]
            self.assertEqual(second,0)


if __name__ == '__main__':
    unittest.main()

"""Independent source and projection oracles; no infinite trend assertions."""
from dataclasses import replace
from fractions import Fraction as Q
import unittest

from observational_succ.prime_clock_resonance import (
    source_passport, project_period, pairing, projection_certificate,
    forced_coherence_gap, uniform_coherence_gap_floor,
)
from observational_succ.succ_internal_matrix_walk import PhasePoly
from observational_succ.cyclotomic_selected_source import character_mean
from observational_succ.bbp_natural_carrier import orbit_state


def collapsed(n):
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


class SourceProjection(unittest.TestCase):
    def test_unwrapped_source_independent_natural_and_closed_sum(self):
        for p in (17, 41, 73, 113):
            x = source_passport(p, -2)
            for n, state in enumerate(x.prefix):
                self.assertEqual(state, orbit_state(n).rational)
                self.assertEqual(state, sum((16**(n-j)*collapsed(j) for j in range(1, n+1)), Q()))
            self.assertTrue(x.validate())

    def test_passport_rejects_mutated_source_lift_and_initial(self):
        x = source_passport(17)
        for index in (0, 1, 4, 8):
            prefix = list(x.prefix)
            prefix[index] += 1
            with self.assertRaises(ValueError):
                replace(x, prefix=tuple(prefix)).validate()
        with self.assertRaises(ValueError):
            replace(x, order=1).validate()
        with self.assertRaises(ValueError):
            replace(x, complement=tuple(Q(-4*pow(16,t,17),17) % 1 for t in range(6))).validate()

    def test_composites_exceptions_and_bad_frequencies(self):
        for p in (3, 5, 9, 25, 65, 81, True):
            with self.assertRaises(ValueError):
                source_passport(p)
        for h in (0, True, 1.0):
            with self.assertRaises(ValueError):
                source_passport(17, h)
        # Local trivial character is legal algebra, not eligible BGK input.
        self.assertTrue(source_passport(17, 17).validate())

    def test_all_divisors_exact_three_sector_certificate(self):
        for p in (17, 41):
            x = source_passport(p)
            for d in range(1, x.delta+1):
                if x.delta % d:
                    continue
                c = projection_certificate(x, d)
                direct = sum((PhasePoly.monomial(s) for s in x.states), PhasePoly.zero())/x.delta
                self.assertEqual(c['full'], direct)
                self.assertEqual(c['full'], c['low']+c['interaction'])
                self.assertEqual(c['invisible_pairing'], PhasePoly.zero())
                self.assertEqual(sum(c['energies'], PhasePoly.zero()), PhasePoly.one())

    def test_d_not_dividing_clock_and_unsynchronized_rejection(self):
        x = source_passport(113)
        c = projection_certificate(x, 3)
        self.assertEqual((x.order, c['period'], c['suborder'], c['repeats']), (7,7,7,6))
        self.assertEqual((c['coset_period'],c['coset_repeats']), (21,2))
        self.assertEqual(c['interaction'],projection_certificate(x,1)['interaction'])
        with self.assertRaises(ValueError):
            projection_certificate(source_passport(17), 4)

    def test_general_projection_selfadjoint_idempotent(self):
        a = tuple(PhasePoly.monomial(Q(j*j, 11)) for j in range(12))
        b = tuple(PhasePoly.monomial(Q(j, 7), (-1)**j) for j in range(12))
        for d in (1,2,3,4,6,12):
            pa, pb = project_period(a,d), project_period(b,d)
            self.assertEqual(project_period(pa,d),pa)
            self.assertEqual(pairing(pa,b,True),pairing(a,pb,True))

    def test_gcd_collapse_independent_arbitrary_vectors(self):
        from math import gcd
        a=tuple(PhasePoly.monomial(Q(j*j+2*j,13)) for j in range(12))
        for d in (1,2,3,4,6,12):
            for L in (1,2,3,4,6,12):
                expected=project_period(a,gcd(d,L))
                self.assertEqual(project_period(project_period(a,d),L),expected)
                self.assertEqual(project_period(project_period(a,L),d),expected)

    def test_fake_antiphase_keeps_resonance_after_compression(self):
        x = source_passport(41)
        u = tuple(PhasePoly.monomial(a) for a in x.primary)
        v = tuple(a.star() for a in u)
        self.assertEqual(pairing(u,v),PhasePoly.one())
        self.assertEqual(project_period(v,x.order),v)
        # A large period, not a low-complexity complement.
        self.assertNotEqual(project_period(v,1),v)


class ForcedGap(unittest.TestCase):
    def test_gap_matches_independent_pair_variance(self):
        for p in (17,41,73,97,113):
            m=(p-1)//8
            for h in (1,-2,5):
                values=[h*collapsed(n) for n in range(m+2,4*m+1)]
                pairs=Q()
                for i in range(len(values)):
                    for j in range(i):
                        z=(values[i]-values[j]) % 1
                        pairs+=min(z,1-z)**2
                self.assertEqual(forced_coherence_gap(p,h),8*pairs/(289*3*m*(3*m-1)))
                self.assertGreater(forced_coherence_gap(p,h),0)

    def test_explicit_uniform_floor_fresh_primes(self):
        for p in (97,113,193,257,337):
            for h in (1,-3,7):
                self.assertGreaterEqual(forced_coherence_gap(p,h), uniform_coherence_gap_floor(p,h))
        with self.assertRaises(ValueError):
            uniform_coherence_gap_floor(17)
        with self.assertRaises(ValueError):
            uniform_coherence_gap_floor(97,145)

    def test_certified_actual_window_respects_gap(self):
        for p in (17,41):
            x=source_passport(p)
            box=character_mean(s % 1 for s in x.states)
            self.assertLess(box.modulus_squared_upper(), (1-forced_coherence_gap(p))**2)

    def test_fixed_frequency_is_essential(self):
        # A finite p can have all source phases aliased by an enormous h.
        from math import lcm
        x=source_passport(17)
        h=lcm(*(s.denominator for s in x.prefix))
        self.assertEqual(forced_coherence_gap(17,h),0)
        self.assertTrue(all((h*s).denominator==1 for s in x.states))


if __name__ == '__main__':
    unittest.main()

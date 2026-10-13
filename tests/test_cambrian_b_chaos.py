"""Independent representations and hostile controls for Cambrian B."""
from fractions import Fraction as F
from itertools import product
from random import Random
import unittest

from observational_succ import cambrian_b_chaos as b
from observational_succ.logistic_observer_tree import (
    chebyshev_mode, transfer_depth, forward_pullback_polynomial, tent, equilibrium_mean,
)
from observational_succ.misiurewicz_phase_quotient import ALPHA


def dense_modes(values):
    out = [F(0)]
    for k,v in values.items():
        coeff = chebyshev_mode(k)
        if len(out)<len(coeff): out.extend([F(0)]*(len(coeff)-len(out)))
        for j,c in enumerate(coeff): out[j]+=v*c
    while len(out)>1 and out[-1]==0: out.pop()
    return tuple(out)


class TransferTests(unittest.TestCase):
    def test_sparse_transfer_against_independent_dense_power_recurrence(self):
        rng=Random(71311)
        for _ in range(75):
            values={rng.randrange(21):F(rng.randrange(-4,5),rng.randrange(1,7))
                    for _ in range(6)}
            for n in range(5):
                self.assertEqual(dense_modes(b.transfer(values,n)),
                                 transfer_depth(dense_modes(values),n))

    def test_advancing_identity_dense_pullback_and_transfer(self):
        values={0:F(2),1:F(1,3),3:F(-2,7)}
        for n,m in product(range(5),range(4)):
            dense=transfer_depth(forward_pullback_polynomial(dense_modes(values),m),n)
            self.assertEqual(dense_modes(b.advancing(values,n,m)),dense)

    def test_no_operator_norm_decay_high_mode_holdout(self):
        for n in (0,1,5,13,38,70):
            high={5*(1<<n):F(1)}
            self.assertEqual(b.transfer(high,n),{5:F(1)})
            self.assertEqual(b.l2_norm_square(high),b.l2_norm_square(b.transfer(high,n)))

    def test_orthogonality_from_independent_exact_arcsine_power_moments(self):
        for k,j in product(range(8),repeat=2):
            a,c=chebyshev_mode(k),chebyshev_mode(j)
            out=[F(0)]*(len(a)+len(c)-1)
            for i,x in enumerate(a):
                for h,y in enumerate(c): out[i+h]+=x*y
            expected=F(0) if k!=j else F(1 if k==0 else 1,1 if k==0 else 2)
            self.assertEqual(equilibrium_mean(out),expected)

    def test_geometric_noncompletion_all_tested_depths(self):
        for ratio in (F(1,5),F(1,2),F(9,10),F(37,41)):
            for n in (0,1,2,10,37):
                witness=b.geometric_lacunary(ratio,n)
                self.assertGreater(witness['residual_sup_norm'],0)
                self.assertEqual(witness['residual_sup_norm']/witness['initial_sup_norm'],ratio**n)
                self.assertFalse(witness['finite_exact_completion'])

    def test_zero_constant_and_mutated_halving_controls(self):
        self.assertEqual(b.transfer({},7),{})
        self.assertEqual(b.transfer({0:F(9)},91),{0:F(9)})
        self.assertEqual(b.transfer({3:F(1)},1),{})
        self.assertNotEqual(b.transfer({2:F(1)},1),{})
        with self.assertRaises(b.CambrianChaosError): b.transfer({1:0.5},1)
        with self.assertRaises(b.CambrianChaosError): b.koopman({1:1},-1)


class NaturalLawAndKneadingTests(unittest.TestCase):
    def test_constant_cell_density_refutation(self):
        witness=b.pf_constant_cell_obstruction()
        self.assertFalse(witness['constant_positive_density_on_three_cells_is_invariant'])
        self.assertNotEqual(*witness['jacobian_coefficients'])

    def test_periodic_multiplier_independent_radical_elimination(self):
        center=(ALPHA+1)*b._q(1)/2
        # Multiply formula by inverse alpha to avoid creating an unsupported division.
        from observational_succ.misiurewicz_phase_quotient import INV_ALPHA
        center=center*INV_ALPHA
        rad2=(ALPHA-3)*(ALPHA+1)*INV_ALPHA**2/4
        independent=ALPHA**2*((1-2*center)**2-4*rad2)
        expected=-ALPHA**2+2*ALPHA+4
        self.assertEqual(independent,expected)
        self.assertTrue(b.alpha_two_cycle_multiplier()['absolute_multiplier_exceeds_2'])

    def test_superstable_three_unique_root_and_iterative_endpoint_oracle(self):
        receipt=b.superstable_three_certificate()
        p=tuple(F(x) for x in receipt['critical_return_polynomial'])
        for r in receipt['root_bracket']+(F(3835,1000),):
            x=F(1,2)
            for _ in range(3): x=r*x*(1-x)
            self.assertEqual(b.poly_at(p,r),x-F(1,2))
        self.assertEqual(receipt['prime_period'],3)
        self.assertEqual(receipt['critical_itinerary'],'C,R,L,C')

    def test_superstable_two_independent_quadratic_ring(self):
        # Q[sqrt5], independent simple pair arithmetic; r=1+sqrt5.
        def add(a,c): return a[0]+c[0],a[1]+c[1]
        def mul(a,c): return a[0]*c[0]+5*a[1]*c[1],a[0]*c[1]+a[1]*c[0]
        def neg(a): return -a[0],-a[1]
        r=(F(1),F(1)); c=(F(1,2),F(0))
        def f(x): return mul(r,mul(x,add((F(1),F(0)),neg(x))))
        self.assertNotEqual(f(c),c)
        self.assertEqual(f(f(c)),c)


class FactorAndNoiseTests(unittest.TestCase):
    def test_periodic_factor_source_path_enumeration(self):
        for d in (1,2,3,5):
            for n in range(7):
                receipt=b.periodic_extension(d,n)
                paths={(j,bits) for j in range(d) for bits in product((0,1),repeat=n)}
                self.assertEqual(len(paths),d*receipt['source_bit_history_count_per_phase'])
                phases={tuple((j+t)%d for t in range(n+1)) for j,_ in paths}
                self.assertEqual(len(phases),d)

    def test_noise_covariance_independent_joint_moments(self):
        for a,c,d in product((F(0),F(1,7),F(1,2),F(1)),repeat=3):
            law=b.noisy_phase_joint(a,c,d)
            self.assertEqual(sum(law.values()),1)
            ex=sum(x*p for (x,y),p in law.items())
            ey=sum(y*p for (x,y),p in law.items())
            exy=sum(x*y*p for (x,y),p in law.items())
            self.assertEqual(exy-ex*ey,b.noisy_phase_covariance(a,c,d))

    def test_unknown_fair_delay_and_correlated_error_mutation(self):
        self.assertEqual(b.noisy_phase_joint(0,0,F(1,2)),
                         {p:F(1,4) for p in product((0,1),repeat=2)})
        self.assertEqual(b.noisy_phase_covariance(0,0,1),F(-1,4))
        # Shared fair noise produces identical reports, outside independence hypothesis.
        actual_shared_error_cov=F(1,4)
        self.assertNotEqual(actual_shared_error_cov,b.noisy_phase_covariance(F(1,2),F(1,2),0))

    def test_missing_history_exact_intervals_and_source_forward_oracle(self):
        for word in ((None,), (0,None,1), (None,None,0,None,1), (1,0,1)):
            intervals=b.partial_history_intervals(word,F(1,3),F(2,3))
            self.assertEqual(len(intervals),1<<word.count(None))
            expected_width=F(1,3)/(1<<len(word))
            for lo,hi in intervals:
                self.assertEqual(hi-lo,expected_width)
                x=(lo+hi)/2
                for symbol in word:
                    if symbol is not None: self.assertEqual(int(x>F(1,2)),symbol)
                    x=tent(x)
                self.assertEqual(x,F(1,2))
            self.assertTrue(all(a[1]<c[0] for a,c in zip(intervals,intervals[1:])))

    def test_invalid_noise_and_history_inputs(self):
        for p in (F(-1,2),F(3,2),0.5,True):
            with self.assertRaises(b.CambrianChaosError): b.noisy_phase_joint(p,0,0)
        for word in ((True,), (2,), (0.0,)):
            with self.assertRaises(b.CambrianChaosError): b.partial_history_intervals(word,F(1,3),F(2,3))

    def test_bounded_noise_against_actual_clipped_tent_trajectory(self):
        x,y=F(1,7),F(1,7)+F(1,10000)
        eps=F(1,10000)
        for n in range(8):
            self.assertLessEqual(abs(x-y),b.bounded_dynamical_error(2,F(1,10000),eps,n))
            x=tent(x)
            y=min(F(1),max(F(0),tent(y)+(eps if n%2 else -eps)))
        self.assertEqual(b.bounded_dynamical_error(1,F(1,100),F(1,200),4),F(3,100))
        with self.assertRaises(b.CambrianChaosError): b.bounded_dynamical_error(2,0,F(-1),3)


if __name__=='__main__': unittest.main()

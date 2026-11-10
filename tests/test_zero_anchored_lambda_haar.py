"""Exact rational, typed beta, true-source and hostile seed controls.

Requires only the existing observational_succ.duck_bbp standard-library module.
No finite outcome claims asymptotic pi normality.
"""
from fractions import Fraction as Q
import unittest

from observational_succ import duck_bbp
from observational_succ import zero_anchored_lambda_haar as z


class SourcePreservation(unittest.TestCase):
    def test_two_independent_arithmetic_routes(self):
        for seed in (Q(0), Q(1, 16), Q(-2, 7), Q(7, 9)):
            state = z.State(0, seed)
            for n in range(15):
                with self.subTest(seed=seed, n=n):
                    self.assertEqual(state, z.from_prefix(n, seed))
                    self.assertEqual(z.recover(state), seed)
                    self.assertEqual(z.recover(z.step(state)), seed)
                    self.assertEqual(z.authenticate(state), seed == 0)
                state = z.step(state)

    def test_canonical_four_poles_and_mutation_alarm(self):
        for n in range(1, 30):
            direct = (Q(4,8*n-7) - Q(2,8*n-4)
                      - Q(1,8*n-3) - Q(1,8*n-2))
            self.assertEqual(duck_bbp.forcing(n), direct)
        start = z.from_prefix(7, 0)
        mutant = z.State(8, 16*start.u + duck_bbp.forcing(8) + Q(1, 31))
        self.assertEqual(z.recover(mutant), Q(1,31*16**8))
        self.assertFalse(z.authenticate(mutant))

    def test_zero_is_not_circle_aliased(self):
        # Seed 1/16 produces the same completed circle orbit as seed zero
        # after the first shift, but their unreduced anchors remain different.
        for n in range(1, 12):
            authentic = z.from_prefix(n, 0)
            alien = z.from_prefix(n, Q(1, 16))
            self.assertEqual(alien.u-authentic.u, 16**(n-1))
            self.assertEqual(z.recover(alien), Q(1,16))
            self.assertFalse(z.authenticate(alien))


class LambdaSemantics(unittest.TestCase):
    def test_capture_free_beta_under_outer_binder(self):
        # lambda z.((lambda x.lambda y.x) z)  -> lambda z.lambda y.z
        term = z.Lam(z.RAT, z.App(z.Lam(z.RAT,z.Lam(z.RAT,z.Var(1))), z.Var(0)))
        expected = z.Lam(z.RAT,z.Lam(z.RAT,z.Var(1)))
        receipt = z.normalize(term)
        self.assertEqual(receipt.value, expected)
        self.assertEqual(receipt.rules, ("beta",))

    def test_closed_serial_compilation_and_prefix_compilation(self):
        for n in range(11):
            for seed in (Q(0), Q(5, 7)):
                with self.subTest(n=n, seed=seed):
                    p = z.normalize(z.serial_program(n, seed))
                    q = z.normalize(z.prefix_program(n, seed))
                    self.assertEqual(p.value, q.value)
                    self.assertEqual(p.result_type, z.STATE)
                    self.assertEqual(p.rules.count('beta'), n)
                    self.assertEqual(p.rules.count('source:step'), n)
                    anchor = z.normalize(z.anchor_program(n,seed))
                    self.assertEqual(anchor.value, z.Lit(z.RAT, seed))
                    self.assertEqual(anchor.rules.count('beta'), n+1)

    def test_two_beta_strategies_agree_on_source_and_tail(self):
        for n in range(1,12):
            for seed in (Q(0),Q(1,16),Q(-2,7)):
                with self.subTest(n=n,seed=seed):
                    for program in (z.serial_program(n,seed),
                                    z.anchor_program(n,seed),
                                    z.completion_program(n,seed,depth=5)):
                        normal=z.normalize(program,strategy="normal")
                        eager=z.normalize(program,strategy="innermost")
                        self.assertEqual(normal.value,eager.value)
                        self.assertEqual(normal.result_type,eager.result_type)
                        self.assertEqual(sorted(normal.rules),sorted(eager.rules))
        self.assertNotEqual(z.normalize(z.serial_program(3)).rules,
                            z.normalize(z.serial_program(3),strategy="innermost").rules)
        with self.assertRaises(ValueError):
            z.normalize(z.serial_program(1),strategy="invented")

    def test_budget_and_invalid_terms(self):
        with self.assertRaises(RuntimeError):
            z.normalize(z.serial_program(4),max_steps=2)
        with self.assertRaises(TypeError):
            z.type_of(z.App(z.Lit(z.RAT,0),z.Lit(z.RAT,1)))
        with self.assertRaises(TypeError):
            z.type_of(z.Var(0))
        with self.assertRaises(TypeError):
            z.Lit(z.RAT,0.0)
        with self.assertRaises(TypeError):
            z.type_of(z.Prim('bad',(z.Lit(z.NAT,0),)))

    def test_guarded_tail_fixed_point_unfold_and_canonical_bounds(self):
        for n in range(12):
            for depth in range(10):
                current = z.guarded_tail(n, depth)
                self.assertEqual((current.lo, current.hi),
                                 duck_bbp.tail_interval(n,depth))
                higher = z.guarded_tail(n,depth+1)
                later = z.guarded_tail(n+1,depth)
                self.assertEqual(higher.lo, (duck_bbp.forcing(n+1)+later.lo)/16)
                self.assertEqual(higher.hi, (duck_bbp.forcing(n+1)+later.hi)/16)
                self.assertLessEqual(current.lo,higher.lo)
                self.assertGreaterEqual(current.hi,higher.hi)
                self.assertGreater(current.hi,current.lo)

    def test_lambda_completion_and_source_square(self):
        for n in range(9):
            receipt=z.normalize(z.completion_program(n,depth=8))
            self.assertEqual(receipt.result_type,z.INTERVAL)
            self.assertEqual(receipt.value,z.Lit(z.INTERVAL,z.complete(z.from_prefix(n,0),8)))
            self.assertEqual(receipt.rules.count('beta'),n+1)
            self.assertEqual(receipt.rules.count('source:complete'),1)
            a=z.complete(z.from_prefix(n,0),8)
            b=z.complete(z.from_prefix(n+1,0),7)
            self.assertEqual((a.lo*16,a.hi*16),(b.lo,b.hi))

    def test_closed_source_folding_intertwines_clock(self):
        for n in range(15):
            lhs = z.step(z.from_prefix(n,0))
            rhs = z.from_prefix(n+1,0)
            self.assertEqual(lhs,rhs)
            self.assertEqual(z.recover(lhs),0)


class CertifiedHaar(unittest.TestCase):
    def test_canonical_pi_hex_prefix(self):
        self.assertEqual(z.certified_digits(16,depth=12),
                         tuple(int(a,16) for a in '3243F6A8885A308D'))

    def test_shadow_from_source_rational_prefix(self):
        # Not an irrational pi oracle: choose an exact rational shadow seed.
        shadow = -z.prefix(60)
        self.assertNotEqual(shadow,0)
        self.assertEqual(z.certified_digits(20,shadow,depth=16),(0,)*20)
        self.assertFalse(z.authenticate(z.from_prefix(19,shadow)))
        self.assertEqual(z.parity_pin((0,)*20),1)

    def test_exact_haar_w1_delta_and_projector(self):
        self.assertEqual(z.exact_haar_defect((Q(0),)), Q(15,32))
        self.assertEqual(z.exact_haar_defect(tuple(Q(i,16) for i in range(16))), Q(0))

    def test_certified_W1_interval_and_comparison(self):
        for seed in (Q(0), -z.prefix(45)):
            for N in (4,8,16,32):
                with self.subTest(seed=seed,N=N):
                    receipt = z.certified_haar_defect(N,seed,depth=12)
                    self.assertLessEqual(0,receipt.lower)
                    self.assertLessEqual(receipt.lower,receipt.midpoint_defect)
                    self.assertLessEqual(receipt.midpoint_defect,receipt.upper)
                    self.assertLessEqual(receipt.upper - receipt.lower, 2*receipt.error)

    def test_cyclic_haar_diagnostics_and_energy(self):
        cases = [(0,)*16,tuple(range(16))*2,
                 tuple(int(c,16) for c in '3243F6A8885A308D')]
        for digits in cases:
            for j in range(3):
                with self.subTest(digits=digits,j=j):
                    delta = z.cyclic_defect(digits,j)
                    gap=z.cyclic_energy(digits,j+1)-z.cyclic_energy(digits,j)
                    self.assertLessEqual(0,gap)
                    self.assertLessEqual(delta*delta,gap)
        self.assertEqual(z.cyclic_defect(tuple(range(16))*2,0),0)
        self.assertEqual(z.cyclic_defect(tuple(range(16))*2,1),Q(15,8))
        self.assertEqual(z.cyclic_defect((0,)*16,0),Q(15,8))
        self.assertEqual(z.cyclic_defect((0,)*16,1),Q(15,8))

    def test_exact_cyclotomic_character_pins(self):
        self.assertEqual(z.formal_character_pin((0,)*8,8), (Q(1),)+(Q(0),)*7)
        self.assertEqual(z.formal_character_pin(tuple(range(16)),8),(Q(0),)*8)
        for h in range(1,16):
            self.assertEqual(z.formal_character_pin(tuple(range(16)),h),(Q(0),)*8)
        digits=(0,1,2,3)*3
        # A forbidden future word gives the exact zero cyclotomic vector.
        self.assertEqual(z.formal_character_pin(digits,3,(10,)),(Q(0),)*8)

    def test_pascal_fourier_partition_and_exact_parity(self):
        for seed in (Q(0), -z.prefix(45)):
            digits=z.certified_digits(12,seed,depth=12)
            for h in (1,4,8,15):
                zero=z.pascal_fourier_pin(12,0,0,h,seed=seed,depth=12)
                self.assertEqual(zero.coefficients,z.formal_character_pin(digits,h))
                self.assertEqual(zero.complex_error_bound,0)
                for m in (1,2,3):
                    pins=[z.pascal_fourier_pin(12,m,j,h,seed=seed,depth=12)
                          for j in range(m+1)]
                    self.assertEqual(tuple(sum((p.coefficients[i] for p in pins),Q())
                                           for i in range(8)),zero.coefficients)
                    for p in pins:
                        self.assertGreaterEqual(p.complex_error_bound,0)

    def test_pascal_upper_really_bounds_finite_haar_defect(self):
        for seed in (Q(0),-z.prefix(45)):
            for N in (4,8,12):
                cert=z.certified_haar_defect(N,seed,depth=12)
                for m in (1,4):
                    with self.subTest(seed=seed,N=N,m=m):
                        self.assertGreaterEqual(z.pascal_haar_upper(N,m,seed,12),cert.upper)

    def test_finite_contraction_excess_does_not_prove_decay(self):
        sh=-z.prefix(45)
        c=z.certified_haar_defect(32,sh,depth=12)
        e=z.certified_haar_defect(16,sh,depth=12)
        lo,hi=z.contraction_excess(c,e,Q(3,4))
        self.assertLess(lo,hi)
        # The shadow is almost the constant-zero path, defect ~ 15/32.
        self.assertGreater(lo, Q(1,10))
        with self.assertRaises(ValueError):
            z.contraction_excess(c,e,Q(1))


if __name__ == '__main__':
    unittest.main()

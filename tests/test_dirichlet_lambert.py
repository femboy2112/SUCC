"""Exact arithmetic Lambert W, independently checked against path enumeration.

The key negative control is deliberate: W_*(zeta-1)(6)=-1 despite
the genuine Euler log having connected coefficient b(6)=0.
Source sensitivity and Weil-sign validity are different propositions.
"""
from fractions import Fraction as Q
import unittest

import mpmath as mp

from observational_succ.dirichlet_lambert import (
    ArithmeticWError, DirichletLambertSnapshot, convolve,
    identity, star_exp, star_lambert_w, star_log_unit,
)
from observational_succ import Engine, Limits, Scalar, source_at


class DirichletLambertTests(unittest.TestCase):

    def test_genuine_euler_source_exact_inversion(self):
        for N in (6,12,24,64,128):
            true=DirichletLambertSnapshot.from_prefix({n:1 for n in range(1,N+1)},N)
            self.assertTrue(true.verify_inverse_identity())
            self.assertEqual(true.w[2],1)
            self.assertEqual(true.w[3],1)
            self.assertEqual(true.w[4],0)
            self.assertEqual(true.w[6],-1)
            self.assertEqual(true.connected[6],0)
            self.assertEqual(true.composite_six()["mixed_composite_euler_consistent"],True)
            self.assertEqual(true.composite_six()["w6"],"-1")
            for p in (2,3,5):
                self.assertEqual(true.w[p],true.h[p])
            if N>=8:
                self.assertEqual(true.w[8],Q(1,2))
                self.assertEqual(true.connected[8],Q(1,3))

    def test_source_mutation_at_six_changes_arithmetic_w(self):
        source={n:1 for n in range(1,33)}
        true=DirichletLambertSnapshot.from_prefix(source,32)
        fake=dict(source); fake[6]=2
        bad=DirichletLambertSnapshot.from_prefix(fake,32)
        self.assertTrue(bad.verify_inverse_identity())
        self.assertEqual(true.w[6],-1)
        self.assertEqual(bad.w[6],0) # zeros are NOT a W_* authenticity test!
        self.assertEqual(bad.connected[6],1)
        self.assertEqual(bad.composite_six()["connected_b6"],"1")
        self.assertFalse(bad.composite_six()["mixed_composite_euler_consistent"])
        self.assertEqual(true.w[2:6],bad.w[2:6])
        self.assertNotEqual(true.w[12:],bad.w[12:])
        self.assertEqual(
            bad.w[6]+bad.source[2]*bad.source[3],bad.connected[6])

    def test_nonunit_multiplicative_character_is_different_from_composite_defect(self):
        # a(n)=(3/2)^v_2(n) remains completely multiplicative, yet
        # its local unitarity law is wrong for zeta. b(6)=0 is not enough.
        def coeff(n):
            a=Q(1)
            while n%2==0:
                a*=Q(3,2)
                n//=2
            return a
        true=DirichletLambertSnapshot.from_prefix({n:1 for n in range(1,33)},32)
        changed=DirichletLambertSnapshot.from_prefix({n:coeff(n) for n in range(1,33)},32)
        self.assertEqual(changed.connected[6],0)
        self.assertEqual(changed.w[6],-Q(3,2))
        self.assertEqual(changed.w[2],Q(3,2))
        self.assertNotEqual(changed.w[6],true.w[6])
        self.assertTrue(changed.verify_inverse_identity())

    def test_shadow_factor_paths_are_distinct_from_scalar_mass(self):
        p=DirichletLambertSnapshot.from_prefix({n:1 for n in range(1,25)},24)
        w6=p.witnesses(6)
        self.assertEqual([x["factors"] for x in w6],
                         [[2,3],[3,2],[6]])
        self.assertEqual([x["tree_weight"] for x in w6],
                         ["-1","-1","1"])
        self.assertEqual(sum(Q(x["signed_amplitude"]) for x in w6),-1)
        for n in range(2,25):
            self.assertEqual(sum(Q(x["signed_amplitude"]) for x in p.witnesses(n)),p.w[n])

    def test_causal_prefix_compatibility_and_fake_future(self):
        a={n:1 for n in range(1,65)}
        small=DirichletLambertSnapshot.from_prefix(a,5)
        long=DirichletLambertSnapshot.from_prefix(a,64)
        self.assertTrue(small.preserve_prefix(long))
        mutated=dict(a);mutated[6]=2
        future=DirichletLambertSnapshot.from_prefix(mutated,64)
        self.assertTrue(small.preserve_prefix(future))
        later=DirichletLambertSnapshot.from_prefix(a,10)
        with self.assertRaises(ArithmeticWError):
            later.preserve_prefix(future)
        with self.assertRaises(ArithmeticWError):
            long.preserve_prefix(small)

    def test_from_engine_reads_only_integrated_events_and_trace_head(self):
        e=Engine(arithmetic=True,limits=Limits(max_target=20))
        for n in range(1,6):
            e.advance(source_at(n),context="zeta",probe="coefficient")
        p=DirichletLambertSnapshot.from_engine(e)
        self.assertEqual(p.horizon,5)
        self.assertEqual(p.source_head,e.head)
        e.predict(6,Scalar(2),"fake predicted future composite")
        e.step(Scalar(2),context="probe",probe="coefficient")
        pre=DirichletLambertSnapshot.from_engine(e)
        self.assertEqual(pre.horizon,5)
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_engine(e,horizon=6)
        e.propagate()
        post=DirichletLambertSnapshot.from_engine(e)
        self.assertEqual(post.horizon,6)
        self.assertEqual(post.connected[6],1)
        self.assertFalse(post.composite_six()["mixed_composite_euler_consistent"])
        self.assertEqual(post.source_head,e.head)

    def test_independent_inverse_equation_fails_when_w_mutated(self):
        real=DirichletLambertSnapshot.from_prefix({n:1 for n in range(1,33)},32)
        w=list(real.w); w[6]+=Q(1,10)
        w=tuple(w)
        self.assertNotEqual(convolve(w,star_exp(w)),real.h)
        self.assertEqual(convolve(real.w,star_exp(real.w)),real.h)
        self.assertEqual(convolve(real.w,identity(32)),real.w)
        with self.assertRaises(ArithmeticWError):
            star_exp(identity(32))

    def test_single_prime_mellin_intertwines_scalar_w(self):
        # Source h(2)=1, h(n)=0 for n!=2. Its Dirichlet-W power
        # series uses exactly the powers of 2 and rooted-tree weights.
        a={n:int(n in (1,2)) for n in range(1,257)}
        p=DirichletLambertSnapshot.from_prefix(a,256)
        self.assertTrue(p.verify_inverse_identity())
        for k in range(1,9):
            coeff=Q((-k)**(k-1),__import__("math").factorial(k))
            self.assertEqual(p.w[2**k],coeff)
        for n in range(2,257):
            if n & (n-1):
                self.assertEqual(p.w[n],0)
        probe=p.analytic_mellin_probe(4,dps=75)
        with mp.workdps(75):
            self.assertLess(abs(probe["analytic_lambert"]-
                                mp.lambertw(mp.mpf(1)/16)),mp.mpf("1e-68"))
            self.assertLess(probe["absolute_error"],probe["truncation_bound"]+
                            mp.mpf("1e-65"))
            self.assertLess(probe["absolute_error"],mp.mpf("2e-9"))

    def test_zeta_safe_mellin_intertwiner_with_explicit_tail(self):
        # h(n)=1 (n>=2) is ζ(s)-1. At σ=4 this is safely inside
        # |h|_σ<1/e, where the scalar W series converges absolutely.
        # The source snapshot is finite; compare also to the TRUE
        # infinite source via the elementary Dirichlet tail.
        for n in (32,128,256):
            p=DirichletLambertSnapshot.from_prefix({k:1 for k in range(1,n+1)},n)
            probe=p.analytic_mellin_probe(4,dps=70)
            with mp.workdps(70):
                self.assertLess(probe["absolute_error"],
                                probe["truncation_bound"]+mp.mpf("1e-58"))
                infinite=mp.lambertw(mp.zeta(4)-1)
                # W' <= 1 on the nonnegative real axis, so source
                # truncation adds <= 1/(3*N^3).
                self.assertLess(abs(probe["finite_star_sum"]-infinite),
                    probe["truncation_bound"]+mp.mpf(1)/(3*n**3)+mp.mpf("1e-58"))
                self.assertLess(probe["abs_input_mass"],1/mp.e)

    def test_malformed_inputs_rejected(self):
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:1,2:1.5},2)
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:1,2:1},4)
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:2,2:1},2)
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:1,2:1j},2)
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:1,2:1},2.0)
        with self.assertRaises(ArithmeticWError):
            convolve((Q(0),Q(1)),(Q(0),Q(1),Q(0)))
        with self.assertRaises(ArithmeticWError):
            star_lambert_w(identity(6))
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({n:1 for n in range(1,10)},9).witnesses(65)
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:1,2:1},2).composite_six()
        with self.assertRaises(ArithmeticWError):
            DirichletLambertSnapshot.from_prefix({1:1,2:1},2).analytic_mellin_probe(1)


if __name__=="__main__":
    unittest.main()

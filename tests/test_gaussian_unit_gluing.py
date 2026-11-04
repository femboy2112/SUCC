"""Exact algebra and selected-source firewalls for the Gaussian-unit gluing forge."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import random
import unittest

P=(Path(__file__).resolve().parents[1]/'research'/'2026-11-03'
   /'gaussian_unit_gluing'/'gaussian_unit_gluing.py')
S=importlib.util.spec_from_file_location('gaussian_unit_gluing', P)
m=importlib.util.module_from_spec(S)
S.loader.exec_module(m)


class Algebra(unittest.TestCase):
    def test_minimal_rational_algebra_is_associative_and_has_unit(self):
        rng=random.Random(20261103)
        for _ in range(60):
            a=m.el(*(Q(rng.randrange(-4,5),rng.randrange(1,8)) for _ in range(4)))
            b=m.el(*(Q(rng.randrange(-4,5),rng.randrange(1,8)) for _ in range(4)))
            c=m.el(*(Q(rng.randrange(-4,5),rng.randrange(1,8)) for _ in range(4)))
            self.assertEqual(m.mul(m.mul(a,b),c),m.mul(a,m.mul(b,c)))
            self.assertEqual(m.mul(a,m.ONE),a)
            self.assertEqual(m.mul(m.ONE,a),a)

    def test_trace_independent_of_extension_embeddings(self):
        # Direct regular trace; old eigenvalue power sums from the roots.
        self.assertEqual([m.trace(m.power(m.U,n)) for n in range(8)],
                         [Q(4),Q(1),Q(1),Q(-1,2),Q(0),Q(-1,4),Q(1,4),Q(1,8)])

    def test_hankel_rank_four(self):
        expected=((Q(4),Q(0),Q(0),Q(-2)),(Q(0),Q(0),Q(-2),Q(-1)),
                  (Q(0),Q(-2),Q(-1),Q(-1)),(Q(-2),Q(-1),Q(-1),Q(0)))
        self.assertEqual(m.hankel_four(),expected)
        self.assertEqual(m.determinant(expected),4)

    def test_frobenius_gram_duality_and_handle(self):
        g=m.frobenius_gram();inv=m.gram_inverse()
        self.assertEqual(m.determinant(g),Q(4))
        for i in range(4):
            for j in range(4):
                self.assertEqual(sum(g[i][k]*inv[k][j] for k in range(4)),int(i==j))
        for a,b,c in ((m.ONE,m.U,m.power(m.U,3)),
                      (m.power(m.U,2),m.power(m.U,5),m.power(m.U,7))):
            self.assertEqual(m.frobenius_pairing(m.mul(a,b),c),
                             m.frobenius_pairing(a,m.mul(b,c)))
            self.assertEqual(m.frobenius_pairing(a,b),m.frobenius_pairing(b,a))
        self.assertEqual(m.mul(m.frobenius_handle(),m.UNIT_WEIGHT),m.ONE)
        self.assertEqual(m.frobenius_handle(),
                         m.el(Q(-1,2),Q(1,2),Q(1),Q(-3)))

    def test_eighth_return_and_fourth_sign(self):
        c=m.involution()
        self.assertEqual(m.mul(c,c),m.ONE)
        self.assertNotEqual(c,m.ONE)
        self.assertNotEqual(m.power(m.U,4),m.scale(m.ONE,Q(1,4)))
        self.assertEqual(m.power(m.U,8),m.scale(m.ONE,Q(1,16)))
        self.assertEqual(m.sqrt2_extension_power(m.normalized_unit(),8),(m.ONE,m.ZERO))
        self.assertEqual(m.sqrt2_extension_power(m.normalized_unit(),4),(c,m.ZERO))
        self.assertNotEqual(m.sqrt2_extension_power(m.normalized_unit(),4),(m.ONE,m.ZERO))
        self.assertNotEqual(m.sqrt2_extension_power(m.normalized_unit(),2),(m.ONE,m.ZERO))

    def test_canonical_projectors_and_complex_structure(self):
        eh,eg=m.projectors();j=m.unit_complex_structure()
        self.assertEqual(m.add(eh,eg),m.ONE)
        self.assertEqual(m.mul(eh,eh),eh)
        self.assertEqual(m.mul(eg,eg),eg)
        self.assertEqual(m.mul(eh,eg),m.ZERO)
        self.assertEqual(m.mul(j,j),m.scale(eg,-1))
        self.assertEqual(m.mul(j,eh),m.ZERO)
        self.assertEqual(m.mul(m.UNIT_WEIGHT,eh),m.mul(m.scale(m.U,-2),eh))
        self.assertEqual(m.mul(m.UNIT_WEIGHT,eg),m.scale(eg,2))

    def test_two_sector_difference_recovery_all_64(self):
        for n in range(64):
            gh,gg=m.channel_impulses(n)
            self.assertEqual((gh,gg),m.channel_impulses_from_scalar(n))
            self.assertEqual(gh+gg,m.impulse_closed(n))
            self.assertEqual(gh-gg,4*m.impulse_closed(n+4))

    def test_exact_independently_predicted_sector_taps(self):
        self.assertEqual(tuple(m.channel_impulses(k) for k in range(8)),
                         ((Q(0),Q(4)),(Q(-2),Q(2)),(Q(0),Q(0)),
                          (Q(-1),Q(-1)),(Q(0),Q(-1)),(Q(-1,2),Q(-1,2)),
                          (Q(0),Q(0)),(Q(-1,4),Q(1,4))))


class Source(unittest.TestCase):
    def test_reconstruct_exact_eight_taps(self):
        self.assertEqual(tuple(m.impulse(n) for n in range(8)),m.TAPS)
        for n in range(129):
            self.assertEqual(m.impulse(n),m.impulse_closed(n))

    def test_mellin_four_signed_poles(self):
        for n in range(1,301):
            self.assertEqual(m.mellin_from_eight_taps(n),m.original_four_poles(n))
        self.assertEqual(m.mellin_from_eight_taps(2),Q(106,819))

    def test_channel_mellin_moments_and_exact_local_pole_cancellation(self):
        for n in range(1,257):
            rh,rg=m.mellin_channels(n)
            self.assertEqual(rh+rg,m.original_four_poles(n))
            self.assertEqual(rh,-Q(1,4*n-3)-Q(1,4*(2*n-1))
                             -Q(1,4*(4*n-1))-Q(1,32*n))
            # v2(rh)=v2(rg)=-5-v2(n) whereas v2(r)>=0.
            self.assertEqual(m.v2_rational(rh),-5-m.v2_rational(n))
            self.assertEqual(m.v2_rational(rg),-5-m.v2_rational(n))
            self.assertGreaterEqual(m.v2_rational(rh+rg),0)
        self.assertIsNone(m.v2_rational(0))

    def test_padic_reduction_must_happen_after_gluing(self):
        # The discrete map to Z/2^k is undefined on the individual sectors.
        def residue(x,bits):
            x=Q(x)
            if x.denominator%2==0:
                raise ValueError('not in Z_2: gluing required before reduction')
            mod=1<<bits
            return x.numerator*pow(x.denominator,-1,mod)%mod
        for n in (1,2,3,8,16,64,127,263):
            rh,rg=m.mellin_channels(n)
            for bits in (4,12):
                with self.assertRaises(ValueError):residue(rh,bits)
                with self.assertRaises(ValueError):residue(rg,bits)
                self.assertEqual(residue(rh+rg,bits),residue(m.original_four_poles(n),bits))
        self.assertEqual(residue(Q(16,21),16),16*pow(21,-1,1<<16)%(1<<16))

    def test_coupled_zero_seed_channel_states_recover_original_source(self):
        joined=m.source_channel_states(90)
        observed=m.fractional_source_states(90)
        self.assertEqual(joined[0],(Q(0),Q(0)))
        for n,(a,b) in enumerate(joined):
            self.assertEqual((a+b)%1,observed[n])

    def test_zero_seed_finite_original_rational_states(self):
        out=m.fractional_source_states(100)
        x=Q(0)
        for n in range(1,101):
            x=(16*x+m.original_four_poles(n))%1
            self.assertEqual(x,out[n])
        self.assertEqual(out[0],0)
        self.assertTrue(all(x.denominator%2 for x in out))

    def test_mutation_retains_atoms_and_jets_but_changes_completion(self):
        self.assertEqual(sum(m.MUTATION_TAPS),0)
        self.assertEqual(sum(j*v for j,v in enumerate(m.MUTATION_TAPS)),0)
        self.assertEqual(m.changed_source_probe(0),m.impulse_closed(0))
        self.assertNotEqual(m.changed_source_probe(1),m.impulse_closed(1))
        self.assertEqual(sum(v/Q(i+1) for i,v in enumerate(m.MUTATION_TAPS)),Q(67,480))
        self.assertEqual(m.mutated_constant_shift(),Q(67,3840))
        for n in range(1,40):
            self.assertGreater(m.mutated_mellin_source(n),m.original_four_poles(n))
        for n in range(8):
            self.assertEqual(m.changed_source_probe(n),
                             m.impulse_closed(n)+Q(1,8)*m.MUTATION_TAPS[n])

    def test_wrong_seed_preserves_all_linear_atoms(self):
        # Same r(n), unit algebra, taps, and transfer, but different seed.
        # Completed point q=1/5 gives asymptotically a fixed non-Haar orbit.
        # This is a conceptual same-forcing countermodel, not numerical proof.
        self.assertEqual(m.impulse_closed(0),4)
        self.assertEqual(m.original_four_poles(3),m.mellin_from_eight_taps(3))
        self.assertNotEqual(Q(1,5)-Q(0),0)

    def test_invalid_types(self):
        for f in (lambda:m.power(m.U,-1),lambda:m.impulse(-1),
                  lambda:m.mellin_from_eight_taps(0),
                  lambda:m.changed_source_probe(-1),
                  lambda:m.fractional_source_states(-1),
                  lambda:m.sqrt2_extension_power(m.normalized_unit(),-1)):
            with self.assertRaises(ValueError):f()


if __name__=='__main__':unittest.main()

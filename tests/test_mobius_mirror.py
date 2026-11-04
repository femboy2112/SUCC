"""Focused original-source Möbius mirror and hostile pairing tests.

Finite tests calibrate algebra, source passports and bounds; they do not prove
all-horizon π normality, all-real asymptotic Weyl cancellation or Lean claims.
"""
import cmath
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

P=(Path(__file__).resolve().parents[1]/'research'/'2026-11-02'/'mobius_mirror'/'mobius_mirror.py')
S=importlib.util.spec_from_file_location('mobius_mirror_source',P)
m=importlib.util.module_from_spec(S);S.loader.exec_module(m)


def z_stereo(t):
    if t is None:return -1j
    t=float(t)
    return 1j*(1+1j*t)/(1-1j*t)


class CircleProjectiveTests(unittest.TestCase):
    def test_projective_global_division_involution(self):
        for t in [None,0,-1,1,Fraction(2,7),Fraction(-3,5),17]:
            self.assertEqual(m.projective_reciprocal(m.projective_reciprocal(t)),
                             None if t is None else Fraction(t))

    def test_phase_conjugation_exact_projective(self):
        for t in [None,0,-1,1,Fraction(2,7),Fraction(-3,5),17]:
            a=z_stereo(t)
            b=z_stereo(m.projective_reciprocal(t))
            self.assertAlmostEqual(abs(a),1.,places=13)
            self.assertAlmostEqual(abs(b-a.conjugate()),0.,places=12)

    def test_original_radix16_projective_reciprocal(self):
        for t in [None,0,-1,1,Fraction(2,7),Fraction(-3,5),17]:
            left=m.projective_radix16(m.projective_reciprocal(t))
            right=m.projective_reciprocal(m.projective_radix16(t))
            self.assertEqual(left,right)

    def test_radix16_projective_matches_complex_power(self):
        for t in [None,0,-1,1,Fraction(2,7),Fraction(-3,5),17]:
            v=m.projective_radix16(t)
            self.assertLess(abs(z_stereo(v)-z_stereo(t)**16),1e-10)

    def test_mobius_rotation_reciprocity(self):
        for t in [None,0,1,Fraction(2,7),Fraction(-3,5)]:
            for q in [None,0,1,Fraction(1,3),Fraction(-2,5)]:
                a=m.projective_reciprocal(m.projective_rotation(t,q))
                b=m.projective_rotation(m.projective_reciprocal(t),
                    None if q is None else -Fraction(q))
                self.assertEqual(a,b)

    def test_quotient_raw_reciprocal_bad(self):
        # 1/2 and 3/2 represent the same circle point but their reciprocals
        # 2 and 2/3 do NOT represent the same circle point.
        a=Fraction(1,2);b=a+1
        self.assertNotEqual((1/a)%1,(1/b)%1)

    def test_dihedral_centralizer_axes(self):
        for k in range(15):
            self.assertTrue(m.fixed_axis_commutes_radix(Fraction(k,15)))
        self.assertFalse(m.fixed_axis_commutes_radix(Fraction(1,2)))
        self.assertFalse(m.fixed_axis_commutes_radix(Fraction(1,7)))

    def test_conjugates_add_cosines_not_cancel(self):
        for q in [Fraction(0),Fraction(1,5),Fraction(3,17)]:
            z=m.circle_e(q)
            self.assertAlmostEqual((z+z.conjugate()).real,2*z.real,places=12)
        self.assertNotAlmostEqual((m.circle_e(Fraction(1,5))+
            m.circle_e(Fraction(-1,5))).real,0,places=6)

    def test_finite_dihedral_symmetric_nonnormal_measure(self):
        # Uniform 15-th roots is reflection and finite-rotation invariant,
        # but Fourier coefficient at h=15 equals 1 (NOT Haar).
        phases=[m.circle_e(Fraction(j,15)) for j in range(15)]
        for k in range(15):
            eta=m.circle_e(Fraction(k,15))
            reflected={round((eta/z).real,12)+1j*round((eta/z).imag,12)
                       for z in phases}
            original={round(z.real,12)+1j*round(z.imag,12) for z in phases}
            self.assertEqual(reflected,original)
        self.assertAlmostEqual(abs(sum(z**15 for z in phases)/15),1,places=12)


class OriginalBBPMirrorTests(unittest.TestCase):
    def test_rational_four_pole_source_exact(self):
        self.assertEqual(m.r_original(1),Fraction(47,15))
        self.assertEqual(m.r_original(2),Fraction(106,819))
        for n in range(1,100):
            self.assertEqual(m.r_original(n),Fraction(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
            self.assertGreater(m.r_original(n),0)

    def test_meromorphic_differential_pole_rigidity(self):
        p=m.source_residues()
        self.assertEqual(list(p.values()),[Fraction(1,2),Fraction(-1,4),
                                            Fraction(-1,8),Fraction(-1,8)])
        self.assertEqual(m.fix_two_pole_coordinate(Fraction(3,8)),4)
        self.assertEqual(m.fix_two_pole_coordinate(Fraction(1,4)),Fraction(5,2))
        self.assertNotEqual(Fraction(5,2)/4,4/Fraction(5,2))
        poles=set(p)
        self.assertNotEqual(poles,{1/x for x in poles})

    def test_original_positive_forcing_has_no_fixed_reflection(self):
        for n in range(2,150):
            self.assertGreater(m.r_original(n),0)
            self.assertLess(m.r_original(n),Fraction(1,2))
        for a in [0,Fraction(1,15),Fraction(2,15),Fraction(1,2)]:
            # The fixed reflection would require a_n+1-16*a_n=2r, impossible
            # at every n because r(n) varies and is non-half-integer.
            self.assertTrue(any(m.centered(m.source_reflection_commutator(n,a))>0
                                for n in range(2,30)))

    def test_finite_rational_mirror_cocycle_every_cutoff(self):
        for B in (1,2,8,32,96):
            axes=m.mirror_axes(B)
            self.assertEqual(axes[-1],0)
            self.assertEqual(axes[0],-2*m.finite_completion(B))
            for n in range(B):
                self.assertEqual(m.mirror_cocycle_defect(axes[n],axes[n+1],
                                 m.r_original(n+1)),0)

    def test_mirror_shadow_is_original_forcing_with_changed_seed(self):
        for B in (4,20,72):
            U,M=m.completed_mirror_shadow(B)
            self.assertEqual(U[0],0)
            self.assertEqual(M[0],-2*m.finite_completion(B))
            self.assertNotEqual(M[0],0)
            for n in range(1,B+1):
                self.assertEqual(M[n],16*M[n-1]+m.r_original(n))
                self.assertEqual(M[n],-U[n]-2*m.finite_future(B)[n])

    def test_zero_seed_preserving_moving_reflection_is_trivial(self):
        U=m.original_states(40)
        axes=[2*u for u in U]
        for n in range(40):
            self.assertEqual(m.mirror_cocycle_defect(axes[n],axes[n+1],
                             m.r_original(n+1)),0)
            self.assertEqual(m.signed_reflection_mirror(U[n],axes[n]),U[n])

    def test_two_cutoff_finite_exact_sewing(self):
        for B,C in [(3,17),(16,30),(29,64),(64,96)]:
            RB=m.finite_future(B); RC=m.finite_future(C)
            for n in range(B+1):
                self.assertEqual(RC[n]-RB[n],Fraction(1,16**(B-n))*RC[B])
                self.assertEqual(-2*RC[n]-(-2*RB[n]),
                                 -2*Fraction(1,16**(B-n))*RC[B])

    def test_gamma_remainder_cutoff_bound(self):
        for B in (8,32,100,256):
            self.assertEqual(m.mirror_cutoff_sum_bound_coefficient(B),
                             Fraction(64,15)*m.gamma_tail_upper(B))

    def test_late_conjugate_shadow_phase_enclosure(self):
        for B,A,h in [(40,10,1),(80,16,5),(120,24,7)]:
            U,shadow=m.completed_mirror_shadow(B)
            R=m.finite_future(B)
            discrepancy=sum(abs(m.circle_e(h*shadow[n])-m.circle_e(-h*U[n]))
                            for n in range(A,B+1))
            rhs=4*math.pi*abs(h)*float(sum(R[A:],Fraction(0)))
            self.assertLessEqual(discrepancy,rhs+1e-10)

    def test_numerical_pair_cannot_create_weyl_cancellation(self):
        U,shadow=m.completed_mirror_shadow(96)
        for h in (1,3,5):
            s=sum(m.circle_e(h*u) for u in U)
            t=sum(m.circle_e(h*v) for v in shadow)
            defect=sum(abs(m.circle_e(h*shadow[n])-m.circle_e(-h*U[n]))
                       for n in range(len(U)))
            self.assertLessEqual(abs(t-s.conjugate()),defect+1e-10)
            self.assertLessEqual(abs((s+t)-2*s.real),defect+1e-10)


class GoldenTwoMirrorTests(unittest.TestCase):
    def test_golden_algebraic_norm_lower_bound(self):
        eta=m.golden_axis()
        for h in range(1,3000):
            u=h*eta
            self.assertGreaterEqual(abs(u-round(u))+1e-12,1/(3*h))
            self.assertLessEqual(1/abs(1-cmath.exp(2j*math.pi*h*eta)),
                                 float(m.golden_condition_number_bound(h))+1e-6)

    def test_two_mirror_exact_fourier_reconstruction(self):
        eta=m.golden_axis()
        U=m.original_states(128)
        for h in (1,2,3,5,11):
            c=sum((m.circle_e(h*v) for v in U),0j)/len(U)
            d0,de=m.mirror_discrepancies(c,h,eta)
            phase=cmath.exp(2j*math.pi*h*eta)
            recovered=((d0-de)/(phase-1)).conjugate()
            self.assertLess(abs(recovered-c),1e-10)
            self.assertLessEqual(abs(c),float(m.golden_condition_number_bound(h))*(abs(d0)+abs(de))+1e-7)

    def test_finite_fibonacci_irrational_mirror(self):
        eta=m.golden_axis()
        for k in range(3,23):
            q=m.finite_golden_axis(k)
            self.assertLess(abs(float(q)-eta),1/m.fib(k)**2)
            if m.fib(k)>=3*16:
                for h in range(1,17):
                    z=m.circle_e(h*q)
                    self.assertGreaterEqual(abs(1-z)+1e-10,2/(3*h))

    def test_two_distinct_fixed_source_compatible_mirrors_cannot_be_irrational(self):
        # Both fixed mirror axes commuting with 16 map are multiples of 1/15.
        for a in [Fraction(k,15) for k in range(15)]:
            for b in [Fraction(k,15) for k in range(15)]:
                self.assertTrue(m.fixed_axis_commutes_radix(a-b))
        eta=m.golden_axis()
        self.assertGreater(abs(eta-Fraction(round(15*eta),15)),1e-3)


class VirtualSheetEnsembleTests(unittest.TestCase):
    def test_each_source_sheet_ensemble_is_exact_haar_below_modulus(self):
        for q in (7,11,31):
            for n in range(7):
                phases=[m.circle_e(Fraction(16**n*k,q)) for k in range(q)]
                self.assertLess(abs(sum(phases)),1e-11)

    def test_source_blind_orthogonal_ensemble_can_hide_selected_coherence(self):
        # ord_11(16)=5: first four time characters are all distinct.
        q,N,h=11,4,1
        self.assertEqual(len({pow(16,n,q) for n in range(N)}),N)
        for original in [[1+0j]*N,
                         [m.circle_e(Fraction(n*n+1,17)) for n in range(N)]]:
            S=[sum(original[n]*m.circle_e(Fraction(h*16**n*k,q))
                   for n in range(N)) for k in range(q)]
            self.assertAlmostEqual(sum(abs(x)**2 for x in S)/q,N,places=11)
            self.assertAlmostEqual(S[0],sum(original))
        self.assertEqual(abs(sum([1+0j]*N)),N)

    def test_two_forcing_sheets_are_exact_conjugates_but_not_same_source(self):
        U=m.original_states(35)
        for n in range(35):
            self.assertEqual(-U[n+1],16*(-U[n])-m.r_original(n+1))
        for h in (1,3,11):
            self.assertLess(abs(sum(m.circle_e(h*(-z)) for z in U)
                                -sum(m.circle_e(h*z) for z in U).conjugate()),1e-9)


if __name__ == '__main__':
    unittest.main()

"""Exact independent finite oracles for two-unit rational SUCC sundials."""
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

from observational_succ.portable_prime_sundial import (
    PortablePrimeSundial as Dial, SundialContractError,
    representation_alias_pair,
)
from observational_succ.rad_ris_transport import rad, ris


def dial(a,b,u,v):
    return Dial(a,b,u,v,"declared-test-source","explicit integer units")


class TestPortablePrimeSundial(unittest.TestCase):
    def test_all_small_2d_coupling_and_diagonal_determinant(self):
        for a,b,u,v in product(range(1,6),repeat=4):
            d=dial(a,b,u,v)
            D=u*b-v*a
            self.assertEqual(d.determinant(),D)
            self.assertEqual(d.offset_phase(),Fraction(a,u)-Fraction(b,v))
            for k,l in product(range(4),repeat=2):
                A,B=a+k*u,b+l*v
                self.assertEqual(d.arms(k,l),(A,B))
                self.assertEqual(d.ratio(k,l),Fraction(A,B))
                self.assertEqual(d.wedge(k,l),D+u*v*(l-k))
                mixed=(d.ratio(k+1,l+1)-d.ratio(k+1,l)
                       -d.ratio(k,l+1)+d.ratio(k,l))
                self.assertEqual(mixed,d.cross_mixed_difference(k,l))
            for n in range(4):
                self.assertEqual(d.wedge(n,n),D)
                self.assertEqual(d.diagonal_difference(n),
                                 d.ratio(n+1,n+1)-d.ratio(n,n))
                self.assertEqual(d.diagonal_stationary_error(n),
                                 d.ratio(n,n)-Fraction(u,v))
                g=gcd(*d.arms(n,n))
                self.assertEqual(D%g,0)
                if D:self.assertLessEqual(g,abs(D))

    def test_same_fraction_different_succ_futures(self):
        first,second=representation_alias_pair()
        self.assertEqual(first.ratio(0,0),second.ratio(0,0))
        self.assertEqual(first.ratio(0,0),Fraction(1,2))
        self.assertEqual(first.ratio(1,1),Fraction(2,3))
        self.assertEqual(second.ratio(1,1),Fraction(3,5))
        self.assertNotEqual(first.determinant(),second.determinant())
        self.assertNotEqual(first.offset_phase(),second.offset_phase())

    def test_homogeneous_scale_is_projective_not_identical_p_clock(self):
        original=dial(1,2,1,1)
        for m in (2,3,6):
            scaled=original.homogeneous_scale(m)
            for k,l in product(range(5),repeat=2):
                self.assertEqual(original.ratio(k,l),scaled.ratio(k,l))
                self.assertEqual(scaled.wedge(k,l),m*m*original.wedge(k,l))
                self.assertEqual(gcd(*scaled.arms(k,l)),m*gcd(*original.arms(k,l)))
            self.assertEqual(original.offset_phase(),scaled.offset_phase())
        self.assertNotEqual(original.prime_clock(2).numerator_class,
                            original.homogeneous_scale(2).prime_clock(2).numerator_class)

    def test_origin_shift_is_covariant_not_invariant(self):
        for a,b,u,v in product(range(1,4),repeat=4):
            frame=dial(a,b,u,v)
            for h,j in ((0,0),(2,3),(4,1)):
                rebased=frame.rebase(h,j)
                self.assertEqual(rebased.offset_phase(),frame.offset_phase()+h-j)
                self.assertEqual(rebased.determinant(),
                                 frame.determinant()+u*v*(j-h))
                for k,l in ((0,0),(2,1),(1,3)):
                    self.assertEqual(rebased.arms(k,l),frame.arms(k+h,l+j))
                    self.assertEqual(rebased.ratio(k,l),frame.ratio(k+h,l+j))

    def test_stationary_dial_has_growing_gcd_no_finite_D_bound(self):
        frame=dial(6,10,3,5)
        self.assertEqual(frame.determinant(),0)
        for n in (0,1,2,8,100,10000):
            self.assertEqual(frame.ratio(n,n),Fraction(3,5))
            self.assertEqual(frame.stationary_gcd_rule(n),(n+2,1))
            self.assertEqual(frame.diagonal_difference(n),0)
        with self.assertRaises(SundialContractError):
            frame.invertible_determinant_part()
        with self.assertRaises(SundialContractError):
            dial(1,2,1,1).stationary_gcd_rule(0)

    def test_prime_to_unit_D_divisor_is_constructively_attainable(self):
        for a,b,u,v in product(range(1,8),repeat=4):
            frame=dial(a,b,u,v)
            if frame.determinant():
                M,n=frame.invertible_determinant_part()
                self.assertEqual(gcd(M,u*v),1)
                self.assertEqual(abs(frame.determinant())%M,0)
                self.assertEqual(frame.diagonal_gcd(n)%M,0)
        sharp=dial(1,20,3,5)
        self.assertEqual(sharp.determinant(),55)
        self.assertEqual(sharp.invertible_determinant_part(),(11,7))

    def test_p_divides_D_not_sufficient_if_unit_noninvertible(self):
        frame=dial(1,2,2,2)
        self.assertEqual(frame.determinant(),2)
        self.assertIsNone(frame.prime_clock(2).numerator_class)
        self.assertIsNone(frame.prime_clock(2).diagonal_class)
        self.assertEqual(frame.prime_clock(2).diagonal_count,0)
        self.assertFalse(frame.crt_synchronize(((2,1),)).possible)

    def test_invertible_local_phases_and_repaired_offset(self):
        frame=dial(1,2,1,1)
        for p,r in ((2,1),(3,1),(5,1),(5,2),(7,2)):
            read=frame.prime_clock(p,r)
            M=p**r
            self.assertEqual(read.numerator_class,((-1)%M,M))
            self.assertEqual(read.denominator_class,((-2)%M,M))
            self.assertEqual(read.relative_phase,(-1)%M)
            self.assertIsNone(read.diagonal_class)
            self.assertEqual(frame.prime_clock(p,r,offset=-1).diagonal_class,
                             ((-1)%M,M))
        combined=frame.crt_synchronize(((2,2),(3,1),(5,1)),offset=-1)
        self.assertTrue(combined.possible)
        self.assertEqual(combined.class_modulus,60)
        self.assertEqual((combined.first_nonnegative_k,combined.first_nonnegative_l),
                         (59,58))
        self.assertEqual(gcd(*frame.arms(59,58)),60)

    def test_modular_brute_force_oracle_with_partial_nonunit_clocks(self):
        # Does NOT call _arm_clock: compare complete residue sets mod p^r.
        for a,b,u,v in product(range(1,5),repeat=4):
            frame=dial(a,b,u,v)
            for p,r in ((2,1),(2,2),(2,3),(3,1),(3,2),(5,1)):
                M=p**r
                for offset in (-2,0,3):
                    read=frame.prime_clock(p,r,offset=offset)
                    A={n for n in range(M) if (a+n*u)%M==0}
                    B={n for n in range(M) if (b+(n+offset)*v)%M==0}
                    def decode(x):
                        return set() if x is None else {
                            n for n in range(M) if (n-x[0])%x[1]==0}
                    self.assertEqual(decode(read.numerator_class),A)
                    self.assertEqual(decode(read.denominator_class),B)
                    self.assertEqual(decode(read.diagonal_class),A&B)
                    self.assertEqual(read.diagonal_count,len(A&B))
                    self.assertEqual(read.independent_grid_count,len(A)*len(B))
                    if offset==0 and gcd(u*v,M)==1:
                        self.assertEqual(bool(A&B),(u*b-v*a)%M==0)
                        self.assertEqual(read.relative_phase,
                                         ((-b*pow(v,-1,M))-(-a*pow(u,-1,M)))%M)
                    elif gcd(u*v,M)>1:
                        self.assertIsNone(read.relative_phase)

    def test_two_prime_crt_oracle_with_signed_offset(self):
        for a,b,u,v in product(range(1,5),repeat=4):
            frame=dial(a,b,u,v)
            specs=((2,2),(3,1))
            for offset in (-1,0,2):
                report=frame.crt_synchronize(specs,offset)
                low=max(0,-offset)
                oracle=[n for n in range(low,low+12)
                        if all((a+n*u)%(p**r)==0 and
                               (b+(n+offset)*v)%(p**r)==0
                               for p,r in specs)]
                self.assertEqual(report.possible,bool(oracle))
                if oracle:
                    self.assertEqual(report.first_nonnegative_k,min(oracle))
                    self.assertEqual(report.first_nonnegative_l,min(oracle)+offset)
                    self.assertEqual(report.first_nonnegative_k%report.class_modulus,
                                     report.residue)
                else:self.assertIsNone(report.residue)

    def test_rad_anchored_prime_births_exhaustive(self):
        for a,b in product(range(1,55),repeat=2):
            frame=Dial.rad_anchored(a,b,"integer-source")
            for k,l in ((0,0),(1,2),(3,1)):
                A,B=frame.arms(k,l)
                result=frame.rad_births(k,l)
                for item,value,original,unit,step in zip(
                    result,(A,B),(a,b),(frame.u,frame.v),(k,l)):
                    self.assertEqual(item.actual_radical,rad(value))
                    self.assertEqual(item.actual_residual,ris(value))
                    self.assertEqual(item.prime_birth_product*unit,rad(value))
                    self.assertEqual(item.residual_step*unit,value)
                    self.assertEqual(item.original_residual,ris(original))
                    self.assertEqual(item.residual_step,ris(original)+step)
        witness=Dial.rad_anchored(12,18,"integer-source")
        self.assertEqual(witness.determinant(),36)
        self.assertEqual(witness.diagonal_gcd(2),6)
        rows=witness.rad_births(2,2)
        self.assertEqual((rows[0].actual_radical,rows[0].actual_residual),(6,4))
        self.assertEqual((rows[1].actual_radical,rows[1].actual_residual),(30,1))
        self.assertEqual(rows[1].new_prime_support,(5,))

    def test_factorial_style_prime_power_wheel_and_frame_portability(self):
        specs=((2,3),(3,1),(5,1))
        frame=dial(1,2,1,1)
        wheel=frame.phase_wheel(specs)
        self.assertEqual(wheel.wheel,120)
        self.assertEqual((wheel.numerator_zero_time,wheel.denominator_zero_time),
                         (119,118))
        self.assertEqual(wheel.phase_offset,119)
        self.assertEqual((wheel.simultaneous_k,wheel.simultaneous_l),(119,238))
        self.assertEqual(frame.arms(119,238),(120,240))
        for h,j in ((0,0),(2,3),(7,1)):
            newer=frame.rebase(h,j).phase_wheel(specs)
            self.assertEqual(newer.phase_offset,(wheel.phase_offset+h-j)%120)
            self.assertEqual(newer.numerator_zero_time,
                             (wheel.numerator_zero_time-h)%120)
            self.assertEqual(newer.denominator_zero_time,
                             (wheel.denominator_zero_time-j)%120)
        for m in (7,11,13):
            newer=frame.homogeneous_scale(m).phase_wheel(specs)
            self.assertEqual(newer.phase_offset,wheel.phase_offset)
        with self.assertRaises(SundialContractError):
            frame.homogeneous_scale(2).phase_wheel(specs)

    def test_all_small_invertible_phase_wheels_independent_roots(self):
        specs=((2,2),(3,1))
        W=12
        for a,b,u,v in product(range(1,7),repeat=4):
            if gcd(u*v,W)!=1:continue
            frame=dial(a,b,u,v)
            w=frame.phase_wheel(specs)
            self.assertEqual(w.phase_offset,
                             (w.denominator_zero_time-w.numerator_zero_time)%W)
            self.assertEqual((a+w.numerator_zero_time*u)%W,0)
            self.assertEqual((b+w.denominator_zero_time*v)%W,0)
            A,B=frame.arms(w.simultaneous_k,w.simultaneous_l)
            self.assertEqual(A%W,0)
            self.assertEqual(B%W,0)

    def test_false_prime_and_source_contracts_rejected(self):
        for bad in ((0,1,1,1),(1,0,1,1),(1,1,-1,1),
                    (1,1,1,0),(True,1,1,1)):
            with self.assertRaises(SundialContractError):dial(*bad)
        frame=dial(1,2,1,1)
        for p,r in ((4,1),(1,1),(2,0),(2,False),(2,16)):
            with self.assertRaises(SundialContractError):frame.prime_clock(p,r)
        for specs in (((2,1),(2,2)),((5,1),(3,1))):
            with self.assertRaises(SundialContractError):
                frame.crt_synchronize(specs)
        with self.assertRaises(SundialContractError):frame.ratio(-1,0)
        with self.assertRaises(SundialContractError):frame.rebase(0,-1)
        with self.assertRaises(SundialContractError):
            frame.prime_clock(5,1,offset=0.5)
        with self.assertRaises(SundialContractError):frame.rad_births(0,0)
        with self.assertRaises(SundialContractError):
            Dial.rad_anchored(1_000_001,2,"source")

    def test_original_source_and_physical_clock_are_not_authenticated(self):
        frame=Dial.rad_anchored(12,18,"declared-s","RAD")
        for n in range(12):
            cert=frame.diagonal_gcd_certificate(n)
            self.assertTrue(cert["gcd_divides_D"])
            self.assertTrue(cert["bounded_by_abs_D_if_nonzero"])
            self.assertLessEqual(cert["gcd"],abs(cert["D"]))
            self.assertEqual(frame.diagonal_difference(n),
                             Fraction(cert["D"],cert["B"]*(cert["B"]+frame.v)))
        self.assertFalse(frame.prime_clock(5).source_authenticated)

    def test_three_shadows_reconstruct_entire_projective_dynamics(self):
        # Independent future evaluations, not copied from the reconstruction
        # algorithm. Equality includes every tested (k,l), not only diagonal.
        for a,b,u,v in product(range(1,6),repeat=4):
            c=dial(a,b,u,v)
            s=c.three_shadows()
            self.assertEqual(s.normalized_a,Fraction(a,b))
            self.assertEqual(s.normalized_u,Fraction(u,b))
            self.assertEqual(s.normalized_v,Fraction(v,b))
            d=Dial.reconstruct_three_shadows(
                s.origin,s.numerator_step,s.denominator_step,
                "new projective representative","source-unknown integer scale")
            self.assertTrue(c.projectively_equal(d))
            self.assertFalse(s.source_authenticated)
            self.assertFalse(s.counterfactual_probes_authorized)
            self.assertEqual(gcd(gcd(d.a,d.b),gcd(d.u,d.v)),1)
            for k,l in product(range(4),repeat=2):
                self.assertEqual(c.ratio(k,l),d.ratio(k,l))
                x,y,z=s.normalized_a,s.normalized_u,s.normalized_v
                self.assertEqual(c.ratio(k,l),(x+k*y)/(1+l*z))
            self.assertEqual(c.offset_phase(),d.offset_phase())

    def test_all_three_canonical_shadows_needed_independent_countermodels(self):
        base=dial(1,2,1,1)
        change_den_unit=dial(1,2,1,2)
        change_num_unit=dial(1,2,2,1)
        change_initial=dial(2,3,1,3)
        def shadows(x):
            return (x.ratio(0,0),x.ratio(1,0),x.ratio(0,1))
        a=shadows(base)
        b=shadows(change_den_unit)
        c=shadows(change_num_unit)
        d=shadows(change_initial)
        self.assertEqual(a[:2],b[:2])
        self.assertNotEqual(a[2],b[2])
        self.assertEqual((a[0],a[2]),(c[0],c[2]))
        self.assertNotEqual(a[1],c[1])
        self.assertEqual(a[1:],d[1:])
        self.assertNotEqual(a[0],d[0])
        self.assertFalse(base.projectively_equal(change_den_unit))
        self.assertFalse(base.projectively_equal(change_num_unit))
        self.assertFalse(base.projectively_equal(change_initial))

    def test_projective_equivalence_cannot_identify_absolute_prime_occupancy(self):
        x=dial(1,2,1,1)
        y=x.homogeneous_scale(2)
        self.assertTrue(x.projectively_equal(y))
        self.assertEqual(x.three_shadows().normalized_a,
                         y.three_shadows().normalized_a)
        self.assertEqual(x.three_shadows().normalized_u,
                         y.three_shadows().normalized_u)
        self.assertEqual(x.three_shadows().normalized_v,
                         y.three_shadows().normalized_v)
        self.assertEqual(x.offset_phase(),y.offset_phase())
        self.assertNotEqual(x.diagonal_gcd(0),y.diagonal_gcd(0))
        self.assertNotEqual(x.prime_clock(2).numerator_class,
                            y.prime_clock(2).numerator_class)
        # Reduced reconstructed frame is valid as a mathematical model,
        # but not certified as the actual original-source integer scale.
        z=Dial.reconstruct_three_shadows(
            y.ratio(0,0),y.ratio(1,0),y.ratio(0,1),
            "declared reconstruction only","canonical projective")
        self.assertEqual(z.arms(0,0),(1,2))
        self.assertNotEqual(z.arms(0,0),y.arms(0,0))

    def test_shadow_reconstruction_rejects_invalid_or_float_probes(self):
        values=(
          (0.5,Fraction(1),Fraction(1,3)),
          (Fraction(1,2),Fraction(1,2),Fraction(1,3)),
          (Fraction(1,2),Fraction(1),Fraction(1,2)),
          (Fraction(1,2),Fraction(1),Fraction(0)),
          (Fraction(1,2),Fraction(1),Fraction(3,4)),
        )
        for x,y,z in values:
            with self.assertRaises(SundialContractError):
                Dial.reconstruct_three_shadows(x,y,z,"s","b")
        with self.assertRaises(SundialContractError):
            dial(1,2,1,1).projectively_equal("1/2")

    def test_reproduce_exact_finite_receipt_subprocess(self):
        root=Path(__file__).resolve().parents[1]
        p=subprocess.run([sys.executable,"-m","scripts.portable_prime_sundial_probe"],
                         cwd=root,capture_output=True,text=True,check=True)
        report=json.loads(p.stdout)
        self.assertEqual(report["status"],
                         "EXACT_FINITE_PORTABLE_SUNDIAL_SOURCE_CONTRACT")
        self.assertEqual(report["independent_frames_checked"],256)
        self.assertEqual(report["prime_power_clock_readings_checked"],1024)
        self.assertEqual(report["diagonal_prime_power_windows_nonempty"],306)
        self.assertEqual(report["invalid_source_or_clock_contracts_rejected"],2)
        self.assertEqual(report["prime_phase_wheel"]["relative_phase"],119)
        self.assertEqual(report["three_shadow_reconstruction"]["readings"],
                         ["1/2","1","1/3"])
        self.assertEqual(report["three_shadow_reconstruction"]["canonical_frame"],
                         [1,2,1,1])
        self.assertEqual(report["three_shadow_reconstruction"]["homothetic_other_frame"],
                         [2,4,2,2])
        self.assertTrue(report["three_shadow_reconstruction"]["ratio_paths_equivalent"])
        self.assertFalse(report["three_shadow_reconstruction"]["original_integer_scale_authenticated"])
        self.assertFalse(report["three_shadow_reconstruction"]["counterfactual_probe_access_authorized"])
        self.assertFalse(report["source_authenticated"])
        self.assertFalse(report["physical_time_model"])
        self.assertFalse(report["primality_inferred_from_phase"])
        self.assertFalse(report["ABC_proved"])
        self.assertFalse(report["RH_proved"])
        self.assertFalse(report["signed_Weil_positive"])


if __name__=="__main__":
    unittest.main()

import unittest
import math
from fractions import Fraction
from observational_succ.golden_circle_triangle import *

class ExactGoldenTest(unittest.TestCase):
    def test_irrational_sign(self):
        self.assertEqual((ALPHA*ALPHA+ALPHA-ONE),ZERO)
        self.assertEqual((ALPHA-ONE).sign(),-1)
        self.assertEqual((ONE-ALPHA).sign(),1)
        self.assertEqual((ALPHA*ALPHA).sign(),1)
        self.assertEqual((ZGolden(1,-2)).sign(),-1)
    def test_floor_is_exact_for_near_integer(self):
        for n in range(0,251):
            x=golden_phase(n)
            self.assertGreaterEqual(x.sign(),0)
            self.assertGreater((ONE-x).sign(),0)
            self.assertEqual(x.b,n)
    def test_return_identity(self):
        for k in range(1,45):
            left=ZGolden(-fibonacci(k-1),fibonacci(k))
            right=alpha_power(k)
            if k%2==0:right=ZGolden(-right.a,-right.b)
            self.assertEqual(left,right)
    def test_gap_invariant_and_exact_refinement(self):
        for k in range(3,15):
            gaps=mesh_gaps(k)
            L,S=alpha_power(k-2),alpha_power(k-1)
            self.assertEqual(len(gaps),fibonacci(k))
            self.assertEqual(sum(g==L for _,_,g in gaps),fibonacci(k-1))
            self.assertEqual(sum(g==S for _,_,g in gaps),fibonacci(k-2))
            self.assertEqual(sum(g!=L and g!=S for _,_,g in gaps),0)
            forward=k%2==1
            starts={(a if forward else b) for a,b,g in gaps if g==L}
            self.assertEqual(starts,set(range(fibonacci(k-1))))
            result=insertions_and_parents(k)
            self.assertEqual(len(result),fibonacci(k-1))
            self.assertEqual({new for _,new,_ in result},set(range(fibonacci(k),fibonacci(k+1))))
    def test_every_long_gap_splits_into_exact_two_children(self):
        for k in range(3,13):
            N=fibonacci(k)
            old=mesh_gaps(k)
            new=mesh_gaps(k+1)
            old_edges={(a,b):g for a,b,g in old}
            new_edges={(a,b):g for a,b,g in new}
            sign=k%2==1
            for j in range(fibonacci(k-1)):
                new_index=N+j
                if sign:
                    a,b=next((a,b) for a,b,g in old if a==j and g==alpha_power(k-2))
                    self.assertEqual(new_edges[(a,new_index)],alpha_power(k))
                    self.assertEqual(new_edges[(new_index,b)],alpha_power(k-1))
                else:
                    a,b=next((a,b) for a,b,g in old if b==j and g==alpha_power(k-2))
                    self.assertEqual(new_edges[(a,new_index)],alpha_power(k-1))
                    self.assertEqual(new_edges[(new_index,b)],alpha_power(k))
    def test_gap_sum_exact(self):
        for k in range(3,25):
            total=ZGolden(0,0)
            for i in range(fibonacci(k-1)): total=total+alpha_power(k-2)
            for i in range(fibonacci(k-2)):total=total+alpha_power(k-1)
            self.assertEqual(total,ONE)
    def test_original_four_poles_exact(self):
        self.assertEqual(original_four_pole(1),Fraction(47,15))
        self.assertEqual(len(zero_seed_epoch(9)),9)
        self.assertEqual(zero_seed_epoch(1),[Fraction(2,15)])
        with self.assertRaises(ValueError):original_four_pole(0)
        with self.assertRaises(ValueError):golden_phase(-1)

class AnalyticNumericControl(unittest.TestCase):
    def test_geometry_area_scaling(self):
        phi=(1+math.sqrt(5))/2
        lam=1/phi
        C=golden_area_constant()
        vals=[]
        for k in (8,10,12,14,16):
            L=2*math.pi*lam**(k-2);S=2*math.pi*lam**(k-1)
            # stable theta-sin(theta) avoids catastrophic cancellation at high k
            def delta(x):return x-math.sin(x)
            deficit=(fibonacci(k-1)*delta(L)+fibonacci(k-2)*delta(S))/2
            vals.append(fibonacci(k)**2*deficit)
        self.assertLess(abs(vals[-1]-C),0.0005)
        self.assertLess(abs(vals[-1]-C),abs(vals[0]-C))
    def test_nodal_quadrature_all_harmonics(self):
        pts=[0., 0.1, 0.34, 0.77, 0.991]
        for k in (5,7,9):
            for h in (1,2,3,16):
                true,sur,bud=triangle_signed_weyl(pts,h,k)
                self.assertLessEqual(abs(true-sur),bud+3e-13)
    def test_coherent_alias_rejected(self):
        for k in (6,9,12):
            true,sur,bud=triangle_signed_weyl([0.]*50,1,k)
            self.assertEqual(true,1)
            self.assertLessEqual(abs(true-sur),bud+3e-13)
            self.assertGreater(abs(sur),0.5)
    def test_original_zero_seed_controls(self):
        for A in (8,16,32):
            phases=[float(x) for x in zero_seed_epoch(A)]
            k=next(k for k in range(3,18) if fibonacci(k)<=A<fibonacci(k+1))
            for h in (1,2,5):
                true,sur,bud=triangle_signed_weyl(phases,h,k)
                self.assertLessEqual(abs(true-sur),bud+3e-12)
    def test_sine_gap_and_triangle_area(self):
        lam=(math.sqrt(5)-1)/2
        for k in range(3,18):
            a,b=lam**k,lam**(k-1)
            L=a+b
            self.assertAlmostEqual(L,lam**(k-2),places=13)
            area=(math.sin(2*math.pi*a)+math.sin(2*math.pi*b)-math.sin(2*math.pi*L))/2
            product=2*math.sin(math.pi*a)*math.sin(math.pi*b)*math.sin(math.pi*L)
            self.assertAlmostEqual(area,product,places=13)
            self.assertGreater(area,0)
    def test_complex_Pascal_circle_native_nonHaar(self):
        lam=(math.sqrt(5)-1)/2
        # Source rank=2, clock theta=1; old TΓ-04 limiting transform.
        for h in (1,2,3,5,13,144):
            z=complex(math.cos(2*math.pi*h*lam),math.sin(2*math.pi*h*lam))
            val=(2-z)**(-2)
            self.assertGreaterEqual(abs(val)+1e-15,1/9)
            self.assertNotEqual(val,0)
    def test_phase_offsets_nonrealization(self):
        # Two finite sensor readings are not all history: grade-only conditional
        # example from OPERATIONAL_TRIANGLE remains a separate witness.
        self.assertEqual(golden_phase(2).b,2)
        self.assertNotEqual(golden_phase(1),golden_phase(2))

if __name__=='__main__':unittest.main()

class NativePascalSourceControl(unittest.TestCase):
    def test_source_R_equals_original_forcing(self):
        for n in range(1,45):
            self.assertEqual(source_R(8*n-7),original_four_pole(n))
    def test_exact_grade_and_normalization(self):
        for a in (1,9,17,65):
            for m in range(0,15):
                q=pascal_source_grade_weights(a,m)
                self.assertEqual(len(q),m+1)
                self.assertEqual(sum(q),1)
                self.assertTrue(all(t>0 for t in q))
                if m>0:
                    self.assertEqual(q[0],source_R(a+8*m)/source_R(a))
    def test_native_diagonal_nonHaar(self):
        lam=(math.sqrt(5)-1)/2
        for h in (1,2,3):
            z=complex(math.cos(2*math.pi*h*lam),math.sin(2*math.pi*h*lam))
            target=(2-z)**(-2)
            old=1e6
            for n in (8,16,32):
                result=pascal_circle_character(8*n-7,n,h)
                err=abs(result-target)
                self.assertLess(err,old)
                old=err
            self.assertLess(old,0.16)
    def test_scalar_character_and_binomial_R_identity(self):
        from math import comb
        lam=(math.sqrt(5)-1)/2
        for a,m,h in ((1,2,1),(9,5,2),(17,9,3),(65,12,4)):
            z=complex(math.cos(2*math.pi*h*lam),math.sin(2*math.pi*h*lam))
            direct=sum(comb(m,k)*z**(m-k)*(1-z)**k*float(source_R(a+8*k)/source_R(a))
                       for k in range(m+1))
            self.assertLess(abs(direct-pascal_circle_character(a,m,h)),3e-10)

class HistorySensitiveTriangle(unittest.TestCase):
    def test_lag_energy_interpolation(self):
        lam=(math.sqrt(5)-1)/2
        for A in (8,16,32):
            pts=[float(x) for x in zero_seed_epoch(A)]
            k=next(k for k in range(3,18) if fibonacci(k)<=A<fibonacci(k+1))
            for h in (1,2,5):
                for H in (1,2,min(5,A),A):
                    truth,observed,budget=triangle_lag_energy(pts,h,k,H)
                    self.assertLessEqual(abs(truth-observed),budget+1e-12)
                    self.assertGreaterEqual(observed,-1e-13)
    def test_coherent_wrong_seed_not_erased(self):
        A=64
        points=[0.]*A
        k=next(k for k in range(3,18) if fibonacci(k)<=A<fibonacci(k+1))
        H=16
        e_true,e_triang,bound=triangle_lag_energy(points,1,k,H)
        expected=1-(H*H-1)/(3*A*H)
        self.assertAlmostEqual(e_true,expected,places=13)
        self.assertAlmostEqual(e_triang,expected,places=13)
        self.assertGreater(e_true,0.9)
    def test_time_reordering_affects_lag_not_spatial(self):
        pts=[0,0,0.5,0.5,0,0.5,0.5,0]
        shuffle=[0,0.5,0,0.5,0,0.5,0,0.5]
        k=7
        spatial1=triangle_signed_weyl(pts,1,k)[1]
        spatial2=triangle_signed_weyl(shuffle,1,k)[1]
        self.assertLess(abs(spatial1-spatial2),1e-14)
        e1=triangle_lag_energy(pts,1,k,3)[0]
        e2=triangle_lag_energy(shuffle,1,k,3)[0]
        self.assertGreater(abs(e1-e2),0.04)
"""Source-specific exact Fourier, Mellin, Haar tests; no zero input."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.classical_tate_window import (
    TateWindowError,Cyclo,TateWindow,diagonal_additive_phases,
    classical_tate_window_probe,
)
from observational_succ.classical_tate_arch_global import (
    PiMonomial,real_gaussian_mellin_integer,
    scaled_real_gaussian_mellin_integer,arch_critical_scale,
    finite_true_euler_product,euler_dirichlet_coefficients,
    euler_tail_contract,arch_global_probe,
)


class ExactCyclotomicTests(unittest.TestCase):
    def test_root_conductor_and_orthogonality(self):
        for p,r in ((2,0),(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)):
            N=p**r
            one=Cyclo.scalar(p,r,1)
            root=Cyclo.phase(p,r,1)
            self.assertEqual(root*root.conjugate(),one)
            self.assertEqual(Cyclo.phase(p,r,N),one)
            self.assertEqual(root*root, Cyclo.phase(p,r,2))
            for k in range(N):
                self.assertEqual(Cyclo.phase(p,r,k).conjugate(),Cyclo.phase(p,r,-k))
            if N>1:
                self.assertEqual(sum((Cyclo.phase(p,r,k) for k in range(N)),
                                     Cyclo.scalar(p,r,0)),Cyclo.scalar(p,r,0))

    def test_exact_root_field_embedding_and_guard(self):
        for p,r in ((2,1),(2,2),(3,1),(3,2)):
            if p**(r+1)>256: continue
            for k in range(p**r):
                lo=Cyclo.phase(p,r,k)
                self.assertEqual(lo.embed(r+1),Cyclo.phase(p,r+1,k*p))
                self.assertEqual((lo*lo.conjugate()).embed(r+1),
                                 lo.embed(r+1)*lo.embed(r+1).conjugate())
        with self.assertRaises(TateWindowError):
            Cyclo.scalar(6,1,1)
        with self.assertRaises(TateWindowError):
            Cyclo.scalar(2,1,Q(1,3)) + Cyclo.scalar(3,1,1)
        with self.assertRaises(TateWindowError):
            Cyclo.scalar(2,1,1).embed(0)
        with self.assertRaises(TateWindowError):
            Cyclo.scalar(2,1,0.5)


class FiniteTateSchwartzAtlasTests(unittest.TestCase):
    def test_fourier_inversion_and_plancherel_two_independent_rational_packets(self):
        for p,a,b in ((2,0,0),(2,0,1),(2,2,1),(2,1,2),
                      (3,0,1),(3,1,1),(5,0,1),(5,1,0)):
            w=TateWindow(p,a,b)
            f=w.vector([Q((j*3+2)%7-3,4) for j in range(w.size)])
            g=w.vector([Q((j*j+4)%5-2,7) for j in range(w.size)])
            d=TateWindow(p,b,a)
            ff=w.fourier(f)
            gg=w.fourier(g)
            self.assertEqual(d.fourier(ff),w.invert(f))
            self.assertEqual(w.inner(f,g),d.inner(ff,gg))
            self.assertEqual(w.additive_integral(f),ff[0])
            self.assertEqual(w.inner(f,f),d.inner(ff,ff))

    def test_direct_known_hadamard_and_gauss_phase_controls(self):
        w=TateWindow(2,0,1)
        one=w.vector((1,0))
        self.assertEqual(w.fourier(one),w.vector((Q(1,2),Q(1,2))))
        self.assertEqual(w.fourier(w.vector((0,1))),w.vector((Q(1,2),Q(-1,2))))
        w3=TateWindow(3,0,1)
        delta=w3.vector((0,1,0))
        root=Cyclo.phase(3,1,1)
        self.assertEqual(w3.fourier(delta),w3.vector((Q(1,3),root/3,root*root/3)))

    def test_support_precision_refinements_commute_with_source_fourier(self):
        for p,a,b in ((2,0,1),(2,1,1),(2,1,2),(3,0,1),(3,1,1),(5,0,1)):
            w=TateWindow(p,a,b)
            if p**(a+b+1)>64:continue
            f=w.vector([Q((j*7+3)%9-4,6) for j in range(w.size)])
            d=TateWindow(p,b,a)
            self.assertEqual(TateWindow(p,a+1,b).fourier(w.support_expand(f)),
                             d.precision_refine(w.fourier(f)))
            self.assertEqual(TateWindow(p,a,b+1).fourier(w.precision_refine(f)),
                             d.support_expand(w.fourier(f)))
            self.assertEqual(TateWindow(p,a+1,b).additive_integral(w.support_expand(f)),
                             w.additive_integral(f).embed(a+b+1))
            self.assertEqual(TateWindow(p,a,b+1).additive_integral(w.precision_refine(f)),
                             w.additive_integral(f).embed(a+b+1))

    def test_unramified_full_test_function_mellin_functional_equation(self):
        count=0
        for p,a,b in ((2,0,1),(2,1,1),(2,0,3),(3,0,2),(3,1,1),(5,0,1)):
            w=TateWindow(p,a,b)
            d=TateWindow(p,b,a)
            for f in (w.vector([int(j==0) for j in range(w.size)]),
                      w.vector([Q((5*j+3)%7-3,8) for j in range(w.size)]),
                      w.vector([Q((j+1)%4-2,5) for j in range(w.size)])):
                for sigma,omega in product((2,3,4),(-1,1)):
                    lhs=w.unramified_mellin(f,sigma,omega)
                    rhs=d.unramified_mellin(w.fourier(f),1-sigma,omega)
                    self.assertEqual(lhs, w.unramified_ratio(sigma,omega)*rhs)
                    count+=1
        self.assertEqual(count,108)

    def test_wrong_haar_and_missing_half_density_controls(self):
        w=TateWindow(3,0,1)
        f=w.vector((1,0,0))
        actual=w.unramified_mellin(f,2)
        ratio=w.unramified_ratio(2)
        dual=TateWindow(3,1,0).unramified_mellin(w.fourier(f),-1)
        self.assertEqual(actual,ratio*dual)
        self.assertNotEqual(actual,ratio*(3*dual))
        with self.assertRaises(TateWindowError):
            w.unramified_mellin(f,0,1)
        with self.assertRaises(TateWindowError):
            TateWindow(6,0,1)
        with self.assertRaises(TateWindowError):
            TateWindow(2,4,3)

    def test_higher_conductor_phase_lost_under_coarsening(self):
        w=TateWindow(3,0,2)
        a=w.vector([int(k==1) for k in range(9)])
        b=w.vector([int(k==4) for k in range(9)])
        # Both live over the same residue mod 3, but differ mod 9.
        self.assertEqual(tuple(sum(a[k].coeff[0] for k in range(j,9,3))
                               for j in range(3)),
                         tuple(sum(b[k].coeff[0] for k in range(j,9,3))
                               for j in range(3)))
        self.assertNotEqual(w.fourier(a)[1],w.fourier(b)[1])

    def test_global_additive_rational_character_exact_product(self):
        for q in (Q(0),Q(1,6),Q(-2,9),Q(17,35),Q(23,36),Q(-7,10)):
            r=diagonal_additive_phases(q)
            self.assertTrue(r['diagonal_global_character_equals_one'])
            phases=sum((Q(v) for _,v in r['finite_places']),Q(0))
            self.assertEqual(phases-q,Q(r['total_integer_phase']))


class ArchimedeanAndEulerTests(unittest.TestCase):
    def test_gaussian_exact_gamma_succ_recurrence_and_scaling(self):
        for s in range(1,16):
            lhs=real_gaussian_mellin_integer(s+2)
            rhs=real_gaussian_mellin_integer(s).multiply_rational(Q(s,2)).times_pi_power(-1)
            self.assertEqual(lhs,rhs)
            for scale in (1,2,3):
                self.assertEqual(scaled_real_gaussian_mellin_integer(s,scale),
                                 real_gaussian_mellin_integer(s).multiply_rational(Q(scale)**(-s)))
        for scale in (1,2,3,4):
            self.assertTrue(arch_critical_scale(scale)['critical_s_half_source_duality'])
        with self.assertRaises(TateWindowError):
            real_gaussian_mellin_integer(0)
        with self.assertRaises(TateWindowError):
            scaled_real_gaussian_mellin_integer(2,0)

    def test_euler_prime_source_and_non_euler_mutant(self):
        for pset in ((2,),(2,3),(2,3,5),(2,3,5,7)):
            for sigma in (2,3,4):
                product_value=finite_true_euler_product(pset,sigma)
                self.assertGreater(product_value,1)
                coeff=euler_dirichlet_coefficients(pset,60)
                partial=sum((Q(coeff[n],n**sigma) for n in range(1,61)),Q(0))
                self.assertLess(partial,product_value)
        self.assertEqual(euler_dirichlet_coefficients((2,3,5),20)[6],1)
        self.assertEqual(euler_dirichlet_coefficients((2,3,5,6),20)[6],2)
        with self.assertRaises(TateWindowError):
            finite_true_euler_product((2,3,6),2)
        with self.assertRaises(TateWindowError):
            finite_true_euler_product((3,2),2)

    def test_euler_tail_bound_is_halfplane_only(self):
        for P,s in ((2,2),(11,2),(17,3)):
            r=euler_tail_contract(P,s)
            self.assertFalse(r['valid_on_critical_line'])
            self.assertEqual(Q(r['uniform_absolute_tail_upper']),Q(P)**(1-s)/Q(s-1))
        self.assertFalse(arch_global_probe()['RH_or_Weil_sign_claimed'])
        self.assertFalse(classical_tate_window_probe()['signed_Weil_positivity_or_RH_proved'])


if __name__=='__main__':
    unittest.main()

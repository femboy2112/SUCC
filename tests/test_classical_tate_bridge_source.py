"""Exact full-coset source controls for the new Tate local interface.

All-test theorems are proved separately in the classical Tate dossier.
Finite evaluations are exact Fraction/cyclotomic calibrations only.
"""
import unittest
from fractions import Fraction as Q

from observational_succ.classical_tate_window import (
    TateWindow, TateWindowError, Cyclo, diagonal_additive_phases,
    classical_tate_window_probe,
)
from observational_succ.classical_tate_arch_global import (
    arch_global_probe, euler_dirichlet_coefficients, euler_tail_contract,
    real_gaussian_mellin_integer,
)


class LocalTateBridgeTests(unittest.TestCase):
    def test_fourier_inversion_and_plancherel(self):
        for p,a,b in ((2,0,1),(2,1,1),(3,0,2),(3,1,1),(5,0,1)):
            w=TateWindow(p,a,b)
            f=w.vector([Q((j*3+2)%7-3,4) for j in range(w.size)])
            g=w.vector([Q((j*j+4)%5-2,7) for j in range(w.size)])
            d=TateWindow(p,b,a)
            self.assertEqual(d.fourier(w.fourier(f)),w.invert(f))
            self.assertEqual(w.inner(f,g),d.inner(w.fourier(f),w.fourier(g)))
            self.assertEqual(w.additive_integral(f),w.fourier(f)[0])

    def test_support_and_precision_sources_have_dual_transports(self):
        for p,a,b in ((2,0,1),(2,1,1),(3,0,1),(3,1,1),(5,0,1)):
            w=TateWindow(p,a,b)
            f=w.vector([Q((j*7+3)%9-4,6) for j in range(w.size)])
            d=TateWindow(p,b,a)
            self.assertEqual(TateWindow(p,a+1,b).fourier(w.support_expand(f)),
                             d.precision_refine(w.fourier(f)))
            self.assertEqual(TateWindow(p,a,b+1).fourier(w.precision_refine(f)),
                             d.support_expand(w.fourier(f)))

    def test_whole_coset_mellin_local_equation_sampled_exactly(self):
        for p,a,b in ((2,0,1),(2,1,1),(3,0,1),(5,0,1)):
            w=TateWindow(p,a,b)
            f=w.vector([Q((j*5+3)%7-3,8) for j in range(w.size)])
            dual=TateWindow(p,b,a)
            for s in (2,3,4):
                for omega in (-1,1):
                    self.assertEqual(w.unramified_mellin(f,s,omega),
                        dual.unramified_mellin(w.fourier(f),1-s,omega)
                        * w.unramified_ratio(s,omega))

    def test_rational_character_and_wrong_haar(self):
        self.assertTrue(diagonal_additive_phases(Q(1,6))
                        ["diagonal_global_character_equals_one"])
        w=TateWindow(3,0,1)
        f=w.vector((1,0,0))
        left=w.unramified_mellin(f,2)
        right=TateWindow(3,1,0).unramified_mellin(w.fourier(f),-1)
        self.assertEqual(left,w.unramified_ratio(2)*right)
        self.assertNotEqual(left,3*w.unramified_ratio(2)*right)
        with self.assertRaises(TateWindowError):
            TateWindow(6,0,1)

    def test_conductor_phase_and_gamma_euler_mutations(self):
        w=TateWindow(3,0,2)
        f=w.vector([int(j==1) for j in range(9)])
        g=w.vector([int(j==4) for j in range(9)])
        self.assertNotEqual(w.fourier(f)[1],w.fourier(g)[1])
        self.assertEqual(euler_dirichlet_coefficients((2,3,5),20)[6],1)
        self.assertEqual(euler_dirichlet_coefficients((2,3,5,6),20)[6],2)
        self.assertEqual(real_gaussian_mellin_integer(5),
                         real_gaussian_mellin_integer(3)
                         .multiply_rational(Q(3,2)).times_pi_power(-1))
        self.assertFalse(euler_tail_contract(17,2)["valid_on_critical_line"])
        self.assertFalse(arch_global_probe()["RH_or_Weil_sign_claimed"])

    def test_exact_receipt_scope(self):
        receipt=classical_tate_window_probe()
        self.assertEqual(receipt["full_coset_functional_equations_checked"],36)
        self.assertFalse(receipt["global_adelic_Poisson_derived"])
        self.assertFalse(receipt["signed_Weil_positivity_or_RH_proved"])


if __name__=="__main__":
    unittest.main()

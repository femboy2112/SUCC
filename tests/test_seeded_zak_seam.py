"""Root-discoverable exact controls for the seeded arithmetic/Zak seam."""
import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/'research'/'2026-10-31'/'seeded_zak_seam'

def load_unique(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

m=load_unique('succ_seeded_zak_seam_source_20261031',DIR/'seeded_seam.py')
o=load_unique('succ_seeded_zak_seam_oracle_20261031',DIR/'independent_oracle.py')

class SourceAndSeam(unittest.TestCase):
    def test_poles_all_exact(self):
        for n in range(1,120):
            self.assertEqual(m.four_pole(n),o.source_via_combined_rational(n))

    def test_positive_edge(self):
        for n in range(1,120):
            self.assertEqual(m.positive_edge_source(n),m.four_pole(n))
            self.assertGreater(m.four_pole(n),0)

    def test_source_decreases(self):
        for n in range(1,99):
            self.assertGreater(m.four_pole(n),m.four_pole(n+1))

    def test_exact_half_quarter_poles(self):
        for n in range(0,9):
            for offset in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                x=Fraction(n)+offset
                self.assertEqual(m.positive_edge_source(x+1),m.four_pole(x+1))

    def test_zero_seed_forward_oracle(self):
        for n in range(0,20):
            self.assertEqual(m.zero_seed_states(n)[-1],o.source_states_from_explicit_sum(n))

    def test_finite_tail_defect(self):
        for x in (0,Fraction(1,4),Fraction(3,4),1,3):
            for J in (0,1,2,5,13):
                self.assertEqual(m.finite_transport_defect(x,J),
                    -Fraction(1,16**J)*m.four_pole(Fraction(x)+J+1))

    def test_seam_finite_all_points(self):
        for K in (1,3,8,18):
            for n in range(K+1):
                left,right=m.finite_past_future_seam(n,K)
                self.assertEqual(left,right)
                self.assertGreaterEqual(left,0)

    def test_alpha_intervals_nested(self):
        previous=(Fraction(0),Fraction(1))
        for k in range(1,25):
            lo,hi=m.alpha_enclosure(k)
            self.assertLess(lo,hi)
            self.assertGreater(lo,previous[0])
            self.assertLess(hi,previous[1])
            self.assertEqual(lo,o.finite_seed_series(k))
            previous=(lo,hi)

    def test_changed_seed_quarter_motion(self):
        eps=Fraction(1,100)
        self.assertEqual(m.periodic_quarter_defect(0,eps),Fraction(1,50))
        self.assertEqual(m.periodic_quarter_defect(1,eps),Fraction(8,25))
        for j in range(0,7):
            self.assertEqual(m.periodic_quarter_defect(j+1,eps),16*m.periodic_quarter_defect(j,eps))

    def test_same_all_integer_samples(self):
        # exact theorem: sin(2 pi*n)=0 for integer n. Both interpolants
        # therefore share the SAME exact source-labelled U_n (not just phases).
        for n,v in enumerate(m.zero_seed_states(12)):
            for eps in (Fraction(-3,7),Fraction(0),Fraction(1,100)):
                self.assertEqual(v+m.periodic_quarter_grid_defect(n,0,eps),v)
                self.assertEqual(v+m.periodic_quarter_grid_defect(n,4,eps),v)

    def test_quarter_grid_finite_transport(self):
        eps=Fraction(-3,17)
        for n in range(7):
            for quarter in range(5):
                self.assertEqual(m.periodic_quarter_grid_defect(n+1,quarter,eps),
                                 16*m.periodic_quarter_grid_defect(n,quarter,eps))
        self.assertEqual(m.periodic_quarter_grid_defect(0,3,eps),-8*eps)

    def test_zak_shift_exact(self):
        v=(1+0j,1j,-1+0j,-1j,1+0j)
        for f in range(-8,9):
            for s in range(-3,4):
                self.assertEqual(m.zak_integer_corner(v,s,f),
                    ((0+1j)**(s*f))*m.zak_integer_corner(v,0,f))

    def test_zak_frequency_period_exact(self):
        v=(1+0j,-1j,1j,-1+0j)
        for t in range(-2,4):
            for f in range(-6,7):
                self.assertEqual(m.zak_integer_corner(v,t,f+4),
                                 m.zak_integer_corner(v,t,f))

    def test_seam_corner_sum(self):
        v=(1+0j,-1j,-1+0j,1j,1+0j)
        self.assertEqual(m.zak_integer_corner(v,0,0),sum(v))

    def test_finitely_many_coefficients_not_flat(self):
        v=(1+0j,1j,-1+0j,-1j)
        self.assertNotEqual(m.zak_integer_corner(v,0,1),m.zak_integer_corner(v,0,2))

    def test_l2_vs_factorial_oracle(self):
        for p in range(3,12):
            self.assertEqual(m.compact_polynomial_bump_l2(p),o.bump_l2_via_factorials(p))

    def test_window_energy_all_n(self):
        E=m.compact_polynomial_bump_l2()
        self.assertGreater(E,0)
        for N in (0,1,2,8,16,100):
            self.assertEqual(m.global_zak_energy(N),N*E)

    def test_chosen_corner_not_bounded_by_global_energy(self):
        # all-one phases give S_N=N but Zak L2 norm squared ~N.
        # This exhibits the lack of an N-independent point-trace bound.
        E=m.compact_polynomial_bump_l2()
        for N in (4,16,64,256):
            self.assertGreater(Fraction(N*N,m.global_zak_energy(N)),Fraction(N,1))
            self.assertGreater(Fraction(N*N,m.global_zak_energy(N)),Fraction(N*N,2*N))

    def test_wrong_input_rejected(self):
        for fn,args in [(m.four_pole,(Fraction(1,2),)),(m.finite_tail,(0,-1)),
                        (m.alpha_enclosure,(0,)),(m.periodic_quarter_defect,(-1,1)),
                        (m.zak_integer_corner,((),0,0)),
                        (m.compact_polynomial_bump_l2,(2,))]:
            with self.assertRaises(ValueError):fn(*args)

    def test_exact_nontrivial_periodic_value(self):
        # At x=1/4, 16^x=2 and sin(2*pi*x)=1, an exact rational source
        # invisible at all integers nevertheless changes U(x) by 2 epsilon.
        self.assertNotEqual(m.periodic_quarter_defect(0,Fraction(1,99)),0)

    def test_reject_fake_exact_float(self):
        with self.assertRaises(ValueError):m.four_pole(1.0)
        with self.assertRaises(ValueError):m.periodic_quarter_defect(0,0.125)

if __name__=='__main__':unittest.main()

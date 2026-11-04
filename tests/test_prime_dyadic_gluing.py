"""Exact finite witnesses for PGC-09 dyadic prime coverage and Gamma bin transport.

Tests cannot prove the unbounded source-selected local collision hypothesis.
"""
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

_PATH=(Path(__file__).resolve().parents[1]/'research'/'2026-11-02'
       /'prime_cofactor_gamma_golden'/'prime_cofactor_gamma.py')
_SPEC=importlib.util.spec_from_file_location('prime_cofactor_gamma_glue',_PATH)
f=importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(f)


def choose_epoch_prime(A):
    assert A%2==0 and A>=4
    for k in range(A//2,A):
        p=8*k+1
        if f.is_prime(p):
            return p
    return None


class DyadicPrimeGluingTests(unittest.TestCase):
    def test_prime_clean_cover_on_finite_dyadic_epochs(self):
        for A in (16,32,64,128,256,512,1024,2048,4096):
            p=choose_epoch_prime(A)
            self.assertIsNotNone(p)
            b,last,reentry=f.birth_window(p)
            self.assertLessEqual(b,A)
            self.assertGreaterEqual(last,2*A-1)

    def test_selected_original_prime_cofactor_covers_epoch(self):
        for A in (16,32,64):
            p=choose_epoch_prime(A)
            b,last,_=f.birth_window(p)
            u=f.original_states(2*A-1)
            for n in range(A,2*A):
                a,co=f.cofactor_decomposition(p,n-b,u)
                self.assertEqual(a+co,u[n])
                self.assertNotEqual(co.denominator%p,0)

    def test_global_completion_one_bin_gamma_transfer(self):
        for L in (4,8,16,32):
            N=L*L;M=L+1
            A0=1<<(M-1).bit_length()
            q=f.alpha_cutoff(N)
            u=f.original_states(N)
            for n,(a,den) in enumerate(f.modular_orbit(q,N)):
                if n<A0:continue
                x_bin=M*a//den
                y=u[n]
                y_bin=(M*(y.numerator%y.denominator))//y.denominator
                self.assertLessEqual(min((x_bin-y_bin)%M,(y_bin-x_bin)%M),1)
                delta=16**n*q-u[n]
                self.assertGreaterEqual(delta,0)
                self.assertLess(delta,Fraction(1,M))

    def test_global_l2_bound_from_dyadic_source_histograms(self):
        for L in (8,16):
            N=L*L;M=L+1
            A0=1<<(M-1).bit_length()
            q=f.alpha_cutoff(N)
            u=f.original_states(2*N)
            counts=f.exact_mesh_occupancy(q,N,M)
            norm_all=math.sqrt(sum(x*x for x in counts))
            rhs=A0
            A=A0
            while A<N:
                block_counts=[0]*M
                for n in range(A,2*A):
                    z=u[n]
                    block_counts[(M*(z.numerator%z.denominator))//z.denominator]+=1
                rhs+=3*math.sqrt(sum(x*x for x in block_counts))
                A*=2
            self.assertLessEqual(norm_all,rhs+1e-10)

    def test_local_collision_baseline_and_wrong_seed(self):
        A=64;M=17
        u=f.original_states(2*A-1)
        counts=[0]*M
        for n in range(A,2*A):
            z=u[n]
            counts[(M*(z.numerator%z.denominator))//z.denominator]+=1
        self.assertGreaterEqual(sum(x*x for x in counts),A*A/M)
        # Wrong completed source seed 1/5 has every phase fixed; violates any
        # growing-mesh local bound C*(A²/M+A) with C independent of M.
        wrong=[0]*M
        wrong[M//5]=A
        self.assertEqual(sum(x*x for x in wrong),A*A)


if __name__=='__main__':
    unittest.main()

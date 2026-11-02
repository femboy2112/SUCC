"""Finite exact controls for PGC-10 self-resolution collision theorem.

A few cases, never proof of the uniform selected-source collision cap.
"""
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

PATH=(Path(__file__).resolve().parents[1]/'research'/'2026-11-02'/'prime_cofactor_gamma_golden'/'prime_cofactor_gamma.py')
SPEC=importlib.util.spec_from_file_location('prime_self_scale_source', PATH)
f=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(f)


def bins(points, M):
    out=[0]*M
    for z in points:
        out[(M*(z.numerator%z.denominator))//z.denominator]+=1
    return out

class SelfScaleTests(unittest.TestCase):
    def test_exact_original_dyadic_self_scale_counts(self):
        known={8:14,16:34,32:52,64:110,128:220,256:504}
        for A,expected in known.items():
            seq=f.original_states(2*A-1)[A:2*A]
            counts=bins(seq,A)
            self.assertEqual(sum(counts),A)
            self.assertEqual(sum(x*x for x in counts),expected)

    def test_universal_fine_coarse_cauchy_at_boundaries(self):
        cases=[([Fraction(j,24) for j in range(24)],24),
               ([Fraction(1,2)]*32,32),
               ([Fraction(11,37)]*4+[Fraction(j,41) for j in range(12)],16)]
        for points,A in cases:
            assert len(points)==A
            fine=sum(x*x for x in bins(points,A))
            for M in range(2,A+1):
                coarse=sum(x*x for x in bins(points,M))
                self.assertLessEqual(coarse,(math.ceil(A/M)+1)*fine)

    def test_original_all_finite_meshes_follow_single_scale(self):
        for A in (16,32,64):
            seq=f.original_states(2*A-1)[A:2*A]
            fine=sum(x*x for x in bins(seq,A))
            for M in range(2,A+1):
                coarse=sum(x*x for x in bins(seq,M))
                self.assertLessEqual(coarse,(math.ceil(A/M)+1)*fine)

    def test_coherent_wrong_completed_seed_fails_self_scale_cap(self):
        for A in (16,32,64):
            completed=[Fraction(1,5)]*A  # 16^n/5 == 1/5 mod 1
            fine=bins(completed,A)
            self.assertEqual(sum(x*x for x in fine),A*A)
            self.assertEqual(Fraction(sum(x*x for x in fine),A),A)

if __name__=='__main__':unittest.main()

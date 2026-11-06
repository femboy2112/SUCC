"""Exact odd-torsion sphere branch, unstable inverse, and source shell checks."""
import importlib.util
from pathlib import Path
from fractions import Fraction as Q
import unittest
P=Path(__file__).resolve().parents[1]/'research/2026-11-05/history_shell/history_shell_probe.py'
spec=importlib.util.spec_from_file_location('history_shell_probe',P)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

def odd_root(y):
    candidates=[(Q(y)+j)/16 for j in range(16)]
    admissible=[x%1 for x in candidates if (x%1).denominator%2==1]
    assert len(admissible)==1
    return admissible[0]

def exact_cell_prob(start,m):
    B=16**m; start=start%1;end=start+Q(1,B)
    out={}
    for j in range(B):
        t=Q(0)
        for integer_part in (0,1):
            l=max(start,integer_part+Q(j,B))
            u=min(end,integer_part+Q(j+1,B))
            if u>l:t+=(u-l)*B
        if t:out[j]=t
    assert sum(out.values())==1
    return out

class SphereHistoryTransfer(unittest.TestCase):
    def test_01_authenticated_original_phases_have_odd_denominators(self):
        us=h.states(128)
        for u in us:
            self.assertEqual((u%1).denominator%2,1)

    def test_02_one_of_sixteen_inverse_sphere_roots_is_arithmetic(self):
        us=h.states(120)
        for n in range(120):
            y=(us[n+1]-h.forcing(n+1))%1
            self.assertEqual(odd_root(y),us[n]%1)
            self.assertEqual(len([1 for j in range(16)
                if (((y+j)/16)%1).denominator%2==1]),1)

    def test_03_unique_odd_root_inverse_is_not_circle_continuous(self):
        for t in (1,10,100,1000):
            qp,qm=16*t+1,16*t-1
            xp=odd_root(Q(1,qp));xm=odd_root(Q(1,qm))
            self.assertEqual(xp,Q(15,16)+Q(1,16*qp))
            self.assertEqual(xm,Q(1,16)+Q(1,16*qm))
            self.assertEqual((16*xp)%1,Q(1,qp))
            self.assertEqual((16*xm)%1,Q(1,qm))
        self.assertEqual(odd_root(Q(0)),0)

    def test_04_original_source_exact_two_step_not_lumpable(self):
        for n,m in ((13,2),(29,2),(61,2)):
            r1=h.forcing(n+1);r2=h.forcing(n+2)
            d1,d2,pair=h.source_nonlumpability(n,m)
            B=16**m
            qbase=int(16**(m+1)*r1)+int(16**m*r2)
            predicted={}
            for offset,prob in enumerate(pair['naive']):
                predicted[(qbase+offset)%B]=prob
            direct=exact_cell_prob(16*r1+r2,m)
            totalvariation=sum(abs(direct.get(i,0)-predicted.get(i,0)) for i in range(B))/2
            self.assertEqual(totalvariation,pair['total_variation'])
            self.assertGreater(totalvariation,0)

    def test_05_toy_base16_direct_interval_is_one_cell(self):
        direct=exact_cell_prob(16*Q(1,512)+Q(1,32),1)
        self.assertEqual(direct,{1:Q(1)})
        self.assertEqual(h.nonlumpability(Q(1,2),Q(1,2))['total_variation'],Q(1,2))

    def test_06_odd_arithmetic_branch_does_not_authenticate_source_coefficients(self):
        x=Q(0)
        for n in range(1,35):
            r_mut=h.forcing(n)+Q(1,8*n-7)
            x=16*x+r_mut
            self.assertEqual((x%1).denominator%2,1)
        self.assertNotEqual(h.forcing(1),h.forcing(1)+Q(1))

if __name__=='__main__':unittest.main()

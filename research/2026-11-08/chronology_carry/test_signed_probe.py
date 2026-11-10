from fractions import Fraction as Q
import itertools
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import signed_probe as sp


class SignedProbeTests(unittest.TestCase):
    def test_padded_windows_against_independent_exact_pairs(self):
        for N in (1,2,7,19):
            values=[(Q((i*7)%11-5,7),Q((i*i)%13-6,11)) for i in range(N)]
            boxes=[sp.cbox(v) for v in values]
            for H in sorted({1,N,max(1,N//2)}):
                receipt=sp.window_receipts(boxes,(H,))['rows'][0]
                pair=Q(0)
                for i in range(N):
                    for j in range(N):
                        weight=max(0,H-abs(i-j))
                        pair+=weight*(values[i][0]*values[j][0]+values[i][1]*values[j][1])
                exact=Q(N+H-1,N*N*H*H)*pair
                lo,hi=receipt['V_interval']
                self.assertLessEqual(Q(lo,sp.cm.SCALE),exact)
                self.assertGreaterEqual(Q(hi,sp.cm.SCALE),exact)
                avg=sp.cscale(sp.csum(values),Q(1,N))
                self.assertLessEqual(sum(x*x for x in avg),exact)

    def test_poisson_identity_with_exceptional_carries(self):
        table={'tables':{'1':{}}}
        for menu,k in (('one',1),('two',2)):
            row={}
            for word in itertools.product(range(16),repeat=k):
                row[sp.cm.key_text(word)]={'center':[sum(word)*100,word[-1]*-300]}
            row[sp.cm.key_text((16,)*k)]={'center':[70000,20000]}
            table['tables']['1'][menu]=row
            digits=[1,4,7,16,16,2,0,9]
            states=[(d,) for d in digits] if k==1 else list(zip(digits,digits[1:]))
            result=sp.poisson_audit(table,1,menu,states)
            self.assertTrue(result['poisson_identity_exact'])
            self.assertTrue(result['finite_sum_identity_exact'])
            self.assertGreater(result['exceptional_interior_states'],0)

    def test_coherent_and_cancelling_residual_controls(self):
        N=64
        coherent=[sp.cbox((Q(1),Q(0))) for _ in range(N)]
        alternating=[sp.cbox((Q((-1)**n),Q(0))) for n in range(N)]
        for H in (2,8,32):
            c=sp.window_receipts(coherent,(H,))['rows'][0]
            a=sp.window_receipts(alternating,(H,))['rows'][0]
            self.assertGreaterEqual(Q(c['V_interval'][1],sp.cm.SCALE),1)
            self.assertLess(Q(a['V_interval'][1],sp.cm.SCALE),Q(1,4))
            self.assertEqual(sp.window_receipts(alternating,(H,))['diagonal'],
                             [sp.cm.SCALE,sp.cm.SCALE])
            self.assertLess(a['signed_cross_term_interval'][1],0)

    def test_finite_range_constants_and_even_power_geometry(self):
        # Exact rational circle samples verify the power-factorization bound
        # used by FR1, independently of a trigonometric evaluator.
        def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
        def power(a,n):
            out=(Q(1),Q(0))
            for _ in range(n):out=mul(out,a)
            return out
        for t in range(-12,13):
            x=Q(t,7)
            z=(Q(1),Q(0));w=((x*x-1)/(1+x*x),2*x/(1+x*x))
            difference=sp.csub(power(w,16),power(z,16))
            chord=sp.cadd(w,z)
            self.assertLessEqual(sum(v*v for v in difference),256*sum(v*v for v in chord))
        for M in range(1,30):
            delta=Q(1,2048*M*M);a=Q(1,32)
            self.assertEqual(4*M*M*delta/a,Q(1,16))
            self.assertEqual(delta/4,Q(1,8192*M*M))


if __name__=='__main__':unittest.main()

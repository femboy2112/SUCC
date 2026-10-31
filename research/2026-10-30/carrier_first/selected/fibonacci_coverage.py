"""Exact unit-sequence counterexample to Fibonacci-prefix-only coverage."""
import json
from fractions import Fraction as Q


def main():
    fs=[0,1]
    for _ in range(23):fs.append(fs[-1]+fs[-2])
    one,minus,omega,omega2=(1,0),(-1,0),(0,1),(-1,-1)
    seq=[one,minus,one,omega,omega2]
    rows=[]
    for k in range(5,23):
        L=fs[k-1];run=L//2 if L%2==0 else (L-3)//2
        block=[one]*run+[minus]*run
        if L%2:block+=[one,omega,omega2]
        assert len(block)==L and tuple(map(sum,zip(*block)))==(0,0)
        seq+=block
        assert len(seq)==fs[k+1]
        assert tuple(map(sum,zip(*seq)))==(0,0)
        N=fs[k]+run
        partial=tuple(map(sum,zip(*seq[:N])))
        assert partial==(run,0)
        rows.append({'k':k,'F_k':fs[k],'gap':L,'midpoint_N':N,
                     'Fibonacci_prefix_sum':[0,0],'midpoint_average':str(Q(run,N))})
    print(json.dumps({'status':'PASS','basis':'1,omega with omega²=−1−omega',
                      'all_terms_unit_complex':True,'rows':rows,
                      'scope':'generic unit-sequence coverage countermodel, not a radix16 orbit'},indent=2))


if __name__=='__main__':main()

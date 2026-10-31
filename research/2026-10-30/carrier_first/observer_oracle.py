"""Separate integer Machin digit enclosure and direct count/lasso oracle.

Does not import observer.py. No independent human-referee claim.
"""
import json
from fractions import Fraction as Q
from pathlib import Path


def atan_bounds(q,S):
    power=q;k=0;lo=hi=0
    while True:
        den=(2*k+1)*power;t=S//den
        if t==0:return lo-1,hi+1,k
        if k%2:lo-=t+1;hi-=t
        else:lo+=t;hi+=t+1
        k+=1;power*=q*q


def main():
    data=json.loads((Path(__file__).parent/'receipts/observer-data.json').read_text())
    text=data['word_hex'];L=len(text);S=16**(L+8)
    a,b,k=atan_bounds(5,S);c,d,j=atan_bounds(239,S)
    atan_terms=[k,j]
    lo=(16*a-4*d)*16**L//S;hi=(16*b-4*c)*16**L//S
    assert lo==hi
    assert Q(16*b-4*c,S)<Q(22,7)
    oracle=format(lo%16**L,f'0{L}X');assert oracle==text
    digits=[int(x,16) for x in text]
    finite_weyl=[]
    for row in data['selected']:
        N=row['N'];k=row['k'];hist={}
        for n in range(N):
            key=(digits[n],int(text[n+1:n+1+k],16) if k else 0)
            hist[key]=hist.get(key,0)+1
        assert sorted([*key,value] for key,value in hist.items())==row['counts']
        # Conditional W1 through exact monotone mass matching, not cumulative formula.
        cost=Q(0)
        for v in {key[1] for key in hist}:
            total=sum(hist.get((d,v),0) for d in range(16))
            left=[Q(hist.get((d,v),0),N) for d in range(16)]
            right=[Q(total,16*N)]*16;i=j=0
            while i<16 and j<16:
                moved=min(left[i],right[j]);cost+=moved*Q(abs(i-j),16)
                left[i]-=moved;right[j]-=moved
                if left[i]==0:i+=1
                if right[j]==0:j+=1
        assert str(cost)==row['rho']
        best=N;wit=None
        # Independent increasing-state search; choose all possible cycle starts.
        for states in range(1,N+1):
            for a in range(states):
                p=states-a
                if all(digits[n]==digits[a+(n-a)%p] for n in range(states,N)):
                    best=states;wit=(a,p);break
            if wit is not None:break
        assert best==row['minimal_states']
        if k==1:
            bound=Q(44,7)*(Q(row['w1_upper'])+Q(1,32*N))
            assert bound<1
            finite_weyl.append({'N':N,'h':1,'normalized_modulus_upper':str(bound)})
    print(json.dumps({'status':'PASS','independent_Machin_digits':L,
          'integer_rounding_scale_bits':4*(L+8),'atan_terms':atan_terms,
          'selected_count_transport_lasso_cases':len(data['selected']),
          'finite_Weyl_bounds_via_O3':finite_weyl,
          'source':'Machin arctangent identity, integer outward term bounds; independent count coupling'},indent=2))


if __name__=='__main__':main()

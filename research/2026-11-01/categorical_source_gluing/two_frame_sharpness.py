"""Exact two-frame noninjectivity certificate for the authentic BBP source cover.

Pure Python standard library: confirms a REAL distinct-point H2 collision, then
certifies that a third observation separates the pair. No decimal approximations,
random fitting, infinite-digit inference, or new source labels enter the proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import permutations
from math import comb


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def scale(a,c):return trim([c*x for x in a])

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def power(a,n):
    out=(1,)
    for _ in range(n):out=mul(out,a)
    return out

def shift(a,k):
    out=(0,)
    for i,c in enumerate(a):
        out=add(out,scale(tuple(comb(i,j)*k**(i-j) for j in range(i+1)),c))
    return out

def evaluate(a,x):
    v=0
    for c in a[::-1]:v=v*x+c
    return v

def interval_eval(a,lo,hi):
    val=(F(0),F(0))
    for c in a[::-1]:
        aa=[val[0]*lo,val[0]*hi,val[1]*lo,val[1]*hi]
        val=(min(aa)+c,max(aa)+c)
    return val

def p_divmod(a,b):
    """Exact polynomial division over rationals, ascending powers."""
    a=list(map(F,trim(a)));b=list(map(F,trim(b)))
    if b==[0]:raise ZeroDivisionError
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        d=len(a)-len(b);factor=a[-1]/b[-1];q[d]+=factor
        for i,coef in enumerate(b):a[d+i]-=factor*coef
        a=list(trim(a))
    return trim(q),trim(a)

def modp_gcd(a,b,p):
    a=[int(x)%p for x in trim(a)];b=[int(x)%p for x in trim(b)]
    def t(v):
        v=[x%p for x in v]
        while len(v)>1 and v[-1]==0:v.pop()
        return v
    while any(b):
        a=t(a);b=t(b)
        while len(a)>=len(b) and any(a):
            factor=a[-1]*pow(b[-1],-1,p)%p;d=len(a)-len(b)
            for i,c in enumerate(b):a[d+i]=(a[d+i]-factor*c)%p
            a=t(a)
        a,b=b,a
    return tuple(t(a))

# f(s,p)=0 is the exact off-diagonal equation for R(x)=R(y):
# s=x+y, p=xy, after dividing the cross-product by (x-y).
# Coefficient polynomials ascending in s, indexed by p degree 0..3.
F0=((10976,-60319,114100,-73760),
    (75628,-308544,318464),
    (215552,-475136),
    (245760,))

def shift_f(f,amount):
    """Replace (s,p) by (s+2j, p+j*s+j*j) for j=amount."""
    j=amount;out=[]
    for degree in range(4):
        v=(0,)
        for higher in range(degree,4):
            term=mul(shift(f[higher],2*j),power((j*j,j),higher-degree))
            v=add(v,scale(term,comb(higher,degree)))
        out.append(v)
    return tuple(out)
F1=shift_f(F0,1)
F2=shift_f(F0,2)
Q=(-8758669850307,203276412515538,-2147182431023808,
   13583685706776288,-56851206836033792,163752693520971264,
   -326110189092528128,435631352005140480,-356902560308264960,
   138011809795276800)
A=(189988416,-2390662784,11554414080,-25663197184,22293381120)
B=(47673279,-606244406,3067138968,-7641171904,8935808256,-3230484480)
RES_SCALE=2111062325329920
LEFT=F(301451,1_000_000)
RIGHT=F(301452,1_000_000)

def sylvester(f,g):
    rows=[]
    for h in (f,g):
        desc=list(reversed(h))
        for offset in range(3):
            rows.append(((0,),)*offset+tuple(desc)+((0,),)*(2-offset))
    return tuple(rows)

def polynomial_resultant(f,g):
    rows=sylvester(f,g)
    assert len(rows)==6 and all(len(row)==6 for row in rows)
    accum=(0,)
    for indices in permutations(range(6)):
        parity=sum(indices[i]>indices[j] for i in range(6) for j in range(i+1,6))%2
        term=(1,)
        for i,j in enumerate(indices):
            term=mul(term,rows[i][j])
        accum=add(accum,scale(term,-1 if parity else 1))
    return trim(accum)

def substituted_numerator(f):
    """The polynomial A(s)^3 f(s,-B(s)/A(s))."""
    out=(0,)
    for i,coef in enumerate(f):
        out=add(out,mul(coef,mul(power(scale(B,-1),i),power(A,3-i))))
    return out

def verify():
    # Prove the claimed Q is *the* eliminant, independently of SymPy.
    resultant=polynomial_resultant(F0,F1)
    if resultant not in (scale(Q,RES_SCALE),scale(Q,-RES_SCALE)):
        raise ArithmeticError('resultant mismatch')
    # Prove Q=0, A!=0 => p=-B/A solves BOTH collision polynomials.
    for f in (F0,F1):
        q,r=p_divmod(substituted_numerator(f),Q)
        if r!=(F(0),):raise ArithmeticError('candidate p does not satisfy collision equation')
    if not(evaluate(Q,LEFT)<0<evaluate(Q,RIGHT)):
        raise ArithmeticError('no certified real zero inside the interval')
    # Coarse but exact bounds, valid for EVERY root in the interval:
    # A>0, B>0, and -1/4 < -B/A < -1/8.
    positivity=(A,B,add(scale(B,8),scale(A,-1)),add(A,scale(B,-4)))
    for poly in positivity:
        if interval_eval(poly,LEFT,RIGHT)[0]<=0:
            raise ArithmeticError('interval positivity failed')
    # Third observation cannot coincide: nonzero modular gcd certifies no
    # common complex root of Q and A^3*f2(s,-B/A).
    v2=substituted_numerator(F2)
    if (len(Q)!=10 or len(v2)!=16 or Q[-1]%101==0 or v2[-1]%101==0
        or len(modp_gcd(Q,v2,101))!=1):
        raise ArithmeticError('third-frame polynomial coprimality failed')
    # Real s,p imply x,y distinct real, with xy=p<0. The -1/4<p<-1/8
    # and s interval imply x in (1/2,7/8), y in (-1/2,-1/7),
    # hence y+1 in (1/2,6/7); neither source coordinate nor its
    # translated value lands on a pole {1/2,3/8,1/4}.
    return {
        'status':'EXACT_REAL_TWO_FRAME_COLLISION_AND_THIRD_FRAME_SEPARATION',
        'resultant_degree':len(Q)-1,
        'resultant_scale':RES_SCALE,
        'root_interval':[str(LEFT),str(RIGHT)],
        'resultant_signs':[int(evaluate(Q,LEFT)<0),int(evaluate(Q,RIGHT)>0)],
        'p_strict_bounds':['-1/4','-1/8'],
        'distinct_real_lifts':True,
        'third_frame_distinguishes_all_resultant_roots':True,
        'independent_oracle':'stdlib Sylvester determinant + exact polynomial divisibility + interval Horner + mod-101 gcd',
    }

if __name__=='__main__':
    import json
    print(json.dumps(verify(),indent=2))

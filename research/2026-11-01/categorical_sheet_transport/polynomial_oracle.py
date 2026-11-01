"""Independent stdlib integer-polynomial certificate checker.

Does not call SymPy, a resultant routine, sheet_transport.R/reconstruct, or
floating arithmetic. Coefficients are in ascending order. Its role is to
check the universal identities, not infer universality from sampled values.
"""
from math import comb, gcd
from functools import reduce

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return tuple(p or [0])

def add(p,q):
    a=[0]*max(len(p),len(q))
    for i,x in enumerate(p): a[i]+=x
    for i,x in enumerate(q): a[i]+=x
    return trim(a)

def scale(p,c): return trim(tuple(c*x for x in p))

def mul(p,q):
    a=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): a[i+j]+=x*y
    return trim(a)

def power(p,n):
    out=(1,)
    for _ in range(n): out=mul(out,p)
    return out

def derivative(p): return trim(tuple(i*p[i] for i in range(1,len(p))))

def shift(p,h):
    out=[0]*len(p)
    for j,x in enumerate(p):
        for i in range(j+1): out[i]+=x*comb(j,i)*h**(j-i)
    return trim(out)

def primitive(p):
    g=reduce(gcd,(abs(x) for x in p)) or 1
    return tuple(x//g for x in p)

A=power((-7,8),4)
D=mul(mul(power((-4,8),2),(-3,8)),(-2,8))
A1=shift(A,1);D1=shift(D,1)

def homogeneous_substitution(terms,degree):
    """D(z)^d D(z+1)^d p(A/D,A1/D1), exactly in Z[z]."""
    out=(0,)
    for i,j,c in terms:
        term=mul(mul(power(A,i),power(D,degree-i)),
                 mul(power(A1,j),power(D1,degree-j)))
        out=add(out,scale(term,c))
    return out

def certificate(a_terms,b_terms,curve_terms):
    pa=homogeneous_substitution(a_terms,3)
    pb=homogeneous_substitution(b_terms,3)
    inverse_residual=add(scale(mul((0,1),pa),8),pb)
    curve_residual=homogeneous_substitution(curve_terms,4)
    shifted=shift(primitive(pa),1)
    # Independent original rational source = (1/8)dlog(A/D).
    N=(16,-89,120)
    denominator=mul(mul((-1,2),(-1,4)),mul((-7,8),(-3,8)))
    dlog_residual=add(mul(add(mul(derivative(A),D),scale(mul(A,derivative(D)),-1)),denominator),
                       scale(mul(mul(A,D),N),-8))
    return {'inverse_residual':inverse_residual,
            'curve_residual':curve_residual,
            'dlog_residual':dlog_residual,
            'denominator_degree':len(pa)-1,
            'shifted_positive':all(c>0 for c in shifted),
            'shifted_coefficients':shifted,
            'minimum_shifted_coefficient':min(shifted)}

# Independent multivariate Z-polynomial certificate arithmetic.
def badd(a,b):
    out=dict(a)
    for ij,c in b.items():out[ij]=out.get(ij,0)+c
    return {ij:c for ij,c in out.items() if c}

def bscale(a,c):return {ij:c*v for ij,v in a.items() if c*v}

def bmul(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),0)+x*y
    return {ij:c for ij,c in out.items() if c}

def bpower(a,n):
    out={(0,0):1}
    for _ in range(n):out=bmul(out,a)
    return out

def bsubstitute(terms,a,b):
    out={}
    for i,j,c in terms:out=badd(out,bscale(bmul(bpower(a,i),bpower(b,j)),c))
    return out

def global_certificate(data):
    X={(1,0):1};Y={(0,1):1};one={(0,0):1}
    # s=x+y, p=xy, and common temporal shifts k.
    f=data['collision_f'];fs=[]
    for k in range(3):
        fs.append(bsubstitute(f,badd(X,bscale(one,2*k)),
                    badd(Y,badd(bscale(X,k),bscale(one,k*k)))))
    residual={}
    for multiplier,polynomial in zip(data['multipliers'],fs):
        h={(i,j):c for i,j,c in multiplier}
        residual=badd(residual,bmul(h,polynomial))
    # Check that f really is the collision polynomial, not an unrelated certificate.
    actual=badd(bmul({(i,0):c for i,c in enumerate(A)},
                    {(0,j):c for j,c in enumerate(D)}),
                bscale(bmul({(0,j):c for j,c in enumerate(A)},
                    {(i,0):c for i,c in enumerate(D)}),-1))
    divided=bmul(badd(X,bscale(Y,-1)),bsubstitute(f,badd(X,Y),bmul(X,Y)))
    key=next(iter(divided));factor=actual[key]//divided[key]
    collision_ok=actual==bscale(divided,factor) and factor!=0
    q0=add(A,scale(D,-1));q1=shift(q0,1)
    inf=add(mul(tuple(data['infinity_multipliers'][0]),q0),
            mul(tuple(data['infinity_multipliers'][1]),q1))
    c0=mul(mul((-7,8),(-1,2)),(16,-89,120));c1=shift(c0,1)
    imm=add(mul(tuple(data['immersion_multipliers'][0]),c0),
            mul(tuple(data['immersion_multipliers'][1]),c1))
    return {'collision_identity':collision_ok,
            'raw_collision_factor':factor,
            'finite_points_separated':residual=={(0,0):data['constant']} and data['constant']!=0,
            'infinity_separated':inf==(data['infinity_constant'],) and data['infinity_constant']!=0,
            'immersion':imm==(data['immersion_constant'],) and data['immersion_constant']!=0}

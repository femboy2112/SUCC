"""Independent Lagrange interpolation and recurrence oracle for the finite sphere seam."""
from fractions import Fraction as F


def add(a,b):
    ret=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):ret[i]+=x
    for i,x in enumerate(b):ret[i]+=x
    return ret


def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def lagrange_weights(n):
    result=[F(0)]
    for j in range(1,n+1):
        polynomial=[F(1)]; denom=F(1)
        for k in range(1,n+1):
            if k!=j:
                polynomial=mul(polynomial,[-F(k),F(1)])
                denom*=j-k
        result=add(result,[x*F(1,16**j)/denom for x in polynomial])
    return tuple(result)


def recurrence(n):
    x=F(0);a=F(0)
    for j in range(1,n+1):
        src=F(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))
        x=16*x+src
        a+=src/F(16**j)
    return x,a

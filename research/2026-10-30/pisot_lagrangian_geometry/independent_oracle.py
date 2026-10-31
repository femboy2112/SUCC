"""Independent six-variable normal-equation oracle for one Pisot plaquette.
Does NOT use the paper's W inverse while constructing the minimizer.
"""
from fractions import Fraction as Q

A=((1,1),(1,0)); B=((2,1),(3,2))

def multiply(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(2)) for i in range(2))

def solve(C,d):
    n=len(d); x=[[Q(C[i][j]) for j in range(n)]+[Q(d[i])] for i in range(n)]
    for k in range(n):
        t=next(i for i in range(k,n) if x[i][k]!=0)
        x[k],x[t]=x[t],x[k]
        a=x[k][k]; x[k]=[c/a for c in x[k]]
        for i in range(n):
            if i==k: continue
            a=x[i][k]
            x[i]=[x[i][j]-a*x[k][j] for j in range(n+1)]
    return tuple(x[i][n] for i in range(n))

def direct(anchor,rate):
    F=(rate,Q(0)); M=[[Q(0)]*6 for _ in range(8)]; b=[Q(0)]*8
    for i in range(2):
        M[i][i]=1; b[i]=multiply(B,anchor)[i]
        M[2+i][2+i]=1; b[2+i]=multiply(A,anchor)[i]+F[i]
        M[4+i][4+i]=1; b[4+i]=F[i]
        M[6+i][4+i]=1
        for j in range(2):
            M[4+i][j]-=A[i][j]
            M[6+i][2+j]-=B[i][j]
    C=[[sum(M[k][i]*M[k][j] for k in range(8)) for j in range(6)] for i in range(6)]
    d=[sum(M[k][i]*b[k] for k in range(8)) for i in range(6)]
    v=solve(C,d)
    residual=[sum(M[k][i]*v[i] for i in range(6))-b[k] for k in range(8)]
    return sum(t*t for t in residual)/2

def predicted(anchor,rate):
    # Formula is deliberately recomputed directly from the two path maps.
    ab=multiply(A,multiply(B,anchor))
    ba=multiply(B,multiply(A,anchor))
    bf=multiply(B,(rate,Q(0)))
    d0=ab[0]-ba[0]+rate-bf[0]
    d1=ab[1]-ba[1]-bf[1]
    return (16*d0*d0-18*d0*d1+9*d1*d1)/126

if __name__=='__main__':
    cases=[((0,0),Q(0)),((1,0),Q(0)),((0,0),Q(47,15)),
           ((1,0),Q(47,15)),((2,-1),Q(13,17)),((-3,4),Q(0))]
    for v,r in cases:
        lhs=direct(tuple(map(Q,v)),r)
        rhs=predicted(tuple(map(Q,v)),r)
        assert lhs==rhs, (v,r,lhs,rhs)
        print('PASS',v,r,lhs)
    print('Six exact independent normal-equation controls PASS')

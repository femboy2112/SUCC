"""Separate Mellin-residue, Beta-product and SymPy-field checks.

Does not import fibonacci_arrows. Same model family, not an external referee.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from math import factorial,comb
import sympy as s


ROOT=Path(__file__).parent


def fib(n):
    if not n:
        return 0
    return int((s.Matrix([[1,1],[1,0]])**n)[0,1])


def residues(L,last):
    q=L+6
    alphas=[L+2]+[L+fib(n)+2 for n in range(2,last+1)]
    C=F(1)
    for a in alphas:
        C*=F(q-a,q+a+1)
    out={q:F(1)}
    # H(z)=C product(z-a)/((z+q+1) product(z+a+1)).
    for a in alphas:
        z=-a-1
        value=C/F(z+q+1)
        for b in alphas:
            value*=z-b
            if b!=a:
                value/=z+b+1
        out[a]=value
    return out,C*C/F(2*q+1)


def R(a):
    return sum((F(c)/F(a+d) for c,d in ((4,0),(-2,3),(-1,4),(-1,5))),F())


def beta_product(u,k):
    out=F(factorial(k))
    for i in range(k+1):
        out/=u+i
    return out


def sensor_moment(a,k,t):
    return sum((c*beta_product(F(a+d,8)+t,k)
                for c,d in ((4,0),(-2,3),(-1,4),(-1,5))),F())/(8*R(a))


def field_interpolation(rows,cols):
    K=s.QQ.algebraic_field(s.sqrt(5))
    la=K.from_sympy((s.sqrt(5)-1)/2)
    qs=[la**fib(i+2) for i in range(rows)]
    rs=[la**fib(i+2) for i in range(cols)]
    J=[[K.convert(F(1+3*i+2*j)) for j in range(cols)] for i in range(rows)]
    total=sum((v for row in J for v in row),K.zero)
    J=[[v/total for v in row] for row in J]
    M=[[sum((J[i][j]*q**i*r**j for i in range(rows) for j in range(cols)),K.zero)
        for r in rs] for q in qs]

    def lagrange(nodes):
        basis=[]
        for i,u in enumerate(nodes):
            coeff=[K.one]
            divisor=K.one
            for j,v in enumerate(nodes):
                if j==i:
                    continue
                nxt=[K.zero]*(len(coeff)+1)
                for k,c in enumerate(coeff):
                    nxt[k]-=v*c
                    nxt[k+1]+=c
                coeff=nxt
                divisor*=u-v
            basis.append([c/divisor for c in coeff])
        return basis

    A,B=lagrange(qs),lagrange(rs)
    recovered=[[sum((M[u][v]*A[u][i]*B[v][j]
                     for u in range(rows) for v in range(cols)),K.zero)
                for j in range(cols)] for i in range(rows)]
    assert recovered==J
    return rows*cols


def main():
    original=json.loads((ROOT/"receipts/probe.json").read_text())
    count=0
    for row in original["finite_residuals"]:
        h,norm=residues(row["L"],row["last_index"])
        assert h=={int(k):F(v) for k,v in row["h"].items()}
        assert norm==F(row["norm_squared"])
        count+=1
    fresh=[]
    for L,last in ((1,7),(5,10),(17,11)):
        h,norm=residues(L,last)
        for k in [L+2]+[L+fib(n)+2 for n in range(2,last+1)]:
            assert sum((c/F(j+k+1) for j,c in h.items()),F())==0
        direct=sum((x*y/F(i+j+1) for i,x in h.items() for j,y in h.items()),F())
        assert direct==norm>0
        fresh.append({"L":L,"last":last,"norm_squared":str(norm)})
    beta_count=0
    for a in (31,113,241):
        for m,d in ((3,4),(6,5),(7,5)):
            J={(i,k):comb(m,i)*comb(d,k-i)*sensor_moment(a,k,m+d-k)
               for i in range(m+1) for k in range(i,i+d+1)}
            assert sum(J.values())==1 and min(J.values())>0
            beta_count+=len(J)
    cycle_count=0
    for row in original["cycle_witnesses"]:
        Z={tuple(map(int,k.split(','))):F(v) for k,v in row['nonzero_edges'].items()}
        H=lambda j:sum((F(1,l) for l in range(1,j+1)),F())
        funcs=[H]+[lambda j,n=n:F(fib(j+n)) for n in (0,1,3,12,23)]
        for f in funcs:
            for g in funcs:
                assert sum((v*f(i)*g(j) for (i,j),v in Z.items()),F())==0
                cycle_count+=1
    interpolation=sum(field_interpolation(r,c) for r,c in ((2,3),(3,3),(4,2)))
    report={"Mellin_residue_reconstructions":count,"fresh_residuals":fresh,
            "native_Beta_joint_entries":beta_count,"translated_Fibonacci_cycle_checks":cycle_count,
            "Lagrange_reconstructed_joint_entries":interpolation,
            "authority":"separate algorithms and fresh data; same-model reasoning"}
    with (ROOT/'receipts/oracle.json').open('x') as f:
        json.dump(report,f,indent=2)
    print(json.dumps(report))


if __name__=='__main__':
    main()

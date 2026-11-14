"""Independent symbolic geometry audit; no claim to simulate physical observers."""
import sympy as s

def ricci_scalar(g, coords):
    n=len(coords)
    gi=g.inv()
    ch=[[[s.simplify(sum(gi[a,d]*(s.diff(g[d,b],coords[c])+s.diff(g[d,c],coords[b])-s.diff(g[b,c],coords[d]))/2 for d in range(n))) for c in range(n)] for b in range(n)] for a in range(n)]
    ric=s.zeros(n)
    for mu in range(n):
        for nu in range(n):
            ric[mu,nu]=s.simplify(sum(s.diff(ch[r][mu][nu],coords[r])-s.diff(ch[r][mu][r],coords[nu])+sum(ch[r][r][k]*ch[k][mu][nu]-ch[r][nu][k]*ch[k][mu][r] for k in range(n)) for r in range(n)))
    scalar=s.simplify(sum(gi[i,j]*ric[i,j] for i in range(n) for j in range(n)))
    E=s.simplify(ric - scalar*g/2)
    return scalar,E

t,x=s.symbols('t x',real=True)
a=s.Function('a')(t)
R2,G2=ricci_scalar(s.diag(-1,a*a),(t,x))
assert s.simplify(R2-2*s.diff(a,t,2)/a)==0,R2
assert G2==s.zeros(2),G2
print('2D FRW: R=',R2,'G=zero')
eta,X,Y,Z,H=s.symbols('eta X Y Z H',real=True,nonzero=True)
scale=-1/(H*eta)
g=scale*scale*s.diag(-1,1,1,1)
R4,G4=ricci_scalar(g,(eta,X,Y,Z))
assert s.simplify(R4-12*H**2)==0,R4
assert s.simplify(G4+3*H**2*g)==s.zeros(4),G4
print('4D conformal dS: R=',R4,'G=-3H² g')

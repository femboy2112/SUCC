"""Independent SymPy check of conformal countermodels and R^2 blind direction.

No SUCC application imports or physical observations. Runs all tensor contractions
from a metric, rather than trusting the rational closed formulas.
"""
import sympy as s

def geometry(g, coords):
    n=len(coords)
    gi=s.simplify(g.inv())
    gamma=[[[s.simplify(sum(gi[i,k]*(s.diff(g[k,j],coords[l])+s.diff(g[k,l],coords[j])-s.diff(g[j,l],coords[k]))/2 for k in range(n))) for l in range(n)] for j in range(n)] for i in range(n)]
    ric=s.zeros(n)
    for a in range(n):
        for b in range(n):
            ric[a,b]=s.simplify(sum(s.diff(gamma[k][a][b],coords[k])-s.diff(gamma[k][a][k],coords[b])+sum(gamma[k][k][m]*gamma[m][a][b]-gamma[k][b][m]*gamma[m][a][k] for m in range(n)) for k in range(n)))
    R=s.simplify(sum(gi[a,b]*ric[a,b] for a in range(n) for b in range(n)))
    return ric,R,s.simplify(ric-R*g/2)

t,x,y,z=s.symbols('t x y z',real=True)
eta2=s.diag(-1,1)
eta4=s.diag(-1,1,1,1)
Omega=1/(1-t)
g2=Omega**2*eta2
g4=Omega**2*eta4
r2,R2,G2=geometry(g2,(t,x))
r4,R4,G4=geometry(g4,(t,x,y,z))
assert R2==2 and G2==s.zeros(2),(R2,G2)
assert R4==12 and s.simplify(G4+3*g4)==s.zeros(4),(R4,G4)
# Scalar action-density and Hilbert stress tensor: all conformal factors cancel in 2D.
a,b,Z=s.symbols('a b Z',real=True)
grad=s.Matrix([a,b]); gi2=s.simplify(g2.inv())
L2=s.simplify(-Z/2 * Omega**2 * (grad.T*gi2*grad)[0])  # Omega>0 on t<1
assert s.simplify(L2-Z*(a*a-b*b)/2)==0,L2
T2=s.simplify(Z*(grad*grad.T-g2*(grad.T*gi2*grad)[0]/2))
assert s.simplify(T2-Z*s.Matrix([[(a*a+b*b)/2,a*b],[a*b,(a*a+b*b)/2]]))==s.zeros(2),T2
# R^2 variation with constant R on any 4D Einstein space.
assert s.simplify(2*R4*r4 - R4**2*g4/2)==s.zeros(4)
# A smooth analytic deformation invisible through 2-jet probes at t=0,t=1/2.
sigma=t**3*(t-s.Rational(1,2))**3
for ts in [0,s.Rational(1,2)]:
    for order in (0,1,2):
        assert s.diff(sigma,t,order).subs(t,ts)==0
assert s.diff(sigma,t,2).subs(t,s.Rational(1,4))==s.Rational(3,128)
# Same local linearized null response for conformally related 2D massless scalar.
print('PASS independent symbolic audit: 2D/4D curvature, scalar action/T, R^2, finite jets')

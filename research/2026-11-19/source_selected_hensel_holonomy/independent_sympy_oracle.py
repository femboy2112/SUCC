"""Independent symbolic oracle; does not import the primary research implementation."""
import sympy as s

z = s.symbols('z')
n,p = s.symbols('n p',positive=True)
A = s.Matrix([[1,1],[1,0]])
M = A.inv()
T = s.Matrix([[16,32,24,8,1],[8,20,18,7,1],[4,12,13,6,1],[2,7,9,5,1],[1,4,6,4,1]])
Q = 4-2*z**3-z**4-z**5
H = s.cancel(Q/(1-z))
qstar = s.expand(Q+(1-z)**2)
hstar = s.cancel(qstar/(1-z))

def poly_mat(P, X):
    c=s.Poly(P,z)
    return sum((coef*(X**k) for (k,),coef in c.terms()),s.zeros(X.rows))

HM=poly_mat(H,M)
HM_star=poly_mat(hstar,M)
assert HM==s.Matrix([[8,1],[1,7]]) and HM.det()==55
assert HM_star==9*s.eye(2) and HM_star.det()==81
assert s.expand(Q.subs(z,1))==0 and Q.diff(z).subs(z,1)==-15
assert qstar.subs(z,1)==0 and qstar.diff(z).subs(z,1)==-15
assert s.expand(T.charpoly(z).as_expr()-(z-1)*(z*z-7*z+1)*(z*z-47*z+1))==0
assert T.det()==1
v=s.Matrix([8,1])
w=s.Matrix([v[0]**(4-j)*v[1]**j for j in range(5)])
assert all(x%11==0 for x in T*w-16*w)
assert (85**2-85-1)%121==0
assert (85**8-104)%121==0
assert (104**2-47*104+1)%121==0
assert (683**2-7*683+1)%841==0

r=lambda t: 4/(8*t-7)-2/(8*t-4)-1/(8*t-3)-1/(8*t-2)
rs=lambda t: r(t)+2/((8*t-7)*(8*t-6)*(8*t-5))
d=s.cancel(15*(r(n)-r(n+1)))
ds=s.cancel(15*(rs(n)-rs(n+1)))
assert s.limit(n**3*d,n,s.oo)==s.Rational(225,32)
assert s.limit(p**6*d.subs(n,(p*p-1)/8),p,s.oo)==3600
assert s.limit(n**2*rs(n),n,s.oo)==s.Rational(15,64)
for prime in (7,11,13,17,29,41,47,73,101):
    N=(prime*prime-1)//8
    for D,res in ((d,-60),(ds,-75)):
        X=s.cancel((prime*prime*D.subs(n,N)))
        top,bot=map(int,s.fraction(X))
        assert bot%prime and top*pow(bot,-1,prime)%prime==res%prime

print('PASS independent SymPy: source/mutant polynomials, matrices, charpoly, Hensel mod p²,')
print('signed commutator constants, real asymptotics, nine fresh prime-square residues')

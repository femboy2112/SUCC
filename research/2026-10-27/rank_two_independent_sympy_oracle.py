"""Independent optional sympy proof check; not used in production or unittest.

The native exact SUCC module uses a different, Fraction-based Q(i) algebra.
"""
import sympy as s

G=s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],
            [s.Rational(1,2),s.Rational(1,2)]])
H=s.Matrix([[0,1],[s.Rational(1,2),0]])
T=s.diag(G,H)
J=s.diag(1,1,-1,-1)
b=s.Matrix([1,0,1,0])
read=s.Matrix([[4,0,0,-4]])
t=s.symbols('t')
assert T**4 == -J/4
assert T**8 == s.eye(4)/16
f=s.factor((read*(s.eye(4)-t*T).inv()*b)[0])
assert s.factor(f-4*(1-t)/((1-t+t*t/2)*(1-t*t/2)))==0
C=s.Matrix.hstack(*[T**n*b for n in range(4)])
O=s.Matrix.vstack(*[read*T**n for n in range(4)])
assert C.det()==s.Rational(1,8)
assert O.det()==32
assert (O*C).det()==4
vplus=[(read[:,:2]*G**n*s.Matrix([1,0]))[0] for n in range(8)]
vminus=[(read[:,2:]*H**n*s.Matrix([1,0]))[0] for n in range(8)]
assert sum(vplus)==s.Rational(15,4) and sum(vminus)==-s.Rational(15,4)
n=s.symbols('n',positive=True)
rp=sum(vplus[j]/(8*n+j-7) for j in range(8))
rm=sum(vminus[j]/(8*n+j-7) for j in range(8))
assert s.limit(n*rp,n,s.oo)==s.Rational(15,32)
assert s.limit(n*rm,n,s.oo)==-s.Rational(15,32)
assert s.limit(n*n*(rp+rm),n,s.oo)==s.Rational(15,64)
print('INDEPENDENT RANK-TWO SYMPY CHECK PASSED: T4/T8, BBP rational K(t), rank4 Hankel, chiral source asymptotics')

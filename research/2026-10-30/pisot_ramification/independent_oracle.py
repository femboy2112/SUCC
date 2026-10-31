"""Independent exact SymPy oracle: non-Pisot to Pisot ramification."""
import sympy as s
from math import comb, sqrt

x,t,z=s.symbols('x t z')
p2=x*x-x-3
q2=(t-1)**2-(t-1)-3
assert s.expand(q2)==t*t-3*t-1
alpha2=(1+s.sqrt(13))/2;beta2=(1-s.sqrt(13))/2
assert 2<alpha2<3 and beta2<-1
assert abs(s.N(beta2+1))<1

A=s.Matrix([[1,0,3],[1,0,0],[0,1,0]])
I=s.eye(3)
B=2*I+A+A**2
p3=x**3-x**2-3
q3=t**3-8*t**2+5*t-1
assert s.factor(A.charpoly(x).as_expr()-p3)==0
assert s.factor(B.charpoly(t).as_expr()-q3)==0
assert B.det()==1
assert (2*I-A)*B==I and B*(2*I-A)==I
assert B.inv()==B**2-8*B+5*I
assert all(int(v)>=0 for v in B)
assert s.discriminant(p3,x)==s.discriminant(q3,t)==-255
assert s.factorint(255)=={3:1,5:1,17:1}
C=s.Matrix([[1,2,13],[0,1,7],[0,1,8]])
assert C.det()==1
assert (B**2)==13*I+7*A+8*(A**2)
assert s.rem(s.expand((2-x)*(x*x+x+2)-1),p3,x)==0
assert s.resultant(p3,t-(x*x+x+2),x)==q3

roots=s.nroots(p3,n=40)
alpha=[r for r in roots if abs(s.im(r))<s.Float('1e-30')][0]
others=[r for r in roots if r!=alpha]
assert s.Rational(9,5)<alpha<2
assert all(abs(s.im(r))>1 for r in others)
assert all(abs(complex(s.N(1/(2-r),30)))<1 for r in others)
assert all(abs(complex(s.N((r*r+r+2),30)))<1 for r in others)
assert abs(float(alpha)-float(2-1/(alpha*alpha+alpha+2)))<1e-12

# An independent dynamic-programming oracle for positive convolutions.
for ell in (2,3):
    d=22
    base=[0]*(d+1);full=[0]*(d+1)
    base[0]=full[0]=1
    for n in range(1,d+1):
        base[n]=base[n-1]+(base[n-ell] if n>=ell else 0)
        full[n]=full[n-1]+(3*full[n-ell] if n>=ell else 0)
    aggregate=[0]*(d+1)
    prod=[1]+[0]*d
    for k in range(d//ell+1):
        prod=[sum(prod[j]*base[i-j] for j in range(i+1)) for i in range(d+1)]
        for n in range(ell*k,d+1):
            aggregate[n]+=2**k*prod[n-ell*k]
    assert aggregate==full
print('Exact polynomial, discriminant, basis-index, matrix-inverse and positive-Pisot grammar: PASS')
print('A3 characteristic:',p3,'nonPisot dominant root:',s.N(alpha,17))
print('B3 characteristic:',q3,'Pisot unit root:',s.N(alpha*alpha+alpha+2,17))
print('Conjugate moduli:',*[round(abs(complex(s.N((r*r+r+2),30))),12) for r in others])
print('Ramified prime candidates (indeed ramified; disc squarefree):',s.factorint(255))

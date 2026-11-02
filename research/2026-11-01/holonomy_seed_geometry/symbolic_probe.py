"""Optional, independent SymPy source algebra cross-check (NOT proof authority)."""
import sympy as s
x=s.Symbol('x')
r=4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)
r_combined=(120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))
assert s.cancel(r-r_combined)==0
d=s.cancel(15*(r-r.subs(x,x+1)))
assert d.subs(x,1)==s.Rational(12301,273)
# The leading terms that prove the one-power curvature tail improvement.
assert s.limit(x**2*r,x,s.oo)==s.Rational(15,64)
assert s.limit(x**3*d,x,s.oo)==s.Rational(225,32)
# Two noncommuting source steps, independent affine-matrix computation.
def mat(n):return s.Matrix([[16,r.subs(x,n)],[0,1]])
F1,F2=mat(1),mat(2)
C=s.simplify(F2*F1*F2.inv()*F1.inv())
assert C==s.Matrix([[1,s.Rational(12301,273)],[0,1]])
# Independent finite quantum seed Fisher identity via centered generators.
for N in (2,3,4,8):
    times=s.Matrix([16**i for i in range(1,N+1)])
    mean=sum(times)/N
    v1=s.simplify(sum((a-mean)**2 for a in times)/N)
    v2=s.simplify(sum((a-b)**2 for a in times for b in times)/(2*N*N))
    assert v1==v2
print('Symbolic source, r~15/(64n^2), d~225/(32n^3), affine Wilson, Fisher variance: PASS')

"""Independent SymPy derivation of the normalized recursive-observer maps."""
import sympy as sp

p=sp.symbols('p',real=True)
P=sp.Matrix([[sp.Rational(3,5),sp.Rational(2,5)],
             [sp.Rational(2,5),sp.Rational(3,5)]])
L0=sp.diag(sp.Rational(2,3),sp.Rational(1,3))
L1=sp.diag(sp.Rational(1,3),sp.Rational(2,3))
row=sp.Matrix([[p,1-p]])

def norm_after(like):
    v=row*P*like
    return sp.factor(v[0]/(v[0]+v[1]))

F0=norm_after(L0)
F1=norm_after(L1)
assert sp.simplify(F0-(4+2*p)/(7+p))==0
assert sp.simplify(F1-(2+p)/(8-p))==0
assert sp.factor(sp.diff(F0,p))==10/(7+p)**2
assert sp.simplify(sp.diff(F1,p)-10/(8-p)**2)==0
roots=sp.solve(sp.together(F0-p),p)
positive=[r for r in roots if 0 < float(r) < 1]
assert len(positive)==1 and sp.simplify(positive[0]-(-5+sp.sqrt(41))/2)==0
cycle=sp.factor(F1.subs(p,F0))
cycle_roots=sp.solve(sp.together(cycle-p),p)
valid=[r for r in cycle_roots if 0<float(r)<1]
assert len(valid)==1 and sp.simplify(valid[0]-(-4+sp.sqrt(19)))==0
assert sp.simplify(F0.subs(p,valid[0])-(1-valid[0]))==0
# Algebraic obstruction to one common fixed point for 0/1 updates.
assert sp.simplify(F0-F1-3*(p+2)*(3-p)/((7+p)*(8-p)))==0
print('INDEPENDENT_SYMBOLIC_PASS')
print('F0(p)=',F0,'F1(p)=',F1)
print('Repeated-0 fixed state0 mass=',positive[0], '~',sp.N(positive[0],14))
print('Alternating cycle even state0 mass=',valid[0], '~',sp.N(valid[0],14))
print('F0 derivative=',sp.diff(F0,p),'F1 derivative=',sp.diff(F1,p))

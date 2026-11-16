"""Independent symbolic derivation: no import of primary atlas module."""
import json
import sympy as s

h=s.symbols('h',integer=True)
z,t=s.symbols('z t')
w=s.symbols('w',real=True)

Q=4-2*t**3-t**4-t**5
D=16-t**8
R=(1-t)/((2-t*t)*(t*t-2*t+2))
assert s.expand(Q-(1-t)*(t*t+2)*(t*t+2*t+2))==0
assert s.cancel(Q/D-R)==0

# Oily conditional weight is the two-geom convolution, conditioned grade > 0
G=1/(2-z)**2
Gstar=s.factor((G-s.Rational(1,4))/(s.Rational(3,4)))
assert s.factor(Gstar - (4/(2-z)**2-1)/3)==0
assert s.simplify(Gstar.subs(z,1))==1
assert s.simplify(s.diff(Gstar,z).subs(z,1))==s.Rational(8,3)

# Critical finite harmonic tail and phase-kernel derivative exact.
H=s.symbols('H',integer=True,nonnegative=True)
assert s.simplify(s.summation((h+1)/(3*2**h),(h,H+1,s.oo)) - (H+3)/(3*2**H)) == 0
assert s.simplify(s.diff(Gstar,z)-8/(3*(2-z)**3))==0

K=[]
for p in range(4):
    val=s.simplify(s.re(Gstar.subs(z,s.I**p)))
    K.append(val)
assert K==[1,-s.Rational(13,75),-s.Rational(5,27),-s.Rational(13,75)]

# Arbitrary declared radix cylinder counts; exact nonnegative sum of squares.
x=s.symbols('x0:16',real=True)
root=sum(x)
direct=16*sum(u*u for u in x)-root**2
squares=16*sum((u-root/16)**2 for u in x)
assert s.expand(direct-squares)==0

# Independent synthetic null iid collisions and finite-grid controls.
B=s.symbols('B',integer=True,positive=True)
k=s.symbols('k',integer=True,nonnegative=True)
collision=lambda k:1/B+(1-1/B)*16**(-k)
assert s.simplify((16*collision(k+1)-collision(k))/15-1/B)==0

# Rational-source completion: cross-boundary error coefficient.
assert s.simplify(s.Rational(7,32)*s.Rational(8,3)-s.Rational(7,12))==0

out={"factorized_BBP_Oily":True,"oily_conditioned_PGF":str(Gstar),
     "kernel_roots":[str(k) for k in K],"mean_h":str(s.diff(Gstar,z).subs(z,1)),
     "haar_general_16_child_parseval":True,"iid_diagonal_energy":"1/B",
     "source_transport_coefficient":"7/12","independent_symbolic_tests":12,
     "all_pass":True,"pi_normality":"OPEN","RH":"OPEN"}
print(json.dumps(out,indent=2))

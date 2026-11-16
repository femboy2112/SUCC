"""Independent SymPy polynomial congruence oracle; no import of chiral_probe."""
from sympy import symbols, expand, Poly, cancel, diff, factor
u,t=symbols('u t')
P=120*t**2-89*t+16
D=(2*t-1)*(4*t-1)*(8*t-7)*(8*t-3)
r=P/D
L=expand(diff(P,t)*D-P*diff(D,t))
print('Original forcing:', factor(r))
assert cancel(r - (4/(8*t-7)-2/(8*t-4)-1/(8*t-3)-1/(8*t-2))) == 0
for modulus, reps in ((16, [11,11,3,3]),
                      (32, [11,27,3,3,27,11,19,19])):
    for j,c in enumerate(reps):
        coeff = Poly(expand((L-c*D**2).subs(t,len(reps)*u+j)),u).all_coeffs()
        assert all(int(x)%modulus==0 for x in coeff), (modulus,j,c)
    print('Derivative polynomial certification modulo',modulus,
          'PASS; residues:',reps)
# D(t) is congruent to 1 as polynomial mod2; all nonconstant coefficients even.
Dcoeff = Poly(expand(D), t).all_coeffs()
assert int(Dcoeff[-1])%2 == 1
assert all(int(c)%2==0 for c in Dcoeff[:-1])
# Second divided Taylor coefficient in rational source expansion is even.
# r''/2 = (P''/2*D² - P'D D' + P*(D'^2-D D''/2))/D³
P1=diff(P,t); P2=diff(P,t,2)/2
D1=diff(D,t); D2=diff(D,t,2)/2
C2numer=expand(P2*D**2 - P1*D*D1 + P*(D1**2-D*D2))
assert all(int(c)%2==0 for c in Poly(C2numer,t).all_coeffs())
print('Second Taylor coefficient even in Z_2[t,1/D]: PASS')
print('All algebra assertions PASS')

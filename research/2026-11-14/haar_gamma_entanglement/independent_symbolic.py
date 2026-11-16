"""Independently encoded SymPy oracle for source-labelled quantum/Haar/Gamma model.

Does not import observational_succ.haar_gamma_entanglement. Uses independent
matrix multiplication/density/partial-trace implementations and symbolic checks.
No external measurements are performed.
"""
import sympy as S

i=S.I; half=S.Rational(1,2)
X=S.Matrix([[0,1],[1,0]])
Y=S.Matrix([[0,-i],[i,0]])
Z=S.diag(1,-1)
Id=S.eye(2)

def bell_sector(z):
    r=S.zeros(4)
    r[0,0]=r[3,3]=half
    r[0,3]=z*half;r[3,0]=S.conjugate(z)*half
    return r

def partial_B(r):
    return S.Matrix([[sum(r[2*a+b,2*a+c] for a in range(2)) for c in range(2)] for b in range(2)])

def p_partial_b(r,P):
    K=S.kronecker_product(P,Id)
    return partial_B(K*r*K.H)

def want(cond,desc):
    if not cond:raise AssertionError(desc)

def zero_matrix(m):return all(S.simplify(e)==0 for e in m)

checks=0
for alpha in range(0,9):
    gam=S.expand((1+i)**(-alpha))
    r=bell_sector(gam)
    want(S.simplify(S.trace(r)-1)==0,'trace')
    checks+=1
    want(zero_matrix(partial_B(r)-Id*half),'fixed Bob marginal')
    checks+=1
    for p in (X,Y,Z):
        Ps=[(Id+s*p)/2 for s in [-1,1]]
        conditional=[p_partial_b(r,Q) for Q in Ps]
        want(zero_matrix(conditional[0]+conditional[1]-Id*half),'Bob no signalling')
        checks+=1
        want(all(S.simplify(S.trace(c)-half)==0 for c in conditional),'marginal probabilities')
        checks+=1
    for left,right,expected in [(Z,Z,1),(X,X,S.re(gam)),(X,Y,-S.im(gam))]:
        got=S.trace(r*S.kronecker_product(left,right))
        want(S.simplify(got-expected)==0,'Pauli scan')
        checks+=1
    pt=S.Matrix([[r[2*a+d,2*c+b] for c in range(2) for d in range(2)] for a in range(2) for b in range(2)])
    # reorder PT_B 2x2 principal block positions |01>,|10> index (1,2)
    minor=S.simplify(pt[1,1]*pt[2,2]-pt[1,2]*pt[2,1])
    want(S.simplify(minor+gam*S.conjugate(gam)/4)==0,'PPT minor')
    checks+=1
    want(S.simplify((4*(1+gam*S.conjugate(gam)))-(4+4/(2**alpha)))==0,'CHSH maximum spectrum')
    checks+=1

r2=bell_sector(-i/2)
cls=bell_sector(0)
want(zero_matrix(S.diag(*(r2[j,j]-cls[j,j] for j in range(4)))),'diagonal Haar indistinguishability');checks+=1
want(S.simplify(S.trace(r2*S.kronecker_product(X,Y))-S.Rational(1,2))==0,'hidden XY quadrature');checks+=1
want(S.simplify(S.trace(cls*S.kronecker_product(X,Y)))==0,'separable control');checks+=1
want(zero_matrix(p_partial_b(bell_sector(1),(Id+X)/2)-S.Matrix([[S.Rational(1,4),S.Rational(1,4)],[S.Rational(1,4),S.Rational(1,4)]])),'Bell steering');checks+=1
want(zero_matrix(p_partial_b(cls,(Id+X)/2)-Id/4),'classical conditioning');checks+=1

# An alternative independent Fourier realization of the Gamma integral.
t=S.symbols('t',positive=True)
for alpha in range(1,7):
    exact=S.integrate(t**(alpha-1)*S.exp(-t)*S.exp(-i*t),(t,0,S.oo))/S.gamma(alpha)
    want(S.simplify(exact-(1+i)**(-alpha))==0,'gamma Fourier-Laplace oracle');checks+=1

# Haar finite digit + propensity normalization calculated independently.
H=S.Matrix([(-1)**a for a in range(16)])
resp=S.Matrix([S.Rational(3,4) if a%2==0 else S.Rational(1,4) for a in range(16)])
policy=S.Matrix([S.Rational(3,32) if a%2==0 else S.Rational(1,32) for a in range(16)])
target=(H.dot(resp))/16
raw=sum(H[a]*resp[a]*policy[a] for a in range(16))
corrected=sum(policy[a]*H[a]*resp[a]/(16*policy[a]) for a in range(16))
want(target==S.Rational(1,4) and raw==S.Rational(1,2) and corrected==target,'selective sampling alias')
checks+=1
print('INDEPENDENT_SYMPY_ORACLE_PASS',{'symbolic_assertions':checks,'depths':9,'gamma_integrals':6,'policy_residual':'1/4','gamma2_imaginary':'-I/2'})

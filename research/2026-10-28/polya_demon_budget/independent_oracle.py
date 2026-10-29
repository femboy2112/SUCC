"""Independent symbolic control: does not import demon_budget or its unittest."""
import sympy as s

a=s.symbols('a', positive=True)
checks=0
for j in range(0,12):
    z=lambda k:sum(a**v for v in range(k+1))
    # Original source transition and geometric tilted transport via separate rational identities.
    u=[s.Rational(1,j+1)]*(j+1)
    pu=[s.Integer(0)]*(j+2)
    for k in range(j+1):
        t=s.Rational(k+1,j+2)
        pu[k]+=u[k]*(1-t)
        pu[k+1]+=u[k]*t
    assert all(s.cancel(v-s.Rational(1,j+2))==0 for v in pu)
    checks+=1
    q=[a**k/z(j) for k in range(j+1)]
    nxt=[s.Integer(0)]*(j+2)
    for k in range(j+1):
        t=a**(j+1-k)*(1-a**(k+1))/(1-a**(j+2))
        nxt[k]+=q[k]*(1-t)
        nxt[k+1]+=q[k]*t
    assert all(s.cancel(nxt[k]-a**k/z(j+1))==0 for k in range(j+2))
    checks+=1
    # An unmodified Pólya transition cannot propagate a geometric amplitude by scalar.
    if j>=1:
        r=s.symbols('r',positive=True)
        rightmost_true=r**j*s.Rational(j+1,j+2)
        rightmost_guessed=r**(j+1)*s.Rational(j+1,j+2)
        assert s.simplify(rightmost_true-rightmost_guessed-s.Rational(j+1,j+2)*r**j*(1-r))==0
        checks+=1
print('independent symbolic checks:',checks, 'PASS')

"""Independent symbolic/combinatorial derivations; imports no primary implementation."""
import sympy as s


def factorial_path_weight(j, k, m):
    # Beta(m,1) mixing integrated for one specific Bernoulli path.
    return s.factorial(k + m - 1) * s.factorial(j-k) * m / s.factorial(j+m)

checks = 0
for m in range(1,7):
    for j in range(0,11):
        denominator = s.rf(j+1,m)
        for k in range(j+1):
            via_integral = s.binomial(j,k)*m*s.beta(k+m,j-k+1)
            via_factorial = s.Rational(m) * s.factorial(j) * s.factorial(k+m-1) / (s.factorial(k)*s.factorial(j+m))
            from_rising = s.Rational(m)*s.rf(k+1,m-1)/denominator
            assert s.simplify(s.expand_func(via_integral)-via_factorial)==0
            assert s.simplify(via_factorial-from_rising)==0
            checks+=1
            # A de Finetti posterior U|K_j=k is Beta(k+1,j-k+1).
            weight=s.rf(k+1,m-1)/s.rf(j+2,m-1)
            assert s.simplify(from_rising-s.Rational(1,j+1)*m*weight)==0
            checks+=1
            h=m*weight
            h_up=m*s.rf(k+2,m-1)/s.rf(j+3,m-1)
            h_stay=m*s.rf(k+1,m-1)/s.rf(j+3,m-1)
            p=s.Rational(k+1,j+2)
            assert s.simplify((1-p)*h_stay+p*h_up-h)==0
            assert s.simplify(p*h_up/h-s.Rational(k+m,j+m+1))==0
            checks+=1
        assert s.simplify(sum([s.Rational(m)*s.rf(k+1,m-1)/denominator for k in range(j+1)])-1)==0
        checks+=1

# Exact model distinction: max of *discrete* grade observations is not
# max of latent uniforms followed by a binomial observation.
for j in range(1,20):
    discrete=s.Rational(2*j+1,(j+1)**2)
    latent=s.Rational(2, j+2)
    assert s.simplify(discrete-latent)!=0
    checks+=1

# Polynomial reciprocity identity proves no roots of P_j(z)=sum_(k=0)^j (k+1)z^k
# on or beyond the unit circle. Reverse R_j(w)=sum (j+1-k)w^k.
# (1-w)R_j(w)=(j+1)-sum_(k=1)^(j+1) w^k;
# for |w|<=1, latter cannot vanish except maybe w=1, where R_j(1)>0.
w=s.symbols('w')
for j in range(1,20):
    R=sum((j+1-k)*w**k for k in range(j+1))
    assert s.expand((1-w)*R - ((j+1)-sum(w**k for k in range(1,j+2))))==0
    assert R.subs(w,1)==s.Rational((j+1)*(j+2),2)
    checks+=1

# Explicit two-branch source reconstruction and first local off-axis zero.
z=s.symbols('z')
for j in range(1,30):
    plus=sum(s.Rational(2*(k+1),(j+1)*(j+2))*z**k for k in range(j+1))
    minus=sum(s.Rational(2*(j+1-k),(j+1)*(j+2))*z**k for k in range(j+1))
    source=sum(s.Rational(1,j+1)*z**k for k in range(j+1))
    assert s.expand((plus+minus)/2-source)==0
    checks+=1
assert s.expand(1+2*z).subs(z,-s.Rational(1,2))==0
assert s.expand(2+z).subs(z,-2)==0
checks+=2

print('INDEPENDENT_SYMPY_ORACLE_CHECKS=',checks,'PASS')

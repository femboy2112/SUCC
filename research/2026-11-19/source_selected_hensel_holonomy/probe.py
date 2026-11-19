"""Authentic BBP source-filter / moving 11-adic frame / ordered-source commutator.

Research-only exact stdlib probes. Source is literal, U0=0, and π-normality OPEN.
"""
from fractions import Fraction
from math import gcd
from cmath import exp, pi

A = ((1, 1), (1, 0))
M = ((0, 1), (1, -1))  # exact inverse of A
T = (
    (16, 32, 24, 8, 1),
    (8, 20, 18, 7, 1),
    (4, 12, 13, 6, 1),
    (2, 7, 9, 5, 1),
    (1, 4, 6, 4, 1),
)
H = (4, 4, 4, 2, 1)
BETA = (7, 4, 3, 2)
C = (4, -2, -1, -1)


def matmul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(len(Y)))
                       for j in range(len(Y[0]))) for i in range(len(X)))


def eye(d):
    return tuple(tuple(int(i == j) for j in range(d)) for i in range(d))


def matpow(B, k):
    assert k >= 0
    R = eye(len(B))
    while k:
        if k & 1:
            R = matmul(R, B)
        B = matmul(B, B)
        k //= 2
    return R


def matsum(*Xs):
    return tuple(tuple(sum(X[i][j] for X in Xs) for j in range(len(Xs[0][0])))
                 for i in range(len(Xs[0])))


def scale(X, c):
    return tuple(tuple(c * x for x in row) for row in X)


def polyeval_mat(coeffs, X):
    return matsum(*(scale(matpow(X, j), c) for j, c in enumerate(coeffs)))


def mat_mod(X, p):
    return tuple(tuple(x % p for x in row) for row in X)


def matvec(X, v, p=None):
    out = tuple(sum(x*y for x, y in zip(row, v)) for row in X)
    return tuple(x % p for x in out) if p is not None else out


def leftmul(v, X, p):
    return tuple(sum(v[i] * X[i][j] for i in range(len(X))) % p for j in range(len(X[0])))


def sym4_vector(v, p):
    a, b = v
    return tuple((pow(a, 4-j, p) * pow(b, j, p)) % p for j in range(5))


def det2(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def hensel_quad(base, b, c, p, precision):
    """Unique simple root of x*x+b*x+c mod p**precision."""
    assert (base*base+b*base+c) % p == 0
    assert gcd((2*base+b), p) == 1
    a, m = base % p, p
    for _ in range(1, precision):
        candidates = [a+k*m for k in range(p) if ((a+k*m)**2+b*(a+k*m)+c) % (m*p) == 0]
        assert len(candidates) == 1
        a, m = candidates[0], m*p
    return a


def source_filter():
    return polyeval_mat(H, M)


def mutated_filter():
    co = tuple(H[j] + (1 if j == 4 else 0) for j in range(5))
    return polyeval_mat(co, M)


def matched_jet_filter():
    """H_*=H+(1-t): shares Q(1)=0, Q'(1)=-15, breaks 11 selection."""
    co=tuple(H[j] + (1 if j==0 else -1 if j==1 else 0) for j in range(5))
    return polyeval_mat(co,M)


def matched_jet_forcing(n):
    a=8*n-7
    return forcing(n)+Fraction(2,a*(a+1)*(a+2))


def forcing(n, coeffs=C):
    assert n >= 1
    return sum((Fraction(c, 8*n-b) for c, b in zip(coeffs, BETA)), Fraction())


def source_order_defect(n, coeffs=C):
    assert n >= 1
    return 15*(forcing(n, coeffs)-forcing(n+1, coeffs))


def commutator_gradient(n):
    return tuple(Fraction(120, (8*n-b)*(8*n+8-b)) for b in BETA)


def source_state(N, seed=Fraction(0)):
    u=[seed]
    for n in range(1,N+1):
        u.append(16*u[-1]+forcing(n))
    return u


def valuation(q,p):
    assert q != 0
    a,b=abs(q.numerator),q.denominator
    v=0
    while a%p==0:
        a//=p;v+=1
    while b%p==0:
        b//=p;v-=1
    return v


def rational_mod_p(q, p):
    assert q.denominator % p
    return q.numerator * pow(q.denominator, -1, p) % p


def visibility_delay(n):
    """First clock delay where swapped-source difference >=1/32 turn."""
    d = source_order_defect(n)
    assert 0 < d < Fraction(1,32), 'requires n>=7'
    k=0
    while 16**k*d < Fraction(1,32):
        k+=1
    assert Fraction(1,32) <= 16**k*d < Fraction(1,2)
    return k,16**k*d


def source_prime_square_event(p):
    assert p >= 7 and p % 2
    n=(p*p-1)//8
    d=source_order_defect(n)
    return n,valuation(d,p),rational_mod_p(p*p*d,p),d


def main_receipt():
    hm=source_filter()
    assert hm == ((8,1),(1,7)) and det2(hm)==55
    assert det2(mutated_filter())==116
    assert matched_jet_filter()==((9,0),(0,9)) and det2(matched_jet_filter())==81
    assert mat_mod(hm,11) == ((8,1),(1,7))
    assert matvec(hm,(1,3),11)==(0,0)
    assert matvec(A,(8,1),11)==(9,8)
    w=sym4_vector((8,1),11)
    assert w==(4,6,9,8,1)
    assert matvec(T,w,11)==tuple((16*z)%11 for z in w)
    ell=(4,2,10,10,1)
    assert leftmul(ell,T,11)==tuple(16*z%11 for z in ell)
    assert sum(x*y for x,y in zip(ell,w))%11==1
    a=hensel_quad(8,-1,-1,11,2)
    ak=hensel_quad(4,-1,-1,11,2)
    lam11=hensel_quad(16,-47,1,11,2)
    lam29=hensel_quad(16,-7,1,29,2)
    assert (a,ak,lam11,lam29)==(85,37,104,683)
    assert pow(a,8,121)==lam11
    assert (8+pow(a,-1,121))%121==92
    assert (8+pow(ak,-1,121))%121==44
    w121=sym4_vector((a,1),121)
    assert matvec(T,w121,121)==tuple((lam11*z)%121 for z in w121)
    rho11=16*pow(lam11,-1,121)%121
    rho29=16*pow(lam29,-1,841)%841
    assert (rho11,rho29)==(56,117)
    for n in range(200):
        assert pow(rho11,n,121)==(1+55*n)%121
        assert pow(rho29,n,841)==(1+116*n)%841
        assert (pow(rho11,n+1,121)*lam11)%121 == (16*pow(rho11,n,121))%121
    # 11-adic gauge memory: exactly one extra digit per factor of 11 in elapsed time.
    for k in range(4):
        mod=11**(k+3)
        lam=hensel_quad(16,-47,1,11,k+3)
        rho=16*pow(lam,-1,mod)%mod
        val=(pow(rho,11**k,mod)-1)%mod
        assert val % (11**(k+1)) == 0 and val % (11**(k+2)) != 0
    # Over one 11-frame period a locked carrier can falsely look Haar after gauge masking.
    assert abs(sum(exp(2j*pi*((1+55*n)%121)/121) for n in range(11))) < 1e-12
    # Authentic ordered-source swap, including a seed-independent affine commutator.
    for n in range(1,65):
        rn,rn1=forcing(n),forcing(n+1)
        assert (16*(16*Fraction(7,11)+rn)+rn1) - (16*(16*Fraction(7,11)+rn1)+rn) == source_order_defect(n)
        assert sum((c*g for c,g in zip(C,commutator_gradient(n))),Fraction()) == source_order_defect(n)
    for n in (7,11,17,29,55,89,144,233,610,987,1597):
        d,z=visibility_delay(n)
        assert 0 < d and Fraction(1,32)<=z<Fraction(1,2)
    for p in (7,11,13,17,19,23,29,41,47):
        n,val,res,d=source_prime_square_event(p)
        assert val==-2 and res==(-60)%p
        star=15*(matched_jet_forcing(n)-matched_jet_forcing(n+1))
        assert valuation(star,p)==-2 and rational_mod_p(p*p*star,p)==(-75)%p
    # Test predicted asymptotic constant via *exact* rational inequalities at held-out scales.
    for n in (5000,10000,25000):
        relative=source_order_defect(n)*n**3 / Fraction(225,32)
        assert Fraction(99,100) < relative < Fraction(101,100)
    print('PASS: exact source-selected 11-adic eigenline, Hensel lift, gauge, phase-masking mutant,')
    print('      source-order commutator, prime-square residues, and logarithmic visibility')
    print('H(M):',hm,'H mutant determinants:',det2(mutated_filter()),det2(matched_jet_filter()))
    print('11-adic eigenline:',w,'11-adic lifted A eigenvalue:',a,'radix-matching T eigenvalue mod 121:',lam11)
    print('11-adic gauge mod 121:',rho11,'29-adic gauge mod 841:',rho29)
    print('Prime source-order events:',[(p,source_prime_square_event(p)[:3]) for p in (7,11,13,17,29,41,47)])
    print('Visibility delays:',[(n,visibility_delay(n)[0]) for n in (7,11,17,29,55,89,144,233,610,987)])
    print('No R0 or pi normality theorem asserted.')

if __name__=='__main__':
    main_receipt()

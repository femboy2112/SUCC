#!/usr/bin/env python3
"""Exact standard-library crucible for SUCC's Fibonacci 2x5x3 / BBP resonance.

READ ONLY. Original BBP forcing and U_0=0 are retained verbatim.
No asymptotic Weyl estimate is claimed or tested.
"""
from fractions import Fraction
from math import isqrt, prod


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    if n == 0:
        return 2
    a, b = 2, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def matadd(A, B, s=1):
    return [[A[i][j]+s*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scale(A, c):
    return [[c*x for x in row] for row in A]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matpow(A, n):
    out = identity(len(A))
    for _ in range(n):
        out = matmul(out, A)
    return out


def transpose(A):
    return [list(row) for row in zip(*A)]


def evalpoly(c, A):
    N = len(A)
    out = [[0]*N for _ in range(N)]
    power = identity(N)
    for a in c:
        out = matadd(out, scale(power, a))
        power = matmul(power, A)
    return out


def prime(p):
    if p <= 1:
        return False
    for q in range(2, isqrt(p)+1):
        if p % q == 0:
            return False
    return True


def order16(p):
    assert p % 2 == 1 and prime(p)
    x = 16 % p
    d = 1
    while x != 1:
        x = (16*x) % p
        d += 1
    return d


def rank_of_appearance(m):
    if m == 1:
        return 1
    a, b = 0, 1
    for k in range(1, 6*m + 1):
        a, b = b % m, (a+b) % m
        if a == 0:
            return k
    raise AssertionError('no appearance found')


def r(n):
    return Fraction(4, 8*n-7)-Fraction(2, 8*n-4)-Fraction(1, 8*n-3)-Fraction(1, 8*n-2)


def mod_fraction(a, p):
    assert a.denominator % p != 0, (a, p)
    return (a.numerator * pow(a.denominator, -1, p)) % p


checks = 0

def check(x, tag):
    global checks
    assert x, tag
    checks += 1


A = [[1, 1], [1, 0]]
A5 = matpow(A, 5)
A10 = matpow(A, 10)
check(A5 == [[8, 5], [5, 3]], '5 step Fibonacci transfer')
check(A10 == [[89, 55], [55, 34]], '10 step Fibonacci transfer')
check(A10 == matadd(scale(A5, 11), identity(2)), '3-term 5-block recurrence')
for k in range(80):
    check(fib(k+10) == 11*fib(k+5)+fib(k), ('block recurrence', k))
check(fib(10) == 55 == fib(5)*lucas(5), 'F10=F5*Lucas5')
for m in range(1, 20):
    check(fib(5*m) % 5 == 0, ('mod 5 resonance',m))
    check(fib(5*m) % 11 == (5 if m%2 else 0), ('mod11 two-cycle',m))

Sym2 = [[1,2,1],[1,1,0],[1,0,0]]
check(matadd(matadd(matadd(matpow(Sym2,3),scale(matpow(Sym2,2),-2)),scale(Sym2,-2)),identity(3))==[[0]*3 for _ in range(3)], 'Sym2 3rd order')
for n in range(30):
    x, y = fib(n+1), fib(n)
    check(x*x-x*y-y*y==(-1)**n, ('Cassini',n))

Ainv = [[0,1],[1,-1]]
Qcoeff = [4,0,0,-2,-1,-1]
QAinv = evalpoly(Qcoeff,Ainv)
check(QAinv==[[7,-6],[-6,13]], 'BBP Q(Fibonacci inverse)')
check(QAinv[0][0]*QAinv[1][1]-QAinv[0][1]*QAinv[1][0]==55, 'source resultant norm 55')
check(QAinv==matadd(scale(identity(2),15),matadd(A5,Ainv),-1),'Q=15I-A5-A^-1')

R = [[int(i==(j+1)%5) for j in range(5)] for i in range(5)]
C = matadd(R,transpose(R))
P = [[int(i==2*j%5) for j in range(5)] for i in range(5)]
J = [[1]*5 for _ in range(5)]
h = [4,4,4,2,1]
H = evalpoly(h,R)
G = matmul(H,transpose(H))
QC = evalpoly(Qcoeff,C)
check(matadd(matmul(matmul(P,G),transpose(P)),QC,-1)==scale(J,57),'pentagon BBP Gram intertwiner')
check(G==[[53,46,40,40,46],[46,53,46,40,40],[40,46,53,46,40],[40,40,46,53,46],[46,40,40,46,53]],'Gram coefficients')
check(QC==matadd(matadd(scale(identity(5),7),scale(C,-6)),scale(J,-11)),'BBP Q(C) algebra')

h_mut = [4,4,4,2,2]
q_mut = [h_mut[0]]+[h_mut[i]-h_mut[i-1] for i in range(1,5)]+[-h_mut[4]]
Gmut = matmul(evalpoly(h_mut,R),transpose(evalpoly(h_mut,R)))
Dmut = matadd(matmul(matmul(P,Gmut),transpose(P)),evalpoly(q_mut,C),-1)
check(Dmut != scale(J,Dmut[0][0]), 'mutant defeats source-specific intertwiner')

check(rank_of_appearance(5)==5,'rank 5')
check(rank_of_appearance(11)==10,'rank 11')
check(rank_of_appearance(9)==12,'rank 9')
for p in [17,23,31,41,73,89,397]:
    d=order16(p)
    z=rank_of_appearance(d)
    for k in range(1,75):
        check((pow(16,fib(k),p)==1)==(k%z==0),('rank/order',p,k))

# F10=55: eligible prime witnesses at BBP terminal clock 56.
N=56
L=55
ps=[p for p in range(isqrt(8*N)+1,8*N+1) if prime(p) and pow(16,L,p)==1]
check(ps==[23,31,41,89,397], 'complete resonant simple prime list')
U=[Fraction(0)]
for n in range(1,N+1):
    U.append(16*U[-1]+r(n))
expected={23:(11,9),31:(5,19),41:(5,33),89:(11,30),397:(11,4)}
observations=[]
for p in ps:
    check(p*p>8*N,'simple p range')
    check(order16(p)==expected[p][0], ('prime order',p))
    check(mod_fraction(Fraction(p)*U[1],p)==0,('prime initial zero',p))
    from_fraction=mod_fraction(Fraction(p)*U[N],p)
    a=0
    for j in range(2,N+1):
        a=(16*a+mod_fraction(p*r(j),p))%p
    check(a==from_fraction==expected[p][1],('independent local recurrence',p))
    check(U[N].denominator%p==0 and a!=0,('prime survives reduced denominator',p))
    observations.append((p,order16(p),a))
check(U[N].denominator%prod(ps)==0,'complete product divides Q56')

# The separate order-9 family: rank z(9)=12 and F12=144, p=73.
p=73
check(order16(p)==9 and rank_of_appearance(9)==12 and pow(16,fib(12),p)==1,'73 resonance')
next_u=U[N]
a130=None
for j in range(N+1,275):
    next_u=16*next_u+r(j)
    if j==130:
        a130=mod_fraction(p*next_u,p)
a274=mod_fraction(p*next_u,p)
check(p*p>8*274,'p73 simple clock window')
check(a130==8 and a274==0 and (a274-a130)%p==65,'p73 source innovation')

print('Exact checks:',checks)
print('F_10=55, F_5=5, L_5=11: PASS')
print('BBP Q(A^-1)=', QAinv, 'det=',55)
print('Pentagonal source Gram conjugacy difference = 57*all-ones: PASS')
print('Changing one of the five memory channels destroys the conjugacy: PASS')
print('Fibonacci rank-of-appearance / prime-order tests: PASS')
print('Resonant simple-prime witnesses for original U56:',observations)
print('Product of five primes:',prod(ps),'divides den(U56):',U[N].denominator%prod(ps)==0)
print('Order-9 p=73 at F12=144: source-local 8 -> 0, innovation 65')
print('Does not prove Weyl cancellation, R0, or base-16 normality of pi.')

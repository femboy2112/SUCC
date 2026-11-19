"""Exact stdlib-only control for causally lifted 2/3/5, BBP null jets, and source pentagon norms."""
from fractions import Fraction
from math import comb
from itertools import permutations
import unittest

H = [4,4,4,2,1]

def r(n):
    if n < 1: raise ValueError('BBP source time starts at n=1')
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def forward_null(n,k):
    return sum(((-1)**j*comb(k,j)*r(n+j) for j in range(k+1)),Fraction(0))

def past_difference(t,k):
    if t-k < 1: raise ValueError('past samples unavailable')
    return sum(((-1)**j*comb(k,j)*r(t-j) for j in range(k+1)),Fraction(0))

def convolve(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    return v

def coeff(k, mutation=False):
    h=H[:]
    if mutation:h[-1]+=1
    op=[0]*(8*k+1)
    for j in range(k+1):op[8*j]=(-1)**j*comb(k,j)
    return convolve(h,op)

def matmul(a,b):
    return [[sum(a[i][z]*b[z][j] for z in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def poly_matrix(c,M):
    n=len(M); p=[[int(i==j) for j in range(n)] for i in range(n)]
    a=[[0]*n for i in range(n)]
    for v in c:
        for i in range(n):
            for j in range(n):a[i][j]+=v*p[i][j]
        p=matmul(p,M)
    return a

def det(A):
    n=len(A)
    ans=0
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        prod=(-1)**inv
        for i in range(n):prod*=A[i][p[i]]
        ans+=prod
    return ans

M=[[0,1],[1,-1]]
R=[[int(i==(j+1)%5) for j in range(5)] for i in range(5)]

def norm_f(c):
    return det(poly_matrix(c,M))

def norm_5(c):
    P=poly_matrix(c,R)
    # columns represent P(e_j-e_4) for j=0..3; first 4 components are coordinates in V_0 basis
    A=[[P[i][j]-P[i][4] for j in range(4)] for i in range(4)]
    return det(A)

def compose(a,b):
    # a after b
    return tuple(a[b[i]-1] for i in range(5))

id5=(1,2,3,4,5)
a=(2,1,4,3,5)  # (12)(34)
b=(1,4,3,5,2)  # (245)

def power(g,k):
    z=id5
    for _ in range(k):z=compose(g,z)
    return z

def causal_word(word):
    n=0; state=1; trace=[]
    for name,g in word:
        n+=1;state=g[state-1];trace.append((n,name,state))
    return n,state,trace

class Causal235ExactTests(unittest.TestCase):
    def test_icosahedral_generators(self):
        self.assertEqual(power(a,2),id5)
        self.assertEqual(power(b,3),id5)
        ab=compose(a,b)
        self.assertEqual(ab,(2,3,4,5,1))
        self.assertEqual(power(ab,5),id5)
        # Distinct noncommutative paths do not commute.
        self.assertNotEqual(compose(a,b),compose(b,a))
        # Count all generated permutations, independent of abstract group label.
        seen={id5}; frontier=[id5]
        while frontier:
            x=frontier.pop()
            for g in (a,b):
                y=compose(g,x)
                if y not in seen: seen.add(y);frontier.append(y)
        self.assertEqual(len(seen),60)
    def test_causal_lift_not_group_identity(self):
        n,s,t=causal_word([('a',a)]*2)
        self.assertEqual((n,s),(2,1));self.assertEqual(len(t),2)
        n,s,t=causal_word([('b',b)]*3)
        self.assertEqual((n,s),(3,1));self.assertEqual(len(t),3)
        n,s,t=causal_word([('b',b),('a',a)]*5)
        self.assertEqual((n,s),(10,1));self.assertEqual(len(t),10)
        self.assertNotEqual((n,s,t),(0,1,[]))
    def test_delayed_causal_source_null(self):
        for n in range(1,23):
            for k in range(9):
                self.assertEqual(forward_null(n,k),(-1)**k*past_difference(n+k,k))
        with self.assertRaises(ValueError):past_difference(4,4)
    def test_exact_fibonacci_pentagon_depth(self):
        for k in range(7):
            c=coeff(k)
            self.assertEqual(norm_f(c),55*(-45)**k)
            self.assertEqual(norm_5(c),55*5**k)
            self.assertEqual(Fraction(norm_f(c),norm_5(c)),(-9)**k)
    def test_source_mutation_breaks_base_intertwiner(self):
        self.assertNotEqual(norm_f(coeff(0,True)),norm_5(coeff(0,True)))
    def test_local_3adic_depth_not_real_small(self):
        for k in range(1,8):
            d=(-9)**k
            self.assertEqual(abs(d),9**k) # growing real magnitude
            self.assertEqual(d%2,1)
            self.assertEqual(d//(3**(2*k)),(-1)**k)

if __name__=='__main__':unittest.main(verbosity=2)

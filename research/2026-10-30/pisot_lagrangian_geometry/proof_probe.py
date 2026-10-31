"""Finite exact checks for SUCC's declared Pisot-variational lattice.
No original BBP source modification, no physical-curvature or pi-normality proof.
"""
from fractions import Fraction as F
import unittest

A=((1,1),(1,0)); B=((2,1),(3,2)); I=((1,0),(0,1))
P=((1,3),(-2,-5)); E=(F(1),F(0))

def mm(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def minus(X,Y):
    return tuple(tuple(X[i][j]-Y[i][j] for j in range(2)) for i in range(2))
def inv(X):
    d=X[0][0]*X[1][1]-X[0][1]*X[1][0]
    return ((F(X[1][1],d),F(-X[0][1],d)),(F(-X[1][0],d),F(X[0][0],d)))
def mv(X,y):
    return tuple(sum(X[i][j]*y[j] for j in range(2)) for i in range(2))
def powm(X,n):
    v=I
    for _ in range(n): v=mm(v,X)
    return v
def source(a):
    a=F(a)
    return 4/a-2/(a+3)-1/(a+4)-1/(a+5)
def energy(v,r):
    C=minus(mm(A,B),mm(B,A))
    f=tuple(r*z for z in E)
    delta=tuple(x+y-z for x,y,z in zip(mv(C,v),f,mv(B,f)))
    W=((9,9),(9,16))
    wd=mv(inv(W),delta)
    return sum(delta[i]*wd[i] for i in range(2))/2

class ExactChecks(unittest.TestCase):
    def test_pisot_characteristic(self):
        self.assertEqual(minus(mm(A,A),A),I)
        self.assertEqual(mm(B,B),((7,4),(12,7)))
        self.assertEqual(B[0][0]*B[1][1]-B[0][1]*B[1][0],1)
    def test_nonflat_and_sixfold(self):
        self.assertEqual(minus(mm(A,B),mm(B,A)),((2,1),(-3,-2)))
        H=mm(inv(mm(B,A)),mm(A,B))
        self.assertEqual(H,((-11,-7),(19,12)))
        self.assertEqual(powm(H,3),((-1,0),(0,-1)))
        self.assertEqual(powm(H,6),I)
    def test_eisenstein(self):
        H=mm(inv(mm(B,A)),mm(A,B))
        self.assertEqual(mm(mm(inv(P),H),P),((0,-1),(1,1)))
        G=((F(19),F(23,2)),(F(23,2),F(7)))
        Ht=((H[0][0],H[1][0]),(H[0][1],H[1][1]))
        self.assertEqual(mm(mm(Ht,G),H),G)
    def test_continuum_log_parity(self):
        self.assertEqual(A[0][0]*A[1][1]-A[0][1]*A[1][0],-1)
        K=((1,2),(2,-1)); J=((0,1),(3,0))
        self.assertEqual(mm(K,K),((5,0),(0,5)))
        self.assertEqual(mm(J,J),((3,0),(0,3)))
        self.assertEqual(minus(mm(K,J),mm(J,K)),((4,2),(-6,-4)))
    def test_flat_control(self):
        A2=mm(A,A)
        self.assertEqual(mm(A,A2),mm(A2,A))
    def test_nonpisot_emergence(self):
        C=((3,1),(1,2))  # A+2I; polynomial x^2-5x+5.
        self.assertEqual(C[0][0]+C[1][1],5)
        self.assertEqual(C[0][0]*C[1][1]-C[0][1]*C[1][0],5)
    def test_authentic_BBP_coefficients(self):
        self.assertEqual(source(1),F(47,15))
        for n in range(1,30):
            self.assertEqual(source(8*n-7),F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
    def test_59_jet_and_matched_fake(self):
        for a in [1,2,7,17,100,12345]:
            expected=-F(59*a*a+465*a+900,a*a*(a+3)*(a+4)*(a+5))
            self.assertEqual(source(a)-F(15,a*a),expected)
            self.assertLess(expected,0)
    def test_exact_minimum_action(self):
        self.assertEqual(energy((F(1),F(0)),F(0)),F(253,126))
        self.assertEqual(energy((F(0),F(0)),F(47,15)),F(94987,28350))
        for n in [1,2,4,8,19]:
            a=8*n-7
            self.assertEqual(energy((F(0),F(0)),source(a)),F(43,126)*source(a)**2)
            self.assertLess(energy((F(0),F(0)),source(a)),energy((F(0),F(0)),F(15,a*a)))

if __name__=='__main__': unittest.main()

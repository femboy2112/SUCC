"""Exact rational tests for a restricted observational Lorentz/energy-tensor model.

Mathematical finite models only, not a measurement of physical spacetime.
Uses Fraction throughout. c=1 and signature (-,+,+,+).
"""
from fractions import Fraction as F
from random import Random
import unittest
from itertools import combinations

Z = F(0)
ONE = F(1)
ETA = ((-ONE,Z,Z,Z),(Z,ONE,Z,Z),(Z,Z,ONE,Z),(Z,Z,Z,ONE))

def mm(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), Z)
                       for j in range(len(b[0]))) for i in range(len(a)))

def tr(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))

def bform(mat,vec,other=None):
    other = vec if other is None else other
    return sum((vec[i]*mat[i][j]*other[j] for i in range(len(vec)) for j in range(len(other))), Z)

def normalize_reader(tensor,spatial):
    """Energy density of the unit timelike observer in direction (1, spatial)."""
    p = tuple(map(F,spatial))
    speed2=sum((v*v for v in p), Z)
    if speed2 >= ONE:
        raise ValueError('observer velocity must be timelike')
    w=(ONE,)+p
    return bform(tensor,w)/(ONE-speed2)

def ten_readings(tensor,s=F(1,3)):
    if not Z < s or 2*s*s >= ONE:
        raise ValueError('choose 0<s and 2s^2<1')
    result={('rest',):normalize_reader(tensor,(0,0,0))}
    for i in range(3):
        for sign in (-1,1):
            vec=[Z]*3;vec[i]=sign*s
            result[('axis',i,sign)]=normalize_reader(tensor,vec)
    for i,j in combinations(range(3),2):
        vec=[Z]*3;vec[i]=vec[j]=s
        result[('pair',i,j)]=normalize_reader(tensor,vec)
    assert len(result)==10
    return result

def reconstruct_tensor(readings,s=F(1,3)):
    """Inverse of 10 density measurements; no physical tensor interpretation assumed."""
    T=[[Z for _ in range(4)] for _ in range(4)]
    T[0][0]=readings[('rest',)]
    for i in range(3):
        qp=(ONE-s*s)*readings[('axis',i,1)]
        qm=(ONE-s*s)*readings[('axis',i,-1)]
        T[0][i+1]=T[i+1][0]=(qp-qm)/(4*s)
        T[i+1][i+1]=((qp+qm)/2-T[0][0])/(s*s)
    for i,j in combinations(range(3),2):
        q=(ONE-2*s*s)*readings[('pair',i,j)]
        tij=(q-T[0][0]-2*s*(T[0][i+1]+T[0][j+1])
             -s*s*(T[i+1][i+1]+T[j+1][j+1]))/(2*s*s)
        T[i+1][j+1]=T[j+1][i+1]=tij
    return tuple(tuple(row) for row in T)

def lambda_boost():
    """Rational 1+1 Lorentz boost with half-rapidity tanh(theta/2)=1/2."""
    return ((F(5,3),-F(4,3)),(-F(4,3),F(5,3)))

def boost4():
    g,h=F(5,3),F(4,3)
    return ((g,-h,Z,Z),(-h,g,Z,Z),(Z,Z,ONE,Z),(Z,Z,Z,ONE))

def inv_boost4():
    g,h=F(5,3),F(4,3)
    return ((g,h,Z,Z),(h,g,Z,Z),(Z,Z,ONE,Z),(Z,Z,Z,ONE))

def transform_covariant_tensor(T,Linv):
    return mm(tr(Linv),mm(T,Linv))

def hermitian_diag_spin_boost(v,r=F(3,2)):
    """SL(2,C) diagonal congruence: x,y fixed; t,z transformed."""
    t,x,y,z=map(F,v)
    plus = r*r*(t+z)
    minus = (t-z)/(r*r)
    return ((plus+minus)/2,x,y,(plus-minus)/2)

def minkowski_norm(v):
    return -v[0]**2+sum((w*w for w in v[1:]),Z)

def matrix_rank(rows):
    A=[list(map(F,row)) for row in rows]
    if not A:return 0
    nr,nc=len(A),len(A[0]); pivot=0
    for c in range(nc):
        ix=next((i for i in range(pivot,nr) if A[i][c]),None)
        if ix is None:continue
        A[pivot],A[ix]=A[ix],A[pivot]
        k=A[pivot][c]
        A[pivot]=[q/k for q in A[pivot]]
        for i in range(nr):
            if i!=pivot and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[pivot][j] for j in range(nc)]
        pivot+=1
        if pivot==nr:break
    return pivot

def density_design(s=F(1,3)):
    w=[(ONE,Z,Z,Z)]
    for i in range(3):
        for sign in (-1,1):
            x=[Z,Z,Z];x[i]=sign*s
            w.append((ONE,*x))
    for i,j in combinations(range(3),2):
        x=[Z,Z,Z];x[i]=x[j]=s
        w.append((ONE,*x))
    out=[]
    for v in w:
        row=[v[i]*v[i] for i in range(4)]
        row.extend(2*v[i]*v[j] for i,j in combinations(range(4),2))
        out.append(row)
    return out

class OperationalGRChecks(unittest.TestCase):
    def test_null_clock_reconstruction(self):
        # g=[[a,b],[b,d]]. Null at (1,+1), (1,-1), clock g(e0,e0)=-1.
        a=-ONE
        # q_+ = a+2b+d=0; q_- = a-2b+d=0 => b=0,d=-a
        b=Z;d=-a
        self.assertEqual(a+2*b+d,Z)
        self.assertEqual(a-2*b+d,Z)
        self.assertEqual((a,b,d),(-ONE,Z,ONE))
        # One null direction + clock is insufficient; a one-parameter family remains.
        b=F(1,4);d=ONE-2*b
        self.assertEqual(a+2*b+d,Z)
        self.assertNotEqual(a-2*b+d,Z)
        self.assertLess(a*d-b*b,Z)  # Still Lorentz signature
    def test_lorentz_boost_invariance(self):
        L=lambda_boost();eta=((-ONE,Z),(Z,ONE))
        self.assertEqual(mm(tr(L),mm(eta,L)),eta)
        self.assertEqual(L[0][0]**2-L[0][1]**2,ONE)
    def test_hermitian_determinant_invariance(self):
        rng=Random(1114)
        for _ in range(99):
            v=tuple(F(rng.randrange(-12,13),rng.randrange(1,9)) for i in range(4))
            self.assertEqual(minkowski_norm(hermitian_diag_spin_boost(v)),minkowski_norm(v))
    def test_stress_energy_tomography(self):
        self.assertEqual(matrix_rank(density_design()),10)
        for removed in range(10):
            mat=density_design()
            del mat[removed]
            self.assertEqual(matrix_rank(mat),9) # each observer essential for generic reconstruction
        rng=Random(2006)
        for _ in range(80):
            T=[[Z]*4 for _ in range(4)]
            for i in range(4):
                for j in range(i,4):
                    T[i][j]=T[j][i]=F(rng.randrange(-21,22),rng.randrange(1,11))
            T=tuple(map(tuple,T))
            self.assertEqual(reconstruct_tensor(ten_readings(T)),T)
    def test_observer_covariance(self):
        T=((F(10),F(2),F(-1),F(3)),(F(2),F(4),F(1),F(-2)),
           (F(-1),F(1),F(5),Z),(F(3),F(-2),Z,F(6)))
        L=boost4();Li=inv_boost4()
        self.assertEqual(mm(tr(L),mm(ETA,L)),ETA)
        Tp=transform_covariant_tensor(T,Li)
        rng=Random(317)
        for _ in range(40):
            w=(ONE,)+tuple(F(rng.randrange(-2,3),12) for _ in range(3))
            wp=tuple(sum((L[i][j]*w[j] for j in range(4)),Z) for i in range(4))
            self.assertEqual(minkowski_norm(w),minkowski_norm(wp))
            self.assertEqual(bform(T,w)/(-minkowski_norm(w)),bform(Tp,wp)/(-minkowski_norm(wp)))
    def test_scalar_field_stress_energy(self):
        # Stress from S_phi = -int sqrt(-g)(1/2 g^-1(dphi,dphi)+V).
        derivative=(F(2),F(1),Z,Z)
        pot=F(1,4)
        kin=bform(ETA,derivative)
        Lagrangian=-(kin/F(2)+pot)
        tensor=tuple(tuple(derivative[i]*derivative[j]+ETA[i][j]*Lagrangian
                           for j in range(4)) for i in range(4))
        self.assertEqual(kin,F(-3))
        self.assertEqual(tensor[0][0],F(11,4))
        self.assertEqual(tensor[1][1],F(9,4))
        self.assertEqual(tensor[0][1],F(2))
    def test_conformal_ambiguity(self):
        # On eta<0, g'=a(eta)^2 * eta, a=-1/(H*eta): same cones,
        # but 4D Ricci scalar changes from 0 to 12 H^2.
        # Algebraic identity R=6 a''/a^3, evaluated exactly at eta=-2,H=3/5.
        h=F(3,5);tm=F(-2)
        a=-ONE/(h*tm)
        second=-2/(h*tm**3)
        R=6*second/(a**3)
        self.assertEqual(R,12*h*h)
        # Same g-null condition: multiplying by a^2 leaves zeros invariant.
        for v in ((ONE,ONE,Z,Z),(ONE,Z,ONE,Z),(ONE,Z,Z,ONE),(ONE,Z,Z,Z)):
            self.assertEqual(minkowski_norm(v)==Z, a*a*minkowski_norm(v)==Z)

if __name__=='__main__':
    unittest.main(verbosity=2)

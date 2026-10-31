"""Exact graph-wave and original-BBP source controls for the interaction-curvature proposal.

Research ONLY: a declared observer/carrier coupling, not physical GR or pi normality.
"""
from fractions import Fraction as F
from math import sin, cos, asin, sqrt, pi
import unittest

POLES=((4,0),(-2,3),(-1,4),(-1,5))
C2=F(1,4)
EPS=F(1,4)

def R(a):
    a=F(a)
    return sum((F(c)/(a+s) for c,s in POLES),F(0))

def kappa(a):
    a=F(a)
    m=-a*(-sum((F(c)/(a+s)**2 for c,s in POLES),F(0)))/R(a)
    return m/2

def L(u,w):
    n=len(u)
    return [w[i]*(u[i]-u[(i+1)%n])+w[(i-1)%n]*(u[i]-u[(i-1)%n])
            for i in range(n)]

def dot(u,v):
    return sum((x*y for x,y in zip(u,v)),F(0))

def step(u_prev,u,w,force=None):
    if force is None: force=[F(0)]*len(u)
    Lu=L(u,w)
    return [2*u[i]-u_prev[i]-C2*Lu[i]+force[i] for i in range(len(u))]

def E(u,v,w):
    d=[b-a for a,b in zip(u,v)]
    return dot(d,d)/2+C2*dot(u,L(v,w))/2

class InteractionCurvatureWave(unittest.TestCase):
    def test_original_four_poles_and_tangent(self):
        for a in (9,17,73,256):
            self.assertGreater(R(a),0)
            self.assertGreater(kappa(a),F(1,2))
            self.assertLess(kappa(a),1)
        a=2**18
        self.assertLess(abs(float(a*(kappa(a)-1)+F(59,30))),1e-4)

    def test_same_support_different_ollivier_curvature(self):
        q=F(1,4)
        for p in (F(1,4),F(1,2)):
            wasserstein=abs(1-p-q)+q
            self.assertEqual(1-wasserstein,p)

    def test_pure_frame_vs_coupled_plaquette(self):
        eta=[F(0),F(1),F(3)]
        a=73;k=kappa(a)
        for t in (0,1):
            alpha=eta[t+1]-eta[t]
            # Pure gauge: A_x(t)=k*eta_t, A_t(t,x)=k*x*alpha
            flat=k*alpha-(k*(8+1)*alpha-k*8*alpha)
            self.assertEqual(flat,0)
            # Coupled link with A_t=0: F_tx=k*alpha, with reference 1*alpha
            self.assertEqual(k*alpha-alpha,(k-1)*alpha)
            self.assertNotEqual((k-1)*alpha,0)
            # Gauge change shifts spatial link to zero, preserves lifted loop
            self.assertEqual(k*alpha,-(-k*alpha*(8+1))+(-k*alpha*8))

    def test_exact_energy_static(self):
        n=13;w=[F(1)]*n
        a=[F((i*i)%7) for i in range(n)]
        b=[F((i*i+i)%11) for i in range(n)]
        value=None
        for _ in range(8):
            z=step(a,b,w)
            now=E(b,z,w)
            if value is None:value=now
            else:self.assertEqual(now,value)
            a,b=b,z

    def test_dynamic_edge_work_balance(self):
        n=13;w0=[F(1)]*n;w1=w0.copy();w1[5]+=F(1,6)
        a=[F(i*i%7) for i in range(n)]
        b=[F((i*i+i)%11) for i in range(n)]
        force=[F(0)]*n;force[5]=F(1,3)
        z=step(a,b,w1,force)
        d=[x-y for x,y in zip(L(b,w1),L(b,w0))]
        rhs=dot([x-y for x,y in zip(z,a)],force)/2+C2*dot(a,d)/2
        self.assertEqual(E(b,z,w1)-E(a,b,w0),rhs)

    def test_source_curvature_launches_wave_with_finite_front(self):
        n=31;m=15;a=73
        u=[F(i) for i in range(n)]
        base=[F(1)]*n
        # Explicit declared curvature-to-conductance law, positive on all edges
        rel=kappa(a)-1
        curved=base.copy();curved[m]+=EPS*rel**2
        ref=step(u,u,base)
        actual=step(u,u,curved)
        pulse=[x-y for x,y in zip(actual,ref)]
        self.assertEqual([i for i,v in enumerate(pulse) if v],[m,m+1])
        self.assertEqual(pulse[m],C2*EPS*rel**2)
        self.assertEqual(pulse[m+1],-C2*EPS*rel**2)
        prev_ref,prev_actual=u,u
        for radius in range(1,5):
            new_ref=step(prev_ref,ref,base)
            new_actual=step(prev_actual,actual,base)
            d=[x-y for x,y in zip(new_actual,new_ref)]
            self.assertTrue(all(v==0 for i,v in enumerate(d)
                                if i<m-radius or i>m+1+radius))
            self.assertNotEqual(d[m-radius],0)
            self.assertNotEqual(d[m+1+radius],0)
            prev_ref,ref=ref,new_ref
            prev_actual,actual=actual,new_actual

    def test_59_squared_information_jet(self):
        a=2**18
        pulse=C2*EPS*(kappa(a)-1)**2
        # 3481/450 is previous four-pole chi-square coefficient.
        self.assertLess(abs(float(a*a*2*(kappa(a)-1)**2)-3481/450),0.0007)
        self.assertLess(abs(float(a*a*pulse)-float(C2*EPS*F(3481,900))),0.00003)

    def test_flat_wave_fourier_and_constant_null(self):
        for n in (8,16,32):
            for k in range(1,n):
                mode=2*pi*k/n
                omega=2*asin(sqrt(float(C2))*abs(sin(mode/2)))
                self.assertAlmostEqual(2*cos(omega)-2,
                                       -4*float(C2)*sin(mode/2)**2,places=12)
        u=[F(1)]*11
        w=[F(1)]*11;w[4]+=F(1,8)
        self.assertEqual(step(u,u,w),u)

if __name__=="__main__":
    unittest.main(verbosity=2)

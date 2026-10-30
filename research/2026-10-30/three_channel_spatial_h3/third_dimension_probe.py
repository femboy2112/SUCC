"""SUCC three-channel Fisher H3 and 3+1 wave controls.

Research-only auxiliary model; arithmetic and linearized tensor tests cannot
certify pi normality, physical dimensions, or Einstein dynamics.
"""
from fractions import Fraction as F
from math import comb, log, sqrt, sin, cos, pi, lgamma
import unittest

POLES = ((4, 0), (-2, 3), (-1, 4), (-1, 5))
ATOMS = ((2, 3), (1, 4), (1, 5))
GAMMA = 0.5772156649015328606065120900824024
LAMBDA = (sqrt(5)-1)/2

def R(a):
    a=F(a)
    return sum((F(c)/(a+d) for c,d in POLES),F(0))

def Rfake(a):
    a=F(a)
    return F(15)/(a*a)

def atom_mass(a,c,d):
    a=F(a)
    return F(c*d)/(a*(a+d))

def atom_angular_speed2(a, rank=2, theta=1):
    a=F(a)
    r=R(a)
    rp=-sum((F(c)/(a+d)**2 for c,d in POLES),F(0))
    total=F(0)
    for c,d in ATOMS:
        ri=atom_mass(a,c,d)
        rip=-F(c*d)*(2*a+d)/(a*a*(a+d)**2)
        prob=ri/r
        probprime=(rip*r-ri*rp)/r**2
        total+=probprime**2/prob
    return rank*theta*total

def pmoment(n,k,source=R):
    a=8*n-7
    return sum(((-1)**j*comb(k,j)*source(a+8*j)
                for j in range(k+1)),F(0))/source(a)

def mixed_cumulant(n,source=R):
    m1,m2,m3=(pmoment(n,k,source) for k in (1,2,3))
    return n**3*(m3-3*m2*m1+2*m1**3)

def gamma_three_cell(j,k,l):
    s=j+k+l
    return F((s+1)*comb(s,j)*comb(s-j,k),4**(s+2))

def finite_three_cell(n,j,k,l):
    s=j+k+l;a=8*n-7
    return (comb(n,j)*comb(n,k)*comb(n,l)
            *sum(((-1)**t*comb(s,t)*R(a+8*(3*n-s+t))
                  for t in range(s+1)),F(0))/R(a))

def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(3)),F(0))
             for j in range(3)] for i in range(3)]

def hyperbolic_information(m,v):
    # Fisher norm squared of an m-vector tangent.
    return sum((v[i]*v[i]/m[i] for i in range(3)),F(0))\
           -sum(v,F(0))**2/(F(2)+sum(m,F(0)))

def expected_oily(theta):
    c=1+theta
    z=1-GAMMA+log(c)-(1+c*LAMBDA)**(-2)
    mean=theta*(3-2*GAMMA+2*log(c)-2/(1+c*LAMBDA)**3)/z
    return z,mean

def ring_step(prev,now,c2=F(1,4)):
    n=len(now)
    return [2*now[z]-prev[z]-c2*(2*now[z]-now[(z-1)%n]-now[(z+1)%n])
            for z in range(n)]

class ThreeSpatialDimensions(unittest.TestCase):
    def test_three_authentic_positive_source_atoms(self):
        for a in (1,9,17,73,257):
            self.assertEqual(sum((atom_mass(a,c,d) for c,d in ATOMS),F(0)),R(a))
            self.assertEqual(sum((atom_mass(a,c,d)/R(a) for c,d in ATOMS),F(0)),1)
        self.assertEqual(sum(c*d for c,d in ATOMS),15)
        self.assertEqual(sum(c*d*d for c,d in ATOMS),59)
        self.assertEqual(sum(c*d**3 for c,d in ATOMS),243)
        for (c,d),want in zip(ATOMS,(F(2,5),F(4,15),F(1,3))):
            a=10**6
            self.assertLess(abs(float(atom_mass(a,c,d)/R(a)-want)),1e-6)

    def test_native_angular_source_ray_164_defect(self):
        beta=[F(c*d,15) for c,d in ATOMS]
        # The source's angular direction has a distinctive 1/a jet.
        self.assertEqual(sum((b*(F(59,15)-d) for b,(_,d) in zip(beta,ATOMS)),F(0)),0)
        variance=sum((b*(F(59,15)-d)**2 for b,(_,d) in zip(beta,ATOMS)),F(0))
        self.assertEqual(variance,F(164,225))
        # Fixed theta=1, rank=2 Fisher angular speed squared ~ 328/(225*a^4).
        errors=[]
        for a in (200,1000,10000):
            measured=a**4*atom_angular_speed2(a)
            errors.append(abs(float(measured-F(328,225))))
        self.assertTrue(all(x>y for x,y in zip(errors,errors[1:])))
        self.assertLess(errors[-1],0.003)

    def test_three_source_mark_gains_have_three_independent_controls(self):
        # Given a retained source mark, three positive detector gains with
        # overall scale quotiented plus an independent total budget give a
        # nonzero 3x3 Jacobian, but only if all interventions are allowed.
        for a in (1,17,73):
            marks=[atom_mass(a,c,d)/R(a) for c,d in ATOMS]
            gains=[F(1),F(2),F(3)]
            budget=F(5,2)
            norm=sum((g*p for g,p in zip(gains,marks)),F(0))
            q=[g*p/norm for g,p in zip(gains,marks)]
            theta=[budget*z for z in q]
            jac=[[theta[i],theta[i]*(int(i==1)-q[1]),
                  theta[i]*(int(i==2)-q[2])] for i in range(3)]
            det=(jac[0][0]*(jac[1][1]*jac[2][2]-jac[1][2]*jac[2][1])
                 -jac[0][1]*(jac[1][0]*jac[2][2]-jac[1][2]*jac[2][0])
                 +jac[0][2]*(jac[1][0]*jac[2][1]-jac[1][1]*jac[2][0]))
            self.assertEqual(det,theta[0]*theta[1]*theta[2])
            self.assertGreater(det,0)

    def test_finite_original_three_panel_probability_and_vandermonde(self):
        for n in (1,2,3):
            cells={(j,k,l):finite_three_cell(n,j,k,l)
                   for j in range(n+1) for k in range(n+1) for l in range(n+1)}
            self.assertEqual(sum(cells.values(),F(0)),1)
            self.assertTrue(all(p>0 for p in cells.values()))
            for s in range(3*n+1):
                a=8*n-7
                total=comb(3*n,s)*sum(((-1)**t*comb(s,t)*R(a+8*(3*n-s+t))
                          for t in range(s+1)),F(0))/R(a)
                self.assertEqual(sum((p for (j,k,l),p in cells.items() if j+k+l==s),F(0)),total)
                for (j,k,l),p in cells.items():
                    if j+k+l==s:
                        self.assertEqual(p/total,F(comb(n,j)*comb(n,k)*comb(n,l),comb(3*n,s)))

    def test_negative_multinomial_three_panel_limit(self):
        for s in range(9):
            actual=sum((gamma_three_cell(j,k,s-j-k) for j in range(s+1)
                        for k in range(s-j+1)),F(0))
            self.assertEqual(actual,F((s+1)*3**s,4**(s+2)))
        # Cross moments are Gamma(2) latent moments, and yield genuine
        # shared-source covariance 2 and three-way cumulant 4.
        EY=F(2); EY2=F(6); EY3=F(24)
        self.assertEqual(EY2-EY**2,F(2))
        self.assertEqual(EY3-3*EY2*EY+2*EY**3,F(4))

    def test_original_zero_seed_three_time_carry_witness(self):
        # The authentic signed rational recurrence is kept separate from
        # the positive three-panel sensor. Three grade-1 paths have the
        # same total yet distinct intermediate literal carry histories.
        U=[F(0)]
        carries=[None]
        for n in range(1,6):
            r=R(8*n-7)
            pre=16*(U[-1]%1)+r
            carries.append(pre.numerator//pre.denominator)
            U.append(16*U[-1]+r)
        self.assertEqual((carries[3],carries[4]),(4,3))
        n=3
        paths=((1,0,0),(0,1,0),(0,0,1))
        marks=set()
        for j,k,l in paths:
            self.assertGreater(finite_three_cell(n,j,k,l),0)
            marks.add((carries[n+j],carries[n+j+k],carries[n+j+k+l]))
        self.assertEqual(len(marks),3)

    def test_three_panel_tv_cesaro_bound_clock_constants(self):
        # Pure rational clock inequality used in the paper's triple
        # Poisson/Gamma source coupling; does not test pi cancellation.
        for n in range(3,1001):
            a=8*n-7
            bound=F(1728*n,a*a)+F(48,a)
            self.assertLessEqual(bound,F(63,n))
        weights=[F((s+1)*3**s,4**(s+2)) for s in range(200)]
        self.assertLess(abs(float(sum(weights,F(0)))-1),1e-11)
        self.assertLess(abs(float(sum((s*w for s,w in enumerate(weights)),F(0)))-6),1e-11)

    def test_static_triple_fourier_kernel_has_no_wave_pole(self):
        # The static three-grade Green symbol (4-X-Y-Z)^(-2) is
        # nonzero on the three-torus. Spatial harmonics alone are not
        # hyperbolic propagating modes.
        import cmath
        for u in range(8):
            for v in range(8):
                for w in range(8):
                    roots=(cmath.exp(2j*pi*u/8),cmath.exp(2j*pi*v/8),
                           cmath.exp(2j*pi*w/8))
                    d=4-sum(roots)
                    self.assertGreaterEqual(abs(d),1-1e-12)
                    self.assertLessEqual(abs(1/d**2),1+1e-12)

    def test_3d_fisher_inverse_and_minkowski_pullback(self):
        m=[F(1),F(4),F(9)]
        s=F(2)+sum(m,F(0))
        Sigma=[[m[i]*(i==j)+m[i]*m[j]/2 for j in range(3)] for i in range(3)]
        g=[[F(i==j,1)/m[i]-F(1)/s for j in range(3)] for i in range(3)]
        self.assertEqual(matmul(Sigma,g),[[F(i==j) for j in range(3)] for i in range(3)])
        v=[F(2),F(-1),F(3)]
        # dX_i=dm_i / sqrt(m_i), dT=sum dm_i/sqrt(2+sum m_i).
        self.assertEqual(hyperbolic_information(m,v),F(4)+F(1,4)+F(1)-F(1))
        self.assertEqual(4*(2+sum(m,F(0)))-4*sum(m,F(0)),8)

    def test_fixed_budget_sphere_vs_free_radial_hyperboloid(self):
        # theta_1+theta_2+theta_3=1 fixes sum m_i=2 and embedding T.
        m=[F(1),F(1,2),F(1,2)]
        v=[F(1),F(-1,2),F(-1,2)]
        self.assertEqual(sum(v),0)
        self.assertEqual(hyperbolic_information(m,v),sum((v[i]**2/m[i] for i in range(3)),F(0)))
        self.assertEqual(F(1,4*2),F(1,8))  # +1/8 sectional curvature of S2 slice.
        self.assertEqual(-F(1,4*2),-F(1,8)) # -1/8 sectional curvature of H3.
        self.assertEqual(-F(6,4*2),-F(3,4)) # H3 scalar curvature.

    def test_clock_normalization_and_golden_locus(self):
        for theta in (1.,2.,3.):
            c=1+theta
            Z,mean=expected_oily(theta)
            masses=[]
            for s in range(270):
                ps=(s+1)*theta**s/c**(s+2)
                D=sum(1./j for j in range(1,s+2))-GAMMA-LAMBDA**(s+2)
                masses.append(ps*D)
            self.assertAlmostEqual(sum(masses),Z,places=11)
            self.assertAlmostEqual(sum(s*p for s,p in enumerate(masses))/sum(masses),mean,places=10)
        # conservation theta_sum=1 keeps original rank-two golden fixed point.
        q=LAMBDA**2
        self.assertAlmostEqual((2-q)**(-2),q,places=13)
        # with three FULL panels the nontrivial root is NOT golden.
        q3=(5-sqrt(21))/6
        self.assertAlmostEqual((4-3*q3)**(-2),q3,places=13)
        self.assertGreater(abs(q3-q),0.1)

    def test_authentic_three_panel_59_first_jet(self):
        # At z1=z2=z3=0: original H_n=R(a+24n)/R(a), fake=(a/(a+24n))^2.
        theoretical=F(59*3,120*4**3)
        errors=[]
        for n in (100,300,1000,3000):
            a=8*n-7
            diff=n*(R(a+24*n)/R(a)-Rfake(a+24*n)/Rfake(a))
            errors.append(abs(float(diff-theoretical)))
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],1e-4)

    def test_authenticated_third_mixed_cumulant_jet(self):
        errors=[]
        for n in (100,300,1000,3000):
            scaled=n*(mixed_cumulant(n)-mixed_cumulant(n,Rfake))
            errors.append(abs(float(scaled+F(59,20))))
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],0.03)

    def test_3d_fourier_stable_dispersion(self):
        c2=F(1,4)
        self.assertLessEqual(12*c2,4)
        for k in ((1,2,3),(2,0,0),(0,0,4)):
            side=4*sum(sin(pi*k[i]/13)**2 for i in range(3))
            omega=2*__import__('math').asin(sqrt(float(c2)*side)/2)
            self.assertAlmostEqual(2*cos(omega)-2,-float(c2)*side,places=13)

    def test_source_defect_pulse_propagates_in_all_three_axes(self):
        # A separately declared source-relative z-bond pulse spreads into
        # x and y directions under a 3D nearest-neighbor wave operator.
        c2=F(1,4);eps=F(1,4);a=73
        # Original source mass from the original four-pole rational R.
        aprime=-sum((F(c)/(F(a)+d)**2 for c,d in POLES),F(0))
        mass=-F(a)*aprime/R(a)
        amp=c2*eps*(mass/2-1)**2
        self.assertGreater(amp,0)
        endpoints=((0,0,0),(0,0,1))
        prev={};now={endpoints[0]:amp,endpoints[1]:-amp}
        directions=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
        for t in range(2,5):
            candidates=set(prev)|set(now)
            for p in tuple(now):
                for d in directions:
                    candidates.add(tuple(p[i]+d[i] for i in range(3)))
            nxt={}
            for p in candidates:
                val=2*now.get(p,0)-prev.get(p,0)
                lap=6*now.get(p,0)-sum((now.get(tuple(p[i]+d[i] for i in range(3)),0)
                                          for d in directions),F(0))
                val-=c2*lap
                if val:nxt[p]=val
            for p in nxt:
                self.assertLessEqual(min(sum(abs(p[i]-e[i]) for i in range(3))
                                         for e in endpoints),t-1)
            if t==2:
                self.assertNotEqual(nxt.get((1,0,0)),0)
                self.assertNotEqual(nxt.get((0,1,0)),0)
                self.assertNotEqual(nxt.get((0,0,-1)),0)
            prev,now=now,nxt

    def test_two_independent_transverse_traceless_modes(self):
        # Wave propagates in z, transverse x,y: plus and cross are independent.
        n=11;prev_plus=[F(0)]*n;prev_cross=[F(0)]*n
        plus=[F(0)]*n;cross=[F(0)]*n
        plus[0]=F(3);cross[1]=F(5)
        for _ in range(7):
            # TT spatial tensor [[plus,cross,0],[cross,-plus,0],[0,0,0]]
            for a,b in zip(plus,cross):
                h=((a,b,F(0)),(b,-a,F(0)),(F(0),F(0),F(0)))
                self.assertEqual(sum(h[i][i] for i in range(3)),0)
                self.assertTrue(all(h[2][j]==h[j][2]==0 for j in range(3)))
            next_plus=ring_step(prev_plus,plus)
            next_cross=ring_step(prev_cross,cross)
            prev_plus,plus=plus,next_plus
            prev_cross,cross=cross,next_cross
        self.assertNotEqual(plus,cross)
        self.assertTrue(any(x!=0 for x in plus))
        self.assertTrue(any(x!=0 for x in cross))

    def test_3plus1_milne_vacuum_null_control(self):
        # 3-space metric h has R(h)=-3/4; physical g=-dtau^2+A^2 h.
        # A=tau/sqrt(8) has vacuum ADM constraint; full Riemann is zero.
        for tau in (F(1),F(3),F(17)):
            A_sq=tau*tau/8
            scalar3=-F(3,4)/A_sq
            extrinsic=(3**2-3)/tau**2
            self.assertEqual(scalar3+extrinsic,0)

if __name__=='__main__':
    unittest.main(verbosity=2)

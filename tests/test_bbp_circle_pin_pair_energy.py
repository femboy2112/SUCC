"""Circle-origin gauge, exact BBP rational pair-coercivity, null controls.

Original source/seed only for finite certificates; algebraic gauge tests have
independent toy endpoints. No full pi normality claim or asymptotic inference.
"""
import unittest
from fractions import Fraction as F
from functools import lru_cache


def torus(x):
    r = F(x) % 1
    return min(r, 1 - r)


def forcing(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


@lru_cache(maxsize=None)
def terminal(N):
    U = F(0)
    for n in range(1,N+1):
        U = 16*U + forcing(n)
    return U


def connection(origin,n,h=1):
    return (16**h*origin(n)-origin(n+h)) % 1


def pair_energy(B):
    U = terminal(2*B)
    views = [U/16**k for k in range(1,B+1)]
    return sum((torus(views[i]-views[j])**2
                for i in range(B) for j in range(i+1,B)),F(0))/B**2


def rho(B):
    return F(8,225*B)*forcing(2*B+1)


def gcadd(u,v): return (u[0]+v[0],u[1]+v[1])
def gcmul(u,v):return (u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def gcconj(u):return (u[0],-u[1])
def gcsub(u,v):return (u[0]-v[0],u[1]-v[1])
def gcnorm(u):return u[0]**2+u[1]**2
ONE=(F(1),F(0));ZERO=(F(0),F(0))
I=(F(0),F(1)); MINUS_ONE=(F(-1),F(0)); MINUS_I=(F(0),F(-1))
ROT=(ONE,I,MINUS_ONE,MINUS_I)


def mean_phases(zs):
    return (sum((z[0] for z in zs),F(0))/len(zs),
            sum((z[1] for z in zs),F(0))/len(zs))


def pair_variance(zs):
    N=len(zs)
    return sum((gcnorm(gcsub(zs[i],zs[j]))
                for i in range(N) for j in range(i+1,N)),F(0))/N**2


def qfilter(v):
    """The BBP 6-tap impulse mask on a periodic auxiliary lag cycle."""
    taps=(4,0,0,-2,-1,-1)
    return tuple(
        (sum((taps[j]*v[(n+j)%len(v)][0] for j in range(6)),F(0)),
         sum((taps[j]*v[(n+j)%len(v)][1] for j in range(6)),F(0)))
        for n in range(len(v)))


class CircleOriginGaugeTests(unittest.TestCase):
    def test_15_exact_constant_origins_preserve_unmodified_radix_law(self):
        roots={F(j,15) for j in range(15)}
        self.assertEqual(len(roots),15)
        self.assertTrue(all(((16*a-a)%1)==0 for a in roots))
        self.assertTrue(all(((16*a-a)%1)!=0 for a in (F(1,14),F(1,4),F(1,7))))
        self.assertEqual({F(j,255) for j in range(255) if (15*F(j,255))%1==0},roots)

    def test_arbitrary_moving_chart_requires_connection(self):
        a=lambda n:F(n*n+3*n+1,37)%1
        for x in (F(1,7),F(4,17),F(1,15)):
            for n in range(0,11):
                phi=lambda i:(16**i*x-a(i))%1
                self.assertEqual(phi(n+1),(16*phi(n)+connection(a,n))%1)
                for h in (1,2,3):
                    self.assertEqual(phi(n+h),(16**h*phi(n)+connection(a,n,h))%1)

    def test_connection_cocycle_is_path_compositional(self):
        for a in (lambda n:F(n*n,37),lambda n:F(3*n+7,15),lambda n:F(1,19)):
            for n in range(4):
                for h in range(1,5):
                    for k in range(1,4):
                        self.assertEqual(connection(a,n,h+k),
                                         (16**k*connection(a,n,h)+connection(a,n+h,k))%1)

    def test_exactly_tracking_chart_is_oracle_not_free_signal(self):
        x=F(1,7)
        a=lambda n:16**n*x
        self.assertTrue(all(((16**n*x-a(n))%1)==0 for n in range(12)))
        self.assertTrue(all(connection(a,n)==0 for n in range(12)))
        # Information is in the source-correlated initial origin a(0)=x.
        self.assertEqual(a(0),x)

    def test_source_null_section_survives_moving_circle_zero(self):
        U=F(0);F0=F(0)
        a=lambda n:F(n*n+2,37)
        for n in range(0,23):
            self.assertEqual(U,F0)
            self.assertEqual((U-a(n))-(F0-a(n)),0)
            if n<22:
                shifted_forcing=forcing(n+1)+16*a(n)-a(n+1)
                self.assertEqual((16*(U-a(n))+shifted_forcing),
                                 16*U+forcing(n+1)-a(n+1))
                U=16*U+forcing(n+1)
                F0=16*F0+forcing(n+1)

    def test_global_rotation_keeps_pair_variance_not_anchor_energy(self):
        zs=(ONE,I,MINUS_ONE,I)
        w=mean_phases(zs)
        expected=1-gcnorm(w)
        self.assertEqual(pair_variance(zs),expected)
        anchor=1-w[0]
        self.assertEqual(anchor,F(1))
        for rot in ROT:
            transformed=tuple(gcmul(rot,z) for z in zs)
            self.assertEqual(pair_variance(transformed),expected)
            self.assertEqual(gcnorm(mean_phases(transformed)),gcnorm(w))
        self.assertNotEqual(1-mean_phases(tuple(gcmul(I,z) for z in zs))[0],anchor)

    def test_fixed_nonunit_orbit_has_R0_but_zero_pair_energy(self):
        x=F(1,15)
        self.assertTrue(all((16**n*x)%1==x for n in range(1,30)))
        zs=(I,)*5  # a nonunit constant phase; exact Gaussian-rational witness
        self.assertEqual(pair_variance(zs),0)
        self.assertEqual(gcnorm(mean_phases(zs)),1)
        self.assertGreater(1-mean_phases(zs)[0],0)

    def test_original_zero_seed_rational_pair_certificates(self):
        for B in (4,8,16,32,64,128):
            c=pair_energy(B)
            self.assertGreater(c,0)
            self.assertLessEqual(c,F(1,8))
            lb=8*c-rho(B)
            self.assertGreater(lb,F(1,5),f'B={B} exact original BBP pair lower')
            self.assertLess(lb,1)

    def test_pair_certificate_is_same_under_common_terminal_origin(self):
        for B in (2,4,8,16):
            U=terminal(2*B)
            vals=[U/16**k for k in range(1,B+1)]
            for alpha in (F(0),F(1,7),F(3,15),F(1,4)):
                shifted=[x-alpha for x in vals]
                left=sum((torus(vals[i]-vals[j])**2
                          for i in range(B) for j in range(i+1,B)),F(0))/B**2
                right=sum((torus(shifted[i]-shifted[j])**2
                           for i in range(B) for j in range(i+1,B)),F(0))/B**2
                self.assertEqual(left,right)

    def test_cyclic_lag_filter_conjugacy_preserves_null_kernel(self):
        N=7
        f=(ONE,I,MINUS_ONE,MINUS_I,ONE,MINUS_I,I)
        g=tuple(ROT[n%4] for n in range(N))
        gf=tuple(gcmul(g[n],f[n]) for n in range(N))
        # Independently implement S^g=G^-1 S G by a local one-step law.
        def shift_g(v):
            return tuple(gcmul(gcconj(g[n]),gcmul(g[(n+1)%N],v[(n+1)%N]))
                         for n in range(N))
        orbit=[f]
        for _ in range(5):
            orbit.append(shift_g(orbit[-1]))
        direct=tuple(gcsub(gcsub((4*f[n][0],4*f[n][1]),
                                   (2*orbit[3][n][0],2*orbit[3][n][1])),
                            gcadd(orbit[4][n],orbit[5][n])) for n in range(N))
        conjugated=tuple(gcmul(gcconj(g[n]),qfilter(gf)[n]) for n in range(N))
        self.assertEqual(conjugated,direct)
        self.assertNotEqual(direct,(ZERO,)*N)
        # A physical constant mode transports into a gauge-dependent kernel.
        one=(ONE,)*N
        self.assertTrue(all(x==ZERO for x in qfilter(one)))
        source_gauge_kernel=tuple(gcmul(gcconj(g[n]),ONE) for n in range(N))
        self.assertTrue(all(x==ZERO for x in
                            (gcmul(gcconj(g[n]),qfilter(tuple(gcmul(g[m],source_gauge_kernel[m])
                                             for m in range(N)))[n]) for n in range(N))))

if __name__=='__main__':unittest.main()

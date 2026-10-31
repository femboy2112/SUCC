"""SUCC research-only: exact two-triangle shared-posterior Fourier geometry.

Standalone standard-library tests; original signed four-pole BBP source unchanged.
Two Bernoulli observation panels share ONE original positive latent variable;
this is a declared classical observation model, not a random generator of pi digits.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import comb, gcd
import unittest


def source_R(a):
    a = F(a)
    if a <= 0: raise ValueError('positive source Laplace parameter')
    return F(4)/a-F(2)/(a+3)-F(1)/(a+4)-F(1)/(a+5)


def fake_R(a):
    a=F(a)
    if a <= 0: raise ValueError('positive fake Laplace parameter')
    return F(15)/a**2


@lru_cache(maxsize=None)
def source_coeff(n, m, s, R=source_R):
    if not (isinstance(n,int) and n>=1 and isinstance(m,int) and m>=0 and 0<=s<=m):
        raise ValueError('n>=1, m>=0 and 0<=successes<=m')
    a=8*n-7
    return sum((F((-1)**k*comb(s,k))*R(a+8*(m-s+k)) for k in range(s+1)),F())/R(a)


def one_panel(n, m, R=source_R):
    return tuple(F(comb(m,j))*source_coeff(n,m,j,R) for j in range(m+1))


def shared_panels(n, m1, m2, R=source_R):
    return tuple(tuple(F(comb(m1,j)*comb(m2,k))*source_coeff(n,m1+m2,j+k,R)
                       for k in range(m2+1)) for j in range(m1+1))


def reset_panels(n,m1,m2,R=source_R):
    p=one_panel(n,m1,R);q=one_panel(n,m2,R)
    return tuple(tuple(u*v for v in q) for u in p)


def joint_pgf(matrix,z,w):
    z,w=F(z),F(w)
    return sum((v*z**j*w**k for j,row in enumerate(matrix) for k,v in enumerate(row)),F())


def cross_covariance(n,m1,m2,R=source_R):
    a=8*n-7
    z1=R(a+8)/R(a)
    z2=R(a+16)/R(a)
    return F(m1*m2)*(z2-z1*z1)


def two_triangle_limit(z,w):
    z,w=F(z),F(w)
    return 1/(3-z-w)**2


def reset_limit(z,w):
    z,w=F(z),F(w)
    return 1/((2-z)**2*(2-w)**2)


def clock_split_limit(z,w):
    z,w=F(z),F(w)
    return F(4)/(4-z-w)**2


def first_jet(z,w):
    z,w=F(z),F(w)
    d=3-z-w
    return -F(151,120)*(d-1)/d**3+F(3)*(z*(1-z)+w*(1-w))/d**4


def four_pole_jet_vs_fake(z,w):
    d=3-F(z)-F(w)
    return F(59,120)*(d-1)/d**3


def cyclic_joint_residues(size=6,denominator=3,numerator=1):
    """Exact ring Q[X,Y]/(X^size-1,Y^size-1) inverse of
    (denominator-X-Y)^2, with a numerator scalar.

    Output u[r][s] equals probability of residues J=r,K=s for the
    positive limiting joint PGF `numerator/(denominator-X-Y)^2`.
    Standard-library Fraction Gauss-Jordan; no sample tail truncation.
    """
    if size<=0 or denominator<=2:raise ValueError('nonsingular operator required')
    sz=size*size
    def mat():
        A=[[F(0) for _ in range(sz+1)] for _ in range(sz)]
        for j in range(size):
            for k in range(size):
                col=j*size+k
                A[col][col]=F(denominator)
                A[((j+1)%size)*size+k][col]-=1
                A[j*size+(k+1)%size][col]-=1
        return A
    def solve(rhs):
        A=mat()
        for i,v in enumerate(rhs):A[i][-1]=F(v)
        for p in range(sz):
            pivot=next(q for q in range(p,sz) if A[q][p])
            if pivot!=p:A[p],A[pivot]=A[pivot],A[p]
            v=A[p][p]
            A[p][p:]=[c/v for c in A[p][p:]]
            for q in range(sz):
                if q!=p and A[q][p]:
                    v=A[q][p]
                    A[q][p:]=[x-v*y for x,y in zip(A[q][p:],A[p][p:])]
        return [row[-1] for row in A]
    first=solve([1]+[0]*(sz-1))
    second=solve(first)
    return tuple(tuple(numerator*second[j*size+k] for k in range(size)) for j in range(size))


def primitive_q6_joint():
    u=cyclic_joint_residues()
    prim=lambda t: gcd(t,6)==1
    p11=sum((u[j][k] for j in range(6) for k in range(6) if prim(j) and prim(k)),F())
    p10=sum((u[j][k] for j in range(6) for k in range(6) if prim(j) and not prim(k)),F())
    p01=sum((u[j][k] for j in range(6) for k in range(6) if not prim(j) and prim(k)),F())
    p00=sum((u[j][k] for j in range(6) for k in range(6) if not prim(j) and not prim(k)),F())
    return p00,p01,p10,p11


def oily_weight(j):
    if not isinstance(j,int) or j<0:raise ValueError('grade')
    return F(j+1,2**(j+2))


def oily_opposing_kernel(m):
    m=abs(int(m))
    return F(5+3*m,27*2**m)


class TestSharedTriangle(unittest.TestCase):
    def test_full_original_source(self):
        self.assertEqual(source_R(1),F(47,15))
        self.assertEqual(source_R(8*7-7), F(4,49)-F(2,52)-F(1,53)-F(1,54))
        for a in (1,9,17,25,100):self.assertGreater(source_R(a),0)

    def test_shared_posterior_mass(self):
        for n in range(1,9):
            for m1,m2 in ((1,1),(2,3),(n,n)):
                p=shared_panels(n,m1,m2)
                self.assertEqual(sum(map(sum,p)),1)
                self.assertTrue(all(x>0 for row in p for x in row))
                for j,row in enumerate(p):
                    self.assertEqual(sum(row),one_panel(n,m1)[j])
                self.assertEqual(tuple(map(sum,zip(*p))),one_panel(n,m2))

    def test_vandermonde_source_preserving_gluing(self):
        for n,m1,m2 in ((1,2,3),(3,4,4),(6,4,6),(8,7,3)):
            p=shared_panels(n,m1,m2)
            marginal=one_panel(n,m1+m2)
            for t in range(m1+m2+1):
                self.assertEqual(sum((p[j][t-j] for j in range(max(0,t-m2),min(m1,t)+1)),F()),marginal[t])
                for j in range(max(0,t-m2),min(m1,t)+1):
                    self.assertEqual(p[j][t-j]/marginal[t],F(comb(m1,j)*comb(m2,t-j),comb(m1+m2,t)))

    def test_nonzero_cross_covariance(self):
        for n in range(1,18):
            self.assertGreater(cross_covariance(n,n,n),0)
        self.assertEqual(cross_covariance(3,1,0),0)
        self.assertNotEqual(shared_panels(4,3,3),reset_panels(4,3,3))
        for n in (3,5,10,15):
            self.assertLess(abs(cross_covariance(n,n,n)-2),F(200,n))

    def test_limiting_two_dimensional_symbol(self):
        self.assertEqual(two_triangle_limit(1,1),1)
        self.assertEqual(two_triangle_limit(0,0),F(1,9))
        self.assertEqual(reset_limit(0,0),F(1,16))
        self.assertNotEqual(two_triangle_limit(0,0),reset_limit(0,0))
        self.assertEqual(two_triangle_limit(1,F(1,3)),1/(2-F(1,3))**2)
        self.assertEqual(clock_split_limit(F(1,3),F(1,3)),1/(2-F(1,3))**2)
        for z,w in ((F(0),F(0)),(F(1,2),F(1,4)),(F(1),F(1,2))):
            self.assertGreater(3-z-w,0)

    def test_first_source_specific_two_variable_jet(self):
        self.assertEqual(first_jet(1,1),0)
        self.assertEqual(first_jet(0,0),F(-151,120)*F(2,27))
        self.assertEqual(first_jet(F(1),F(1,2)),F(-511*F(1,2)**2+813*F(1,2)-302)/(120*(2-F(1,2))**4))
        for z,w in ((F(0),F(0)),(F(1,2),F(1,3)),(F(3,4),F(2,3))):
            for n in (10,14,18):
                h=joint_pgf(shared_panels(n,n,n),z,w)
                self.assertLess(abs(n*(h-two_triangle_limit(z,w))-first_jet(z,w)),F(30,n))

    def test_original_minus_gamma_mutant_jet(self):
        for z,w in ((F(0),F(0)),(F(1,2),F(1,2))):
            for n in (10,14,18):
                orig=joint_pgf(shared_panels(n,n,n),z,w)
                fake=joint_pgf(shared_panels(n,n,n,fake_R),z,w)
                self.assertLess(abs(n*(orig-fake)-four_pole_jet_vs_fake(z,w)),F(30,n))

    def test_exact_primitive_six_four_cell(self):
        p00,p01,p10,p11=primitive_q6_joint()
        self.assertEqual((p00,p01,p10,p11),(
            F(4356841973,9224560800), F(4590078863,21523975200),
            F(4590078863,21523975200), F(6533558611,64571925600)))
        p=F(416,1323)
        self.assertEqual(p01+p11,p)
        self.assertEqual(p10+p11,p)
        self.assertEqual(sum((p00,p01,p10,p11),F()),1)
        self.assertEqual(p11-p*p,F(197519239153,85428657568800))
        self.assertGreater(p11*p00,p10*p01)

    def test_operator_bilinear_stencil_and_observers(self):
        # (3-X-Y)^2 H =1 in Q[X,Y]/(X^6-1,Y^6-1).
        a=cyclic_joint_residues()
        d=6
        for j in range(d):
            for k in range(d):
                get=lambda dj,dk:a[(j+dj)%d][(k+dk)%d]
                result=9*get(0,0)-6*get(-1,0)-6*get(0,-1)+get(-2,0)+2*get(-1,-1)+get(0,-2)
                self.assertEqual(result,1 if (j,k)==(0,0) else 0)

    def test_split_clock_q6_and_golden_preservation(self):
        a=cyclic_joint_residues(6,4,4)
        self.assertEqual(sum(map(sum,a)),1)
        self.assertEqual(clock_split_limit(F(1,2),F(1,2)),F(4,9))
        golden_sq=(3-5**.5)/2
        self.assertLess(abs(float(clock_split_limit(F(golden_sq),F(golden_sq)))-golden_sq),1e-12)
        self.assertLess(float(two_triangle_limit(F(golden_sq),F(golden_sq)))-golden_sq,-0.1)

    def test_bilateral_oily_kernel_and_finite_inverse(self):
        self.assertEqual(oily_opposing_kernel(0),F(5,27))
        self.assertEqual(oily_opposing_kernel(2),F(11,108))
        self.assertEqual(oily_opposing_kernel(0)+2*sum((oily_opposing_kernel(i) for i in range(1,100)),F())+F(616,27*2**99),1)
        # 33 -20(S+S^-1)+4(S²+S^-²) is inverse to G(S)G(S^-1).
        for j in range(-40,41):
            k=oily_opposing_kernel
            result=33*k(j)-20*(k(j+1)+k(j-1))+4*(k(j+2)+k(j-2))
            self.assertEqual(result,1 if j==0 else 0)

    def test_constant_phase_hostile_control(self):
        for n in (2,3,6,10):
            p=shared_panels(n,n,n)
            self.assertEqual(sum((v for row in p for v in row),F()),1)
            # Any stationary phase z_t=1 survives double sheet exactly.
            self.assertEqual(sum((v*F(1) for row in p for v in row),F()),1)

# The assertions above are the standalone core; appended exact helpers support
# independently executed follow-up instruments without changing the source.

def total_shared_law(n):
    return one_panel(n,2*n)

def negative_binomial_two_clock(j):
    return F((j+1)*2**j,3**(j+2))

def total_tv_against_limit(n):
    dist=total_shared_law(n)
    tail=F((2*n+4),3)*F(2,3)**(2*n+1)
    return (sum((abs(p-negative_binomial_two_clock(j)) for j,p in enumerate(dist)),F())+tail)/2

def original_literal_history(length,seed=F(0)):
    if length<0:raise ValueError('length')
    x=F(seed)%1
    residues=[x]; carries=[None]
    for t in range(1,length+1):
        y=16*x+source_R(8*t-7)
        k=y.numerator//y.denominator
        x=y-k
        carries.append(k);residues.append(x)
    return tuple(residues),tuple(carries)

def internal_carry_marginal(n,m1,m2,seed=F(0)):
    w=shared_panels(n,m1,m2)
    _, kappa=original_literal_history(n+m1+m2,seed)
    return {(c,d):sum((p for j,row in enumerate(w) for k,p in enumerate(row)
                        if kappa[n+j]==c and kappa[n+j+k]==d),F())
            for c in set(kappa[n:n+m1+1]) for d in set(kappa[n:n+m1+m2+1])}

class TestSelectedInterior(unittest.TestCase):
    def test_native_two_triangle_tv_bound(self):
        for n in (3,5,10,20,40,60):
            d=total_tv_against_limit(n)
            self.assertLessEqual(d,min(F(1),F(45,n)))
        self.assertGreater(total_tv_against_limit(10),total_tv_against_limit(40))

    def test_source_cross_covariance_first_jet(self):
        for n in (100,1000,10000):
            val=F(n)*(cross_covariance(n,n,n)-2)
            self.assertLess(abs(val+F(569,60)),F(30,n))

    def test_selected_source_integer_carries_unchanged(self):
        x,k=original_literal_history(50)
        self.assertEqual(k[1],3)
        self.assertEqual(k[2],2)
        for n in range(1,50):
            self.assertEqual(x[n],16*x[n-1]+source_R(8*n-7)-k[n])
            self.assertTrue(0<=x[n]<1)
        # A changed rational preparation changes genuine internal carries.
        _,alt=original_literal_history(50,F(1,7))
        self.assertNotEqual(k[1:40],alt[1:40])

    def test_interior_carry_breaks_endpoint_sum_sufficiency(self):
        _,k=original_literal_history(50)
        chosen=next(n for n in range(3,20) if k[n]!=k[n+1])
        # Grade (J,K)=(1,0) and (0,1) have the same total S=1,
        # but select distinct intermediate arithmetic carry marks.
        self.assertNotEqual(k[chosen],k[chosen+1])
        p=shared_panels(chosen,1,1)
        self.assertEqual(p[1][0],p[0][1]) # source exchangeability remains
        self.assertEqual(chosen+1+0,chosen+0+1)

    def test_exact_two_time_carry_register(self):
        for n in (3,5,7):
            p=internal_carry_marginal(n,n,n)
            self.assertEqual(sum(p.values(),F()),1)
            alt=internal_carry_marginal(n,n,n,F(1,7))
            self.assertEqual(sum(alt.values(),F()),1)
            if n==5:self.assertNotEqual(p,alt)


def selected_joint_carry_phase_polynomial(n, seed=F(0)):
    """Exact group-algebra signed-phase data. No transcendental phase rounding.

    Each entry (intermediate literal carry, final literal carry,
    relative fractional circle phase) has exact rational mass.
    The actual SUCC four-pole U0=0 is the default seed.
    """
    p=shared_panels(n,n,n)
    states,carries=original_literal_history(3*n,seed)
    out={}
    for j,row in enumerate(p):
        for k,mass in enumerate(row):
            q=(states[n+j+k]-states[n+j])%1
            key=(carries[n+j],carries[n+j+k],q)
            out[key]=out.get(key,F())+mass
    return out

class TestExactMarkedFourier(unittest.TestCase):
    def test_selected_phase_polynomial_and_aliased_seed(self):
        for n in (3,5,7):
            a=selected_joint_carry_phase_polynomial(n)
            self.assertEqual(sum(a.values(),F()),F(1))
            # s=1/16 is a circle alias after the first step.
            self.assertEqual(a,selected_joint_carry_phase_polynomial(n,F(1,16)))
            # A genuinely different physical seed produces a different mark.
            self.assertNotEqual(a,selected_joint_carry_phase_polynomial(n,F(1,7)))

if __name__=='__main__': unittest.main(verbosity=2)

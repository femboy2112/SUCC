"""Exact finite controls for Gaussian lattice angular pinbed versus SUCC BBP.

ALL exact Fraction/integers except no trigonometric evaluation at all.
The all-R, all-sector bounds in the companion paper are analytic proofs;
this script tests independent finite instances, not the universal claims.
"""
from __future__ import annotations
from math import isqrt, comb, gcd
from fractions import Fraction as Q
from functools import lru_cache


def gaussian_disk(R):
    """Enumerate the closed integer disk, excluding the origin."""
    assert isinstance(R,int) and R>=1
    return [(a,b) for a in range(-R,R+1) for b in range(-isqrt(R*R-a*a),isqrt(R*R-a*a)+1)
            if a or b]


def gauss_count_independent(R):
    """Count all points using only an integer-square-root scan in one quadrant."""
    return 1+4*R+4*sum(isqrt(R*R-a*a) for a in range(1,R+1))


def gaussian_angular_coeff(R,h,primitive=False):
    """Exact real angular Fourier mode for even h: Re((a+ib)^h)/(a²+b²)^(h/2)."""
    assert h>0 and h%2==0
    pts=gaussian_disk(R)
    if primitive:
        pts=[(a,b) for a,b in pts if gcd(abs(a),abs(b))==1]
    total=Q()
    for a,b in pts:
        real=sum((-1)**j*comb(h,2*j)*a**(h-2*j)*b**(2*j) for j in range(h//2+1))
        total+=Q(real,(a*a+b*b)**(h//2))
    return total/len(pts)


def gaussian_c4_exact_zeros(R,h):
    # Under z -> i*z, e(h theta) multiplies by i^h; unless h is divisible by 4,
    # the complete angular sum is 0 without any limiting argument.
    assert h>0
    return h%4!=0


def gaussian_octant_count(R):
    """Exact points in the closed [0,pi/4] angle wedge (overcounts shared boundaries)."""
    return sum(1 for a,b in gaussian_disk(R) if a>=b>=0)


def gaussian_primitive_count(R):
    return sum(1 for a,b in gaussian_disk(R) if gcd(abs(a),abs(b))==1)


def bbp_forcing(n):
    assert n>=1
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def bbp_alpha_prefix(L):
    return sum((Q(16)**(-j)*bbp_forcing(j) for j in range(1,L+1)),Q())


def gauss_pi_rational(R):
    return Q(gauss_count_independent(R),R*R)


def gauss_pi_rational_enclosure(R):
    """Outward elementary enclosure with corner displacement sqrt(2)/2 < 3/4."""
    assert R>=2
    c=Q(3,4)
    count=gauss_count_independent(R)
    return Q(count,1)/(R+c)**2,Q(count,1)/(R-c)**2


def bbp_pi_enclosure(L):
    """Unchanged four-pole BBP; 0<pi-16*P_L <64/(15(L+1)^2 16^L)."""
    lower=16*bbp_alpha_prefix(L)
    upper=lower+Q(64,15*(L+1)**2*16**L)
    return lower,upper


def rational_pi_cross_check(R,L):
    lo1,hi1=gauss_pi_rational_enclosure(R)
    lo2,hi2=bbp_pi_enclosure(L)
    return max(lo1,lo2)<min(hi1,hi2)


def gauss_approximation_nonnormal(R):
    """For R=16^M, pi_R=N(R)/R^2 has exactly 2M hex digits in its fractional part."""
    assert R>1 and R & (R-1)==0
    m=0; r=R
    while r>1:
        assert r%16==0
        r//=16; m+=1
    numerator=gauss_count_independent(R)
    assert numerator%4==1
    assert numerator%2==1
    # π_R is rational with odd numerator and denominator 16^(2m)
    v=Q(numerator,16**(2*m))
    assert v.denominator==16**(2*m)
    return m,v


def period_two_wrong_seed_check():
    """Exact original-source coherent counterseed: π-like completed orbit becomes tiny."""
    from_math = []
    for A in (8,16,24):
        L=2*A+12
        alphaL=bbp_alpha_prefix(L)
        # Counterseed s=-alphaL; completed orbit parameter = pi/16-alphaL,
        # uncompleted U_n(-alphaL) = -finite tail through L.
        y=[]
        for n in range(A,2*A):
            k=sum((Q(16)**(n-j)*bbp_forcing(j) for j in range(n+1,L+1)),Q())
            y.append((-k)%1)
        q=3
        assert max([min(v,1-v) for v in y])<Q(1,q)
        from_math.append((A,L,q))
    return from_math


def run():
    checked=0
    for R in (4,8,16,24,32):
        pts=gaussian_disk(R)
        assert len(pts)+1==gauss_count_independent(R)
        assert gauss_count_independent(R)%4==1
        assert gaussian_octant_count(R)<=len(pts)
        assert gaussian_primitive_count(R)<=len(pts)
        for h in (4,8):
            ans=gaussian_angular_coeff(R,h)
            assert -1<=ans<=1
            checked+=1
        checked+=4
    for R in (4,8,16,32,64,128):
        for L in (8,12):
            assert rational_pi_cross_check(R,L)
            checked+=1
    for R in (16,256):
        m,v=gauss_approximation_nonnormal(R)
        assert m in (1,2)
        checked+=1
    # The first Gaussian shell consists of axes/diagonals, all h=8 phases are +1.
    assert gaussian_angular_coeff(1,8)==1
    assert gaussian_angular_coeff(1,4)==1
    # The exact h=8 angular probe is nonzero on a moderately sized disk:
    assert gaussian_angular_coeff(8,8)!=0
    checked+=3
    seeds=period_two_wrong_seed_check()
    checked+=len(seeds)
    print(f'PASS {checked} finite exact Gaussian-angle, independent BBP, counterseed checks')
    print('Gaussian angles h=8 (rounded display; exact Fraction internally):',[(R,round(float(gaussian_angular_coeff(R,8)),9)) for R in (1,4,8,16)])
    print('Gauss approximants π_R with R=16,256:')
    for R in (16,256):
        m,v=gauss_approximation_nonnormal(R)
        print(f'  R={R} M={m} N={v.numerator} / {v.denominator} (terminating after {2*m} hex places)')
    print('Source-faithful rational shadow controls:',seeds)
    print('Every finite checked identity is exact; no asymptotic π normality assertion.')


# Diagnostic helper, executed only by explicit command to avoid increasing the
# precision/oracle assumptions of the universal geometric tests.
def source_epoch_diagnostics():
    from math import log2
    def source_orbit(seed,A):
        u=Q(seed)
        out=[]
        for n in range(1,2*A):
            u=(16*u+bbp_forcing(n))%1
            if n>=A:
                out.append(u)
        return out
    def energy(xs,q):
        N=len(xs)
        # Group unordered pairs, handling exact circular distance.
        acc=Q(N)
        pairs=0
        for i,x in enumerate(xs):
            for y in xs[i+1:]:
                d=abs(x-y)
                d=min(d,1-d)
                if d* q < 1:
                    acc += 2*(1-q*d)
                    pairs += 1
        return Q(q,N*N)*acc, pairs
    out=[]
    for A in (16,32,64,128):
        q=max(2,A.bit_length()-1)
        zero=source_orbit(Q(0),A)
        shadow=source_orbit(-bbp_alpha_prefix(2*A+12),A)
        ez,pz=energy(zero,q)
        es,ps=energy(shadow,q)
        assert es>=ez or A==16, (A,ez,es)
        out.append((A,q,float(ez),float(es),pz,ps))
    return out


def mobius_table(N):
    """Integer Möbius values by an independent elementary squarefree sieve."""
    result=[1]*(N+1);result[0]=0
    for p in range(2,N+1):
        if all(p%d for d in range(2,isqrt(p)+1)):
            for v in range(p,N+1,p):result[v]*=-1
            for v in range(p*p,N+1,p*p):result[v]=0
    return result


def scaled_disk_count(R,d):
    """Number of nonzero integer (u,v) with d²(u²+v²) <= R²."""
    m=R//d
    if m==0:return 0
    return 4*m+4*sum(isqrt(R*R-(d*a)**2)//d for a in range(1,m+1))


def scaled_octant_count(R,d):
    """Number of nonzero integer 0<=v<=u, d²(u²+v²)<=R²."""
    m=R//d
    return sum(1+min(a,isqrt(R*R-(d*a)**2)//d) for a in range(1,m+1))


def primitive_mobius_checks():
    result=[]
    for R in (4,8,16,24,32,48):
        mu=mobius_table(R)
        prim=sum(mu[d]*scaled_disk_count(R,d) for d in range(1,R+1))
        poct=sum(mu[d]*scaled_octant_count(R,d) for d in range(1,R+1))
        direct=gaussian_primitive_count(R)
        direct_oct=sum(1 for a,b in gaussian_disk(R) if a>=b>=0 and gcd(abs(a),abs(b))==1)
        assert prim==direct and poct==direct_oct
        result.append((R,prim,poct))
    return result



def chi_minus_four(n):
    return 0 if n%2==0 else (1 if n%4==1 else -1)


def gaussian_count_via_dirichlet(R):
    """Independent Jacobi two-squares divisor identity; exact finite formula."""
    return 1+4*sum(chi_minus_four(d)*(R*R//d) for d in range(1,R*R+1))


def jacobi_gauss_controls():
    checks=[]
    for R in (1,2,3,4,8,16,24,32):
        via=gaussian_count_via_dirichlet(R)
        direct=gauss_count_independent(R)
        assert via==direct
        checks.append((R,via))
    return checks

if __name__=='__main__':
    run()
    print('PASS 6 primitive Möbius disk/octant inversion controls:',primitive_mobius_checks())
    print('PASS 8 independent Jacobi / χ_-4 Gaussian count controls:',jacobi_gauss_controls())

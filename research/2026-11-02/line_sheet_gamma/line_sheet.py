"""Original BBP line/sheet Laplace kernels, one-scale collision, and multi-prime passport.

Exact arithmetical steps use Fraction. Floating Laplace/circle sheet probes
are diagnostics, NOT certified interval bounds or proof of pi normality.
The universal all-real kernel result has a separately stated paper proof.
"""
from fractions import Fraction
from math import cos, exp, expm1, fsum, gcd, isqrt, log, pi, sin


def kappa(t):
    """Universal positive Euler--Mascheroni Laplace-line kernel, t>0."""
    if t <= 0:
        raise ValueError('t must be positive')
    if t < 1.e-3:
        return 0.5-t/12+t**3/720-t**5/30240+t**7/1209600
    return 1/t-1/expm1(t)


def bbp_sheet_source_kernel(t):
    """Exact four-pole source Gamma tail Laplace density, evaluated floating."""
    if t <= 0:
        raise ValueError('t must be positive')
    u = exp(-t/8)
    P = (1-u)*(u*u+2)*(u*u+2*u+2)
    return u*P/(8*(16-u**8))


def small_sheet_lower(t):
    """Proved lower bound on convolution sheet for 0<t<=6."""
    if not (0 < t <= 6):
        raise ValueError('requires 0<t<=6')
    return t/64-t*t/384+t**3/13824


def long_sheet_lower(t):
    """Proved lower bound on convolution sheet for all t>0."""
    if t <= 0:
        raise ValueError('t>0')
    return log(1+t/2)/(8*(t+4))


def sheet_kernel_numeric(t, panels=4096):
    """Simpson float diagnostic for (kappa*kappa)(t)/16, not proof."""
    if t <= 0 or panels <= 0 or panels%2:
        raise ValueError('t>0, panels positive/even')
    step = t/panels
    def integrand(j):
        x=j*step
        a = 0.5 if j==0 else kappa(x)
        b = 0.5 if j==panels else kappa(t-x)
        return a*b
    total=integrand(0)+integrand(panels)
    total+=4*fsum(integrand(j) for j in range(1,panels,2))
    total+=2*fsum(integrand(j) for j in range(2,panels,2))
    return total*step/48


def exact_kernel_coefficients():
    """Paper-derived exact small-time coefficients for source and sheet."""
    return {
      'kappa_t0':(Fraction(1,2),Fraction(-1,12),Fraction(0),Fraction(1,720)),
      'source':(Fraction(0),Fraction(1,64),Fraction(-7,1024),Fraction(55,24576)),
      'gamma_sheet':(Fraction(0),Fraction(1,64),Fraction(-1,384),Fraction(1,13824)),
      'sheet_minus_source':(Fraction(0),Fraction(0),Fraction(13,3072),Fraction(-479,221184)),
      'laplace_cubic_gap':Fraction(13,1536),
    }


def kernel_polynomial_identity(u):
    """Exact u-polynomial identity used in 0<t<=4 comparison."""
    u=Fraction(u)
    R=u**4-u**3-u**2+3*u-1
    lhs=u*(16-u**8)-(u*u+2)*(u*u+2*u+2)
    rhs=(1-u)*(u*u+2)*(u*u+2*u+2)*R
    return lhs==rhs


def endpoint_rational_certificates():
    """Pure Fraction certificate facts in piecewise kernel proof."""
    u=Fraction(11,20)
    P=4-2*u**3-u**4-u**5
    q=u*P/(8*(16-u**8))
    L5=Fraction(5,64)-Fraction(25,384)+Fraction(125,13824)
    L6=Fraction(6,64)-Fraction(36,384)+Fraction(216,13824)
    return {'q_at_11_over_20':q,
            'q_below_1_over_64':q<Fraction(1,64),
            'L5':L5,'L5_above_1_over_48':L5>Fraction(1,48),
            'L6':L6, 'R_half':Fraction(3,16)}


def original_source(n):
    if n<1:raise ValueError('n>=1')
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)


def original_states(N):
    if N<0:raise ValueError('N>=0')
    U=[Fraction(0)]
    for n in range(1,N+1):
        U.append(16*U[-1]+original_source(n))
    return U


def prime_q(n):
    if n<2:return False
    return all(n%p for p in range(2,isqrt(n)+1))


def epoch_prime_family(A):
    """All p=8k+1 prime with A/2<=k<A, covering [A,2A)."""
    if A<2 or A&(A-1):raise ValueError('A must be dyadic power of 2')
    return [8*k+1 for k in range(A//2,A) if prime_q(8*k+1)]


def prime_birth_residue(p,n):
    if not (p>5 and p%8==1 and prime_q(p)):
        raise ValueError('prime p>5 == 1 mod8 required')
    k=(p-1)//8
    if not (k+1<=n<=4*k):
        raise ValueError('n outside prime-clean source window')
    return 4*pow(16,n-(k+1),p)%p


def simultaneous_prime_cofactor(n, primes, state):
    """Exact CRT decomposition of original U_n into all p-primary sheets."""
    co=Fraction(state)
    factors=[]
    for p in primes:
        a=prime_birth_residue(p,n)
        factors.append((p,a))
        co-=Fraction(a,p)
    if not all(co.denominator%p for p in primes):
        raise AssertionError('complementary real/p-adic source passport failed')
    return factors,co


def galois_pair_character(primes,d):
    """Exact finite joint Galois pair kernel (not selected real embedding)."""
    if d<0:raise ValueError('nonnegative lag required')
    ans=Fraction(1)
    if d==0:return ans
    for p in primes:
        if pow(16,d,p)!=1:
            ans*=Fraction(-1,p-1)
    return ans


def short_lag_nonaliases(primes,d):
    return sum(1 for p in primes if pow(16,d,p)!=1)


def coherent_counterfeit(n, primes, Q):
    """Hostile p-free cofactor, NOT the original BBP source/seed."""
    if Q<=0 or any(gcd(Q,p)>1 for p in primes):
        raise ValueError('Q must be positive and coprime to every prime')
    y=sum((Fraction(a,p) for p,a in [(p,prime_birth_residue(p,n)) for p in primes]),Fraction(0))
    f=Q*y
    nearest=(2*f.numerator+f.denominator)//(2*f.denominator)
    co=Fraction(-nearest,Q)
    assert all(co.denominator%p for p in primes)
    delta=y+co
    assert abs(delta) <= Fraction(1,2*Q)
    return co,delta


def source_selfscale_collision(A,states=None):
    """Exact original U0=0 dyadic self-resolution collision, source only."""
    if A<2 or A&(A-1):raise ValueError('A power of two >=2')
    if states is None:states=original_states(2*A-1)
    counts=[0]*A
    for n in range(A,2*A):
        q=states[n];r=q.numerator%q.denominator
        counts[(A*r)//q.denominator]+=1
    return counts,Fraction(sum(c*c for c in counts),A)


if __name__=='__main__':
    for t in (.01,.1,1.,2.,4.,5.,6.,8.,16.,32.,128.):
        sh=sheet_kernel_numeric(t)
        print('t=%.2f GammaSheet=%.12g BBP=%.12g positive_gap=%.12g' %
              (t,sh,bbp_sheet_source_kernel(t),sh-bbp_sheet_source_kernel(t)))
    for A in (16,32,64,128,256):
        primes=epoch_prime_family(A)
        counts,C=source_selfscale_collision(A)
        print('A=%d primes=%d source_C=%s'%(A,len(primes),str(C)))

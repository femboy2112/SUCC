"""Oily–Macaroni totient and *connected* 3rd-order BBP packet shadow.

Source: the two-stage positive polynomial compiler of PR #309 at
8e9d8a4d7d42bb0931f899ac221f27fccf090b36; no original SUCC source
changes.  These are auxiliary packet observables, NOT selected π-orbit
Weyl estimates.  All finite certificate coefficients use exact Fraction.

The source grade J and boundary variable X have joint density
    x^(8n) p_j(x) dx / T_n
where R(x)=sum_j p_j(x) is the original BBP Green density.  In the
limit, J has weights (j+1)/2^(j+2), Y=8n(1-X) -> Gamma(2), and J,Y
become independent.  Their connected covariance retains O(1/n) structure.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import gcd, isqrt
from typing import Callable


def _positive_integer(n, label="integer", maximum=100000):
    if type(n) is not int or not 1 <= n <= maximum:
        raise ValueError(f"{label}: positive ordinary integer <= {maximum} required")
    return n


def mobius(d: int) -> int:
    _positive_integer(d, "Mobius index")
    if d == 1:
        return 1
    out, n = 1, d
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            out = -out
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out = -out
    return out


def divisors(q: int) -> tuple[int, ...]:
    _positive_integer(q, "modulus")
    return tuple(d for d in range(1,q+1) if q%d == 0)


def endpoint_weight(j: int) -> Q:
    if type(j) is not int or j < 0:
        raise ValueError("nonnegative packet grade")
    return Q(j+1, 2**(j+2))


def multiple_weight(d: int) -> Q:
    """Exact E[1_(d|J)] = [1+(d-1)2^-d]/[4(1-2^-d)^2]."""
    _positive_integer(d, "divisor")
    t=Q(1,2**d)
    return (1+(d-1)*t)/(4*(1-t)**2)


def primitive_mass(q: int) -> Q:
    """Totient: P(gcd(J,q)=1), with gcd(0,q)=q.

    q=1 includes grade zero. Multiplicativity does not hold: the same
    nonuniform grade J generates the different prime filters.
    """
    return sum((mobius(d)*multiple_weight(d) for d in divisors(q)), Q())


def primitive_residue_distribution(q: int, depth: int) -> tuple[Q, ...]:
    """Exact truncated UN-normalized weights in Z/q; omitted mass known."""
    _positive_integer(q,"modulus")
    _positive_integer(depth,"depth", 200)
    out=[Q() for _ in range(q)]
    for j in range(depth):
        if gcd(j,q)==1:
            out[j%q]+=endpoint_weight(j)
    return tuple(out)


def primitive_root_formula(q: int, z) -> complex:
    """Numerical evaluation ONLY of an exact rational function (|z|=1).

    C_q(z) = (1/4) sum_(d|q) mu(d)[1+(d-1)t]/(1-t)^2,
    t=(z/2)^d. Not a certified complex interval.
    """
    _positive_integer(q,"modulus")
    total=0j
    for d in divisors(q):
        t=(z/2)**d
        total += mobius(d)*(1+(d-1)*t)/(4*(1-t)**2)
    return total


def odd_fourier_limit(z):
    """Exact algebraic expression 4z/(4-z^2)^2 (|z|=1)."""
    return 4*z/(4-z*z)**2


def odd_shadow_coefficient(z):
    """Exact rational-function coefficient 2C-zC'=4z(4-5z²)/(4-z²)^3."""
    return 4*z*(4-5*z*z)/(4-z*z)**3



def primitive_complex_mellin(n:int, q:int, h:int, s, precision:int=55):
    """NUMERICAL complex first/second Mellin fields (diagnostic, not proof).

    Computes the actual common-source integral K_n(g,s) by independent
    quadrature. For dyadic q the exact identity simplifies the numerator:
      z*a**s/(4*T_n) integral_0^1 x^(8n+1)(1-x)^(s+1)
               /[(1-z²u²)(1-z²v²)] dx.
    The source T_n is integrated independently.  No pi digits or orbit
    normality enter this auxiliary observable. Analytic paper theorem
    requires Re(s)>-2.
    """
    _positive_integer(n,"time")
    _positive_integer(q,"modulus")
    if type(h) is not int or type(precision) is not int or not 20<=precision<=250:
        raise ValueError("integer frequency and finite precision 20..250 required")
    import mpmath as mp
    with mp.workdps(precision):
        a=8*n
        z=mp.e**(2j*mp.pi*h/q)
        s=mp.mpc(s)
        if mp.re(s)<=-2:
            raise ValueError("absolute Mellin domain Re(s)>-2")
        den=mp.quad(lambda x:x**a*source_kernel(x),[0,mp.mpf('0.5'),1])
        if q&(q-1)==0:
            f=lambda x:z*a**s*x**(a+1)*(1-x)**(s+1)/(
                4*(1-z*z*packet_u(x)**2)*(1-z*z*packet_v(x)**2))
        else:
            f=lambda x:x**a*source_kernel(x)*conditional_primitive_character(x,q,z)*(a*(1-x))**s
        num=mp.quad(f,[0,mp.mpf('0.5'),1])
        return +num/den


def packet_u(x):
    return x-x*x/2


def packet_v(x):
    return x*x/2


def source_kernel(x):
    """Exactly the PR #309 reduced original BBP Green density."""
    if not 0 <= x <= 1:
        raise ValueError("source x must belong to [0,1]")
    return (1-x)/((2-x*x)*(x*x-2*x+2))


def conditional_grade_pgf(x,z):
    """E_x[z^J] for two independent geometric packet stages; numeric/complex."""
    if not 0 <= x <= 1:
        raise ValueError("source coordinate outside [0,1]")
    u,v=packet_u(x),packet_v(x)
    return (1-u)*(1-v)/((1-z*u)*(1-z*v))


def conditional_odd_character(x,z):
    """E_x[z^J 1_(J odd)] = (1-u)(1-v)z(u+v)/[(1-u²z²)(1-v²z²)]."""
    if not 0 <= x <= 1:
        raise ValueError("source coordinate outside [0,1]")
    u,v=packet_u(x),packet_v(x)
    return (1-u)*(1-v)*z*(u+v)/((1-z*z*u*u)*(1-z*z*v*v))


def conditional_primitive_character(x,q,z):
    """Exact rational-function Mobius projector for |z|<=1, x in [0,1]."""
    if not 0 <= x <= 1:
        raise ValueError("source coordinate outside [0,1]")
    _positive_integer(q,"modulus")
    u,v=packet_u(x),packet_v(x)
    if u == v:
        # limits at x=0 or x=1 are explicit and remove the divided difference
        if x == 0:
            return 1 if q == 1 else 0
        return primitive_root_formula(q,z)
    return (1-u)*(1-v)/(u-v)*sum(
        mobius(d)*(u/(1-(u*z)**d)-v/(1-(v*z)**d))
        for d in divisors(q)
    )


def kernel_odd_unnormalized(x,z):
    """SOURCE IDENTITY: R(x)*E_x[z^J 1odd] without cancellation loss."""
    u,v=packet_u(x),packet_v(x)
    return z*x*(1-x)/(4*(1-z*z*u*u)*(1-z*z*v*v))


def end_grade_first_variation(j):
    """Derivative: q_j(1-delta)=w_j[1+(2-j)delta]+O(delta²)."""
    return (2-j)*endpoint_weight(j)


def shadow_limit(q,z):
    """Exact-rational-function expression for a Cov(primitive*z^J, logY)."""
    # For general q, the generating function is holomorphic, so use
    # 2*C(z) - z C'(z) via exact divisor formula.
    total=0j
    for d in divisors(q):
        t=(z/2)**d
        term= (2*(1+(d-1)*t)/(1-t)**2
               -d*t*(d+1+(d-1)*t)/(1-t)**3)/4
        total += mobius(d)*term
    return total


def poly_mul(a,b):
    out=[Q() for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return tuple(out)


def packet_polynomial(j: int) -> tuple[Q,...]:
    """P_j(x)=(1-x)/4 sum_(k=0)^j u^k v^(j-k) as exact coefficients."""
    if type(j) is not int or not 0<=j<=64:
        raise ValueError("grade in 0..64 for exact polynomial budget")
    up=[(Q(1),)]
    vp=[(Q(1),)]
    for _ in range(j):
        up.append(poly_mul(up[-1],(Q(),Q(1),Q(-1,2))))
        vp.append(poly_mul(vp[-1],(Q(),Q(),Q(1,2))))
    out=[Q()]*(2*j+1)
    for k in range(j+1):
        part=poly_mul(up[k],vp[j-k])
        for m,val in enumerate(part):out[m]+=val
    return poly_mul(tuple(x/4 for x in out),(Q(1),Q(-1)))


def packet_log_moments(n: int, j: int) -> tuple[Q,Q,Q]:
    """Exact integral of x^(8n)p_j(x)*(log(1-x))^k for k=0,1,2.

    The log moments are all **rational**, since p_j is polynomial and the
    log integrals are Beta/digamma differences. No gamma or zeta numeric
    evaluation is needed. This is not the infinite full-packet sum.
    """
    _positive_integer(n,"source time",10000)
    poly=packet_polynomial(j)
    a=8*n
    m0=m1=m2=Q()
    # coefficient representation of p_j itself (has 1-x factor).
    # For each c*x^i *(1-x): use degree i inside the factorization.
    assert sum(poly)==0
    # divide p_j by (1-x) exactly via prefix partial sums.
    quotient=[];acc=Q()
    for c in poly[:-1]:
        acc+=c
        quotient.append(acc)
    for i,c in enumerate(quotient):
        if not c:continue
        N=a+i+2
        beta=Q(1,(a+i+1)*(a+i+2))
        h=sum((Q(1,k) for k in range(1,N+1)),Q())
        h2=sum((Q(1,k*k) for k in range(1,N+1)),Q())
        m0+=c*beta
        m1+=c*beta*(1-h)
        m2+=c*beta*((1-h)**2+h2-1)
    return m0,m1,m2


def finite_primitive_log_covariance(n:int,depth:int,q:int=2,h:int=0):
    """Exact Fraction coefficient pair A,B for finite packet covariance:

    Cov(1_gcd(J,q)=1 * root_q^(hJ), (logY-c)^2)
      = A + 2(log(8n)-c) B,
    where for q=2 (h parity), root_q^h is +/-1 so A,B rational.

    Finite packet law is normalized by T_(n,depth), not true T_n.
    This function restricts to q=2 for rational exact audit.
    """
    _positive_integer(n,"source time",10000)
    _positive_integer(depth,"depth",200)
    if q!=2 or type(h) is not int:
        raise ValueError("exact rational connected shadow currently q=2 only")
    A=[Q(),Q(),Q()]
    P=[Q(),Q(),Q()]
    for j in range(depth):
        m=packet_log_moments(n,j)
        for k in range(3):
            A[k]+=m[k]
            if j%2:P[k]+=(-1 if h%2 else 1)*m[k]
    Z=A[0]
    if not Z:
        raise ArithmeticError("zero finite source mass")
    logcov=P[1]/Z-P[0]*A[1]/Z**2
    log2cov=P[2]/Z-P[0]*A[2]/Z**2
    return {"n":n,"depth":depth,"normalizer":Z,"primitive_mass":P[0]/Z,
            "coefficient_constant":log2cov,"coefficient_log":2*logcov,
            "relative_to_c":"constant+coefficient_log*(log(8n)-c)",
            "selected_weyl_bound_proved":False}


def compiler_error(depth:int)->Q:
    """PR #309 sharp pointwise relative loss bound rho_M."""
    _positive_integer(depth,"depth",200)
    return Q(depth+2,2**(depth+1))


def weighted_selected_transport_budget(N:int,depth:int):
    """Uniform in dyadic character AND original phase.

    For W_n=E_n[1_(J odd) z^J], C=4z/(4-z²)^2,
      |1/N sum e(hU_n) W_n - C*(S_N(h)/N)|
      <= H_N/N.
    Replacing W_n with exact finite-depth normalized W_(n,M)
    adds at most 2 rho_M. **Both coherent changed-seed orbits and
    authentic zero-seed orbits satisfy this!** No saving is generated.
    """
    _positive_integer(N,"horizon")
    rho=compiler_error(depth)
    h=sum((Q(1,k) for k in range(1,N+1)),Q())
    return {"N":N,"depth":depth,"harmonic":h,
            "full_packet_mean_error_upper":h/N,
            "finite_packet_mean_error_upper":h/N+2*rho,
            "limit_dyadic_character_modulus_lower":Q(4,25),
            "proves_phase_cancellation":False}


def parity_shadow_predictions():
    """Exact coefficients, with Omega=phi^-1-gamma only as separate scalar.

    a Cov(1odd,logY)->-4/27; a Cov(1odd,(logY-q*)²)
      -> (-8/27)*(phi^-1-gamma).
    """
    return {"scalar_totient":Q(4,9),"first_log_shadow":Q(-4,27),
            "third_shadow_multiplier":Q(-8,27),
            "golden_fixed_point_polynomial":(1,-3,1),
            "source_only_proves_normality":False}

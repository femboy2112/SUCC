"""Exact finite probes for the SUCC gauge-anchored pi/RH frontier.

No RH or pi-normality proof. All model-choice bounds below are relative to
finite observers; changed-source controls are explicitly NOT BBP-zero-seed or
Euler-product preserving. Existing classical source identities are imported.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import factorial, isqrt


def forcing(n: int) -> Q:
    """Authenticated four-pole BBP forcing, n>=1."""
    if type(n) is not int or n < 1:
        raise ValueError("BBP source clock must be positive integer")
    return Q(4, 8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def bbp_state(n: int, seed: Q=Q(0)) -> Q:
    """Exact source U_n(seed); positive seed changes the source contract."""
    if type(n) is not int or n<0 or type(seed) not in (Q,int):
        raise ValueError("Nonnegative source clock and rational seed required")
    state=Q(seed)
    for j in range(1,n+1):
        state=16*state+forcing(j)
    return state


def green_truncated(n: int, depth: int) -> Q:
    """Truncated future BBP Green correction T_{n,depth}."""
    if type(n) is not int or n<0 or type(depth) is not int or depth<0:
        raise ValueError("Nonnegative clock and depth")
    return sum((Q(1,16**j)*forcing(n+j) for j in range(1,depth+1)),Q(0))


def green_residual(n: int, depth: int) -> Q:
    """Exact finite leftover of conjugacy V_{n+1}=16 V_n."""
    if type(n) is not int or n<0 or type(depth) is not int or depth<0:
        raise ValueError("Invalid n/depth")
    v_now=bbp_state(n)+green_truncated(n,depth)
    v_next=bbp_state(n+1)+green_truncated(n+1,depth)
    residual=v_next-16*v_now
    expected=Q(1,16**depth)*forcing(n+depth+1)
    if residual!=expected:
        raise AssertionError("Source Green cocycle sign or time indexing wrong")
    return residual


def lagarias_lower_certificate(n: int, exp_degree=16, log_terms=30) -> dict:
    """RIGOROUS rational lower bound on H_n+exp(H_n)*log(H_n)-sigma(n).

    Taylor(exp) and atanh(log) series have all nonnegative terms when H>=1.
    If lower_gap>0 then Lagarias's n-th inequality is certified strictly.
    For n=1 exact equality is evaluated without series.
    """
    if type(n) is not int or n<1 or type(exp_degree) is not int or exp_degree<0 or type(log_terms) is not int or log_terms<0:
        raise ValueError("Positive n and nonnegative truncation sizes")
    h=sum((Q(1,k) for k in range(1,n+1)),Q(0))
    if n==1:
        return {"n":1,"H":Q(1),"sigma":1,"lower_gap":Q(0),"exp_degree":exp_degree,"log_terms":log_terms}
    e_low=sum((h**k/factorial(k) for k in range(exp_degree+1)),Q(0))
    t=(h-1)/(h+1)
    l_low=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(log_terms)),Q(0))
    s=sum(d+(n//d if d*d !=n else 0) for d in range(1,isqrt(n)+1) if n%d==0)
    return {"n":n,"H":h,"sigma":s,"lower_gap":h+e_low*l_low-s,
            "exp_degree":exp_degree,"log_terms":log_terms}


def lagarias_rational_interval(n: int, exp_degree=16, log_terms=30) -> dict:
    """Lower AND upper rational margins for n-th Lagarias inequality.

    Taylor-exp remainder bounded by a geometric ratio (requires H<K+2).
    Atanh-log remainder bounded using the first omitted denominator.
    The correct result is PASS, FAIL or UNRESOLVED (not RH proof).
    """
    if type(n) is not int or n<1 or type(exp_degree) is not int or exp_degree<0 or type(log_terms) is not int or log_terms<1:
        raise ValueError('Finite n>=1, exp degree>=0 and >=1 log term required')
    r=lagarias_lower_certificate(n,exp_degree,log_terms)
    if n==1:return {'n':1,'lo':Q(0),'hi':Q(0),'verdict':'EQUALITY_AT_1'}
    h=r['H']
    if h>=exp_degree+2:
        raise ValueError('Degree too small for geometric exp upper bound')
    exp_lo=sum((h**k/factorial(k) for k in range(exp_degree+1)),Q(0))
    exp_hi=exp_lo+ (h**(exp_degree+1)/factorial(exp_degree+1))/(1-h/Q(exp_degree+2))
    t=(h-1)/(h+1)
    log_lo=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(log_terms)),Q(0))
    log_hi=log_lo+2*t**(2*log_terms+1)/(Q(2*log_terms+1)*(1-t*t))
    lo=h+exp_lo*log_lo-r['sigma']
    hi=h+exp_hi*log_hi-r['sigma']
    assert lo<=hi and lo==r['lower_gap']
    verdict='PASS' if lo>0 else 'FAIL' if hi<0 else 'UNRESOLVED'
    return {'n':n,'lo':lo,'hi':hi,'verdict':verdict}


def lagarias_rigorous_range(end: int=128, exp_degree=16, log_terms=30) -> dict:
    """FINITE certificate only. Does not assert the universal RH criterion."""
    if type(end) is not int or end<2 or end>2048:
        raise ValueError("Finite bounded test only")
    items=[lagarias_lower_certificate(n,exp_degree,log_terms) for n in range(2,end+1)]
    failures=[x['n'] for x in items if x['lower_gap']<=0]
    min_item=min(items,key=lambda x:x['lower_gap'])
    return {"tested_through":end,"strict_lower_bounds":not failures,"failed_to_certify":failures,
            "minimal_lower_gap_n":min_item['n'],"minimal_lower_gap":min_item['lower_gap'],
            "proves_RH":False}


def polynomial_multiply(a: tuple[Q,...], b: tuple[Q,...]) -> tuple[Q,...]:
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=Q(x)*Q(y)
    return tuple(out)


def polynomial_evaluate(a: tuple[Q,...], value: Q) -> Q:
    return sum((Q(c)*Q(value)**k for k,c in enumerate(a)),Q(0))


def derivative_coefficients(a: tuple[Q,...],order=1) -> tuple[Q,...]:
    if type(order) is not int or order<0:
        raise ValueError("Nonnegative derivative order")
    for _ in range(order):
        a=tuple((k+1)*a[k+1] for k in range(len(a)-1))
    return a or (Q(0),)


def symmetric_xi_impostor(sample_z: tuple[Q,...], jet_order=2, off_line_imag=Q(1,2)) -> dict:
    """Model-only, even-real ENTIRE surrogate: cos(z) * Q(z^2).

    cos(z) has only real zeros. Q has a root at z=+/-i*off_line_imag,
    agrees with 1 to jet_order at every listed REAL rational sample z.
    IMPORTANT: this is NOT the authentic completed zeta or its Euler product.
    """
    if not sample_z or any(type(z) not in (int,Q) for z in sample_z):
        raise ValueError("Finite rational real sample set required")
    if type(jet_order) is not int or jet_order<0 or type(off_line_imag) not in (int,Q) or off_line_imag<=0:
        raise ValueError("Jet order / imaginary zero parameter invalid")
    p=(Q(1),)
    for a in sample_z:
        for _ in range(jet_order+1):
            p=polynomial_multiply(p,(-Q(a)**2,Q(1)))
    target_w=-Q(off_line_imag)**2
    norm=polynomial_evaluate(p,target_w)
    if norm==0:raise ValueError("Unusable off-line target")
    q=tuple((Q(int(k==0))-p[k]/norm) for k in range(len(p)))
    return {"polynomial_w":q,"sample_z":tuple(map(Q,sample_z)),"jet_order":jet_order,
            "off_line_imag":Q(off_line_imag),"root_exact":polynomial_evaluate(q,target_w)==0,
            "preserves_even_and_real_symmetry":True,"preserves_zeta_Euler_source":False}


def finite_phase_bound(mode: int, observed_terms: int, shared_digit_count: int) -> Q:
    """Rational coefficient B such that |sum exp(2πih16^n x)-...|<=2π B.

    x,y share first M base16 fractional digits. For 0<=n<N,
    |16^n(x-y)| <=16^(n-M), hence B=|h|(16^N-1)/(15*16^M).
    This is a bound for TWO DIFFERENT source seeds/completions, not zero-seed BBP.
    """
    if any(type(v) is not int for v in (mode,observed_terms,shared_digit_count)) or observed_terms<0 or shared_digit_count<observed_terms:
        raise ValueError("Integer Fourier mode; M>=N>=0")
    return Q(abs(mode)*(16**observed_terms-1),15*16**shared_digit_count)


def newman_logical_status(rh: bool, lambda_sign: int) -> bool:
    """Truth-table guard: actual theorem Lambda>=0, RH iff Lambda<=0.
    Input is a HYPOTHETICAL truth assignment, not a numeric Lambda.
    """
    if type(rh) is not bool or type(lambda_sign) is not int or lambda_sign not in (-1,0,1):
        raise ValueError("Typed hypothetical propositions only")
    return lambda_sign>=0 and rh == (lambda_sign<=0)

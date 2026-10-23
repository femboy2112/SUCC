"""Exact circle time-carry correlations and 3-adic orbit countermodels.

All coefficients use integer or Fraction arithmetic. Source for the theorems:
research/2026-10-23/CIRCLE_TIME_CARRY_RESONANCE.md.
No pi-normality claim.
"""
from fractions import Fraction as Q
from math import comb, isqrt

def _integer(x, low=0):
    if type(x) is not int or x < low:
        raise ValueError("integer source outside contract")
    return x

def prime_carry_product(a, b):
    """C(a+b,a) from the complete Legendre/Kummer prime-power carries."""
    _integer(a); _integer(b)
    n = a+b
    result = 1
    for p in range(2,n+1):
        if any(p%d==0 for d in range(2,isqrt(p)+1)):
            continue
        power=p
        while power<=n:
            carry=n//power-a//power-b//power
            if carry not in (0,1):
                raise ArithmeticError("not a lawful addition carry")
            if carry:
                result*=p
            power*=p
    return result

def chord_fourier(power, via_carries=False):
    """Coefficients of (2-z-z^-1)^power, including complete arithmetic."""
    _integer(power)
    return {h: (-1 if h%2 else 1)*(
        prime_carry_product(power+h,power-h) if via_carries
        else comb(2*power,power+h))
        for h in range(-power,power+1)}

def time_frequency_table(base,times,powers,via_carries=False):
    """Signed frequencies sum_j h_j * base^time_j; no fake independence."""
    _integer(base,2)
    if not times or len(times)!=len(powers):
        raise ValueError("nonempty matching source histories")
    if (any(type(t) is not int or t<0 for t in times)
            or len(set(times))!=len(times)):
        raise ValueError("distinct nonnegative observation times")
    counts={0:1}
    for time,k in zip(times,powers):
        coeff=chord_fourier(k,via_carries)
        nxt={}
        for address,c in counts.items():
            for h,w in coeff.items():
                address2=address+h*base**time
                nxt[address2]=nxt.get(address2,0)+c*w
        counts=nxt
    return {a:c for a,c in counts.items() if c}

def haar_joint(base,times,powers,via_carries=False):
    """Haar time-correlation: exact zero-frequency integer coefficient."""
    return time_frequency_table(base,times,powers,via_carries).get(0,0)

def haar_single(k):
    _integer(k)
    return comb(2*k,k)

def first_time_carry_defect(base):
    _integer(base,2)
    return haar_joint(base,(0,1),(base,1))-2*haar_single(base)

def orbit_3adic(level):
    """One complete 16th-power orbit of 1/3^r, residues 1 mod 3."""
    _integer(level,2)
    modulus=3**level; period=3**(level-1)
    address=1; orbit=[]
    for _ in range(period):
        orbit.append(address)
        address=(16*address)%modulus
    if (address!=1 or len(set(orbit))!=period
            or set(orbit)!=set(range(1,modulus,3))):
        raise ArithmeticError("source orbit is not the required 3-adic coset")
    return tuple(orbit)

def periodic_joint(level,times,powers):
    """Exact full-period joint chord mean for x=1/3^r and base 16."""
    _integer(level,2)
    period=3**(level-1)
    freq=time_frequency_table(16,times,powers)
    result=freq.get(0,0)
    for h,c in freq.items():
        if h>0 and h%period==0:
            if freq.get(-h)!=c:
                raise ArithmeticError("conjugate phase transport broken")
            twice_cos=2 if (h//period)%3==0 else -1
            result+=c*twice_cos
    return result

def periodic_moment(level,power):
    return periodic_joint(level,(0,),(power,))

def periodic_fejer_energy(level,band):
    """At M<3^(r-1) the positive energy is identically 1."""
    _integer(level,2); _integer(band)
    period=3**(level-1);q=band//period
    return Q(1+2*q)-Q(period*q*(q+1),band+1)

def probe_support(base,times,powers):
    _integer(base,2)
    if not times or len(times)!=len(powers) or len(set(times))!=len(times):
        raise ValueError("bad finite probe history")
    return sum(_integer(k)*base**_integer(t)
               for t,k in zip(times,powers))

def finite_probe_alias(level,times,powers):
    """A sufficient exact finite-observer indistinguishability condition."""
    _integer(level,2)
    return 3**(level-1)>probe_support(16,times,powers)

def hankel_det(moment_function,size):
    """Exact rational Bareiss determinant for moments 0..2*size."""
    _integer(size)
    a=[[Q(moment_function(i+j)) for j in range(size+1)]
       for i in range(size+1)]
    previous=Q(1)
    for k in range(size):
        pivot=a[k][k]
        if pivot==0:
            return Q(0)
        for i in range(k+1,size+1):
            for j in range(k+1,size+1):
                a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])/previous
        for i in range(k+1,size+1):
            a[i][k]=Q(0)
        previous=pivot
    return a[size][size]

def select_3adic_counterfeit(pi_lo,pi_hi,level):
    """Rational selected from certified polygon pi bounds, not digit input."""
    _integer(level,2)
    lo,hi=Q(pi_lo),Q(pi_hi)
    if not Q(3)<lo<=hi<Q(4):
        raise ValueError("requires strict source-derived pi interval")
    modulus=3**level;period=modulus//3
    mid=(lo+hi)/2-3
    t=(modulus*mid-1)/3+Q(1,2)
    k=(t.numerator//t.denominator)%period
    x=Q(1+3*k,modulus)
    def arc_dist(y):
        d=abs(x-y)
        return min(d,1-d)
    error=max(arc_dist(lo-3),arc_dist(hi-3))
    if error>Q(1,2*period)+(hi-lo)/2:
        raise ArithmeticError("unexpected source/coset approximation defect")
    return x,error

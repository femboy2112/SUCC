"""Exact signed-CRT instruments; finite certificates, not normality proofs.

Independent of the parent prime_stroboscope implementation. The primary path
uses exact circle recurrence. The oracle in test_signed_crt uses unrolled
rational pole sums. Trigonometric certificates use Machin and Taylor bounds.
"""
from fractions import Fraction as F
from math import isqrt, lcm
from functools import lru_cache

COEFFICIENTS = (4, -2, -1, -1)
OFFSETS = (1, 4, 5, 6)


def source(n, coefficients=COEFFICIENTS):
    if n < 1:
        raise ValueError('positive source time required')
    return sum((F(c, 8*(n-1)+d) for c, d in zip(coefficients, OFFSETS)), F())


def orbit(last, seed=F(), coefficients=COEFFICIENTS):
    u = F(seed) % 1
    out = [u]
    for n in range(1, last+1):
        u = (16*u + source(n, coefficients)) % 1
        out.append(u)
    return out


def prime(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p)+1))


def order(p):
    if not prime(p) or p == 2:
        raise ValueError('odd prime required')
    t, a = 1, 16 % p
    while a != 1:
        t, a = t+1, a*16 % p
    return t


def birth(p):
    if not prime(p) or p < 13 or p % 4 != 1:
        raise ValueError('prime p>=13, p=1 mod4 required')
    return (p+7)//8 if p % 8 == 1 else (p+3)//8


def primary_split(u, p):
    """Exact prime-power Q/Z split. Return primary numerator, p-power, cofiber."""
    if not prime(p):
        raise ValueError('prime required')
    u = F(u) % 1
    denominator = u.denominator
    power = 1
    while denominator % p == 0:
        power *= p
        denominator //= p
    a = u.numerator * pow(denominator, -1, power) % power if power > 1 else 0
    cofiber = (u-F(a, power)) % 1
    assert cofiber.denominator % p
    return a, power, cofiber


def first_period(p, values=None):
    b, d = birth(p), order(p)
    assert b+d <= (p+1)//2
    if values is None:
        values = orbit(b+d-1)
    phases = values[b:b+d]
    primary, cofiber = [], []
    for u in phases:
        a, power, v = primary_split(u, p)
        assert power == p
        primary.append(F(a, p))
        cofiber.append(v)
    assert len(set(primary)) == d
    initial = 4 if p % 8 == 1 else -1
    assert all(primary[j] == F(initial*pow(16,j,p) % p,p) for j in range(d))
    return b, phases, primary, cofiber


def nearest_complement(a, modulus, D):
    """Nearest D-grid restoration of a/modulus; modulus and D coprime."""
    from math import gcd
    if modulus <= 1 or D <= 0 or gcd(modulus,D) != 1:
        raise ValueError('positive coprime conductors required')
    a %= modulus
    # round D*a/modulus to nearest integer (exact tie convention irrelevant
    # for odd modulus). The residual is signed in [-1/(2D),1/(2D)].
    nearest = (2*D*a+modulus)//(2*modulus)
    b = (-nearest) % D
    z = F(a,modulus)-F(nearest,D)
    assert abs(z) <= F(1,2*D)
    assert (F(a,modulus)+F(b,D)-z).denominator == 1
    return b,z


def twist_energy_certificate(phases, p):
    """Exact coefficient proof for (1/p) sum_t |S(h+tD)|² = L.

    Coefficients in t are tested symbolically. No floating point identity is
    accepted as the proof. This applies when all p-primary numerators differ.
    """
    split = [primary_split(u,p) for u in phases]
    if any(power != p for _,power,_ in split):
        raise ValueError('all phases must have conductor p exactly once')
    numerators = [a for a,_,_ in split]
    if len(set(numerators)) != len(phases):
        raise ValueError('repeated primary residues require collision energy')
    D = lcm(*(v.denominator for _,_,v in split))
    assert D % p
    for i,u in enumerate(phases):
        for j,v in enumerate(phases):
            # The t-character vanishes after summing t precisely off diagonal.
            turn = (D*(u-v)) % 1
            assert (turn == 0) == (i == j)
            assert (p*turn).denominator == 1
    return {'length':len(phases), 'mean_square':len(phases),
            'twists':p, 'step':D, 'off_diagonal_terms_annihilated':len(phases)*(len(phases)-1)}


def arctan_interval(inverse, terms):
    x = F(1,inverse)
    total = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)), F())
    other = total + (-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(total,other),max(total,other)


@lru_cache(None)
def pi_interval():
    a,b = arctan_interval(5,35)
    c,d = arctan_interval(239,12)
    # Machin identity plus alternating-series errors. Coarsening outward keeps
    # Taylor rational denominators small without relying on decimal pi digits.
    lo,hi = 16*a-4*d,16*b-4*c
    scale = 10**30
    return F((lo*scale).__floor__(),scale),F((hi*scale).__ceil__(),scale)


def trig_interval(turn):
    """Return certified cos/sin intervals for exp(2*pi*i*turn).

    Center and round the rational turn to denominator 10^16; its angular error
    is bounded using pi<22/7. Taylor at the rational midpoint angle is bounded
    by the first omitted absolute term (Taylor-Lagrange, derivatives <=1).
    """
    turn = F(turn) % 1
    if turn > F(1,2):
        turn -= 1
    scale = 10**16
    grid = F((turn*scale+F(1,2)).__floor__(),scale)
    pl,pu = pi_interval()
    theta = (pl+pu)*grid
    angle_error = 2*F(22,7)*abs(turn-grid)+(pu-pl)*abs(grid)
    cos_total, sin_total = F(1),theta
    cos_term,sin_term=F(1),theta
    for k in range(1,24):
        cos_term *= -theta*theta/F((2*k-1)*(2*k))
        sin_term *= -theta*theta/F((2*k)*(2*k+1))
        cos_total += cos_term
        sin_total += sin_term
    cos_error = abs(cos_term*theta*theta/F(47*48))+angle_error
    sin_error = abs(sin_term*theta*theta/F(48*49))+angle_error
    # The omitted cos term uses denominator 47*48; sin uses 48*49.
    return ((cos_total-cos_error,cos_total+cos_error),
            (sin_total-sin_error,sin_total+sin_error))


def char_sum_box(phases,h=1):
    rl=rh=il=ih=F()
    for u in phases:
        (a,b),(c,d)=trig_interval(h*u)
        rl,rh,il,ih=rl+a,rh+b,il+c,ih+d
    return (rl,rh),(il,ih)


def square_interval(interval):
    lo,hi=interval
    return (F() if lo<=0<=hi else min(lo*lo,hi*hi),max(lo*lo,hi*hi))


def sqrt_interval(interval, digits=12):
    lo,hi=interval
    if lo<0:
        raise ValueError('nonnegative interval required')
    scale=10**digits
    lower=isqrt((lo*scale*scale).__floor__())
    upper=isqrt((hi*scale*scale).__ceil__())+1
    return F(lower,scale),F(upper,scale)


def magnitude_interval(box):
    x=square_interval(box[0]);y=square_interval(box[1])
    return sqrt_interval((x[0]+y[0],x[1]+y[1]))


def variation_interval(phases,h=1):
    lo=hi=F()
    for a,b in zip(phases,phases[1:]):
        cos=trig_interval(h*(b-a))[0]
        ll,uu=sqrt_interval((max(F(),2-2*cos[1]),min(F(4),2-2*cos[0])))
        lo+=ll;hi+=uu
    return lo,hi


def interaction_interval(phases,h=1):
    if len(phases)<2:
        raise ValueError('at least two phases')
    lo=hi=F()
    for a,b in zip(phases,phases[1:]):
        l,u=trig_interval(h*(b-a))[0]
        lo+=1-u;hi+=1-l
    d=len(phases)-1
    return lo/d,hi/d


def coherent_dyadic_control(first,last,extra=8):
    """Reproduce all-odd-primary finite-coherence and eventual-circle aliasing.

    Use only rational BBP series partial sum; at n<=last the omitted positive
    Green tail and dyadic rounding have explicitly bounded phase lifts.
    This is a changed seed, not an authentic-source counterexample.
    """
    if not (1<=first<=last) or extra<1:
        raise ValueError('ordered positive window and extra depth required')
    M=last+extra
    partial=sum((source(n)/16**n for n in range(1,M+1)),F())
    # partial < pi/16 < partial+16^-M/(8M+1)^2.
    denominator=16**M
    seed=-F((partial*denominator).__floor__(),denominator)
    # delta = seed+pi/16 is positive and strictly below this rational bound.
    delta_upper=F(1,denominator)*(1+F(1,(8*M+1)**2))
    pure_upper=16**last*delta_upper
    bare_lower=-F(1,(8*first+1)**2)
    assert pure_upper<F(2,16**extra)
    original=orbit(M)
    changed=orbit(M,seed)
    for n in range(M+1):
        difference=(changed[n]-original[n])%1
        assert difference.denominator & (difference.denominator-1) == 0
    assert all(changed[n]==original[n] for n in range(M,M+1))
    for n in range(first,last+1):
        z=changed[n]
        assert z<=pure_upper or z>=1+bare_lower
    return {'first':first,'last':last,'depth':M,'seed':seed,
            'pure_phase_upper':pure_upper,'bare_lift_lower':bare_lower,
            'bare_lift_upper':pure_upper,'alias_from':M,
            'changed_phases':changed[first:last+1],
            'original_phases':original[first:last+1]}

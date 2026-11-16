"""Exact, source-typed SUCC observation instruments; NO claim of pi normality.

P = pointed four-pole BBP and its exact digit enclosures; stochasticity
appears only in declared observer choices/readouts. Oily grade -> harmonic
frequency is a proposed instrument, not a BBP dynamical intertwiner.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from math import lcm


def _nat(n, minimum=0):
    if type(n) is not int or n < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return n


def forcing(n: int) -> Q:
    _nat(n, 1)
    return (Q(4,8*n-7) - Q(2,8*n-4)
            -Q(1,8*n-3) - Q(1,8*n-2))


def original_state(n: int) -> Q:
    _nat(n)
    state = Q(0)
    for j in range(1,n+1):
        state=16*state+forcing(j)
    return state


def selected_hex_digits(depth: int, max_refinements=60) -> tuple[int,...]:
    """Certify first `depth` base-16 digits of x=pi/16, from zero-seeded source.

    Uses exact BBP moment positivity/monotonicity imported from SUCC.
    Does NOT read decimal pi or digits supplied by a foreign oracle.
    """
    _nat(depth,1)
    _nat(max_refinements,1)
    p=Q(0)
    scale=16**depth
    for n in range(1,depth+max_refinements+1):
        p+=forcing(n)/16**n
        upper=p+forcing(n+1)/Q(15*16**n)
        lower_value=(scale*p).__floor__()
        if lower_value==(scale*upper).__floor__():
            val=lower_value
            return tuple((val//16**(depth-1-i))%16 for i in range(depth))
    raise RuntimeError("UNRESOLVED precision budget, not a digit obstruction")


def source_shell_words(B: int, length: int) -> tuple[tuple[int,...],...]:
    _nat(B,1)
    _nat(length,1)
    digs=selected_hex_digits(2*B+length)
    return tuple(tuple(digs[n:n+length]) for n in range(B,2*B))


def oily_grade(j: int) -> Q:
    _nat(j)
    return Q(j+1,2**(j+2))


def oily_harmonic(h: int) -> Q:
    _nat(h,1)
    return Q(h+1,3*2**h)


def oily_tail(H: int) -> Q:
    """Probability mass on harmonics h>H in the nonzero Oily2 grade."""
    _nat(H,0)
    return Q(H+3,3*2**H)


def oily_mean_h() -> Q:
    return Q(8,3)


def gamma_frequency_kernel(z: complex) -> complex:
    """Presentation-only complex kernel; math tests use independent exact grid."""
    if abs(z)>1+1e-12:
        raise ValueError("circle or disk only")
    return (4/(2-z)**2-1)/3


def source_all_mode_transfer_budget(B: int) -> Q:
    """|OilyEnergy(completed pi shell)-OilyEnergy(rational U shell)|.

    Uses strict T_n<1/(64*n^2), 2*pi<7 and E_q[h]=8/3.
    """
    _nat(B,1)
    return Q(7,12*B**2)


def haar_next_digit_detail(words: tuple[tuple[int,...],...], k: int) -> Q:
    """One 16-ary Haar collision energy at depth k; exact Fraction.

    H_k=(16 sum_{|v|=k+1}p(v)^2 - sum_{|v|=k}p(v)^2)/15.
    """
    _nat(k)
    if not words or any(len(w)<=k for w in words):
        raise ValueError("All samples need at least k+1 digits")
    if any(type(c) is not int or not 0<=c<16 for w in words for c in w):
        raise ValueError("Radix-16 integer digit required")
    B=len(words)
    parents=Counter(w[:k] for w in words)
    children=Counter(w[:k+1] for w in words)
    numerator=16*sum(n*n for n in children.values()) - sum(n*n for n in parents.values())
    if numerator<0:
        raise AssertionError("Haar Parseval nonnegativity violated")
    return Q(numerator,15*B*B)


def haar_pair_response(left: tuple[int,...],right: tuple[int,...],k: int) -> Q:
    """Unbiased single-pair response from the full child-character bank."""
    _nat(k)
    if len(left)<=k or len(right)<=k:
        raise ValueError("Need next-digit readouts")
    if left[:k]!=right[:k]:
        return Q(0)
    return Q(1) if left[k]==right[k] else Q(-1,15)


def haar_pair_oracle(words: tuple[tuple[int,...],...], k: int) -> Q:
    """Independent pair enumeration, no histograms or Fourier computation."""
    return sum((haar_pair_response(a,b,k) for a in words for b in words),Q(0))/len(words)**2


def haar_volume_energy(words:tuple[tuple[int,...],...], K:int) -> tuple[Q,Q]:
    """Depth 0..K-1 Haar energy, and exact upper bound 2^-K for tail."""
    _nat(K,1)
    if any(len(w)<K for w in words):
        raise ValueError("Insufficient depth")
    value=sum((Q(1,2**(k+1))*haar_next_digit_detail(words,k)
               for k in range(K)),Q(0))
    assert Q(0)<=value<=Q(1)
    return value,Q(1,2**K)


def q4_complex_character(numer: int) -> tuple[int,int]:
    """i**numer, as a pair of exact integer real/imag components."""
    return ((1,0),(0,1),(-1,0),(0,-1))[numer%4]


def quarter_grid_weyl(phases:tuple[int,...],h:int)->tuple[Q,Q]:
    """e(h z) averaged for z=phases[n]/4 (exact Gaussian rationals)."""
    _nat(h,1)
    if not phases or any(type(x)is not int or not 0<=x<=3 for x in phases):
        raise ValueError("Quarter-grid labels 0..3")
    v=[q4_complex_character(h*x) for x in phases]
    return Q(sum(x[0] for x in v),len(v)),Q(sum(x[1] for x in v),len(v))


def quarter_grid_harmonic_energy(phases:tuple[int,...],h:int)->Q:
    r,i=quarter_grid_weyl(phases,h)
    return r*r+i*i


def quarter_grid_oily_energy(phases:tuple[int,...],H:int)->tuple[Q,Q]:
    _nat(H,1)
    value=sum((oily_harmonic(h)*quarter_grid_harmonic_energy(phases,h)
               for h in range(1,H+1)),Q(0))
    assert Q(0)<=value<=1
    return value,oily_tail(H)


def quarter_grid_oily_pair_oracle(phases:tuple[int,...],H:int)->Q:
    _nat(H,1)
    B=len(phases)
    ans=Q(0)
    for h in range(1,H+1):
        pair=Q(sum(q4_complex_character(h*(a-b))[0]
                   for a in phases for b in phases),B*B)
        ans+=oily_harmonic(h)*pair
    return ans


def quarter_grid_gram_purity(phases:tuple[int,...],H:int)->Q:
    """D/H=2 sum_{h=1}^{H-1}(1-h/H)|W(h)|²."""
    _nat(H,2)
    return sum((Q(2*(H-h),H)*quarter_grid_harmonic_energy(phases,h)
                for h in range(1,H)),Q(0))


def quarter_grid_gram_pair_oracle(phases:tuple[int,...],H:int)->Q:
    """Independent direct Fejer pair kernel: avg(F_H(delta))/H - 1."""
    _nat(H,2)
    B=len(phases)
    def fejer(delta):
        points=[q4_complex_character(k*delta) for k in range(H)]
        return sum(z[0] for z in points)**2+sum(z[1] for z in points)**2
    return Q(sum(fejer(a-b) for a in phases for b in phases),H*B*B)-1


def exact_digit_changes(digits:tuple[int,...],B:int,k:int)->Q:
    """Fraction changed between digits d_n,d_(n+k) in n in [B,2B)."""
    _nat(B,1)
    _nat(k,1)
    if len(digits)<2*B+k:
        raise ValueError("Digit precision insufficient")
    return Q(sum(digits[n]!=digits[n+k] for n in range(B,2*B)),B)


def exact_binary_changes(digits:tuple[int,...],B:int)->Q:
    """R0 binary change rate in [4B,8B), using source hex digits."""
    _nat(B,1)
    if len(digits)<2*B+1:
        raise ValueError("Need next digit for trailing binary bit")
    binary=[]
    for d in digits:
        binary.extend((d>>3&1,d>>2&1,d>>1&1,d&1))
    return Q(sum(binary[m]!=binary[m+1] for m in range(4*B,8*B)),4*B)


def conductor_births(N:int)->tuple[bool,...]:
    """Real source denominator births, not arbitrary fake-prime events."""
    _nat(N,1)
    size=1
    out=[]
    for n in range(1,N+1):
        new=lcm(size,forcing(n).denominator)
        out.append(new>size)
        size=new
    return tuple(out)


def finite_witness_detect(values,chosen_indices=None):
    """One-sided negative certificate on supplied proved signed values only.

    Does NOT evaluate the completed Weil form; values must come from
    an independent actual original-source rigorous-sign instrument.
    """
    if chosen_indices is None:
        chosen_indices=range(len(values))
    for j in chosen_indices:
        q=values[j]
        if type(q) not in (int,Q):
            raise ValueError("Exact rational or rigorously verified sign required")
        if q<0:
            return j
    return None


def propensity_corrected_mean(probe_law: tuple[Q,...], response: tuple[Q,...])->Q:
    """Exact expectation of a single Horvitz-Thompson probe of a uniform target.

    Returns sum_{a} pi(a)*response[a]/(N*pi(a)); a missing probe
    invalidates identification of the full uniform target.
    """
    if len(probe_law)!=len(response) or not response:
        raise ValueError("Every source position must have one probability")
    if any(type(q) not in (Q,int) or q<=0 for q in probe_law):
        raise ValueError("Probe support must be full and positive")
    if sum(probe_law,Q(0))!=1:
        raise ValueError("Probe distribution must sum to one")
    if any(type(x) not in (Q,int) for x in response):
        raise ValueError("Exact observable values required")
    N=len(response)
    return sum((probe_law[a]*response[a]/(N*probe_law[a]) for a in range(N)),Q(0))

# Rational trigonometric enclosures: a finite certified readout, not an
# assumption that pi itself has a known digit distribution.
from math import factorial as _factorial

def atan_interval_reciprocal(denominator: int, terms:int=12)->tuple[Q,Q]:
    _nat(denominator,2)
    _nat(terms,1)
    x=Q(1,denominator)
    partial=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    next_term=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(partial,partial+next_term),max(partial,partial+next_term)

def machin_pi_interval(terms:int=12)->tuple[Q,Q]:
    """From classical identity pi=16 atan(1/5)-4 atan(1/239)."""
    a,b=atan_interval_reciprocal(5,terms),atan_interval_reciprocal(239,terms)
    lo,hi=16*a[0]-4*b[1],16*a[1]-4*b[0]
    if not Q(3)<lo<hi<Q(22,7):
        raise AssertionError("Machin source interval failed")
    return lo,hi

def certified_unit_character(q:Q, pi_interval:tuple[Q,Q], degree:int=12)->tuple[Q,Q,Q]:
    """Return rational complex approximation + absolute error per component.

    Actual character is exp(2*pi*i*q), and each component's difference
    from returned approximation is <= returned error.
    """
    _nat(degree,2)
    if type(q) not in (int,Q):
        raise ValueError("Exact rational phase required")
    a=Q(q)%1
    if a>Q(1,2):a-=1
    lo,hi=pi_interval
    if type(lo) is not Q or type(hi) is not Q or not 3<lo<hi<Q(22,7):
        raise ValueError("Certified rational pi interval required")
    phase=a*(lo+hi)
    phase_error=abs(a)*(hi-lo)
    cos=sum((Q((-1)**j,_factorial(2*j))*phase**(2*j) for j in range(degree+1)),Q(0))
    sin=sum((Q((-1)**j,_factorial(2*j+1))*phase**(2*j+1) for j in range(degree+1)),Q(0))
    cos_error=abs(phase)**(2*degree+2)/_factorial(2*degree+2)+phase_error
    sin_error=abs(phase)**(2*degree+3)/_factorial(2*degree+3)+phase_error
    return cos,sin,max(cos_error,sin_error)

def certified_original_oily_energy(B:int,H:int,*,machin_terms:int=12,taylor_degree:int=12)->dict:
    """Rigorous rational interval for COMPLETE Oily energy of selected pi shell.

    Error pays each truncated frequency, original rational U -> completed
    pi Green tail over *all harmonics*, and Taylor/Machin rounding.
    Heavy at large B: use limited certified epochs, no asymptotic claim.
    """
    _nat(B,1)
    _nat(H,1)
    pi_box=machin_pi_interval(machin_terms)
    value=Q(0);trig_err=Q(0)
    states=[original_state(n) for n in range(B,2*B)]
    for h in range(1,H+1):
        cos_sum=Q(0);sin_sum=Q(0);delta=Q(0)
        for u in states:
            c,s,e=certified_unit_character(h*u,pi_box,taylor_degree)
            cos_sum+=c;sin_sum+=s;delta+=e
        rr,ii=cos_sum/B,sin_sum/B
        d=delta/B
        weight=oily_harmonic(h)
        value+=weight*(rr*rr+ii*ii)
        trig_err+=weight*(4*d+2*d*d)
    total_err=trig_err+oily_tail(H)+source_all_mode_transfer_budget(B)
    return {
        'B':B,'H':H,
        'lower':max(Q(0),value-total_err),
        'upper':min(Q(1),value+total_err),
        'raw_rational_source_estimate':value,
        'trigonometric_error':trig_err,
        'unseen_harmonic_tail':oily_tail(H),
        'original_source_transport_budget':source_all_mode_transfer_budget(B),
        'pi_interval':pi_box,
        'claim':'CERTIFIED-FINITE / pi-normality OPEN',
    }

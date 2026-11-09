"""Source-authenticated prime-clock / real-carry arithmetic and spectral probes.

Research only: a prime clock's phase or carry is NOT a real BBP digit.
All recurrence identities use exact Fraction; Fourier diagnostics use complex floats.
The original four signed BBP poles and literal zero seed remain unchanged.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt, pi, log, sqrt, lcm
from cmath import exp
from typing import Sequence

from .duck_bbp import forcing

CHANNELS = ((3, 2), (4, 1), (5, 1))


def positive_parts(n: int) -> tuple[Fraction, Fraction, Fraction]:
    if type(n) is not int or n < 1:
        raise ValueError("source time n must be >=1")
    a = 8*n - 7
    return tuple(Fraction(w*d, a*(a+d)) for d, w in CHANNELS)


def prime_check(p: int) -> bool:
    if type(p) is not int or p < 2:
        return False
    return all(p % j for j in range(2, isqrt(p)+1))


def balanced_boundaries(A: int, p: int) -> tuple[int, int, int, int, int]:
    if type(A) is not int or A < 16 or not prime_check(p) or p <= 5 or p % 8 != 1:
        raise ValueError("A>=16, authenticated p=1 mod8, p>5 needed")
    k = (p-1)//8
    t = (A, 4*k+1, 5*k+1, 6*k+1, 2*A)
    if not t[0] < t[1] < t[2] < t[3] < t[4] or k+1 > A:
        raise ValueError("p is not a complete four-stage balanced clock on [A,2A)")
    if p*p <= 16*A:
        raise ValueError("simple p-pole regime p^2 > 16A required")
    return t


def p_unit_residue(fr: Fraction, p: int) -> int:
    """p*fr mod p, only in the p^(-1) simple-pole regime."""
    q = p*Fraction(fr)
    if q.denominator % p == 0:
        raise ValueError("p^2-pole or invalid p-adic source term")
    return q.numerator * pow(q.denominator, -1, p) % p


def frac_floor(q: Fraction) -> int:
    return q.numerator // q.denominator


@dataclass(frozen=True)
class CarryRecord:
    n: int
    real_carry: int
    prime_carry: int
    carry_slip: int
    residue: int
    injection: int
    source: Fraction
    real_phase: Fraction
    cofactor: Fraction
    channel_residues: tuple[int, int, int]
    channel_carries: tuple[int, int, int]
    channel_injections: tuple[int, int, int]
    junction: int
    junction_previous: int
    injection_wrap: int


def replay_epoch(A: int, p: int, seed: Fraction = Fraction(0),
                 lookahead: int = 0) -> tuple[CarryRecord, ...]:
    """Exact zero/selected-seed BBP phase and all 3 prime channels through [A,2A).

    All seed shifts with denominator prime to p have the SAME p-primary
    histories. No p-adic irrational embedding or pi oracle is used.
    """
    balanced_boundaries(A, p)
    if type(lookahead) is not int or lookahead < 0:
        raise ValueError("nonnegative lookahead required")
    if 2*A + lookahead >= ((p-1)//8 + 1) + p:
        raise ValueError("lookahead reaches next p-shell")
    if p*p <= 8*(2*A+lookahead):
        raise ValueError("lookahead leaves simple p-pole regime")
    seed = Fraction(seed)
    if seed.denominator % p == 0:
        raise ValueError("seed is not p-integral")
    x = seed % 1
    c = 0
    ci = (0, 0, 0)
    tau = 0
    out = []
    for n in range(1, 2*A+lookahead):
        r = forcing(n)
        parts = positive_parts(n)
        if sum(parts) != r:
            raise AssertionError("original source passport changed")
        jj = tuple(p_unit_residue(v, p) for v in parts)
        j = p_unit_residue(r, p)
        wrap = (sum(jj)-j)//p
        zi = tuple((16*v+t)//p for v,t in zip(ci, jj))
        new_ci = tuple((16*v+t)%p for v,t in zip(ci, jj))
        new_tau = sum(new_ci)//p
        prime_carry = (16*c+j)//p
        c_new = (16*c+j)%p
        if c_new != sum(new_ci)%p:
            raise AssertionError("scalar and channel p-residues disagree")
        if prime_carry != sum(zi)+new_tau-16*tau-wrap:
            raise AssertionError("three-channel carry-gluing equation failed")
        prev_cofactor = x-Fraction(c,p)
        raw = 16*x+r
        kappa = frac_floor(raw)
        x_new = raw-kappa
        b_new = x_new-Fraction(c_new,p)
        if b_new-16*prev_cofactor != r-Fraction(j,p)-(kappa-prime_carry):
            raise AssertionError("real/prime carry-cofactor cocycle failed")
        if n >= A:
            out.append(CarryRecord(n,kappa,prime_carry,kappa-prime_carry,
                       c_new,j,r,x_new,b_new,new_ci,zi,jj,new_tau,tau,wrap))
        x,c,ci,tau = x_new,c_new,new_ci,new_tau
    return tuple(out)


def stage_events(records: Sequence[CarryRecord]) -> tuple[tuple[int,int,int,int], ...]:
    return tuple((r.n,r.injection,r.prime_carry,r.real_carry)
                 for r in records if r.injection)


def digit_word_counts(records: Sequence[CarryRecord], depth: int, *, prime: bool) -> Counter:
    if type(depth) is not int or depth < 1 or depth > len(records):
        raise ValueError("1<=depth<=number of records")
    vals = [int((r.prime_carry if prime else r.real_carry) % 16) for r in records]
    return Counter(tuple(vals[i:i+depth]) for i in range(len(vals)-depth+1))


def digit_tv_uniform(counts: Counter, depth: int) -> Fraction:
    """Exact finite total variation from uniform over 16^depth words."""
    N = sum(counts.values())
    if N < 1 or type(depth) is not int or depth < 1:
        raise ValueError("nonempty and depth>=1 required")
    B = 16**depth
    return Fraction(sum(abs(B*c-N) for c in counts.values()) +
                    (B-len(counts))*N, 2*B*N)


def complex_char(h: int, z: int) -> complex:
    return exp(2j*pi*(h*z % 16)/16)


def signed_carry_covariance(records: Sequence[CarryRecord], h: int) -> dict:
    """Exact algebraic covariance structure, numerically evaluated."""
    N = len(records)
    if N==0 or type(h) is not int or h%16==0:
        raise ValueError("nonempty epoch, h nonzero mod16")
    prime = [complex_char(h,r.prime_carry) for r in records]
    slip = [complex_char(h,r.carry_slip) for r in records]
    real = [complex_char(h,r.real_carry) for r in records]
    am=sum(prime)/N
    bm=sum(slip)/N
    wm=sum(real)/N
    cov=sum(a*b for a,b in zip(prime,slip))/N-am*bm
    assert abs(wm-(cov+am*bm))<2e-12
    return {"real_mean":wm, "prime_mean":am,"slip_mean":bm,
            "signed_covariance":cov, "reconstruction_error":abs(wm-(cov+am*bm))}


def pulse_formula(p: int) -> tuple[tuple[int,int], ...]:
    """The three actual p-birth events WITHIN the balanced epoch."""
    if p%8 != 1 or not prime_check(p):
        raise ValueError("p=1 mod8 prime needed")
    k=(p-1)//8
    return ((4*k+1,(-1*pow(2,-1,p))%p),
            (5*k+1,(-1*pow(5,-1,p))%p),
            (6*k+1,(-1*pow(6,-1,p))%p))


def shadow_seed(A: int, extra: int = 10, bits: int = 80) -> Fraction:
    """Exact epoch-dependent p-integral coherent counterfeit, NO pi oracle.

    Used only to refute claims derived from p-primary phases alone.
    """
    if type(A) is not int or A < 16 or extra < 1 or bits < 1:
        raise ValueError("positive clock/margins required")
    N=2*A+extra
    M=8*A+bits
    alpha=sum((forcing(n)/16**n for n in range(1,N+1)),Fraction(0))
    y=alpha*(1<<M)
    return -Fraction(frac_floor(y),1<<M)


def shadow_negative_certificate(A: int, seed: Fraction,
                                extra: int = 10, bits: int = 80) -> bool:
    """Rational sign enclosures for U_n(seed) in (-1,0) at [A-1,2A).

    Exact sufficient proof: alpha=sum16^-j r(j) and tail<16^-N/(15(N+1)^2).
    T_n > r(n+1)/16, T_n < r(n+1)/15 for all n in the epoch.
    """
    N=2*A+extra
    alpha=sum((forcing(j)/16**j for j in range(1,N+1)),Fraction(0))
    rem=Fraction(1,15*(N+1)**2*16**N)
    delta_low=seed+alpha
    delta_high=delta_low+rem
    if not 0<=delta_low<=Fraction(1,1<<(8*A+bits)) or delta_high<0:
        return False
    # Since both 16^n and 1/(n+1)^2 are monotonic within the epoch,
    # direct rational checks can be kept as a hostile finite certificate.
    for n in range(A-1,2*A):
        lo=16**n*delta_low-forcing(n+1)/15
        hi=16**n*delta_high-forcing(n+1)/16
        if not -1<lo or not hi<0:
            return False
    return True


def stage_prime_digit_bound(A: int, p: int, depth: int,
                            subgroup_delta: float) -> float:
    """Conditional analytic per-word bound from BEC-04 and exact discrete Fourier.

    delta is the declared imported complete-subgroup additive-character bound;
    NOT computed by this function and NOT a proof it holds for any chosen p.
    """
    balanced_boundaries(A,p)
    if type(depth) is not int or depth < 1 or subgroup_delta < 0:
        raise ValueError("valid word depth and nonnegative certified delta")
    # m is multiplicative order of 16 modulo p, exactly computed finite.
    z=16%p;m=1
    while z!=1:
        z=z*16%p;m+=1
    return 1/p+(1+log(p))*(subgroup_delta+
            4*sqrt(p)*(2+log(m))/A)+8*depth/A


def chrono_stage_counts(records: Sequence[CarryRecord], A: int,p: int,
                        depth: int) -> dict:
    """Observed forward words with a break at prime-birth edges, never reconnected."""
    bounds=balanced_boundaries(A,p)
    counts=[]
    for i in range(4):
        left,right=bounds[i],bounds[i+1]
        sub=[r for r in records if left<=r.n<right]
        clean=[r for r in sub if r.injection==0]
        # Exclude any start with a birth within its word; a short stage has
        # a natural truncation, no cyclic wrapping across the birth boundary.
        words=[]
        for j in range(len(sub)-depth+1):
            window=sub[j:j+depth]
            if all(r.injection==0 for r in window):
                words.append(tuple(r.prime_carry%16 for r in window))
        counts.append({"stage":i+1,"interval":[left,right],"windows":len(words),
                       "distinct_words":len(set(words)),
                       "tv_uniform":str(digit_tv_uniform(Counter(words),depth)) if words else None})
    return {"depth":depth,"stages":counts}


# The first-shell rational channel normalizers are inherited from #554.
STAGE_RATIONAL_SLOPES = ((2, 1, 1), (3, 2, 2),
                         (15, 8, 10), (45, 24, 25))
STAGE_COMMON_DENOMINATORS = (1, 2, 10, 30)


def stage_index(n: int, A: int, p: int) -> int:
    bounds = balanced_boundaries(A,p)
    if not (A <= n < 2*A):
        raise ValueError("n must be in balanced epoch")
    return next(i for i in range(4) if bounds[i] <= n < bounds[i+1])


def predicted_channel_residues(n: int, A: int, p: int) -> tuple[int,int,int]:
    """Prime-Frobenius 3-channel source normalizer, no stored orbit phases."""
    i=stage_index(n,A,p)
    a=STAGE_RATIONAL_SLOPES[i]
    D=STAGE_COMMON_DENOMINATORS[i]
    first=(p-1)//8+1
    u=(pow(16,n-first,p)*pow(D,-1,p))%p
    return tuple((v*u)%p for v in a)


def junction_law_exact(slope: tuple[int,int,int]) -> tuple[Fraction,Fraction,Fraction]:
    """Exact Lebesgue law for floor(sum_j frac(slope_j*t)), 0<=t<1.

    Finite sum over lcm cells; no numerical integration or statistical fit.
    Reflection t->1-t proves mass[0]==mass[2].
    """
    if len(slope)!=3 or any(type(x) is not int or x<1 for x in slope):
        raise ValueError("three positive integer slopes")
    L=lcm(*slope)
    S=sum(slope)
    mass0=Fraction(0)
    for m in range(L):
        low=Fraction(m,L)
        high=Fraction(m+1,L)
        floors=sum(v*m//L for v in slope)
        cap=Fraction(1+floors,S)
        mass0+=max(Fraction(0),min(high,cap)-low)
    return mass0,1-2*mass0,mass0


def weighted_junction_law() -> tuple[Fraction,Fraction,Fraction]:
    """Limit under the 12/5 balanced stage proportions of #554."""
    weights=(Fraction(1,5),Fraction(3,10),Fraction(3,10),Fraction(1,5))
    parts=[junction_law_exact(a) for a in STAGE_RATIONAL_SLOPES]
    return tuple(sum((weights[s]*parts[s][i] for s in range(4)),Fraction(0))
                 for i in range(3))


def junction_phase_mean(h: int, prob: tuple[Fraction,Fraction,Fraction]) -> complex:
    """Predicted spectral line at the junction, not at the real BBP digit."""
    if len(prob)!=3 or sum(prob)!=1:
        raise ValueError("probability triple needed")
    return sum(float(x)*complex_char(h,j) for j,x in enumerate(prob))


def conditional_prime_digit_bound(A: int, p: int, depth: int,
                                  subgroup_delta: float) -> tuple[float,float]:
    """Per-word and total-variation UPPER BOUNDS for A forward starts.

    Source/prime conditions: the four BEC stages of p=1mod8, lookahead
    depth-1 remains in first simple-pole shell, and delta is an AUTHENTIC
    proved bound for complete nonzero additive subgroup character means.
    BEC-04 controls each clean chronological interval, the exact finite
    Fourier transform of a contiguous p-grid interval costs ≤1+log(p),
    and at most 3*depth starting words touch the three p-birth events.
    No local->real carry agreement is assumed.
    """
    balanced_boundaries(A,p)
    if type(depth) is not int or not (1<=depth<=A//4):
        raise ValueError("1<=depth<=A/4")
    if 2*A + depth-1 >= ((p-1)//8+1)+p:
        raise ValueError("depth crosses first p-shell")
    eps=stage_prime_digit_bound(A,p,depth,subgroup_delta)
    return eps,min(1.0,16**depth*eps/2)


def renormalized_boundary_balance(records: Sequence[CarryRecord], p: int) -> dict:
    """EXACT 16^-n cohomological boundary identities on any contiguous segment.

    Normalized by 16^first to keep modest rational denominators. This does
    not assert anything about UNWEIGHTED temporal signed covariances.
    """
    if not records or not prime_check(p):
        raise ValueError("contiguous nonempty records, p prime")
    a=records[0].n
    b=records[-1].n
    if any(x.n!=a+i for i,x in enumerate(records)):
        raise ValueError("records must be consecutive")
    z_lhs=sum((Fraction(r.prime_carry-sum(r.channel_carries),16**(r.n-a))
               for r in records),Fraction(0))
    z_rhs=Fraction(records[-1].junction,16**(b-a))-16*records[0].junction_previous
    # First cocycle determines the previous real complementary chart exactly.
    first=records[0]
    Bprev=(first.cofactor-first.source+Fraction(first.injection,p)+
           first.carry_slip)/16
    b_lhs=sum((Fraction(r.carry_slip,16**(r.n-a)) for r in records),Fraction(0))
    forcing_phase=sum((Fraction(r.source-Fraction(r.injection,p),16**(r.n-a))
                       for r in records),Fraction(0))
    b_rhs=16*Bprev-Fraction(records[-1].cofactor,16**(b-a))+forcing_phase
    if z_lhs!=z_rhs or b_lhs!=b_rhs:
        raise AssertionError("renormalized carry/source boundary identity broken")
    return {"prime_three_channel_weighted_sum":z_lhs,
            "prime_three_channel_endpoints":z_rhs,
            "real_prime_weighted_slip":b_lhs,
            "real_prime_cofactor_endpoints_plus_forcing":b_rhs,
            "source_forcing_integral":forcing_phase}


def prime_order_16(p: int) -> int:
    if not prime_check(p) or p<=5:
        raise ValueError("p>5 genuine prime")
    z=16%p;m=1
    while z!=1:
        z=z*16%p;m+=1
    return m


def periodic_junction_symbol(p: int, stage: int, u: int) -> int:
    """Stage-resolved junction carries, indexed by exponent n-(p-1)/8-1.

    In each of the four exact first-shell regimes, the phase is a rational
    direction vector, and the clock is periodic with ord_p(16).
    """
    if not prime_check(p) or p<=5 or p%8!=1 or type(stage) is not int or not 0<=stage<4:
        raise ValueError("p=1mod8 prime, stage 0..3")
    a=STAGE_RATIONAL_SLOPES[stage]
    D=STAGE_COMMON_DENOMINATORS[stage]
    q=(pow(16,u,p)*pow(D,-1,p))%p
    return sum((v*q)%p for v in a)//p


def junction_emission_lines(p: int, stage: int, h: int = 8) -> tuple[complex, ...]:
    """Fourier coefficients of exactly periodic prime-junction symbol.

    Each coefficient is one finite p-clock spectral line; no randomness.
    """
    if type(h) is not int:
        raise ValueError("integer frequency")
    m=prime_order_16(p)
    vals=[complex_char(h,periodic_junction_symbol(p,stage,u)) for u in range(m)]
    return tuple(sum(vals[u]*exp(-2j*pi*j*u/m) for u in range(m))/m
                 for j in range(m))


def junction_epoch_line_response(A: int,p: int,h: int,t: int) -> complex:
    """Exact Fourier-window composition of four stage line families.

    Uses a direct finite geometric window sum for numerical stability; complex
    result is a diagnostic (the identity is finite Fourier inversion).
    """
    if type(t) is not int:
        raise ValueError("temporal harmonic must be integer")
    bounds=balanced_boundaries(A,p)
    m=prime_order_16(p)
    first=(p-1)//8+1
    total=0j
    for s,(left,right) in enumerate(zip(bounds,bounds[1:])):
        lines=junction_emission_lines(p,s,h)
        for j,coefficient in enumerate(lines):
            # sum_{n=left}^{right-1} exp(2pi i(j*(n-first)/m-t*(n-A)/A))
            q=exp(2j*pi*(j/m-t/A))
            start=exp(2j*pi*(j*(left-first)/m-t*(left-A)/A))
            length=right-left
            if (j*A-t*m)%(m*A)==0:
                window=start*length
            else:
                window=start*(1-q**length)/(1-q)
            total+=coefficient*window
    return total


def junction_direct_epoch_dft(records: Sequence[CarryRecord],h:int,t:int) -> complex:
    if not records:
        raise ValueError("nonempty source epoch")
    a=records[0].n
    N=len(records)
    return sum(complex_char(h,r.junction)*exp(-2j*pi*t*(r.n-a)/N)
               for r in records)


def spectral_resolvent_junction(records: Sequence[CarryRecord],z: complex) -> dict:
    """Exact algebra of the radix coboundary as a time-frequency filter.

    For J_n=tau_n-16*tau_{n-1}, its z-transform is filtered by
    (1-16z); this multiplier does not vanish on |z|=1.
    """
    if not records or any(r.n!=records[0].n+i for i,r in enumerate(records)):
        raise ValueError("contiguous nonempty source period needed")
    tau0=records[0].junction_previous
    L=len(records)
    J=sum((r.junction-16*r.junction_previous)*z**(i+1)
          for i,r in enumerate(records))
    T=tau0+sum(r.junction*z**(i+1) for i,r in enumerate(records))
    rhs=(1-16*z)*T-tau0+16*records[-1].junction*z**(L+1)
    # finite sum (1-16z)T -tau0 +16 tau_L z^(L+1)
    if abs(J-rhs)>1e-6*(1+abs(J)+abs(rhs)):
        raise AssertionError("finite spectral-resolvent identity failed")
    return {'junction_transform':J,'filtered_transform':rhs,
            'multiplier':1-16*z}

"""Source-anchored 16-by-16 hexadecimal pair transport and Fourier intertwiners.

Research only. Every scalar matrix is a two-digit observation, NOT a
normality theorem. Its fully faithful Yoneda-shaped lift has measure-valued
entries containing the entire residual tail. All source actions preserve
U_0=0 and the four original signed BBP poles (imported, never patched).

No randomness/Markov property is assumed for BBP digits. Complex Fourier
computations are diagnostics; exact integer pair-energy identities are the
certificates. Python 3.10+, standard library only.
"""
from __future__ import annotations

from collections import Counter
from cmath import exp
from fractions import Fraction
from math import pi
from typing import Sequence

RADIX = 16


def validate_digits(digits: Sequence[int], *, min_count: int = 2) -> None:
    if len(digits) < min_count or any(type(a) is not int or not 0 <= a < RADIX for a in digits):
        raise ValueError(f"at least {min_count} hexadecimal digits (integers 0..15) required")


def pair_counts(digits: Sequence[int], *, cyclic: bool = True) -> tuple[tuple[int, ...], ...]:
    """Original chronology. Cyclic convention buys exactly equal row/col margins."""
    validate_digits(digits)
    n = len(digits)
    out = [[0 for _ in range(RADIX)] for _ in range(RADIX)]
    for i in range(n if cyclic else n-1):
        out[digits[i]][digits[(i+1) % n]] += 1
    return tuple(tuple(row) for row in out)


def validate_counts(counts: Sequence[Sequence[int]]) -> int:
    if len(counts) != RADIX or any(len(row) != RADIX for row in counts):
        raise ValueError("expected a 16 x 16 count matrix")
    if any(type(v) is not int or v < 0 for row in counts for v in row):
        raise ValueError("counts must be nonnegative exact integers")
    n = sum(sum(row) for row in counts)
    if n < 1:
        raise ValueError("positive count total required")
    return n


def marginal_counts(counts: Sequence[Sequence[int]]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    validate_counts(counts)
    return (tuple(sum(row) for row in counts),
            tuple(sum(counts[a][b] for a in range(RADIX)) for b in range(RADIX)))


def difference_counts(counts: Sequence[Sequence[int]]) -> tuple[int, ...]:
    validate_counts(counts)
    return tuple(sum(counts[a][(a+d)%RADIX] for a in range(RADIX))
                 for d in range(RADIX))


def exact_energy_split(counts: Sequence[Sequence[int]]) -> dict[str, Fraction]:
    """Projection onto diagonal digit-translation invariants and complement.

    M_ab=C_ab/N, (Pi M)_ab=Q_(b-a)/(16N). Frobenius orthogonality gives
       256||M-J/256||² = 256||M-Pi M||²+256||Pi M-J/256||².
    All returned rational quantities are mathematical certificates, not fit.
    """
    n=validate_counts(counts)
    q=difference_counts(counts)
    full=Fraction(256*sum(c*c for row in counts for c in row)-n*n,n*n)
    relative=Fraction(16*sum(v*v for v in q)-n*n,n*n)
    basis=Fraction(sum((16*counts[a][b]-q[(b-a)%RADIX])**2
                       for a in range(RADIX) for b in range(RADIX)), n*n)
    if basis+relative!=full or min(basis,relative,full)<0:
        raise AssertionError("exact relative/basis orthogonal decomposition failed")
    p1=marginal_counts(counts)[0]
    one_digit=Fraction(16*sum(c*c for c in p1)-n*n,n*n)
    if one_digit>basis:
        raise AssertionError("single-digit imbalance must lie in basis-sensitive sector")
    return {"pair_energy":full,"relative_energy":relative,
            "basis_energy":basis,"one_digit_energy":one_digit}


def fourier_pair_modes(counts: Sequence[Sequence[int]]) -> tuple[tuple[complex,...], ...]:
    """Unnormalized character transform hat M(u,v)=sum_ab M_ab exp[-2pii(ua+vb)/16].

    The unitary 16x16 F has entries (1/4)exp(-2pii ua/16), so
    hat M = 16 F M F^T. A transpose, NOT conjugate transpose: both digit
    coordinates are transformed as characters. Source-oriented sign matters.
    """
    n=validate_counts(counts)
    chi=[[exp(-2j*pi*u*a/RADIX) for a in range(RADIX)] for u in range(RADIX)]
    result=[]
    for u in range(RADIX):
        row=[]
        for v in range(RADIX):
            row.append(sum(counts[a][b]*chi[u][a]*chi[v][b]
                           for a in range(RADIX) for b in range(RADIX))/n)
        result.append(tuple(row))
    return tuple(result)


def sector_energy_float(counts: Sequence[Sequence[int]]) -> dict[str,float]:
    """Diagnostic complex check; exact cert is exact_energy_split()."""
    z=fourier_pair_modes(counts)
    relative=sum(abs(z[u][(-u)%RADIX])**2 for u in range(1,RADIX))
    basis=sum(abs(z[u][v])**2 for u in range(RADIX)
              for v in range(RADIX) if (u+v)%RADIX != 0)
    return {"relative_energy":relative,"basis_energy":basis}


def primitive_order(h: int) -> int:
    if type(h) is not int:
        raise ValueError("integer Fourier index required")
    h%=RADIX
    if h==0: return 1
    from math import gcd
    return RADIX//gcd(RADIX,h)


def primitive_sector_masses(counts: Sequence[Sequence[int]]) -> dict[tuple[int,int],float]:
    """A 5x5 table of the 1,2,4,8,16 cyclotomic character order pair sectors."""
    z=fourier_pair_modes(counts)
    out={(a,b):0. for a in (1,2,4,8,16) for b in (1,2,4,8,16)}
    for u in range(RADIX):
        for v in range(RADIX):
            out[(primitive_order(u),primitive_order(v))]+=abs(z[u][v])**2
    return out


def de_bruijn_16(order: int) -> tuple[int,...]:
    """Deterministic classical de Bruijn cycle; pair-Haar may still be nonnormal."""
    if type(order) is not int or not 1<=order<=3:
        raise ValueError("order 1..3 only (bounded hostile controls)")
    a=[0]*(RADIX*order+1)
    seq=[]
    def db(t:int,p:int)->None:
        if t>order:
            if order%p==0:
                seq.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,RADIX):
                a[t]=j
                db(t+1,t)
    db(1,1)
    assert len(seq)==RADIX**order
    return tuple(seq)


def cyclic_word_energy(digits: Sequence[int], depth: int) -> Fraction:
    validate_digits(digits)
    if type(depth) is not int or not 1<=depth<=len(digits):
        raise ValueError("1 <= depth <= N")
    n=len(digits)
    counts=Counter(tuple(digits[(i+j)%n] for j in range(depth)) for i in range(n))
    return Fraction(RADIX**depth*sum(v*v for v in counts.values())-n*n,n*n)


def fractional_digits_of(x: Fraction, depth: int) -> tuple[int,...]:
    """Exact rational test carrier, using the half-open radix-cell convention."""
    if not isinstance(x,Fraction) or not 0<=x<1 or type(depth) is not int or depth<1:
        raise ValueError("rational x in [0,1), integer depth>=1")
    ds=[]
    for _ in range(depth):
        z=RADIX*x
        a=z.numerator//z.denominator
        ds.append(a)
        x=z-a
    return tuple(ds)


def two_digit_tail_lift(points: Sequence[Fraction]) -> dict[tuple[int,int,Fraction],Fraction]:
    """Measure-valued 16x16 carrier matrix: cell (a,b) is a measure on T²-tail.

    Returned dictionary codes M_ab({y}) for each actual rational test point.
    Scalar masses throw away y. The lift is injective on all Borel laws,
    not just these finite rational atomic test laws.
    """
    if not points or any(not isinstance(x,Fraction) or not 0<=x<1 for x in points):
        raise ValueError("nonempty rational points in [0,1) required")
    n=len(points)
    out:dict[tuple[int,int,Fraction],Fraction]={}
    for x in points:
        a,b=fractional_digits_of(x,2)
        y=(RADIX**2*x)%1
        key=(a,b,y)
        out[key]=out.get(key,Fraction())+Fraction(1,n)
    return out


def reconstruct_from_lift(lift:dict[tuple[int,int,Fraction],Fraction]) -> dict[Fraction,Fraction]:
    """Exact inverse mu=sum_ab (B_a o B_b)_* M_ab."""
    if not lift:raise ValueError("nonempty lift required")
    out:dict[Fraction,Fraction]={}
    for (a,b,y),weight in lift.items():
        if not (type(a) is int and 0<=a<RADIX and type(b) is int and 0<=b<RADIX
                and isinstance(y,Fraction) and 0<=y<1 and isinstance(weight,Fraction)
                and weight>=0):
            raise ValueError("invalid source tail atom")
        x=Fraction(RADIX*a+b, RADIX*RADIX)+y/(RADIX*RADIX)
        out[x]=out.get(x,Fraction())+weight
    if sum(out.values(),Fraction())!=1:
        raise ValueError("normalized lift required")
    return out


def _floor_char_coeff(m:int,h:int,shift:Fraction) -> complex:
    """Exact analytic character formula evaluated in complex precision.
    Uses the already proved SUCC FLP-03 law; f_0=1, not the 1/m formula.
    """
    if not isinstance(shift,Fraction) or not 0<=shift<1:
        raise ValueError("shift fraction in [0,1) required")
    h=h%RADIX
    if h==0:return 1+0j if m==0 else 0j
    if m==0 or (m-h)%RADIX:return 0j
    return (RADIX*(1-exp(-2j*pi*h/RADIX))/(2j*pi*m)
            * exp(2j*pi*m*float(shift)/RADIX))


def fejer_carry_pair_direct(phase:Fraction, r:Fraction, s:Fraction,
                            h:int,k:int,aperture:int) -> complex:
    """Independent product of two individual SUCC FLP-03 Fejer pin readings."""
    if not isinstance(phase,Fraction) or not 0<=phase<1:
        raise ValueError("rational phase in [0,1) required")
    if type(aperture) is not int or aperture<2:raise ValueError("aperture>=2")
    y=(RADIX*phase+r)%1
    def scalar(x,shift,mode):
        return sum((1-abs(m)/aperture)*_floor_char_coeff(m,mode,shift)
                   *exp(2j*pi*m*float(x)) for m in range(-aperture+1,aperture))
    return scalar(phase,r,h)*scalar(y,s,k)


def fejer_carry_pair_lattice(phase:Fraction,r:Fraction,s:Fraction,
                             h:int,k:int,aperture:int) -> complex:
    """Two-frequency source-twisted BBP Fourier lattice m+16*l.

    psi_{u,v;n}(x)=F_{r(n),u}(x)*F_{r(n+1),v}({16x+r(n)}).
    Product of Fejer expansions has modes (m+16*l) and factor
      exp[2pii*((m*r+l*s)/16 + l*r)].
    Its equality to the direct product is exact finite algebra. Convergence
    to the sharp floor pair has the separate, source-unproved boundary cost.
    """
    if not isinstance(phase,Fraction) or not 0<=phase<1:
        raise ValueError("rational phase in [0,1) required")
    if type(aperture) is not int or aperture<2:raise ValueError("aperture>=2")
    # Build unshifted F_h coefficients independently from the shifted direct evaluator.
    def modes(v:int):
        return [(m,(1-abs(m)/aperture)*_floor_char_coeff(m,v,Fraction()))
                for m in range(-aperture+1,aperture)
                if _floor_char_coeff(m,v,Fraction()) != 0]
    sm=0j
    for m,cm in modes(h):
        for l,cl in modes(k):
            phase_arg= ((m+RADIX*l)*phase
                         + Fraction(m, RADIX)*r
                         + Fraction(l, RADIX)*s + l*r)
            sm+=cm*cl*exp(2j*pi*float(phase_arg%1))
    return sm


def forced_carry_pair(n:int,phase:Fraction)->tuple[int,int]:
    """Real BBP two successive literal carries; source loaded on demand."""
    if type(n) is not int or n<2 or not isinstance(phase,Fraction) or not 0<=phase<1:
        raise ValueError("n>=2 and original rational circle phase required")
    from .duck_bbp import forcing
    r,s=forcing(n),forcing(n+1)
    a=(RADIX*phase+r).numerator//(RADIX*phase+r).denominator
    new=(RADIX*phase+r)%1
    b=(RADIX*new+s).numerator//(RADIX*new+s).denominator
    return a,b


def quarter_turn_kernel() -> tuple[tuple[complex,...],...]:
    """Unitary DFT (16x16), the finite Heisenberg/Weil quarter turn."""
    return tuple(tuple(exp(-2j*pi*i*j/RADIX)/4 for j in range(RADIX))
                 for i in range(RADIX))


def blocking_polynomial(group:int) -> tuple[int,...]:
    """Coefficients of B_g(t)=sum_{j=0}^{g-1}16^(g-1-j)*t^j.

    On t=e^(-8x), this multiplies the authentic Q(x) Laplace density
    after regrouping g source steps into one radix 16**g step.
    """
    if type(group) is not int or group<1:
        raise ValueError("integer g >= 1")
    return tuple(RADIX**(group-1-j) for j in range(group))


def blocking_at_t(group:int, t:Fraction) -> Fraction:
    """Exact scaled q-integer / q-Gamma recurrence ratio for rational t."""
    if not isinstance(t,Fraction) or not 0<=t<=1:
        raise ValueError("rational t in [0,1]")
    return sum((c*t**j for j,c in enumerate(blocking_polynomial(group))),Fraction())


def qgamma_ratio_at_q(group:int,q:Fraction) -> Fraction:
    """[g]_q = Gamma_q(g+1)/Gamma_q(g) for 0<q<1 (DLMF 5.18.7).

    This evaluates the finite recurrence ratio, NOT the infinite
    q-Gamma product. Its identity is classical and is checked algebraically.
    """
    if type(group) is not int or group<1 or not isinstance(q,Fraction) or not 0<q<1:
        raise ValueError("g>=1 integer, rational 0<q<1")
    return (1-q**group)/(1-q)


def blocked_source_forcing(block:int,group:int) -> Fraction:
    """Exact original r, grouped g terms; zero-seed regrouping, no new source."""
    if type(block) is not int or block<1:
        raise ValueError("block index >=1")
    from .duck_bbp import forcing
    return sum((RADIX**(group-j)*forcing(group*(block-1)+j)
                for j in range(1,group+1)),Fraction())


def blocked_laplace_four_poles(block:int,group:int) -> Fraction:
    """Exact Laplace of Q_g, retaining all 4*g rational pole terms.

    For a=8*g*(block-1)+1 and B_g(e^-8x)=sum_j b_j e^(-8jx),
    integral exp(-a*x) Q(x) B_g(e^-8x) dx
      = sum_j b_j*[4/(a+8j)-2/(a+8j+3)-1/(a+8j+4)-1/(a+8j+5)].
    """
    if type(block) is not int or block<1:
        raise ValueError("block>=1")
    a=8*group*(block-1)+1
    return sum((coef*(Fraction(4,a+8*j)-Fraction(2,a+8*j+3)
                      -Fraction(1,a+8*j+4)-Fraction(1,a+8*j+5))
                for j,coef in enumerate(blocking_polynomial(group))), Fraction())


def blocking_endpoint_jets(group:int) -> tuple[int,int]:
    """(Q_g'(0), Q_g''(0)); Q'(0)=15, Q''(0)=-59.

    Q_g=Q*B_g(exp(-8x)); the simple endpoint zero survives every fixed g.
    """
    coeff=blocking_polynomial(group)
    value=sum(coeff)
    first_derivative=-8*sum(j*c for j,c in enumerate(coeff))
    return (15*value,-59*value+30*first_derivative)


def stroboscopic_pair_split(digits:Sequence[int]) -> dict[str,Fraction]:
    """Exact even/odd time-frame energy split from radix256 blocking.

    For the archived fractional-π digits, zero-based odd starts correspond to
    the original alpha=pi/16 blocked U_(2k) clock for k>=1; zero-based
    even starts correspond to the once-shifted pi-fractional clock.
    All-start empirical M averages the two stroboscopic frames at even N.
    (E_even+E_odd)/2 = E_all + 64 ||M_even-M_odd||_F^2.
    """
    validate_digits(digits)
    n=len(digits)
    if n%2:raise ValueError("even N for both equally weighted time frames")
    c=pair_counts(digits)
    even=[[0]*RADIX for _ in range(RADIX)]
    odd=[[0]*RADIX for _ in range(RADIX)]
    for i in range(n):
        a=digits[i]
        b=digits[(i+1)%n]
        (even if i%2==0 else odd)[a][b]+=1
    size=n//2
    def energy(z):
        return Fraction(256*sum(v*v for row in z for v in row)-size*size,size*size)
    e_even,e_odd=energy(even),energy(odd)
    e_all=exact_energy_split(c)['pair_energy']
    stroboscopic=Fraction(64*sum((even[a][b]-odd[a][b])**2 for a in range(RADIX)
                                for b in range(RADIX)),size*size)
    assert Fraction(e_even+e_odd,2)==e_all+stroboscopic
    return {'all':e_all,'even':e_even,'odd':e_odd,'stroboscopic':stroboscopic}


def haar_reference_pair_law(r:Fraction,s:Fraction) -> tuple[tuple[Fraction,...],...]:
    """Independent exact interval-integral oracle, NOT an original π orbit.

    With x~Lebesgue, kappa_1=floor(16*x+r) (mod 16),
    y={16*x+r}, kappa_2=floor(16*y+s) (mod16).
    Split at all rational preimages of both floor thresholds. For ANY
    0<=r,s<1 the exact reference pair law is 1/256 per cell.
    """
    if any(not isinstance(z,Fraction) or not 0<=z<1 for z in (r,s)):
        raise ValueError("rational source shifts in [0,1) required")
    cuts={Fraction(0),Fraction(1)}
    for c in range(0,17):
        x=(Fraction(c)-r)/RADIX
        if 0<x<1:cuts.add(x)
        for j in range(0,17):
            x=(Fraction(c)+Fraction(j-s,RADIX)-r)/RADIX
            if 0<x<1:cuts.add(x)
    points=sorted(cuts)
    out=[[Fraction() for _ in range(RADIX)] for _ in range(RADIX)]
    for left,right in zip(points,points[1:]):
        mid=(left+right)/2
        u=RADIX*mid+r
        a=u.numerator//u.denominator
        y=u-a
        v=RADIX*y+s
        b=v.numerator//v.denominator
        out[a%RADIX][b%RADIX]+=right-left
    if sum(map(sum,out),Fraction()) != 1:
        raise AssertionError("reference measure normalization failed")
    return tuple(tuple(row) for row in out)


def genuine_prime_stage_matrix_mixture(digits:Sequence[int], A:int, p:int)->dict:
    """Optional cross-front experiment: original #554 four p-birth stage boundaries.

    digits[j-1] is the certified completed zero-seed BBP digit j.
    The 16x16 entries are joint real *completed digits*, not modular p-phases.
    Every stage sample has a future digit available; source stage labels come
    from the authenticated simple-pole prime clock, not fitted to digits.
    """
    validate_digits(digits)
    if type(A) is not int or A<16 or len(digits)<2*A:
        raise ValueError("A>=16 and need completed original digits through 2A")
    from .balanced_prime_clock import epoch_stage_boundaries
    bounds=epoch_stage_boundaries(A,p)
    stages=[]
    total=[[0]*RADIX for _ in range(RADIX)]
    for lo,hi in zip(bounds,bounds[1:]):
        c=[[0]*RADIX for _ in range(RADIX)]
        for n in range(lo,hi):
            a,b=digits[n-1],digits[n]
            c[a][b]+=1
            total[a][b]+=1
        stages.append((hi-lo, tuple(tuple(row) for row in c)))
    if sum(k for k,_ in stages)!=A:
        raise AssertionError("stage boundary loses original epoch starts")
    full=exact_energy_split(total)['pair_energy']
    avg_stage=sum((Fraction(length,A)*exact_energy_split(c)['pair_energy']
                   for length,c in stages),Fraction())
    positive_mixing=sum((Fraction(length,A)*Fraction(256)*sum(
        (Fraction(c[a][b],length)-Fraction(total[a][b],A))**2
        for a in range(RADIX) for b in range(RADIX))
        for length,c in stages),Fraction())
    if avg_stage != full+positive_mixing:
        raise AssertionError("signed-birth stage variance decomposition failed")
    return {"prime":p,"epoch":A,"boundaries":bounds,"weights":tuple(Fraction(k,A) for k,_ in stages),
            "overall_energy":full,"stage_energies":tuple(exact_energy_split(c)['pair_energy'] for _,c in stages),
            "weighted_stage_energy":avg_stage,"stage_mixing_energy":positive_mixing}

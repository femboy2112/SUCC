"""Original zero-seeded BBP Gamma lag and split/inert prime radical witnesses.

Exact fractions/integers. No pi digits used in source construction.
The external fixed-modulus PNT-AP is an explicitly separate asymptotic input.
Finite data and Galois averaging are NOT selected real Fourier bounds.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd, isqrt, prod, log


def r(n: int) -> F:
    if type(n) is not int or n < 1: raise ValueError('original source n>=1')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def beta_cap(s: int | F) -> F:
    """Positive upper T(s) < 1/((8s+1)(8s+2)); rational s>0."""
    s=F(s)
    if s<=0: raise ValueError('positive s')
    return 1/((8*s+1)*(8*s+2))


def shear_cap(s: int | F,d: int | F) -> F:
    """0<T(s)-T(s+d) < beta_cap(s)-beta_cap(s+d)."""
    s,d=F(s),F(d)
    if s<=0 or d<=0: raise ValueError('s,d positive')
    return beta_cap(s)-beta_cap(s+d)


def shear_cube_cap(s: int | F,d: int | F) -> F:
    """Looser derivative bound d/(32 s^3), s>0, d>0."""
    s,d=F(s),F(d)
    if s<=0 or d<=0: raise ValueError('s,d positive')
    return d/(32*s**3)


def shear_interval(n:int,d:int,depth:int=32) -> tuple[F,F]:
    """Exact source-only enclosure for lag correction Delta_d T(n)>0.

    Difference of original tails, using all four signed terms. The omitted
    positive terms sum to <r(n+depth+1)/(15*16**depth), by monotonicity r.
    """
    if any(type(z) is not int for z in (n,d,depth)) or n<1 or d<1 or depth<1:
        raise ValueError('positive integer n,d,depth')
    z=sum((F(r(n+j)-r(n+d+j), 16**j) for j in range(1,depth+1)),F())
    upper=z+r(n+depth+1)/F(15*16**depth)
    if not (0<z<upper and upper<shear_cap(n,d)):
        # Small depth can give loose upper exceeding the independent beta cap;
        # it is still an enclosing interval, so no erroneous assertion.
        if not (0<z<upper): raise ArithmeticError('positive lag lost')
    return z,upper


def tail_interval(n:int,depth:int=32)->tuple[F,F]:
    """Exact rational source-only interval for the genuine future Green tail."""
    if type(n) is not int or type(depth) is not int or n<1 or depth<1:
        raise ValueError('n,depth positive integers')
    z=sum((F(r(n+j),16**j) for j in range(1,depth+1)),F())
    return z,z+r(n+depth+1)/F(15*16**depth)


def telescoped_shear_upper(A:int,d:int)->F:
    """Upper for sum_{n=A}^{B-1}(T(n)-T(n+d)) at ANY B>A.

    Equal to initial d tails less terminal d tails, hence <= sum of d beta caps.
    """
    if type(A) is not int or type(d) is not int or A<1 or d<1:
        raise ValueError('A,d positive integers')
    return sum((beta_cap(A+j) for j in range(d)),F())


def uniform_signed_lag_chord_upper(A:int,d:int,h:int)->F:
    """Rigorous rational ceiling on |selected lag sum - pure pi lag sum|.

    2*pi<44/7 and telescoped_shear_upper bound, for ANY window ending B>A.
    Signed PNT and equidistribution NOT assumed.
    """
    if type(h) is not int or h==0: raise ValueError('nonzero integer h')
    return F(44,7)*abs(h)*telescoped_shear_upper(A,d)


def is_prime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,isqrt(n)+1,2))


def clean_passports(A:int,c_num:int=4,c_den:int=3)->dict:
    """Correct original p≡1 mod8 and p≡3 mod4 windows, not a fake long inert window."""
    if any(type(z) is not int for z in (A,c_num,c_den)) or A<8 or c_den<1 or not(c_den<c_num) or 2*c_num>=3*c_den:
        raise ValueError('A>=8, 1<c<3/2 rational')
    end=(c_num*A+c_den-1)//c_den
    kminus=(2*c_num*A+3*c_den-1)//(3*c_den)
    plus=tuple((8*k+1,k+1) for k in range((A+1)//2,A) if is_prime(8*k+1))
    minus=tuple((4*k-1,k) for k in range(kminus,A+1) if is_prime(4*k-1))
    for p,b in plus:
        if b>A or 4*(b-1)<end-1:raise ArithmeticError('bad split window')
    for p,b in minus:
        if b>A or (3*b+1)//2<end: raise ArithmeticError('bad inert window')
    pp=tuple(x[0] for x in plus+minus)
    return {'A':A,'end':end,'plus':plus,'minus':minus,'primes':pp,'product':prod(pp)}


def selected_prime_residue(p:int,b:int,n:int,kind:str)->int:
    """For the authentic original source during the p-clean injection window."""
    if not is_prime(p) or p<=5 or n<b: raise ValueError('true source p and n>=birth')
    if kind=='plus' and p==8*(b-1)+1 and n<=4*(b-1): a=4
    elif kind=='minus' and p==4*b-1 and n<(3*b+1)//2: a=-pow(2,-1,p)
    else: raise ValueError('invalid prime passport')
    return a*pow(16,n-b,p)%p


def nonalias_radical(pack:dict,d:int,h:int=1)->int:
    """Guaranteed squarefree divisor of den(h*(U_(n+d)-U_n)) on clean window."""
    ps=pack['primes']
    if type(d) is not int or not 1<=d<pack['end']-pack['A'] or type(h) is not int or h==0 or abs(h)>pack['A']:
        raise ValueError('genuine lag and 0<|h|<=A required')
    return prod(p for p in ps if pow(16,d,p)!=1)


def nonalias_radical_gcd(pack:dict,d:int)->int:
    """Independent exact integer formula P/gcd(P,16**d-1)."""
    if type(d) is not int or not 1<=d<pack['end']-pack['A']:
        raise ValueError('genuine lag')
    return pack['product']//gcd(pack['product'],16**d-1)


def strict_exponent(c_num:int=4,c_den:int=3)->float:
    c=c_num/c_den
    return 3-4*c/3-(c-1)*log(16)


def exact_original_orbit(last:int,initial:F=F(0))->list[F]:
    """Original signed source recurrence; source index and fractional part not conflated."""
    if type(last) is not int or last<0:raise ValueError('last>=0')
    u=F(initial)
    out=[u]
    for n in range(1,last+1):
        u=16*u+r(n)
        out.append(u)
    return out


def fraction_close(x:F,y:F)->F:
    """Circular distance of two exact rational phases."""
    z=(F(x)-F(y))%1
    return min(z,1-z)


def positive_seed_counterfeit(A:int,mesh:int,pack:dict|None=None)->dict:
    """Exact rational changed seed preserving ALL selected p-primary passports.

    It uses only rational BBP prefixes, no pi digits. All states in the chosen
    clean window occupy ONE mesh bin near fixed point 1/5. Original U0=0 is
    deliberately changed. P-adic integrality alone is not a mixing theorem.
    """
    if type(A) is not int or type(mesh) is not int or A<8 or mesh<2 or mesh>A or mesh&(mesh-1):
        raise ValueError('A>=8 and power-of-two mesh 2<=mesh<=A')
    pack=pack or clean_passports(A)
    if pack['A']!=A:raise ValueError('mismatched declared prime window')
    N=pack['end']-1
    M=N+1
    P=pack['product']
    Q=32*mesh*16**N*P+1
    # alpha_M = sum_{j<=M} 16^-j r(j), with no pi input.
    alphaM=sum((r(j)/16**j for j in range(1,M+1)),F())
    goal=F(1,5)-alphaM
    w=goal*Q+F(1,2)
    nearest=w.numerator//w.denominator
    seed=F(nearest,Q)
    assert gcd(seed.denominator,P)==1
    error_bound=F(16**N,2*Q)+F(16**N,16**M)*beta_cap(M)+beta_cap(A)
    assert error_bound<F(1,10*mesh)
    # As mesh a power of 2, dist of 1/5 from a mesh boundary >=1/(5m).
    assert (mesh%5)!=0
    return {'seed':seed,'q':Q,'P':P,'alpha_prefix':alphaM,'M':M,'N':N,'error_upper':error_bound,'mesh':mesh,'A':A}


def verify_rational_seed(pack:dict,proof:dict)->dict:
    """Independent exact original forward recurrence; compare clean p residues."""
    st=exact_original_orbit(pack['end']-1,proof['seed'])
    authentic=exact_original_orbit(pack['end']-1)
    m=proof['mesh']
    counts=[0]*m
    margin=proof['error_upper']
    for n in range(pack['A'],pack['end']):
        x=st[n]%1
        assert fraction_close(x,F(1,5))<margin
        counts[int(m*x)]+=1
        for kind in ('plus','minus'):
            for p,b in pack[kind]:
                a=p*st[n]; z=p*authentic[n]
                assert a.denominator%p and z.denominator%p
                s=a.numerator*pow(a.denominator,-1,p)%p
                t=z.numerator*pow(z.denominator,-1,p)%p
                assert s==t==selected_prime_residue(p,b,n,kind)
    if sum(v>0 for v in counts)!=1:raise AssertionError('counterfeit was not in ONE bin')
    return {'N':len(st)-1,'window_size':pack['end']-pack['A'],
            'occupied_cells':sum(v>0 for v in counts),'E':F(m),'counts':counts,
            'selected_prime_passports_preserved':True}


if __name__=='__main__':
    for A in (32,48,96):
        p=clean_passports(A)
        print('A=',A,'p=',len(p['primes']),'radical h1 d1:',nonalias_radical(p,1))


def _floor(z:F)->int:
    return z.numerator//z.denominator


def _ceil(z:F)->int:
    return -_floor(-z)


def circle_distance(z:F)->F:
    z=F(z)%1
    return min(z,1-z)


def interval_circle_near_status(low:F,high:F,mesh:int)->str:
    """Exact, conservative near/far/ambiguous for ALL reals in [low,high].

    Its endpoints must be rational. Integer and half-integer crossings are
    handled explicitly instead of reducing endpoints separately modulo one.
    """
    low,high=F(low),F(high)
    if high<low or type(mesh) is not int or mesh<2:raise ValueError('valid interval/mesh')
    rho=F(1,mesh)
    if high-low>=1:
        return 'ambiguous'
    mi=F(0) if _ceil(low)<=_floor(high) else min(circle_distance(low),circle_distance(high))
    ma=F(1,2) if _ceil(low-F(1,2))<=_floor(high-F(1,2)) else max(circle_distance(low),circle_distance(high))
    if ma<=rho:return 'near'
    if mi>rho:return 'far'
    return 'ambiguous'


def original_pi_lag_certificate(states:list[F],n:int,d:int,mesh:int,depth:int=24)->dict:
    """Rigorous ORIGINAL source-only test for the completed pi lag at radius 1/m.

    U_(n+d)-U_n=Q*pi+Delta_d T(n). Subtract interval from rational
    unwrapped difference, then classify the resulting interval on the circle.
    No externally computed pi digits enter. This is FINITE only.
    """
    if type(n) is not int or type(d) is not int or n<1 or d<1 or n+d>=len(states):
        raise ValueError('valid original source indices')
    lo,hi=shear_interval(n,d,depth)
    diff=states[n+d]-states[n]
    status=interval_circle_near_status(diff-hi,diff-lo,mesh)
    return {'classification':status,'original_source_near':circle_distance(diff)<=F(1,mesh),
            'shear_lo':lo,'shear_hi':hi,'completed_pi_interval_lo':diff-hi,
            'completed_pi_interval_hi':diff-lo,'original_phase':diff%1}

# Finite-to-global completion, with NO pi digits as construction inputs.


def gamma_tail_lower(s: int | F) -> F:
    """Strict original BBP Green-tail lower, from the exact Beta integrand.

    B(s)*(1-6/(8s+3)) < T(s) < B(s), s>=1.
    The proof uses 0<=1-1/D(x)<=3(1-x) on [0,1].
    """
    s=F(s)
    if s<1: raise ValueError('s>=1')
    return beta_cap(s)*(1-F(6)/(8*s+3))


def source_prefix_alpha(M:int) -> F:
    """Original rational prefix alpha_M=U_M/16^M, no pi digits."""
    if type(M) is not int or M<1: raise ValueError('M positive integer')
    u=F(0)
    for n in range(1,M+1):
        u=16*u+r(n)
    return u/16**M


def gamma_shadow_horizon(M:int,mesh:int)->dict:
    """Sharp within-one-step global BBP rational-shadow horizon.

    q_lower is the largest q>=0 CERTIFIED by a strict beta cap to have
    m*16^q*T_M<1. The true maximal q is q_lower or q_lower+1,
    since T_M/B_M>1/16 for M>=1. All arithmetic is exact rational.
    """
    if type(M) is not int or type(mesh) is not int or M<1 or mesh<2:
        raise ValueError('M>=1, mesh>=2 integers')
    B=beta_cap(M); L=gamma_tail_lower(M)
    q=-1
    while mesh*16**(q+1)*B<1:
        q+=1
    if q<0: raise ValueError('mesh too fine for even the cutoff time')
    assert 16*L>B
    return {'M':M,'mesh':mesh,'guaranteed_extra_steps':q,
            'possible_true_extra_steps':(q,q+1),
            'tail_lower':L,'tail_upper':B,
            'certified_displacement_upper':16**q*B,
            'two_steps_later_lower':16**(q+2)*L}


def completed_pi_interval(M:int,n:int)->tuple[F,F]:
    """Rigorous rational enclosure of 16^n*pi/16, from alpha_M + Gamma.

    Identifies X_n=16^n*alpha_M+16^(n-M)*T_M. No pi digits used.
    The endpoints are strict and must be reduced modulo 1 with care.
    """
    if type(M) is not int or type(n) is not int or M<1 or n<0:
        raise ValueError('M>=1,n>=0 exact indices')
    z=source_prefix_alpha(M)
    multiplier=F(16**n,16**M)
    base=16**n*z
    return base+multiplier*gamma_tail_lower(M),base+multiplier*beta_cap(M)


def certified_phase_bin(M:int,n:int,mesh:int)->int|None:
    """If the strict analytic enclosure fits one mesh cell, certify that cell."""
    if type(mesh) is not int or mesh<2: raise ValueError('mesh>=2')
    low,high=completed_pi_interval(M,n)
    a=(mesh*low).numerator//(mesh*low).denominator
    b=(mesh*high).numerator//(mesh*high).denominator
    return a%mesh if a==b else None


RADIAL_TAPS=(F(2),F(-2),F(-1),F(-2),F(-1,2),F(-1,2),F(1,4),F(0))


def finite_null_radial(N:int)->F:
    """Exact finite radial/null BBP channel; positive for finite N, ->0.

    Original October 26 two-quadratic channel formula, independently
    reconstructed here from its finite signed coefficient taps.
    """
    if type(N) is not int or N<1: raise ValueError('N>=1')
    return sum((c/F(16**j*(8*j+k+1))
                for j in range(N) for k,c in enumerate(RADIAL_TAPS)),F(0))


def finite_null_radial_upper(N:int)->F:
    """Proof: R_N=2 int_0^1 d(t^(8N)/16^N)*log F(t),
    and 0<log F(t)<=2(1-t) on (0,1)."""
    if type(N) is not int or N<1: raise ValueError('N>=1')
    return F(4,16**N*(8*N+1))


def rational_ghost_cloud(pack:dict,mesh:int)->dict:
    """Counterfeit ALL selected p-residue clocks while all real phases cohere.

    This is NOT the original source trajectory: only the selected p-primary
    source passports, their mod-p recurrence, and a common odd conductor
    survive. The missing real cofactor is changed explicitly by a CRT lift.
    """
    A,end=pack['A'],pack['end']
    if type(mesh) is not int or mesh<2 or mesh&(mesh-1):
        raise ValueError('mesh power of two')
    D=1
    from math import lcm
    for j in range(1,end):
        D=lcm(D,r(j).denominator)
    R=pack['product']
    if D%R: raise ArithmeticError('source common denominator missed a prime passport')
    for p in pack['primes']:
        if D%(p*p)==0:raise ArithmeticError('p-primary exponent not one on clean window')
    old=prod(p for p in range(7,2*A) if is_prime(p))
    if old==1 or D%(R*old):
        raise ArithmeticError('old generic prime product not in complementary conductor')
    assert F(R,2*D)<F(1,5*mesh)
    orbit=exact_original_orbit(end-1)
    fake={}
    for n in range(A,end):
        t=D*(orbit[n]%1)
        if t.denominator!=1:raise ArithmeticError('shared odd denominator failed')
        a=int(t)%R
        centered=a if 2*a<R else a-R
        x=F(1,5)+F(centered,D)
        if int(mesh*(x%1))!=int(F(mesh,5)):raise ArithmeticError('fake cloud left its bin')
        for kind in ('plus','minus'):
            for p,b in pack[kind]:
                px=p*x; po=p*orbit[n]
                if px.denominator%p==0 or po.denominator%p==0:
                    raise ArithmeticError('p-primary not clean')
                value=lambda z:(z.numerator*pow(z.denominator,-1,p))%p
                if value(px)!=value(po) or value(px)!=selected_prime_residue(p,b,n,kind):
                    raise ArithmeticError('fake p residue mismatch')
        fake[n]=x
    return {'A':A,'end':end,'mesh':mesh,'D':D,'R':R,'old_prime_product':old,
            'common_conductor_quotient':D//R,
            'original_source':False,
            'matches_all_selected_p_residue_clock_values':True,
            'all_fake_states_one_mesh_bin':True,
            'fake_states':fake,
            'real_arc_radius_upper':F(R,2*D),
            'coprime_residue_fraction':prod((F(p-1,p) for p in pack['primes']), start=F(1))}


def oriented_boundary_flux(delta:F,shear:F,mesh:int)->dict:
    """Exact signed near-pair crossing when TRUE delta=SOURCE delta-shear.

    For m>=4 and 0<shear<1/m, original source delta on R/Z.
    The near-pair indicator gains on (rho,rho+shear], loses on
    [1-rho,1-rho+shear), and is otherwise unchanged.
    A positive shear comes from the original strictly decreasing tail.
    """
    delta,shear=F(delta)%1,F(shear)
    if type(mesh) is not int or mesh<4 or not F(0)<shear<F(1,mesh):
        raise ValueError('mesh>=4 and 0<shear<1/mesh required')
    rho=F(1,mesh)
    gain=int(rho<delta<=rho+shear)
    loss=int(1-rho<=delta<1-rho+shear)
    before=int(circle_distance(delta)<=rho)
    after=int(circle_distance(delta-shear)<=rho)
    if after-before!=gain-loss:
        raise ArithmeticError('oriented Gamma boundary flux identity failed')
    return {'gain':gain,'loss':loss,'signed_flux':gain-loss,
            'source_near':before,'completed_near':after}


def binary_boundary_is_2adic_unit(delta:F,mesh:int)->bool:
    """For 2-integral rational delta and even mesh, m*delta-1 is a 2-adic unit.

    It says nothing about the REAL size of delta-1/mesh.
    """
    delta=F(delta)
    if type(mesh) is not int or mesh<2 or mesh%2 or delta.denominator%2==0:
        raise ValueError('even mesh, 2-integral rational required')
    return ((mesh*delta-1).numerator%2==1 and (mesh*delta-1).denominator%2==1)

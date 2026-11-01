"""Research-only authentic BBP four-pole lag-resolvent and VdC bridge.

Everything returned is exact rational/integer. Complex Weyl asymptotics remain OPEN.
"""
from fractions import Fraction as F
from math import comb


def r(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive integer source index')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def original_states(N, seed=F(0)):
    if type(N) is not int or N<0 or type(seed) not in (int,F):
        raise ValueError('N>=0, rational seed')
    u=F(seed); out=[u]
    for j in range(1,N+1):
        u=16*u+r(j)
        out.append(u)
    return tuple(out)


def lag_forcing(n,k):
    if type(n) is not int or n<1 or type(k) is not int or k<1:
        raise ValueError('n,k positive integers')
    return sum((16**(k-j)*r(n+j) for j in range(1,k+1)),F(0))


def lag_identity(n,k,seed=F(0)):
    U=original_states(n+k,seed)
    return U[n+k]-U[n]==(16**k-1)*U[n]+lag_forcing(n,k)


def lag_forcing_bound(k):
    """Sum_(n>=1) lag_forcing(n,k) < (16^k-1)/32.

    Uses r(n+1)<15/(64*n^2), sum_n 1/n^2<2.
    """
    if type(k) is not int or k<1: raise ValueError('positive lag')
    return F(16**k-1,32)


def lag_phasor_error_bound_rational(k,h):
    """Upper bound on |C_(N,k) - D_(N,k)| valid ALL N>k.

    Precisely < (pi*|h|/16)*(16^k-1); uses pi<22/7,
    so returns 11*|h|*(16^k-1)/56 > actual bound.
    """
    if type(h) is not int or h==0:raise ValueError('nonzero h')
    return F(11*abs(h)*(16**k-1),56)


def shifted_lag_frequency(k,h):
    if type(k) is not int or k<1 or type(h) is not int or h==0:
        raise ValueError('k>=1, h nonzero')
    return h*(16**k-1)


def v_p_int(n,p):
    if type(n) is not int or n==0 or type(p) is not int or p<2:
        raise ValueError('nonzero integer and declared prime')
    n=abs(n);v=0
    while n%p==0: v+=1;n//=p
    return v


def conductor_profile(k):
    """Exact LTE prime-3/5 ranks for cofactor 16^k-1."""
    if type(k) is not int or k<1:raise ValueError('positive k')
    q=16**k-1
    return {'cofactor':q,'v2':v_p_int(q,2),'v3':v_p_int(q,3),
            'v5':v_p_int(q,5),'v3_by_lte':1+v_p_int(k,3),
            'v5_by_lte':1+v_p_int(k,5)}


def signed_lag_exponents(U,k,h):
    """Two exact rational phase argument lists, not evaluated as complex."""
    if type(h) is not int or h==0 or type(k) is not int or k<1 or k>=len(U):
        raise ValueError('valid h,k and state sequence')
    N=len(U)-1
    actual=[];reduced=[]
    for n in range(1,N-k+1):
        actual.append((h*(U[n+k]-U[n]))%1)
        reduced.append((h*(16**k-1)*U[n])%1)
    return tuple(actual),tuple(reduced)


def gaussian_mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def gaussian_conj(a): return (a[0],-a[1])


def gaussian_sum(a): return tuple(sum(z[j] for z in a) for j in range(2))


def gaussian_norm2(a): return a[0]*a[0]+a[1]*a[1]


def gaussian_vdc(z,K):
    """All-Gaussian-exact VdC inequality on unit phases, not a fake BBP sample.

    Returns integer RHS and LHS of
      K^2 |S|^2 <= (N+K-1)*(K*N+2*sum_(k<K)(K-k)Re C_k).
    """
    N=len(z)
    if type(K) is not int or not 1<=K<=N:
        raise ValueError('1<=K<=N')
    if any(gaussian_norm2(u)!=1 for u in z):
        raise ValueError('unit Gaussian phases required')
    c=[]
    for lag in range(1,K):
        c.append(sum(gaussian_mul(z[n+lag],gaussian_conj(z[n]))[0]
                     for n in range(N-lag)))
    lhs=K*K*gaussian_norm2(gaussian_sum(z))
    corr=K*N+2*sum((K-k)*c[k-1] for k in range(1,K))
    rhs=(N+K-1)*corr
    assert corr>=0 and rhs>=lhs
    return {'lhs':lhs,'rhs':rhs,'lag_real':tuple(c),'N':N,'K':K}


def vdc_lag_error_bound_rational(K,N,h):
    """Rational upper bound on total-source error in normalized VdC bracket.

    2/(K*N)*sum_(k=1)^(K-1)(1-k/K) |C_k-D_k|
      < 11|h|/(28*K*N) * sum_(k=1)^(K-1)(1-k/K)(16^k-1).
    """
    if type(K) is not int or not 1<=K<=N or type(h) is not int or h==0:
        raise ValueError('valid K,N,h')
    exact=F(2,K*N)*sum((F(K-k,K)*lag_phasor_error_bound_rational(k,h)
                         for k in range(1,K)),F(0))
    coarse=F(11*abs(h)*(16**K-16),420*K*N) if K>=2 else F(0)
    # this coarse uses sum_(k=1)^(K-1)16^k=(16^K-16)/15
    assert exact<=coarse
    return {'weighted_rational_upper':exact,'coarse_upper':coarse}


def dyadic_character_zero(a,k,h):
    """Exact cyclic character sum for source U_n mod2^a full period.

    Source DSI isometry implies U_n mod2^a permutes all residues;
    (16^k-1) odd, so character average vanishes iff 2^a∤h.
    """
    if type(a) is not int or a<1 or type(k) is not int or k<1 or type(h) is not int or h==0:
        raise ValueError('positive a,k and h nonzero')
    return h%2**a!=0


def exact_dyadic_lag_histogram(a,k,h,start=1):
    """Exact integer frequency histogram for the TRUE zero-seed BBP source."""
    if not 1<=a<=12 or not 1<=k<=25 or type(h) is not int or h==0 or start<1:
        raise ValueError('finite dyadic controls')
    q=2**a
    U=original_states(start+q-1)
    counts=[0]*q
    for n in range(start,start+q):
        x=U[n]
        t=(x.numerator*pow(x.denominator,-1,q))%q
        counts[(h*(16**k-1)*t)%q]+=1
    return tuple(counts)


def coherent_lag_lower_bound(N,k,h):
    """Same-forcing s*=-pi/16, symbolic anti-control.

    For fixed k, |D_(h,k)(N;s*)-(N-k)| < (pi|h|/16)(16^k-1).
    Only returns strict rational upper via pi<22/7; no pi numeric input.
    """
    if type(N) is not int or type(k) is not int or N<=k or type(h) is not int or h==0:
        raise ValueError('N>k>=1, h nonzero')
    return {'coherent_count':N-k,
            'max_difference_rational':lag_phasor_error_bound_rational(k,h),
            'normalized_lower':max(F(0),F(N-k)-lag_phasor_error_bound_rational(k,h))/N}


def exact_gram_grouping(phi):
    """Exact identity: full offdiagonal =2*sum_(k>=1)Re C_k.

    Input any finite unit Gaussian phase sequence (independent, exact oracle).
    """
    if any(gaussian_norm2(z)!=1 for z in phi):
        raise ValueError('unit phases')
    N=len(phi);G=gaussian_norm2(gaussian_sum(phi))
    corr=sum(sum(gaussian_mul(phi[n+k],gaussian_conj(phi[n]))[0]
                 for n in range(N-k)) for k in range(1,N))
    assert G-N==2*corr
    return {'offdiagonal':G-N,'twice_signed_lag':2*corr}


def _machin_pi_bracket(iterations=22):
    """Exact rational π enclosure using Machin and alternating arctan series."""
    if type(iterations) is not int or iterations<1:
        raise ValueError('positive terms')
    def A(q):
        partial=sum((F((-1)**j,(2*j+1)*q**(2*j+1))
                     for j in range(iterations)),F(0))
        remainder=F(1,(2*iterations+1)*q**(2*iterations+1))
        return partial-remainder,partial+remainder
    a,b=A(5);c,d=A(239)
    return 16*a-4*d,16*b-4*c


def cos_interval(x,cos_terms=17,pi_terms=20,round_digits=12,phase_digits=20):
    """Rigorous outward interval for cos(2πx), rational/Fraction ONLY.

    Uses arctan/Machin interval; Taylor's global derivative bound;
    each output is outward-rounded to multiples of 10^-round_digits.
    No decimal trigonometry, no unknown π digits as oracle.
    """
    from math import factorial
    if type(x) not in (int,F) or type(cos_terms) is not int or cos_terms<1 or type(round_digits) is not int or not 4<=round_digits<=24:
        raise ValueError('exact x and valid precision')
    x=F(x)%1
    if x>F(1,2):x-=1
    # Before Taylor arithmetic, round the EXACT rational circle phase to a
    # bounded-denominator rational. Include Lipschitz error explicitly.
    phase_unit=10**phase_digits
    index=(x.numerator*phase_unit)//x.denominator
    phase_center=F(2*index+1,2*phase_unit)
    phase_error=F(1,2*phase_unit)
    lower_pi,upper_pi=_machin_pi_bracket(pi_terms)
    mid_pi=(lower_pi+upper_pi)/2
    angle=2*phase_center*mid_pi
    theta2=angle*angle
    term=F(1);total=term
    for j in range(1,cos_terms):
        term*=-theta2/F(2*j*(2*j-1))
        total+=term
    err=(upper_pi-lower_pi) + F(44,7)*phase_error + F(22,7)**(2*cos_terms)/factorial(2*cos_terms)
    low=total-err;high=total+err
    unit=10**round_digits
    a=low.numerator*unit//low.denominator
    b=-( (-high.numerator*unit)//high.denominator )
    assert F(a,unit)<=low<=high<=F(b,unit)
    return F(a,unit),F(b,unit)


def selected_signed_lag_interval(N,K,h=1,seed=F(0),cos_terms=17,pi_terms=20,round_digits=12):
    """Certified finite interval for weighted lag-reduced REAL cosine sum.

    L=(2/(KN)) sum_(k=1)^(K-1)(1-k/K) sum_(n=1)^(N-k)
         cos(2π h(16^k-1)U_n(seed)).
    This is NOT an all-horizon or π-normality theorem.
    """
    if type(N) is not int or not 2<=N<=10000 or type(K) is not int or not 1<=K<=N or type(h) is not int or not h or type(seed) not in (int,F):
        raise ValueError('valid finite source and harmonic')
    U=original_states(N,seed)
    lower=upper=F(0)
    scale=F(2,K*N)
    for k in range(1,K):
        weight=scale*F(K-k,K)
        cf=h*(16**k-1)
        for n in range(1,N-k+1):
            a,b=cos_interval(cf*U[n],cos_terms,pi_terms,round_digits)
            lower+=weight*a
            upper+=weight*b
    return lower,upper


def signed_lag_mass(K,N):
    """If every reduced lag phase is 1, weighted signed observable mass."""
    if type(K) is not int or not 1<=K<=N:raise ValueError('valid K,N')
    direct=F(2,K*N)*sum((F(K-k,K)*(N-k) for k in range(1,K)),F(0))
    closed=F(K-1,K)*(1-F(K+1,3*N))
    assert direct==closed
    return closed


def vdc_certificate_from_signed_lag_interval(N,K,h,score):
    """Certified upper bound on |S_N(h)|^2/N^2 from signed lag score.

    Uses the exact source forcing bridge and rigorous π<22/7.
    NO future/cancellation assumption is substituted.
    """
    if len(score)!=2 or score[0]>score[1]:raise ValueError('ordered interval')
    E=vdc_lag_error_bound_rational(K,N,h)['weighted_rational_upper']
    return max(F(0),F(N+K-1,N)*(F(1,K)+score[1]+E))


def nearzero_nonnormal_shadow_lag_error_bound(source_depth,N,K,h):
    """Rigorous finite signed-lag-score sensitivity to PR433's irrational s_L.

    s_L=q_L-pi/16=-16^-L T_L, where original source has
      |s_L|<16^-L / ((8L+1)(8L+2)).
    The *completed* changed orbit is rational and provably nonnormal.
    Error is an explicit rational upper bound using pi<22/7, no pi digits.
    """
    if type(source_depth) is not int or type(N) is not int or type(K) is not int or type(h) is not int or not h or source_depth<N or N<2 or not 1<=K<=N:
        raise ValueError('source_depth>=N>=2, K valid, h nonzero')
    delta=F(1,16**source_depth*(8*source_depth+1)*(8*source_depth+2))
    # |cos(2pi(x+u))-cos(2pi*x)|<=2pi*|u|<44/7 |u|.
    # L has coefficient 2/(KN)*(1-k/K) for each shifted sample.
    return (F(88*abs(h),7*K*N)*delta *
            sum((F(K-k,K)*(16**k-1)*F(16*(16**(N-k)-1),15)
                 for k in range(1,K)),F(0)))
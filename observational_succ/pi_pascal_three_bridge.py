"""Source-faithful Pascal ×3 / ×16 bridge (research-only).

Extends SUCC's ternary-chart PR #275; does NOT reassert novelty for its
positive filter. No selected π normality, same-law tripling, or real-circle
one-sixteenth bound is established. All certificates below are rational.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import comb, gcd, isqrt
from .pi_source_collision import bbp_forcing, bbp_states


def weighted_three(n: int) -> tuple[Q,...]:
    if type(n) is not int or n < 0: raise ValueError('n >= 0 integer')
    w=tuple(Q(comb(n,k)*2**k,3**n) for k in range(n+1))
    assert sum(w,Q())==1
    return w


def selected_shadow_error(n: int, h: int=1) -> Q:
    """|Pascal_n[e(h y_(k+1))]-Pascal_n[e(h16^k π)]|<bound."""
    if type(h) is not int or not h:raise ValueError('h nonzero integer')
    weighted_three(n)
    return Q(99*abs(h),224*(n+1)*(n+2))


def tauber_identity(values: tuple[int|Q,...]) -> dict:
    if not values or any(type(z) not in (int,Q) for z in values):
        raise ValueError('nonempty int/Fraction sequence')
    a=tuple(Q(x) for x in values)
    N=len(a);m=2*N//3;p=Q(2,3)
    b=tuple(sum((weighted_three(n)[k]*a[k] for k in range(n+1)),Q())
            for n in range(N))
    occ=tuple(sum((weighted_three(N)[k] for k in range(j+1,N+1)),Q())
              for j in range(N))
    exact=p*sum(b,Q())
    assert exact==sum((a[k]*occ[k] for k in range(N)),Q())
    error=sum(a[:m],Q())-exact
    A=max(map(abs,a))
    assert error**2 <= A*A*(Q(2*N,9)+1)
    return {'N':N,'prefix':m,'error':str(error),
            'squared_upper':str(A*A*(Q(2*N,9)+1))}


def signed_filter(t: int, j: int) -> dict:
    """(E−13)^j y_t = 3^j y_t + source correction modulo one.

    Corrector is sourced from the authentic four-pole forcing and retains
    literal vs centered integer carry. Its sign is (-1)^(j-1).
    """
    if type(t) is not int or t<1 or type(j) is not int or j<1:
        raise ValueError('t,j positive integers')
    y=bbp_states(t+j)
    F=sum((comb(j,k)*(-13)**(j-k)*y[t+k] for k in range(j+1)),Q())
    C=Q()
    for a in range(1,j+1):
        coef=sum(comb(j,k)*(-13)**(j-k)*16**(k-a)
                 for k in range(a,j+1))
        C+=coef*bbp_forcing(t+a)
    assert (F-3**j*y[t]-C).denominator==1
    bound=Q(13**j-(-3)**j,16)*bbp_forcing(t+1)
    assert 0<(-1)**(j-1)*C<=bound
    return {'t':t,'j':j,'correction':str(C),'upper':str(bound),
            'source_phase':str(F%1),'target_phase':str((3**j*y[t])%1)}


def prime_square(q: int,r: int,t: int)->dict:
    """Exact lax defect P_qP_r-P_(qr) on actual unwrapped BBP U_t.

    P_q=(16-q+(q-1)E)/15; difference is (q-1)(r-1)/225
    times (E-1)(E-16). Source asymptotic t^3 defect tends
    -(q-1)(r-1)/480, but no source-law invariance follows.
    """
    if any(type(a) is not int for a in (q,r,t)) or q<2 or r<2 or q*r>16 or t<1:
        raise ValueError('2<=q,r, qr<=16, t>=1')
    c=Q((q-1)*(r-1),225)
    u=[Q()]
    for n in range(1,t+3):u.append(16*u[-1]+bbp_forcing(n))
    direct=c*(u[t+2]-17*u[t+1]+16*u[t])
    derived=c*(bbp_forcing(t+2)-bbp_forcing(t+1))
    upper=c*Q(240,(8*t+1)*(8*t+2)*(8*t+3))
    assert direct==derived<0 and -direct<upper
    return {'q':q,'r':r,'t':t,'defect':str(direct),
            'absolute_upper':str(upper),
            'asymptotic_t3_limit':str(-Q((q-1)*(r-1),480))}


def prime_square_associator(q:int,r:int,s:int)->bool:
    if any(type(x) is not int or x<2 for x in (q,r,s)) or q*r*s>16:
        raise ValueError('positive factorization within 16 required')
    def add(a,b):return tuple((a[k] if k<len(a) else 0)+(b[k] if k<len(b) else 0)
                            for k in range(max(len(a),len(b))))
    def mul(a,b):
        c=[Q()]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return tuple(c)
    def F(v):return (Q(16-v,15),Q(v-1,15))
    def D(a,b):
        z=mul(F(a),F(b));w=F(a*b)
        return tuple(z[k]-(w[k] if k<len(w) else 0) for k in range(3))
    assert add(mul(D(q,r),F(s)),D(q*r,s))==add(mul(F(q),D(r,s)),D(q,r*s))
    return True


def mixed_selector(N: int,L: int, h: int=1,q: int=3)->dict:
    """Double source path, exact Haar L2 and positive Fejer selection.

    B=|h|16^N q^L. Error for full selected rectangle is at most
    (1-16^-N)(1-q^-L)/(15(q-1)NL). q=3 gives <1/(30NL).
    Distinct-frequency L2=1/(NL) holds for q=3 and any nonzero h,
    NOT for q a power of two.
    """
    if any(type(x) is not int or x<1 for x in (N,L,q)) or q<2 or type(h) is not int or h==0:
        raise ValueError('N,L positive, q>=2, h nonzero integers')
    frequencies=[h*16**n*q**j for n in range(N) for j in range(L)]
    from collections import Counter
    c=Counter(frequencies)
    B=abs(h)*16**N*q**L
    weights=[Q(B-abs(x),B) for x in frequencies]
    assert min(weights)>0
    loss=sum((1-w for w in weights),Q())/(N*L)
    assert loss==Q((16**N-1)*(q**L-1),15*(q-1)*N*L*16**N*q**L)
    return {'frequencies_distinct':len(c)==N*L,'paths':N*L,
            'haar_L2_for_zero_forcing':str(Q(sum(v*v for v in c.values()),(N*L)**2)),
            'selected_path_integral_abs_error':str(loss),'selector_bandwidth':B}


def rational_tripling_fake(power: int,H: int)->dict:
    """Changed-selector rational counterfeit; all tested low modes disappear."""
    if type(power) is not int or not 2<=power<=5 or type(H) is not int or not 1<=H<5**(power-1):
        raise ValueError('2<=power<=5; 1<=H<5^(power-1)')
    modulus=5**power
    orbit=[pow(3,j,modulus) for j in range(4*5**(power-1))]
    assert len(set(orbit))==len(orbit)
    for h in range(1,H+1):
        buckets=[0]*modulus
        for a in orbit:buckets[h*a%modulus]+=1
        for k in range(5**(power-1)):
            assert len({buckets[k+d*5**(power-1)] for d in range(5)})==1
    return {'denominator':modulus,'checked_frequencies':H,
            'vanishing_modes_proved':True,'base16_normality':'FALSE',
            'selected_BBP_source':'CHANGED'}

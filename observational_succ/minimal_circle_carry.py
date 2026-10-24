"""Minimal circle covering laws: sharp additive carry thresholds and causal Green source.

All executable identities are integer or Fraction exact. General analytic
and Haar-moment theorems have separate proofs in the companion research dossier.
π normality is NOT claimed.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial

def _integer(n, lower=0):
    if type(n) is not int or n < lower:
        raise ValueError(f"integer >= {lower} required")
    return n

def occupancies(parts, total):
    _integer(parts,1); _integer(total)
    def rec(m,k):
        if m==1:
            yield (k,)
            return
        for v in range(k+1):
            for tail in rec(m-1,k-v):
                yield (v,)+tail
    yield from rec(parts,total)

def multinomial(a):
    w=factorial(sum(a))
    for n in a:
        w//=factorial(n)
    return w

def _cap(length,degree,max_states):
    _integer(max_states,1)
    if comb(length+degree-1,degree)>max_states:
        raise ValueError("finite source enumeration cap exceeded")

def exact_origin_moment(base,length,degree,*,modulus=None,max_states=130000):
    """Exact integral |sum_(j<N) exp(2πi*b^j*x)|^(2k) over Haar or q-grid."""
    _integer(base,2);_integer(length,1);_integer(degree)
    if modulus is not None:
        _integer(modulus,2)
    _cap(length,degree,max_states)
    values=Counter()
    for a in occupancies(length,degree):
        freq=sum(n*base**j for j,n in enumerate(a))
        if modulus is not None:
            freq%=modulus
        values[freq]+=multinomial(a)
    return sum(z*z for z in values.values())

def independent_origin_moment(length,degree,*,max_states=130000):
    """Independent uniform-circle comparison: diagonal multinomial sum."""
    _integer(length,1);_integer(degree)
    _cap(length,degree,max_states)
    return sum(multinomial(a)**2 for a in occupancies(length,degree))

def first_carry_excess(base,length):
    """For k=b+1, Haar moment minus independent moment, EXACT."""
    _integer(base,2);_integer(length,1)
    if length<=2:
        return 0
    return 2*(base+1)*(length-2)+(base+1)**2*(length-2)*(length-3)

def first_carry_witness(base,earliest=0,gap=2):
    """b*b^i+b^(i+gap) = b^(i+1)+b*b^(i+gap-1), gap>=2."""
    _integer(base,2);_integer(earliest);_integer(gap,2)
    a=[0]*(earliest+gap+1);c=a[:]
    a[earliest]+=base;a[earliest+gap]+=1
    c[earliest+1]+=1;c[earliest+gap-1]+=base
    assert tuple(a)!=tuple(c)
    assert sum(a)==sum(c)==base+1
    assert sum(t*base**j for j,t in enumerate(a))==sum(t*base**j for j,t in enumerate(c))
    return tuple(a),tuple(c)

def no_carry_high_moment_bound(base,length,degree):
    """For k<=b, E|F_N|^(2k) <= k!*N^k; NOT pointwise in origin."""
    _integer(base,2);_integer(length,1);_integer(degree)
    if degree>base:
        raise ValueError("bound requires k<=b")
    return factorial(degree)*length**degree

def needed_alias_free_frame_labels(base,length,degree):
    """Necessary label count for exact Haar 2k moment on q-origin grid, k<=b."""
    _integer(base,2);_integer(length,1);_integer(degree)
    if degree>base:
        raise ValueError("colliding multisets for k>b")
    return comb(length+degree-1,degree)

def sufficient_grid_for_2k_moment(base,length,degree,modulus):
    """Sufficient, not necessary: q>k*b^(N-1)."""
    _integer(base,2);_integer(length,1);_integer(degree);_integer(modulus,2)
    return modulus>degree*base**(length-1)

def haar_bad_frame_upper(base,length,threshold):
    """Optimal among universal no-carry k-moment Markov bounds for k<=b."""
    _integer(base,2);_integer(length,1)
    e=Q(threshold)
    if not Q(0)<e<=Q(1):
        raise ValueError("0 < probability threshold <= 1 required")
    upper,k=min((Q(factorial(k),length**k)/e**(2*k),k)
                for k in range(1,base+1))
    return k,min(Q(1),upper)

def authentic_bbp_forcing(n):
    _integer(n,1)
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)

def finite_green_section(n,depth,base=16):
    """Bounded causal BBP Green section truncated K steps ahead."""
    _integer(n);_integer(depth,1);_integer(base,2)
    return sum((authentic_bbp_forcing(n+k)/base**k for k in range(1,depth+1)),Q())

def finite_green_residual(n,depth,base=16):
    """b*t_n^K-t_(n+1)^K-r(n+1)=-b^(-K)*r(n+K+1)."""
    _integer(n);_integer(depth,1);_integer(base,2)
    return (base*finite_green_section(n,depth,base)
            -finite_green_section(n+1,depth,base)-authentic_bbp_forcing(n+1))

def finite_green_l1_control(forcing_values,base=16):
    """Finite-support causal section and sharp L1 source norm bound."""
    _integer(base,2)
    f=tuple(Q(v) for v in forcing_values)
    if not f or any(v<0 for v in f):
        raise ValueError("nonempty nonnegative source required")
    N=len(f);out=[Q()]*N
    for j in range(N-1,-1,-1):
        out[j]=(f[j]+(out[j+1] if j+1<N else Q()))/base
    left=sum(f,Q());right=sum(out,Q())
    assert right<=left/Q(base-1)
    return left,right,tuple(out)

def finite_green_l2_ratio_squared(length,base=16):
    """Finite constant sources approach the SHARP ||G||=1/(b-1) bound."""
    _integer(length,1);_integer(base,2)
    _,_,t=finite_green_l1_control([1]*length,base)
    return sum((v*v for v in t),Q())/length

def rational_nonnormal_green_tail(n):
    """Positive infinite-Hankel-rank source can still select rational phase."""
    _integer(n)
    return Q(1,(n+1)*(n+2))

def rational_nonnormal_forcing(n,base=16):
    _integer(n,1);_integer(base,2)
    return base*rational_nonnormal_green_tail(n-1)-rational_nonnormal_green_tail(n)

def zero_action_circle_origins(base):
    """Unanchored minimum chord-step action selects only FIXED origins."""
    _integer(base,2)
    return tuple(Q(i,base-1) for i in range(base-1))

def zero_chord_step(base,phase):
    _integer(base,2)
    return ((base-1)*Q(phase)).denominator==1

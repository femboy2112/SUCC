"""Two-sided SUCC/FUCC symmetry does not by itself pin the EPR coupling.

Finite exact positive joint distributions on cyclic p-clock pairs. This is
classical probability; the special shift-permutation support defines a
separate pure maximally entangled quantum vector if given coherent amplitudes.
No physical coupling is measured or uniquely identified by this module.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd
from .observation_pinned_geometry import ObservationContractError, _p, _level, _int


def _weights(weights,p,k):
    _p(p);_level(k)
    N=p**k
    if N>1024:raise ObservationContractError('finite exact correlation budget')
    if type(weights) is not dict or not weights:
        raise ObservationContractError('nonempty source-relative phase distribution required')
    out={}
    for c,w in weights.items():
        _int(c,0)
        if c>=N or type(w) not in (int,F) or F(w)<0:
            raise ObservationContractError('invalid exact correlation and weight')
        out[c]=F(w)
    if sum(out.values(),F())!=1:
        raise ObservationContractError('relative phase distribution must be normalized')
    return out


def source_joint_coupling(p,k,weights):
    """Diagonal-S invariant joint law nu(x,y)=w(y-x)/p^k."""
    w=_weights(weights,p,k)
    N=p**k
    result={}
    for x in range(N):
        for c,prob in w.items():
            if prob:
                y=(x+c)%N
                result[(x,y)]=result.get((x,y),F())+prob/N
    return result


def source_marginals(joint,p,k):
    _p(p);_level(k)
    N=p**k
    left=[F()]*N;right=[F()]*N
    for (x,y),w in joint.items():
        left[x]+=w;right[y]+=w
    return tuple(left),tuple(right)


def relative_phase_distribution(joint,p,k):
    _p(p);_level(k)
    N=p**k
    w=[F()]*N
    for (x,y),prob in joint.items():
        w[(y-x)%N]+=prob
    return tuple(w)


def diagonal_succ_invariant(joint,p,k):
    _p(p);_level(k)
    N=p**k
    return all(joint.get(((x+1)%N,(y+1)%N),F())==value
               for (x,y),value in joint.items())


def diagonal_unit_dilation_invariant(joint,p,k,q):
    _p(p);_level(k);_int(q,1)
    N=p**k
    if gcd(q,p)!=1:
        raise ObservationContractError('nonunit FUCC is not a root-level permutation')
    return all(joint.get(((q*x)%N,(q*y)%N),F())==value
               for (x,y),value in joint.items())


def epr_shift_support(p,k,c):
    """Support of pure Psi_c=1/sqrt(N) sum_x |x,x+c> (not a density)."""
    _p(p);_level(k);_int(c,0)
    N=p**k
    return frozenset((x,(x+c)%N) for x in range(N))


def epr_reciprocal_succ_mirror(p,k,c):
    """(S_L tensor I)Psi_c=(I tensor S_R^-1)Psi_c, all c."""
    src=epr_shift_support(p,k,c)
    N=p**k
    left=frozenset(((x+1)%N,y) for x,y in src)
    right=frozenset((x,(y-1)%N) for x,y in src)
    return left,right


def unit_scale_shift(p,k,c,q):
    _p(p);_level(k);_int(c,0);_int(q,1)
    if q%p==0:raise ObservationContractError('not a finite-clock automorphism')
    return (q*c)%(p**k)


def delayed_relative_phase_counterfeit(p,K):
    """Pure shifts c=0 and c=p^K agree at all first K levels, not level K+1."""
    _p(p);_int(K,1)
    if K>8:raise ObservationContractError('finite exact horizon budget')
    return {"same_through_depth_K":all((p**K)%(p**k)==0 for k in range(1,K+1)),
            "separated_at_K_plus_one":(p**K)%(p**(K+1))!=0,
            "candidate_shifts":(0,p**K)}

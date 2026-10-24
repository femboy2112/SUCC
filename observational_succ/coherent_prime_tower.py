"""Exact positive-affine SUCC tower and three-ray Bruhat--Tits quantum code.

This is a *chosen* embedding of prime-sensitive arithmetic operators into a
three-ray, depth-filtered quantum secret-sharing system. The Bruhat--Tits
lattices are genuine Q_2 lattice classes. Placement, triadic logical digits,
and the quantum alphabet are NOT claimed to be p-adically canonical, a CFT,
or an Einstein--Rosen geometry.

The infinite-dimensional claims are PAPER results obtained from compatible
isometries and strong (not norm) operator limits; finite code is an exact
replay oracle only. The existing 3-qutrit [[3,1,2]] code is classical.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import isqrt
from .arithmetic_epr_star import PAIRS, codeword, pair_decode, pair_encode


class TowerContractError(ValueError):
    """Malformed source, geometry, finite cutoff, or quantum region."""


NORMALS = ((1, 0), (0, 1), (1, 1))


def level_size(level):
    if type(level) is not int or not 1 <= level <= 7:
        raise TowerContractError("finite executable level must be 1..7")
    return 3 ** level


def _integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise TowerContractError(f"integer at least {minimum} required")
    return x


def _coeff(x):
    if type(x) not in (int, F):
        raise TowerContractError("exact integer or Fraction, not float/bool")
    return F(x)


def prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def arithmetic_digits(n, level):
    """Encode the ORIGINAL n>=1 as least-significant-first base-3 digits of n-1."""
    size = level_size(level)
    if type(n) is not int or not 1 <= n <= size:
        raise TowerContractError("source element outside declared prefix")
    x = n-1
    digits=[]
    for _ in range(level):
        digits.append(x % 3)
        x //= 3
    assert x==0
    return tuple(digits)


def source_index(digits):
    if type(digits) is not tuple or len(digits) < 1 or len(digits)>7:
        raise TowerContractError("exact nonempty trit tuple required")
    if any(type(d) is not int or d not in (0, 1, 2) for d in digits):
        raise TowerContractError("invalid trit")
    return 1+sum(d*3**j for j,d in enumerate(digits))


def affine_endpoint(n, a, b):
    """Authenticated positive affine monoid action n |-> a*n+b."""
    _integer(n,1)
    _integer(a,1)
    _integer(b,0)
    return a*n+b


def affine_cutoff(n, level, a, b):
    """Truncated affine transition; None denotes an explicitly lost exit."""
    N=level_size(level)
    if type(n) is not int or not 1<=n<=N:
        raise TowerContractError("source address outside prefix")
    f=affine_endpoint(n,a,b)
    return f if f<=N else None


def affine_coefficients(coeffs, a, b):
    """Exact finite basis action on N=3^level; arbitrary N also admitted."""
    if type(coeffs) not in (tuple, list) or not coeffs:
        raise TowerContractError("nonempty coefficient vector")
    _integer(a,1)
    _integer(b,0)
    N=len(coeffs)
    out=[F()]*N
    for i, val in enumerate(coeffs,1):
        y=a*i+b
        if y<=N:
            out[y-1]+=_coeff(val)
        else:
            _coeff(val)  # still enforce exact source inputs even if exiting
    return tuple(out)


def affine_adjoint_coefficients(coeffs, a, b):
    if type(coeffs) not in (tuple,list) or not coeffs:
        raise TowerContractError("nonempty coefficient vector")
    _integer(a,1)
    _integer(b,0)
    N=len(coeffs)
    vals=tuple(_coeff(v) for v in coeffs)
    return tuple(vals[a*n+b-1] if a*n+b <=N else F() for n in range(1,N+1))


def prefix_composition_oracle(level,a,b,c,d):
    """Verify T_(a,b) T_(c,d)=T_(a*c,a*d+b), exhaustive finite oracle."""
    N=level_size(level)
    _integer(a,1);_integer(c,1);_integer(b,0);_integer(d,0)
    for n in range(1,N+1):
        inner=affine_cutoff(n,level,c,d)
        lhs=affine_cutoff(inner,level,a,b) if inner is not None else None
        rhs=affine_cutoff(n,level,a*c,a*d+b)
        if lhs!=rhs:
            raise ArithmeticError((level,a,b,c,d,n,lhs,rhs))
    return N


def exit_defect(level,a,b):
    """Exact nonintertwining J_k T_k vs T_(k+1) J_k at the finite boundary."""
    N=level_size(level)
    level_size(level+1)
    return tuple((n,a*n+b) for n in range(1,N+1)
                 if N<a*n+b<=3*N)


def sample_dirichlet(coeffs, exponents=None):
    """Exact finite Dirichlet evaluation on Re(s)=positive integers."""
    if type(coeffs) not in (tuple,list) or not coeffs:
        raise TowerContractError("nonempty coefficient vector")
    arr=tuple(_coeff(v) for v in coeffs)
    M=len(arr) if exponents is None else _integer(exponents,1)
    if M>40:
        raise TowerContractError("maximum 40 exact rational sample evaluations")
    return tuple(sum((val*F(1,n**s) for n,val in enumerate(arr,1)),F())
                 for s in range(1,M+1))


def inverse_dirichlet_samples(samples):
    """Independent exact Gaussian inverse for N<=12, no numeric interpolation."""
    if type(samples) not in (tuple,list) or not samples:
        raise TowerContractError("nonempty sample array")
    N=len(samples)
    if N>12:
        raise TowerContractError("inverse exact oracle limited to 12 samples")
    matrix=[[F(1,n**s) for n in range(1,N+1)]+[_coeff(samples[s-1])]
            for s in range(1,N+1)]
    for pivot in range(N):
        k=next((i for i in range(pivot,N) if matrix[i][pivot]!=0),None)
        if k is None:
            raise ArithmeticError("singular declared distinct positive source chart")
        matrix[pivot],matrix[k]=matrix[k],matrix[pivot]
        denom=matrix[pivot][pivot]
        matrix[pivot]=[q/denom for q in matrix[pivot]]
        for i in range(N):
            if i==pivot:continue
            mult=matrix[i][pivot]
            if mult:
                matrix[i]=[u-mult*v for u,v in zip(matrix[i],matrix[pivot])]
    return tuple(row[N] for row in matrix)


def lattice_ray_cosets(depth, branch):
    """L_{v,r}/(2^r Z_2)^2, with v one of three primitive normals."""
    if type(depth) is not int or not 1<=depth<=6:
        raise TowerContractError("finite 2-adic depth 1..6")
    if type(branch) is not int or branch not in (0,1,2):
        raise TowerContractError("three distinct initial lattice lines")
    M=2**depth
    a,b=NORMALS[branch]
    return frozenset((x,y) for x in range(M) for y in range(M)
                     if (a*x+b*y)%M==0)


def ray_distance(branch_a,depth_a,branch_b,depth_b):
    if type(branch_a) is not int or branch_a not in (0,1,2):
        raise TowerContractError("invalid first ray")
    if type(branch_b) is not int or branch_b not in (0,1,2):
        raise TowerContractError("invalid second ray")
    _integer(depth_a,0);_integer(depth_b,0)
    if depth_a==0 or depth_b==0:
        return depth_a+depth_b
    return abs(depth_a-depth_b) if branch_a==branch_b else depth_a+depth_b


def encoded_basis(level,n):
    """Unnormalized support of W_k|n>; each term amplitude 3^(-k/2)."""
    ds=arithmetic_digits(n,level)
    support=[]
    for js in product(range(3),repeat=level):
        out=tuple(tuple((js[r]+branch*ds[r])%3 for r in range(level))
                  for branch in range(3))
        support.append(out)
    assert len(set(support))==3**level
    return tuple(support)


def decoded_two_ray(pair,word):
    if pair not in PAIRS or type(word) is not tuple or len(word)!=3:
        raise TowerContractError("two visible rays of 3 required")
    length=len(word[0])
    if length<1 or length>7 or any(type(w) is not tuple or len(w)!=length for w in word):
        raise TowerContractError("matched positive finite ray depths expected")
    ds=[];ks=[]
    for r in range(length):
        i,k=pair_decode(pair,(word[pair[0]][r],word[pair[1]][r]))
        ds.append(i);ks.append(k)
    return tuple(ds),tuple(ks)


def boundary_affine(pair,word,a,b):
    """Actual operator acting on TWO RAYS only, pointwise on computational basis.

    Decoding the two rays gives a logical base-three index and spectator ancilla;
    the affine source map acts on logical index, preserving ancilla and erased ray.
    The output None is the zero vector due a legitimate finite cutoff.
    """
    ds,ks=decoded_two_ray(pair,word)
    level=len(ds)
    n=source_index(ds)
    dest=affine_cutoff(n,level,a,b)
    if dest is None:
        return None
    new_digits=arithmetic_digits(dest,level)
    result=[list(row) for row in word]
    for r in range(level):
        visible=pair_encode(new_digits[r],ks[r],pair)
        for index, digit in zip(pair, visible):
            result[index][r]=digit
    return tuple(tuple(row) for row in result)


def boundary_affine_adjoint(pair,word,a,b):
    """Adjoint of the finite injective positive-affine partial isometry."""
    ds,ks=decoded_two_ray(pair,word)
    level=len(ds)
    n=source_index(ds)
    _integer(a,1);_integer(b,0)
    if n<=b or (n-b)%a:
        return None
    predecessor=(n-b)//a
    if predecessor<1:
        return None
    new_digits=arithmetic_digits(predecessor,level)
    result=[list(row) for row in word]
    for r in range(level):
        visible=pair_encode(new_digits[r],ks[r],pair)
        for index, digit in zip(pair, visible):
            result[index][r]=digit
    return tuple(tuple(row) for row in result)


def two_ray_mirror_numerators(level,p,left_pair,right_pair,beta_even=2):
    """Finite even-beta thermofield after W_k on each side, exact Fraction.

    Compare B_p(L) and p^(beta/2) B_p^dagger(R), weights n^(-beta/2).
    Common physical amplitude 1/(3^level sqrt(Z_N)) omitted identically.
    """
    if not prime(p):
        raise TowerContractError("a true rational prime required")
    if type(beta_even) is not int or beta_even not in (2,4,6):
        raise TowerContractError("exact test supports only even beta=2,4,6")
    half=beta_even//2
    if left_pair not in PAIRS or right_pair not in PAIRS:
        raise TowerContractError("two valid boundary recovery regions required")
    N=level_size(level)
    if level>2:
        raise TowerContractError("full 2-sided enumerated oracle budget level <=2")
    left={};right={}
    for n in range(1,N+1):
        w=F(1,n**half)
        supports=encoded_basis(level,n)
        for l in supports:
            result_l=boundary_affine(left_pair,l,p,0)
            for r in supports:
                if result_l is not None:
                    key=(result_l,r)
                    left[key]=left.get(key,F())+w
                result_r=boundary_affine_adjoint(right_pair,r,p,0)
                if result_r is not None:
                    key=(l,result_r)
                    right[key]=right.get(key,F())+(p**half)*w
    return ({k:v for k,v in left.items() if v},
            {k:v for k,v in right.items() if v})


def encoded_refinement_oracle(level,n):
    """W_(k+1) J_k = (W_k tensor W|0>) on each codeword exactly."""
    level_size(level+1)
    if type(n) is not int or not 1<=n<=level_size(level):
        raise TowerContractError("original n outside smaller source chart")
    expected={tuple(ray+(j,) for ray in word)
              for word in encoded_basis(level,n) for j in range(3)}
    actual=set(encoded_basis(level+1,n))
    return (len(expected),expected==actual)


def source_boundary_exit(level,a,b):
    """Finite exit norm witness, not an excuse to assert strict tower naturality."""
    xs=exit_defect(level,a,b)
    return {'level':level,'a':a,'b':b,'witnesses':xs,
            'operator_norm':int(bool(xs)),
            'strong_limit_for_fixed_source_basis':True,
            'operator_norm_convergence_claimed':False}

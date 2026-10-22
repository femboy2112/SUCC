"""Exact source-weighted SUCC/FUCC reciprocal transport and Pascal prime occupations.

Scope: positive integer carrier, genuine prime V_p, p-residue clocks, finite
Gibbs detailed balance, flat weighted affine squares, and divided-power paths.
The complete infinite Markov/source and Hilbert statements require paper proofs.
Neither retrocausation, gravitational dynamics, nor Weil/RH positivity follows.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
from math import isqrt, prod


class ReciprocalSourceError(ValueError):
    """Wrong source, phase clock, cardinality, or numeric proof instrument."""


def integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise ReciprocalSourceError(f"exact integer >= {minimum} required")
    return x


def prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2,isqrt(p)+1))


def genuine_prime(p):
    if not prime(p):
        raise ReciprocalSourceError("actual rational prime, not fake generator")
    return p


def exact(v):
    if type(v) not in (int,Q):
        raise ReciprocalSourceError("only int/Fraction exact coefficients, no floats")
    return Q(v)


def vstar(n,p):
    """The actual FUCC Hilbert adjoint, not an inverse on nonmultiples."""
    integer(n,1); genuine_prime(p)
    return n//p if n%p==0 else None


def reciprocal_braid(n,p):
    """V_p* S^p |n> = S V_p* |n>, including the zero/nonunit sector."""
    integer(n,1); genuine_prime(p)
    lhs=vstar(n+p,p)
    q=vstar(n,p)
    rhs=(q+1) if q is not None else None
    return lhs,rhs


def residue_clock(n,p):
    """Bijective complete p-phase: n-1=p*(quotient-1)+residue."""
    integer(n,1); genuine_prime(p)
    return ((n-1)//p+1,(n-1)%p)


def from_residue_clock(quotient,residue,p):
    integer(quotient,1); genuine_prime(p)
    if type(residue) is not int or not 0<=residue<p:
        raise ReciprocalSourceError("complete residue witness required")
    return p*(quotient-1)+residue+1


def clock_succ(quotient,residue,p):
    """Local carry automaton encoding exactly one global additive successor."""
    from_residue_clock(quotient,residue,p)
    return ((quotient,residue+1) if residue<p-1 else (quotient+1,0))


def mixed_radix(n,p,q):
    """Two read orders; returned digits differ by a canonical carry permutation."""
    integer(n,1); genuine_prime(p); genuine_prime(q)
    x,r=residue_clock(n,p)
    m,s=residue_clock(x,q)
    y,u=residue_clock(n,q)
    mm,t=residue_clock(y,p)
    if m!=mm or p*s+r!=q*t+u:
        raise ArithmeticError("source-specific mixed-radix comparison failed")
    return ((m,s,r),(mm,t,u))


def direct_mixed_radix_change(s,r,p,q):
    """R=p*s+r=q*t+u, including nontrivial phase transport (not a swap)."""
    genuine_prime(p); genuine_prime(q)
    if type(s) is not int or type(r) is not int or not 0<=s<q or not 0<=r<p:
        raise ReciprocalSourceError("wrong mixed-radix source digits")
    R=p*s+r
    return (R//q,R%q)


def gibbs_unnormalized(n,beta):
    integer(n,1); integer(beta,2)
    return Q(1,n**beta)


def oriented_rates(n,target,beta):
    """Upward rate pi(target)/pi(n), reverse rate 1, under beta-log energy."""
    integer(n,1); integer(target,1); integer(beta,2)
    if target<=n:
        raise ReciprocalSourceError("upward edge must strictly increase arithmetic n")
    return Q(n,target)**beta,Q(1)


def finite_source_edges(N,primes,beta):
    """Distinguish parallel SUCC and prime FUCC channels, no fake primes."""
    integer(N,2); integer(beta,2)
    ps=tuple(genuine_prime(p) for p in primes)
    if len(set(ps))!=len(ps):
        raise ReciprocalSourceError("duplicate prime source label")
    edges=[]
    for n in range(1,N+1):
        if n+1<=N:
            up,down=oriented_rates(n,n+1,beta)
            edges.append((n,n+1,"S",up,down))
        for p in ps:
            if p*n<=N:
                up,down=oriented_rates(n,p*n,beta)
                edges.append((n,p*n,f"V_{p}",up,down))
    return tuple(edges)


def finite_generator(N,primes,beta):
    """Finite reflecting-boundary continuous-time generator as exact rationals."""
    edges=finite_source_edges(N,primes,beta)
    G=[[Q(0) for _ in range(N)] for _ in range(N)]
    for n,m,_,up,down in edges:
        G[n-1][m-1]+=up
        G[m-1][n-1]+=down
        G[n-1][n-1]-=up
        G[m-1][m-1]-=down
    return tuple(tuple(r) for r in G)


def finite_stationarity(N,primes,beta):
    """Exact detailed balance per edge, row sums, and pi L=0."""
    G=finite_generator(N,primes,beta)
    unscaled=tuple(gibbs_unnormalized(n,beta) for n in range(1,N+1))
    Z=sum(unscaled,Q())
    pi=tuple(t/Z for t in unscaled)
    edge_fails=[]
    for n,m,source,up,down in finite_source_edges(N,primes,beta):
        if pi[n-1]*up!=pi[m-1]*down:
            edge_fails.append((n,m,source))
    row_sums=tuple(sum(row,Q()) for row in G)
    balance=tuple(sum((pi[i]*G[i][j] for i in range(N)),Q()) for j in range(N))
    return {"edge_fails":edge_fails,"row_sums":row_sums,"pi_L":balance,
            "Z":Z,"pi":pi,"edges":finite_source_edges(N,primes,beta)}


def finite_dirichlet_form(values,N,primes,beta):
    if len(values)!=N:
        raise ReciprocalSourceError("one observable per source state")
    f=tuple(exact(v) for v in values)
    z=sum((gibbs_unnormalized(n,beta) for n in range(1,N+1)),Q())
    energy=Q()
    for n,m,_,up,_ in finite_source_edges(N,primes,beta):
        energy+=(gibbs_unnormalized(n,beta)/z)*up*(f[n-1]-f[m-1])**2
    return energy


def weighted_affine_diamond(n,p,beta):
    """V_p S versus S^p V_p: both channel-rate path products, exact."""
    integer(n,1); genuine_prime(p); integer(beta,2)
    left=oriented_rates(n,n+1,beta)[0]*oriented_rates(n+1,p*(n+1),beta)[0]
    right=oriented_rates(n,p*n,beta)[0]
    for j in range(p):
        right*=oriented_rates(p*n+j,p*n+j+1,beta)[0]
    direct=Q(n,p*(n+1))**beta
    return left,right,direct


def tfd_mirror_coefficient(n,a,b,beta_even=2):
    """M_beta(U_ab) e_(a*n+b) = ((a*n+b)/n)^(beta/2) e_n."""
    integer(n,1); integer(a,1); integer(b,0)
    if type(beta_even) is not int or beta_even<2 or beta_even%2:
        raise ReciprocalSourceError("finite exact mirror requires even beta")
    return Q(a*n+b,n)**(beta_even//2)


def mirror_affine_on_basis(m,a,b,beta_even=2):
    integer(m,1); integer(a,1); integer(b,0)
    if type(beta_even) is not int or beta_even<2 or beta_even%2:
        raise ReciprocalSourceError("finite exact mirror requires even beta")
    if m<=b or (m-b)%a:
        return None
    n=(m-b)//a
    if n<1:
        return None
    return (n,tfd_mirror_coefficient(n,a,b,beta_even))


def _complete_occupations(width,rank):
    """Independent direct finite oracle, no path recurrence used."""
    if width==1:
        yield (rank,)
        return
    for k in range(rank+1):
        for tail in _complete_occupations(width-1,rank-k):
            yield (k,)+tail


def pascal_prime_rank(primes,rank,beta_even=2):
    """Vacuum divided-power exponential: C_p|alpha>=(alpha_p+1)|alpha+e_p>."""
    ps=tuple(genuine_prime(p) for p in primes)
    if not ps or len(ps)>5 or len(set(ps))!=len(ps):
        raise ReciprocalSourceError("1..5 distinct prime channels required")
    integer(rank,0)
    if rank>9 or type(beta_even) is not int or beta_even<2 or beta_even%2:
        raise ReciprocalSourceError("finite exact budget beta even, rank<=9")
    weights=tuple(Q(1,p**(beta_even//2)) for p in ps)
    out={(0,)*len(ps):Q(1)}
    for k in range(1,rank+1):
        nxt={}
        for alpha,amplitude in out.items():
            for i,weight in enumerate(weights):
                b=list(alpha)
                b[i]+=1
                b=tuple(b)
                nxt[b]=nxt.get(b,Q())+amplitude*weight*(alpha[i]+1)/k
        out=nxt
    return out


def direct_prime_rank(primes,rank,beta_even=2):
    ps=tuple(genuine_prime(p) for p in primes)
    if not ps or len(ps)>5 or len(set(ps))!=len(ps):
        raise ReciprocalSourceError("valid finite prime catalog required")
    integer(rank,0)
    if rank>9 or type(beta_even) is not int or beta_even<2 or beta_even%2:
        raise ReciprocalSourceError("finite exact rank and thermal exponent expected")
    return {alpha:Q(1,prod(p**(alpha[i]*(beta_even//2)) for i,p in enumerate(ps)))
            for alpha in _complete_occupations(len(ps),rank)}


def pascal_last_step(alpha):
    """Cotransition in an endpoint-conditioned flat divided-power path ensemble."""
    if type(alpha) is not tuple or not alpha or any(type(a) is not int or a<0 for a in alpha):
        raise ReciprocalSourceError("exact positive occupation coordinate required")
    k=sum(alpha)
    if not k:
        return {}
    return {tuple(a-(i==j) for j,a in enumerate(alpha)):Q(alpha[i],k)
            for i in range(len(alpha)) if alpha[i]}


def gibbs_rank_nonprojective(primes,beta=2):
    """Two-prime, rank2 -> rank1 Pascal cotransition vs Gibbs rank1.

    Neither finite rank conditional is the initial segment law of all others
    under alpha_p/k cotransitions for unequal thermal prime weights.
    """
    ps=tuple(genuine_prime(p) for p in primes)
    if len(ps)!=2 or ps[0]==ps[1]:
        raise ReciprocalSourceError("two distinct authenticated primes")
    integer(beta,2)
    q=tuple(Q(1,p**beta) for p in ps)
    expected=q[0]/sum(q)
    h2=q[0]**2+q[0]*q[1]+q[1]**2
    projected=(q[0]**2+q[0]*q[1]/2)/h2
    return expected,projected

"""Source-relative shape covariance versus edge-valued noncommutativity.

The continuum theorem is established in the companion mathematical dossier.
These Fraction matrices are INDEPENDENT lattice controls, not quadrature of
the original real Gamma.  The genuine Suzuki source is checked separately.
"""
from fractions import Fraction as F


class TransportError(ValueError):
    pass


def rat(x):
    if type(x) not in (int, F):
        raise TransportError("integer/Fraction only")
    return F(x)


def multiply(A, B):
    n = len(A)
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(n)), F(0))
                       for j in range(n)) for i in range(n))


def subtract(A, B):
    n = len(A)
    return tuple(tuple(A[i][j]-B[i][j] for j in range(n)) for i in range(n))


def add(A, B):
    n = len(A)
    return tuple(tuple(A[i][j]+B[i][j] for j in range(n)) for i in range(n))


def wedge(u, v):
    n = len(u)
    return tuple(tuple(u[i]*v[j]-v[i]*u[j] for j in range(n))
                 for i in range(n))


def exact_rank(A):
    if not A or any(len(row) != len(A) for row in A):
        raise TransportError("nonempty square rational matrix required")
    M = [list(map(rat, row)) for row in A]
    n, rank = len(M), 0
    for j in range(n):
        pivot = next((k for k in range(rank, n) if M[k][j]), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        v = M[rank][j]
        M[rank] = [z/v for z in M[rank]]
        for k in range(rank+1, n):
            factor = M[k][j]
            if factor:
                M[k] = [z-factor*w for z,w in zip(M[k], M[rank])]
        rank += 1
    return rank


def finite_boundary_control(n=13, k=9, q=F(1,2)):
    """Rational Toeplitz E_ij=q^|i-j|, compressed shift A and exterior paths.

    Odd n centers reflection at an INTEGER for rational parity checks.
    k>n/2 gives separate nonempty L, C and R; k<n-1 avoids degeneracy.
    """
    if (type(n) is not int or type(k) is not int or n < 9 or n > 21
            or n % 2 != 1 or not n//2 < k < n-1):
        raise TransportError("odd finite window with both edges and center required")
    q = rat(q)
    if not 0 < q < 1:
        raise TransportError("0<q<1 exponential-kernel surrogate required")
    a = tuple(tuple(F(int(i==j+k)+int(i+k==j)) for j in range(n))
              for i in range(n))
    e = tuple(tuple(q**abs(i-j) for j in range(n)) for i in range(n))
    direct = subtract(multiply(a,e), multiply(e,a))
    for s in (-n, -2, 0, 3, n):
        if any(q**abs((i+s)-(j+s))!=e[i][j]
               for i in range(n) for j in range(n)):
            raise ArithmeticError("unrestricted kernel form not covariant")
    # Independently sum paths that leave the observation window.
    outside = tuple(range(-k,0)) + tuple(range(n,n+k))
    leaked = tuple(tuple(sum((
        q**abs(i-z)*F(int(z==j+k)+int(z==j-k)) -
        F(int(i==z+k)+int(i+k==z))*q**abs(z-j)
        for z in outside),F(0)) for j in range(n)) for i in range(n))
    origin=(n-1)//2
    hp=tuple(q**(-(i-origin)) for i in range(n))
    hm=tuple(q**(i-origin) for i in range(n))
    rp=tuple(hp[i] if i>=k else F(0) for i in range(n))
    lm=tuple(hm[i] if i<n-k else F(0) for i in range(n))
    boundary=tuple(tuple(q**k*(rp[i]*hm[j]-hm[i]*rp[j]
                                  +lm[i]*hp[j]-hp[i]*lm[j])
                        for j in range(n)) for i in range(n))
    ue=tuple(rp[i]+lm[i] for i in range(n))
    ve=tuple(hm[i]+hp[i] for i in range(n))
    uo=tuple(rp[i]-lm[i] for i in range(n))
    vo=tuple(hm[i]-hp[i] for i in range(n))
    pe=tuple(tuple(q**k*F(1,2)*x for x in row) for row in wedge(ue,ve))
    po=tuple(tuple(q**k*F(1,2)*x for x in row) for row in wedge(uo,vo))
    if direct!=leaked or direct!=boundary or direct!=add(pe,po):
        raise ArithmeticError("direct, exterior and rank-four paths disagree")
    if any(direct[i][j]!=-direct[j][i] for i in range(n) for j in range(n)):
        raise ArithmeticError("commutator not skew")
    if any(ue[i]!=ue[n-1-i] or ve[i]!=ve[n-1-i] or
           uo[i]!=-uo[n-1-i] or vo[i]!=-vo[n-1-i] for i in range(n)):
        raise ArithmeticError("incorrect reflection sector transport")
    ranks=(exact_rank(direct),exact_rank(pe),exact_rank(po))
    if ranks!=(4,2,2):
        raise ArithmeticError("rank-four/two-parity packet obstruction false")
    return {
        "source_type":"RATIONAL_LATTICE_CONTROL_NOT_ORIGINAL_GAMMA_QUADRATURE",
        "cells":n,"shift":k,"q":str(q),
        "unrestricted_form_covariant":True,
        "same_window_commuting":False,
        "exterior_leakage_identity":True,
        "rank_four_boundary":ranks[0],
        "even_parity_rank":ranks[1],
        "odd_parity_rank":ranks[2],
        "full_gamma_tower_rank_four_proved":False,
        "source_S4_positive_proved":False,
        "RH_proved":False,
    }


def original_source_transport_contract():
    """Gate continuum theorem's b, alpha, prime and provenance assumptions."""
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from . import source_weil_hierarchy as source
    sha=verify_original_suzuki_source()["source_git_blob"]
    if sha!="0cc8510b71d178fc79e8d410a86d8b6014cf9178":
        raise TransportError("original signed source Git blob mismatch")
    if source.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise TransportError("genuine first-prime impulse absent")
    b=source.log2_iv()
    if not F(1,2)<b.lo<=b.hi<F(1):
        raise TransportError("source log2 violates exact edge geometry")
    return {
        "source_type":"ORIGINAL_SUZUKI_FIRST_PRIME_REAL_GAMMA",
        "source_git_blob":sha,"prime_wavefront":((2,2)),
        "source_log2_interval":(str(b.lo),str(b.hi)),
        "first_real_gamma_alpha":"1/2",
        "single_rung_continuum_boundary_rank":4,
        "single_rung_each_parity_rank":2,
        "proof_status":"PAPER_PROVED_SEPARATE_FROM_RATIONAL_CONTROL",
        "whole_gamma_tower_rank_four_proved":False,
        "S4_positive_proved":False,"RH_proved":False,
    }

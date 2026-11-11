"""Exact finite covariance split for the source-labelled parity observer.

The source adapter PPP-02 uses integer-completed parity
s_n=(-1)^floor(U_n+T_n).  The first fractional hexadecimal-digit parity
f({U_n+T_n}) is s_(n+1); finite epoch means differ by a paid endpoint term.
See the signed covariance audit in the Cayley source observer dossier.

This module accepts supplied exact sign rows; it does not reconstruct or
validate their BBP/CRT provenance.  Its identities hold for those finite
rows, and do not establish source-selected asymptotic cancellation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class SignedSample:
    """One exact sign row; source provenance is a separate adapter obligation."""
    n: int
    a: int   # prime-side sign
    b: int   # complete complementary sign
    s: int   # supplied real parity, required to equal a*b
    eps: int # future-tail integer-boundary correction, in {0,1}

    def __post_init__(self) -> None:
        if type(self.n) is not int or self.n < 0:
            raise ValueError("n must be a nonnegative integer")
        if any(type(v) is not int or v not in (-1,1)
               for v in (self.a,self.b,self.s)):
            raise ValueError("a, b and s must be exact integer signs")
        if self.s != self.a*self.b:
            raise ValueError("source parity must satisfy s=a*b")
        if type(self.eps) is not int or self.eps not in (0,1):
            raise ValueError("eps must be an exact integer bit")


def _rows(rows) -> tuple[SignedSample, ...]:
    rows = tuple(rows)
    if not rows:
        raise ValueError("a nonempty sequence of signed samples is required")
    if any(type(row) is not SignedSample for row in rows):
        raise TypeError("SignedSample rows required")
    return rows


def _mean(values) -> Q:
    values = tuple(values)
    return Q(sum(values),len(values))


def _covariance(a, b) -> Q:
    a, b = tuple(a), tuple(b)
    return _mean(x*y for x,y in zip(a,b))-_mean(a)*_mean(b)


def covariance(rows) -> Q:
    """Exact Cov(a,b)=E[ab]-E[a]E[b], for every nonempty valid sample."""
    rows = _rows(rows)
    return _covariance((r.a for r in rows),(r.b for r in rows))


def two_fiber_table(rows):
    """Exact counts and beta=(E[b|a=1]-E[b|a=-1])/2.

    Both conditioning fibers must be populated.  ``P`` means E[a*b];
    the old implementation erroneously returned E[b] under this key.
    """
    from collections import Counter
    rows = _rows(rows)
    counts = Counter((r.a,r.b) for r in rows)
    pp,pm,mp,mm = (counts[pair] for pair in ((1,1),(1,-1),(-1,1),(-1,-1)))
    if not pp+pm or not mp+mm:
        raise ValueError("both source-sign fibers must be populated")
    u_plus = Q(pp-pm,pp+pm)
    u_minus = Q(mp-mm,mp+mm)
    return {
        'pp': pp, 'pm': pm, 'mp': mp, 'mm': mm,
        'u_plus': u_plus, 'u_minus': u_minus,
        'beta': (u_plus-u_minus)/2,
        'm': Q(pp+pm-mp-mm,len(rows)),
        'P': Q(pp+mm-pm-mp,len(rows)),
        'complement_mean': Q(pp+mp-pm-mm,len(rows)),
    }


def tail_boundary_coupling(rows) -> Q:
    """The change in Cov(a,b) caused by the supplied boundary corrections.

    Put c=b*(-1)^eps, the complement after removing those corrections.
    Return Cov(a,b)-Cov(a,c)=2*Cov(a,b*eps) exactly.  This preserves the
    historical function name while fixing its old implementation, which
    accidentally computed the different observable Cov(a*b,eps).
    """
    rows = _rows(rows)
    a = tuple(r.a for r in rows)
    b_eps = tuple(r.b*r.eps for r in rows)
    return 2*_covariance(a,b_eps)


def check_decomposition_identity(rows) -> dict:
    """Exact covariance linearity under b=b*eps+b*(1-eps).

    This is a finite identity for supplied rows.  A small source tail alone
    does not prove that the supplied eps=1 rows have small frequency.
    """
    rows = _rows(rows)
    a = tuple(r.a for r in rows)
    cov_eps = _covariance(a,(r.b*r.eps for r in rows))
    cov_neps = _covariance(a,(r.b*(1-r.eps) for r in rows))
    total = cov_eps+cov_neps
    return {
        'cov_eps': cov_eps,
        'cov_neps': cov_neps,
        'sum': total,
        'matches_direct': total==covariance(rows),
    }


if __name__=='__main__':
    # Synthetic reproduction of previously certified counts, not a new
    # source reconstruction or independently measured boundary frequency.
    rows=[]
    for a,b,count in ((1,1,133),(1,-1,121),(-1,1,125),(-1,-1,133)):
        rows.extend(SignedSample(0,a,b,a*b,0) for _ in range(count))
    table=two_fiber_table(rows)
    print('2x2 table:',table)
    print('Cov(a,b) =',covariance(rows),'= (1-m^2)*beta =',
          (1-table['m']**2)*table['beta'])
    print('decomposition (supplied eps=0):',check_decomposition_identity(rows))

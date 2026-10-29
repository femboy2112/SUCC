"""Exact finite SUCC Pólya source, observer selection and history likelihoods.

Research model: contains no zeta-zero positions, no physical-work assumption.
"""
from fractions import Fraction


def f(x):
    return Fraction(x)


def native_birth(j,k):
    assert 0 <= k <= j
    return Fraction(k+1,j+2)


def controlled_birth(a,j,k):
    a=f(a)
    assert 0 < a < 1 and 0 <= k <= j
    return a**(j+1-k)*(1-a**(k+1))/(1-a**(j+2))


def source(j):
    return [Fraction(1,j+1)]*(j+1)


def tilted(a,j):
    a=f(a)
    assert 0 < a < 1 and j >= 0
    z=sum((a**k for k in range(j+1)),Fraction(0))
    return [a**k/z for k in range(j+1)]


def selection(a,j):
    """Snapshot sampling: P(A|k)=a**k; condition on accepted A."""
    a=f(a)
    p=source(j)
    accept=sum((p[k]*a**k for k in range(j+1)),Fraction(0))
    return [p[k]*a**k/accept for k in range(j+1)], accept


def history(j,a=None):
    """Probability of each binary word of increments, native or controlled."""
    h={():Fraction(1)}
    for i in range(j):
        nxt={}
        for word,prob in h.items():
            k=sum(word)
            t=native_birth(i,k) if a is None else controlled_birth(a,i,k)
            nxt[word+(0,)]=prob*(1-t)
            nxt[word+(1,)]=prob*t
        h=nxt
    return h


def selected_history_at_terminal(a,j):
    """A source trajectory sampled once and accepted with probability a**K_j."""
    a=f(a)
    p=history(j)
    z=sum((v*a**sum(w) for w,v in p.items()),Fraction(0))
    return {w:v*a**sum(w)/z for w,v in p.items()},z


def finite_history_rejection(a,j):
    """Any finite controlled history law has a source-postselection realization."""
    p=history(j)
    q=history(j,a)
    assert all(v>0 for v in p.values())
    M=max(q[w]/p[w] for w in p)
    acceptance={w:(q[w]/p[w])/M for w in p}
    success=sum((p[w]*acceptance[w] for w in p),Fraction(0))
    posterior={w:p[w]*acceptance[w]/success for w in p}
    assert posterior==q and success == 1/M
    return success, acceptance

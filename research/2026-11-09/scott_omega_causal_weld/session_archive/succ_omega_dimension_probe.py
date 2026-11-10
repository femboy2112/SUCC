"""Local, standalone probes for the SUCC / lambda-omega dimensional hypothesis.

Scope: exact lambda beta steps for omega(k) chains; structural finite
product-grid tests; CRT/Fourier reindexing; spherical chart/curvature
checks. This does NOT establish a C-monoid construction or pi normality.
No GitHub writes. Python 3.10+, standard library only.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from collections import Counter
from itertools import product


@dataclass(frozen=True)
class Var:
    name: str


@dataclass(frozen=True)
class Abs:
    var: str
    body: object


@dataclass(frozen=True)
class App:
    fn: object
    arg: object


def apply_many(items):
    assert len(items) >= 2
    head = App(items[0], items[1])
    for item in items[2:]:
        head = App(head, item)
    return head


def omega(k):
    assert k >= 2
    return Abs('x', apply_many([Var('x')] * k))


def omega_chain(k, copies):
    assert copies >= 2
    return apply_many([omega(k)] * copies)


def substitute_closed(term, name, replacement):
    """Capture-safe in this probe ONLY because replacement is a closed omega(k)."""
    if isinstance(term, Var):
        return replacement if term.name == name else term
    if isinstance(term, Abs):
        return term if term.var == name else Abs(term.var, substitute_closed(term.body, name, replacement))
    if isinstance(term, App):
        return App(substitute_closed(term.fn, name, replacement),
                   substitute_closed(term.arg, name, replacement))
    raise TypeError(type(term))


def leftmost_beta(term):
    if isinstance(term, App):
        if isinstance(term.fn, Abs):
            return substitute_closed(term.fn.body, term.fn.var, term.arg), True
        head, did = leftmost_beta(term.fn)
        if did:
            return App(head, term.arg), True
        arg, did = leftmost_beta(term.arg)
        return (App(term.fn, arg), True) if did else (term, False)
    if isinstance(term, Abs):
        body, did = leftmost_beta(term.body)
        return (Abs(term.var, body), True) if did else (term, False)
    return term, False


def test_omega():
    cases = 0
    for k in range(2, 9):
        for initial_copies in (2, 3, 5, 8):
            t = omega_chain(k, initial_copies)
            for s in range(5):
                expected = omega_chain(k, initial_copies + s * (k - 2))
                assert t == expected, (k, initial_copies, s)
                t, did = leftmost_beta(t)
                assert did
                cases += 1
    # Important: self-application at k=2 loops, but at k>2 grows syntactically.
    return cases


def test_independent_grid():
    cases = 0
    for depth in range(1, 16):
        states = {(i, j) for i in range(depth + 1) for j in range(depth + 1 - i)}
        assert len(states) == (depth + 1) * (depth + 2) // 2
        # A single raw Ω4 trajectory has only depth+1 distinct syntactic lengths.
        assert len(states) > depth + 1
        for i, j in states:
            if i + j < depth:
                sx = lambda p: (p[0] + 1, p[1])
                sy = lambda p: (p[0], p[1] + 1)
                assert sx(sy((i, j))) == sy(sx((i, j)))
                cases += 1
    return cases


def crt_map(t, m, n):
    return (t % m, t % n)


def phase_hist_2d(m, n, weights, h, k):
    """Exact formal sum over powers of a primitive (m*n)-th root of unity."""
    return Counter({r: sum(v for (i, j), v in weights.items()
                           if (n*h*i + m*k*j) % (m*n) == r)
                    for r in range(m*n)})


def phase_hist_1d(m, n, weights, h, k):
    L = m*n
    idx = (n*h + m*k) % L
    return Counter({r: sum(weights[crt_map(t,m,n)] for t in range(L)
                           if idx*t % L == r) for r in range(L)})


def test_crt_fourier():
    m, n = 3, 4
    assert gcd(m,n) == 1
    L = m*n
    assert len({crt_map(t,m,n) for t in range(L)}) == L
    a_x = next(a for a in range(L) if a%m == 1 and a%n == 0)
    a_y = next(a for a in range(L) if a%m == 0 and a%n == 1)
    assert (a_x, a_y) == (4, 9)
    for t in range(L):
        i,j = crt_map(t,m,n)
        assert crt_map(t+a_x,m,n) == ((i+1)%m,j)
        assert crt_map(t+a_y,m,n) == (i,(j+1)%n)
    weights = {(i,j): 1 + 2*i + 3*j + i*j for i in range(m) for j in range(n)}
    count = 0
    for h,k in product(range(m),range(n)):
        assert phase_hist_2d(m,n,weights,h,k) == phase_hist_1d(m,n,weights,h,k)
        count += 1
    # The 12 2D Fourier modes map bijectively to 12 1D modes.
    assert len({(n*h+m*k)%L for h,k in product(range(m),range(n))}) == L
    # Equal sizes: diagonal synchronized walk has uniform x and y marginals
    # but leaves 240/256 sites and has nonzero joint Fourier (h,k)=(1,15).
    side = 16
    diagonal = [(t,t) for t in range(side)]
    assert len(set(diagonal)) == side and side*side-len(set(diagonal)) == 240
    assert {x for x,y in diagonal} == {y for x,y in diagonal} == set(range(side))
    assert all((x+15*y)%side == 0 for x,y in diagonal)
    # Since every character value equals 1 on this walk, average is exactly 1.
    # The uniform 16x16 law gives average zero for (1,15) character.
    return count, (a_x,a_y)


def test_curried_pinbed():
    cases = 0
    for nx,ny in ((3,4),(8,9),(16,16)):
        # A sheet as two indexed successors and as one function-valued row.
        pin = lambda i,j: i*i+7*j+3*i*j
        curried = lambda i: lambda j: pin(i,j)
        uncurried = lambda p: curried(p[0])(p[1])
        for i,j in product(range(nx),range(ny)):
            assert pin(i,j) == uncurried((i,j))
            cases += 1
    return cases


def inverse_complex_fraction(z):
    a,b = z
    norm = a*a+b*b
    if norm == 0:
        raise ZeroDivisionError
    return (a/norm,-b/norm)


def test_sphere():
    cases = 0
    for z in [(Fraction(1), Fraction(0)),
              (Fraction(1), Fraction(1)),
              (Fraction(3,2), Fraction(-7,3)),
              (Fraction(-2,5), Fraction(19,13))]:
        assert inverse_complex_fraction(inverse_complex_fraction(z)) == z
        cases += 1
    # Regular octahedron: V=6,E=12,F=8, 4 equilateral faces at each vertex.
    V,E,F = 6,12,8
    assert V-E+F == 2
    angular_defect_over_pi = Fraction(2) - 4*Fraction(1,3)
    assert angular_defect_over_pi == Fraction(2,3)
    assert V*angular_defect_over_pi == 4 # total integrated curvature 4π
    return cases



def test_plaquette_holonomy():
    """A finite synthetic 2D U(1) connection, NOT an authentic BBP phase."""
    L = 16
    ux = lambda i,j: j % L
    uy = lambda i,j: 0
    def curvature(ax,ay,i,j):
        # x then y versus y then x: sum of integer root-of-unity exponents
        return (ax(i,j) + ay(i+1,j) - ax(i,j+1) - ay(i,j)) % L
    g = lambda i,j: (3*i+7*j+i*j) % L
    ux2 = lambda i,j: (ux(i,j) + g(i,j) - g(i+1,j)) % L
    uy2 = lambda i,j: (uy(i,j) + g(i,j) - g(i,j+1)) % L
    cells=0
    for i,j in product(range(8),range(8)):
        assert curvature(ux,uy,i,j) == 15 # e^(-2πi/16), nonflat
        assert curvature(ux2,uy2,i,j) == 15 # gauge invariant
        assert curvature(lambda x,y:0,lambda x,y:0,i,j) == 0
        cells+=1
    return cells


def main():
    print('OMEGA: verified beta-growth E_k(m) -> E_k(m+k-2) in',test_omega(),'independent exact reductions')
    print('GRID: independent 2D SUCCs commute; growth-rank contrast in',test_independent_grid(),'states')
    modes, steps = test_crt_fourier()
    print('CRT: 3x4 torus equals 12-state one-clock scan,',modes,'exact Fourier modes, local steps',steps)
    print('CRT NEGATIVE: 16x16 diagonal leaves 240 pins unvisited, has invisible non-Haar Fourier mode (1,15)')
    print('CURRY: verified',test_curried_pinbed(),'exact pin readings in uncurried and curried descriptions')
    print('SPHERE: verified',test_sphere(),'exact stereographic transitions, octahedral Euler=2 and defect sum=4pi')
    print('HOLONOMY: verified',test_plaquette_holonomy(),'synthetic flux plaquettes + gauge invariance, NOT source-derived')
    print('SCOPE: no full C-monoid, topological dimension collapse, source-selected decay, or π-normality proof')

if __name__ == '__main__':
    main()
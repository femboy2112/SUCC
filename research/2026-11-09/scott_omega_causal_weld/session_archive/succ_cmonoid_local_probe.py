"""SUCC C-monoid/categorical-shadow exploratory receipts.

Read-only research prototype, NOT a construction of a C-monoid.

Only Python standard library. Uses affine submonoid and its arrow-category
squares/cubes, plus a finite transformation-monoid Karoubi proxy.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product

@dataclass(frozen=True)
class Affine:
    a: Fraction
    b: Fraction

    def __post_init__(self):
        object.__setattr__(self, 'a', Fraction(self.a))
        object.__setattr__(self, 'b', Fraction(self.b))
        assert self.a > 0

    def __call__(self, x):
        return self.a * Fraction(x) + self.b

    def after(self, other):
        """self ◦ other"""
        return Affine(self.a * other.a, self.a * other.b + self.b)

    def power(self, n):
        assert n >= 0
        out = ID
        for _ in range(n):
            out = self.after(out)
        return out

ID = Affine(1, 0)
S = Affine(1, 1)

def V(p):
    assert p >= 1
    return Affine(p,0)

@dataclass(frozen=True)
class Square:
    """An arrow in Arr(BM): src -> dst via left and right."""
    src: Affine
    dst: Affine
    left: Affine
    right: Affine

    def __post_init__(self):
        assert self.right.after(self.src) == self.dst.after(self.left), 'square does not commute'

    def then(self, other):
        assert self.dst == other.src
        return Square(self.src, other.dst,
                      other.left.after(self.left),
                      other.right.after(self.right))

@dataclass(frozen=True)
class Cube:
    """An arrow in Arr(Arr(BM)): a commuting cube of four Square arrows."""
    front: Square
    back: Square
    top: Square
    bottom: Square

    def __post_init__(self):
        assert self.top.src == self.front.src
        assert self.top.dst == self.back.src
        assert self.bottom.src == self.front.dst
        assert self.bottom.dst == self.back.dst
        assert self.front.then(self.bottom) == self.top.then(self.back), 'cube does not commute'

def alpha(p,k):
    """V_p ∘ S^k = S^(pk) ∘ V_p, as arrow category morphism."""
    return Square(S.power(k), S.power(p*k), V(p), V(p))


def four_pole_r(n):
    assert n >= 1
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def block(n, length):
    """U_(n+length) from U_n: the actual frozen four-pole source."""
    assert n >= 0 and length >= 0
    corr = sum((16**(length-j) * four_pole_r(n+j)
                for j in range(1,length+1)), Fraction(0))
    return Affine(16**length, corr)


def compose_maps(f,g):
    """On a finite set, f ∘ g for functions represented by value tuples."""
    return tuple(f[g[i]] for i in range(len(f)))


def finite_karoubi_proxy(n=3):
    """NOT a C-monoid: finite all-functions transformation monoid proxy."""
    maps = [tuple(values) for values in product(range(n), repeat=n)]
    ids = [f for f in maps if compose_maps(f,f) == f]
    pairs = {(e,f):[a for a in maps if compose_maps(f,compose_maps(a,e))==a]
             for e in ids for f in ids}
    for e in ids:
        assert e in pairs[e,e]
    for e in ids:
        for f in ids:
            for g in ids:
                for a in pairs[e,f]:
                    for b in pairs[f,g]:
                        assert compose_maps(b,a) in pairs[e,g]
    return len(maps),len(ids),sum(len(v) for v in pairs.values()),len(pairs)


def observer_congruence_control():
    """A one-point probe fiber does not define a congruence under precomposition."""
    f = (0,1,2)                 # identity on a 3-point carrier
    g = (0,0,2)                 # f(0)=g(0), f(1)!=g(1)
    h = (1,1,1)                 # h transports the probe at 0 to hidden input 1
    probe = {0}
    assert all(f[x] == g[x] for x in probe)
    fh = compose_maps(f,h)
    gh = compose_maps(g,h)
    assert fh[0] != gh[0]
    # Stable probe closure under all endomorphisms: {0,1,2}.
    carrier = tuple(range(3))
    all_maps = list(product(carrier, repeat=3))
    closure = {z[i] for z in all_maps for i in probe}
    assert closure == set(carrier)
    return len(closure)


def normalize_law(law):
    out = {}
    for x,mass in law.items():
        x=Fraction(x)%1
        out[x]=out.get(x,Fraction(0))+Fraction(mass)
    return {x:m for x,m in out.items() if m}


def tail_push(law):
    """T_* for T(x)={16x}; an exact rational atomic law."""
    out={}
    for x,mass in law.items():
        t=(16*x)%1
        out[t]=out.get(t,Fraction(0))+mass
    return normalize_law(out)


def uniform_preimages(law):
    """C gives 16 uniformly weighted antecedents of each actual tail."""
    out={}
    for y,mass in law.items():
        for a in range(16):
            t=(a+y)/16
            out[t]=out.get(t,Fraction(0))+mass/16
    return normalize_law(out)


def Q(law):
    return uniform_preimages(tail_push(law))


def haar_split_control():
    laws=[{Fraction(0):Fraction(1)},
          {Fraction(1,7):Fraction(1)},
          {Fraction(1,7):Fraction(2,3), Fraction(3,11):Fraction(1,3)}]
    for law in laws:
        assert tail_push(uniform_preimages(law)) == law
        assert Q(Q(law)) == Q(law)
    grid=Q({Fraction(0):Fraction(1)})
    assert len(grid)==16 and set(grid.values())=={Fraction(1,16)}
    # Uniform first digit of a finite 16-grid is not a uniform measure on the circle.
    assert tail_push(grid)=={Fraction(0):Fraction(1)}
    return len(laws)


def run():
    # Monoid's categorical successor and factorization identities.
    for p,q in [(2,3),(2,5),(3,7),(11,13)]:
        assert V(p).after(S) == S.power(p).after(V(p))
        assert V(p).after(V(q)) == V(p*q) == V(q).after(V(p))
        assert V(p).after(S) != S.after(V(p))
        # Higher coherent cube induced solely by the affine monoid.
        cube = Cube(front=alpha(p,1), back=alpha(p,q),
                    top=alpha(q,1), bottom=alpha(q,p))
        lhs = cube.front.then(cube.bottom)
        rhs = cube.top.then(cube.back)
        assert lhs == rhs == Square(S, S.power(p*q), V(p*q), V(p*q))
    print('AFFINE: 4 independent (p,q) instances of source/target-square + cube interchange verified')

    # Source-labelled block law: chronological grouping is associative.
    blocks_tested = 0
    for n in [0,1,7,16]:
        for p in range(0,5):
            for q in range(0,5):
                assert block(n+p,q).after(block(n,p)) == block(n,p+q)
                blocks_tested += 1
    assert block(0,1)(0) == four_pole_r(1)
    print(f'BBP: {blocks_tested} exact Fraction block-composition equalities verified')

    # Divergence of history and a lossy future fractional-state quotient.
    s=Fraction(0)
    t=Fraction(1,16)
    for n in range(1,10):
        assert (block(0,n)(s)-block(0,n)(t)).denominator == 1
    assert block(0,0)(s) != block(0,0)(t)
    print('SEED: zero and 1/16 seeds have different initial states, identical fractional outputs for n >= 1')
    print(f'OBSERVER: point probe fails congruence; action-closed probe set has {observer_congruence_control()} states')

    maps,ids,morphisms,types=finite_karoubi_proxy(3)
    print(f'KAROUBI FINITE PROXY: {maps} base maps, {ids} idempotent objects, '
          f'{morphisms} typed morphisms across {types} homsets')
    print(f'HAAR SPLIT: T_* C=id and Q²=Q on {haar_split_control()} exact atomic laws; Q(delta_0) is non-Haar')
    print('C-MONOID: NOT implemented; no claim of exponentials/CCC for these finite or affine proxies')

if __name__ == '__main__':
    run()

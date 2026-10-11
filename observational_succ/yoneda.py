"""Finite Yoneda laboratory: paths, probes, source-derived bridges.

This is classical finite category theory implemented as a bounded research
instrument. Full Yoneda is faithful; a restricted observer need not be.
No zeta zeros, global arithmetic positivity, or Gamma operators are involved.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import prod

from .core import BudgetExceeded, DomainError
from .arithmetic import factorization


@dataclass(frozen=True)
class Arrow:
    source: object
    target: object
    word: tuple[int, ...] = ()


def _bounded_objects(objects, limit=128):
    result = tuple(dict.fromkeys(objects))
    if not result or len(result) > limit or len(result) != len(tuple(objects)):
        raise DomainError("Category needs 1..128 distinct objects")
    return result


class DivisibilityCategory:
    """Thin category: a -> b iff a divides b, one morphism per pair, WITHOUT exposing the codomain ratio."""
    def __init__(self, objects):
        self.objects = _bounded_objects(tuple(objects))
        if any(type(n) is not int or not 1 <= n <= 1_000_000 for n in self.objects):
            raise DomainError("Divisibility objects must be bounded positive integers")

    def identity(self, obj):
        self._check(obj)
        return Arrow(obj, obj)

    def _check(self, obj):
        if obj not in self.objects:
            raise DomainError("Object is not in this category")

    def hom(self, a, b):
        self._check(a)
        self._check(b)
        if b % a:
            return ()
        return (Arrow(a, b, ()),)  # thin hom is a singleton; ratio is not a permitted local reading

    def compose(self, left, right):
        if right.target != left.source or right not in self.hom(right.source, right.target) or left not in self.hom(left.source, left.target):
            raise DomainError("Composition is undefined")
        return self.hom(right.source, left.target)[0]


class PathCategory:
    """Free finite path category for multiplication by encountered factors.

    The endpoints may be unrealized shadow targets. Intermediate arithmetic
    labels must be objects. Histories with equal endpoints remain distinct.
    """
    def __init__(self, objects, factors, *, max_paths=10000, max_depth=16):
        self.objects = _bounded_objects(tuple(objects))
        if any(type(n) is not int or not 1 <= n <= 1_000_000 for n in self.objects):
            raise DomainError("Path objects must be bounded positive integers")
        self.factors = tuple(sorted(set(factors)))
        if not self.factors or any(type(p) is not int or p < 2 or p > 1_000_000 for p in self.factors):
            raise DomainError("A path needs encountered integer multipliers >=2")
        if type(max_paths) is not int or not 1 <= max_paths <= 100000:
            raise BudgetExceeded("Bad path budget")
        if type(max_depth) is not int or not 1 <= max_depth <= 32:
            raise BudgetExceeded("Bad depth budget")
        self.max_paths, self.max_depth = max_paths, max_depth
        self._cache = {}

    def _check(self, obj):
        if obj not in self.objects:
            raise DomainError("Object is not in this category")

    def identity(self, obj):
        self._check(obj)
        return Arrow(obj, obj)

    def hom(self, a, b):
        self._check(a)
        self._check(b)
        if b % a:
            return ()
        key = (a, b)
        if key in self._cache:
            return self._cache[key]
        paths = []
        objects = set(self.objects)

        def rec(at, word):
            if at == b:
                paths.append(Arrow(a, b, word))
                if len(paths) > self.max_paths:
                    raise BudgetExceeded("Path hom-set expansion exceeded")
                return
            if len(word) >= self.max_depth:
                # A path exceeding max_depth might still reach b:
                if any(at * p <= b and b % (at * p) == 0 and at * p in objects for p in self.factors):
                    raise BudgetExceeded("Path depth truncation cannot be treated as no paths")
                return
            for p in self.factors:
                target = at * p
                if target <= b and b % target == 0 and target in objects:
                    rec(target, word + (p,))

        rec(a, ())
        self._cache[key] = tuple(paths)
        return self._cache[key]

    def compose(self, left, right):
        if right.target != left.source:
            raise DomainError("Noncomposable arrows")
        if right not in self.hom(right.source, right.target) or left not in self.hom(left.source, left.target):
            raise DomainError("Arrow does not belong to the declared path category")
        composed = Arrow(right.source, left.target, right.word + left.word)
        if composed not in self.hom(composed.source, composed.target):
            raise DomainError("Composite path was not retained")
        return composed


def valuation(n):
    """Exact additive *formal* log-coordinate, not a floating log(n)."""
    return tuple(factorization(n))


def _exp_table(val):
    return dict(val)


class ValuationCategory:
    """Source-derived image of divisibility in formal prime-log coordinates."""
    def __init__(self, integers):
        ints = _bounded_objects(tuple(integers))
        self.by_integer = {n: valuation(n) for n in ints}
        if len(set(self.by_integer.values())) != len(ints):
            raise DomainError("Valuation encoding lost a distinct integer")
        self.objects = tuple(self.by_integer.values())

    def _check(self, obj):
        if obj not in self.objects:
            raise DomainError("Unknown formal log-coordinate")

    def identity(self, obj):
        self._check(obj)
        return Arrow(obj, obj)

    def hom(self, a, b):
        self._check(a)
        self._check(b)
        aa, bb = _exp_table(a), _exp_table(b)
        if any(k > bb.get(p, 0) for p, k in aa.items()):
            return ()
        differences = tuple(p for p, k in b for _ in range(k - aa.get(p, 0)))
        return (Arrow(a, b, differences),)

    def compose(self, left, right):
        if right.target != left.source or right not in self.hom(right.source, right.target) or left not in self.hom(left.source, left.target):
            raise DomainError("Noncomposable graded arrows")
        return self.hom(right.source, left.target)[0]

    def grade(self, arrow):
        if arrow not in self.hom(arrow.source, arrow.target):
            raise DomainError("Arrow is not a formal logarithmic degree")
        return tuple(sorted(arrow.word))


class FiniteFunctor:
    """A checked functor; images are declarations, not inferred isomorphisms."""
    def __init__(self, source, target, object_image, arrow_image):
        self.source, self.target = source, target
        self.object_image, self.arrow_image = object_image, arrow_image

    def verify(self, *, max_compositions=300000):
        for x in self.source.objects:
            if self.object_image(x) not in self.target.objects:
                raise DomainError("Mapped object absent")
            if self.arrow_image(self.source.identity(x)) != self.target.identity(self.object_image(x)):
                raise DomainError("Identity not preserved")
        arrows = []
        for x in self.source.objects:
            for y in self.source.objects:
                for f in self.source.hom(x, y):
                    image = self.arrow_image(f)
                    if image not in self.target.hom(self.object_image(x), self.object_image(y)):
                        raise DomainError("Functor does not preserve arrow typing")
                    arrows.append(f)
        checked = 0
        for f in arrows:
            for g in arrows:
                if f.target != g.source:
                    continue
                checked += 1
                if checked > max_compositions:
                    raise BudgetExceeded("Functor composition verification budget reached")
                if self.arrow_image(self.source.compose(g, f)) != self.target.compose(self.arrow_image(g), self.arrow_image(f)):
                    raise DomainError("Functor does not preserve composition")
        return {"objects": len(self.source.objects), "arrows": len(arrows),
                "composable_pairs_checked": checked, "status": "verified_finite"}

    def hom_faithfulness(self):
        violations = []
        for x in self.source.objects:
            for y in self.source.objects:
                a = self.source.hom(x, y)
                b = self.target.hom(self.object_image(x), self.object_image(y))
                im = tuple(self.arrow_image(f) for f in a)
                if len(set(im)) != len(im):
                    violations.append(("nonfaithful", x, y))
                if set(im) != set(b):
                    violations.append(("not_full", x, y))
        return {"full": not any(z[0] == "not_full" for z in violations),
                "faithful": not any(z[0] == "nonfaithful" for z in violations),
                "violations": tuple(violations)}


def valuation_bridge(source: DivisibilityCategory):
    target = ValuationCategory(source.objects)
    return FiniteFunctor(source, target,
                         lambda n: target.by_integer[n],
                         lambda f: target.hom(target.by_integer[f.source], target.by_integer[f.target])[0])


def forget_path_bridge(source: PathCategory):
    target = DivisibilityCategory(source.objects)
    return FiniteFunctor(source, target, lambda n: n,
                         lambda f: target.hom(f.source, f.target)[0])


def restricted_yoneda(category, target, probe_objects):
    """Presheaf hom-sets restricted to a declared full observer subcategory.

    The returned *profile* contains no target label. For non-thin categories,
    one must also inspect precomposition actions for full presheaf equality.
    """
    probes = tuple(probe_objects)
    if len(set(probes)) != len(probes):
        raise DomainError("Duplicate probe contexts")
    return tuple(tuple(f.word for f in category.hom(p, target)) for p in probes)


def representable_natural_transform(category, arrow, probe_objects):
    """Yoneda sends arrow a->b to f |-> arrow∘f at every context."""
    if arrow not in category.hom(arrow.source, arrow.target):
        raise DomainError("Not a morphism of this category")
    result = {}
    for x in probe_objects:
        result[x] = {f: category.compose(arrow, f) for f in category.hom(x, arrow.source)}
    return result


def enumerate_natural_transforms(category, a, b, probes, *, max_candidates=100000):
    """Literal Nat(y_J a,y_J b), including spurious restricted observers.

    Finite brute-force enumerator; raises rather than silently clip. It verifies
    the naturality square for every arrow between declared observer contexts.
    """
    probes = tuple(probes)
    if not probes or len(probes) != len(set(probes)):
        raise DomainError("Observer context category must be nonempty and distinct")
    components = []
    total = 1
    for x in probes:
        domain, codomain = category.hom(x, a), category.hom(x, b)
        n = len(codomain) ** len(domain)
        total *= n
        if total > max_candidates:
            raise BudgetExceeded("Naturality enumeration budget exceeded")
        if domain and not codomain:
            return []
        options = [{domain[i]: codomain[choices[i]] for i in range(len(domain))}
                   for choices in product(range(len(codomain)), repeat=len(domain))]
        components.append(options)
    transformations = []
    for selected in product(*components):
        eta = dict(zip(probes, selected))
        natural = True
        for x in probes:
            for y in probes:
                for h in category.hom(x, y):
                    for f in category.hom(y, a):
                        if eta[x][category.compose(f, h)] != category.compose(eta[y][f], h):
                            natural = False
                            break
                    if not natural: break
                if not natural: break
            if not natural: break
        if natural:
            transformations.append(eta)
    return transformations


def validate_yoneda(category, a, b, probes=None):
    probes = tuple(category.objects if probes is None else probes)
    hom = category.hom(a, b)
    nat = enumerate_natural_transforms(category, a, b, probes)
    represented = [representable_natural_transform(category, f, probes) for f in hom]
    # For full Yoneda this must hold. For restricted observer failure is data.
    assert all(e in nat for e in represented)
    return {"source_hom_count": len(hom), "natural_transform_count": len(nat),
            "represented_count": len(represented), "surjective": all(e in represented for e in nat),
            "probe_count": len(probes)}


class CompanionBridge:
    """Finite companion profunctor B(c,d)=Hom_D(F(c),d), from an actual functor.

    Merely satisfying these axioms is not RH positivity. When F is nonfaithful,
    the bridge faithfully records the LOSS of path information.
    """
    def __init__(self, functor):
        self.functor = functor
        self.functor.verify()

    def fiber(self, c, d):
        F = self.functor
        return F.target.hom(F.object_image(c), d)

    def left_action(self, source_arrow, member):
        F = self.functor
        if member.source != F.object_image(source_arrow.target) or member not in F.target.hom(member.source, member.target):
            raise DomainError("Wrong left profunctor fiber")
        return F.target.compose(member, F.arrow_image(source_arrow))

    def right_action(self, target_arrow, member):
        F = self.functor
        if member.target != target_arrow.source or member not in F.target.hom(member.source, member.target):
            raise DomainError("Wrong right profunctor fiber")
        return F.target.compose(target_arrow, member)

    def verify_interchange(self, source_arrow, member, target_arrow):
        a = self.right_action(target_arrow, self.left_action(source_arrow, member))
        b = self.left_action(source_arrow, self.right_action(target_arrow, member))
        if a != b:
            raise DomainError("The source/target bridge actions fail to commute")
        return True



def co_yoneda_companion(bridge: CompanionBridge, a, d, *, max_pairs=30000,
                       max_relations=150000):
    """Construct the finite coend Hom_C(a,-) tensor_C B(-,d).

    Quotient pairs (f:a->c, h:F(c)->d) by
      (k∘f, h) ~ (f, h∘F(k)).
    The induced map [f,h] -> h∘F(f) must be a bijection onto B(a,d).
    This is a constructive finite co-Yoneda calculation, not an RH trace.
    """
    F=bridge.functor
    C,D=F.source,F.target
    if a not in C.objects or d not in D.objects:
        raise DomainError("co-Yoneda target is outside the declared categories")
    pairs=[]
    for c in C.objects:
        for f in C.hom(a,c):
            for h in bridge.fiber(c,d):
                pairs.append((c,f,h))
                if len(pairs)>max_pairs:
                    raise BudgetExceeded("co-Yoneda witness budget exceeded")
    ids={pair:i for i,pair in enumerate(pairs)}
    parent=list(range(len(pairs)))

    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i

    def union(i,j):
        p,q=find(i),find(j)
        if p!=q:parent[p]=q

    relations=0
    for c in C.objects:
        for c2 in C.objects:
            for k in C.hom(c,c2):
                for f in C.hom(a,c):
                    for h in bridge.fiber(c2,d):
                        relations+=1
                        if relations>max_relations:
                            raise BudgetExceeded("co-Yoneda relation budget exceeded")
                        right=(c2,C.compose(k,f),h)
                        left=(c,f,bridge.left_action(k,h))
                        if right not in ids or left not in ids:
                            raise DomainError("co-Yoneda relation has missing typed witness")
                        union(ids[right],ids[left])

    classes={}
    for i,pair in enumerate(pairs):
        mapped=bridge.left_action(pair[1],pair[2])
        root=find(i)
        classes.setdefault(root,set()).add(mapped)
    if any(len(image)!=1 for image in classes.values()):
        raise DomainError("Bridge quotient identified distinct target observations")
    image=set(next(iter(values)) for values in classes.values())
    expected=set(bridge.fiber(a,d))
    if image != expected or len(classes)!=len(expected):
        raise DomainError("Co-Yoneda transport failed to reconstruct the target fiber")
    return {"status":"verified_finite_co_yoneda", "raw_witness_pairs":len(pairs),
            "coend_relations":relations, "equivalence_classes":len(classes),
            "target_hom_count":len(expected),
            "forgotten_history_classes":len(pairs)-len(classes),
            "warning":"An automatically coherent companion profunctor is not a source-derived Weil polarization"}


def verify_companion_actions(bridge: CompanionBridge, *, max_checks=250000):
    """Exhaustively check identities, contravariance, covariance, interchange.

    These equations are automatic for an honest functor. Their purpose here
    is to catch a fabricated or mistyped bridge implementation.
    """
    F=bridge.functor
    C,D=F.source,F.target
    ops=0
    for c in C.objects:
        for d in D.objects:
            for h in bridge.fiber(c,d):
                if bridge.left_action(C.identity(c),h)!=h:
                    raise DomainError("Companion fails source identity")
                if bridge.right_action(D.identity(d),h)!=h:
                    raise DomainError("Companion fails target identity")
                for x in C.objects:
                    for f in C.hom(x,c):
                        for e in D.objects:
                            for g in D.hom(d,e):
                                ops+=1
                                if ops>max_checks:
                                    raise BudgetExceeded("Companion action audit budget exceeded")
                                bridge.verify_interchange(f,h,g)
                                for y in C.objects:
                                    for f2 in C.hom(y,x):
                                        if bridge.left_action(C.compose(f,f2),h) != bridge.left_action(f2,bridge.left_action(f,h)):
                                            raise DomainError("Companion source composition failed")
                                for z in D.objects:
                                    for g2 in D.hom(e,z):
                                        if bridge.right_action(D.compose(g2,g),h) != bridge.right_action(g2,bridge.right_action(g,h)):
                                            raise DomainError("Companion target composition failed")
    return {"status":"verified_finite_companion_actions","interchange_checks":ops}

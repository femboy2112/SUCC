"""Wild-embedding observer obstructions: exact finite models, not a horned sphere.

Two independent layers:
 (1) intrinsic combinatorial S² is blind to an embedding's exterior;
 (2) truncated Magnus reports miss deep nonabelian free-group words.

The ACTUAL Alexander horned sphere's nontrivial exterior pi1 is an external
1924 theorem; H1=0 follows by classical Alexander duality. It is NOT
modeled as a finite free group, an S3 quotient, or a realized 3D mesh.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import factorial


class WildObserverError(ValueError):
    pass


def _integer(value, low=0, high=12):
    if type(value) is not int or not low <= value <= high:
        raise WildObserverError("exact integer within finite research budget required")
    return value


def inverse_word(word):
    return tuple(-v for v in reversed(tuple(word)))


def reduce_word(word):
    """Free reduction in F<a,b>, tokens a=1, b=2, inverses negative."""
    stack = []
    for v in word:
        if type(v) is not int or v not in (-2, -1, 1, 2):
            raise WildObserverError("free-group generators are +/-1, +/-2")
        if stack and stack[-1] == -v:
            stack.pop()
        else:
            stack.append(v)
    return tuple(stack)


def commutator(x, y):
    x, y = reduce_word(x), reduce_word(y)
    return reduce_word(x + y + inverse_word(x) + inverse_word(y))


def nested_commutator(depth):
    """w_0=b, w_(k+1)=[a,w_k]. No 3D embedding is asserted."""
    _integer(depth, 0, 8)
    w = (2,)
    for _ in range(depth):
        w = commutator((1,), w)
    return w


def abelianization(word):
    w = reduce_word(word)
    return tuple(sum((1 if t == j else -1 if t == -j else 0) for t in w)
                 for j in (1, 2))


def _padd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
        if not out[k]:
            del out[k]
    return out


def _pmul(a, b, depth):
    out = {}
    for x, c in a.items():
        for y, d in b.items():
            if len(x) + len(y) <= depth:
                z = x + y
                out[z] = out.get(z, 0) + c*d
    return {k:v for k,v in out.items() if v}


def magnus_expansion(word, degree):
    """Noncommutative truncated Magnus shadow into Z<X,Y>/(degree>k).

    a -> 1+X; b -> 1+Y; inverse -> geometric alternating series.
    A nontrivial coefficient PROVES a word is nonidentity, because the
    identity maps to 1. Converse not assumed at any fixed degree.
    """
    _integer(degree, 0, 9)
    current = {(): 1}
    for token in reduce_word(word):
        letter = 0 if abs(token) == 1 else 1
        if token > 0:
            factor = {(): 1}
            if degree:
                factor[(letter,)] = 1
        else:
            factor = {tuple([letter]*k): (-1)**k for k in range(degree+1)}
        current = _pmul(current, factor, degree)
    return current


def magnus_report(word, degree):
    """Exact finite probe, ordered independent of dict iteration."""
    m = magnus_expansion(word, degree)
    return tuple(sorted((k,v) for k,v in m.items() if k and v))


def first_visible_order(word, max_degree=9):
    _integer(max_degree, 1, 9)
    for d in range(1, max_degree+1):
        if magnus_report(word,d):
            return d
    return None


def deep_commutator_receipt(level):
    _integer(level, 1, 7)
    w = nested_commutator(level)
    low = magnus_report(w,level)
    hi = magnus_report(w,level+1)
    leading = tuple([0]*level+[1])
    return {
        "level":level,
        "word_length":len(w),
        "abelianization":abelianization(w),
        "up_to_level":low,
        "first_visible_degree":first_visible_order(w,level+1),
        "leading_X_power_Y_coefficient":
            dict(hi).get(leading,0),
        "proven_nonidentity_in_free_toy":bool(hi),
        "proven_actual_alexander_exterior_representation":False,
    }


def _rank_q(rows):
    """Exact rational matrix rank, including empty/zero matrices."""
    if not rows:
        return 0
    A = [[Fraction(v) for v in r] for r in rows]
    n=len(A[0])
    if any(len(r)!=n for r in A):
        raise WildObserverError("ragged boundary matrix")
    pivot=0
    for col in range(n):
        r=next((k for k in range(pivot,len(A)) if A[k][col]),None)
        if r is None: continue
        A[pivot],A[r]=A[r],A[pivot]
        factor=A[pivot][col]
        A[pivot]=[v/factor for v in A[pivot]]
        for row in range(pivot+1,len(A)):
            fac=A[row][col]
            if fac:
                A[row]=[x-fac*y for x,y in zip(A[row],A[pivot])]
        pivot+=1
        if pivot==len(A):
            break
    return pivot


def intrinsic_double_cone():
    """Pure abstract triangulated sphere: NOT an ambient 3D embedding."""
    vertices=("N","S","E0","E1","E2","E3")
    faces=tuple(
        (apex,f"E{j}",f"E{(j+1)%4}") if apex=="N" else
        (apex,f"E{(j+1)%4}",f"E{j}")
        for apex in ("N","S") for j in range(4))
    edges=tuple(sorted({tuple(sorted((u,v))) for face in faces
                        for u,v in ((face[0],face[1]),(face[1],face[2]),
                                    (face[2],face[0]))}))
    boundary1=[[0]*len(edges) for _ in vertices]
    boundary2=[[0]*len(faces) for _ in edges]
    for j,(u,v) in enumerate(edges):
        boundary1[vertices.index(u)][j]=-1
        boundary1[vertices.index(v)][j]=1
    for j,(a,b,c) in enumerate(faces):
        for u,v in ((b,c),(a,c),(a,b)):
            sign=-1 if (u,v)==(a,c) else 1
            edge=tuple(sorted((u,v)))
            orient=1 if (u,v)==edge else -1
            boundary2[edges.index(edge)][j]+=sign*orient
    for v in range(len(vertices)):
        for face in range(len(faces)):
            assert sum(boundary1[v][e]*boundary2[e][face]
                       for e in range(len(edges))) == 0
    rank1=_rank_q(boundary1)
    rank2=_rank_q(boundary2)
    return {
        "vertices":len(vertices), "edges":len(edges), "faces":len(faces),
        "Euler":len(vertices)-len(edges)+len(faces),
        "Betti_Q":(len(vertices)-rank1,
                   len(edges)-rank1-rank2,
                   len(faces)-rank2),
        "ambient_embedding_certified":False,
        "exterior_pi1_computed":False,
    }


def compose(p,q):
    if len(p)!=len(q) or sorted(p)!=list(range(len(p))) or sorted(q)!=list(range(len(q))):
        raise WildObserverError("same-degree exact permutations required")
    return tuple(p[q[i]] for i in range(len(p)))


def inverse_perm(p):
    out=[0]*len(p)
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)


def perm_commutator(p,q):
    return compose(compose(compose(p,q),inverse_perm(p)),inverse_perm(q))


def sign_perm(p):
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return (-1)**inversions


def permutation_commutator_spectrum(n, even_only=False):
    """Small finite groups: A5 is perfect, S3 is not.

    This is NOT a homomorphism out of the horned-sphere exterior group.
    """
    _integer(n, 2, 5)
    G=tuple(p for p in permutations(range(n)) if not even_only or sign_perm(p)==1)
    image={perm_commutator(p,q) for p in G for q in G}
    return {
        "group_order":len(G),
        "distinct_commutators":len(image),
        "every_element_is_a_commutator":len(image)==len(G),
        "identity":tuple(range(n)),
    }


def predicted_magnus_lie_polynomial(level):
    """Independent binomial expansion of ad_X^level(Y), integer coefficients."""
    from math import comb
    _integer(level,1,7)
    return {tuple([0]*(level-j)+[1]+[0]*j):(-1)**j*comb(level,j)
            for j in range(level+1)}


def verify_full_magnus_leading_form(level):
    """Check EVERY coefficient in the first observable nonabelian layer."""
    _integer(level,1,7)
    w=nested_commutator(level)
    polynomial=magnus_expansion(w,level+1)
    homogeneous={mon:c for mon,c in polynomial.items()
                 if len(mon)==level+1 and c}
    expected=predicted_magnus_lie_polynomial(level)
    return {
        "level":level,
        "no_lower_order_signal":all(not c or len(mon)>level
                                    for mon,c in polynomial.items() if mon),
        "full_free_lie_layer_matches":homogeneous==expected,
        "nonzero_terms":len(homogeneous),
        "not_an_alexander_sphere_group_presentation":True,
    }

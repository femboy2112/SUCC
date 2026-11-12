"""Boundary-first finite linear dynamics tomography (exact Q arithmetic).

Finite Hankel realization / observability / boundary filter bank. No theorem
about arbitrary nonlinear carrier, RH, pi normality, or physical holography.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product


def q(x):
    if type(x) not in (int, F):
        raise TypeError("only exact integer/Fraction values")
    return F(x)


def mat(a):
    if not a or not a[0] or any(len(row) != len(a[0]) for row in a):
        raise ValueError("nonempty rectangular matrix required")
    return tuple(tuple(q(x) for x in row) for row in a)


def mul(a, b):
    a, b = mat(a), mat(b)
    if len(a[0]) != len(b):
        raise ValueError("incompatible dimensions")
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def rank(a):
    a = [list(row) for row in mat(a)]
    rows, cols = len(a), len(a[0])
    r = 0
    for j in range(cols):
        p = next((i for i in range(r, rows) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        x = a[r][j]
        a[r] = [v/x for v in a[r]]
        for i in range(rows):
            if i != r:
                z = a[i][j]
                a[i] = [a[i][k]-z*a[r][k] for k in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def model(a, b, c):
    a, b, c = mat(a), mat(b), mat(c)
    n = len(a)
    if len(a[0]) != n or len(b) != n or len(b[0]) != 1 or len(c[0]) != n:
        raise ValueError("A square, b column, C with n columns")
    return a, b, c


def moments(a, b, c, count):
    a, b, c = model(a, b, c)
    if type(count) is not int or count < 1:
        raise ValueError("positive count")
    v = b
    out = []
    for _ in range(count):
        out.append(tuple(row[0] for row in mul(c, v)))
        v = mul(a, v)
    return tuple(out)


def hankel(a, b, c, depth):
    a, b, c = model(a, b, c)
    if type(depth) is not int or depth < 1:
        raise ValueError("positive depth")
    seq = moments(a, b, c, 2*depth-1)
    return tuple(tuple(seq[i+j][0] for j in range(depth)) for i in range(depth))


def observability(a, c):
    a, c = mat(a), mat(c)
    n = len(a)
    if len(a[0]) != n or len(c[0]) != n:
        raise ValueError("bad dimensions")
    current = c
    rows = []
    for _ in range(n):
        rows.extend(current)
        current = mul(current, a)
    return tuple(rows)


def reachability(a, b):
    a, b = mat(a), mat(b)
    n = len(a)
    if len(a[0]) != n or len(b) != n or len(b[0]) != 1:
        raise ValueError("bad dimensions")
    v = b
    cols = []
    for _ in range(n):
        cols.append(tuple(x[0] for x in v))
        v = mul(a, v)
    return tuple(tuple(cols[j][i] for j in range(n)) for i in range(n))


def filter_masks(n, filters):
    """Boundary diagonal masks f_h(j); filter row c_j*f_h(j)."""
    if type(n) is not int or n < 1:
        raise ValueError("positive channel count")
    if not filters or any(len(f) != n for f in filters):
        raise ValueError("complete filter rows")
    return mat(filters)


def filtered_outputs(a, b, c, filters, count):
    a, b, c = model(a, b, c)
    if len(c) != 1:
        raise ValueError("single boundary row")
    f = filter_masks(len(a), filters)
    bank = tuple(tuple(c[0][j]*row[j] for j in range(len(a))) for row in f)
    return moments(a, b, bank, count)


def reconstruct_state_from_filters(c, filters, outputs):
    """Unique state only if filtered boundary rows have full column rank.

    Overdetermined exact solver with rank check and consistency.
    """
    c = mat(c)
    if len(c) != 1:
        raise ValueError("single boundary row")
    n = len(c[0])
    f = filter_masks(n, filters)
    if len(outputs) != len(f):
        raise ValueError("filter/output count mismatch")
    rows = [[c[0][j]*f[i][j] for j in range(n)] + [q(outputs[i])]
            for i in range(len(f))]
    if rank([row[:n] for row in rows]) != n:
        raise ValueError("boundary filters do not separate all states")
    if rank(rows) != n:
        raise ValueError("inconsistent boundary readings")
    aug = [row[:] for row in rows]
    pivots = []
    r = 0
    for j in range(n):
        p = next((i for i in range(r,len(aug)) if aug[i][j]),None)
        if p is None:
            continue
        aug[r],aug[p] = aug[p],aug[r]
        d=aug[r][j]
        aug[r]=[x/d for x in aug[r]]
        for i in range(len(aug)):
            if i!=r:
                v=aug[i][j]
                aug[i]=[aug[i][k]-v*aug[r][k] for k in range(n+1)]
        pivots.append(j)
        r+=1
    result=[F()]*n
    for i,j in enumerate(pivots):
        result[j]=aug[i][-1]
    return tuple(result)


def identity_filters(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive dimension")
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))


def signed_future_filter(digits, base, depth, h):
    """Exact formal Z[Z/base] signed conditional first-digit filter.

    Return future-word -> exponent-residue -> integer coefficient; NO complex
    numerical phase evaluation and NO assumption of equidistribution.
    """
    if type(base) is not int or base < 2 or type(depth) is not int or depth < 0:
        raise ValueError("valid base/depth")
    if type(h) is not int or h % base == 0:
        raise ValueError("nontrivial integer character")
    digits=tuple(digits)
    if len(digits)<depth+1 or any(type(x) is not int or not 0<=x<base for x in digits):
        raise ValueError("finite base digits")
    out={}
    for i in range(len(digits)-depth):
        future=digits[i+1:i+depth+1]
        if depth==0:
            future=()
        e=(h*digits[i])%base
        bucket=out.setdefault(future,{})
        bucket[e]=bucket.get(e,0)+1
    return out


def conditional_defect_numerator(digits, base, depth):
    """Exact sum over a,w of |base*N_(a,w)-N_w|, denominator base*N.

    N is number of noncyclic windows; not a normality proof.
    """
    if type(base) is not int or base<2 or type(depth) is not int or depth<0:
        raise ValueError("invalid base/depth")
    digits=tuple(digits)
    if len(digits)<depth+1 or any(type(x) is not int or not 0<=x<base for x in digits):
        raise ValueError("finite base digits")
    counts={}
    for i in range(len(digits)-depth):
        w=digits[i+1:i+depth+1]
        counts[(digits[i],w)]=counts.get((digits[i],w),0)+1
    futures={w for a,w in counts}
    return sum(abs(base*counts.get((a,w),0)-sum(counts.get((k,w),0) for k in range(base)))
               for w in futures for a in range(base))


def bbp_forcing(n):
    if type(n) is not int or n<1:
        raise ValueError("n>=1")
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def bbp_prefix(count, seed=0):
    """Original unwrapped four-pole BBP recurrence and explicit seed."""
    if type(count) is not int or count<0:
        raise ValueError("count>=0")
    x=q(seed)
    out=[x]
    for n in range(1,count+1):
        x=16*x+bbp_forcing(n)
        out.append(x)
    return tuple(out)


def source_pin(values, seed):
    """Exact source-correct recurrence + initial seed check."""
    values=tuple(q(x) for x in values)
    if not values:
        raise ValueError("nonempty history")
    return values[0]==q(seed) and all(
        values[n]==16*values[n-1]+bbp_forcing(n)
        for n in range(1,len(values)))


def radial_response(a,b,c,depth):
    """Emit boundary time jets with explicit depth and full-rank diagnosis."""
    a,b,c=model(a,b,c)
    return {"jets":moments(a,b,c,depth),
            "hankel_rank":rank(hankel(a,b,c,depth)),
            "reachable_rank":rank(reachability(a,b)),
            "observable_rank":rank(observability(a,c)),
            "ambient_dimension":len(a)}

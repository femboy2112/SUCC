"""Exact original-source collision instruments. No pi digits or float gates.

The annulus and dilated-window theorems have limited coverage; see PROOFS.md.
The source-asymptotic normality premise is not an implemented assumption.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import lcm


def source(n):
    if n < 1:
        raise ValueError('positive source time required')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def full_source(last):
    """Stream n, residue, full pole modulus, literal carry; starts at U0=0.

    O(size of modulus) working memory. All four signed injections remain.
    The modulus depends on last, but the represented rational states do not.
    """
    if last < 0:
        raise ValueError('nonnegative last time required')
    den = 1
    for n in range(1, last+1):
        den = lcm(den, 8*n-7, 8*n-4, 8*n-3, 8*n-2)
    a = 0
    yield 0, a, den, 0
    for n in range(1, last+1):
        injection = (4*(den//(8*n-7))-2*(den//(8*n-4))
                     -den//(8*n-3)-den//(8*n-2))
        carry, a = divmod(16*a+injection, den)
        yield n, a, den, carry


def phases(last):
    if last < 0:
        raise ValueError('nonnegative last time required')
    out, x = [], F(0)
    for n in range(1, last+1):
        x = (16*x+source(n)) % 1
        out.append(x)
    return out


def digest_integer(x):
    if x < 0:
        raise ValueError('unsigned integer required')
    return sha256(x.to_bytes(max(1, (x.bit_length()+7)//8), 'big')).hexdigest()


def slow_mesh(A):
    if A < 2 or A & (A-1):
        raise ValueError('dyadic A >= 2 required')
    j = A.bit_length()-1
    return max(2, 1 << (j.bit_length()-1))


def packet_depth(mesh, divisor):
    """Largest k>=0 with divisor*16**k <= mesh, or -1 if none."""
    if mesh < 1 or divisor < 1:
        raise ValueError('positive inputs required')
    k, size = -1, divisor
    while size <= mesh:
        k += 1
        size *= 16
    return k


def shell_bound(A, mesh):
    if A < 64 or not 64 <= mesh <= A:
        raise ValueError('A>=64 and 64<=mesh<=A required')
    K = packet_depth(mesh, 4)
    a, b = divmod(A-1, K+1)
    return (K+1)*a*(a+1)+2*(a+1)*b


def distance_numerator(a, den):
    a %= den
    return min(a, den-a)


def annulus_census(residues, den, A, mesh):
    """All pairs in one exact original epoch, with temporal exclusion budgets.

    Input is residues of times A,...,2A-1. This instrument checks the theorem
    on supplied data; it does not authenticate arbitrary lists as BBP states.
    """
    ceiling = shell_bound(A, mesh)
    if len(residues) != A or den < 1 or any(not 0 <= x < den for x in residues):
        raise ValueError('A residues in [0,den) required')
    K = packet_depth(mesh, 4)
    rows, near_total, inner_total, shell_total = [], A, A, 0
    violations = []
    for d in range(1, A):
        near, inner, hits, excluded = 0, 0, [], set()
        for i in range(A-d):
            v = distance_numerator(residues[i+d]-residues[i], den)
            if mesh*v <= den:
                near += 1
                if 8*mesh*v < den:
                    inner += 1
                else:
                    hits.append(i)
                    for q in range(1, min(K, A-d-1-i)+1):
                        j = i+q
                        vq = distance_numerator(residues[j+d]-residues[j], den)
                        if mesh*vq <= den:
                            violations.append([d, i, q])
                        excluded.add(j)
        assert near == inner+len(hits)
        rows.append({'lag':d, 'near':near, 'strict_inner':inner,
                     'shell':len(hits), 'excluded_starts':len(excluded),
                     'shell_ceiling':(A-d+K)//(K+1),
                     'near_ceiling':A-d-len(excluded)})
        near_total += 2*near
        inner_total += 2*inner
        shell_total += 2*len(hits)
    return {'A':A, 'mesh':mesh, 'K':K, 'ordered_near':near_total,
            'ordered_strict_inner':inner_total, 'ordered_shell':shell_total,
            'ordered_shell_ceiling':ceiling, 'violations':violations, 'lags':rows}


def exact_pair_oracle(points, mesh):
    """Independent quadratic Fraction oracle, including both threshold ends."""
    near = inner = shell = 0
    for x in points:
        for y in points:
            v = abs(x-y) % 1
            v = min(v, 1-v)
            if v <= F(1, mesh):
                near += 1
                if v < F(1, 8*mesh):
                    inner += 1
                else:
                    shell += 1
    return near, inner, shell


def mirror_cylinder(index, depth):
    """J([a/B,(a+1)/B)) = ((j-1)/B,j/B] modulo 1, B=16**depth.

    Returns integer endpoint numerators j-1,j (not reduced) over B. Reversed
    endpoint ownership matters; callers must interpret the interval on circle.
    """
    if depth < 1 or not 0 <= index < 16**depth:
        raise ValueError('valid base-16 cylinder required')
    B = 16**depth
    j = B//16-index
    return j-1, j, B


def literal_carry_relation(x, n, depth):
    """Exact cylinder transition with forcing and endpoints, x in [0,1)."""
    if depth < 1 or not 0 <= x < 1:
        raise ValueError('depth>=1 and x in [0,1) required')
    B = 16**depth
    a = (B*x).__floor__()
    u = B*x-a
    injection_carry = (16*u+B*source(n+1)).__floor__()
    y = (16*x+source(n+1)) % 1
    b = (B*y).__floor__()
    assert b == (16*a+injection_carry) % B
    return a, injection_carry, b


def iid_ceiling(counts):
    N, m = sum(counts), len(counts)
    if N < 1 or m < 2:
        raise ValueError('nonempty sample and >=2 cells required')
    E = F(m*sum(x*x for x in counts), N*N)
    return E, 1+F(m-1, N)


def witness_packets(residues, den, A, mesh, h=1):
    """Finite ORIGINAL lag witnesses; no assumed Diophantine onset.

    residues[n-1] represents U_n. Certify source distances > 1/mesh for each
    member directly. Search itself uses distance>1/32 on original states,
    which is separate from the paper theorem's completed-orbit existence.
    """
    if A < 1 or h == 0 or len(residues) < 25*A:
        raise ValueError('h!=0 and source through 25A required')
    k = packet_depth(mesh, 64)
    if k < 0 or k > A:
        raise ValueError('mesh must allow a packet starting at or after A')
    rows = []
    for d in range(1, A+1):
        found = None
        for t in range(2*A, 24*A+1):
            v = distance_numerator(h*(residues[t+d-1]-residues[t-1]), den)
            if 32*v <= den:
                continue
            costs = [distance_numerator(h*(residues[t-j+d-1]-residues[t-j-1]), den)
                     for j in range(k+1)]
            if all(mesh*vj > den for vj in costs):
                found = {'lag':d, 'witness':t, 'packet_start':t-k,
                         'packet_size':k+1, 'minimum_scaled_distance':
                         [min(costs)*mesh//den, (min(costs)*mesh//den)+1]}
                break
        if found is None:
            raise AssertionError(f'finite witness search failed at lag {d}')
        rows.append(found)
    return {'A':A, 'mesh':mesh, 'h':h, 'depth':k,
            'ordered_exclusions':2*A*(k+1), 'witnesses':rows}

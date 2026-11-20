"""Exact finite observer-head pinbed, coding, and BBP source-family controls.

Research only. Instruments are declared calibrated algebraic maps; no physical GPS,
source interventions, or pi-normality theorem is asserted. Standard library only.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations

BETA = (7, 4, 3, 2)
ORIGINAL = (Q(0), Q(4), Q(-2), Q(-1), Q(-1))


def rational_matrix(rows):
    data = [tuple(Q(z) for z in row) for row in rows]
    if not data:
        return tuple()
    n = len(data[0])
    if any(len(row) != n for row in data):
        raise ValueError("ragged matrix")
    return tuple(data)


def rank(rows, columns=None):
    mat = [list(row) for row in rational_matrix(rows)]
    if not mat:
        return 0
    nc = len(mat[0])
    if columns is not None and nc != columns:
        raise ValueError("wrong number of columns")
    pivot_row = 0
    for j in range(nc):
        pivot = next((i for i in range(pivot_row, len(mat)) if mat[i][j]), None)
        if pivot is None:
            continue
        mat[pivot], mat[pivot_row] = mat[pivot_row], mat[pivot]
        inv = Q(1) / mat[pivot_row][j]
        mat[pivot_row] = [v * inv for v in mat[pivot_row]]
        for i in range(len(mat)):
            if i != pivot_row and mat[i][j]:
                coeff = mat[i][j]
                mat[i] = [a - coeff*b for a,b in zip(mat[i], mat[pivot_row])]
        pivot_row += 1
        if pivot_row == len(mat):
            break
    return pivot_row


def solve_unique(rows, outputs):
    """Unique exact affine linear solve Ax=y, with overdetermined consistency."""
    A = rational_matrix(rows)
    y = tuple(Q(t) for t in outputs)
    if not A or len(A) != len(y):
        raise ValueError("nonempty observations and matched outputs required")
    n = len(A[0])
    if len(A) < n:
        raise ValueError("too few observations")
    aug = [list(A[i]) + [y[i]] for i in range(len(A))]
    pivots = []
    pos = 0
    for j in range(n):
        pivot = next((i for i in range(pos, len(aug)) if aug[i][j]), None)
        if pivot is None:
            continue
        aug[pivot], aug[pos] = aug[pos], aug[pivot]
        inv = Q(1) / aug[pos][j]
        aug[pos] = [x * inv for x in aug[pos]]
        for i in range(len(aug)):
            if i != pos and aug[i][j]:
                factor = aug[i][j]
                aug[i] = [a-factor*b for a,b in zip(aug[i], aug[pos])]
        pivots.append(j)
        pos += 1
    if len(pivots) != n:
        raise ValueError("not identifiable: deficient rank")
    if any(not any(aug[i][:n]) and aug[i][n] for i in range(pos, len(aug))):
        raise ValueError("inconsistent readings")
    return tuple(aug[i][n] for i in range(n))


def matvec(matrix, vector):
    v = tuple(Q(t) for t in vector)
    A = rational_matrix(matrix)
    if any(len(row) != len(v) for row in A):
        raise ValueError("dimension mismatch")
    return tuple(sum((a*b for a,b in zip(row,v)), Q(0)) for row in A)


def determined_by(heads, target):
    """Exact target descent: ker(heads) subset ker(target)."""
    H = rational_matrix(heads)
    F = rational_matrix(target)
    if not H or not F or len(H[0]) != len(F[0]):
        raise ValueError("need compatible nonempty maps")
    return rank(H + F) == rank(H)


def full_spark(rows):
    """Every k-head square selection is invertible; strong uniform matroid."""
    H = rational_matrix(rows)
    if not H or len(H) < len(H[0]):
        return False
    k = len(H[0])
    return all(rank(tuple(H[i] for i in inds)) == k for inds in combinations(range(len(H)), k))


def target_distance(rows, target):
    """Minimum number of head reports affected by a change in target.

    Algebraic Hamming distance over the exact infinite field Q; no claim of
    stable noisy recovery from arbitrarily small real-valued differences.
    """
    H = rational_matrix(rows)
    F = rational_matrix(target)
    if not H or not F or len(H[0]) != len(F[0]):
        raise ValueError("nonempty compatible maps required")
    m = len(H)
    max_zero = -1
    for size in range(m+1):
        for idx in combinations(range(m), size):
            zero_rows = tuple(H[i] for i in idx)
            r0 = rank(zero_rows)
            if rank(zero_rows + F) > r0:
                max_zero = max(max_zero, size)
    return m - max_zero if max_zero >= 0 else m+1


def decode_corruptions(rows, outputs, allowed_errors):
    """Exhaustive exact decoding; supports <= allowed_errors entire head faults."""
    H = rational_matrix(rows)
    y = tuple(Q(z) for z in outputs)
    if len(H) != len(y) or not H:
        raise ValueError("bad observations")
    if type(allowed_errors) is not int or allowed_errors < 0:
        raise ValueError("invalid error budget")
    k = len(H[0])
    hits = set()
    for idx in combinations(range(len(H)), k):
        R = tuple(H[j] for j in idx)
        if rank(R) < k:
            continue
        theta = solve_unique(R, tuple(y[j] for j in idx))
        pred = matvec(H, theta)
        if sum(a!=b for a,b in zip(y, pred)) <= allowed_errors:
            hits.add(theta)
    if len(hits) != 1:
        raise ValueError("no unique source within corruption budget")
    return hits.pop()


def left_syndrome_basis(rows):
    """Basis of all row-combination checks lambda^T H=0 over Q."""
    H = rational_matrix(rows)
    if not H:
        raise ValueError("nonempty H required")
    m = len(H)
    n = len(H[0])
    mat = [[H[i][j] for i in range(m)] for j in range(n)]
    pivots = []
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r,n) if mat[i][col]),None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        factor = Q(1)/mat[r][col]
        mat[r] = [q*factor for q in mat[r]]
        for i in range(n):
            if i!=r and mat[i][col]:
                factor = mat[i][col]
                mat[i] = [a-factor*b for a,b in zip(mat[i],mat[r])]
        pivots.append(col)
        r+=1
        if r==n:
            break
    basis=[]
    for free in range(m):
        if free in pivots:
            continue
        vec=[Q(0)]*m
        vec[free]=Q(1)
        for i,piv in enumerate(pivots):
            vec[piv]=-mat[i][free]
        basis.append(tuple(vec))
    return tuple(basis)


def syndrome(rows, outputs):
    y=tuple(Q(v) for v in outputs)
    if len(rows)!=len(y):
        raise ValueError("mismatched outputs")
    return matvec(left_syndrome_basis(rows),y)


def gps2_matrix(directions):
    return rational_matrix((*u,1) for u in directions)


def gps3_matrix(directions):
    return rational_matrix((*u,1) for u in directions)


def bbp_row(n):
    """Exact unwrapped U_n row in (seed, c_7,c_4,c_3,c_2)."""
    if type(n) is not int or n<0:
        raise ValueError("n>=0")
    return (Q(16**n),) + tuple(sum((Q(16**(n-j),8*j-beta) for j in range(1,n+1)),Q(0)) for beta in BETA)


def bbp_state(n, parameters=ORIGINAL):
    return matvec([bbp_row(n)], parameters)[0]


def forcing(n):
    if type(n) is not int or n<1:
        raise ValueError("n>=1")
    return sum((c*Q(1,8*n-beta) for c,beta in zip(ORIGINAL[1:],BETA)),Q(0))


def bbp_prefix(M):
    if type(M) is not int or M<0:
        raise ValueError("M>=0")
    return sum((forcing(n)/16**n for n in range(1,M+1)),Q(0))


def bbp_terminal_tail(n,M):
    if type(n) is not int or type(M) is not int or not 0<=n<=M:
        raise ValueError("0<=n<=M")
    return sum((forcing(j)/16**(j-n) for j in range(n+1,M+1)),Q(0))


def circle_fraction(v):
    q=Q(v)
    return Q(q.numerator%q.denominator,q.denominator)


def xor_shared_head_records(a,b):
    """Two individually target-blind observations that jointly recover b."""
    if a not in (0,1) or b not in (0,1):
        raise ValueError("binary source")
    return (a,a^b)


def common_frame_gauge(edge_phases, vertex_phases, paths):
    """Return matching-root/target forward holonomies; arithmetic turns mod 1.

    edge_phases maps (u,v,label) -> phase in Q/Z, and paths are edge lists.
    """
    phases = {}
    for e,q in edge_phases.items():
        phases[e] = Q(q)+Q(vertex_phases[e[1]])-Q(vertex_phases[e[0]])
    path_vals=[]
    for path in paths:
        if not path or any(path[i][1]!=path[i+1][0] for i in range(len(path)-1)):
            raise ValueError("invalid directed path")
        path_vals.append(circle_fraction(sum((phases[e] for e in path),Q(0))))
    if len(set((path[0][0],path[-1][1]) for path in paths))!=1:
        raise ValueError("cannot compare different endpoints")
    return tuple(circle_fraction(v-path_vals[0]) for v in path_vals)

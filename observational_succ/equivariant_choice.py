"""Exact finite observer-relative choice and equivariant stochastic lifting.

A finite source/reported T-action is a pair of total deterministic maps per
label and a surjective, equivariant observation map. Section feasibility uses
Fraction arithmetic; finite stochastic feasibility is an exact rational LP
vertex enumeration, not a floating point heuristic. Capped to small carriers.

Scope: finite declared source tables; a kernel is a probability-valued lift,
not a physical prior and not an actual source-history identifier.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

Q = Fraction


@dataclass(frozen=True)
class FiniteActionQuotient:
    """Integer-labelled states/reports, with one or more lawful T generators."""

    q: tuple[int, ...]
    y_size: int
    source_actions: tuple[tuple[int, ...], ...]
    report_actions: tuple[tuple[int, ...], ...]

    def __post_init__(self):
        n = len(self.q)
        if (n < 1 or type(self.y_size) is not int or self.y_size < 1 or
                any(type(v) is not int for v in self.q) or
                set(self.q) != set(range(self.y_size))):
            raise ValueError("Nonempty X and surjective q:X -> Y required")
        if not self.source_actions or len(self.source_actions) != len(self.report_actions):
            raise ValueError("At least one paired source/report generator is required")
        for t, u in zip(self.source_actions, self.report_actions):
            if len(t) != n or len(u) != self.y_size:
                raise ValueError("Total action lengths must match X and Y")
            if any(type(v) is not int or v < 0 or v >= n for v in t):
                raise ValueError("Invalid source action")
            if any(type(v) is not int or v < 0 or v >= self.y_size for v in u):
                raise ValueError("Invalid report action")
            if any(self.q[t[x]] != u[self.q[x]] for x in range(n)):
                raise ValueError("The source/report action diagram must commute")

    @property
    def x_size(self):
        return len(self.q)

    @property
    def fibers(self) -> tuple[tuple[int, ...], ...]:
        return tuple(tuple(x for x, yy in enumerate(self.q) if yy == y)
                     for y in range(self.y_size))

    def is_group_generated(self):
        """A finite set of permutation generators generates a finite group."""
        return all(set(t) == set(range(self.x_size)) and
                   set(u) == set(range(self.y_size))
                   for t, u in zip(self.source_actions, self.report_actions))


def verify_point_section(m: FiniteActionQuotient, s: tuple[int, ...]) -> bool:
    return (len(s) == m.y_size and
            all(x in m.fibers[y] for y, x in enumerate(s)) and
            all(t[s[y]] == s[u[y]]
                for t, u in zip(m.source_actions, m.report_actions)
                for y in range(m.y_size)))


def point_section(m: FiniteActionQuotient):
    """Find an equivariant deterministic section or return None (exhaustive)."""
    for s in product(*m.fibers):
        if verify_point_section(m, s):
            return s
    return None


def uniform_fiber_kernel(m: FiniteActionQuotient):
    return tuple(tuple(Q(1, len(m.fibers[y])) if x in m.fibers[y] else Q(0)
                       for x in range(m.x_size)) for y in range(m.y_size))


def verify_kernel(m: FiniteActionQuotient, k: tuple[tuple[Q, ...], ...]) -> bool:
    """Verify normalization, fiber support, nonnegativity and every action law."""
    if len(k) != m.y_size or any(len(row) != m.x_size for row in k):
        return False
    if any(any(type(p) not in (int, Q) or p < 0 or
                   (m.q[x] != y and p != 0) for x, p in enumerate(row)) or
           sum(row, Q(0)) != 1 for y, row in enumerate(k)):
        return False
    for t, u in zip(m.source_actions, m.report_actions):
        for y in range(m.y_size):
            dist = [Q(0)] * m.x_size
            for x, mass in enumerate(k[y]):
                dist[t[x]] += mass
            if tuple(dist) != tuple(k[u[y]]):
                return False
    return True


def delta_section(m: FiniteActionQuotient, s: tuple[int, ...]):
    return tuple(tuple(Q(int(x == s[y])) for x in range(m.x_size))
                 for y in range(m.y_size))


def constraint_matrix(m: FiniteActionQuotient):
    """A p=b,p>=0; unknowns p(y,x) only when q(x)=y; all integer data."""
    cols = tuple((y, x) for y in range(m.y_size) for x in m.fibers[y])
    index = {v: i for i, v in enumerate(cols)}
    A, b, labels = [], [], []
    for y in range(m.y_size):
        row = [0] * len(cols)
        for x in m.fibers[y]:
            row[index[y, x]] = 1
        A.append(tuple(row)); b.append(1); labels.append(("normal", y))
    for gi, (t, u) in enumerate(zip(m.source_actions, m.report_actions)):
        for y in range(m.y_size):
            target_y = u[y]
            for dst in m.fibers[target_y]:
                row = [0] * len(cols)
                for src in m.fibers[y]:
                    if t[src] == dst:
                        row[index[y, src]] += 1
                row[index[target_y, dst]] -= 1
                A.append(tuple(row)); b.append(0)
                labels.append(("action", gi, y, dst))
    return tuple(A), tuple(b), cols, tuple(labels)


def solve_unique_columns(A, b, support):
    """Solve overdetermined A[:,support] z=b, requiring full column rank."""
    k = len(support)
    work = [[Q(row[j]) for j in support] + [Q(v)]
            for row, v in zip(A, b)]
    pivot_rows, pivot_row = [], 0
    for col in range(k):
        candidate = next((j for j in range(pivot_row, len(work))
                          if work[j][col] != 0), None)
        if candidate is None:
            return None
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        inv = work[pivot_row][col]
        work[pivot_row] = [a / inv for a in work[pivot_row]]
        for j in range(len(work)):
            if j == pivot_row:
                continue
            coeff = work[j][col]
            if coeff:
                work[j] = [u - coeff * v for u, v in zip(work[j], work[pivot_row])]
        pivot_rows.append(pivot_row)
        pivot_row += 1
    if any(all(work[j][c] == 0 for c in range(k)) and work[j][k] != 0
           for j in range(len(work))):
        return None
    return tuple(work[j][k] for j in pivot_rows)


def stochastic_section(m: FiniteActionQuotient, max_variables=12):
    """Exact rational feasibility for small finite action quotients.

    Feasible fiber-normalized kernels form a compact rational polytope;
    it has a rational vertex with linearly independent positive-support
    columns. Enumerating supports is complete, but exponential. A return of
    None below max_variables is a proved infeasibility verdict of this exact
    procedure; limit and continuum applications are excluded.
    """
    if m.x_size > max_variables:
        raise ValueError("Exponential exact solver limited by max_variables")
    s = point_section(m)
    if s is not None:
        return delta_section(m, s)
    candidate = uniform_fiber_kernel(m)
    if verify_kernel(m, candidate):
        return candidate
    A, b, cols, _ = constraint_matrix(m)
    for size in range(1, len(cols) + 1):
        for support in combinations(range(len(cols)), size):
            solution = solve_unique_columns(A, b, support)
            if solution is None or any(x < 0 for x in solution):
                continue
            v = [Q(0)] * len(cols)
            for j, value in zip(support, solution):
                v[j] = value
            rows = [[Q(0)] * m.x_size for _ in range(m.y_size)]
            for (y, x), value in zip(cols, v):
                rows[y][x] = value
            result = tuple(tuple(row) for row in rows)
            if verify_kernel(m, result):
                return result
    return None


def verify_farkas(A, b, witness):
    """Check exact infeasibility certificate: λA >= 0, λb < 0."""
    if len(witness) != len(A):
        return False
    return (sum((Q(w) * Q(v) for w, v in zip(witness, b)), Q(0)) < 0 and
            all(sum((Q(w) * Q(row[j]) for w, row in zip(witness, A)), Q(0)) >= 0
                for j in range(len(A[0]))))


def total_variation(a, b):
    return sum((abs(Q(x) - Q(y)) for x, y in zip(a, b)), Q(0)) / 2


def max_covariance_defect(m: FiniteActionQuotient, k):
    """Max TV gap between evolving a chosen distribution and relifting."""
    result = Q(0)
    for t, u in zip(m.source_actions, m.report_actions):
        for y in range(m.y_size):
            p = [Q(0)] * m.x_size
            for x, mass in enumerate(k[y]):
                p[t[x]] += mass
            result = max(result, total_variation(p, k[u[y]]))
    return result


def minimal_merging_model():
    """3 source states, 2 reports, 1 T; action descends but no stochastic lift."""
    # a -> b -> c -> c; q(a)=u, q(b)=q(c)=w; u -> w -> w
    return FiniteActionQuotient((0, 1, 1), 2, ((1, 2, 2),), ((1, 1),))


def incompatible_predecessors_model():
    """4 source states, 3 reports, two incompatible histories merging in w."""
    return FiniteActionQuotient((0, 1, 2, 2), 3,
                                ((2, 3, 2, 3),), ((2, 2, 2),))


def finite_swap_model():
    return FiniteActionQuotient((0, 0), 1, ((1, 0),), ((0,),))


def transient_cycle_model():
    # a <-> b; c -> a; a source-invariant probability requires mass(c)=0.
    return FiniteActionQuotient((0, 0, 0), 1, ((1, 0, 0),), ((0,),))


def actions_generate_finite_group(m: FiniteActionQuotient):
    """Enumerate permutation pairs (X,Y), including identity, for small G."""
    if not m.is_group_generated():
        raise ValueError("Not a family of permutation generators")
    id_pair = (tuple(range(m.x_size)), tuple(range(m.y_size)))
    gens = list(zip(m.source_actions, m.report_actions))
    found = {id_pair}
    todo = [id_pair]
    while todo:
        tx, ty = todo.pop()
        for gx, gy in gens:
            nxt = (tuple(gx[tx[x]] for x in range(m.x_size)),
                   tuple(gy[ty[y]] for y in range(m.y_size)))
            if nxt not in found:
                found.add(nxt)
                todo.append(nxt)
    return tuple(sorted(found))


def stabilizer_fixed_section(m: FiniteActionQuotient):
    """Return group-equivariant point section iff every orbit stabilizer fixes a fiber element."""
    group = actions_generate_finite_group(m)
    s = [-1] * m.y_size
    for y in range(m.y_size):
        if s[y] >= 0:
            continue
        stabilizer = [gx for gx, gy in group if gy[y] == y]
        chosen = next((x for x in m.fibers[y] if all(gx[x] == x for gx in stabilizer)), None)
        if chosen is None:
            return None
        for gx, gy in group:
            yy = gy[y]
            xx = gx[chosen]
            if s[yy] not in (-1, xx):
                raise AssertionError("Internal group consistency failure")
            s[yy] = xx
    result = tuple(s)
    assert verify_point_section(m, result)
    return result


def lax_fiber_transport(m: FiniteActionQuotient):
    """Check canonical set-valued MAY lift: T_X(q^-1(y)) subset q^-1(T_Y y)."""
    return all({t[x] for x in m.fibers[y]}.issubset(set(m.fibers[u[y]]))
               for t, u in zip(m.source_actions, m.report_actions)
               for y in range(m.y_size))


def translation_window_defect(radius: int):
    """Exact TV defect under +1 shift of uniform[-radius, radius] on Z."""
    if type(radius) is not int or radius < 0:
        raise ValueError("radius must be nonnegative integer")
    weight = Q(1, 2 * radius + 1)
    before = {k: weight for k in range(-radius, radius+1)}
    after = {k+1: mass for k, mass in before.items()}
    return sum((abs(before.get(k, Q(0))-after.get(k, Q(0)))
                for k in set(before)|set(after)), Q(0)) / 2


@dataclass(frozen=True)
class FiniteMarkovQuotient:
    """A stochastic source law already lumpable to a Markov report law."""
    q: tuple[int, ...]
    y_size: int
    source_transition: tuple[tuple[Q, ...], ...]
    report_transition: tuple[tuple[Q, ...], ...]

    def __post_init__(self):
        nx=len(self.q)
        ny=self.y_size
        if (not nx or type(ny) is not int or ny<1 or
                any(type(v) is not int for v in self.q) or
                set(self.q)!=set(range(ny))):
            raise ValueError('Require finite surjective quotient')
        if len(self.source_transition)!=nx or len(self.report_transition)!=ny:
            raise ValueError('Wrong matrix dimensions')
        for matrix,dim in ((self.source_transition,nx),(self.report_transition,ny)):
            for row in matrix:
                if (len(row)!=dim or
                        any(type(x) not in (int,Q) or Q(x)<0 for x in row) or
                        sum(map(Q,row),Q(0))!=1):
                    raise ValueError('Require stochastic matrix with rational rows')
        for x in range(nx):
            for yy in range(ny):
                if sum((Q(self.source_transition[x][xx]) for xx in range(nx)
                        if self.q[xx]==yy),Q(0)) != Q(self.report_transition[self.q[x]][yy]):
                    raise ValueError('Source stochastic law does not descend to reports')

    @property
    def fibers(self):
        return tuple(tuple(x for x in range(len(self.q)) if self.q[x]==y)
                     for y in range(self.y_size))


def markov_constraints(m:FiniteMarkovQuotient):
    """K P_X = P_Y K with K_y supported on q^-1(y); exact rational A p=b."""
    nx=len(m.q)
    cols=tuple((y,x) for y in range(m.y_size) for x in m.fibers[y])
    ix={c:i for i,c in enumerate(cols)}
    A=[];b=[];labels=[]
    for y in range(m.y_size):
        row=[Q(0)]*len(cols)
        for x in m.fibers[y]:row[ix[y,x]]=Q(1)
        A.append(tuple(row));b.append(Q(1));labels.append(('normal',y))
    for y in range(m.y_size):
        for xx in range(nx):
            row=[Q(0)]*len(cols)
            for x in m.fibers[y]:
                row[ix[y,x]]+=Q(m.source_transition[x][xx])
            row[ix[m.q[xx],xx]]-=Q(m.report_transition[y][m.q[xx]])
            A.append(tuple(row));b.append(Q(0));labels.append(('markov',y,xx))
    return tuple(A),tuple(b),cols,tuple(labels)


def verify_markov_kernel(m:FiniteMarkovQuotient, k):
    nx=len(m.q)
    if len(k)!=m.y_size or any(len(row)!=nx for row in k):return False
    for y,row in enumerate(k):
        if sum(row,Q(0))!=1 or any(Q(p)<0 or (m.q[x]!=y and p!=0)
                                  for x,p in enumerate(row)):
            return False
    for y in range(m.y_size):
        for xx in range(nx):
            lhs=sum((Q(k[y][x])*Q(m.source_transition[x][xx]) for x in range(nx)),Q(0))
            rhs=sum((Q(m.report_transition[y][yy])*Q(k[yy][xx])
                     for yy in range(m.y_size)),Q(0))
            if lhs!=rhs:return False
    return True


def markov_stochastic_section(m:FiniteMarkovQuotient,max_variables=12):
    """Exact complete finite LP vertex search, capped to avoid runaway enumeration."""
    nx=len(m.q)
    if nx>max_variables:raise ValueError('Exact vertex enumeration exceeds variable cap')
    A,b,cols,_=markov_constraints(m)
    for size in range(1,len(cols)+1):
        for support in combinations(range(len(cols)),size):
            sol=solve_unique_columns(A,b,support)
            if sol is None or any(v<0 for v in sol):continue
            k=[[Q(0)]*nx for _ in range(m.y_size)]
            for j,v in zip(support,sol):
                y,x=cols[j]
                k[y][x]=v
            res=tuple(tuple(row) for row in k)
            if verify_markov_kernel(m,res):return res
    return None

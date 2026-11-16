"""Exact finite source-coupled observer filtering, smoothing and policy control.

Scope: declared source stochastic kernels J_a(x,x',o), not authenticated
physical sensors. All probabilities and monetary/action costs are rational.
State carries its original identity separately from its current dynamics.
No posterior is assigned to a zero-likelihood record; no observational
policy may invent an unlicensed source probe.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product

Q = Fraction


def rational(x):
    if type(x) not in (int, Q):
        raise ValueError('Exact rational inputs only, never floats or bools')
    return Q(x)


def normalize(weights):
    xs = tuple(rational(x) for x in weights)
    if not xs or min(xs) < 0:
        raise ValueError('Require nonempty nonnegative exact weights')
    z = sum(xs, Q(0))
    if z <= 0:
        raise ValueError('Zero likelihood is not a posterior')
    return tuple(x/z for x in xs)


@dataclass(frozen=True)
class JointInstrument:
    """J[x][xp][o]=Pr(next=xp, outcome=o | current=x, chosen action)."""
    joint: tuple[tuple[tuple[Q, ...], ...], ...]
    cost: Q
    tag: str = 'declared-source-instrument'

    def __post_init__(self):
        n = len(self.joint)
        if n < 1 or type(self.cost) not in (Q, int) or self.cost <= 0:
            raise ValueError('Nonempty source, positive rational action cost required')
        o = len(self.joint[0][0]) if self.joint[0] else 0
        if o < 1:
            raise ValueError('At least one output required')
        for row in self.joint:
            if len(row) != n or any(len(cell) != o for cell in row):
                raise ValueError('Joint source and outcome dimensions mismatch')
            vs = [rational(p) for cell in row for p in cell]
            if any(p < 0 for p in vs) or sum(vs, Q(0)) != 1:
                raise ValueError('Each source state requires normalized joint law')

    @property
    def n(self):
        return len(self.joint)

    @property
    def output_count(self):
        return len(self.joint[0][0])

    @property
    def transition(self):
        return tuple(tuple(sum(cell, Q(0)) for cell in row)
                     for row in self.joint)

    def post_state_likelihood(self):
        """Return L[xp][o] iff J[x][xp][o]=P[x][xp]*L[xp][o].

        An unvisited xp can choose an arbitrary normalized likelihood; the
        returned factorization must still reproduce every joint source entry.
        """
        n, o = self.n, self.output_count
        P = self.transition
        L = []
        for xp in range(n):
            seen = None
            for x in range(n):
                if P[x][xp] != 0:
                    row = tuple(self.joint[x][xp][y] / P[x][xp] for y in range(o))
                    if seen is not None and row != seen:
                        return None
                    seen = row
            L.append(seen if seen is not None else tuple(Q(1 if y == 0 else 0) for y in range(o)))
        return tuple(L)


def instrument_from_post_likelihood(P, L, cost=Q(1), tag='factorized-source'):
    n = len(P)
    if n < 1 or len(L) != n:
        raise ValueError('State dimensions mismatch')
    for row in P:
        if len(row) != n or any(rational(p) < 0 for p in row) or sum(map(rational, row), Q(0)) != 1:
            raise ValueError('Invalid Markov matrix')
    k = len(L[0])
    for row in L:
        if len(row) != k or any(rational(p) < 0 for p in row) or sum(map(rational,row),Q(0)) != 1:
            raise ValueError('Invalid likelihood')
    J=tuple(tuple(tuple(rational(P[x][xp])*rational(L[xp][y]) for y in range(k))
                  for xp in range(n)) for x in range(n))
    return JointInstrument(J, rational(cost), tag)


def initial_pairs(prior):
    """joint P(original,current) starts on the diagonal."""
    prior=tuple(rational(p) for p in prior)
    if prior != normalize(prior):
        raise ValueError('Prior must be normalized')
    n=len(prior)
    return tuple(tuple(prior[a] if a==x else Q(0) for x in range(n)) for a in range(n))


def update_pair(belief, inst, outcome):
    """(Pr(outcome|evidence,action), P(original,current-next|new evidence))."""
    n=inst.n
    if type(outcome) is not int or not 0 <= outcome < inst.output_count:
        raise ValueError('Unknown observation label')
    if len(belief) != n or any(len(row) != n for row in belief):
        raise ValueError('Belief/source state mismatch')
    result=[[Q(0)]*n for _ in range(n)]
    for a in range(n):
        for x in range(n):
            mass=rational(belief[a][x])
            if mass < 0:
                raise ValueError('Negative belief mass')
            for xp in range(n):
                result[a][xp]+=mass*inst.joint[x][xp][outcome]
    z=sum((v for row in result for v in row),Q(0))
    if z==0:
        return Q(0),None
    return z,tuple(tuple(v/z for v in row) for row in result)


def update_current(prior, inst, outcome):
    """Source-correct Bayesian filter on present state only."""
    if len(prior)!=inst.n or tuple(map(rational,prior)) != normalize(prior):
        raise ValueError('Current state prior must be normalized')
    n=inst.n
    if type(outcome) is not int or not 0 <= outcome < inst.output_count:
        raise ValueError('Unknown outcome')
    mass=tuple(sum((rational(prior[x])*inst.joint[x][xp][outcome]
                   for x in range(n)),Q(0)) for xp in range(n))
    z=sum(mass,Q(0))
    return (z,tuple(v/z for v in mass)) if z else (Q(0),None)


def outcome_law(belief, inst):
    return tuple(update_pair(belief,inst,o)[0] for o in range(inst.output_count))


def current_marginal(belief):
    return tuple(sum((row[x] for row in belief), Q(0)) for x in range(len(belief)))


def original_marginal(belief):
    return tuple(sum(row,Q(0)) for row in belief)


def run_trace(initial, insts, events):
    """Events are (licensed action index, actual outcome index)."""
    belief=initial
    likelihood=Q(1)
    for action,outcome in events:
        z,belief=update_pair(belief,insts[action],outcome)
        if z==0:
            return Q(0), None
        likelihood*=z
    return likelihood,belief



@dataclass(frozen=True)
class SourceCostMeter:
    """Calibrated path-dependent resource cost, tied to J[x][xp][o].

    This cost is assumed available for resource accounting, not silently
    counted as an additional observed signal. If its realized value is
    actually read, include that cost reading in the observable outcome of J.
    """
    table: tuple[tuple[tuple[Q, ...], ...], ...]
    unit: str = 'declared-cost-unit'

    def expected(self, belief, inst):
        n=inst.n
        if len(self.table)!=n or any(len(row)!=n for row in self.table):
            raise ValueError('Cost/source dimensions mismatch')
        if not isinstance(self.unit,str) or not self.unit:
            raise ValueError('Calibrated cost units required')
        if len(belief)!=n or any(len(row)!=n for row in belief):
            raise ValueError('Belief dimensions mismatch')
        result=Q(0)
        for x in range(n):
            mass=sum((Q(belief[a][x]) for a in range(n)),Q(0))
            for xp in range(n):
                costrow=self.table[x][xp]
                if len(costrow)!=inst.output_count:
                    raise ValueError('Cost/outcome dimensions mismatch')
                for y,c in enumerate(costrow):
                    c=rational(c)
                    if c<0:
                        raise ValueError('Negative physical/resource cost')
                    result+=mass*inst.joint[x][xp][y]*c
        return result

def stop_risk(belief, labels):
    n=len(belief)
    if len(labels)!=n:
        raise ValueError('Labels must describe original states')
    bylabel={}
    for a,row in enumerate(belief):
        bylabel[labels[a]]=bylabel.get(labels[a],Q(0))+sum(row,Q(0))
    return Q(1)-max(bylabel.values())


@dataclass(frozen=True)
class Decision:
    value: Q
    action: int | None
    branches: tuple[tuple[int,'Decision'],...]=()


def optimal_bayes_policy(initial, instruments, target, horizon, meters=None):
    """Exact finite-horizon minimal expected cost + 0-1 target error.

    Objective: 1 - max posterior target mass when stopping, plus cost
    per chosen action. Decisions adapt to licensed observations.
    This is *Bayesian*, not worst-case guaranteed identification.
    """
    if type(horizon) is not int or horizon<0:
        raise ValueError('Horizon must be a nonnegative integer')
    n=len(initial)
    if not instruments or len(target)!=n or any(inst.n!=n for inst in instruments):
        raise ValueError('Need compatible source laws and target')
    if sum((v for row in initial for v in row),Q(0))!=1:
        raise ValueError('Prior belief is not normalized')
    if meters is None:
        meters=(None,)*len(instruments)
    if len(meters)!=len(instruments):
        raise ValueError('One declared meter per instrument is required')

    @lru_cache(None)
    def solve(b,h):
        best=Decision(stop_risk(b,target),None)
        if h==0:
            return best
        for i,inst in enumerate(instruments):
            branches=[]
            total=inst.cost + (meters[i].expected(b,inst) if meters[i] is not None else Q(0))
            for o in range(inst.output_count):
                z,nb=update_pair(b,inst,o)
                if z==0:
                    continue
                child=solve(nb,h-1)
                total+=z*child.value
                branches.append((o,child))
            if total<best.value:
                best=Decision(total,i,tuple(branches))
        return best
    return solve(initial,horizon)


def dobrushin_delta(P):
    """Dobrushin contraction coefficient, exact total variation."""
    n=len(P)
    return max((sum((abs(Q(P[i][j])-Q(P[k][j])) for j in range(n)),Q(0))/2
                for i in range(n) for k in range(n)),default=Q(0))


def tv(p,q):
    if len(p)!=len(q):
        raise ValueError('Dimensional mismatch')
    return sum((abs(Q(a)-Q(b)) for a,b in zip(p,q)),Q(0))/2


def contraction_bound(inst):
    """Conservative uniform bound 2(M/m) delta(P), or None.

    When <1, every fixed-action, realized-outcome update is contractive
    uniformly in total variation, provided all post-state emission
    probabilities are strictly positive. Closed-loop changes of action
    depending on prior are NOT covered.
    """
    L=inst.post_state_likelihood()
    if L is None:
        return None
    values=[v for row in L for v in row]
    if min(values)<=0:
        return None
    return 2*max(values)/min(values)*dobrushin_delta(inst.transition)


def iterate_same_outcome(prior, inst, outcome, count):
    if type(count) is not int or count<0:
        raise ValueError('Nonnegative iteration count required')
    result=[tuple(prior)]
    for _ in range(count):
        z,nxt=update_current(result[-1],inst,outcome)
        if z==0:
            raise ValueError('Attempted zero-likelihood iteration')
        result.append(nxt)
    return tuple(result)


def _rank(vectors):
    """Exact rational row-rank of a list of equal-length column-value vectors."""
    if not vectors:
        return 0
    a=[list(map(Q,v)) for v in vectors]
    d=len(a[0]);row=0
    if any(len(v)!=d for v in a):
        raise ValueError('Incompatible predictive-vector lengths')
    for j in range(d):
        pivot=next((k for k in range(row,len(a)) if a[k][j]),None)
        if pivot is None:
            continue
        a[row],a[pivot]=a[pivot],a[row]
        v=a[row][j]
        a[row]=[x/v for x in a[row]]
        for k in range(len(a)):
            if k!=row and a[k][j]:
                fac=a[k][j]
                a[k]=[u-fac*w for u,w in zip(a[k],a[row])]
        row+=1
        if row==len(a):
            break
    return row


def predictive_operator(inst, outcome, values):
    """Heisenberg/source-side precomposition: M_{a,o} f."""
    n=inst.n
    if len(values)!=n or type(outcome) is not int or not 0<=outcome<inst.output_count:
        raise ValueError('Invalid predictive operator input')
    return tuple(sum((inst.joint[x][xp][outcome]*Q(values[xp])
                      for xp in range(n)),Q(0)) for x in range(n))


def predictive_span(instruments):
    """Certified minimal invariant space of all future transcript-probability vectors.

    Returns basis, layer at which a basis vector was found, and exact
    stabilization depth. Starts from constant 1, closes under every
    licensed M_{action,outcome}; stabilization by n-1 rounds maximum.
    """
    if not instruments or any(i.n!=instruments[0].n for i in instruments):
        raise ValueError('Need a nonempty family of source-compatible instruments')
    n=instruments[0].n
    basis=[tuple(Q(1) for _ in range(n))]
    depths=[0]
    for depth in range(1,n+1):
        old=tuple(basis)
        for b in old:
            for inst in instruments:
                for outcome in range(inst.output_count):
                    nxt=predictive_operator(inst,outcome,b)
                    if _rank(basis+[nxt])>len(basis):
                        basis.append(nxt)
                        depths.append(depth)
        if len(basis)==len(old):
            assert depth-1<=n-1
            return tuple(basis),tuple(depths),depth-1
        if len(basis)>n:
            raise AssertionError('Linear span exceeded finite source dimension')
    raise AssertionError('Finite-dimensional predictive closure failed')


def predictive_partition(instruments):
    basis,depths,stabilized=predictive_span(instruments)
    n=instruments[0].n
    groups={}
    for x in range(n):
        signature=tuple(v[x] for v in basis)
        groups.setdefault(signature,[]).append(x)
    return tuple(tuple(indices) for indices in groups.values())


def direct_sum_instruments(left,right):
    """Independent source alternatives in a shared action/outcome/cost language.

    No coupling between the two models is invented; resource costs and
    observable labels must already agree. Useful for exact comparison of
    future transcript laws across candidate source models.
    """
    if (len(left)!=len(right) or not left or
            any(a.output_count!=b.output_count or a.cost!=b.cost
                for a,b in zip(left,right))):
        raise ValueError('Model comparisons require a common action, output and cost contract')
    n1=left[0].n;n2=right[0].n
    def make(a,b):
        k=a.output_count;zero=tuple(Q(0) for _ in range(k))
        rows=[]
        for x in range(n1):
            rows.append(tuple(a.joint[x]) + tuple(zero for _ in range(n2)))
        for x in range(n2):
            rows.append(tuple(zero for _ in range(n1)) + tuple(b.joint[x]))
        return JointInstrument(tuple(rows),a.cost,'source-model-disjoint-sum')
    return tuple(make(a,b) for a,b in zip(left,right))


def predictively_equivalent_priors(left,right,prior_left,prior_right):
    """Exact iff on all finite action/outcome words under shared protocol.

    The fixed-point span of the disjoint union certifies equality of every
    source-model transcript probability for the two initial mixtures.
    It does not certify identical hidden histories, physical adequacy, or
    outcome-dependent resource meter laws.
    """
    if (not left or not right or len(prior_left)!=left[0].n or
            len(prior_right)!=right[0].n):
        raise ValueError('Initial distributions/source models mismatch')
    pa=tuple(map(rational,prior_left));pb=tuple(map(rational,prior_right))
    if pa!=normalize(pa) or pb!=normalize(pb):
        raise ValueError('Only normalized source priors are comparable')
    instruments=direct_sum_instruments(left,right)
    basis,_,_=predictive_span(instruments)
    n=len(pa)
    return all(sum((p*v[x] for x,p in enumerate(pa)),Q(0))==
               sum((p*v[n+x] for x,p in enumerate(pb)),Q(0))
               for v in basis)


def brier_loss(forecast, observed):
    """Exact proper scoring on a preregistered finite outcome alphabet."""
    p=tuple(map(rational,forecast))
    if p!=normalize(p) or type(observed) is not int or not 0<=observed<len(p):
        raise ValueError('Valid normalized forecast and actual outcome required')
    return sum(((v-Q(int(i==observed)))**2 for i,v in enumerate(p)),Q(0))


def expected_brier(forecast,truth):
    q=tuple(map(rational,forecast));p=tuple(map(rational,truth))
    if len(q)!=len(p) or q!=normalize(q) or p!=normalize(p):
        raise ValueError('Calibrated distributions require a common normalized alphabet')
    return sum((p[i]*brier_loss(q,i) for i in range(len(p))),Q(0))


def brier_excess(forecast,truth):
    """Strictly proper Brier excess = squared Euclidean forecast difference."""
    q=tuple(map(rational,forecast));p=tuple(map(rational,truth))
    return expected_brier(q,p)-expected_brier(p,p)

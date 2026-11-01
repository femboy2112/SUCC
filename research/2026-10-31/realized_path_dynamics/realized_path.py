"""Exact finite realized-prefix path dynamics, Doob bridge, and ordered BBP operators.

Research-only. All transitions, costs, and priors are DECLARED model inputs.
The genuine original four-pole zero-seeded BBP dynamics have no stochastic
branching. Positive observer probabilities must not be confused with quantum
amplitudes, real-circle phases, or thermodynamic dissipation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from typing import Mapping


@dataclass(frozen=True)
class Edge:
    label: str
    dest: str
    prior: F
    cost: int = 0

    def __post_init__(self):
        if (not isinstance(self.label,str) or not self.label or
                not isinstance(self.dest,str) or not self.dest or
                type(self.cost) is not int or self.cost < 0 or
                not isinstance(self.prior,F) or self.prior <= 0):
            raise ValueError("Edge must have exact positive Fraction prior, nonnegative integer cost and labels")


@dataclass(frozen=True)
class Path:
    labels: tuple[str,...]
    states: tuple[str,...]
    prior: F
    cost: int

    @property
    def endpoint(self) -> str:
        return self.states[-1]


@dataclass
class PathModel:
    """Finite, ordered, time-indexed path automaton with exact transition priors."""
    root: str
    layers: tuple[dict[str,tuple[Edge,...]],...]
    targets: frozenset[str]

    def __post_init__(self):
        if not self.layers or not isinstance(self.root,str) or not self.root:
            raise ValueError("Nonempty rooted finite horizon required")
        reached={self.root}
        for t,layer in enumerate(self.layers):
            if set(layer) != reached:
                raise ValueError(f"Only exactly reachable states allowed at time {t}")
            after=set()
            for state,edges in layer.items():
                if not edges or any(not isinstance(e,Edge) for e in edges):
                    raise ValueError("Every reachable state requires lawful edges")
                if sum((e.prior for e in edges),F(0))!=1:
                    raise ValueError("Transition priors must be normalized exact rationals")
                if len({e.label for e in edges})!=len(edges):
                    raise ValueError("Action labels must be distinct at each state")
                after.update(e.dest for e in edges)
            reached=after
        if not self.targets or not self.targets <= reached:
            raise ValueError("Declared target must lie in final reachable states")

    def enumerate_paths(self) -> tuple[Path,...]:
        paths=[Path((),(self.root,),F(1),0)]
        for layer in self.layers:
            paths=[Path(p.labels+(edge.label,),p.states+(edge.dest,),
                        p.prior*edge.prior,p.cost+edge.cost)
                   for p in paths for edge in layer[p.endpoint]]
        if sum((p.prior for p in paths),F())!=1:
            raise ArithmeticError("Reference path mass is not one")
        return tuple(paths)

    def desirability(self,lam:F=F(1,2)) -> tuple[dict[str,F],...]:
        if not isinstance(lam,F) or not (0<lam<=1):
            raise ValueError("Discount must be an exact Fraction in (0,1]")
        states={e.dest for edges in self.layers[-1].values() for e in edges}
        h=[{} for _ in range(len(self.layers)+1)]
        h[-1]={state:F(state in self.targets) for state in states}
        for t in range(len(self.layers)-1,-1,-1):
            h[t]={state:sum((e.prior*lam**e.cost*h[t+1][e.dest]
                             for e in edges),F()) for state,edges in self.layers[t].items()}
        if h[0][self.root]==0:
            raise ValueError("No positive-cost target path under declared source")
        return tuple(h)

    def optimal_transition(self,t:int,state:str,lam:F=F(1,2)) -> dict[str,F]:
        if type(t) is not int or not 0<=t<len(self.layers):
            raise ValueError("Valid transition time needed")
        h=self.desirability(lam)
        if state not in self.layers[t] or h[t][state]==0:
            raise ValueError("Non-reachable or nonviable history")
        p={e.label:e.prior*lam**e.cost*h[t+1][e.dest]/h[t][state]
           for e in self.layers[t][state]}
        if sum(p.values(),F())!=1:
            raise ArithmeticError("Doob path measure not normalized")
        return p

    def tilted_paths(self,lam:F=F(1,2)) -> dict[Path,F]:
        h=self.desirability(lam)
        total=h[0][self.root]
        return {p:(p.prior*lam**p.cost/total if p.endpoint in self.targets else F())
                for p in self.enumerate_paths()}

    def condition(self,prefix:tuple[str,...],lam:F=F(1,2)) -> tuple[F,dict[Path,F]]:
        if not isinstance(prefix,tuple) or len(prefix)>len(self.layers):
            raise ValueError("Prefix must be a tuple within horizon")
        q=self.tilted_paths(lam)
        mass=sum((weight for p,weight in q.items() if p.labels[:len(prefix)]==prefix),F())
        if mass==0:
            raise ValueError("Cannot realize a path with zero posterior support")
        return mass,{p:(w/mass if p.labels[:len(prefix)]==prefix else F()) for p,w in q.items()}


def history_model() -> PathModel:
    """A/B have IDENTICAL visible state x=1 but DIFFERENT futures/target odds."""
    return PathModel(
        root="root",
        layers=(
            {"root":(Edge("A","A",F(1,2)),Edge("B","B",F(1,2)))},
            {"A":(Edge("hit","T",F(3,4)),Edge("miss","X",F(1,4))),
             "B":(Edge("hit","T",F(1,4),cost=2),Edge("miss","X",F(1,4)),
                   Edge("sidetrack","Y",F(1,2)))}),
        targets=frozenset({"T"}))


def observed_position(state:str)->int:
    return {"root":0,"A":1,"B":1,"T":2,"X":0,"Y":4}[state]


def deconditioned_future_support(model:PathModel,prefix:tuple[str,...])->frozenset[str]:
    """Physical possibility support of reference model after observed word."""
    matching=[p.endpoint for p in model.enumerate_paths()
              if p.labels[:len(prefix)]==prefix]
    return frozenset(matching)


def posterior_partition_identity(model:PathModel,lam:F=F(1,2))->bool:
    """Exact finite Gibbs/KL algebra: Q*(path)/(R(path)*lam^cost)=1/Z."""
    h=model.desirability(lam)[0][model.root]
    paths=model.tilted_paths(lam)
    return all(q/(path.prior*lam**path.cost)==1/h
               for path,q in paths.items() if q)


def zero_temperature_branch(lam:F)->F:
    """Exact target-constrained model's probability of A, 3/(3+lambda^2)."""
    return history_model().optimal_transition(0,"root",lam)["A"]


Mat=tuple[tuple[F,F],tuple[F,F]]
IDENTITY:Mat=((F(1),F()),(F(),F(1)))
ZERO:Mat=((F(),F()),(F(),F()))


def matmul(a:Mat,b:Mat)->Mat:
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)),F())
                       for j in range(2)) for i in range(2))  # type: ignore[return-value]


def matscale(a:Mat,s:F)->Mat:
    return tuple(tuple(s*v for v in row) for row in a)  # type: ignore[return-value]


def matadd(a:Mat,b:Mat)->Mat:
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2)) # type: ignore[return-value]


def original_source(n:int)->F:
    if type(n) is not int or n<1:
        raise ValueError("Positive integer original source index required")
    return (F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))


def source_step(n:int)->Mat:
    return ((F(16),original_source(n)),(F(),F(1)))


def source_product(N:int)->Mat:
    if type(N) is not int or N<0:
        raise ValueError("N must be a nonnegative integer")
    p=IDENTITY
    for n in range(1,N+1):p=matmul(source_step(n),p)
    return p


def original_state(N:int)->F:
    return source_product(N)[0][1]


def original_action(N:int)->F:
    return original_state(N)/16**N


def symplectic_source_action(N:int)->F:
    """Sum original canonical source increments, exact rational SUCC A_N=x_N p_N."""
    if type(N) is not int or N<0:
        raise ValueError("N must be a nonnegative integer")
    return sum((original_source(n)/16**n for n in range(1,N+1)),F())


def source_commutator()->F:
    """(F_2 F_1 - F_1 F_2) upper-right, actual signed order difference."""
    a,b=source_step(1),source_step(2)
    return matmul(b,a)[0][1]-matmul(a,b)[0][1]


def finite_operator_path_integral(steps:tuple[tuple[tuple[F,int,Mat],...],...],
                                 lam:F=F(1,2))->tuple[Mat,Mat]:
    """Independent-step exact matrix path integral, enumeration vs ordered transfer.

    Returns (direct path sum, product of weighted transfer operators).
    Ordered matrices must not be replaced by commuting scalar factors.
    """
    if not isinstance(steps,tuple) or not steps:
        raise ValueError("At least one step required")
    for step in steps:
        if not step or sum((p for p,_,_ in step),F())!=1:
            raise ValueError("Each step must have normalized exact probability")
    direct=ZERO
    for choices in product(*steps):
        w=F(1);m=IDENTITY
        for prior,cost,op in choices:
            w*=prior*lam**cost
            m=matmul(op,m)
        direct=matadd(direct,matscale(m,w))
    transfer=IDENTITY
    for step in steps:
        op=ZERO
        for prior,cost,mat in step:
            op=matadd(op,matscale(mat,prior*lam**cost))
        transfer=matmul(op,transfer)
    return direct,transfer


def dependent_path_integral()->tuple[Mat,Mat]:
    """History-conditioned second-step choice differs from naïve average kernels."""
    first=source_step(1);second=source_step(2)
    avg=lambda a,b,p:matadd(matscale(a,p),matscale(b,1-p))
    direct=matadd(matscale(matmul(avg(second,IDENTITY,F(3,4)),first),F(1,2)),
                  matscale(avg(second,IDENTITY,F(1,4)),F(1,2)))
    naive=matmul(avg(second,IDENTITY,F(1,2)),avg(first,IDENTITY,F(1,2)))
    return direct,naive


def phase_model_counterexample()->tuple[F,F]:
    """Same positive paths, entropy and costs: maximum vs zero phase sum."""
    weights=(F(1,2),F(1,2))
    same=sum(weights,F());opposite=weights[0]-weights[1]
    return same,opposite


def entropy_future_counterexample()->tuple[F,int]:
    """Prior trajectory entropy=5/2 bits; after choosing A, future entropy=3."""
    return F(5,2),3


def normalized_generator(n:int)->Mat:
    """Rank-one idempotent G_n, with F_n=I+15G_n.

    The ACTUAL Hamiltonian generator is (ln 16)*G_n, but all rational
    finite identities can be checked without introducing transcendental logs.
    """
    return ((F(1),original_source(n)/15),(F(),F()))


def generator_commutator(i:int,j:int)->F:
    a,b=normalized_generator(i),normalized_generator(j)
    return matmul(a,b)[0][1]-matmul(b,a)[0][1]


def symplectic_segment(n:int,x:F,p:F,quarter_ticks:int)->tuple[F,F]:
    """Exact time-s flow for s=k/4, 16^s=2^k, of H_n=(ln16)*p*(x+r(n)/15).

    Only positions/momenta of the exact original n-th source step and
    rational quarter-times are returned; physical Hamiltonian not claimed.
    """
    if not isinstance(x,F) or not isinstance(p,F) or type(quarter_ticks) is not int or not 0<=quarter_ticks<=4:
        raise ValueError("Exact Fraction canonical coordinates and quarter-step required")
    z=2**quarter_ticks
    r=original_source(n)
    return (F(z)*x+F(z-1)*r/15,p/F(z))


def micro_paths_same_endpoint(n:int,x:F)->tuple[tuple[F,F],tuple[F,F]]:
    """Two authentic-source affine decompositions with equal end but different intermediate states.

    A: V16 then translation by r(n).
    B: translation by r(n)/16 then V16.
    Histories are NOT different physical BBP trajectories; they are alternative
    exact expressions of the SAME source step and selected character.
    """
    if not isinstance(x,F):raise ValueError("Fraction initial state required")
    r=original_source(n)
    return ((F(16)*x,F(16)*x+r),(x+r/16,F(16)*(x+r/16)))


def ordered_band_expansion(N:int)->Mat:
    """Exact affine ordered product from the ORIGINAL right-zero idempotent band.

    Product F_N...F_1=I+15*sum_(j=1)^N 16^(N-j) G_j.
    This is an algebraic subset expansion, not a quantum path integral.
    """
    if type(N) is not int or N<0:raise ValueError("Nonnegative integer horizon required")
    total=IDENTITY
    for j in range(1,N+1):
        total=matadd(total,matscale(normalized_generator(j),F(15*16**(N-j))))
    return total


def subset_band_expansion(N:int)->Mat:
    """Independent direct subset enumeration (2^N histories), no recurrence."""
    if type(N) is not int or not 0<=N<=14:
        raise ValueError("Explicit subset count is restricted to N<=14")
    s=IDENTITY
    for mask in range(1,1<<N):
        chosen=[i+1 for i in range(N) if mask & (1<<i)]
        g=IDENTITY
        for index in sorted(chosen,reverse=True):
            g=matmul(g,normalized_generator(index))
        s=matadd(s,matscale(g,F(15**len(chosen))))
    return s


def tied_geodesic_model()->PathModel:
    """Two paths to the SAME endpoint with equal source action; no unique selector."""
    return PathModel('root',({'root':(Edge('first','T',F(1,2),1),
                                      Edge('second','T',F(1,2),1))},),frozenset({'T'}))


def doob_path_weight(model:PathModel,labels:tuple[str,...],lam:F=F(1,2))->F:
    """Ordered product of tilted transitions from the realized full history."""
    if not isinstance(labels,tuple) or len(labels)!=len(model.layers):
        raise ValueError("Full exact action history required")
    states=model.root
    mass=F(1)
    h=model.desirability(lam)
    for t,label in enumerate(labels):
        edges={edge.label:edge for edge in model.layers[t][states]}
        if label not in edges:
            raise ValueError("Operation not permitted by this history")
        edge=edges[label]
        if h[t][states]==0:return F()
        mass*=edge.prior*lam**edge.cost*h[t+1][edge.dest]/h[t][states]
        states=edge.dest
    return mass


def time_entropy_only_no_go(N:int)->tuple[int,F]:
    """Uniform time-index entropy log2 N doesn't determine signed phase average.

    Returned exact pair is (N,1): same time distribution has phases all +1
    or alternating roots giving different signed sums. The actual BBP coherent
    q=1/5 altered-seed counterpart is cited/proved in the dossier.
    """
    if type(N) is not int or N<2 or N%2:
        raise ValueError("An even nonzero time horizon is required")
    return N, sum((F(1 if j%2==0 else -1) for j in range(N)),F())/N


def finite_action_tail_mass(cutoff:int)->F:
    """Finite exact prefix of Σ_(n>=1)(alpha-A_n)=Σ_(j>=2)(j−1)r(j)/16^j.

    The infinite total has a PAPER proof bound <1/1024, independent of cutoff.
    """
    if type(cutoff) is not int or cutoff<2 or cutoff>10000:
        raise ValueError("Finite positive cutoff 2..10000 required")
    return sum((F(j-1)*original_source(j)/16**j for j in range(2,cutoff+1)),F())


def rational_action_tilt_weights(N:int)->tuple[F,...]:
    """Concrete rational positive time weights f(A_n)=1/(1+A_n).

    Pure exact finite comparator for the general Lipschitz-reweighting theorem;
    these weights do not create or certify real-circle cancellation.
    """
    if type(N) is not int or N<1 or N>10000:
        raise ValueError("Finite N 1..10000 required")
    return tuple(F(1)/(1+original_action(n)) for n in range(1,N+1))


def weighted_mean_real(phases:tuple[F,...],weights:tuple[F,...])->F:
    """Exact rational toy character mean used to validate transport algebra only."""
    if not phases or len(phases)!=len(weights) or any(w<=0 for w in weights):
        raise ValueError("Matched nonempty phases and positive weights required")
    return sum((p*w for p,w in zip(phases,weights)),F())/sum(weights,F())

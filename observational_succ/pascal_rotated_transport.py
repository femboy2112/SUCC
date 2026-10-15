"""Pascal/rotated observation and Gamma moment transport for Observational SUCC.

Source scope: exact formal commutative steps, graded Pascal paths, finite positive
Bernoulli boundary ensembles, exact change-of-basis matrices, and declared
moment laws. Ordered noncommutative words are evaluated in the existing
structural_coupling.CyclicExtension. No physical instrumentation or RH.

A finite geometric 90-degree rotation, a transpose/adjoint of a Pascal operator,
a Bayesian cotransition and a Mellin integral are FOUR DISTINCT operations.
None is silently identified with the others.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
from typing import Sequence

from .structural_coupling import CyclicExtension, Element


class PascalTransportError(ValueError):
    """Malformed source, nonexistent experiment, or unsupported promotion."""


def exact(v: int | Q) -> Q:
    if type(v) is int or type(v) is Q:
        return Q(v)
    raise PascalTransportError("Only exact int/Fraction coefficients admitted")


def bounded(n: int, cap: int = 64) -> int:
    if type(n) is not int or n < 0 or n > cap:
        raise PascalTransportError(f"Grading requires integer n in [0,{cap}]")
    return n


@dataclass(frozen=True)
class PascalCell:
    n: int
    k: int
    multiplicity: int
    address: Q
    a_steps: int
    b_steps: int


@dataclass(frozen=True)
class UnitFrame:
    """Two source-declared primitive steps; a and b are units, not probabilities."""
    a: Q
    b: Q
    source_id: str = "declared_pascal_source"
    basis_id: str = "declared_units"
    epoch: int = 0

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", exact(self.a))
        object.__setattr__(self, "b", exact(self.b))
        if not self.source_id or not self.basis_id or type(self.epoch) is not int or self.epoch < 0:
            raise PascalTransportError("Nonempty source/basis and nonnegative epoch required")

    def cell(self, n: int, k: int) -> PascalCell:
        bounded(n)
        if type(k) is not int or not 0 <= k <= n:
            raise PascalTransportError("Pascal coordinate must satisfy 0 <= k <= n")
        return PascalCell(n, k, comb(n, k), (n-k)*self.a+k*self.b, n-k, k)

    def row(self, n: int) -> tuple[PascalCell, ...]:
        bounded(n)
        return tuple(self.cell(n, k) for k in range(n+1))

    def parents(self, n: int, k: int) -> tuple[PascalCell, ...]:
        self.cell(n,k)
        if n == 0:
            return ()
        return tuple(self.cell(n-1,j) for j in (k-1,k) if 0 <= j <= n-1)

    def collapse_witness(self, n: int) -> tuple[PascalCell, PascalCell] | None:
        """Find two different path-count cells having the same ACTUAL address."""
        row = self.row(n)
        for i in range(len(row)):
            for j in range(i+1,len(row)):
                if row[i].address == row[j].address:
                    return (row[i],row[j])
        return None


def formal_path_monomials(n: int) -> tuple[tuple[tuple[int,int],int], ...]:
    """Symbolic (A,B) degrees; remains faithful even when numerical units alias."""
    bounded(n)
    return tuple((((n-k),k),comb(n,k)) for k in range(n+1))


def coproduct_monomial(n: int) -> tuple[tuple[tuple[int,int],int], ...]:
    """Delta(x^n) for primitive x; equals Pascal row by definition."""
    return formal_path_monomials(n)


def divided_power_product(m: int, n: int) -> int:
    """Coefficient of e_(m+n) in e_m * e_n, e_j=x^j/j!."""
    bounded(m);bounded(n)
    return comb(m+n,m)


def coproduct_divided(n: int) -> tuple[tuple[tuple[int,int],int], ...]:
    bounded(n)
    return tuple(((k,n-k),1) for k in range(n+1))


def triple_split_coefficient(n: int, a: int, b: int, c: int, side: str) -> int:
    """Independent (Delta⊗id)Delta or (id⊗Delta)Delta coefficient."""
    bounded(n)
    if any(type(v) is not int or v < 0 for v in (a,b,c)) or a+b+c!=n:
        raise PascalTransportError("Triple graded partition required")
    if side == "left":
        return comb(n,a+b)*comb(a+b,a)
    if side == "right":
        return comb(n,a)*comb(n-a,b)
    raise PascalTransportError("Choose left or right coassociation")


def antipode_cancellation(n: int) -> int:
    bounded(n)
    return sum(comb(n,k)*(-1)**k for k in range(n+1))


def pascal_matrix(order: int, unit: int | Q = 1) -> tuple[tuple[Q, ...], ...]:
    """B_d moment transport m_n -> sum C(n,k)d^(n-k)m_k, including n=0."""
    bounded(order,32);d=exact(unit)
    return tuple(tuple(Q(comb(n,k))*d**(n-k) if k<=n else Q(0)
                       for k in range(order+1)) for n in range(order+1))


def matmul(a: Sequence[Sequence[Q]],b: Sequence[Sequence[Q]]) -> tuple[tuple[Q,...],...]:
    n=len(a)
    if not n or any(len(r)!=n for r in a) or len(b)!=n or any(len(r)!=n for r in b):
        raise PascalTransportError("Matching square finite matrices required")
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(n)),Q(0))
                       for j in range(n)) for i in range(n))


def apply_pascal(moments: Sequence[int | Q], unit: int | Q = 1) -> tuple[Q, ...]:
    d=exact(unit)
    if not moments or len(moments)>33:
        raise PascalTransportError("Nonempty bounded finite moment sequence required")
    M=tuple(exact(x) for x in moments)
    return tuple(sum((Q(comb(n,k))*d**(n-k)*M[k] for k in range(n+1)),Q(0))
                 for n in range(len(M)))


def weighted_adjoint(a: Sequence[Sequence[Q]], weights: Sequence[int | Q]) -> tuple[tuple[Q,...],...]:
    """W^-1 A^T W for a strictly positive declared pairing W."""
    n=len(a)
    w=tuple(exact(x) for x in weights)
    if not n or len(w)!=n or any(t<=0 for t in w) or any(len(r)!=n for r in a):
        raise PascalTransportError("Positive, complete metric and square operator required")
    return tuple(tuple(w[j]*a[j][i]/w[i] for j in range(n)) for i in range(n))


def weighted_pair(u: Sequence[Q],v: Sequence[Q],weights: Sequence[Q]) -> Q:
    if len(u)!=len(v) or len(u)!=len(weights):
        raise PascalTransportError("Pairing dimension mismatch")
    return sum((exact(u[i])*exact(v[i])*exact(weights[i]) for i in range(len(u))),Q(0))


def matrix_apply(m: Sequence[Sequence[Q]],x: Sequence[Q]) -> tuple[Q,...]:
    if not m or any(len(row)!=len(x) for row in m):
        raise PascalTransportError("Operator/vector dimensions differ")
    return tuple(sum((exact(t)*exact(v) for t,v in zip(row,x)),Q(0)) for row in m)


def rotate_clockwise(n: int, k: int, depth: int) -> tuple[int,int]:
    """Literal finite 90° screen-clockwise rotation of (x=k,y=n), y downward.

    This is NOT an infinite-dimensional operator transform; a fixed cell
    drifts to x=N-n as depth N -> infinity.
    """
    bounded(depth)
    if type(n) is not int or type(k) is not int or not 0<=k<=n<=depth:
        raise PascalTransportError("Cell outside finite triangle")
    return (depth-n,k)


def unrotate_clockwise(x: int,y: int,depth: int) -> tuple[int,int]:
    bounded(depth)
    if any(type(v) is not int for v in (x,y)) or not 0<=x<=depth or not 0<=y<=depth-x:
        raise PascalTransportError("Cell outside rotated triangle")
    return (depth-x,y)


def forward_binomial(n: int, p: int | Q) -> tuple[Q,...]:
    bounded(n)
    p=exact(p)
    if not 0<=p<=1:
        raise PascalTransportError("Bernoulli source law must be in [0,1]")
    return tuple(Q(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1))


def backward_kernel(n: int,k: int) -> tuple[tuple[int,Q],...]:
    """Central Pascal cotransition conditioned on (n,k); p-independent.

    Return previous k' and probability. Boundary zero mass represented
    by absent transition; only claims for source-supported vertices are lawful.
    """
    bounded(n)
    if n==0 or type(k) is not int or not 0<=k<=n:
        raise PascalTransportError("Nonroot valid successor required")
    return tuple((prev,prob) for prev,prob in ((k-1,Q(k,n)),(k,Q(n-k,n)))
                 if prob>0)


def project_backwards(row: Sequence[int | Q]) -> tuple[Q,...]:
    """Law of previous count after cotransport from row n to n-1."""
    if type(row) not in (tuple,list) or len(row)<2 or len(row)>65:
        raise PascalTransportError("Need normalized row n>=1")
    probs=tuple(exact(q) for q in row)
    if any(q<0 for q in probs) or sum(probs,Q(0))!=1:
        raise PascalTransportError("Complete nonnegative normalized source law required")
    n=len(probs)-1
    ans=[Q(0) for _ in range(n)]
    for k,p in enumerate(probs):
        for j,back in backward_kernel(n,k):
            ans[j]+=p*back
    return tuple(ans)


def mixture_binomial(n: int, prior: Sequence[tuple[int | Q,int | Q]]) -> tuple[Q,...]:
    bounded(n)
    if not prior:
        raise PascalTransportError("Declare a nonempty boundary measure")
    w=tuple(exact(v) for v,_ in prior)
    if any(v<0 for v in w) or sum(w,Q(0))!=1:
        raise PascalTransportError("Normalized nonnegative prior required")
    rows=[forward_binomial(n,p) for _,p in prior]
    return tuple(sum((w[i]*rows[i][k] for i in range(len(w))),Q(0)) for k in range(n+1))


def ordered_word_fiber(n: int,k: int,max_n: int=10) -> tuple[tuple[str,...], ...]:
    """All genuinely ordered length-n words with exactly k B steps."""
    bounded(n,max_n)
    if type(k) is not int or not 0<=k<=n:
        raise PascalTransportError("Invalid path fiber coordinate")
    return tuple(word for word in product(('A','B'),repeat=n) if word.count('B')==k)


def evaluate_extension_fiber(ext: CyclicExtension,n: int,k: int,
                             a: Element=(1,0),b: Element=(0,1)) -> tuple[tuple[Element,int],...]:
    """Multiset of endpoints of all ordered words; never assume AB=BA."""
    ext.check_element(a); ext.check_element(b)
    result:dict[Element,int]={}
    for word in ordered_word_fiber(n,k):
        state=ext.identity
        for symbol in word:
            state=ext.multiply(state,a if symbol=='A' else b)
        result[state]=result.get(state,0)+1
    return tuple(sorted(result.items()))


def commutator_witness(ext:CyclicExtension,a:Element=(1,0),b:Element=(0,1)) -> tuple[Element,Element] | None:
    ext.check_element(a);ext.check_element(b)
    ab=ext.multiply(a,b);ba=ext.multiply(b,a)
    return None if ab==ba else (ab,ba)


def factorial_moment(n:int,rate:int|Q=1) -> Q:
    bounded(n)
    r=exact(rate)
    if r<=0:
        raise PascalTransportError("Positive exponential source rate required")
    return Q(factorial(n),1)/r**n


def shifted_exponential_moment(n:int,unit:int|Q=0,rate:int|Q=1) -> Q:
    """Integral_0^infty rate e^-rate*t (t+unit)^n dt for integer n>=0."""
    bounded(n)
    d=exact(unit)
    r=exact(rate)
    if r<=0:
        raise PascalTransportError("Positive exponential source rate required")
    return sum((Q(comb(n,k))*d**(n-k)*factorial_moment(k,r) for k in range(n+1)),Q(0))


def shift_moment_recurrence(n:int,unit:int|Q,rate:int|Q=1) -> Q:
    """IBP: M_n(d)=d^n+(n/r) M_(n-1)(d), n>=1; M_0=1."""
    bounded(n);d=exact(unit);r=exact(rate)
    if r<=0:
        raise PascalTransportError("Positive rate required")
    if n==0:return Q(1)
    return d**n+Q(n)*shifted_exponential_moment(n-1,d,r)/r


def shifted_atomic_moment(n:int,unit:int|Q=0,atom:int|Q=1) -> Q:
    """Independent positive carrier delta_atom: valid Pascal but NOT Gamma."""
    bounded(n)
    a=exact(atom);d=exact(unit)
    if a<0:
        raise PascalTransportError("Atomic measure supported on R>=0 required")
    return (a+d)**n

@dataclass(frozen=True)
class SyntheticPascalReceipt:
    source_id:str
    basis_id:str
    epoch:int
    action_word:tuple[str,...]
    observed_address:Q
    origin:str="declared_simulation"

    def __post_init__(self)->None:
        if (not self.source_id or not self.basis_id or type(self.epoch) is not int or self.epoch<0
            or any(x not in ('A','B') for x in self.action_word)
            or self.origin!='declared_simulation'):
            raise PascalTransportError("Malformed source/basis/epoch or forged physical receipt")
        object.__setattr__(self,"observed_address",exact(self.observed_address))


def check_synthetic_receipt(frame:UnitFrame,r:SyntheticPascalReceipt)->bool:
    if r.source_id!=frame.source_id or r.basis_id!=frame.basis_id or r.epoch!=frame.epoch:
        raise PascalTransportError("Source-map or epoch mismatch")
    predicted=r.action_word.count('A')*frame.a+r.action_word.count('B')*frame.b
    if predicted!=r.observed_address:
        raise PascalTransportError("Claimed receipt disagrees with declared source law")
    return True


def residue_walk_law(n:int,modulus:int,a:int,b:int,p:int|Q) -> tuple[Q,...]:
    """Exact group-algebra specialization Q[C_modulus] of Pascal walk."""
    bounded(n)
    if any(type(v) is not int for v in (modulus,a,b)) or not 2<=modulus<=64:
        raise PascalTransportError("Declared finite cyclic carrier and integer step labels required")
    row=[Q(0)]*modulus
    for k,prob in enumerate(forward_binomial(n,p)):
        row[((n-k)*a+k*b)%modulus]+=prob
    return tuple(row)


def cyclic_convolve(u:Sequence[Q],v:Sequence[Q]) -> tuple[Q,...]:
    if not u or len(u)!=len(v):
        raise PascalTransportError("Same finite cyclic source group required")
    m=len(u)
    return tuple(sum((exact(u[i])*exact(v[(j-i)%m]) for i in range(m)),Q(0)) for j in range(m))


def parity_character(n:int,a:int,b:int,p:int|Q)->Q:
    """Character chi_1 on C2: ((1-p)(-1)^a + p(-1)^b)^n."""
    bounded(n)
    if type(a) is not int or type(b) is not int:
        raise PascalTransportError("Integer units needed for parity spectral character")
    p=exact(p)
    if not Q(0)<=p<=Q(1):
        raise PascalTransportError("Probability outside [0,1]")
    return ((1-p)*(Q(-1) if a%2 else Q(1)) + p*(Q(-1) if b%2 else Q(1)))**n


def group_word_sum(ext:CyclicExtension,n:int,a:Element=(1,0),b:Element=(0,1)) -> tuple[tuple[Element,int],...]:
    """Full noncommuting expansion (R_a+R_b)^n on the group identity."""
    bounded(n,10)
    ext.check_element(a);ext.check_element(b)
    counts:dict[Element,int]={}
    for w in product(('A','B'),repeat=n):
        x=ext.identity
        for letter in w:
            x=ext.multiply(x,a if letter=='A' else b)
        counts[x]=counts.get(x,0)+1
    return tuple(sorted(counts.items()))


def falsely_commutative_sum(ext:CyclicExtension,n:int,a:Element=(1,0),b:Element=(0,1)) -> tuple[tuple[Element,int],...]:
    """INVALID unless a and b commute: sum_k C(n,k) a^(n-k) b^k."""
    bounded(n,10)
    ext.check_element(a);ext.check_element(b)
    counts:dict[Element,int]={}
    for k in range(n+1):
        x=ext.identity
        for letter in ('A',)*(n-k)+('B',)*k:
            x=ext.multiply(x,a if letter=='A' else b)
        counts[x]=counts.get(x,0)+comb(n,k)
    return tuple(sorted(counts.items()))


def bayes_backwards_from_p(n:int,k:int,p:int|Q) -> tuple[tuple[int,Q],...]:
    """Derive reversed edge law from a Bernoulli(p) source; refuse null events."""
    bounded(n)
    p=exact(p)
    if not 0<=p<=1 or n<1 or type(k) is not int or not 0<=k<=n:
        raise PascalTransportError("Valid positive-horizon and Bernoulli source needed")
    current=forward_binomial(n,p)[k]
    if current==0:
        raise PascalTransportError("Cannot condition on a zero-likelihood source event")
    prev=forward_binomial(n-1,p)
    out=[]
    for j,prob in ((k-1,p),(k,1-p)):
        if 0<=j<n:
            mass=prev[j]*prob/current
            if mass:out.append((j,mass))
    if sum((q for _,q in out),Q(0))!=1:
        raise AssertionError("Bayes prior lost mass")
    return tuple(out)


def generalized_binomial(s: int | Q,k:int)->Q:
    """Finite falling-factorial coefficient at rational NONINTEGER time s.

    It extends Pascal's algebraic recursion; for s outside nonnegative
    integers the resulting row is generally infinite and signed, not a
    probability law or positive path-count measure.
    """
    s=exact(s);bounded(k,128)
    v=Q(1)
    for j in range(k):
        v*=Q(s-j,j+1)
    return v


def generalized_pascal_prefix(s:int|Q,cutoff:int,z:int|Q)->Q:
    bounded(cutoff,128);z=exact(z)
    return sum((generalized_binomial(s,k)*z**k for k in range(cutoff+1)),Q(0))


def binomial_absolute_tail_enclosure(s:int|Q,cutoff:int,z:int|Q)->Q:
    """Certified absolute tail for generalized (1+z)^s on this domain.

    For s>-1, |z|<1, and first omitted N=cutoff+1 >= ceil(s),
    |a_(k+1)|/|a_k|=|s-k| |z|/(k+1) <= |z| for k>=N.
    Bound tail <= |binom(s,N) z^N|/(1-|z|).
    No assertion outside this certified monotone-ratio cone.
    """
    s=exact(s);z=exact(z);bounded(cutoff,127)
    N=cutoff+1
    if s<=-1 or abs(z)>=1 or Q(N)<s:
        raise PascalTransportError("Outside certified generalized-binomial tail domain")
    return abs(generalized_binomial(s,N)*z**N)/(1-abs(z))


def laguerre_two_atom_moment(n:int)->int:
    """Positive 2-node quadrature impostor of Exp(1) moments, all exact.

    Nodes: 2+-sqrt(2). Weights for low/high nodes respectively
    (2+sqrt(2))/4, (2-sqrt(2))/4. The moments satisfy
        m_0=m_1=1, m_n=4m_(n-1)-2m_(n-2).
    Therefore they match n! through n=3, but m_4=20 !=24.
    This is a finite-prefix source-map obstruction, not Gamma uniqueness.
    """
    bounded(n)
    if n<=1:return 1
    a,b=1,1
    for _ in range(2,n+1):
        a,b=b,4*b-2*a
    return b


# PB8: operational count/time-axis duality, not a literal geometrical turn.
def discrete_wait_probability(trials:int,events:int,p:int|Q)->Q:
    """P(T_events=trials) in independent Bernoulli(p) trials (Pascal pmf)."""
    bounded(trials)
    bounded(events)
    p=exact(p)
    if events<1 or not Q(0)<=p<=Q(1):
        raise PascalTransportError("Positive event target and lawful Bernoulli p required")
    if trials<events:
        return Q(0)
    return Q(comb(trials-1,events-1))*p**events*(1-p)**(trials-events)


def discrete_wait_survival(trials:int,events:int,p:int|Q)->Q:
    """Exact event equivalence P(T_events>trials)=P(N_trials<events)."""
    bounded(trials);bounded(events)
    if events<1:
        raise PascalTransportError("Positive event target required")
    return sum(forward_binomial(trials,p)[:events],Q(0))


def colored_poisson_prefactor(events:int,k:int,mean:int|Q,p:int|Q)->Q:
    """Coefficient of e^-mean in P(N_t=events,K_B=k).

    Assumes a homogeneous rate and iid Bernoulli(p) mark per event. This is
    an algebraic joint law, not an observed physical event.
    """
    bounded(events)
    if type(k) is not int or not 0<=k<=events:
        raise PascalTransportError("Bad number of B-colored events")
    lam=exact(mean)
    if lam<0:
        raise PascalTransportError("Poisson mean nonnegative")
    return lam**events/Q(factorial(events))*forward_binomial(events,p)[k]


def exp_minus_rational_bracket(x:int|Q,even_order:int=22)->tuple[Q,Q]:
    """Alternating rational Taylor bracket for exp(-x), x in [0,1]."""
    x=exact(x)
    if not Q(0)<=x<=Q(1) or type(even_order) is not int or even_order<2 or even_order%2 or even_order>100:
        raise PascalTransportError("Use 0<=x<=1 and a positive even Taylor truncation")
    partial=sum(((-x)**j/Q(factorial(j)) for j in range(even_order+1)),Q(0))
    return partial-x**(even_order+1)/Q(factorial(even_order+1)),partial


def continuous_wait_survival_bracket(events:int,mean:int|Q,even_order:int=22)->tuple[Q,Q]:
    """Enclose P(T_events>t)=exp(-mean) sum_(k<events) mean^k/k!."""
    bounded(events)
    if events<1:
        raise PascalTransportError("At least one arrival required")
    mean=exact(mean)
    l,u=exp_minus_rational_bracket(mean,even_order)
    p=sum((mean**k/Q(factorial(k)) for k in range(events)),Q(0))
    return l*p,u*p


def binomial_poisson_total_variation_bound(trials:int,mean:int|Q)->Q:
    """TV(Bin(trials,mean/trials),Poi(mean)) <= mean^2/trials.

    Proof: TV(Bern(p),Poi(p))=p(1-e^-p) <= p^2,
    tensorize via independent maximal couplings and push forward by sum.
    """
    bounded(trials)
    mean=exact(mean)
    if trials<1 or not 0<=mean<=trials:
        raise PascalTransportError("Finite Bernoulli trials require p=mean/trials in [0,1]")
    return mean**2/Q(trials)


def dual_count_time_certificate(trials:int,events:int,mean:int|Q,even_order:int=22)->dict:
    """Rigorous rational comparison of discrete Pascal wait and Erlang limit.

    Here each discrete slot has size delta=t/trials and p=lambda*delta.
    Only mean=lambda*t is required to specify this fixed observation window.
    """
    bound=binomial_poisson_total_variation_bound(trials,mean)
    p=exact(mean)/Q(trials)
    actual=discrete_wait_survival(trials,events,p)
    low,high=continuous_wait_survival_bracket(events,mean,even_order)
    worst=max(abs(actual-low),abs(actual-high))
    return dict(discrete_survival=actual,continuous_lower=low,continuous_upper=high,
                tv_bound=bound,rigorous_comparison_pass=worst<=bound)


def count_by_time(event_times:Sequence[int|Q],time:int|Q)->int:
    """Deterministic count on a finite nondecreasing event-time source path."""
    times=tuple(exact(t) for t in event_times)
    t=exact(time)
    if t<0 or any(x<0 for x in times) or any(times[i]>times[i+1] for i in range(len(times)-1)):
        raise PascalTransportError("Ordered nonnegative actual event-time source required")
    return sum(x<=t for x in times)


def time_of_event(event_times:Sequence[int|Q],index:int)->Q:
    """Index starts at 1: generalized inverse of the counting function."""
    times=tuple(exact(t) for t in event_times)
    if type(index) is not int or index<1 or index>len(times):
        raise PascalTransportError("Requested event not in finite declared source history")
    if any(x<0 for x in times) or any(times[i]>times[i+1] for i in range(len(times)-1)):
        raise PascalTransportError("Nondecreasing nonnegative source path required")
    return times[index-1]


def count_time_adjunction(event_times:Sequence[int|Q],time:int|Q,index:int)->bool:
    """The pathwise theorem N(time)>=index iff T_index<=time.

    Check directly with independent count and indexed event access. Valid for
    nondecreasing paths, including simultaneous events; no Poisson assumption.
    """
    return (count_by_time(event_times,time)>=index)==(time_of_event(event_times,index)<=exact(time))


@dataclass(frozen=True)
class FractionalGammaSUCC:
    """Mathematical continuous positive convolution semigroup, not a physical event.

    For alpha>=0, lambda>0, the measure at alpha is Gamma(alpha,lambda)
    (delta_0 at alpha=0). Integer alpha counts Poisson arrival gaps;
    fractional alpha is an *analytic shape parameter*, not a half event.
    """
    shape:Q
    rate:Q=Q(1)

    def __post_init__(self)->None:
        object.__setattr__(self,'shape',exact(self.shape))
        object.__setattr__(self,'rate',exact(self.rate))
        if self.shape<0 or self.rate<=0:
            raise PascalTransportError("Gamma semigroup needs nonnegative shape and positive common rate")

    def compose(self,other:'FractionalGammaSUCC')->'FractionalGammaSUCC':
        if not isinstance(other,FractionalGammaSUCC) or self.rate!=other.rate:
            raise PascalTransportError("Cannot mix untransported source time scales/rates")
        return FractionalGammaSUCC(self.shape+other.shape,self.rate)

    def moment(self,n:int)->Q:
        """E[X^n] = alpha^(rising n) / lambda^n; n=0 returns 1."""
        bounded(n)
        out=Q(1)
        for j in range(n):
            out*=self.shape+j
        return out/self.rate**n

    def laplace_signature(self,u:int|Q)->tuple[Q,Q]:
        """Symbolic positive base^(shape), not float-evaluated."""
        u=exact(u)
        if u<0:
            raise PascalTransportError("Require u>=0 for probability Laplace control")
        return (self.rate/(self.rate+u),self.shape)


def gamma_succ_convolution_moment(a:FractionalGammaSUCC,b:FractionalGammaSUCC,n:int)->Q:
    """Pascal-Hopf convolution of gamma-source moments; fail on rate mismatch."""
    bounded(n)
    if a.rate!=b.rate:
        raise PascalTransportError("Gamma tensor source rates incompatible")
    return sum((Q(comb(n,k))*a.moment(k)*b.moment(n-k) for k in range(n+1)),Q(0))

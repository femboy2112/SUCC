"""A source-labelled prior and inflationary causal frontier for SUCC.

RESEARCH ONLY.  Exact finite probability laws, not physical cosmology, not
quantum mechanics, and not the original BBP phase orbit.  `theta` denotes
an independently specified binary symmetric transmission channel, NOT an
established identification with the Oily source's memory-retention rates.

Mathematical contract:
  * root Bernoulli prior and independent, source-labelled edge transitions;
  * a product-cylinder probability law on each finite expanding tree;
  * exact finite Bayes reconstruction from leaf observations;
  * separate FLRW analog and discrete source-clock controls;
  * Oily endpoint linear register energy tested as a DECLARED duplicated
    source carrier, not interpreted as a stochastic channel.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import log2


class PriorInflationError(ValueError):
    """Invalid source prior, channel, evidence, or expansion contract."""


def _fraction(value, name):
    if isinstance(value, bool):
        raise PriorInflationError(f"{name} cannot be boolean")
    try:
        return F(value)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        raise PriorInflationError(f"{name} must be finite rational") from e


def _unit(value, name):
    v = _fraction(value, name)
    if not F(0) <= v <= F(1):
        raise PriorInflationError(f"{name} must belong to [0,1]")
    return v


def _positive_int(value, name):
    if type(value) is not int or value < 1:
        raise PriorInflationError(f"{name} must be positive integer")
    return value


def _spin(x):
    if type(x) is not int or x not in (-1, 1):
        raise PriorInflationError("source spin must be exactly -1 or +1")
    return x


@dataclass(frozen=True)
class BinaryTreePrior:
    """Source law for root spin and independently transmitted descendants.

    A nonuniform root prior is allowed: geometry alone does not select a prior.
    A nonzero edge correlation is stipulated, never inferred from Oily.
    """

    branching: int
    theta: F
    root_plus: F = F(1, 2)
    source_id: str = "declared-binary-broadcast-control-v1"

    def __post_init__(self):
        _positive_int(self.branching, "branching")
        object.__setattr__(self, "theta", _unit(self.theta, "theta"))
        object.__setattr__(self, "root_plus", _unit(self.root_plus, "root_plus"))
        if not self.source_id or not isinstance(self.source_id, str):
            raise PriorInflationError("nonempty source label required")

    @property
    def p_same(self):
        return (1 + self.theta) / 2

    @property
    def p_flip(self):
        return (1 - self.theta) / 2

    def transition(self, parent: int, child: int) -> F:
        _spin(parent); _spin(child)
        return self.p_same if parent == child else self.p_flip

    def finite_cylinder(self, nodes: tuple[int, ...], depth: int) -> F:
        """Breadth-first complete b-ary tree through depth, exact probability.

        Includes root value as nodes[0]. This is an *event probability* of
        assigned states at ALL listed vertices, rather than a marginal leaf
        probability. One can sum over children to verify consistency.
        """
        if type(depth) is not int or depth < 0 or depth > 9:
            raise PriorInflationError("finite depth must be integer in [0,9]")
        count = sum(self.branching**k for k in range(depth + 1))
        if len(nodes) != count:
            raise PriorInflationError("source assignment does not match tree")
        for v in nodes: _spin(v)
        result = self.root_plus if nodes[0] == 1 else 1 - self.root_plus
        for i in range(1, count):
            parent = (i - 1) // self.branching
            result *= self.transition(nodes[parent], nodes[i])
        return result

    def _leaf_likelihood(self, leaf_signs: tuple[int, ...], depth: int):
        """For fixed boundary, P(boundary|node root=+/-), no fitting."""
        if depth == 0:
            x = _spin(leaf_signs[0])
            return (F(1), F(0)) if x == 1 else (F(0), F(1))
        span = self.branching ** (depth - 1)
        lp, lm = F(1), F(1)
        for k in range(self.branching):
            cp, cm = self._leaf_likelihood(
                leaf_signs[k * span: (k+1) * span], depth - 1
            )
            lp *= self.p_same * cp + self.p_flip * cm
            lm *= self.p_flip * cp + self.p_same * cm
        return lp, lm

    def leaf_likelihoods(self, leaves: tuple[int, ...], depth: int):
        if type(depth) is not int or depth < 0 or depth > 9:
            raise PriorInflationError("finite depth must be integer in [0,9]")
        if len(leaves) != self.branching ** depth:
            raise PriorInflationError("incorrect number of frontier observations")
        for x in leaves: _spin(x)
        return self._leaf_likelihood(leaves, depth)

    def posterior_root(self, leaves: tuple[int, ...], depth: int) -> F:
        """Bayes-optimal fair/biased root posterior using frontier ONLY.

        At depths when the specified evidence has probability zero, no
        conditional probability is defined; no fabricated selection.
        """
        lp, lm = self.leaf_likelihoods(leaves, depth)
        num = self.root_plus * lp
        den = num + (1-self.root_plus) * lm
        if den == 0:
            raise PriorInflationError("evidence impossible under declared source")
        return num / den

    def level_statistics(self, depth: int, max_leaves: int = 12):
        """Exact finite Bayes-accuracy and floating conditional MI (bits).

        Enumerates all boundaries only when finite observation budget allows.
        Fractions are exact; the decimal information uses logarithms.
        """
        if type(depth) is not int or depth < 0 or depth > 9:
            raise PriorInflationError("invalid depth")
        n = self.branching ** depth
        if n > max_leaves:
            raise PriorInflationError("exhaustive frontier exceeds budget")
        acc = F(0)
        info = 0.0
        for leaves in product((-1, 1), repeat=n):
            lp, lm = self.leaf_likelihoods(leaves, depth)
            plus, minus = self.root_plus*lp, (1-self.root_plus)*lm
            total = plus+minus
            acc += max(plus, minus)
            if total > 0:
                posterior = plus / total
                if posterior > 0:
                    info += float(plus) * log2(float(posterior/self.root_plus)) if self.root_plus else 0
                if posterior < 1:
                    info += float(minus)*log2(float((1-posterior)/(1-self.root_plus))) if self.root_plus < 1 else 0
        return {"depth": depth, "leaves": n, "accuracy_exact": acc, "mutual_info_bits": info}


def finite_inflation_scale(growth: int, n: int, end: int | None = None) -> int:
    """Discrete physical scale a_n=growth^min(n,end). Not a light speed."""
    _positive_int(growth, "growth")
    if growth == 1:
        raise PriorInflationError("growth must exceed one")
    if type(n) is not int or n < 0:
        raise PriorInflationError("time index must be nonnegative")
    if end is not None and (type(end) is not int or end < 0):
        raise PriorInflationError("inflation-end must be nonnegative integer")
    return growth ** min(n, end) if end is not None else growth**n

def discrete_conformal_budget(growth: int, n: int, end: int | None = None) -> F:
    """Declared unit-tick null budget sum 1/a_k, not continuum FLRW integral.

    For unending inflation, budget tends to growth/(growth-1). For a finite
    phase that stops at end, the budget subsequently grows without bound.
    """
    _positive_int(growth, "growth")
    if growth <= 1:
        raise PriorInflationError("growth must exceed 1")
    if type(n) is not int or n < 0 or n > 10000:
        raise PriorInflationError("invalid finite time")
    if end is not None and (type(end) is not int or end < 0):
        raise PriorInflationError("inflation-end must be nonnegative integer")
    q = F(1, growth)
    if end is None or n <= end:
        return (1-q**n)/(1-q)
    return (1-q**end)/(1-q) + (n-end)*q**end


def _two_by_two_mult(a, b):
    return (
        (a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]),
        (a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]),
    )


def oily_parameters(x):
    """Literal authenticated Oily u,v; NOT an observer channel theorem."""
    x = _unit(x, "Oily x")
    return x - x*x/2, x*x/2


def oily_matrix_power(x, n: int):
    """Exact M(x)^n, M=[[u,1],[0,v]]; n=0 is identity."""
    u, v = oily_parameters(x)
    if type(n) is not int or n < 0 or n > 10000:
        raise PriorInflationError("invalid power")
    if n == 0:
        return ((F(1),F(0)),(F(0),F(1)))
    # divided difference, including exact repeated-root collision u=v
    coupling = n*u**(n-1) if u == v else (u**n - v**n)/(u-v)
    return ((u**n, coupling), (F(0), v**n))


def linear_branch_energy(branching: int, n: int, x=F(1)) -> F:
    """Sum of squared Frobenius amplitudes over replicated linear carriers.

    A deliberately duplicated two-register signal, not a probability and
    NOT Kesten–Stigum reconstruction of the original signed BBP orbit.
    """
    _positive_int(branching, "branching")
    m = oily_matrix_power(x,n)
    return branching**n * sum(v*v for row in m for v in row)


def oily_critical_energy_closed(branching: int, n: int) -> F:
    _positive_int(branching,"branching")
    if type(n) is not int or n < 0:
        raise PriorInflationError("n must be nonnegative")
    return F(branching,4)**n * (2 + 4*n*n)


def ks_signal_to_noise(branching: int, theta) -> F:
    """Broadcast-tree signal/noise ratio b theta^2; separate from Oily M."""
    _positive_int(branching, "branching")
    theta = _unit(theta, "theta")
    return branching * theta * theta


def normalized_census_variance(branching: int, theta, depth: int) -> F:
    """Exact Var(Z_depth/(b theta)^depth |root), b-ary BSC broadcast.

    The signal estimator has mean equal to the root spin. It is *one*
    estimator; bounded variance above KS suffices for positive recovery.
    Below KS, formal result for symmetric binary trees comes from EKPS.
    """
    _positive_int(branching, "branching")
    theta = _unit(theta, "theta")
    if theta == 0:
        raise PriorInflationError("zero theta does not admit unbiased census")
    if type(depth) is not int or depth < 0 or depth > 1000:
        raise PriorInflationError("invalid depth")
    gain = branching*theta*theta
    return (1-theta*theta) * sum((gain**(-j) for j in range(1,depth+1)), F(0))


def correlated_remote_update(theta, observed: int) -> F:
    """P(remote bit = +1 | one distant correlated local bit observed).

    Source root uniform, two independent children given root, BSC(theta).
    Updating a posterior is not superluminal transmission to remote site.
    """
    theta = _unit(theta, "theta"); _spin(observed)
    return (1 + observed * theta*theta) / 2


def golden_lucas_scale(n: int) -> int:
    """Integer recursive shadow of Pisot inflation a_n=phi^n.

    L_n=phi^n+psi^n, psi=-1/phi. Integer L_n has recurrence
    L_(n+2)=L_(n+1)+L_n, with L0=2,L1=1. At n>=2 it grows.
    No spacetime metric or inflationary field equation is claimed here.
    """
    if type(n) is not int or n<0 or n>100000:
        raise PriorInflationError("nonnegative finite Lucas index required")
    a,b=2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def embedded_causal_tree(branching:int, depth:int, growth:int=2):
    """Exact comoving coordinates for a b-ary causal network with expansion.

    Level zero root is at chi=0. In each unit tick from level n to n+1,
    each of b children moves by offset (2k-b+1)*growth**(-n)/(2b), for
    k=0..b-1. This is strictly within the DECLARED discrete causal reach
    growth**(-n). It is NOT an isometric embedding of a full FLRW metric;
    the latter has a separate continuous null integral. Nodes retain distinct
    source labels even when coordinates coincide.
    """
    _positive_int(branching,'branching')
    _positive_int(growth,'growth')
    if growth<=1 or type(depth) is not int or depth<0 or depth>12:
        raise PriorInflationError('growth>=2 and finite depth 0..12 required')
    layers=[(F(0),)]
    for n in range(depth):
        old=layers[-1]
        if len(old)*branching>16000:
            raise PriorInflationError('declared finite embedding capacity exceeded')
        scale=growth**n
        new=tuple(parent+F(2*k-branching+1,2*branching*scale)
                  for parent in old for k in range(branching))
        layers.append(new)
    return tuple(layers)


def original_deflated_oily_L(x) -> F:
    """Literal original positive Oily rational L(x)=R(x)/(1-x)."""
    x=_unit(x,'Oily x')
    return 1/((2-x*x)*(x*x-2*x+2))


def oily_preobservation_unnormalized(x,a:int) -> F:
    """Bayesian PRE-observation weight x^a L(x); Z0 requires integration."""
    x=_unit(x,'Oily x')
    if type(a) is not int or a<0 or a>100000:
        raise PriorInflationError('finite nonnegative source time exponent required')
    return x**a * original_deflated_oily_L(x)


def oily_frontier_event_likelihood(x) -> F:
    """Declared admissible conditional sensor probability P(A|x)=1-x."""
    x=_unit(x,'Oily x')
    return 1-x


def oily_postobservation_unnormalized(x,a:int) -> F:
    """Bayes posterior kernel exactly x^a * authentic positive Oily R(x)."""
    return oily_preobservation_unnormalized(x,a)*oily_frontier_event_likelihood(x)


def uniform_L_event_probability(a:int)->F:
    """Exact benign control L(x)=1, prior Beta(a+1,1), event (1-x).

    P(A)=1/(a+2); posterior density Beta(a+1,2). This is NOT the
    authentic rational Oily L(x); it calibrates the source-asymptotic gate.
    """
    if type(a) is not int or a<0:
        raise PriorInflationError('nonnegative integer exponent required')
    return F(1,a+2)


def max_entropy_vacancy_double_imbalance(x) -> F:
    """Original max-entropy two-channel source: P(B=0)-P(B=2)=1-x.

    B is the number of active independent Bernoulli(x/2) microchannels.
    This is a signed expectation, NOT a fixed two-bit event probability.
    A literal event likelihood 1-x requires a further calibrated sensor.
    """
    x=_unit(x,'Oily x')
    p=x/2
    return (1-p)**2-p*p

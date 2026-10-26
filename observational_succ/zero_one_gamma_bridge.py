"""Zero/one successor charts, positive Euler defects and true BBP moment transport.

All finite numbers are exact Fraction intervals. Analytic domains:
  x>0 (real gamma/digamma chart), n>=1 (authenticated BBP source).
The Loewner inequalities and ratio monotonicity are classical integral proofs,
not established by finite tests. No claims about Weyl cancellation or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial


class GammaBridgeError(ValueError):
    """Wrong carrier, unsupported index, source, or insufficient precision."""


def q(value, positive=False):
    if type(value) not in (int, Q):
        raise GammaBridgeError("require exact rational, never float/bool")
    v = Q(value)
    if positive and v <= 0:
        raise GammaBridgeError("strictly positive rational chart required")
    return v


def idx(value, minimum=0, maximum=3000):
    if type(value) is not int or not minimum <= value <= maximum:
        raise GammaBridgeError("bounded integer index required")
    return value


@dataclass(frozen=True)
class RationalInterval:
    lower: Q
    upper: Q

    def __post_init__(self):
        if type(self.lower) is not Q or type(self.upper) is not Q or self.lower>self.upper:
            raise GammaBridgeError("ordered exact rational interval required")

    @property
    def width(self):
        return self.upper-self.lower

    def add(self, other):
        if not isinstance(other, RationalInterval):
            raise GammaBridgeError("common rational value chart required")
        return RationalInterval(self.lower+other.lower,self.upper+other.upper)

    def scale(self, value):
        a=q(value)
        lo,hi=a*self.lower,a*self.upper
        return RationalInterval(min(lo,hi),max(lo,hi))


def log_positive_interval(value, terms=20):
    """Exact artanh log enclosure for positive rational value.

    z=(x-1)/(x+1). Partial sum = 2 sum_{k=0}^{m-1} z^(2k+1)/(2k+1)
    and absolute tail <= 2|z|^(2m+1)/[(2m+1)(1-z^2)].
    """
    x=q(value,True)
    idx(terms,1,250)
    if x==1:
        return RationalInterval(Q(0),Q(0))
    z=(x-1)/(x+1)
    partial=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    tail=2*abs(z)**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return RationalInterval(partial-tail,partial+tail)


def logarithmic_successor_unit(origin, terms=20):
    """Exact unit successor, with its nonunit natural-log coordinate increment."""
    x=q(origin,True)
    ell=log_positive_interval((x+1)/x,terms)
    return {"origin":x,"additive_successor":Q(1),
            "multiplicative_ratio":(x+1)/x,
            "log_increment":ell,"normalized_log_unit":Q(1)}


def gamma_defect_interval(origin, terms=20):
    """delta_x = 1/x-log((x+1)/x), exact rational outward bracket."""
    x=q(origin,True)
    ell=log_positive_interval((x+1)/x,terms)
    return RationalInterval(1/x-ell.upper,1/x-ell.lower)


def generalized_defect_integer(power, origin):
    """delta_{r,x}=x^-r-int_0^1 (x+t)^-r dt, r>=2 exact."""
    idx(power,2,30)
    x=q(origin,True)
    integral=(x**(1-power)-(x+1)**(1-power))/Q(power-1)
    return x**(-power)-integral


@dataclass(frozen=True)
class GammaFieldCertificate:
    origin: Q
    cells: int
    logarithm_terms: int
    prefix: RationalInterval
    tail: RationalInterval
    total: RationalInterval


def gamma_field_certificate(origin, cells, logarithm_terms=20):
    """G(x)=log x-psi(x)=sum_{k>=0} delta_(x+k).

    Since W(t)=(1-t)C(t) with 1/2<=C<=1,
    1/[2u(u+1)]<=delta_u<=1/[u(u+1)] for all u>0.
    Sum over k>=N telescopes between 1/[2(x+N)] and 1/(x+N).
    """
    x=q(origin,True)
    idx(cells,0,1500)
    idx(logarithm_terms,1,250)
    prefix=RationalInterval(Q(0),Q(0))
    for k in range(cells):
        prefix=prefix.add(gamma_defect_interval(x+k,logarithm_terms))
    v=x+cells
    tail=RationalInterval(1/(2*v),1/v)
    return GammaFieldCertificate(x,cells,logarithm_terms,prefix,tail,prefix.add(tail))


def gamma_r_finite_bracket(power, origin, cells):
    """Certified rational shifted generalized Euler field for integer r>=2.

    E_r(x)=sum_{k>=0} [ (x+k)^-r - int_0^1(x+k+u)^-r du ]
          =HurwitzZeta(r,x)-x^(1-r)/(r-1).
    Convexity/decrease give telescoped remaining tail
        1/[2(x+N)^r] <= remainder <= 1/(x+N)^r.
    Finite results are exact Fraction; no zeta evaluator is imported.
    """
    idx(power,2,30)
    x=q(origin,True)
    idx(cells,0,1500)
    prefix=sum((generalized_defect_integer(power,x+k)
                for k in range(cells)),Q())
    v=x+cells
    return RationalInterval(prefix+1/(2*v**power),prefix+1/v**power)


def authentic_bbp_forcing(n):
    """The one original four-pole rational source from Coherent Main X."""
    idx(n,1,100_000)
    from .bbp_natural_carrier import exact_forcing
    return exact_forcing(n)


def bbp_polynomial(t):
    t=q(t)
    return (1-t)*(t*t+2)*(t*t+2*t+2)


def bbp_factor(t):
    t=q(t)
    return (t*t+2)*(t*t+2*t+2)


@dataclass(frozen=True)
class BridgeCellCertificate:
    n: int
    x: Q
    euler_defect: RationalInterval
    authentic_forcing: Q
    lower_ratio: Q
    upper_ratio: Q
    verified_with_rational_bounds: bool


def bbp_gamma_cell_certificate(n, terms=20):
    """Finite-scope exact interval check of universal analytic inequality.

       4 delta_(8n-7) <= true_r(n) <= 30 delta_(8n-7).
    The all-n theorem uses positive-kernel density comparison, not samples.
    """
    idx(n,1,100_000)
    x=Q(8*n-7)
    d=gamma_defect_interval(x,terms)
    source=authentic_bbp_forcing(n)
    if d.lower<=0:
        raise GammaBridgeError("increase logarithm precision to certify positive defect")
    lo=source/d.upper
    hi=source/d.lower
    if not (Q(4)<lo<=hi<Q(30)):
        raise GammaBridgeError("increase precision or audit the authentic BBP source")
    return BridgeCellCertificate(n,x,d,source,lo,hi,True)


def bbp_gamma_quadratic(coefficients,terms=35):
    """Finite exact gamma/BBP moment Gram quadratic comparison.

    m_k^Euler=delta_(8k+1), m_k^BBP=true_r(k+1).
    H_BBP between 4 H_Euler and 30 H_Euler in Loewner order.
    A finite interval computation checks a particular polynomial vector.
    """
    if not isinstance(coefficients,tuple) or not coefficients or len(coefficients)>8:
        raise GammaBridgeError("finite nonempty polynomial coefficient tuple required")
    c=tuple(q(v) for v in coefficients)
    if not any(c):
        raise GammaBridgeError("nonzero test polynomial required")
    idx(terms,1,250)
    source=Q(0)
    euler=RationalInterval(Q(0),Q(0))
    for i,a in enumerate(c):
        for j,b in enumerate(c):
            v=a*b
            if not v:continue
            source+=v*authentic_bbp_forcing(i+j+1)
            euler=euler.add(gamma_defect_interval(8*(i+j)+1,terms).scale(v))
    if not (source>0 and euler.lower>0 and 4*euler.upper<source<30*euler.lower):
        raise GammaBridgeError("insufficient interval precision or wrong source")
    return {"coefficients":c,"gamma_form":euler,"bbp_form":source,
            "pointwise_ratio_lower":Q(4),"pointwise_ratio_upper":Q(30),
            "finite_certificate":True}


@dataclass(frozen=True)
class SharedResolventCertificate:
    """A gamma-vacuum Neumann sum and positive outer bound on BBP pi."""
    depth: int
    gamma_resolvent: RationalInterval
    pi_outer: RationalInterval
    unseen_gamma_tail: RationalInterval


def shared_resolvent_certificate(depth,logarithm_terms=28):
    """Exact rational finite gamma-operator bounds and compared BBP value.

    Pi_gamma=sum_{k>=0}16^-k delta_(8k+1), Pi_BBP=sum 16^-k r(k+1).
    Pointwise 4W<=P<=30W gives 4Pi_gamma<=Pi_BBP<=30Pi_gamma.
    Gamma tail uses delta_(8k+1) positive/decreasing and geometric 16^-k.
    """
    N=idx(depth,0,350)
    idx(logarithm_terms,1,250)
    prefix=RationalInterval(Q(0),Q(0))
    for k in range(N):
        prefix=prefix.add(gamma_defect_interval(8*k+1,logarithm_terms).scale(Q(1,16**k)))
    x=8*N+1
    lo=Q(1,16**N)*Q(1,2*x*(x+1))
    hi=Q(16,15)*Q(1,16**N)*Q(1,x*(x+1))
    tail=RationalInterval(lo,hi)
    total=prefix.add(tail)
    if total.lower<=0:
        raise GammaBridgeError("increase logarithmic precision")
    return SharedResolventCertificate(N,total,RationalInterval(4*total.lower,30*total.upper),tail)


def beta_integer(a,b):
    """Beta(a,b) with positive integer arguments, exact rational factorial ratio."""
    idx(a,1,100_000)
    idx(b,1,300)
    numerator=Q(factorial(b-1))
    for j in range(b):
        numerator/=a+j
    return numerator


def solve_exact(rows,rhs):
    n=len(rhs)
    if not n or len(rows)!=n or any(len(row)!=n for row in rows):
        raise GammaBridgeError("positive-dimensional square system required")
    m=[[q(a) for a in row]+[q(b)] for row,b in zip(rows,rhs)]
    for k in range(n):
        pivot=next((j for j in range(k,n) if m[j][k]!=0),None)
        if pivot is None:
            raise GammaBridgeError("singular exact moment Gram")
        m[pivot],m[k]=m[k],m[pivot]
        d=m[k][k]
        m[k]=[a/d for a in m[k]]
        for j in range(n):
            if j==k:continue
            d=m[j][k]
            m[j]=[a-d*b for a,b in zip(m[j],m[k])]
    return tuple(row[-1] for row in m)


@dataclass(frozen=True)
class FiniteJetMomentMutant:
    """POSITIVE alternative kernel matching first K authentic moments and M jets.

    P_e(t)=P(t)+epsilon*t*(1-t)^(M+1)*Q_K(t^8).
    Q_K is the monic orthogonal polynomial for measure t(1-t)^(M+1)dt
    and coordinates y=t^8. K exact moments are unchanged, endpoint
    derivatives through degree M are unchanged, and the next moment differs.
    """
    matched_moments: int
    matched_endpoint_jets: int
    polynomial_coefficients: tuple[Q,...]
    epsilon: Q
    first_unmatched_moment_shift: Q
    positivity_factor_floor: Q
    source_polynomial_at_16: Q
    resolvent_shift_bracket: RationalInterval

    def kernel_at(self,t):
        t=q(t)
        if not 0<=t<=1:
            raise GammaBridgeError("mutation positive only on the ordered unit carrier")
        f=sum((c*t**(8*i) for i,c in enumerate(self.polynomial_coefficients)),Q())
        return bbp_polynomial(t)+self.epsilon*t*(1-t)**(self.matched_endpoint_jets+1)*f

    def moment_shift(self,index):
        idx(index,0,100_000)
        m=self.matched_endpoint_jets
        return self.epsilon*sum((c*beta_integer(8*(index+i)+2,m+2)
                                 for i,c in enumerate(self.polynomial_coefficients)),Q())


def finite_jet_moment_mutant(matched_moments,matched_endpoint_jets):
    """Countermodel: simultaneous finite zero/one jets and BBP moments not rigid.

    The positive source perturbation has amplitude small enough that its
    bracket Q(t)+epsilon*t*(1-t)^M*poly(t^8) >=3 for t in [0,1].
    """
    K=idx(matched_moments,1,8)
    M=idx(matched_endpoint_jets,1,12)
    gram=[[beta_integer(8*(i+j)+2,M+2) for j in range(K)] for i in range(K)]
    rhs=[-beta_integer(8*(i+K)+2,M+2) for i in range(K)]
    coeffs=solve_exact(gram,rhs)+(Q(1),)
    epsilon=Q(1)/(1+sum((abs(c) for c in coeffs),Q()))
    first=epsilon*sum((coeffs[i]*beta_integer(8*(K+i)+2,M+2)
                       for i in range(K+1)),Q())
    norm=epsilon*sum((coeffs[i]*coeffs[j]*beta_integer(8*(i+j)+2,M+2)
                      for i in range(K+1) for j in range(K+1)),Q())
    if first<=0 or first!=norm:
        raise ArithmeticError("finite moment counterfeit failed its independent norm check")
    source_at_16=sum((c*Q(16)**i for i,c in enumerate(coeffs)),Q())
    if source_at_16<=0:
        raise ArithmeticError("orthogonal polynomial must be positive above [0,1]")
    # Exact positive-resolvent identity from polynomial orthogonality:
    # int w Q/(1-y/16) = int w Q^2/(1-y/16) / Q(16).
    # Thus 1 <= (1-y/16)^-1 <= 16/15 gives rational two-sided bounds.
    shift=RationalInterval(first/source_at_16,Q(16,15)*first/source_at_16)
    out=FiniteJetMomentMutant(K,M,coeffs,epsilon,first,Q(3),source_at_16,shift)
    if any(out.moment_shift(j)!=0 for j in range(K)):
        raise ArithmeticError("orthogonal mutant unexpectedly changes authenticated prefix")
    return out

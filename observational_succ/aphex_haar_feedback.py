"""Aphex-shaped SUCC observer feedback, NOT the undocumented song's intended law.

The 1999 track-title equation has no authoritative variable semantics.
Here D=predicted-minus-observed centered signed probe; F=authenticated
centered source feature; g=M^{-1}=g_reference+beta is a chosen response gain.
This is exact deterministic least squares, not a proof of pi normality.
"""
from dataclasses import dataclass
from fractions import Fraction

Q = Fraction
ZERO = Q(0)
ONE = Q(1)


@dataclass(frozen=True)
class ProbeFit:
    n: int
    source_mean: Q
    complement_mean: Q
    real_sign_mean: Q
    source_variance: Q
    covariance: Q
    coefficient: Q
    residual_energy: Q


def _signed(seq):
    a = tuple(Q(x) for x in seq)
    if not a or any(x not in (-ONE, ONE) for x in a):
        raise ValueError("must supply a nonempty +/-1 sign stream")
    return a


def fit_sign_coupling(source_signs, complement_signs):
    """Exact normalized signed covariance of two chronological parity streams.

    Returns beta*=Cov(a,b)/Var(a).  Fails closed if a is constant.
    Only finite observed streams are fitted; no asymptotic rate is inferred.
    """
    a,b=_signed(source_signs),_signed(complement_signs)
    if len(a)!=len(b):
        raise ValueError("equal lengths required")
    N=len(a)
    ma=sum(a,ZERO)/N
    mb=sum(b,ZERO)/N
    x=[v-ma for v in a]
    y=[v-mb for v in b]
    V=sum((z*z for z in x),ZERO)/N
    C=sum((z*t for z,t in zip(x,y)),ZERO)/N
    if not V:
        raise ValueError("no identifiable local parity mode: source variance zero")
    beta=C/V
    loss=sum(((v-beta*u)**2 for u,v in zip(x,y)),ZERO)/(2*N)
    assert (sum((u*v for u,v in zip(a,b)),ZERO)/N)==ma*mb+C
    assert loss==Q(1,2)*(sum((v*v for v in y),ZERO)/N-C*C/V)
    return ProbeFit(N,ma,mb,ma*mb+C,V,C,beta,loss)


def aphex_step(fit: ProbeFit, beta, step_size):
    """One *calibrated*, offline batch descent step on exactly measured data.

    E(beta)=1/(2N)*sum((y_n-beta*x_n)^2); grad=V*beta-C.
    beta_new=beta-eta*grad, with 0<eta<2/V a strict descent
    whenever grad != 0.  Not a causal streaming proof or ergodic estimate.
    """
    beta,eta=Q(beta),Q(step_size)
    V,C=fit.source_variance,fit.covariance
    if not 0<eta<2/V:
        raise ValueError("stability interval: 0 < eta < 2/Var(source)")
    grad=V*beta-C
    next_beta=beta-eta*grad
    def loss(t): return fit.residual_energy+V*(t-fit.coefficient)**2/2
    improvement=loss(beta)-loss(next_beta)
    assert improvement==eta*(1-eta*V/2)*grad*grad
    assert improvement>=0
    return next_beta,grad,improvement


def original_parity_probe(states, prime):
    """Adapter to authenticated SourceParity records from the original BBP core.

    Uses real completed source sign, NOT the incorrect 'Weyl h=8' shortcut.
    Requires a valid p-primary coordinate with exponent one at every time.
    """
    if not states:
        raise ValueError("empty source window")
    a=[]
    b=[]
    for s in states:
        if not any(q==prime and m==prime for q,m,_ in s.coordinates):
            raise ValueError("selected source prime missing or p^2 present")
        av=Q((-1)**s.local(prime))
        real=Q((-1)**s.completed_parity)
        a.append(av)
        b.append(av*real)
    return fit_sign_coupling(a,b)


def calibrate_gain(beta, reference=ONE):
    """Chosen positive inverse response gain; fail closed rather than fake mass.

    Note: inverse gain is a *defined observer parameter*, not inferred
    physical mass, p-adic phase, or novel BBP arithmetic.
    """
    beta,reference=Q(beta),Q(reference)
    if reference+beta<=0:
        raise ValueError("inverse-response gain must be positive")
    return reference+beta

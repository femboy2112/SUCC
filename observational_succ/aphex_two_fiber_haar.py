"""Two-fiber Haar identification of the Aphex/BBP signed parity coupling.

This is finite exact algebra on source-labeled signs, not source-selected pi
normality. The fitted beta requires real complementary observations and
therefore must NEVER be represented as a source-only prediction.
"""
from dataclasses import dataclass
from fractions import Fraction

from observational_succ.aphex_haar_feedback import fit_sign_coupling

Q = Fraction
Z = Q(0)
O = Q(1)


def signed(values):
    out = tuple(Q(v) for v in values)
    if not out or any(v not in (-O, O) for v in out):
        raise ValueError("nonempty sequence of exact +/-1 observations required")
    return out


@dataclass(frozen=True)
class TwoFiberHaar:
    n: int
    n_plus: int
    n_minus: int
    a_mean: Q
    b_mean: Q
    parity_mean: Q
    complement_given_plus: Q
    complement_given_minus: Q
    haar_detail: Q
    common_response: Q
    source_error: Q
    conditional_residual_energy: Q


def two_fiber_haar(source_signs, complement_signs):
    """Proved exact identities for any observed +/-1 streams.

    a=selected source (e.g. genuine prime parity), b=the complete
    complementary real/CRT sign. The real parity observable is a*b.

    beta* = (E[b|a=+1] - E[b|a=-1])/2
    E[a*b] = beta* + E[a]*(E[b|a=+1]+E[b|a=-1])/2
    hence |E[a*b]-beta*| <= |E[a]|, with sharp constant 1.

    The input b is NOT generated from a alone. This is source-conditioned
    observation, not a theorem that the true BBP orbit is Haar.
    """
    a, b = signed(source_signs), signed(complement_signs)
    if len(a) != len(b):
        raise ValueError("source and complement must have equal length")
    plus = [b[i] for i,x in enumerate(a) if x == 1]
    minus = [b[i] for i,x in enumerate(a) if x == -1]
    if not plus or not minus:
        raise ValueError("both source-sign fibers must be populated")
    n = len(a)
    mu_plus = sum(plus, Z) / len(plus)
    mu_minus = sum(minus, Z) / len(minus)
    detail = (mu_plus-mu_minus)/2
    common = (mu_plus+mu_minus)/2
    ma = sum(a,Z)/n
    mb = sum(b,Z)/n
    ms = sum((x*y for x,y in zip(a,b)), Z)/n
    regression = fit_sign_coupling(a,b)
    assert regression.coefficient == detail
    assert regression.real_sign_mean == ms
    assert regression.complement_mean == mb
    assert regression.covariance == (1-ma*ma)*detail
    assert mb == common+ma*detail
    assert ms == detail+ma*common
    assert abs(ms-detail) <= abs(ma)
    # Exact minimum L2 residual with intercept; low residual IS NOT Haar.
    min_loss = ((Q(len(plus),n)*(1-mu_plus*mu_plus))
                +Q(len(minus),n)*(1-mu_minus*mu_minus))/2
    assert min_loss == regression.residual_energy
    return TwoFiberHaar(
        n,len(plus),len(minus),ma,mb,ms,
        mu_plus,mu_minus,detail,common,abs(ms-detail),min_loss
    )


def real_parity_bound(result: TwoFiberHaar, imported_prime_mean_bound: Q):
    """Finite bound |real parity mean| <= |Haar detail|+prime-mean bound.

    BEC may provide a conditional bound on the genuine local source mean,
    but importing one NEVER establishes decay of the detail itself.
    """
    b = Q(imported_prime_mean_bound)
    if b < 0 or abs(result.a_mean) > b:
        raise ValueError("prime marginal bound must be sound and nonnegative")
    assert abs(result.parity_mean) <= abs(result.haar_detail) + b
    return abs(result.haar_detail)+b


def perturbation_budget(source_signs, original_complement, perturbed_complement):
    """Sharp L1-stability of calibrated Haar detail at fixed prime labels.

    For eps = average |b-bhat| and m=mean(a), both fibers populated,
    |beta(b)-beta(bhat)| <= eps/(1-|m|).

    Perturbations are finite arbitrary rational readouts, not required to be
    +/-1. This is useful for *paid* approximate probe/tail readouts.
    """
    a = signed(source_signs)
    b = tuple(Q(v) for v in original_complement)
    bh = tuple(Q(v) for v in perturbed_complement)
    if len(b)!=len(a) or len(bh)!=len(a):
        raise ValueError("all streams must have equal length")
    if any(v not in (-O,O) for v in b):
        raise ValueError("exact original complement must be +/-1")
    n=len(a)
    p = [i for i,x in enumerate(a) if x==1]
    m = [i for i,x in enumerate(a) if x==-1]
    if not p or not m:
        raise ValueError("both source sign fibers required")
    mu_b_plus=sum((b[i] for i in p),Z)/len(p)
    mu_b_minus=sum((b[i] for i in m),Z)/len(m)
    mu_h_plus=sum((bh[i] for i in p),Z)/len(p)
    mu_h_minus=sum((bh[i] for i in m),Z)/len(m)
    diff=abs((mu_h_plus-mu_h_minus-mu_b_plus+mu_b_minus)/2)
    eps=sum((abs(x-y) for x,y in zip(b,bh)),Z)/n
    imbalance=abs(sum(a,Z)/n)
    bound=eps/(1-imbalance)
    assert diff<=bound
    return diff,bound,eps


def original_bbp_two_fiber(states, p):
    """Adapter: full authenticated real/prime parity ledger of #572.

    Fails on missing or higher-power p-coordinate; uses real completed digit
    parity to construct b=a*s, so DOES NOT infer b independently of real data.
    """
    if not states:
        raise ValueError("empty source epoch")
    a=[]
    b=[]
    for s in states:
        if not any(q == p and m == p for q,m,_ in s.coordinates):
            raise ValueError("required simple-pole genuine prime absent")
        v = Q((-1)**s.local(p))
        a.append(v)
        b.append(v*Q((-1)**s.completed_parity))
    return two_fiber_haar(a,b)

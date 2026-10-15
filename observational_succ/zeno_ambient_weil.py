"""Source-typed Zeno completion and authentic prime/Gamma ambient boundary calculus.

This is an exact finite mathematical experiment library, not a physical
supertask, an all-place operator intertwiner, or a proof of RH.

The new source-specific theorem is the *nonvanishing boundary commutator*:
for the CENTERED expanding window P_a=1_[-a,a] on L2(R), true prime
b=log(2), T_b f(x)=f(x+b), C_0 f=k*f, k(t)=1/(2 cosh(t/2)), a>=b,
  ||[P_a T_b P_a, P_a C_0 P_a]|| >= 2 log(2)/5 > 11/40.
As a grows, P_a tends strongly to I and the compressed commutator tends
strongly to zero, but NOT in norm. The norm witness follows the MOVING
left boundary; for a fixed left endpoint [0,L] the strong-limit claim would
be FALSE since P_[0,L] tends instead to the half-line projection.
This is boundary leakage, not nonflat full-source holonomy.

The finite rational matrix controls sample the actual Carleman kernel at
steps 2 log2 (the true prime-power n=4); they do NOT replace the continuum.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt, factorial
from typing import Iterable


class ZenoError(ValueError):
    """Invalid exact source, observer scope or completion declaration."""


def exact(x) -> Q:
    if type(x) is not int and not isinstance(x, Q):
        raise ZenoError("Exact integer or Fraction required, not float/complex/bool")
    return Q(x)


def nat(n: int, high: int = 4096) -> int:
    if type(n) is not int or not 0 <= n <= high:
        raise ZenoError(f"Exact nonnegative stage <= {high} required")
    return n


@dataclass(frozen=True)
class SourceFrame:
    source_id: str
    epoch: int
    basis_id: str
    carrier: str

    def __post_init__(self):
        if (not all(type(x) is str and x for x in
                    (self.source_id, self.basis_id, self.carrier)) or
                type(self.epoch) is not int or self.epoch < 0):
            raise ZenoError("A nonempty source/basis/carrier and exact epoch are required")

    def match(self, other: "SourceFrame") -> bool:
        return self == other


@dataclass(frozen=True)
class ZenoStage:
    stage: int
    position: Q
    tail_upper: Q
    endpoint: Q
    source: str

    def __post_init__(self):
        nat(self.stage)
        if (not all(isinstance(v, Q) for v in (self.position,self.tail_upper,self.endpoint)) or
                type(self.source) is not str or not self.source):
            raise ZenoError("Exact Frac endpoint and nonempty source are required")
        if self.tail_upper < 0 or abs(self.endpoint - self.position) > self.tail_upper:
            raise ZenoError("Invalid tail certificate")


def dichotomy(n: int) -> ZenoStage:
    """All finite Zeno stages miss 1, with exact geometric tail 2^-n."""
    nat(n)
    tail = Q(1, 2**n)
    return ZenoStage(n, Q(1) - tail, tail, Q(1), "formal_dyadic_succ")


def achilles(n: int, gap=Q(9, 10), runner=1, tortoise=Q(1, 10)) -> dict:
    """Finite pursuit catches only at its mathematically appended endpoint."""
    nat(n)
    gap, runner, tortoise = exact(gap), exact(runner), exact(tortoise)
    if gap <= 0 or runner <= tortoise or tortoise < 0:
        raise ZenoError("Positive gap, runner>tortoise>=0 required")
    r = tortoise / runner
    total = gap / (runner - tortoise)
    elapsed = total * (1 - r**n)
    remaining = total * r**n
    assert elapsed + remaining == total
    return {"stage": n, "ratio": r, "elapsed": elapsed,
            "time_tail_exact": remaining, "total_catch_time": total,
            "source": "constant_velocity_pursuit_mathematical_model",
            "physical_omega_executed": False}



def harmonic_nonzeno_block(k: int) -> dict:
    """Vanishing increments 1/n need not yield a finite global endpoint.

    Group integers [2^j+1,2^(j+1)] into k blocks. Each contributes
    >=1/2, so H_(2^k)>=1+k/2. An infinite-sum claim must provide a
    SUMMABLE error budget, not merely individual increments->0.
    """
    nat(k,12)
    N=2**k
    h=sum((Q(1,n) for n in range(1,N+1)),Q())
    floor=Q(1)+Q(k,2)
    if h<floor:raise ArithmeticError("harmonic block proof inconsistent")
    return {"k":k,"finite_N":N,"sum":h,"lower":floor,
            "terms_tend_to_zero":True,"series_converges":False}


def stadium_frame_demo(speed:Q, t:Q) -> dict:
    """The moving-rows stadium is a source/frame calibration problem.

    Two bodies move at +v and -v with respect to a fixed clock; their
    relative displacement is 2*v*t. Failure to label the common time
    and coordinate frame creates an apparent factor-of-two puzzle.
    """
    speed,t=exact(speed),exact(t)
    if speed<=0 or t<0:raise ZenoError("Positive rational velocity and nonnegative time required")
    a=speed*t;b=-speed*t
    return {"clock":"one common time t", "A_velocity":speed,
            "B_velocity":-speed,"A_position":a,"B_position":b,
            "relative_displacement":a-b,"relative_speed":2*speed,
            "source":"Galilean labelled carrier, not actual relativistic spacetime"}

def sqrt2_completion_chart(n: int) -> dict:
    """Finite rational intervals converge to sqrt2 in real completion, NOT Q."""
    nat(n, 512)
    d = 1 << n
    a = isqrt(2*d*d)
    lo, hi = Q(a, d), Q(a+1, d)
    assert lo*lo < 2 < hi*hi
    return {"stage": n, "lower": lo, "upper": hi,
            "width": Q(1, d), "source_carrier": "Q",
            "completion_carrier": "R", "realization_in_original_Q": False}



def zeno_rational_pole(n: int) -> dict:
    """Continuous Q->Q rational law f(q)=1/(q²-2) has NO continuous R extension.

    Dyadic q_n approaches sqrt2 from below, while |f(q_n)|>2^n/3
    for n>=1. This is a strict finite-to-global morphism obstruction:
    completion of arguments does not extend unbounded/nonuniform maps.
    """
    if type(n) is not int or not 1 <= n <= 256:
        raise ZenoError("Finite rational pole certificate stage 1..256 required")
    c=sqrt2_completion_chart(n)
    q=c["lower"]
    v=Q(1)/(q*q-2)
    lower=Q(2**n,3)
    if not -v > lower:
        raise ArithmeticError("Failed rational pole divergence certificate")
    return {"stage":n,"argument":q,"rational_pole_value":v,
            "absolute_value_strictly_greater_than":lower,
            "original_source":"Q with f(q)=1/(q²-2)",
            "no_continuous_extension_to_R":True}


def lipschitz_zeno_transport(n:int,slope:Q,offset:Q) -> dict:
    """Fully supported example of transporting a Lipschitz arrow to completion.

    The affine rational map f(x)=a*x+b has Lipschitz constant |a|.
    Source path 1-2^-n approaches 1, and f endpoints inherit EXACT
    error |a|*2^-n. Unlike the rational-pole countermodel, a sound
    extension exists on all R.
    """
    x=dichotomy(n)
    slope,offset=exact(slope),exact(offset)
    return {"stage":n,"finite_value":slope*x.position+offset,
            "completed_value":slope+offset,
            "exact_error":abs(slope)*x.tail_upper,
            "Lipschitz_constant":abs(slope),
            "unique_completion_extension":True,
            "physical_actualization_claimed":False}

def _mul_poly(a: tuple[Q,...], b: tuple[Q,...]) -> tuple[Q,...]:
    out = [Q(0)] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def evaluate_poly(coeffs: Iterable[Q], x) -> Q:
    x = exact(x)
    ans = Q(0)
    for c in reversed(tuple(coeffs)):
        ans = ans*x + exact(c)
    return ans


def derivative_poly(coeffs: Iterable[Q]) -> tuple[Q,...]:
    a = tuple(coeffs)
    return tuple(exact(a[i])*i for i in range(1,len(a)))


def arrow_derivative_alias(sample_times: tuple[Q,...], pivot: Q) -> dict:
    """Two polynomial motions agree at ALL supplied times, different velocity."""
    if (type(sample_times) is not tuple or not 1 <= len(sample_times) <= 16):
        raise ZenoError("Exact finite nonempty sample tuple required")
    times = tuple(exact(t) for t in sample_times)
    pivot = exact(pivot)
    if len(set(times)) != len(times) or pivot not in times:
        raise ZenoError("Distinct rational times including pivot required")
    coeffs = (Q(1),)
    for t in times:
        coeffs = _mul_poly(coeffs, (-t, Q(1)))
    derivative_at_pivot = evaluate_poly(derivative_poly(coeffs),pivot)
    if not derivative_at_pivot:
        raise ArithmeticError("Distinct sample locations must have nonzero derivative")
    normalized = tuple(v/derivative_at_pivot for v in coeffs)
    assert all(evaluate_poly(normalized,t)==0 for t in times)
    assert evaluate_poly(derivative_poly(normalized), pivot)==1
    return {"times":times, "pivot":pivot, "zero_motion":(Q(0),),
            "indistinguishable_motion":normalized,
            "zero_velocity":Q(0), "other_velocity":Q(1),
            "source":"exact_finite_polynomial_kinematics"}


def noncommuting_limit_order(n: int, m: int) -> dict:
    nat(n,4096);nat(m,4096)
    if n==0 or m==0:raise ZenoError("positive indices required")
    return {"entry":Q(n,n+m),
            "first_n_then_m":Q(1), "first_m_then_n":Q(0),
            "joint_uniform_limit_exists":False}


def log2_enclosure(terms:int=12) -> tuple[Q,Q]:
    """Arctanh(1/3) exact rational enclosure for the true log2."""
    if type(terms) is not int or not 1 <= terms <= 80:
        raise ZenoError("Positive Taylor term count <=80 required")
    z = Q(1,3)
    lo = sum((2*z**(2*k+1)/Q(2*k+1) for k in range(terms)), Q())
    first = 2*z**(2*terms+1)/Q(2*terms+1)
    upper = lo + first/(1-z*z)
    return lo, upper



def prime_log_enclosure(p:int,terms:int=12) -> tuple[Q,Q]:
    """Pure rational enclosure of log genuine prime using dyadic transport.

    p=2^m*u, 1<=u<2. Compute log p=m*log2+log u using
    2atanh((u-1)/(u+1)), whose ratio z is <=1/3. The source checks
    actual primality, not just the algebra of a composite dilation.
    """
    if type(p) is not int or p<2 or p>100000 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise ZenoError("Primitive authentic prime p in [2,100000] required")
    l2,h2=log2_enclosure(terms)
    m=p.bit_length()-1
    u=Q(p,2**m)
    z=(u-1)/(u+1)
    v=sum((2*z**(2*k+1)/Q(2*k+1) for k in range(terms)),Q())
    remainder=2*z**(2*terms+1)/Q(2*terms+1)/(1-z*z)
    return m*l2+v,m*h2+v+remainder


def primitive_prime_boundary_certificate(p:int,a:Q,terms:int=12) -> dict:
    """Source-faithful family of C0/prime-p continuum boundary obstructions.

    For EVERY true prime p, a>=log p, the norm of the compressed
    commutator on L2([-a,a]) is >= p log p/(p^2+1)>0, whereas
    centered-window strong convergence is zero as a grows.
    Primality is the original Euler-source eligibility rule; composites
    still act as geometric dilations but may not masquerade as a prime.
    """
    a=exact(a)
    lo,hi=prime_log_enclosure(p,terms)
    if a<hi:raise ZenoError("Window must extend at least one genuine log p shift")
    c=Q(p,p*p+1)
    return {"prime":p,"source":"authentic_Euler_primitive_prime_and_single_real_Gamma_C0",
            "window_halfwidth":a,"logp_lower":lo,"logp_upper":hi,
            "commutator_norm_lower":c*lo,
            "global_commutation":True,"centered_strong_limit_zero":True,
            "operator_norm_limit_zero":False,"Weil_positive_proved":False}

def true_carlemann_sample(offset_steps: int) -> Q:
    """Original C0(2k log2)=2^|k|/(2^(2|k|)+1), all exact."""
    if type(offset_steps) is not int or abs(offset_steps) > 256:
        raise ZenoError("Exact bounded integer sample offset required")
    k=abs(offset_steps)
    return Q(2**k,2**(2*k)+1)


def source_boundary_certificate(window_halfwidth: Q, terms: int=12) -> dict:
    """All-test continuum commutator lower bound for a>=log2.

    Use the CENTERED P_a=1_[-a,a], for which P_a -> I strongly.
    Translate its interval unitarily into [0,2a] FOR THE NORM PROOF ONLY:
    take f=1_[0,b]/sqrt(b), b=log2, and restrict [S,K]f to [0,b].
    Here K=C0 with true kernel k(t)=1/(2cosh(t/2)). For a>=b,
    [S,K]f(x)=integral_0^b k(x+b-y)f(y)dy >= k(2b)*sqrt(b),
    so ||[S,K]|| >= b*k(2b)=2 log2/5 >11/40.
    The witness follows x=-a at each a; thus it does not contradict
    strong convergence to zero on FIXED L2(R) vectors. An expanding
    [0,L] instead would converge to the half-line, NOT I.
    No completed Weil sign conclusion follows.
    """
    a = exact(window_halfwidth)
    lo,hi=log2_enclosure(terms)
    if a < hi:
        raise ZenoError("Can only certify windows a >= upper enclosure of log2")
    lower=Q(2,5)*lo
    if lower <= Q(11,40):
        raise ZenoError("Use at least two arctanh terms for strict 11/40 witness")
    return {"source":"authentic_prime_2_and_original_Carleman_Gamma_layer",
            "window_halfwidth":a,"prime_shift":"log2",
            "log2_lower":lo,"log2_upper":hi,
            "commutator_norm_lower":lower,
            "strict_rational_witness":Q(11,40),
            "valid_on_whole_continuum_L2_window":True,
            "true_full_carrier_commutes":True,
            "centered_windows_expand_to_whole_R":True,
            "compressed_commutator_strong_to_zero":True,
            "compressed_commutator_norm_to_zero":False,
            "proved_full_Weil_sign":False}


def _matmul(a:tuple[tuple[Q,...],...],b:tuple[tuple[Q,...],...]):
    n=len(a)
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(n)),Q())
                       for j in range(n)) for i in range(n))


def source_discrete_Carleman_commutator(size:int) -> dict:
    """Exactly sampled original C0 at true log4_SUCC on a finite window.

    Sampling is only a diagnostic of continuum boundary leakage; NOT an
    exact discretization of an integral operator nor a signed Weil Gram.
    """
    if type(size) is not int or not 2<=size<=32:
        raise ZenoError("Finite exact window dimension 2..32 required")
    K=tuple(tuple(true_carlemann_sample(i-j) for j in range(size))
            for i in range(size))
    S=tuple(tuple(Q(int(j==i+1)) for j in range(size)) for i in range(size))
    sk,ks=_matmul(S,K),_matmul(K,S)
    defect=tuple(tuple(sk[i][j]-ks[i][j] for j in range(size)) for i in range(size))
    for i in range(size):
        for j in range(size):
            expected=(K[i+1][0] if j==0 and i<size-1 else Q(0))
            if i==size-1 and j>0:expected=-K[size-1][j-1]
            if defect[i][j]!=expected:
                raise ArithmeticError("Nontrivial source projection identity failed")
    return {"size":size,"shift":"log4 genuine 2-power jet",
            "Carleman_matrix":K,"boundary_commutator":defect,
            "first_boundary_entry":defect[0][0],
            "underlying_uncompressed_operators_commute":True,
            "valid_Weil_signed_lower_bound":False}




def centered_discrete_zeno_commutator(radius:int) -> dict:
    """Exact strong-vs-norm escape with actual sampled C0 and true log4 SUCC.

    On ell²(Z), K is convolution by summable positive-definite source
    sequence k_j=2^|j|/(2^(2|j|)+1). S is a unit shift, so SK=KS.
    Compress to [-N,N]. Then ||[P_NSP_N,P_NKP_N]||>=k_1=2/5,
    while ||[... ] e_0||=k_(N+1)<2^(-N-1). For every fixed
    finite-support v, norm->0 by the absolute-summability tail, hence
    strong->0 by uniform boundedness. This is a discrete *analytic*
    theorem on the sampled C0 kernel; it does NOT realize full Weil.
    """
    if type(radius) is not int or not 1 <= radius <= 15:
        raise ZenoError("Exact compressed discrete Zeno radius 1..15 required")
    size=2*radius+1
    A=source_discrete_Carleman_commutator(size)
    D=A['boundary_commutator'];center=radius
    col=tuple(row[center] for row in D)
    decay=true_carlemann_sample(radius+1)
    if not(all(v==0 for v in col[:-1]) and col[-1]==-decay):
        raise ArithmeticError("Central source vector failed edge-only leakage proof")
    bound=Q(1,2**(radius+1))
    if not 0<decay<bound:
        raise ArithmeticError("True sampled Gamma source must have geometric tail")
    return {"radius":radius,"window_size":size,
            "full_source_commutes":True,
            "central_vector_commutator_norm":decay,
            "central_vector_decay_upper":bound,
            "norm_lower_for_all_radii":Q(2,5),
            "operator_norm_limit_zero":False,
            "strong_limit_on_fixed_vectors_zero":True,
            "full_completed_Weil_sign_proved":False}

def source_sampled_parity_poles(size:int) -> dict:
    """Even/odd reflection blocks of authentic Carleman and pole samples.

    Coordinates x_j=2(j-mid)log2, odd window length. Then true
    c=cosh(x/2) and s=sinh(x/2) have RATIONAL samples. The reflection
    R fixes c and negates s; the true C0 Toeplitz sample commutes with R.
    This is a finite lattice calibration of the ACTUAL completed rank-two
    pole, not a continuum H0^1 sign certificate or an Euler factor at 4.
    """
    if type(size) is not int or size<3 or size>31 or size%2!=1:
        raise ZenoError("Odd exact window size 3..31 required")
    mid=size//2
    pos=tuple(j-mid for j in range(size))
    power=lambda j:Q(2)**j
    c=tuple((power(j)+power(-j))/2 for j in pos)
    s=tuple((power(j)-power(-j))/2 for j in pos)
    K=source_discrete_Carleman_commutator(size)['Carleman_matrix']
    if not all(c[i]==c[size-1-i] and s[i]==-s[size-1-i] for i in range(size)):
        raise ArithmeticError("Original pole parity/source mismatch")
    if not all(K[i][j]==K[size-1-i][size-1-j] for i in range(size)
               for j in range(size)):
        raise ArithmeticError("Original Gamma reflection symmetry failed")
    e=tuple(Q(j*j) for j in pos)
    o=tuple(Q(j) for j in pos)
    dot=lambda u,v:sum((a*b for a,b in zip(u,v)),Q())
    cross=sum((e[i]*K[i][j]*o[j] for i in range(size) for j in range(size)),Q())
    if cross!=0 or dot(e,s)!=0 or dot(o,c)!=0:
        raise ArithmeticError("Parity transport must be exact on source grid")
    return {"sample_size":size,"log_step":"log4 genuine 2-power chart",
            "cosh":c,"sinh":s,"even_test":e,"odd_test":o,
            "odd_even_Gamma_cross":cross,
            "positive_even_pole_example":2*dot(e,c)**2,
            "negative_odd_pole_example":-2*dot(o,s)**2,
            "total_Weil_Q_signed":True,"global_sign_proved":False}

def gamma_H1_signed_error(J:int) -> dict:
    """Import PR71's genuine completed-Gamma signed H1-form remainder bound."""
    nat(J,100000)
    A=Q(2*J)+Q(1,2)
    eps=max(Q(9,8*A*A)+Q(1,2*A**3),
            Q(1,2*A*A)+Q(2,A**3))
    return {"Gamma_rungs":J,"A":A,"epsilon":eps,
            "form_domain":"H0^1(-a,a)",
            "source":"parent_PR71_original_completed_Weil",
            "signed_QJ_proved_positive":False,
            "positivity_requires_separate_all_test_bound":True}



def odd_pole_sharp_H1_bounds(a:Q, last_term:int=12) -> dict:
    """Exact rational enclosure of the source's sharp odd-pole H0^1 dual norm.

    Let L(v)=integral_(-a)^a v(x)sinh(x/2) dx, ||v||_H=||v'||_2.
    The Riesz vector is 4[(sinh(a/2)/a)x-sinh(x/2)]; hence
       ||L||^2 = 4(a+sinh a) - 16(cosh a-1)/a
                 = sum_(n>=2) 4(n-1)a^(2n+1)/((n+1)(2n+1)!).
    This series has nonnegative terms. For 0<a<=2 consecutive term
    ratio <= a²/28 <=1/7, bounding the tail by a geometric series.
    The negative original pole term is -2 |L(v)|²; neither positive
    even-pole nor Gamma/prime/contact terms have been omitted by claim.
    """
    a=exact(a)
    if not 0<a<=2 or type(last_term) is not int or not 2<=last_term<=100:
        raise ZenoError("Odd-pole power series requires rational 0<a<=2 and n>=2")
    def term(n):
        return Q(4*(n-1),(n+1)*factorial(2*n+1))*a**(2*n+1)
    lower=sum((term(n) for n in range(2,last_term+1)),Q())
    upper=lower+term(last_term+1)/(1-a*a/Q(28))
    if not 0<lower<upper:
        raise ArithmeticError("Failure of source positive-series tail")
    return {"window_halfwidth":a,"last_summed_n":last_term,
            "odd_pole_dual_norm_squared_lower":lower,
            "odd_pole_dual_norm_squared_upper":upper,
            "negative_rank_one_form_H1_budget_upper":2*upper,
            "exact_source":"g(x)=sinh(x/2), original completed Weil odd pole",
            "true_positive_Weil_Q_proved":False}


def odd_pole_first_moment_null_bound(a:Q) -> dict:
    """An actual full-test source-negative-pole bound on codimension one.

    For v in H0^1(-a,a) with integral x*v(x)=0, 0<a<=1,
    |sinh(x/2)-x/2| <= |x|^3 cosh(a/2)/48,
    ||v||_2<=a||v'||_2, cosh(a/2)<=(1-a²/8)^-1.
    Consequently 2|<v,sinh(x/2)>|² <=
       a^9/[4032*(1-a²/8)^2] ||v'||².
    This is an exact all-test inequality for ONE negative term, not the
    full completed Weil form. The suppressed term is O(a^9) vs O(a^5).
    """
    a=exact(a)
    if not 0<a<=1:
        raise ZenoError("Rational first-moment pole bound requires 0<a<=1")
    b=a**9/(Q(4032)*(1-a*a/Q(8))**2)
    return {"window_halfwidth":a,"codimension":1,
            "moment_constraint":"integral_-a^a x v(x) dx = 0",
            "negative_odd_pole_H1_bound":b,
            "entire_infinite_dimensional_moment_null_subspace":True,
            "source":"original completed Weil rank-one odd pole",
            "complete_Weil_sign_proved":False}

def hidden_negative_witness(horizon:int) -> dict:
    """Arbitrary finite matrix prefix misses a negative self-adjoint direction."""
    nat(horizon,100000)
    return {"checked_prefix":horizon,"negative_coordinate":horizon+1,
            "operator":"I-2P_(horizon+1)",
            "coincides_with_I_on_prefix":True,
            "negative_Rayleigh":Q(-1),"full_Weil_source":False}


@dataclass(frozen=True)
class LawEdge:
    source: str
    target: str
    law: str
    status: str
    proof_family: str
    assumptions: tuple[str,...]

    def __post_init__(self):
        if any(type(s) is not str or not s for s in
               (self.source,self.target,self.law,self.status,self.proof_family)):
            raise ZenoError("Complete type/law/provenance annotation required")
        if self.status not in ("PROVED_LOCAL","CLASSICAL","CONDITIONAL","UNVERIFIED","REFUTED"):
            raise ZenoError("No untyped status promotion")
        if type(self.assumptions) is not tuple:
            raise ZenoError("Assumptions must be an immutable tuple")


def model_shape_graph() -> tuple[LawEdge,...]:
    """An explicit graph of prerequisites; no conjectural edge can certify RH."""
    return (
      LawEdge("finite_succ","Cauchy_profile","summable tail with declared metric", "CLASSICAL","analysis",("complete normed target",)),
      LawEdge("Cauchy_profile","completed_model","Cauchy completion universal property","CLASSICAL","topology",("metric completion",)),
      LawEdge("lipschitz_arrow","completion_transport","uniformly continuous map extends to complete target","CLASSICAL","functional analysis",("uniform continuity and complete target",)),
      LawEdge("pointwise_arrow","completion_transport","any continuous map extends without uniform continuity","REFUTED","rational pole countermodel",("uniform continuity absent",)),
      LawEdge("completed_model","original_carrier_actualized","completion-to-source surjection","CONDITIONAL","VOYAGER",("source closed/image realizable",)),
      LawEdge("finite_reports","inverse_limit","projective compatibility","CLASSICAL","VOYAGER",("finite-discrete report diagram",)),
      LawEdge("inverse_limit","original_carrier_actualized","source-image closedness","CONDITIONAL","VOYAGER",("compact original source and continuity",)),
      LawEdge("holomorphic_germ","analytic_continuation","source identity on open connected overlap","CLASSICAL","complex analysis",("connected domain and holomorphicity",)),
      LawEdge("prime_Euler_source","signed_Weil","real Gamma, half-density, poles, Euler identification","CLASSICAL","Suzuki/Weil",("C_c^infty domain",)),
      LawEdge("signed_Weil","global_PSD","true source all-test lower bound", "UNVERIFIED","RH-hard",("all intervals and source-matched domain",)),
      LawEdge("source_dilations","ambient_Gamma","canonical half-density and Carleman","CLASSICAL","PR86",("L2 real carrier, true p",)),
      LawEdge("ambient_Gamma","boundary_leakage","compressed prime and Gamma commutator","PROVED_LOCAL","this research",("a>=log2",)),
      LawEdge("authentic_prime_p","boundary_leakage","p log(p)/(p²+1) continuum boundary obstruction","PROVED_LOCAL","this research",("a>=log p",)),
      LawEdge("boundary_leakage","global_PSD","boundary commutator alone fixes sign","REFUTED","source-sign firewall",("full signed pole/contact still present",)),
      LawEdge("pointwise_approximants","uniform_operator_limit","pointwise->norm without conditions","REFUTED","Zeno",("uniform norm/tightness missing",)),
      LawEdge("source_Gamma_ladder","signed_Weil","uniform signed H1 approximate identification","CLASSICAL","PR71",("authentic source",)),
      LawEdge("moment_null_test","negative_pole_budget","source Taylor cancellation and Poincare","PROVED_LOCAL","this research",("0<a<=1, int x*v=0",)),
    )


def model_proof_path(start: str,target: str, edges:tuple[LawEdge,...]|None=None,
                     assumptions:tuple[str,...]=()) -> dict:
    """Do not follow CONDITIONAL/MISSING/REFUTED edges, even if graph connected."""
    if edges is None: edges=model_shape_graph()
    if type(assumptions) is not tuple or any(type(s) is not str for s in assumptions):
        raise ZenoError("Explicit assumptions required")
    queue=[(start, ())]
    visited={start}
    while queue:
        node,path=queue.pop(0)
        if node==target:
            if target=="global_PSD":
                return {"status":"UNVERIFIED_OR_BLOCKED","RH_proved":False}
            return {"status":"PROVED_WITH_DECLARED_PREMISES","path":path,
                    "premises":tuple(sorted({a for e in path for a in e.assumptions})),
                    "RH_proved":False}
        for edge in edges:
            if edge.source!=node or edge.target in visited:
                continue
            authorized=edge.status in ("CLASSICAL","PROVED_LOCAL")
            if authorized:
                visited.add(edge.target)
                queue.append((edge.target,path+(edge,)))
    return {"status":"UNVERIFIED_OR_BLOCKED","start":start,"target":target,
            "conditional_requests_not_discharge":True,"RH_proved":False}


def verdict_receipt() -> dict:
    d=dichotomy(12)
    a=achilles(8)
    h=harmonic_nonzeno_block(8)
    std=stadium_frame_demo(Q(3,2),Q(4,3))
    rt=sqrt2_completion_chart(16)
    rational_pole=zeno_rational_pole(12)
    fun=lipschitz_zeno_transport(12,Q(7,3),Q(-2))
    alias=arrow_derivative_alias((Q(-1),Q(0),Q(1)),Q(0))
    boundary=source_boundary_certificate(Q(1),20)
    prime3=primitive_prime_boundary_certificate(3,Q(2),20)
    matrix=source_discrete_Carleman_commutator(5)
    discrete_zeno=centered_discrete_zeno_commutator(10)
    gamma=gamma_H1_signed_error(64)
    parity=source_sampled_parity_poles(5)
    pole=odd_pole_sharp_H1_bounds(Q(1,2),10)
    moment=odd_pole_first_moment_null_bound(Q(1,2))
    return {"scope":"FORMAL_ZENO_AND_TRUE_PRIME2_CARLEMAN_BOUNDARY",
            "source_parent":"2feb678f9d29c2b5d520b084be62cde328a8941f",
            "dichotomy":{"stage":12,"position":str(d.position),"tail":str(d.tail_upper)},
            "achilles":{"stage":8,"elapsed":str(a['elapsed']),"tail":str(a['time_tail_exact']),"catch":str(a['total_catch_time'])},
            "plurality":{"k":8,"harmonic_prefix":str(h['sum']),"lower":str(h['lower']),"convergent":False},
            "stadium":{"a":str(std['A_position']),"b":str(std['B_position']),"relative":str(std['relative_displacement'])},
            "sqrt2":{"stage":16,"lower":str(rt['lower']),"upper":str(rt['upper']),"original_rational_source":False},
            "nonuniform_map":{"stage":12,"value":str(rational_pole['rational_pole_value']),"strict_magnitude_lower":str(rational_pole['absolute_value_strictly_greater_than'])},
            "uniform_map":{"stage":12,"finite_value":str(fun['finite_value']),"completion":str(fun['completed_value']),"exact_tail":str(fun['exact_error'])},
            "arrow":{"sample_agreement":all(evaluate_poly(alias['indistinguishable_motion'],t)==0 for t in alias['times']),
                     "velocity_gap":str(alias['other_velocity']-alias['zero_velocity'])},
            "prime3":{"source_primitive":3,"norm_lower":str(prime3['commutator_norm_lower'])},
            "boundary":{"strict_norm_lower":str(boundary['strict_rational_witness']),
                        "certified_lower":str(boundary['commutator_norm_lower']),
                        "exact_log2_interval":[str(boundary['log2_lower']),str(boundary['log2_upper'])],
                        "strong_limit_zero":True,"norm_limit_zero":False},
            "true_prime_power_matrix":{"size":5,"first_boundary_entry":str(matrix['first_boundary_entry']),
                                       "rightmost_negative":str(matrix['boundary_commutator'][-1][-1])},
            "discrete_centered_limit":{"radius":10,"fixed_center_decay":str(discrete_zeno['central_vector_commutator_norm']),
                                       "upper":str(discrete_zeno['central_vector_decay_upper']),
                                       "norm_lower":str(discrete_zeno['norm_lower_for_all_radii'])},
            "signed_gamma_H1":{"J":64,"epsilon":str(gamma['epsilon']),"proved_sign":False},
            "parity":{"grid":5,"signed_odd":str(parity['negative_odd_pole_example']),"even_odd_cross":str(parity['odd_even_Gamma_cross'])},
            "source_pole":{"a":"1/2","sharp_dual_norm_squared_upper":str(pole['odd_pole_dual_norm_squared_upper']),
                           "moment_null_negative_budget":str(moment['negative_odd_pole_H1_bound']),
                           "full_signed_Weil_PSD":False},
            "graph":{"nodes":len({e.source for e in model_shape_graph()}|{e.target for e in model_shape_graph()}),
                     "edges":len(model_shape_graph()),
                     "RH_reachable":model_proof_path('prime_Euler_source','global_PSD')['status']},
            "PHYSICAL_ACTUALIZATION":False,"RH_PROVED":False,
            "academic_novelty_independently_established":False}

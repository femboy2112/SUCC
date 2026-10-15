"""APOLLO PRIME-ACTIVE: certified support-measure domains for the TRUE Weil form.

The source is the SHA-checked original completed zeta Suzuki/Weil module.
The analytic inequalities and Hilbert-feature domain contract are proved in
research/2026-10-15/APOLLO_PRIME_ACTIVE_DOMAIN_CERTIFICATION.md.

Exact Fraction functions CHECK analytical hypotheses/budgets; tests do NOT
establish universal quantifiers by exhaustively enumerating vectors.
No nontrivial zero positions, fitted covariance, general Weil sign, or RH proof.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

from .apollo_derivative_jets import _source
from .one_object_transport import OneObjectError, _fraction
from .completed_weil_transport import von_mangoldt_labels


class PrimeDomainError(OneObjectError):
    """An actual source, compact support, or rational error gate failed."""


SOURCE_WEIGHT_UPPERS = (
    (2, 2, F(1, 2)),
    (3, 3, F(2, 3)),
    (4, 2, F(3, 8)),
    (5, 5, F(3, 4)),
    (7, 7, F(3, 4)),
)
FIRST_HALF = F(1, 2)
FIRST_SPARSE_MEASURE = F(1, 32)
ALL_FIVE_HALF = F(1)
ALL_FIVE_SPARSE_MEASURE = F(1, 16384)


def _proof_source():
    src = _source()  # verifies original Suzuki Git blob before ANY certificate
    if src.AUTHENTIC_TAPE != ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2)):
        raise PrimeDomainError("Original first-prime Weil tape is not canonical")
    if not src.contact_iv().hi < F(43,8):
        raise PrimeDomainError("Source Gamma/contact bound C_inf<43/8 absent")
    if not src.log2_iv().lo > F(2,3):
        raise PrimeDomainError("Original strict rational log2>2/3 absent")
    if not src.log_iv(3).lo > F(1):
        raise PrimeDomainError("Original first-prime interval must exclude n=3")
    if not src.log_iv(8).lo > F(2):
        raise PrimeDomainError("Original all-five interval must exclude n>=8")
    return src


def _upper_weight(src, n: int, p: int, bound: F):
    if src.real_prime_power(n) != p:
        raise PrimeDomainError("Attempt to admit fake or wrong primitive arithmetic")
    interval = src.log_iv(p) * src.sqrt_inverse(n)
    if not interval.lo > 0 or not interval.hi < bound:
        raise PrimeDomainError("Original source upper bound insufficient")
    return interval


def gamma_sixteen_fraction() -> F:
    """First 16 genuine Gamma/OU spectral masses beta_j=4/(4j+1)."""
    return sum((F(4, 4*j+1) for j in range(16)), F())


def dyadic_gamma_4096_lower() -> F:
    """Exact rational lower for true sum(j<4096) 4/(4j+1), no 4096-F sum.

    Write S_4096=S_16+sum_{r=4}^{11} sum_{j=2^r}^{2^(r+1)-1}1/(j+1/4).
    Each block >=log((2^(r+1)+1/4)/(2^r+1/4))
               >log(2)-1/(4*2^r) >2/3-1/(4*2^r).
    Verified log2 bound comes from source. All terms EXACT Fraction.
    """
    return (gamma_sixteen_fraction()+8*F(2,3)
            -sum((F(1,4*2**k) for k in range(4,12)), F()))


def _support_measure(m: int | F, limit: F) -> F:
    if type(m) not in (int, F):
        raise PrimeDomainError("Support bound must be a typed exact int/Fraction")
    amount = F(m)
    if not 0 < amount <= limit:
        raise PrimeDomainError("Declared measurable support budget outside proved domain")
    return amount


@dataclass(frozen=True)
class SparseWeilDomain:
    ambient_halfwidth: F
    support_measure_upper: F
    gamma_mode_count: int
    uniform_weil_l2_floor: F
    strict_rational_lower: F
    active_prime_labels: tuple[int,...]
    source: str = "SHA_PINNED_AUTHENTIC_COMPLETED_WEIL_ZETA"
    conditional_on_measured_support: bool = True
    all_tests_in_domain: bool = True
    h01_test_domain_extension_by_continuity: bool = True
    bounded_operator_on_all_L2_claimed: bool = False
    full_ambient_weil_positivity_proved: bool = False
    RH_proved: bool = False


def first_prime_sparse_domain(measure_upper: int | F = FIRST_SPARSE_MEASURE) -> SparseWeilDomain:
    """At a=1/2 (true p=2 ON), all compact-smooth tests on any E of |E|<=1/32.

    For arbitrary f supported in E:
      Gamma_j(f) >= (beta_j-m)||f||²,
      -C_inf||f||² >-43/8||f||²,
      -2w2 Re<T_log2 f,f> >-1||f||²,
      negative pole >-m/4||f||² (sinh(1/4)<1/3).
    For 16 genuine Gamma modes the exact lower is
      S16 -16m -43/8 -1 -m/4 >1/10
    even at m=1/32. All omitted Gamma modes positive.
    E is a DECLARED support set, not computed from an arbitrary function.
    """
    src = _proof_source()
    _upper_weight(src, 2, 2, F(1,2))
    m = _support_measure(measure_upper, FIRST_SPARSE_MEASURE)
    margin = gamma_sixteen_fraction() - 16*m - F(43,8) - 1 - m/4
    if margin <= F(1,10):
        raise ArithmeticError("Source sparse p=2 gamma domination not certified")
    return SparseWeilDomain(FIRST_HALF,m,16,F(1,10),margin,(2,))


def prime_two_pair_packet_domain() -> dict:
    """ACTUAL two-packet LINEAR DOMAIN E=U union(U+log2), at a=1/2.

    U=(-7/16,-7/16+1/64). Its translation by the exact true b=log2
    lies inside (-1/2,1/2), with intervals disjoint. For every smooth
    f=f0+f1 on these two packets, translated overlap obeys
        |<T_log2 f,f>|<=||f||²/2.
    The original sign becomes Q_zeta(f)>(3/5)||f||².
    The true prime overlap can be nonzero, e.g. f1(x)=f0(x-log2).
    """
    src = _proof_source()
    w = _upper_weight(src,2,2,F(1,2))
    b = src.log_iv(2)
    length=F(1,64)
    left=F(-7,16)
    if not F(-1,2)<left<left+length < F(0):
        raise ArithmeticError("Bad first source packet")
    if not F(0)<left+b.lo or not left+length+b.hi < F(1,2):
        raise ArithmeticError("Translated authentic n=2 packet exits first window")
    if not b.lo>length:
        raise ArithmeticError("Genuine shift not disjoint from old packet")
    m=2*length
    margin=gamma_sixteen_fraction()-16*m-F(43,8)-F(1,2)-m/4
    if not margin>F(3,5):
        raise ArithmeticError("True prime-overlap packet source margin lost")
    return {"halfwidth":FIRST_HALF,"base_U":(left,left+length),
            "right_U":"base_U + genuine log(2) exactly",
            "right_U_endpoint_intervals":((left+b.lo,left+b.hi),
                                           (left+length+b.lo,left+length+b.hi)),
            "actual_prime_shift_interval":(b.lo,b.hi),
            "actual_prime_weight_interval":(w.lo,w.hi),
            "union_measure":m,"Gamma_rungs":16,
            "all_test_Q_over_L2_strict_rational_lower":margin,
            "uniform_weil_L2_lower":F(3,5),
            "exact_prime_overlap_upper_ratio":F(1,2),
            "nonzero_prime_transfer_possible":True,
            "valid_for_every_complex_Cc_infinity_test_on_fixed_E":True,
            "PR107_ambient_operator":"authentic G_a on L2_zero(-1/2,1/2)",
            "PR107_comparison_metric":"Neumann K=V*V, not identity",
            "PR107_original_low_short_sign_proved":False,"RH_proved":False}


def full_five_source_a_one_sparse_domain(
        measure_upper: int | F = ALL_FIVE_SPARSE_MEASURE) -> SparseWeilDomain:
    """Every true test on every E⊂(-a,a), 0<a<=1, with |E|<=1/16384.

    At a=1, genuine active prime powers exactly 2,3,4,5,7; n=6
    is not a source and n>=8 has log n>=log8>2.
    The weights have SHA-certified strict upper total 73/24.
    Gamma S4096 > exact dyadic lower from log2>2/3;
      Gamma_j >= (beta_j-m)||f||², j<4096.
    Negative pole <=2m||f||² since sinh(a/2)<1 for a<=1.
    Therefore source bound
      S4096_lower - 4096m -43/8 -2(73/24) -2m > 1/2
    for all m<=1/16384. TRUE source, not a source-free sign fit.
    """
    src = _proof_source()
    for n,p,upper in SOURCE_WEIGHT_UPPERS:
        _upper_weight(src,n,p,upper)
    if tuple((n,p) for n,p in von_mangoldt_labels(7)) != tuple(
            (n,p) for n,p,_ in SOURCE_WEIGHT_UPPERS):
        raise PrimeDomainError("Original active source cutoff changed")
    m = _support_measure(measure_upper, ALL_FIVE_SPARSE_MEASURE)
    sum_upper=sum((limit for _n,_p,limit in SOURCE_WEIGHT_UPPERS),F())
    if sum_upper != F(73,24):
        raise ArithmeticError("Source coefficient upper budget invalid")
    margin=(dyadic_gamma_4096_lower()-4096*m-F(43,8)
            -2*sum_upper-2*m)
    if not margin>F(1,2):
        raise ArithmeticError("Five authentic place sparse bound failed")
    return SparseWeilDomain(ALL_FIVE_HALF,m,4096,F(1,2),margin,
                            (2,3,4,5,7))


def any_five_prime_activation_pair(n: int, length: F = F(1,32768)) -> dict:
    """Exact SOURCE-CERTIFIED paired packet domain crossing any of 5 jets.

    At a=1, U=(-1+delta,-1+2delta), E=U union(U+log n)
    where n ∈{2,3,4,5,7}, delta=1/32768. Both packets are
    inside (-1,1) and are pairwise disjoint. All other authentic
    active shifts have |log m-log n|>delta and cannot couple them.
    Only the n shift contributes a NONZERO POSSIBLE prime overlap.
    For f∈Cc∞(E), |<T_log n f,f>|<=||f||²/2.
    The source margin >5, stronger than the general a<=1 sparse bound.
    """
    if type(n) is not int or n not in (2,3,4,5,7):
        raise PrimeDomainError("Only genuine active original prime-power packet")
    if type(length) is not F or not 0<length<=F(1,32768):
        raise PrimeDomainError("Source packet requires positive exact tiny width")
    src=_proof_source()
    labels=tuple((j,p) for j,p,_ in SOURCE_WEIGHT_UPPERS)
    b=src.log_iv(n)
    origin=-1+length
    if not b.lo>length or origin+2*length+b.hi>=1:
        raise PrimeDomainError("Authentic translated source interval exits a=1")
    for other,_p in labels:
        if other==n:continue
        otherlog=src.log_iv(other)
        separated=(b.lo-otherlog.hi>length or
                   otherlog.lo-b.hi>length)
        if not separated:
            raise PrimeDomainError("Different prime waves overlap at selected packet budget")
    weight_upper=next(u for j,p,u in SOURCE_WEIGHT_UPPERS if j==n)
    weight=_upper_weight(src,n,src.real_prime_power(n),weight_upper)
    m=2*length
    lower=(dyadic_gamma_4096_lower()-4096*m-F(43,8)
           -weight_upper-2*m)
    if not lower>5:
        raise ArithmeticError("Exactly one genuine prime coupled packet not certified")
    return {"active_prime_power":n,"original_primitive_prime":src.real_prime_power(n),
            "base_U":(origin,origin+length),
            "translated_U":"base_U + genuine log(n)",
            "translated_endpoint_intervals":((origin+b.lo,origin+b.hi),
                                              (origin+length+b.lo,origin+length+b.hi)),
            "true_shift_interval":(b.lo,b.hi),
            "true_half_density_weight_interval":(weight.lo,weight.hi),
            "only_matching_prime_overlap":n,
            "all_other_prime_transfer_zero":True,
            "L2_pairwise_overlap_ratio_upper":F(1,2),
            "support_measure_upper":m,"Gamma_rungs":4096,
            "true_source_Weil_L2_lower":F(5),
            "strict_exact_margin":lower,
            "source_derived_Hilbert_contraction_on_linear_test_domain":True,
            "point_kernel_Gram_positive_on_all_of_minus1_to1":False,
            "RH_proved":False}


def exact_packet_overlap_bump(length: F, exponent: int = 4) -> dict:
    """Independent EXACT beta integral for one true translated-packet witness.

    f0(x)=t^m(delta-t)^m, t=x-left, on U; f1(x)=f0(x-log n)
    on U+log n, with zero elsewhere. This polynomial is C^(m-1), not
    Cc∞; source theorem applies to *smooth* approximants as well.
    Two-packet L2 norm²=2 E and 〈T_log n f,f〉=E,
    where E=delta^(4m+1)*(2m)!²/(4m+1)!.
    No irrational coordinates or floating integrals enter this identity.
    """
    if type(length) is not F or length<=0 or length>F(1,64):
        raise PrimeDomainError("Exact positive packet length<=1/64")
    if type(exponent) is not int or not 4<=exponent<=12:
        raise PrimeDomainError("C^3-or-better exact bump exponent 4..12")
    m=exponent
    energy=length**(4*m+1)*F(factorial(2*m)**2,factorial(4*m+1))
    return {"packet_length":length,"polynomial_degree":2*m,
            "one_packet_exact_L2":energy,
            "two_packet_exact_L2":2*energy,
            "one_prime_translated_overlap":energy,
            "relative_prime_overlap":F(1,2),
            "finite_polynomial_is_Cc_infinity":False,
            "smooth_equal_translate_witness_exists":True,
            "RH_proved":False}


def synthetic_sparse_budget(J: int, m: F, contact_upper: F,
                            prime_budget: F, pole_budget: F) -> dict:
    """HOSTILE control: pure algebra can certify fake source only as SYNTHETIC.

    Never returns an original-source theorem. A mutant contact, coefficient,
    or missing Gamma rung must NOT pass source authentication.
    """
    if type(J) is not int or not 1<=J<=16:
        raise PrimeDomainError("Synthetic finite-rung budget 1..16")
    for v in (m,contact_upper,prime_budget,pole_budget):
        if type(v) is not F or v<0:
            raise PrimeDomainError("Exact nonnegative rational synthetic controls")
    gamma=sum((F(4,4*j+1) for j in range(J)),F())-J*m
    lower=gamma-contact_upper-prime_budget-pole_budget
    return {"synthetic":True,"original_source_authenticated":False,
            "candidate_lower":lower,"candidate_positive":lower>0,
            "RH_proved":False}



def isolated_prime_sixteen_packet(n: int, length: F = F(1,128)) -> dict:
    """Better a=1 domain: ONE source jet active on its translated packets.

    For each n in genuine 2,3,4,5,7, E=U union(U+log n),
    U=(-1+delta,-1+2delta), 0<delta<=1/128.
    The intervals lie strictly inside (-1,1), and all other true
    prime-power log shifts differ from log n by >delta.
    Only n's compressed translation survives on E with norm<=1/2
    in the REAL part, giving -w_n||f||². All real Gamma rungs
    other than first 16 remain PSD; first 16 give S16-16|E|.
    C_inf<43/8; w_n<3/4; negative sinh pole<=2|E|.
    Exact rational margin:
         S16 - 16*(2delta) -43/8-3/4-2*(2delta) >1/2
    even at delta=1/128.
    The source-defined contraction exists on Cc∞(E), but not on all
    Suzuki tests in (-1,1). THIS IS NOT RH.
    """
    if type(n) is not int or n not in (2,3,4,5,7):
        raise PrimeDomainError("Genuine original five-jet source required")
    if type(length) is not F or not F()<length<=F(1,128):
        raise PrimeDomainError("Finite exact packet delta<=1/128 required")
    src=_proof_source()
    b=src.log_iv(n)
    left=-1+length
    if not b.lo>length or not left+length+b.hi<1:
        raise PrimeDomainError("Original source packets do not fit (-1,1)")
    for other,p,ub in SOURCE_WEIGHT_UPPERS:
        if other==n:continue
        bo=src.log_iv(other)
        if not (b.lo-bo.hi>length or bo.lo-b.hi>length):
            raise PrimeDomainError("Other prime clock not rigorously separated")
    p=src.real_prime_power(n)
    exact_ub=next(w for j,q,w in SOURCE_WEIGHT_UPPERS if j==n)
    w=_upper_weight(src,n,p,exact_ub)
    if exact_ub>F(3,4):
        raise PrimeDomainError("Original prime upper budget not available")
    m=2*length
    lower=gamma_sixteen_fraction()-16*m-F(43,8)-F(3,4)-2*m
    if not lower>F(1,2):
        raise ArithmeticError("Sixteen-rung isolated-prime source sign failed")
    return {"active_original_prime_power":n,
            "primitive_prime":p,
            "Gamma_modes":16,
            "halfwidth":F(1),
            "base_U":(left,left+length),
            "right_U":"base_U + exact source log(n)",
            "log_interval":(b.lo,b.hi),
            "original_weight_interval":(w.lo,w.hi),
            "isolated_wavefront":True,
            "other_four_prime_overlaps_exactly_zero":True,
            "support_measure_upper":m,
            "half_shift_overlap_norm_ratio":F(1,2),
            "source_signed_Weil_L2_lower":F(1,2),
            "strict_rational_margin":lower,
            "source_positive_Hilbert_contraction_exists_on_CcE":True,
            "full_ambient_G_a_positive":False,
            "RH_proved":False}



def source_support_union_gate(halfwidth: F,
                              component_upper_measures: tuple[F,...]) -> dict:
    """Exact source-indexed GLUING budget for multiple admissible supports.

    For a=1/2 or any a<=1 the corresponding verified universal bound
    survives a union if Σ component measure upper bounds <= source budget.
    This is a SUFFICIENT condition by subadditivity of Lebesgue measure.
    A rejected sum is UNVERIFIED, NOT an original zeta negative witness.
    """
    if type(halfwidth) is not F or halfwidth not in (F(1,2),F(1)):
        raise PrimeDomainError("Only authenticated a=1/2 or a<=1 budget chart")
    if (type(component_upper_measures) is not tuple
            or not 1<=len(component_upper_measures)<=32
            or any(type(m) is not F or m<=0 for m in component_upper_measures)):
        raise PrimeDomainError("Nonempty tuple of exact positive measure upper bounds")
    total=sum(component_upper_measures,F())
    if halfwidth==F(1,2):
        cert=first_prime_sparse_domain(total)
    else:
        cert=full_five_source_a_one_sparse_domain(total)
    return {"chart_halfwidth":halfwidth,
            "component_bounds":component_upper_measures,
            "union_bound":total,
            "all_cross_terms_covered_by_source_budget":True,
            "source_certified_signed_Weil_L2_floor":cert.uniform_weil_l2_floor,
            "componentwise_positivity_alone_would_be_insufficient":True,
            "original_Weil_global_sign_proved":False,
            "RH_proved":False}


def prime_packet_low_moment_rank(n: int = 2, rank: int = 30) -> dict:
    """Exact rational low-moment separation WITHIN one p=2 packet.

    Distinct rational sample points in the first packet form a Vandermonde
    with positive determinant. In the ANALYTIC domain Cc∞(U), the linear
    moment map f -> (∫x^k f(x)dx)_{0<=k<rank} is onto R^rank:
    a polynomial annihilating all such test integrals vanishes identically
    on U, so the dual map is injective. The exact Vandermonde calibration
    is NOT an explicit inverse moment/Suzuki low Schur certificate.
    The map can be arbitrarily ill-conditioned for narrow U.
    """
    if n!=2 or type(n) is not int or type(rank) is not int or not 1<=rank<=30:
        raise PrimeDomainError("Original p2 packet and 1..30 moment gate only")
    domain=prime_two_pair_packet_domain()
    lo,hi=domain["base_U"]
    delta=hi-lo
    nodes=tuple(lo+delta*F(k+1,rank+1) for k in range(rank))
    if any(not lo<t<hi for t in nodes):
        raise ArithmeticError("Exact source packet Vandermonde node exits domain")
    determinant=F(1)
    for j in range(rank):
        for i in range(j):
            determinant*=nodes[j]-nodes[i]
    if determinant<=0:
        raise ArithmeticError("Moment rank calibration unexpectedly singular")
    return {"moment_rank":rank,
            "interval_U":(lo,hi),
            "strict_rational_nodes":nodes,
            "Vandermonde_determinant_positive":True,
            "Vandermonde_determinant":determinant,
            "true_Cc_infinity_moment_map_surjective":True,
            "Legendre_1_to_rank_projection_of_u_i_fprime_surjective":True,
            "uniform_inverse_moment_norm_bound_supplied":False,
            "original_Legendre_low_Schur_sign_proved":False,
            "RH_proved":False}

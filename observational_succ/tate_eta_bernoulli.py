"""Tate x eta: canonical Bernoulli transport vs accidental Weil margins.

This research instrument keeps three DIFFERENT mathematically typed sources:
1. The original zeta Weil/Suzuki bound from DYSPON-SPHERE I (real Gamma,
   authentic prime-2, contact and poles; no zeta-zero inputs);
2. Dedekind's modular eta q-product over ALL positive integers, whose
   q^(1/24) exponent is fixed by classical modular inversion;
3. The Eisenstein divisor-current Dirichlet series zeta(s) zeta(s-1),
   whose TWO prime-power log-derivative channels cancel to -zeta'/zeta.

It does not identify eta modular positivity with original Weil positivity.
Everything finite/arithmetic uses int/Fraction, never sampled RH zeros.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

from .tate_prime_clock_uv import (
    genuine_first_prime_sparse_weil_certificate, PrimeClockGateError
)


class EtaTransportError(ValueError):
    """Refused an invalid or silently retyped source/normalization."""


def _rational(x) -> F:
    if type(x) not in (int, F):
        raise EtaTransportError("Exact int/Fraction parameter required")
    return F(x)


def bernoulli_heat_ledger() -> dict:
    """The exact constant term of sum_{n>=1} n exp(-n t).

    Identity for t>0: e^-t/(1-e^-t)^2 = 1/(4 sinh(t/2)^2).
    Formal Taylor:
      2 sinh(t/2)/t = 1 + t^2/24 + t^4/1920 + ...
      1/(4 sinh(t/2)^2) = t^-2 - 1/12 + t^2/240 + ...
    The heat constant equals analytically continued zeta(-1), NOT the
    ordinary divergent sum 1+2+3+...
    """
    u = F(1, 2**2 * factorial(3))  # 1/24
    v = F(1, 2**4 * factorial(5))  # 1/1920
    heat_constant = -2 * u
    heat_t2 = 3*u*u - 2*v
    eta_exponent = -heat_constant/2
    assert heat_constant == F(-1, 12) and heat_t2 == F(1, 240)
    assert eta_exponent == F(1, 24)
    return {
        "B2": F(1, 6),
        "zeta_of_minus_one": heat_constant,
        "heat_laurent_coefficient_t_minus_two": F(1),
        "heat_laurent_constant": heat_constant,
        "heat_laurent_t_squared": heat_t2,
        "canonical_eta_exponent": eta_exponent,
        "interprets_divergent_sum_as_analytic_continuation": True,
        "RH_proved": False,
    }


def original_weil_margin_ablation() -> dict:
    """Recover exact APOLLO/DYSPON original-source lower, not a new constant."""
    old = genuine_first_prime_sparse_weil_certificate()
    margin = old["uniform_source_margin_exact_lower"]
    exact = sum((F(4,4*j+1) for j in range(16)), F()) - F(111,16)
    if margin != exact:
        raise ArithmeticError("Original zeta source lower no longer matches gamma/prime/contact")
    # Genuine pinned source confirms the theorem; target rational cutoffs are
    # completely free BELOW its actual exact conservative lower margin.
    return {
        "source": old["source"],
        "original_source_lower": margin,
        "one_twenty_fourth_works": margin > F(1,24),
        "one_twenty_second_works": margin > F(1,22),
        "one_twenty_first_not_certified_by_this_bound": margin < F(1,21),
        "equal_to_eta_exponent": margin == F(1,24),
        "free_choice_of_all_rational_thresholds_below_lower": True,
        "arithmetic_eta_normalization_inferred_from_Weil_bound": False,
        "RH_proved": False,
    }


def eta_modular_s_defect(alpha, t_over_pi):
    """EXACT coefficient of pi in the log of the modular S defect.

    E_alpha(t) = exp(-alpha*t) prod_{n>=1}(1-exp(-n*t)).
    Classical Dedekind eta (alpha=1/24) obeys
      E(t) = sqrt(2*pi/t) E(4*pi^2/t).
    For t = c*pi, division by this canonical modular relation gives
      exp(-pi*(alpha-1/24)*(c-4/c)).
    Return the rational coefficient of pi. Zero at c=2 for EVERY alpha,
    hence testing only the self-dual point is a PROBE GAP.
    """
    aa,c=_rational(alpha),_rational(t_over_pi)
    if c<=0:
        raise EtaTransportError("Positive Archimedean modular time required")
    delta=aa-F(1,24)
    return {
        "chosen_q_exponent": aa,
        "canonical_q_exponent": F(1,24),
        "t_over_pi": c,
        "log_defect_over_minus_pi": delta*(c-F(4)/c),
        "S_transport_passes_at_this_clock": delta*(c-F(4)/c)==0,
        "all_positive_clocks_S_transport": delta==0,
        "self_dual_false_pass_possible": c==2 and delta!=0,
        "RH_proved": False,
    }


def eta_T_multiplier_exponent(alpha) -> dict:
    """T: tau->tau+1 determines multiplier alpha mod Z, not the exact alpha."""
    aa=_rational(alpha)
    delta=aa-F(1,24)
    return {
        "eta_T_exponent": aa,
        "canonical_exponent": F(1,24),
        "canonical_T_character": delta.denominator == 1,
        "S_still_required_to_fix_integer_gauge": delta!=0,
        "eta_power_24_cusp_order": 24*aa,
        "simple_cusp_zero_if_normalized": 24*aa==1,
        "RH_proved": False,
    }


def _divisors(n:int) -> tuple[int,...]:
    if type(n) is not int or n<1:
        raise EtaTransportError("Positive source integer required")
    return tuple(d for d in range(1,n+1) if n%d==0)


def _valuation(n:int) -> dict[int,int]:
    if type(n) is not int or n<1:
        raise EtaTransportError("Positive source integer required")
    out={}
    p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
        p+=1
    if n>1:
        out[n]=out.get(n,0)+1
    return out


def sigma_one(n:int) -> int:
    """Finite divisor-source coefficient of eta logarithmic derivative."""
    return sum(_divisors(n))


def eta_q_log_derivative_coefficients(N:int, alpha=F(1,24)) -> tuple[F,...]:
    """Independently compute q*d/dq log E_alpha from the finite q-product.

    Truncation to q^N is EXACT: factors 1-q^m for m>N cannot affect
    any coefficient up to q^N.  Returned coefficients index 0..N.
    Coeff(0)=alpha; Coeff(n)=-sigma_1(n) for n>=1.
    """
    if type(N) is not int or not 1<=N<=256:
        raise EtaTransportError("Finite q-polynomial truncation 1..256 required")
    a=_rational(alpha)
    product=[0]*(N+1)
    product[0]=1
    for k in range(1,N+1):
        for j in range(N,k-1,-1):
            product[j]-=product[j-k]
    inverse=[0]*(N+1)
    inverse[0]=1
    for n in range(1,N+1):
        inverse[n]=-sum(product[k]*inverse[n-k] for k in range(1,n+1))
    answer=[a]
    for n in range(1,N+1):
        answer.append(F(sum(k*product[k]*inverse[n-k] for k in range(1,n+1))))
    return tuple(answer)


def _dirichlet_inverse(coeff:tuple[int,...]) -> tuple[int,...]:
    """Formal Dirichlet inverse of a(1)=1 with full finite coefficient exactness."""
    N=len(coeff)-1
    if N<2 or coeff[0]!=0 or coeff[1]!=1 or any(type(v) is not int for v in coeff):
        raise EtaTransportError("Source tuple a[0]=0,a[1]=1; integer coefficients required")
    out=[0]*(N+1)
    out[1]=1
    for n in range(2,N+1):
        out[n]=-sum(coeff[d]*out[n//d] for d in _divisors(n) if d>1)
    return tuple(out)


def formal_dirichlet_log_derivative(coeff:tuple[int,...]) -> tuple[dict[int,int],...]:
    """Exact n^-s Dirichlet coefficients of -D'(s)/D(s), in log-prime basis.

    Because log n = sum_p v_p(n) log p, the coefficient of n^-s
    is represented as a dict {p: integer multiple of log(p)}. This
    avoids transcendental fits and detects fake composite source atoms.
    """
    inv=_dirichlet_inverse(coeff)
    N=len(coeff)-1
    values=[{}]
    for n in range(1,N+1):
        row={}
        for d in _divisors(n):
            for p,k in _valuation(d).items():
                row[p]=row.get(p,0)+coeff[d]*k*inv[n//d]
        values.append({p:v for p,v in row.items() if v})
    return tuple(values)


def _subtract_rows(a:dict[int,int], b:dict[int,int]) -> dict[int,int]:
    return {p:v for p in set(a)|set(b) if (v:=a.get(p,0)-b.get(p,0))}


def eta_eisenstein_prime_transducer(N:int=64, fake_composite_six=False) -> dict:
    """Exact all-coefficients-through-N Eisenstein -> original Euler prime jet.

    From eta q-derivative -sigma1(n), form the DIRICHLET rather than
    ordinary q-series D(s)=sum sigma1(n)n^-s = zeta(s)zeta(s-1) (Re s>2).
    Its log derivative is a two-channel genuine prime source
      -D'/D = sum_{p,k} (1+p^k)*log(p) / p^(ks).
    Subtract shifted zeta(s-1) log derivative, n*log(p) on prime powers,
    obtaining exactly -zeta'/zeta = sum log(p)/p^(ks).
    The fake n=6 mutation breaks this, and must NOT be source-laundered.
    """
    if type(N) is not int or not 6<=N<=256:
        raise EtaTransportError("Finite 6..256 Dirichlet source horizon required")
    if type(fake_composite_six) is not bool:
        raise EtaTransportError("Explicit boolean source mutation flag required")
    div=[0]+[sigma_one(n) for n in range(1,N+1)]
    if fake_composite_six:
        div[6]+=1
    shift=[0]+list(range(1,N+1))
    zeta=[0]+[1]*N
    eisen=formal_dirichlet_log_derivative(tuple(div))
    shifted=formal_dirichlet_log_derivative(tuple(shift))
    original=formal_dirichlet_log_derivative(tuple(zeta))
    rows=tuple(_subtract_rows(eisen[n],shifted[n]) for n in range(N+1))
    mismatches=tuple(n for n in range(2,N+1) if rows[n]!=original[n])
    composite6=rows[6]
    # Strong check of separate channels only for the *unmutated* source.
    if not fake_composite_six:
        for n in range(2,N+1):
            val=_valuation(n)
            source={} if len(val)!=1 else {next(iter(val)):(n+1)}
            shift_source={} if len(val)!=1 else {next(iter(val)):n}
            if eisen[n]!=source or shifted[n]!=shift_source:
                raise ArithmeticError("Exact original divisor prime-current identity failed")
        if mismatches or composite6:
            raise ArithmeticError("Original prime log-current transport failed")
    else:
        if 6 not in mismatches or composite6!={2:1,3:1}:
            raise ArithmeticError("Fake-composite negative control no longer discriminates")
    return {
        "source_type": "EISENSTEIN_SIGMA1" if not fake_composite_six else "MUTATED_NON_EULER_SIGMA1",
        "finite_horizon": N,
        "mellin_source": "Gamma(s)*zeta(s)*zeta(s-1) for Re(s)>2",
        "prime_jet_parent": "(-D'/D)=(1+n)*Lambda(n) on n=p^k",
        "prime_jet_shifted": "-zeta'(s-1)/zeta(s-1)=n*Lambda(n) on n=p^k",
        "prime_jet_difference": "-zeta'(s)/zeta(s)=Lambda(n) on n=p^k",
        "composite_six_residual_prime_log_basis": composite6,
        "mismatch_indices": mismatches,
        "transport_preserves_genuine_von_mangoldt": not mismatches,
        "source_authentic": not fake_composite_six,
        "all_critical_line_transport_certified": False,
        "original_Weil_Gamma_contact_identified": False,
        "RH_proved": False,
    }


def primary_source_interface_status() -> dict:
    """Typed map explicitly prevents illicit eta->RH promotion."""
    return {
        "canonical_Bernoulli_eta_q_exponent":F(1,24),
        "eta_dirichlet_domain":"Re(s)>2",
        "eta_heat_archimedean":"Gamma(s)",
        "original_zeta_prime_dirichlet_domain":"Re(s)>1",
        "original_zeta_Weil_half_density":F(1,2),
        "original_zeta_archimedean":"pi^(-s/2)*Gamma(s/2)",
        "eta_product_over":"ALL_POSITIVE_INTEGERS",
        "zeta_Euler_product_over":"GENUINE_PRIMES",
        "missing_transport":"source-faithful completed signed Weil Schwarz-Bruhat map with pole/contact and global positivity",
        "eta_modular_transport_is_not_Weil_positivity":True,
        "RH_proved":False,
    }

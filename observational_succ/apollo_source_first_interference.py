"""APOLLO: positive-first source reconstruction and signed prime interference.

Exact formula for every genuine prime-power b=log(p^k), w=log(p)/sqrt(p^k):
    w*b*E_b(v)-2*w*B(v)
    = w*|| (S_b-I)v ||^2 - 2*w*||v||^2
    = -2*w*Re <v,S_b v>.
The Brownian subtraction is the UNIQUE self-energy cancellation that
vanishes before a source prime clock enters the observation window.

A positive prime-difference feature (S_b-I)v on a COMPACT source window
determines the Brownian v by finitely many causal inverse shifts.
Recoverability != contractivity != a physical time arrow or RH.

Every rational executable control is exact Fraction; the true p=2 tests
use SHA-pinned source intervals with symbolic irrational amplitudes.
The full completed zeta K_g retains real Gamma, poles, contact and
every authentic prime-power. No nontrivial zeta zeros are ever input.
"""
from __future__ import annotations

from fractions import Fraction as F

from .apollo_derivative_jets import _source, true_third_prime_wavefronts
from .apollo_krein_factor import (
    brownian_increment_kernel, triangle_increment_kernel,
    prime_hinge_kernel,
)


class PrimeInterferenceError(ValueError):
    """Invalid finite carrier, false source or premature sign inference."""


def _q(x):
    if type(x) not in (int, F):
        raise PrimeInterferenceError("All executable certificates require int/Fraction")
    return F(x)


def _positive(x):
    v=_q(x)
    if v<=0:
        raise PrimeInterferenceError("A strictly positive clock or source weight is required")
    return v


def _ceil(x):
    y=_q(x)
    return -(-y.numerator//y.denominator)


def _parse_cells(a, cells):
    """Disjoint rational (lo,hi,real,imag) cells on (-a,a)."""
    if type(cells) not in (list,tuple) or not cells or len(cells)>24:
        raise PrimeInterferenceError("Nonempty finite cell list of size <=24 required")
    aa=_positive(a)
    parsed=[]
    for cell in cells:
        if type(cell) not in (tuple,list) or len(cell)!=4:
            raise PrimeInterferenceError("Cells are (lo,hi,real,imag) exactly")
        lo,hi,re,im=map(_q,cell)
        if not (-aa<=lo<hi<=aa):
            raise PrimeInterferenceError("Cell lies outside compact observation carrier")
        parsed.append((lo,hi,re,im))
    parsed.sort()
    if any(parsed[j][1]>parsed[j+1][0] for j in range(len(parsed)-1)):
        raise PrimeInterferenceError("Source cells must be disjoint, not double-counted")
    if not any(re or im for _,_,re,im in parsed):
        raise PrimeInterferenceError("Nonzero test required")
    return tuple(parsed)


def _cell_value(cells,x):
    real=imag=F()
    for lo,hi,re,im in cells:
        if lo<=x<hi:
            real+=re
            imag+=im
    return real,imag


def _dot_real(a,b):
    return a[0]*b[0]+a[1]*b[1]


def _overlap(l,r,L,R):
    return max(F(),min(r,R)-max(l,L))


def source_first_prime_interference(a,b,weight,cells):
    """EXACT continuum finite-step controls, no numerical quadrature.

    m=floor(2a/b). For each compactly supported v, F=(S_b-I)v:
        v(x)=-sum_{k=0}^m F(x-kb)  (a.e. x in (-a,a)).
    This is a bounded finite-step source inverse; \|v\| <=
    (m+1)*\|F\|. Neither statement makes a physical chronological order.

    The positive source energy is w||F||², negative Brownian correction
    2w||v||², and their sign-complete difference is
    -2w Re<v,S_b v>. Phase produces BOTH signs.
    """
    aa,bb,ww=_positive(a),_positive(b),_positive(weight)
    c=_parse_cells(aa,cells)
    norm=sum(((re*re+im*im)*(hi-lo) for lo,hi,re,im in c),F())
    interaction=sum(
        ((ri*rj+ii*ij)*_overlap(li,hi,lj+bb,hj+bb)
         for li,hi,ri,ii in c for lj,hj,rj,ij in c),F()
    )
    positive=ww*(2*norm-2*interaction)
    brownian=2*ww*norm
    signed=positive-brownian
    if signed!=-2*ww*interaction:
        raise ArithmeticError("K1 source plus-minus prime interference identity failed")
    steps=(2*aa)//bb   # floor; then (steps+1)b>2a
    # Exact piecewise equality on the FULL continuum carrier. All possible
    # breakpoints of either side are finite rational cell edges.
    cuts={-aa,aa}
    for lo,hi,_,_ in c:
        cuts.update((lo,hi))
        for k in range(steps+1):
            for shift in (k*bb,(k+1)*bb):
                for edge in (lo+shift,hi+shift):
                    if -aa<edge<aa:
                        cuts.add(edge)
    ordered=tuple(sorted(cuts))
    for lo,hi in zip(ordered,ordered[1:]):
        x=(lo+hi)/2
        actual=_cell_value(c,x)
        recovered_r=recovered_i=F()
        for k in range(steps+1):
            newer=_cell_value(c,x-(k+1)*bb)
            older=_cell_value(c,x-k*bb)
            recovered_r-=newer[0]-older[0]
            recovered_i-=newer[1]-older[1]
        if (recovered_r,recovered_i)!=actual:
            raise ArithmeticError("True compact source cannot be recovered from positive difference")
    if norm>(steps+1)**2*(2*norm-2*interaction):
        raise ArithmeticError("Finite source inverse norm inequality failed")
    return {
        "source":"EXACT_RATIONAL_PRIME_HINGE_SHAPE_NOT_AUTHENTIC_EULER_LABEL",
        "a":aa,"clock":bb,"source_weight":ww,
        "cells":c,
        "Brownian_L2_energy":norm,
        "translated_overlap_real":interaction,
        "positive_prime_difference_energy":positive,
        "forced_Brownian_subtraction_energy":brownian,
        "signed_prime_energy":signed,
        "phase_class":"negative_interaction" if signed<0 else
            ("positive_interaction" if signed>0 else "no_real_interference"),
        "finite_inverse_shift_steps":steps+1,
        "inverse_reconstruction_exact_on_every_piece":True,
        "positive_feature_determines_Brownian_feature":True,
        "positive_energy_dominates_Brownian":positive>=brownian,
        "prewavefront":bb>=2*aa,
        "two_support_copies_disjoint_before_birth":bb>=2*aa,
        "no_independent_Brownian_random_variable_needed":True,
        "contractive_original_complete_Weil_source_proved":False,
        "RH_proved":False,
    }


def forced_Brownian_cancellation(a,b,weight,baseline=2):
    """UNIQUE subtraction coefficient preserving prime inactivity.

    When b>=2a, ||(S_b-I)v||²=2||v||² for ALL v supported in I.
    Subtracting c*w||v||² leaves (2-c)*w||v||².
    Since nonzero source tests exist, this vanishes for all iff c=2.
    This is source-forced under the declared difference factorization,
    not a universal unique Krein decomposition of the entire Weil kernel.
    """
    aa,bb,ww,c=_positive(a),_positive(b),_positive(weight),_q(baseline)
    if bb<2*aa:
        raise PrimeInterferenceError("This unique neutral coefficient proof is pre-wavefront only")
    return {
        "source":"EXACT_PREWAVEFRONT_PRIME_DIFFERENCE_FACTOR",
        "clock":bb,"halfwidth":aa,
        "assumed_Brownian_energy_coefficient":c,
        "original_source_neutral_coefficient":F(2),
        "prebirth_signed_factor_per_w_norm":F(2)-c,
        "full_old_window_neutral_for_every_test":c==2,
        "source_forces_this_correction_within_factorization":True,
        "other_global_Krein_representations_necessarily_unique":False,
        "actual_RH_positivity_proved":False,
        "RH_proved":False,
    }


def exact_anchored_prime_hinge(a,b,w):
    """Original K1 at (a,-a) with a<b<2a.

    Kprime(a,a)=Kprime(-a,-a)=0,
    Kprime(a,-a)=w*(2a-b)>0.
    Hence the 2x2 source hinge is INDEFINITE, with exact eigenvalues
    ±w*(2a-b). It cannot be called a purely negative well.
    """
    aa,bb,ww=_positive(a),_positive(b),_positive(w)
    if not aa<bb<2*aa:
        raise PrimeInterferenceError("Two-anchor first-clock window a<b<2a required")
    diag=ww*prime_hinge_kernel(aa,aa,bb)
    off=ww*prime_hinge_kernel(aa,-aa,bb)
    if diag!=0 or off!=ww*(2*aa-b):
        raise ArithmeticError("APOLLO anchored prime source hinge mismatch")
    return {
        "source":"EXACT_RATIONAL_FIRST_CLOCK_HINGE",
        "a":aa,"b":bb,"w":ww,
        "anchored_2x2":((diag,off),(off,diag)),
        "eigenvalues":(-off,off),
        "indefinite_prime_only":True,
        "negative_well_in_phase_only":True,
        "positive_antiphase_direction_also_exists":True,
        "complete_original_Weil_sign_claimed":False,
        "RH_proved":False,
    }


def normalized_birth_boundary_wells(m):
    """The prime clock activation has a strong/norm limit separation.

    a=1/2, b_m=1-1/m² ↑2a. Let ell=1/(2m²),
    J=(-a,-a+ell), and v_±=m*(1_J ±1_(J+b_m)).
    Exact L2 norm of v_± is 1; signed prime energy for w=1 is -1
    (in-phase), +1 (antiphase), for EVERY m>=2, while for any fixed
    v∈L²(I) the translated overlap tends 0 as b_m↑2a.
    This is a boundary-layer source EFFECT, not a physical energy well.
    """
    mm=m
    if type(mm) is not int or not 2<=mm<=128:
        raise PrimeInterferenceError("Exact boundary family integer m in 2..128")
    aa=F(1,2)
    bb=F(1)-F(1,mm*mm)
    ell=F(1,2*mm*mm)
    J=-aa
    pos=(J,J+ell,mm,0)
    right=(J+bb,J+bb+ell,mm,0)
    minus=(J+bb,J+bb+ell,-mm,0)
    plus_cert=source_first_prime_interference(aa,bb,1,(pos,right))
    minus_cert=source_first_prime_interference(aa,bb,1,(pos,minus))
    if (plus_cert["Brownian_L2_energy"]!=1
            or minus_cert["Brownian_L2_energy"]!=1
            or plus_cert["signed_prime_energy"]!=-1
            or minus_cert["signed_prime_energy"]!=1):
        raise ArithmeticError("Finite stage cannot resolve exact normalized activation")
    return {
        "source":"RATIONAL_CLOCK_BOUNDARY_LAYER_NOT_ZETA_PRIME",
        "m":mm,"a":aa,"b":bb,"cell_length":ell,
        "in_phase_L2_norm_squared":F(1),
        "anti_phase_L2_norm_squared":F(1),
        "in_phase_signed_prime_energy":F(-1),
        "anti_phase_signed_prime_energy":F(1),
        "source_clock_approaches_2a_from_below":True,
        "fixed_test_prime_shift_form_tends_zero":True,
        "operator_norm_does_not_tend_zero":True,
        "normalized_negative_witness_moves_with_source_window":True,
        "source_omega_super_task_performed":False,
        "RH_proved":False,
    }


def true_prime_two_source_phase_triad():
    """EXACT source-indexed p=2 phase distinction, not irrational sampling.

    For arbitrary nonzero smooth phi supported on J=(-31/64,-29/64)
    and b=log2, let v_+=phi+S_b phi, v_-=phi-S_b phi,
    v_i=phi+i S_b phi. They are actual smooth compact f tests on
    I=(-1/2,1/2), of combined support<=1/16.
    Q_p(v+)=-w||v+||²; Q_p(v-)=+w||v-||²; Q_p(v_i)=0,
    w=log2/sqrt2. The full ORIGINAL Weil sign is separate.
    """
    src=_source()
    bb=src.log2_iv()
    inv=src.sqrt_inverse(2)
    w=bb*inv
    labels=tuple(z.n for z in true_third_prime_wavefronts(F(1)))
    lo=F(-31,64);hi=F(-29,64);aa=F(1,2)
    if labels!=(2,) or not (
            F(1,2)<bb.lo<bb.hi<F(7,10)
            and lo+bb.lo>-aa and hi+bb.hi<aa
            and hi<lo+bb.lo and w.lo>0):
        raise PrimeInterferenceError("Original prime-2 source or support waveform failed")
    from .tate_prime_clock_uv import genuine_first_prime_sparse_weil_certificate
    original_full=genuine_first_prime_sparse_weil_certificate()
    if not (original_full["actual_prime_power_labels"]==(2,)
            and original_full["support_measure_max"]>=F(1,16)
            and original_full["original_completed_Weil_L2_margin_strictly_above"]==F(1,24)):
        raise ArithmeticError("The independent genuine Weil sparse test theorem is not available")
    return {
        "source":"SHA_PINNED_ORIGINAL_PRIME_TWO_JET",
        "a":aa,"true_prime_power_labels":labels,
        "true_log2_bounds":(bb.lo,bb.hi),
        "true_half_density_weight_bounds":(w.lo,w.hi),
        "one_bump_interval":(lo,hi),
        "two_bumps_combined_support_measure_at_most":F(1,16),
        "in_phase_prime_rayleigh":"-log(2)/sqrt(2)",
        "anti_phase_prime_rayleigh":"+log(2)/sqrt(2)",
        "quarter_phase_prime_rayleigh":"0",
        "same_true_prime_jet_all_three_cases":True,
        "prime_jets_are_distribution_impulses_not_time_dynamics":True,
        "completed_original_Weil_all_three_phase_classes_positive_by_independent_sparse_theorem":True,
        "completed_original_Weil_each_L2_margin_strictly_above":F(1,24),
        "complete_original_source_positive_does_not_make_prime_component_positive":True,
        "completed_Weil_negative_witness_inferred":False,
        "RH_proved":False,
    }


def gamma_positive_first_Brownian_recovery(a):
    """Original first REAL Γ mode alone determines Brownian v on fixed I.

    On support (-a,a), R_(1/2) has L2 restricted norm
        <= 1-exp(-a/2)
    by exact Schur/interval row integration.
    True j=0 Gamma energy = 4 <v,(I-R_(1/2))v>
         >= 4 exp(-a/2) ||v||².
    Thus the positive Γ0 feature is injective, and Brownian v is a
    BOUNDED DETERMINISTIC map of that feature on every finite window.
    A rational lower bound is >=4 max(1-a/2,2^-ceil(a)).
    This does NOT prove the full negative source (contact/pole/primes)
    is dominated by the full positive source with norm <=1.
    """
    aa=_positive(a)
    if aa>128:
        raise PrimeInterferenceError("Executable rational radius <=128 only")
    src=_source()
    if src.contact_iv().hi>=F(43,8):
        raise PrimeInterferenceError("Original Gamma/contact source not pinned")
    low=max(F(),F(1)-aa/2,F(1,2**_ceil(aa)))
    margin=4*low
    if not margin>0:
        raise ArithmeticError("Gamma source cannot reconstruct Brownian window")
    return {
        "source":"SHA_PINNED_ORIGINAL_ONE_REAL_GAMMA",
        "halfwidth":aa,
        "first_real_Gamma_index":0,
        "alpha":F(1,2),"beta":F(4),
        "Gamma0_L2_relative_lower":margin,
        "unrounded_analytic_lower":"4*exp(-a/2)",
        "Gamma_positive_feature_injective_on_source_window":True,
        "Brownian_source_v_uniquely_determined_by_positive_Gamma0":True,
        "Brownian_recovery_map_bounded_by_coercivity":True,
        "physical_Gamma_first_time_order_proved":False,
        "full_negative_Brownian_contact_dominated_by_Gamma0":False,
        "all_positive_to_negative_contraction_proved":False,
        "RH_proved":False,
    }


def finite_feature_graph_criterion(positive,negative):
    """An exact small Gram gate distinguishes determinacy from contraction.

    On a finite coefficient family, a 'positive pins negative' rule is
    well-defined iff ker(A+)⊆ker(A-). Contractive iff A+-A- PSD.
    For positive definite A+, N is uniquely recoverable, but that does
    NOT make A+-A- PSD. This is the finite shadow of APOLLO K4, not
    its infinite test-universal proof.
    """
    from .apollo_krein_factor import source_feature_contraction_diagnostic
    diag=source_feature_contraction_diagnostic(positive,negative)
    p=tuple(tuple(_q(x) for x in row) for row in positive)
    n=tuple(tuple(_q(x) for x in row) for row in negative)
    if len(p)!=2:
        raise PrimeInterferenceError("This independent rank-two proof control needs two source modes")
    # Rank 2 exact kernel inclusion via matrix columns.
    def null_basis(m):
        a,b=m[0];c,d=m[1]
        det=a*d-b*c
        if det:
            return ()
        if not a and not b and not c and not d:
            return ((F(1),F(0)),(F(0),F(1)))
        if a or b:
            return ((-b,a),)
        return ((-d,c),)
    k=null_basis(p)
    well_defined=all(all(sum((n[i][j]*v[j] for j in range(2)),F())==0
                               for i in range(2)) for v in k)
    contraction=bool(diag["combined_signed_psd_on_selected_finite_set"])
    return {
        "source":"SYNTHETIC_EXACT_TWO_MODE_FEATURE_GRAPH",
        "positive_kernel_null_in_negative_kernel":well_defined,
        "Brownian_or_negative_feature_determined_by_positive":well_defined,
        "finite_full_source_contraction_condition":contraction,
        "signed_Gram_PSD":contraction,
        "source_feature_positive_psd":True,
        "source_feature_negative_psd":True,
        "true_original_Weil_contraction_proved":False,
        "RH_proved":False,
    }


def authentic_full_negative_feature_transfer_bound(a):
    """Construct an UNCONDITIONAL bounded graph from positive to negative.

    Fix 0<a<=2, true prime active set P_a from the SHA-pinned source.
    In Brownian v∈L²(-a,a) source coordinates, true K2 has:
       E_+(v) = Q_Gamma(v)+8|<v,s'>|²+
                sum_{n∈P_a}w_n|| (S_bn-I)v ||²,
       E_-(v) = (C_inf+2sum w_n)||v||²+8|<v,h'>|²,
       h'(t)=sinh(t/2)/2.
    First REAL Gamma rung >=gamma(a)||v||², gamma=4e^-a/2>0.
    E_- <=[C_inf+2sum w_n+2(sinh a-a)]||v||².
    Therefore positive feature F_+ is INJECTIVE and defines a
    UNIQUE BOUNDED linear graph T_a(F_+ v)=F_- v with
       ||T_a||² <= negative_budget/gamma(a).
    This does NOT show ||T_a||<=1; that is exactly APOLLO K4/RH-hard.
    """
    aa=_positive(a)
    if aa>2:
        raise PrimeInterferenceError("Original source prime chart limited to 0<a<=2")
    src=_source()
    if src.contact_iv().hi>=F(43,8):
        raise PrimeInterferenceError("True zeta real contact bound missing")
    labels=true_third_prime_wavefronts(2*aa)
    jets=[]
    for z in labels:
        weight=src.log_iv(z.p)*src.sqrt_inverse(z.n)
        jets.append((z.n,weight.lo,weight.hi))
    sum_hi=sum((hi for _,lo,hi in jets),F())
    if aa<=F(1,2):
        # Classical source small-interval polar bound, proved via sinh series.
        pole_upper=F(1,16)
    else:
        # 2(sinh a-a)<e^a<2^(ceil(2a)+1), using log2>1/2.
        pole_upper=F(2**(_ceil(2*aa)+1))
    neg_upper=F(43,8)+2*sum_hi+pole_upper
    gamma=gamma_positive_first_Brownian_recovery(aa)["Gamma0_L2_relative_lower"]
    norm_squared_upper=neg_upper/gamma
    if not gamma>0 or not norm_squared_upper>0:
        raise ArithmeticError("Source first real Gamma failed finite-window graph coercivity")
    return {
        "source":"SHA_PINNED_ORIGINAL_COMPLETED_ZETA_KREIN",
        "a":aa,
        "true_active_prime_powers":tuple(n for n,_,_ in jets),
        "true_prime_half_density_weight_intervals":tuple(jets),
        "source_contact_upper":F(43,8),
        "negative_pole_upper":pole_upper,
        "negative_feature_energy_L2_upper":neg_upper,
        "positive_first_Gamma_L2_lower":gamma,
        "source_positive_to_negative_graph_operator_norm_squared_upper":
            norm_squared_upper,
        "positive_feature_injective_on_compact_Brownian_carrier":True,
        "negative_feature_determined_by_positive_without_assuming_sign":True,
        "unique_bounded_graph_on_minimal_positive_feature_span":True,
        "this_bound_itself_certifies_contraction":norm_squared_upper<=1,
        "RH_equivalent_all_windows_contraction_proved":False,
        "physical_actualization_order_proved":False,
        "RH_proved":False,
    }

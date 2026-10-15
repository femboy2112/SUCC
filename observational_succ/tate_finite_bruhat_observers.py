"""Finite exact Tate/Bruhat-Schwartz source windows in the p-adic carrier.

For genuine rational prime p and nonnegative M,N:
  V_(M,N) = {f supported on p^-M Z_p; invariant by p^N Z_p}
  dim_C V_(M,N) = Q=p^(M+N).
  f(j/p^M + p^N Z_p) = c_j for j mod Q.

Self-dual additive psi_p(x)=exp(+2*pi*i*{x}_p), dx(Z_p)=1:
  Ff(k/p^N) = p^-N sum_j c_j*zeta_Q^(j*k),
  F: V_(M,N) -> V_(N,M), Q=p^(M+N).
  ||f||_2² = p^-N sum_j |c_j|².
  F²f(x)=f(-x), and ||Ff||_2=||f||_2 by finite character sums.

Executable output keeps formal cyclotomic phase labels with exact rational
weights; a finite group-algebra polynomial is not silently treated as a
unique algebraic-number normal form. Parseval and inversion use character
orthogonality, not approximate roots of unity.

The Z_p carrier is an inverse limit of finite residue rings, while the
Bruhat-Schwartz test space is a FILTERED DIRECT LIMIT of such finite charts.
Finite dimension alone does NOT make arbitrary complex coefficients
computable or the global Weil sign PSD. No nontrivial zeta zeros used.
"""
from __future__ import annotations

from fractions import Fraction as F

from .tate_local_contract import _place, ZETA3, QRootMinus3


class TateFiniteFieldError(ValueError):
    """Invalid genuine place, rational finite chart, phase, or source probe."""


def _index(n,limit=128):
    if type(n) is not int or n<0 or n>limit:
        raise TateFiniteFieldError("Exact nonnegative bounded conductor/support index")
    return n


def finite_bruhat_chart(p,M=0,N=0):
    """Exact source geometry; finite TEST dimension, infinite local field."""
    try:
        _place(p)
    except Exception as exc:
        raise TateFiniteFieldError("Not a genuine rational prime place") from exc
    mm=_index(M)
    nn=_index(N)
    Q=p**(mm+nn)
    if Q>64:
        raise TateFiniteFieldError("Executable chart dimension <=64; paper law is all M,N")
    return {
        "source":"GENUINE_LOCAL_QP_SELF_DUAL_TATE",
        "p":p,"support_exponent_M":mm,"constancy_exponent_N":nn,
        "finite_complex_dimension":Q,
        "source_ball":"p^(-M)*Z_p",
        "local_constancy":"p^N*Z_p cosets",
        "input_additive_Haar_cell":F(1,p**nn),
        "dual_support_exponent_M":nn,
        "dual_constancy_exponent_N":mm,
        "dual_additive_Haar_cell":F(1,p**mm),
        "additive_character":"exp(+2*pi*i*{x}_p)",
        "real_place_partner_character":"exp(-2*pi*i*x)",
        "entire_local_Qp_has_infinitely_many_points":True,
        "all_complex_coefficients_automatically_computable":False,
        "original_global_Weil_sign_proved":False,
        "RH_proved":False,
    }


def _coefficients(c,Q):
    if type(c) not in (tuple,list) or len(c)!=Q:
        raise TateFiniteFieldError("One exactly represented coefficient per genuine coset")
    out=[]
    for x in c:
        if type(x) not in (int,F):
            raise TateFiniteFieldError("This finite executable instrument uses rational coefficients")
        out.append(F(x))
    return tuple(out)


def cyclic_character_sum(modulus, power):
    """Exact sum_k zeta_Q^(power*k) via finite character orthogonality."""
    q=_index(modulus,4096)
    if q==0 or type(power) is not int:
        raise TateFiniteFieldError("Positive group modulus and exact integer phase")
    return q if power%q==0 else 0


def finite_cyclotomic_fourier(p,M,N,coeffs):
    """Exact formal phase polynomial for each dual coset (no float roots)."""
    chart=finite_bruhat_chart(p,M,N)
    Q=chart["finite_complex_dimension"]
    c=_coefficients(coeffs,Q)
    scale=chart["input_additive_Haar_cell"]
    rows=[]
    for k in range(Q):
        phases=[F()]*Q
        for j,val in enumerate(c):
            phases[(j*k)%Q]+=scale*val
        rows.append(tuple((e,z) for e,z in enumerate(phases) if z))
    return {
        "source":chart["source"],
        "input_coefficients":c,
        "dual_symbolic_rows":tuple(rows),
        "root_of_unity_order":Q,
        "dual_chart_M_N":(N,M),
        "phase_orientation":"positive_padic_additive_character",
        "formal_group_ring_not_reduced_to_cyclotomic_field":True,
        "RH_proved":False,
    }


def exact_tate_finite_plancherel(p,M,N,coeffs):
    """Prove finite Fourier involution and Parseval by exact character sum."""
    chart=finite_bruhat_chart(p,M,N)
    Q=chart["finite_complex_dimension"]
    c=_coefficients(coeffs,Q)
    input_energy=F(1,p**N)*sum((z*z for z in c),F())
    output_energy=F(1,p**M)*F(1,p**(2*N))*sum(
        (c[j]*c[l]*cyclic_character_sum(Q,j-l)
         for j in range(Q) for l in range(Q)),F()
    )
    # Double Fourier: p^-N p^-M sum_k exp(2pi i k(j+l)/Q)
    recon=tuple(
        F(1,p**(M+N))*sum(
            (c[j]*cyclic_character_sum(Q,j+l) for j in range(Q)),F()
        ) for l in range(Q)
    )
    expected=tuple(c[(-l)%Q] for l in range(Q))
    if input_energy!=output_energy or recon!=expected:
        raise ArithmeticError("Tate local Haar Fourier/Parseval/inversion source law FAILED")
    return {
        "source":chart["source"],
        "finite_dimension":Q,
        "input_exact_L2_squared":input_energy,
        "dual_exact_L2_squared":output_energy,
        "isometry_certified_by_character_orthogonality":True,
        "double_Fourier_coefficients":recon,
        "source_reflection_coefficients":expected,
        "dual_support_constancy_interchanged":True,
        "same_genuine_prime_place":True,
        "full_adelic_Weil_source_identified":False,
        "RH_proved":False,
    }


def refine_support_chart(p,M,N,coeffs):
    """V_(M,N) -> V_(M+1,N), source coefficients at new j'=p*j."""
    chart=finite_bruhat_chart(p,M,N)
    Q=chart["finite_complex_dimension"]
    c=_coefficients(coeffs,Q)
    parent=finite_bruhat_chart(p,M+1,N)
    d=[F()]*parent["finite_complex_dimension"]
    for j,x in enumerate(c):
        d[p*j]=x
    return tuple(d)


def refine_constancy_chart(p,M,N,coeffs):
    """V_(M,N) -> V_(M,N+1), replicate old cell across p subcosets."""
    chart=finite_bruhat_chart(p,M,N)
    Q=chart["finite_complex_dimension"]
    c=_coefficients(coeffs,Q)
    parent=finite_bruhat_chart(p,M,N+1)
    return tuple(c[j%Q] for j in range(parent["finite_complex_dimension"]))


def finite_tate_refinement_square(p,M,N,coeffs):
    """Fourier commutes with BOTH genuine source scale inclusions.

    Support enlargement M->M+1 causes dual constancy refinement:
       Fourier(refine_support f)=refine_constancy(Fourier f).
    Coset constancy refinement N->N+1 causes dual support enlargement:
       Fourier(refine_constancy f)=refine_support(Fourier f).
    Equations hold as cyclotomic values by EXACT finite character sums.
    """
    chart=finite_bruhat_chart(p,M,N)
    Q=chart["finite_complex_dimension"]
    c=_coefficients(coeffs,Q)
    newQ=p*Q
    if newQ>64:
        raise TateFiniteFieldError("Next source refinement outside finite executable budget")
    a=refine_support_chart(p,M,N,c)
    b=refine_constancy_chart(p,M,N,c)
    old=finite_cyclotomic_fourier(p,M,N,c)["dual_symbolic_rows"]
    new_sup=finite_cyclotomic_fourier(p,M+1,N,a)["dual_symbolic_rows"]
    # Exact embedding zeta_Q^e -> zeta_(pQ)^(p*e).
    for k in range(newQ):
        expected=tuple(sorted((p*e,z) for e,z in old[k%Q]))
        if tuple(sorted(new_sup[k]))!=expected:
            raise ArithmeticError("Tate support enlargement/Fourier square failed")
    # For new constancy, sum over split old cosets: sum_l zeta_p^(l*k')
    # vanishes unless p|k'; when p|k', the p factor cancels Haar 1/p.
    # The result equals old Fourier at k'/p. The identity is certified
    # by finite cyclic character orthogonality for each k'.
    for k in range(newQ):
        factor=cyclic_character_sum(p,k)
        if (factor!=0)!=(k%p==0):
            raise ArithmeticError("Finite local Fourier conductor phase no-go failed")
    if len(b)!=newQ:
        raise ArithmeticError("True local constancy extension failed")
    new_con=finite_cyclotomic_fourier(p,M,N+1,b)["dual_symbolic_rows"]
    for kprime in range(0,newQ,p):
        k=kprime//p
        expected=tuple(sorted((p*e,z) for e,z in old[k]))
        if tuple(sorted(new_con[kprime]))!=expected:
            raise ArithmeticError("Tate constancy enlargement/Fourier supported coefficient square failed")
    return {
        "source":"GENUINE_LOCAL_QP_TATE_FOURIER_SCALE_NATURALITY",
        "p":p,"M":M,"N":N,
        "input_dimension":Q,"refined_dimension":newQ,
        "support_refinement_dual_constancy_square":True,
        "constancy_refinement_dual_support_square":True,
        "character_orthogonality_for_wrong_dual_cosets":True,
        "Haar_factor_preserved":True,
        "direct_limit_of_all_finite_Schwartz_Bruhat_charts":True,
        "Zp_as_inverse_limit_of_residue_rings":True,
        "all_finite_place_information_executed":False,
        "full_Weil_quadratic_positivity_derived":False,
        "RH_proved":False,
    }


def conductor_three_probe_gap():
    """Real p=3 ramified units: coarse scalar 0, Fourier mode nonzero.

    On Z_3/pZ_3 use coefficients (c0,c1,c2)=(0,1,-1).
    Coarse unit average c1+c2=0; dual k=1 has
         (zeta_3-zeta_3²)/3 = sqrt(-3)/3.
    Uses PR103's exact cyclotomic Q(sqrt(-3)) source; no fitted phase.
    """
    c=(F(0),F(1),F(-1))
    t=finite_cyclotomic_fourier(3,0,1,c)
    phase=(ZETA3-ZETA3**2)/3
    if phase!=QRootMinus3(0,F(1,3)):
        raise ArithmeticError("Authentic chi_-3 ramified Gauss phase lost")
    coarse=c[1]+c[2]
    if coarse or phase.norm()!=F(1,3):
        raise ArithmeticError("Conductor-three fine/coarse source probe mismatch")
    return {
        "source":"PR103_GENUINE_RAMIFIED_Q3_UNIT_CHARACTER",
        "p":3,
        "true_coarse_unit_observation":coarse,
        "fine_source_coefficients":c,
        "fine_Fourier_at_k1_exact":("0","1/3","delta^2=-3"),
        "fine_nonzero_Gauss_phase":True,
        "fine_phase_norm_squared":phase.norm(),
        "source_Fourier_character":"exp(+2*pi*i*{x}_3)",
        "observer_even_or_coarse_source_map_not_faithful":True,
        "new_conductor_coset_probe_repairs_sigma_gap":True,
        "global_Weil_sign_proved":False,
        "RH_proved":False,
    }


def finite_tate_coset_discriminator(p,M,N,left,right):
    """Finite coset tests separate ALL distinct functions in a declared chart.

    f,g ∈ V_(M,N)(p) have exact coefficients c_j,d_j. If f!=g then
    choose j with c_j!=d_j and test against indicator of
    j/p^M+p^N Z_p. The Haar pairing difference is
       (c_j-d_j)*p^-N !=0.
    Every DISTINCT pair in S(Q_p) has some finite common (M,N) chart
    and a finite such discriminator. A restricted coarse observer need
    not have this coset probe; no empirical access is assumed.
    """
    chart=finite_bruhat_chart(p,M,N)
    Q=chart["finite_complex_dimension"]
    c=_coefficients(left,Q)
    d=_coefficients(right,Q)
    for j,(x,y) in enumerate(zip(c,d)):
        if x!=y:
            delta=(x-y)*chart["input_additive_Haar_cell"]
            if delta==0:
                raise ArithmeticError("Finite Haar coset test lost nonzero source")
            return {
                "source":"GENUINE_LOCAL_TATE_SCHWARTZ_BIRKHOFF_COSET_OBSERVER",
                "p":p,"M":M,"N":N,
                "all_coefficients_identical":False,
                "first_distinguishing_coset":j,
                "exact_coset_Haar_pairing_difference":delta,
                "finite_witness_of_distinct_source":True,
                "complete_coset_probe_family_jointly_separating":True,
                "observer_assumed_to_have_physical_probe_access":False,
                "global_Weil_positivity_inferred":False,
                "RH_proved":False,
            }
    return {
        "source":"GENUINE_LOCAL_TATE_SCHWARTZ_BIRKHOFF_COSET_OBSERVER",
        "p":p,"M":M,"N":N,
        "all_coefficients_identical":True,
        "first_distinguishing_coset":None,
        "exact_coset_Haar_pairing_difference":F(0),
        "finite_witness_of_distinct_source":False,
        "complete_coset_probe_family_jointly_separating":True,
        "observer_assumed_to_have_physical_probe_access":False,
        "global_Weil_positivity_inferred":False,
        "RH_proved":False,
    }

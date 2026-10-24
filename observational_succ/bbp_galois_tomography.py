"""Exact p-free Galois tomography of the FULL BBP prime-birth window.

Unlike an untwisted Gauss period, W_a includes the authentic rational
complementary phases. Their finite denominators are coprime to p, so
conjugating zeta_p while FIXING their cyclotomic field is legitimate.

Trace / second moment: classical root-of-unity orthogonality, not
selected-embedding cancellation. Finite p=97 certified outlier:
a=1 has squared normalized amplitude > twice the Galois RMS squared.
No pi normality theorem or Galois independence assumption is imported.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb, gcd, lcm

from .bbp_prime_window_projection import (
    window_parameters, source_complement_window,
)
from .bbp_cyclotomic_birth import (
    forced_states, construct_coprime_clock_counterfeit, counterfeit_upper,
)
from .bbp_prime_window_signed_intervals import (
    box_phase, box_modulus_squared_interval,
)


def _integer(n: int) -> int:
    if type(n) is not int:
        raise ValueError("integer Fourier index required")
    return n


def _natural(n: int,minimum: int=0) -> int:
    if type(n) is not int or n<minimum:
        raise ValueError(f"integer >= {minimum} required")
    return n


def source_field_conductor(p: int) -> int:
    """LCM of ALL p-free rational phase denominators in the actual window."""
    w=source_complement_window(p)
    q=1
    for phase in w:
        q=lcm(q,phase.denominator)
    if gcd(q,p)!=1:
        raise AssertionError("p-free complementary field was not p-free")
    return q


def source_galois_window(p: int,h: int=1) -> dict:
    """Typed (p, L, B, Delta, h, p-free phase list, distinct p exponents)."""
    _integer(h)
    m,L,delta,B=window_parameters(p)
    if h%p==0:
        raise ValueError("nontrivial modulo-p Fourier character required")
    w=source_complement_window(p)
    z=tuple(4*h*pow(16,s,p)%p for s in range(L))
    if len(set(z))!=L or any(x==0 for x in z):
        raise AssertionError("p-subgroup time labels collapsed")
    if any(phase.denominator%p==0 for phase in w):
        raise AssertionError("p-free hypothesis lost")
    return {"p":p,"m":m,"L":L,"B":B,"delta":delta,"h":h,
            "p_exponents":z,"complement":w}


def rational_cyclotomic_group_ring_moment(p: int,h: int=1) -> dict:
    """EXACT algebraic full twisted second moment, no trig or floats.

    Coefficients of formal [q] for q in Q/Z in
      sum_(a!=0)|W_a|² = p*sum_s|V_s|² - |sum_s V_s|²
    are compared by two *distinct* finite enumerations:
      pairwise Ramanujan coefficients (p-1 if equal p-phase else -1),
      versus complete-L coset block convolution.
    Their evaluation in cyclotomic K_p is then exactly the claimed
    Galois trace formula. Arithmetic identities hold even before
    quotienting by the cyclotomic polynomial of the complement.
    """
    inp=source_galois_window(p,h)
    L,B,delta=inp["L"],inp["B"],inp["delta"]
    w=inp["complement"]
    # Left: integrate every character of the LOCAL p-primary field.
    left={}
    for i in range(delta):
        for j in range(delta):
            k=(h*(w[i]-w[j]))%1
            coef=inp["p"]-1 if (i-j)%L==0 else -1
            left[k]=left.get(k,0)+coef
    # Right: independently expand p*sum_s|V_s|²-|sum_s V_s|².
    # Do the negative GLOBAL convolution first, then the positive
    # COMPLETE BLOCK convolution. No use of local-time equality gate.
    right={}
    for phase_i in w:
        for phase_j in w:
            k=(h*(phase_i-phase_j))%1
            right[k]=right.get(k,0)-1
    for s in range(L):
        block=[w[b*L+s] for b in range(B)]
        for phase_i in block:
            for phase_j in block:
                k=(h*(phase_i-phase_j))%1
                right[k]=right.get(k,0)+p
    left={k:v for k,v in left.items() if v}
    right={k:v for k,v in right.items() if v}
    if left!=right:
        raise AssertionError("relative Galois orthogonality failed")
    return {"p":p,"L":L,"B":B,"Delta":delta,
            "signed_group_ring_terms":len(left),
            "coefficient_l1":sum(abs(x) for x in left.values()),
            "same_p_residue_pair_count":delta*B,
            "total_pair_count":delta*delta}


def galois_exception_fraction_bound(p: int,threshold: Q) -> Q:
    """Every possible p-free complementary source: exact Markov fraction.

    Among a in Fp* the proportion with |W_a|/Delta >= eps is <=
      min(1, p/((p-1)*L*eps²)).
    This says NOTHING pointwise about the source-selected a=1.
    """
    if type(threshold) not in (int,Q) or Q(threshold)<=0:
        raise ValueError("positive rational amplitude threshold required")
    inp=source_galois_window(p)
    eps=Q(threshold)
    return min(Q(1),Q(p,(p-1)*inp["L"])/(eps*eps))


def _box_sum(boxes):
    total=[Q(),Q(),Q(),Q()]
    for row in boxes:
        for i in range(4):
            total[i]+=row[i]
    return tuple(total)


def source_selected_galois_outlier_interval(p: int,h: int=1,
                                            terms: int=14,
                                            arctan_terms: int=26):
    """Certified selected |W_1/Delta|² lower and Galois RMS² upper.

    Exact rational phase inputs; Machin/arctangent and cosine Taylor
    bounds from the parent's independent interval oracle.
    Only small N accepted so CI does not generate huge rational exponents.
    """
    _integer(h);_natural(terms,1);_natural(arctan_terms,1)
    inp=source_galois_window(p,h)
    L,B,delta=inp["L"],inp["B"],inp["delta"]
    if delta>54:
        raise ValueError("finite complex interval budget requires Delta<=54")
    states=forced_states(4*inp["m"])
    selected_box=_box_sum(box_phase(h*states[inp["m"]+t],
                                    terms,arctan_terms)
                          for t in range(delta))
    lower_sq,_=box_modulus_squared_interval(selected_box)
    selected_lower=lower_sq/(delta*delta)

    w=inp["complement"]
    # Each V_s=sum_(b<B)e(h*w_(bL+s)).
    # |V_s|²=B+2*sum_(b<c)cos(2*pi*h*(w_b-w_c)).
    # Sum over s and enclose only the cos REAL coordinate.
    sumV2_lo=Q(delta)
    sumV2_hi=Q(delta)
    for s in range(L):
        for b in range(B):
            for c in range(b+1,B):
                box=box_phase(h*(w[b*L+s]-w[c*L+s]),
                              terms,arctan_terms)
                sumV2_lo+=2*box[0]
                sumV2_hi+=2*box[1]
    if sumV2_lo<0 and sumV2_hi<0:
        raise AssertionError("cyclotomic sum of squared amplitudes negative")
    sumV2_lo=max(Q(),sumV2_lo)
    sumV2_hi=max(Q(),sumV2_hi)
    # Exact RMS formula subtracts |sum_s V_s|² >=0;
    # dropping it gives a sound slightly larger rational upper.
    rms_upper=min(Q(1),Q(p,(p-1)*delta*delta)*sumV2_hi)
    if selected_lower>1 or rms_upper<0:
        raise AssertionError("invalid complex enclosure")
    return {"p":p,"h":h,"L":L,"Delta":delta,
            "selected_normalized_amplitude_sq_lower":selected_lower,
            "galois_mean_square_upper":rms_upper,
            "subgroup_weight_squares_bracket":(sumV2_lo,sumV2_hi),
            "selected_over_twice_rms_certified":
                selected_lower>2*rms_upper}


def prime_free_single_rule_counterexample(p: int,padding: int=4) -> dict:
    """One-dimensional autonomous p-free complement can RESONATE.

    For the exact source-independent countercontrol of parent CBCW-07,
    choose x=4/p+s/Q with Q odd coprime p and |x|<=1/(2Q).
    Then w_t=16^t*s/Q (all denominators p-free), and selected
    |sum_(t<Delta)e(16^t*x)|/Delta >=1-error/Delta.
    The fake orbit uses the tiniest UNFORCED rule, not authentic BBP r(n).
    Galois RMS still has at most p/((p-1)*L); no contradiction.
    """
    _natural(padding)
    inp=source_galois_window(p)
    alpha,q=construct_coprime_clock_counterfeit(p,inp["delta"],padding)
    if q%p==0:
        raise AssertionError("fake complement p-free conductor lost")
    bound=counterfeit_upper(inp["delta"],q)
    lower=Q(1)-bound/inp["delta"]
    if lower <= 0:
        raise AssertionError("near-resonant source bound was not positive")
    # M <= p/[(p-1)L]*Delta² and W_1/Delta >= lower.
    # Thus selected exceptional amplification A >=
    # lower²*(p-1)*L/p. This approaches L as Q becomes huge.
    amplification_lower=lower*lower*Q((p-1)*inp["L"],p)
    return {"p":p,"Delta":inp["delta"],"L":inp["L"],
            "denominator":q,"phase":alpha,
            "selected_normalized_amplitude_lower":lower,
            "universal_galois_rms_sq_upper":Q(p,(p-1)*inp["L"]),
            "exceptional_amplification_lower":amplification_lower}

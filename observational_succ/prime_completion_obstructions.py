"""Source-indexed p-adic phantom fixed points and DNR closed-set Hilbert shadow.

PAPER PROOF: every finite residue of excluded source n=0 has legitimate positive
source representative p^r; across all r the p-adic limit is forbidden n=0.
The binary DNR tree embeds as a nonempty closed K subset Z_2 with no
computable points (classical), and Haar(K)=0 by infinitely many forced digits.
Finite tests are bounded; no infinite point construction or physical model.
"""
from __future__ import annotations

from fractions import Fraction as Q
from .effective_field_gates import (
    diagonal_tree_admissible, diagonal_tree_level_witness,
    bounded_self_output, encode_counter_program,
)
from .classical_tate_window import TateWindow, TateWindowError, is_prime


def _natural(n: int, *, maximum: int = 10000) -> int:
    if type(n) is not int or n < 0 or n > maximum:
        raise TateWindowError("Exact nonnegative index within declared finite budget required")
    return n


def phantom_zero_stage(p: int, r: int, m: int) -> dict:
    """Genuine source n=p^r and excluded p-adic limit zero share mod p^r."""
    if not is_prime(p):
        raise TateWindowError("A genuine prime is required")
    _natural(r, maximum=20)
    if not r:
        raise TateWindowError("A positive observation precision is required")
    _natural(m, maximum=100000)
    if m < 2:
        raise TateWindowError("Use a genuinely nonidentity multiplier m>=2")
    N=p**r
    source_n=N
    chart_x=source_n-1
    phantom_chart=(-1)%N
    assert chart_x%N==phantom_chart
    actual_after=m*source_n
    transported=(m*chart_x + (m-1))%N
    assert transported==phantom_chart
    assert (m*(-1)+(m-1))==-1
    return {"prime":p,"precision":r,"modulus":N,
            "actual_source_n":source_n,"actual_source_positive":True,
            "actual_after_multiplication":actual_after,
            "phantom_n":0,"phantom_n_in_source":False,
            "source_chart_residue":chart_x%N,
            "phantom_chart_residue":phantom_chart,
            "all_multipliers_fix_the_formal_chart_point_minus_one":True,
            "finite_modular_observation_separates_actual_source_from_phantom":False,
            "original_source_has_nontrivial_multiplicative_fixed_point":False}


def cantor_digit_to_integer(bits: tuple[int,...]) -> int:
    if (type(bits) is not tuple or any(type(x) is not int or x not in (0,1) for x in bits)):
        raise TateWindowError("Finite canonical 2-adic source digit tuple required")
    return sum(b<<i for i,b in enumerate(bits))


def integer_to_cantor_digits(x: int, n: int) -> tuple[int,...]:
    _natural(n,maximum=48)
    _natural(x,maximum=2**48)
    return tuple((x>>i)&1 for i in range(n))


def idealhard_2adic_stage(n: int) -> dict:
    """Finite clopen C_n subset Z_2 from a *real* constrained source tree.

    Resource cap 0<=n<=7 makes enumeration honest and finite. The
    unbounded closed-set theorem is an independent paper derivation.
    """
    _natural(n,maximum=7)
    allowed=tuple(x for x in range(1<<n)
                  if diagonal_tree_admissible(integer_to_cantor_digits(x,n)))
    if not allowed:
        raise AssertionError("The classical DNR tree unexpectedly has an empty level")
    forced=tuple(i for i in range(n) if bounded_self_output(i,n) is not None)
    expected=1<<(n-len(forced))
    if len(allowed)!=expected:
        raise AssertionError("The exact finite independent-coordinate count failed")
    return {"level":n,"modulus":1<<n,"admissible_residues":allowed,
            "forced_digit_positions":forced,"admissible_count":len(allowed),
            "real_haar_mass":Q(len(allowed),1<<n),
            "infinite_source_path_computed":False}


def idealhard_2adic_packet(n: int):
    """Actual Schwartz-Bruhat cylinder indicator on Z_2, normalized Haar."""
    if n < 1:
        raise TateWindowError("Conductor-positive Fourier control required")
    data=idealhard_2adic_stage(n)
    win=TateWindow(2,0,n)
    vector=win.vector(tuple(int(j in data["admissible_residues"]) for j in range(win.size)))
    return win,vector


def padded_immediate_halt_indices(how_many: int) -> tuple[int,...]:
    """Explicit infinite effective family of distinct immediately halting programs.

    Program HALT followed by k syntactically valid unreachable HALTs:
    every such program halts instantly regardless of its self-input.
    """
    _natural(how_many,maximum=64)
    codes=tuple(encode_counter_program(((0,),)*(k+1)) for k in range(how_many))
    assert len(set(codes))==len(codes)
    return codes


def idealhard_prime_bridge_probe() -> dict:
    phantom=phantom_zero_stage(3,3,7)
    stages=[idealhard_2adic_stage(n) for n in range(1,7)]
    for older,newer in zip(stages,stages[1:]):
        assert {j % older["modulus"] for j in newer["admissible_residues"]}.issubset(
            older["admissible_residues"])
        assert newer["real_haar_mass"]<=older["real_haar_mass"]
    w,f=idealhard_2adic_packet(5)
    ww=TateWindow(2,5,0)
    assert w.inner(f,f)==ww.inner(w.fourier(f),w.fourier(f))
    assert w.inner(f,f)==w.additive_integral(f)
    halts=padded_immediate_halt_indices(4)
    for e in halts:
        assert bounded_self_output(e,1)==e%2
    return {"kind":"CLASSICAL_PRIME_COMPLETION_OBSTRUCTIONS_RECEIPT",
            "unit_origin_phantom_stage":phantom,
            "idealhard_2adic_finite_haar_masses":[str(x["real_haar_mass"]) for x in stages],
            "idealhard_2adic_stage_counts":[x["admissible_count"] for x in stages],
            "idealhard_2adic_nested_residue_constraints":True,
            "idealhard_cylinder_exact_fourier_parseval":True,
            "explicit_immediately_halting_program_indices":list(halts),
            "closed_set_nonempty_proved_in_code":False,
            "global_computable_2adic_path_constructed":False,
            "global_haar_zero_claim_backed_by_paper_padding_proof":True,
            "completed_Weil_positivity_or_RH_proved":False}

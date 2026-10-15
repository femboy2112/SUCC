"""Source-compatible gluing: finite recursive proof versus ghost couplings.

These are EXACT rational mathematical controls showing:
  * a finite recursive positive law CAN prove an all-stage global sign
    without physically evaluating every matrix (SimpleField proof shape);
  * separate PSD old/new blocks NEVER suffice without the cross Schur
    and singular source range gate (FuckedField gluing obstruction);
  * independent positive/negative source feature births can cancel on
    old observations, so missing coupled source transport is real debt.

All matrices here are explicitly SYNTHETIC, never original zeta Weil G.
The authentic low Schur A-R0 remains unknown for RH.
"""
from __future__ import annotations

from fractions import Fraction as F


class FieldGluingError(ValueError):
    pass


def _q(x):
    if type(x) not in (int,F):
        raise FieldGluingError("Exact rational source scalar required")
    return F(x)


def exact_scalar_schur_gluing(parent, cross, newborn, *,
                              parent_source="SYNTHETIC_SOURCE",
                              child_source="SYNTHETIC_SOURCE"):
    """Exact 2x2 block PSD with singular-parent Moore-Penrose firewall.

    M=[[A,B],[B,D]]. For A>0, PSD iff D-B²/A>=0.
    For A=0, PSD iff B=0 and D>=0. This is the smallest valid
    source-indexed extension theorem. It demonstrates why old/new
    individual positivity is not enough and why range matters.
    """
    a,b,d=map(_q,(parent,cross,newborn))
    if type(parent_source) is not str or type(child_source) is not str:
        raise FieldGluingError("Declared nonblank source stamps are mandatory")
    if not parent_source or not child_source or parent_source!=child_source:
        raise FieldGluingError("SOURCE_STAMP_MISMATCH: no lawful gluing")
    if a<0:
        raise FieldGluingError("A negative parent cannot be called PSD")
    singular=a==0
    range_condition=(not singular or b==0)
    schur=d-b*b/a if a else (d if b==0 else None)
    is_psd=(d>=0 and range_condition and (schur is not None and schur>=0))
    det=a*d-b*b
    assert is_psd==(a>=0 and d>=0 and det>=0)
    return {
        "source":"SYNTHETIC_SCALAR_SOURCE_GLUING",
        "parent_A":a,"cross_B":b,"new_D":d,
        "principal_determinant":det,
        "parent_singular":singular,
        "cross_in_parent_range":range_condition,
        "true_schur_when_defined":schur,
        "separate_parent_and_newborn_PSD":a>=0 and d>=0,
        "complete_block_PSD":is_psd,
        "source_stamps_equal":True,
        "original_zeta_G_or_Weil_identified":False,
        "RH_proved":False,
    }


def recursive_positive_gram_stage(n, coupling=F(1,2)):
    """Finite name for uniform ALL-n positive source law G_n=L_n L_n*.

    L_n=I+t S_n (lower bidiagonal, shift to next coordinate). As n grows,
    top-left truncation of G_(n+1) agrees with G_n. For INFINITE
    L=I+tS on ell², ||L* x|| >=(1-|t|)||x|| when |t|<1,
    so G=LL* >=(1-|t|)² I globally. One symbolic proof covers ALL n.
    Finite matrices here only calibrate the algebra.
    """
    if type(n) is not int or not 1<=n<=20:
        raise FieldGluingError("Test matrix cutoff 1<=n<=20")
    t=_q(coupling)
    if not -1<t<1:
        raise FieldGluingError("A uniform nonzero gap requires |t|<1")
    L=tuple(tuple(F(1) if i==j else (t if i==j+1 else F())
                  for j in range(n)) for i in range(n))
    G=tuple(tuple(sum((L[i][k]*L[j][k] for k in range(n)),F())
                  for j in range(n)) for i in range(n))
    explicit=tuple(tuple(
        (F(1) if i==0 else F(1)+t*t) if i==j
        else (t if abs(i-j)==1 else F())
        for j in range(n)) for i in range(n))
    if G!=explicit:
        raise ArithmeticError("Recursive signed source law does not match exact Gram")
    # Finite n source law yields an ALL-n theorem through infinite shift norm,
    # not from enumerating finitely many tested n.
    return {
        "source":"SYNTHETIC_RECURSIVE_BIDIAGONAL_GLOBAL_LAW",
        "size_n":n,
        "finite_L_matrix":L,
        "finite_G_matrix":G,
        "exact_factorization_G_equals_L_Lstar":True,
        "all_n_compatible_prefix_law_by_formula":True,
        "infinite_law":"G=(I+t*S)(I+t*S)* on ell2",
        "uniform_infinite_positive_gap":(1-abs(t))**2,
        "proof":"||L* x|| >= (1-|t|)||x||, |t|<1",
        "all_infinite_matrices_physically_evaluated":False,
        "original_zeta_Weil_sign_proved":False,
        "RH_proved":False,
    }


def paired_neutral_source_birth(plus,minus,birth):
    """APOLLO K5 control: both feature channels gain equal positive energy.

    The net signed old-window observable is UNCHANGED, though neither
    positive/negative feature object is unchanged. No exact all-a source
    contraction is inferred from that visible neutrality.
    """
    p,m,w=map(_q,(plus,minus,birth))
    if p<0 or m<0 or w<=0:
        raise FieldGluingError("Two PSD channel energies and a positive birth required")
    return {
        "source":"SYNTHETIC_CALIBRATION_OF_ACTUAL_APOLLO_PAIRED_BIRTH",
        "old_signed_source_value":p-m,
        "new_positive_feature_energy":p+w,
        "new_negative_feature_energy":m+w,
        "new_signed_source_value":(p+w)-(m+w),
        "signed_old_window_unchanged":True,
        "both_feature_carriers_changed":True,
        "independent_feature_nesting_is_not_a_contraction_proof":True,
        "original_source_a_genuine_all_radii_contraction_proved":False,
        "RH_proved":False,
    }

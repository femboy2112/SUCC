"""Executable finite shadows of infinite, *separately proved* completion models.

These constructors NEVER infer an omega theorem from a bounded computation. They
return exact finite witnesses useful for falsification and demonstration only.
"""
from __future__ import annotations
from dataclasses import dataclass


class LimitError(ValueError):
    pass


OMEGA="<ideal boundary source>"


def delayed_rival_shadow(probe_index:int,source:int|str)->int:
    """Indicator that source is EXACTLY positive integer probe_index.

    OMEGA has all-zero reports, positive source k has one at probe k. At
    every finite prefix the sources OMEGA and any k outside it are aliased;
    across ALL k>=1 they are distinguishable. (Written theorem, not code.)
    """
    if type(probe_index) is not int or probe_index < 1:
        raise LimitError("Positive probe number required")
    if source!=OMEGA and (type(source) is not int or source<1):
        raise LimitError("Source must be a positive integer or distinguished boundary")
    return int(source==probe_index)


def omega_rival_at_horizon(horizon:int)->dict:
    """Witness target ambiguity under a finite prefix, never omega acceptance."""
    if type(horizon) is not int or horizon<0:
        raise LimitError("Nonnegative stage")
    rival=horizon+1
    reports=tuple(range(1,horizon+1))
    if any(delayed_rival_shadow(i,OMEGA)!=delayed_rival_shadow(i,rival) for i in reports):
        raise AssertionError("Claimed dark pair unexpectedly resolved")
    return {"status":"FINITE_PREFIX_INSUFFICIENT", "boundary_source":OMEGA,
            "rival":rival,"first_distinguishing_probe":rival,"checked_prefix":horizon}


def unrealizable_limit_prefix(horizon:int)->dict:
    """For X=N>=1 and p_n(k)=1 if k<=n else 0, all-zero prefixes are
    each realizable by k>n; all-zero INFINITE report has no source in N.
    """
    if type(horizon) is not int or horizon<0:
        raise LimitError("Nonnegative finite horizon")
    witness=horizon+1
    actual=tuple(int(witness<=n) for n in range(1,horizon+1))
    assert actual==(0,)*horizon
    return {"finite_all_zero_history":actual,"finite_realizing_source":witness,
            "infinite_report_realizable":False,
            "infinite_nonrealizability_requires_mathematical_proof":True}


def halting_reduction_probe(program_halted_by_stage:bool,source:int)->int:
    """One finite observation of halting-based reduction on source {0,1}.

    Not an oracle for the halting problem. The written reduction defines
    p_n(0)=0 and p_n(1)=1 iff target program halts WITHIN n operations.
    """
    if type(source) is not int or source not in (0,1) or type(program_halted_by_stage) is not bool:
        raise LimitError("Must provide a finite bounded-halting oracle result")
    return source*int(program_halted_by_stage)


def partition_refinement_depth(source_size:int,strict_refinements:int)->bool:
    """Elementary bound: at most N-1 strict refinements of N-point partition.

    This bounds COUNT of strict changes, not WHEN those changes occur.
    """
    if any(type(i) is not int or i<1 for i in (source_size,strict_refinements+1)):
        raise LimitError("Finite positive source and nonnegative refinement count")
    return strict_refinements <= source_size-1


def cantor_real_target_prefix(depth:int)->dict:
    """Cantor source {0,1}^N, T(x)=sum_{k>=1} 2^-k x_k (continuous).

    The first 'depth' coordinate reports determine T to error <=2^-depth,
    but never determine it exactly for all sources. Countermodel flips the
    next bit after the already observed zero prefix.
    """
    from fractions import Fraction
    if type(depth) is not int or not 0<=depth<=200:
        raise LimitError("Finite depth 0..200 required")
    return {"depth":depth,"max_tail_span":Fraction(1,2**depth),
            "same_prefix_target_gap_witness":Fraction(1,2**(depth+1)),
            "status":"FINITE_APPROXIMATION_NOT_EXACT_IDENTIFICATION",
            "infinite_source_space_required":True}

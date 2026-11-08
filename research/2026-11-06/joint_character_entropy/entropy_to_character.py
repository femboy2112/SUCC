"""Numerical diagnostics for the rigorously proved J19 entropy→Weyl inequality.

Uses floating Shannon entropies: these diagnostics DO NOT certify a sharp finite
bound by themselves. Exact signed-Weyl intervals come from signed_certificate.py.
"""
from __future__ import annotations
import math
from typing import Sequence
from joint_entropy import block_entropy,h_binary


def source_clock_character_bound(output_segment: Sequence[int], *, k:int,L:int,h:int,
                                 source_period:int=7,observer_states:int=16,base:int=16)->dict:
    """J19 RHS using output L-block entropy; M=N-k+1 decoded phases.

    Input must be the actual causal output stream and the source declared
    periodic of source_period.  The function cannot itself verify provenance.
    """
    N=len(output_segment)
    if (not(1<=k<=L<=N) or L%k or abs(h)>=base**k or h==0 or
        source_period<1 or observer_states<1 or base<2):
        raise ValueError('invalid J19 domain')
    A=N-k+1
    epsilon=(L-k)/A
    deficit=L*math.log(base)-block_entropy(output_segment,L)
    debt=(k/L)*(deficit+math.log(source_period*observer_states))
    debt+=h_binary(epsilon)+epsilon*k*math.log(base)
    # Pi upper bound 22/7, used instead of numerical math.pi for the cell term.
    rhs=math.sqrt(2*max(0,debt))+2*(22/7)*abs(h)/(base**k)
    return {'A':A,'k':k,'L':L,'h':h,'observed_block_deficit':deficit,
            'input_deficit_bound':debt,'rhs_diagnostic':rhs,
            'nonvacuous_below_one':rhs<1}

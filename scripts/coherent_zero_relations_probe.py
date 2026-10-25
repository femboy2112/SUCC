#!/usr/bin/env python3
"""SUCC two-basis zero relations + sharp finite-cycle minimax receipts."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from observational_succ.coherent_zero_relations import (
    bbp_zero_balance,bbp_finite_positive_kernel,base16_graph,digit_discrepancy,
    finite_coboundary_minimax,finite_prefix_coboundary,
)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--verify',action='store_true')
    args=p.parse_args()
    proof=bbp_zero_balance()
    graph=base16_graph(17)
    digits=digit_discrepancy(17)
    m=finite_coboundary_minimax(graph,digits)
    fake=finite_prefix_coboundary((Q(1),)*17)
    if args.verify:
        assert proof.check() and len(proof.routes)==2
        assert bbp_finite_positive_kernel(Q(1))==0
        assert bbp_finite_positive_kernel(Q(1,2))>0
        assert m.optimal_uniform_residual==Q(15,16)
        assert all(m.potential[i]-m.potential[graph[i]]+m.residual[i]==digits[i]
                   for i in range(17))
        assert (fake[-1]-fake[0])/17==1
    print(json.dumps({
      'source':'Q:authentic-four-pole-BBP',
      'proof_conditional_on_authenticated_chart':True,
      'polynomial_zero_routes':len(proof.routes),
      'checked_exact_polynomial_identity':proof.check(),
      'endpoint_kernel_at_one':str(bbp_finite_positive_kernel(Q(1))),
      'radix16_fixed_point_digit_zero_discrepancy':str(digits[0]),
      'sharp_global_coboundary_residual':str(m.optimal_uniform_residual),
      'finite_telescoping_counterexample_normalized_boundary':str((fake[-1]-fake[0])/17),
      'pi_normality_proved':False,
      'RH_proved':False,
      'local_verified':args.verify,
    },sort_keys=True,indent=2))


if __name__=='__main__':main()

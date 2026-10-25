#!/usr/bin/env python3
"""Exact Fraction receipts for SUCC two-domain conservative boundary flux."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from observational_succ.conservative_boundary_flux import (
    two_sided_euler_budget, laplacian, graph_port_balance, schur_port,
    dynamic_port_operator, rc_power_balance, nested_information_budget,
    correlated_energy_ledger, two_domain_transport_budget,
    rectangle_curvature, true_prime_product,
)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    scalar=two_sided_euler_budget(2,4,5)
    path=laplacian(3,((0,1,Q(1)),(1,2,Q(1))))
    ports=graph_port_balance(path,(0,2),(1,0,0))
    static=schur_port(path,(0,2))
    dyn1=dynamic_port_operator(path,(0,1,0),(0,2),1)
    dyn2=dynamic_port_operator(path,(0,2,0),(0,2),1)
    rc=rc_power_balance(path,(0,2),(1,Q(1,4),0),(2,))
    nested=nested_information_budget((1,2,3,4),(Q(1,4),)*4,
                       ((0,1,2,3),),((0,1),(2,3)))
    correlation=correlated_energy_ledger((1,1),(2,2),(Q(1,2),)*2)
    bridge=two_domain_transport_budget(((1,2,1),(0,1,1)),(1,2,3),
          ((1,0,0),(0,1,0),(0,0,0)),((1,1),(0,0)))
    fake=true_prime_product(2,11)*Q(36,35)-1
    if args.verify:
        assert scalar.observable_gap==Q(1,9)
        assert rectangle_curvature(2,4,5,7,11)==0
        assert fake>two_sided_euler_budget(2,11,11).succ_above
        assert (ports.raw_energy,ports.port_energy,ports.hidden_energy)==(1,Q(1,2),Q(1,2))
        assert static!=dyn1 and dyn1!=dyn2
        assert rc.boundary_input_power==rc.resistive_dissipation+rc.hidden_storage_rate
        assert (nested.coarse_unresolved,nested.fine_unresolved,nested.visible_innovation)==(Q(5,4),Q(1,4),1)
        assert correlation.cross_term==-4
        assert (bridge.total_squared,bridge.cross_term)==(26,-60)
    print(json.dumps({
       'program':'CBF-source-typed-two-domain-flux',
       'status':'verified' if args.verify else 'not_requested',
       'exact_scalar_gap':str(scalar.observable_gap),
       'scalar_succ_upper':str(scalar.succ_above),
       'scalar_prime_lower':str(scalar.prime_below),
       'static_graph_port_energy':str(ports.port_energy),
       'hidden_graph_energy':str(ports.hidden_energy),
       'dynamic_m1':[[str(v) for v in row] for row in dyn1],
       'dynamic_m2':[[str(v) for v in row] for row in dyn2],
       'physical_power':str(rc.boundary_input_power),
       'physical_dissipation':str(rc.resistive_dissipation),
       'physical_stored_rate':str(rc.hidden_storage_rate),
       'nested_innovation_energy':str(nested.visible_innovation),
       'oblique_two_domain_interaction':str(bridge.cross_term),
       'RH_proved':False,'pi_normality_proved':False,
       'source_physical_authentication':False,
    },indent=2,sort_keys=True))


if __name__=='__main__':
    main()

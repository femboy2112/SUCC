"""Reproducible finite *diagnostic only*: selected and rational changing-seed controls.

No numerical result is treated as an asymptotic theorem or source-independent proof.
"""
from __future__ import annotations
from fractions import Fraction
from math import cos,sin,pi
import json
import importlib.util
from pathlib import Path

P=Path(__file__).with_name('edge_seed_tomography.py')
spec=importlib.util.spec_from_file_location('est',P)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)


def character_sum(values, h:int):
    c=0j
    for u in values:
        # A rational modulo 1, *then* floating real evaluation. Exact rational
        # phase is source-authenticated; complex evaluation is approximate.
        phase=float((h*Fraction(u))%1)
        c+=complex(cos(2*pi*phase),sin(2*pi*phase))
    return c


def report():
    rows=[]
    for N in (16,32,64,128):
        u=a.original_states(N+1)
        K=N+64
        cK=a.bbp_constant_prefix(K)
        for h in (1,3,5,15):
            vertex=character_sum(u[1:N+1],h)
            edge=character_sum((u[n+1]-u[n] for n in range(1,N+1)),h)
            h15=character_sum(u[1:N+1],15*h)
            control=character_sum((u[n]-16**n*cK for n in range(1,N+1)),h)
            bound=a.edge_phase_mismatch(N,h)
            rows.append({
                'N':N,'h':h,
                'selected_vertex_abs_mean':round(abs(vertex)/N,9),
                'selected_edge_abs_mean':round(abs(edge)/N,9),
                'vertex_15h_abs_mean':round(abs(h15)/N,9),
                'edge_minus_15vertex_actual_abs':round(abs(edge-h15),9),
                'edge_minus_15vertex_analytic_upper_2pi_dist':round(2*pi*float(bound),9),
                'rational_seed_control_abs_mean':round(abs(control)/N,9),
                'rational_seed_control_K':K,
            })
    return {'label':'FINITE_DIAGNOSTIC_ONLY_NOT_PI_PROOF',
            'base':'BBP four-pole zero seed and source-preserving changing rational seeds',
            'tomography':{'first_nine_prime':73,'modes':9,'total_channels':73,
                          'D':list(a.difference_set_73()),
                          'ordered_differences':72},
            'alias_free_prime_table':{str(N):a.first_alias_free_prime(N) for N in range(2,15)},
            'measurements':rows}

if __name__=='__main__':print(json.dumps(report(),indent=2))

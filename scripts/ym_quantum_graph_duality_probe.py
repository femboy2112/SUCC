"""Replay finite SUCC/QM graph-Haar gauge witnesses using exact rational sources.

Run from SUCC root:
  python scripts/ym_quantum_graph_duality_probe.py

This is not a theorem prover, Lean replay, or four-dimensional mass-gap result.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

# A complete SUCC checkout need not be pip-installed for this exact probe.
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0,str(_ROOT))

from observational_succ.ym_quantum_graph_duality import (
    s3_group, cyclic_group, HaarSubdivision, simultaneous_conjugacy_orbits,
    burnside_conjugation_orbits, gauge_invariant_density_not_physical,
    new_cycle_haar_detail, conditional_haar_energy,
    physical_spectral_receipt, path_sum, z2_physical_matrix,
    finite_reflection_gram, toy_wilson_factor_graph,
    two_plaquette_source_transport, subdivision_edge_mode_entanglement,
    haar_poincare_transfer,
)
from fractions import Fraction as Q


def _source_sha(name: str) -> str:
    path=Path(__file__).resolve().parents[1] / name
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict:
    g=s3_group()
    group=HaarSubdivision(g)
    f=tuple(range(g.order))
    F=tuple(Q(i*i-3*i+6,5) for i in range(g.order**2))
    orbit_count=len(simultaneous_conjugacy_orbits(g,2))
    assert orbit_count==burnside_conjugation_orbits(g,2)==11
    h=z2_physical_matrix()
    # 16-ary conditional word detail checks SUCC's existing Haar junction format.
    counts=tuple((i*i+7*i+4)%17 for i in range(16**2))
    wavelet=conditional_haar_energy(counts,16,1)
    return {
        "claim_status":"EXACT FINITE CALCULATIONS + PAPER PROOFS; NOT YANG-MILLS CONTINUUM",
        "source_contract":"SUCC PR #614 finite group S3 source and Z2 lattice gauge toy",
        "upstream_succ_main_at_start":"db9fb4b84672050efa79b13377f1e73364598a14",
        "module_sha256":_source_sha('observational_succ/ym_quantum_graph_duality.py'),
        "tests_sha256":_source_sha('tests/test_ym_quantum_graph_duality.py'),
        "S3_subdivision":group.exact_receipt(f,F),
        "S3_joint_two_loop_gauge_orbits":orbit_count,
        "Z2_density_twirl_mutant":gauge_invariant_density_not_physical(),
        "new_Z2_physical_cycle":new_cycle_haar_detail(),
        "SUCC_base16_conditional_haar":{k:(str(v) if isinstance(v,Q) else v)
                                        for k,v in wavelet.items()},
        "S3_edge_mode_entanglement":subdivision_edge_mode_entanglement(g),
        "Z2_edge_mode_entanglement":subdivision_edge_mode_entanglement(cyclic_group(2)),
        "finite_Z2_Hamiltonian":physical_spectral_receipt(),
        "graph_vs_matrix_path_n3":str(path_sum(h,(1,0),(0,1),3)),
        "finite_reflection_positive_Gram":finite_reflection_gram(),
        "toy_Wilson_source":toy_wilson_factor_graph(),
        "nontrivial_RG_source_transport_defect":two_plaquette_source_transport(),
        "physical_margin_linear":haar_poincare_transfer(Q(1,8),"linear"),
        "physical_margin_quadratic":haar_poincare_transfer(Q(1,8),"quadratic"),
        "original_YM_Lean_proof_rebuilt":False,
        "full_SUCC_suite_run_by_this_script":False,
        "YM_mass_gap":"OPEN",
        "warning":"Gauge-invariant Hilbert details, finite positivity and graph path counts are NOT a 4D source-selected mass-gap estimate.",
    }


def main() -> None:
    print(json.dumps(run(),sort_keys=True,indent=2))


if __name__=='__main__':
    main()

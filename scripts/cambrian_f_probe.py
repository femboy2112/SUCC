#!/usr/bin/env python3
"""Emit/replay the exact six-assignment F receipt (not a proof or test runner)."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.cambrian_f_closure import (
    BlockSystem, quantum_backaction_witness, fluid_high_high_witness,
    attention_witness, finite_query_rival, null_probe_constraint_rank,
    scalar_hankel_rank,
)


def exact_json(value):
    if isinstance(value,Q): return str(value)
    if isinstance(value,dict): return {k:exact_json(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)): return [exact_json(v) for v in value]
    return value


def receipt():
    two=BlockSystem(((0,),),((1,1),),((1,),(1,)),
                    ((Q(1,2),0),(0,Q(1,3))),((1,),),((0,),(0,)))
    initial=BlockSystem(((0,),),((1,),),((0,),),((Q(1,2),),),((1,),),((0,),))
    tiny=BlockSystem(((0,),),((1,),),((1,),),((Q(1,2),),),((1,),),((0,),))
    twin=BlockSystem(((0,),),((Q(1,2),Q(1,2)),),((1,),(1,)),
                     ((Q(1,2),0),(0,Q(1,2))),((1,),),((0,),(0,)))
    heldout=((Q(2,7),),(Q(-3,11),),(Q(4,13),),(Q(5,17),),(Q(-7,19),))
    a,b,c=(two.kernel(k)[0][0] for k in range(3))
    files=('observational_succ/cambrian_f_closure.py',
           'observational_succ/quantum_records.py',
           'observational_succ/dynamic_boundary_inverse.py',
           'tests/test_cambrian_f_closure.py')
    assignments=[
        {'id':31,'executed':True,'domain':'finite-dimensional quantum instruments; exact real qubit controls',
         'question':'Does equality of current POVMs determine every future observation law?',
         'quantifiers':'POVM equality for every input density; future inequality at one explicit density',
         'positive':'full outcome/poststate instrument supports causal composition',
         'rival':'same present outcome law suffices for causal closure',
         'probe':'same Z outcome 1, different posterior, then second Z readout',
         'verdict':'rival refuted by exact countermodel; unconditional DPI classical',
         'evidence':quantum_backaction_witness(),
         'postselection_control':{'initial_trace_distance':Q(1,10),'conditioned_trace_distance':Q(25,106)},
         'independent_route':'Kraus completeness/POVM algebra and primary Watrous instrument definitions',
         'limit':'No claim of human quantum cognition or speedup; no finite enumeration over all density matrices'},
        {'id':32,'executed':True,'domain':'finite-dimensional block-linear systems; declared initial/source interface',
         'question':'When does hidden elimination yield exact autonomous closure versus memory?',
         'quantifiers':'every x0, input sequence; separate every z0 versus z0=0 domains',
         'positive':'exact history+initial-forcing law preserves source trajectories',
         'rival':'current resolved state always suffices after eliminating hidden state',
         'probe':'independent full-block powers, hidden-initial variants, nilpotent delays, heldout rate mutation',
         'verdict':'paper proof of sharp finite kernel criterion; physical ontology remains underdetermined',
         'evidence':{'two_rate_closure':two.closure_certificate(),'two_rate_hankel_determinant':a*c-b*b,
                     'finite_kernel_certificate_assumes_known_hidden_dimension':True,
                     'hidden_initial_countermodel':initial.closure_certificate(),
                     'same_boundary_distinct_hidden_counts':[tiny.hidden_dimension,twin.hidden_dimension],
                     'same_heldout_boundary_trajectory':tiny.simulate((Q(3,8),),(0,),heldout)[0]==
                                                        twin.simulate((Q(3,8),),(0,0),heldout)[0],
                     'twin_minimal_kernel_rank':scalar_hankel_rank(twin,4)},
         'independent_route':'inductive elimination proof, 32 rational systems via unpartitioned matrix-power oracle',
         'limit':'Kernel minimality is interface-relative; no physical network/source authentication'},
        {'id':33,'executed':True,'domain':'Lorentz forms in a calibrated coordinate basis; constant-coefficient Maxwell symbol',
         'question':'What geometry is fixed by exact null rays, and which principal modes are physical?',
         'quantifiers':'every symmetric form vanishing on declared rational null rays; each positive conformal scale',
         'positive':'sufficient null evidence determines a conformal class; Maxwell constraints retain transverse modes',
         'rival':'null evidence fixes absolute metric scale and all unconstrained symbol modes are physical',
         'probe':'rational null constraint rank, metric scale mutation, timelike normalization, longitudinal symbol control',
         'verdict':'paper conformal theorem and exact scale/longitudinal countermodels',
         'evidence':{'constraint_rank_and_metric_coordinates':null_probe_constraint_rank(3),
                     'same_null_cone_scales':[1,4],'timelike_squared_lengths':[-1,-4],
                     'maxwell_transverse_multiplier_xi_2_3_6_speed_2':196},
         'independent_route':'entrywise rational ray proof, exact matrix constraint rank and symbol square',
         'limit':'No general manifold boundary-rigidity theorem without causality/observation hypotheses'},
        {'id':34,'executed':True,'domain':'smooth divergence-free 2D torus initial states; cutoff |k|<=1; Leray projection',
         'question':'Can every projected NS vector field be an instantaneous function of resolved velocity alone?',
         'quantifiers':'every integer N>=2 provides a high-high countermodel; all smooth source states is the refuted domain',
         'positive':'nonlinear stress/hidden information is needed for exact closure',
         'rival':'P w=0 entails no projected nonlinear acceleration',
         'probe':'high-high difference q=(0,1), then pressure-removing Leray projector',
         'verdict':'exact filtered identity; universal instantaneous closure refuted on specified interface',
         'evidence':fluid_high_high_witness(7),
         'independent_route':'trigonometric calculation and independent rational Fourier convolution at heldout N=4,11,23',
         'limit':'No continuum finite-memory theorem, 3D NS regularity claim, or rejection of restricted/statistical closure'},
        {'id':35,'executed':True,'domain':'finite adaptive point-query access to computable Boolean sequences; finitary theories',
         'question':'Does finite all-clear query evidence certify an all-n sentence or add proof authority at omega?',
         'quantifiers':'every finite stopping transcript on the all-one source admits a computable single-hole rival',
         'positive':'extra structural authority can prove universally; finite black-box observations cannot',
         'rival':'finite all-clear observations certify universal truth/unprovability by themselves',
         'probe':'freeze adaptive query transcript then introduce a computable hole outside its support',
         'verdict':'paper finite-query no-go; finite support/dovetail boundaries retained',
         'evidence':finite_query_rival(tuple(range(1024))),
         'independent_route':'adaptive transcript induction plus exact set replay and structural algebraic positive control',
         'access_gap':'PA representability/reflection formalization not implemented',
         'limit':'No inference of RH/NS independence or actual infinite elapsed computation'},
        {'id':36,'executed':True,'domain':'declared finite phenomenological attention-policy toy',
         'question':'Does current belief determine future attention/probes/source-relative revision?',
         'quantifiers':'all four (belief,protection) toy states and both fixed source bits; no empirical quantifier',
         'positive':'retaining policy state repairs causal sufficiency and distinguishes availability from selection',
         'rival':'same present belief guarantees same next update',
         'probe':'same belief with different protection, then release intervention followed by reveal',
         'verdict':'finite model counterexample; typed TLICA interface proposed only',
         'evidence':attention_witness(),
         'independent_route':'complete finite transition-table witness and both-source policy replay',
         'access_gap':'No current external TLICA repository audit or empirical calibration',
         'limit':'No neuroscience, psychiatric mechanism, physical-law claim, or combined truth score'},
    ]
    return exact_json({'schema':'cambrian_f_results_v1','base_commit':'5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
        'worker_count':1,'assignment_count':6,'assignment_ids':[31,32,33,34,35,36],
        'proof_kind':'paper proofs plus exact finite executable controls; no new Lean theorem',
        'novelty':'classical mathematics; new-to-project synthesis; academic priority unestablished',
        'independence':'initial conclusion message sent before cross-pollination; same-model workers are not external referees',
        'source_hashes':{f:sha256((ROOT/f).read_bytes()).hexdigest() for f in files},
        'assignments':assignments,
        'primary_sources':[
            'https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf',
            'https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf',
            'https://arxiv.org/abs/1611.03311',
            'https://doi.org/10.1103/PhysRevFluids.2.014604',
            'https://arxiv.org/abs/1611.02143',
            'https://arxiv.org/abs/1405.3386',
            'https://doi.org/10.1007/BF01700692',
            'https://www.astro.puc.cl/~rparra/tools/PAPERS/turing_1936.pdf']})


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--check',action='store_true')
    args=p.parse_args()
    out=receipt()
    if args.check:
        frozen=json.loads((ROOT/'research/2026-10-13/cambrian_f_results.json').read_text())
        if out!=frozen: raise SystemExit('cambrian F frozen receipt differs from exact replay')
        print('cambrian F: all six assignments and source hashes replay exactly')
    else:
        print(json.dumps(out,indent=2,sort_keys=True))

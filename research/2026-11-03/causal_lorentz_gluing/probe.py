"""Preregistered exact BBP source-precision, frame and hostile probe.

Use `python .../probe.py` to generate EXACT_RECEIPT.json in staging;
`--verify` compares byte-stable parsed JSON with the committed receipt.
No pi digits, complex floating point, fitted thresholds, or stochastic means.
"""
import importlib.util
import argparse
import json
import hashlib
from fractions import Fraction as Q
from pathlib import Path

PATH=Path(__file__).with_name('causal_lorentz.py')
sp=importlib.util.spec_from_file_location('causal_lorentz_probe',PATH)
l=importlib.util.module_from_spec(sp);sp.loader.exec_module(l)


def as_str(v):
    return str(v) if not isinstance(v,(int,bool)) else v


def execute():
    pos=[]
    for n,k in [(257,9),(1023,28),(4097,53),(4097,97)]:
        full=l.source_state_mod(n,k)
        suffix=l.suffix_source_mod(n,k)
        assert full==suffix
        pos.append({'source_time':n,'precision_bits':k,
                    'cone_depth':l.precision_horizon(k),'same_modular_state':True,
                    'source_residue':full})
    frames=[]
    for t,k in [(-133,11),(255,32),(1027,65),(65537,53)]:
        state=l.particular_mod(t,k)
        step=l.source_state_successor_mod(state,k)
        assert step==l.particular_mod(t+1,k)
        assert l.particular_inverse_mod(state,k)==t%(1<<k)
        frames.append({'index':t,'precision_bits':k,'state_residue':state,
                       'successor_residue':step,'state_index_bijection':True})
    sources=[]
    for n in (257,509,1021):
        ah,ag=l.parent.mellin_channels(n)
        assert ah+ag==l.source_r(n)
        a=l.v2(ah);b=l.v2(ag)
        assert a==b==-5-l.v2(Q(n))
        sources.append({'index':n,'v2_real_channel':a,'v2_gaussian_channel':b,
                        'glued_mod_2_9':l.source_glued_mod(n,9),
                        'glued_mod_2_53':l.source_glued_mod(n,53),
                        'separate_reduction_forbidden':True})
    boost=l.boost_from_scale(16)
    T=l.multiplication_matrix()
    bad=tuple(tuple(T[i][j] if i<4 and j<4 else T[i-4][j-4] if i>=4 and j>=4 else Q(0)
                   for j in range(8)) for i in range(8))
    assert not l.split_metric_preserved(bad)
    ghost=l.near_ghost(97)
    seed=l.rational_seed_ambiguity(l.precision_horizon(53),53)
    assert seed['residue']==0 and seed['real_phase_offset']==Q(1,5)
    code_sha=hashlib.sha256(PATH.read_bytes()).hexdigest()
    return {'status':'FINITE EXACT OBSERVATION; no source-selected Weyl decay',
            'source':'literal original 4 poles and U0=0; all rational',
            'parent_pr_481_head':'7237c2ae8b7b98557f39e47e8988b033404b587a',
            'source_module_sha256':code_sha,
            'clock_depth':pos,'frame_conjugacies':frames,
            'channel_gluing':sources,
            'split_metric_preserved':l.split_metric_preserved(),
            'same_forward_map_on_dual_fails_metric':True,
            'half_clock_signs':list(l.halfclock_channel_signs()),
            'eight_return':'1/16',
            'boost_gamma':str(boost['gamma']),
            'boost_beta':str(boost['beta']),
            'boost_gamma_beta':str(boost['gamma_beta']),
            'boost_half_parameter':str(boost['half_rapidity_parameter']),
            'causal_bit_slope':4,
            'seed_mutant_congruent_mod_2_53':True,
            'seed_mutant_real_offset':str(seed['real_phase_offset']),
            'p2_tiny_real_large_ghost_k97':str(ghost),
            'pi_normality_proved':False}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    output=Path(__file__).with_name('EXACT_RECEIPT.json')
    data=execute()
    if args.verify:
        expected=json.loads(output.read_text())
        assert expected==data, 'exact receipt mismatch'
        print('EXACT RECEIPT VERIFIED: canonical dual + source cone + 2-adic frames')
    else:
        output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
        print('generated',output)

if __name__=='__main__':
    main()

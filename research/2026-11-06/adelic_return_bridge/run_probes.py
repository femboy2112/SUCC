"""Deterministic finite controls; actual original four-pole zero-seed only."""
from __future__ import annotations
import json
from bridge import (raw_phases, exact_return_witness,
                    normalized_phase_diagnostics, return_fiber_energy_float,
                    source_return_sum_mod, v_padic_mod)

def run():
    states,carries=raw_phases(2240)
    returns=[exact_return_witness(states,carries,k) for k in (9,10,11)]
    assert all(q['n']==128 and q['unwrapped_residues_equal'] for q in returns)
    recon=[{'n':n,'denominator_bits':states[n].denominator.bit_length(),
            'fractional_numerator_bits':states[n].numerator.bit_length(),
            'integer_carry_bits':carries[n].bit_length()} for n in (73,149,293,587)]
    rs=[normalized_phase_diagnostics(states,carries,k) for k in (9,10)]
    energy=[return_fiber_energy_float(states,k,M) for k,M in ((3,64),(4,32),(5,16))]
    clones=[]
    for k in range(1,11):
        Q=1<<k
        for n in (0,7,43,128):
            a=source_return_sum_mod(n,Q,k);b=v_padic_mod(n,k)
            if a!=b: raise AssertionError(f'source clone failed n={n} k={k}')
            clones.append({'k':k,'n':n,'same':True})
    flips=[]
    for k in range(1,11):
        Q=1<<k;mod=1<<(k+1)
        for n in (0,7,43,128):
            old=v_padic_mod(n,k+1)
            future=v_padic_mod(n+Q,k+1)
            next_source=source_return_sum_mod(n,Q,k+1)
            if future!=(old+Q)%mod or next_source!=(old+Q)%mod:
                raise AssertionError('original source one-bit flip failed')
            flips.append({'k':k,'n':n,'verified':True})
    return {'claim_label':'OBSERVED-FINITE','original_U0':'0','four_signed_poles':True,
            'return_witnesses':returns,'denominator_budget':recon,
            'float_diagnostics_only':{'normalized_residue_reference':rs,'return_fiber_energy':energy},
            'source_return_clone_cases':len(clones),'all_source_clone_checks_passed':True,
            'one_bit_flip_cases_postregistration':len(flips),
            'all_one_bit_flip_checks_passed':True,
            'real_selected_weyl_infinite':'OPEN','pi_base16_normality':'OPEN',
            'fresh_probes_preregistered':True,
            'caution':'The exact fraction hashes and comparisons are exact; printed decimal, RMS and entropy numbers are floating diagnostics, not rigorous real-Weyl certificates.'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))

"""Replayable exact finite source receipts; logs never imply asymptotic normality."""
from __future__ import annotations
import importlib.util
import json
import pathlib
import sys
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parent

def load(stem):
    spec=importlib.util.spec_from_file_location('succ_entropy_probe_'+stem,ROOT/(stem+'.py'))
    obj=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=obj
    spec.loader.exec_module(obj)
    return obj


def generate():
    m=load('carrier_entropy'); l=load('laurent_lag'); o=load('independent_oracle')
    profiles=[]
    for n in (64,128,256,512,1024,2048):
        xs=m.selected_states(n)
        x=m.empirical_profile(xs,3)
        x['profile']=[{key:val for key,val in record.items() if key not in ('entropy_nats','kl_nats','conditional_deficit_nats')}
                      for record in x['profile']]
        profiles.append(x)
    debruijn=m.debruijn_cycle(16,2)
    c2=m.cyclic_word_counts(debruijn,2)
    c3=m.cyclic_word_counts(debruijn,3)
    clock=[]
    for n in (256,1024,4096,16384):
        for d in (2,3,4):
            k=l.corrected_clock(n,d)
            clock.append({'N':n,'laurent_order':d,'K':k,'h1_transport_budget':str(l.aggregate_transport_budget(n,k,1,d)),
                          'h3_transport_budget':str(l.aggregate_transport_budget(n,k,3,d))})
    ratios=[]
    for a in (4,5,6):
        n=4**a//2; k=a
        lead,actual,eps=l.first_positive_curvature_bound(n,k)
        ratios.append({'N':4**a,'k':k,'n':n,'phase_correction_exact':str(actual),
                       'leading_exact':str(lead),'upper_error_bound':str(eps),
                       'target_limit':'1/16'})
    return {
        'status':'FINITE_EXACT_RECEIPTS_NOT_PI_NORMALITY',
        'source_contract':'original four signed poles, literal U0=0',
        'parent':'702cf6fa45c9e6d10bd48c84efe7d3c4389a9037',
        'base':16,
        'source_check_first_48':all(m.source(j)==o.source_combined_direct(j) for j in range(1,49)),
        'selected_collision_profiles':profiles,
        'debruijn_control':{'period':len(debruijn),'depth2_cells':len(c2),'depth3_cells':len(c3),
                            'exact_depth2_collision':str(m.collision_defect_from_counts(c2,256,2)),
                            'exact_depth3_collision':str(m.collision_defect_from_counts(c3,256,3)),
                            'conditional_third_digit_entropy':'0'},
        'rational_counterfeit_N8':str(m.rational_completed_counterfeit(8)),
        'exact_laurent_moments':{str(d):str(l.moment(d)) for d in range(2,7)},
        'corrected_clock_budgets':clock,
        'critical_bulk_phase_receipts':ratios,
        'authority':'exact rational/integer tests + paper proof; no Lean kernel or all-horizon signed saving'
    }


def main():
    data=generate()
    text=json.dumps(data,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    target=ROOT/'FINITE_RECEIPT.json'
    if '--check' in sys.argv:
        if not target.exists() or target.read_text()!=text:raise SystemExit('FINITE_RECEIPT_MISMATCH')
        print('FINITE_RECEIPT_EXACT_REPLAY_PASS')
    else:
        target.write_text(text)
        print('WROTE',target,'bytes',len(text))

if __name__=='__main__':main()

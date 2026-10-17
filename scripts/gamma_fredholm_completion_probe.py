"""Exact reproducible research probe; source mode requires original frozen SUCC."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from observational_succ import gamma_fredholm_completion as C


def build(source=False):
    w=C.odd_legendre_135_witness()
    d={'program':'AUTHENTIC_GAMMA_FREDHOLM_COMPLETION_2026_10_17',
       'first_prime_window':'1/2',
       'authentic_source_module_required_for_spectral_claim':True,
       'synthetic_and_source_certificate_unequated':True,
       'source_blob_expected':'0cc8510b71d178fc79e8d410a86d8b6014cf9178',
       'rational_witness':{'modes':[[i,str(v)] for i,v in w['modes']],
          'u_polynomial_coeff_ascending':[str(x) for x in w['u_polynomial_ascending']],
          'norm_sq':str(w['norm_sq']),'derivative_norm_sq':str(w['derivative_norm_sq'])},
       'gamma_tail_J64_lower':str(C.gamma_tail_H01_lower(64,w['norm_sq'],w['derivative_norm_sq'])),
       'gamma_tail_J64_upper':str(C.gamma_tail_source_upper(64,w['norm_sq'])),
       'original_signed_source_authenticated':source,
       'authentic_fifth_mode_completion':C.authentic_fifth_mode_completion(64) if source else None,
       'authentic_J8_feature_gram':C.authentic_fredholm_feature_gram(8,16) if source else None,
       'certified_complete_first_window_sign':False,
       'all_radii_Weil_sign_proved':False,
       'RH_proved':False}
    return d


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',action='store_true');parser.add_argument('--verify',action='store_true')
    parser.add_argument('--output');args=parser.parse_args();d=build(args.source)
    if args.verify:
        assert F(d['gamma_tail_J64_lower'])>F(838,1000000)
        assert F(d['gamma_tail_J64_upper'])>F(d['gamma_tail_J64_lower'])
        if args.source:
            assert d['authentic_fifth_mode_completion']['fully_completed_same_vector_positive_strict']
            assert d['authentic_fifth_mode_completion']['truncated_negative_strict']
            assert d['authentic_J8_feature_gram']['dimension']==18
            assert not d['authentic_J8_feature_gram']['source_positivity_certified']
        assert not d['RH_proved']
    content=json.dumps(d,sort_keys=True,indent=2)+'\n'
    if args.output:Path(args.output).write_text(content)
    else:print(content,end='')


if __name__=='__main__':main()

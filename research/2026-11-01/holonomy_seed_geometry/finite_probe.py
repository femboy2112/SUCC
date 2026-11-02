"""Optional, *non-certifying* high-precision diagnostics plus rational receipts.
The mathematical correctness of the infinite theorems rests on PROOFS.md,
not numerical convergence. Preregistered K/h sets may not be changed by outcome.
"""
from __future__ import annotations
from pathlib import Path
import sys,importlib.util,json
from fractions import Fraction as F

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('new_holonomy_module',HERE/'holonomy_geometry.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def run():
    import mpmath as mp
    mp.mp.dps=200
    out={'scope':'finite pure control-state overlap diagnostics; not proof authority',
      'precision_dps':200,'K':[4,8,16,32,48],'harmonics':[1,3,5],
      'cases':[], 'rational_curvature_receipts':[], 'positive_moment_mutants':[]}
    # Uses *two* mathematically dependent routes to the finite future tail:
    # the original source series and the completed alpha=pi/16. The independence
    # is implementation-level, not a blind witness to pi normality.
    for K in out['K']:
        q=m.source_prefix_q(K)
        q_mp=mp.mpf(q.numerator)/q.denominator
        delta=mp.pi/16-q_mp
        tail_mp=mp.fsum((mp.mpf(m.r(K+j).numerator)/(m.r(K+j).denominator*16**j)
                        for j in range(1,120)))
        if not (delta>0 and abs(tail_mp-mp.power(16,K)*delta)<mp.mpf('1e-100')*max(1,abs(tail_mp))):
            raise ArithmeticError('independent source-tail diagnostic mismatch')
        for h in out['harmonics']:
            overlap=mp.fsum([mp.exp(-2j*mp.pi*h*mp.power(16,n)*delta)
                              for n in range(1,K+1)])/K
            distance=mp.sqrt(max(0,1-abs(overlap)**2))
            bound=mp.sqrt(mp.mpf(m.finite_shadow_norm_upper_sq(K,h).numerator)/m.finite_shadow_norm_upper_sq(K,h).denominator)
            out['cases'].append({'K':K,'h':h,'trace_distance':mp.nstr(distance,30),
               'proven_upper':mp.nstr(bound,30),'inside_proven_upper':bool(distance<bound),
               'geometric_source_independent':True})
    for M in range(1,11):
        v=m.pi_upper(M);err=m.pi_error_bound(M)
        out['rational_curvature_receipts'].append({'M':M,'pi_upper':str(v),'pi_error_upper':str(err),
                 'pi_upper_decimal':mp.nstr(mp.mpf(v.numerator)/v.denominator,30),
                 'error_upper_decimal':mp.nstr(mp.mpf(err.numerator)/err.denominator,12)})
    for M in range(1,7):
        p=m.rational_nonnormal_mutant_certificate(M)
        out['positive_moment_mutants'].append({'M':M,'rational_target':str(p['q']),
          'max_density_tilt_times_C':str(p['epsilon_interval'][1]*p['C']),
          'unchanged_prefix':True, 'nonnormal_witness_frequency':str(p['non_normal_harmonic'])})
    return out

if __name__=='__main__':
    outfile=HERE/'FINITE_DIAGNOSTICS.json'
    out=run();outfile.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'diagnostic_cases':len(out['cases']),
        'all_inside_upper':all(z['inside_proven_upper'] for z in out['cases']),
        'pi_receipts':len(out['rational_curvature_receipts']),
        'finite_mutants':len(out['positive_moment_mutants'])},indent=2))

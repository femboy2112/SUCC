"""Reproducible original-source Gamma-tail endpoint-resolvent certificate."""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

from observational_succ import original_continuum_residual as R
from observational_succ import gamma_tail_resolvent_refinement as T


def serializable(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serializable(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serializable(v) for v in x]
    return x


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source',action='store_true')
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--compare',action='store_true',
        help='Run the costly complete paired J8/J16/J24 original source comparison')
    parser.add_argument('--depth',type=int,choices=(8,16,24),nargs='+')
    parser.add_argument('--output')
    options = parser.parse_args()
    if not options.source:
        raise SystemExit('Original source required; refuse a synthetic positive replacement.')
    holdout = T.independent_original_source_holdouts()
    baseline = {str(J):{str(i):T.gamma_tail_resolvent_bound(
        R.high_boundary_match(i)['h'],J) for i in range(1,5)} for J in (8,16,24)}
    result = {
        'program':'ORIGINAL_GAMMA_TAIL_ENDPOINT_RESOLVENT',
        'source_git_blob':T.SOURCE_SHA,
        'fresh_source_holdouts':holdout,
        'unfitted_boundary_match_tail_bounds':baseline,
        'first_window_S4_sign':'OPEN',
        'RH_proved':False,
    }
    if options.compare:
        comparisons = {}
        for J in options.depth or (8,16,24):
            M = {8:80,16:128,24:184}[J]
            parent = R.source_residual_schur_trial(J,M)
            retained = T.source_tail_resolvent_schur_trial(J,M,fit='parent')
            comparisons[str(J)] = {'parent':parent,'retained_tail':retained}
        result['same_parent_coefficients_comparison'] = comparisons
    if options.verify:
        assert holdout['full_signed_channels_intersect']
        assert holdout['source_shell_intersects']
        assert holdout['omitted_leading_Laplacian_mutant_disjoint']
        assert holdout['reversed_leading_sign_mutant_disjoint']
        assert not result['RH_proved']
        result['verification'] = 'PASS'
    if options.output:
        Path(options.output).write_text(json.dumps(serializable(result),indent=2,sort_keys=True)+'\n')
    summary = {
        'source_git_blob':T.SOURCE_SHA,
        'fresh_signed_J7_holdout':holdout['full_signed_channels_intersect'],
        'fresh_J13_to_J23_shell_holdout':holdout['source_shell_intersects'],
        'leading_term_mutants_rejected':(
            holdout['omitted_leading_Laplacian_mutant_disjoint']
            and holdout['reversed_leading_sign_mutant_disjoint']),
        'comparisons_run':list(result.get('same_parent_coefficients_comparison',{})),
        'first_window_S4_sign':'OPEN','RH_proved':False,
        'verification':result.get('verification','NOT_REQUESTED'),
    }
    print(json.dumps(summary,sort_keys=True))


if __name__=='__main__':main()

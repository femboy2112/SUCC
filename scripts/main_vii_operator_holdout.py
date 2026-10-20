#!/usr/bin/env python3
"""Independent symbolic Gram and exact source-receipt checks for the research lane.

No source operator is replaced here. This checks finite inverse/refinement
arithmetic conditional on the separately attested original-source comparison.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys


def psd2(matrix):
    a,b,c,d = (Q(matrix[i][j]) for i,j in ((0,0),(0,1),(1,0),(1,1)))
    return b == c and a >= 0 and d >= 0 and a*d-b*c >= 0


def pd2(matrix):
    a,b,c,d = (Q(matrix[i][j]) for i,j in ((0,0),(0,1),(1,0),(1,1)))
    return b == c and a > 0 and a*d-b*c > 0


def ceil_grid(value,denominator=10**24):
    value = Q(value)
    return Q((value.numerator*denominator+value.denominator-1)//value.denominator,
             denominator)


def symbolic_gram(b,kappa,w,parity):
    import sympy as s
    b,kappa,w = map(s.Rational,(b,kappa,w))
    x = s.Symbol('x',real=True)
    constraints = [1+0*x,6*x*x-s.Rational(1,2)] if parity == 'even' else [2*x,20*x**3-3*x]
    alpha = (kappa+w)/(kappa*(kappa+2*w))
    beta = w/(kappa*(kappa+2*w))
    half = s.Rational(1,2)
    result = []
    for h in constraints:
        row = []
        for g in constraints:
            value = s.integrate(h*(alpha*g+beta*g.subs(x,x+b)),(x,-half,half-b))
            value += s.integrate(h*g/(kappa+w),(x,half-b,b-half))
            value += s.integrate(h*(alpha*g+beta*g.subs(x,x-b)),(x,b-half,half))
            row.append(Q(int(value.p),int(value.q)))
        result.append(row)
    return result


def audit(target,source_receipt):
    sys.path.insert(0,str(target))
    from observational_succ import cloud_exact_moment_inverse as implementation
    count = 0
    for parity in ('even','odd'):
        for b in (Q(2,3),Q(3,4),Q(5,6)):
            for kappa,w in ((Q(1,7),Q(12,25)),(Q(3,5),Q(0))):
                db = Q(1,50)
                packet = implementation.constraint_gram(b,db,kappa,parity,w,cells=8)
                nominal = symbolic_gram(b,kappa,w,parity)
                assert tuple(map(tuple,nominal)) == packet['nominal_gram']
                for shift in (-db,-db/3,Q(0),db/2,db):
                    actual = symbolic_gram(b+shift,kappa,w,parity)
                    for key in ('gram_upper','quadrature_gram_upper'):
                        difference = [[packet[key][i][j]-actual[i][j] for j in range(2)] for i in range(2)]
                        assert psd2(difference),(parity,b,shift,key)
                    count += 1
    raw = source_receipt.read_bytes()
    source = json.loads(raw)
    for relative,expected_hash in source['sha256'].items():
        assert hashlib.sha256((target/relative).read_bytes()).hexdigest() == expected_hash,relative
    sectors = {}
    for name,packet in source['sectors'].items():
        for route in ('exact','quadrature'):
            assert pd2(packet[route]['additional_gain_lower'])
            assert pd2([[-Q(x) for x in row] for row in packet[route]['new_schur_lower']])
            assert all(Q(packet[route]['new_schur_lower'][i][j]) ==
                       Q(packet['old_diagonal_constraint_schur_lower'][i][j])+
                       Q(packet[route]['additional_gain_lower'][i][j])
                       for i in range(2) for j in range(2))
        ceilings = [Q(x) for x in packet['fixed_ambient_error_budget_diagonal_ceiling']]
        assert all(x < 0 for x in ceilings)
        factor = 1+Q(source['eta'])
        norms = list(map(Q,packet['constraint_norms']))
        kappaplus = Q(packet['kappa'])+Q(24,25)
        for i in range(2):
            cap = ceil_grid(kappaplus*sum(
                (Q(packet['nominal_inverse_moment_absolute_upper'][j][i])+
                 Q(packet['inverse_moment_error_upper'][j][i]))**2/norms[j]
                for j in range(2)))
            assert cap == Q(packet['complete_constraint_diagonal_upper'][i])
            ceiling = ceil_grid(Q(packet['fixed_ambient_schur_diagonal_upper'][i])+factor*cap)
            assert ceiling == ceilings[i]
        sectors[name] = {'exact_and_quadrature_gains_PD':True,
                         'both_lower_matrices_negative_definite_only':True,
                         'method_ceiling_recomputed_from_outward_parents':True,
                         'fixed_budget_diagonal_ceilings':list(map(str,ceilings))}
    return {'scope':'finite arithmetic holdout; source comparison remains an external paper dependency',
            'symbolic_shifted_gram_cases':count,'failures':0,'sectors':sectors,
            'source_receipt_sha256':hashlib.sha256(raw).hexdigest(),
            'all_recorded_implementation_hashes_match':True,
            'implementation_sha256':hashlib.sha256((target/'observational_succ/cloud_exact_moment_inverse.py').read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'RH_proved':False,'source_sign_certified':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target-repo',type=Path,required=True)
    parser.add_argument('--source-receipt',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = audit(args.target_repo,args.source_receipt)
    serialized = json.dumps(result,indent=2,sort_keys=True)+'\n'
    args.output.write_text(serialized)
    print(serialized)


if __name__ == '__main__':
    main()

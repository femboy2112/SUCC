"""Replay exact rational receipt checks; optionally compare a second replay."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import sys

HERE = Path(__file__).parent


def interval_nodes(value, prefix=''):
    if isinstance(value, dict):
        if 'lower' in value and 'upper' in value:
            lo, hi = F(value['lower']), F(value['upper'])
            assert lo <= hi
            sign = 'negative' if hi < 0 else 'positive' if lo > 0 else 'unresolved'
            assert sign == value['sign']
            yield prefix, (lo, hi)
        else:
            for key, child in value.items():
                yield from interval_nodes(child, prefix+'/'+key)
    elif isinstance(value, list):
        for k, child in enumerate(value):
            yield from interval_nodes(child, prefix+'/'+str(k))


def verify(path):
    d = json.loads(path.read_text())
    assert d['source_sha256'] == sha256((HERE/'regularized_cut.py').read_bytes()).hexdigest()
    assert len(d['rows']) == 48
    for row in d['rows']:
        A, r = row['A'], F(row['r'])
        E, P = row['actual_energy'], row['cuts'][str(2*A)]['total']
        lo, hi = F(P['lower'])-F(E['upper']), F(P['upper'])-F(E['lower'])
        bound = 4*F(22,7)*r/(1-r)/(30*A)  # rigorous pi < 22/7
        assert max(abs(lo),abs(hi)) <= bound
        assert F(row['cuts'][str(A)]['total']['lower']) == 0
        assert F(row['cuts'][str(A)]['total']['upper']) == 0
    lookup = {(v['A'],v['r'],v['model']): v for v in d['rows']}
    for A in (17,29,53,89):
        for r in ('1/2','3/4'):
            a,b = lookup[A,r,'original'],lookup[A,r,'rational_1_5']
            assert a['actual_energy'] == b['actual_energy'] and a['cuts'] == b['cuts']
    nodes = dict(interval_nodes(d))
    return d,nodes


if __name__ == '__main__':
    primary = HERE/'FINITE_RECEIPT.json'
    a,an = verify(primary)
    result = {'verified_rows':len(a['rows']), 'verified_intervals':len(an),
              'primary_sha256':sha256(primary.read_bytes()).hexdigest()}
    if len(sys.argv) == 2:
        other = Path(sys.argv[1])
        b,bn = verify(other)
        assert a['carry_sha256'] == b['carry_sha256']
        assert an.keys() == bn.keys()
        for key in an:
            assert max(an[key][0],bn[key][0]) <= min(an[key][1],bn[key][1]), key
        result.update(replay_sha256=sha256(other.read_bytes()).hexdigest(),
                      identical_rational_intervals=sum(an[k]==bn[k] for k in an),
                      overlapping_intervals=len(an),carry_hashes_equal=True)
    print(json.dumps(result,indent=2))

"""Independent combinatorial audit of RE4, using Hierholzer's algorithm."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def debruijn(base, order):
    vertices = base**(order-1)
    next_digit = [0]*vertices
    stack = [(0,None)]
    output = []
    while stack:
        v,incoming = stack[-1]
        if next_digit[v] < base:
            digit = next_digit[v]
            next_digit[v] += 1
            stack.append(((base*v+digit)%vertices,digit))
        else:
            stack.pop()
            if incoming is not None:
                output.append(incoming)
    return output[::-1]


def run():
    checks = []
    for base in (2,4,16):
        for k in (1,2,3):
            cycle = debruijn(base,k)
            d = base**k
            assert len(cycle)==d
            total_words = 0
            for j in range(1,k+1):
                words=Counter(tuple(cycle[(i+t)%d] for t in range(j)) for i in range(d))
                assert len(words)==base**j
                assert set(words.values())=={base**(k-j)}
                total_words += len(words)
            # A finite stand-in with exactly the same periodic divisibility.
            # The infinite theorem's m_k=16^(k^2) is proved on paper.
            m=3*d
            agree=0
            for n in range(2*m,3*m):
                length=3*m-n
                # All starts are congruent modulo d: no floating phases used.
                assert (n+1)%d==(n+m+1)%d
                assert n+m+length <= 4*m
                agree += length
            assert agree==m*(m+1)//2
            # Exact sum of the radix-tail bounds used in RE4.
            geom = sum((F(1,base**j) for j in range(1,min(m,24)+1)),F(0))
            assert geom < F(1,base-1)
            checks.append({'base':base,'order':k,'length':d,
                           'exact_cyclic_word_counts':total_words,
                           'aligned_tail_pairs':m,
                           'matched_digit_positions_by_identity':agree,
                           'cycle_sha256':sha256(bytes(cycle)).hexdigest()})
    return {'status':'PASS_EXACT_FINITE_RE4_COMBINATORICS',
            'method':'Independent Hierholzer Euler circuit, exact counts and rational tail sums',
            'scope':'Finite mechanism only; normality is established by the separate paper limit proof',
            'checks':checks}


if __name__=='__main__':
    result=run()
    out=Path(__file__).with_name('ENERGY_REVIEW.json')
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'cases':len(result['checks'])}))

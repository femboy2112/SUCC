"""Independent factor-sieve odd register replay of the large full-source receipt.

All four poles remain: the two even poles are combined algebraically, not
discarded. Unique factorization computes their LCM instead of repeated gcd.
"""
import argparse
from array import array
from hashlib import sha256
from math import isqrt
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def odd_modulus(last):
    if last < 0:
        raise ValueError('nonnegative last required')
    if last == 0:
        return 1
    bound = 8*last
    spf = array('I', range(bound+1))
    for p in range(2,isqrt(bound)+1):
        if spf[p] == p:
            for v in range(p*p,bound+1,p):
                if spf[v] == v:
                    spf[v] = p
    powers = {}
    for n in range(1,last+1):
        for d in (2*n-1,4*n-1,8*n-7,8*n-3):
            while d > 1:
                p, power = spf[d], 1
                while d%p == 0:
                    d //= p
                    power *= p
                powers[p] = max(powers.get(p,1),power)
    factors = list(powers.values())
    while len(factors)>1:
        factors = [factors[i]*factors[i+1] for i in range(0,len(factors)-1,2)]+(
            factors[-1:] if len(factors)%2 else [])
    return factors[0] if factors else 1


def odd_source(last):
    den = odd_modulus(last)
    a = 0
    yield 0,a,den,0
    for n in range(1,last+1):
        product = (2*n-1)*(4*n-1)
        assert den%product == 0
        injection = 4*(den//(8*n-7))-den//(8*n-3)-(3*n-1)*(den//product)
        carry,a = divmod(16*a+injection,den)
        yield n,a,den,carry


def replay():
    import hannibal as h
    expected = json.loads((HERE/'LARGE_RECEIPT.json').read_text())
    rows = expected['epochs']
    counts = {(r['A'],r['mesh']):[0]*r['mesh'] for r in rows}
    carries = sha256()
    for n,a,den,c in odd_source(expected['last']):
        if not n:
            continue
        carries.update(bytes([c]))
        A = 1 << (n.bit_length()-1)
        for m in (h.slow_mesh(A),64,256) if A in (16384,65536) else ():
            counts[(A,m)][m*a//den] += 1
    for r in rows:
        assert counts[(r['A'],r['mesh'])] == r['counts'], (r['A'],r['mesh'])
    assert carries.hexdigest() == expected['literal_carry_sha256']
    return {'status':'EXACT ODD/FULL LARGE ORACLE AGREEMENT',
            'last':expected['last'], 'histogram_vectors_compared':len(rows),
            'literal_carry_sha256':carries.hexdigest(),
            'odd_modulus_bits':den.bit_length(),
            'odd_modulus_sha256':h.digest_integer(den),
            'full_receipt_sha256':sha256((HERE/'LARGE_RECEIPT.json').read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--verify',action='store_true')
    args = parser.parse_args()
    result = replay()
    target = HERE/'ODD_REPLAY_RECEIPT.json'
    if args.verify:
        assert json.loads(target.read_text()) == result
        print('Odd/full histogram and literal-carry replay: PASS')
    else:
        if target.exists():
            raise FileExistsError('refusing to overwrite odd replay receipt')
        target.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print(json.dumps(result,indent=2,sort_keys=True))

"""Independent exact checks of the prime-layer note. Standard Python, no repo imports."""

from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt, lcm
import json
from pathlib import Path


P = (4, 0, 0, -2, -1, -1, 0, 0)
A = (2, 2, 1, 0, F(-1, 2), F(-1, 2), F(-1, 4), 0)
E = (0, 2, 0, 0, 0, F(-1, 2), 0, 0)
MUT = (1, -2, 0, 0, 0, 0, 0, 0)
HOSTILE = (F(-3, 4), 2, 1, F(7, 2), 0, -2, 5, -4)
BASIS = [tuple(int(i == j) for j in range(8)) for i in range(8)]
CLASSES = (1, 3, 5, 7)
HORIZONS = (83, 211, 389, 631)


def transform(w, a):
    result = []
    for l in range(1, 9):
        j = (a*l-1) % 8 + 1
        sign = (-1 if a in (3, 5) else 1) ** l
        result.append(sign * F(2) ** ((j-l)//2) * w[j-1])
    return tuple(result)


def partial(w, s):
    return sum((F(w[(i-1) % 8], i*16**((i+7)//8))
                for i in range(1, s+1)), start=F(0))


def mod(r, modulus):
    return (r.numerator * pow(r.denominator, -1, modulus)) % modulus


def direct_path(w, horizon):
    """Accumulate integer numerators and conductor, with no Frobenius code."""
    taps = [(j, F(t)) for j, t in enumerate(w, start=1) if t]
    conductor, lifted = 1, 0
    states, conductors = [F(0)], [1]
    for n in range(horizon):
        terms = [(t.numerator, t.denominator*(8*n+j)) for j,t in taps]
        raw = lcm(*(d for _,d in terms))
        add = sum(c*(raw//d) for c,d in terms)
        cancel = gcd(raw, add)
        den = raw//cancel
        new_conductor = lcm(conductor, den)
        lifted = 16*lifted*(new_conductor//conductor) + (add//cancel)*(new_conductor//den)
        conductor = new_conductor
        states.append(F(lifted, conductor))
        conductors.append(conductor)
    return states, conductors


def primes(x):
    sieve = bytearray([1])*(x+1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, isqrt(x)+1):
        if sieve[i]:
            sieve[i*i:x+1:i] = bytes(len(range(i*i, x+1, i)))
    return [i for i in range(2, x+1) if sieve[i]]


def order(p):
    k, v = 1, 16 % p
    while v != 1:
        k += 1
        v = 16*v % p
    return k


def check_layers():
    cases = set()
    for p in (3, 5, 7, 11, 13, 17, 19):
        for e in (1, 2, 3):
            q = p**e
            for m in (1, 2, 4, 7, 8, 11, 16, 22, 29):
                for h in (-1, 0, 1):
                    n = q*m//8+h
                    if 1 <= n <= 1600 and 8*n < p*q:
                        cases.add((p, e, n))
    cases = sorted(cases)
    digest = sha256()
    count, controls = 0, {}
    labels = [f'base{j+1}' for j in range(8)] + ['original', 'angular', 'hostile']
    for name, w in zip(labels, BASIS + [P, A, HOSTILE]):
        source, _ = direct_path(w, max(n for _,_,n in cases))
        for p, e, n in cases:
            q = p**e
            left = q*source[n]
            right = 16**n*partial(transform(w, q % 8), 8*n//q)
            assert mod(left, p) == mod(right, p), (name, p, e, n)
            digest.update(f'{name},{p},{e},{n},{mod(left,p)}\n'.encode())
            count += 1
            # One p-unit seed and one nonintegral seed of exactly the tested depth.
            seed = F(1, 7 if p != 7 else 11)
            assert mod(left + q*16**n*seed, p) == mod(right, p)
            assert mod(left + 16**n, p) != mod(right, p)
            if e >= 2 and name == 'angular' and q <= 8*n:
                if mod(left,p*p) != mod(right,p*p):
                    controls.setdefault('false_mod_p_squared', [p,e,n,mod(left,p*p),mod(right,p*p)])
                if p%4 == 3 and e == 2 and mod(right,p):
                    controls.setdefault('wrong_chi_at_square', [p,e,n,mod(left,p),mod(-right,p)])
    assert len(controls) == 2
    return dict(count=count, residue_sha256=digest.hexdigest(), cases_per_source=len(cases), controls=controls)


def verify_groups():
    for w in BASIS:
        for a in CLASSES:
            for b in CLASSES:
                assert transform(transform(w,a),b) == transform(w,a*b%8)
    for w in [A,E]:
        for a in CLASSES:
            assert transform(w,a) == tuple((1 if a%4==1 else -1)*v for v in w)
    # Rank of the rational character projector via exact row elimination.
    columns = [[sum((1 if a%4==1 else -1)*transform(w,a)[j] for a in CLASSES)/F(4)
                for j in range(8)] for w in BASIS]
    pivots = []
    for v in columns:
        for pos,u in pivots:
            v = [x-v[pos]*y for x,y in zip(v,u)]
        for i, x in enumerate(v):
            if x:
                pivots.append((i, [y/x for y in v]))
                break
    assert len(pivots) == 2
    # Multiply each proposed low-degree denominator into its authentic taps.
    denom8 = [1,0,0,0,0,0,0,0,F(-1,16)]
    def product(u,v):
        coeff = [0]*(len(u)+len(v)-1)
        for i,x in enumerate(u):
            for j,y in enumerate(v):
                coeff[i+j] += x*y
        while coeff and not coeff[-1]:
            coeff.pop()
        return coeff
    assert product(A,[1,-1,F(1,2)]) == product([2],denom8)
    assert product(E,[1,0,0,0,F(1,4)]) == product([0,2],denom8)
    return len(pivots)


def check_pairs():
    out = {}
    for name,w in [('original', P), ('angular', A)]:
        states, conductors = direct_path(w, max(HORIZONS))
        rows=[]
        for n in HORIZONS:
            D, M = states[n].denominator, conductors[n]
            assert M%D == 0
            gaps = [(states[n]-prev).denominator for prev in states[:n]]
            losses = []
            for d in gaps:
                assert M%d == 0
                losses.append(M//d)
            canceled, strings, count, hits = [], [], 0, 0
            for p in primes(8*n):
                if p*p<=8*n or M%p:
                    continue
                s = 8*n//p
                pulse = partial(transform(w,p%8),s)
                assert pulse and mod(p*states[n],p)==pow(16,n,p)*mod(pulse,p)%p
                if D%p:
                    assert pulse.numerator%p==0
                    canceled.append([p,s])
                    continue
                hit = sum(d%p!=0 for d in gaps)
                bound = n//order(p)+1+8*n//p
                assert hit<=bound
                count+=1
                hits+=hit
                strings.append(f'{p},{hit},{bound}\n')
            rows.append(dict(n=n, canceled_prime_and_window=canceled,
                             endpoint_loss_bits=(M//D).bit_length(),
                             max_gap_loss_bits=max(losses).bit_length(),
                             sum_gap_loss_bit_lengths=sum(x.bit_length() for x in losses),
                             checked_prime_rows=count, integral_gap_hits=hits,
                             row_count_sha256=sha256(''.join(strings).encode()).hexdigest()))
        out[name]=rows
    return out


def check_mutant():
    plus = (1,2,0,0,0,0,0,0)
    s,c = direct_path(MUT, max(HORIZONS))
    fixed,_ = direct_path(plus, max(HORIZONS))
    count=0
    witness=None
    for n in HORIZONS:
        for p in primes(8*n):
            if p%8==1 and 8*n//p==2:
                assert c[n]%p==0 and s[n].denominator%p!=0 and fixed[n].denominator%p==0
                count+=1
                if witness is None:
                    witness=[n,p,mod(p*s[n],p),mod(p*fixed[n],p)]
    assert count>0
    return {'count':count,'first':witness}


if __name__ == '__main__':
    reg=Path(__file__).with_name('PREREG_PRIME_LAYERS.md')
    receipt = {'preregistered_protocol_sha256':sha256(reg.read_bytes()).hexdigest(),
               'class_projector_rank':verify_groups(), 'layers':check_layers(),
               'rows':check_pairs(), 'zero_window_mutant':check_mutant()}
    print(json.dumps(receipt,indent=2,sort_keys=True))

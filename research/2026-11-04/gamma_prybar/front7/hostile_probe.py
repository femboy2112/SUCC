"""Exact finite calibration for sparse interventions and previously named controls."""
import json
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from math import isqrt, lcm, prod


def forcing(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def prime(p):
    return p > 1 and all(p % j for j in range(2, isqrt(p)+1))


def prime_power(x, p):
    result = 1
    while x % p == 0:
        x //= p
        result *= p
    return result


def orbit(injections, seed=F(0)):
    states = [seed]
    for term in injections[1:]:
        states.append(16*states[-1]+term)
    return states


def integer_path(last):
    clock, lift, residue = 1, 0, 0
    states, clocks, carries = [F(0)], [clock], [0]
    for n in range(1, last+1):
        source = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        enlarged = lcm(clock, source.denominator)
        ratio = enlarged//clock
        injection = source.numerator*(enlarged//source.denominator)
        lift = 16*ratio*lift + injection
        carry, residue = divmod(16*ratio*residue + injection, enlarged)
        assert lift % enlarged == residue
        states.append(F(lift, enlarged))
        carries.append(carry)
        clocks.append(enlarged)
        clock = enlarged
    return states, clocks, carries


def sparse(source, clocks, kind):
    v = [F(0)]
    resets = {}
    next_reset = 2 if kind == 'ternary' else 7
    new_clock = 1
    for n in range(1, len(clocks)):
        provisional = 16*v[-1]+source[n]
        error = F(0)
        if n == next_reset:
            if kind == 'ternary':
                denominator = prime_power(clocks[n-1], 3)
                target = provisional
                next_reset += 3*max(1, (n.bit_length()-1)//24)
            else:
                denominator = clocks[n//2]
                lookahead = F(0)
                for index in range(3*n, n, -1):
                    lookahead = (source[index] + lookahead)/16
                target = provisional + lookahead
                next_reset *= 2
            error = -F(round(denominator*target), denominator)
            resets[n] = error
            assert not prime(8*n-7)
        v.append(provisional+error)
        new_clock = lcm(new_clock, (source[n]+error).denominator)
        assert new_clock == clocks[n]
    return v, resets


def distance(x):
    z = x % 1
    return min(z, 1-z)


def measure(points, q):
    pts = sorted(x % 1 for x in points)
    doubled = pts + [1+x for x in pts]
    max_arc = 0
    near = 0
    width = F(1,q)
    for point in pts:
        right = bisect_left(doubled, point+width)-bisect_left(doubled, point)
        left = bisect_left(doubled, point+1)-bisect_right(doubled, point+1-width)
        near += right+left
        max_arc = max(max_arc, right)
    return {'points':len(pts), 'ordered_near':near, 'max_half_open_arc':max_arc}


def birth_checks(n, source):
    p = 8*n-7
    cofactor = (p+3)*(p+4)*(p+5)//8
    delta_hi = F(1,2*p*p)-F(1,3*p**3)+F(1,4*p**4)
    low = 30*(delta_hi-F(1,5*p**5))-F(49,p**3)
    high = 30*delta_hi-F(49,p**3)+F(236,p**4)
    assert low < source < high and cofactor*(high-low)<1
    assert (p*source-4).numerator % p == 0
    assert not low < source + F(1,cofactor) < high


def ghost_cloud(A, actual, clocks):
    # Both corrected prime families from #485/#487.
    end = (4*A+2)//3
    primes = [8*k+1 for k in range((A+1)//2, A) if prime(8*k+1)]
    primes += [4*k-1 for k in range((8*A+8)//9, A+1) if prime(4*k-1)]
    P, D = prod(primes), clocks[end-1]
    cloud = []
    for x in actual[A:end]:
        address = D*x
        assert address.denominator == 1
        centered = (address.numerator + P//2) % P - P//2
        y = F(1,5)+F(centered,D)
        assert all((x-y).denominator % p for p in primes)
        cloud.append(y)
    return measure(cloud,8)


def receipt():
    epochs, q = [32,64,128], 8
    last = 2*max(epochs)-1
    terms = [F(0)]+[forcing(n) for n in range(1,3*last+1)]
    actual, clocks, carries = integer_path(last)
    assert actual == orbit(terms[:last+1])
    for n in range(1,last+1):
        assert carries[n] == (16*(actual[n-1]%1)+terms[n])//1
    ternary, corrections3 = sparse(terms, clocks, 'ternary')
    dyadic, corrections2 = sparse(terms, clocks, 'dyadic')
    born = [b for b in range(1,last+1) if prime(8*b-7)]
    for b in born:
        p = 8*b-7
        if p >= 41:
            birth_checks(b,terms[b])
        for n in range(b,min(last+1,2*b)):
            assert (dyadic[n]-actual[n]).denominator % p
    for v,u in zip(ternary,actual):
        den = (v-u).denominator
        assert prime_power(den,3) == den
    mutations = {
        'sign_flip_last':orbit([F(0)]+[terms[n]+F(2,8*n-2) for n in range(1,last+1)]),
        'jet_matched':orbit([F(0)]+[terms[n]+F(1,(8*n+1)**6) for n in range(1,last+1)]),
    }
    rows = {}
    for A in epochs:
        # #492 source-native wrong seed computed from literal four-pole prefix.
        prefix = sum(terms[j]*F(1,16**j) for j in range(1,2*A+1))
        seed = F(round(-clocks[A]*prefix),clocks[A])
        states = {'genuine':actual, 'ternary':ternary, 'dyadic':dyadic,
                  'source_native_seed':orbit(terms[:2*A],seed), **mutations}
        nonbirth = [n for n in range(A,2*A) if n not in born]
        epoch = {}
        for label,path in states.items():
            epoch[label] = measure(path[A:2*A],q)
            epoch[label]['nonbirth_near'] = measure([path[n] for n in nonbirth],q)['ordered_near']
        # The fixed irrational counterseed gives -T_n. All these tails lie
        # strictly between -1/[(8A+1)(8A+2)] and 0 by the original Green bound.
        assert F(1,(8*A+1)*(8*A+2)) < F(1,q)
        epoch['fixed_negative_completion'] = {'certified_max_arc':A, 'certified_near':A*A}
        epoch['ghost_487_clean_window'] = ghost_cloud(A,actual,clocks)
        epoch['fixed_rational'] = measure([F(1,5)]*A,q)
        epoch['periodic'] = measure([F(pow(16,n,7),7) for n in range(A,2*A)],q)
        epoch['grid_prefix'] = measure([F(i,A) for i in range(A)],q)
        epoch['zero_continuation'] = measure([F(0)]*A,q)
        # Synthetic diagnostic: local observations can be stitched without
        # any common forcing law. Change each p principal part independently.
        local_only = [F((i*i+1)%(8*b-7),8*b-7) for i,b in enumerate(born) if A<=b<2*A]
        epoch['fabricated_prime_points'] = measure(local_only,q)
        rows[str(A)] = epoch
    return {'surrogate_q':q, 'verified_last':last, 'births':len(born),
            'ternary_reset_count':len(corrections3), 'dyadic_resets':sorted(corrections2),
            'epochs':rows}


if __name__ == '__main__':
    print(json.dumps(receipt(),indent=2,sort_keys=True))

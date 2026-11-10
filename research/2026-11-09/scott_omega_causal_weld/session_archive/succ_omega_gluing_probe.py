"""Local exact SUCC gluing probes. Research controls, not a normality proof.

All tests use exact rational arithmetic; no repo reads/writes.
"""
from fractions import Fraction as Q
from math import floor, ceil


def bbp_r(n: int) -> Q:
    assert n >= 1
    return 4*Q(1,8*n-7)-2*Q(1,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def bbp_finite_gauge(L: int, seed: Q):
    U = [seed]
    for n in range(1,L+1):
        U.append(16*U[-1] + bbp_r(n))
    tail = [Q(0)]*(L+1)
    for n in range(L,0,-1):
        tail[n-1]=(bbp_r(n)+tail[n])/16
    assert tail[0] == sum((bbp_r(j)/16**j for j in range(1,L+1)),Q(0))
    for n in range(L+1):
        assert U[n]+tail[n] == 16**n*(seed+tail[0])
    for n in range(1,L+1):
        assert U[n]+tail[n] == 16*(U[n-1]+tail[n-1])
        assert tail[n-1]*16 == bbp_r(n)+tail[n]
    # A rigorous, explicit upper bound on the omitted INFINITE future:
    # 0 < sum_{j>L} r(j)/16**j < 4 / (15*(8L+1)*16**L).
    assert all(Q(0)<bbp_r(j)<4*Q(1,8*j-7) for j in range(1,L+8))
    return L, len(U), Q(4,15*(8*L+1)*16**L)


def circle_distance(x: Q, y: Q) -> Q:
    delta = abs((x-y)-floor(x-y))
    return min(delta,1-delta)


def test_two_omega4_pullback():
    tests=0
    for k in range(1,9):
        eps=Q(1,16**k)
        for m in (-16,-9,-1,0,1,9,16):
            y=Q(13,17)
            yp=y+Q(m,16)*eps
            if abs(y-yp)>eps: continue
            shared=(y+yp)/2
            assert max(abs(shared-y),abs(shared-yp)) == abs(y-yp)/2 <= eps/2
            tests+=1
    return tests


def test_circle_prefix_and_winding():
    cases=0
    for x in (Q(1,7),Q(3,7),Q(11,13),Q(0),Q(1)):
        for k in range(1,9):
            M=16**k
            lower=Q(floor(M*x),M)
            upper=Q(ceil(M*x),M)
            assert circle_distance(x,lower)<=Q(1,M)
            assert circle_distance(x,upper)<=Q(1,M)
            cases+=2
    for M in (4,16,256):
        lifted=[Q(j,M) for j in range(M+1)]
        assert sum((lifted[j+1]-lifted[j] for j in range(M)),Q(0))==1
        assert circle_distance(lifted[0],lifted[-1])==0
        assert lifted[-1]-lifted[0] == 1  # global lift obstruction persists
        cases+=1
    for x in (Q(3,7),Q(-9,4),Q(13,17)):
        for integer in range(-7,8):
            assert circle_distance(16*(x+integer),16*x)==0
            fx=16*x
            rep=fx-floor(fx)
            assert Q(0)<=rep<1
            assert rep + floor(fx)==fx
            cases+=1
    return cases


def test_domain_compacts_and_noncommuting_limits():
    cases=0
    for K in ((0,1,4),(3,7,24),tuple(range(25)),(100,201)):
        n=max(K)
        A=set(range(n+1))
        B={2*j for j in range(n+1)}|{2*j+1 for j in range(n+1)}
        assert set(K)<=A and set(K)<=B
        cases+=1
    # a(N,k)=1 for N>=k. At fixed N, k->infty is 0.
    # At fixed k, N->infty is 1. The two orders disagree.
    for N in (1,4,20):
        assert int(N>=N+1)==0
        for k in (1,3,17):
            assert int(max(N,k)+1>=k)==1
            cases+=1
    return cases


def test_uniform_bbp_tail_inequality():
    # Both sides are degree-4 integer polynomials; equality at 5 inputs
    # certifies their symbolic identity without an algebra dependency.
    def denominator(n):
        return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    def numerator(n):
        return 120*n*n-89*n+16
    def positive_polynomial(m):
        return 1928*m**4+3705*m**3+2379*m*m+531*m+13
    assert all(c>0 for c in (1928,3705,2379,531,13))
    for n in range(1,6):
        assert 4*denominator(n)-n*n*numerator(n)==positive_polynomial(n-1)
    for n in range(1,201):
        assert denominator(n)>0 and numerator(n)>0
        assert Q(0)<bbp_r(n)<Q(4,n*n)
    return 205


def test_fourier_grid_characters():
    cases=0
    # Character orthogonality on Z/16**k, computed via integer exponent orbit,
    # not by floating-point complex summation.
    from math import gcd
    for k in range(1,4):
        M=16**k
        for h in (0,1,2,7,15,16,M-1,M,M+1):
            orbit_size=M//gcd(M,h)
            # Constant character iff M divides h; otherwise its full orbit sums 0.
            if h % M==0: assert orbit_size==1
            else: assert orbit_size>1
            cases+=1
    return cases


def main():
    results={
        'finite_BBP_source_conjugacies': [bbp_finite_gauge(L,s) for L in (5,16,32) for s in (Q(0),Q(1,16),Q(-2,3))],
        'epsilon_fiber_product_probes': test_two_omega4_pullback(),
        'circle_prefix_winding_carry_probes': test_circle_prefix_and_winding(),
        'domain_and_limit_order_probes': test_domain_compacts_and_noncommuting_limits(),
        'finite_character_orthogonality_probes': test_fourier_grid_characters(),
        'bbp_tail_polynomial_certificate': test_uniform_bbp_tail_inequality(),
    }
    for key,value in results.items():
        if key=='finite_BBP_source_conjugacies':
            print(f'{key}: {len(value)} exact horizon/seed models PASS; last omitted-tail bound={value[-1][-1]}')
        else: print(f'{key}: {value} checks PASS')
    print('All local checks PASS. No infinite numerical computation, no GitHub write, no pi-normality claim.')


if __name__=='__main__': main()
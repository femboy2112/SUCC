"""Independent finite checks of derivations, not infinite proofs."""
from fractions import Fraction as Q
from itertools import combinations, product
import json
import math


PAIRS = ((3, 2), (4, 1), (5, 1))


def source(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def regrouped_source(n):
    a = 8*n-7
    return sum((Q(v*d, a*(a+d)) for d,v in PAIRS), Q())


def check_source():
    for n in list(range(1,81))+[127,256,1024]:
        assert source(n) == regrouped_source(n)
    eu = sum((Q(v*d*d,2) for d,v in PAIRS),Q()) / 15
    eu2 = sum((Q(v*d**3,3) for d,v in PAIRS),Q()) / 15
    ej, ej2 = Q(16,15), Q(272,225)
    eb = 8*ej-7+eu
    eb2 = 64*ej2-112*ej+49+2*(8*ej-7)*eu+eu2
    assert eu == Q(59,30)
    assert eu2 == Q(27,5)
    assert eb == Q(7,2)
    assert eb2 == Q(55,3)
    return {"source_identity_cases":83,"E_U":str(eu),"E_U2":str(eu2),
            "E_B":str(eb),"E_B2":str(eb2)}


def check_extension():
    for a,b in product(range(16), repeat=2):
        u,c = divmod(a,2)
        v,d = divmod(b,2)
        coord = 2*((u+v+c*d)%8)+(c^d)
        assert coord == (a+b)%16
    split_candidates = [s for s in range(16) if (2*s)%16 == 0]
    assert split_candidates == [0,8]
    assert all(s%2 == 0 for s in split_candidates)
    return {"addition_cases":256,"order_two_section_candidates":split_candidates,
            "homomorphic_section_exists":False}


def check_even_mode():
    A = (0,4,5,6)
    support = [k for k in range(256) if sum((k>>i)&1 for i in A)%2 == 0]
    assert len(support) == 128
    count_checked = 0
    for order in range(1,4):
        for inds in combinations(range(8), order):
            counts = {}
            for k in support:
                bits = tuple((k>>i)&1 for i in inds)
                counts[bits] = counts.get(bits,0)+1
            assert len(counts) == 2**order
            assert set(counts.values()) == {128//2**order}
            count_checked += 1
    for offset in (0,4):
        assert all(sum(((k>>offset)&15)==d for k in support)==8 for d in range(16))
    # ζ=e(1/128), with minimal polynomial X^64+1. Reduce exact numerator
    # sum_{k in support} ζ^k; nonzero degree<64 remainder certifies nonzero.
    remainder = [0]*64
    for k in support:
        j = k%128
        remainder[j%64] += 1 if j<64 else -1
    assert any(remainder)
    return {"support_size":128,"uniform_marginal_subsets_checked":count_checked,
            "both_full_digit_marginals_uniform":True,
            "h":2,"denominator":256,"expectation_denominator":128,
            "cyclotomic_modulus":"X^64+1",
            "nonzero_remainder":{str(i):c for i,c in enumerate(remainder) if c}}


def check_tail_numeric():
    from decimal import Decimal as D, getcontext
    getcontext().prec=70
    rows=[]
    for n in (1,2,8,64,1024,16384):
        a=D(8*n)
        T=D(0)
        A=D(0)
        for j in range(1,65):
            b=8*j-7
            for d,v in PAIRS:
                rate=a+b
                T += D(v)*D(16)**(-j)*(1/rate-1/(rate+d))
                A += D(v)*D(16)**(-j)*((1+(rate/a).ln())/rate-
                        (1+((rate+d)/a).ln())/(rate+d))
        eta=A/T
        assert 0 < eta <= (1+D(7)/(2*a)).ln()
        assert eta >= D(7)/(2*a)-55/a**2
        assert eta >= (1+1/a).ln()
        rows.append({"n":n,"a_eta":str(a*eta),"a2_T":str(a*a*T),
                     "T_over_eta2":str(T/eta**2)})
    return {"status":"OBSERVED Decimal diagnostics, not certificates",
            "depth":64,"dps":70,"rows":rows}


if __name__ == "__main__":
    result={"source":check_source(),"extension":check_extension(),
            "even_mode":check_even_mode(),"tail_numeric":check_tail_numeric()}
    print(json.dumps(result,indent=2))

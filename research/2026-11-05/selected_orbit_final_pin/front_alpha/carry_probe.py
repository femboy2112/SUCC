"""Exact arithmetic instrument for forcing-induced macro-carry corrections.

No pi digits or floating-point sign decisions. This module is research-only.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json

C = Q(1920, 2457)
EPOCHS = (125, 257, 521)
DEPTHS = (1, 2, 3)


def floor(x: Q) -> int:
    return x.numerator // x.denominator


def source(n: int) -> Q:
    if n < 1:
        raise ValueError("source index must be positive")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def source_polynomial(n: int) -> Q:
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def orbit(N: int, seed: Q = Q(0), multiplier: int = 1):
    """Unwrapped signed-pole path versus polynomial circle path."""
    lifted = [seed]
    circles = [seed % 1]
    carries = [None]
    for n in range(1, N+1):
        tap = multiplier*source(n)
        assert tap == multiplier*source_polynomial(n)
        lifted.append(16*lifted[-1]+tap)
        raw = 16*circles[-1]+multiplier*source_polynomial(n)
        carries.append(floor(raw))
        circles.append(raw % 1)
        assert lifted[-1] % 1 == circles[-1]
        assert floor(lifted[-1])-16*floor(lifted[-2]) == carries[-1]
    return lifted, circles, carries


def source_block(n: int, m: int, multiplier: int = 1) -> Q:
    return sum((16**(m-j)*multiplier*source(n+j) for j in range(1,m+1)), Q())


def tail_interval(n: int, terms: int = 24):
    lo = sum((source(n+j)/16**j for j in range(1, terms+1)), Q())
    # Positive decreasing source: the omitted geometric tail is at most this.
    hi = lo + source(n+terms+1)/Q(15*16**terms)
    return lo, hi


def periodic_completion(p: int):
    lo, hi = tail_interval(0, p+24)
    q = 16**p-1
    a, b = floor(q*lo+Q(1,2)), floor(q*hi+Q(1,2))
    assert a == b
    beta = Q(a,q)
    assert max(abs(beta-lo),abs(beta-hi)) <= Q(1,2*q)
    return beta


def bound(A: int, m: int, constant: Q = C):
    if A < 1 or m < 1 or constant <= 0:
        raise ValueError("positive A, m and constant required")
    B = 16**m
    threshold = Q(15*(A+1)**2)/constant
    L, power = 0, 1
    while power*B <= threshold:
        L += 1
        power *= B
    if L < 1:
        return {"applicable":False,"L":L,"max_corrections":None}
    return {"applicable":True,"L":L,
            "max_corrections":m*((A+m*L-1)//(m*L))}


def pressure(counts, size: int, B: int) -> Q:
    return Q(B*sum(k*k for k in counts.values()),size*size)


def exact_row(lifted, circles, carries, A: int, m: int, multiplier: int = 1):
    B=16**m
    cells, words = Counter(), Counter()
    exceptions=[]
    for n in range(A, 2*A):
        x=circles[n]
        w=floor(B*x)
        R=source_block(n,m,multiplier)
        K=floor(lifted[n+m])-B*floor(lifted[n])
        word=sum(16**(m-j)*carries[n+j] for j in range(1,m+1))
        assert K==word==floor(B*x+R)
        b=K-w
        assert R<1 and b in (0,1)
        assert ((K % B)!=w)==(b==1)
        assert circles[n+m] == B*x+R-K
        if b:
            assert 0 <= circles[n+m] < R
            exceptions.append(n)
        cells[w]+=1; words[K % B]+=1
    theorem=bound(A,m,C*max(multiplier,1))
    if theorem["applicable"]:
        assert len(exceptions)<=theorem["max_corrections"]
        for residue in range(m):
            hits=[n for n in exceptions if n % m==residue]
            assert all(b-a>=m*theorem["L"] for a,b in zip(hits,hits[1:]))
    Pc,Pw=pressure(cells,A,B),pressure(words,A,B)
    assert abs(Pc-Pw)<=Q(2*B*len(exceptions),A)
    return {"A":A,"m":m,"cell_pressure":str(Pc),"carry_pressure":str(Pw),
            "correction_indices":exceptions,"bound":theorem,
            "pressure_difference_bound":str(Q(2*B*len(exceptions),A)),
            "cell_counts":dict(sorted(cells.items())),"carry_counts":dict(sorted(words.items()))}


def interval_row(A: int,m: int,beta: Q):
    """Certify same-forcing completed orbit beta*16^n - T_n."""
    B=16**m; cells=Counter(); words=Counter(); exceptions=[]
    for n in range(A,2*A):
        tlo,thi=tail_interval(n)
        plo,phi=16**n*beta-thi,16**n*beta-tlo
        common_floor=floor(plo)
        assert common_floor==floor(phi)
        xlo,xhi=plo-common_floor,phi-common_floor
        wlo,whi=floor(B*xlo),floor(B*xhi)
        R=source_block(n,m)
        klo,khi=floor(B*xlo+R),floor(B*xhi+R)
        assert wlo==whi and klo==khi
        b=klo-wlo
        assert b in (0,1)
        if b: exceptions.append(n)
        cells[wlo]+=1; words[klo%B]+=1
    theorem=bound(A,m)
    if theorem["applicable"]:
        assert len(exceptions)<=theorem["max_corrections"]
    return {"A":A,"m":m,"cell_pressure":str(pressure(cells,A,B)),
            "carry_pressure":str(pressure(words,A,B)),"correction_indices":exceptions,
            "bound":theorem,"tail_interval_terms":24,
            "cell_counts":dict(sorted(cells.items())),"carry_counts":dict(sorted(words.items()))}


def digest_integers(values):
    h=sha256()
    for value in values:
        data=str(value).encode()
        h.update(len(data).to_bytes(8,"big"));h.update(data)
    return h.hexdigest()


def digest_rationals(values):
    h=sha256()
    for value in values:
        for number in (value.numerator,value.denominator):
            data=abs(number).to_bytes(max(1,(abs(number).bit_length()+7)//8),"big")
            h.update(b"-" if number<0 else b"+")
            h.update(len(data).to_bytes(8,"big"));h.update(data)
    return h.hexdigest()


def generate():
    N=2*max(EPOCHS)+max(DEPTHS)-1
    result={"schema":1,"parent":"749931f0f357c60ef4e21879d96b0306999f428f",
            "status":"exact finite certificates; no asymptotic selection conclusion",
            "N":N,"source_bound_constant":str(C),"families":{}}
    for name,seed,multiplier in (("original_zero",Q(),1),("rational_seed_1_5",Q(1,5),1),
                                 ("numerator_times_two_zero",Q(),2),("unforced_zero",Q(),0)):
        U,x,c=orbit(N,seed,multiplier)
        rows=[exact_row(U,x,c,A,m,multiplier) for A in EPOCHS for m in DEPTHS]
        result["families"][name]={"seed":str(seed),"source_multiplier":multiplier,
            "unwrapped_state_sha256":digest_rationals(U),
            "literal_carry_sha256":digest_integers(c[1:]),"rows":rows}
    beta=periodic_completion(11)
    for name,b in (("coherent_completion",Q()),("period_11_completion",beta)):
        result["families"][name]={"completion_beta":str(b),
            "rows":[interval_row(A,m,b) for A in EPOCHS for m in DEPTHS]}
    U,x,c=orbit(77)
    result["low_epoch_domain_probe"]=exact_row(U,x,c,37,3)
    return result


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    path=Path(__file__).with_name("FINITE_RECEIPT.json")
    result=generate()
    if args.write:
        path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    else:
        assert json.loads(path.read_text())==json.loads(json.dumps(result))
    for name,family in result["families"].items():
        print(name,[(r["A"],r["m"],r["cell_pressure"],len(r["correction_indices"])) for r in family["rows"]])
    print("PASS exact source paths, interval controls, correction spacing and pressure transport")


if __name__=="__main__": main()

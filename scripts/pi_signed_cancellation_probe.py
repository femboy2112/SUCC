#!/usr/bin/env python3
"""Exact finite instruments for the signed-cancellation obstruction dossier.

Only standard-library rational arithmetic is used. Trigonometric enclosures
reduce rational phases modulo one BEFORE any approximation, enclose pi by
Machin's alternating formula, and use rational Taylor remainders. Neither
finite samples nor a passing receipt certify normality. All analytic claims
are scoped in the accompanying paper proofs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
from typing import Iterable

PARENT_SHA = "fca58d3e0289e57596dd8ca74bace325a450df31"


def require_int(n, minimum=0):
    if type(n) is not int or n < minimum:
        raise ValueError("integer outside domain")
    return n


def four_pole(n: int) -> Q:
    require_int(n, 1)
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def cancelled(n: int) -> Q:
    require_int(n, 1)
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def authentic_states(N: int) -> tuple[Q, ...]:
    require_int(N)
    out = [Q(0)]
    for n in range(1, N+1):
        r = four_pole(n)
        if r != cancelled(n):
            raise ArithmeticError("source identity failed")
        out.append(16*out[-1]+r)
    return tuple(out)


def pc320_tail(n: int) -> Q:
    require_int(n)
    return Q(n+1, (2*n+1)*(4*n+1)*(8*n+1))


def pc320_state(n: int) -> Q:
    return Q(16**require_int(n))-pc320_tail(n)


def pc320_forcing(n: int) -> Q:
    require_int(n, 1)
    return 16*pc320_tail(n-1)-pc320_tail(n)


def tail_interval(n: int, terms: int = 16) -> tuple[Q, Q]:
    """T_n in (lo,hi), from exact finite source and r(m)<1/m², m>=2."""
    require_int(n, 1); require_int(terms, 1)
    lo = sum((four_pole(n+j)/16**j for j in range(1, terms+1)), Q(0))
    # Every omitted n+j is >=n+terms+1. Sum of 16^-j is 16^-terms/15.
    debt = Q(1, 15*16**terms*(n+terms+1)**2)
    return lo, lo+debt


def floor_q(x: Q) -> int:
    return x.numerator // x.denominator


def ceil_q(x: Q) -> int:
    return -floor_q(-x)


def outward(lo: Q, hi: Q, bits=48) -> tuple[Q, Q]:
    if lo > hi:
        raise ValueError("reversed interval")
    scale = 1 << bits
    return Q(floor_q(lo*scale), scale), Q(ceil_q(hi*scale), scale)


def arctan_interval(inv: int, terms: int = 32) -> tuple[Q, Q]:
    require_int(inv, 2); require_int(terms, 1)
    total = sum((Q((-1)**j, (2*j+1)*inv**(2*j+1)) for j in range(terms)), Q(0))
    nxt = Q((-1)**terms, (2*terms+1)*inv**(2*terms+1))
    return min(total, total+nxt), max(total, total+nxt)


@lru_cache(maxsize=None)
def pi_interval() -> tuple[Q, Q]:
    a,b = arctan_interval(5)
    c,d = arctan_interval(239)
    return outward(16*a-4*d, 16*b-4*c, 80)


def phase_interval(phase: Q, bits=48, order=40) -> tuple[tuple[Q,Q],tuple[Q,Q]]:
    """Outward cos(2π phase), sin(2π phase), no float conversion.

    Reduce exactly to [-1/2,1/2), round that bounded number to a binary
    rational, and Taylor-expand both real functions to degree `order`.
    The derivative bound one gives remainder <=4^(order+1)/(order+1)!.
    """
    if not isinstance(phase, Q):
        phase = Q(phase)
    require_int(bits, 8); require_int(order, 4)
    reduced = (phase+Q(1,2)) % 1-Q(1,2)
    scale = 1 << bits
    rounded = Q(floor_q(reduced*scale), scale)
    pl,pu = pi_interval(); pm=(pl+pu)/2
    x = 2*pm*rounded
    if abs(x) >= 4:
        raise ArithmeticError("Taylor domain broken")
    # Angle perturbation, using pi<22/7 and |rounded|<=1/2.
    angle_debt = Q(44,7)*abs(rounded-reduced)+(pu-pl)*abs(rounded)
    debt = angle_debt+Q(4**(order+1), factorial(order+1))
    real=Q(0); imag=Q(0); term=Q(1)
    for j in range(order+1):
        if j:
            term *= x/j
        if j%4 == 0: real += term
        elif j%4 == 1: imag += term
        elif j%4 == 2: real -= term
        else: imag -= term
    def clipped(v):
        lo,hi=outward(v-debt,v+debt,bits)
        return max(Q(-1),lo), min(Q(1),hi)
    return clipped(real),clipped(imag)


def square_interval(pair: tuple[Q,Q]) -> tuple[Q,Q]:
    a,b=pair
    if a>b: raise ValueError("reversed interval")
    return (Q(0) if a<=0<=b else min(a*a,b*b), max(a*a,b*b))


def energy_interval(phases: Iterable[Q], modulus: int, h=1) -> tuple[Q,Q]:
    """Certified E=M/N² sum |class phase sum|² on indices 0..N-1."""
    require_int(modulus,1)
    if type(h) is not int: raise ValueError("integer h")
    phases=tuple(phases); N=len(phases)
    if not N: raise ValueError("nonempty phases")
    sums=[[Q(0)]*4 for _ in range(modulus)]
    for n,q in enumerate(phases):
        (rl,rh),(il,ih)=phase_interval(h*q)
        row=sums[n%modulus]
        row[0]+=rl;row[1]+=rh;row[2]+=il;row[3]+=ih
    lo=Q(0);hi=Q(0)
    for a,b,c,d in sums:
        rl,rh=square_interval((a,b));il,ih=square_interval((c,d))
        lo+=rl+il;hi+=rh+ih
    return outward(Q(modulus,N*N)*lo,Q(modulus,N*N)*hi,40)


def gaussian_energy(values: Iterable[tuple[Q,Q]], modulus: int) -> tuple[Q,Q]:
    """Exact (E,Q_M) for Gaussian rational values, including unequal cells."""
    require_int(modulus,1)
    values=tuple(values);N=len(values)
    if not N: raise ValueError("nonempty values")
    counts=[0]*modulus;sums=[[Q(0),Q(0)] for _ in range(modulus)]
    for n,(re,im) in enumerate(values):
        t=n%modulus;counts[t]+=1;sums[t][0]+=re;sums[t][1]+=im
    squares=[re*re+im*im for re,im in sums]
    E=Q(modulus,N*N)*sum(squares,Q(0))
    projected=sum((Q(s,c) for s,c in zip(squares,counts) if c),Q(0))/N
    return E,projected


def refinement_increment(values, coarse: int, fine: int) -> Q:
    """Exact weighted squared difference of child/parent conditional means."""
    require_int(coarse,1);require_int(fine,1)
    if fine%coarse: raise ValueError("not a nested partition")
    values=tuple(values);N=len(values)
    if not N: raise ValueError("nonempty values")
    def means(m):
        counts=[0]*m;sums=[[Q(0),Q(0)] for _ in range(m)]
        for n,(x,y) in enumerate(values):
            t=n%m;counts[t]+=1;sums[t][0]+=x;sums[t][1]+=y
        return counts,[(x/c,y/c) if c else (Q(0),Q(0)) for c,(x,y) in zip(counts,sums)]
    _,a=means(coarse);cs,b=means(fine)
    return sum((Q(cs[t],N)*((b[t][0]-a[t%coarse][0])**2+(b[t][1]-a[t%coarse][1])**2) for t in range(fine)),Q(0))


def debruijn(radix: int, order: int) -> tuple[int,...]:
    """Deterministic lexicographic cyclic de Bruijn word (FKM recursion)."""
    require_int(radix,2);require_int(order,1)
    if radix**order>100000:
        raise ValueError("declared finite enumeration budget exceeded")
    a=[0]*(radix*order);out=[]
    def visit(t,p):
        if t>order:
            if order%p==0: out.extend(a[1:p+1])
        else:
            a[t]=a[t-p];visit(t+1,p)
            for j in range(a[t-p]+1,radix):
                a[t]=j;visit(t+1,t)
    visit(1,1)
    return tuple(out)


def cyclic_counts(word, length):
    word=tuple(word);require_int(length,1)
    if not word: raise ValueError("nonempty word")
    return Counter(tuple(word[(n+j)%len(word)] for j in range(length)) for n in range(len(word)))


def periodic_phase(word, offset=0, radix=16) -> Q:
    word=tuple(word)
    if not word: raise ValueError("nonempty word")
    num=0
    for j in range(len(word)):
        d=word[(offset+j)%len(word)]
        if type(d) is not int or not 0<=d<radix: raise ValueError("invalid digit")
        num=radix*num+d
    return Q(num,radix**len(word)-1)


def marked_stages(reference, periods, endpoints):
    """Finite E6 marker construction; does not assert reference normality."""
    reference=tuple(reference);periods=tuple(periods);endpoints=tuple(endpoints)
    if len(periods)!=len(endpoints) or not periods:
        raise ValueError("nonempty matching schedules")
    if any(type(d) is not int or not 0<=d<16 for d in reference):
        raise ValueError("invalid reference digit")
    digits=[];records=[];previous_word=None;previous_length=0
    for period,end in zip(periods,endpoints):
        require_int(period,1);require_int(end,1)
        if period>len(reference) or end<=len(digits) or end>100000:
            raise ValueError("finite construction budget or schedule")
        start=len(digits);word=list(reference[:period]);predicted=None
        if previous_word is not None:
            predicted=previous_word[previous_length%len(previous_word)]
            word[0]=0 if predicted>=2 else 3
            if abs(word[0]-predicted)<2:raise ArithmeticError("marker separation")
        length=end-start
        digits.extend(word[j%period] for j in range(length))
        records.append({"start":start,"end":end,"period":period,
                        "word":tuple(word),"predicted":predicted})
        previous_word=word;previous_length=length
    return tuple(digits),tuple(records)


def finite_digit_value(digits):
    value=0;digits=tuple(digits)
    for d in digits:value=16*value+d
    return Q(value,16**len(digits))


def marker_certificate():
    """Exact approximation separation, valid for every remaining continuation."""
    digits,records=marked_stages(tuple(range(16))*2,(3,5,7,9,11),(4,16,64,256,1024))
    lo=finite_digit_value(digits);hi=lo+Q(1,16**len(digits))
    for record in records[:-1]:
        start=record['start'];end=record['end']
        rational=finite_digit_value(digits[:start])+periodic_phase(record['word'])/16**start
        separation=min(abs(lo-rational),abs(hi-rational))
        if lo<=rational<=hi:separation=Q(0)
        if separation<Q(1,16**(end+1)):raise ArithmeticError("marker lower bound")
        if max(abs(lo-rational),abs(hi-rational))>Q(1,16**end):
            raise ArithmeticError("common-prefix upper bound")
        if rational.denominator>16**start*(16**record['period']-1):
            raise ArithmeticError("periodic denominator")
    return {"scope":"finite marker controls, not a normality certificate",
            "certified_approximants":len(records)-1,"digits":len(digits),
            "sha256":hashlib.sha256(bytes(digits)).hexdigest()}


def sparse_phase_interval(n: int, lookahead: int = 32) -> tuple[Q,Q]:
    """Fractional part of 16^n ξ, ξ=Σ_j>=0 16^(-2^j), outward."""
    require_int(n);require_int(lookahead,1)
    cutoff=n+lookahead;p=1;lo=Q(0)
    while p<=cutoff:
        if p>n:lo+=Q(1,16**(p-n))
        p*=2
    # Omitted sparse positions are a subset of ALL positions >lookahead.
    return lo,lo+Q(1,15*16**lookahead)


def cut_status(y_interval, T_interval) -> int | None:
    """Prove membership in a one-sided digit cut; -1 = outside, None = unresolved.

    Input y enclosure must be contained in [0,1). A cut index 0..15 is
    returned only if the ENTIRE y interval lies in [a/16,a/16+T_low).
    """
    yl,yh=y_interval;tl,th=T_interval
    if not Q(0)<=yl<=yh<Q(1) or not Q(0)<tl<=th<Q(1,16):
        raise ValueError("invalid enclosure")
    for a in range(16):
        if Q(a,16)<=yl and yh<Q(a,16)+tl:
            return a
    for a in range(16):
        if yh>=Q(a,16) and yl<Q(a,16)+th:
            return None
    return -1


def ceil_log(base: int, target: int) -> int:
    require_int(base,2);require_int(target,1)
    power=1;j=0
    while power<target:power*=base;j+=1
    return j


def mixed_budget(N: int, h: int, lags: Iterable[int]) -> dict:
    require_int(N,1)
    if type(h) is not int or not h:raise ValueError("nonzero integer h")
    lags=tuple(lags)
    for lag in lags:require_int(lag,1)
    k=len(lags);d=sum(lags)
    w=max(1,ceil_log(16,abs(h)*2**k*N));D=d+w
    J=0
    while 2**J*D<N+D:J+=1
    m=isqrt(abs(h))
    if m*m<abs(h):m+=1
    bad=min(N,D*(2+J))
    bound=2*bad+Q(44,105)+2*m+Q(11*abs(h),112*m)
    return {"N":N,"h":h,"lags":lags,"order":k,"span":d,"w":w,"D":D,"J":J,"bad_count_upper":bad,"absolute_sum_error_upper":bound}


def interior_cut_bound(N: int, Qstart: int = 0) -> dict:
    """Paper-proved all-carrier bound; Qstart initial indices paid trivially."""
    require_int(N,1);require_int(Qstart)
    if Qstart>=N:raise ValueError("Qstart<N")
    L=0
    while 16**(L+2)<=15*(Qstart+2)**2:L+=1
    bound=Qstart+((N-Qstart)+L)//(L+1)
    return {"N":N,"Q":Qstart,"L":L,"nonzero_cut_count_upper":bound}


def sparse_wrap_bound(N: int) -> dict:
    """Paper two-sided deficit bound for the carrier 16^(n-1)xi."""
    require_int(N,1)
    H=max(1,ceil_log(16,200*(N+1)**2))
    bad=min(N,(H-1)*(1+(2*N).bit_length()-1))
    deficit_lower=(N.bit_length()-1)**2//4
    return {"N":N,"H":H,"bad_count_upper":bad,"deficit_lower":deficit_lower,"wrap_count_lower":N-bad}


def validate_payload(payload, expected):
    """Compare against a freshly reconstructed receipt, never trust input flags."""
    if payload.get("pi_normality_proved") is not False:
        raise ValueError("false normality authority")
    if payload != expected:
        raise ValueError("receipt/source/bound mismatch")


def authentic_y_interval(state: Q, n: int, terms=16):
    """Enclose {16^(n-1)pi} from the exact source Green identity."""
    lo,hi=tail_interval(n,terms);lo+=state%1;hi+=state%1
    if floor_q(lo)!=floor_q(hi):return None
    shift=floor_q(lo)
    return lo-shift,hi-shift


def mixing_transition(q: int):
    require_int(q,3)
    if q%2==0:raise ValueError("q must be coprime to radix16")
    probs=(Q(1,8),)+(Q(7,120),)*15
    P=[[Q(0) for _ in range(q)] for _ in range(q)]
    for j in range(q):
        for d,p in enumerate(probs):P[j][(16*j+d)%q]+=p
    return tuple(tuple(row) for row in P)


def matmul(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))) for i in range(len(a)))


def mixing_certificate(q=17):
    P=mixing_transition(q);m=ceil_log(16,q)
    R=tuple(tuple(Q(i==j) for j in range(q)) for i in range(q))
    for _ in range(m):R=matmul(R,P)
    if not all(sum(row)==1 for row in P):raise ArithmeticError("row sum")
    if not all(sum(P[i][j] for i in range(q))==1 for j in range(q)):raise ArithmeticError("column sum")
    lower=Q(7,120)**m
    minimum=min(x for row in R for x in row)
    if minimum<lower:raise ArithmeticError("Doeblin minorization")
    # Exact digit mean and the first Fourier factor at a primitive16th root.
    mean=sum((d*(Q(1,8) if d==0 else Q(7,120)) for d in range(16)),Q(0))
    first=Q(1,8)-Q(7,120)
    high_mode_lower=first*(1-Q(7,120)*Q(22,7))
    return {"q":q,"m":m,"entry_minimum":str(minimum),"minorization_lower":str(lower),"digit_mean":str(mean),"first_factor":str(first),"mode_q_real_lower":str(high_mode_lower)}


def qstr(q):return str(q)


def source_hashes():
    script=Path(__file__).resolve()
    candidate=script.parent.parent/"tests"/"test_pi_signed_cancellation_probe.py"
    if not candidate.exists():candidate=script.with_name("test_pi_signed_cancellation_probe.py")
    files=[script]
    if candidate.exists():files.append(candidate)
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def build_receipt():
    U=authentic_states(256)
    energies=[]
    for N,M,h in ((48,16,1),(144,48,1),(144,48,2),(256,48,17),(256,48,1)):
        lo,hi=energy_interval(U[1:N+1],M,h)
        cl,ch=energy_interval((pc320_state(n) for n in range(1,N+1)),M,h)
        energies.append({"N":N,"M":M,"h":h,"authentic_interval":[qstr(lo),qstr(hi)],"pc320_interval":[qstr(cl),qstr(ch)]})
    values=tuple((Q((-1)**n),Q(0)) for n in range(32))
    e1,q1=gaussian_energy(values,1);e2,q2=gaussian_energy(values,2)
    if (e1,e2,q2-q1,refinement_increment(values,1,2))!=(0,1,1,1):raise ArithmeticError("refinement control failed")
    actual_seam=Counter()
    for n in range(1,257):
        y=authentic_y_interval(U[n],n)
        actual_seam[None if y is None else cut_status(y,tail_interval(n))]+=1
    seam=[]
    for end in (64,256,1024):
        counts=Counter(cut_status(sparse_phase_interval(n-1,24),tail_interval(n,12)) for n in range(1,end+1))
        seam.append({"N":end,"certified_wrap":counts[0],"certified_nonzero":sum(counts[a] for a in range(1,16)),"certified_outside":counts[-1],"ambiguous":counts[None]})
    db=[]
    for radix,order in ((2,1),(2,5),(16,1),(16,2)):
        word=debruijn(radix,order)
        for r in range(1,order+1):
            counts=cyclic_counts(word,r)
            if len(counts)!=radix**r or set(counts.values())!={radix**(order-r)}:raise ArithmeticError("de Bruijn failure")
        db.append({"radix":radix,"order":order,"length":len(word),"sha256":hashlib.sha256(bytes(word)).hexdigest()})
    return {"schema":1,"parent_sha":PARENT_SHA,"authority":"VERIFIED_FINITE; paper limits separate","pi_normality_proved":False,"source_hashes":source_hashes(),"energies":energies,"actual_pi_seams":{"N":256,"certified_wrap":actual_seam[0],"certified_nonzero":sum(actual_seam[a] for a in range(1,16)),"certified_outside":actual_seam[-1],"ambiguous":actual_seam[None]},"marker_control":marker_certificate(),"mixing_control":mixing_certificate(),"refinement_witness":{"E_1":"0","E_2":"1","weighted_increment":"1"},"sparse_seams":seam,"debruijn":db,"interior_cut_budgets":[interior_cut_bound(10**6,1000),interior_cut_bound(10**9,1000000)],"sparse_wrap_budgets":[sparse_wrap_bound(10**6),sparse_wrap_bound(10**9)],"mixed_budgets":[{k:(qstr(v) if isinstance(v,Q) else v) for k,v in mixed_budget(10**6,17,lags).items()} for lags in ((1,),(1,2,3),(31,127))]}


def serialized_receipt():
    return json.dumps(build_receipt(),sort_keys=True,indent=2)+"\n"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument("--write",type=Path)
    group.add_argument("--verify",type=Path)
    args=parser.parse_args();expected=serialized_receipt()
    if args.verify:
        if args.verify.read_text()!=expected:
            raise SystemExit("RECEIPT REJECTED: bytes, source hashes, values or authority differ")
        print("VERIFIED_FINITE receipt replay passed; normality remains OPEN")
    elif args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True);args.write.write_text(expected)
        print("Wrote exact finite receipt; normality remains OPEN")
    else:print(expected,end="")


if __name__=="__main__":main()

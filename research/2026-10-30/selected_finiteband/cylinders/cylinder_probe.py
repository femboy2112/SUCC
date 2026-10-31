"""Exact source/word controls; paper proofs are in CYLINDERS_AND_STONEHAM.md."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from math import comb
import json

DELTA = Q(1, 20)


def source(n):
    if n < 1:
        raise ValueError("n>=1")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def tail_interval(n, terms=14):
    lo = sum((source(n+j)/16**j for j in range(1, terms+1)), Q())
    return lo, lo+source(n+terms+1)/(15*16**terms)


def tail_difference_interval(n, terms=14):
    a, b = tail_interval(n, terms)
    c, d = tail_interval(n+1, terms)
    return a-d, b-c


def centered(x):
    return (x+Q(1, 2)) % 1-Q(1, 2)


def distance(x):
    return abs(centered(x))


def classify_interval(lo, hi, threshold=DELTA):
    """Strict slip bool, or None if a threshold/circle seam is unresolved."""
    if hi < lo or hi-lo >= 1:
        raise ValueError("ordered interval of width<1 required")
    # Distance is 1-Lipschitz on R; this enclosure is seam safe.
    mid=(lo+hi)/2
    radius=(hi-lo)/2
    dlo=max(Q(), distance(mid)-radius)
    dhi=min(Q(1, 2), distance(mid)+radius)
    if dlo > threshold:
        return True
    if dhi <= threshold:
        return False
    return None


def digits(x, count):
    out=[]
    for _ in range(count):
        x=16*(x % 1)
        d=x.numerator//x.denominator
        out.append(d)
        x-=d
    return tuple(out)


def word_bound(length, slips):
    return 16*sum(comb(length-1, j)*15**j
                  for j in range(min(2*slips, length-1)+1))


def transitions(word):
    return sum(a != b for a, b in zip(word, word[1:]))


def bbp_words(count):
    u=Q()
    points=[]
    word=[]
    slip=[]
    for n in range(1, count+1):
        u=(16*u+source(n)) % 1
        points.append(u)
        a, b=tail_interval(n)
        low=(16*(u+a)).__floor__()
        high=(16*(u+b)).__floor__()
        if low != high:
            raise AssertionError("uncertified digit; extend the tail")
        word.append(low % 16)
        slip.append(distance(15*u+source(n+1)) > DELTA)
    return points, tuple(word), tuple(slip)


def stoneham_surrogate(c, N):
    if c < 2:
        raise ValueError("c>=2")
    births=set()
    t=c
    while t < N:
        births.add(t)
        t*=c
    z=Q()
    out=[z]
    for n in range(1, N):
        z=(16*z+(Q(1, n) if n in births else 0)) % 1
        out.append(z)
    return out


def stoneham_stage(c, p):
    start=c**p
    return stoneham_surrogate(c, c*start)[start:]


def stoneham_stage_index(c, N):
    if N <= c:
        raise ValueError("N>c")
    p=1
    while c**(p+1) <= N-1:
        p+=1
    return p


def stoneham_energy_bound_parts(c, N, H):
    if c not in (3, 5) or H < 2:
        raise ValueError("c in {3,5}, H>=2")
    p=stoneham_stage_index(c, N)
    # Return exact rational coefficients: constant plus pi times coefficient.
    return Q(c)+Q(H*(c+c*(c-1)*p), N), Q(4*(H*H-1), 45*(c-1)*N)


def walsh_refinement(cycle, depth):
    N=len(cycle)
    child=Counter(tuple(cycle[(i+j) % N] for j in range(depth+1))
                  for i in range(N))
    parent=Counter(tuple(cycle[(i+j) % N] for j in range(depth))
                   for i in range(N))
    q0=Q(16**depth*sum(v*v for v in parent.values()), N*N)
    q1=Q(16**(depth+1)*sum(v*v for v in child.values()), N*N)
    currents=defaultdict(int)
    for word, count in child.items():
        for mask in range(1, 16):
            sign=(-1)**((word[-1] & mask).bit_count())
            currents[(word[:-1], mask)]+=sign*count
    rhs=Q(16**depth*sum(v*v for v in currents.values()), N*N)
    return q0, q1, rhs, len({key[1] for key in currents})


def debruijn():
    # Iterative Euler circuit, independent of parent FKM construction.
    neighbors=[list(range(15, -1, -1)) for _ in range(16)]
    stack=[0]
    circuit=[]
    while stack:
        v=stack[-1]
        if neighbors[v]:
            stack.append(neighbors[v].pop())
        else:
            circuit.append(stack.pop())
    return tuple(circuit[::-1][1:])


def run():
    assert DELTA+Q(16, 17**3) < Q(1, 17)
    assert Q(15, 4096)+Q(16, 17**3) < DELTA
    assert Q(1, 17)-Q(16, 17**3) > DELTA
    _, word, slip=bbp_words(320)
    assert word[:8] == (2, 4, 3, 15, 6, 10, 8, 8)
    source_rows=[]
    for A in (2, 17, 61, 127, 251):
        for L in (4, 8, 16, 32):
            block=word[A-1:A-1+L]
            K=sum(slip[A-1:A-1+L])
            changes=transitions(block)
            assert changes <= 2*K
            assert K <= 2*changes+2
            source_rows.append(dict(A=A,L=L,strict_slips=K,changes=changes,
                                    word=''.join(format(x,'X') for x in block)))
    rational_checks=0
    ambiguous=0
    tail=[tail_difference_interval(n) for n in range(2, 10)]
    for numerator in range(1021):
        y=Q(numerator, 1021)
        word0=digits(y, 8)
        states=[]
        for lo, hi in tail:
            states.append(classify_interval(15*y+lo,15*y+hi))
            y=16*y % 1
        if None in states:
            ambiguous+=1
        else:
            assert transitions(word0) <= 2*sum(states)
            assert sum(states) <= 2*transitions(word0)+2
            rational_checks+=1
    reverse_checks=0
    for A in (2, 13, 103):
        for L in (1, 3, 7):
            for digit in range(16):
                for remainder in (Q(), Q(1, 17), Q(16, 17)):
                    value=Q(digit*(16**(L+2)-1),15*16**(L+2))+remainder/16**(L+2)
                    y=value
                    for n in range(A,A+L):
                        lo,hi=tail_difference_interval(n)
                        assert classify_interval(15*y+lo,15*y+hi) is False
                        y=16*y % 1
                    reverse_checks+=1
    periodic=[]
    y=Q(1,255)
    for n in range(1, 129):
        lo,hi=tail_difference_interval(n)
        state=classify_interval(15*y+lo,15*y+hi)
        if n>=2:
            assert state is True
        assert (17*y) % 1 == Q(1,15)
        if n in (1,2,3,64,127,128):
            periodic.append(dict(n=n,completed=str(y),strict_slip=state,
                                 tail_low=str(lo),tail_high=str(hi)))
        y=16*y % 1
    stages=[]
    for c,p in ((3,1),(3,2),(3,4),(3,5),(5,1),(5,2),(5,3)):
        stage=stoneham_stage(c,p)
        counts=Counter(stage)
        expected={Q(1+c*j,c**p) for j in range(c**(p-1))}
        assert set(counts)==expected
        assert set(counts.values())=={c*(c-1)}
        stages.append(dict(c=c,p=p,grid_size=len(counts),multiplicity=c*(c-1),
                           stage_length=len(stage)))
    c2=stoneham_stage(2,3)
    assert len(set(c2)) != 2**2
    wrows=[]
    for label, cycle in (('period2',(0,1)),('debruijn_order2',debruijn())):
        for depth in range(5):
            q0,q1,rhs,masks=walsh_refinement(cycle,depth)
            assert q1-q0==rhs and masks==15
            wrows.append(dict(control=label,depth=depth,Q=str(q0),next_Q=str(q1),
                              defect=str(rhs),nontrivial_masks=masks))
    return dict(status='PASS',source_rows=source_rows,
                source_digits_certified=len(word),source_slips=sum(slip),
                rational_transducer_checks=rational_checks,ambiguous=ambiguous,
                constant_word_reverse_checks=reverse_checks,period2_rows=periodic,
                stoneham_stages=stages,c2_grid_premise_refuted=True,
                walsh_rows=wrows,scope='finite exact checks; asymptotic statements use paper proofs')


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))

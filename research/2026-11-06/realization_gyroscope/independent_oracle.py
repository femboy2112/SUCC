"""Small, differently decomposed exact arithmetic oracle for research-only probe.

Uses the combined A/D rational source formula and a direct closed Green sum,
not the main implementation's iterative state recurrence. Same arithmetic
provenance, so this is not an independent mathematical referee.
"""
from fractions import Fraction
from gyroscope import forcing, source_state, tail_interval, prefix, circle, interleave_phase


def alternative_source(n):
    a=120*n*n-89*n+16
    d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return Fraction(a,d)


def closed_state(n, seed=0):
    return (16**n*Fraction(seed) + sum((16**(n-j)*alternative_source(j)
               for j in range(1,n+1)),Fraction(0))) % 1


def check():
    source_cases=0
    state_cases=0
    interval_cases=0
    for n in [1,2,3,4,5,9,17,41,89,173,307,509]:
        assert alternative_source(n)==forcing(n)
        source_cases += 1
    for seed in [0,Fraction(1,5),Fraction(7,31)]:
        for n in [0,1,2,3,5,8,13,19,31,61,97]:
            assert closed_state(n,seed)==source_state(n,seed)
            state_cases +=1
    for n in [1,2,5,13,29,59,131]:
        lo,hi=tail_interval(n,12)
        # A distinct 40-step sum must be inside the rigorous enclosure.
        direct=sum((Fraction(1,16**j)*alternative_source(n+j)
                    for j in range(1,41)),Fraction(0))
        assert lo < direct < hi
        assert hi <= Fraction(1,15*(n+1)**2)
        interval_cases +=1
    # Two independent ways to read the 4-phase factor map.
    for beta in [Fraction(1,5),Fraction(7,31),Fraction(3,17)]:
        x=beta
        slots=[]
        for i in range(63):
            slots.append(x%1)
            x=(2*x)%1
        assert slots[:60]==list(interleave_phase(beta,15))
    # Independent exact radix digit extraction via floor(16^m x) mod 16.
    for x in (closed_state(31),closed_state(61),Fraction(7,31)):
        for m in range(1,8):
            digit=( (16**m*x).numerator // (16**m*x).denominator ) % 16
            assert digit == prefix(x,16,m)[-1]
    print(f'INDEPENDENT_FORMULA_ORACLE PASS | {source_cases} source, '
          f'{state_cases} closed-state, {interval_cases} interval checks, '
          'phase/recoding checks PASS')

if __name__=='__main__': check()

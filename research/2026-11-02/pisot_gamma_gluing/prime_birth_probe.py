"""Original BBP first-pole prime birth: exact finite rationals, no phase floats.

Proof that a signed window with newborn last term is nonzero is in
PRIME_BIRTH_STRICTNESS.md and uses field-degree theory, not this script.
"""
import importlib.util
from pathlib import Path
from fractions import Fraction

spec=importlib.util.spec_from_file_location(
    "pg_original",Path(__file__).with_name("pell_gamma.py"))
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

PRIMES=(17,41,73,89,97,113,137,193,233,241)


def valuation(q,p):
    if q==0:raise ValueError("only nonzero rational valuations")
    a=abs(q.numerator);b=q.denominator;k=0
    while a%p==0:
        a//=p;k+=1
    while b%p==0:
        b//=p;k-=1
    return k


def exact_prime_birth_row(p):
    b=(p+7)//8
    assert p>5 and 8*b-7==p
    assert all(g.state(i).denominator%p for i in range(b))
    B=g.state(b)-Fraction(4,p)
    assert B.denominator%p
    assert valuation(g.state(b),p)==-1
    return {"p":p,"birth_time":b,"v_p_U_b":-1,
            "all_earlier_states_p_free":True,
            "newborn_p_free_cofactor":True}


if __name__=="__main__":
    import json
    print(json.dumps([exact_prime_birth_row(p) for p in PRIMES],indent=2))

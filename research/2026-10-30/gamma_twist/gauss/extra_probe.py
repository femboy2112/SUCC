"""Exact fiber, prime-power conductor, and Galois-average adversarial probes."""
import itertools
import json
from fractions import Fraction
from math import gcd

import sympy as s

from gauss_exact import AUTH, MUTATION, Cyclo, GaussSystem, cofiber, orbit, valuation


def main():
    matrix = s.Matrix([[(u*d)%8 for d in (1,4,5,6)] for u in (1,3,5,7)])
    assert matrix.rank()==3 and matrix[:3,:3].det()==64
    assert matrix.nullspace()==[s.Matrix(MUTATION)]
    gauss = GaussSystem(17)
    authentic=gauss.weighted()
    assert gauss.character(2,2)==Cyclo.monomial(17,scalar=-1)
    checked=0
    # The valuation equations already exclude all off-kernel candidates;
    # full exact Gauss equality is then checked on every surviving vector.
    candidates=[]
    for delta in itertools.product(range(-3,4),repeat=4):
        if matrix*s.Matrix(delta) != s.zeros(4,1):
            continue
        c=tuple(a+b for a,b in zip(AUTH,delta))
        equal=gauss.weighted(c)==authentic
        assert equal==(delta[0]%2==0)
        candidates.append({"delta":list(delta),"full_equality":equal})
        checked+=1
    for t in range(-6,7):
        c=tuple(a+t*b for a,b in zip(AUTH,MUTATION))
        assert (gauss.weighted(c)==authentic)==(t%2==0)
    births=[]
    for ell in (3,5,7,11,13):
        for a in (2,3):
            Q=ell**a
            n=(Q+7)//8 if Q%8==1 else (Q+3)//8 if Q%8==5 else (Q+1)//4
            value=orbit(n)
            assert valuation(value,ell)==-a
            removed=17
            _,_,v=cofiber(value,removed)
            assert valuation(v,ell)==-a
            births.append({"ell":ell,"a":a,"n":n,"vp":-a,
                "removed_primary":removed,"remaining_root_has_prime_square":True})
    def null_prefix(N):
        z=Fraction()
        for n in range(1,N+1):
            z=16*z+sum((Fraction(c,8*n-8+d)
                for d,c in enumerate((-8,8,4,8,2,2,-1),start=1)),Fraction())
        return z
    averages=[]
    for family,n,p,value in (("authentic",2,13,orbit(2)),
                              ("seven_pole_null",20,13,null_prefix(20)),
                              ("seven_pole_null",100,13,null_prefix(100))):
        _,_,v=cofiber(value,p)
        D=v.denominator
        factors=s.factorint(D)
        mu=0 if max(factors.values())>1 else (-1)**len(factors)
        phi=int(s.totient(D))
        if family=="seven_pole_null":
            assert -Fraction(1,8*n+1)<value<0
        assert mu==0
        averages.append({"family":family,"n":n,"p":p,"cofiber_order":str(D),
            "galois_average":str(Fraction(mu,phi)),
            "selected_null_character_distance_upper":str(Fraction(44,7*(8*n+1)))
                if family=="seven_pole_null" else None,
            "bound_basis":"2*pi<44/7 and |E_n|<1/(8n+1)" if family=="seven_pole_null" else None})
    # Explicit trace computation in a cyclotomic polynomial quotient at D=315.
    X=s.Symbol('X')
    P=s.Poly(s.cyclotomic_poly(315,X),X)
    primitive=s.Poly.from_dict({(a,):1 for a in range(315) if gcd(a,315)==1},X)
    assert primitive.rem(P).is_zero
    print(json.dumps({"status":"PASS","single_prime_age_matrix":[list(map(int,row)) for row in matrix.tolist()],
        "rank":3,"minor":64,"kernel":[1,-3,1,1],
        "finite_cube_size":7**4,"kernel_survivors":candidates,
        "additional_t_values":list(range(-6,7)),"prime_power_births":births,
        "galois_average_controls":averages,"exact_primitive_trace_315":0},indent=2))


if __name__ == '__main__':
    main()

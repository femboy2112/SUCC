"""Separate Cartesian field/character enumeration and univariate cyclotomic oracle.

Imports neither gauss_exact nor tests. Reads emitted exact objects, constructs
F_p[u]/(u^2-d) with polynomial convolution, locates order-eight characters by
power residue (no full discrete-log table), and reduces in Q[X]/Phi_(8p).
SymPy supplies only polynomial reduction; the field enumeration is explicit.
"""
import argparse
import json
from fractions import Fraction
import sympy as sp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("receipt")
    args = parser.parse_args()
    report = json.load(open(args.receipt))
    X = sp.Symbol("X")
    checks = []
    for row in report["gauss_rows"]:
        p, f, q, d = (row[key] for key in ("p","f","q","quadratic_nonsquare"))
        modulus = sp.Poly(sp.cyclotomic_poly(8*p,X),X,domain=sp.QQ)

        def multiply(a,b):
            poly = [0,0,0]
            for i in range(2):
                for j in range(2):
                    poly[i+j] += a[i]*b[j]
            return ((poly[0]+d*poly[2])%p,poly[1]%p)

        def power(a,k):
            z=(1,0)
            for bit in bin(k)[2:]:
                z=multiply(z,z)
                if bit == '1':
                    z=multiply(z,a)
            return z

        rho=power(tuple(row["generator"]),(q-1)//8)
        eighth={power(rho,j):j for j in range(8)}
        assert len(eighth)==8
        raw={j:[0]*(8*p) for j in range(1,8)}
        for a in range(p):
            for b in range(p if f==2 else 1):
                if a==b==0:
                    continue
                x=(a,b)
                character_index=eighth[power(x,(q-1)//8)]
                conjugate=power(x,p) if f==2 else (0,0)
                trace=(a+conjugate[0])%p
                if f==2:
                    assert (b+conjugate[1])%p==0
                for j in range(1,8):
                    raw[j][(-p*j*character_index+8*trace)%(8*p)] += 1
        for delta, coeff in raw.items():
            exact=sp.Poly.from_dict({(i,):c for i,c in enumerate(coeff) if c},X,domain=sp.QQ).rem(modulus)
            imported=row["gauss_sums"][str(delta)]
            converted={}
            for index,a in enumerate(imported["numerators"]):
                i,j=divmod(index,p-1)
                exponent=(p*i+8*j)%(8*p)
                converted[(exponent,)]=converted.get((exponent,),0)+sp.Rational(a,imported["denominator"])
            target=sp.Poly.from_dict(converted,X,domain=sp.QQ).rem(modulus)
            assert exact == target, (p,delta)
        # Separate product order: residue classes mod p, then whole blocks.
        M=p**3
        gamma={}
        for numerator in range(1,8):
            n=numerator*pow(8,-1,M)%M
            values=[]
            for residue in range(1,p):
                value=1
                for integer in range(residue,n,p):
                    value=value*integer%M
                values.append(value)
            answer=(-1)**n
            for value in reversed(values):
                answer=answer*value%M
            gamma[numerator]=answer%M
        unit=1
        for i in range(f):
            for delta,c in zip((1,4,5,6),(4,-2,-1,-1)):
                unit=unit*pow(gamma[delta*p**i%8],c,M)%M
        assert unit==row["gk"]["unit_mod_p_power"]
        checks.append({"p":p,"exact_gauss_sums_compared":7,"gamma_unit_mod_p3":unit})
    # Direct weighted-prefix formula, separate from recurrence implementation.
    def prefix(N):
        return sum((Fraction(c*16**(N-j),8*j-8+d)
            for j in range(1,N+1) for c,d in zip((4,-2,-1,-1),(1,4,5,6))),Fraction())
    for row in report["source_birth_and_cancellation_witnesses"]:
        u=prefix(row["n"])
        v=Fraction(row["cofiber"])
        difference=u-Fraction(row["primary_numerator"],row["primary_denominator"])-v
        assert difference.denominator==1
        ell=row["foreign_odd_prime"]
        assert v.denominator%ell==0 and ell not in (2,row["p"])
    print(json.dumps({"status":"PASS","distinct_implementation_not_independent_proof_authority":True,
        "field_and_gamma_rows":checks,"exact_gauss_sum_comparisons":7*len(checks),
        "cofiber_prefix_comparisons":len(report["source_birth_and_cancellation_witnesses"])},indent=2))


if __name__ == "__main__":
    main()

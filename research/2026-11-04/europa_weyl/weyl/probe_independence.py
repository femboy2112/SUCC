"""Relative Mann-slicing certificates, using only actual rational differences."""
from fractions import Fraction
from math import prod
import json
from finite_weyl import trajectory
from probe_separation import primes


def source_check(A):
    _, points = trajectory(2*A-1)
    top = [p for p in primes(16*A) if p > 4*A]
    rows = []
    for h, B in ((-1,1), (16**A,15), (prod(top[:3]),3**7*prod(top[3:5]))):
        misses = []
        minimum_witness = None
        for t in range(A+1,2*A):
            for n in range(A,t):
                denominator = (h*(points[t]-points[n])).denominator
                prime = next((p for p in top if 4*t<p<=8*t-7 and
                              denominator % p == 0 and B % p != 0),None)
                if prime is None:
                    misses.append([n,t])
                elif minimum_witness is None or minimum_witness > prime:
                    minimum_witness = prime
        rows.append({"h":str(h),"B":str(B),"pairs":A*(A-1)//2,
                     "no_witness":misses, "minimum_witness":minimum_witness})
    return {"A":A,"rows":rows}


def seven_gon_control():
    # 1,z,...,z^5 is a basis; z^6 = -(1+z+...+z^5) by Phi_7.
    basis = [[int(i==j) for j in range(6)] for i in range(6)]
    columns = basis + [[-1]*6]
    def rank(vectors):
        rows = [list(map(Fraction,v)) for v in vectors]
        start = 0
        for col in range(6):
            pivot = next((i for i in range(start,len(rows)) if rows[i][col]),None)
            if pivot is None:
                continue
            rows[pivot],rows[start]=rows[start],rows[pivot]
            for row in rows[start+1:]:
                scale = row[col] / rows[start][col]
                for j in range(6):
                    row[j] -= scale*rows[start][j]
            start += 1
        return start
    sums = list(map(sum,zip(*columns)))
    ranks = [rank(columns[:i]+columns[i+1:]) for i in range(7)]
    assert sums == [0]*6 and ranks == [6]*7
    # The field contains z when B=7: (-z)*1 + 1*z = 0.
    field_relation = [a-b for a,b in zip(columns[1],columns[1])]
    return {"complete_sum":sums,"one_omission_ranks":ranks,
            "field_conductor_7_relation":field_relation}


if __name__ == "__main__":
    print(json.dumps({"epochs":[source_check(A) for A in (31,54,89)],
                      "seven_gon":seven_gon_control()},indent=2))

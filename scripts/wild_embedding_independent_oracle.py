"""INDEPENDENT finite group-matrix oracle for Alexander commutator depth.

No import from the primary wild source code or zero-side zeta/spectral data.
This verifies only exact algebraic identities through stage four, not
Alexander's 3D topological realization (classical Hatcher import).
"""
from __future__ import annotations
import json


def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def multiply(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def invert_uni(A):
    """Inverse of I+N by finite alternating nilpotence sum."""
    n=len(A)
    N=[[A[i][j]-int(i==j) for j in range(n)] for i in range(n)]
    I=identity(n)
    acc=identity(n)
    term=identity(n)
    for power in range(1,n):
        term=multiply(term,N)
        for i in range(n):
            for j in range(n):
                acc[i][j]+=(-1)**power*term[i][j]
    assert multiply(A,acc)==I and multiply(acc,A)==I
    return acc


def bracket(A,B):
    return multiply(multiply(multiply(A,B),invert_uni(A)),invert_uni(B))


def nested(degree,start,n):
    if degree==0:
        M=identity(n)
        M[start][start+1]=1
        return M
    left=nested(degree-1,start,n)
    right=nested(degree-1,start+2**(degree-1),n)
    return bracket(left,right)


def report():
    rows=[]
    for k in range(5):
        dim=2**k+1
        actual=nested(k,0,dim)
        expected=identity(dim)
        expected[0][-1]=1
        assert actual==expected
        rows.append({'depth':k,'matrix_dimension':dim,
                     'top_right_entry':actual[0][-1],
                     'all_lower_upper_entries_zero':True,
                     'nilpotency_class':2**k})
    return {'status':'INDEPENDENT_INTEGER_MATRIX_CALIBRATION',
            'source':'Alexander_Hatcher_group_substitution_not_3D_geometry',
            'unitriangular_detectors':rows,
            'RH_proved':False}


if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))

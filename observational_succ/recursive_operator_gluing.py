"""Exact finite block-Schur certificates for model-of-model signed interactions.

Finite rational algebra only. Matrices are declared candidate interaction blocks;
no identification with the completed Weil operator is inferred.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations

class CouplingError(ValueError):pass

def rat(x):
    if type(x) not in (Q,int):raise CouplingError('exact rational entries required')
    return Q(x)

def matrix(rows):
    if not rows or any(not r for r in rows):raise CouplingError('empty matrix')
    n=len(rows[0])
    if any(len(r)!=n for r in rows):raise CouplingError('ragged matrix')
    return tuple(tuple(rat(x) for x in row) for row in rows)

def symmetric(A):return len(A)==len(A[0]) and all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))
def minor(M, subset):return tuple(tuple(M[i][j] for j in subset) for i in subset)

def determinant(M):
    A=[list(row) for row in matrix(M)]
    n=len(A)
    if len(A[0])!=n:raise CouplingError('determinant needs square')
    sign=1
    for i in range(n):
        pivot=next((k for k in range(i,n) if A[k][i]),None)
        if pivot is None:return Q()
        if pivot!=i:
            A[i],A[pivot]=A[pivot],A[i]
            sign=-sign
        v=A[i][i]
        for j in range(i+1,n):
            factor=A[j][i]/v
            for k in range(i,n):A[j][k]-=factor*A[i][k]
    out=Q(sign)
    for i in range(n):out*=A[i][i]
    return out

def principal_minors(A):
    A=matrix(A)
    if not symmetric(A):raise CouplingError('symmetric required')
    return tuple((index,determinant(minor(A,index)))
                 for n in range(1,len(A)+1)
                 for index in combinations(range(len(A)),n))

def psd(A):return all(det>=0 for _,det in principal_minors(A))
def pd(A):
    A=matrix(A)
    if not symmetric(A):raise CouplingError('symmetric required')
    return all(determinant(minor(A,tuple(range(i))))>0 for i in range(1,len(A)+1))

def inverse(A):
    A=matrix(A);n=len(A)
    if len(A[0])!=n:raise CouplingError('inverse requires square')
    T=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        pivot=next((r for r in range(i,n) if T[r][i]),None)
        if pivot is None:raise CouplingError('non-invertible A')
        T[i],T[pivot]=T[pivot],T[i]
        v=T[i][i];T[i]=[x/v for x in T[i]]
        for k in range(n):
            if k!=i:
                v=T[k][i];T[k]=[x-v*y for x,y in zip(T[k],T[i])]
    return tuple(tuple(row[n:]) for row in T)

def transpose(M):return tuple(zip(*M))
def product(A,B):
    if len(A[0])!=len(B):raise CouplingError('composition dimension mismatch')
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),Q())
                       for j in range(len(B[0]))) for i in range(len(A)))

def block(A,C,B):
    A=matrix(A);C=matrix(C);B=matrix(B)
    n=len(A);m=len(B)
    if not symmetric(A) or not symmetric(B) or len(C)!=n or len(C[0])!=m:
        raise CouplingError('bad block shapes')
    return tuple(A[i]+C[i] for i in range(n))+tuple(tuple(C[k][j] for k in range(n))+B[j] for j in range(m))

@dataclass(frozen=True)
class SchurCertificate:
    a_pd: bool
    b_psd: bool
    complete_psd: bool
    schur_psd: bool
    schur: tuple[tuple[Q,...],...]
    schur_minors: tuple
    source_claim: str = 'DECLARED_BLOCKS_NOT_AUTHENTIC_WEIL'


def certify_schur(A,C,B):
    A=matrix(A);B=matrix(B);C=matrix(C)
    if not pd(A):raise CouplingError('A must be strictly positive for Schur inversion')
    if not symmetric(B) or len(C)!=len(A) or len(C[0])!=len(B):
        raise CouplingError('misaligned source blocks')
    cross=product(transpose(C),product(inverse(A),C))
    S=tuple(tuple(B[i][j]-cross[i][j] for j in range(len(B))) for i in range(len(B)))
    full=block(A,C,B)
    return SchurCertificate(True,psd(B),psd(full),psd(S),S,principal_minors(S))

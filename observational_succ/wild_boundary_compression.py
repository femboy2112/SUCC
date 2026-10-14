"""Exact observer-compression defect and its three-map coherence law.

A finite analogue of bulk commuting transport becoming noncommuting under
an observer window. Not a literal wild S² embedding or original Weil sign.

PR #86 already contains the genuine prime/Gamma boundary commutator.
This is an independent finite rational probe of the algebraic interface.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F

class BoundarySourceError(ValueError):
    pass

def _rat(x):
    if type(x) not in (F,int):
        raise BoundarySourceError("only exact rational source coordinates")
    return F(x)

def mat(rows):
    if not rows or not isinstance(rows,(list,tuple)) or not all(isinstance(r,(list,tuple)) for r in rows):
        raise BoundarySourceError("matrix is a nonempty list of rows")
    n=len(rows[0])
    if n<1 or any(len(r)!=n for r in rows):
        raise BoundarySourceError("matrix width mismatch")
    return tuple(tuple(_rat(v) for v in row) for row in rows)

def shape(A):
    A=mat(A)
    return len(A),len(A[0])

def zero(m,n):
    return tuple(tuple(F() for j in range(n)) for i in range(m))

def eye(n):
    if type(n) is not int or not 1<=n<=20:
        raise BoundarySourceError("exact finite positive order <=20")
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))

def transpose(A):
    A=mat(A)
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def add(A,B):
    A=mat(A);B=mat(B)
    if shape(A)!=shape(B):raise BoundarySourceError("matrix addition dimensions")
    return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))

def scale(s,A):
    s=_rat(s);A=mat(A)
    return tuple(tuple(s*x for x in row) for row in A)

def sub(A,B):
    return add(A,scale(-1,B))

def multiply(A,B):
    A=mat(A);B=mat(B)
    if len(A[0])!=len(B):raise BoundarySourceError("matrix composition dimensions")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F())
                       for j in range(len(B[0])))
                 for i in range(len(A)))

def commutator(A,B):
    return sub(multiply(A,B),multiply(B,A))

def compress(A,indices):
    A=mat(A)
    if len(A)!=len(A[0]):raise BoundarySourceError("square operator required")
    indices=tuple(indices)
    if (not indices or len(indices)!=len(set(indices))
        or any(type(x) is not int or not 0<=x<len(A) for x in indices)):
        raise BoundarySourceError("indexed lawful observer subspace required")
    return tuple(tuple(A[i][j] for j in indices) for i in indices)

def leakage(A,B,indices):
    """Phi(AB)-Phi(A)Phi(B) = P A (I-P) B P, EXACT."""
    A=mat(A);B=mat(B)
    n=len(A)
    if shape(A)!=(n,n) or shape(B)!=(n,n):
        raise BoundarySourceError("same square global source")
    I=tuple(indices)
    compress(A,I) # validation
    outer=tuple(j for j in range(n) if j not in I)
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in outer),F())
                       for j in I) for i in I)

def compression_defect(A,B,indices):
    return sub(compress(multiply(A,B),indices),
               multiply(compress(A,indices),compress(B,indices)))

def three_model_coherence(A,B,C,indices):
    """Exact associativity constraint on the NONFUNCTORIAL compression defect.

    Phi(A)D(B,C)-D(AB,C)+D(A,BC)-D(A,B)Phi(C)=0.
    This is an identity, NOT a claim of a Hochschild class for Phi.
    """
    D=lambda x,y:leakage(x,y,indices)
    phi=lambda x:compress(x,indices)
    term1=multiply(phi(A),D(B,C))
    term2=D(multiply(A,B),C)
    term3=D(A,multiply(B,C))
    term4=multiply(D(A,B),phi(C))
    return sub(add(sub(term1,term2),term3),term4)

def source_shift(n):
    """One authentic finite cyclic permutation carrier (toy)."""
    if type(n) is not int or not 3<=n<=20:
        raise BoundarySourceError("finite cycle order 3..20")
    return tuple(tuple(F(i==(j+1)%n) for j in range(n)) for i in range(n))

@dataclass(frozen=True)
class BoundaryCertificate:
    source_id:str
    basis:str
    epoch:int
    full_commutator:tuple
    compressed_commutator:tuple
    norm_square_frobenius:F
    leakage_difference_matches:bool
    triple_coherence_zero:bool
    gamma_source_identified:bool=False
    weil_sign_certified:bool=False

def finite_boundary_certificate(n=5,window=(0,1,2),
                                source_id="FINITE_CYCLIC_TOY",
                                epoch=0,basis="ORTHONORMAL_STATES"):
    """C=3I+T+T^* PSD and commutes with unitary T BEFORE compression.

    C = I +(I+T)(I+T)^*; so positivity is an exact sum-of-squares,
    not a floating spectral claim. Phi(C) is PSD, Phi(T) contraction.
    """
    if (not isinstance(source_id,str) or not source_id.strip()
        or not isinstance(basis,str) or not basis.strip()
        or type(epoch) is not int or epoch<0):
        raise BoundarySourceError("named exact source, basis, epoch required")
    T=source_shift(n);Tstar=transpose(T);Ident=eye(n)
    if multiply(T,Tstar)!=Ident or multiply(Tstar,T)!=Ident:
        raise BoundarySourceError("invalid unitary source transport")
    C=add(scale(3,Ident),add(T,Tstar))
    sum_of_squares=add(Ident,multiply(add(Ident,T),transpose(add(Ident,T))))
    if C!=sum_of_squares:raise BoundarySourceError("positive source factorization fails")
    full=commutator(T,C)
    phiT=compress(T,window)
    phiC=compress(C,window)
    small=commutator(phiT,phiC)
    difference=sub(leakage(C,T,window),leakage(T,C,window))
    coherence=three_model_coherence(T,C,Tstar,window)
    return BoundaryCertificate(source_id,basis,epoch,full,small,
         sum((x*x for row in small for x in row),F()),
         small==difference,coherence==zero(len(tuple(window)),len(tuple(window))))

def gauge_conjugation(A,signs):
    """Legal same-basis-transport by orthogonal diagonal +/-1 unitary."""
    A=mat(A)
    signs=tuple(signs)
    if len(A)!=len(A[0]) or len(signs)!=len(A) or any(type(s) is not int or s not in (-1,1) for s in signs):
        raise BoundarySourceError("declared diagonal unitary basis transport")
    return tuple(tuple(signs[i]*A[i][j]*signs[j] for j in range(len(A))) for i in range(len(A)))


def quadratic(A,vector):
    """Exact real Hermitian Rayleigh numerator on the declared vector."""
    A=mat(A)
    n=len(A)
    if n!=len(A[0]) or len(vector)!=n:
        raise BoundarySourceError("square matrix and typed state dimension")
    v=tuple(_rat(x) for x in vector)
    return sum((v[i]*A[i][j]*v[j] for i in range(n) for j in range(n)),F())


def unitary_sign_invariance_control():
    """Exact 2x2 rational 3-4-5 orthogonal transport cannot repair a sign.

    Any genuine unitary intertwining of Weil G_a preserves negative depth.
    THIS rational toy does not assert a wild-embedding->Weil unitary functor.
    """
    U=((F(3,5),-F(4,5)),(F(4,5),F(3,5)))
    G=((F(1),F()),(F(),F(-1)))
    if multiply(transpose(U),U)!=eye(2):
        raise BoundarySourceError("rational unitary failed")
    Gnew=multiply(multiply(U,G),transpose(U))
    w=(F(),F(1))
    Uw=tuple(sum((U[i][j]*w[j] for j in range(2)),F()) for i in range(2))
    before=quadratic(G,w)
    after=quadratic(Gnew,Uw)
    assert before==after==F(-1)
    return {"original_negative_rayleigh":before,
            "transported_negative_rayleigh":after,
            "unitary_basis_certified":True,
            "actual_wild_to_weil_intertwiner":False,
            "rh_proved":False}

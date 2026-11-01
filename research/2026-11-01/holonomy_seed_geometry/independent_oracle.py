"""Independent finite computational routes for the source, polynomial Gram
linear system, and curvature-to-state finite transport.

Does not import the principal module. Shared original mathematical source does
not constitute an independent external witness.
"""
from fractions import Fraction as F
from itertools import permutations


def original_combined(n):
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def original_orbit(n,s=F(0)):
    return 16**n*s+sum((16**(n-j)*original_combined(j) for j in range(1,n+1)),F())


def original_weighted_curvature_state(n):
    """Rebuild r_j from final r_n plus consecutive differences, not Pascal inversion."""
    rN=original_combined(n)
    values={n:rN}
    for j in range(n-1,0,-1):
        values[j]=values[j+1]+original_combined(j)-original_combined(j+1)
    return sum((16**(n-j)*values[j] for j in range(1,n+1)),F())


def determinant(M):
    n=len(M)
    if any(len(row)!=n for row in M):raise ValueError("square")
    total=F()
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=F((-1)**inversions)
        for i,j in enumerate(p):term*=M[i][j]
        total+=term
    return total


def gram_determinants(m):
    moments=[original_combined(j+1) for j in range(2*m)]
    return [determinant([[moments[i+j] for j in range(n)] for i in range(n)]) for n in range(1,m+1)]


def monic_polynomial_cramer(m):
    mat=[[original_combined(i+j+1) for j in range(m)] for i in range(m)]
    rhs=[-original_combined(i+m+1) for i in range(m)]
    d=determinant(mat)
    if not d:raise ArithmeticError("nonpositive moment Gram")
    coeff=[]
    for col in range(m):
        A=[[rhs[i] if j==col else mat[i][j] for j in range(m)] for i in range(m)]
        coeff.append(determinant(A)/d)
    return tuple(coeff)+(F(1),)


def geometric_qfi_var(n):
    a=[16**j for j in range(1,n+1)]
    return F(sum((x-y)**2 for x in a for y in a),2*n*n)


def geometric_shadow_mode_norm_sq(n):
    return sum((F(1,16**(2*(n-j))) for j in range(1,n+1)),F())/n

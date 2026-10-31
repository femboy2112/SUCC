"""Exact rational instruments for SHARPNESS.md; altered coherent seed only."""
from fractions import Fraction as F


def bulk_upper(m, b, A):
    """Rational majorant on |sum_(m<=n<=b)e(-A T_n)|, A positive rational."""
    if type(m) is not int or type(b) is not int or not 1 <= m <= b:
        raise ValueError('integer 1<=m<=b required')
    if type(A) not in (int, F) or A <= 0:
        raise ValueError('positive exact A required')
    A = F(A)
    return min(F(b-m+1), 1+F(11, 112*m*m)*A+F((8*b+6)**3, 45)/A)


def coherent_score_limit(c):
    """Paper theorem applies to exact 2<c<3; does not concern selected zero."""
    if type(c) not in (int, F) or not 2 < c < 3:
        raise ValueError('exact 2<c<3 required')
    c = F(c)
    return 4/c-4/(c*c)


def transport_obstruction(c):
    return 1-coherent_score_limit(c)

"""Independent exact source, curvature and geometric path checks (stdlib only)."""
from fractions import Fraction as F
from math import comb


def source_oracle(n:int)->F:
    # Independent positive Euler-density expression (polynomial quadrature).
    a=8*n-8
    return F(4,a+1)-F(2,a+4)-F(1,a+5)-F(1,a+6)

def bbp_oracle(n:int)->F:
    # Independent explicit convolution, not the sequential recurrence.
    return sum((16**(n-j)*source_oracle(j) for j in range(1,n+1)),F())

def geometric_squared_identity(y_lower:F, y_upper:F, y_next:F):
    """For exact algebraic y_k: (y_next-2)^2=4-y_k and 0<y_next<=2."""
    return y_lower==y_upper and (y_next-2)**2==4-y_lower

def first_wilson(n:int)->F:
    # Rewrite as terminal source plus corrected next term, separate from curvature sum.
    total=sum((F(16,16**j)*source_oracle(j) for j in range(1,n+1)),F())
    return total+F(16,15*16**n)*source_oracle(n+1)

def tangent_double_homogeneous(a:F,b:F)->tuple[F,F]:
    # Homogeneous projective t=a/b: no affine denominator division.
    a,b=F(a),F(b)
    return 2*a*b,b*b-a*a

def angle_add_homogeneous(a:F,b:F,c:F,d:F)->tuple[F,F]:
    # t1=a/b, t2=c/d, sum corresponds to (ad+bc)/(bd-ac).
    return a*d+b*c,b*d-a*c

def radix16_homogeneous(a:F,b:F)->tuple[F,F]:
    for _ in range(4):a,b=tangent_double_homogeneous(a,b)
    return a,b

def radix16_pair_by_binomial(a:F,b:F)->tuple[F,F]:
    """Independent complex-binomial derivation of Cayley power map (v+iu)^16."""
    aa=bb=F(0)
    for j in range(17):
        term=F(comb(16,j))*b**(16-j)*a**j
        if j%2:aa+=(-1)**((j-1)//2)*term
        else:bb+=(-1)**(j//2)*term
    return aa,bb


def circle_cayley(a:F,b:F)->tuple[F,F]:
    """Exact real and imaginary coordinates of (b+ia)/(b-ia)."""
    a,b=F(a),F(b)
    if a==0 and b==0:raise ValueError('invalid projective point')
    d=a*a+b*b
    return (b*b-a*a)/d,2*a*b/d


def circle_product(c1:tuple[F,F],c2:tuple[F,F])->tuple[F,F]:
    return c1[0]*c2[0]-c1[1]*c2[1], c1[0]*c2[1]+c1[1]*c2[0]


def circle_power(x:tuple[F,F],n:int)->tuple[F,F]:
    out=(F(1),F(0))
    for _ in range(n):out=circle_product(out,x)
    return out


def free_heat_log_ratio(length_squared:F,t:F)->F:
    """-log K_t(length)/K_t(0) in the Euclidean free-line heat kernel."""
    t=F(t)
    if t<=0:raise ValueError('positive heat time required')
    return F(length_squared)/(4*t)


def normalized_heat_square_quotient(arc_length_squared:F,diameter_squared:F,t:F)->F:
    """The ratio of normalized heat actions is (L_arc/L_diam)^2, no π input."""
    return free_heat_log_ratio(arc_length_squared,t)/free_heat_log_ratio(diameter_squared,t)

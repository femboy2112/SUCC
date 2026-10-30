"""Exact declared Fibonacci probes; no numerical pi digits or source changes."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb


def fib(n):
    if n < 0:
        raise ValueError("nonnegative index")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    return 2 * fib(n + 1) - fib(n)


@dataclass(frozen=True)
class QL:
    """a+b*lambda, lambda^2=1-lambda."""
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    @staticmethod
    def of(x):
        return x if isinstance(x, QL) else QL(F(x))

    def __add__(self, x):
        x = self.of(x)
        return QL(self.a + x.a, self.b + x.b)

    __radd__ = __add__

    def __neg__(self):
        return QL(-self.a, -self.b)

    def __sub__(self, x):
        return self + -self.of(x)

    def __rsub__(self, x):
        return self.of(x) - self

    def __mul__(self, x):
        x = self.of(x)
        return QL(self.a*x.a+self.b*x.b,
                  self.a*x.b+self.b*x.a-self.b*x.b)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.of(x)
        norm = x.a*x.a-x.a*x.b-x.b*x.b
        if not norm:
            raise ZeroDivisionError
        return self * QL((x.a-x.b)/norm, -x.b/norm)

    def __pow__(self, n):
        if n < 0:
            return (QL(1)/self)**(-n)
        y, x = QL(1), self
        while n:
            if n & 1:
                y *= x
            x *= x
            n //= 2
        return y

    def __bool__(self):
        return bool(self.a or self.b)


LAM = QL(0, 1)


def solve(matrix, rhs):
    n = len(matrix)
    A = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if A[i][j])
        A[j], A[pivot] = A[pivot], A[j]
        q = A[j][j]
        A[j] = [x/q for x in A[j]]
        for i in range(n):
            if i != j:
                q = A[i][j]
                A[i] = [x-q*y for x,y in zip(A[i], A[j])]
    return [row[-1] for row in A]


def rational_null(matrix):
    A = [[F(x) for x in row] for row in matrix]
    rows, cols = len(A), len(A[0])
    pivots, r = [], 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        q = A[r][c]
        A[r] = [x/q for x in A[r]]
        for i in range(rows):
            if i != r:
                q = A[i][c]
                A[i] = [x-q*y for x,y in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    free = next(c for c in range(cols) if c not in pivots)
    v = [F(0)]*cols
    v[free] = F(1)
    for i,c in enumerate(pivots):
        v[c] = -A[i][free]
    return v, len(pivots)


def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0))


def triangle_fib_probe(j):
    return [QL(harmonic(j)), QL(fib(j)), QL(fib(j+1)), LAM**j]


def cycle_witness(m=6, d=5):
    basis = [(i,k) for i in range(m) for k in range(i+1,i+d)]
    constraint_rows = []
    for u in range(4):
        for v in range(4):
            row = [(triangle_fib_probe(i)[u]-triangle_fib_probe(i+1)[u]) *
                   (triangle_fib_probe(k)[v]-triangle_fib_probe(k+1)[v])
                   for i,k in basis]
            for component in ("a","b"):
                values = [getattr(x,component) for x in row]
                if any(values):
                    constraint_rows.append(values)
    coeff, rank = rational_null(constraint_rows)
    Z = {(i,k):F(0) for i in range(m+1) for k in range(i,i+d+1)}
    for c,(i,k) in zip(coeff,basis):
        for e,s in [((i,k),1),((i+1,k+1),1),((i,k+1),-1),((i+1,k),-1)]:
            Z[e] += s*c
    scale = max(abs(x) for x in Z.values())
    return {e:x/scale for e,x in Z.items()}, rank, len(basis)


def R(a):
    a = F(a)
    return 4/a-2/(a+3)-1/(a+4)-1/(a+5)


def beta_sensor(a, p_degree, t_degree):
    return sum(((-1)**j*comb(p_degree,j)*R(F(a)+8*(t_degree+j))
                for j in range(p_degree+1)), F(0))/R(a)


def native_joint(a,m,d):
    return {(i,k):comb(m,i)*comb(d,k-i)*beta_sensor(a,k,m+d-k)
            for i in range(m+1) for k in range(i,i+d+1)}


def paired_alias(a,m=6,d=5):
    J = native_joint(a,m,d)
    Z,rank,dim = cycle_witness(m,d)
    eps = beta_sensor(a,m+d,m+d)/2
    return J,{e:J[e]+eps*Z[e] for e in J},Z,eps,rank,dim


def moment(J, f, g):
    return sum((v*f(i)*g(j) for (i,j),v in J.items()),QL())


def fib_nodes(n):
    return [LAM**fib(i+2) for i in range(n)]


def tomography(J, rows, cols):
    qs,rs = fib_nodes(rows),fib_nodes(cols)
    C = [[q**j for j in range(rows)] for q in qs]
    D = [[r**j for j in range(cols)] for r in rs]
    M = [[sum((QL(J.get((i,j),0))*q**i*r**j
               for i in range(rows) for j in range(cols)),QL())
          for r in rs] for q in qs]
    left = [solve(C,[M[i][j] for i in range(rows)]) for j in range(cols)]
    out = [solve(D,[left[j][i] for j in range(cols)]) for i in range(rows)]
    return M,out


def projection_residual(L, last_index):
    """Projection onto t^(L+2), t^(L+F_n+2), 2<=n<=last_index."""
    if L < 0 or last_index < 2:
        raise ValueError
    exps = [L+2]+[L+fib(n)+2 for n in range(2,last_index+1)]
    q = L+6
    A = [[F(1,x+y+1) for y in exps] for x in exps]
    b = [F(1,x+q+1) for x in exps]
    c = solve(A,b)
    h = {q:F(1),**{x:-v for x,v in zip(exps,c)}}
    norm2 = poly_inner(h,h)
    product = F(1,2*q+1)
    for x in exps:
        product *= F(q-x,q+x+1)**2
    return h,norm2,product


def poly_inner(p,q):
    return sum((a*b*F(1,i+j+1) for i,a in p.items() for j,b in q.items()),F(0))


def twice_integrated(h,L):
    # x^L integral_x^1 (t-x) h(t) dt
    out = {}
    for k,c in h.items():
        for j,v in [(L,c/F(k+2)),(L+1,-c/F(k+1)),
                    (L+k+2,c/F((k+1)*(k+2)))]:
            out[j] = out.get(j,F(0))+v
    return {j:v for j,v in out.items() if v}


def poly_moment(p,k):
    return sum((v/F(j+k+1) for j,v in p.items()),F(0))


def infinite_norm_bracket(L,last_index=24):
    q=L+6
    exps=[L+2]+[L+fib(n)+2 for n in range(2,last_index+1)]
    upper=F(1,2*q+1)
    for x in exps:
        upper*=F(q-x,q+x+1)**2
    tail=(2*q+1)*2*(F(1,fib(last_index+1))+F(1,fib(last_index+2)))
    if tail>=1 or fib(last_index+1)<=4:
        raise ValueError("increase prefix for a positive tail certificate")
    return upper*(1-tail)**2,upper,tail


def zeckendorf(n):
    if n<0:
        raise ValueError
    chosen=[]
    while n:
        j=2
        while fib(j+1)<=n:
            j+=1
        chosen.append(j)
        n-=fib(j)
    return chosen

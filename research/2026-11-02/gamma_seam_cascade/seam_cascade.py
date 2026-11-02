"""Original BBP Gamma-seam gluing and universal signed Haar cascade.

Research-only: these exact identities DO NOT prove an asymptotic selected
signed loss or pi normality. Preserve original poles and literal U_0=0.
"""
from fractions import Fraction
from functools import lru_cache

POLES = ((4, 7), (-2, 4), (-1, 3), (-1, 2))


def r(n):
    if n < 1:
        raise ValueError('n must be positive')
    return sum((Fraction(c, 8*n-a) for c, a in POLES), Fraction())


def r_combined(n):
    if n < 1:
        raise ValueError('n must be positive')
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


@lru_cache(maxsize=4096)
def alpha_cut(b):
    if b < 0:
        raise ValueError('cutoff must be nonnegative')
    return sum((Fraction(1,16**j)*r(j) for j in range(1,b+1)), Fraction())


def future_seam(n,b):
    """R(n,b) = 16^n(alpha_b-alpha_n); exact, nonnegative rational."""
    if n < 0 or b < n:
        raise ValueError('0 <= n <= b')
    return sum((Fraction(1,16**(j-n))*r(j) for j in range(n+1,b+1)), Fraction())


def state_at(n):
    """Original BBP U_n, with literal U0=0."""
    if n < 0:
        raise ValueError('n >= 0')
    return 16**n*alpha_cut(n)


def seamed_state(n,b):
    """Endpoint-b chart reconstructs the exact U_n for ANY b>=n."""
    return 16**n*alpha_cut(b)-future_seam(n,b)


def verify_glue(n,m,b):
    if not 0 <= n <= m <= b:
        raise ValueError('0 <= n <= m <= b')
    F_nm = future_seam(n,m)
    F_mb = future_seam(m,b)
    F_nb = future_seam(n,b)
    assert F_nb == F_nm + Fraction(1,16**(m-n))*F_mb
    assert alpha_cut(b)-alpha_cut(m) == Fraction(1,16**m)*F_mb
    assert seamed_state(n,m) == seamed_state(n,b) == state_at(n)
    return True


def tail_upper(n):
    """T_n <= 1/[(8n+1)(8n+2)] via the original Beta kernel."""
    if n < 0:
        raise ValueError('n >= 0')
    return Fraction(1,(8*n+1)*(8*n+2))


def late_source_character_l1_bound_over_pi(h, a):
    """Coefficient c: total late U-vs-pi character error <= pi*c."""
    if a < 1:
        raise ValueError('a >= 1')
    return Fraction(abs(h), 32*a)


def left_cutoff_rephase_bound_over_pi(h, m):
    """Coefficient c: earlier-phase change extending cut m to m+L <= pi*c."""
    if m < 1:
        raise ValueError('m >= 1')
    return Fraction(32*abs(h),15)*tail_upper(m)


def paired_energies(z, L):
    """Exact Gaussian-rational aggregate child, wavelet, parent energies.

    z consists of complex-number pairs (Fraction real, Fraction imaginary).
    All relations are algebraic, independent of any Gamma hypothesis.
    """
    if L<1 or len(z)%(2*L):
        raise ValueError('2L must divide sequence length')
    def accum(xs):
        return (sum((v[0] for v in xs), Fraction()),
                sum((v[1] for v in xs), Fraction()))
    def norm2(v):
        return v[0]*v[0]+v[1]*v[1]
    E=W=P=Fraction()
    for a in range(0,len(z),2*L):
        x=accum(z[a:a+L]); y=accum(z[a+L:a+2*L])
        E+=norm2(x)+norm2(y)
        W+=norm2((x[0]-y[0],x[1]-y[1]))
        P+=norm2((x[0]+y[0],x[1]+y[1]))
    assert P == 2*E-W
    return E,W,P


def scale_energies(z):
    """List (L,E_L,W_L,P_L), plus root E_N (with W=None)."""
    N=len(z)
    if not N or (N&(N-1)):
        raise ValueError('length must be a power of two')
    result=[]
    L=1
    while 2*L<=N:
        E,W,P=paired_energies(z,L)
        result.append((L,E,W,P))
        L*=2
    result.append((N,result[-1][3] if len(result)>0 else
                   z[0][0]**2+z[0][1]**2,None,None))
    return result


def exact_energy_cascade(z):
    """Exact normalized energy cascade; C0=1 iff input phases are units."""
    N=len(z)
    levels=scale_energies(z)
    out=[]
    for L,E,W,P in levels[:-1]:
        C=E/Fraction(N*L)
        next_C=P/Fraction(N*2*L)
        assert C-next_C==W/Fraction(2*N*L)
        assert C>=next_C
        out.append((L,C,C-next_C,next_C))
    return out


def prefix_energy_ceiling(N,L,E):
    """C_L and L/N; for |z_n|<=1, max_prefix/N <=sqrt(C_L)+L/N."""
    if N<1 or L<1 or N%L:
        raise ValueError('L divides N')
    return Fraction(E,N*L),Fraction(L,N)


def source_gamma_seam_sum_moments(t):
    """Positive Hausdorff source integral of (1-u^8)^t; NOT phase mixing."""
    if t<0:
        raise ValueError('t >= 0')
    from math import comb
    P=(4,0,0,-2,-1,-1)
    return sum((Fraction((-1)**j * comb(t,j)*c,8*j+idx+1)
                for j in range(t+1) for idx,c in enumerate(P) if c),Fraction())

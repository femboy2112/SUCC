"""Source-faithful BBP antiphase window certificates, with NO normality claim.

The exact arithmetic retains all four signed original poles and U_0=0.
Euler/Gamma residual is NOT assigned as an actual angular increment.
"""
from fractions import Fraction
from math import gcd


def source(n):
    if n < 1: raise ValueError("n>=1 required")
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def odd_source(n):
    if n < 1: raise ValueError("n>=1 required")
    return (Fraction(4,8*n-7)-Fraction(1,8*n-3)
            -Fraction(3*n-1,(2*n-1)*(4*n-1)))


def states(last):
    if last<0: raise ValueError("last>=0")
    q=Fraction(0); out=[q]
    for n in range(1,last+1):
        q=16*q+source(n)
        out.append(q)
    return out


def centered(q):
    q=Fraction(q)
    a=q.numerator%q.denominator
    return Fraction(min(a,q.denominator-a),q.denominator)


def exact_time_antiphase_cost(U,start,L,h):
    """Mean exact circle distance of equal-lag time pairs from half-turn."""
    if start<0 or L<1 or h==0 or start+2*L>len(U):
        raise ValueError("invalid time pair horizon/h")
    return sum((centered(h*(U[n+L]-U[n])-Fraction(1,2))
                for n in range(start,start+L)), Fraction(0))/L


def exact_phase_bins(U,start,N,M):
    if start<0 or N<1 or M<2 or start+N>len(U):
        raise ValueError("invalid bin horizon")
    counts=[0]*M
    for n in range(start,start+N):
        q=U[n]
        a=q.numerator%q.denominator
        counts[(M*a)//q.denominator]+=1
    return counts


def antiphase_bin_pairs(M,h):
    """Nonoverlapping phase-bin matching with exactly opposite h-center phases.

    For h=2^v*g, g odd, shift=T=M/2^(v+1); in each T-residue
    cycle pair consecutive even and odd indices. M should be power of 2.
    """
    if h==0 or M<2 or M&(M-1):raise ValueError("h!=0, M power of two")
    h=abs(h);v=0
    while h%2==0:
        h//=2;v+=1
    if M<2**(v+1):raise ValueError("mesh cannot resolve this h")
    T=M//2**(v+1)
    return [(a+(2*j)*T,a+(2*j+1)*T)
            for a in range(T) for j in range(2**v)]


def antipodal_imbalance(counts,h):
    pairs=antiphase_bin_pairs(len(counts),h)
    N=sum(counts)
    if not N:raise ValueError("nonempty histogram required")
    return Fraction(sum(abs(counts[a]-counts[b]) for a,b in pairs),N)


def histogram_energy(counts):
    N=sum(counts)
    if not N:raise ValueError("nonempty histogram required")
    return Fraction(len(counts)*sum(v*v for v in counts),N*N)


def lag_forcing(U,n,L):
    """Exact unwrapped identity U_(n+L)-U_n=(16^L-1)U_n+F(n,L)."""
    if n<0 or L<1 or n+L>=len(U):raise ValueError("invalid lag")
    F=sum((16**(L-j)*source(n+j) for j in range(1,L+1)),Fraction(0))
    assert U[n+L]-U[n]==(16**L-1)*U[n]+F
    return F


def tail_upper(n):
    if n<1:raise ValueError("n>=1")
    return Fraction(1,(8*n+1)*(8*n+2))


def alpha_from_source(B):
    return sum((source(j)/16**j for j in range(1,B+1)),Fraction(0))


def finite_future(n,B):
    if n<0 or n>B:raise ValueError("0<=n<=B")
    return sum((source(j)/16**(j-n) for j in range(n+1,B+1)),Fraction(0))


def coarse_phase_sensitivity(counts,h):
    """Squared fluctuation controls h-specific antipodal occupancy imbalance."""
    a=antipodal_imbalance(counts,h)
    E=histogram_energy(counts)
    assert a*a<=E-1
    return a, E-1


def pseudo_stationarity_character_budget(N,h):
    """(2+2π|h| Σ_{j<=N}r(j))/N; return exact rational π-free factor.

    Uses |e(x)-e(y)|<=2π|x-y| and two end terms, giving
    |c_N(16h)-c_N(h)| <= [2+2π|h|sum_{j=1}^N r(j)]/N.
    """
    if N<1 or h==0:raise ValueError("N>=1,h!=0")
    return Fraction(2,N),Fraction(2*abs(h),N)*sum((source(j) for j in range(1,N+1)),Fraction(0))


def common_odd_modular_lift(last):
    """Independent all-original four-pole phase lift using combined odd factors.

    Returns odd D and residues a_0,...,a_last in [0,D) with {U_n}=a_n/D.
    The two even source poles are COMBINED EXACTLY before 2-local lifting;
    no approximation or replacement of the original forcing occurs.
    """
    if last<0:raise ValueError("last>=0 required")
    from math import lcm
    D=1
    for n in range(1,last+1):
        D=lcm(D,8*n-7,8*n-3,(2*n-1)*(4*n-1))
    assert D%2==1
    x=0; arr=[0]
    for n in range(1,last+1):
        inject=(4*(D//(8*n-7)) - (D//(8*n-3))
                -(3*n-1)*(D//((2*n-1)*(4*n-1))))
        x=(16*x+inject)%D
        arr.append(x)
    return D,arr


def modular_time_pair_cost(D,arr,start,L,h):
    """Return unREDUCED exact numerator/denominator for mean half-turn cost.

    Each term is |2*((h*(a_(n+L)-a_n)) mod D)-D|/(2D).
    Shared modulus removes thousands of costly Fraction gcd reductions.
    """
    if D<1 or D%2!=1 or start<0 or L<1 or h==0 or start+2*L>len(arr):
        raise ValueError("invalid modular pair inputs")
    S=0
    for n in range(start,start+L):
        z=(h*(arr[n+L]-arr[n]))%D
        S+=abs(2*z-D)
    return S,2*D*L


def modular_bins(D,arr,start,N,M):
    if D<1 or start<0 or N<1 or M<2 or start+N>len(arr):
        raise ValueError("invalid modular bins")
    out=[0]*M
    for a in arr[start:start+N]:
        out[M*a//D]+=1
    return out

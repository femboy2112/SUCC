"""Independent exact full-lift BBP mesoscopic collision instrument.

All arithmetic claims use integer common-denominator recurrence, NOT π digits.
Fejér calculations are floating diagnostics only, never proof certificates.
Four signed poles and literal U_0=0 are fixed.
"""
from fractions import Fraction
from math import cos, lcm, pi, sin


def common_denominator(last_n):
    """A nonminimal but exact denominator for every U_n with 0 <= n <= last_n."""
    if last_n < 0:
        raise ValueError('last_n must be nonnegative')
    den = 1
    for n in range(1, last_n + 1):
        for d in (8*n-7, 8*n-4, 8*n-3, 8*n-2):
            den = lcm(den, d)
    return den


def original_modular_lift(last_n):
    """Yield (n,a,D) with 0<=a<D and {U_n}=a/D exactly.

    Uses D=lcm of every original pole denominator through last_n,
    then U_n = 16 U_(n-1) + original_r(n) in Z/DZ, U_0=0.
    It does not replace the BBP source with a counterfeit CRT clock.
    """
    den = common_denominator(last_n)
    a = 0
    yield 0, a, den
    for n in range(1, last_n + 1):
        injection = (4*(den//(8*n-7)) - 2*(den//(8*n-4))
                     - den//(8*n-3) - den//(8*n-2))
        a = (16*a + injection) % den
        yield n, a, den



def online_modular_lift(last_n):
    """Independent online exact phase lift with changing denominator D_n.

    Unlike original_modular_lift, there is no future-horizon common denominator.
    At each step lift the previous numerator into lcm(D_(n-1), four poles).
    """
    if last_n < 0:
        raise ValueError('last_n must be nonnegative')
    a, den = 0, 1
    yield 0, a, den
    for n in range(1, last_n + 1):
        d0,d1,d2,d3 = 8*n-7,8*n-4,8*n-3,8*n-2
        next_den = lcm(den,d0,d1,d2,d3)
        injection = (4*(next_den//d0) - 2*(next_den//d1)
                     - next_den//d2 - next_den//d3)
        a = (16*a*(next_den//den)+injection) % next_den
        den=next_den
        yield n,a,den


def exact_near_pair_count(residues, modulus, mesh):
    """O(N log N) exact number of ORDERED near pairs on real circle.

    Counts (i,j), including diagonal and repeated phases, satisfying
       mesh*min(|a_i-a_j|, modulus-|a_i-a_j|) <= modulus.
    Avoids floating distances and a quadratic pair loop. Assumes 0<=a<D.
    """
    if mesh<2 or modulus<1 or not residues or any(not(0<=a<modulus) for a in residues):
        raise ValueError('invalid mesh, modulus, or residues')
    s=sorted(residues)
    N=len(s)
    linear=wrap=0
    j=1
    for i in range(N):
        if j<i+1:
            j=i+1
        while j<N and mesh*(s[j]-s[i])<=modulus:
            j+=1
        linear+=j-i-1
    j=1
    for i in range(N):
        if j<i+1:
            j=i+1
        while j<N and mesh*(modulus-(s[j]-s[i]))>modulus:
            j+=1
        wrap+=N-j
    # For mesh=2 the two semicircle tests overlap at antipodal pairs.
    overlap=0
    if mesh==2:
        from collections import Counter
        hist=Counter(s)
        if modulus%2==0:
            overlap=sum(c*hist.get(a+modulus//2,0) for a,c in hist.items()
                        if a+modulus//2<modulus)
    return N+2*(linear+wrap-overlap)

def source_epoch_counts(A, mesh):
    """Exact ORIGINAL zero-seed counts in mesh bins on [A,2A)."""
    if A < 2 or A & (A-1):
        raise ValueError('A must be a dyadic integer >=2')
    if mesh < 2:
        raise ValueError('mesh must be >=2')
    counts = [0]*mesh
    for n, a, den in original_modular_lift(2*A-1):
        if n >= A:
            counts[(mesh*a)//den] += 1
    assert sum(counts) == A
    return counts


def mesoscopic_mesh(dyadic_exponent, beta_num, beta_den):
    """m_(2^j)=2^floor(beta*j), beta=beta_num/beta_den in (0,1]."""
    if (dyadic_exponent < 1 or beta_num < 1 or beta_den < beta_num):
        raise ValueError('requires j>=1 and 0<beta<=1 rational')
    return max(2, 1 << ((dyadic_exponent*beta_num)//beta_den))


def source_profiles(max_exponent, beta_num=1, beta_den=2, min_exponent=3):
    """Single shared integer-lift pass, multiple exact dyadic mesh energies.

    Returns {A: (m, counts, E)} where E=m/A^2 sum_j counts_j^2.
    Memory is O(max(meshes)+size of a single common modulus), not Fraction history.
    """
    if max_exponent < min_exponent or min_exponent < 1:
        raise ValueError('invalid dyadic range')
    meshes = {1 << j: mesoscopic_mesh(j,beta_num,beta_den)
              for j in range(min_exponent,max_exponent+1)}
    counts = {A: [0]*m for A,m in meshes.items()}
    for n,a,den in original_modular_lift((1 << (max_exponent+1))-1):
        if n < (1 << min_exponent):
            continue
        A = 1 << (n.bit_length()-1)
        if A in meshes:
            counts[A][meshes[A]*a//den] += 1
    return {A: (meshes[A], counts[A], Fraction(meshes[A]*sum(t*t for t in counts[A]),A*A))
            for A in sorted(meshes)}


def normalized_collision(counts):
    """Exact m/N^2 sum cell_count^2 for arbitrary nonempty finite sample."""
    N = sum(counts)
    if N == 0 or len(counts) < 2:
        raise ValueError('nonempty sample; at least two bins')
    return Fraction(len(counts)*sum(v*v for v in counts), N*N)


def bin_rationals(points, mesh):
    """Exact bins for rational phases, with fractional part chosen in [0,1)."""
    if mesh < 2:
        raise ValueError('mesh must be >=2')
    ans = [0]*mesh
    for x in points:
        x = Fraction(x)
        ans[mesh*(x.numerator % x.denominator)//x.denominator] += 1
    return ans


def fejer_energy_float(points, mesh):
    """Q=1+(2/N^2)sum_{h=1}^{m/2-1}(1-2h/m)|S_h|^2.

    Noncertified double-precision oracle. Rational phases are reduced modulo 1
    before conversion to float; usable only for small/medium finite tests.
    """
    if mesh < 2 or mesh % 2:
        raise ValueError('mesh must be an even integer >=2')
    phases = []
    for x in points:
        x = Fraction(x)
        phases.append(float(Fraction(x.numerator % x.denominator, x.denominator)))
    if not phases:
        raise ValueError('nonempty sample required')
    N=len(phases)
    Q=1.0
    for h in range(1,mesh//2):
        re=sum(cos(2*pi*h*x) for x in phases)
        im=sum(sin(2*pi*h*x) for x in phases)
        Q += (2.0/(N*N))*(1.0-2.0*h/mesh)*(re*re+im*im)
    return Q


def gamma_excess_sqrt_bound(A):
    """Rigorous bound π/sqrt(12288*A), as float for diagnostics only."""
    if A < 2 or A & (A-1):
        raise ValueError('requires dyadic A>=2')
    return pi/(12288*A)**0.5


if __name__ == '__main__':
    for A, (mesh, counts, energy) in source_profiles(11, 1, 2, 8).items():
        print('A=%d mesh=%d exact_E=%s' % (A, mesh, energy))

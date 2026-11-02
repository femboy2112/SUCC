"""Exact BBP first-pole prime/cofactor and single-mesh collision probes.

Research only. Rational equalities, integer collisions, and source bounds are
exact; complex Fourier/Galois amplitude diagnostics are FLOAT and unproved
asymptotic. No pi digits or altered original BBP source are inputs.
"""
from fractions import Fraction
from math import cos, pi, sin, sqrt, isqrt


def bbp_r(n: int) -> Fraction:
    if n < 1:
        raise ValueError('source indices start at one')
    return (Fraction(4, 8*n-7)-Fraction(2, 8*n-4)
            -Fraction(1, 8*n-3)-Fraction(1, 8*n-2))


def original_states(max_n: int):
    if max_n < 0:
        raise ValueError('max_n must be nonnegative')
    states=[Fraction(0)]
    for n in range(1,max_n+1):
        states.append(16*states[-1]+bbp_r(n))
    return states


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2,isqrt(n)+1):
        if n%p==0:
            return False
    return True


def birth_window(p: int):
    """Returns b, last clean index, first secondary pole for p=8k+1."""
    if p <= 5 or p % 8 != 1 or not is_prime(p):
        raise ValueError('requires prime p>5, p=1 (mod 8)')
    k=(p-1)//8
    return k+1, 4*k, 4*k+1


def cofactor_decomposition(p: int, t: int, states=None):
    """U_(b+t) = 4*16**t/p + p-integral rational B_t.

    Valid exactly for 0 <= t < 3*k. B_t denominator is not divisible by p.
    """
    b, last, _=birth_window(p)
    if not (0 <= t <= last-b):
        raise ValueError('outside p-clean interval')
    if states is None:
        states=original_states(b+t)
    q=Fraction(4*16**t,p)
    co=states[b+t]-q
    if co.denominator % p == 0:
        raise AssertionError('source primality/passport unexpectedly failed')
    return q,co


def p_residue(x: Fraction, p: int):
    """Reduction of a p-integral rational mod p."""
    if x.denominator % p == 0:
        raise ValueError('nonintegral at p')
    return (x.numerator * pow(x.denominator,-1,p))%p


def centered_residue(a: int, q: int) -> int:
    """Absolute minimal residue of a modulo q, 0 <= distance <= q/2."""
    v=a%q
    return min(v,q-v)


def exact_phase_distance(q: Fraction) -> Fraction:
    """Nearest-integer real distance, exact for rational q."""
    return Fraction(centered_residue(q.numerator,q.denominator),q.denominator)


def prime_cofactor_pair_certificate(p: int, s: int, t: int, states=None):
    """Exact CRT/Archimedean integer data for a pair inside p-clean window.

    Returns {p, q, prime_numer, cofactor_numer, joint_numer,
             centered_joint, distance}. The denominator q is coprime to p,
    joint_numer=prime_numer*q+p*cofactor_numer, and the selected real
    distance is abs(joint_numer mod p*q)/(p*q); this is NOT averaged.
    """
    b,last,_=birth_window(p)
    if not (0 <= s < t <= last-b):
        raise ValueError('require 0 <= s < t < clean length')
    if states is None:
        states=original_states(b+t)
    _,bs=cofactor_decomposition(p,s,states)
    _,bt=cofactor_decomposition(p,t,states)
    difference=bt-bs
    c,q=difference.numerator,difference.denominator
    assert q%p!=0
    aprime=4*(16**t-16**s)
    joint=aprime*q+p*c
    den=p*q
    return dict(p=p,q=q,prime_numer=aprime,cofactor_numer=c,
                joint_numer=joint,centered_joint=centered_residue(joint,den),
                distance=Fraction(centered_residue(joint,den),den))


def alpha_cutoff(b: int) -> Fraction:
    if b < 0: raise ValueError('b must be nonnegative')
    total=Fraction(0)
    radix=1
    for n in range(1,b+1):
        radix*=16
        total+=bbp_r(n)/radix
    return total


def modular_orbit(q: Fraction,n: int):
    """Yields exact numerator a_n, common denominator D for {16**n q}."""
    if n<0: raise ValueError('negative n')
    den=q.denominator
    a=q.numerator%den
    for _ in range(n):
        yield a,den
        a=16*a%den


def exact_mesh_occupancy(q: Fraction,n: int,m: int):
    """Counts bins floor(m * {16**t q}) by integer arithmetic only."""
    if n<=0 or m<=1: raise ValueError('require n>=1, m>=2')
    counts=[0]*m
    for a,den in modular_orbit(q,n):
        counts[m*a//den]+=1
    assert sum(counts)==n
    return counts


def mesh_collision_energy(counts: list[int]):
    """Integer-rational M/N**2 sum_j count_j**2."""
    n=sum(counts)
    if n<=0:raise ValueError('empty counts')
    return Fraction(len(counts)*sum(v*v for v in counts),n*n)


def exact_near_pair_count(q: Fraction,n: int,m: int) -> int:
    """#ordered pairs whose real-circle separation <= 1/m, exact."""
    residues=[a for a,_ in modular_orbit(q,n)]
    den=q.denominator
    count=0
    for a in residues:
        for b in residues:
            v=abs(a-b)
            if m*min(v,den-v) <= den:
                count+=1
    return count


def fejer_energy_numeric(q: Fraction,n: int,h: int):
    """Finite float diagnostic; NOT an interval or asymptotic certificate."""
    arr=[a for a,d in modular_orbit(q,n)]
    den=q.denominator
    e=1.0
    for m in range(1,h+1):
        phases=[2*pi*float(Fraction((m*a)%den,den)) for a in arr]
        c=sum(complex(cos(t),sin(t)) for t in phases)/n
        e+=2*(1-m/(h+1))*abs(c)**2
    return e


def fejer_mesh_majorant_constant() -> float:
    """Universal kernel/bin inequality constant 3 + pi**2/12."""
    return 3+pi*pi/12


def e_rational(q: Fraction):
    """Float realization of exact rational phase, for diagnostics only."""
    a=q.numerator%q.denominator
    v=2*pi*float(Fraction(a,q.denominator))
    return complex(cos(v),sin(v))


def order_of_16(p: int):
    """Exact order of 16 in F_p*."""
    if p<3 or p%2==0 or not is_prime(p):
        raise ValueError('p must be odd prime')
    z=16%p
    d=1
    while z!=1:
        z=(z*16)%p
        d+=1
    return d


def galois_energy_pair(p:int,t:int,h:int=1,states=None):
    """Returns (selected |S|², Galois-mean |S|²), float diagnostic.

    Both sums follow exact cyclotomic character identities, but w_t is
    evaluated floating; the test separately verifies against explicit
    automorphism enumeration. The source/cofactor decomposition is EXACT.
    """
    b,last,_=birth_window(p)
    if not (1<=t<=last-b+1 and h%p!=0):
        raise ValueError('t outside clean window or p divides h')
    if states is None:states=original_states(b+t-1)
    groups={}
    w=[];selected=0j
    for i in range(t):
        a=4*pow(16,i,p)%p
        _,co=cofactor_decomposition(p,i,states)
        z=e_rational(h*co)
        groups[a]=groups.get(a,0j)+z
        w.append(z)
        selected+=e_rational(Fraction(h*a,p))*z
    mean=(p*sum(abs(z)**2 for z in groups.values())-abs(sum(w))**2)/(p-1)
    return abs(selected)**2,mean


def galois_direct_mean(p:int,t:int,h:int=1,states=None):
    """Independent explicit Galois mean over nonzero u (float)."""
    b,last,_=birth_window(p)
    if not (1<=t<=last-b+1 and h%p!=0):
        raise ValueError('t outside clean window or p divides h')
    if states is None:states=original_states(b+t-1)
    co=[cofactor_decomposition(p,i,states)[1] for i in range(t)]
    ans=0.0
    for u in range(1,p):
        z=sum(e_rational(Fraction(4*h*u*pow(16,i,p),p)+h*co[i])
              for i in range(t))
        ans+=abs(z)**2
    return ans/(p-1)


def fake_cofactor(p:int,t:int,H:int,Q:int):
    """Hostile p-free cofactor that makes SELECTED phase arbitrarily coherent.

    NOT the original BBP forcing. Requires Q coprime p and Q>0.
    Returns exact rational cofactor vector b_t whose phases satisfy
    ||4*16**t/p+b_t|| <= 1/(2Q), for every t. Thus finite Fejer
    energy >= 1+H*(1-pi*H/Q)**2 for Q>pi*H.
    """
    birth_window(p)
    if t<1 or H<1 or Q<1 or Q%p==0:
        raise ValueError('invalid counterfeit dimensions')
    out=[]
    for i in range(t):
        a=(4*pow(16,i,p))%p
        rounded=(2*Q*a+p)//(2*p) # nearest int to Q*a/p
        b=Fraction(-rounded,Q)
        assert b.denominator%p!=0
        assert exact_phase_distance(Fraction(a,p)+b)<=Fraction(1,2*Q)
        out.append(b)
    return out


def gamma_tail_upper(n:int):
    """Inherited source-positive exact bound T_n <= 1/(8n+1)(8n+2)."""
    if n<1:raise ValueError('n>=1')
    return Fraction(1,(8*n+1)*(8*n+2))


def euler_defect_lower(n:int):
    """Classic lower H_n-log n-gamma > 1/(2n)-1/(12n**2)."""
    if n<1:raise ValueError('n>=1')
    return Fraction(6*n-1,12*n*n)


def exact_gamma_square_gap(n:int):
    """Positive rational witness lower(D_n²/16)-upper(T_n), n>=2."""
    if n<2:raise ValueError('proved simple positivity for n>=2')
    lower=euler_defect_lower(n)
    ans=lower*lower/16-gamma_tail_upper(n)
    assert ans>0
    return ans


def fib(k:int):
    if k<0:raise ValueError('k>=0')
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a


def eta_power_ring(k:int):
    """Integers a,b with eta**k=a+b*eta and eta²=1-eta."""
    if k<0:raise ValueError('k>=0')
    a,b=1,0
    for _ in range(k):a,b=b,a-b
    return a,b


def exact_golden_circle_return(k:int):
    """Pure integer equality F_k eta-F_(k-1)=(-1)^(k-1)eta**k."""
    if k<1:raise ValueError('k>=1')
    a,b=eta_power_ring(k)
    sign=(-1)**(k-1)
    return (sign*a,sign*b)==(-fib(k-1),fib(k))


def finite_harmonic_shell(k:int) -> float:
    """Finite shell H_(F[k+1])-H_(F[k])-log(F[k+1]/F[k]).

    Float diagnostic; no Euler gamma constant needed.
    """
    from math import log
    if k<2:raise ValueError('k>=2')
    a,b=fib(k),fib(k+1)
    return sum(1/j for j in range(a+1,b+1))-log(b/a)


if __name__=='__main__':
    for p in (17,41,73,89,97,113,137,193,233,241,257):
        b,last,reset=birth_window(p)
        S=original_states(reset)
        assert all(cofactor_decomposition(p,t,S)[1].denominator%p for t in range(last-b+1))
        t=min(last-b+1,1+(p-1)//8)
        selected,avg=galois_energy_pair(p,t,1,S)
        print('p=%d clean=[%d,%d] reentry=%d ord16=%d T=%d selected_normsq=%.6g Galois_mean_normsq=%.6g' %
              (p,b,last,reset,order_of_16(p),t,selected/t**2,avg/t**2))
    for L in (4,8,16,32):
        n=L*L;m=L+1;q=alpha_cutoff(n)
        counts=exact_mesh_occupancy(q,n,m)
        obs=mesh_collision_energy(counts)
        print('L=%d N=%d M=%d integer_collision=%s approx=%.10f' % (L,n,m,obs, float(obs)))

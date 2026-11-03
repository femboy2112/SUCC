"""SUCC research: exact projective circle reciprocity and original BBP mirror cocycle.

All source/state/finite mirror claims use Fraction; unit-circle trig checks are
floating diagnostics only. Never infer selected Weyl cancellation or normality.
"""
from fractions import Fraction
from math import comb, cos, pi, sin, sqrt


def r_original(n):
    if n < 1:
        raise ValueError('source n>=1 required')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def original_states(B):
    if B < 0:
        raise ValueError('B>=0 required')
    U = [Fraction(0)]
    for n in range(1, B+1):
        U.append(16*U[-1] + r_original(n))
    return U


def finite_future(B):
    """Return R_{n,B}=sum_{j=n+1}^B 16^(n-j) r(j), exactly, n=0..B."""
    if B < 0:
        raise ValueError('B>=0 required')
    R = [Fraction(0)]*(B+1)
    for n in range(B-1, -1, -1):
        R[n] = (r_original(n+1) + R[n+1])/16
    return R


def finite_completion(B):
    return finite_future(B)[0]


def mirror_axes(B):
    """Exact time-dependent source-intertwining phase-reflection offsets."""
    return [-2*x for x in finite_future(B)]


def mirror_cocycle_defect(axis_n, axis_next, forcing_next):
    return Fraction(axis_next)-16*Fraction(axis_n)-2*Fraction(forcing_next)


def signed_reflection_mirror(unwrapped_phase, axis):
    return Fraction(axis)-Fraction(unwrapped_phase)


def completed_mirror_shadow(B):
    """(original U, mirror U) with same genuine positive forcing and rational seed.

    Mirror starts at -2*alpha_B, *not* at literal zero. Its state at n is
    J_{n,B}(U_n)=-U_n-2R_{n,B}=U_n-2*16**n*alpha_B.
    """
    U = original_states(B)
    R = finite_future(B)
    alpha = R[0]
    shadow = [u-2*(16**n)*alpha for n,u in enumerate(U)]
    assert all(shadow[n] == -U[n]-2*R[n] for n in range(B+1))
    return U, shadow


def t16_polynomials(t):
    """P16, Q16: imag/real of (1+i*t)^16, exactly for rational t."""
    t=Fraction(t)
    P=sum(((-1)**((k-1)//2)*comb(16,k)*t**k
          for k in range(1,17,2)), Fraction(0))
    Q=sum(((-1)**(k//2)*comb(16,k)*t**k
          for k in range(0,17,2)), Fraction(0))
    return P,Q


def projective_radix16(t):
    """Radix map t(x)=tan(pi*(x-1/4)), None denotes projective infinity."""
    if t is None:
        return Fraction(-1)
    P,Q=t16_polynomials(t)
    if P+Q==0:
        return None
    return (P-Q)/(P+Q)


def projective_reciprocal(t):
    """The global involution 0<->infinity and t->1/t."""
    if t is None:
        return Fraction(0)
    t=Fraction(t)
    if t==0:
        return None
    return Fraction(1)/t


def projective_rotation(t, q):
    """Möbius rotation by phase u with q=tan(pi*u), projective rational chart.

    q may be Fraction for algebraic unit tests; authentic BBP r(n) produces
    tan(pi*r(n)) algebraically, and the exact circle recurrence is tested
    separately in additive rational phases.
    """
    if q is None:
        if t is None:
            return Fraction(0)
        return -1/Fraction(t) if t else None
    if t is None:
        return Fraction(-1)/Fraction(q) if q else None
    t,q=Fraction(t),Fraction(q)
    if 1-t*q==0:
        return None
    return (t+q)/(1-t*q)


def circle_e(q):
    """Floating diagnostic phase e(q), using exact rational reduction first."""
    q=Fraction(q)
    x=Fraction(q.numerator % q.denominator, q.denominator)
    a=2*pi*float(x)
    return complex(cos(a),sin(a))


def source_reflection_commutator(n, axis=Fraction(0)):
    """J_a after F_n minus F_n after J_a, in additive circle coordinates."""
    if n < 0:
        raise ValueError('n>=0 required')
    return -15*Fraction(axis)-2*r_original(n+1)


def centered(q):
    q=Fraction(q)
    a=q.numerator%q.denominator
    return Fraction(min(a,q.denominator-a),q.denominator)


def source_residues():
    """Simple poles of r(z) dz (no pole at infinity)."""
    return {Fraction(7,8):Fraction(1,2),
            Fraction(1,2):Fraction(-1,4),
            Fraction(3,8):Fraction(-1,8),
            Fraction(1,4):Fraction(-1,8)}


def fix_two_pole_coordinate(x):
    x=Fraction(x)
    return (x-Fraction(7,8))/(x-Fraction(1,2))


def gamma_tail_upper(n):
    if n<1:
        raise ValueError('n>=1 required')
    return Fraction(1,(8*n+1)*(8*n+2))


def mirror_cutoff_sum_bound_coefficient(B):
    """Factor multiplying pi*|h| for total B+1 phase difference, exact.

    Bound < (64*pi*|h|/15) T_B and T_B<=gamma_tail_upper(B).
    """
    if B<1:
        raise ValueError('B>=1 required')
    return Fraction(64,15)*gamma_tail_upper(B)


def fixed_axis_commutes_radix(a):
    """J_a(x)=a-x commutes with 16x iff 15*a is integer."""
    return (15*Fraction(a)).denominator==1


def golden_axis():
    return (sqrt(5)-1)/2


def mirror_discrepancies(c, h, axis=0.0):
    """(Delta0,Delta_axis): phase-reflection discrepancies for one Fourier coefficient."""
    if not h:
        raise ValueError('nonzero harmonic required')
    phase=complex(cos(2*pi*h*axis),sin(2*pi*h*axis))
    return c-c.conjugate(), c-phase*c.conjugate()


def golden_condition_number_bound(h):
    """Elementary norm proof yields 1/|1-e(h*eta)| <= 3|h|/4."""
    if not h:
        raise ValueError('nonzero harmonic required')
    return Fraction(3*abs(h),4)


def fib(k):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a


def finite_golden_axis(k):
    if k<2:
        raise ValueError('k>=2 required')
    return Fraction(fib(k-1),fib(k))


if __name__=='__main__':
    for B in (8,64,256):
        U, mirror=completed_mirror_shadow(B)
        a=mirror_axes(B)
        assert all(mirror_cocycle_defect(a[n],a[n+1],r_original(n+1))==0
                   for n in range(B))
        print('B=',B,'mirror_seed=',mirror[0], 'tail_bound=',gamma_tail_upper(B),
              'cutoff_error_coefficient=',mirror_cutoff_sum_bound_coefficient(B))

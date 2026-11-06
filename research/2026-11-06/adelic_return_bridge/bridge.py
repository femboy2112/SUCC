"""Independent finite probes for cross-place BBP observations.

Mathematical all-horizon proofs are in THEOREMS.md. Python tests are finite only.
Genuine source r(n) and literal U_0=0; exact Fraction modular and circle arithmetic.
"""
from __future__ import annotations
from fractions import Fraction
from math import cos, sin, pi, sqrt
from hashlib import sha256


def source_z(n: int) -> Fraction:
    """Original rational BBP source at any integer clock, including Z2 past."""
    if type(n) is not int:
        raise TypeError('integer clock required')
    return Fraction(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def original_source(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('original source defined at positive integer times')
    return source_z(n)


def independent_four_pole(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('n>=1')
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def mod2_fraction(q: Fraction, k: int) -> int:
    if type(k) is not int or k<1: raise ValueError('k positive')
    q=Fraction(q)
    if q.denominator%2==0: raise ValueError('2-adic denominator not unit')
    mod=1<<k
    return q.numerator*pow(q.denominator,-1,mod)%mod


def raw_phases(count: int) -> tuple[list[Fraction],list[int]]:
    if type(count) is not int or count<1: raise ValueError('count positive')
    x=Fraction(0)
    states=[x]
    carries=[0]
    carry=0
    for n in range(1,count):
        unwrapped_step=16*x+original_source(n)
        next_carry=unwrapped_step.numerator//unwrapped_step.denominator
        x=unwrapped_step%1
        carry=16*carry+next_carry
        states.append(x)
        carries.append(carry)
    return states,carries


def carry_increments(phases: list[Fraction]) -> list[int]:
    """Recover one-step true integer carries by exact positive-time source."""
    increments = [0]
    for n in range(1,len(phases)):
        t=16*phases[n-1]+original_source(n)
        increments.append(t.numerator//t.denominator)
    return increments


def carry_mod_recent(increments: list[int], n: int, k: int) -> int:
    """C_n modulo 2^k from only last ceil(k/4) signed integer carries."""
    if n<0 or n>=len(increments) or k<1: raise ValueError('bounds')
    terms=min(n,(k+3)//4)
    return sum((16**j)*increments[n-j] for j in range(terms)) % (1<<k)


def v_padic_mod(n: int, k: int) -> int:
    """Independent past-directed source completion, truncated exactly mod 2^k."""
    if k<1: raise ValueError('k positive')
    m=1<<k
    s=0
    for j in range((k+3)//4):
        s=(s+(16**j)*mod2_fraction(source_z(n-j),k))%m
    return s


def real_phase_from_2adic_carry(n: int, k: int, x: Fraction,
                                 carry: int) -> Fraction:
    """Exactly reconstruct x once 2^k covers known odd denominator of x."""
    v=v_padic_mod(n,k)
    c=carry%(1<<k)
    return reconstruct_frac((v-c)%(1<<k),x.denominator,k)


def d_circle(x: Fraction, y: Fraction) -> Fraction:
    d=(x-y)%1
    return min(d,1-d)


def exact_return_witness(states: list[Fraction], carries: list[int], k: int, low: int=128, high: int=191,
                         threshold: Fraction=Fraction(1,4)) -> dict:
    q=1<<k
    if high+q>=len(states): raise ValueError('insufficient history')
    for n in range(low,high+1):
        gap=d_circle(states[n+q],states[n])
        if gap>=threshold:
            mod=1<<k
            rv=(mod2_fraction(states[n],k)+carries[n])%mod
            rm=(mod2_fraction(states[n+q],k)+carries[n+q])%mod
            # Hash the exact large rational numerator/denominator in a stable binary format.
            def binary(x):
                return x.to_bytes((x.bit_length()+7)//8 or 1,'big')
            digest=sha256(binary(gap.numerator)+b'/'+binary(gap.denominator)).hexdigest()
            return {'k':k,'lag':q,'n':n,'exact_ge_quarter':gap>=Fraction(1,4),
                    'exact_rational_sha256_bigendian':digest,
                    'numerator_bits':gap.numerator.bit_length(),
                    'denominator_bits':gap.denominator.bit_length(),
                    'distance_decimal':round(float(gap),12),
                    'modulus':mod,'unwrapped_left_residue':rv,'unwrapped_right_residue':rm,
                    'unwrapped_residues_equal':rv==rm,
                    'fractional_left_residue':mod2_fraction(states[n],k),
                    'fractional_right_residue':mod2_fraction(states[n+q],k)}
    return {'k':k,'lag':q,'n':None,'found':False}


def reconstruct_frac(v: int, d: int, k: int) -> Fraction:
    """Exact numerator recovery when x=a/d in [0,1), d known odd, 2**k>=d."""
    if type(d) is not int or d<1 or d%2==0: raise ValueError('odd positive denominator')
    if type(k) is not int or k<1 or 1<<k<d: raise ValueError('precision insufficient')
    mod=1<<k
    a=d*v%mod
    if a>=d: raise ValueError('inconsistent residue and bounded numerator')
    return Fraction(a,d)


def normalized_phase_diagnostics(states: list[Fraction], carries: list[int], k: int) -> dict:
    """FLOAT diagnostics. Exact mathematical claim: residues permute and surrogate sum=0."""
    N=1<<k
    if len(states)<N: raise ValueError('insufficient states')
    z=0j; surrogate=0j; error=0.; corr=0j
    rs=[]
    for n in range(N):
        x=states[n]
        residue=(mod2_fraction(x,k)+carries[n])%N
        rs.append(residue)
        phase=complex(cos(2*pi*float(x)),sin(2*pi*float(x)))
        ref=complex(cos(2*pi*residue/N),sin(2*pi*residue/N))
        z+=phase
        surrogate+=ref
        error+=abs(phase-ref)**2
        corr+=phase*ref.conjugate()
    if set(rs)!=set(range(N)): raise AssertionError('p-adic Haar period failed')
    return {'k':k,'N':N,'weyl_abs_float':round(abs(z/N),12),
            'surrogate_abs_float':round(abs(surrogate/N),12),
            'rms_phase_error_float':round(sqrt(error/N),12),
            'cross_correlation_abs_float':round(abs(corr/N),12),
            'surrogate_exact_mean_zero':True}


def shadow(n: int) -> Fraction:
    return Fraction(n,(2*n-1)**4)


def source_return_sum_mod(n: int, q: int, k: int) -> int:
    """S_q(n)=sum_(j=1)^q 16^(q-j)r(n+j) modulo 2^k, iteratively."""
    if n<0 or q<1 or k<1: raise ValueError('bounds')
    mod=1<<k; total=0
    for j in range(1,q+1):
        total=(16*total+mod2_fraction(source_z(n+j),k))%mod
    return total


def return_fiber_energy_float(phases: list[Fraction], k: int, M: int,
                              h: int=1) -> dict:
    """FLOAT ONLY: p-adic-return conditional Fourier L2 energy, not proof of decay."""
    q=1<<k
    if len(phases)<q*M or M<1: raise ValueError('insufficient phases')
    means=[]
    for a in range(q):
        s=sum(complex(cos(2*pi*h*float(phases[a+j*q])),
                      sin(2*pi*h*float(phases[a+j*q]))) for j in range(M))/M
        means.append(s)
    return {'k':k,'q':q,'M':M,'h':h,
            'return_energy_float':round(sum(abs(z)**2 for z in means)/q,12),
            'signed_weyl_squared_float':round(abs(sum(means)/q)**2,12),
            'diagonal_contribution_float':round(1/M,12)}

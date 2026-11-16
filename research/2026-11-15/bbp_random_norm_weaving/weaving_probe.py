"""Original four-pole BBP: randomized norm weaving, shared-threshold defects.

All arithmetic inputs for source/integral comparisons are exact (Fraction).
Floating circle phases are *only* finite smoke checks, never normality proof.
The source datum is unchanged: U_0=0, r(n) four original poles.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import cos, pi, sin, sqrt


def forcing(n: int) -> Fraction:
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def weight_polynomial(t):
    return 4-2*t**3-t**4-t**5


def factorized_weight(t):
    return (1-t)*(2+t*t)*(2+2*t+t*t)


def original_kernel(t):
    return 1/(16-t**8)


def chiral_kernel(t):
    return (16+t**8)/(256+t**16)


def defect_kernel(t):
    return 2*t**16/((16-t**8)*(256+t**16))


def chiral_sign(n: int) -> int:
    if n < 0 or type(n) is not int:
        raise ValueError('n must be nonnegative integer')
    return 1 if (n//2)%2==0 else -1


def chiral_source_partial(terms: int) -> Fraction:
    return sum((Fraction(chiral_sign(n), 16**(n+1)) * forcing(n+1)
                for n in range(terms)), Fraction())


def bbp_source_partial(terms: int) -> Fraction:
    return sum((Fraction(1, 16**n) * forcing(n)
                for n in range(1,terms+1)), Fraction())


def disk_weave(u1: float,u2: float) -> tuple[float,float,float,int]:
    """One-to-one (almost everywhere) square-to-disk probability transport.

    Returns Cartesian Z real/imag, radius, branch I.  The normalized
    angular coordinate uses the discarded min/max ratio and argmax bit.
    """
    if not (0 <= u1 <= 1 and 0 <= u2 <= 1):
        raise ValueError('uniform coordinates must lie in [0,1]')
    m=max(u1,u2)
    if m == 0: return 0.,0.,0.,0
    bit=0 if u1 >= u2 else 1
    angle=pi*(min(u1,u2)/m+bit)
    return m*cos(angle),m*sin(angle),m,bit


def disk_unweave(x: float, y: float) -> tuple[float,float]:
    """Inverse square-to-disk map off zero and angle seam."""
    from math import atan2, hypot
    r=hypot(x,y)
    if r > 1+1e-12:
        raise ValueError('not in unit disk')
    if r == 0: return 0.,0.
    angle=atan2(y,x)
    if angle<0: angle+=2*pi
    bit=0 if angle<pi else 1
    v=angle/pi-bit
    return ((r,r*v) if bit==0 else (r*v,r))


def source_random_channels(t, uniforms):
    """Six auxiliary iid U(0,1) variables, grouped independently given t."""
    if not 0<=t<=1 or len(uniforms)!=6 or any(not 0<=u<=1 for u in uniforms):
        raise ValueError('required t in [0,1] and six uniforms in [0,1]')
    u0,u1,u2,v1,v2,v3=uniforms
    a=int(u0>t)
    b=2+int(max(u1,u2)<=t)
    c=2+2*int(v1<=t)+int(max(v2,v3)<=t)
    return a,b,c


def source_probabilities(t, uniforms):
    a,b,c=source_random_channels(t,uniforms)
    scale=a*b*c
    p0=scale*original_kernel(t)
    pchi=scale*chiral_kernel(t)
    assert 0<=pchi<=p0<=1, (t,p0,pchi)
    return p0,pchi


def shared_source_clicks(t, uniforms, w):
    """Nested Bernoulli coupling of pi/16 and positive chiral defect."""
    if not 0<=w<=1: raise ValueError('w must be uniform coordinate')
    p0,pchi=source_probabilities(t,uniforms)
    return int(w<=p0),int(w<=pchi)


def chiral_jet(n: int):
    return (7+4*chiral_sign(n)) % 16


def two_time_chiral_phases(n: int,z0: float,h: int=1):
    """The two authentic CH-05 phases, with z_(n+2)=16² z_n (mod1)."""
    omega_phase=2*pi/16
    a=complex(cos(omega_phase*chiral_jet(n)+2*pi*h*z0),
              sin(omega_phase*chiral_jet(n)+2*pi*h*z0))
    b=complex(cos(omega_phase*chiral_jet(n+2)+2*pi*h*256*z0),
              sin(omega_phase*chiral_jet(n+2)+2*pi*h*256*z0))
    return a,b


def two_path_probability(a: complex, b: complex, setting: float=0.):
    """Squared coherent norm; a,b must have modulus one."""
    if abs(abs(a)-1)>1e-10 or abs(abs(b)-1)>1e-10:
        raise ValueError('need unit complex phases')
    rotation=complex(cos(setting),sin(setting))
    return abs(b+rotation*a)**2/4


def two_probe_click(u1: float,u2: float,a: complex,b: complex,setting=0.):
    """Source phase amplitude threshold, AND of two independent uniforms."""
    p=two_path_probability(a,b,setting)
    return int(max(u1,u2)<=sqrt(p))


def shared_norm_product(u1: float,u2: float,a: complex,b: complex):
    """Use the *same* disk coordinate at both source times."""
    x,y,r,_=disk_weave(u1,u2)
    z=complex(x,y)
    return (z*b)*(z*a).conjugate()


def threshold_pair_shared(u1:float,u2:float,p:float,q:float):
    """Nested Bernoulli coupling across source times (p and q)."""
    if not 0<=p<=1 or not 0<=q<=1:
        raise ValueError('probabilities must lie in [0,1]')
    m=max(u1,u2)
    return int(m<=sqrt(p)),int(m<=sqrt(q))


def lifted_original_states(last_n: int) -> list[Fraction]:
    u=Fraction(0)
    out=[u]
    for n in range(1,last_n+1):
        u=16*u+forcing(n)
        out.append(u)
    return out


def mod_two_power(x: Fraction, modulus: int) -> int:
    if modulus < 1 or modulus&(modulus-1) or x.denominator%2==0:
        raise ValueError('modulus power of 2; denominator odd')
    return (x.numerator*pow(x.denominator,-1,modulus))%modulus


def original_jet_direct(states: list[Fraction],n: int,k: int) -> int:
    q=16**k
    return mod_two_power((states[n+q]-states[n])/q,16)


def expected_source_factor(t):
    """Analytical expectation of the three independent random groups."""
    return (1-t)*(2+t*t)*(2+2*t+t*t)


def threshold_q_probability(a: complex,b: complex,theta: float):
    return two_path_probability(a,b,theta)


def geometric_source_index(rng) -> int:
    """Source n>=1 with P(n)=15/16^n, via p=15/16 stopping."""
    n=1
    while rng.random()<1/16:
        n+=1
    return n


def stopped_source_click(rng, *, return_index=False):
    """A finite-a.s. Bernoulli program whose click probability is pi/16.

    No pi constant or digit fixture is present in this algorithm.  At epoch n,
    8(n-1) independent uniforms generate a max-norm threshold gate t^(8n-8).
    One common T couples the original four-pole factorization's three groups.
    An extra Bernoulli W<=ABC/15 completes the original series normalization.
    """
    n=geometric_source_index(rng)
    t=rng.random()
    abcs=source_random_channels(t,[rng.random() for _ in range(6)])
    volume_ok=all(rng.random()<=t for _ in range(8*(n-1)))
    click=int(volume_ok and rng.random()<=math_prod(abcs)/15)
    return (click,n) if return_index else click


def math_prod(values):
    result=1
    for v in values: result*=v
    return result


def chiral_gram(n:int,m:int)->Fraction:
    """Exact common-threshold two-time signed Gram, with no random sampling."""
    if n < 0 or m < 0:
        raise ValueError('source time nonnegative')
    return chiral_sign(n)*chiral_sign(m)*forcing(n+m+1)


def coherent_collision_energy(n:int,k:int)->Fraction:
    """E |sum_j binom(k,j) H_(n+2j)|² for H_n=χ_n T^(8n)sqrt(ABC).

    Exact rational source-only formula; strict positivity as a positive integral.
    """
    from math import comb
    if n<0 or k<0 or type(n) is not int or type(k) is not int:
        raise ValueError('n,k must be nonnegative integers')
    return sum(((-1)**j*comb(2*k,j)*forcing(2*n+2*j+1)
                for j in range(2*k+1)),Fraction())


def coherent_collision_limit(k:int)->Fraction:
    """lim_n n^(2k+2) E_k(n) = 15 Gamma(2k+2)/256."""
    from math import factorial
    if type(k) is not int or k<0:
        raise ValueError('k nonnegative integer')
    return Fraction(15*factorial(2*k+1),256)

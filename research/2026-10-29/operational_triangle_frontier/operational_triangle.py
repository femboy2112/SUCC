"""Source-authenticated operational triangle: exact finite rational reference instruments.

Research-only. Not a π digit sampler or proof of normality. Python >= 3.10.
All probabilities refer to one retained latent X drawn from the original BBP source.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))


def fraction(x):
    return Fraction(x)


@lru_cache(maxsize=None)
def R(a):
    a = Fraction(a)
    if a <= 0:
        raise ValueError('positive source parameter required')
    return sum((Fraction(c, 1) / (a + d) for d, c in POLES), Fraction())


def r(n):
    if n < 1:
        raise ValueError('native BBP clock starts at 1')
    return R(8*n-7)


def latent_joint_weight(a, m, j, t=0):
    """E[e^(-t*a*X) 1_{J=j}] at original mu_a, with J|X~Bin(m,1-e^-8X).

    t>=0 and a,z rational give exact rational outputs.
    """
    if m < 0 or Fraction(a) <= 0 or Fraction(t) < 0:
        raise ValueError('need m>=0, a>0, t>=0')
    if j < 0 or j > m:
        return Fraction()
    b = Fraction(a) * (1 + Fraction(t))
    return comb(m, j) * sum(
        ((-1)**k * comb(j, k) * R(b + 8*(m-j+k)) for k in range(j+1)),
        Fraction(),
    ) / R(Fraction(a))


def endpoint_mass(a, m, j):
    return latent_joint_weight(a, m, j)


def joint_path(a, m, z, t=0):
    """Superposition over endpoint states of the explicit history sum."""
    z = Fraction(z)
    return sum((z**j * latent_joint_weight(a, m, j, t)
                for j in range(m+1)), Fraction())


def joint_source(a, m, z, t=0):
    """Second, source-side route to same Laplace/grade generating polynomial."""
    if m < 0 or Fraction(t) < 0 or Fraction(a) <= 0:
        raise ValueError('invalid parameters')
    z = Fraction(z)
    b = Fraction(a) * (1+Fraction(t))
    return sum((comb(m, k) * z**(m-k) * (1-z)**k * R(b+8*k)
                for k in range(m+1)), Fraction()) / R(Fraction(a))


def posterior_laplace(a, m, j, t):
    mass = endpoint_mass(a, m, j)
    if mass <= 0:
        raise ValueError('invalid or empty posterior')
    return latent_joint_weight(a, m, j, t)/mass


def posterior_prediction(a, m, j):
    """Retained-field probabilities of next (failure, success) given grade j."""
    if not 0 <= j <= m:
        raise ValueError('grade out of range')
    p = endpoint_mass(a, m, j)
    # Divide out combinatorial factors: a selected word has probability p/C(m,j).
    w = p / comb(m, j)
    fail = endpoint_mass(a, m+1, j) / comb(m+1, j) / w
    success = endpoint_mass(a, m+1, j+1) / comb(m+1, j+1) / w
    return fail, success


def source_superposition(a, m):
    return tuple(endpoint_mass(a, m, j) for j in range(m+1))


def harmonic(j):
    if j < 0:
        raise ValueError('nonnegative grade required')
    return sum((Fraction(1, k) for k in range(1, j+1)), Fraction())


def harmonic_path(a, m):
    return sum((endpoint_mass(a, m, j)*harmonic(j)
                for j in range(m+1)), Fraction())


def harmonic_source(a, m):
    return harmonic(m) - sum((R(Fraction(a)+8*k)/k for k in range(1, m+1)), Fraction())/R(Fraction(a))


def gamma_difference(a, m):
    """Digamma difference written as finite rational sums (no gamma numerical input)."""
    a = Fraction(a)
    return sum((Fraction(c, 1)/(a+d) *
                sum((Fraction(8,1)/(a+d+8*k) for k in range(1,m+1)),Fraction())
                for d,c in POLES), Fraction()) / R(a)


def joint_first_jet(z, t):
    """Proved O(1/n) joint Gamma--Poisson coefficient for authentic BBP clock."""
    z, t = Fraction(z), Fraction(t)
    d=2+t-z
    if d <= 0:
        raise ValueError('d must be positive')
    return (59*t*t+92*t*z-33*t-511*z*z+813*z-302) / (120*d**4)


def joint_fake_first_jet(z, t):
    """Positive Gamma-matched fake Q_fake(x)=15*x, same native clock."""
    z,t=Fraction(z),Fraction(t)
    d=2+t-z
    b=z-1
    return Fraction(7,4)*b/d**3-3*b*(1+b)/d**4


def joint_source_defect(z,t):
    """Authentic minus fake first correction, source-specific 59-jet."""
    z,t=Fraction(z),Fraction(t)
    d=2+t-z
    return Fraction(59,120)*(1+t-z)/d**3


def bbp_state(n, seed=Fraction()):
    if n<0:
        raise ValueError('n must be nonnegative')
    x=Fraction(seed)
    for k in range(1,n+1):
        x=16*x+r(k)
    return x


def frac(x):
    x=Fraction(x)
    return x-x.numerator//x.denominator


def carry(n, seed=Fraction()):
    if n<1:
        raise ValueError('carry only for n>=1')
    b=16*frac(bbp_state(n-1,seed))+r(n)-frac(bbp_state(n,seed))
    if b.denominator!=1:
        raise AssertionError('noninteger carry')
    return int(b)


def phase_frequency_terms(n, h, seed=Fraction(), depth=None):
    """Formal auxiliary-seed Fourier series indexed by integers h*16**j.

    Each (frequency, mass, fractional-turn, literal-carry) encodes the exact
    coefficient mass*exp(2πi*turn), without using floating complex exponentials.
    Seed perturbation is u/16**n and its character frequency is h*16**j.
    """
    if n<1 or h==0:
        raise ValueError('n>=1 and nonzero integer h required')
    if depth is None:
        depth=n
    if depth<0:
        raise ValueError('depth must be nonnegative')
    a=8*n-7
    return tuple((h*16**j,endpoint_mass(a,depth,j),frac(h*bbp_state(n+j,seed)),carry(n+j,seed))
                 for j in range(depth+1))


def fourier_coefficient(terms, frequency):
    """Exact orthogonality on [0,1] of integer characters e(k*u)."""
    matched=[(q,phase) for k,q,phase,_ in terms if k==frequency]
    return tuple(matched)


def endpoint_prediction_variance(a):
    """Exact >0 variance of posterior prediction E[e^-8X | J_1]."""
    z=R(Fraction(a)+8)/R(a)
    row=source_superposition(a,1)
    return sum((row[j]*(posterior_prediction(a,1,j)[0]-z)**2 for j in range(2)),Fraction())


def shared_vs_reset(a):
    """Covariance of two failure indicators using same latent X."""
    a=Fraction(a)
    z=R(a+8)/R(a)
    return R(a+16)/R(a)-z*z

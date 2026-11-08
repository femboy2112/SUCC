"""Exact three positive channels of the authentic four-pole BBP source.

All positive source observables here are seed-blind. No pi-normality claim.
"""
from fractions import Fraction
from math import cos, sin

SHIFTS = (3, 4, 5)
WEIGHTS = (2, 1, 1)


def component(a, d):
    a = Fraction(a)
    return Fraction(1) / a - Fraction(1) / (a + d)


def source(a):
    return sum((w * component(a, d) for w, d in zip(WEIGHTS, SHIFTS)), Fraction(0))


def source_four_poles(a):
    a = Fraction(a)
    return 4 / a - 2 / (a + 3) - 1 / (a + 4) - 1 / (a + 5)


def raw_gram(a):
    """Rational Gram of 1-exp(-d*x), weighted by exp(-a*x)dx."""
    a = Fraction(a)
    return tuple(tuple(1/a - 1/(a+di) - 1/(a+dj) + 1/(a+di+dj)
                       for dj in SHIFTS) for di in SHIFTS)


def determinant_3(m):
    a,b,c=m[0]; d,e,f=m[1]; g,h,i=m[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def principal_minors(a):
    m = raw_gram(a)
    return (m[0][0], m[0][0]*m[1][1]-m[0][1]**2, determinant_3(m))


def channel_weights(a):
    r = source(a)
    return tuple(w*component(a,d)/r for w,d in zip(WEIGHTS, SHIFTS))


def response(z):
    return 1/(2-z)**2


def response_magnitude(theta):
    return 1/(5-4*cos(theta))


def channel_character(a, theta, marks):
    """Marked positive-source response, NOT the selected BBP phase."""
    weights=channel_weights(a)
    return sum(float(w)*complex(cos(theta*mark), sin(theta*mark))
               for w,mark in zip(weights,marks))


def signed_covariance(prime_phases, complementary_phases):
    """Actual joint phases must be supplied; source weights cannot infer them."""
    if len(prime_phases)!=len(complementary_phases) or not prime_phases:
        raise ValueError("equal nonempty histories required")
    n=len(prime_phases)
    p=sum(prime_phases)/n
    c=sum(complementary_phases)/n
    return sum(x*y for x,y in zip(prime_phases,complementary_phases))/n-p*c

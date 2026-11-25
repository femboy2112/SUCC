"""Independent symbolic matrix route for signed/paired source quotient weights."""
from fractions import Fraction
from random import Random
import sympy as sp
from observational_succ.principia_coupling_mass import (
    make_mass, compress_mass, verify_compressed_mass, evaluate_compression,
    gaussian_shell_coupling,
)

rng=Random(24011226)
count=0
for trial in range(180):
    n=1+rng.randrange(6)
    k=1+rng.randrange(4)
    source_classes=tuple(f'c{rng.randrange(k)}' for _ in range(n))
    weights=tuple(Fraction(rng.randrange(-5,6),rng.randrange(1,5)) for _ in range(n))
    kernel=tuple(tuple(Fraction(rng.randrange(-4,5),rng.randrange(1,4)) for j in range(n)) for i in range(n))
    m=make_mass(f'holdout-{trial}',tuple(f'p{i}' for i in range(n)),source_classes,weights,kernel)
    cert=verify_compressed_mass(m,compress_mass(m))
    labels=cert.classes
    incidence=sp.Matrix([[int(source_classes[i]==label) for label in labels] for i in range(n)])
    a=sp.Matrix([sp.Rational(v.numerator,v.denominator) for v in weights])
    K=sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in row] for row in kernel])
    ref_linear=incidence.T*a
    ref_kernel=incidence.T*K*incidence
    assert tuple(Fraction(ref_linear[i]) for i in range(len(labels)))==cert.linear
    assert tuple(tuple(Fraction(ref_kernel[i,j]) for j in range(len(labels))) for i in range(len(labels)))==cert.pairing
    f=tuple(Fraction(rng.randrange(-3,4),rng.randrange(1,5)) for _ in labels)
    g=tuple(Fraction(rng.randrange(-3,4),rng.randrange(1,5)) for _ in labels)
    direct=incidence*sp.Matrix([sp.Rational(v.numerator,v.denominator) for v in f])
    other=incidence*sp.Matrix([sp.Rational(v.numerator,v.denominator) for v in g])
    check=(direct.T*a)[0],(direct.T*K*other)[0]
    assert evaluate_compression(m,cert,f,g)==tuple(map(Fraction,check))
    count+=1

# One non-fitted genuine-Gaussian source check: independent sums of powers.
for n,order in [(2,2),(2,4),(3,2),(3,4)]:
    m=gaussian_shell_coupling(n,order)
    cert=compress_mass(m)
    assert sum(m.linear,Fraction(0))==sum(cert.linear,Fraction(0))
    assert sum((a for row in m.pairing for a in row),Fraction(0))==sum((a for row in cert.pairing for a in row),Fraction(0))
print('COUPLING_MASS_INDEPENDENT_SYMPY_PASS',count,'source systems, 4 actual CM shell checks')

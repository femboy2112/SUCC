"""Exact finite witnesses for conditional observational GR.

This is a source-model laboratory, not a physical GR derivation.  The
reference derivation and limits are in RESEARCH.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations

ZERO = Q(0)
ONE = Q(1)


def rational(x):
    if type(x) not in (int, Q):
        raise TypeError("Exact rational input required")
    return Q(x)


def conformal_factor(t, H=1):
    t, H = rational(t), rational(H)
    if 1-H*t <= 0:
        raise ValueError("Outside the oriented conformal patch")
    return 1/(1-H*t)


def metric_2d(t, H=1):
    o = conformal_factor(t,H)
    return ((-o*o, ZERO), (ZERO, o*o))


def scalar_curvature_2d(H=1):
    H=rational(H)
    return 2*H*H  # for Omega = (1-Ht)^-1, not a general conformal formula


def classical_scalar_action_density_2d(omega, phi_t, phi_x, kinetic=1):
    """-sqrt(-g)*kinetic*g^ab phi_a phi_b/2 for g=Omega^2*eta."""
    o,a,b,k = map(rational,(omega,phi_t,phi_x,kinetic))
    if o <= 0 or k <= 0: raise ValueError("positive scale/kinetic required")
    return -k*o*o*((-a*a+b*b)/(o*o))/2


def classical_scalar_coordinate_stress(omega, phi_t, phi_x, kinetic=1):
    """Covariant T_ab under g=Omega^2 eta; 2D conformal massless scalar."""
    o,a,b,k=map(rational,(omega,phi_t,phi_x,kinetic))
    if o <= 0 or k <= 0: raise ValueError("positive scale/kinetic required")
    q=k*(a*a+b*b)/2
    return ((q,k*a*b),(k*a*b,q))


def normalized_rest_energy(omega, phi_t, phi_x, kinetic=1):
    o=rational(omega)
    return classical_scalar_coordinate_stress(o,phi_t,phi_x,kinetic)[0][0]/(o*o)


def massless_coordinate_wave_residual(omega, dtt_phi, dxx_phi):
    o,a,b=map(rational,(omega,dtt_phi,dxx_phi))
    if o <= 0: raise ValueError("positive conformal factor required")
    return (-a+b)/(o*o)


def conformal_massless_scalar_density(d, omega, gradient_norm, kinetic=1):
    """In dimension d, -kinetic/2 * Omega^(d-2) * eta^ab phi_a phi_b."""
    o,norm,k=map(rational,(omega,gradient_norm,kinetic))
    if type(d) is not int or d < 2 or o <= 0 or k <= 0:
        raise ValueError("dimension >=2; positive scale, kinetic")
    return -k*o**(d-2)*norm/2


def null_directions_4d():
    """9 rational null directions, sufficient for the 9 tracefree components."""
    axes=[(ONE,ONE,ZERO,ZERO),(ONE,-ONE,ZERO,ZERO),
          (ONE,ZERO,ONE,ZERO),(ONE,ZERO,-ONE,ZERO),
          (ONE,ZERO,ZERO,ONE),(ONE,ZERO,ZERO,-ONE)]
    for i,j in combinations(range(1,4),2):
        v=[ZERO]*4
        v[0]=ONE
        v[i]=Q(3,5)
        v[j]=Q(4,5)
        axes.append(tuple(v))
    return tuple(axes)


def minkowski_norm(k):
    return -k[0]**2+sum(v*v for v in k[1:])


def symmetric_components(T):
    if len(T)!=4 or any(len(row)!=4 for row in T):
        raise ValueError("4x4 tensor required")
    if any(T[i][j]!=T[j][i] for i in range(4) for j in range(4)):
        raise ValueError("symmetric tensor required")
    return tuple(T[i][j] for i in range(4) for j in range(i,4))


def measurement_row(k):
    if len(k)!=4: raise ValueError("4-vector required")
    return tuple(k[i]*k[j]*(1 if i==j else 2)
                 for i in range(4) for j in range(i,4))


def null_measurements(T):
    coeffs=symmetric_components(T)
    return tuple(sum(a*b for a,b in zip(measurement_row(k),coeffs))
                 for k in null_directions_4d())


def rank_exact(matrix):
    if not matrix: return 0
    a=[list(map(rational,row)) for row in matrix]
    cols=len(a[0]);rank=0
    if any(len(row)!=cols for row in a):raise ValueError("rectangular matrix required")
    for j in range(cols):
        piv=next((i for i in range(rank,len(a)) if a[i][j]!=0),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        q=a[rank][j];a[rank]=[x/q for x in a[rank]]
        for i in range(len(a)):
            if i==rank:continue
            fac=a[i][j]
            if fac:
                a[i]=[x-fac*y for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank


def r2_metric_variation_constant_einstein(R):
    """Coefficient of g_ab for variation of sqrt(-g) R^2 on 4D Einstein space."""
    R=rational(R)
    return 2*R*(R/4)-R*R/2


def poisson_volume_intensity(dim, scale, rate):
    """Intensity measure lambda * sqrt(-g), for constant conformal scale."""
    if type(dim) is not int or dim < 2: raise ValueError("dimension required")
    o,rate=map(rational,(scale,rate))
    if o<=0 or rate<=0:raise ValueError("positive factors required")
    return rate*o**dim


def finite_bits_entropy_over_log2(n,uniform=True):
    """Shannon entropy in *bits*: uniform n free bits vs a fixed hidden configuration."""
    if type(n) is not int or n<0:raise ValueError("n nonnegative integer")
    return n if uniform else 0


def jacobson_coupling_from_area_entropy(alpha, hbar=1):
    """Returns G_eff=1/(4*hbar*alpha) in c=k_B=1, conditional on Jacobson axioms."""
    a,h=map(rational,(alpha,hbar))
    if a<=0 or h<=0:raise ValueError("positive calibrated entropy density and hbar required")
    return 1/(4*h*a)


def scalar_stress_4d(gradient, kinetic=1, potential=0):
    """Hilbert tensor for minimally coupled real scalar in Minkowski 3+1."""
    if len(gradient)!=4:raise ValueError("four covariant gradient components required")
    p=tuple(map(rational,gradient))
    z=rational(kinetic); v=rational(potential)
    if z<=0:raise ValueError("positive kinetic normalization required")
    norm=-p[0]**2+sum(a*a for a in p[1:])
    eta=(-ONE,ONE,ONE,ONE)
    return tuple(tuple(z*p[i]*p[j] - (eta[i] if i==j else ZERO)*(z*norm/2+v)
                       for j in range(4)) for i in range(4))


def normalized_thermo_matter_ratio(entropy_density, kinetic):
    """Z/alpha: field-equation source coupling, with shared absolute scale removed."""
    a,z=map(rational,(entropy_density,kinetic))
    if a<=0 or z<=0:raise ValueError("positive physical normalizations required")
    return z/a

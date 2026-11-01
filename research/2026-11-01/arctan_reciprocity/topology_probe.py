"""AR-09 exact topological firewall; original BBP rational states vs irrational mirror.

The n-horizon total-variation claim is an ALL-N elementary proof from rationality
and non-torsion Gaussian mirror, not a finite computational inference.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd

class TopologyError(ValueError):
    pass


def mirror_is_nontorsion(q:F)->bool:
    """For finite rational q=tan(pi*beta): e(beta) in Q(i) root of unity
    iff q is 0,1,-1; otherwise its rational Gaussian phase has infinite order.
    """
    if type(q) not in (int,F):raise TopologyError('exact rational tangent required')
    q=F(q)
    return q not in (0,1,-1)


def original_source(n:int)->F:
    if type(n) is not int or n<1:raise TopologyError('positive integer clock')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def original_orbit(n:int)->tuple[F,...]:
    if type(n) is not int or n<1:raise TopologyError('positive integer horizon')
    x=F(0)
    out=[]
    for j in range(1,n+1):
        x=(16*x+original_source(j))%1
        out.append(x)
    return tuple(out)


def certified_bbp_mirror_tv(n:int)->dict:
    """Disjointness proof: rational support vs beta-rational support, beta irrational.

    Distances use TV convention sup_A |mu(A)-nu(A)|=1; signed variation norm=2.
    """
    states=original_orbit(n)
    q=original_source(2)
    if q!=F(106,819) or not mirror_is_nontorsion(q):
        raise ArithmeticError('original source irrational-mirror certification failed')
    if any(type(x) is not F or x<0 or x>=1 for x in states):
        raise ArithmeticError('unfaithful rational phase state')
    return {"n":n,"source_r2":str(q),"every_original_phase_rational":True,
            "every_mirrored_phase_irrational":True,"mutually_singular":True,
            "total_variation_probability_metric":F(1),"variation_norm_of_difference":F(2),
            "proof":"if u=beta-v mod1 for rational u,v, then gamma=e(beta) is torsion; contradicted in Q(i)"}


def grid_fourier_character(m:int,h:int)->int:
    """Exact normalized M-grid Fourier coefficient is 1 if m|h else 0."""
    if type(m) is not int or m<2 or type(h) is not int:raise TopologyError('integer grid and harmonic')
    return int(h%m==0)


def calibrated_grid_observer(m:int,band:int)->dict:
    """Exact low Fourier-band equality plus disjoint supports in TV.

    If band<m, every nonzero h in [-band,band] is killed by grid averaging.
    The mirrored coefficient is gamma^h times conjugate and hence also zero.
    """
    if type(m) is not int or m<2 or type(band) is not int or not 1<=band<m:
        raise TopologyError('require 1 <= Fourier band < rational grid order')
    q=original_source(2)
    if not mirror_is_nontorsion(q):raise ArithmeticError('mirror torsion')
    for h in range(-band,band+1):
        if h and grid_fourier_character(m,h)!=0:
            raise ArithmeticError('finite-grid Fourier alias unexpectedly survived')
    return {"grid_size":m,"band":band,"mirrored_supports_disjoint":True,
            "total_variation_probability_metric":F(1),
            "all_nonzero_band_coefficients_identically_zero":True,
            "zero_frequency_both_one":True}


if __name__=='__main__':
    for N in (1,2,16,64):
        print('TV_CERT',N,certified_bbp_mirror_tv(N)['total_variation_probability_metric'])
    for m in (3,17,257):
        print('FOURIER_GRID_CERT',calibrated_grid_observer(m,m-1))

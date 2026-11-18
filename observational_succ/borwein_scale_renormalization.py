"""Exact Borwein block/scale-renormalization for original zero-seeded BBP.

All returned finite energies and source-tail bounds are rational.  The
asymptotic pi normality theorem remains open; no finite test proves decay.
"""
from fractions import Fraction as F
from .borwein_quantitative_certificate import (
    U, source_r, L, HAAR_MEAN, polynomial_quadrature, autocorrelation,
    FOURIER_FLOOR,
)

L_MAX = F(32, 289)
L_LIP = F(144, 289)
ATOMIC_FLOOR = FOURIER_FLOOR**2 / 16
GRID_UPPER = F(8, 3) * (F(11, 289))**2


def paired_original_blocks(start, length):
    """One authentic terminal rational U_{start+2*length}, both blocks."""
    if type(start) is not int or start < 0 or type(length) is not int or length < 1:
        raise ValueError('start>=0 and length>=1 are required')
    terminal_clock = start + 2*length
    endpoint = U(terminal_clock)
    shadows = tuple((endpoint/F(16**(terminal_clock-n)))%1
                    for n in range(start,terminal_clock))
    return shadows[:length], shadows[length:]


def block_variance(phases):
    return polynomial_quadrature(phases)


def pair_defect(left,right):
    """Exact nonnegative D=(1/4)||Phi_left-Phi_right||_L2^2."""
    if not left or not right or len(left)!=len(right):
        raise ValueError('equal positive lengths required')
    ea=block_variance(left)
    eb=block_variance(right)
    eu=block_variance(tuple(left)+tuple(right))
    return (ea+eb)/2-eu


def pair_defect_autocorrelation(left,right):
    """Independent source-rational double-sum implementation of D."""
    if not left or not right or len(left)!=len(right):
        raise ValueError('equal positive lengths required')
    n=len(left)
    kaa=sum((autocorrelation(a-b) for a in left for b in left),F(0))
    kbb=sum((autocorrelation(a-b) for a in right for b in right),F(0))
    kab=sum((autocorrelation(a-b) for a in left for b in right),F(0))
    return (kaa+kbb-2*kab)/F(4*n*n)


def original_pair_report(start,length):
    """(E_left,E_right,E_combined,D,epsilon_true_shadow) as exact Fractions."""
    left,right=paired_original_blocks(start,length)
    ea=block_variance(left)
    eb=block_variance(right)
    eu=block_variance(left+right)
    defect=(ea+eb)/2-eu
    if defect < 0:
        raise ArithmeticError('incorrect exact polynomial quadrature: negative defect')
    m=start+2*length
    eps=F(16,7225*length)*source_r(m+1)
    return ea,eb,eu,defect,eps


def step_coboundary_bound(length):
    """Universal L-infinity filtered T_*-invariance defect; not equidistribution."""
    if type(length) is not int or length<1:raise ValueError
    return F(2)*L_MAX/length


def phase_multiset_covers_dilated_mode(left,right,h):
    """Check Fourier dilation identity by exact integer-angle multiset.

    If right=T^N(left) on the circle, the right h-character values equal
    the left (16^N*h)-character values, including multiplicities.
    This is algebraic, not an analytic approximation.
    """
    from collections import Counter
    if not left or len(left)!=len(right) or type(h) is not int or h==0:
        raise ValueError
    n=len(left)
    return Counter((F(h)*v)%1 for v in right)==Counter((F(16**n*h)*v)%1 for v in left)


def atomic_floor_for_length(n):
    if type(n) is not int or n<1:raise ValueError
    return ATOMIC_FLOOR/n**4


def uniform_grid_upper_for_length(n):
    if type(n) is not int or n<1:raise ValueError
    return GRID_UPPER/n**4


def exact_uniform_grid(n):
    if type(n) is not int or n<1:raise ValueError
    return tuple(F(j,n) for j in range(n))


def scaled_residual_bound(old_length,new_length):
    """All-orbit prefix L2 feature distance <=2||L||inf*(N-M)/N.

    If N=M the bound is zero.  For any origin a, uses same trajectory.
    Not a source-specific decay theorem.
    """
    if type(old_length) is not int or type(new_length) is not int:
        raise ValueError
    if old_length<1 or new_length<old_length:raise ValueError
    return F(2)*L_MAX*F(new_length-old_length,new_length)


def original_prefix_phases(length):
    """Literal source zero, one rational endpoint U_length, clocks 0..length-1."""
    if type(length) is not int or length<1:raise ValueError
    terminal=U(length)
    return tuple((terminal/F(16**(length-n)))%1 for n in range(length))


def constant_single_atom_energy():
    """The source-independent ||L(theta-.)-Haar(L)||^2 for any theta."""
    return F(335872,304434045)


def wavelet_detail_budget(phases):
    """Exact weighted nonnegative binary-tree detail budget, any length.

    At a node I with children A,C, its contribution to the GLOBAL budget
    is (|I|/N)[(|A|/|I|)E_A+(|C|/|I|)E_C-E_I].
    Thus the sum is E_atom-E_whole for any rational phase list, without
    stochastic assumptions or a claim about pi normality.
    """
    pts=tuple(F(t)%1 for t in phases)
    length=len(pts)
    if not pts: raise ValueError('nonempty circle history required')
    def recurse(seq):
        n=len(seq)
        if n==1: return F(0)
        cut=n//2
        left,right=seq[:cut],seq[cut:]
        le,re=block_variance(left),block_variance(right)
        here=block_variance(seq)
        contribution=F(n,length)*(F(cut,n)*le+F(n-cut,n)*re-here)
        if contribution<0:raise ArithmeticError('negative exact wavelet contrast')
        return contribution+recurse(left)+recurse(right)
    return recurse(pts)


def wavelet_remaining_energy(phases):
    """Exact nonzero Haar residual after spending source-wavelet details."""
    return constant_single_atom_energy()-wavelet_detail_budget(phases)


def prefix_shadow_tail(length):
    """L-infinity/L2 feature error for true pi prefix vs one source endpoint."""
    if type(length) is not int or length<1:raise ValueError
    return F(16,7225*length)*source_r(length+1)

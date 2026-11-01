"""OPTIONAL non-certifying numerical illustration of the flat-top alias filter.

This uses numpy quadrature, not interval arithmetic. Proofs use only the
analytic inequalities in PROOFS.md and Fraction regression tests.
"""
from __future__ import annotations
import argparse, json, math
import numpy as np


def _cutoff(s):
    a=np.abs(s)
    psi=np.ones_like(a)
    psi[a>=.25]=0.
    mask=(a>.125)&(a<.25)
    u=(a[mask]-.125)*8.
    left=np.exp(-1/u)
    right=np.exp(-1/(1-u))
    psi[mask]=right/(left+right)
    return psi


def _r(x):
    return 4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)


def _t(x):
    result=np.zeros_like(x,dtype=float)
    for j in range(1,17):
        result+=16.**(-j)*_r(x+j)
    return result


def band_value(M,N,q,h,points):
    if not 1<=M<=N: raise ValueError('need 1<=M<=N')
    L=16**M
    s=-.25+(np.arange(points,dtype=float)+.5)*(.5/points)
    psi=_cutoff(s)
    sinpi=np.sin(np.pi*s)
    D=np.sin(np.pi*(6*L+1)*s)/sinpi
    H=(np.sin(np.pi*L*s)/(L*sinpi))**4
    K=H*D
    s_complex=np.zeros(N,dtype=complex)
    b_complex=np.zeros(N,dtype=complex)
    for n in range(1,N+1):
        x=n+s
        values=q*16.**x-_t(x)
        phase=np.exp((2j*np.pi*h)*np.remainder(values,1))
        b_complex[n-1]=np.mean(.5*psi*K*phase)
        u=q*16.**n-float(_t(np.array([float(n)]))[0])
        s_complex[n-1]=np.exp((2j*np.pi*h)* (u%1))
    return {"M":M,"N":N,"q_label":"selected pi/16" if abs(q-math.pi/16)<1e-12 else "coherent 1/5",
        "sample_prefix": [float(np.sum(s_complex[:M]).real),float(np.sum(s_complex[:M]).imag)],
        "band": [float(np.sum(b_complex).real),float(np.sum(b_complex).imag)],
        "difference": float(abs(np.sum(b_complex)-np.sum(s_complex[:M]))),
        "b_per_cell_abs": [float(abs(z)) for z in b_complex]}


def slice_energy(N,q,h,points):
    s=-.25+(np.arange(points,dtype=float)+.5)*(.5/points)
    psi=_cutoff(s)
    total=np.zeros(points,dtype=complex)
    for n in range(1,N+1):
        values=q*16.**(n+s)-_t(n+s)
        total+=np.exp((2j*np.pi*h)*np.remainder(values,1))
    diag=float(.5*N*np.mean(psi**2))
    full=float(.5*np.mean(psi**2*np.abs(total)**2))
    return {"N":N,"q":q,"h":h,"diagonal":diag,"full_energy":full,
            "offdiagonal":full-diag,"strict_paper_bound_at_h1":"8/(75*pi)"}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--points',type=int,default=131072)
    a=p.parse_args()
    if a.points<8192 or a.points%2: p.error('Need at least 8192 even samples')
    results=[]
    for q in (math.pi/16,.2):
        for M,N in ((1,3),(2,4)):
            a1=band_value(M,N,q,1,a.points)
            a2=band_value(M,N,q,1,a.points*2)
            a2['grid_difference']=abs(complex(*a1['band'])-complex(*a2['band']))
            a2['proof_grade']=False
            results.append(a2)
    slices=[]
    for q in (math.pi/16,.2):
        for N in (2,3):
            a1=slice_energy(N,q,1,a.points)
            a2=slice_energy(N,q,1,a.points*2)
            a2['grid_difference']=abs(a2['offdiagonal']-a1['offdiagonal'])
            a2['proof_grade']=False
            slices.append(a2)
    print(json.dumps({"kind":"finite_nonproof_diagnostic", "results":results,
                      "continuous_slice_diagnostics":slices},indent=2))

if __name__=='__main__':main()

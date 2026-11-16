#!/usr/bin/env python3
"""Reproduce the scientific figure; values are floating-point diagnostics."""
from pathlib import Path
import json
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def weights(omega, max_degree):
    p0=(1+omega*omega)*math.pi*omega/math.sinh(math.pi*omega) if omega else 1.0
    out=np.empty(max_degree+1)
    out[0]=p0
    for m in range(max_degree):
        out[m+1]=out[m]*(m*m+omega*omega)/((m+1)*(m+2))
    return out


def main():
    root=Path(__file__).resolve().parent
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                         'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
    fig.suptitle('Gamma compression keeps one coordinate of a unit phase',fontsize=17)
    x=np.linspace(0.001,12,500)
    scalar=(1+x*x)*np.pi*x/np.sinh(np.pi*x)
    axes[0].semilogy(x,scalar,color='#7438a5',linewidth=2.5,label=r'$|c_0|^2=|\Gamma(2+i\omega)|^2$')
    axes[0].axhline(1,color='#b58a1c',linewidth=2,label=r'Full mode energy $\sum_m |c_m|^2=1$')
    axes[0].set(xlabel=r'Log-frequency $\omega$',ylabel='Squared norm',ylim=(1e-13,2))
    axes[0].set_title('Scalar readout becomes small')
    axes[0].legend(frameon=False,loc='lower left')
    axes[0].grid(alpha=.15)
    colors=['#4597aa','#dd9330','#7438a5']
    for omega,color in zip([4,12,40],colors):
        p=weights(omega,int(6*omega*omega))
        degree=np.arange(len(p))
        axes[1].plot(degree/(omega*omega),(omega*omega)*p,
                     color=color,linewidth=1.7,label=rf'$\omega={omega}$')
    y=np.linspace(.04,6,1500)
    axes[1].plot(y,y**-3*np.exp(-1/y),'k--',linewidth=1.8,
                 label=r'Limit: $y^{-3}e^{-1/y}$')
    axes[1].set(xlabel=r'Rescaled degree $m/\omega^2$',ylabel=r'Rescaled mode weight $\omega^2|c_m|^2$',
                xlim=(0,4),ylim=(0,1.6))
    axes[1].set_title('Energy occupies higher retained modes')
    axes[1].legend(frameon=False)
    axes[1].grid(alpha=.15)
    fig.savefig(root/'gamma_mode_energy.png',dpi=180)
    report={'scope':'Floating-point illustration of the proved modal identities; not interval certification',
            'omega_10_scalar_squared_norm':float(weights(10,0)[0]),
            'omega_10_cutoff_711_squared_error':float(1-weights(10,711).sum()),
            'omega_10_cutoff_711_proved_upper_bound':'2525/253116',
            'inverse_gamma2_limit_density':'y^-3 exp(-1/y), y>0',
            'curves':[4,12,40]}
    (root/'receipts/figure_values.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()

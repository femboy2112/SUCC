"""Read-only visualization of a finite observation receipt. No new inference."""
from __future__ import annotations
import argparse, json
from pathlib import Path


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('receipt',type=Path)
    parser.add_argument('--out',type=Path,default=Path('/tmp/succ_zero_origin_figures'))
    args=parser.parse_args(argv)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    data=json.loads(args.receipt.read_text(encoding='utf-8'))
    args.out.mkdir(parents=True,exist_ok=True)
    checkpoints=data['checkpoints']
    n=[r['n'] for r in checkpoints]
    fig,ax=plt.subplots(figsize=(8,4.6),layout='constrained')
    for k in (1,2,3):
        normalized=[r['word_energies'][k-1]*r['n']/(16**k-1) for r in checkpoints]
        ax.plot(n,normalized,marker='o',label=f'{k}-digit word mode')
    ax.axhline(1,linestyle='--',label='1/N reference scale')
    ax.set_xscale('log',base=2)
    ax.set_xlabel('Number of certified π hex digits, N (from U₀=0)')
    ax.set_ylabel('N Eₖ / (16ᵏ − 1)')
    ax.set_title('Observed normalized word discrepancy across time')
    ax.legend()
    fig.savefig(args.out/'zero_origin_energy_time.png',dpi=160)
    plt.close(fig)
    final=data['final_controls']
    samples=['BBP','same_counts_shuffled','toy_spectral_feedback','same_counts_sorted','periodic_balanced','debruijn_order3','coherent_shadow']
    v=[final[s]['checkpoint']['word_energies'][2] for s in samples]
    fig,ax=plt.subplots(figsize=(9.2,4.8),layout='constrained')
    ax.bar(range(len(samples)),v)
    ax.set_yscale('symlog',linthresh=.05)
    ax.set_xticks(range(len(samples)),[s.replace('_','\n') for s in samples],rotation=25,ha='right',fontsize=8)
    ax.set_ylabel('Length-3 discrepancy energy, E₃ (symmetric-log axis)')
    ax.set_title('Same low-order mass can conceal sharply different chronology')
    fig.savefig(args.out/'zero_origin_controls_depth3.png',dpi=160)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(8.3,4.6),layout='constrained')
    peaks=[r['spectral']['largest_nonzero_power'] for r in checkpoints]
    ax.plot(n,peaks,marker='o',label='Original BBP h=1 non-DC peak')
    ax.plot(n,[1 for _ in n],linestyle='--',label='Balanced periodic 16-cycle peak')
    ax.set_xscale('log',base=2)
    ax.set_yscale('log')
    ax.set_xlabel('Number of certified π hex digits, N')
    ax.set_ylabel('Largest normalized nonzero temporal Fourier power')
    ax.set_title('Persistent spectral line vs observed diffuse power')
    ax.legend()
    fig.savefig(args.out/'zero_origin_peak_spectral_line.png',dpi=160)
    plt.close(fig)
    hexfile=args.receipt.parent/'certified_hex_16384.txt'
    if hexfile.exists():
        from math import cos,pi,sin
        ds=[int(c,16) for c in hexfile.read_text(encoding='ascii').strip()]
        xx=[0.];yy=[0.];x=y=0.
        for d in ds:
            x+=cos(2*pi*d/16);y+=sin(2*pi*d/16)
            xx.append(x);yy.append(y)
        fig,ax=plt.subplots(figsize=(6,6),layout='constrained')
        stride=max(1,len(ds)//512)
        ax.plot(xx[::stride]+[xx[-1]],yy[::stride]+[yy[-1]],lw=.9)
        ax.scatter([0,xx[-1]],[0,yy[-1]],s=[35,35])
        ax.annotate('Origin: U₀=0',xy=(0,0),xytext=(5,5),textcoords='offset points')
        ax.annotate(f'16,384-digit endpoint' if len(ds)==16384 else f'{len(ds)}-digit endpoint',
                    xy=(xx[-1],yy[-1]),xytext=(5,5),textcoords='offset points')
        ax.set_aspect('equal',adjustable='box')
        ax.set_xlabel('Real cumulative digit character')
        ax.set_ylabel('Imaginary cumulative digit character')
        ax.set_title('Literal unit-step spectral walk from zero')
        fig.savefig(args.out/'zero_origin_unit_phase_walk.png',dpi=160)
        plt.close(fig)
    print('Charts written to',args.out)

if __name__=='__main__':
    main()

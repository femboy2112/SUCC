"""Optional finite trace visualization; empirical diagnostics only."""
import json
import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    data=json.loads(Path(sys.argv[1]).read_text())
    out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    n=data['input']['digits']
    fig,ax=plt.subplots(figsize=(10,4))
    for rank,order in enumerate(('2','4','8','16'),1):
        x=data['exact_reset_walk']['spectral_zeros'][order]
        ax.scatter(x,[rank]*len(x),s=13,label=f'order {order}, rank {order}//2: {len(x)} returns')
    ax.set_xlim(0,n+120)
    ax.set_yticks((1,2,3,4),('parity • rank 1','quarter-turn • rank 2','eighth-turn • rank 4','sixteenth-turn • rank 8'))
    ax.set_xlabel('First N hexadecimal digits of π (certified original BBP prefix)')
    ax.set_title('Exact integer spectral-return horizons (not all-digit balance)')
    ax.grid(alpha=.25)
    fig.tight_layout();fig.savefig(out/'zero_seed_spectral_return_times.png',dpi=160)
    plt.close(fig)
    xs=[];lines={1:[],2:[],3:[]}
    for h,payload in sorted(data['checkpoints'].items(), key=lambda pair:int(pair[0])):
        xs.append(int(h))
        for k in (1,2,3):
            v=payload[str(k)]['renormalized']
            lines[k].append(v['numerator']/v['denominator'])
    fig,ax=plt.subplots(figsize=(10,4))
    for k in (1,2,3):
        ax.plot(xs,lines[k],marker='o',label=f'k={k} renormalized discrepancy')
    ax.axhline(1,linestyle='--',linewidth=1,label='iid expectation (not a deterministic target)')
    ax.set_xscale('log',base=2);ax.set_yscale('log')
    ax.set_xlabel('N certified digits, logarithmic scale')
    ax.set_ylabel('N E_k(N)/(16^k−1), logarithmic scale')
    ax.set_title('Renormalized word energy across the original zero-seed path')
    ax.grid(alpha=.25)
    ax.legend()
    fig.tight_layout();fig.savefig(out/'renormalized_word_spectral_energy.png',dpi=160)
    plt.close(fig)
    print('wrote figures to',out)
if __name__=='__main__':main()

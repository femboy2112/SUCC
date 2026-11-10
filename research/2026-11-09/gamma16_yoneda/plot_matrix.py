"""Plot non-proof 16x16 empirical BBP matrix and its Fourier modes."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from observational_succ.bbp_gamma16_matrix import pair_counts, fourier_pair_modes

HERE=Path(__file__).resolve().parent
s=(HERE/'REUSED_HEX_40960.txt').read_text().strip()
d=tuple(int(ch,16) for ch in s)
raw=pair_counts(d)
c=np.array(raw)
z=np.array(fourier_pair_modes(raw))
fig,ax=plt.subplots(figsize=(7.2,6.5))
im=ax.imshow(c, interpolation='nearest',aspect='equal')
ax.set(title='Source-certified π/16: adjacent hex-digit counts (N = 40,960)',
       xlabel='Next digit b',ylabel='Current digit a')
ax.set_xticks(range(16), list('0123456789ABCDEF'))
ax.set_yticks(range(16), list('0123456789ABCDEF'))
fig.colorbar(im,ax=ax,shrink=.82,label='Exact pair count; Haar reference = 160')
fig.tight_layout()
fig.savefig(HERE/'pair_counts_16x16.png',dpi=150)
plt.close(fig)
z[0,0]=0
fig,ax=plt.subplots(figsize=(7.2,6.5))
im=ax.imshow(abs(z), interpolation='nearest',aspect='equal')
ax.set(title='Nontrivial joint Fourier modes (DC omitted)',
       xlabel='Future character v',ylabel='Current character u')
ax.set_xticks(range(16),list('0123456789ABCDEF'))
ax.set_yticks(range(16),list('0123456789ABCDEF'))
fig.colorbar(im,ax=ax,shrink=.82,label='Fourier coefficient magnitude (diagnostic)')
fig.tight_layout()
fig.savefig(HERE/'fourier_modes_16x16.png',dpi=150)
plt.close(fig)
print('Wrote pair_counts_16x16.png, fourier_modes_16x16.png')

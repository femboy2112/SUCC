# Next selected-source gate after the forge

The round is closed with the [dossier](PI_SELECTED_PHASE_FORGE.md),
[claim ledger](../../docs/CLAIM_SUPPLEMENT_PI_SELECTED_PHASE.md), and
[validation receipt](PI_SELECTED_PHASE_VALIDATION.md). Normality remains OPEN.
No additional experiment or promised continuation is part of this receipt.

## The narrower unresolved object

Use the original carries and common forcing conductors. Retain
$b_t=c_t\mathbf1_{\{Q_t=Q_{t-1}\}}$, without changing the original source.
Set $H_N=\max(2,1+\lfloor\sqrt{\lfloor\log_2N\rfloor^3}\rfloor)$ and
let $J_N$ be minimal with $16^{J_N}\ge NH_N^2$. The remaining sufficient
estimate is

$$
2\sum_{h=1}^{H_N-1}\left(1-\frac h{H_N}\right)
\left|\frac1N\sum_{n=1}^N
e\left(h\sum_{j=1}^{J_N}16^{-j}b_{n+j}\right)\right|^2=o(1).
$$

The sparse-carry and truncation theorems pay every comparison error from
this exact finite observable to the original pi orbit. The displayed
bound is **not proved**. The new unconditional logarithmic absolute loss
only excludes extreme coherence of the authentic full orbit; it does not
control this moderate-coherence problem.

## An exact carrier available for that next gate

The following is a PAPER-PROVED elementary corollary of the finite prefix
formula and classical cyclotomic/Walsh identities, not a new cancellation
bound or Lean result. Let $M=16^{J_N}$ and

$$
a_n=\left(\sum_{j=1}^{J_N}b_{n+j}16^{J_N-j}\right)\bmod M.
$$

Then $NH_N^2\le M<16NH_N^2$, and the finite Gram matrix lies in
$\mathbb Q[\zeta_M]$. The large original odd conductors have been replaced
in this **derived finite observable** by one dyadic carrier with a paid
tail. The original source still selects every coefficient. A carry of
value 16 must be retained before the final reduction; reducing each
carry modulo 16 separately is wrong.

For a frequency $h$ put $L=M/\gcd(M,h)$ and let
$C_r=\#\{n:a_n\equiv r\pmod L\}$. If $L>1$, then

$$
\sum_{n=1}^N e(ha_n/M)=0
\quad\Longleftrightarrow\quad
C_r=C_{r+L/2}\quad(0\le r<L/2).
$$

Indeed the reduced frequency is odd, hence a Galois automorphism reduces
the zero test to frequency one. Division by
$\Phi_L(X)=X^{L/2}+1$ leaves the polynomial with coefficients
$C_r-C_{r+L/2}$ of degree less than $L/2$; minimality of $\Phi_L$ proves
necessity and sufficiency. For $L=1$ the sum is $N$. The zero test needs
only sparse integer counts, not expansion of the entire cyclotomic field.

With normalized Walsh coefficients
$\omega_s=N^{-1}\sum_r C_r(-1)^{\operatorname{popcount}(s\mathbin{\&}r)}$,
Walsh inversion makes the same condition equivalent to the vanishing of
**every** coefficient with $L/2\le s<L$. Lower-order balance cannot replace
this full block, which includes the highest interaction.

There is also a decisive limitation. The full histogram on $M$ residues
has support at most $N$. Parseval and Cauchy--Schwarz give

$$
\sum_{s\ne0}\omega_s^2
=M\sum_x(C_x/N)^2-1
\ge M/N-1\ge H_N^2-1.
$$

Thus small **global** Walsh energy is impossible at this exact conductor
schedule. Only its selected low Fourier compression can tend to zero.
This support obstruction does not bound that compression from below.
The exact prefix instrument already supplies the inputs to these
identities; no new finite asymptotic or kernel certificate is claimed.

Any next estimate must survive both the exact-forcing changed-seed controls
and the positive changed-forcing carry/tower control, without combining
their different preserved features. It must use more than irrationality
type, unlabelled prime marginals, total Walsh energy, or small transport
costs. Scholarly novelty of these elementary carrier observations is not
asserted.

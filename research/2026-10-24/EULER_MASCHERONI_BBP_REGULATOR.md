# Euler--Mascheroni, the authentic BBP source, and a uniform regulator defect

**Status:** paper proofs and exact finite certificates. The original BBP forcing
is preserved only at exponent $s=1$. No pi-normality or RH conclusion is claimed.
Scholarly priority of the elementary synthesis has not been established.

This note connects the shifted finite part in
[the successor/refinement note](EULER_MASCHERONI_SUCCESSOR_REFINEMENT.md)
to the actual source used by the repository. It supplies an explicit
noncommuting-limit theorem on that source family, with a tail bound valid for
every real $s>0$. It does not replace a selected source by a Haar ensemble.

## 1. Fix the four rays before transforming them

For $n\ge1$ define

$$
r_s(n)=\frac4{(8n-7)^s}-\frac2{(8n-4)^s}
       -\frac1{(8n-3)^s}-\frac1{(8n-2)^s}.
$$

The ordinary BBP source is $r(n)=r_1(n)$, and its original zero-initial
recurrence is

$$
U_0=0,\qquad U_n=16U_{n-1}+r_1(n).
$$

The classical BBP identity and the existing corrected source proof give

$$
\pi=\sum_{n\ge1}16^{-(n-1)}r_1(n),\qquad
U_n=16^{n-1}\pi-T_n,
$$

$$
0<T_n<\frac1{(8n+1)(8n+2)}<\frac1{64n^2}.
$$

See [the source repair](BBP_SOURCE_MEMORY_REPAIR.md) and
[the unchanged source module](../../observational_succ/bbp_source_memory.py).
The four numbers $7,4,3,2$ are denominator offsets; they are not orbit points.
Changing $s$ changes the forcing. Changing the recurrence initial state also
changes the selected orbit, even when the forcing remains identical.

## 2. An exact finite Lerch refinement

For $a>0$ let

$$
\Phi_N(z,s,a)=\sum_{n=0}^{N-1}\frac{z^n}{(n+a)^s}.
$$

Partitioning $n=pk+j$, for every integer $p\ge2$, gives the finite identity

$$
\Phi_{pN}(z,s,a)
=p^{-s}\sum_{j=0}^{p-1}z^j
  \Phi_N\!\left(z^p,s,\frac{a+j}{p}\right).
\tag{1}
$$

This is a finite bijection of source indices, so it needs no exchange of
limits. Both the phase factor $z^j$ and the new regulator $z^p$ are required.
It applies equally to prime and composite $p$; calling a partition a prime
refinement does not make it an independent Euler factor.

Set

$$
(c_1,c_2,c_3,c_4)=(4,-2,-1,-1),\qquad
(a_1,a_2,a_3,a_4)=\left(\frac18,\frac12,\frac58,\frac34\right).
$$

Then, still at every finite horizon,

$$
\sum_{n=1}^N z^{n-1}r_s(n)
=8^{-s}\sum_{j=1}^4 c_j\Phi_N(z,s,a_j).
\tag{2}
$$

For $|z|<1$ this converges locally uniformly for complex $s$. The classical
Lerch family therefore gives an honest common coordinate system:

$$
\mathcal B_s(z)=8^{-s}\sum_{j=1}^4c_j\Phi(z,s,a_j),
\qquad \mathcal B_1(1/16)=\pi.
\tag{3}
$$

The definition and source conventions are those of
[DLMF 25.14](https://dlmf.nist.gov/25.14). Equations (1)--(2), rather than
analytic resemblance alone, establish the finite connection to this repo.

## 3. A positive decomposition gives a uniform tail

For real $s>0$ write $f_s(x)=x^{-s}$. The signed forcing has the exact
positive-difference decomposition

$$
r_s(n)=2[f_s(8n-7)-f_s(8n-4)]
       +[f_s(8n-7)-f_s(8n-3)]
       +[f_s(8n-7)-f_s(8n-2)].
\tag{4}
$$

Each difference is $s\int_A^B t^{-s-1}\,dt$. The total interval length,
including multiplicities, is $2\cdot3+4+5=15$. Since the integrand is strictly
decreasing,

$$
\frac{15s}{(8n-2)^{s+1}}
<r_s(n)<\frac{15s}{(8n-7)^{s+1}}.
\tag{5}
$$

In particular the unregulated series

$$
B(s)=\sum_{n\ge1}r_s(n)
$$

converges for every real $s>0$. Integral comparison in (5) gives, for $N\ge1$,

$$
\boxed{
\frac{15}{8}(8N+6)^{-s}
<B(s)-\sum_{n=1}^Nr_s(n)
<\frac{15}{8}(8N-7)^{-s}.}
\tag{6}
$$

For the lower bound integrate the lower comparison function from $N+1$ to
infinity. For the upper bound integrate the upper comparison function from
$N$ to infinity. This proves (6) for all positive $s$ simultaneously; it is
not an extrapolation from the integer-power certificate functions.

For complex $s$ in a compact subset of $\Re s>0$, the same integral
decomposition bounds the absolute value by a constant times
$n^{-\Re s-1}$. Thus the series is locally normally convergent there.

For a fixed $0<z<1$ the positive terms in (4) also decrease with $n$, giving
the simple geometric remainder

$$
0<\mathcal B_s(z)-\sum_{n=1}^Nz^{n-1}r_s(n)
\le\frac{z^N r_s(N+1)}{1-z}.
\tag{7}
$$

Equation (7) produces rational pi enclosures at $s=1,z=1/16$ without any
digit-frequency assumption.

## 4. The exponent-zero mass is lost by taking the cutoff first

For $\Re s>1$, ordinary summation gives

$$
B(s)=8^{-s}\sum_{j=1}^4c_j\zeta(s,a_j).
\tag{8}
$$

Every Hurwitz zeta has the same simple pole at $s=1$, of residue one.
Since $\sum c_j=0$, (8) extends to an entire function. It agrees with the
series in the whole half-plane $\Re s>0$ by the preceding normal convergence
and the identity theorem. Equivalently, using
$G(s,a)=\zeta(s,a)-1/(s-1)$,

$$
B(s)=8^{-s}\sum_{j=1}^4c_jG(s,a_j).
\tag{9}
$$

The classical value $\zeta(0,a)=1/2-a$ now gives

$$
\boxed{B(0)=\sum_{j=1}^4c_j(1/2-a_j)=\frac{15}{8}.}
\tag{10}
$$

By contrast, $r_0(n)=4-2-1-1=0$ for every finite $n$. Thus

$$
\lim_{s\downarrow0}\lim_{N\to\infty}\sum_{n=1}^Nr_s(n)=\frac{15}{8},
\qquad
\lim_{N\to\infty}\lim_{s\downarrow0}\sum_{n=1}^Nr_s(n)=0.
\tag{11}
$$

The precise cofinal statement is stronger. If $s\downarrow0$, $N\to\infty$
and $s\log N\to c\in[0,\infty]$, the two sides of (6) have the same limit
$(15/8)e^{-c}$, with $e^{-\infty}=0$. Hence

$$
\boxed{
\sum_{n=1}^Nr_s(n)\longrightarrow
\frac{15}{8}(1-e^{-c}).}
\tag{12}
$$

For the particularly transparent clock $s=1/m$, $N=b^m$, integer $b\ge2$,

$$
\sum_{n=1}^{b^m}r_{1/m}(n)\longrightarrow
\frac{15}{8}\left(1-\frac1b\right).
$$

At $b=2$ the limit is $15/16$. These limits follow from (6) and (10), not
from the optional numerical Hurwitz evaluation.

The other regulator has a separate seam. For fixed $|z|<1$,
$\mathcal B_0(z)=0$, whereas letting $z\uparrow1$ first at $s>0$ recovers
$B(s)$ and then (10). The regulator and the exponent must both be recorded.

## 5. Where Euler's constant enters, and where it cancels

At $s=1$, $G(1,a)=-\psi(a)$, with $\psi$ the digamma function. Therefore

$$
B(1)=-\frac18\sum_{j=1}^4c_j\psi(a_j).
$$

The common $-\gamma$ term in the rational digamma values cancels because
$\sum c_j=0$. Gauss's formula and the reflection law give

$$
B(1)=\frac\pi4+\frac{5\sqrt2\pi}{16}
      +\frac{5\log2}{8}
      +\frac{5\sqrt2}{8}\log(1+\sqrt2).
\tag{13}
$$

It is approximately $3.38604761959719$, while
$\mathcal B_1(1/16)=\pi$. Setting $z=1$ has changed the weighting of the
original BBP expansion. Equation (13) is an optional classical evaluation;
none of the certificates uses that decimal value as an input.

The useful shared object is the full shifted, regulated source family.
Knowing the scalar $\gamma=G(1,1)$ does not supply all the shifts, the BBP
regulator, or the selected orbit's Fourier cancellation.

## 6. Implementation, controls, and the numerical failure receipt

[euler_bbp_regulator.py](../../observational_succ/euler_bbp_regulator.py)
implements finite Lerch partitions, exact integer-exponent forcing, rational
tails, and the analytic boundary value. The exact functions accept
integers/Fractions. Their finite domain is narrower than the paper theorem's
real/complex domain and is labelled accordingly.

[The focused tests](../../tests/test_euler_bbp_regulator.py) compare the
$s=1$ source with the unchanged BBP module at 256 indices, check independent
residue interleavings, compare pi intervals with Machin bounds, and reject
missing factors, false endpoint identifications, and invalid inputs.
[The combined probe](../../scripts/euler_mascheroni_probe.py) records exact
finite certificates in [the receipt](euler_mascheroni_validation/probe_receipt.json).

An audit found a real failure in the optional floating-point diagnostic:
the Hurwitz differences at $m=400,N=2^{400}$ returned **0.0 at 70 dps**,
but **0.948528108646579546014716 at 220 dps**. Intermediate values are of
order $N$, so a fixed working precision erases the residual. The
[original failure receipt](euler_mascheroni_validation/bbp_precision_failure.json)
is preserved. The implementation now rejects precision below an upper bound
on the decimal digits of $N$ plus 35 guard digits, and caps the diagnostic
budget. This is a cancellation guard, not a rigorous error certificate;
the optional readout remains labelled numerical-only.

## 7. The next obligation

The new uniform tail controls an authentic source deformation and resolves
the cutoff/exponent order explicitly. It does not control
$\sum_{N<n\le pN}e(hU_n)/n$: exponentiating a selected long recurrence
introduces cancellation which positivity of (4) does not settle.
[The character note](EULER_MASCHERONI_CHARACTER_TAUBERIAN.md) proves the exact
two-time-dilation target and its source-to-pi error. That is the next
arithmetic obligation, for every fixed nonzero integer $h$ and both $p=2,3$.

### Provenance

- Existing corrected BBP source and tail: repository main
  `e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
- Classical Hurwitz pole, special values, and analytic continuation:
  [DLMF 25.11](https://dlmf.nist.gov/25.11).
- Classical digamma reflection and multiplication:
  [DLMF 5.5](https://dlmf.nist.gov/5.5).
- Classical Lerch definition and recurrences:
  [DLMF 25.14](https://dlmf.nist.gov/25.14).
- The proofs above were checked internally by same-model agents; this is
  not independent external refereeing or new Lean-kernel authority.

# OPERATION MESOSCOPIC SPECTRAL ARMY — conditional normality at every positive spatial exponent

**2026-11-02 | Research only.** Base-16 normality of pi remains OPEN. The following elementary implications are *paper proofs*, not Lean theorems or a source-selected cancellation estimate. Stack strictly on draft PR #474 head `f60ebe5885c1de1f618d52445de77e089e841d3a`. Parent #474 provides the exact original four-pole Gamma tail and earlier self-scale sublog sufficient condition. Do not modify `U_0=0`, source poles, canonical archives or main.

## Definitions and exact source contract

The ORIGINAL Bailey–Borwein–Plouffe source is

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`.

Put `alpha=pi/16`, `X_n=16^n alpha (mod 1)` and `T_n=sum_(k>=1)16^{-k}r(n+k)`. The original identity and inherited positive Gamma bound are

`X_n=U_n+T_n (mod 1)`, `0<T_n<1/((8n+1)(8n+2))<1/(64 n^2)` for n>=1.

For a finite multiset of N real-circle phases, write `v_j` for occupancy of the j-th half-open interval of length 1/m, `E_(N,m)=(m/N^2)*sum_j v_j^2`, and `S_N(h)=sum_n exp(2 pi i h x_n)`. All meshes below are even powers of two. For a dyadic epoch A, phases are the *selected original zero-seeded* `U_A,...,U_(2A-1)`, never a prime-averaged surrogate.

## MSA-01. Exact full-modulus and independent changing-modulus representations (PROVED)

Let `D_N=lcm{8n-7,8n-4,8n-3,8n-2 : 1<=n<=N}`. Define `a_0=0` and, modulo D_N,

`a_n=16*a_(n-1)+4*D_N/(8n-7)-2*D_N/(8n-4)-D_N/(8n-3)-D_N/(8n-2)`.

All displayed quotients are integers. Induction proves `0<=a_n<D_N` and `{U_n}=a_n/D_N`. An independent online representation takes `d_0=1,b_0=0`, `d_n=lcm(d_(n-1),four pole denominators at n)`, and

`b_n = (16*(d_n/d_(n-1))*b_(n-1) + source injection scaled by d_n) mod d_n`.

It satisfies `{U_n}=b_n/d_n` by the same elementary source identity but a different integer evaluation path. Both oracles retain ALL four signed poles and the literal zero boundary, including the real selected embedding. They do not prove limiting normality.

## MSA-02. Exact near-pair / fixed-bin equivalence (PROVED)

Define the ordered, diagonal-inclusive near-pair count

`P_(N,m)=#{(n,t): m * ||x_n-x_t||_(R/Z) <= 1}`.

Every pair in one bin has circle distance <=1/m. Every near pair lies in equal or neighboring bins (cyclically). Thus, by Cauchy–Schwarz on adjacent occupancies,

`sum_j v_j^2 <= P_(N,m) <= 3*sum_j v_j^2`.

Consequently `E_(N,m) <= (m/N^2)*P_(N,m) <= 3 E_(N,m)`. This removes dependence on the arbitrary bin origin, up to a universal constant. The code computes P exactly by sorting a common-denominator residue list and two monotone sweeps; an antipodal correction is necessary at m=2. It is calibrated against an O(N^2) independent oracle.

## MSA-03. TWO-SIDED exact Fejer / occupancy comparison (PROVED)

For even m>=2 put H=m/2-1, `F_H(t)=(H+1)^(-1)|sum_(k=0)^H exp(2 pi i k t)|^2` and

`Q_(N,m)=(1/N^2)*sum_(n,t) F_H(x_n-x_t) = 1+(2/N^2)*sum_(h=1)^H (1-2h/m)|S_N(h)|^2`.

Then, for ALL N, even m, and circle phases,

`(2/pi^2)*E_(N,m) <= Q_(N,m) <= (3/2+pi^2/6)*E_(N,m)`.

**Lower:** for `||t||<=1/m`, `|sin(pi m t/2)|>=m||t||` and `|sin(pi t)|<=pi||t||`; hence `F_H(t)>=2m/pi^2`, including by continuity t=0. Restrict the positive pair-kernel to ordered within-bin pairs to obtain `Q>=2E/pi^2`.

**Upper:** let cyclic distance d between bin indices be 0,1,...,floor(m/2). If d<=1 use `F_H<=m/2`. For d>=2 the circle distance between points is >=(d-1)/m, hence `|sin(pi t)|>=2(d-1)/m` and `F_H(t)<=m/[2(d-1)^2]`. The nonnegative circulant bin-weight kernel has row sum at most `1+2*(1+sum_(k>=1)1/k^2)=3+pi^2/3`. Applying 2ab<=a^2+b^2 proves the asserted upper constant `(3+pi^2/3)/2`. No equidistribution premise or independent-phase assumption enters.

In particular, for the selected source on [A,2A), `E_(A,m_A)=o(log A)` is equivalent (up to constants) to the **positive growing-band original Fourier criterion** `Q_(A,m_A)=o(log A)`.

## MSA-04. Gamma tail STABILITY in Fourier Hilbert norm (PROVED)

Take N=A selected states on [A,2A), compare `U_n` against `X_n=16^n*pi/16`, and choose m=A. Let `Q_U`, `Q_X` denote their respective energies from MSA-03. From `|exp(2pi ihU_n)-exp(2pi ihX_n)|<=2pi|h|T_n` and `sum_(n=A)^(2A-1)T_n<=1/(64A)`, each Fourier sum differs by at most `pi h/(32A)`.

Use the weighted vector with entries `sqrt(2(1-2h/A))*S(h)/A` for 1<=h<=A/2-1. Its squared norm equals `Q-1`. The reverse triangle inequality and `sum_(h=1)^(A/2-1)h^2<=A^3/24` therefore give the **uniform quantitative selected-orbit bound**

`|sqrt(Q_U-1)-sqrt(Q_X-1)| <= pi/sqrt(12288 A)`.

This is a genuine positive Hilbert-norm transport with exact source-tail error; neither side is shown small. It is not a normality result, and the same tail law exists for hostile changed seeds.

## MSA-05. MESOSCOPIC CONDITIONAL NORMALITY, any beta>0 (PROVED IMPLICATION, SOURCE PREMISE OPEN)

**Theorem.** Fix ANY `0<beta<=1`. For each dyadic `A=2^j`, set `m_A=max(2,2^floor(beta*j))` and define the *original zero-seeded* epoch energy

`E_(A,beta)= (m_A/A^2)*sum_(i<m_A) #{A<=n<2A: floor(m_A*{U_n})=i}^2`.

If `E_(A,beta)=o(log A)` as dyadic A->infinity, **then pi is normal in base 16**. The hypothesis is OPEN; this theorem makes no claim that pi satisfies it.

**Proof with ALL prefixes (not just dyadic endpoints).** Choose constants `0<kappa<2*beta/(2+beta)` and `kappa/beta<theta<1-kappa/2`. For arbitrary N->infinity set `M=2^floor(kappa log_2 N)` and `A0=2^ceil(theta log_2 N)`. Then `sqrt(M)*A0/N=O(N^(kappa/2+theta-1))=o(1)` and, for every dyadic epoch A>=A0 with A<N, `m_A>=M` eventually, since `theta*beta>kappa`. Also `M T_n<1` for n>=A0 eventually.

Discard first A0 phases of the TRUE completed orbit X: their M-bin histogram has l2 norm at most A0. For each remaining full/partial epoch `[A,min(2A,N))`, let `v(A,m_A)` denote the full ORIGINAL source m_A-bin histogram. Universal fine-to-coarse Cauchy (parent PGC-10) gives the full source M-bin norm bound

`||u_(A,M)||_2^2 <= (m_A/M+2)*sum_i v_i(A,m_A)^2 <= 3*A^2*E_(A,beta)/M`.

The TRUE phase `X_n=U_n+T_n` moves monotonically forward by less than ONE M-bin because `0<T_n<1/M`. Thus each true bin receives points from at most itself and the preceding original bin. For the partial epoch its histogram norm is bounded by `2||u_(A,M)||_2` of the complete source epoch. Minkowski and `sum_(dyadic A<N) A <2N` yield, with `B_(N,M)=(M/N^2)*sum_(j<M) c_j^2` for the true X-prefix histogram,

`sqrt(B_(N,M)) <= sqrt(M)*A0/N + (2 sqrt(3)/N)*sum_(A0<=A<N,dyadic) A*sqrt(E_(A,beta))`

`<= o(1)+4 sqrt(3)*sqrt(max_(A0<=A<N,dyadic)E_(A,beta)) = o(sqrt(log N))`.

The last equality follows since A0->infinity, A<=N, and the assumed dyadic `E_(A,beta)/log A->0`. Hence `B_(N,M)=o(log N)`. MSA-03 gives `Q_(N,M)=o(log N)` for TRUE radix orbit X, at a growing harmonic window `H=M/2-1`.

Fix h!=0. Choose K~log_16 M~kappa log_16 N distinct modes `h*16^k` for 0<=k<K, with `|h|16^(K-1)<=M/4` so their Fejer weights are >=1/2 for sufficiently large N. The exact radix shift yields `|S_N(h*16^k)/N-S_N(h)/N|<=2k/N` (only the initial and terminal phase differ). Therefore

`Q_(N,M)-1 >= K*(max(0, |S_N(h)|/N-2K/N))^2`.

Since `Q_(N,M)=o(log N)`, `K~c log N` and `K/N->0`, we obtain `S_N(h)/N->0` for every fixed nonzero integer h and EVERY N->infinity. Weyl's criterion proves equidistribution of `{16^n*(pi/16)}` and hence base-16 normality of pi. This proves the implication ONLY.

**Concrete useful settings:** beta=1/4, kappa=1/8, theta=2/3 work. Thus an original selected epoch collision bound `E_(A,1/4)=o(log A)` using only about `A^(1/4)` bins would suffice. The exact coefficients and beta need not be tied to a preferred prime; this is a deterministic carrier theorem.

**Strictly weaker finite requirement:** In an arbitrary A-point observation cloud, distribute A/m points at one fine A-cell in each of m coarse m-cells. Then `E_(A,m)=1` yet `E_(A,A)=A/m`, arbitrarily large if m=A^beta with beta<1. This construction is NOT a BBP source orbit; it proves only that the inequality at a coarse resolution cannot reconstruct the fine-scale condition.

## MSA-06. Source-specific prime frequencies remain nontrivial (COROLLARY of #474)

At each original epoch [A,2A), #474's simultaneous clean prime set has primes `p=8k+1` with `A/2<=k<A`, so `p>4A`. Our Fourier band has `1<=h<=m_A/2<=A/2`, hence `p` never divides h. The original phase decomposition `U_n=sum_p a_(p,n)/p + C_n` remains exact in this band; the complementary **selected real** `C_n` remains essential. Galois-averaged Ramanujan suppression alone cannot bound MSA-03's real selected `S_N(h)`.

## MSA-07. Same-four-pole coherent counterseed (PROVED NEGATIVE CONTROL)

Take the SAME source r(n), but different real initial seed `s*=1/5-pi/16`. The completed orbit is now the fixed point 1/5 under multiplication by 16, and its source recurrence states satisfy `U_n(s*)=1/5-T_n (mod 1)`. Since every dyadic `m_A<=A` is coprime to 5, the distance from 1/5 to the nearest m_A-bin boundary is at least `1/(5m_A)`. For n>=A, `T_n<1/(64A^2)<1/(5m_A)`; EVERY point of the hostile epoch therefore lies in the same mesh cell, with `E_(A,beta)=m_A`, not `o(log A)` for any beta>0. Same poles and Gamma sheet, different seed; source-forcing-only positivity is insufficient.

## Proof debt / claim ledger

- MSA-01, 02, 03: elementary **DISCLOSED paper lemmas**; no Lean certificate claimed.
- MSA-04: **DISCLOSED paper source-tail stability bound**, source identity/tail inherited from #474; no uniform energy saving obtained.
- MSA-05: **DISCLOSED conditional implication**. Premise `E_(A,beta)=o(log A)` for the actual original U_0=0 orbit is **UNVERIFIED / OPEN**, for EVERY beta>0. Pi normality remains OPEN.
- MSA-06: inherited #474 prime passport with new frequency-window bookkeeping; selected harmonic saving OPEN.
- MSA-07: **DISCLOSED negative control** excluding seed-uniform arguments, not a counterexample to original U_0=0.

Next discriminator: prove the original selected, real Archimedean near-pair estimate `P_(A,m_A)=o(A^2 log A/m_A)` for **any fixed beta>0** on ALL sufficiently large dyadic A, carrying all four signed source poles and the actual cofactor; or prove an alternative selected signed bound. Finite numerical receipts cannot discharge this quantifier.

**Classical antecedents:** Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001), 175–190, https://doi.org/10.1080/10586458.2001.10504441 . Lagarias, *On the Normality of Arithmetical Constants*, Experimental Mathematics 10 (2001), 355–368, https://doi.org/10.1080/10586458.2001.10504456 (cautions that general orbit-conjugacy mechanisms also occur in counterexamples). Fejer kernels and Weyl's criterion are classical; no external originality for those is claimed.

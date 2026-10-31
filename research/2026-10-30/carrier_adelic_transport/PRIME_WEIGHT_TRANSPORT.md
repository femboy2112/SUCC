# Exact prime-power transport of the authentic BBP source family

**Status: PROVED LOCAL, classical divisor reindexing specialized to the
source-authenticated common family.** This is not an Euler product for the
BBP coefficients, a new scholarly-priority claim, or a selected phase bound.

Write `c=(4,-2,-1,-1)`, `b=(7,4,3,2)`, `beta_i=b_i-u`, `|u|<1`, and

\[
r_u(n)=\sum_i\frac{c_i}{8n-\beta_i},\qquad
\Theta(s,z,u)=\sum_{n\ge1}z^n n^{-s}r_u(n).
\]

## 1. Prime-power weighting is an exact derivative observation

For `|z|<1` and every complex `s`,

\[
\boxed{-\partial_s\Theta(s,z,u)
=\sum_{p\ {\mathrm{prime}}}\sum_{k\ge1}(\log p)
\sum_{m\ge1}\frac{z^{p^k m}r_u(p^k m)}{(p^k m)^s}.}\tag{P1}
\]

The same formula holds at `z=1` when `Re(s)>-1`, with `Theta=D`.

**Proof.** Unique factorization gives
`log n=sum_(p^k|n) log p`, with each prime power divisor counted once.
Differentiating the defining series inserts `log n`; then reindex
`n=p^k m`. Absolute convergence follows from
`r_u(n)=O(n^-2)` uniformly on compact source-shift domains and

`sum_(p^k|n) log p=log n`.

For `|z|<1`, exponential decay dominates every bounded range of
`Re(s)` and every fixed logarithmic power. At `z=1`,
`sum n^(-Re(s)-2) log n` converges precisely in the claimed sufficient
half-plane. These arguments justify the derivative and rearrangement.

The inner weight is **log p**, not **log(p^k)=k log p**. Replacing it by
the latter already fails at `n=4`: the divisor contributions become
`log 2+log 4` instead of `log 4`.

## 2. Prime dilation changes the complete pole vector

For a complex pole vector `beta` with `max_i |beta_i|<8` and the fixed
weights `sum_i c_i=0`, define

\[
r_{\beta,c}(m)=\sum_i\frac{c_i}{8m-\beta_i},\qquad
\Theta_{\beta,c}(s,z)=\sum_{m\ge1}z^m m^{-s}r_{\beta,c}(m).
\]

If `q=p^k`, the exact arithmetic dilation is

\[
r_{\beta,c}(qm)=q^{-1}r_{\beta/q,c}(m).
\]

Thus P1 is equivalently

\[
\boxed{-\partial_s\Theta_{\beta,c}(s,z)
=\sum_{p,k\ge1}(\log p)\,(p^k)^{-s-1}
\Theta_{\beta/p^k,c}(s,z^{p^k}).}\tag{P2}
\]

This is a direct source-native transport: prime powers dilate the
arithmetic clock, scale every source pole, and replace `z` by `z^q`.
The prefactor contains the additional `q^-1` from the rational source,
besides the `q^-s` from the Dirichlet weight.

It is **not** a single common source shift. Such a shift would require
`b_i-v=(b_i-u)/q` for all i. Subtract two equations: the left pole
spacing is `b_i-b_j`, the right spacing `(b_i-b_j)/q`. Distinct poles
and `q>1` make that impossible. The enlarged pole-vector carrier is
therefore the correct closed domain of this operation.

## 3. Compatibility with the all-pole zeta transport

The residue coefficients from the spectral source dossier obey

`a_j(beta/q)=q^(-(j-1))a_j(beta)`.

At `z=1`, in `Re(s)>-1`, P1/P2 and the established zeta expansion give

\[
\boxed{-\partial_s D(s,u)
=\sum_{j\ge2}a_j(u)\zeta(s+j)
\sum_{p,k\ge1}\frac{\log p}{p^{k(s+j)}}
=-\sum_{j\ge2}a_j(u)\zeta'(s+j).}\tag{P3}
\]

The prime sum is used only at `Re(s+j)>1`, where it converges and
equals `-zeta'(s+j)/zeta(s+j)`. The sum of shifted zeta functions does
not itself acquire an Euler product. Beyond this domain, meromorphic
continuation of the final expression is legitimate; substitution
into the divergent raw prime sums is not.

At the authentic completed endpoint, P1 supplies the convergent
prime-weighted observation

\[
-\partial_s\Theta(0,1/16,0)
=\sum_{n\ge1}16^{-n}r_0(n)\log n.
\]

This uses the same original four-pole source whose value observation
is `Theta(0,1/16,0)=pi/16`. It measures logarithmic clock weighting.
It does not claim a physical phase or cancellation of `e(hU_N)`.
The initial seed remains separate. Moreover, the all-order flat
source countermodel changes this prime-weighted quantity while
preserving all polar residues: its source difference is negative
at every time after its fixed prefix, and `log n>0` for n>=2.

## 4. Authority and exact calibration

The underlying identities are unique factorization and ordinary
absolutely convergent Dirichlet-series rearrangement. The external
classical identity for zeta's logarithmic derivative comes from
differentiating its convergent Euler product; see NIST DLMF §25.2(iv),
<https://dlmf.nist.gov/25.2#iv>. No BBP Euler multiplicativity is used.

`prime_weight_transport_probe.py` checks exact formal coefficients of
the `log p` basis in finite sums by independent factorization and
prime-power enumeration, the full source dilation, incorrect
prime-power weights, and the impossible single-shift reduction.
These finite tests calibrate the algebra; convergence is proved above.

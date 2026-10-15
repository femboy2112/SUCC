# Part III — the actual half-density transport: reciprocal-cell dilation

**Branch:** research/zero-centered-residue-observers-2026-10-13. **RH PROVED: no.** This is an explicit isometric **semigroup** construction, not a completed source-derived Weil form or proof of the zero locations.

The important distinction from [Part II](ZERO_CENTERED_FUCC_PULLBACK.md): the sampling pullback T_q f(k)=f(qk) has operator norm q on the reciprocal-cell Hilbert space. But the geometrically meaningful dilation x->q*x acts by a completely different map on the integer-cell observer, and has a natural half-density normalization.

## ZCR-A01: exact discrete Archimedean dilation (PROVED LOCAL)

Let H=ell²(N,w), w_k=1/[k(k+1)], canonically identified with the functions constant on reciprocal cells I_k=(1/(k+1),1/k) in L²(0,1). Extend these functions by zero outside (0,1).

For q>=2, define (D_q f)(x)=f(qx). If x lies in I_k, then 1/x lies between k and k+1, so floor(1/(qx))=floor(k/q) almost everywhere. Therefore on integer-cell sequences:

  (D_q f)(k) = f(floor(k/q)) for k>=q;  0 for 1<=k<q.

This statement is exact at the level of cell-constant functions. It **is not** the integer address sampling T_q f(k)=f(qk) of Part II. Confusing them destroys the correct operator norm and source-map semantics.

## ZCR-A02: normalized isometry and non-surjectivity (PROVED LOCAL)

Each block of q consecutive cells indexed qj,...,q(j+1)-1 has total measure

  sum_(k=qj)^(q(j+1)-1) w_k
   = 1/(qj)-1/[q(j+1)]=w_j/q.

Therefore for every f in H,

  ||D_q f||² = ||f||²/q.

Define U_q=sqrt(q) D_q. Then **U_q* U_q = I** (adjoint in H), U_q U_r=U_(qr), and U_q is an isometry. It is **not surjective**, because every image vanishes in cells k<q and is constant on each q-cell block. A semigroup isometry is not a group-unitary action.

The exact adjoint is weighted block averaging, not point sampling:

  (D_q* f)(j)= 1/w_j sum_(k=qj)^(q(j+1)-1) w_k f(k).

Hence D_q*D_q=I/q. This explicitly separates lawful categorical transport from false unitary or sampling identifications.

## ZCR-A03: Mellin character and why 1/2 appears (PROVED LOCAL with classical Mellin analysis)

For complex s where its integral converges, L_s(f)=int_0^1 f(x)x^(s-1)dx. Substitution u=qx yields

  L_s(D_q f)=q^(-s)L_s(f),

and therefore

  **L_s(U_q f)=q^(1/2-s)L_s(f)**.

For integer s>=1 this holds on *each individual reciprocal cell* by an exact rational telescope:

  sum_(k=qj)^(q(j+1)-1) [k^(-s)-(k+1)^(-s)]/s
    = q^(-s)[j^(-s)-(j+1)^(-s)]/s.

Consequently the spectral scaling character is lambda_q(s)=q^(1/2-s), with

  **|lambda_q(s)|=1 precisely if Re(s)=1/2**.

This is the classical half-density/Mellin-Plancherel normalization expressed as an exact integer-cell source map. It is not a new physical explanation of the Riemann zeros. Most importantly: L_s is a *bounded* functional on H only for Re(s)>1/2. The unit-modulus boundary Re(s)=1/2 therefore does not automatically supply bounded eigenfunctionals or force a genuine arithmetic zero. The source-dependent zeta annihilation relation remains a separate condition.

The same algebra holds for any semigroup dilation q, prime or composite. **The half-density line is a representation-theoretic fact, not a way to distinguish authentic Euler prime data from fake sources.**

## ZCR-A04: exact controls and failures of naive intertwining

- Tested q=2,3,4,5,6,7, j=1..13, s=1..4. Every block-mass and block-Mellin identity is exact rational, with no floats.
- Tested independent, irregular rational finite-support source sequences against norm/moment covariance for q=2,3,5 and s=1,2,3.
- Negative control: for f={1:1,2:2,3:3}, D_2 f has value zero at k=1 while T_2 f(1)=f(2)=2. Thus these are inequivalent operators even though both arise from arithmetic scaling.
- Unitary-global-action reading REFUTED: U_q is an isometry into a proper image, not onto. A full bilateral dilation group on L²(R_+,dx) is a different carrier with different source/domain requirements.
- No nontrivial-zero coordinates are read, no analytic continuation is inferred from finite blocks, no full Gamma/poles/Weil form or RH theorem is established.

**Next verdict-changing problem:** Find a genuinely source-derived mapping between prime-jet FUCC, reciprocal-cell isometries, and completed Weil/Suzuki kernels that preserves multiplication, phases, test-function domains and all Archimedean terms. It must reject the fake-composite and matched non-Euler controls. Recovering the line Re(s)=1/2 from half-density normalization **without** a zero-selection theorem is only a coordinate/symmetry achievement.

**Classical context:** Mellin-Plancherel is Fourier-Plancherel after x=e^u. The half-density shift on L²(dx) is standard; e.g. J. Twamley and G. J. Milburn, *The Quantum Mellin transform* (2007), https://arxiv.org/abs/quant-ph/0702107. The exact reciprocal-cell realization is a useful SUCC representation, not a claim of priority for Mellin theory.

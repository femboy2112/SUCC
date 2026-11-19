# Companion: pulsed Fibonacci sheets and complementary 7/11 Jacobians

**2026-11-19; exact algebra, research-only.** This is a distinct operator from #667's quartic Fibonacci readout. Neither this operator nor its comparison to the source proves R0 or pi normality.

## Exact pulse geometry

Let a background sheet have value one, with the disturbance stored separately as u_t. On Z² let K_2=S_x+S_y be the two positive-axis shift operators. A unit impulse u_0=delta_(0,0) gives u_t(x,y)=binomial(t,x) for x,y>=0 and x+y=t, zero otherwise. The accumulated displayed sheet has values 1+binomial(x+y,x) on x+y<=t.

Projecting onto n=x+2y gives

$$
\sum_{x,y\ge0}\binom{x+y}{x}z^{x+2y}=\frac1{1-z-z^2}.
$$

The projected pulse response is exactly F_(n+1). The corresponding one-dimensional recurrence has the disturbance Jacobian K_F=S+S², where S is the one-site shift. Its derivative is genuinely the same linear operator, not just a diagrammatic analogy. The two-state Fibonacci companion A and T=Sym^4(A²) of #667 are alternative finite-dimensional representations, **not automatically the same full-sheet dynamics**.

## Fourier rotation and a real-field obstruction

On an N-site periodic sheet, diagonalize the cyclic shift S_N in the complex Fourier basis. The eigenvalues of K_F=S_N+S_N² are

$$
\lambda_j=\zeta_N^j+\zeta_N^{2j},\qquad |\lambda_j|\le2.
$$

Thus **16 is not a complex/real eigenvalue**, and there can be no nonzero time-independent linear readout ell satisfying ell*K_F=16ell over the real or complex fields. For the five-channel T the analogous real claim also fails, because chi_T(16)=-3³5³11·29 is nonzero. Any source-faithful coupling to actual BBP therefore needs a paid time-dependent/source-injected/nonlinear wrapped-phase mechanism; finite-field spectral matches alone are not it.

If N is even, the alternating sheet mode (1,-1,1,-1,...) is killed exactly by K_F because S acts by -1 and S² by +1. If N is odd, K_F is invertible over R: S invertible and I+S has no -1 eigenvalue. In fact |det K_F|=2 for N odd and det K_F=0 for N even. Over F_2, regardless of parity, the constant mode is killed because K_F*1=2*1=0. Thus a lawful moving observer cannot re-create that lost channel after advancement without having retained earlier information.

## A complementary p=7 finite-field bridge

For every N, K_F*1=2*1. At p=7, 16=2 (mod 7), so the **sheet's constant mode** is a genuine homogeneous 16-eigenchannel and its scalar period is ord_7(16)=3. At p=11 the sheet's constant mode 2 is not 16=5; by contrast #668's quartic **T** has the actual 11-eigenrow ell_11=(4,2,10,10,1), but no 16-eigenrow mod 7. The two observers therefore have complementary local finite-field relations:

- Sheet K_F constant mode matches scalar radix 16 mod 7, while a real eigenvalue 16 is impossible (spectral radius <=2).
- Quartic T has a primitive 16-eigenmode mod 11, and also mod 29 as a hostile control; the 11 fixed-eigenvalue lift to 11² fails.
- Original source-filter H(A^-1) of #666 has determinant 55=5*11, an independent literal-polynomial evaluation, not yet an intertwiner from the full BBP orbit to either observer.

This is a concrete role for the user's kernel-on-a-uniform-sheet and 2–3–5–7–11 examples. The modes are **not** independent stochastic clocks; their apparent matches are not evidence of signed real-orbit cancellation.

## Discriminating next probe

Build a source-labelled, chronological injection to the two observers, retain their p-power source principal parts and real cofactor phase, and compare **signed joint** cross-responses on held-out original-zero BBP shells. Require a mathematically authenticated source-to-real map, not just T or K_F spectral coincidence. Controls: wrong seed, sparse cold-shell orbit, p=29 match, mod-2 mode loss, and an even-sheet alternating input. The strongest open target remains a **uniform all-B lower wall norm or signed Weyl estimate**.

The accompanying stdlib sheet_probe.py contains exact finite controls for the periodic kernel, parity loss, p=7/p=11 multipliers, determinant and binomial-to-Fibonacci counts. These finite checks do not validate an asymptotic pi theorem.
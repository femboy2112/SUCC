# Reciprocal arctangent, Gaussian geometry and chiral phase

For real x>0, `atan(x)+atan(1/x)=+pi/2`. For x<0 the principal-branch value is `-pi/2`. At 0 the real `1/x` expression is undefined; the projective Möbius map `J([a:b])=[b:a]` remains well defined and exchanges 0 with infinity. Do not turn the piecewise real identity into a globally continuous lift of angular phase to real numbers: that would forget the integer winding/carry.

The Cayley coordinate `C(t)=(1+it)/(1-it)=exp(2i atan t)` gives the algebraically exact identity `C(1/t)=-C(t)^(-1)`. This is implemented on CP1 by the SU2 matrix `i sigma_x`, a 180-degree sphere rotation; it REVERSES orientation only on the chosen real projective equator. The circle angular 1-form `eta=2dt/(1+t²)` satisfies `J*eta=-eta`.

The original circle step `F_r(z)=e(r)z^16` is not J-equivariant with the same source label. The transported label is

`J F_r J = F_(1/2-r)`.

With original U0=0, dual U0=1/2, the exact unwrapped recurrence gives `U_n^dual = 1/2-U_n+8(16^n-1)/15`. Its conjugate Fourier phase is `S_N^dual(h)=(-1)^h conjugate(S_N(h))`. At the joint level, `mu_hat_joint(h,k)=(-1)^k S_N(h-k)/N`. At h=k this is always exactly (-1)^h, exhibiting maximum phase coupling, not two independent orthogonal witnesses. Any attempt to multiply or average the chiral witnesses as though independent is refuted.

The half-turn `1/2` changes the odd-denominator source clock to an even-denominator chiral sector; naive ×16 modulo2Q ceases to be a permutation. The full source-compatible repair is detailed in CATEGORICAL_GLUING.md.

## Why the arctan idea also gives an independent geometric calibration of pi

The **exact Gaussian integer factorization**

`(5+i)^4 = (476+480 i) = 2(1+i)(239+i)`

implies `4 atan(1/5) - atan(1/239) = pi/4` after checking the first-quadrant branch (the left angle is positive and below pi/2). Thus

`pi = 16 atan(1/5) - 4 atan(1/239)`.

For any truncation of alternating `atan(x)=x-x³/3+x⁵/5-...`, first-omitted-term inequalities give exact rational upper/lower intervals. This is an independent angular path/π oracle, useful for verifying BBP-source certificate bounds without importing decimal π digits. The identity is classical and the parameters `5,239` are NOT newly sourced from the BBP four-pole residues.

## Stronger NEW-to-SUCC payoff

The ORIGINAL four-pole BBP generating integral has precisely the relative angular/coboundary decomposition of PROOFS F12, which **derives the BBP-to-pi identity by original rational partial fractions**:

`(P(t)/(16-t^8))dt = (1/8)*2dt/(1+(t-1)^2) + dG(t)`;
`G(t)=(1/8)log((2-t²)/(t²-2t+2))`, `G(0)=G(1)=0`.

This is source-specific geometry, stronger than Machin alone. Do not mistake relative-period equality for phase-frequency equidistribution or a quantum tunneling law.

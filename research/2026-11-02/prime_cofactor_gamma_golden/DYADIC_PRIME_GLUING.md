# PGC-09 — dyadic prime-clean epoch COVERAGE and global ℓ² gluing

**2026-11-02 · New conditional source-selected theorem, no π-normality proof.**
This addendum repairs the originally proposed need for a direct prime-window covering of ALL checkpoint PAIRS. An exact norm inequality means coverage of well-chosen TIME BLOCKS suffices. It is more economical to attack one prime/cofactor interval per dyadic epoch than pairs spanning distant epochs.

## I. Classical arithmetic supplies prime-clean time coverage (PROVED)

For all sufficiently large dyadic integers \(A=2^j\), the prime number theorem in arithmetic progressions, at FIXED modulus 8, gives a prime \(p=8k+1\) with

\[
\boxed{\lceil A/2\rceil\le k\le A-1.}
\tag{DYG-01}
\]

Indeed primes \(p\equiv1\pmod8\) between \(4A+1\) and \(8A-7\) have cardinality asymptotic to \(A/\log A\to\infty\). (PNT-AP is an unconditional CLASSICAL theorem; e.g. https://math.colorado.edu/~rohi1040/expository/analytic.pdf, §9.) For this prime, the authentic PGC-01 original source clean interval \([k+1,4k]\) contains the ENTIRE dyadic epoch \([A,2A)\), since \(k+1\le A\) and \(4k\ge2A-1\).

Consequently the following *exact* source-cofactor description holds on EVERY sufficiently late complete dyadic epoch, for a suitable prime \(p\) depending on \(A\):

\[
\boxed{U_n=\frac{4\,16^{n-(k+1)}}p+B_{n-(k+1)},\quad
B_{n-(k+1)}\in\mathbb Z_{(p)},\quad A\le n<2A.}
\tag{DYG-02}
\]

This does NOT require RH or primes in unusually short intervals. It requires only a fixed-ratio interval in a fixed arithmetic progression. The prime's multiplicative order may still be small, and the cofactor is not independent.

## II. State the ONE source-selected local arithmetic estimate still missing (OPEN)

For a dyadic \(A\) and integer mesh \(2\le M\le A\), let

\[
u_j(A,M)=\#\big\{A\le n<2A:\lfloor M\{U_n\}\rfloor=j\big\},
\quad j=0,\ldots,M-1.
\]

In DYG-02 this is an explicit selected real histogram of the ORIGINAL p-primary plus COMPLETE complementary p-free cofactor (the p choice does not change U). The proposed local anti-conspiracy estimate is

\[
\boxed{\exists C<\infty,\ A_*:\quad
\sum_{j=0}^{M-1}u_j(A,M)^2
\le C\left(\frac{A^2}{M}+A\right)
\quad\forall\text{ dyadic }A\ge A_*,\ \forall\,2\le M\le A.}
\tag{OPEN-LOCAL-COLLISION}
\]

The \(+A\) diagonal floor is necessary when \(A\ll M\); even uniform independent points have a diagonal contribution. No original-source bound of this form has been proved. It is a more localized, source-attested replacement for a global all-pair bound.

## III. Exact Gamma finite-seam transport shifts at most ONE circle bin

Fix the parent source-selected square checkpoint \(N=L^2\), \(M=L+1\), with exact rational \(\alpha_N\). The earlier Gamma Seam identity is

\[
16^n\alpha_N=U_n+R_{n,N},\qquad
0\le R_{n,N}\le T_n\le\frac1{(8n+1)(8n+2)}<\frac1{64n^2}
\quad(1\le n\le N).
\]

For every \(n\ge M\), this displacement is strictly less than \(1/M\). Therefore the \(M\)-bin label of the finite rational completed phase \(\{16^n\alpha_N\}\) differs **cyclically by at most one neighboring bin** from the true original rational zero-seeded phase \(\{U_n\}\). No hard-bin boundary exemption or typicality assumption is needed; circle-wrap is allowed.

If \(v_j\) is the \(M\)-bin histogram of a subset of a late dyadic epoch, and \(u_j\) that of the FULL original U epoch, then componentwise

\[
v_j\le u_{j-1}+u_j+u_{j+1},
\quad
\boxed{\|v\|_{\ell^2}\le3\|u\|_{\ell^2}.}
\tag{DYG-03}
\]

Indices are cyclic mod M; Young's convolution inequality or Cauchy gives the bound. Partial terminal epochs are controlled by the FULL source epoch because occupancy is nonnegative.

## IV. The global checkpoint is a geometric sum of dyadic local certificates

Let \(A_0=2^{\lceil\log_2 M\rceil}\), so \(M\le A_0<2M\). The early prefix \(0\le n<A_0\) contributes at most \(A_0\) to the ℓ² histogram norm, regardless of phases. Partition remaining times \(n<N\) into successive dyadic epochs \([A,2A)\), \(A=A_0,2A_0,4A_0,\ldots\), with a possibly truncated final epoch.

Assume **OPEN-LOCAL-COLLISION** holds for all these large \(A\) with the global M. Apply DYG-03, the ℓ² triangle inequality, \(\sqrt{x+y}\le\sqrt x+\sqrt y\), and geometric sums \(\sum A\le2N\), \(\sum\sqrt A\le (1-2^{-1/2})^{-1}\sqrt N\). The rational completed-orbit histogram \(c_j\) then satisfies

\[
\boxed{
\left(\sum_{j<M}c_j^2\right)^{1/2}
\le 2M+\frac{6\sqrt C\,N}{\sqrt M}
+\frac{3\sqrt C}{1-2^{-1/2}}\sqrt N.
}
\tag{DYG-04}
\]

For \(N=L^2,M=L+1\), multiply by \(\sqrt M/N\) and square to obtain the explicit asymptotic consequence

\[
\boxed{\limsup_{L\to\infty}
\frac{M}{N^2}\sum_{j<M}c_j^2\le36C.}
\tag{DYG-05}
\]

PGC-05 bounds the original \(\mathscr Q_L\) by \((3+\pi^2/12)\) times this integer energy, and parent #471 GF-07 then gives base-16 π normality.

**DYG-06, rigorous conditional theorem:** the source-specific **local** estimate OPEN-LOCAL-COLLISION for all sufficiently large dyadic epochs and all \(2\le M\le A\), together with the already PROVED PGC-01 prime clean law and Gamma tail, would prove π normality in base 16. Only the local estimate is unproved. The cross-epoch offdiagonal pairs are **paid automatically** by deterministic ℓ² Minkowski gluing; we no longer need a separate prime covering for every ordered pair.

## V. Proof debt, controls and launch point

- **Proved classical:** p≡1 (mod8) coverage of each sufficiently large dyadic epoch from the fixed-modulus PNT-AP; ℓ² triangle and Fejér majorants.
- **Proved original-source:** p-clean recurrence, exact p-free cofactor and Gamma source tail give correct arithmetic realization of each epoch and one-bin transport.
- **OPEN:** one uniform selected real cofactor/prime-mixed local histogram estimate \(u(A,M)\), for all large dyadic A and growing meshes. Galois-averaged energy PGC-03 is not this estimate. p=257 has order 4 despite epoch coverage.
- **Hostile seed:** the same original four poles with real initial shift \(s=1/5-\pi/16\) has completed constant orbit; original source U phase tends a constant, so its late local histograms have ℓ² energy ≍\(A^2\), violating OPEN-LOCAL-COLLISION for growing M. Thus the sought estimate MUST genuinely use \(U_0=0\) and original real realization.
- **Falsifier:** find unbounded dyadic epochs with selected original \(u(A,M)^2\) substantially above \(A^2/M+A\), at meshes \(M\lesssim A\). Any proposed uniform local C is then false; a slower-growing admissible mesh, sparse-mesoscopic dissipation, or a different norm may still work.

This is a proof-producing **route reduction**, not a proof of the local premise. It retains complete p-free cofactor, real embedding, original four signed poles and causal zero seed. The strong exact \(\gamma\)-defect bound PGC-06 ensures Gamma transport without phase smearing; it contributes no missing local collision saving.

## VI. PGC-10 subsequently compresses the open all-M quantifier

See [SELF_SCALE_PRIME_COLLISION.md](SELF_SCALE_PRIME_COLLISION.md). A universal fine→coarse bin identity shows that a single uniform bound on the **self-resolution** original state histogram — A points [A,2A) in A equal bins — implies OPEN-LOCAL-COLLISION at all M≤A (with an absolute multiplicative constant). The open input to this dyadic gluing theorem is now equivalently one exact scalar per dyadic A, rather than a family of independently hypothesized meshes. This simplification does NOT supply the required all-A arithmetic estimate. Wrong completed real seed 1/5 has self-scale collision energy A, so the condition is indeed source-selected.

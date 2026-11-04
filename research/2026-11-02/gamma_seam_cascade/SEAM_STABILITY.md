# GS-02B — normalized full-hierarchy stability under a single finite Gamma cutoff

**2026-11-02; research-only additive corollary to PROOFS.md.** This sharpens the user's "truncate the infinite tails at two adjacent measured windows, then glue" proposal into a whole-hierarchy *quantitative* statement. It does not imply any asymptotic signed gap.

Fix the ORIGINAL four signed BBP poles, U_0=0. Let a>=1, b>a, N=b−a=2^J. Define the exact rational endpoint alpha_b=Σ_(k=1)^b16^(-k)r(k). For n=a+1,...,b compare the TWO source-attested unit phases

\[
z_n=e(hU_n), \qquad w_n=e(h16^n\alpha_b).
\]

Their exact rational exponents satisfy

\[
16^n\alpha_b-U_n=R_{n,b}
=\sum_{j=n+1}^b16^{n-j}r(j)\in[0,T_n].
\]

The authentic positive Gamma/Beta tail bound T_n<=1/[(8n+1)(8n+2)]<=1/(64n²) implies the **total** error

\[
\boxed{\varepsilon=\sum_{n=a+1}^b|z_n-w_n|
\le 2\pi|h|\sum_{n>a}T_n \le \frac{\pi|h|}{32a}.}
\]

For every dyadic block length L=2^j dividing N, let E_j(z) and E_j(w) be the sums of squared COMPLEX block amplitudes; let W_j(z),W_j(w) be the aggregate signed Haar squared differences. Because each block amplitude has modulus <=L, each wavelet difference has modulus <=2L, and block phase errors are summable over disjoint blocks, triangle inequality only for the **error**, not for the signed base amplitudes, proves

\[
\boxed{|E_j(z)-E_j(w)|\le2L\varepsilon,\qquad
|W_j(z)-W_j(w)|\le4L\varepsilon.}
\]

Consequently the normalized coherence C_j=E_j/(NL) and normalized Haar-loss increment \(\omega_j=W_j/(2NL)\) satisfy for EVERY j simultaneously

\[
\boxed{
|C_j(z)-C_j(w)|\le\frac{\pi|h|}{16aN},\qquad
|\omega_j(z)-\omega_j(w)|\le\frac{\pi|h|}{16aN}.}
\]

This is a uniform-in-level stability theorem: **a single finite rational original Gamma cutoff certifies the full late-window coherence cascade with O_h(1/(aN)) normalized transport error**, regardless of the number of measured points or of the window scale. It remains valid when the two adjacent windows are computed separately and exact boundary cocycles are used to glue them; the exponent chart of PROOFS.md agrees exactly on the overlap.

For any prefix m<=N, the two corresponding signed partial Fourier sums differ by at most \(\varepsilon\) in absolute value, i.e. at most \(\pi|h|/(32aN)\) after dividing by N.

**Important limitation:** the bounds control the *difference* of two fully specified phase fields. They do not bound either field's coherence or supply a positive lower bound on the real signed cross-window defect. Relative energy ratios W/E are also unstable when E is very small; use additive normalized C and omega certificates, never divide a bare interval by an unboundedly small energy without an independent lower enclosure. A coherent changed real seed under the same Gamma forcing remains a decisive counterexample to any seed-blind inference.

This result is derived from the source-authentic positive Gamma tail, an exact rational chart and classical triangle/Cauchy bounds. It is not an unconditional π-normality theorem, RH theorem, physical interference effect, or external priority claim.

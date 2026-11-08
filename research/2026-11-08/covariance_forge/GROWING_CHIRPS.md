# CF-R1: growing polynomial degree with an explicit budget

**PROVED PAPER corollary of CFS-7 and the pinned PE source theorem.**
This is a local-prime signed correlation estimate, not the full real Weyl
estimate. The fixed-degree CFS-7 proof is retained unchanged; here the degree
growth is paid explicitly. Natural logarithms are used.

Use the original source and deterministic p_A selector of PE9. Write
m_A=ord_(p_A)(16)>p_A^(1/3), and let eps_A be the exact interval-weight
distance between its complete clean cycles and [A,2A). For any integer
sequence d_A>=1 such that

\[
2^{d_A}=o(\log p_A),
\]

we have the unconditional local-source theorem

\[
\sup_{1\le h<p_A}\ \sup_{P\in\mathbb R[X],\ \deg P\le d_A}
\left|\frac1A\sum_{n=A}^{2A-1}
 e\bigl(h[U_n(0)]_{p_A}+P(n)\bigr)\right|\longrightarrow0.
\tag{R1}
\]

All polynomial coefficients may depend arbitrarily on the source history and
on A. Their magnitudes are unrestricted. The source prime is selected by its
arithmetic order, not by the observed real phase. For each fixed rational
wrong seed the local statement also survives eventually, so it does not
authenticate literal zero by itself.

**Proof with constants.** Let gamma>0 be the already imported BK exponent.
Choose any fixed c with 0<c<min(gamma,1/6). Suppress A and set
H=floor(sqrt(m/d)). The degree hypothesis gives d=O(log log p), while
m>p^(1/3). Hence eventually H>=2 and d(H-1)<m. Also

\[
\frac1H+\frac{d(H-1)}m+p^{-\gamma}
\le3\sqrt{d/m}+p^{-\gamma}\le p^{-c}
\]

for all sufficiently large p. The first inequality uses floor(x)>=x/2 for
x>=2; the last absorbs both constants and sqrt(d) into the strict exponent
margin. CFS-7 now gives, uniformly over all the displayed coefficients,

\[
\left|\mathbb E_{I_p} e(h[U_n]_p+P(n))\right|
\le 5^{1-2^{-d}}p^{-c/2^d}
\le5\exp\!\left(-c\frac{\log p}{2^d}\right).
\]

Transferring the identical unit-modulus sequence to the actual source epoch
costs at most eps_A. Thus the exact bound is

\[
\boxed{\quad\rho_A^{(d)}
=\varepsilon_A+5\exp\!\left(-c\frac{\log p_A}{2^{d_A}}\right)
\longrightarrow0.\quad}\tag{R2}
\]

The sufficiently-large threshold depends on c and the chosen degree sequence.
No numerical gamma or effective threshold is supplied. No all-epoch power
rate is inferred for eps_A. This completes the proof.

For example d_A=floor((1/2)log_2(log p_A)), eventually at least1, gives a
clean-cycle error at most5 exp(-c sqrt(log p_A)). Taking d_A approximately
log_2(log p_A) with only a bounded subtraction does **not** make this bound
vanish, and is not licensed by R1.

## The precise learning premise it would support

For a finite predictor v_n=sum_(j=1)^M c_j e(P_j(n)), with each deg P_j<=d_A,
let K_A=sum_j|c_j|. Uniformity and the exact factorization ab=e(hU) imply

\[
|W_A(h;0)|\le \rho_A^{(d)}K_A+
 \mathbb E_{[A,2A)}|b_n-v_n|.\tag{R3}
\]

The phases, coefficients and menu may be learned adaptively; uniformity
already covers the selected predictor. To prove the authentic Weyl gate by
this route one must still construct, for every fixed h!=0, original-source
predictors satisfying BOTH rho_A^(d)K_A->0 and the displayed error->0.
That premise is **OPEN and strictly stronger than cancellation alone**.
It is not established by a finite fit, observability, complete source
authentication, a low parameter count, or memory retention.

The terminal-support shadows have the same local clock and W_A->1. They
therefore force K_A>=(|W_A|-error)_+/rho_A^(d) for every such fit. Arbitrary
interpolation by degree A-1 escapes the proved degree budget; it supplies no
cheap certificate. The signed covariance route itself remains available even
if this restricted predictor class turns out to be inadequate.

Provenance: root corollary of the spectral bearing's CFS-7, whose finite
differencing proof was checked by the arithmetic and crucible bearings.
This is a same-model, different-method audit, not external refereeing or a
Lean proof. **Pi normality: OPEN. RH: OPEN.**

# Anchored causal Fourier front: exact reduction and unpaid estimate

Source: pinned main's `selected_orbit`, `renorm_transport/PROOFS.md`,
`main_xx_forge/front_c/PROOFS.md`, #520 seed-charge classification,
#542 APH-01, and #529 AT1–AT7. These are read-only dependencies.
The following is a classical signed decomposition applied to the original
source, not a new upper bound on its correlations.

Fix h≠0 and write z_n=e(hU_n(0)), n in [A,2A). Define
\[
C_A(d;h)=\frac1A\sum_{n=A}^{2A-1-d}
e\bigl(h(U_{n+d}(0)-U_n(0))\bigr).
\]
Its exact source form is
\[
C_A(d;h)=\frac1A\sum_n
e\bigl(h(16^d-1)U_n(0)+hS_d(n)\bigr).
\tag{A1}
\]
Keep the chronological source sum and all signs. Dividing by its forcing
factor leaves a higher-frequency selected character; it does not create a
martingale difference. Compensating by z_n(16^dh) instead would erase the
seed and turn the observable into a known forcing phase.

For 1≤H≤A, extend z by zero outside the epoch. Summing over all A+H−1
windows gives the exact Gram identity
\[
\sum_m\left|\sum_{j=0}^{H-1}z_{m-j}\right|^2
=HA+2\sum_{d=1}^{H-1}(H-d)\operatorname{Re}(A C_A(d;h)).
\]
Each original z appears in H windows. Cauchy–Schwarz therefore gives
\[
|c_A(h)|^2\le\frac{A+H-1}{AH}
\left[1+2\sum_{d=1}^{H-1}(1-d/H)\operatorname{Re}C_A(d;h)\right].
\tag{A2}
\]
This proof retains signed cross terms; replacing them with local positive
pin energies loses the required information. A sufficient premise is
H=H(A)→∞, H=o(A), and the bracketed weighted correlation sum=o(H), for
each fixed h. That premise is **OPEN for literal zero** and no lower theorem
debt than the existing signed-lag route has been established here.

On the coherent same-forcing seed s*=−π/16, U_n=−T_n. For fixed d,
C_A(d;h)→1; uniformly for d≤H=o(A), positivity and the tail bound give
C_A(d;h)=(A−d)/A+O_h(A^−2). The weighted sum is of order H. Memory of
closed source-corrected loops is identical on this control and cannot pay
the missing premise. The arithmetic AR theorem gives a stronger **finite
authentication** control with rational, epoch-dependent seeds and the
original finite carry transcript preserved.

## Four attempted mechanisms and their exact failure points

1. **Martingale subtraction from learned source beliefs.** Conditional
   expectations require an explicit probability law on candidate seeds.
   Under Haar seed the phases have ensemble cancellation, but a point s=0
   has measure zero. L2 or almost-sure bounds do not bound that point.
   Under the singleton prior at zero there is no independent randomness;
   conditional centering removes the whole known signal and leaves no
   estimate on its original mean. No original-source martingale law was
   derived.
2. **Adaptive phase alignment.** Measuring z and multiplying by conjugate(z)
   makes every response 1, even for the cancelling two-point law {0,1/2}
   at h=1 (or any odd h).
   This changes the observable. A causal feedback protocol must retain its
   phase settings and undo their action before it can estimate the native
   Weyl mean. An unbiased lock-in estimates that mean; it does not make it
   small. #543's variance result survives with that distinction.
3. **Source telescoping and Gamma/BV weights.** Main front C proves the exact
   duality between bounded-variation weights and maximal partial Weyl sums.
   The multiplier a_n=e(hS_d(n)) has no independently proved source-selective
   cancellation after coupling to e(h(16^d−1)U_n). Summation by parts and
   analytic smoothing transport the unpaid estimate. #496's boundary limit
   remains an assumption, not a consequence of finite coefficients.
4. **Learned partitions with positive local energies.** Spectral SP-4 proves
   E(refinement)−E(coarsening) is a conditional variance. It is nonnegative
   both on Haar-like cancellation and coherent controls. The global mean
   still includes all inter-cell signed correlations; no sign inference
   from the increment is valid.

## Arithmetic alternative: a coverage obligation now discharged

The following conditional route makes the extra debt visible. Partition
all but R_A indices of [A,2A) into disjoint complete clean prime-clock blocks
I. On each block choose an original newborn prime p_I>5 not dividing h,
with length m_I=ord_(p_I)(16). Require I to be consecutive and contained
in [n_(p_I),n'_(p_I)), between its first pole birth and next pole occurrence,
so AT3–AT5 provide a nonzero simple residue and a full clean coset. Write
\(a_n=e([hU_n]_{p_I})\), \(b_n=e(hU_n-[hU_n]_{p_I})\).
AT5 and the elementary covariance identity give
\[
|c_A(h)|\le \frac{R_A}{A}+
\sum_I\frac{m_I}{A}
\left(\frac{\sqrt{p_I}}{m_I}
+|\mathbb E_I(a b)-\mathbb E_I a\,\mathbb E_I b|\right).
\tag{A3}
\]
Proof: split the sum by the disjoint blocks, bound each by AT6, and bound
uncovered unit phases by their count. Thus sublinear uncovered size plus
vanishing weighted Gauss and covariance costs is sufficient. This elementary
Gauss-only version is not established. A stronger finite-field input now
discharges coverage and local cancellation by a different, single-prime route:
`arithmetic/PRIME_EPOCH_THEOREM.md` PE1–PE9 uses the exact clean interval
for p=1 mod8, elementary order counting, fixed-modulus PNT/AP and
Bourgain–Konyagin. Its deterministic p_A~4A supplies a complete-cycle epoch
of length (p_A−1)/4~A. Transferring normalized averages to [A,2A) costs o(1).
Consequently the selected p_A-principal character cancels on **every** large
epoch. The real phase equals that character times its complementary factor;
PE11 proves the original Weyl mean equals their bilinear covariance plus o(1).
**That original-source covariance bound remains OPEN.**
AR1 shows that even preserving all original local prime characters on an
epoch is insufficient if unseen complementary denominator support is allowed.
For the true zero source that support is prescribed, which is exactly the
constraint a successful next proof must use.

## Verdict

A1–A3 are complete conditional/algebraic statements, inherited classical
tools with exact source transport. PE1–PE9 add an unconditional all-epoch
local-prime cancellation theorem. This pays actual coverage and marginal
debts of #529, while leaving the real signed covariance unchanged as an open
equivalent gate. The finite arithmetic/history obstruction and continuum
sensor cost explain why learning and local cancellation alone cannot supply
that estimate. No full real-circle signed upper saving, LS or H2* was proved.

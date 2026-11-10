# Independent audit record

**PE9/PE14:** no substantive defect found. The scope of imported BK and PNT/AP,
the pole chronology, complete local cycles, bad-order counting, overlap error,
and the complex step `|W−1|²≤2(1−Re W)` were checked. A moving local prime is
not the complete real character, and epoch-dependent seeds are not one fixed
nonnormal rational seed. The primary BK PDF was freshly read, not accepted only
from the previous agent's report.

**Root fixed-point interval instrument:** no substantive defect found. The
phase reduction is to the nearest quarter turn, so |x|≤π/4<1. Degree-26 cosine
and degree-27 sine Horner evaluation, with outward operations and errors 1/28!
and 1/29!, enclose the true phases. Common-denominator recurrence, independent
modular power sums, principal parts with unreduced denominators, AR center,
shadow phase evolution, and bilinear covariance were checked. The positive
prefix inequality checks exactly whether a perturbed lift crosses an integer.
The independent containment oracle's final hashes cover the later numerator
type check and summary-output edit; no interval-core change occurred.

**Sparse probe:** normalized DFT and the −k index are correct. Top upper energy
endpoints give an upper bound on every s-support's captured energy; top lower
endpoints give a lower bound on the maximum. The resulting residual interval
remains valid when coefficient ranking is uncertain. No sparse model is assumed
true merely because the computation can fit one.

**CFS-7 polynomial temporal chirps:** independent derivation found no defect.
Starting with `H sum F = sum_n sum_(j<H)F(n+j)`, finite-support Cauchy–Schwarz
produces the stated weighted correlation identity with m+H−1 outer positions.
For H≤m it yields `x_j²≤2/H+2x_(j+1)`. Writing t=1/H and z_j=x_j+t gives
`z_j²≤2x_(j+1)+4t+t²≤5z_(j+1)`, since 0≤t≤1 and x_(j+1)≥0. Iteration gives
the factor `5^(2^d−1)` exactly. Repeated positive-shift differences have support
`[0,m−sum h_i)`, not a cyclic wrap. On that support the source coefficient is
`xi product(g^h_i−1)`, nonzero because 0<h_i<m=ord_p(g). A degree-d polynomial
becomes constant after d differences. BK bounds the complete cycle, and at
most d(H−1) omitted endpoints cost that amount divided by m. Fixed d and
H=floor(sqrt(m)) satisfy the hypotheses eventually; translating to another
complete cycle preserves polynomial degree and the bound is uniform in all
real coefficients. The final interval gluing is therefore legitimate. This
does not justify unrestricted growing polynomial degree or arbitrary history phases.

**Controlled growing-degree corollary:** the root's subsequent extension is
sound when d_A≥1 and `2^d_A=o(log p_A)`. Set H=floor(sqrt(m_A/d_A)). Eventually
H≥sqrt(m_A/d_A)/2, so the terminal bracket is at most
`3sqrt(d_A/m_A)+p_A^(−gamma)`. Also d_A<m_A makes the support condition valid.
The hypothesis implies d_A=O(loglog p_A), while m_A>p_A^(1/3); consequently the
bracket is eventually at most p_A^(−c) for every fixed
`0<c<min(gamma,1/6)`. Taking the 2^d_A-th root gives the uniform bound
`5 exp(−c log p_A / 2^d_A)→0`, plus the same epoch-gluing error. Uniformity in
all real polynomial coefficients and across shifted cycles is retained. Merely
subtracting a bounded number from log2(log p_A) does not make this bound vanish.

**New sharp scope correction:** finite-memory inability to authenticate zero
was rejected as an overstatement. Exact zero, complete denominator support
plus all its local principal parts, or sufficiently sharp bounded-height data
can isolate the seed. The new growing-carry counterfeits omit those extra
conditions. Their carry prefix is explicitly J_A=floor((A−1)/5); they do not
cover every possible memory-growth schedule.

All this is paper/source review plus finite exact or interval computation.
No new Lean certificate or independent scholarly referee is claimed. The full
literal-zero complementary covariance, π normality and RH remain OPEN.

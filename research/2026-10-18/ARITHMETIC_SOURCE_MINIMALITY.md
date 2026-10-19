# Arbitrarily late arithmetic counterfeits and the trace identification boundary

**Date:** 2026-10-18. **Authority:** full elementary proofs below, exact rational
finite checks, classical analytic continuation of the ordinary zeta function.
**Status:** PROVED LOCAL within the stated source class; academic priority
UNVERIFIED. This is an arithmetic source-identification obstruction, not an
obstruction to proving RH. No zero ordinates are construction inputs.

## 1. Audited source state and verdict

The audit read the actual remote branch blobs, rather than assuming their PR
descriptions were theorems already integrated in main:

| Research lane / PR | Inspected head | Mathematical dependency retained |
|---|---|---|
| Prime jets, #157 | `1bcebd265ee78ae6faef5995467df6c1d85b42cf` | Global uniform dilation counting (UDC) is explicitly equivalent to the affine braid; not derived from jets |
| Source minimality, #162 | `3512c24bd582f8572d98bc0728d2cf947b7e7d2f` | All prime-power quotients, or the full additive renewal identity, are independent global source hypotheses |
| Orbit-clock genesis, #165 | `dea8b7f982fd3eb2361ccd5a12d360bcadfa3689` | Free rooted orbit gives set factors; continuous factors require disjoint residue closures; faithful reconstruction further requires point separation |
| Connes/orientation, #169 | `64aa0810d9016c9c6948034d0543424f46db011e` | Local coefficients, positive multiplicative kernels and normalized cylinders do not identify the completed signed Weil distribution |
| Mobius index at infinity, #176 | `a17197697c0ea0259592500b233419fbedf691cf` | MII-09 already proves contact/character nonidentification; MII-11/12 give a genuine finite-adele additive test/Fourier map, not the completed idelic trace |

The first three papers already state the load-bearing infinite quantifiers
honestly. Rebranding UDC as a local rank law would lose that honesty. Their
existing finite shadows and the fixed `9/2,35/11` Beurling example leave a
useful question: can **one model simultaneously** preserve an arbitrarily
long exact prefix and the strong global analytic summaries? The answer below
is yes, with the exact first failing braid supplied in advance.

The inherited MOG manuscript contains one concrete algebraic error: MOG-08 states the
eigenvalues of its two-dimensional compression as the full operator spectral
endpoints. Section 5 supplies the correction. Its positivity conclusion survives.
The erroneous sentence was introduced by commit
`04a5173b6809e841a441aea0815cec5983a7cab0`; the inspected MOG file at both
the #169 and #176 heads has git blob `4323b0e610f34ea44613ea892f94cdbc418e479e`.
It is an inherited error, not an assertion that PR #176 originated it.

## 2. The arbitrary-horizon theorem (ASM-01)

Let a Beurling source mean a locally finite increasing sequence of primitive
real values greater than one, with finite words multiplied in a free
commutative monoid. Its counting measure counts **source words**, so collisions
cannot be silently erased. The ordinary primes define the calibration source.

**Theorem.** For every finite real horizon `H >= 1`, there is a rational,
collision-free Beurling source `B` with all of the following properties:

1. Its primitive values, prime-power jet measure, counting measure and all
   bounded word operations whose values stay in `[1,H]` agree exactly with
   ordinary arithmetic.
2. The first additive-real cell is `[1,2]`, of ordinary Lebesgue length one.
3. Its generalized integer count satisfies `N_B(X)=X+O(log^2 X)`; its prime
   count differs from the ordinary prime count by at most two everywhere.
4. In `Re(s)>0`, its meromorphic zeta function is `zeta_B(s)=zeta(s) F(s)`
   with `F` holomorphic and nowhere zero and `F(1)=1`. In particular its pole
   at one has the same residue and its critical-strip zero divisor, including
   multiplicity, is identical to that of zeta.
5. Its rank successor and multiplication by the unchanged generator two fail
   the affine braid. The first specified witness is an exact defect `-1`.

**Construction.** Choose ordinary primes `p>max(H,2)` and `q>p^2`, and put

\[
A=p^2-p+1,\qquad
a=\frac{p^2}{p-1},\qquad
b=\frac{qA}{q+p(p-1)}.
\]

Replace the primitive generators `p,q` by `a,b`, retaining every other
ordinary prime. Thus the word values are

\[
B=\{m a^j b^k:m\in\mathbb N_{>0},\ (m,pq)=1,\ j,k\in\mathbb N_0\}.
\]

**Collision-free source.** The rational valuations at the deleted places give

\[
v_p(a)=2,\quad v_q(a)=0,\quad v_p(b)=0,\quad v_q(b)=1.
\]

Indeed `A=1 mod p`, the denominator of `b` is `q mod p`, and `q>A` divides
neither `A` nor `p(p-1)`. Equality of two word values first forces the same
`j,k` by their `p,q` valuations, and cancellation then forces the same `m`.
Every atom has unit mass globally, not just in the executed finite sample.

**Prefix and first failure.** We have `a=p+1+1/(p-1)>p+1`. The inequality
`b>p+1` is equivalent to `q(p-2)>p^2-1`, which follows from `q>p^2` and
`p>=3`. Therefore

\[
B\cap[1,p+1]=\{1,2,\ldots,p-1,p+1\}.
\]

This proves the exact prefix statement and first cell calibration. The atom
at `p` is absent; the full additive renewal identity already has residual
`nu_B({p})-nu_B({p-1})=-1`. Let `r` be increasing atomic rank and `S` its
successor, and let `V_2 x=2x`. For `x=(p-1)/2`, `Sx=x+1`, and

\[
r(V_2Sx)-r(V_2x)-r(2)=r(p+1)-r(p-1)-2=p-(p-1)-2=-1.
\]

Thus `V_2 S != S^2 V_2` even though every earlier bounded observation can be
made exact. This is a concrete failing source rectangle, not just a failure
to prove a universal assertion.

**Density with an effective elementary error bound.** Write

\[
C=(1-p^{-1})(1-q^{-1}),\qquad
R(y)=\lfloor y\rfloor-\lfloor y/p\rfloor-\lfloor y/q\rfloor
       +\lfloor y/(pq)\rfloor.
\]

Then `R(y)` counts positive integers at most `y` coprime to `pq`, and
`|R(y)-Cy|<=2`. Direct substitution gives

\[
(1-a^{-1})(1-b^{-1})=C,
\qquad N_B(X)=\sum_{a^j b^k\le X}R(X/(a^j b^k)).
\]

For `X>=1`, let `J=max{j:a^j<=X}` and `K=max{k:b^k<=X}`. The finite
inclusion-exclusion error is at most `2(J+1)(K+1)`. To compare the main term
with the entire geometric sum `X`, separate the omitted tail by `j<=J` and
`j>J`. In the former part, let `K_j=max{k:b^k<=X/a^j}`. Then

\[
X\sum_{k>K_j}a^{-j}b^{-k}<\frac1{1-b^{-1}},\qquad
X\sum_{j>J,k\ge0}a^{-j}b^{-k}
<\frac1{(1-a^{-1})(1-b^{-1})}.
\]

Multiplication by `C=(1-a^{-1})(1-b^{-1})` proves the explicit bound

\[
\boxed{|N_B(X)-X|\le
2(J+1)(K+1)+(J+1)(1-a^{-1})+1.}
\]

This is `O(log^2 X)` for the fixed source and proves density one without
using numerical asymptotics or zeta residues. Exactly two primitive values
were removed and two added, so `|pi_B(X)-pi(X)|<=2`, transferring the ordinary
prime number theorem whenever that classical result is supplied.

**Analytic summaries.** Absolute convergence on `Re(s)>1` gives

\[
F(s)=\frac{(1-p^{-s})(1-q^{-s})}{(1-a^{-s})(1-b^{-s})},
\qquad \zeta_B(s)=\zeta(s)F(s).
\]

For any `u>1`, `|u^{-s}|<1` on `Re(s)>0`, so every factor `1-u^{-s}` is
holomorphic and nowhere zero there. The density identity gives `F(1)=1`.
Ordinary zeta continuation now proves the asserted meromorphic continuation,
residue and zero-divisor equality, without reading any zero locations. QED.

**Executed exact instance:** for `H=100`, the constructor selected `p=101`,
`q=10211`, `a=10201/100`, `b=103141311/20311`. It returned `N_B(100)=100`,
`N_B(101)=100`, and the braid rectangle `x=50`, `Sx=51`,
`r(100)=100`, `r(102)=101`, giving defect `101-100-2=-1`.

**Boundary.** The theorem does not preserve the full completed functional
equation, the canonical real Gamma source, the authentic all-place Tate
structure or the complete signed Weil distribution. Those are stronger
source data. Identical zeros in one domain do not identify those data.

## 3. Finite protocol corollary and precise scope (ASM-02)

A *bounded spectral observation* is any deterministic function of the
primitive/word/jet source restricted to `[1,H]` for some finite `H`. It may
perform exact finite convolutions, factor-word comparisons, successor tests
whose required endpoints stay in the horizon, or derived finite matrices.

**Corollary.** No adaptive protocol which terminates on ordinary arithmetic
after finitely many bounded spectral observations can soundly conclude,
among all sources in Theorem ASM-01, that the source has the global affine
braid, even if it is additionally supplied the exact facts `N(X)=X+O(log^2 X)`,
the ordinary PNT, residue one, first-cell calibration, and the zeta
critical-strip zero divisor.

**Proof.** Run the terminating protocol on ordinary arithmetic. Let `H` bound
the finitely many queried horizons on that run. Select the countermodel from
ASM-01 beyond `H`. Induction on the adaptive query number shows the same
answers force the same next query and eventual verdict; every supplied
analytic summary also holds for this countermodel. Its explicitly failing
braid makes a positive verdict unsound. QED.

This conclusion concerns finite measurements in a stated query language.
A finite **proof of a universal source invariant** is not a bounded spectral
measurement. Such a proof can establish the braid or renewal law. We do not
claim undecidability, a barrier to mathematics, or inability to distinguish
each counterfeit eventually: the next decisive test is its omitted `p` atom
or the displayed `V_2` rectangle. For randomized protocols, the elementary
argument applies to each fixed realized finite random tape; no statistical
error lower bound is asserted here.

## 4. Other controls and axiom minimality

The inherited #162 procyclic shadow is logically separate: for finite queried
periods `m_i`, choose `e=max(1,max_i v_2(m_i))`. The infinite pointed group

\[
\mathbb Z/2^e\mathbb Z\ \times\prod_{\ell\ \mathrm{odd\ prime}}\mathbb Z_\ell
\]

has every simple prime quotient and every queried cyclic quotient, with all
the same reduction maps, but no `C_(2^(e+1))`. It does not refute a globally
proved carry-lift schema. The new finite helper records the omitted period.

Other mandatory controls are independently executed: adding primitive six
beside two and three creates multiplicity two at six; the scale `n->n^2`
preserves multiplicative ranks and every affine braid while changing the
first additive-real cell length to three. These rule out conflating free
labels with authentic primes, or ordered rank with Archimedean normalization.

No genuinely weaker source-only sufficient axiom has been proved in this
round. The alternatives remain explicitly quantified:

- Global UDC / braid reconstructs multiplicative rank, leaving one positive
  power-scale gauge; an independent real normalization removes that gauge.
- Full `nu=delta_1+(x->x+1)_*nu` on the independently supplied positive real
  half-line forces the integer comb by compact-support telescoping.
- All authenticated finite prime-power factors, their lawful bonding maps
  and separation reconstruct the appropriate procyclic carrier.

Calling any of these a single equation or a constructor does not eliminate
its universal source premise. Their sufficiency and independence statements
already belong to the audited branches; ASM-01 adds a uniform adverse family
simultaneously preserving exact prefixes and strong analytic summaries.

## 5. Operator audit and the missing contact (ASM-03, ASM-04)

For the literal isometry `V_p e_n=e_(pn)`, set
`A_p=(I-p^(-1/2)V_p)^*(I-p^(-1/2)V_p)`. Its compression to `e_1,e_p` is

\[
\begin{pmatrix}1+p^{-1}&-p^{-1/2}\\-p^{-1/2}&1+p^{-1}\end{pmatrix}.
\]

**Correction to inherited MOG-08 (origin `04a5173`, present in #169 and #176):** its eigenvalues are
`1+p^(-1) +/- p^(-1/2)`, not `(1 +/- p^(-1/2))^2`. The latter are the
endpoints of the full half-line operator spectrum. An exact rational receipt
is the compression characteristic polynomial

\[
t^2-2(1+p^{-1})t+(1+p^{-1})^2-p^{-1},
\]

whose constant coefficient differs from `(1-p^(-1))^2`. Both compressed
eigenvalues remain strictly positive. The correction is additive here; the
archived original is untouched.

**Contact nonidentification, a classical distribution observation already
used in #176 MII-09.** Work in
the additive log coordinate, with `f^*(t)=conj(f(-t))`. For any Hermitian
distribution `W` on smooth compactly supported tests and any real `c`, put
`W_c=W+c delta_0`. All tests supported away from the identity have identical
pairings with `W_c` and `W`; their off-identity prime impulses and reciprocal
symmetry agree whenever `W` is reciprocal. But

\[
W_c(f*f^*)=W(f*f^*)+c\|f\|_{L^2}^2.
\]

For any fixed nonzero admissible `f`, choosing `c` sufficiently negative
makes this value negative. Thus even **complete off-identity matching** and
orientation do not authenticate the contact or positivity. This does not
produce a negative witness for the authentic Weil form: its contact is fixed
by the canonical normalization and may not be changed. A finite sieve or
Hilbert Gram construction must prove that precise normalization, the poles,
Gamma contribution, and test transport, as well as the off-identity weights.

Connes' local trace theorem includes a Fourier-normalized distributional
extension at the identity. Connes–Consani's Theorem 1 concerns tests supported
in `[2^(-1/2),2^(1/2)]` with the specified Fourier vanishing conditions; it
does not supply positivity for all radii. These primary results support the
need for a source-specific trace comparison, not a promotion of the auxiliary
positive kernels to the original signed form.

**Counting-state correction to #176 MII-06 (ASM-05).** The functional
`tau_N(T)=Tr(P_N T P_N)/N` is a normal state on `B(ell^2(N))`; its restriction
to the finite corner is tracial. It is not a trace on the full algebra, so
the manuscript's phrase "finite tracial states" must be read as referring
only to those corners. In fact for the literal multiplier `V_2`,

\[
\tau_N(V_2^*V_2)=1,\qquad
\tau_N(V_2V_2^*)=\lfloor N/2\rfloor/N\longrightarrow\tfrac12.
\]

Consequently no weak-* cluster state of this sequence is tracial on the
full bounded-operator algebra. The manuscript's conclusion that every such
cluster state is singular/non-normal remains valid: all fixed rank-one
diagonal projections have limiting weight zero. These are two different
properties. This correction reinforces the need to specify a trace domain
and regularization before identifying counting-state limits with a Connes
trace. It does not invalidate the finite CRT/Haar or sieve projection proofs.

## 6. Validation, provenance and academic comparison

The new implementation uses `Fraction` arithmetic only. Its counting oracle
uses inclusion-exclusion; the tests independently convolve finite geometric
word series, preserving multiplicities. Unrelated `p,q` holdouts test both
nearby and distant choices. Positive, counterfeit-six, incomplete-clock,
wrong-scale, wrong-domain, budget, and wrong-compression controls run.

Observed local baseline:

- Current branch `test_unit_prime_succ.py`: **10/10 passed**.
- Exact #165 arithmetic dependency closure, extracted to a temporary isolated
  package at `dea8b7f982fd3eb2361ccd5a12d360bcadfa3689`: **108/108 passed**.
  This included prime jets, profinite index, source minimality, carry/clock
  compiler, orbit clocks, incidence inversion and topological clock factors.
  It is not a claim about that remote branch's entire repository CI.
- New `python -m unittest discover -s tests -p
  'test_arithmetic_source_minimality.py' -v`: **10/10 passed**.

Finite tests validate the executable instances. The universal source and
analytic conclusions have the proofs above; there is no Lean claim here.

| Claim | Closest precedent | Difference and authority |
|---|---|---|
| ASM-01 late rational family | Classical Beurling arithmetic; #162's fixed paired mutant | Uniform arbitrary horizon, explicit next braid defect and effective `O(log^2 X)` count bound; PROVED LOCAL; priority UNVERIFIED |
| ASM-02 adaptive observation obstruction | Elementary indistinguishability / finite transcript argument | Adds the simultaneously preserved analytic summaries; PROVED LOCAL in stated query language |
| Capped procyclic shadow | Classical supernatural classification; #162 | Rechecked executable witness; CLASSICAL / inherited |
| ASM-03 compression correction | Elementary spectral calculation | Fixes a specific archived manuscript error; PROVED LOCAL |
| ASM-04 contact freedom | Classical distribution theory | Explicit explanation of the missing identification in the SUCC trace route; CLASSICAL, not a new RH theorem |
| ASM-05 counting states are nontracial on the full operator algebra | Elementary isometry/range-projection calculation | Corrects #176 MII-06's terminology while preserving its non-normality conclusion; CLASSICAL |

Primary references, checked 2026-10-18:

1. A. Beurling, *Analyse de la loi asymptotique de la distribution des nombres
   premiers generalises. I*, Acta Math. **68** (1937), 255–291,
   [DOI 10.1007/BF02546666](https://doi.org/10.1007/BF02546666).
   Publisher metadata was verified; the original full-text download met a
   security wall. No uninspected theorem from that paper is used in the proof.
2. A. Connes, *Trace formula in noncommutative geometry and the zeros of the
   Riemann zeta function*, [arXiv:math/9811068](https://arxiv.org/html/math/9811068v1),
   especially the local trace formula and its normalized distribution at one.
3. A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean
   place*, [arXiv:2006.13771](https://arxiv.org/html/2006.13771v1), introduction,
   Theorem 1 and Appendix E on signs/normalizations. Theorem 1's support and
   vanishing hypotheses are retained above.

**Verdict-changing next task:** supply an independently justified global
source invariant that excludes ASM-01's rational family, or prove the full
source-preserving test transport including canonical identity contact. More
prefixes or another positive auxiliary Gram matrix cannot settle that gap.

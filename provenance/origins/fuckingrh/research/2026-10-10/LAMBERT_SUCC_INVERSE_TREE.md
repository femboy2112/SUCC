# Lambert W as a SUCC inverse chart and rooted-tree realization

**Date:** 2026-10-10. **RH remains OPEN.** Parent \`aletheia/succ-shadow-gamma-selection-2026-10-10\` at \`284f39a63bf1e1b9a87ef988738676e22215aec6\`. Main remains unchanged. This work does not use zeta zeros or a completed Weil-form Gram.

**User's hypothesis (kept distinct from our construction):** Lambert W seems to strip a global, complicated exponential/logarithmic basis away from a locally recoverable variable. The many successor-like "+1" terms may signal an exact connection to SUCC, gamma/factorial realization, and the shadow of growing path structure.

**Our mathematical repair:** treat W as (a) an *inverse coordinate chart* for the bulk of \(\log\Gamma(N+1)\), where exact SUCC provides the residual and verifies the answer; and (b) an *analytic completion of an exact recursively generated rooted-tree species*. Establish branch choices and mutation controls before interpreting any connection to RH.

**Primary mathematical sources:**
- NIST DLMF §4.13, [Lambert W and branches](https://dlmf.nist.gov/4.13), defining \(W(z)e^{W(z)}=z\), the derivative singularity at \(-e^{-1}\), and the tree function.
- NIST DLMF §5.11, [Stirling/Gamma asymptotics](https://dlmf.nist.gov/5.11), especially 5.11.1–5.11.3.
- Flajolet and Sedgewick, *Analytic Combinatorics*, Chapter II, [rooted labeled tree species \(T=z e^T\)](https://algo.inria.fr/flajolet/Publications/AnaCombi1to9.pdf).
- Previous repository checkpoints: \`actualization/gamma_succ_path.py\`, \`actualization/infinite_realization.py\`, \`actualization/succ_shadow_window.py\`; source-connected log/Weil no-gos in \`wiki/08-the-reformulations-catalog.md\`.

## 1. The important +1: inverse Jacobian, not a free SUCC law

W is defined by \(z=w e^w\). Differentiation gives

\[
\frac{dz}{dw}=e^w(1+w),\qquad
\boxed{W'(z)=\frac{e^{-W(z)}}{1+W(z)}}.
\]

The occurrence of \(1+w\) is the derivative of a PRODUCT. It is a precise
*local differential analogue* of mixing identity and growth terms; it is
not by itself the arithmetic successor \(S|n\rangle=|n+1\rangle\).

The Jacobian vanishes at \(w=-1,z=-e^{-1}\). W therefore has a square-root
branch point there: inversion breaks down exactly at this fold. The
principal branch \(W_0\) is real and monotone for \(z\ge0\);
for \(-e^{-1}<z<0\), the two real branches \(W_0\) and \(W_{-1}\)
read the same scalar z but produce distinct preimages.

**Boundary lesson:** path/branch selection cannot be inferred from the
scalar inverse equation alone. Specify the domain and source-constructed
branch. This is closely related to the earlier shadow-window selection
protocol, but *different* from Gamma's periodic gauge and complex-log
winding classes.

## 2. SUCC factorial mass: exact path, W bulk inversion, exact correction

For \(n\ge1\), the actual finite arithmetic path has

\[
M_n=n!=\prod_{k=1}^n k,\qquad
Y_n=\log M_n=\log\Gamma(n+1).
\]

Every successor step records \(Y_{n+1}-Y_n=\log(n+1)\).
Moreover, Legendre valuation and the prior \`FactorialSuccPath\` give an
**exact prime-factor history** for each integer stage.

Stirling's expansion starts with

\[
Y_n=n(\log n-1)+\frac12\log(2\pi n)+O(n^{-1}).
\]

The bulk map \(B(x)=x(\log x-1)\) can be inverted *exactly as a function*
for positive y, choosing the \(x>e\) branch:

\[
y=B(x)
\quad\Longrightarrow\quad
\boxed{x=\exp(1+W_0(y/e))=\frac y{W_0(y/e)}}.
\]

**This does not invert Gamma exactly.** It yields a good initial coordinate.
To infer a discrete factorial rank from an integer target M, the code
calculates this W seed, then applies finite SUCC corrections until it
independently checks

\[
\boxed{n!\le M<(n+1)!}
\]

using **exact integer arithmetic**. The result retains the complete
prime valuations of \(n!\). An inaccurate W seed cannot manufacture a
false certificate: it only changes the number of correction steps.

The precise missing residual is

\[
D_n=\log(n!)-n(\log n-1)
  =\tfrac12\log(2\pi n)+O(n^{-1})>0.
\]

Its exact successor increment is

\[
\boxed{
D_{n+1}-D_n
=1-n\log(1+1/n)>0.
}
\]

Thus the W chart and the gamma/SUCC residue have separate dynamical
states. The bulk inverse is a useful preconditioner, not a magic
quotient that restores all lost information.

**The branch fold itself is checkable.** For \(-1<y<0\),
\(x(\log x-1)=y\) has TWO positive preimages:
\[
x_0=\exp(1+W_0(y/e))\in(1,e),\qquad
x_{-1}=\exp(1+W_{-1}(y/e))\in(0,1).
\]
They meet at y=-1, x=1. The positive integer SUCC chart
chooses the first by its declared \(x\ge1\) domain. None of this
implies the analogous choice of a global RH spectral branch.

## 3. The stronger combinatorial surprise: rooted trees ARE Lambert W

Consider the species \(\mathcal T=\mathcal X\times\mathrm{SET}(\mathcal T)\):
a tree is one root connected to an unordered set of rooted smaller trees.
For labeled objects the exponential generating function satisfies

\[
\boxed{T(z)=ze^{T(z)},\qquad T(z)=-W_0(-z).}
\]

By Cayley's formula, the number of labeled rooted trees on n vertices is
\(a_n=n^{n-1}\). Hence

\[
T(z)=\sum_{n\ge1}t_nz^n,\qquad
\boxed{t_n=\frac{n^{n-1}}{\Gamma(n+1)}}.
\]

This is a legitimate *combinatorial-to-analytic transport*: discrete
finite branching histories, gamma/factorial normalization, and W all
occur in ONE proved object.

**Exact source construction without looking up the closed formula.**
Differentiate \(T=ze^T\), or equivalently
\(e^T=T/z\), to derive for n>=2:

\[
\boxed{
t_1=1,\qquad
t_n=\frac1{n-1}\sum_{k=1}^{n-1}k\,t_k\,t_{n-k}.
}
\]

The code constructs these rational coefficients *only* from earlier
finite stages, retaining a source mutation option. Their equality to
\(n^{n-1}/n!\) is an independent check, with a second low-n
implementation enumerating literally valid rooted parent maps.

The successor ratio is especially revealing:

\[
\boxed{
\frac{t_{n+1}}{t_n}
=\left(1+\frac1n\right)^{n-1}\longrightarrow e.
}
\]

By the ratio test, \(T\) has radius of convergence \(1/e\).
There the principal and secondary solutions of \(T=ze^T\) coalesce at
\(T=1,z=1/e\); the inverse Jacobian \(1-T\) vanishes and \(T'\)
becomes singular. This is a classical exact instance in which **finite
SUCC coefficients determine a limiting analytic branch with a genuine
global singularity**.

**Analogous +1 law shared with Gamma bulk:** the Gamma error increments
as \(1-n\log(1+1/n)\) while tree coefficient growth is
\((n-1)\log(1+1/n)\), so

\[
(D_{n+1}-D_n)+\log(t_{n+1}/t_n)
=1-\log(1+1/n).
\]

This is an exact comparison in a COMMON log-SUCC coordinate. It does
not establish any identity with Weil's explicit formula.

## 4. An important shadow falsifier: ordinary leaf SUCC is incomplete

Let \(a_n=n^{n-1}\). Start from a rooted tree on labels 1..n,
and naively add the new SUCC vertex n+1 only as a LEAF. There are
n possible attachment sites. This accounts for

\[
n a_n=n^n
\]

resulting rooted trees. But the true new count is

\[
a_{n+1}=(n+1)^n>n^n.
\]

**The missing structures contain new vertex n+1 as a root or an internal
vertex.** Full rooted-tree generation requires the forest/set
decomposition and its previously unobserved intermediate structures;
one terminal leaf extension does not exhaust the combinatorial paths.

This mirrors the prior SUCC/shadow distinction: endpoint adjacency,
full path information, and complete higher decompositions are different
probe classes. Its mathematical source is tree species, not arithmetic
primality.

## 5. Non-principal branch and source mutation controls

At \(0<z<1/e\), the real implicit equation \(T=ze^T\) has two positive
solutions:

\[
T_0(z)=-W_0(-z)\in(0,1),\qquad
T_{\mathrm{other}}(z)=-W_{-1}(-z)>1.
\]

Only \(T_0\) is the **formal power series with T(0)=0** built by the
finite rooted-tree recursion. The other branch diverges as z->0+
and cannot be selected by analytic finite-tree coefficients at the
origin. This is an actual branch-selection theorem from *declared
source-generating structure*, not an arbitrary principal-value label.

A mutated coefficient at level n=6 violates the exact functional
equation there: the residual of \(T-ze^T\) is a prescribed nonzero
rational \(\delta\). Later terms must adapt to the mutation, and the
functional identity no longer holds. This distinguishes true tree
source from an arbitrary numerical power series. In small cases, a
separate enumeration of all rooted parent maps validates the counts,
reducing accidental agreement with a memorized formula.

**But the decisive RH negative control remains:** replace the true
Euler/Dirichlet coefficient at n=6 by a fake non-prime-power connected
impulse. The factorial mass and W seed stay exactly unchanged, because
they do not read \(\Lambda(n)\), Euler multiplicativity, or Gamma's
Weil coupling. Likewise generic weighted-tree species
\(T=ze^{\lambda T}\) also has a Lambert-W solution,
\(-\lambda^{-1}W(-\lambda z)\): seeing W is not evidence of the
specific Euler arithmetic required by RH.

## 6. The specific role of Lambert W in the RH program

Lambert W is valuable as an **arithmetic index/rank preconditioner and
combinatorial closure instrument**, including the following realistic
uses: invert the growth of a factorial/Gamma SUCC resource budget;
locate a large expected activation horizon from a mass model with
n log n leading growth; and expose branch points and missing shadow
paths in generative combinatorial models.

It is **not** presently an RH proof mechanism. A scalar normalization
that survives fake primes, a PNT-like rank estimate with no phase
information, or a generic positive rooted-tree count fails the
arithmetic-mutation gate. The critical line is not the Lambert-W
branch cut, and the tree singularity at 1/e cannot be identified
with a zeta zero without a separate exact theorem.

**Next proof-bearing instrument:** enrich the species/Ind representation
with actual source coefficients \(\Lambda(p^k)\), \(\log p\), and
half-density, then seek a *mutant-sensitive* finite-to-archimedean
transform on a specified Mellin/Weil form core. Any proposed W-normal
form must identify its source-derived sign with the FULL Weil form
under a controlled limit and independent positivity theorem. Until
then it is a coordinate change only.

## 7. Claim ledger and reproduction

| Claim | Status | Verification |
|---|---|---|
| \(W\) inverts the real bulk \(x(\log x-1)\) with declared branches | **DISCLOSED** (algebra) | \`test_w_exact_stirling_bulk_inverse_positive_branch\` |
| Factorial rank from W+SUCC is exact when checked by integer factorial bounds | **DISCLOSED** (finite algorithm) | \`test_w_is_seed_not_certified_full_gamma_inverse\` |
| \(D_{n+1}-D_n=1-n\log(1+1/n)\) | **DISCLOSED** (algebra) | residual tests |
| Rooted-tree recursion produces Cayley \(n^{n-1}\), analytic \(T=-W_0(-z)\) | **DISCLOSED** (classical species theorem) | recurrence + separate parent-map enumeration + analytic calibration |
| Leaf-only SUCC fails to recover all rooted trees | **DISCLOSED** (finite exact inequality) | independent count |
| \(t_{n+1}/t_n\to e\), and branch point \(1/e\) | **DISCLOSED** (classical ratio and W theory) | exact rational sequence |
| Finite tree-series near branch fits \(W_0\) but not \(W_{-1}\) | **OBSERVED** (numerical; branch theorem separate) | series vs W |
| \(W\) rank normalization is insensitive to fake prime connected coefficient at 6 | **REFUTED** as proof candidate | source mutation test |
| A W normal form gives full Weil positivity or RH | **UNVERIFIED** | no source-domain positivity theorem |

To reproduce:
\`\`\`sh
python scripts/lambert_succ_probe.py --factorial-stage 32 --tree-stage 40
python -m unittest discover -s tests/actualization -p 'test_lambert_succ.py' -v
\`\`\`

**Boundary:** No zero ordinates were used; no infinity was executed,
no continuous Gamma inverse was claimed, and no positivity theorem
was smuggled from the branch choice. Exact finite proofs and
high-precision numerical calibrations remain separate.

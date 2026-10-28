# Carry × Pólya × original BBP: results and proof boundaries

Research branch `research/bbp-resolvent-observer-rigidity-2026-10-28`, based on
draft PR [#348](https://github.com/femboy2112/SUCC/pull/348) at
`fec9b7a72dd6b8c7550d7915070ee8094f2b94a2`.
The live parent chain was checked before changes: #344 `f10632ee`,
#346 `34c83015`, #347 `8345ce28`, #348 `fec9b7a7`; Main XIII is `b763ba8e`.
The handoff's alternate `research/origin-locked-causal-growth-2026-10-28`
branch name is absent from the remote; the explicit user-specified #348 head
is the coherent parent actually used. Main, siblings, and frozen archives
are preserved. This is a stacked research draft, not an integration into main.

**Three results survive independent derivation and hostile tests.** The signed
observer has an exact boundary obstruction; the original BBP forcing has a
minimal fourth-order zeta relation; source-marked Pólya growth has a coherent
isometric realization with a sharp auxiliary-dimension and leakage law.
No selected signed Weyl saving, π normality, RH, physical quantum
implementation, or academic novelty is claimed.

## 1. Primary theorem: exact signed boundary and spectral obstruction

Use the original divisor embedding
\(J|n\rangle=d(n)^{-1/2}\sum_{ab=n}|a,b\rangle\), the pair shift
\(S_A|a,b\rangle=|a+1,b\rangle\), and \(T=J^*S_AJ\).
Set \(D_N=\sum_{n\le N}d(n)\) and
\(x_N=D_N^{-1/2}\sum_{n\le N}\sqrt{d(n)}|n\rangle\).
For every integer \(N\ge1\) and every complex sequence \(|f(n)|\le1\),
with \(M_f\) diagonal, the exact identity is

\[
D_N\langle x_N,[M_f,T]x_N\rangle
=\underbrace{\sum_{b=1}^N f\bigl(b\lfloor N/b\rfloor\bigr)}_{B_N(f)}
-\underbrace{\sum_{n=1}^N f(n)}_{S_N(f)}.
\]

Moreover

\[
\sup_{|f|\le1}|\langle x_N,[M_f,T]x_N\rangle|
=\frac{2\lfloor N/2\rfloor}{D_N}\sim\frac1{\log N}.
\]

The same sharp bound holds if the supremum is restricted to unit phases.
**Proof mechanism:** for each fixed second factor \(b\), all differences
along \(b,2b,\ldots,b\lfloor N/b\rfloor\) telescope. The terminal
multiplicity \(c_N(n)=\#\{b\mid n:n+b>N\}\) satisfies
\(\sum c_N=N\), vanishes exactly on the first half, and is at least one
on the second half. Thus \(\sum|c_N(n)-1|=2\lfloor N/2\rfloor\);
choose phases −1 on the first half and +1 on the second to attain it.

This applies literally to the authentic
\(f_h(n)=\exp(2\pi i h U_n(0))\). The small commutator scalar is therefore
universal and cannot supply cancellation by itself. The terminal boundary
is load-bearing: constant phases give \(B_N=S_N=N\). Even a phase sequence
with vanishing mean can retain a boundary of order \(N\). This is a scoped
obstruction to this scalar transfer, not a claim that all commutator methods
must fail.

The companion spectral result is also exact:
\(\langle x_N,Tx_N\rangle=1-N/D_N\), \(\|T\|=1\), and
\(L=I-\operatorname{Re}T\) has trivial kernel but \(0\) in its essential
spectrum. The obstruction persists after any fixed finite origin prefix is
hard-pinned and after compact perturbations. Ratios of vertex phases give
only unitary conjugates of this operator, hence cannot make its spectrum
identify the BBP source. The actual pair \((M_f,T)\) and commutator retain
more information than those spectra; they are not declared source-blind.

Full quantified proofs and controls:
[signed observer dossier](BBP_SIGNED_OBSERVER_AUDIT.md).
The Lean file [DivisorBoundary.lean](../../formal/DivisorBoundary.lean)
checks the all-horizon finite ray identity over every commutative ring.
It does not formalize the Hilbert normalization or infinite spectral claims.

## 2. Original-forcing analytic advance

Let \(F(s)=\sum r(n)n^{-s}\), with the original four-pole forcing, and
\((\mathcal T G)(s)=G(s-1)\). Then

\[
Q(\mathcal T)F=
\frac{120\zeta(s-2)-89\zeta(s-1)+16\zeta(s)}{512},\qquad
Q(z)=(z-7/8)(z-1/2)(z-3/8)(z-1/4).
\]

This polynomial shift order four is minimal. Among ordinary Dirichlet
series converging absolutely on a right half-plane, this equation uniquely
determines the original forcing coefficients. The proof is coefficient
uniqueness followed by the coprimality of the numerator and denominator
of the actual source rational function; it is not an invented Euler product.

The normally convergent expansion
\(F(s)=\sum_{k\ge2}a_k\zeta(s+k)\), with
\(a_k=(4\,7^{k-1}-2\,4^{k-1}-3^{k-1}-2^{k-1})/8^k>0\), proves
the complete negative-integer pole tower and explicit truncation bounds.
The handoff's finite part at −1 is independently recovered exactly;
all negative-integer finite parts are derived. A unique decaying heat
response gives the genuine Mellin relation, including its nonzero
\(t\log t\) term.

Two precise completion obstructions prevent overinterpreting this relation:
no finite product of positive-slope Gamma factors and a nonzero rational
factor supplies a scalar reflection equation; the entire repair
\(F(s)/\Gamma(s+1)\) has alternating negative-integer values, real zeros
between them, and no reflection with a real center. These results are
restricted to their stated completion classes.

[Analytic dossier and literature](BBP_DIRICHLET_RESOLVENT.md).
All these analytic invariants are independent of the seed. The coherent
same-forcing seed \(-\pi/16\) defeats a Weyl inference from them alone.

## 3. Source-covariant coherent observer theorem

At source dimension \(m=j+1\), the positive Pólya transition has a
nearest-neighbor isometric lift into the next fiber tensor a two-dimensional
auxiliary space. It preserves the original basis transition probabilities
and maps the marked uniform pure state exactly to the next marked uniform
pure state with the auxiliary system returned to a fixed pure state.
Dimension two is necessary for \(m\ge2\), and one suffices for \(m=1\).

For **any** such lift returning that auxiliary state on the marked input,
the accepted Kraus component is forced. The complementary squared norm is

\[
\frac1{m(m+1)}\sum_{\ell=1}^{m-1}
\ell(m-\ell)|v_\ell-v_{\ell-1}|^2,
\]

with eigenvalues \(r(r+1)/[m(m+1)]\), \(0\le r<m\).
This gives sharp leakage bounds away from the uniform ray. It also shows
why the earlier stochastic-matrix amplitude loss is not an unavoidable
cost on the marked state: a lawful coherent lift can eliminate it there.
For general positive nearest-neighbor source marginals, a rowwise
orthogonal construction preserves the marked square-root source vector.
The higher-rank uniform Pólya construction has sharp auxiliary dimension
\(\min(c,j+1)\) for \(c\) channels at grade \(j\).

The terminal Oily law, nearest-neighbor grade growth, almost-sure stopping,
and split-independent stopping already force the intermediate marginals;
they need not be separately assumed. An explicit split-dependent stopping
countermodel shows where uniqueness really fails.

[Coherence dossier](POLYA_COHERENCE_RIGIDITY.md).
[PolyaCoherence.lean](../../formal/PolyaCoherence.lean) checks the real
all-dimension Gram identity and first nonzero mode, not the full complex
channel or full Hahn spectral theorem. No dimensionless normalization is
identified with physical \(\hbar\).

## 4. Proof authority, reproducibility, and unresolved gate

The three derivations were developed in parallel by agents using the same
model and the same authenticated repository sources, then cross-reviewed.
That is methodological and algebraic redundancy, not three independent
source families or an external peer review. The exact implementations,
symbolic oracles, formal kernel, and primary literature supply distinct
checks with explicitly different scopes.

The [claim supplement](../../docs/CLAIM_SUPPLEMENT_CARRY_POLYA_RESOLVENT.md)
keeps paper, kernel, finite, refuted, and open claims separate. Local IDs
are intentionally unregistered; historical FQIDs are untouched.
The [validation record](CARRY_POLYA_VALIDATION.md) and machine receipts
record actual commands, dependency pins, hashes, exits, and limitations.

```sh
python scripts/check_carry_polya_source.py --output /tmp/carry-polya-source --full
python scripts/check_carry_polya_lean.py --output /tmp/carry-polya-lean
python scripts/build_math_memory.py --check
```

The Lean runner accepts `--dependency-project` for a read-only compatible
mathlib cache and checks every pinned package revision before compiling.
The source runner replays inherited oracles in a temporary layout rather
than rewriting their stored receipts. Hosted checks are tracked separately.

The remaining π-normality gate is exactly
\(\sum_{n\le N}\exp(2\pi i hU_n(0))=o(N)\) for each fixed nonzero
integer \(h\). The highest-value next target is a signed estimate retaining
the selected zero-seeded boundary information. Neither a smaller generic
commutator, a more accurate forcing moment, nor an independently drawn
prime prior closes it. The next [research handoff](../../handoffs/CARRY_POLYA_RESOLVENT_NEXT_2026-10-28.md)
specifies the surviving options and their falsifiers.

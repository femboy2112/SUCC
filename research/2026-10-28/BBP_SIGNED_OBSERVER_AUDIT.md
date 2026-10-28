# A sharp signed-boundary obstruction for the origin-locked BBP observer

**Date:** 2026-10-28. **Parent:** `fec9b7a72dd6b8c7550d7915070ee8094f2b94a2`
(draft PR #348). **Authority:** paper proofs below, independently reviewed
algebra, exact finite tests, and a separately delimited Lean boundary core.
**π normality and RH remain OPEN. Academic priority is UNVERIFIED.**

The substantive result is that a natural signed scalar of the new BBP
commutator tends to zero for **every** bounded phase sequence, at an exactly
optimal uniform rate. Its apparent cancellation is a hyperbolic boundary
effect. The missing term is an explicit signed boundary sum, which can be of
order N. A companion theorem rules out a uniform spectral gap for the
divisor-jump observer, even after any fixed finite origin pin. These are
obstructions to specified proof architectures, not counterexamples to the
authentic zero-seeded BBP orbit or to π normality.

## 1. Definitions and exact source boundary

All integers in Hilbert-space indices below are positive. Let

\[
d(n)=\#\{b:b\mid n\},\quad
J e_n=d(n)^{-1/2}\sum_{ab=n}e_{a,b},\quad S_A e_{a,b}=e_{a+1,b},
\quad T=J^*S_AJ.
\]

Thus J is an isometry, S_A is a unilateral isometry in each b-fiber, and

\[
T e_n=\sum_{b\mid n}\frac{e_{n+b}}{\sqrt{d(n)d(n+b)}},\qquad \|T\|\le1.
\tag{1}
\]

This is the operator from the parent dossier, not the ordinary successor
`e_n -> e_(n+1)`. Write `Re T=(T+T*)/2` and `L=I-Re T`.
For a bounded sequence f let M_f be its diagonal multiplication operator and
`K_f=[M_f,T]=M_f T-T M_f`. For every N≥1 put

\[
D(N)=\sum_{n\le N}d(n)=\sum_{b\le N}\lfloor N/b\rfloor,
\qquad x_N=D(N)^{-1/2}\sum_{n\le N}\sqrt{d(n)}e_n,
\tag{2}
\]

and `κ_N(f)=<x_N,K_f x_N>`, with the inner product conjugate-linear in its
first variable. These are declared test vectors. Their squared coordinate
weights are d(n)/D(N); **they are neither the uniform integer sampling measure
nor a replacement zeta/Oily source**.

In the application, without any changed source,

\[
f_h(n)=e^{2\pi i hU_n(0)},\qquad U_0=0,\quad
U_n=16U_{n-1}+r(n),\quad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\tag{3}
\]

The implementation imports `exact_forcing` from
[`bbp_natural_carrier.py`](../../observational_succ/bbp_natural_carrier.py)
and literal divisor fibers from
[`origin_fiber_arithmetic_observer.py`](../../observational_succ/origin_fiber_arithmetic_observer.py).
The original π identification is the separately established
[`DUCK_BBP_SOURCE_IDENTITY.md`](../2026-10-21/DUCK_BBP_SOURCE_IDENTITY.md).
Source SHA-256 values are in
[`BBP_SIGNED_OBSERVER_RECEIPT.json`](BBP_SIGNED_OBSERVER_RECEIPT.json).
No source, seed, archival file, or prior theorem status is modified here.

## 2. DSO-01: exact signed transfer and sharp universal bound

**Theorem.** For every bounded complex sequence f and every N≥1, define

\[
S_N(f)=\sum_{n\le N}f(n),\quad
B_N(f)=\sum_{b\le N}f\bigl(b\lfloor N/b\rfloor\bigr),\quad
c_N(n)=\#\{b\mid n:n+b>N\}.
\]

Then

\[
\boxed{D(N)\kappa_N(f)=B_N(f)-S_N(f)
=\sum_{n\le N}(c_N(n)-1)f(n).}
\tag{4}
\]

Moreover, the supremum over all sequences with |f(n)|≤1 is exactly

\[
\boxed{\sup_{|f|\le1}|\kappa_N(f)|=
\frac{2\lfloor N/2\rfloor}{D(N)}\sim\frac1{\log N}.}
\tag{5}

The supremum is attained by unit-modulus phases, namely f(n)=−1 for
n≤floor(N/2), and f(n)=1 for n>floor(N/2). The maximizing sequence may depend
on N; this is a sharp *uniform-in-f* assertion, not an asymptotic for the
authentic BBP sequence.

**Proof.** Inserting (1) and (2) cancels both divisor square roots:

\[
D(N)\kappa_N(f)=\sum_{\substack{n\le N,\ b\mid n\\n+b\le N}}
[f(n+b)-f(n)].
\]

Write n=ab and sum first along each b-fiber. Its allowed a values are
`1,...,floor(N/b)-1`, so the sum telescopes to
`f(b floor(N/b))-f(b)`. Summing b proves (4). Alternatively, n has d(n)−1
incoming edges and d(n)−c_N(n) outgoing edges within the cutoff, giving
coefficient c_N(n)−1 directly.

Each b≤N has exactly one last vertex `b floor(N/b)`, hence
`sum_(n≤N)c_N(n)=N`. Also c_N(n)=0 exactly when n≤floor(N/2): if 2n≤N
every divisor is at most n≤N−n; if 2n>N the divisor b=n is an outgoing
boundary edge. Therefore the coefficients c_N(n)−1 are −1 in the first
half and nonnegative in the second. Their sum is zero, and their l1 norm is
`2 floor(N/2)`. The triangle inequality gives (5); the stated signs attain it.
Finally,

\[
NH_N-N\le D(N)\le NH_N,\qquad
\log(N+1)\le H_N\le1+\log N,
\tag{6}
\]

prove `D(N)/(N log N)->1`. For an entirely explicit estimate, N≥2 gives
`|κ_N(f)|≤1/[log(N+1)-1]` whenever |f|≤1. ∎

**Consequence for the actual source.** For every fixed nonzero integer h,
the authentic zero-seeded BBP phase satisfies (4)–(5), and consequently
`κ_N(f_h)->0`. This is a new rigorous estimate for this specified observable,
but it gives **no signed Weyl saving**. The exact relation is

\[
\frac{S_N(f_h)}N=\frac{B_N(f_h)}N-
\frac{D(N)}N\kappa_N(f_h).
\tag{7}
\]

The factor D(N)/N grows like log N, while B_N can have modulus N. Discarding
either term is invalid. Even an `o(1/log N)` commutator estimate alone would
not control the boundary. The constant sequence f=1 gives κ_N=0 and
`B_N=S_N=N` exactly.

**Lean boundary.** [`formal/DivisorBoundary.lean`](../../formal/DivisorBoundary.lean)
proves `signed_boundary_identity` for every commutative ring and every N,
by nested floor-indexed ray telescoping. The separate runner records its
actual kernel execution and axiom audit. It formalizes the finite sum in
(4), including the constant-phase counterexample. The Hilbert square-root
normalization, the edge/pair bijection, sharp l1 bound, and infinite spectral
claims remain paper proofs; they are **not** silently covered by that kernel
statement.

## 3. DSO-02: injective Laplacian with zero essential spectral gap

**Theorem.** The bounded self-adjoint operator L is positive, has trivial
kernel, and has zero in its essential spectrum. In fact, for every N≥1,

\[
\langle x_N,Tx_N\rangle=1-\frac N{D(N)},\qquad
\langle x_N,Lx_N\rangle=\frac N{D(N)},
\tag{8}
\]

\[
\|(I-T)x_N\|^2\le\frac{2N}{D(N)},\qquad
\|Lx_N\|^2\le\frac{2N}{D(N)}.
\tag{9}
\]

In particular `||T||=1`, although every individual basis column in the
parent result has squared norm at most 1/2.

**Proof.** `J x_N` is the normalized indicator of the finite hyperbola
`H_N={(a,b):ab≤N}`. Each of its N nonempty b-fibers loses exactly its first
point and acquires exactly one point beyond its last under S_A. Hence

\[
|H_N\cap S_AH_N|=D(N)-N,\quad
\|(I-S_A)Jx_N\|^2=2N/D(N).
\]

These give (8) and the first bound in (9) by compression. The exact identity

\[
L=\tfrac12J^*(I-S_A)^*(I-S_A)J
\tag{10}
\]

gives positivity and, since `||I-S_A||≤2`, the second bound in (9).
If Lx=0, (10) forces S_AJx=Jx. A square-summable vector invariant under the
unilateral shift in each b-fiber is zero, so x=0.

Each fixed coordinate of x_N tends to zero, and `||x_N||=1`. Approximating an
arbitrary test vector by finitely supported vectors proves `x_N` converges
weakly to zero. Equations (6) and (9) make it a singular Weyl sequence for
L at zero. The essential-spectrum assertion follows from the classical
Weyl criterion; the sequence and error are explicit here. The first bound
in (9) also makes 1 an approximate eigenvalue of T, so its contraction norm
is exactly 1. ∎

**Finite origin pinning.** For every fixed M≥0 and N>M let

\[
x_{M,N}=\frac{\sum_{M<n\le N}\sqrt{d(n)}e_n}{\sqrt{D(N)-D(M)}}.
\]

If N≥2M, every b≤N has a nonempty interval of a with M<ab≤N. The same
fiber count gives the exact formula

\[
\langle x_{M,N},Lx_{M,N}\rangle=\frac N{D(N)-D(M)}.
\tag{11}
\]

For a general shell the numerator is the number of nonempty b-fibers.
Thus restricting to vectors whose first M coordinates are zero does not
create a positive gap. Likewise, for every compact self-adjoint K,
`Kx_N->0` in norm, so `(L+K)x_N->0` and zero remains in its essential
spectrum. Fixed finite-rank origin penalties are included. This does not
exclude a noncompact or N-dependent constraint, or a bound restricted to
the actual BBP vector rather than to all Hilbert vectors.

**Finite-matrix trap.** The finite forward compression `P_N T P_N` is
strictly triangular and nilpotent, so all its eigenvalues are zero.
Nevertheless, the infinite T has approximate eigenvalue 1. The finite
self-adjoint `P_N L P_N` instead has least eigenvalue at most N/D(N), by
(8). Finite forward eigenvalues alone are an invalid gap diagnostic here.

## 4. DSO-03: BBP endpoint phase twists are pure gauge

For every unit-modulus sequence f, let

\[
T_f=M_fTM_f^*,\qquad L_f=I-\operatorname{Re}T_f=M_fLM_f^*.
\tag{12}
\]

The edge n→m carries the ratio f(m)/f(n). For every closed undirected walk
the oriented product of these ratios is exactly 1: the vertex factors
telescope. Thus the twist is a pure gauge, including on actual divisor
cycles such as `2 -> 3 -> 4 -> 2`. This uses no seed/forcing assumption.

It follows directly from (12) that the spectra, essential spectra, operator
norms and other unitarily invariant data of T_f or L_f are independent of
f. Any fixed real bounded diagonal potential V commutes with M_f, so the
same is true of `L_f+V` relative to `L+V`. Diagonal origin pinning therefore
does not distinguish the original zero seed from another phase source.
Hard coordinate restrictions also commute with M_f.

**Important scope:** the commutator K_f itself, its entrywise phases,
matrix elements with a fixed reference vector, and the joint pair `(T,M_f)`
can distinguish sources. Equation (12) does **not** say otherwise. It rules
out a source-discriminating argument that retains only the unitarily
invariant spectrum of the endpoint-ratio twist. A nontrivial magnetic
holonomy would require additional edge data that are not merely ratios of
one vertex phase; such data must be derived from the source, not invented.

## 5. DSO-04: stronger same-forcing and cancellation controls

### Coherent seed: faster scalar decay with nonzero mean

The native forcing equals A(n)/Q(n), where
`A=120n^2-89n+16` and `Q=(2n-1)(4n-1)(8n-7)(8n-3)`.
Writing n=t+2 gives the exact certificate

`Q(n)-n^2 A(n)=392t^4+2201t^3+4494t^2+3902t+1185`.

Thus `0<r(n)≤n^-2` for n≥2. The classical BBP identity gives, for the
explicitly changed seed `s*=-π/16`,

\[
U_n(s_*)=-T_n,\qquad T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
0<T_n\le\frac1{15(n+1)^2}.
\]

For every fixed integer h, set `f_h^*(n)=exp(-2πihT_n)`. Then
`|1-f_h^*(n)|≤2π|h|/[15(n+1)^2]`, whence its Weyl mean tends to 1.
Because the boundary c_N is supported on n>N/2 and sums to N,

\[
|B_N(f_h^*)-N|\le\frac{8\pi|h|}{15N},\qquad
|\kappa_N(f_h^*)|\le\frac{2\pi|h|}{15D(N)}(1+4/N).
\tag{13}
\]

Here `sum_(n≥1)(n+1)^-2<1`, by comparison with `1/[n(n+1)]`.
Indeed the absolutely convergent source-specific constant

\[
A_h=\sum_{n\ge1}(1-e^{-2\pi ihT_n})
\]

satisfies `D(N)κ_N(f_h^*) -> A_h`. For h≠0 its real part is strictly
positive: each real summand is nonnegative, and T_1 is irrational because
`T_1=π-r(1)`. Thus even decay of order `1/(N log N)` is compatible with a
nonnormal orbit of the **same forcing**. This orbit changes the seed and
is never called an authentic-zero-seed counterexample.

### A mean-zero phase with a nonzero boundary mean

For the separate comparison phase f(n)=(-1)^n, `|S_N|≤1`, but

\[
\frac{B_N(f)}N\longrightarrow1-\log2>0,\qquad
\kappa_N(f)\sim\frac{1-\log2}{\log N}.
\tag{14}
\]

To prove this, group b by `k=floor(N/b)`. For even k the phase (-1)^(kb)
is 1 and the interval has length
`floor(N/k)-floor(N/(k+1))`. For odd k the alternating sum has modulus at
most 1. For k≤K=floor(sqrt N), each even interval count differs from
`N/[k(k+1)]` by less than 1; all larger k together contain at most
`N/(K+1)` b-values. The corresponding limiting tail is bounded by the
same quantity. Hence

\[
\left|B_N(f)-N\sum_{\substack{k\ge1\\k\text{ even}}}\frac1{k(k+1)}\right|
\le K+\frac{2N}{K+1}\le3\sqrt N.
\]

The series equals `sum_(j≥1)(1/(2j)-1/(2j+1))=1-log2`. This establishes
(14). This comparison is **not** the BBP trajectory; it shows why the two
large terms in (7) may legitimately cancel and why individually forcing
both to vanish is stronger than cancellation of one arbitrary phase.

### Source and typing controls

For a rational changed seed s=k/15, the actual recurrence gives
`U_n(s)-U_n(0)=16^n s`, so the phases differ by a single global factor
`exp(2πihs)`. Edge ratios and pure-gauge spectra coincide. Absolute phase
turns and the declared seed receipt distinguish them. The altered first
four-pole coefficient `4 -> 5` also obeys (4) and (12), but its imported
source passport fails. Neither invariance certifies source authenticity.

The graph uses literal integer factorizations. Treating 6 as another
primitive prime gives six virtual split states at integer 6 instead of its
four actual divisor states; the native prime API rejects this input.
Likewise a two-mode ζ² prior is not the ordinary ζ source. No Gibbs law,
probability/amplitude identification, Pólya mixing claim, physical hbar,
or averaged-prior statement is used in these proofs. The finite test
`T e_1=e_2/sqrt2` explicitly retains amplitude loss.

## 6. Proof, computation and prior-art ledger

| Local ID | Exact claim and authority | Countermodel / limitation | Next falsifier or proof gap |
|---|---|---|---|
| DSO-01 | (4)–(5), PAPER-PROVED; nested pair-ray equality additionally LEAN KERNEL via the separate runner | Constant and coherent seeds have vanishing scalar with nonzero mean | A claimed signed transfer must retain B_N and D(N)/N |
| DSO-02 | (8)–(11), PAPER-PROVED using an explicit singular Weyl sequence | No source-specific BBP phase vector was asserted to equal x_N | A uniform gap must contradict these exact Rayleigh witnesses; a restricted source-bound needs genuinely additional hypotheses |
| DSO-03 | (12), CLASSICAL gauge algebra / PAPER-PROVED application | Does not make the joint pair (T,M_f) or K_f source-blind | Exhibit a source-derived non-gradient edge observable or retain a non-invariant marked reference |
| DSO-04 | (13)–(14), PAPER-PROVED exact asymptotics | Both are labelled comparison sources; neither refutes the original seed | Audit any stronger scalar-decay gate against the coherent seed and the retained boundary |
| DSO-F | finite counts, rational residuals, exact phase-turn transport, negative controls | EXACT FINITE TEST only | Replay outside checkout and mutate source, normalization, orientation or boundary term |
| DSO-OPEN | `sum_(n≤N) f_h(n)=o(N)` for every h≠0 on (3) | OPEN | Independently control signed selected phases; (7) alone is a rearrangement, not progress on their order |

The parent independently checked the incoming/outgoing degree proof of (4),
the sharp l1 norm, the hyperbolic intersection count, and the hard-pinned
shell count. This is a separate derivation/review, but shares the same
repository sources and model family. The Python probe compares direct
pair-space enumeration, grouped floor quotients and source-imported exact
rational phase turns. It never treats matching finite cases as the proof
of an infinite statement.

Relevant primary references were inspected on 2026-10-28:

- Fabila-Carrasco, Lledó and Post, *Spectral preorder and perturbations of
  discrete weighted graphs*, [arXiv:2005.08080](https://arxiv.org/abs/2005.08080),
  Definition 2.11 and Proposition 3.3: exact magnetic potentials are gauge
  transformations and give unitary equivalence. This is classical machinery,
  not a claimed new gauge theorem.
- Gerald Teschl, *Mathematical Methods in Quantum Mechanics*,
  [author-hosted text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
  Lemmas 6.17–6.18: singular Weyl sequences and compact-perturbation
  invariance of essential spectrum. Our contribution to this dossier is
  the explicit divisor-hyperbola witness and its exact rate.
- Bailey, Borwein and Plouffe, *On the Rapid Computation of Various
  Polylogarithmic Constants*,
  [DOI 10.1090/S0025-5718-97-00856-9](https://doi.org/10.1090/S0025-5718-97-00856-9):
  original BBP source, used through SUCC's pinned source proof above.

The search establishes classical ancestry for the general tools. It is
not an exhaustive priority search for (4)–(5) on this particular compressed
operator. No academic novelty or breakthrough is claimed.

Reproduce the finite evidence:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_divisor_observer_spectrum.py'
python scripts/divisor_observer_spectrum_probe.py
```

The probe defaults to stdout and accepts `--output PATH`; it does not
overwrite a committed receipt unless that path is explicitly supplied.
Full native, provenance, observer, ordinal, specialized source, hosted CI
and Lean evidence are reported separately in the integration validation.

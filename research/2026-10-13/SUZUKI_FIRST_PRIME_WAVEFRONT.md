# SUZUKI-1 — Source-faithful first prime wavefront, lost operator norm, and a rigorous boundary-layer rescue

**Research date:** 2026-10-13 (America/New_York; remote push may be 2026-10-14 UTC). **Primary source:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, dated 2026-09-23, https://arxiv.org/html/2606.09096v3 (equations (1.3), (1.5)–(1.8), (8.2), (8.7), §8.5). **Stacked source base:** SUCC draft PR #62 at `fb4fb91d46218ac121f4a4887f7322e79d3d0b70` (descends through PR #60, PR #59, `main@6e0d88f1...`). **Status:** rigorously **PROVED LOCAL** via written elementary proofs below; finite input/output interfaces **TESTED MODEL** by exact rational tests; not independently Lean-checked. The mathematical ingredients are classical spectral theory/Weil's explicit formula. Independent academic novelty **UNVERIFIED**. **RH PROVED: no.** No nontrivial zero positions are read.

## 0. Correct operator contract and the target

Use Suzuki's exactly normalized Weil functional, not an approximate or fitted zeta completion. For `v ∈ C_c^∞((-a,a), C)` extend by zero; `f=v*\tilde v`, `\tilde v(x)=conj(v(-x))`, and define

`h(t) = exp(-t/2)/(1-exp(-2t))` for `t>0`, `C_0 = γ` (Euler constant),

`b_q = Λ(q)/sqrt(q)`, `c_q=log q` for authentic prime powers `q=p^j>=2`.

Suzuki's Weil form, in the convention of his introduction, is

```
Q_W(v) = integral_R f(t)(e^(t/2)+e^(-t/2))dt
  - sum_q b_q [f(c_q)+f(-c_q)]
  - (log(4pi)+gamma)f(0)
  - integral_0^infinity [f(t)+f(-t)-2e^(-t/2)f(0)] h(t) dt.
```

**Important:** the first term is `2 Re(A_+ conjugate(A_-))` with `A_±=∫v(x)e^(±x/2)dx`. It is NOT `|A_+|²+|A_-|²`, and is not generally nonnegative. The prime sum is finite for compact support, with `q<=e^(2a)`. All Γ/pole/residue content is retained in `h`, the rank-two term, and the scalar constant.

**Theorem S1.0 (zero-independent full explicit-form decomposition, classical/algebraic).** For the specified smooth domain,

```
Q_W(v) = ∫_0^∞ ||v - τ_t v||² h(t) dt
          − [log(4pi)+gamma+log 2+pi/2] ||v||²
          − 2 Σ_{q<=e^(2a)} b_q Re ∫ v(x+c_q) conjugate(v(x)) dx
          + 2 Re(A_+ conjugate(A_-)),
```

where translations act on the *zero extension to R*. No zeros of ζ are used. **Proof:** `f(t)+f(-t)=2||v||²−||v−τ_t v||²`, `f(0)=||v||²`. The constant term from the integral is

```
I=∫_0^∞ (1-e^(-t/2)) h(t) dt
  =2∫_0^1 (1-u)/[1-u^4]du
  =2∫_0^1 1/[(1+u)(1+u²)]du
  = log(2)/2 + pi/4.
```

Therefore `2I=log 2+pi/2`. The pole/rank-two expression follows from Fubini. This is simply a reorganization of the original Weil formula, **not** a new proof of source-derived positivity. A scalar Fourier multiplier by itself does not replace the rank-two term.

**Dynamical meaning:** the prime arithmetic is a finite family of signed, source-authenticated *translation correlations*, against a continuous real-place translation-difference energy. The gamma/pole contribution is not an arbitrary positive covariance and not detachable without altering the source.

## 1. The exact first source wavefront

Let `c=log 2`, `b=log 2 / sqrt 2`, and

```
0 < w=2a-c,
log(2)/2 < a < log(3)/2 < c.
```

The ONLY contributing positive prime-power index `q<=e^(2a)` is `q=2`; `Λ(2)=log2`. The prime-generated continuous screw-kernel component in Suzuki's (1.3) is

```
g_2(t) = b (|t|-c)_+.
```

Define its unprojected compact operator on `L²(-a,a)` by

```
(R_a u)(x)= ∫_{-a}^a g_2(x-y)u(y)dy.
```

Suzuki's `G_a` acts on mean-zero functions with extra orthogonal projections `P_a`; the authentic prime component is `P_a R_a P_a`, **not** the full `R_a`. We use the unprojected operator to obtain a valid Hilbert–Schmidt bound `||P_a R_a P_a||_HS <= ||R_a||_HS`, without treating equality as automatic.

### S1.1 — Sharp Hilbert–Schmidt threshold law (PROVED LOCAL)

For any real `b>0`, `c>0`, `c/2<a<c` and `w=2a-c`,

```
||R_a||_HS² = b² w^4 / 6,   ||R_a||_HS = b w² / sqrt(6).
```

**Proof.** `|x-y|>c` holds in two disjoint opposite-corner triangles of side `w` in `(-a,a)^2`. With `r=a-x`, `s=y+a`, the kernel in one corner equals `b(w-r-s)` for `r,s>=0, r+s<w`. So

```
||R_a||_HS² = 2b² ∫_0^w∫_0^(w-r) (w-r-s)² ds dr
             = 2b²*(w^4/12)=b² w^4/6.
```

As `a` approaches `log2/2` from above, `||R_a||_HS = O(w²)`. This is actual smallness in a *compact-kernel* norm, not evidence about the differentiated original Weil form.

### S1.2 — An opposite operator-topology theorem (PROVED LOCAL)

On `C_c^∞(-a,a)` define `Q_2(v)=⟨R_a v',v'⟩`. Distributionally,

```
g_2''(t) = b[δ(t-c)+δ(t+c)].
```

Integrating by parts twice (compact support, no boundary ghosts) gives

```
Q_2(v) = −2b Re ∫_{-a}^{a-c} v(x+c) conjugate(v(x)) dx.
```

For `c/2<a<c`, the left strip `L=(-a,a-c)` and right strip `R=(c-a,a)` are disjoint. Translation by `c` is a unitary identification `L²(L) -> L²(R)`. The bounded extension of this quadratic form on `L²(-a,a)` is the off-diagonal block operator

```
B_2 |_(L⊕R) = [  0      -b U*  ]
              [ -b U      0    ],    B_2 |_(L⊕R)^⊥ = 0.
```

Consequently

```
||B_2||_op = b,   spec(B_2) = {-b, 0, b}.
```

The spectral signs `±b` have infinite multiplicity: choose arbitrary orthonormal smooth bumps in `L`, pair each with its `c`-translate in `R`, and take plus/minus combinations. In particular, in the genuine first-prime window,

```
||B_2||_op = log(2)/sqrt(2) > 0,
```

**uniformly in every a > log(2)/2**, despite the compact-kernel norm tending to zero.

**Status/meaning:** This is a rigorously derived *operator-norm discontinuity of the isolated first-prime contribution under zero-extended embeddings*. It does not assert norm discontinuity of Suzuki's full self-adjoint `A_a`: the latter carries a varying domain, full real-place term and established continuous `λ_a`.

**Regularity-cost corollary.** Any smooth bump `v` supported in these two width-`w` endpoint strips obeys the 1D Poincaré bound

```
||v'||² >= (pi/w)² ||v||².
```

The hidden `±b` prime eigenmodes therefore demand derivative energy growing at least as `w^{-2}` as the strips collapse. A fixed finite basis with bounded derivatives can miss them even when the operator norm remains `b`. This is a concrete `IdealHard`-style interface issue, not an actual physical energy measurement.

## 2. Moonshot result: the complete real place repairs the thin-edge subspace

The cheap conclusion `Q_2(v)≥−b||v||²` does NOT imply `Q_W(v)` positive. We now retain the *complete* Archimedean terms via S1.0.

### S1.3 — Quantitative unconditional first-prime boundary positivity (PROVED LOCAL)

Set `c=log2`, `b=c/sqrt2`, and let

```
0 < w=2a-c <= c/65536.
```

Write `L=(-a,-a+w)`, `R=(a-w,a)`. For **every nonzero** smooth compactly supported complex-valued `v` with `supp(v) ⊂ L∪R`, the genuine completed Weil form satisfies

```
                   Q_W(v) > (8/35) ||v||².      (S1.3)
```

**Proof — geometry and source.** The bound on `w` forces `log2<2a<log3`, hence *only* the authentic `q=2` prime wavefront contributes. For every `t ∈ [w,c-w]`, the sets `supp(v)` and `supp(τ_t v)` are disjoint: each strip has width `w` and their intervening gap is `c-w>=w`. Therefore

```
||v-τ_t v||² = 2||v||²    on [w,c-w].
```

Since `h(t)=e^{-t/2}/(1-e^{-2t}) >= 1/(2sqrt2 t)` for `t<=c` (using `e^{-t/2}>=1/sqrt2` and `1-e^{-2t}<=2t`), the positive real-place translation energy obeys

```
∫_0^∞ ||v-τ_t v||² h(t)dt
   >= (1/sqrt2) log[(c-w)/w] ||v||².
```

The rank-two term is bounded below using Cauchy–Schwarz:

```
2 Re(A_+ conjugate(A_-)) >= −4 sinh(a)||v||².
```

The only prime term obeys `Q_2(v)>=−b||v||²`. Hence S1.0 proves the *source-correct* inequality

```
Q_W(v) >= [ (1/sqrt2) log((c-w)/w)
             − log(4pi)−gamma−log2−pi/2−4sinh(a)−b ] ||v||².
```

**Rigorous numerical-free constant step.** Since `w/c <= 1/65536`, `(c-w)/w >= 65535`. Elementary certified bounds:

- `1/sqrt2 > 7/10`; `e < 68/25` and `(68/25)^11<65535`, hence `log65535>11`.
- `log2<7/10`, `b=log2/sqrt2<1/2`; `pi<22/7`, `log(4pi)<13/5`; Euler `gamma<3/5`.
- `a < 9/25` and `sinh(a) <= a/(1-a²/6)` for `a<sqrt6`; hence `4sinh(a)<3/2`.

These comparisons have independent rational witnesses in `onset_archimedean_certificate()`: `e` is bounded by its degree-6 Taylor sum plus `1/4410`; `log(4pi)<13/5` follows because the degree-5 Taylor sum for `e^(13/5)` exceeds `88/7`; `log2<7/10` from the degree-3 lower exponential sum; `gamma<3/5` from `gamma < H_32−log32` and the first three positive atanh terms for `log2`; the bound `sinh(x)<=x/(1-x²/6)` follows from `(2j+1)! >= 6^j`. The classical `pi<22/7` is invoked explicitly.

The bracket is therefore strictly above

```
(7/10)*11 − [13/5 + 3/5 + 7/10 + 11/7 + 3/2 + 1/2]
 = 77/10 − 523/70 = 8/35.
```

QED.

**Critical domain firewall:** S1.3 concerns a narrow two-strip subspace **after** the first real prime interaction. It does NOT show `λ_a>0`, positivity for all smooth tests, existence of a cross-interval spectral limit, or RH. It supplies a genuine arithmetic/Archimedean **coupled** form inequality on a declared source-visible boundary subspace, not a test-dependent fake kernel.

### S1.4 — Why there is no contradiction (PROVED LOCAL / CLASSICAL)

Embed all interval spaces by zero extension in `L²(R)`. As `a↓c/2`, the prime-differential `B_2` is supported on two shrinking strips; for any fixed `v∈L²(R)`, `||B_2 v|| <= b (||1_L v||+||1_R v||) ->0`. Thus `B_2 ->0` **strongly**, while `||B_2||=b` for every `a>c/2`.

The first new prime is invisible to each fixed regular probe in the limit but remains detectable by a *moving*, increasingly localized normalized observer. This is the exact same strong-vs-operator-norm distinction seen in the reciprocal-cell Wold-shell PR #61, though no canonical SUCC-to-Suzuki intertwiner is asserted.

## 3. Independent exact Neumann metric control

Suzuki §8.2 writes, on mean-zero `u∈L_0²(-a,a)`, `K_a=(-Δ_N)^(-1)` with kernel

```
N(x,y)=(x²+y²)/(4a)−|x−y|/2+a/6.
```

For real mean-zero piecewise constant `u` and `v(x)=∫_{-a}^x u(t)dt`, we prove and test

```
⟨K_a u,u⟩=||v||².
```

In particular `u=1` on `(-a,0)` and `u=-1` on `(0,a)` gives `||v||² = 2a³/3`. Exact rational double-rectangle kernel integrations match the antiderivative norm at 4 rational interval widths. This is an authentic **metric compatibility gate**, not a claim of Weil positivity.

## 4. Hostile controls and experiment receipt

1. **Fake composite:** `q=6` has `Λ(6)=0`, and is rejected as a positive prime-power jet; `q=4` is recognized as `2²` with `Λ(4)=log2`, not `log4`. The first interval includes 2, not 3 or 4.
2. **Wrong half-density:** modifying `b` shifts the nonzero translated form even though its symmetry remains intact; this shows the sign mode itself is **not** a sufficient source authenticator.
3. **Wrong log phase:** replacing the genuine translation length `log2` with a synthetic rational `c` changes the overlap response. The synthetic rational `c=7/10` is **solely an exact integration oracle**, never passed off as `log2`.
4. **Mean-zero/domain:** Neumann inverse interface rejects inputs with nonzero mean or missing coverage.
5. **Positive kernel fallacy:** `||R_a||_HS→0` is compatible with `||B_2||=b`; do not infer a full Weil sign from compact-kernel estimates.
6. **Cross-prime/matched non-Euler:** this dossier **does not** construct a Dirichlet/Hecke conductor-sensitive operator or the full matched Davenport–Heilbronn control; its one-prime source theorem has scope only `e^(2a)<3`.

The direct two-dimensional ramp integration (piecewise-polynomial rectangle primitives) is independently compared to the twice-integrated-by-parts translation formula for multiple signed sources, phase lengths and piecewise-linear functions. All tests are zero-independent exact `fractions.Fraction` or integer-exact arithmetic. `log`/`sqrt` values used in certificates are rational interval enclosures, never floating-point proof values. External primary facts from Suzuki are identified above and not re-proved.

## 5. Next research rounds — falsification first

A. **Full interval positivity near prime 2.** Split `L²(-a,a)=L²(L⊕R) ⊕ L²(interior)` with *the full* Archimedean quadratic form. Prove an explicit two-sided Schur complement or a block coercivity estimate controlling all interior-edge coupling. S1.3 only treats edge-supported states. A proof of `λ_a>0` for some interval beyond the classical small-`a` bounds would be an RH-relevant advance without assuming RH.

B. **Second wavefront and interactions.** At `a=log3/2`, add `q=3`, keeping complete Γ/pole source and studying the interacting translated blocks. At `a=log4/2`, retain `Λ(4)=log2` rather than `log4`; fake composite and phase mutants are mandatory. Analyze possible cancellations in the full operator rather than adding operator norms as if exact.

C. **Dual observer connection / compact metric.** In source-faithful `H^1_0`, compute the generalized pair `(G_a,K_a)` and certify its *full infinite-dimensional complement*. Kernel Hilbert–Schmidt smallness is not enough after derivative; use a uniform domain-correct source norm or demonstrate a no-go. Incorporate the genuine Neumann pairing and unbounded spectral domain, not a Euclidean Gram proxy.

D. **Global a→∞ / Suzuki (1.12).** Seek a valid normalization and limit only after a source-identified family and cross-interval deficiency/boundary transport exists. A finite interval's self-adjoint spectral function does not prove RH. No hidden use of zeros to construct the candidate.

**Verdict:** A real local arithmetic/Archimedean coupling lemma was proved; an operator-topology pitfall was exposed; the exact domain of the missing global estimate has become sharper. `RH PROVED: no`. No full `G_a-c(a)K_a≽0` theorem, no spectral limit and no global Nyman bound are claimed.

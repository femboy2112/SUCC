# Cloud institute: primary-source map and proof obligations

Date: 2026-10-20. Base: `0e56e0ae26f3d52a2ea34c0a4288478139fcb634`.
This is a source reconstruction, not a novelty or correctness certificate for imported results.
The lane dossiers contain full independently developed proofs; no paper is redistributed.

## 1. Source ledger

| Source and exact version | Statement and hypotheses checked | Mechanism / concrete SUCC obligation | Status and boundary |
|---|---|---|---|
| Bernert–Browning–Lichtman–Teräväinen, [arXiv:2410.12234v2](https://arxiv.org/html/2410.12234v2), revision 9 May 2026, Theorems 1.2–1.3 | For primitive positive `a+b=c≤X` and `rad(abc)<c^λ`, the exceptional count is `≪ε X^((23λ+3)/40+ε)` for `0<λ≤2`; for fixed `0<λ<1`, `≪ε,λ X^(0.6+ε)`. | Anatomical monomial decomposition, Fourier moments and geometry of numbers. Proposition 3.1 treats a dyadic monomial family; Proposition 4.1 exploits primitive lattice points. | EXTERNAL THEOREMS. These count a radical sublevel set. They do not directly bound SUCC's full `ris(abc)^t` moment. A weighted layer integration with controlled constants would be needed. Lane B's new-to-project proof does not import these estimates. |
| Ramanujan, [On certain trigonometrical sums…](https://ramanujan.sirinudi.org/Volumes/published/ram21.pdf), 1918, §2, equations (2.6)–(2.7) | For integer `N`, `c_q(N)=Σ_{d|gcd(q,N)} d μ(q/d)`, obtained by Möbius inversion of complete additive-character sums. | Characters → integer divisor formula → coprime multiplicativity. Lane C supplies the separate absolute-convergence proof for the Goldbach series. | CLASSICAL. A finite identity alone never licenses rearranging an infinite series. `N=0` requires exclusion in that convergence claim. |
| R. G. Douglas, [On majorization, factorization, and range inclusion…](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf), Proc. AMS 17 (1966), 413–415, Theorem 1 | For bounded Hilbert-space operators `A,B`, `ran A⊆ran B` iff `AA*≤λ²BB*` for some finite `λ` iff `A=BC` with bounded `C`. Actual ranges, not only their closures. | Form the bounded map `B*x↦A*x`, extend on the closure and take its adjoint. This identifies the correct bounded inverse-response obligation. | CLASSICAL. Replacing actual range inclusion by dense-range inclusion is invalid; unbounded realizations need new domain hypotheses. |
| Masatoshi Suzuki, [Weil's quadratic form via the screw function](https://arxiv.org/html/2606.09096v3), v3, 23 September 2026, Theorem 1.1 and §8.5 | The localized signed Weil operator is the Friedrichs extension of the specified symmetric realization. The primitive Rayleigh quotient becomes `<G_a u,u>/<K_a u,u>` under `u=Dv`, with `K_a=(-Δ_N)^(-1)` on the declared mean-zero space. | Track derivative/primitive coordinates and their different norms. Source identity and a form core are indispensable. | EXTERNAL THEOREM / classical framework. Compactness of `G_a` does not rule out a positive generalized lower bound relative to `K_a`. The paper's infinite spectral-limit conjecture is not a theorem. |
| Jineon Baek and Seewoo Lee, mathlib [MasonStothers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/MasonStothers.html); repository bridge pins mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` | Polynomial abc over a field: nonzero coprime polynomials with zero sum satisfy the radical degree bound or all derivatives vanish. | Wronskian and divisibility provide the polynomial descent; field characteristic and derivative alternative are load-bearing. | CLASSICAL / formal library theorem. The pinned source is authoritative for the exact lemma signature; current online documentation has a simplified signature. No integer-abc transport is supplied. |
| Montgomery–Vaughan, *The large sieve* (1973), bibliographic identity checked on [Montgomery's publication list](https://websites.umich.edu/~hlm/rpubs.html); mathematical exposition checked in [Vaughan's own notes](https://personal.science.psu.edu/rcv4/LargeSieve.pdf) | For frequencies separated modulo 1 by `δ>0` and coefficients on `N` consecutive integers, the sharp classical bound has factor `N−1+δ^(-1)`. Reduced fractions with denominators ≤Q have spacing ≥Q^(-2). | Mean-square sampling controls a whole frequency family. It cannot by itself give cancellation of a specified arithmetic weight on every minor arc. | CLASSICAL / author-source reconstruction. Original 1973 PDF endpoints failed (403/timeout); no claim of reading that original proof. The exact-grid special case below is proved directly. |

## 2. Independently derived calibration cases

### 2.1 Exact-grid Fourier sampling (CLASSICAL, complete proof)

Let `q,N≥1`, `M` integer, and `a_n` complex for `M<n≤M+N`. Write
`S(x)=Σ_n a_n exp(2πinx)`. Finite character orthogonality gives

`Σ_{j=0}^{q−1}|S(j/q)|² = q Σ_{r mod q}|Σ_{n≡r mod q} a_n|²`.

Each residue class has at most `ceil(N/q)` integers. Cauchy–Schwarz, applied
inside each class and then summed, proves

`Σ_j |S(j/q)|² ≤ q ceil(N/q) Σ_n |a_n|²`.

If `N≤q`, there is at most one integer per class and equality holds with
factor `q`. This is a finite, exact theorem for arbitrary weights; no
arithmetic randomness assumption enters. Repeated frequencies instead give
`R|S(0)|²`; taking `a_n=1` shows why separation is necessary for a bound
independent of `R`. The missing arithmetic input for Goldbach is cancellation
or a suitable major/minor-arc estimate for its particular weights.

### 2.2 Diagonal Douglas obstruction (CLASSICAL, complete proof)

On `ℓ²(N)`, let `A=I` and `B e_n=e_n/n`. The range of `B` is dense, since it
contains every finitely supported vector, but does not contain `x=(1/n)_n`:
its only possible preimage is the non-square-summable constant sequence.
If `A=BC` with `C` bounded, then `C e_n=n e_n`, a contradiction. Equivalently,
`I≤λ² B²` would require `1≤λ²/n²` for every `n`. Thus closure of ranges does
not replace the quantitative factorization assumption. Conversely, if
`A e_n=a_n e_n`, `B e_n=b_n e_n`, with real nonnegative entries, `a_n=0`
whenever `b_n=0`, and `sup_{b_n>0} a_n/b_n=L<∞`, then the diagonal operator
`C e_n=(a_n/b_n)e_n` (zero on the kernel) gives `A=BC` and `||C||=L`.

### 2.3 Polynomial calibration (CLASSICAL, complete calculation)

Over `Q[x]`, `A=x`, `B=1−x`, `C=1` obey `A+B=C`. Their product is squarefree
of degree two, and `max degree=1=2−1`, attaining Mason–Stothers. In
characteristic `p`, `x^p+(1−x)^p=1` has maximum degree `p` but radical degree
two; all derivatives vanish. Removing the derivative/characteristic gate
would therefore be false. This calculation tests a hypothesis boundary,
not the trusted kernel execution of a general theorem.

## 3. Dependency cuts and novelty tax

- **CRT:** an exact boundary budget and a coprimality tail are proof-producing
  inputs. Fixed-modulus asymptotics do not supply an arbitrary moving-modulus
  estimate. Lane A records the actual permitted regime.
- **ABC:** primitive determinant spacing retains information discarded by
  diagonal Cauchy–Schwarz. Lane B's full moment result is a project advance;
  publication-level originality remains UNVERIFIED. Its bound does not claim
  to improve BBLT's exceptional-set theorems.
- **Goldbach:** exact character algebra plus summable absolute tails closes
  the finite-to-infinite arithmetic bridge. It supplies no prime-pair
  asymptotic without an independent analytic error estimate.
- **RH:** a primitive closed-form realization can carry a relative bound.
  It does not supply the signed-source lower bound. Lane D checks an actual
  source enclosure and identifies the remaining quantitative deficit.
- **Formal authority:** an imported theorem name, a callback returning true,
  and a successful exact certificate checker are different objects. Lane E
  isolates executable rational certificates and formal elaboration. Lane F
  attacks the current metadata interfaces at a pinned head.

The paths are mathematically connected through explicit maps and estimates,
not through an assertion that one universal categorical functor is already
available. All major number-theoretic targets remain OPEN.

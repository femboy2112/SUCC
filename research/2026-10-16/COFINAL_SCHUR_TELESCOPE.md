# SOURCE-INDEXED COFINAL SCHUR TELESCOPE — finite observer accuracy without an a priori depth bound

**Research date:** 2026-10-16. **Base:** `femboy2112/SUCC` `research/collective-observer-2026-10-16@f7cc849d588629fec0db1d73a5418456b5087ed2` (draft #143), which descends from SUCC-λ #139 and E-consensus #140. **Independent arithmetic source sibling:** PR #137 `95dbf40553e54c901e9998e14b1b9d67298fa89e`; not merged into this branch. **Status:** elementary source-*conditional* paper theorem plus exact synthetic models and a fail-closed algebraic test interface. No actual Suzuki sign certificate, global positivity, proof of RH, physical sensor or Lean analytic theorem. The following mathematical computability implication is **not claimed as academic novelty**; the application is new-to-branch.

## 0. Faithful problem and immediately relevant precedents

The motivation is an **evolving E**: enlarge its legitimate source-calibrated probe menu, high-degree response space and numerical accuracy, rather than demand one finite frozen observation reconstruct the full object. For the real Gaussian Gamma source the sibling PRs #141/#142 and collective observer #143 have certified band-dependent sampling approximation, as well as alias obstructions to fixed rational clocks. The present problem is **different**: the *zero-shift signed source Schur short* at the authentic first-prime radius `a=1/2`, not pointwise or bandwise Gamma approximation. Do not conflate an expanding clock horizon with a uniform bound on `D^{-1}`.

Original signed Suzuki/Weil source: `observational_succ/source_weil_hierarchy.py` blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, SHA256 `183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`, origin commit `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. Fixed source includes both poles, contact, actual prime-2 half-density and full real Gamma. Suzuki primary source: [Weil's quadratic form via the screw function](https://arxiv.org/html/2606.09096v3), formula (1.3), Sections 2, 8. No nontrivial-zero locations are input.

The critical prior **analytic premises**, each scoped as a paper-source theorem rather than a Lean kernel fact, are [#137 `FRACTIONAL_SOURCE_RANGE_AUDIT`](https://github.com/femboy2112/SUCC/blob/95dbf40553e54c901e9998e14b1b9d67298fa89e/research/2026-10-16/FRACTIONAL_SOURCE_RANGE_AUDIT.md), [#137 source response certificate](https://github.com/femboy2112/SUCC/blob/95dbf40553e54c901e9998e14b1b9d67298fa89e/research/2026-10-16/AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md), and [#137 independently reviewed optimal residual corollary](https://github.com/femboy2112/SUCC/blob/95dbf40553e54c901e9998e14b1b9d67298fa89e/reviews/2026-10-16_OPTIMAL_RESIDUAL_COROLLARY_AUDIT.md). #143 derives better **zero-response** lower caps but neither parity sign is established. Neither source family is independent from its Gamma/coercivity assumptions.

## 1. Correct operator and finite response inequality (inherited, rederived)

Let `I=(-1/2,1/2)`, `H=L²_0(I)`, `PH=span(l_1,...,l_4)` for `l_j(t)=P_j(2t)`, `QH=P_4^perp`, `M=P_3^perp`. Their coordinate metric is **exactly** `W=diag(1/3,1/5,1/7,1/9)`. Let `J:PH->H` be inclusion and `G` the *unmodified original completed signed kernel* on this interval. Write `A=PGP`, `B=QGP`, `D=QGQ`. For `Vu(t)=int_{-1/2}^t u(s)ds` on `QH` and `T f=(G_raw f)'`, put

    R=Pi_M T|QH,    Y=Pi_M T|PH.

The inherited source-specific high coercivity statement is

    D >= kappa V*V,    kappa=20699/1000000>0.                    (H)

For any finite rational high-polynomial matrix `U:PH->span(l_5,...,l_N)`, set

    F_U=Y-RU,
    C_U=F_U*F_U,
    H_U=(J-U)*G(J-U).

The **actual** original source integration-by-parts identity, on the genuine high domain, is `(B-DU)=-V*F_U`. Indeed for high `u` the primitive `Vu` lies in `H¹_0(I) cap M`, so no boundary term survives, and `<G(J-U)x,u>=-<T(J-U)x,Vu>`.

The high quadratic completion and (H) give

    0 <= H_U-S0 <= kappa^-1 C_U,
    H_U-kappa^-1 C_U <= S0 <= H_U.                      (T1)

The expression `S0=A-(D^-1/2 B)*(D^-1/2 B)` is through the *square-root range*, not a bounded `D^-1`. The bound on the linear high functional using (H) supplies the range condition in the usual completion argument. The source identity and the sign of (H) must be checked as **analytic input**, not obtained from a typed source string.

For any low vector `x`, the proof uses

    H_U[x]-S0[x]
      = sup_(w in QH){ 2 Re <(B-DU)x,w>-<Dw,w> }
      <= sup_(w){2 ||F_U x|| ||Vw||-kappa||Vw||^2}
      <= kappa^-1 ||F_U x||^2.

No bounded high inverse, positive shift, finite eigenvalue approximation or degree-dependent rate is inserted here.

## 2. The computable-source lemma (new synthesis; PAPER, ANALYTIC HYPOTHESES LISTED)

**CS-01.** For each **rational polynomial** finite response `U`, the exact source values `H_U` and `||F_U l_j||²`, `j=1..4`, are computable real quantities **provided** the inherited signed source formula and following explicitly quantitative primitive truncations are correctly identified:

1. The positive full-Gamma form tail `0<=G-G_J<=tau_J I`, with
   `tau_J=2/(4J+1)^2+16/(4J+1)^3`.
2. The *differentiated* Gamma source obeys `||T-T_J||<=eta_J`, where
   `eta_J=2/(4J+1)+8/(4J+1)^2`, by Young's inequality and the source `L¹` kernel tail. **Do not replace this with tau_J.**
3. At each finite `J`, the remaining two poles, contact, prime-2 step and Gamma rungs are explicit computable piecewise polynomial/exponential kernels on the finite square, with computable breakpoints `0`, `log 2` and endpoints. Their coefficients (`pi`, Euler's constant, `log 2`, `sqrt 2`, finite exponentials) have rational convergent enclosing algorithms. Thus pairings with fixed rational polynomials, and squared `L²` norms of their projected derivative convolutions, can be enclosed to arbitrary absolute precision by validated analytic integration or interval quadrature. The step contribution must be partitioned at its actual source breakpoint. The endpoint derivative uses `Pi_M`, not differentiation after projection.
4. The polynomial vector norms of `J-U`, including all high coefficients, are exactly computable in `W` and the high Legendre metric. Consequently `tau_J ||J-U||²` and `eta_J ||J-U||` can be explicitly paid **after** the response is chosen; `J` must grow if `||U||` grows.

This is a constructive arithmetic-computability assertion about fixed **tests**, not a computation of the zero-shift inverse. The repository contains bounded-degree versions of the original-source exact integrals and interval bounds in `arithmetic_resolvent.py`, `collective_spectral.py`, and `suzuki_legendre_source.py`. An **unbounded-degree, fully integrated** certified evaluator is **not yet implemented** by this branch; therefore CS-01 remains an algorithm-existence PAPER claim dependent on those analytic formulae and the trust model of rational transcendental enclosures.

A concrete certified scalar *residual majorant* for each polynomial U is

    c_U = sum_(j=1)^4 (2j+1) (E_J,j + eta_J ||(J-U)l_j||)^2,   (T2)

where `E_J,j` is any source-certified upper bound on `||Pi_M T_J (J-U)l_j||`. Then `C_U<=c_U W` in the original low coordinate metric. Approximate `H_U` by a rational symmetric `Hhat_U` with `-e_U W<=H_U-Hhat_U<=e_U W` (using finite-J source pairings, exact error propagation and the actual `tau_J` tail). The **conditional finite certificate** is

    Hhat_U - (e_U+c_U/kappa) W <= S0 <= Hhat_U + e_U W.     (T3)

Its width in the `W`-operator norm is `2e_U+c_U/kappa`. Both sides retain the same original source and every analytic dependency. Merely writing plausible bound numbers into an object does not establish the hypotheses (our typed packet reports `source_identification_authenticated=False`).

## 3. Main result: a total adaptive finite-to-fixed-global accuracy telescope

**CS-02 [PAPER, conditional on (H), source-specific `closure Ran R=M`, and CS-01].** There exists a single, finite-step-at-each-output procedure `T(k)` which, for every natural `k`, **eventually halts** and returns a rational U and rational 4x4 matrices L_k, H_k with

    L_k <= S0 <= H_k,  H_k-L_k <= 2^(-k) W.             (T4)

No explicit `k -> degree(U)` formula, claim of practical running time, actual sign, or uniform-in-radius statement is part of this result.

**Algorithm.** Fairly enumerate (degree, height, rational coefficients) for all four columns of U in finite rational Legendre spans, and dovetail the interval precision and Gamma cutoffs used to evaluate the source residual and energy. For each candidate request rigorous bounds as in CS-01. Halt on the first verified `2e_U+c_U/kappa<2^-k` and return the matrices (T3). The source records, old observation history and all interval debts remain part of the certificate. With a finite budget, exhaustion is `UNRESOLVED`, not `S0>=0` or `S0<0`.

**Proof of totality, carefully separated from complexity.** The actual source-specific density `closure Ran R=M` gives, for each j, finite-polynomial high responses u_j with residual norm arbitrarily small: first approximate `Yl_j` by `Ru` in the dense image, then approximate u by high polynomials using boundedness of R. Next approximate their finitely many real/complex coefficients by rationals without losing the strict residual margin. Thus one **rational finite** U has the total trace residual `<kappa 2^-k/4`. CS-01 means its residual certified upper c_U can eventually be made as close to that trace as desired by increasing **both** the Gamma cutoff and the interval precision; choose `c_U/kappa<2^-k/2`. Similarly its finite energy `H_U` can be enclosed with `2e_U<2^-k/2`. The fair dovetail visits that response and precision. It halts. The sandwich (T3) certifies (T4). QED, under the listed source hypotheses.

This result is not a novel computable-analysis principle: it is a source-indexed instantiation of the elementary fact that a uniformly computable sequence of nonnegative finite errors known to have infimum zero yields an effective **search-for-threshold** procedure. A monotone computable sequence tending to a known computable limit has an effective convergence modulus *by search*, though no short a priori degree formula need follow. Compare [effective Dini/monotone convergence](https://www.sciencedirect.com/science/article/pii/S1571066105000083). The original #137 optimal-residual review already recognized **conditional strict-sign semidecision**; CS-02 states the stronger **uniform requested accuracy** conclusion and specifies the missing original-source finite-evaluation interface. Do not credit it as an RH breakthrough.

**Weaker source target.** The entire dense range is *sufficient but stronger than needed*. The proof uses only

    Ran(Y) subset closure Ran(R).                                  (T5)

By the Hilbert-space orthogonal-complement theorem, (T5) is equivalent to

    ker(R*) subset ker(Y*).

A direct four-column proof of (T5) could avoid the full Gamma Carleman/domain density argument, if the existing full-range claim is independently challenged. Conversely, an explicit `f in ker R*` with `Y*f !=0` would refute the telescope approximation theorem on the claimed source. This is a concrete source-specific falsification target.

## 4. Strict sign consequences versus singular impossibility

**CS-03 [PAPER, conditional].** The returned brackets converge in low operator norm and compute every scalar entry of S0 (with respect to the known W metric) to requested rational tolerance. If `S0>=delta I` for some strict `delta>0`, some finite *verified* lower matrix is positive definite. If S0 has a strictly negative low direction, some finite verified upper matrix has a strictly negative rational direction. Standard finite exact rational PSD and vector sign checks then halt. No promise is made for singular semidefinite S0.

A strictly negative `S0` direction implies a negative original G test on a finite (possibly very deep) high response, after the selected source energy's error is paid. The exact conversion to an original *smooth* compact test requires an approximating smooth source test with a separate bound; one cannot silently substitute a merely low-dimensional auxiliary Gram or a source-truncated kernel. This does not give a guaranteed low-radius counterexample if RH is false at a different support radius.

**CS-04 [COUNTEREXAMPLES, EXACT FINITE].** The script contains three infinite *synthetic* diagonal families:

1. **Delayed hidden mode:** choose low A=1/2, high `D_j=4^-j`, `V_j=2^-j`, residual map `R_j=-2^-j` and the only nonzero target coordinate `Y_m=-1`. Every `N<m` has `H_N=+1/2` and error bound spanning zero, while at N=m the short is `-1/2`. m is arbitrary. The response coefficient `U_m=2^m` can be huge. No early sign detector exists uniformly across this synthetic family.
2. **Nonattained response:** take `D_j=j^-4`, `V_j=j^-2`, `R_j=-j^-2`, `Y_j=-1/j`. The true target lies in ell² but not the actual range R, so high responses `U_N,j=j` have divergent norm, yet the exact residual squared tail `sum_(j>N)j^-2` has certified upper bound `1/N`, and the Schur telescope converges. With low A=2, a strictly positive short eventually receives a finite certificate. This explicitly defeats the claim that a bounded inverse or a bounded response sequence is necessary for effective telescoping.
3. **Singular boundary:** use `D_j=16^-j`, `V_j=4^-j`, `R_j=-4^-j`, `Y_j=-2^-j`, low A=1/3 and a valid nonsharp coercivity constant kappa=1/2. Then S0=0 exactly, but at every stage `H_N=4^-N/3` and `H_N-kappa^-1 C_N=-4^-N/3`; the brackets converge while both signs remain possible. A global sign rule cannot follow from shrinking intervals alone.

All three cases satisfy appropriate positivity and square-root response conditions with **declared** non-Suzuki sources. They do not refute the authentic-source theorem. The full affine/categorical/E-observer provenance system cannot eliminate these indistinguishabilities by duplicating an unperformed observation. A fabricated source ID, missing pole, fake prime six, or wrong interval radius cannot be counted as the original Weil source.

## 5. Where the RH proof is STILL missing

The requested `fixed first-prime S0 -> computable point` bridge is **conditionally closed at the mathematical algorithm-existence level**, not yet executed at arbitrary analytic precision. What is NOT closed:

- **Actual runtime source evaluator:** implement source- and SHA-pinned, arbitrary-degree finite polynomial energy and full projected-derivative residual *interval oracles*. The existing fixed-J cells and exact Legendre source integrals are seeds, not an unlimited interface. Every evaluation must pay `tau_J||J-U||²`, `eta_J||J-U||`, mixed cross-moments and interval rounding, and reject source-changing mutations.
- **Actual first-window sign:** current lower/upper matrices from #143 still straddle zero. CS-02 would compute their limit if run with sufficiently many certified stages, but it cannot guarantee that either sign decision halts at a singular limit; even a strict sign may be astronomically expensive. No numerical sign was newly resolved here.
- **All radii:** at a>1/2 new genuine prime powers enter; source high coercivity, low/high splitting, derivation estimate and target-specific dense range need new proofs. CS-02 does not uniformly apply across radii. For RH, a genuine source-wide Weil positivity result is needed for every compactly supported smooth test. A fixed positive first window is insufficient.
- **Analytic premise audit:** (H), whole-Gamma log-domain density and completed Weil source identification remain paper proofs, not fully formalized Lean theorems. Hashes plus successful CI are finite software provenance, not analytic truth.
- **Uniform forcing depth:** no bound of the form degree<=explicit-simple `F(k,source bounds)` is currently established. No source-specific weak-spectrum tail exponent or lower spectral gap is proved. The computable *search* modulus does not imply efficient runtime, first finite sign witness, or classification of RH as decidable.

## 6. Exact test and code status

`observational_succ/cofinal_schur_telescope.py` implements pure rational exact finite source squares, all-principal-minor PSD checking, the source-normalized *conditional* four-low packet with explicit unfulfilled premises, and three infinite analytic toy families with exact rational finite-stage error bounds. `tests/test_cofinal_schur_telescope.py` exercises matrix inequalities, all 81 small 2x2 rational high trials, bad B/D/coercivity/source/metric/channel mutants, and the delayed/unbounded/singular controls. `scripts/cofinal_schur_telescope_probe.py` emits deterministic JSON `RH_proved:false`, `cofinal_actual_source_oracle_integrated:false`, with model-relative signs and conditional packet authority.

At local development checkpoint: **35/35 focused unittest tests passed**, the generated synthetic receipt is deterministic (verify separately before publication). This environment cannot clone live GitHub; code publication uses the GitHub connector. Full SUCC validation must be checked on this exact branch head and must not be inferred from parent #143 green CI.

## 7. Next bounded experiment and independent falsifier

Implement an authenticated **full-source `CertifiedTrial(U,J,precision)`** evaluator for arbitrary rational Legendre U using the pinned original real Gamma/prime-contact/pole kernels and a *fresh* arbitrary-precision integration/tail certificate. Start with U=0 to reproduce #143 parity bounds; test at degree <=20 to reproduce #137's exact high-response upper matrices; then fit an explicit source-adapted U and verify strict reduction of C_U using *independent* interval/integration routes. Only after reproducing both parents move to larger degree and adaptive confidence targets. The algorithm must separately support unsuccessful source tests and retain failed trials, rather than laundering them into a global sign. If certified c_U falls below a given target, publish the returned rational response, Loewner matrices, and error budget; otherwise report BUDGET_UNRESOLVED.

Investigate separately whether just (T5) can be proved by the actual source without the full density/Carleman theorem; that is the cleanest conceptual missing lemma. A counterexample annihilator or error in the current source-domain argument would force a revision before any sign search can be trusted.

**End verdict:** an **adaptive accuracy bridge** exists conditional on the stated original-source mathematics, but **global Weil positivity and RH remain open**.

# SUCC — Operation Triangle Genesis: posterior path sum, observed point, and BBP frontier

**2026-10-29; DRAFT RESEARCH ONLY.** This additive continuation is based on exact [PR #386](https://github.com/femboy2112/SUCC/pull/386), commit `9c85894428e4ca1f8609d9ea1a79af1f51f1551f`, on the inherited #383/#381/#379/#373/#367 chain. Read-only siblings include #368–#372, #374–#378, #380, #382, #384 and #385. Nothing here changes `main`, BBP's four signed poles, `U_0=0`, archives, existing production paths, historical theorem IDs, or workflow configuration. **π base-16 normality and RH remain OPEN.**

## The corrected research hierarchy — DO NOT erase the earlier intuition

The author's original **Harmonic Numbers / Golden Ratio / Euler–Mascheroni triangle** and **Oily–Macaroni** (`Omega_OM=phi^{-1}-gamma`) retain their names, authorship/provenance and mathematical roles. The naming is already recorded in `research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md` (merged PR #365); preserve it verbatim. The original triangle is a real **specialization / coordinate family**, not discarded. Continue searching for it in Gamma/negative-binomial/rank-two/supercritical branching and arithmetic-source spaces, but do not claim it is universal.

The new **formal apparatus** is the typed operational triangle:

```text
          finite-path/source update  K
                     /           \
                    /             \
                   v               v
      superposed endpoint field ----> observer / selected point
      (mass + posterior)            (linear, nonlinear, carry)
                    O
```

An edge here must have a declared map; path superposition and linear observations commute, but normalization, logarithms, quotient projection, and selected integer carries require separate accounting. A **point** retains the posterior law on the latent source; a grade alone is not an arbitrary state replacement. This is an exact classical finite path-sum diagram, *not* a quantum wave-function assertion or a π-digit sampling mechanism.

## Main new statements

1. **Full joint finite generating law:**
   `F_(a,m)(z,t)=E_mu_a[e^(-taX)(z+(1-z)e^(-8X))^m]` has TWO exact original-four-pole finite descriptions: source-shift polynomial and superposed path/posterior sum. It conserves `F(1,t)=R(a(1+t))/R(a)` at every depth.
2. **Lossless source sufficient statistic (but not universal):** for the declared retained-`X` conditional-i.i.d. sensor and full ordered binary history `W`, the endpoint count `J=#ones` satisfies `X ⟂ W | J` and `I(X;W)=I(X;J)` at every finite depth. The posterior is unchanged under permutation of a fixed-grade word. The *prior* alone cannot replace the posterior. A concrete order-sensitive latent countermodel breaks sufficiency.
3. **Information loss under premature projection:** already at depth two, merging grades `J=0,2` into a parity/nonprimitive bit joins strictly different posterior source fields. Likewise resetting `X` between trials misses the strict covariance `R(a+16)/R(a)-[R(a+8)/R(a)]²>0`. The paths are flat under order swapping yet statistically dependent: **memory is not curvature**.
4. **Universal emergence class:** if a positive source kernel has a legitimate local asymptotic `Q(x)~c x^(r-1)` near zero and the observer depth satisfies `8m/a→theta>0`, the scaled field and count converge jointly to `Y~Gamma(r,1)`, `J|Y~Poisson(theta Y)`, with `F_(r,theta)(z,t)=[1+t+theta(1-z)]^(-r)`. The original four-pole source has `r=2,theta=1`, hence `F_infty=(2+t-z)^(-2)`.
5. **Origin of the author's triangle:** for `theta=1`, the limiting endpoint PGF is `G_r(z)=(2-z)^(-r)` with offspring mean `r`; a nontrivial attracting fixed point exists iff `r>1`. At rank two it is exactly `q_2=phi^(-2)`, with `lambda=1-q_2=phi^(-1)`. The *declared* `Y~Gamma(2)` log/Laplace readouts give `E log Y - E exp(-lambda Y)=lambda-gamma`. Here `gamma` is the Gamma/digamma harmonic finite part; the golden root is a specific two-channel/rank-two fixed point. This supplies a **testable class of spaces** in which the old triangle appears. Branching/extinction interpretation is an auxiliary declared iteration, not BBP physical offspring.
6. **NEW two-dimensional authentic 59-jet:** at the original native diagonal `a_n=8n-7`, `m=n`, `F_n(z,t)=(2+t-z)^(-2)+J_BBP(z,t)/n+O_K(n^-2)` on compact `0<=z<=1,0<=t<=T`, with

   ```text
   J_BBP(z,t) = [59 t² +92 tz -33 t -511 z² +813 z -302]/[120(2+t-z)^4].
   J_BBP - J_fake = 59(1+t-z)/[120(2+t-z)^3]
   ```

   where `Q_fake(x)=15x` with exactly the same sensor/clock. At `t=0` this recovers PR #386's harmonic `-59/(320n)` difference. This is source discrimination of a **joint source/grade observable**; it does not uniquely identify all positive source mutants, and no selected signed Fourier saving follows.
7. **NEW exact seed-resolved Fourier tomography:** the finite perturbation `s→s+u/16^n` produces a trigonometric polynomial with distinct integer frequencies `h*16^j`; its `h*16^j` Fourier coefficient is exactly `q_(a_n,m)(j)e(hU_(n+j)(s))`. One can recover all weighted *selected* phases without aliasing from this declared observer, before integer carry projection. Merely averaging over the seed displacement yields zero for *every* seed (including a coherent nonnormal counterseed), an exact no-go. Fourier recovery is information preservation, **not normality**. Literal integer carries must be retained as additional marks.

## Files and reproduction

- [THEOREMS.md](THEOREMS.md): hypotheses, exact equations, complete derivations, countermodels and claims boundaries.
- [CLAIMS.md](CLAIMS.md): new TG-01–TG-10 claims with status and falsifiers.
- [operational_triangle.py](operational_triangle.py): standard-library exact Fraction implementation.
- [test_operational_triangle.py](test_operational_triangle.py): focused exact source, path, posterior, carry and negative-control tests.
- [independent_oracle.py](independent_oracle.py): independent symbolic and high-precision numerical source/grade first-jet controls. Requires SymPy/mpmath (already research/test extras in root pyproject).
- [VALIDATION.md](VALIDATION.md): precisely scoped executed and unexecuted tests.
- [INTEGRATION_HANDOFF.md](INTEGRATION_HANDOFF.md): Claude's ancestry-aware integration protocol and post-main triangle frontier.

Run from this directory:

```sh
python -m unittest -v test_operational_triangle.py
python independent_oracle.py
python -m compileall -q operational_triangle.py test_operational_triangle.py independent_oracle.py
```

**No full SUCC root suite, hosted exact-head CI, Lean, or external peer review is claimed for this branch.** The surviving post-main frontier is an independent, source-authenticated, zero-seed-sensitive signed **intertime** carry/character estimate that fails on the coherent same-forcing seed `s=-pi/16`, counterfeit sources, phase-only aliases and premature marginal projections. The exact operational triangle is the apparatus in which to pose and test that obligation.

# Next execution: retain the signed boundary, exploit the minimal source equation

Start from the actual head of draft branch
`research/bbp-resolvent-observer-rigidity-2026-10-28` (discover its PR and
head live). Parent #348 is `fec9b7a72dd6b8c7550d7915070ee8094f2b94a2`.
Read AGENTS.md, METHOD, the mathematical memory index, source manifests,
[result summary](../research/2026-10-28/CARRY_POLYA_SOURCE_LOCKED_SUMMARY.md),
[claim supplement](../docs/CLAIM_SUPPLEMENT_CARRY_POLYA_RESOLVENT.md),
and [validation](../research/2026-10-28/CARRY_POLYA_VALIDATION.md).
Preserve main, original source/seed, archive receipts, and historical namespaces.
Use another isolated non-main child branch and draft PR. No merge or release.

## Load-bearing facts to retain

1. For T=J*S_AJ and the normalized divisor-hyperbola vector x_N,
   `D(N)<x_N,[M_f,T]x_N>=B_N(f)-S_N(f)`, where
   `B_N(f)=sum_(b<=N) f(b floor(N/b))`. The sharp unit-phase supremum of
   the scalar is `2 floor(N/2)/D(N) ~ 1/log N`. Its smallness is universal;
   the original signed boundary cannot be dropped.
2. T has norm one, despite every basis column's squared norm <=1/2.
   `I-Re T` is injective but has zero essential spectral gap, even after
   a fixed finite hard origin pin or compact perturbation. Explicit
   Rayleigh shell witnesses and rates are in the dossier. Finite forward
   matrices are nilpotent; their spectra do not approximate this boundary.
3. Endpoint-ratio phase twists have only pure-gauge spectra. The joint
   marked pair `(M_f,T)` can still discriminate sources; it is not ruled out.
4. The original BBP Dirichlet response satisfies a minimal order-four
   zeta-forced shift equation. Within absolutely convergent ordinary
   Dirichlet series the equation identifies the entire forcing. It never
   identifies the seed. Full poles, all Laurent constants, heat/Mellin
   response and two precisely scoped completion obstructions are proved.
5. Pólya growth has a two-dimensional coherent environment lift that
   preserves the marked uniform source with no residual environment
   information on that source. Every admissible lift has the same accepted
   component and leakage spectrum `r(r+1)/(m(m+1))` on general inputs.
   In c channels the minimal environment dimension is `min(c,j+1)`.
   This is a constructed observer law, not the BBP carry history.
6. The all-x terminal law plus grade-only stopping already forces the
   reached-grade marginals. Dropping their separate stipulation does not
   create ambiguity. Actual ambiguity after allowing split-dependent
   stopping has an exact diamond-flow counterexample.

## Prioritized next proof gaps

**A — selected signed information.** Seek a bound on the actual combination
`B_N(f_h)−D(N)κ_N(f_h)` with `U_0=0`, or a different signed transfer retaining
the absolute phase mark. Its current expression is exactly the original
Weyl sum, not a solved reduction. Any purported improvement must distinguish
the genuine zero seed from the coherent same-forcing seed `−π/16`.
Do not demand both terms separately vanish without justification: the
mean-zero comparison `f(n)=(-1)^n` has `B_N/N→1−log2`.
First falsifier for scalar-only gates: coherent seed has
`κ_N=O_h(1/(N log N))` while the phase mean tends to one.

**B — analytic relation with genuine source content.** Study vector-valued
or explicitly additive completions of the four-pole resolvent, or precise
asymptotics derived from its heat ODE. Standard finite positive-slope
Gamma-product scalar completion is excluded; reciprocal-Gamma repair is
entire but not self-reflecting about any real center. A new proposal must
state its domain, source transform, boundary terms and inversion theorem.
Use the known BBP Gamma primitive as an exact shared-source relation,
not shared constants as evidence. Check primary literature before priority claims.

**C — nonuniform coherence and signed phases.** Extend the universal
accepted-component classification to higher-rank nonuniform source laws
or characterize locality graphs with multiple shared output rows. Those
graphs permit cross-row cancellations, so the present minimal-dimension
proof does not transfer automatically. Distinguish auxiliary leakage from
irreversible information loss: the full V is an isometry. Physical hbar
requires a separate physical model and units.

## Required replay and authority

```sh
python scripts/check_carry_polya_source.py --output /tmp/carry-polya-source --full
python scripts/check_carry_polya_lean.py --output /tmp/carry-polya-lean
python scripts/build_math_memory.py --check
```

For an existing compatible cache pass `--dependency-project PATH` to the
Lean runner. It checks every exact package revision and exports theorem
types and axioms. Nine kernel declarations cover the finite boundary
identity and real Pólya Gram algebra only; all infinite analytic/spectral
claims remain paper proofs. Source runner checks 25 commands, exact
receipts, wrong-source controls, and inherited specialized source oracles.
Full native regression and hosted CI remain separately observable gates.

New claims need independently checked proofs, quantified limitations,
countermodels, exact source hashes, tests, and a next falsifier. Scoped
CPS/BDR/DSO/PCR references are not global FQIDs. Regenerate the discovery
catalog after documentation changes without rewriting the historical
namespace registry. Retain the existing proof failures and corrected
implementation details recorded in the validation note.

**Still open:** fixed-h signed Weyl cancellation on the original zero seed,
π normality, RH, physical realization and academic novelty. Deliver an
actual proved advance or a precisely quantified obstruction, not another
unexecuted analogy.

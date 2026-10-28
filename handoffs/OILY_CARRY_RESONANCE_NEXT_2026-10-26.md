# Next execution: source-selected branch energy and the carry alias pair

**Execution request, not a representation-only round.** Start from the live
draft branch `research/oily-carry-resonance-2026-10-26`; resolve its exact head
and CI afresh. This branch is stacked on #310, itself on #309 and #306.
Main is not the combined research tree. No merge, release, or normality
announcement is authorized by this handoff.

Read `AGENTS.md`, `docs/METHOD.md`, `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`,
the [synthesis](../research/2026-10-26/OILY_CARRY_RESONANCE_SYNTHESIS.md),
the [validation record](../research/2026-10-26/OILY_CARRY_RESONANCE_VALIDATION.md),
and all four mathematical dossiers linked there before choosing a new route.

## The source and target stay fixed

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

The outstanding theorem is `sum_(n<=N) e(hU_n)=o(N)` for each fixed nonzero
integer `h`. The existing uniform `O_h(1)` Green transfer already handles the
π orbit. Do not spend another round proving that equivalence.

## What must be reused

1. **Selected logarithmic loss now has coefficient `1/29`.** Its onset remains
   unspecified; the exact all-frequency cutoff has one additional geometric
   block. The finite lemma uses branch-difference norm 546 rather than the old
   coordinatewise `34a<1` condition. Read `OILY_DIRECT_ARITHMETIC.md` completely.
   Nine finite Lean declarations do not formalize its infinite analytic proof.
2. **A literal carry coupling exists.** The word `A_(n,L)`, conductor `Q`,
   forcing numerator `B`, and terminal remainder `R` obey
   `QA=16^L Q{U_n}+B-R`. Its dyadic primitive status is only terminal parity.
3. **The actual primitive carry Fourier identity contains the missing mode:**

   $$P(h)=\tfrac12[G(z)F(h)-G(-z)F(h+16^L/2)],\quad z=e(h/16^L).$$

   Recovering both primitive and even outputs recovers the original word
   character. The full packet transform has exact inverse `(2I-S)^2`.
4. **True cumulants have a different hierarchy from raw golden-centered
   moments.** At fixed order `m`, their leading coefficients are
   `m! [v^m] f_g(1/(1+v))`; the odd-grade third cumulant is `8/81` at
   order `(8n)^-2`. They are center-invariant, grade-dependent, and insensitive
   to the outer smooth endpoint weight. These are not π authentication data.
5. **The source time tilt does not uniquely supply temporal dependence.**
   Two explicit kernels have identical complete marginals but primitive
   covariance zero versus a limit `20/81`.
6. **Source-only fixed-harmonic phase resonance has a sharp degree boundary.**
   Nontrivial seed-invariant monomials need reduced degree at least 17.
   The first is the recurrence itself and has the same value on coherent
   changed seeds. This is a restricted grammar theorem, not a universal no-go.

## First attack: quantitative integer-branch energy

Use the phase-lift branch-energy construction in the direct-arithmetic
continuation and its standalone exact oracle. It retains actual source states
and minimizes over finitely many rational phase-center cells. Establish any
new all-horizon lower bound on that energy **from the original source and
zero selector**, not from its observed finite growth.

The immediate discriminants are: authentic source, terminal-zero rational
changed seed with identical forcing, one-impulse altered source, and a coherent
zero-forcing orbit. Preserve the exact recurrence residual. Distinguish the
phase-center-dependent integer branch tape from the original literal carry tape;
derive their map if combining the instruments.

**Do not overpromote this route.** A positive-density event count or fixed
positive fraction of total deficit gives at most a fixed relative saving.
The present quadratic instrument has a stronger proved obstruction:
`E_min<=289(N-2)/4`, so its deficit bound `(2/289)E_min` can never exceed
`(N-2)/2`. Alternating opposite phases attain this ceiling while their sum
can be zero. **No possible lower bound for this same energy can, through
this inequality alone, prove normality.** Use it to expose selector-sensitive
arithmetic or build a provably stronger signed inequality; do not propose
an impossible asymptotic value of the existing energy.
Normality still requires the normalized modulus to tend to zero. Before any
iteration argument, state how overlap is paid and why the same local energy
is not counted multiple times. A frequency-ladder contraction must escape the
already proved time-shift identity; simply assuming a ratio below one assumes
a much stronger unproved cancellation theorem.

## Second attack: the growing carry alias, preserving both signs

Choose a declared `L_N` and retain the **pair**
`F_(N,L_N)(h), F_(N,L_N)(h+16^L_N/2)` with its true source packet law.
The existing word-to-orbit error tends to zero at fixed `h` and growing depth;
it does not do so at the alias frequency. Any proposed lift of fixed-mode
estimates to the alias must pay that error explicitly.

Try to derive a signed joint inequality using the exact odd-conductor decoder,
actual forcing numerators, terminal remainders, and primitive quadratic atoms.
It must use more information than terminal parity or equal marginal digits.
A character of a different random law, a conditional expectation chosen to
equal the desired character, or a boundedly invertible re-encoding pays no
cancellation debt by itself.

## Third attack: genuinely external arithmetic input

Revisit Bailey–Crandall, inverse exponential-sum methods, cyclotomic/Galois
constraints and Diophantine methods only with an explicit candidate lemma.
The original Bailey–Crandall paper already contains the exact combined
recurrence. Its Hypothesis A is not an available theorem.

Finite irrationality type alone is insufficient for a superlogarithmic
absolute loss: the sparse base-16 selector has exponent two and nearly
maximal Fourier sums. A promising external theorem must see a source property
that this control lacks. Write the hypotheses beside the actual source map
before importing the theorem. Use primary sources and verify domains.

## Acceptance gates and workflow

- Prefer an actual new selected bound of larger **order**, even if far weaker
  than normality. Another coefficient improvement is valid but must be labeled
  as such and weighed against a genuinely new arithmetic mechanism.
- For a normality claim, close every fixed nonzero frequency, every limiting
  and uniformity step, the source selector, and the signed cross-block estimate.
- For a no-go claim, exhibit a typed counterexample in its stated grammar.
  Do not claim an altered source refutes the actual zero-seeded theorem.
- Use `oily_signed_certificate.py` for sound finite character/cross-block
  enclosures. It retains the signed off-diagonal term; it is not an infinite
  certificate. Replay all deterministic receipts and deliberate mutants.
- Work in an isolated non-main branch; keep imported sources byte-identical.
  Group changes before pushing. Run targeted tests first, then native full
  provenance/Python/observer/ordinal gates and applicable pinned Lean exports
  and mutants. Report clean hosted CI separately from qualified local checks.
- Keep one principal source/claim state. Workers must deliver proofs or exact
  falsifiers, source pins, scope, and reproducible evidence. Same-family model
  agreement is not external peer review.

The round succeeds if it pays a new signed arithmetic estimate or eliminates
a precise false implication with reusable evidence. It does not succeed merely
by making a familiar constant appear in another carrier.

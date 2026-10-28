# Oily–Macaroni to selected π: a stronger constant and sharper arithmetic obligations

**Result:** the selected BBP logarithmic deficit coefficient improves from
`1/1250` to `1/29`. The order is still logarithmic. **π base-16 normality and RH
remain open.** This round does not establish the requested `o(N)` cancellation.
No merge or proof announcement is authorized by this research draft.

## Live source passport

The complete mandatory handoff was read first through the GitHub connector.
The implementation is an isolated non-main worktree based on #310, not a
modification of another active worktree. Live heads at reconstruction:

| Object | Verified commit | Relationship |
|---|---|---|
| main / Main XI | `6dd80730c3575d91f746546a25da5aedbd2e2737` | common main ancestor |
| #306 | `7989be5753341c5e74d570e8fea51e00129d2d0a` | signed pushforward draft |
| #309 | `8e9d8a4d7d42bb0931f899ac221f27fccf090b36` | stacked on #306 |
| #310 | `a8c7c85b7a1900d422090f1757c174e7aac69f44` | immediate parent, stacked on #309 |
| #307 | `c41af6b0a1e96a7758cbf891cd56014be743beb0` | separate Mellin/Hilbert draft, read but not merged |
| #308 | `48bbfc78f499fbcac6e0b51f06a3ec60aa693731` | separate quadratic-atom draft, read but not merged |

The source remains exactly the four-pole `r(n)`, `U_0=0`, and radix 16.
Native adapters are reused. The original import pin
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`, its 72 provenance entries, and
frozen archives are unchanged. No π digit array or normality premise is an
arithmetic construction input.

## The hole contract

- **Exact target:** for every fixed nonzero integer `h`,
  `S_N(h)=sum_(n=1)^N exp(2 pi i h U_n)=o(N)`.
- **Starting state:** open pathway gap. Uniform Green-tail transport is proved;
  packet characters have a nonzero limit; a logarithmic absolute loss is proved.
- **Weakest current closure:** signed `o(N²)` total off-diagonal block energy,
  or the prescribed conductor-flat low-frequency gate with all transport costs.
- **Novelty test:** a changed representation is not a smaller bound. The actual
  new inequality must be stated on the selected orbit, with quantifiers intact.
- **Cheapest falsifiers:** changed seed with identical forcing; source-mutated
  zero seed; parity-alias counterexamples; a wrong adjacent coefficient norm;
  packet regrading; invalid analytic differentiation; dropped cross-block signs.
- **Finite boundary:** exact calculators can certify or refute finite bounds.
  They do not lift finite normal-looking behavior to any limiting frequency.
- **Remaining lamp:** a source-and-selector-specific arithmetic estimate in
  the moderate-coherence regime, where the total deficit scales with a block.

## What the mathematical work established

| Result | Earned authority | What it buys / what it does not |
|---|---|---|
| Integer-branch energy coercivity and selected loss `1/29` | Paper proof; 12 finite/adversarial tests; finite Lean core | Larger logarithmic coefficient, same asymptotic order |
| Exact minimum branch-event energy and its sharp ceiling | Paper inequality; rational breakpoint sweep and independent grid oracle | Real finite selected bounds; instrument alone cannot certify sublinear modulus |
| Literal carry-word / odd-conductor decoder | Exact finite algebra and independent source reconstruction | Retains integer lifts and source-time carries |
| Carry-translated packet totient with exact Fourier alias | Paper identity and 14 exact tests | Exposes an uncontrolled growing cross-digit mode |
| Packet convolution inverse `(2I-S)^2` | Finite algebra | Full smoothing preserves information; no automatic saving |
| Center-invariant mixed cumulant hierarchy | Paper asymptotic proof, independently audited beta expansion | Odd third cumulant `(8n)^2 κ -> 8/81`; leading Euler/golden term absent |
| Two source-derived cross-time couplings | Explicit probability kernels and covariance calculation | Same full marginals/time tilt permit different temporal covariance |
| Minimal fixed-harmonic seed-invariant degree 17 | Integer character proof | Low-degree source-only monomials cannot manufacture the zero selector |
| Sound selected Fourier and signed cross-block enclosures | Rational remainder proof; 8 calibration/mutation tests | Finite evidence for actual characters, retaining every cross-block sign |

The main new bound is

$$
|S_N^U(h)|\le N-\frac1{29}
\max\left(0,\lfloor\log_8N\rfloor-
\max(J_1,1+\lceil\log_{64}|h|\rceil)\right),
$$

for one unspecified integer `J_1`, all `N>=1`, and all nonzero integer `h`.
The ratio `1250/29` compares **leading coefficients**, not effective finite
horizons: the two onset thresholds are neither extracted nor assumed equal.

The arithmetic input is the published corrected
[Zeilberger–Zudilin irrationality estimate](https://arxiv.org/abs/1912.06345v2),
used only through `mu(pi)<15/2`. It is not a new theorem of this repository.
The source identity and zero selector turn near-coherence into a forbidden
rational approximation; the new contribution is the energy cost of differing
integer branches. Full proof: [direct arithmetic](OILY_DIRECT_ARITHMETIC.md).

The carry object is genuinely conditioned on literal source words, but its
translation rule is a **declared construction**, not a proved unique canonical
coupling. For `q=16^L`, `z=e(h/q)`, its primitive character is

$$P(h)=\tfrac12\big[G(z)F(h)-G(-z)F(h+q/2)\big],\qquad G(z)=(2-z)^{-2}.$$

The second mode grows with depth. Fixed-frequency cancellation cannot be
silently applied there. Full proof: [carry-conditioned totient](CARRY_CONDITIONED_TOTIENT.md).

The higher-shadow theorem is also specific about information loss. For fixed
bounded grade observable `g`, fixed positive integer `m`, and
`f_g(x)=E[g(J)|X=x]`,

$$
\lim_{n\to\infty}(8n)^m\kappa(g(J),\underbrace{\log Y,\ldots,\log Y}_{m})
=m!\,[v^m]f_g(1/(1+v)).
$$

Center shifts disappear, but grade changes do not. The leading term is also
insensitive to the outer smooth positive endpoint weight, so it cannot
authenticate all four BBP poles. The original golden-centered covariance
remains correct for its declared center. It is a different observable.
Full proofs: [cross-time grammar](OILY_CROSS_TIME_GRAMMAR.md).

There is also a useful new exact arithmetic inequality. For the true
phase lifts `q_n(theta)` and their integer branch differences `B_n(theta)`,
put

$$
E_{N,h}=\min_\theta\sum_{n=1}^{N-2}
\big[h(r(n+2)-r(n+1))-B_n(\theta)\big]^2.
$$

The minimum is rational and computable over finitely many exact lift cells,
including tied-boundary cases. The paper proves, for every `N>=3`,

$$N-|S_N^U(h)|\ge\frac2{289}E_{N,h}.$$

The authenticated `N=128,h=1` receipt certifies normalized modulus below
`0.759`; the same-forcing terminal-zero changed seed has negligible certified
loss. This is finite source discrimination, not an asymptotic extrapolation.
The adversarial audit also proves the **sharp universal ceiling**
`E_(N,h)<=289(N-2)/4`, attained by alternating opposite phases. Therefore
this instrument alone cannot certify modulus below `(N+2)/2`, even on
examples whose actual sum is zero. It is a useful arithmetic witness and
an explicitly limited intermediate inequality, not a route to normality
without a stronger signed mechanism.

## Routes refuted or sharply limited this round

1. **Scalar primitive carry mass determines the Fourier orbit:** false.
   Dyadic primitivity sees terminal parity, and equal digit marginals admit
   different joint characters. The new alias identity preserves the missing term.
2. **Source packet smoothing supplies decay:** false in this model. Its inverse
   is an explicit signed polynomial in cyclic successor, of operator norm at most 9.
3. **The source time tilt uniquely prescribes cross-time packet correlation:**
   false. Independent redraw and survival/redraw kernels have identical full
   marginals and covariances zero versus a limit `20/81` for odd grade.
4. **The golden-centered first-order third shadow is the true centered
   cumulant:** false. The true third cumulant begins at second order with `8/81`.
5. **Fourth-order coefficient holonomy is a fourth-order selector-free
   arithmetic phase resonance:** false in the fixed-harmonic monomial grammar.
   Its minimum nontrivial invariant degree is 17; the first resonance is just
   `Z_n^16 conjugate(Z_(n+1))=e(-h r(n+1))`, the same for every seed.
6. **The disjoint branch norm 514 also covers adjacent transitions:** false.
   Their shared coordinate changes it to 546; the formal mutant is rejected.
7. **Arbitrarily strong use of this branch-energy inequality alone proves
   normality:** false. Its exact half-modulus ceiling is attained by the
   alternating null-sum control; see the sawtooth covariance proof in the audit.

These counterexamples do not disprove π normality or rule out other mathematical
languages. They reject the displayed implications within their declared domains.

## External arithmetic comparison

The original [Bailey–Crandall paper](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf)
already prints this rational recurrence as equation (3), and makes its
equidistribution conditional on Hypothesis A. Merely recognizing the recurrence
as a rational-function or two-atom system does not discharge that hypothesis.
[Lagarias](https://arxiv.org/pdf/math/0101055) explains that shadowing the
unforced radix orbit holds much more generally, including outside the proposed
arithmetic class. This independently locates the missing arithmetic selection
estimate. We use neither paper's conjectural premise as a theorem.

## Verification, provenance, and next work

See [validation record](OILY_CARRY_RESONANCE_VALIDATION.md),
[hostile audit](OILY_HOSTILE_AUDIT.md), and
[finite signed instrument](OILY_SIGNED_FINITE_INSTRUMENT.md).
Delegated derivations shared a model family and source lineage. Different
reconstructions, exact arithmetic, primary references, and a proof kernel can
fail differently; they are not external mathematical peer review.

The [scoped claim supplement](../../docs/CLAIM_SUPPLEMENT_OILY_CARRY_RESONANCE.md)
records domains, authority and countermodels without creating a global claim
namespace. The [next-round handoff](../../handoffs/OILY_CARRY_RESONANCE_NEXT_2026-10-26.md)
requires a new arithmetic estimate rather than another scalar character or
renaming of the Weyl gate. The current bound remains `N-Omega_h(log N)`.

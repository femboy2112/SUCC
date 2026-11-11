# Obstructions — arguments that were actually tried, and why each fails

Each entry: the attractive mechanism, what was derived, the receipt that kills or bounds it, and
the invariant it was missing. Failures are retained on purpose. Claim references are to
[THEOREMS](THEOREMS.md) and [SCOTT_TRANSPORT](SCOTT_TRANSPORT.md). **π normality remains OPEN.**

## O-1. "The innovation decorrelates from its history, so the lag correlation decays" — REFUTED as an inference

*Mechanism.* Factor `e(h(U_(n+ℓ)-U_n)) = A_n Z_n` with history `A_n = e(h(16^ℓ-1)U_n)` and
innovation `Z_n = e(hΔ_ℓ(n))`; prove `E[Z] → 0` (done: IAD-04); conclude `E[AZ] → 0`.

*Receipt.* The exact gauge identity IAD-05: `A_n = C_n·conj(Z_n)·e(-hτ_n)`. The history factor
contains the conjugate innovation, so `Cov(A,Z) = E[C] + O(|E[Z]| + |h|B^(-2))`: the decoupling
statement **is** the completed correlation. Typed countermodel: the coherent seed `s = -x` has the
same forcing and the same `Z` (so the same `E[Z] → 0`), `A = conj(Z)e(-hτ)`, and `E[AZ] → 1`.

*Missing invariant.* Anything at all about the seed; `Z` is seed-independent.

## O-2. Arithmetic conditional decoupling over a source filtration (Objective A) — NO SHORTCUT

Filtrations examined on the shell with counting measure:

| Filtration `F` | `E[Z | F]` | `A` measurable? | Outcome |
|---|---|---|---|
| trivial | `→ 0` in the window (IAD-04) | no | O-1 |
| full clock `σ(n)` | `= Z`, modulus 1 | yes | no decay; tautological |
| clock residues `σ(n mod q)`, `q·h16^ℓ ≤ (15/8)B³` | `≤ 4401B²/((1-(ℓ+q)/B)h16^ℓ)` uniformly (IAD-04 corollary) | no | a genuine conditional innovation bound, but item 1 fails |
| 2-power clock `σ(n mod 2^k)` | as above | `U_n mod 2^k` **is** measurable (RS-01, 2-adic isometry), the real phase of `(16^ℓ-1)U_n` is not | 2-adic measurability does not transfer (RS-04/RS-08) |
| fresh-prime strata (birth pattern of the window) | not controlled | no | by IAD-09c only an inequation per cell |
| `σ(C)` or `σ(A)` | — | yes | chosen to make the conclusion tautological; rejected by the mission's own rule |

*Receipt.* IAD-05 Corollary 2: for every `F`,
`| ‖E[Z|F]‖_1 - ‖E[C|F]‖_1 | ≤ 2‖A - E[A|F]‖_1 + (π/32)|h|B^(-2)`. A filtration meeting both
requirements of Objective A exists only if the completed orbit already has cell-by-cell lag
cancellation on it, which is stronger than the target. No filtration was found with a
source-derived bound on `‖E[C|F]‖_1`, and none can be found by manipulating the split.

## O-3. "Inherited history is `p`-integral at a fresh prime while the innovation is not, so they are independent" — REFUTED as an inference

*Derived.* IAD-09b: at a prime `p` born in the window the `p`-component of `U_(n+ℓ) - U_n` is
exactly `ρ/p` with `ρ ≡ c·16^(age)`, a deterministic function of the birth pole and the age, and
`U_n ∈ Z_(p)`.

*Receipt.* (i) Integrality is not independence: the fresh component is a fixed number for each
`n`; there is no ensemble over which it varies while the rest is held fixed. (ii) Its only
consequence is the inequation IAD-09c, whose metric content is `1/den = exp(-(6+o(1))n)`.
(iii) On any given shell the hijacked seed of IAD-07 has identical births and identical fresh
components and all lag summands `≈ 1`.

*Not a zero-density issue.* The mean number of births per mesoscopic window is `≈ 2.164·c`
(IAD-09e). Mass is available; cancellation is not.

## O-4. Finite additive-character reciprocity with real lift (Objective B, instrument 1) — REDUCES TO KNOWN-HARD SUMS

For a fresh pole the place weld IAD-09d identifies the `p`-adic component with the real term
`c·16^k/p` modulo one. Summing over birth times turns the fresh-prime sub-ensemble into sums of the
shape `Σ_m e(N/(8m-a))` with `N = h·c·16^k`. For `N ≤ B^K` these are classical van der Corput
sums (the same range as the innovation theorem — nothing new). For exponentially large `N`
(ages `k ≫ (log B)^(3/2)`; this threshold is quoted from memory of the Vinogradov–Korobov range and
is **UNVERIFIED**) no method is known to this dossier; they are of the type "distribution of
`16^k mod m` over `m`". And the fresh-prime sub-sum is not the full phase: the old-prime
complement and the winding are untouched (IAD-07).

## O-5. Complete-conductor, large-sieve and dispersion bounds (Objective B, instrument 3) — LENGTH MISMATCH

- A single place: for one prime `p ≍ B`, the `p`-component of `U_n` runs through
  `16^(n-j)ρ/p` between events, and incomplete geometric sums give square-root cancellation
  (Korobov-type bounds, non-trivial only for length `> √p`). Single-place decay is real and is the
  already-recorded "prime marginals are Haar" phenomenon.
- Several places: the joint component has modulus `q = ∏ p`; a length-`B` sum is non-trivial only
  for `q < B²`, i.e. at most one prime of size `≍ B` plus small ones. The full conductor is
  `exp((6+o(1))n)` (CG-01) against length `B`: the orbit is exponentially sparse in the complete
  CRT ensemble.
- Dispersion over the lag variable is circular:
  `Σ_ℓ |Σ_n e(h(Y_(n+ℓ) - Y_n))|² = Σ_(n,n') Σ_ℓ e(h(Y_(n+ℓ) - Y_(n'+ℓ) - Y_n + Y_(n')))`,
  again lag correlations of the same orbit (an additive-energy form).
- Decisive for finite-horizon arguments: by IAD-07, on any given shell **no** finite set of places
  at finite precision, and no set omitting one place, determines the real phase even up to
  coherence.

## O-6. "The arithmetic can pay: 6 nats of denominator per step exceed log 16 per digit" — REFUTED both ways

*Not necessary.* Stoneham-type constants (TR-04 calibration) are normal while the rational states
`{b^n·(partial sum)}` have denominators of size `≤ n`: polynomial conductor growth.
*Not sufficient.* AT-07: zero seed, every odd conductor depth, completed orbit identically 0.
Conductor growth is neither an entropy source nor a certificate.

## O-7. "A mesoscopic band of favourable lags pays the correlation budget" — BOUNDED (IAD-06)

The Kusmin–Landau band has ratio `(3-δ)/(2+δ) < 2`, supports only the two-point difference set,
and pays at most half of the energy: `limsup |W_B|² ≤ 1/2`. It does not pay the `O(B)` long lags
of the near-pair energy, and it does not need to: multiples `jℓ_0` of one mesoscopic lag would
suffice (the sufficient gate of IAD-06), but for `j ≥ 2` those lie in the aliasing regime.

*How much can positivity alone give? (OBSERVED FINITE, floating-point LP; `band_lp_probe.py`.)*
For positive measures of mass 1 whose Fourier coefficients vanish at every lag in `[a, b]`, the
largest possible atom at frequency 0 (the squared mean) was computed by linear programming on a
grid. It is scale-invariant in `a` and equals `0.5` for a single lag, `≈ 0.4972` at ratio `1.1`,
`≈ 0.4472` (numerically `1/√5`) at ratio `1.5`, and `≈ 0.37` just below ratio `2`. Each value
certifies, to LP tolerance, the *existence* of a positive-definite correlation sequence with that
squared mean and zero band correlations. So, using correlation positivity alone, a band of
bounded ratio can never force `W → 0`; at the Kusmin–Landau ratio the best conceivable constant
is about `0.45`, against `0.5` from the two-point kernel of IAD-06. The closed form `1/√5` is a
numerical observation, not a theorem, and these are general positive-definite sequences, not
unimodular orbit data.

## O-8. "The prescribed schedule `L(B) = ½log_16 B` is a stronger, more informative target" — REFUTED (IAD-02)

The signed Fejér functional is antitone in the window; normality pays every schedule. With the
coarse constant `4/L` the prescribed schedule is uninformative below `B = 16^10` (the sharp form
of (1.2) is informative from `L = 2`); either way the schedule adds no content. What would be
schedule-sensitive is a term-by-term bound over the growing frequency set, a different statement.

## O-9. "Use the irrationality measure of π as the transcendence input" — QUANTIFIED GAP (IAD-08)

Refereed knowledge gives zero-runs at position `B` of length `≤ 6.1033·B`. The wall needs
`≤ B - log_16 B + O(1)` for a *fixed* saving on all large shells; normality needs `o(B)`
(`v_16(π) = 0`). Even the unrefereed claim `μ(π) = 2` would give only `(1+ε)B`. And Diophantine
type is not sufficient: `1/17` satisfies the wall's conclusion and is periodic.

## O-10. "Scott continuity of the weld transports the statistics" — TRUE FOR TRANSPORT, EMPTY AS A SOURCE (SWT-00, SWT-06)

No Scott-open observation implies or refutes normality. Tame channels transport it between names
of the same real, including across the finite/analytic seam (SWT-04), and merging of ω's is free
exactly on the antitone side (SWT-05A). None of this produces cancellation, and the seam-density
statement `ρ(N) = o(N)` itself is not known unconditionally.

## What every failure has in common

Every route above uses only information invariant under at least one of the following changes,
each of which destroys the conclusion:

| Change | Preserves | Destroys |
|---|---|---|
| seed `0 → -x` (coherent) | forcing, innovations, all smooth estimates | everything (orbit ≡ 0) |
| seed `0 → a/q^k` (IAD-07) | the above **and** all places `≠ q` | coherence on a full shell |
| forcing → AT-07 null source | zero seed, complete census, conductor growth | orbit ≡ 0 |
| `x → 1/17` | Diophantine type at `16^B` | equidistribution |

A successful argument must be sensitive to all four at once: the specific forcing, the
authenticated zero seed, the complete place census, **and** something strictly beyond Diophantine
type. No such mechanism was found in this round.

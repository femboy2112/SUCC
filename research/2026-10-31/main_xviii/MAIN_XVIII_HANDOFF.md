# Operation Main XVIII — handoff and next proof-producing attack

**Research-status.** This is the forward pointer for the round after Main XVIII. It states the open
target precisely, names the sharpest current localization, and lists the predeclared falsifiers that
any proposed proof must survive.

## 1. The open target (unchanged firewall)

π base-16 normality is equivalent to the **selected signed Weyl gate**: for every fixed nonzero
integer harmonic `h`,

```
  T_N(h) = Σ_{n ≤ N} e(h · U_n(0)) = o(N)          ⇔        Sbar_N(h) = o(1),
```

with the authentic forcing `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)`,
`r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)`. This remains **OPEN**, along with RH, Weil
positivity (≠ positive covariance), general Collatz, and shifted Lonely Runner `n = 18..94`.

## 2. What Main XVIII added, and what it did not

Main XVIII sharpened the time-correlated form of the gate. The signed lag observable

```
  L_{N,K}(h) = (2 / (K N)) · Σ_{k=1}^{K-1} (1 − k/K) · Re Σ_{n=1}^{N-k} e^{2πi h (16^k − 1) U_n}
```

now has a certified source-transport error at the usable clock depth `K = floor(log_4 N)`, and a
two-scale Jensen argument makes the original and doubled-clock signed criteria **equivalent** inside
the BBP forcing family. A gate equivalence is a criterion; it is not progress on the premise.

Main XVIII did **not** prove the selected zero-boundary signed asymptotic estimate. It added a sharp
hostile **barrier** (at the coherent seed, `K ∼ c·log₁₆ N`, `2 < c < 3`, the reduced lag score tends
to `4/c − 4/c²` while the actual score tends to `1`; the positive gap `(1 − 2/c)²` rules out
seed-uniform vanishing transport at that scale) and two nonnormal counterexample families. These are
negative results that constrain proof routes.

## 3. The next attack

**Prove (or refute) the selected zero-boundary signed asymptotic estimate for fixed nonzero `h`:**
that the signed lag mass of the *authentic zero-seed* orbit vanishes, i.e. the inner signed sums
`Re Σ_{n} e^{2πi h (16^k − 1) U_n}` exhibit genuine cancellation across the whole clock rather than
only the transport reduction. Equivalent reformulations to pursue in parallel:

- the Main XVII **cofiber second-moment / non-conspiracy bound** (NET-XVII-2): a source-derived `L²`
  (not total-variation) bound on the cofiber cross-term of a BBP first-birth window — still the
  sharpest localization of the *untwisted* gate and complementary to the lag observable here;
- the edge-normality gate (`#432`) read beyond nine tomographic modes only with a correct,
  horizon-aware alias analysis;
- a source-derived reason the authentic orbit avoids the coherent-seed barrier of §2 — the barrier
  shows a seed-*uniform* argument cannot work, so the proof must use the specific four-pole forcing.

## 4. Predeclared falsifiers (a proposed proof must survive all of these)

- `s* = −π/16`: same four-pole forcing, genuinely nonnormal orbit `U_n(s*) = −T_n`. A seed-blind
  all-seed normality argument is wrong; it must fail here.
- AT-07 seven-pole null (`z = w − 2r`): zero seed, all odd conductor depths, coherent phases coexist.
- SC-05 block-coherent seeds; horizon-dependent rational coherent seeds `s_K`.
- exact dyadic-rounding near-zero irrational seeds (Weyl sum within `22|h|/(105 M²)` of zero for `M`
  terms, then coherent `O(log M)` later);
- prime-smooth `q = 3^a 5^b` completed orbits with exact limiting signed spectrum `1_{(q/15)|h}` (pass
  arbitrarily many low modes while nonnormal).

Any argument that would also certify one of these as normal is refuted on arrival.

## 5. Standing obligations carried forward

- Main XVII: NET-XVII-2 (above); formalize `w₂ < 28 n²`; a calibrated re-derivation of the `n = 31`
  probe bounds; tighten two `formal/PolyaCoherence.lean` docstrings.
- Keep `formal/` the authority: no paper proof in this round was kernel-checked; new Lean declarations
  are future work, not a Main XVIII deliverable.

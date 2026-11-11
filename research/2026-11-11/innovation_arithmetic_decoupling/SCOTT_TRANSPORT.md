# Scott transport — what the domain order carries even though it cannot see normality

**Baseline:** Main XXIV `071ce1e0`. Companion to [THEOREMS](THEOREMS.md). **π normality remains
OPEN.** Everything proved here is an identity, a transport statement or an interchange lemma; none
is a statistical estimate for π.

**Maintainer's thesis under test.** *"Just because Scott domain theory doesn't 'see' normality
doesn't mean it doesn't provide a channel that accurately transports normality. It reasons in a
way in which all ω's can be considered the same; we need it for welding finite and analytic
places."*

**Verdict in one paragraph.** The thesis is correct in a precise, limited sense, and the limits
are sharp. (1) *Transport:* normality is carried unchanged through every Scott-continuous stream
map that is a density-zero edit of a sliding-block code (SWT-01), and the weld between the finite
places and the analytic place is exactly such a channel: the literal carries of the **rational**
source are a redundant radix-16 name of π/16, and π is normal iff that rational carry stream is
(SWT-02…04). (2) *All ω's the same:* limits over two different ω's may be merged along **any**
cofinal schedule when the statistical functional is antitone in one of them (SWT-05A); the Fejér
window of the Main XXIV handoff is of this kind, which is why its schedule is free (IAD-02). When
the functional is isotone (SWT-05B), merging is precisely the open content. (3) *Limit of the
channel:* transport moves normality between names of the same point; it creates none, and the
hijack theorem IAD-07 shows the "channel" from finite places to the real phase is not even a
function unless the place census is complete.

Status labels as in THEOREMS.md.

## SWT-00 — two conceptual corrections (PROVED LOCAL / CLASSICAL IMPORT)

**(a) Scott topology.** Let `Σ = {0,…,15}`, `D = Σ^* ∪ Σ^ω` with the prefix order (an
ω-algebraic dcpo; Scott-open sets are unions of cylinders `↑w`). Let `N ⊂ Σ^ω` be the normal
sequences. `N` is a Borel set — indeed Π⁰₃-complete (Ki–Linton 1994, CLASSICAL IMPORT). A
Π⁰₃ description **is** an expression of normality as a Borel property of the limit point; high
Borel rank does not make it inexpressible. The legitimate obstruction is order-theoretic:

> For every finite word `w`, the cylinder `↑w` contains normal and non-normal sequences. Hence no
> nonempty Scott-open set is contained in `N` or in its complement, the indicator of `N` is not
> Scott-continuous, and no finite prefix forces or refutes any statistical law.

*Proof.* Append to `w` a normal sequence, respectively `0^ω`; block frequencies ignore finite
prefixes. ∎

**(b) Martingales.** For a deterministic sequence, any probability measure on an index set and any
filtration define conditional expectations, and these can be nontrivial and explicitly bounded:
IAD-04 bounds `‖E[Z | n mod q]‖_∞` for uniform measure on a shell. What is missing is not the
formal existence of conditional laws but a **proved, useful conditional law for the distinguished
arithmetic trajectory** — by IAD-05, precisely a bound on `‖E[C | F]‖_1` for the completed
correlation `C`.

## SWT-01 — the transport lemma (PROVED LOCAL)

Let `A, Γ` be finite alphabets. A *sliding-block code* is `Φ(u)_n = φ(u_n, …, u_(n+m-1))` for a
fixed `φ : A^m → Γ`. Say `v` is a *density-zero edit* of `v'` if `#{n < N : v_n ≠ v'_n} = o(N)`.
A **tame channel** `u ↦ v` is one for which `v` is a density-zero edit of `Φ(u)`.

**Lemma.** (i) If `v` is a density-zero edit of `v'`, then for every word `w` of length `k`,
`|occ_N(w; v) - occ_N(w; v')| ≤ k·#{n < N+k : v_n ≠ v'_n} = o(N)`. (ii) If `u` is generic for a
shift-invariant measure `μ` (all block frequencies converge to `μ`), then every tame image `v` is
generic for `Φ_* μ`. (iii) Tame channels compose. In particular a tame channel with a tame inverse
transports normality in both directions.

*Proof.* (i) A length-`k` window of `v` differs from that of `v'` only if it contains an edited
position, and each edited position lies in at most `k` windows. (ii) Block counts of `Φ(u)` are
finite sums of block counts of `u`; then apply (i). (iii) A sliding-block image of a density-zero
edit is a density-zero edit of the sliding-block image (window `m` multiplies the edit count by at
most `m`). ∎

Tame channels are Scott-continuous when the edit positions are decided by finite look-ahead (as in
SWT-03). Scott continuity alone is **not** enough: the constant map and the map deleting every
second digit are Scott-continuous and destroy normality. The transported invariant is the
statistical tameness, which the order does not see but does not obstruct.

## SWT-02 — the rational source emits a redundant radix-16 name of π/16 (PROVED LOCAL)

For the literal zero seed put `C_n = ⌊U_n⌋` and the **literal carry** `κ_n = C_n - 16 C_(n-1)`
(`n ≥ 1`), exactly as in `integer_bbp_carrier` / the frontier contract (carry 16 is retained).

**Proposition.** `κ_n = ⌊16{U_(n-1)} + r(n)⌋ ∈ {0, 1, …, 16}` for every `n ≥ 1`, and

```text
C_n = Σ_(j=1)^n 16^(n-j) κ_j,        0 < x - C_n/16^n < (1 + T_n)/16^n,        x = Σ_(j≥1) κ_j 16^(-j).
```

*Proof.* `U_n = 16C_(n-1) + 16{U_(n-1)} + r(n)` with `0 ≤ 16{U_(n-1)} + r(n) < 17` (`r(1) = 47/15`
with `U_0 = 0`; `r(n) < 1` for `n ≥ 2`). And `16^n x = Y_n = C_n + {U_n} + T_n`. ∎

So `κ ∈ {0,…,16}^ω` is a base-16 expansion of `x = π/16` over the **redundant** digit set
`{0,…,16}`, computed from rational arithmetic only (no tail, no π oracle). Redundant digit sets
are the classical device that makes real arithmetic prefix-continuous: the BBP source natively
outputs the Scott-admissible name, and the standard hexadecimal digits are its normalization.

## SWT-03 — the seam law (PROVED LOCAL; uses irrationality of π only for finiteness of runs)

Let `ε_n = ⌊Y_n⌋ - C_n` and let `d_n = ⌊Y_(n+1)⌋ - 16⌊Y_n⌋ ∈ {0,…,15}` be the hexadecimal digits
(`d_0 = 3`, `d_1 d_2 … = 243F6A88…`).

**Theorem.** For all `n ≥ 0`:

1. `ε_n ∈ {0, 1}`, and `ε_n = 1 ⟺ {Y_n} < T_n ⟺ {U_n} ≥ 1 - T_n`;
2. `d_n = κ_(n+1) + ε_(n+1) - 16 ε_n` (the integer-carry cocycle of #579);
3. for `n ≥ 1`: `ε_n = 1 ⟹ d_n = 0` and `κ_(n+1) ∈ {15, 16}`;
4. `κ_(n+1) = 16 ⟹ ε_n = 1` and `ε_(n+1) = 0`;  and  `κ_(n+1) = 15` with `ε_(n+1) = 1 ⟹ ε_n = 1`;
5. consequently `ε_n = 1` **iff** the carry stream continues `κ_(n+1) κ_(n+2) … = 15^a 16 …` for
   some finite `a ≥ 0`: the seam is decided by finite look-ahead in the rational stream, and
   `d_n ≠ κ_(n+1)` only for `n` inside or immediately before such a pattern.

*Proof.* (1) `Y_n = C_n + {U_n} + T_n` and `0 < T_n < 1`. (2) `⌊Y_(n+1)⌋ = 16⌊Y_n⌋ + d_n` and
`C_(n+1) = 16C_n + κ_(n+1)`. (3) `{Y_n} < T_n < 1/16` for `n ≥ 1`, so `d_n = ⌊16{Y_n}⌋ = 0`; then
(2) gives `κ_(n+1) = 16 - ε_(n+1)`. (4) `κ_(n+1) = 16` means `16{U_n} + r(n+1) ≥ 16`, i.e.
`{U_n} ≥ 1 - r(n+1)/16 > 1 - T_n` because `T_n = r(n+1)/16 + T_(n+1)/16`; so `ε_n = 1`, hence
`d_n = 0` and (2) gives `ε_(n+1) = 0`. If `κ_(n+1) = 15` and `ε_(n+1) = 1`, (2) gives
`d_n = 16 - 16ε_n ≤ 15`, forcing `ε_n = 1`. (5) By (3) a run of `ε = 1` reads `15, 15, …` in `κ`
until a 16 ends it, and by (4) the pattern conversely forces the run backwards. A run cannot be
infinite: `ε_n = 1` for all `n ≥ n_0` would give `d_n = 0` for all `n ≥ n_0`, so `x ∈ Q`. ∎

Controls. The coherent seed `s = -x` has `U_n(s) = -T_n`, `C_n = -1`, `κ ≡ 15`, `ε ≡ 1`: an
infinite seam run, legal because its completed point `x + s = 0` is rational. The finiteness
clause therefore genuinely uses the seed. RIO-09/RIO-10 of `inertial_origin_q6` give further
source-only constraints on the 17-letter carry language (zero-carry runs `< 2log_16 n + O(1)`;
`16 → 0`).

**Seam density.** Put `ρ(N) = #{n < N : ε_n = 1}`. From (5), with `a_j` the length of the maximal
run of 15's ending at position `j-1` of `κ` and `b_N` the length of the maximal run of 15's ending
at position `N`:

```text
ρ(N) ≤ Σ_(j ≤ N, κ_j = 16) (1 + a_j)  +  1 + b_N        (a bound in source-side data only).
```

`ρ(N) = o(N)` is implied by normality of either stream (next theorem) but is **not known
unconditionally**: it says that the positions followed by `≈ 2 log_16 n` zeros have density zero in
the hexadecimal expansion of π. Heuristically `Σ_n T_n < ∞` predicts only finitely many seam
events; none occurs for `n ≤ 1300` (OBSERVED FINITE, see PROBES). **OPEN**, strictly weaker than
normality.

## SWT-04 — normality is transported across the finite/analytic weld (PROVED LOCAL)

**Theorem.** The following are equivalent.

1. `x = π/16` is normal in base 16 (every block `w ∈ {0,…,15}^k` has limiting frequency `16^(-k)`
   in `d`).
2. In the rational carry stream `κ^+ = (κ_(n+1))_(n≥0)`, every block `w ∈ {0,…,15}^k` has limiting
   frequency `16^(-k)`.

In either case the letter 16 has frequency 0, `ρ(N) = o(N)`, and for every block `w` of length `k`

```text
| occ_N(w; d) - occ_N(w; κ^+) | ≤ 2k · ρ(N + k).
```

*Proof.* By SWT-03(2), `d_n ≠ κ_(n+1)` only if `ε_n = 1` or `ε_(n+1) = 1`; this is the displayed
inequality (SWT-01(i)). (1)⟹`ρ = o(N)`: `ε_n = 1` forces `{Y_n} < T_n < 1/(64n²)`, so for each
fixed `K` and all large `n` the block `0^K` occurs at position `n`; its frequency is `16^(-K)`, so
`limsup ρ(N)/N ≤ 16^(-K)` for every `K`. (2)⟹`ρ = o(N)`: the sixteen single-letter frequencies
sum to 1, so the letter 16 has frequency 0. Fix `K`. In the seam-density bound, the terms with
`a_j < K` contribute at most `K·#{j ≤ N : κ_j = 16} = o(N)`; positions inside a run of 15's of
length `≥ K` number at most `2·occ_N(15^⌈K/2⌉; κ) + K = 2N·16^(-⌈K/2⌉) + o(N)`, which also bounds
`b_N` and the remaining terms. Let `K → ∞`. Then transport the block frequencies. ∎

**Reading.** The Archimedean tail `T_n` is statistically invisible: it acts only on the seam set,
which has density zero under either hypothesis. *All of the normality of π lives in the integer
parts `⌊U_n⌋` of rational numbers whose complete prime genealogy is known* (CG-01, IAD-09). This is
the exact weld of the finite and analytic places requested by the thesis, in symbolic form; it is
the digit-level counterpart of the LL-02 transfer `|J^x - J^u| ≤ 8q²/(15(A+1)²)`. It is an
equivalence, not an estimate, and it is recorded as such.

## SWT-05 — when all ω's are the same: the one-sided interchange lemma (PROVED LOCAL)

Let `a(B, λ) ∈ [0, ∞)` be defined for a shell index `B` and a second index `λ ∈ N` (window, lag
band, resolution, depth).

**(A) Antitone side — every schedule agrees.** Suppose `a(B, λ') ≤ a(B, λ) + λ/λ'` for all
`λ ≤ λ'`, and `lim_B a(B, λ) = α_λ` for each fixed `λ`. Then for **every** `λ(B) → ∞`:

```text
limsup_B a(B, λ(B)) ≤ inf_λ α_λ.
```

*Proof.* `limsup_B a(B, λ(B)) ≤ α_λ + limsup_B λ/λ(B) = α_λ` for each `λ`. ∎

**(B) Isotone side — the schedule is the content.** Suppose `a(B, ·)` is nondecreasing and
`lim_B a(B, λ) = α_λ` with `α_∞ = sup_λ α_λ < ∞`. Then *some* `λ(B) → ∞` has
`limsup_B a(B, λ(B)) ≤ α_∞` (diagonal extraction), but a prescribed schedule may fail.

*Proof.* Choose `B_1 < B_2 < …` with `a(B, λ) ≤ α_λ + 1/λ` for `B ≥ B_λ` and set
`λ(B) = max{λ : B_λ ≤ B}`. ∎

**Instances.**

| Interface | Functional | Side | Consequence |
|---|---|---|---|
| Source depth `L` in `U_n + T_n^(L)` (causal weld) | nested rational intervals | fully directed in the interval domain | ordinary Scott continuity: exact weld, both limits commute |
| Fejér window of the handoff | `a = √γ_L` (IAD-02, (2.1)) | **A** | every schedule `L(B) → ∞` is the same statement as normality |
| von Neumann window means of any bounded sequence | `‖window mean‖²` | **A** | finite form of the mean ergodic theorem |
| Near-pair energy `J_(A,q) = ‖μ_A * g_q‖²` (LL-01) | isotone in `q` along divisibility | **B** | a slow diagonal `q_A` is free; a prescribed `q_A` is genuine content; `J_(A,q) ≥ q/A` |

(For LL-01: `g_q` is the average of `k` translates of `g_(kq)`, so `‖μ * g_q‖ ≤ ‖μ * g_(kq)‖` by
Minkowski; and the diagonal of the pair sum gives `J ≥ q/A`.)

**Domain reading.** Write `𝕌 = ([0,∞], ≥)` for the upper reals and `𝕃 = ([0,∞], ≤)` for the lower
reals; Scott-continuous maps into them are the upper/lower semicontinuous functionals. In case A
the net `λ ↦ a(B, λ)` increases in `𝕌`: a longer window is *more information*, and the target
statement "`inf = 0`" is a directed supremum. The lemma is then a diagonal lemma that needs
monotonicity in **one** index only: the ω of windows and the ω of shells may be merged along any
path that is cofinal in the sense of D-2 of `scott_omega_causal_weld/SCOTT_COFINAL_SCHEDULE.md`,
although `a` is not monotone in `B` at all. In case B the net increases in `𝕃` and the target
"`sup < ∞`" is an upper bound on a directed family — the one kind of statement the order cannot
help with (here the supremum over `q` is the `L²` norm of an atomic measure, i.e. `∞`).

So "all ω's can be considered the same" is a **theorem on the 𝕌-side and false on the 𝕃-side**.
This is a usable sorting rule for future interfaces: put the open statement in antitone form and
its schedule is free; if it is only available in isotone form, the schedule *is* the missing
estimate.

## SWT-06 — what the channel cannot do (PROVED LOCAL, by reference)

- **Transport creates nothing.** SWT-01 and SWT-04 move normality between two names of the same
  real number. Every hostile seed is transported just as faithfully: the coherent seed is carried
  to `κ ≡ 15`.
- **The finite places alone are not a domain of definition.** By IAD-07, for every odd prime `q`
  there are seeds with identical data at all places `≠ q` and completed orbit `≈ 0` on a whole
  shell. A "channel" from an incomplete place census to the real phase is not single-valued, so
  there is nothing for Scott continuity to transport. The weld requires the complete census plus
  the integer floor — which is exactly the object `⌊U_n⌋` of SWT-02.
- **The 2-adic clock is not an entropy source.** RS-04 of `adelic_return_bridge` shows there is no
  measurable equivariant Haar-to-Haar map from the 2-adic odometer to the `×16` circle map
  (entropy 0 versus `log 16`). A tame channel preserves limiting block statistics (SWT-01(ii)), so
  it cannot originate at a zero-entropy clock.
- **A capacity heuristic that fails.** "The rational state gains `6` nats of denominator per step
  (CG-01), more than the `log 16 ≈ 2.77` nats per digit, so the arithmetic can pay for normality"
  is neither necessary nor sufficient; see OBSTRUCTIONS O-6.

**Classical frame (CLASSICAL IMPORT, cited for orientation, not used in proofs):** normality is
finite-state incompressibility (Schnorr–Stimm; Dai–Lathrop–Lutz–Mayordomo), and is preserved by
rational affine maps (Wall) and finite-automaton selection (Agafonov); finite-state dimension is
preserved by rational arithmetic (Doty–Lutz–Nandakumar). SWT-01 is the elementary special case
needed here. Citations and verification status are in [SOURCE_MAP](SOURCE_MAP.md).

# Dual radix completion: mirror–remainder, 2/3/5 clocks, and the Collatz zero seam

**20 November 2026 · additive SUCC research, review-only.** Base: [PR #679](https://github.com/femboy2112/SUCC/pull/679), original four-pole source and zero seed untouched. This dossier tests the proposal that the **plain mirror is the digit-complement bookkeeping frame**, while the **transmitted remainder carries the next causal distinction**, and that the `16=4²`, `3`, and `5` arithmetic create a meaningful bridge to Collatz. Statements below are new-to-this-SUCC arrangement of elementary/classical results, not novelty claims. **General Collatz, π base-16 normality (including R0), and RH remain OPEN.**

## Frozen input and essential types

Let `b=16`, `d_j∈{0,...,15}`. The real fractional point is `x_R=Σ_(j>=1)d_j/16^j` (converges in R); the *separately constructed* 2-adic digit shadow is `y_2=Σ_(j>=1)d_j16^(j−1)` (converges in Z_2). **These are two representations of a digit sequence, not an identification of real π with a pre-existing 2-adic π.** A 3-adic observer of *finite ledgers* is distinct again: no unrestricted `Σ 16^j` convergence in Q_3. The current finite source register is `M_n=floor(16^n x_R)=Σ_(j<=n)d_j16^(n−j)`, for a nonambiguous infinite expansion; its successor is `M_(n+1)=16M_n+d_(n+1)`. A 2-adic shadow *prefix register* is `Y_n=Σ_(j<=n)d_j16^(j−1)` and is the radix reversal of `M_n`.

The only authentic BBP source used in DRCS-09 is `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U0=0`, `x_R=π/16=Σ16^(−n)r(n)` via classical BBP, including exact tail. Constant-digit and altered-seed models are separately labelled controls. Distinguish the general radix `16`, the auxiliary Fibonacci H-root geometry of #678, and the actual π orbit.

## DRCS-01 — The ordinary mirror IS an exact 16-channel bookkeeping symmetry (CLASSICAL, PROVED)

On a non-boundary `x∈(0,1)`, put `d=floor(16x)`, `r=16x−d∈(0,1)` and mirror `R(x)=1−x`. Then

\[
\boxed{D_{16}(1-x)=(15-d,\,1-r),\qquad D_{16}(x)=(d,r).}
\]

The exception at `r=0` is real: at a threshold the right/left canonical expansion differs, so use the two-sided boundary or a declared half-open convention. For full *infinite* digit words, the symbolic mirror `\bar d_j=15−d_j` always defines both completed representations. It yields

\[
\boxed{x_R(\bar d)=1-x_R(d),\qquad y_2(\bar d)=-1-y_2(d).}
\]

Proof: the complementary digit sums are `Σ_(j>=1)15/16^j=1` in R and `Σ_(j>=0)15·16^j=15/(1−16)=−1` in Z_2.

**Wave-level statement, not just point coordinates:** import the already PROVED unitary split of #679, `(Uf)_d(r)=f((d+r)/16)/4` from `L²([0,1])` to `⊕_d L²([0,1])`. Let `(R f)(x)=f(1−x)` and `(\widetilde Rg)_d(r)=g_(15−d)(1−r)`. Then

\[
\boxed{UR=\widetilde R U}\quad\text{(almost everywhere)}.
\]

Both sides are unitary involutions. Proof: `1−(d+r)/16=(15−d+1−r)/16`. This is a literal, calibrated **basis-independent mirror/bookkeeping intertwiner**; the through-slit remainder and complement carry all phase-state information **if the digit and orientation are retained**. It generates no additional independent bits and is not a physical mirror-scattering Hamiltonian.

## DRCS-02 — One chronological word, two completions, one symbolic successor (CLASSICAL, PROVED)

The full sequence space `Σ={0,...,15}^N` maps injectively to `Z_2` by `d↦y_2`, with inverse recovering each successive low 4-bit nibble. It maps onto `[0,1]` by `d↦x_R`, with only the familiar base-16 terminating/recurring-F ambiguities; choose canonical expansions to remove them except explicit endpoints.

Let `σ` delete the first digit; for a symbolic sequence `d=(d1,d2,...)`,

\[
\boxed{x_R(σd)=16x_R(d)-d_1,\qquad y_2(σd)=\frac{y_2(d)-d_1}{16}.}
\]

The first is a real expanding successor, the second the 2-adic digit shift, both acting on the same ordered digit record. **This is not a direct continuous ring isomorphism** between R and Q_2. In either branch, the digit plus remainder reconstructs the input: `x=(d+x_next)/16` in R, `y=d+16 y_next` in Z_2. The complement `d↦\bar d` commutes with symbolic deletion `σ` and changes frames by the affine involutions above.

**Normality transport (exact equivalence, not proof):** for the original π word define `y_π=Σ_(j>=1)d_j(π/16)16^(j−1)∈Z_2`. For every `k`, `σ^n(y_π) mod16^k` is the length-k chronological word beginning at digit `n+1` (read from low to high nibbles). The empirical shifts `N^(-1)Σ_(n<N)δ_(σ^n y_π)` converge weakly to Haar on Z_2 **if and only if** π is normal in base 16. Proof: the clopen residue cylinders modulo `16^k` generate the 2-adic Borel topology and have Haar mass `16^(−k)`. This changes the *observer representation*, not the unknown signed frequency estimates.

## DRCS-03 — The 2↔3↔5 reciprocal radix triangle (EXACT elementary)

Let

\[
J_n=\frac{16^n-1}{15}=\underbrace{11\ldots1}_{n\ \mathrm{hex\ digits}},\quad
A_n=5J_n=\underbrace{55\ldots5}_{n},\quad
B_n=3J_n=\underbrace{33\ldots3}_{n}.
\]

Then the *same finite clock* simultaneously satisfies

\[
\boxed{3A_n+1=5B_n+1=15J_n+1=16^n=2^{4n}.}
\]

More generally for `q∈{3,5,15}`, set `d_q=15/q` and `D_(q,n)=d_q J_n`. Then `qD_(q,n)+1=16^n` identically, and the written hexadecimal digits are all `d_q`. The **real right-infinite** constant-digit word represents `+1/q`, while the **2-adic left-infinite** same digit word represents `−1/q`:

\[
\boxed{0.\overline{d_q}_{16}=\frac1q\quad(\mathbb R),\qquad
\ldots\overline{d_q}_{16}=-\frac1q\quad(\mathbb Z_2).}
\]

Both are fixed points of the respective base-16 digit-shift map, under the common symbolic model. The 3-branch is **ordinary Collatz**; the 5- and 15-branch identities are `5x+1`, `15x+1` controls, **not** 3x+1 dynamics.

The mirror of `A_n` is `\bar A_n=16^n−1−A_n=10J_n=2A_n` (hex A's). It obeys `3\bar A_n+2=2·16^n` but `3\bar A_n+1=2·16^n−1` is odd. Therefore **the radix mirror is NOT a conjugacy of the ordinary Collatz map**, even though it is an exact conjugacy of digit bookkeeping. Already `5` (odd) and `A_hex=10` (even) give a concrete parity counterexample.

## DRCS-04 — The same journals are clock-isometric at 3 and 5, attracting at 2 (CLASSICAL LTE)

For distinct `m,n≥0`, and `p∈{3,5}`, the lifting-the-exponent lemma applied to `16^|m−n|−1` gives

\[
\boxed{v_p(J_m-J_n)=v_p(m-n).}
\]

Therefore the time-labelled map `n↦J_n` extends to an isometry from Z_3 to Z_3 and from Z_5 to Z_5 (the odometers of #675). Multiplying by the digit `5` or `3` changes precision:

| State | 3-adic clock difference | 5-adic clock difference | 2-adic chronological limit |
|---|---|---|---|
| `A_n=5J_n` | `v3(m−n)` | `v5(m−n)+1` | `−1/3` |
| `B_n=3J_n` | `v3(m−n)+1` | `v5(m−n)` | `−1/5` |
| `J_n` | `v3(m−n)` | `v5(m−n)` | `−1/15` |

Since `qD_(q,n)+1=16^n`, `v2(qD+1)=4n`, proving the limits. In *ordinary* increasing integer time there need not be a 3-adic limit: this is an isometric **clock-time extension** from `n∈Z_3`, not a convergence claim as real `n→∞`.

## DRCS-05 — Exact Collatz suffix-peeling theorem (PROVED, all integer inputs)

Let `C(N)=N/2` if `N` even, and `(3N+1)/2` if `N` odd, with `N>0`. Fix `k≥1`. The following are equivalent for every integer `N≥0`:

\[
\boxed{16^k\mid 3N+1}\quad\Longleftrightarrow\quad
\boxed{N\equiv\underbrace{55\ldots5}_{k}\pmod{16^k}}.
\]

Because 3 is a unit modulo `16^k`, the solution of `3N+1≡0` is unique; it is `5J_k` by DRCS-03. When the condition holds, write `N=16^k A+5J_k` with `A≥0`. Then

\[
\boxed{3N+1=16^k(3A+1),\qquad C^{4k}(N)=3A+1,\qquad v_2(3N+1)=4k+v_2(3A+1).}
\]

The first Collatz step is odd and creates `2^(4k−1)(3A+1)`; the following `4k−1` steps are even halvings, so the equality has no assumed Collatz convergence. Each trailing hexadecimal **5** is literally four shortcut Collatz halvings once the `3N+1` numerator has been formed. For `N=A_k=5J_k` the prefix `A=0`, giving `C^(4k)(A_k)=1`. This proves only the explicitly identified family, **not universal Collatz**.

**Maximum valuation among n-digit registers:** for `0≤N<16^n`, `v2(3N+1)≤4n`, with equality **only** at `N=A_n`. Indeed `3N+1<3·16^n`; if its 2-adic valuation exceeded `4n`, it would have to equal `2·16^n` (the only possible power of 2 in range), but that is `2 mod3`, unlike `3N+1≡1 mod3`.

## DRCS-06 — The accelerated odd Collatz map is singular exactly at the 2-adic zero seam (PROVED)

On positive odd integers define `C_odd(N)=(3N+1)/2^{v2(3N+1)}`. The sequence `A_n` tends in Z_2 to `−1/3`, and `C_odd(A_n)=1` for every `n`. But the distinct odd sequence `A_n+2·16^n` tends to the **same** 2-adic limit and satisfies

\[
\boxed{C_{odd}(A_n+2\cdot16^n)=7}\quad\forall n≥1.
\]

Proof: `3(A_n+2·16^n)+1=7·16^n`, with 7 odd. The map `C_odd` has **no continuous extension at `−1/3`** (two approaching sequences yield 1 and 7). At that limit the numerator `3x+1` vanishes 2-adically, so its finite 2-adic valuation ceases to exist. The unaccelerated shortcut map `C` does extend to `−1/3` and sends it to `0` in one step; do not conflate these domains. In fact for each *fixed* `j≥1`, `C^j(A_n)→0` in Z_2 as `n→∞`, while the **moving** horizon `C^(4n)(A_n)=1` for all n. This is an explicit nonuniform finite/completed observation boundary, not an infinite-time physical traversal or a proof of a positive-integer orbit property outside the family.

## DRCS-07 — A first-mismatch valuation instrument (PROVED exact)

For `q∈{3,5,15}` let `d=15/q` and let `y∈Z_2` have radix-16 digits `(a_1,a_2,...)` from least significant to most. If the first k digits equal `d`, and the next is `a_(k+1)≠d`, then

\[
\boxed{v_2(qy+1)=4k+v_2(a_{k+1}-d).}
\]

Proof: `y=d J_k+16^k(a_(k+1)+16z)`, so `qy+1=16^k(1+q a_(k+1)+16qz)`. Using `1+qd=16`, the bracket is `q(a_(k+1)−d) mod16`. Since `0<|a_(k+1)−d|<16` and `q` is odd, its valuation is 0,1,2 or3 and cannot be changed by the higher multiple of16. An indefinitely constant word is the actual 2-adic root `y=−1/q` with `qy+1=0`.

This is the requested extra information in the **transmitted remainder**: the first mismatch and up to three sub-nibble precision bits are objectively encoded in the 2-adic response of the full digit history, even if a coarse reflected-digit head saw only the prior repeated channel. It is also a testable *observer readout formula*, not a source-dependent π normality estimate.

## DRCS-08 — A three-head 2/3/5 digit recovery code (CLASSICAL, exact and minimal for declared heads)

For *arbitrary* hexadecimal digits, the finite prefix ledger obeys `M_(n+1)=16M_n+d_(n+1)`. Consequently

\[
M_{n+1}\equiv M_n+d_{n+1}\pmod3,\quad
M_{n+1}\equiv M_n+d_{n+1}\pmod5,\quad
M_{n+1}\equiv d_{n+1}\pmod2.
\]

If the previous `M_n mod15` is retained, and three calibrated next-state heads supply `M_(n+1) mod3`, `mod5`, and `mod2`, their data uniquely reconstruct `d_(n+1)∈{0,...,15}`. The first two give digit mod15, leaving only possible collision `0` versus `15`; parity distinguishes them. Removing any one of the three heads permits some digit collision (in the declared unconditioned digit family). This is an exact GPS/error-correcting *acquisition* example with restricted scalar readouts, **not** guaranteed correction of a corrupted head or a proof of physical independence.

## DRCS-09 — A canonical 2-adic digit shadow of the authenticated BBP source (SOURCE-SPECIFIC FINITE)

The original zero-seeded four-pole BBP identity, together with the positive rational tail bound `0<x−P_M<16^(−M)r(M+1)/15`, verifies its first 12 digits **`3243F6A8885A`**, where `x=π/16`. Define the 2-adic digit shadow

\[
\boxed{Y_\pi=\sum_{j≥1}d_j(\pi/16)16^{j-1}\in\mathbb Z_2.}
\]

Its finite source-certifiable prefix is `Y_π≡0xA5888A6F3423 mod16^12`. In particular `Y_π≡0x23=35 (mod256)`, reflecting first digits `3,2`. For the `5x+1` observer, `y=3+16y_tail` gives `5y+1=16(1+5y_tail)`. Because `y_tail≡2 mod16` (the second digit),

\[
\boxed{v_2(5Y_\pi+1)=4,\qquad v_2(3Y_\pi+1)=1.}
\]

The first value is *one hexadecimal digit* of agreement with the repeated-3 2-adic root `−1/5`, followed by an immediate departure: `((5Y_π+1)/16) mod16=11`. The occurrence of 11 here is a two-digit elementary residue, **not** an authenticated identification with #670's 11-adic Fibonacci eigenchannel. Crucially **`Y_π` is a digit-coded 2-adic companion, not a literal identification of transcendental real π as a 2-adic scalar.** This result is finite and known from the BBP digits, and supplies no asymptotic normality estimate.

## DRCS-10 — Collatz-valuation cylinder criterion for base-16 normality and R0 (EXACT CONDITIONAL)

For any nonambiguous real hexadecimal digit sequence, let `M_n` be its n-digit integer prefix. For `q∈{3,5,15}` and `d=15/q`:

\[
\boxed{v_2(qM_{n+k}+1)\ge4k\quad\Longleftrightarrow\quad
(d_{n+1},\ldots,d_{n+k})=(d,\ldots,d).}
\]

This is DRCS-05's modular inverse with 3 replaced by any odd q dividing15. Equivalently the 2-adic shadow's shift obeys `v2(qσ^nY+1)≥4k`. If the real number is base-16 normal, these event frequencies tend to `16^(−k)` for every fixed k. **The converse for this restricted family of constant-digit words is false in general**, since it doesn't test all 16^k words.

For π's actual phases `θ_n={16^nπ/16}`, if for some `q∈{3,5,15}` the `k=1` events have positive lower density on every late dyadic integer shell, then R0 follows. Indeed for each event, `θ_n∈[d/16,(d+1)/16)` and `1−cos(2πθ_n)≥1−cos(2πd/16)>0` (as `1≤d≤5`). This is a **conditional quantitative certification path**, not an established event-density bound for the actual source. It must not be used as a hidden assumption to claim π-normality.

## DRCS-11 — No direct 2-adic ↔ 3-adic additive chart (EXACT NO-GO)

Every continuous additive group homomorphism `f:Z_2→Z_3` is zero. Proof: integers are dense in Z_2, so let `a=f(1)∈Z_3`. Since `2^k→0` in Z_2, continuity would force `2^k a→0` in Z_3. But `|2^ka|_3=|a|_3` for all k; hence `a=0`, and density gives `f=0`. Thus the 2/3/5 link above is the **same integer chronology and its different completions**, not a secretly assumed continuous isomorphism transporting 2-adic state to a 3-adic clock. The 3-adic odometer theorem applies to the special affine geometric clocks, not to every arbitrary BBP digit prefix as `n→∞`.

## DRCS-12 — Steelman, crucible, verdict

**SURVIVES / proved with explicit scope:** the mirror is an exact 16-way unitary bookkeeping symmetry; the same ordered digits admit real and 2-adic completions with opposite constant-digit fixed points; the universal radix16 clock carries exact 3/5-adic odometers; one family of Collatz odd-to-one preimages is literally repeating hexadecimal 5s; each trailing 5 induces four shortcut halvings; the accelerated odd Collatz map has a nonextendable 2-adic seam at `−1/3`; the first mismatching digit produces an exact valuation defect; calibrated 2/3/5 observer heads recover one digit; the original BBP first-12 source digits specify a canonical finite 2-adic shadow and known valuation probes.

**REFUTED shortcut:** the ordinary radix mirror is an autoconjugacy of Collatz (`5 ↔ 10` disproves it); 3/5 clocks establish that the actual π orbit is equidistributed (constant-digit periodic sources satisfy all clock identities); a 2-adic digit encoding is an intrinsic embedding of real π into Q_2; source-filter H's auxiliary 5/11 determinants supply a proved map to the universal q=3,5 radix fixed points; or finite BBP digit certificates prove an infinite lower-density theorem.

**OPEN:** derive a **genuinely source-specific** long-range signed inequality from the original zero-seeded four-pole source, in the transmitted-remainder/prime-cofactor observer frame, forcing late-shell R0 and ultimately every Weyl mode. The source-dependent bound must fail on same-forcing wrong-seed controls and survive source mutations, moving-frame dephasing, phase aliases, and cold shells.

## Provenance / classical antecedents

- Inherits #679 digit/remainder unitary and #675 base16 3/5-adic odometers; no claims to originate standard base-expansion arithmetic, LTE, 2-adic Collatz parity theory, Pontryagin/Haar, or exact coding-theoretic rank criteria.
- Prior SUCC research [#667](https://github.com/femboy2112/SUCC/pull/667) contains distinct 2/3/5 Fibonacci clocks and Collatz branch-cylinders; [#670](https://github.com/femboy2112/SUCC/pull/670) contains *auxiliary* 11-adic source eigenchannels; [#676](https://github.com/femboy2112/SUCC/pull/676) contains observer-headed source reconstruction. The present statements do not import those unrelated sources as independent derivations.
- Source on 2-adic Collatz parity/autoconjugacy (different from our mirror): Monks and Yazinski, *The autoconjugacy of the 3x+1 function* (Discrete Math 2004), https://doi.org/10.1016/S0012-365X(03)00125-0 . Our ordinary base16 complement is **not** their Collatz parity-vector autoconjugacy.
- Independent executable finite checks in `test_dual_radix.py` and `independent_audit.py`; all finite tests are calibration, not universal proof or external peer review.

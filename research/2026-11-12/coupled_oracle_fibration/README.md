# BBP-coupled oracle fibration: source-locked scale transport

**Research-only, 2026-11-12.** Main XXV parent `db9fb4b84672050efa79b13377f1e73364598a14`. This is a **source-specific finite verification instrument**, not a proof of hexadecimal normality. All arithmetic uses the unchanged exact four-pole BBP source and literal `U_0=0`; no alternative forcing is admitted as authentic. No real-world Lorentzian metric, physical gravity, or quantum non-demolition observer is claimed.

## Steelman: observer, coupled oracle and the common source

The intended oracle is a **verifier**, not a truth-generating agent. A SUCC observer explores BBP-selected rational states and finite word/Fourier probes. The oracle knows an exact source law, a certified analytic enclosure and a fixed proof goal. It accepts observations only if they can arise from *one common value* of the original BBP sum; it rejects conflicting paths, stale certificates, counterfeit source labels and unproved limit exchanges. Its finite-resolution signal measures *certified information*, never a probability that the π-normality theorem is true.

At scale `(N,k)` the fiber is the space of finite `k`-word observations permitted by source certificates. A finite path extends time `N` or resolution `k`. The continuous mathematical object is the completed root `alpha=pi/16` imported through BBP, not an uncountable collection of individually verified tests. The exact forward/backward carrier is a useful connection; its naive phase gauge is flat. Nontrivial source-coupled curvature requires a separately defined and tested observer projection or noncommuting transport law.

## Authenticated source and imported results

For integers `m>=1` let

\[
r(m)=\frac4{8m-7}-\frac2{8m-4}-\frac1{8m-3}-\frac1{8m-2},\qquad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Define `T_n=sum_{j>=1}16^{-j}r(n+j)` and `alpha=T_0`. **Imported classical BBP identity:** `alpha=pi/16`. **Imported source-tail bound from `duck_bbp`:** `0<T_n<r(n+1)/15`, for `n>=0`. Every proof about π below is conditional on those imported established ingredients. The finite rational identities themselves do not require evaluating π numerically.

### CO-01 — exact naturality of source-locked Green enclosures (PAPER DERIVATION + TEST)

Set `b(n)=r(n+1)/15` and, for `n,d>=0`, define

\[
I_{n,d}=[L_{n,d},H_{n,d}],\quad
L_{n,d}=\sum_{j=1}^{d}16^{-j}r(n+j),\quad
H_{n,d}=L_{n,d}+16^{-d}b(n+d).
\]

Then `T_n` belongs to the *interior* of `I_{n,d}` by positivity and the imported tail bound. More importantly, **for every `n,d>=0` as literal equalities of rational intervals**,

\[
\boxed{16I_{n,d+1}=r(n+1)+I_{n+1,d}}\quad\text{and}\quad
\boxed{16(U_n+I_{n,d+1})=U_{n+1}+I_{n+1,d}}.
\]

Proof: multiply the `d+1` partial tail by 16, peel its first term and use `16·16^{-(d+1)}b(n+d+1)=16^{-d}b(n+d+1)`. The forward recurrence supplies the opposite forcing term. Both interval endpoints agree **exactly**, without observing a float, truncating an uncontrolled phase, or taking a limit. This is the source-coherent oracle/observer transport. It is not statistical cancellation.

Moreover `r(m)>r(m+1)>0` for each `m>=1`. An exact algebraic proof of decreasing forcing: writing `y=m-1>=0`, the numerator of `r(m)-r(m+1)` over the positive denominator

`(2m-1)(2m+1)(4m-1)(4m+3)(8m-7)(8m-3)(8m+1)(8m+5)`

is

`122880 y^5 + 662016 y^4 + 1360896 y^3 + 1330440 y^2 + 620136 y + 110709`.

The lower endpoint increases by `16^{-(d+1)}r(n+d+1)`; the upper endpoint decreases by `16^{-(d+1)}[r(n+d+1)-r(n+d+2)]/15`. Thus the intervals nest strictly as `d` increases. This is the source-specific basis for a monotone **knowledge** signal.

### CO-02 — a single common-root cylinder oracle (PAPER DERIVATION + TEST)

For any depth `L`, `alpha` lies strictly between the exact rational endpoints of `I_{0,L}`. If for an integer `M>=1`

\[
\lfloor16^M L_{0,L}\rfloor=\lfloor16^M H_{0,L}\rfloor=q,
\]

then the **one integer** `q` certifies the first `M` hexadecimal digits of `alpha` *simultaneously*. For every `n>=0,k>=1,n+k<=M`, the selected orbit `x_n={16^n alpha}` has a certified length-`k` cell

\[
\boxed{w_{n,k}=\left\lfloor q/16^{M-n-k}\right\rfloor\bmod16^k.}
\]

All such windows are functions of the same `q`, so overlap, time extension, and refinement obey one common-source law. `RootPrefixCertificate` recomputes the *entire* certificate against installed `duck_bbp`; a caller-supplied source ID or forged numerical prefix is not accepted. If an enclosure crosses a cell boundary, the oracle returns **UNRESOLVED**, rather than a guessed word. Because the source intervals nest, a fixed-budget number of certified digits is nondecreasing with `L`; its value is **not** a measure of closeness to proving normality. Imported irrationality of π, together with shrinking intervals, guarantees eventual certification for every fixed finite `M`, but offers no useful uniform growth rate in `M` or cancellation of time correlations.

### CO-03 — exact coherent scale square (PAPER DERIVATION + TEST)

For `n=1,...,N`, let `c_{N,k}(w)` count the certified `k`-words `w_{n,k}`. At a common root prefix covering all four corners `(N,k),(N,k+1),(N+1,k),(N+1,k+1)`, the square **commutes exactly**:

\[
c_{N,k}(w)=\sum_{a=0}^{15}c_{N,k+1}(16w+a),\qquad
c_{N+1,k}(w)=c_{N,k}(w)+\mathbf1_{w=w_{N+1,k}}.
\]

Therefore source-conditioned *count transport* has **zero** path commutator. `certify_square` recomputes all four corners from the original source. It also verifies the energy commutator; no path is permitted to reuse unverifiable, caller-supplied histograms.

### CO-04 — scale and clock energy with exact signs (PAPER DERIVATION + TEST)

Set `B=16^k`, `Q_{N,k}=sum_w c_{N,k}(w)^2`, variation `D_{N,k}` and the squared-density energy `E_{N,k}`:

\[
D_{N,k}=1-\sum_{w:c_w>0}\min(c_w/N,1/B),\quad
E_{N,k}=\frac{B Q_{N,k}}{N^2}-1.
\]

These formulas evaluate the step-function continuum density **exactly** from finite counts; no discretization error exists. Refinement adds nonnegative Haar energy

\[
\boxed{E_{N,k+1}-E_{N,k}=
\frac{B}{16N^2}\sum_{w,a}\left(16c_{N,k+1}(16w+a)-c_{N,k}(w)\right)^2\ge0.}
\]

A single new word `v=w_{N+1,k}` gives the **signed** time increment

\[
\boxed{E_{N+1,k}-E_{N,k}=
B\left[\frac{Q_{N,k}+2c_{N,k}(v)+1}{(N+1)^2}-\frac{Q_{N,k}}{N^2}\right].}
\]

The latter can increase or decrease. Therefore a monotone 'gravity' or truth-closeness scalar **cannot** be identified with finite discrepancy energy alone. Exact finite-support restrictions also give

\[
D_{N,k}\ge\max(0,1-N/16^k),\qquad
E_{N,k}\ge\max(0,16^k/N-1).
\]

An arbitrary normal sequence satisfies `lim_N D_{N,k}=0` at each fixed `k`, but also `sup_k D_{N,k}=1` for every finite `N`. Thus `sup_k lim_N D=0` and `lim_N sup_k D=1`. The two infinity operations **cannot** be interchanged; normality does not demand they commute.

### CO-05 — the pure-gauge curvature no-go (PAPER DERIVATION + TEST)

Put `phi(n,h)=h U_n mod 1` on a discrete time–frequency grid. Define oriented edge transports by *differences of this common vertex potential*. The time edge is `h(15U_n+r(n+1))` and the frequency edge is `U_n`, both modulo 1. Around each square,

\[
\underbrace{h(U_{n+1}-U_n)+U_{n+1}}_{\text{time then frequency}}
-\underbrace{[U_n+(h+1)(U_{n+1}-U_n)]}_{\text{frequency then time}}=0.
\]

Hence the exact phase connection is flat **even though it retains the authentic BBP forcing**. The arithmetic carrier is locally coupled, but a nonzero *gauge-invariant* curvature does not follow. To establish curvature, introduce a distinct operational connection (e.g. information-losing projector or explicit frame change), maintain path-specific source recovery, and use a hostile countermodel. See existing `holonomy_proof_transport.py` for a separate nonflat *declared* GF(2)^2 example, not a BBP physical-field measurement.

### CO-06 — exact finite-prefix counterfeit (COUNTERMODEL + TEST)

For any certified prefix integer `q` of length `M`, let

\[
\beta=(q+\tfrac12)16^{-M}.
\]

The rational `beta` shares all first `M` base-16 digits with `alpha`, so **every** certified `w_{n,k}` for `n+k<=M` agrees. Yet `beta` has eventually zero digits and is nonnormal. It does **not** satisfy the original BBP identity and zero-seed forcing. Therefore finite-prefix consistency, coherence, and an ever stronger prefix signal **do not imply normality**. The oracle's original-source check is essential but still cannot supply cancellation by itself.

## Verdict / claim ladder

| ID | Scope | Status | Authority / falsifier |
|---|---|---|---|
| CO-01 | Exact rational source-tail interval naturality, all `n,d>=0` | **PAPER DERIVATION**, finite checked | Recompute endpoints; mutated source test |
| CO-02 | Original-source common-root prefix and windows for finite `L,M,n,k` | **PAPER DERIVATION**, finite checked | Force boundary crossing; forge prefix/seed/source |
| CO-03 | Source-authenticated finite `(N,k)` square commutation | **PAPER DERIVATION**, finite checked | Wrong parent cell, wrong time sample |
| CO-04 | Exact finite Haar energy, signed time energy and support bounds | **PAPER DERIVATION**, finite checked | Compare independent histogram formulas; both time signs |
| CO-05 | Pure-potential Fourier phase holonomy is zero | **PAPER DERIVATION**, finite checked | Explicit oriented square, all tested `h` |
| CO-06 | Same finite prefix admits a nonnormal counterfeit | **COUNTERMODEL**, finite checked | Rational eventually-zero sequence |
| CO-07 | Oracle-selected transport forces growing-scale defect decay for π | **UNVERIFIED / OPEN** | Needs original-source signed temporal saving |

No claim of independent peer verification or full Lean authority is made. The computations are local and exact, but classical BBP/π identification and the infinite-limit statements are imported or paper proofs. No computed data promotes CO-07.

## Reproducible finite probe

```sh
python -m unittest tests.test_bbp_coupled_oracle -v
python scripts/bbp_coupled_oracle_probe.py --depth 32 --digits 17 --N 10 --k 2
```

The research branch also provides `tests/test_bbp_coupled_oracle.py` (hostile controls), `observational_succ/bbp_coupled_oracle.py` (stdlib-only exact checker), and `scripts/bbp_coupled_oracle_probe.py` (JSON receipt). All new paths are additive; no source, frozen import, CI workflow, historical contract, main branch, tag, or release is modified. Maintainer-required whole-repo validation commands are specified in `AGENTS.md` and must be run in an environment containing the complete checkout. An isolated local reproduction is *not* a claim that those gates passed.

## Next falsifiable theorem (not a disguised restatement)

The oracle should next operate over the **source-current** residual highlighted in draft PR #608, not merely certify more digits. Supply a source-selected inequality giving positive lower density of the relevant centered carry currents, or a *uniform prescribed-scale* Fourier saving on the exact zero-seed recurrence. Test it against changed-seed countermodels, conductor-matched nonnormal sequences, and the current halo of exact BBP-tail identities. A genuine result must prove a universal-in-epoch saving (with constants/ranges) that the counterfeit cannot satisfy. No such theorem is established here.

## Provenance / nearby work

- Original authenticated source: `observational_succ/duck_bbp.py`, `observational_succ/selected_orbit.py`, `docs/PI_NORMALITY_FRONTIER.md`, `docs/PI_FRONTIER_CONTRACT.md`, `provenance/IMPORT_MANIFEST.json`.
- Earlier categorical pinbed and holonomy: `observational_succ/fourier_yoneda_pinbed.py`, `observational_succ/holonomy_proof_transport.py`.
- Main XXV verified frontier: `docs/MAIN_XXV_HANDOFF.md` and `docs/SUCC_MAIN_XXV_INTEGRATION_AUDIT_2026-11-12.md`.
- Open sibling drafts (inspected as metadata, not merged): PR #605 boundary filters, #606 holographic tomography, #607 transducers, #608 Leah–Gamma/source currents. This branch does not import their unmerged claims as theorems.

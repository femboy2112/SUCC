# Operation Main XIX — claim registry, countermodel ledger, scoping caveats

**Audit model.** Three independent read-only reviewers (one per cluster) re-derived the
load-bearing algebra from scratch and re-ran the committed probes on the compliant interpreter
(mpmath 1.4.1, no `python -I`); the principal independently re-verified the central Laurent-clock
sharpness theorem. **Verdict: Cluster A (#437) INTEGRATE-SCOPED, Cluster B (#452) INTEGRATE-SCOPED,
Cluster C (#455) INTEGRATE. Firewall INTACT across all three. No DEFER.** No mathematical status is
promoted.

## 1. Firewall (all OPEN; verified, nothing promoted)

Base-16 (and base-3) π normality; the signed Weyl gate `S_N(h)=∑_{n≤N}e(hU_n)=o(N)` for all fixed
`h≠0`; RH; Weil positivity (≠ positive covariance); general Collatz; shifted Lonely Runner
n=18..94. Each is OPEN in every cluster ledger checked (FP-05/FP-08; AC-16, CH-08/09, CPR-09, HG-09;
LCS-06/07, CRE-10, CSG-14/15, and the trunk ledgers ZJB/SZS/U2U/AQC/RSP/RP/AR). Every equivalence,
criterion, identity, and coboundary is labeled as such — a reformulation, not progress on the
premise. No positive-Weil-from-positive-covariance assertion anywhere. `U_0=0` literal and the four
signed poles unchanged; `∑16^{−n}r(n)=π/16` reconfirmed to ~3e-42 by two reviewers.

## 2. Central result — Laurent-clock sharpness (LCS, cluster C)

Keeping the authentic four-pole forcing and the distinct real counterseed `s_*=−π/16`
(`U_n(s_*)=−T_n`, completed point 0, rational, nonnormal, not in the original finite rational-state
register): for every fixed integer `d≥1`, integer `h≠0`, real `c∈(d+1,d+2)`, and
`K_N=⌊c·log_16 N⌋`,

- `L^C_{N,K_N}(h;s_*) → 1`,
- `L^[d]_{N,K_N}(h;s_*) → 2(d+1)/c − (d+1)²/c²`,
- transport defect `L^C − L^[d] → (1 − (d+1)/c)² > 0`.

**Independently verified** (principal + cluster-C reviewer, two separate code bases):
- exact remainder identity (1) `R^[d]_{n,k}=F_{n,k}−F^[d]_{n,k}` by two routes at exact rationals
  (incl. non-integer `n=37/3`);
- sign lemma `(−1)^{d+1}a_d(j)>0` (d up to 39, j up to 119): the shifted terms with weights
  2+1+1=4 strictly exceed `4u^d`;
- exact `c_d` table by two generating-function methods: `1/64, −7/512, 55/4096, −595/32768,
  8551/262144` (and `c_6=−149467/2097152`);
- finite-N trend: `L^C→1`; `L^[d]` stays strictly below with a positive gap matching the predicted
  defect to ~1% at the largest reachable horizon for d=1 and d=2; per-lag profiles match the
  leading-coefficient model `m(ρ)=∫_1^∞ cos(2π c_d ρ s^{d+1})s^{−2}ds` to 3 digits.

**Status and scope.** PROVED PAPER (classical tools: geometric remainder, Eulerian power sums, Abel
summation, sine-chord bound, Riemann integration), with exact rational and finite-N witnesses; **not**
a Lean theorem. `d=1,c=5/2` recovers Main XVIII PR #435's barrier `1/25`; the new content is every
`d≥2`. **This is a seed-uniform source-transport-precision barrier — a NEGATIVE result.** It is NOT
a source-selected impossibility theorem, NOT a statement about the actual `U_0=0` seed, and NOT
progress on π normality. Nuance for the next round: for `s_*` itself `L^[d]→2a−a²>0`, so the
corrected clock still *detects* the nonnormal seed; what fails is the uniform transport inequality,
not detection. Self-consistent with #454 CRE-08 (gap `→0` as `c→(d+1)^+`, matching transport error
`O(1/K²)` at `c=d+1`).

## 3. Per-cluster claim ledger (as integrated; statuses are the research authors', audit-checked)

**Cluster A — four-pole path interference (#437).** FP-01 (U=2V3+V4+V5) exact; FP-02 moments
`0,15,151,1209,8995,64905,461611,3259089`, `P(t)=(1−t)(t²+2)(t²+2t+2)`; FP-03a Prony det `−115200`,
inertia (1+,3−), recovery *iff ≤4 atoms* (sufficient "IF", correctly stated); FP-04/04B Beta mutant
(extra poles, completed `q`, non-original source); FP-05 joint character `μ̂(2h,h,h)` EXACT identity,
decay OPEN; FP-05B pairwise-Haar + triple lock `e(2X+Y+Z)=1`; FP-06A/06B Poisson aliases (q=1/5
collectively `>N−11|h|/56−1/(6|h|)`, zero alias `O(1)`). FP-08 and selected π normality OPEN.

**Cluster B — arctan/chiral + finite-history (#452).** AC-13 (Mellin `= (1/8)`angular `+ dG`, `G`
endpoint-vanishing; implies classical BBP π identity without importing it — verified symbolically,
`G=(1/8)log((2−t²)/(t²−2t+2))`); AC-04 dual `r^∨=1/2−r`, integer carry `8(16ⁿ−1)/15`; AC-05 dual
mode a reparametrization (no new cancellation); AC-14 cross-ratios `470596/225` vs `1728` over all
24 orderings (refutes naive Möbius/sphere identification); CH-02/03 seven samples determine / six do
not (resultant `−7372800`); AC-11/17/18, CH-03/07 genuine refuted negatives with named hypotheses;
AC-03 support rule brute-forced independently to a=3 (0 violations of 1.4M nonzero entries). AC-16,
CH-08/09 OPEN.

**Cluster C — categorical / entropy / Laurent (#455) + shared trunk.** LCS as §2. CRE-02
entropy-maximality ⇔ normality (reformulation, not proof); CRE-03 Parseval (`∑|m|²=Q`, to 1e-14);
CRE-04 resolution ceiling `D_{N,k}≥max(0,log(M/N))` (refutes only the naive one-resolution
certificate); CRE-05 hostile seed `1/5−π/16→δ_{1/5}`, entropy 0; CRE-06 order-2 de Bruijn
(`D_{N,2}=0` yet nonnormal: `H_3=log256`, `D_3=log16`, `Q_3=15`). Categorical: CSG-02 S4 monodromy
(order 24, trivial deck), CSG-06 false-span sheet switch + associative lifted composition, CSG-16
two-frame failure sharp (third frame separates all 9 complex collisions), CST-05 three-frame global
embedding (87-digit certificate exact). CSG-14/15 UNVERIFIED. **Category-spine: REUSE of the existing
`operational_yoneda_descent`/`noncommuting_proof_transport` machinery — no competing `Category`
spine; new local types are arithmetic data.**

## 4. Countermodel ledger (hostile controls that any future proof must exclude)

| control | mechanism | kills |
|---|---|---|
| `s_*=−π/16` (counterseed, completed 0) | `U_n=−T_n`; positive transport defect `(1−(d+1)/c)²` | seed-uniform vanishing-transport at `c∈(d+1,d+2)`, every `d` |
| `q=1/5` (same forcing, altered completed point) | `S_N=N·e(h/5)+O(1)`; Poisson aliases `>N−11|h|/56−…` | source/seed-blind alias-vanishing routes |
| `q=1/5−π/16` | empirical measure `→δ_{1/5}`, entropy 0 | "×16-invariance + same source ⇒ Haar" |
| order-2 de Bruijn | `D_{N,2}=0`, globally periodic, nonnormal | "maximal scrambling at one finite resolution + coherence ⇒ normal" |
| `r'(N+m)=r(N)2^{−m}` source mutant | same first N states, rational completion | finite-history-only inferences |
| Beta `B(8n,9)` mutant (#437) | matches 8 moments, extra poles, rational `q` | first-eight-jet-only source proofs |

Not excluded: a route using the exact literal `U_0=0` boundary and diagonal rationality — the open
frontier (see `MAIN_XIX_HANDOFF.md`).

## 5. Scoping caveats (documentation/test hygiene; research prose NOT rewritten — consistent policy)

All low-severity; none changes a verdict or the firewall. Recorded here, not patched into the
quarantined research dirs (same policy as Main XVII/XVIII):

1. **Formula-echo / vacuous-certificate tests.** The LCS limit tests (`test_laurent_clock_sharpness`)
   echo the closed-form `limiting_profile`; `two_frame_sharpness.verify()` returns `True` literals
   (reached only after real checks that raise on failure); several `holonomy`/`finite_history`
   tests assert constant inequalities or a function against its own formula; #437 `test_15/16`
   assert the hardcoded `11|h|/56`, `1/(30q|h|)`. The underlying math is independently confirmed by
   the reviewers' re-derivation and the principal's finite-N run; the committed tests under-witness
   it. Recommended follow-up (handoff): add a committed per-lag "profile-shift" probe for the LCS
   limits.
2. **"Independent" oracles share source and author.** The per-cluster `independent_oracle.py` /
   `symbolic_probe.py` use genuinely different algorithms (permutation-vs-Laplace determinant,
   convolution-vs-recurrence, sympy-vs-stdlib) but the same source mathematics — independent
   *implementations*, not external referees (the VALIDATION files admit this).
3. **Stale counts / blob hashes.** #437 test-count drift (26/28 vs true 30) and VALIDATION blob-hash
   churn; LCS VALIDATION "198 partial, 1 skip" is a historical snapshot (0 skips on the full
   checkout).
4. **Rhetoric / over-read labels.** #452 `PROOFS.md` "MAJOR SOURCE/GEOMETRY TRANSPORT" for a
   classical rederivation (the file itself concedes non-novel); LCS-06 "REFUTED universal
   extension" refutes seed-uniform transport, not the selected seed; #437 FINITE_DIAGNOSTICS "because
   ... coupled deterministic source" over-reads an `N^{−1/2}` vs `N^{−3/2}` gap present for any
   equidistributing model.
5. **Strawman-ish refutations.** AC-14 refutes a Möbius/sphere identification nothing in the repo
   proposed; the lawful non-Möbius functor question is explicitly left "not established."
6. **Circular control, `ε_q`.** #437 FP-04B's `ε_q=(q−π/16)/B_*` bakes π into the counterfeit —
   legitimate as a source-map-adequacy control, circular only if cited as an organically occurring
   rival source.
7. **Research-dir prefixes stay local.** FP/AC/CH/CSG/CRE/LCS/CPR/HG/ZJB/SZS/U2U/AQC/RSP/RP/AR mint
   **no** registry namespace by design (like Main XVII's PIG/BC/… and XVIII's CT/TWTH/…); they key
   by path in the catalog, so there is no machine collision.

## 6. Directive-critical confirmations

- **No competing category spine** (§3 / cluster C finding): the categorical work reuses
  `operational_yoneda_descent` and `yoneda` machinery; no parallel `Category` core.
- **No silently-skipped upstream tests**: the formerly-skippable `ObservationPathCategory` /
  sheet-adapter / parent-pointed-source tests all execute and pass on the genuine checkout (0 skips
  across every audited module); skips occur only under `python -I` or a broken import path. The full
  P0 suite is run under the compliant venv (see `MAIN_XIX_VALIDATION.md`).

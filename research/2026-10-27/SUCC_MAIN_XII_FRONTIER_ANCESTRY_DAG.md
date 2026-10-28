# SUCC Main XII — Frontier Ancestry DAG and Inventory Manifest

**Status:** research manifest (discovery layer). Computed 2026-10-27 against `main = 6dd80730c3575d91f746546a25da5aedbd2e2737`.
**Method:** true Git ancestry via `git merge-base --is-ancestor` over every open PR head, **not** PR `base=` labels (AGENTS.md discipline). A closed PR is not necessarily merged; a `base=` label is not ancestry.
**Firewall:** π base-16 and base-3 normality **OPEN**; the only signed real estimate is `∀ h≠0: Σ_{n≤N} e(h U_n) = o(N)` — where `e(x) := exp(2πix)` and `U_n = 16^{n−1}π − T_n` is the **real** four-pole orbit mod 1 (**not** an integer carry-recursion, for which the sum is trivially `N`) — on the authentic four-pole source, an **UNPROVEN required cancellation, not an existing bound**. RH **OPEN**. Nothing in this manifest promotes those.

## 1. Roots, stack, leaves

Six PRs root the open frontier. Four fork cleanly from current `main`; two are **stale**.

| PR | branch | true parent | ahead/behind main | note |
|----|--------|-------------|-------------------|------|
| #306 | pi-signed-pushforward-obstruction | **MAIN (clean)** | 1 / 0 | Skeleton-Key M3 no-go; stack root of #309–#311 |
| #307 | oily-macaroni-source-mellin-hilbert | **MAIN (clean)** | 3 / 0 | independent Oily I (leaf) |
| #308 | bbp-atomic-two-quadratic-gaussian | **MAIN (clean)** | 1 / 0 | BBP ground-floor atoms (leaf) |
| #341 | math-memory-farey-gauss-consolidation | **MAIN (clean)** | 4 / 0 | **this consolidation's integration base** (leaf) |
| #334 | prime-ladder-ravel-audit | **STALE** `de257fad` | 14 / 118 | forked from OLD main, 118 behind |
| #337 | furstenberg-kempner-firewall | **STALE** `de257fad` | 6 / 118 | corrective child of #334, also stale |

Everything else (#309–#340) is **one deep single-parent tree rooted at #306**, verified linear except for documented sibling forks:

```
main 6dd80730
├─ #306 ─ #309 ─ #310 ─┬─ #311 (leaf)
│                      └─ #312 ─ #313 ─┬─ #314 ─ #316 ─┬─ #317 ─ #319 ─ #320 ─ #321 ─ #322 ─ #323 ─ #324 ─┬─ #325 (leaf)
│                      │               │               └─ #318 (leaf, WTF audit)                           ├─ #326 (leaf, prior π audit — this session)
│                      │               └─ #315 (leaf, sibling off #313)                                    └─ #327 ─ #328 ─┬─ #329 ─ #331 ─ #333 ─ #336 ─ #339 (leaf)
│                                                                                                                           └─ #330 ─ #332 ─ #335 ─ #338 ─ #340 (leaf)
├─ #307 (leaf)   ├─ #308 (leaf)   ├─ #341 (leaf)
└─ #334 (STALE) ─ #337 (STALE, leaf)
```

**Leaf tips (nothing descends from them):** 307, 308, 311, 315, 318, 325, 326, 334, 337, 339, 340, 341.

## 2. Per-cluster unique contributions (inventory digest)

Read-only inventory over all 34 frontier PRs (247 claim referents, 158 firewall-sensitive). Firewall read **INTACT** in every cluster: no prose over-claim of normality/o(N)/RH; every branch self-labels those OPEN.

- **Oily / Γ / φ genesis** (#306, #307, #309, #310, #311): #306 `SK2-D` `is_cartesian` signed-transport firewall (the round's one positive classical product) + an eight-front obstruction map handing the gate back to arithmetic; #307 exact complex two-time BBP source Hilbert Gram (`BL-7`); #309 two-quadratic-atom minimal dim-4 realization, 8-step return, PGF fixed point **q\*=φ⁻²** (Oily packet — distinct from Gauss λ=φ⁻¹); #310 Möbius oily-totient `C_q(z)` + third-order golden-centered shadow carrying `−(8/27)(φ⁻¹−γ)`; #311 integer-branch Euclidean coercivity → DC-1 constant 1/1250→1/29.
- **Inside-out / Seinfeld / WTF** (#312–#318): IO-1..8 Koopman inside-out duality; #313 **`K_N = O(N/log N)`** genuine classical packing bound; #314 exact coherence-group path-sum disintegration; #316 shared-source "referee-not-applause" calibration firewall; #317 whole-block coercivity 1/29→1/14; #318 additive integration audit of #316 (verdict SOUND; caught a vacuous hardcoded-`15/15/0` certificate — reusable lesson).
- **π selected-boundary CRT core** (#319–#324): mixed-lag/periodic-template coercivity; #320 **`v₂(r(x)−r(y))=v₂(x−y)`** 2-adic source isometry + sharp nonnormal source-mutant countermodel `PC-9`; #321 `C_past=0` 2-adic zero boundary (`BW-1`); #322 binary bit-gate odometer + 3-adic isometry `TR-1` + joint 2×3 CRT clock `CRT-1`; #323 causal Green convolution + LTI delay no-go `ECHO-5`; #324 CRT Plancherel identity `SB-3` + the **o(N) energy GATE (unproved sufficient criterion)** + `SB-4` sharp per-band counterfeit.
- **π signed / prime-7 / var-length / solenoid** (#325, #327–#330): #325 bad-reduction prime set exactly **{2,3,5}** + λ⁸=16 + p≥7 collision law `GPR-4`; #327 `SCB-01` genuine `O(N/log N)` seam bound + `SCB-11` REFUTED bundle; #328 prime-7 source descent (fiber spectra, obs-prime set {31,109,251}); #329 derivative-valuation variable-length bitcode law; #330 solenoid digit-memory + normality **equivalence** `SNE-2` + odometer-factor no-go `SNE-5`.
- **Adelic / rank-two / chiral / log-germ / ternary** (#331–#333, #335, #336, #338–#340): #331 certified base-3 digit **handle** (from published π² & π√3 base-729 BBP sources — a certified *computation*, **not** a base-3 spigot, base-3 normality OPEN); #332 all-rank adelic transport + `AR-4` transverse-trace obstruction + `AR-5` conditional-on-Rudolph-Johnson; #333 rank-two chiral E-tower gluing + `RT-OBSTRUCTION`; #335 BBP log Dirac comb; #336 two-clock filter + `CT-QUOTIENT`/`CT-SPECTRAL` equivalences; #338 zero/one jet characters + `ZO-3` all-depth obstruction (REFUTED transport); #339 dual-jet source rigidity; #340 oily q=1 log-germ coefficients (`OZO-germ-Weyl` UNVERIFIED).
- **Prime-ladder / Furstenberg / BBP-atomic** (#308, #334, #337): #308 BBP octic → two rational quadratic atoms + 8-return holonomy (NOT stale; clean off main); **#334 (STALE, author "Ravel"/deepseek-v4)** all-prime measure rigidity (classical) but labels a transcendence→entropy→normality reduction PROVED — its entropy leg is unproven; **#337 (STALE)** supplies the refutation receipt: the Kempner number `κ=Σ2^{−2^j}` is transcendental, irrationality exponent 2, **zero** topological entropy (`FK-1`), killing #334's bridge.

## 3. Integration decision

Per the Main XII handoff and AGENTS.md firewall: **only the #341 additive discovery layer + this consolidation's own work** (catalog, DAG manifest, expanded relation graph, topic pages, safe registry reconciliation) is a candidate for `main`. The entire #306-rooted π/Oily/BBP/Gaussian tree and the stale #334/#337 pair stay **research-only** — inventoried, provenance-pinned, status-honest in the memory graph, **not** merged. Force-merging unproven-normality frontier work into `main` is the one prohibited move.

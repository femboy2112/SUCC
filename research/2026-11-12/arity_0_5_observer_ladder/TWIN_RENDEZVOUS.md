# Twin observers in a larger carrier: rendezvous, relative frames, environmental defects

**2026-11-12, research-only.** This continues draft SUCC PR #604 on the Main XXV branch, preserving the original four-pole BBP source and `U_0=0`. **R0, pi normality, Goldbach, completed Weil positivity, RH and a physical model of wavefunction collapse remain OPEN.** The new mathematics below is a *chosen operational model* with classical quantum-information and Minkowski ingredients. Neither a causal physical implementation nor a claim of novel priority is established.

## 0. Steelman — the larger universe and the meeting-only comparison

Declare a larger hypothetical system, comprising an arithmetic source `S`, two source-directed finite observers `A` (local-rooted) and `B` (global-rooted), a possible environment/carrier `E`, worldlines with local charts and a future rendezvous event `M`:

```
                           S (common source law)
                         /                     \
                        A --> local paths       B <-- global/symmetry paths
                         \                     /
                      [transport models into chart M]
                         \       only here     /
                          [present outputs] --> compare
                                  |
                         source anchors + Bell syndrome
```

Each observer's **current** report at `M` is `(model_M, meeting_M, source_witness, frame)`. Earlier events from different spacetime patches are not directly compared. Any current record of such an event must pass through a declared and tested transport (`T_A`, `T_B`) before it enters the common basis. A report about the past is currently held *information*, not a past event re-actualized. The model has no privileged physically instantaneous comparison outside the joint future light cone.

A mathematical tensor product `H_A ⊗ H_B ⊗ H_E` and a chosen Bell preparation model an entangled *pair of registers*. They do not assert that arbitrary mathematical observers, the BBP algorithm, or the physical carrier are intrinsically quantum-entangled. An unmeasured unitary collision with `E` can entangle subsystems and reduce the **two-observer marginal** before the meeting. No physical collapse or superluminal signal is required. “Collapse only at the middle” is therefore a **control goal** (postpone chosen Bell measurement), not a theorem about all carrier interactions or an interpretation-independent physical claim.

## 1. RV-01 — transport present outputs, not historical points

In a flat, declared `1+1` Minkowski chart with `c=1`, define the exact rational local-to-common boost

```
t = gamma (t' + v x'),   x = gamma (x' + v t'),
gamma^2 (1-v^2) = 1,  |v| < 1, gamma > 0.
```

The inverse uses `-v`, and `t^2-x^2` is preserved identically. In exact `Fraction` arithmetic choose left frame `(v,gamma)=(3/5,5/4)` and right `(-3/5,5/4)`. The common meeting `M=(3,0)` has **different local coordinates**. Once transported to the same chart both observers report the same event. A known meeting target must also be checked; merely colliding at another event does not satisfy the protocol. Timelike-or-null causal reachability holds from `(0,-2)` and `(0,+2)` to `M`, and fails for superluminal or past-directed displacements. These are *flat-model checks*, not geodesic parallel transport, spin transport or gravitational curvature.

If output is a Minkowski two-vector, compare `T_A(m_A)` and `T_B(m_B)`. In general the appropriate type may instead be a gauge field, spinor or transport functor. Do not transport a Hilbert vector with a nonunitary Lorentz boost while claiming it preserves a qubit norm: choose and justify the relevant representation and connection separately. Transports are part of the source map, not free frame labels.

**Countermodel:** both present outputs may agree on the *same wrong model*. Meeting agreement alone is never mathematical truth, source authentication or an all-history certificate.

## 2. RV-02 — exact environment-overlap theorem

Fix normalized environment states `|e_0>`, `|e_1>`, and a preparation/evolution such that

```
|Psi> = (|00>|e_0> + |11>|e_1>)/sqrt(2).
gamma = <e_0|e_1>  (complex).
```

Tracing out the environmental register produces

```
rho_AB = ( |00><00| + |11><11|
         + conj(gamma)|00><11| + gamma|11><00| )/2,
F_plus = <Phi+|rho_AB|Phi+> = (1 + Re gamma)/2,
purity = Tr(rho_AB^2) = (1 + |gamma|^2)/2.
```

Proof: expand `|Psi><Psi|` and trace the two environmental cross terms, then multiply the resulting `2×2` supported matrix. By Cauchy–Schwarz, `|gamma|<=1`. In this chosen balanced family, reduced `AB` is pure iff `|gamma|=1`, equivalently the two environment states coincide **up to phase**; target Bell fidelity `F_plus=1` further requires the **calibrated** `gamma=1`. For *pure* marker alternatives, their trace-distance distinguishability is `D=sqrt(1-|gamma|^2)`, yielding `D^2+|gamma|^2=1` (this equality is restricted to the present pure-marker model; the general visibility/distinguishability result is an inequality).

An exact rational marker family is `e_0=(1,0)`, `e_1=(c,s)` with `c=(1-u^2)/(1+u^2)`, `s=2u/(1+u^2)`. At `u=1/2`: `gamma=3/5`, `F_plus=4/5`, `Tr rho_AB^2=17/25`, `D^2=16/25`. At `u=1`, gamma zero, purity `1/2` and Bell-plus click probability `1/2`. All calculations use exact rational density matrices; no simulation of actual environmental decoherence is claimed.

**Correction to the intuitive hypothesis:** no *measurement* is necessary for the AB marginal to become mixed. It suffices that distinguishable which-path information is stored in `E`. Conversely, an intermediate interaction can be **coherently uncomputed**. Start with `(|000>+|110>)/sqrt(2)` on `ABE`. Apply CNOT(A→E): GHZ-like entangled state, `Tr rho_AB^2=1/2`. Then apply CNOT(B→E): original `|Phi+>_AB|0>_E` is restored **without a measurement**, because A and B are perfectly correlated. The system interacted *twice* with the carrier. Thus “any carrier interaction causes permanent collapse” is refuted by an exact circuit. Distinct unobserved environment registers can instead retain records and keep the AB state mixed.

A projective Bell-plus **click** is not itself a proof of premeasurement purity: the marked mixed state clicks with probability `1/2`. Statistical characterization requires repeated independent preparations or other validated measurement assumptions. For independent identically prepared copies, the probability of `m` consecutive Bell-plus clicks in that example is `2^-m` under the stated IID model; correlation between trials invalidates that formula.

## 3. RV-03 — full-strength relational no-go: paired wrong paths can be invisible

Let `|Phi_d> = d^-1/2 sum_j |j,j>`. For every unitary `U ∈ U(d)`,

```
(U ⊗ conj(U))|Phi_d> = |Phi_d>.
```

Proof: the coefficient of `|a,b>` is `d^-1/2 sum_j U_aj conj(U_bj)`, exactly `d^-1/2 (U U†)_ab = d^-1/2 delta_ab`. Therefore **even perfect, noiseless, joint Bell-state tomography at rendezvous cannot identify each path**: it identifies the *relative* action modulo the common stabilizer. Path agreement is a gauge-equivalence assertion unless an external source/reference pin breaks the stabilizer.

Exhaustive Pauli test: assign each local path an error from `{I,X,Z,XZ}` (the last equals Y up to global phase). Measuring the two stabilizers `ZZ` and `XX` gives four Bell syndromes: `Phi+`, `Phi-`, `Psi+`, `Psi-`. There are 16 Pauli error pairs; each outcome has **four** preimages. In particular `I⊗I`, `X⊗X`, `Z⊗Z` and `(XZ)⊗(XZ)` are indistinguishable on `|Phi+>` up to physically irrelevant global phase. A lone `Z` or `X` preserves the state's purity and entanglement but moves it to an orthogonal Bell sector; an “incoherent” unitary path does not necessarily kill entanglement.

This is a **decisive counterexample** to the unrestricted claim “the twins can obtain pure concordance iff both independently walked the correct path.” No Bell calibration on a lone entangled pair can eliminate the joint stabilizer without restricting the error family or supplying additional independent sources of information.

## 4. RV-04 — a restricted soundness construction, with extra reference ports

The no-go suggests a minimal finite **repair**, not a proof of a universal method. Retain the primary twin pair `A--B`, and introduce **two additional distinct Bell pairs** `A'--R_A` and `B'--R_B`, with the reference ports `R_A` and `R_B` at rendezvous. Each observer carries its respective separate witness qubit, not a clone of its primary entangled qubit.

Under the **explicit promise** that the chosen Pauli path error `E_A` acts uniformly on both A and A' and `E_B` acts uniformly on B and B', and the references remain calibrated and protected, at the common meeting event measure three Bell comparisons:

- `A'--R_A`: Bell syndrome `Phi+` iff `E_A=I` (mod phase) within the Pauli alphabet.
- `B'--R_B`: Bell syndrome `Phi+` iff `E_B=I` (mod phase).
- `A--B`: a relational check of twin correlations and environment leakage.

The two independent witness syndromes give **16 distinct ordered outcomes** on the 16 Pauli error pairs, so both witnesses returning `Phi+` is equivalent to both Pauli paths being clean **under the stated uniform-coupling and noiseless reference assumptions**. There is no deterministic guarantee for arbitrary noise, errors acting differently across physical qubits, reference loss, forged source labels or arbitrary continuous path families. For continuous U(d) a finite fixed number of Bell syndromes cannot directly separate all paths; additional controls/measurements or admitted completeness assumptions are needed.

No comparisons are made between remote historical events: these are present quantum/reference outputs measured together at `M`. In practice, distributing and protecting these additional entangled pairs is itself a demanding experimental assumption, not a free logical primitive.

## 5. RV-05 — the original BBP source pin remains mandatory

Retain the exact original source, never overwrite imported originals:

```
r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2),
U_0(s)=s, U_n(s)=16 U_(n−1)(s)+r(n),
P_n=sum_(j=1)^n 16^(-j)r(j),
Z_n(s)=16^(-n)U_n(s)-P_n=s.
```

A **present-time report** may include `(n,U_n)` and the independent public original-source contract. A verifier at `M` can compute `Z_n`; in the declared exact rational seed family, `Z_n=0` rejects the counterfeit `s=1/16` even though its later circle phases alias. Two matching reports with a common wrong seed can agree and pass an unanchored relational check while failing their own `Z_n=0` checks. The same principle detects the symbolic coherent counterseed `s=-pi/16` by the existing symbolic zero-anchor kernel, without claiming the finite rational code can represent that irrational seed exactly.

This check is **algebraic**, not evidence that the claimed earlier physical events occurred or that the report's data are unforgeable. A fully physical version additionally needs source-labelled measurement instruments, a trusted audit/commitment channel, and verified causal frame transport. Both observers passing `Z_n=0`, with consistent present models and perfect Bell coherence, still does **not** imply any signed estimate for the original selected sequence. The Main XXV R0 statement remains

```
exists eta>0, B0, forall B>=B0:
Re[(1/B) sum_{n=B}^{2B-1} exp(2pi i 16^n pi/16)] <= 1-eta.
```

No finite Bell correlation or general positivity bound resolves R0. At best, this construction gives a **faithfulness/consistency gate** for an independently established source-specific estimate.

## 6. Steelman → crucible → verdict

- **PROVED LOCAL (classical ingredients):** exact rational Lorentz chart transport; all-N Bell environment-overlap formulas; universal `U⊗conj(U)` stabilizer no-go; deterministic Pauli-syndrome classification; conditional independent-reference soundness on 16 errors; exact arithmetic `Z_n` identity. Tests provide finite checks, not all-quantifier proof authority.
- **REFUTED with exact witnesses:** every interaction irreversibly collapses entanglement (two CNOT uncompute); an incoherent unitary destroys the entangled relation (one Pauli gate maps Bell state to another); pure Bell acceptance certifies both individual paths (`Z⊗Z`); single Bell-plus click certifies purity (dephased AB clicks with probability `1/2`); identical present models certify truth (two matching incorrect reports).
- **UNVERIFIED/OPEN:** unique global physical carrier or intrinsic collapse boundary, complete source-derived spinor/frame identification, autonomous quantum path authorization, source-authenticated transport to signed π R0 estimates, Goldbach and RH.

### Provenance and nonduplication

Reuses SUCC `docs/FOUNDATIONS.md` and Main XXV frontier; `observational_succ/twin_circle_observers.py` / `research/2026-10-11/TWIN_OBSERVER_FIELD_INVARIANCE.md` (twin symmetry); `research/2026-11-05/unit_pair_bell/` (entanglement/zero/source firewall, Bell errors and countermodels); `research/2026-11-07/pinbed_yoneda_oscillators/ANCHORED_PATHS_VS_HOLONOMY.md` (seed-blind closed holonomy); PR #604's `BIDIRECTIONAL_CHANNELS.md` (finite/global selection seam). The new code is a **finite exact laboratory adapter**, not an alternative foundational category or a claim of replacing the existing modules.

External physics background: Englert, *Phys. Rev. Lett.* 77, 2154 (1996), doi:10.1103/PhysRevLett.77.2154 (which-way/visibility); Kwiat, Steinberg & Chiao, *Phys. Rev. A* 45, 7729 (1992) (quantum eraser); Ma et al., *PNAS* 110, 1221 (2013), doi:10.1073/pnas.1213201110 (causal locality and quantum erasure). These support the quantum-information **interpretation**, not our BBP/source-specific claims or an apparatus realization.

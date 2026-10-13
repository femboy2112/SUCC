# F47 — Collective phase: calibrated clocks, conserved mean, and source limits

First-generation investigator, 2026-10-13. Immutable source parent
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`; branch
`research/swm-f47-2026-10-13`. The shared investigator protocol alone was read;
no other first-generation dossier or intermediate conclusion was consulted.
Only the three F47 artifacts in this directory are contributions.

**Verdict:** the calibrated pairwise-averaging theorem **SURVIVES** with a
complete author derivation and exact finite controls. Its core is **CLASSICAL**
consensus mathematics. The executable examples are **TESTED MODEL**. Proposed
uncalibrated clock/source inferences are **REFUTED** below. Independent principal
review by a non-deriver is still required; this dossier does not discharge it or
promote any shared ledger claim. No academic novelty or physical clock result.

## 1. Original question

Can observers with different local clocks coordinate a phase while preserving
an explicitly defined source-relative invariant? Which information is needed
to compare phases, and what fails when clocks or the shared source are not
calibrated? The faithful strong reading separates two operations: **observing**
a deterministic periodic quotient of one source, and **changing** observer
clock offsets by a specified communication protocol. Agreement between
representations alone does not establish that a physical interaction occurred.

The pathway gap is an absent typed coordination law. We fill it with a narrow
law: common unit drift, invertible affine charts, exact pair updates at common
event times, and bounded connected edge coverage. The probe gap is whether raw
clock agreement authenticates that law or its source. Exact aliased worlds
resolve that question negatively.

## 2. Existing mathematical context

Primary sources checked live on 2026-10-13:

* Boyd, Ghosh, Prabhakar and Shah, *Randomized Gossip Algorithms*, IEEE TIT
  52(6), 2508–2530 (2006), [author-hosted paper](https://stanford.edu/~boyd/papers/pdf/gossip.pdf).
  Section I-A and equations (1)–(2) specify pairwise averaging; Section II
  separates sum preservation from convergence. Their random asynchronous clock
  model differs from our deterministic bounded schedule. We derive our own
  conservative range bound instead of importing their probabilistic rate.
* Singer, *Angular Synchronization by Eigenvectors and Semidefinite
  Programming*, ACHA 30, 20–36 (2011), [author-hosted paper](https://web.math.princeton.edu/~amits/publications/angular_synchronization.pdf),
  Section 1. Exact relative offsets on a connected graph determine phases up
  to one global additive phase. Relative registration leaves a gauge freedom;
  it does not supply absolute source time.
* Shi, Mikael Johansson and Karl Henrik Johansson, *Randomized Gossip
  Algorithm with Unreliable Communication* (2012),
  [original author submission](https://arxiv.org/abs/1203.6028).
  Communication dependence and success laws matter to consensus and average
  preservation. Our one-sided-delivery counterexample uses exact arithmetic
  rather than asserting their probabilistic theorem in another setting.

Repository authority read: AGENTS.md, README.md, docs/FOUNDATIONS.md,
docs/METHOD.md, docs/ARCHITECTURE.md, docs/ROADMAP.md, relevant CLAIM_LEDGER.md
entries O307–O316 and O444–O458, and provenance/IMPORT_MANIFEST.json.
The two input modules are native, absent from the historic import manifest:

| Path | Exact first originating commit | Relevant obligation |
| --- | --- | --- |
| observational_succ/misiurewicz_phase_quotient.py and its source dossier | `b9d84bb39594a7b35d214288ca914e516f23660e` | Boundary-excluded binary phase, exact lag transport, source alias |
| observational_succ/dual_boundary_observers.py and its source dossier | `583ef6b605d6fc47654e571ea43caaa05c016a12` | Common-factor versus joint-information distinction; source-fiber target decoder |

Their exact origin blobs were inspected and hashed. The dual-boundary dossier
at the parent has a subsequent DB7 appendix; its original DB1–DB6 were checked
against the originating commit. Both input Python files match their origin
bytes. The receipt preserves origin and parent/current SHA256 separately.
The frozen foundations dossier and import source
`ba075348b7bcc66d938b3e0ca96c26e95bba340a` remain unchanged. No imported code
or historical original is modified. Repository novelty is not scholarly novelty.

## 3. Proposed SUCC objects

Let \(V=\{0,\ldots,N-1\}\), \(N\ge2\), and let \(G=(V,E)\) be a fixed finite
**connected undirected** graph. Each event activates one edge \(e_n=\{i,j\}\).
The schedule is a mathematical communication contract, not an inferred
physical scheduler. A fixed integer \(B\ge1\) satisfies

\[
 E\subseteq\{e_{kB},\ldots,e_{(k+1)B-1}\}\quad\text{for every }k\ge0.
\]

These are aligned blocks, not a hidden assumption that all arbitrary sliding
windows are covered. Repeated edges inside a block are allowed. There are no
directed, stale, simultaneous competing, lost, or Byzantine updates.

Use lifted real clock offsets \(z^n\in\mathbb R^N\). The source reference clock
has common unit drift \(\theta(t)=t\). Declared event times \(t_n\in\mathbb R\)
are nondecreasing and known exactly to the mathematical protocol. Each observer
has a known chart \(h_i(u)=a_i u+b_i\), \(a_i>0\), so its reported controlled
clock at event \(n\) is

\[
 H_n(z)_i=a_i(t_n+z_i)+b_i,\qquad
 D_n(x)_i=(x_i-b_i)/a_i-t_n.
\]

The source, calibration epoch, event index and common event time accompany a
record. They are type checks, not physical attestations. \(D_nH_n=I\) and
\(H_nD_n=I\). The local-to-local same-event map is
\(C_{ij}=h_jh_i^{-1}\), with actual coherence law
\(C_{jk}C_{ij}=C_{ik}\). The probe checks all 27 triangles for three charts.

Let \(P_{ij}\) replace both endpoint offsets by their half-sum and retain all
other offsets. This means both endpoints read the same pre-update state and
both updates commit. The controlled local transition is the affine map

\[
 U_{e,n}=H_{n+1}\circ P_e\circ D_n.
\]

It is an ideal jump-controlled clock model. It is not a Kuramoto oscillator,
an autonomous biological oscillator, a physical model with propagation delays,
or a protocol that discovers unknown rate/offset calibrations. Actual event
records are append-only; replacing a current controlled value does not erase
earlier observations.

## 4. Candidate theorem

**F47-A — calibrated averaging theorem (CLASSICAL core; complete local
derivation supplied, independent acceptance pending).** For every \(N,G,B\)
and schedule as above, every family \(a_i>0,b_i,t_n\), and every initial
\(z^0\in\mathbb R^N\), the recurrence \(x^{n+1}=U_{e_n,n}(x^n)\),
\(x^0=H_0(z^0)\), has decoded offsets \(z^n=D_n(x^n)\) satisfying:

\[
 \mu=\frac1N\sum_i z_i^n=\frac1N\sum_i z_i^0,
 \quad R_n=\max_i z_i^n-\min_i z_i^n,
 \quad L=(N-1)B,
 \quad\alpha=2^{-L},
\]

\[
 \boxed{R_n\le(1-\alpha)^{\lfloor n/L\rfloor}R_0,
 \qquad |z_i^n-\mu|\le R_n,
 \qquad z_i^n\longrightarrow\mu.}
\]

The preserved invariant in local coordinates is exactly
\(I_n(x)=N^{-1}\sum_i((x_i-b_i)/a_i-t_n)\). The common calibrated clock
approaches \(t_n+\mu\), not necessarily the true source time \(t_n\).
Its signed source-time offset is \(\mu\); an anchor or the premise \(\mu=0\) is extra.
The rate is in **committed pair events**, not seconds. Arbitrary fair infinite
scheduling is not asserted to provide this uniform bound.

**F47-B — finite-time equality is not guaranteed (REFUTED stronger claim).**
For three clocks starting at \((0,0,1)\), no finite sequence of exact
half-average pair updates can make all values equal. Every current value is
dyadic, whereas their invariant mean is \(1/3\). Under a covered path schedule
F47-A nevertheless proves convergence. An ideal limit is not executed infinity.

## 5. Proof attempt

This is a complete elementary derivation, not a finite-search proof.

1. **Actual commuting square.** Since \(D_{n+1}H_{n+1}=I\),
   \(D_{n+1}U_{e,n}=P_eD_n\). Induction gives \(z^{n+1}=P_{e_n}z^n\).
   Thus all clock-chart claims reduce through invertible declared maps to the
   same real offset recurrence; raw equality of \(x_i\) is unnecessary.
2. **Invariant and controls.** Each \(P_e\) is nonnegative and doubly stochastic.
   Active self weights are \(1/2\); other self weights are \(1\). Hence it
   preserves sums, fixes constants, and maps every value into the former
   minimum/maximum interval. If
   \(\mathcal E(z)=\sum_i(z_i-\mu)^2\), direct expansion gives
   \(\mathcal E(z)-\mathcal E(P_{ij}z)=(z_i-z_j)^2/2\). This checks the
   update sign and amount; energy monotonicity alone is not the rate proof.
3. **A common positive matrix column.** Take any \(L\)-step aligned segment
   and its product \(Q=P_{e_{s+L-1}}\cdots P_{e_s}\), \(s=qL\). Follow its
   column corresponding to one root \(r\). Initially the positive support is
   \(\{r\}\). Positive diagonal weights prevent support from shrinking.
   At every pair step a positive entry is reduced by at most a factor \(2\),
   and a newly positive entry is at least half a formerly positive entry.
   Thus every positive entry after \(\ell\) steps is at least \(2^{-\ell}\).
   If the support at the beginning of a \(B\)-block is proper, connectedness
   supplies a fixed graph edge crossing it. That edge occurs in the block;
   either its outside endpoint already became positive or that activation
   makes it positive. Each such block grows support by at least one vertex.
   After \(N-1\) blocks, every row has \(Q_{ir}\ge2^{-L}=\alpha\).
4. **Range contraction.** Subtract the common root mass from each row:
   \(Q=\alpha\mathbf1e_r^{\mathsf T}+(1-\alpha)S\), where \(S\) is
   nonnegative row-stochastic. The first term is the same scalar in every
   output coordinate, so \(R(Qz)=(1-\alpha)R(Sz)\le(1-\alpha)R(z)\).
   Iterate on the aligned \(L\)-blocks. Remaining steps cannot increase range,
   proving the displayed bound for every \(n\). Since the conserved mean lies
   between minimum and maximum, each value converges to that mean.
5. **F47-B.** Integers are dyadic and averaging preserves the dyadic rationals.
   Exact equality of all three finite current values would force each to be
   \(1/3\), which is not dyadic. The contradiction holds for every finite
   pair sequence, not merely the 20-step control in the receipt.

All quantifiers concern this specified mathematical law. None says unknown
physical oscillators, instrument clocks, or human observers satisfy it.

## 6. Crucible

Predictions were fixed before running the exact probe: the calibrated square,
sum, energy identity and conservative common-column bound must hold; deliberate
loss of a hypothesis must produce the witnesses below. Finite controls are
diagnostics of the maps and derivation, not universal certificates.

| Stronger inference tested | Exact hostile witness | Verdict and repair |
| --- | --- | --- |
| Raw identical clocks entail normalized phase lock without calibration | World A: charts \(u,u\), offsets \((0,0)\). World B: charts \(u,u-1\), offsets \((0,1)\). Both raw streams are ((t,t)) for every \(t\), but offset ranges are 0 and 1. Receipt checks identical affine coefficients, not only samples. | **REFUTED**. Require declared calibrated maps or retain the two-world ambiguity. |
| A binary phase report identifies initial source phase with unknown label/clock parity | \(y_n=p_0\oplus c\oplus(n\bmod2)\): \((p_0,c)=(0,0)\) and \((1,1)\) give identical streams. | **REFUTED**. One calibrated parity anchor separates these two worlds. |
| Connected graph alone gives lock | Only edge 01 is activated on the three-node path; \((0,2,10)\mapsto(1,1,10)\) is thereafter fixed with range 9. | **REFUTED**. Require actual coverage, not potential graph edges. |
| Fair copying is sufficient | On two nodes repeated simultaneous copying swaps \((0,1)\leftrightarrow(1,0)\). Sum is preserved, edge is always active, and range remains 1. | **REFUTED**. Half-average self weights are load-bearing. |
| One-sided delivery preserves mean | \((0,2)\mapsto(1,2)\) changes mean \(1\mapsto3/2\). | **REFUTED**. Require atomic paired commits or another explicitly proved invariant. |
| Local registrations always glue | Three positive affine maps \(A_{01}=I,A_{12}=I,A_{20}(u)=u+1\) have loop \(u\mapsto u+1\); a consistent shared coordinate would require \(u=u+1\). | **REFUTED**. Check cycle holonomy before claiming a common chart. |
| Current consensus retains original micro-identity | Source states \((0,2),(1,1),(2,0)\) all average to \((1,1)\); original left coordinate does not factor through that current report. | **REFUTED**. Preserve the original history separately; only the sum is promised. |
| Phase agreement authenticates one physical carrier | One fair bit read twice and two distinct labeled carriers initialized by a shared preparation have identical report table \(P(00)=P(11)=1/2\). | **REFUTED as inference**. Source-sensitive interventions with independently checked ownership are new information. |
| Uniform finite-time exact averaging always follows | F47-B's non-dyadic mean \(1/3\). | **REFUTED**. Retain the event-count error bound and ideal-limit boundary. |

The concrete probe checks 27 schedules and 1,467 initial vectors. It exhausts
connected graphs on 2 and 3 vertices and their edge permutations; separate
4-vertex path, star, dense and slack schedules extend the regime. Matrix
multiplication is a second implementation that never calls the update routine,
but shares the same author and mathematical premises. A nonperiodic 12-event
control changes the order of each covering block, uses distinct affine charts
and variable rational times. Its mean is \(7/4\), final decoded offsets are
\((41/32,41/32,71/32,71/32)\), and final range is \(15/16\). It is an
additional preselected regime, not a statistically independent empirical holdout.

## 7. Verdict

| Claim | Domain/hypotheses | Status | Support and next falsifier |
| --- | --- | --- | --- |
| F47-A: calibrated covered pair averaging converges to conserved decoded mean with the displayed rate | Lifted real offsets; connected undirected graph; atomic exact half-average; known affine charts/common times; aligned bounded coverage | **CLASSICAL core**, complete local derivation supplied; independent review pending | Proof in §5, exact receipt. Independent reviewer should attack the common-column support-growth argument with nonperiodic slack blocks. |
| Code realizes the stated square and exact finite controls | Fractions; declared source/epoch; stated finite cases | **TESTED MODEL** | Reproducible receipt, 27 triangles, 27 schedules, 1,467 vectors, six rejection controls. Mutate one endpoint update or rate inverse. |
| Lag-corrected phase equals initial phase in the inherited source domain | Boundary-excluded exact Misiurewicz quotient or declared legal symbolic path; known parity/labels | **CLASSICAL / inherited local theorem** | Actual 4-step algebraic orbit and ten lag covariance controls; next test noisy or ambiguous boundary sensors. |
| Unknown calibration, source identity or arbitrary scheduler can be inferred from agreement | Domains include the listed paired worlds | **REFUTED** | Receipts in §6, with repairs preserving the rival worlds. |

The theorem gains a precise preservation and convergence law in observer
coordinates. It does not discover the calibrations, authenticate source identity,
identify a physical invariant measure, preserve every original source target,
or certify a physical time/resource advantage. A scalar conserved mean may
itself be the wrong source target.

## 8. Remaining obstruction

The minimum next lemma is a **calibration-error transport law**: with correct
unit rates but assumed origins \(\hat b_i=b_i+\varepsilon_i\), derive the true
post-consensus offsets and a sharp residual lock error from the bounded
\(\varepsilon_i\). A claimed robust protocol must carry that residual rather
than declaring exact physical lock. Unequal rate errors, delay, quantization
and dropped commits are separate extensions requiring separate proofs.

Independent principal non-deriver review is pending and mandatory before
mathematical acceptance. There is no independent local proof-assistant check.
The parent explicitly restricted this first-generation run to bounded probes:
the full repository suite and compilers were not run. No CI claim is made.

## 9. Cross-domain connection with actual maps

The inherited logistic source has \(f(x)=\alpha x(1-x)\), where
\(\alpha^3-2\alpha^2-4\alpha-8=0\), on its certified postcritical core. On
\(J^*=J\setminus\bigcup_{n\ge0}f^{-n}(D)\), the genuine map
\(\phi:J^*\to\mathbb Z/2\) sends A/B to 0 and C to 1, with
\(\phi f=\mathsf{flip}\phi\). A report at declared integer lag \(n_i\)
and label calibration \(c_i\) is \(y_i=\phi(x_0)\oplus n_i\oplus c_i\).
The transport \(T_i(y)=y\oplus n_i\oplus c_i\) makes
\(T_i y_i=\phi(x_0)\) for every allowed source, not by a metaphor but by
composition of the displayed maps. The phase label itself is not a real
offset on which averaging is defined; averaging \(\mathbb Z/2\) reports would
need a separate law. Our real protocol retains a lifted clock coordinate.

Under the **declared** balanced symbolic source, raw lag covariance is
\((-1)^n/4\), transported covariance \(1/4\). The character
\(\chi(p)=(-1)^p\) gives raw signs \((1,-1)\) at lags 0 and 1: squared
sum 0 and incoherent power 2. Multiplication by the lawful lag signs gives
\((1,1)\) and squared sum 4. These are exact classical character identities,
not truth probabilities or physical interference. Both routes are one source
family; removing that family removes the evidence. No second independent
source, leave-one-family-out robustness, or quantum speedup is inferred.

For real source input \(x=2/5\), the probe checks the actual algebraic orbit
through four steps, with calibrated phase constantly 0. It also verifies
\(f(2/5)=f(3/5)\), preserving the micro-identity counterexample. It does not
promote finite boundary avoidance of these rational points to membership in
\(J^*\) for all future times. The fixed boundary point still blocks an
everywhere-defined flipping phase.

The dual-boundary adapter is the actual `DualFiniteTower.claim_factors` map:
on the three-state source in §6 it returns an original-source pair whose
current equal reports disagree on the target. The initial joint history does
factor the target. Thus controlled consensus, information sharing and source
reconstruction are three different predicates in exact types.

In Aletheia coordinates: κ is contact with native exact source modules and
synthetic control records, not physical measurement; φ is survival of the
specified derivation/probes; σ is declared calibration/source mapping and
remains physically unattested; ρ warrants scrutiny of attractive agreement;
μ includes both positive and hypothesis-removal controls. The new discriminating
contact for σ is calibrated source-sensitive intervention, not another aligned
report from the same preparation. No musical metaphor, neuroscience law,
physical transfinite computation, Euler/Gamma identification or RH conclusion.

## 10. Deliverables

* [F47_COLLECTIVE_PHASE.md](F47_COLLECTIVE_PHASE.md): ten-section dossier,
  theorem, complete derivation, sharp scope, countermodels and review gate.
* [F47_probe.py](F47_probe.py): bounded stdlib exact probe, invoking two unchanged
  native source modules. Limits: 29 CPU seconds and 256 MiB address space;
  outer commands also use a 30-second wall timeout.
* [F47_RECEIPT.json](F47_RECEIPT.json): exact rational traces, original and
  parent/current hashes, matrix controls, source aliases and refusal evidence.

Commands from the assigned worktree (exit 0):

```sh
timeout 30s python -B research/2026-10-13/SWARM_ATLAS/F47_probe.py --write research/2026-10-13/SWARM_ATLAS/F47_RECEIPT.json
timeout 30s python -B research/2026-10-13/SWARM_ATLAS/F47_probe.py --verify research/2026-10-13/SWARM_ATLAS/F47_RECEIPT.json
git diff --check
```

The generation and replay commands run the finite controls, recompute source
hashes against the immutable parent and check the probe hash in the receipt.
The measured replay used 0.86 seconds wall time and 24,120 KiB maximum resident
memory, exit 0, under the stated address-space/CPU limits. Timing is a local
execution receipt, not a cross-machine complexity guarantee.
Only F47 artifacts are staged and committed; no push, shared registry change,
runtime/default change, archive rewrite, merge, release, or full-suite claim.

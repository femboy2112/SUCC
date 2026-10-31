# Human T-action, Dirac frame resets, and inverse snapshot reconstruction

**SUCC research dossier — 2026-10-30.** **Status:** exact classical mathematics in a **declared observer/chart model**, plus a **CONJECTURED** source-specific bridge. **Not** a physical ontology, a new proof of normality, a proof of the Riemann Hypothesis, or an assertion about how actual human brains compute. The author's term **human T-action** is retained for the *observation / choice / recentering* interface. Physical event, mathematical orbit, observed report, and chosen chart are separate types.

**Parent:** `main@e18ba565ca540adb7edf3292f5593929e76d91c5` (Operation Main XVI). This file is additive; no authenticated BBP source or selector, historical theorem or imports, original signed poles, `U_0=0`, existing public claims, or core runtime is modified.

## 0. Motivation and the faithful reading

The author's hypothetical **snapshot universe** supplies before/after observations without direct access to the intervening dynamics. Human investigators reconstruct possible paths or generators. Multiple generators may explain the same snapshots (epicyclic fitting is not source identification). In SUCC language, the *human T-action* attaches an observed/selected mark and recenters the next local frame at the realized endpoint. A Dirac mass is then a natural *distributional representation of an instantaneous reset in that chart*. It is **not**, without independent physical evidence and a specified dynamical instrument, proof that the physical carrier undergoes a literal delta-force.

We distinguish four maps:

1. `P`: a source-authenticated physical or arithmetic evolution law;
2. `O`: a typed measurement/report map producing a finite record;
3. `H`: the digit/choice/recentering operation retaining both selected mark and residual;
4. `Q`: a chosen **between-report interpolation** of local coordinates.

The key operator is not a conflation of these maps: `O(P)` need not identify `P`; a jump in `Q` need not be a jump in `P`; retaining `(mark,residual)` need not make an arbitrary history, source, or physical state reconstructible.

## 1. The exact human T-action on a radix-b chart (HTS-01; CLASSICAL / PROVED PAPER)

Let the integer base `b>=2` and define the half-open state space `I=[0,1)`. For **every** `x in I`, set

\[
 d_b(x)=\lfloor bx\rfloor\in\{0,\dots,b-1\},\qquad
 R_b(x)=bx-d_b(x)\in I,\qquad
 H_b(x)=(d_b(x),R_b(x)).
\]

Then

\[
 H_b:I\longrightarrow\{0,\dots,b-1\}\times I
 \quad\text{is bijective with inverse}\quad H_b^{-1}(d,r)=\frac{d+r}{b}.
\]

**Proof.** The half-open partition `I_d=[d/b,(d+1)/b)` has `floor(bx)=d`, and the affine map `x -> bx-d` maps `I_d` bijectively onto `I`. On every pair `(d,r)`, `(d+r)/b` lies in `I_d`, establishing both compositions. This is an elementary symbolic-dynamics coding, not a claim of new scholarly priority.

For an orbit `x_{n+1}=R_b(x_n)`, `d_n=d_b(x_n)`, a *realized digit* is an irreversible addition to the observer's journal but an **information-preserving** transition in the augmented pair `(d_n,x_{n+1})` relative to `x_n`. If the digit is thrown away, `R_b` has exactly `b` preimages of each residual. Informational forgetting and mathematical recentering must not be confused.

**Human/semantic boundary.** The words "selected" and "choice" name the reported observation; they do not imply human volition changes the deterministic digits of a fixed number. For `x={pi}` and `b=16`, the hexadecimal digits are already mathematically determined, whether or not an observer knows them. The next-frame *coordinate origin* may be called zero after the update, but the actual residual `x_{n+1}` need not equal numeric zero. The zero is a chart/anchor, not a claim that the subsequent state vanishes.

## 2. The Dirac mass is the jump of the declared frame chart (HTS-02; CLASSICAL / PROVED PAPER)

Fix frame spacing `a>0`. For **each** orbit from Section 1, define the right-continuous *multiplicative interpolation* on `n a <= t < (n+1)a`:

\[
 Q(t)=b^{(t-na)/a}x_n.\tag{2.1}
\]

It is a **model choice**, not a recovered physical path. At a boundary `t_n=(n+1)a`,

\[
 Q(t_n^-)=b x_n,\quad Q(t_n^+)=x_{n+1}=b x_n-d_n,
 \quad [Q]_{t_n}=Q(t_n^+)-Q(t_n^-)=-d_n.\tag{2.2}
\]

Consequently, as a distribution on `(0,infinity)` (locally finite sums; test functions compactly supported),

\[
 \boxed{DQ=\frac{\log b}{a}\,Q(t)\,dt
       -\sum_{n\ge0}d_n\,\delta_{(n+1)a}.}\tag{2.3}
\]

**Proof.** Differentiating (2.1) away from boundaries yields `(log b/a)Q`. Integration by parts separately on each interval, then summing, contributes exactly the jump `[Q]_{t_n}=-d_n` at each internal boundary. Equivalently, for every `phi in C_c^infinity((0,infinity))`,

\[
 -\int_0^\infty Q(t)\,\phi'(t)\,dt
 =\frac{\log b}{a}\int_0^\infty Q(t)\phi(t)\,dt
   -\sum_{n\ge0}d_n\phi((n+1)a).\tag{2.4}
\]

**The literal frame reset:** under **this** chart convention, a reset at a digit boundary is *exactly* the Dirac-atomic part of its distributional derivative. It is not merely a visual metaphor. Notice that for `d_n=0`, the boundary carries no jump despite the observer advancing to the next frame; the existence of a frame boundary does **not** imply a nonzero delta in this coordinate.

An equally valid *affine expansion chart* is `Q_aff(n a+s a)=x_n[1+(b-1)s]` for `0<=s<1`. It has the same jump `-d_n`, and

\[
 DQ_{aff}=\frac{b-1}{a}x_n\,dt\quad\text{on }(na,(n+1)a)
       -\sum_{n\ge0}d_n\delta_{(n+1)a}.
\]

The test suite checks an exact distributional pairing for this affine variant with rational coefficients, not merely the jump at one boundary.

### Non-negotiable negative control (HTS-03; REFUTED physical-necessity implication)

Define instead the *continuous* interpolation

\[
 C(na+s a)=(1-s)x_n+s x_{n+1},\qquad 0\le s\le1.
\]

Then **the same discrete orbit and snapshots** are reproduced but `C` has no boundary jumps and hence **no Dirac masses** in `DC`. Therefore

> "Discrete observations (or the human T-action alone) imply that the underlying physical evolution contains literal Dirac impulses"

is **REFUTED** by this explicit continuous interpolation. The defensible statement is the **conditional distributional identity (2.3)** for the declared jump chart. The proposed physical significance is a separate **UNVERIFIED** empirical hypothesis requiring a specific observable conjugate to impulse and independent temporal probes.

## 3. Connection to the already installed logarithmic sawtooth (HTS-04; CLASSICAL)

SUCC's `research/2026-10-27/BBP_LOG_DIRAC_SAWTOOTH_THREAD.md` (LS-1) establishes, for `P_a(t)={t/a}-1/2`,

\[
 \sum_{k\in\mathbb Z}\delta_{ka}-a^{-1}dt=-D P_a.
\]

This is the same distributional calculus: a smooth `1/a` drift between boundaries and unit reset jumps at boundaries. However **a sampling comb** `sum delta_(na)` marks *when frames are read*, whereas the **reset-current** `-sum d_n delta_((n+1)a)` records *how much the chosen chart jumps*. They are distinct measures; the latter requires actual digit marks. The existing authentic BBP *source-shifted* log nodes `t_n=n log16 - epsilon-shift_n` and Green pulses (LS-2/LS-2b) are a **third** object. Do not substitute these three combs for one another or conflate normalized Haar time with selected digit phases.

A separate prior SUCC motif is the prime-power event train `sum_(p,k) (log p) delta_(k log p)` and Gamma/Mellin's continuous weighted superposition of multiplicative atoms. Shared distributional mathematics does **not** identify these atomic supports or prove a physical, spectral, Weil, or BBP source isomorphism.

## 4. Why the before/after data do not reconstruct the generator (HTS-05; CLASSICAL)

A continuous circle history `z(t)=exp(i omega t)` observed at `t=n a` is observationally identical, for **every** integer `n`, to

\[
 z_k(t)=\exp\{i(\omega+2\pi k/a)t\},\quad k\in\mathbb Z,
\]

although the histories disagree between sample instants for `k != 0`. This is **temporal aliasing**. A sampling/reconstruction theorem needs extra bandwidth, regularity, source, or multi-clock constraints. Snapshot agreement, no matter how exact, is not generator identification.

For radix-b digit observations `O_N(x)=(d_0,...,d_(N-1))`, each feasible observed word has precisely the cylinder fiber

\[
 O_N^{-1}(d_0,\ldots,d_{N-1})
 =\left[\sum_{j=0}^{N-1}\frac{d_j}{b^{j+1}},\;
          \sum_{j=0}^{N-1}\frac{d_j}{b^{j+1}}+b^{-N}\right).
\]

Every such cylinder has a periodic-eventually rational seed and, by the classical almost-everywhere normality theorem for base-b expansions, also normal seeds. Thus **no finite list of digits alone certifies normality of its particular source**. Knowing the *full source specification*, rather than merely finite reports, is an additional constraint and potentially changes the reconstruction problem.

## 5. Haar factorization is exact but is not selected arithmetic (HTS-06; CLASSICAL)

For `X` distributed with normalized Lebesgue measure on `[0,1)`, change of variables in the `b` digit cells gives

\[
 (H_b)_*(dx)=\frac1b\sum_{d=0}^{b-1}\delta_d\otimes dr.
\]

So the first digit is uniform and independent of the recentered residual, and repeated use yields i.i.d. uniform digits for **Lebesgue-almost-every** initial seed (indeed as a measure-law). This is a property of the *ensemble*. It does not say that a fixed, source-selected `x={pi}` follows that typical law. One may retain the record and recenter without turning the numerical source into a probability draw. Conditioning on a selected digit versus resetting to an unconditional prior are different operations in SUCC's operational triangle.

Counterexamples: `x=0` produces `0,0,0,...` and `R_b(0)=0` forever; the full digit + residual action and its Dirac current remain perfectly well defined. Also, the source-shifted counterseed `s_*=-pi/16` in SUCC's authentic BBP recurrence retains the forcing but gives `U_n(s_*)=-T_n -> 0` (see the Main XVI seed-alias dossier). Such trajectories disprove any implication "exact frame reset -> normality" or "same forcing -> normality" without a selector constraint.

## 6. Authentication gate: where this meets SUCC's actual BBP recurrence

**Do not replace the historical four-pole source.** The authentic source in the 2026-10-27 dossier is

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
 \qquad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Its inherited Green identity is `U_(n+1)=pi*16^n - T_(n+1)` with a positive summable tail. Hence the actual fractional `U` phases and true radix-16 pi orbit have a bounded Fourier-sum comparison inherited from LS-3 / Main XVI, **not an exact equality of digit marks** at every index. A wrap/carry near a radix boundary can change a literal digit even when the real-phase discrepancy is small. No argument may silently set `d_n=floor(16 {U_n})` equal to an authentic pi digit without checking the chosen shift, Green tail, and literal carry.

The **still open** sourced gate is, for each fixed integer `h != 0`,

\[
 T_N(h)=\sum_{n=1}^N e^{2\pi i h U_n(0)}=o(N),
 \qquad \overline S_N(h)=T_N(h)/N=o(1).
\]

`Sbar_N=o(N)` is vacuous and forbidden; refer to `research/2026-10-29/triangle_genesis_repair/WEYL_NORMALIZATION_CONVENTION.md`. Every new observer must preserve the authentic `r`, `U_0=0`, four signed poles, full integer carry, and source posterior rather than claiming cancellation from uniform sampled Haar or scalar Gamma weights.

The source-aware version of the inverse problem is:

\[
 \mathcal F_N(d;\mathcal S)=\{\text{source-compatible candidate dynamics}\ P:
                O_N(P)=d\},
\]

where `S` is an explicitly declared authenticated source class. **Reconstruction** asks whether `F_N` shrinks to a uniquely compatible dynamical object; **property certification** asks whether *every* survivor has the desired invariant. Neither follows merely from a finite fit. If the property holds for all compatible candidates despite nonunique dynamics, path identification is not required. For unrestricted base-b seeds, HTS-05 shows this route fails; extra source/selection input is essential.

## 7. Steelman -> crucible -> verdict, with next verdict-changing probes

| ID | Steelman / exact statement | Receipt | Verdict and boundary |
|---|---|---|---|
| HTS-01 | Retain digit and residual; `H_b` invertible for all `x in [0,1)` | Half-open partition + exact inverse; finite rational test | **CLASSICAL / PROVED PAPER**; no reverse recovery after discarding digit |
| HTS-02 | Chosen expansion-then-recenter chart has reset current `-sum d_n delta` | Piecewise integration by parts + exact rational affine pairing | **CLASSICAL / PROVED PAPER** for declared chart only |
| HTS-03 | Snapshot/reset implies physical impulses | Continuous interpolation with identical snapshots | **REFUTED as an implication**; physical carrier model UNVERIFIED |
| HTS-04 | Bernoulli sawtooth derivative and reset current use the same jump calculus | LS-1; distinct weights and supports | **CLASSICAL analogy / typed distinction**; no source identification |
| HTS-05 | Snapshots alone identify continuum dynamics / certify selected normality | Oscillator aliases + digit cylinder with normal/nonnormal members | **REFUTED as universal implication**; extra source constraints required |
| HTS-06 | Uniform Haar source factors into digit and residual | Partition substitution | **CLASSICAL ensemble theorem**; no pi selection |
| HTS-07 | Authentic BBP frame-reset field *forces new signed intertime cancellation* | No such bound supplied; same-source counterseed/LS-4b/LS-5 controls | **CONJECTURED / UNVERIFIED**; open for pi normality |

**Finite verification:** `python -m unittest tests.test_human_t_action_snapshot` (or `python -m unittest discover -s tests -p 'test_human_t_action_snapshot.py'`). The tests use Python `Fraction` for 10 exact-model probes: invertibility, digit-loss fibers, jump magnitude, distribution pairing, sign mutation, finite Haar-grid fibers, finite-prefix underdetermination, temporal aliasing, continuous-interpolation countermodel, and nonnormal zero orbit. They do **not** execute repo-wide verification or independently prove any infinite selected statement.

**Next discriminatory probe.** Fix a nonzero character `h`, a finite native BBP horizon, and a source-typed pair of observer histories retaining `(d_n, residual_n, exact r(n), seed, carry, log-clock alias index)`. Construct an explicit **non-scalar**, noncircular intertime statistic from the source alone; predict a quantitative separation for the authentic `U_0=0` source versus (i) same forcing with `s*=-pi/16`, (ii) rational circle `alpha=1`, (iii) source-mutant/carry-mutant controls, (iv) source-matched higher-jet fakes, and (v) independent holdouts. Declare pass/fail/ambiguous before computing. A finite split is instrumentation, not an asymptotic normality bound. The genuine target remains a **new source-specific signed Weyl estimate**, not a restatement of the Weyl criterion or of the digit-selection event.

**Provenance and related dossiers:**

- `../../docs/FOUNDATIONS.md` — finite embodied observers, actualized records, proof boundary.
- `../../docs/OPERATIONAL_TRIANGLE.md` — source update, retained posterior, observation maps, memory-vs-curvature and Jensen defects.
- `../2026-10-27/BBP_LOG_DIRAC_SAWTOOTH_THREAD.md` and `../../docs/CLAIM_SUPPLEMENT_LOG_DIRAC_SAWTOOTH.md` — LS-1–7, exact log sampling comb, source pulse/Green, moving Mellin aliases.
- `../2026-10-29/triangle_genesis_repair/SEED_ALIAS_CLASSIFICATION.md` and `../2026-10-29/triangle_genesis_repair/WEYL_NORMALIZATION_CONVENTION.md` — controls, actual gate.
- `../../docs/CLAIM_SUPPLEMENT_CIRCLE_ORIGIN_GAUGE.md` — source-relative circle origin and false origin averaging.
- `../../docs/CLAIM_SUPPLEMENT_HISTORY_DTN.md` — interior/boundary inverse non-identification.
- Classical mathematics: the distributional derivative of functions of bounded variation; standard symbolic dynamics for the map `x -> {b x}`; uniform Lebesgue radix digits and Borel's normal-number theorem; frequency aliasing in sampled harmonic signals. No new academic-priority claim for these results.

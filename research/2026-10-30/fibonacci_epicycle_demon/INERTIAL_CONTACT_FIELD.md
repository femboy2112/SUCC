# SUCC: inertial finite capacity versus active causal information contact

Date: 2026-10-30. Additive research-only continuation of draft PR #397; Main XVI base e18ba565ca540adb7edf3292f5593929e76d91c5. No change to signed four-pole BBP source, U_0=0, archives, theorem namespaces, production, or main. Read-only context: #390-#392 (extrusion and Oily source), #396 (human T-action), #397 (no-discard information accounting), #398 (prime stroboscope).

## Author's load-bearing correction

> "inertial is loadbearing here, you can couple to infinite structure if you are actively moving. otherwise you're just locked into more geodesic degrees of freedom in the field."

**Steelman:** a finite observer cannot carry infinitely many independently realized distinctions in a bounded **internal** memory at any finite stage; it can successively access an unbounded carrier by finite interactions while exporting or compressing witnessed history. A finite symbolic description can designate an infinite object without independently observing every degree of freedom. The word *inertial* distinguishes possessed internal state from accessible external field structure.

**Critical precision:** operational "active" means a fresh distinguishable causal contact, not necessarily proper acceleration or nongeodesic motion. In relativity a free-falling geodesic can encounter new field data. A stationary receiver can receive a dynamic signal. An accelerated observer moving through a homogeneous field may get no new distinguishable data. Requiring acceleration would introduce a physically incorrect absolute-motion criterion.

## IC-01: coupled observer-carrier axioms (DECLARED)

Internal observer register S_t has at most 2^K distinguishable states for a fixed finite K, even when contact history grows. Let C_t be a carrier state, a_t an admissible probe/interaction, Y_t=O_(a_t)(C_t) the actual observation, and R_t an external retained record. A joint update is
\[
(S_{t+1},R_{t+1},C_{t+1})
=F_{a_t}(S_t,R_t,C_t,Y_t).
\]
No-discard means the **actually witnessed history** W_(0:t) can be recovered from the declared sufficient record (S_t,R_t) together with public protocol metadata. The claim is not that inaccessible unmeasured carrier bits must be stored. Read-only probing is allowed; a genuine physical backaction law on C requires a separately declared interaction and conservation mechanism. The environment can hold a growing record even while the observer's internal K stays fixed. A physical tape-head position may encode an external spatial address, but that address is not magically free if the interface must serialize it.

## IC-02: finite-memory obstruction and active external path (DISCLOSED)

If M possible witnessed histories are all admissible and each must be reconstructed from (S_T,R_T), with at most 2^K internal states and 2^E external record values, injectivity gives
\[
\boxed{K+E\ge\log_2 M}.
\]
For T independent b-ary contacts (all b^T words allowed), K+E>=T log₂ b. A constant K with E=0 cannot retain arbitrary independent histories for unbounded T. But E_T can grow, and a one-bit control head can scan an infinite carrier and append each bit to an external record, thereby preserving every finite prefix with K fixed. There is no finite-time infinite-information acquisition at finite bandwidth.

In SUCC's **declared** two-panel source model, if the full ordered 2n-trial Bernoulli word was actually witnessed, then conditional on known total grade s there are binom(2n,s) equiprobable admissible histories, even under total-grade Oily weighting. Therefore
\[
E\ge\max(0,\lceil\log_2\binom{2n}s\rceil-K).
\]
At s=1 and no external storage E=0, universal reconstruction requires 2n<=2^K, i.e. n<=2^(K-1). For any n beyond this capacity horizon either memory, external retention, or the observer's exact-history contract must change. This is a **memory capacity horizon**, not a black-hole causal event horizon. If only total grade was ever measured and word order was never witnessed, its unobserved order is not knowingly discarded.

Oily–Macaroni normalization from PR #397 changes the distribution of total grades but does not remove conditional chronological distinctions. Its asymptotic expected history uncertainty is 5.6580417264 log₂ n + O(1) bits, under its declared auxiliary ensemble. It is not a universal bit lower bound for the single computable π digit string.

## IC-03: fresh contact, not acceleration, is the discriminating instrument (DISCLOSED toy model)

Let an infinite frozen carrier consist of independent fair bits C_0,C_1,... . A **precommitted deterministic** sequence of probe addresses i_1,...,i_T produces Y_t=C_(i_t). The exact information of the collected observations is
\[
H(Y_1,\ldots,Y_T)=|\{i_1,\ldots,i_T\}|\text{ bits}.
\]
A stationary frozen probe i_t=0 gives one bit in total; a moving probe i_t=t gives T bits; cycling among p addresses saturates at p bits. But a stationary spatial probe of a **time-varying** field C_(0,t) can also receive T independent bits. Likewise freely falling geodesics can sample new spatial data and accelerating paths in homogeneous fields may sample none. Geometric displacement, acceleration, and new information contact are distinct variables.

For a declared ensemble and precommitted action path define the per-step conditional contact current
\[
J_t=H(Y_t\mid Y_{<t}, i_{1:T})\in[0,\log_2|\mathcal Y_t|].
\]
Chain rule gives H(Y_(1:T)|path)=ΣJ_t. Adaptive policies may leak data into the action-selection record, which must be included rather than conditioned away. For one fixed deterministic π stream assigned a point-mass prior, Shannon information gain is zero; using this instrument for π requires an explicit ensemble of possible carrier completions or a source-derived operational prior, and cannot silently assume independent random digits.

## IC-04: SUCC source-locked radix evolution is an exact lossless rechart (DISCLOSED, critical firewall)

The human T-action of draft PR #396 and SUCC's recentered BBP source use
\[
H_b(y)=(d,\{by\}),\quad d=\lfloor by\rfloor,\quad
y=\frac{d+\{by\}}b.
\]
At b=16 this retains the observed hexadecimal digit plus the residual. Keeping BOTH is bijective (with canonical half-open radix interval); forgetting d is many-to-one. In native zero-seeded BBP, the exact recentered trajectory is y_n={16^(n-1)π}, and observed digits must retain the correct integer seam/carry. Original four signed poles and U_0=0 are never modified.

However y is an exact real carrier coordinate, with infinitely many potential digits; putting y into a supposedly K-bit internal register would violate the axiom by assumption. With only m known exact radix-16 prefix digits, all 16 next-digit possibilities remain compatible with finite-prefix data, no matter how many times one symbolically iterates the same map without additional precision/knowledge. π is computable, so a finite program can calculate more digits using expanding computational resources; that is a sequential access process, not inertial infinite-memory possession.

## IC-05: observational geodesic directions and three nonidentical horizons (PROPOSED)

Given an observational map O and local tangent direction v, dO(v)=0 means motion along v is **locally invisible to this probe**. It does not mean v is physically lightlike, a spacetime null geodesic, or curvature. Such directions are candidates for the user's "geodesic degrees of freedom" in the restricted sense that they represent carrier distinctions not reached by this observation map. If more probes are added, the null directions can shrink.

Separate:
1. **Storage horizon:** lossless witnessed-history reconstruction exceeds finite internal+exported capacity.
2. **Contact/reachability horizon:** no admissible path and sensing channel can reach a specified carrier distinction within the modeled causal domain.
3. **GR event horizon:** a global spacetime causal boundary, distinct from the central singularity; a free-falling observer can cross a large black hole event horizon without any local curvature divergence. Sources: https://science.nasa.gov/universe/black-holes/anatomy/ and https://plato.stanford.edu/entries/spacetime-singularities/ .

A SUCC "causal-information-path defect" should measure actual failure of path reachability or observer distinguishability under a specified carrier and interaction grammar. Do NOT equate finite capacity with GR singularity or mistake the commuting posterior squares of PR #392 for nonzero curvature. Genuine nonzero holonomy requires an operationally specified, frame-transported, **noncommuting** history/carry channel with a gauge-invariant comparison.

## IC-06: verdict ledger and next falsifier

**DISCLOSED:** finite-state cardinality obstruction; exact SUCC s=1 storage bound; independent-bit static/moving/cyclic probes; radix digit+residual left-invertibility; an m-digit prefix never fixes the (m+1)th digit across all continuations.

**DECLARED:** bounded inertial register axiom, append-only external ledger, local carrier coupling policy, conditional contact entropy under a specified prior.

**REFUTED:** acceleration as necessary for new information; moving through homogeneous data as sufficient; exact real residual as a literal finite K-bit physical register; black-hole horizon as a local density singularity; positive posterior memory as automatic spacetime curvature.

**CONJECTURED/UNVERIFIED:** source-sensitive contact metric/connection; nontrivial history holonomy; physical observer-gravity coupling; π's normality/RH.

**Next discriminating probe:** compare (A) frozen stationary sensor, (B) active distinct-contact sensor with lossless external record, (C) same path with grade-only projection or posterior reset, then (D) actual original-zero-seed two-time signed carry/phase tensor. Reject the coherent same-forcing seed s*=-π/16 and higher-jet-matched mutants; calibrate normal Stoneham and nonnormal de Bruijn controls; demand a new non-circular signed all-horizon Weyl or occupancy bound.

Validation scope: standalone exact Fraction and combinatorial probe tests in inertial_contact_probe.py. Full native SUCC root tests, hosted CI, Lean, blind review NOT RUN. Research-only additive note.

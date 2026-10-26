# Categorical observer atlas

**Purpose.** Make category theory *operational and load-bearing* across SUCC species, as the
discipline for reasoning toward the selected-π estimate (`docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`).
It is **not** a new universal category and **not** a philosophical reframing.

**Firewall (AGENTS.md rule 6; `docs/ARCHITECTURE.md`).** A candidate categorical diagram counts
only with (i) a defined functor/action and object domain, and (ii) a *tested* commutation **or** a
*proved* obstruction. A matching numerical invariant, a positive Gram, or a visually attractive
analogy is **not** a theorem. Positive physical/semantic covariance is **not** a source-derived
positive Weil form. These lines describe π only if the actual arithmetic source says so.

**Reuse, do not rebuild.** Main already carries a deep categorical core (≈352 categorical unit
tests pass on the integrated tree). The de-facto **spine** is
`operational_yoneda_descent.ObservationPathCategory` + `yoneda.FiniteFunctor`. New SUCC species
are declared as *instances* of this spine, never as a second incompatible category class.
`prime_clock_yoneda.py` is the working template (true ring quotient $\mathbb Z/p^r\to\mathbb
Z/p^k$ as a `CertifiedSourceMorphism`; genuine-prime $V_q$ descends; a flat square hides a
noncommuting defect in its kernel).

## The seven typed layers

Each layer lists its objects/morphisms, its governing law, and whether it **REUSES** an existing
module or needs **NEW** construction. Status tags: *reuse-tested* (module exists, tests pass),
*new-obligation* (typed target, not yet proved), *negative-theorem* (a proved non-existence to keep).

| # | Layer | Objects / morphisms / law | Status | Where |
|---|-------|---------------------------|--------|-------|
| 1 | Arithmetic source/history | realized finite states $(n,U_n,r(n),U_0{=}0,$ integer carry, conductor$)$; successor $S$; genuine-prime FUCC $V_p$; typed boundary labels | **REUSE** (reuse-tested) | `integer_bbp_carrier`, `pi_source_genesis`, `pi_lag_carry`, `reciprocal_succ_fucc`, `carry_safe_polyphase`, `prime_clock_yoneda`, `edge_carrier_reconstruction`; thin typed adapter to `ObservationPathCategory` = the only new piece |
| 2 | Null / Seinfeld | free source-labelled expressions with evaluation-to-zero; syzygies; path 1-chains retaining provenance; char-$p$ Frobenius thickening with $p$-integrality gates | **NEW** | no existing category module (adjacent: `koszul_prime_cancellation`, `arithmetic_interactions` N=5 firewall). Content lands via #294/#295 (SS/SPH); categorical wrapper is new-obligation |
| 3 | Observer / indexed | fibers of states; probe access; target descent through observational equivalence; finite paid policies; source-realization firewall | **REUSE** (reuse-tested) | `beck_chevalley_source` ⋈ `carrier_indexed`; `operational_yoneda_descent.restricted_yoneda_arrow_detection`; `adaptive_proof_policy`; `no_ghost` (possible ≠ performed) |
| 4 | Phase / signed interference | exact $\mathbb Q[\mathbb Q/\mathbb Z]$ amplitudes; **full off-diagonal** $K_{a,b}=z_a\overline{z_b}$; pushforward $K\mapsto P K P^{*}$; Fourier/Fejér/Walsh/cyclotomic projections; positivity only after complex evaluation | **PARTIAL reuse + NEW wrapper** | pieces: `tate_schwartz_functor`, `profinite_hilbert`, `pascal_carry_interferometry` (Walsh), `bochner_kernels`; the **functorial $K\mapsto PKP^{*}$ naturality statement is new-obligation** |
| 5 | Geometry | $0,1,\infty$ **distinct** on $\mathbb{RP}^1$ (on $\mathbb R/\mathbb Z$, $0{=}1$ needs a cut + source-lift); fourth point $\lambda_n=\{U_n\}$ cross-ratio off-puncture; golden $\lambda$ and $j=2048$ are **chosen references**, not the source orbit ($\lambda_1=2/15$); the 16 groups $C_{16}, C_4{\times}C_4, (C_2)^4$ are **nonisomorphic** | **NEW** | no $\mathbb{RP}^1$ 0/1/∞ or Lattès module (adjacent: `dual_chart_riemann_roch`, `projective_euler_normalization`, `observation_pinned_geometry`); content via #303 |
| 6 | Analytic / boundary | additive-harmonic vs logarithmic SUCC; Gamma / q-Gamma normalizations; Euler–Mascheroni; Hurwitz/Epstein finite parts; Green tails; signed completed Weil as a **separate** RH gate | **REUSE** | `euler_mascheroni_succ`, `prime_categorical_sphere`, `tate_idelic_zeta`; content via #302 |
| 7 | Formal proof | Lean proposition statements from actual modules; explicit hypotheses; paper vs tested-finite vs kernel-checked vs conjecture | **REUSE** (fails-closed) | `proof_authority` (A/B/C/D), `proof_contracts` (quantifier prefix; blocks $\forall N\exists C\to\exists C\forall N$), `claim_namespaces` |

## Required diagrams as typed obligations (prove-or-obstruct, none assumed)

1. **Signed-interference pushforward.** $z'=P_f z,\ K'=P_fKP_f^{*}$ under partition coarsening
   $f$; check composition, restriction, provenance in $\mathbb Q[\mathbb Q/\mathbb Z]$ before
   root-of-unity evaluation. The missing signed low-frequency term is the typed obligation that
   *is* the π gate (§2 of the frontier doc) — never an automatic zero from positivity.
2. **Observed time-dependent conjugacy.** $g_n(x)=x-U_n$ conjugates $T_n$ to $x\mapsto16x$ but
   transports $e(hx)\mapsto e(h(y+U_n))$. **Negative theorem (keep):** no nonconstant continuous
   time-*independent* $F$ intertwines every authentic $T_n$ with one fixed map (dense subgroup of
   forcing differences). The time-indexed gauge preserves observations *only with transported readout*.
3. **Finite Beck–Chevalley (reuse #194).** Formal pullback equality $\neq$ actual-source
   realization; test the comparison map and ghost witnesses. Prove base change for amplitude
   pushforward $f_!$ on genuine pullback squares, then its tensor-square coherence — **no** claim
   of a new general theorem.
4. **Projective four-point / optional fifth.** Six cross-ratio charts, singular boundaries,
   exact golden $j$, noninjectivity. $M_{0,4}$/$M_{0,5}$ pentagon is classical; an associator is
   demanded only **after** a genuine monoidal source-labelled transport and a chosen flat
   connection. A KZ associator or $\zeta(2)$ appearance alone does not authenticate BBP.
5. **Functor obstructions (negative theorems, keep).** No group isomorphism among $C_{16}$,
   $C_4{\times}C_4$, $(C_2)^4$; the time-independent intertwiner no-go above.
6. **Target descent.** Observational equivalence determines the target only if the target is
   constant on observation fibers; destructive probes can defeat even pairwise-distinguishable
   single-copy identification. **No** assumption that finite normality readouts determine infinite normality.

## Collision traps (verified during integration)

- **"Atlas" is already overloaded**: `CARRIER_ATLAS.md`, `PI_GEARBOX_ATLAS.md`, the VOYAGER
  48+12 atlas, `edge_carrier_reconstruction.atlas`, `hilbert_weil_atlas.py`,
  `pontryagin_tate_atlas.py`. This doc is deliberately **"categorical observer atlas"** and mints
  **no** new claim-ID prefix (it cites existing PSF/OSP/SGO/IMW/GZB/CZB/SPH/SS claims). Run
  `claim_namespaces.unregistered_prefix_collisions` before adding any new prefix.
- **Duplicate type names**: `FiniteDynamics` lives in *both* `swarm_categories` and
  `evolving_observer_categories` (not the same type); `DescentError` in three modules; a second
  Beck–Chevalley (`covariant_proof_descent.FiniteBeckChevalley`) beside `beck_chevalley_source`.
  A Phase-3 module importing these must name its source explicitly.
- **Name traps**: `source_history_transport.py` is $W_1$ optimal transport, **not** categorical
  (≠ `carrier_indexed.transport_actual_history`); `mobius_index_infinity.py` is the Möbius
  *sieve* $\mu$, **not** Möbius maps on $\mathbb{RP}^1$.
- **Formal authority fails closed**: `_formal_catalogue.APPROVED_RECORD_DIGESTS` has exactly one
  entry on main and is owned by the integration coordinator. There is **no** Beck–Chevalley Lean
  file — `beck_chevalley_source` is Python-tested, so any BC claim is *Observed/tested*, not
  kernel-proved.

## What this atlas does not claim

It does not assert a source-faithful BBP functor, an $E_N^{*}=d_N^2$ identity, signed-Weil
positivity, π normality, RH, or any unprovability result. It records which existing categorical
machinery is reused, what remains a typed obligation, and which non-existence results are proved
and must be preserved.

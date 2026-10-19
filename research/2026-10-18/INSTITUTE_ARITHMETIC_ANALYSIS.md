# Authentic Gamma tail: a sharp logarithmic envelope and a paid Schur improvement

**Date:** 2026-10-18. **Authority:** paper proof, exact rational certificates,
and a replay of the original signed source; no Lean proof of the functional
analysis. **RH PROVED: NO.** The true first-window signed Schur form remains
undecided. Academic novelty of the inequalities is **UNVERIFIED**; the method
is classical convex quadrature and Fourier multiplier analysis.

## 1. Source and branch reconstruction relevant to this result

The integration worktree starts from main `610efac`. This stream read the
following actual commit objects, without merging their unreviewed stacks:

| PR | Exact head | Mathematical boundary retained |
|---|---|---|
| 155 | `1a84799575ca38a33ed552cf94a0850b5632525e` | Piecewise genuine prime-hinge integration; differentiated quotient projector; high bound is K-relative. A finite positive high compression gives no infinite surplus theorem. |
| 157 | `1bcebd265ee78ae6faef5995467df6c1d85b42cf` | Prime-index reconstruction imports an actual universal procyclic source and its cofinal finite quotients. Finite clocks do not establish cofinality. |
| 162 | `3512c24bd582f8572d98bc0728d2cf947b7e7d2f` | Carry/CRT and source-minimality obligations; density-one/isozero generalized-prime sources need not have the original completion. |
| 163 | `f038076a377b8906789994524664023bc8dd871f` | Actual source center/edge residual observations; measured rank-one cross sign is not the entire unknown Gram cross sign. |
| 165 | `dea8b7f982fd3eb2361ccd5a12d360bcadfa3689` | LCM/Möbius prime jets require declared arithmetic source; finite orbit thresholds do not supply arbitrary clocks. |
| 168 | `089467b38e5ae2f096dba49a91ab96e9ff48c671` | A genuine finite Gamma packet may repair a selected signed direction; no all-high or all-radius positivity follows. |
| 169 | `64aa0810d9016c9c6948034d0543424f46db011e` | Local scaling tests away from identity; successor does not descend to the multiplicative adèle-class quotient. Principal value/contact remains a separate obligation. |
| 171 | `8c46cca801b57a6381dfac08e41731ca70d38904` | Carleman boundary strong limit is not operator-norm convergence; its H1 test bound is not a K-relative inverse bound. |
| 172 | `793f559ecf4fee9c9b03b98020bb20e3d7e36f3e` | Full valuation towers repair the discarded p² shell; Koszul-Hodge positivity is an auxiliary source form. |
| 173 | `a2ea6859416f0cb6a2939ec577453c6ea9227a84` | Weighted backward clock and flat Haar become separated in total variation; changing measure needs a transported action. |
| 174 | `6fb1dba87ed273350a636b14b248fccacfb88934` | Primitive K-Hilbert completion and H²-zero-extension trials; authenticated positivity on two high directions is a finite-subspace statement. |
| 175 | `8216c6fc042704aecd5fb7872facd681216e4be7` | Koszul generator multiplication can vanish on homology while its chain-level source clock/defect remains nonzero. |
| 176 | `a17197697c0ea0259592500b233419fbedf691cf` | Positive Möbius projectors and genuine compact-open finite-adèle tests do not reconstruct character, conductor, real Gamma or identity contact. |
| 177 | `f309d9104ba480c1999c962af1df7c50f19e1bfe` | Full original continuum action residual; paid H1/H2 Gamma tails; source-conditional Schur lower, with sign still open. |

These are scoped dossier audits, not certifications of every theorem/test on
those branches. Commit ancestry and complete repository validation are recorded
by the principal stream. Shared source files and shared branch ancestry are
one provenance family, not independent sources.

The immutable code source used here is
`observational_succ/source_weil_hierarchy.py`, Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`. Its genuine single-real-Gamma
term in the screw kernel is

\[
 -\sum_{j\ge0}\frac4{(4j+1)^2}
       (1-e^{-(4j+1)|t|/2}).
\]

The original completed source also contains the true prime-power tape,
half-density, contact and both poles. The present comparison changes none of
those channels. The source module is byte-checked before a claimed authentic
receipt. `provenance/IMPORT_MANIFEST.json` and the frozen originating-source
commit were inspected; the Gamma source above is a subsequent SUCC source
artifact, not falsely relabelled as an original imported file.

The primary external normalization was checked against Suzuki's
[equation (1.3) and the primitive/operator domains](https://arxiv.org/html/2606.09096v3).
No zero ordinates are inputs.

## 2. IN-GAMMA-01: convex logarithmic enclosure, with optimal shift

**Quantified statement.** For every integer J>=1 and every real frequency
ξ, put d=4J+1 and

\[
 m_J(\xi)=\sum_{j\ge J}
 \frac{16\xi^2}{(4j+1)((4j+1)^2+4\xi^2)}.
\]

Then

\[
 \boxed{\frac12\log\left(1+\frac{4\xi^2}{d^2}\right)
       +\frac{8\xi^2}{d(d^2+4\xi^2)}
 \ \le m_J(\xi)\le\
       \frac12\log\left(1+\frac{4\xi^2}{(d-2)^2}\right).}
 \tag{1}
\]

The constant shift 2 is the smallest real c for which the upper of the form
`(1/2) log(1+4ξ²/(d-c)²)` can hold simultaneously for all J>=1 and all ξ,
with positive denominator d-c.

**Proof.** At ξ=0 everything is zero. Otherwise define

\[
 f(s)=\frac{16\xi^2}{s(s^2+4\xi^2)},\qquad s>0.
\]

It is positive, decreasing, integrable at infinity, and strictly convex:

\[
 f''(s)=
 \frac{32\xi^2(6s^4+12s^2\xi^2+16\xi^4)}
 {s^3(s^2+4\xi^2)^3}>0.
\]

Convex midpoint quadrature on each width-four cell centred at d+4k gives

\[
 f(d+4k)\le\frac14\int_{d+4k-2}^{d+4k+2}f(s)\,ds.
\]

Summing the nonnegative cells and taking the monotone limit gives the upper
in (1), because

\[
 \frac14\int_a^\infty f(s)\,ds
       =\frac12\log(1+4\xi^2/a^2).
\]

Convex trapezoidal quadrature on [d+4k,d+4k+4] gives
`(1/4) ∫_d^∞ f <= sum_(k>=0) f(d+4k) - f(d)/2`, proving the lower.
The factor 1/4 is the authentic rung spacing, not an adjustable source weight.

For sharpness, dominated convergence as ξ→0 gives
`m_J(ξ)/ξ² ->16 sum_(k>=0)(d+4k)^(-3)`. By the lower just proved this is at
least `2/d²+8/d³`. A putative upper with fixed c<2 would give
`2/(d-c)²`. For sufficiently large d=4J+1,

\[
 (d+4)(d-c)^2-d^3
  =(4-2c)d^2+(c^2-8c)d+4c^2>0,
\]

so the required inequality fails for sufficiently small nonzero ξ. This
proves optimality within the stated family; it does not assert optimality
among all possible Gamma-tail bounds. ∎

The exact tests independently refute shifts c=0 and c=1. The prefix/integral
oracle is implemented separately from midpoint quadrature; its finite checks
calibrate arithmetic, while the proof above supplies the universal quantifier.

## 3. IN-GAMMA-02: legitimate operator-action improvement

Let I be a bounded interval and extend functions by zero to the real line.
For d_j=4j+1, the source primitive rung is

\[
 \Gamma_j=\frac4{d_j}I-E_{d_j/2},\qquad
 E_\alpha F(x)=\int_{\mathbb R}e^{-\alpha|x-y|}F(y)\,dy.
\]

Under the Fourier convention in which differentiation multiplies by iξ,
`E_α` has multiplier `2α/(α²+ξ²)`, so the omitted positive tower has precisely
the multiplier `m_J` above. The interval action is its restriction to I.

For every `F in H¹_0(I)` the zero extension belongs to H¹(R), and

\[
 \boxed{\|\Gamma_{\ge J}F\|_{L^2(I)}
 \le \frac{13}{16(d-2)}\|F'\|_{L^2(I)}.}                 \tag{2}
\]

If in addition `F in H²_0(I)` (both F and F' have zero traces), its zero
extension belongs to H²(R), and

\[
 \boxed{\|\Gamma_{\ge J}F\|_{L^2(I)}
 \le\frac2{(d-2)^2}\|F''\|_{L^2(I)}.}                  \tag{3}
\]

**Proof of constants and domains.** The elementary inequality
`log(1+y²)<=13y/16` holds for all y>=0. For
`F(y)=13y/16-log(1+y²)`, the derivative has the sign of
`13y²-32y+13`. Its only positive local minimum is
`y+=(16+sqrt(87))/13`, enclosed by `[1948/1000,1949/1000]`.
An exact atanh-series log bound certifies

\[
 \frac{13}{16}\frac{1948}{1000}
 -\log\left(1+(1949/1000)^2\right)>1/100.
\]

Together with F(0)=0, its derivative sign pattern proves the claim on the
whole positive half-line. Substitution `y=2|ξ|/(d-2)` into (1) gives
`m_J(ξ)<=13|ξ|/[16(d-2)]`. Likewise `log(1+t)<=t` gives
`m_J(ξ)<=2ξ²/(d-2)²`. Squaring these **pointwise multiplier inequalities**,
integrating against `|Fhat|²`, and applying Plancherel proves (2)/(3).
Restriction to I is a contraction. Dominated convergence justifies the
infinite positive multiplier sum and its action on the declared domains. ∎

The H² conclusion requires the derivative trace condition. A general H¹_0
primitive has boundary deltas in the distributional second derivative of its
zero extension; it cannot enter (3). Neither theorem is a bounded
`L² -> L²` tail estimate, and neither turns the derivative-carrier source
bound `D4>=κK` into `D4>=κI` on derivative L².

The old source bounds from PR177 were
`σ_old=1/d+4/d²` and `τ_old=2/d²+16/d³`.
Equation (2) is strictly better for every J>=1, as follows from
`3d²+32d-128>0` for d>=5. Equation (3) is strictly better for J>=2;
at J=1 it is worse and the code retains the old H² bound. It always chooses
the minimum of independently valid bounds, never a fitted effective norm.

| J | old H¹ coefficient | new H¹ coefficient | old H² coefficient | selected H² coefficient |
|---|---|---|---|---|
| 1 | 9/25 | 13/48 | 26/125 | 26/125 |
| 2 | 13/81 | 13/112 | 34/729 | 2/49 |
| 8 | 37/1089 | 13/496 | 82/35937 | 2/961 |
| 24 | 101/9409 | 13/1520 | 210/912673 | 2/9025 |

At J8 the H¹ coefficient improves by `4195/18352` (~22.86%) and the H²
coefficient by `3464/39401` (~8.79%). These refer to action-norm budgets,
not to the actual unknown Schur error.

## 4. IN-GAMMA-03: real source replay and exact Schur gain

The optional probe exports **only** the package at the exact PR177 commit
into a temporary directory. It does not install or merge that branch. The
child Python process is limited to 1 GiB address space and 240 CPU seconds,
with a 270-second parent timeout. The replay uses J8, Taylor degree80, polar
degree18, eta=1/4, the existing source-selected rational high trials, the
entire original continuum action and signed low energies.

Every original `H²_0` endpoint trace is rechecked. The original source error
budgets, finite continuum residual Gram, contact, poles, prime2, half-density,
inherited high coercivity and fitted coefficients are unchanged. The new
Gamma constants alone reduce each column's omitted action error.

For each parity block the archived bound has a tail contribution
`-(1+1/eta) sum_i epsilon_i² I/κ`. Consequently the new lower differs from
the old lower by the **exact positive scalar**

\[
 \Delta_\pi I=\frac5{\kappa_\pi}
  \left(\sum_i(\epsilon_{\rm finite,i}+t_{\rm old,i})^2
       -\sum_i(\epsilon_{\rm finite,i}+t_{\rm new,i})^2\right)I.
                                                               \tag{4}
\]

The receipt retains the full rational matrices and verifies `Δπ>0`, so
the following displayed decimals are summaries, not proof certificates:

| derivative parity | exact gain, decimal display | old worst diagonal | new worst diagonal | new lower PSD? |
|---|---:|---:|---:|---|
| odd | 0.0108104393105858 | -0.0274289870243312 | -0.0166185477137454 | no |
| even | 0.0048590125939643 | -0.0127028756009474 | -0.0078438630069831 | no |

Thus this is an actual strict Loewner improvement of a full continuum
source-conditional S4 lower, but the sign remains **AMBIGUOUS**. A negative
lower matrix is not a negative vector of the genuine signed Weil form.
The inherited high coercivity premise has not been independently re-proved
in this stream. The result does not certify all radii, RH, or a positive
Connes trace.

## 5. Source-compatible arithmetic interface, and what is still missing

The arithmetic branches provide several compatible *local* interfaces:

1. A universal profinite clock with its declared cofinal finite quotients
   recovers genuine subgroup indices; Haar shell mass then fixes `p^-k`.
2. The source log clock supplies `log p`, so combining shell half-density
   and that clock recovers the magnitude `log(p) p^(-k/2)`.
3. Finite Möbius tests `sum_(d|M) μ(d) 1_(d Zhat)` are genuine
   Schwartz–Bruhat functions. Their finite Fourier transform and Haar
   normalization are well-defined without changing the atomic Hilbert space
   into Haar L² by assertion.
4. Local Connes compact-open tests away from identity require actual
   multiplicative Haar and inversion transport; additive successor does not
   automatically act on the multiplicative quotient.

These routes lose or omit different data. A chain-level prime multiplication
that is nullhomotopic can have a nonzero source-clock commutator. Passing to
homology therefore cannot be treated as an information-preserving transport
of the source trace. Positive sieve projections have no character phase,
conductor, real Gamma, polar or canonical identity-contact specification.
Their positivity cannot identify the original signed completed distribution.

A defensible next comparison domain is finite sums of tensors
`φ_infinity ⊗ 1_(a+d Zhat)` with real Schwartz `φ_infinity`, together with
their explicit Fourier transforms and source normalization. To compare a
scaling trace on that domain with the original signed Weil functional still
requires its regularized identity term and compatible Mellin/pushforward
domain. No such full comparison is proved here. The immutable source gate
rejects coefficient mutations, but byte equality of a module does not prove
that every proposed operator interpretation matches the primary paper.

## 6. Prior art, independence and failed routes

The multiplier has the exact classical representation

\[
 m_J(\xi)=\Re\psi(J+1/4+i\xi/2)-\psi(J+1/4),
\]

by the [standard partial-fraction digamma expansion](https://dlmf.nist.gov/5.7.E6).
Convex midpoint/trapezoidal bounds are classical. Shifted Gamma/digamma
inequalities have an extensive literature; the checked primary paper by
[Diamond and Straub (2015)](https://arxiv.org/abs/1508.03267) treats shifted
Gamma expansions and complete monotonicity. It is a relevant comparison,
not an asserted exact prior occurrence of (1). Connes's
[trace-formula paper](https://arxiv.org/abs/math/9811068) is the source of the
regularized scaling-trace setting, not a theorem supplied by the finite
projection construction.

**Novelty boundary:** the source-specific logarithmic envelope, optimal
shift proof, rational constant certificate and measured source Schur gain
are new contributions to this worktree. No academic priority is claimed.
Exact prior-art equivalence for the complex-digamma inequality remains an
explicit debt before a standalone publication claim.

The derivation was done in a separate arithmetic/analysis agent stream;
the principal independently checked its convex derivative and quadrature
factors. Both use the same model/repository context. This is method/reasoning
diversity, not blind external peer review. The prefix+integral oracle has
different arithmetic decomposition but the same authenticated source.

Failed routes preserved:

- Hostile review corrected the certificate field from
  `strict_global_minimum_margin` to `positive_local_minimum_margin`:
  the positive margin bounds F at its positive local minimum, whereas
  F(0)=0 is the global minimum. The inequality proof and numerical
  certificates are unchanged. The replay receipt received only this
  metadata-key correction; its source computation was not rerun.
- `log(1+y²)<=4y/5` is false: y=2 gives `log5>8/5`, certified exactly.
- Using d rather than d-2 as the upper-log denominator is false; a shift of
  one also fails. Both have exact positive-frequency counterexamples.
- Calling the new H² coefficient uniformly better at J1 is false.
- A coarse monotone-prefix **upper** can exceed a stronger valid midpoint
  upper. Initial independent tests used 64/96 terms and failed this overly
  strong enclosure condition. At J31, ξ=500 the true interval overlaps the
  midpoint envelope; it is the coarse remainder that is too wide.
  A retained regression verifies this and that 1024 terms resolve it.
- The optional archive replay initially rejected Git's top-level directory
  entry `observational_succ`; the archive-member validation was repaired
  before any source run. This was an execution preflight failure, not a
  mathematical result.

## 7. Receipts and remaining discriminators

Executed commands:

```sh
python3 -m unittest discover -s tests -p 'test_institute_schur.py' -v
python3 scripts/institute_schur_probe.py \
  --output research/2026-10-18/INSTITUTE_GAMMA_RECEIPT.json
/tmp/succ-institute-venv/bin/python scripts/institute_schur_probe.py \
  --replay-pr177 \
  --output research/2026-10-18/INSTITUTE_GAMMA_SCHUR_REPLAY.json
```

The focused suite passes seven tests, with 16 separate held-out rational
frequency/cutoff calibrations. The probe adds 20 calibration cases. Python
3.12.3 was used; source replay uses the principal's isolated mpmath1.3.0
environment. The replay JSON records exact coefficients, matrices, source
commit/blob, version, runtime and resource limits. The proof uses no floating
point; displayed runtime and decimal summaries are metadata only. A clone
without PR177's commit object must fetch that reviewed commit before using
the optional replay. Ordinary new tests require no such branch dependency.

| Claim | Authority | Remaining debt |
|---|---|---|
| IN-GAMMA-01 | PAPER PROVED; rational arithmetic controls | Lean analysis formalization; exact prior-art search |
| IN-GAMMA-02 | PAPER PROVED on explicit H¹_0/H²_0 domains | No full-L² or K-inverse promotion allowed |
| IN-GAMMA-03 | EXACT SOURCE REPLAY, inherited coercivity conditional | Both new lower blocks remain negative definite (negative diagonals and positive determinants); this does not decide the true S4 sign |
| arithmetic-to-completed-Weil trace | UNVERIFIED | Common domain, contact, poles, conductor, phase, regularized trace |
| completed all-radius positivity/RH | UNVERIFIED | No complete source-positive identification or all-radius proof |

The highest-value next probes for this stream are:

1. Insert the frequency-resolved logarithmic upper itself, with a certified
   low/high Fourier split, into the actual residual norm. Reducing it first
   to a universal derivative coefficient discards source-frequency data.
2. Use exact exp-polynomial OU boundary layers for the same lawful trials
   to reach deeper J without large Taylor-polynomial costs; independently
   cross-check the original signed channels and new Gamma budgets.
3. Establish a genuine directional source-surplus square-root range theorem
   on the **actual residual**, or exhibit its failure. More finite positive
   high-space samples cannot pay that infinite-dimensional debt.

This is a publishable-quality technical lemma and reproducible improvement
candidate for an appendix, pending external review and prior-art resolution.
It is not yet a standalone significant new theorem about the zeta function.

## 8. Deeper J24 replay and an exact obstruction to all Young parameters

The principal subsequently replayed the same source at J24, Taylor degree
192, polar degree18, retaining the improved Gamma constants and eta=1/4.
`INSTITUTE_GAMMA_SCHUR_J24.json` records the exact output. Decimal displays
of the new conservative blocks are

\[
 L_{\rm odd}\simeq
 \begin{pmatrix}-.000958609&-.000412570\\-.000412570&-.000546265\end{pmatrix},
 \qquad
 L_{\rm even}\simeq
 \begin{pmatrix}-.001247105&-.000843774\\-.000843774&-.000923772\end{pmatrix}.
\]

Both conservative lower matrices are negative definite by **exact rational**
leading-diagonal and determinant checks. This still gives no negative
direction for the genuine source form. It motivates the following specific
discriminator: is the arbitrary choice eta=1/4 responsible for the failed
certificate?

### IN-GAMMA-04: universal Young-parameter obstruction on fixed source data

Let T be a real symmetric retained trial-energy lower, M a positive
semidefinite nominal continuum residual Gram, κ>0 the retained source high
coercivity constant, and δ_i>=0 the separately certified residual-column
errors. These objects are held fixed. For a real coefficient direction c set

\[
 t=c^TTc,\quad m=c^TMc,\quad e=\sum_i |c_i|\delta_i,
 \qquad H=\kappa t-m-e^2.
\]

The best value obtainable by optimizing scalar Young in the direct triangle
residual majorant is

\[
 t-\kappa^{-1}(\sqrt m+e)^2.                              \tag{5}
\]

It is **strictly negative iff**

\[
 H<0\quad\hbox{or}\quad(H\ge0\ \hbox{and}\ H^2<4me^2).   \tag{6}
\]

In particular, (6) prevents a PSD certificate from **every** η>0 and every
positive diagonal Young allocation of these same column errors. The simpler
condition `κt<m` proves the obstruction even if the declared error budgets
are reduced to zero in this sufficient-bound formula while T,M,κ remain
fixed.

**Proof.** For two columns put a=|c1|δ1,b=|c2|δ2. A diagonal error allocation
with θ>0 has directional size

\[
 g_\theta=(1+\theta)a^2+(1+\theta^{-1})b^2
          =(a+b)^2+(\sqrt\theta a-b/\sqrt\theta)^2\ge e^2.
\]

The original isotropic choice also dominates e² by Cauchy–Schwarz. More
generally, for positive weights with sum w_i=1,
`sum_i (|ci|δi)²/w_i >= e²`. For every η>0,

\[
 (1+\eta)m+(1+\eta^{-1})g
 \ge(\sqrt m+\sqrt g)^2\ge(\sqrt m+e)^2.
\]

Equality is attained at η=sqrt(g/m) when m,g are positive; degenerate cases
give the same infimum at the parameter boundary. Thus (5) is an upper
envelope of the family of conservative lower certificates in direction c.
Rearranging its strict negativity gives `H<2 sqrt(m)e`, equivalent to (6),
including the cases m=0 or e=0. The test must check the sign of H **before**
squaring. If κt<m then even the nominal residual term suffices. ∎

This is an exact obstruction to a specified **sufficient-certificate
family**, not a spectral statement about the real high operator. The actual
source has structured errors, additional positive energy, and possible
non-scalar inverse estimates which T,M,κ,δ do not retain.

### Authentic fixed-budget result

One fresh J24 source evaluation exported the full original decomposition;
the code then changed only exact rational Young parameters. Its reconstructed
eta=1/4 lower agrees **entry for entry** with the principal's sealed J24
receipt. The saved decomposition is
`INSTITUTE_GAMMA_ETA_SOURCE.json`, SHA256
`0a24144e8a22178296ad314e846ea13ab41a67efc291a42b6764f73d61e0d7aa`.
Resume mode rejects every other cache digest. The source remains the PR177
commit and immutable source blob specified above.

Each parity used 15 dyadic η values from 1/128 to128 and, for each, the
original isotropic error allocation plus 15 dyadic θ values: 240 exact
matrix certificates per parity. None is PSD. This finite grid is only an
exploration; the following rational witnesses close the universal question:

| parity | direction c | t, decimal display | m, decimal display | t−m/κ, decimal display |
|---|---|---:|---:|---:|
| odd derivative | (1,0) | .000145244174621102 | .000082253324849424 | −.000507559990850513 |
| even derivative | (1,0) | .000328758536963199 | .000330361966138415 | −.000750855731462995 |

Both deficits are strictly negative as exact fractions in
`INSTITUTE_GAMMA_ETA_SEARCH.json`. Thus **all** positive η and all positive
diagonal error allocations fail for these fixed retained source objects.
In fact the witnesses prove the stronger purely algebraic statement:
for **every** η>0 and **every** positive-semidefinite matrix D,

\[
 c^T\left[T-\frac{(1+\eta)M+D}{\kappa}\right]c
 \le t-m/\kappa<0\qquad(c=(1,0)).
\]

This assertion depends only on the recorded rational T,M, positive κ, and
their exact inequality; it does not require assuming that the source
coercivity hypothesis is true. The receipt separately preserves the exact
nominal gap `κt-m`. Interpreting any of these matrices as source Schur lowers
still requires its original source hypotheses.
Even removing the declared error penalties from this formula cannot make
its first diagonal nonnegative. The fixed Young parameter is therefore
**not** the sole bottleneck. Improving the source trial, the retained trial
energy, the nominal residual itself, or the scalar inverse comparison is
necessary for this route. Reducing Gamma error alone with unchanged T/M is
insufficient; increasing J can change T/M and is not ruled out.

The next discriminator should target source-specific residual cancellation
or a genuine non-scalar inverse bound, instead of further η tuning on this
same packet. None of this proves a negative original Weil energy or RH.

### Execution and audit trail

`scripts/institute_eta_probe.py` performs one bounded source evaluation and
all later calculations from its exact decomposition. `--resume-source` skips
source recomputation and verifies the sealed cache digest. The completed
algebra replay took approximately one second and under25MiB; its exact
timing is metadata in the receipt. Source computation has 1GiB and240 CPU
second limits and the parent timeout is270 seconds. Four focused tests
check parameter sensitivity, off-axis obstructions despite positive axes,
diagonal error allocations, and the H<0-before-squaring requirement.

Two attempts exited before producing a complete serialized receipt. The
first wrapper did not expose child stderr. The second completed source and
algebra but failed while serializing the large squared exact witness:
Python's default4300-digit integer conversion cap was exceeded. This actual
failure is preserved in `INSTITUTE_GAMMA_ETA_FAILURE.log`.
The source decomposition was checkpointed before serialization. The repaired
script uses a guarded50000-digit cap for this bounded exact calculation and
replays algebra from the sealed cache, without a third expensive source run.
The first failure's precise cause was not observed directly; the second is
the recorded diagnosis, not an invented successful run.

Reproduction:

```sh
# Fresh source command used by the failed attempts; now serialization-safe:
/tmp/succ-institute-venv/bin/python scripts/institute_eta_probe.py \
  --output research/2026-10-18/INSTITUTE_GAMMA_ETA_SEARCH.json
# Executed repair path reuses the sealed source; it does not rerun the source:
/tmp/succ-institute-venv/bin/python -m unittest discover -s tests \
  -p 'test_institute_eta.py' -v
/tmp/succ-institute-venv/bin/python scripts/institute_eta_probe.py \
  --resume-source research/2026-10-18/INSTITUTE_GAMMA_ETA_SOURCE.json \
  --output research/2026-10-18/INSTITUTE_GAMMA_ETA_SEARCH.json
```

The claim is **PAPER PROVED / EXACT FINITE SOURCE-CERTIFICATE OBSTRUCTION**.
Its algebra is classical. Academic novelty is not claimed. The source
application retains the inherited coercivity hypothesis and current chosen
trials/error budgets. The hostile audit stream separately reconstructs the
source decomposition and witness; that check must be reported from its own
receipt rather than inferred from this stream's tests.

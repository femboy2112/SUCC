# Operation PRIME GENESIS: convolutional arithmetic, affine-braid rigidity, and the Archimedean unit

**Date:** 2026-10-17. **Proposed base:** SUCC `main` at `610efacf02556e1c5922bc5d4e87d0087f19b446` (verify actual PR ancestry). **Scope:** mathematical carrier reconstruction, not an RH proof. **Status:** elementary conditional paper proofs + exact bounded machine instances + explicit missing source law. **Historical source data, original Suzuki operator, completed Gamma/poles/Weil tests are unchanged.**

> **Question.** Which source laws force an abstract multiplicative prime-jet geometry to carry the **ordered semiring** of positive integers, instead of an arbitrary Beurling generalized-number system?
>
> **Verdict.** Prime jets, their convolution exponential, free unique factorization, logarithmic flatness, and positive Euler/Mellin transforms **DO NOT** force it. A uniform *rank-dilation law* plus one independently normalized additive real Haar cell **DO**; the rank-dilation law is equivalent to the global affine braid. No source-only derivation of it has been established. Source-law derivation is the remaining goal.

## 0. Repository map and prior-art firewall

Original SUCC representation works assumed the ordinary integer carrier before comparing successor and prime multiplication:

- `research/2026-10-16/UNIT_PRIME_SUCC_FLAT_CORRESPONDENCE.md` / `observational_succ/unit_prime_succ.py`: weighted vacuum SUCC/FUCC vectors, affine braid, distinct operator defects. Equality of a weighted vector is **not** conjugacy of SUCC and FUCC.
- `research/2026-10-16/UNIT_PRIME_TATE_LOG_CLOCK_BRIDGE.md`: genuine finite-place Haar shell mass, real Gaussian and Gamma, true prime-power current; the real place is an additional source law.
- `research/2026-10-16/SUCC_FUCC_TATE_MELLIN_SOURCE_TRIANGLE.md`: exact hyperbolic factor cone versus natural prefix and convergence bounds. Finite prime rectangles are **not** natural prefixes.
- `research/2026-10-15/EDGE_CARRIER_RECONSTRUCTION_LAB.md`: source-preserving bigger-carrier certificates and correct non-equivalences.
- Latest `research/2026-10-16/SUCC_ACADEMIC_MAIN_III_RESEARCH_FRONTIER.md` and open source-exact Suzuki PRs: complete signed Weil positivity and original first-window Schur sign remain unresolved.

**Classical mathematical provenance:** A. Beurling (1937), generalized prime systems, *Acta Math.* 68, 255–291, DOI `10.1007/BF02546666`; H. G. Diamond and W.-B. Zhang, *Beurling Generalized Numbers*, AMS Mathematical Surveys and Monographs 213 (2016), chapter 3, *dN as an Exponential and Chebyshev's Identity*; Bost–Connes, *Selecta Math.* 1 (1995), 411–457, DOI `10.1007/BF01589495`, for a **related** affine/zeta dynamical system. Convolutional counting and Euler products are not SUCC inventions. The ordered-rank proof below uses elementary multiplicative rigidity; originality/priority is **UNVERIFIED**.

## 1. Input law, carrier and source-indexed controls

Declare a finite/countable set of abstract primitive labels `j ∈ J` and the **free** commutative monoid

\[
 M=\bigoplus_{j\in J}\mathbb N_0 e_j,\quad 1_M=0,\quad V_j\alpha=\alpha+e_j.
\]

The positive cone in the **metatheory** uses finite integer exponents; `N` is *not* a privileged source carrier with predecessor/successor/ordinary primality. Assign strictly positive prime log clocks `λ_j` such that

1. `u := inf_j λ_j > 0` (a genuine source gap);
2. for each `T < ∞`, only finitely many `λ_j ≤ T` (local finiteness);
3. the evaluation `h(α)=Σ α_j λ_j` is **injective** (independent prime-word evaluation; stronger than simply having free word labels).

Let `q_j=e^{λ_j}>1`. Conditions 1–2 make the image `h(M)` locally finite; condition 3 makes its atom masses one. In the program, rational `q_j` are encoded as exact `Fraction`, without evaluating `log`, `exp`, prime enumeration, ζ, or any nontrivial zero. **Labels are declarations, not independently authenticated arithmetic primes.** Repeated-valued or fake composite labels are permitted as hostile models and yield collisions.

At each finite horizon `H`, only words with `∏q_j^{α_j}≤H` are source-accessible. A generator beyond the horizon is invisible; an observer cannot infer its absence.

## 2. JET-01 — classical prime-jet convolution exponential

Use logarithmic additive convolution `*` and the Dirac mass `δ_t` at log-energy `t`:

\[
 J=\sum_j\sum_{k\ge1}\lambda_j\,\delta_{k\lambda_j},\quad
 \Pi=t^{-1}J=\sum_j\sum_{k\ge1}\frac1k\delta_{k\lambda_j},\quad
 \mu=\exp_*\Pi:=\delta_0+\sum_{r\ge1}\frac{\Pi^{*r}}{r!}.
\]

**Theorem (CLASSICAL / paper proof):** On each bounded interval, these convolutions and their exponential are finite sums. Moreover,

\[
 \mu=\underset{j\in J}{*}\left(\sum_{k\ge0}\delta_{k\lambda_j}\right)
 =\sum_{\alpha\in M}\delta_{h(\alpha)}.
\]

**Proof:** At each single generator `j`, `exp(Σ_{k≥1}z^k/k)=1/(1-z)` as a formal series. Every nonempty jet has log-energy ≥u, so in `[0,T]` only orders `r≤T/u` occur and finitely many generator/exponent coordinates contribute. Multiply finite truncated formal identities and pass to a locally finite measure limit. Injectivity of `h` makes every atom's mass one; without it, mass equals the count of source-distinct words at the same real position. QED.

**No natural number source:** The expression for μ is built by multiplicative word concatenation; any ordinary integer enumeration is applied **afterwards**, to calibrate a target system.

If `Z(s)=∫e^{-st}dμ(t)` converges in a suitable half-plane, then

\[
 Z(s)=\prod_j(1-e^{-s\lambda_j})^{-1},\qquad
 -Z'(s)/Z(s)=\int e^{-st}\,dJ(t).
\]

For `λ_p=log p` this specializes to `ζ(s)` and the authentic `Λ(p^k)=log p`, with `Λ(6)=0`, on `Re(s)>1`. For generic Beurling systems the convergence abscissa may differ; there is **no zero-reading or critical-line substitution** here.

## 3. JET-02 — causal invertibility and primitive rediscovery

Let `ν=μ−δ_0`. The gap condition implies the formal convolution logarithm is locally finite:

\[
 \boxed{\log_*\mu=\sum_{r\ge1}\frac{(-1)^{r-1}}r\nu^{*r}=\Pi.}
\]

**Proof:** The formal series `log(exp X)=X` is legitimate in every bounded energy window because positive-degree multiplication strictly advances at least `u`. Equivalently truncate in increasing energy order and compare coefficients; no analytic continuation or infinite numerical approximation is involved. QED.

**Primitive extraction (CLASSICAL / elementary induction):** Given the full composite multiplicity measure μ, inspect positive atom positions in increasing order. Divide out all word contributions forced by previously recovered generators. At the least remaining unexplained atom `x`, the residual nonnegative integer mass equals the multiplicity of new primitive generator species at `x`. Continue. Uniqueness follows by the least-discrepancy induction. Repeated **source species** of the same numeric q are recovered with multiplicity, even when spectral injectivity is false. The finite script checks the claimed factorization against an independent direct-word enumerator; the algorithm does not prove that the supplied μ genuinely originated in such a source without verifying its residuals.

This inversion can reconstruct a declared prime **multiset from composite mass**, not its external authenticity. Injecting a new independent `V_6` into the ordinary generators is revealed as a new atom of the *convolution logarithm* at `log6`; it does not become an authentic rational prime just because a representation accepts the declaration.

## 4. JET-03 — reconstructed successor and measure-native braid

Assume the spectrum is infinite, locally finite, and collision-free. Enumerate its atoms

\[
 0=t_1<t_2<t_3<\cdots;\qquad m_n=h^{-1}(t_n),\quad r(m_n)=n.
\]

Define the *rank successor* `S(m_n)=m_(n+1)`. This alone yields a set with order type `N_{>0}`; **every** qualifying Beurling source does so, and it says nothing about its original multiplicative law.

For each generator `P_j=e_j`, set `d_j=r(P_j)` (a rank measurement, not an assumed arithmetic prime label). Define **uniform dilation counting (UDC)** purely in the composite source measure:

\[
 \boxed{\mu((h(V_jx),\,h(V_jSx)])=\mu([0,\lambda_j])=d_j
 \quad\text{for every }j\text{ and }x\in M.}\tag{UDC}
\]

Because all atoms have unit mass, UDC is **equivalent** to the affine braid

\[
 \boxed{V_jS=S^{d_j}V_j.}\tag{BRAID}
\]

**Proof of equivalence:** Its left side counts exactly `r(V_jSx)−r(V_jx)` atomic ranks. This equals `d_j` exactly when the two endpoints differ by `d_j` successor edges. QED. *UDC is a measure-native specification, not an independent proof of the braid.* No existing SUCC source law supplies UDC for a generic free prime-jet system.

## 5. JET-04 — rank/scale rigidity theorem (main conditional result)

**Theorem (PROVED PAPER, under global UDC or BRAID):** With the assumptions of §§1 and 4, if UDC holds for **every** generator and **every** successor edge, then

1. `r:M→N_{>0}` is an ordered multiplicative monoid isomorphism;
2. there exists one constant `c>0` such that `h(x)=c log r(x)`;
3. consequently `r(P_j)` ranges over **exactly** the ordinary rational primes (one for each primitive label).

**Proof (1):** Write `m_n=S^{n−1}1`. For a generator `P_j`, global braid and the base `V_j1=P_j=m_(d_j)` give

\[
 V_jm_n=V_jS^{n-1}1=S^{d_j(n-1)}P_j=m_{d_j n}.
\]

Thus `r(P_jm_n)=d_j n` for every n. Every word is a finite product of primitive generators, so iterating gives `r(xy)=r(x)r(y)`; surjectivity and injectivity hold by its definition as an enumerating rank. This is a multiplicative monoid isomorphism.

**Proof (2):** Let `f(n)=exp[h(r^{-1}(n))]`. Because `r` preserves multiplication, `f(mn)=f(m)f(n)`. The log spectrum is increasing, so `f` is strictly increasing and `f(1)=1`. For any `m,n>1`, integer exponents `a,b>0` compare `m^a` with `n^b`. Strict monotonicity and multiplicativity ensure that `a log m ≤ b log n` exactly when `a log f(m) ≤ b log f(n)`. Density of rational numbers forces

`log f(m)/log m = log f(n)/log n = c`.

Therefore `f(n)=n^c`, `c>0`, proving the stated log rigidity.

**Proof (3):** Isomorphisms of free commutative monoids preserve irreducibles. The irreducibles of positive integers under multiplication are exactly the usual primes. Since `M` is freely generated by its `P_j`, their ranks are exactly those primes. QED.

**Important logical boundary:** Global BRAID is an infinite source-wide axiom equivalent to multiplicativity of rank, **not something derived from unique prime jets**. A finite number of passing braids is not this theorem's premise.

## 6. JET-05 — one independently normalized Archimedean unit removes scale

On positive reals, the multiplicative Haar measure is `d×x=dx/x=dt`, where `t=log x`; the ordinary additive Haar measure is **different**: `dx=e^t dt`. The latter must be fixed by an independently justified real-place normalization, not tuned after seeing μ.

Let `I_1=[t_1,t_2)=[0,c log2)`. Require the single source-coupling calibration

\[
 \boxed{\int_{I_1} e^t dt=1.}\tag{UNIT}
\]

Then `2^c−1=1` and hence `c=1`. Combining BRAID with UNIT yields

\[
 h(m_n)=\log n,\quad \mu=\sum_{n\ge1}\delta_{\log n},\quad
 r(M)=(\mathbb N_{>0},\times).
\]

Finally define `x⊕y=r^{-1}(r(x)+r(y))`. This gives an ordered commutative semiring with zero adjoined when desired; `S(x)=x⊕r^{-1}(1)` and multiplication distributes over addition because `r` transports both operations. This constructs addition **after** the multiplicative carrier; it does not prove the physical/causal realization of additive SUCC.

A stronger **independent alternative** is the full cell matching law

\[
 \int_{t_n}^{t_{n+1}} e^t dt=\mu([t_n,t_{n+1}))=1,\quad\forall n.
\]

This directly forces `e^{t_n}=n` by induction even without BRAID, but imposes infinitely many Archimedean cell equations; it is not a consequence of the jets.

## 7. JET-06 — no-go independence / hostile source models

All exact finite measurements are recorded in `PRIME_JET_GENESIS_RECEIPT.json`. Infinite implications below are independently proved as simple constructions:

| Source family | Factor words collide? | BRAID? | UNIT? | Mathematical verdict |
|---|---:|---:|---:|---|
| True q_j=p_j | No | Yes | Yes | Positive calibration (uses known target as external validation) |
| `q_3=3/2`, all other q_p=p | **No** | **No** | No | Free prime jets and flat energy **do not imply BRAID** |
| `q_3=9/2`, all other q_p=p | **No** | **No** | **Yes** | UNIT alone **does not imply BRAID** |
| Every q_p=p² | No | **Yes** | **No** | BRAID alone leaves global power gauge `c=2` |
| Admit independent q_6=6 alongside p=2,3 | **Yes** | Rank undefined | No canonical rank | Duplicate source species; mass μ(6)=2 |
| Omit q_5 | No | Not the target | Depends | Missing unit positions despite valid Euler structure |
| Add a hidden q_101 beyond H=30 | Not visible | Unchanged on tested prefix | Unchanged | No finite horizon authenticates global completeness |
| Double all prime-jet weights | Generally not counting | Not a legal free-word model | N/A | Positivity of weights does not make canonical word counting |

**Proof of collision-free mutations:** If `q_3=3/2` (or `9/2`) while all other generators are genuine primes `p≠3`, the ordinary 3-adic exponent of a rational word equals the source exponent of `q_3` (or twice that exponent); all other generator exponents are then recoverable from the remaining rational prime valuations. Thus the spectral evaluation is injective **globally**, not merely up to the finite test. In both systems UDC fails by explicit finite rank witness.

**Proof of the scale family:** For every `c>0`, `q_p=p^c` gives image `{n^c:n≥1}`, rank `r(n^c)=n`, all affine braids intact, and first additive-real unit cell `2^c−1`. The unit calibration selects exactly c=1.

**Proof of finite-horizon impossibility:** Given any finite log/size cutoff H and any source, adjoining a new free generator at size q>H changes neither its finite restricted jets nor the composite measure in that horizon. If the new generator clashes with old factorizations at a later point, its error appears only later. Therefore a fixed finite source closure cannot infer absence of all later ghosts.

## 8. JET-07 — affine endpoint agreement has unbounded FUCC causal cost

Every pair of words `α,β` has a coordinatewise meet `γ_j=min(α_j,β_j)`. Legal backward and forward FUCC paths from `α` down to γ and up to β give shortest word-graph distance

\[
 d_F(\alpha,\beta)=\sum_j|\beta_j-\alpha_j|.
\]

**Proof:** Each legal ±generator changes one coordinate by exactly one, hence at least the ℓ¹ distance is necessary. The meet path is lawful and attains that bound. QED.

In the authenticated integer source this specializes to

\[
 \boxed{d_F(a,b)=\Omega(a/\gcd(a,b))+\Omega(b/\gcd(a,b)).}
\]

For adjacent integers `n,n+1`, `gcd(n,n+1)=1`, so `d_F(n,n+1)=Ω(n)+Ω(n+1)`. Take `n=2^k−1`; its successor has `Ω(2^k)=k`, so the FUCC edge cost is ≥k and **unbounded**. But the same successor has logarithmic displacement `log((n+1)/n)→0`. There is no uniform bounded-length FUCC compilation of all unit-SUCC edges, nor an isometric identification of their causal metrics.

Nevertheless their **flat endpoint energy** agrees:

\[
 \sum_j(\beta_j-\alpha_j)\lambda_j=\log(b/a),\qquad
 \sum_{m=a}^{b-1}\log(1+1/m)=\log(b/a).
\]

Their **additive length** requires the separately normalized real density:

\[
 b-a=\int_{\log a}^{\log b}e^t dt=a(e^{\Delta h}-1).
\]

The common endpoint is not an equality of path histories or dynamical operators; it is an **observable-level transport with nontrivial causal-cost distortion**.

## 9. JET-08 — independent classical adelic intersection route, with a warning

SUCC's existing `EDGE_CARRIER_RECONSTRUCTION_LAB.md`, `finite_adele_localization.py`, and the standard Tate/Pontryagin source supply a second route if the source is already the **rational field** plus all its genuine p-adic valuation rings:

\[
 \boxed{\{q\in\mathbb Q:q>0,\ q\in\mathbb Z_p\ \forall p<\infty\}=\mathbb N_{>0}.}
\]

**Classical proof:** Write `q=a/b` in lowest terms with positive `b`. If every `v_p(q)≥0`, no prime divides b, so b=1; positivity selects the positive integers. The reverse inclusion is immediate. This reconstructs N as the *globally integral, Archimedean-positive rational diagonal*. It does **not** follow merely from an abstract Beurling spectrum: the full field `Q`, its standard all-prime valuations, the diagonal embedding, and the real sign are powerful independently declared source structure. Nor is it an independent genesis of all arithmetic if constructing Q already assumed Z/N earlier.

**Finite access negative control:** Checking `v_p(q)≥0` only for `p≤97` cannot distinguish `1` from `1/101` as globally integral. The omitted 101-place is a concrete next discriminator. This dovetails with the source-indexed no-ghost discipline.

The two reconstruction routes have different inputs and do not constitute independent confirmations of a source-free origin of N. They do provide a precise future **comparison map:** prove whether a source-licensed adelic integral-rational diagonal induces UDC for its prime-jet spectrum, keeping genuine additive and multiplicative Haar distinct. Importing the ordinary rational diagonal already imports much of the target, so noncircularity must be audited arrow by arrow.

## 10. Execution contract, receipt, and trust boundary

Artifacts (new, additive; no preserved source files mutated):

- `observational_succ/prime_jet_genesis.py`: exact `JetSource`, symbolic Pi, exp_* word reconstruction, numeric pushforward collisions, inverse log_*, greedy primitive recovery, affine defects, unit cell and FUCC cost.
- `tests/test_prime_jet_genesis.py`: pure-stdlib independent directed tests, including genuinely collision-free source mutants and source budget fails.
- `scripts/prime_jet_genesis_probe.py --verify`: independent word oracle, convolution log inverse, rediscovery, 56 systematic generator-triple holdouts, deterministic receipt comparison.
- `research/2026-10-17/PRIME_JET_GENESIS_RECEIPT.json`: typed deterministic finite outputs. Written by explicit `--write-receipt`, verified without writing by `--verify`.
- `.github/workflows/prime-jet-genesis.yml`: dedicated focused Python 3.10 and 3.13 checks (if hosted workflow runs, their independent results must be inspected).

Reproduction:

```bash
python -m unittest discover -s tests -p 'test_prime_jet_genesis.py' -v
python scripts/prime_jet_genesis_probe.py --verify
```

**Scope note:** Exact runtime tests are not a Lean proof, an infinite algorithm, a physical source sensor, or an independent derivation of UDC. Local isolates run only these additive files; full repo provenance and full suite must run on an actual checkout/hosted runner.

## 11. Claim ledger (new-to-project labels, not priority claims)

| ID | Claim | Status | Dependency / next probe |
|---|---|---|---|
| PJG-01 | `μ=exp_*Pi` and jet Laplace/log identities in stated domain | **CLASSICAL / PROVED PAPER** | Beurling/Diamond–Zhang; positive-gap hypothesis |
| PJG-02 | `log_*μ=Pi` and primitive multiset recovery | **CLASSICAL / PROVED PAPER; FINITE EXACT TESTED** | Positive gap, finite source; mutate coefficient/fake source |
| PJG-03 | UDC iff global affine braid on unit-mass ordered source | **PROVED PAPER / conditional** | Rank and all-source quantifiers; distinct from derived law |
| PJG-04 | Global braid ⇒ multiplicative rank and uniform log scale | **PROVED PAPER / conditional** | Ordered free monoid; hostile arbitrary q and power gauges |
| PJG-05 | Single correctly normalized additive-Haar unit ⇒ `c=1` | **PROVED PAPER / conditional** | Arch source is independent; calibrated q_3=9/2 kills braid |
| PJG-06 | Conv/word/inverse/primitive tests | **TESTED EXACT FINITE** | Receipt + targeted tests; no infinite theorem from trials |
| PJG-07 | Generalized free word source alone determines N | **REFUTED** | Globally injection-preserving q_3=3/2 or 9/2 |
| PJG-08 | One unit calibration alone determines arithmetic | **REFUTED** | Globally collision-free q_3=9/2 |
| PJG-09 | Braid alone fixes physical log scale | **REFUTED** | q_p=p^c, any c>0 |
| PJG-10 | Prime-FUCC cost for one S edge uniformly bounded | **REFUTED** | n=2^k−1, costs ≥k |
| PJG-11 | Adelic rational local-integrality intersection identifies N | **CLASSICAL IMPORT / PROVED PAPER** | Uses full Q, all Z_p, real positivity; not source-free |
| PJG-12 | Jet/Tate/Haar/Poisson **derive** the infinite UDC source law | **UNVERIFIED** | Need independent source-derived all-state dilation-count certificate |
| PJG-13 | This reconstruction implies signed completed Weil positivity/RH | **UNVERIFIED / RH OPEN** | Real Gamma, both poles, correct half-density and full sign still needed |

## 12. The next verdict-changing mathematics

**Gate A: Source-native UDC.** Construct from independently supplied SUCC causal/path/categorical and real-place Haar laws a scalar **counting transfer operator** acting on μ. Prove or refute that its dilation interval counts are exactly `d_j`, without using any `r(xy)=r(x)r(y)` as a premise. If the derivation merely rewrites the braid, mark it circular.

**Gate B: A weakened rigidity problem.** Classify infinite locally finite Beurling systems for which affine defects vanish outside a sparse/finite family of cells or satisfy bounded discrepancy. Can they be forced into power-scaled integers under an independent asymptotic normalization? Supply explicit countermodels and keep asymptotic information distinct from exact identities.

**Gate C: All-place adelic alternative.** In the currently established source-indexed rational/CRT/Poisson construction, derive the globally integral positive diagonal and its cell projector. Check whether this supplies nontrivial UDC information without reconstructing the rational integers earlier in the chain. Use an omitted-prime denominator witness as the mandatory negative control.

**Gate D: Prove source preservation into Tate (not RH sign).** Once the genuinely normalized integer tape is obtained, send `J=Σ_p Σ_{k≥1} (log p)δ_{klog p}` and canonical multiplicative Haar shell weights into existing `StandardTateSource`. Check Γ, both polar residues, parity/conductor, and full signed test domains. **Never** identify a positive `σ>1` probability Gram with the original signed Suzuki/Weil form.

**Final verdict:** The route is mathematically lawful and exposes an exact **equivalence criterion** for natural-number arithmetic. Its distinctive unsolved component is source-derived global UDC, not computation of further prime jets. `RH PROVED: NO`.

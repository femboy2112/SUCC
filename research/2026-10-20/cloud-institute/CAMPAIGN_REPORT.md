# Operation SUCC cloud institute — completed research campaign

Date: 2026-10-20. Repository: [femboy2112/SUCC](https://github.com/femboy2112/SUCC).
This report distinguishes proved mathematical statements, executed checks, and remaining research obligations. Six researchers ran concurrently in isolated worktrees; the coordinator owned literature reconstruction and reconciliation. All reviewers used the same underlying model. Separate tasks and algorithms are disclosed as such, not misrepresented as independent human referees.

## 1. Principal mathematical gain

For positive primitive triples `a+b=c<=X`, define `ris(n)=n/rad(n)` and

\[
S_t(X)=\sum_{a+b=c\le X,\ (a,b)=1}\operatorname{ris}(abc)^t.
\]

Lane B supplies complete paper proofs, separately audited, that for every fixed real `0<=t<2/3`,

\[
S_t(X)\ll_t X^2,
\qquad
\lim_{X\to\infty}\frac{S_t(X)}{X^2}
=\frac1{2\zeta(2)}\prod_p\left(1+\frac{3p}{p+1}
\frac{p^t-1}{p^2(1-p^{t-1})}\right).
\]

This extends the project's previous diagonal range `t<1/2` and establishes an actual local-density-to-global-mean theorem. The proof retains primitive determinant separation, uses positive powerful-divisor coefficients, and supplies a quantitative uniform-integrability budget before taking infinite limits. It does not infer a weighted moment from BBLT's different exceptional-set theorem.

Status: **PROVED LOCAL** on the stated infinite mathematical domain; classical methods/new-to-project synthesis. Academic originality remains **UNVERIFIED**. The endpoint `t=2/3`, an optimized effective convergence rate, and formalization of this arithmetic theorem remain open. This campaign proves neither RH, integer abc, nor binary Goldbach.

## 2. Repository state, ancestry, and isolation

The baseline was reconstructed from live Git and GitHub, rather than assumed from the brief:

| Ref | Exact pinned head | Relationship |
|---|---|---|
| `main` | `0e56e0ae26f3d52a2ea34c0a4288478139fcb634` | Baseline for every cloud lane |
| [PR200](https://github.com/femboy2112/SUCC/pull/200), `research/proof-forge-mason-stothers-2026-10-20` | `e2f92a6b7e3835c3223abc294688ad9b85045811` | Draft targeting main |
| [PR201](https://github.com/femboy2112/SUCC/pull/201), `research/rigidity-forge-2026-10-20` | `cbc4010458c00be995b8af3f229c9bba410301e2` | Draft stacked on PR200 |

The final live-state receipt records the last refresh. No change to these three heads was observed during the campaign. No cloud branch depends on PR200/201. No main push, merge, force-push, archival rewrite, release, or edit to Claude's branches occurred. GitHub write permission was verified. Shell Git lacked push credentials, so the connected GitHub API published commit trees; every remote tree was checked for exact equality with its tested local tree. Commit metadata can therefore differ while content is identical. The manifest records both identities.

All branch names below have prefix `research/astra-cloud-` and suffix `-2026-10-20`.

| Lane / branch middle | Draft | Published content head | Parent and dependencies |
|---|---|---|---|
| A / `crt-ascent` | [207](https://github.com/femboy2112/SUCC/pull/207) | `7466f0d4bfca0ae00ff4d4b355bb14cba4bbb544` | Direct child of pinned main; standalone |
| B / `abc-correlations` | [208](https://github.com/femboy2112/SUCC/pull/208) | `1c6f2adfe3ebbd1dc6613e9adb4e95bdef2f3e29` | Direct child of pinned main; contains its own fixed-divisor proof |
| C / `goldbach-harmonic` | [204](https://github.com/femboy2112/SUCC/pull/204) | `d0fa95d49040b70439a0ef72cf2ed754ff88824d` | Direct child of pinned main; standalone |
| D / `operator-theory` | [205](https://github.com/femboy2112/SUCC/pull/205) | `fca107cde969b68566699d9da98944a363c89434` | Direct child of pinned main; imports existing source routines, explicitly identified |
| E / `formal-proofs` | [203](https://github.com/femboy2112/SUCC/pull/203) | `fd16f5766629e02cb92c0ca0607afad45799f2cc` | Parent `9e1283d5ecb532706b04175e857531511b25c242`; all four commits descend from pinned main |
| F / `hostile-holdouts` | [206](https://github.com/femboy2112/SUCC/pull/206) | `a86c37ef87526c339bebfd21d0232bcf2f5b45a4` | Direct child of pinned main; explicit optional audit target is PR201 |
| G / `institute-report` | [202](https://github.com/femboy2112/SUCC/pull/202) | This report commit; exact SHA is recorded in the PR description | Parent `e8bcb6e62e843eb93818d8d67c6bcdde61e2b109`, itself directly from pinned main |

The report cannot contain its own Git commit hash. PR202's final description identifies that hash and its tree without a recursive self-reference. Every scientific lane's exact final hash is recorded above and in `CAMPAIGN_MANIFEST.json`.

## 3. Completed results and boundaries by lane

### A. Quantitative CRT ascent

For every integer `W>=1`, real `X>=0`, and set `R` of residue pairs modulo `W`,

\[
\left|N_R(X)-\frac{|R|X^2}{2W^2}\right|
\le |R|\left(\frac{3X}{2W}+1\right).
\]

An exact floor sum proves this bound and the uniform sharpness of the leading coefficient `3/2`. A different unit-cell geometric argument proves the same error order with coefficient `2`; it is not presented as a second proof of the sharper constant. Relative nonprimitive error vanishes uniformly for `W=o(X)` regardless of residue sparsity.

For global coprimality, an exact Möbius identity yields a computable rational finite-center interval plus an explicit omitted-divisor budget. With `r=|R_prim|>0`, a primitive asymptotic follows under

\[
W\log X=o(X),\qquad W^2=o(X\sqrt r).
\]

These are sufficient, not optimal, growth conditions. Genuine prime-power occupation densities, the remaining infinite coprimality factor, and thin rectangle errors are proved. Fixed pairwise-coprime divisors `d,e,f` have primitive triangle density
`(2 zeta(2) def)^(-1) product_{p|def} p/(p+1)`.

Counterexamples refute arbitrary near-scale modulus uniformity and finite-prime primitivity as a substitute for gcd. At `X=4097`, the event `v_2(a)=12`, with the other two slots odd, has one actual point versus naive main term `16785409/32768>500`. Short-side resolution matters for unbalanced boxes.

Validation: 13 tests, 48 fresh probe cases, and a separate 96-case gcd census. The full paper proof was audited by C and the coordinator. **PROVED LOCAL; CLASSICAL** mechanisms. No Lean proof. Full statements: [A dossier](https://github.com/femboy2112/SUCC/blob/7466f0d4bfca0ae00ff4d4b355bb14cba4bbb544/research/2026-10-20/CLOUD_CRT_ASCENT.md).

### B. Correlation beyond the diagonal

The exact expansion `f_t=1*g_t` has `g_t(p)=0` and
`g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}` for `k>=2`. For `t>=0` its coefficients are nonnegative and supported on powerful integers. Compatibility of divisors of primitive `a,b,c` forces the three divisors to be pairwise coprime.

For `D=def`, distinct compatible primitive slopes satisfy
`|a/c-a'/c'|>=D/X^2`; hence their count is at most `1+X^2/D`. This is the information discarded by the diagonal majorant. In the sector `H=ris(abc)<=X`, powerful support gives `D<=H^2<=X^2`. In the other sector a separate radical-pair Rankin bound gives
`T_X(y)<=3 C_eta X^(2+2eta) y^(-2/3)`.

Set `eta=(2/3-t)/2`,
`A_p(t)=(p^t-1)/(p^2(1-p^(t-1)))`,
`E_3(t)=product_p(1+3A_p(t))`, and
`C_eta=product_p(1+2/[p(p^eta-1)])`. Both products converge in the stated range, and

\[
S_t(X)\le\left(2E_3(t)+\frac{2C_\eta}{2/3-t}\right)X^2.
\]

For `t<s<2/3`, truncating each divisor expansion at `L` leaves normalized mass at most `K_s L^(-(s-t)/2)`, uniformly for all `X>=2`. Fixed-divisor CRT limits followed by this uniform tail prove the mean value in section 1. Formal convergence of its Euler product for `t<1` does not extend the proved theorem beyond `2/3`.

Counterexamples: `(441,400,841)` invalidates removing the density-count cutoff even within powerful primitive triples. Without primitivity, `a=b=n,c=2n` gives `ris(2n^3)>=n^2`, so the corresponding moment exceeds order `X^2` for `t>1/2`.

Validation: 15 new tests, 41 adjacent existing tests, 19,812 independent referee counting cases, and separate paper audits of both the bound and the limit. **PROVED LOCAL**, not formally verified. BBLT v2's actual parameter ranges were checked; no priority claim or direct exceptional-set-to-moment implication is asserted. [B dossier](https://github.com/femboy2112/SUCC/blob/1c6f2adfe3ebbd1dc6613e9adb4e95bdef2f3e29/research/2026-10-20/CLOUD_ABC_CORRELATIONS.md).

### C. Arithmetic-harmonic transport

Finite character orthogonality, primitive residue counts, and CRT give exact Ramanujan divisor and multiplicativity identities. For each fixed nonzero integer `N`, absolute convergence is proved before factoring

\[
\sum_{q\ge1}\frac{\mu(q)^2c_q(N)}{\varphi(q)^2}
=\prod_p\left(1+\frac{c_p(N)}{(p-1)^2}\right).
\]

The `N=0` absolute-convergence extension is refuted. Odd `N` gives zero through the factor at 2; even `N` gives `2C_2 product_{p|N,p>2}(p-1)/(p-2)`. In particular `2C_2` is the value at powers of 2, not at `2p` for odd `p`.

For integer prime cutoff `P>=2`, let `F_P` be the finite product and `R` the residual of `|N|` after removing all powers of each prime `p<=P`. With `k=floor(log_(P+1) R)` computed by integer comparisons and `E_P=1/(4 ceil(P/2)-2)`,

\[
F_P(1-E_P)\le\mathfrak S(N)\le F_P(P/(P-1))^k.
\]

This avoids factoring the residual or requiring that all prime divisors of `N` lie below `P`. A distinct modulus-cutoff theorem gives absolute tail at most `12 D(N)/Q`, where `D(N)=product_{p|N}(1+p/(p-1))`. Moving-`N` ranges are separately stated; prime and modulus cutoffs are never conflated.

Validation: 13 tests, exact cyclotomic reductions through `q=40`, direct primitive-pair counts through `q=80`, hostile cutoff/normalization cases, and referee/coordinator proof audits. **PROVED LOCAL; CLASSICAL/new-to-project transport.** No analytic prime-pair asymptotic or Goldbach proof. [C dossier](https://github.com/femboy2112/SUCC/blob/d0fa95d49040b70439a0ef72cf2ed754ff88824d/research/2026-10-20/CLOUD_RAMANUJAN_TRANSPORT.md).

### D. Operator transport and actual signed source

The paper theorem specifies exactly when a `K=V*V`-relative lower bound transfers to a coercive closed form on the primitive completion: descent through the kernel, density in the completed range, closability in the primitive norm, and a form core for identification with the intended source extension. Compactness in derivative coordinates is not used to deny primitive coercivity.

A concrete counterexample shows why closability cannot be dropped. On `ell^2`, take `V=diag(1/n)`, `h=(1/n)`, and `q(u)=||Vu||^2+|<u,h>|^2`. The derivative form is bounded and closed, but its primitive transport contains `|sum F_n|^2` and is not closable. Vectors with first `m` entries `1/m` are the decisive sequence. Separate kernel and non-core examples expose the other missing assumptions.

For the actual source enclosure, imposing polynomial constraints on the inverse response subtracts
`B^-1 L(L* B^-1 L)^-1 L* B^-1`. An independently proved conservative version pays exact polynomial-moment and shift errors. A fresh `J=8,M=80` source replay preserves Gamma, completed poles, contact, half-density and genuine prime-power weights, with no zero locations as inputs. The paid improvements are positive definite in both parity blocks:

\[
10^{-18}\begin{pmatrix}3463996955140&-167747527079\\-167747527079&64529071408\end{pmatrix},\quad
10^{-18}\begin{pmatrix}21236511115671&14290598047569\\14290598047569&9616958211169\end{pmatrix}.
\]

The resulting lower enclosure still does not prove positivity; its negative lower eigenvalues do not prove negativity of the true source. The verdict remains **AMBIGUOUS**, RH **OPEN**. Existing Gamma/source/error routines are shared dependencies, not an independent reimplementation. A source-history attribution error was also identified: `source_weil_hierarchy.py` came into SUCC at `b0cef75f47de29b1326b351df35b9e5423f2ed4f`, and is not one of the 72 imported-manifest entries.

Validation: 9 tests, fresh source replay, exact positivity checks for the savings, source hashes, and referee audit. The transport theorem is **PROVED LOCAL** under its full hypotheses; application to source positivity remains conditional on the missing signed inequality. [D dossier](https://github.com/femboy2112/SUCC/blob/fca107cde969b68566699d9da98944a363c89434/research/2026-10-20/CLOUD_OPERATOR_SOURCE_FORENSICS.md).

### E. Formal Schur benchmark and rational certificates

Lean 4.14.0 with mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` actually checked the finite real Schur equivalence and four finite negative-direction/extraction lemmas. [Hosted run 39479505726](https://github.com/femboy2112/SUCC/actions/runs/39479505726), job `118824073301`, succeeded on merge checkout `076ae599348fbe30b7a5de813c633bc93bc1fafb`, combining pinned main with cloud head `c4092a702c9161d8d7815132c323c4991da01b6c`.

Every exported theorem has exactly `{propext, Classical.choice, Quot.sound}` in its printed axiom set. No `sorryAx` occurs in the valid build. Both false mutations failed as expected. Later changes only add/normalize receipt documentation; the checked Lean source remains SHA256 `537c440caab2ab889e14821acb114ae8e8c752af8a2dadedc406dd29f0bd70a1`. The first build exposed a missing real-star-order instance and was repaired before any verified claim. Local execution encountered a `/proc` restriction; it was not bypassed, and the hosted kernel supplied the actual verdict.

The final published head `fd16f576...` subsequently passed the kernel again in [run 39480589258](https://github.com/femboy2112/SUCC/actions/runs/39480589258), job `118827791355`, on merge checkout `bf925d0d1337334e915b7ba5918c87163bdc20c8`. The coordinator retrieved that job's logs: all five valid axiom audits and both rejected mutations were reproduced.

Separately, a complete paper proof and rational algorithm return either a negative rational vector or an exact positive weighted Gram decomposition for every finite rational symmetric matrix. Zero pivots, positive Schur pivots, and negative diagonals are handled exhaustively. A separate checker recomputes exact identities; no callback or caller-supplied theorem name is proof authority.

Validation: 9 tests, including 854 exhaustive and 120 seeded matrices, PSD controls and extreme precision; referee holdouts at dimensions 3,5,8 and epsilon down to `10^-400`. Full elimination correctness, the rational-to-real bridge, and Python-to-Lean refinement remain paper-proved/tested, **not fully formalized**. Classical finite linear algebra, not infinite positivity. [E dossier](https://github.com/femboy2112/SUCC/blob/fd16f5766629e02cb92c0ca0607afad45799f2cc/research/2026-10-20/CLOUD_FORMAL_SCHUR.md).

### F. Hostile holdouts against the actual stacked head

All nine findings target exact PR201 head `cbc4010...`; the complete dossier supplies reproduction, actual/expected outcome, mathematical explanation, affected status, repair and regression fixture for each. Existing tests and CI did not exclude these cases.

| Finding | Decisive failure | Required boundary or repair |
|---|---|---|
| F01 | Contract requests source authenticity while supplied source witness says false; result still reports authentic | Authenticate the witness independently and bind it to the claim |
| F02 | Post-construction status mutation promotes an unproved contract | Immutable or revalidated proof state |
| F03 | A supposedly uniform constant depends on the quantified size variable | Check dependency graph and quantifier scope |
| F04 | Nonexistent theorem/kernel names support a false statement | Trusted kernel receipt, not descriptive metadata |
| F05 | `nI-(1+epsilon)J`, `n=3`, `epsilon=10^-14`: negative all-ones vector exists, target extractor raises | Complete exact elimination; compare against lane E |
| F06 | `singular_series_enclosure(2,5/2)` accepts a fractional cutoff and returns upper bound 1; a valid rational lower bound is `135/128` | Enforce the integer-cutoff domain before computing |
| F07 | `bblt_anatomy(256,4)` leaves `n0=256` despite a purported bounded remainder | Match the actual anatomical regrouping theorem |
| F08 | `2C_2=S(2p)` normalization wording fails; at `p=5` ratio is `4/3` | Correct the statement to powers of 2 / full local factors |
| F09 | For `H=10^30`, matrix `[[H+2,1],[1,H+2]]` returns exact minimum `H+3` instead of `H+1` due to float ordering | Order algebraic eigenvalues exactly or certify rational intervals |

F05 is an incompleteness witness, not a demonstrated false PSD verdict. F06 refutes an admitted malformed input, not the integer-domain theorem. F08 refutes the quoted normalization, not the existing constant enclosure. These distinctions prevent the hostile audit itself from overclaiming.

Validation: 4 new tests and 31 adjacent target tests passed; the latter passing despite the findings is recorded. The audit also reviewed B–E with explicit limits on reviewer independence. No Claude module was repaired in this branch. [F dossier](https://github.com/femboy2112/SUCC/blob/a86c37ef87526c339bebfd21d0232bcf2f5b45a4/research/2026-10-20/CLOUD_HOSTILE_AUDIT.md).

### G. Primary sources and research obligations

[SOURCE_MAP.md](SOURCE_MAP.md) reconstructs exact statements and versions from BBLT v2, Ramanujan's 1918 paper, Douglas's 1966 theorem, Suzuki v3, the pinned mathlib polynomial abc bridge, and Vaughan's own large-sieve notes. It records assumptions, ranges, mechanisms and concrete SUCC obligations. The original 1973 large-sieve PDF could not be retrieved; that limitation is stated rather than paper access invented.

Complete calibration arguments cover exact-grid Fourier sampling, the failure of dense-range substitution in Douglas factorization, and the characteristic-`p` derivative alternative in polynomial abc. D supplies the closed-form/core reconstruction and A the elementary lattice mechanism. These are recovered classical results and new-to-project connections. Literature reconstruction supplies no general arithmetic cancellation theorem and no publication-priority certificate.

## 4. What has actually been independently verified

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Floor-sum versus geometric unit-cell counting | Two distinct universal routes to A's error order | Two independent derivations of the sharp `3/2` constant |
| Primitive slope packing plus separately counted gcd/CRT holdouts | A complete B proof with falsification attempts on 19,812 finite cases | An external referee or formal arithmetic proof |
| Direct residue counts versus cyclotomic character reduction | Exact finite C identities through independent implementations | Universal convergence without the written tail proof |
| Actual source replay plus exact paid correction matrices | A rigorously accounted tightening conditional on declared source routines | Independent source authentication of every inherited routine; RH positivity |
| Rational checker plus Lean kernel | Exact rational certificates; five actual finite formal theorems | Formal refinement of the whole Python algorithm |
| Combined aggregate run | All 63 new tests coexist and required probes pass | Proof of any infinite theorem or resolution of F's target defects |

`AGGREGATE_RECEIPT.json` preserves commands, hashes and results. The aggregate was detached and unpublished, with all 36 A–F additions placed on pinned main. No existing file was overwritten. There were zero inter-lane path collisions and zero changed-path overlaps with either PR200 or PR201. Provenance verified 72 entries; observer foundations and ordinal probes exited successfully. A log-only whitespace issue was found, corrected with the transformation disclosed, and rechecked. Code and checked formal sources were unchanged by that cleanup.

The full baseline suite passed **6,135 tests on both Python 3.13 and 3.10**, in 734.607 and 949.657 seconds respectively, on the source-map-only coordinator head `e8bcb6e...`. [Workflow 39478977020](https://github.com/femboy2112/SUCC/actions/runs/39478977020) completed successfully, including the subsequent required source/probe steps; jobs `118822254779` and `118822254899` supply the logs. That head changes no executable or test file from pinned main.

The completed hosted Python 3.13 job `118822967192` in [run 39479185292](https://github.com/femboy2112/SUCC/actions/runs/39479185292) additionally passed **6,148 tests in 733.813 seconds**: the full pinned-main suite plus C's 13 new tests. Its subsequent source/probe steps also passed. This is broad regression evidence on PR204, not a claim that the full combined 6,198-test A–F suite completed. The separate combined 63-test run did complete.

The broad baseline/CI status is recorded in `VALIDATION_STATUS.json`; completed, pending and interrupted runs are distinguished. A local uncapped baseline run was interrupted after 3,187 success markers because it made the runtime unresponsive. A capped aggregate rerun was stopped after the completed hosted regression evidence became available; no full local-suite pass is claimed. A passing job is not conflated with completion of every job in its workflow. Dependency-incomplete preliminary attempts are not counted as successful validation.

## 5. Merge readiness and integration order

All seven PRs remain drafts. Each scientific PR is independently based on main; the following order is for review convenience, not an undeclared stack:

1. **F then E:** use the hostile cases to review Claude's repairs; compare complete rational witnesses with the independent benchmark. Verify proof-authority changes against genuine receipts. Do not treat adding F's tests as repairing the target interfaces.
2. **A then B:** integrate quantitative residue infrastructure and the arithmetic mean-value theorem. B already contains a standalone density proof, so neither commit imports the other branch.
3. **C:** integrate harmonic arithmetic and carefully adapt Claude's major-arc interface to the explicit fixed/moving cutoff contracts.
4. **D:** integrate the source dossier and optional inverse-response improvement after reviewing shared source-error assumptions. Preserve the ambiguous positivity verdict.
5. **G / coordinator:** reconcile central claim indexes once the maintainer selects final branches. This campaign deliberately leaves common registries and README unchanged to avoid cross-lane conflicts.

| Draft | Changed files | Validation / status | Claude compatibility and review requirement |
|---|---|---|---|
| 207 / A | Module, test, probe, dossier, JSON receipt (5) | 13 focused + aggregate; PROVED LOCAL | No path overlap; methodological holdout for Claude's elementary count |
| 208 / B | Module, test, probe, dossier, JSON receipt (5) | 15 focused, 41 adjacent, referee census + aggregate; PROVED LOCAL | No path overlap; new determinant/tail argument and mean-value theorem |
| 204 / C | Module, test, probe, dossier, JSON receipt (5) | 13 focused + aggregate; PROVED LOCAL | No path overlap; complements major arcs, does not assume them |
| 205 / D | Module, test, source probe, dossier, source receipt (5) | 9 focused + source replay + aggregate; source sign AMBIGUOUS | No path overlap; shared inherited source dependencies must remain explicit |
| 203 / E | Workflow; six formal-support files; module/test; dossier, receipt, normalized kernel log (12) | 9 focused + actual Lean + aggregate; finite formal scope only | No path overlap; independent algorithm/checker, not a patch to Claude's implementation |
| 206 / F | Runner, test, dossier, receipt (4) | 4 focused, 31 adjacent target tests + aggregate; exact counterexamples | No path overlap; targets pinned stacked heads and must be rerun after repairs |
| 202 / G | Source map, report, manifest, aggregate receipt and validation snapshot | Source comparison, tree/ancestry/path checks | Coordinator documentation only; no mathematical status promotion via metadata |

Exact filenames, parents, local/remote trees and SHA256 values are in the machine-readable manifest and per-lane receipts. Broad CI completion and maintainer review remain integration gates wherever the snapshot reports pending work. No merge authorization is inferred from this report.

## 6. Smallest next verdict-changing probes

| Direction | Next decisive obligation | Gap type / falsifier |
|---|---|---|
| A sparse primitive transfer | Improve the omitted-divisor discrepancy with explicit dependence on sparse residue geometry, beyond `W^2=o(X sqrt r)` | Pathway gap; test near-scale empty/deep-power families before any stronger uniform claim |
| B endpoint | Prove a summable improvement to the radical-tail bound at exponent `2/3`, or produce a primitive family whose endpoint moment diverges after `X^2` normalization | Mathematical boundary of this method; Euler-product convergence alone is insufficient |
| B quantitative mean | Combine finite-divisor errors with the already proved `L^(-(s-t)/2)` tail and optimize `L(X)` | Probe gap with ingredients now available; constants and modulus growth must be explicit |
| C Goldbach connection | Obtain a source-faithful analytic error smaller than the positive singular-series main term in the claimed range | Pathway gap outside this arithmetic bridge; finite local products cannot supply it |
| D signed positivity | Use the exact two-moment Gram inverse and a separately varied Gamma depth in the same signed-source enclosure | Quantitative probe gap; a tighter still-negative lower bound remains inconclusive |
| E full formal authority | Formalize termination and invariant preservation of the rational eliminator, then bind certificate data to kernel-checked results | Refinement gap; metadata names or callbacks cannot close it |
| F repairs | Rerun all nine exact holdouts against each new actual Claude head, retaining expected status distinctions | Verification gap; success on old tests is already known insufficient |
| G novelty | External expert/prior-art review of the primitive weighted mean theorem and its relationship to existing moment estimates | Academic-access/review gap; project usefulness does not establish priority |

The campaign's strongest completed transport is B's finite-divisor density plus uniform integrability to a global Euler-product mean. A supplies explicit moving-modulus budgets, C supplies an absolutely convergent arithmetic-harmonic bridge, and E supplies actual formal finite authority. D and F expose precisely where those capabilities still cannot certify the original infinite signed source.

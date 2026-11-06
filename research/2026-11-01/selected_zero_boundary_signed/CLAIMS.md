# Claim ledger — selected zero-boundary signed-lag attack

Research-status; no canonical SUCC claim is promoted and this mints no registry namespace
(prefix `SZB` stays local, like prior π-frontier rounds). Labels: **PROVED LOCAL** (exact
identity/derivation + exact or certified finite check), **REFUTED** (explicit counterexample /
numerical certificate within stated scope), **NEGATIVE / REPRESENTATION IDENTITY** (true but
seed/source-blind, so not a normality mechanism), **OBSTRUCTION**, **OPEN/UNVERIFIED**.

| ID | Exact scoped proposition | Status | Receipt / boundary |
|---|---|---|---|
| SZB-01 | Zero-seed corrected lag phase `= [(T_n−T_{n+k})−R_d(n,k)] + (x_{n+k}−x_n)`, `x_m={16^{m−1}π}`; so at `K_N=⌊(d+1)log_16 N⌋` the zero-seed score = counterseed corrected score + Fejér-lag π-digit autocorrelation | PROVED LOCAL (exact identity) | `probe.py`; `limsup L^[d](N,K_N;0)≤0 ∀h` would prove base-16 normality — it IS the gate, not a route |
| SZB-02 | Candidate one-sided lemma "`L^[d](N,K_N;0)≥0` and per-lag `Re D^[d]_{h,k}/(N−k)≥0`" | **REFUTED** | 16/16 configs (`d∈{2,3}`, `h∈{1,3,5,7}`, `N∈{16384,65536}`) have negative per-lag corr; aggregate sign-oscillates. No positivity shortcut |
| SZB-03 | The AC-13 angular-period identity (`∫P/(16−t^8)=π/16`) determines a normality criterion | **NEGATIVE / REPRESENTATION IDENTITY** | identity is seed-blind (source-only); holds identically for the zero seed and the nonnormal `q=1/5` orbit (`|S_N|/N=1.0000`); fixes only `π/16` |
| SZB-04 | Within-cell signed control at affordable resolution gives a new seed-specific bound | **OBSTRUCTION** | `S_N(h·16^k)` = gate at harmonic `h·16^k` (digit-shift invariant; `|·|/N` independent of `k`); ceiling `D_{N,k}≥log(M/N)` forces `M≤N` |
| SZB-05 | Any sufficient route must use the exact `U_0=0` boundary + diagonal rationality (seed-specific), since seed-uniform transport / angular period / entropy routes are each seed-blind or gate-equivalent | PROVED LOCAL (meta, by SZB-02..04 + Main XIX LCS/CRE) | the one discriminator the current stack lacks |
| SZB-06 | Base-16 π normality; the signed Weyl gate `∀h≠0: S_N(h)=o(N)`; RH | **OPEN / UNVERIFIED** | no new signed estimate supplied this round |

**Next verdict-changing probe.** A signed statistic that is provably sensitive to the completed
point (π-digits vs `1/5` vs `0`) — e.g. a source-selected lag estimate conditioned on the exact
zero boundary and the diagonal rationality of `{U_n(0)}` — tested to FAIL on `q=1/5`, the counterseed
`−π/16`, the dyadic near-zero family, and the prime-smooth `q=3^a5^b` family. A re-expression of the
Weyl criterion as a period, a reparametrized angle, an entropy equivalence, or a seed-uniform
transport bound does NOT qualify.

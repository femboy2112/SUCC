# Next decisive SUCC cross-place theorem — make source replication yield *signed* real cancellation

**Gate:** prove a nontrivial original-source bound on the exact 2-adic return-fiber real correlation energy, not merely on a 2-adic residue projection.

With Q=2^k, N=QM, x_n={U_n}, and nonzero h, define

`R_(Q,M)(h)=Q^-1 Σ_(a=0)^(Q-1) | M^-1 Σ_(t=0)^(M-1) exp(2πih U_(a+tQ)) |²`.

The finite identity `|W_N(h)|²<=R_(Q,M)(h)` is proved. Quantified asymptotic saving of R for the exact original source at epoch sizes with N_(j+1)/N_j→1 would force the real Weyl gate, hence π normality. **No such signed inequality was proved this round.** There is no lower bound `R>=1/M`; off-diagonal correlations may be negative. A finite reduction to already known W is NOT progress.

## Candidate source mechanisms / required discriminators

- **Real carry-cocycle:** Original `C_n mod2^K` depends only on most recent ceil(K/4) carry increments, but the full real phase at time n needs original odd denominator `d_n` and K>=log₂d_n. Try a sharp *conditional signed* inequality for the correlation between `V(n) mod2^K`, the true carries and denominators, not a Haar assumption about independent components. Test against the rational shadow `H(n)=n/(2n−1)^4`, which has source-isometric 2-adic Haar and real nonnormality.
- **Self-cloning future-source:** The original exact congruence `S_(2^k)(n) ≡ U_n+2^k mod2^(k+1)` replicates the state. Estimate the REAL phases of `(16^(2^k)−1)U_n+S_(2^k)(n)`, taking the *integer carry quotient* into account, on long return fibers; prove cancellation without assuming Haar or a periodic-source model.
- **Factor/entropy barrier:** A stationary deterministic 2-adic-clock-only factor has zero entropy and cannot produce real Haar. Any proposed productive bridge must introduce source-conditioned carry/digit-history entropy or use a fundamentally different nonstationary observable with explicit error budget. Replacing a phase with the normalized residue `(V(n) mod2^K)/2^K` does not work: fresh floating mismatches exceed 1.
- **Source uniqueness:** Dual-boundary and 2-adic Haar properties are shared by explicit rational coboundary mutants. Carry-cocycle identities should be tested under gauge mutants `r+2H(n)−32H(n−1)` to detect source-blind algebra.

## Falsifiable outcomes

PASS only if a bound is valid for ALL large epochs (or an explicitly dense subsequence), has actual signed saving for selected original h, is independently checked, rejects coherent periodic real completions and rational shadows, and does not silently replace unwrapped U by fractional x in Z₂. FAIL if it is merely a 2-adic Haar restatement, its numerics require already assuming π digits normal, or a seed/source countermodel reproduces it. AMBIGUOUS if only finite values pass; preserve raw outputs and do not promote claims.

Before merging PRs: native provenance, >12k full test suite, observer/ordinal probes, formal source check and hosted exact-head CI still required. Parent PR stack #527→#526→#525 remains draft; no merges/releases here.

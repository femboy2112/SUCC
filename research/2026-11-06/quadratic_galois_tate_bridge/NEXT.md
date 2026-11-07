# Next research round — the signed Artin/Weil bridge, not another parity coincidence

**Starting point:** [RESEARCH.md](RESEARCH.md), QR-01 through QR-09, on research branch `research/quadratic-pisot-galois-tate-reflection-2026-11-06`; pinned base `main@d32342d`. **RH OPEN. pi normality OPEN.**

## A. Exact arithmetic gate

Derive from `O_K=Z[(1+sqrt5)/2]`, with no fitted zeros, the source-labelled finite-place table for p=2,3,5,7,11,13 and one 1 mod 5 / 4 mod 5 / 2 mod 5 / 3 mod 5 holdout per class. Preserve p=2 maximal order and p=5 ramification. Test the actual polynomial quotient and Frobenius before passing to local Euler factors. Negative controls: use `Z[sqrt5]` at 2, fake `chi`, and replace `chi5(p)` with the wrong unit norm `N(phi^p)`.

**Pass:** independently matched exact finite Euler-factor coefficients with a proof for all unramified p. **Fail:** any wrong-ring mutant passes unnoticed. **Ambiguous:** finite-only examples without the root-splitting theorem.

## B. Exact analytic distribution gate

Using authentic `zeta_K=zeta*L(s,chi5)`, derive at the level of meromorphic log derivatives and then completed explicit-formula distributions the identity:
\[
(\Lambda_K)'/\Lambda_K
=(\Lambda_{\mathbb Q})'/\Lambda_{\mathbb Q}
 +(\Lambda_{\chi_5})'/\Lambda_{\chi_5},
\]
on a common open zero/pole-free domain, with the canonical distributional continuation, test spaces and all pole, Gamma, conductor, trivial-zero and prime-power terms included. Only then consider the corresponding additive **signed Weil** functionals on a declared common test domain.

**Pass:** a point-by-point gamma/prime/pole ledger and a proven common-domain equality, not just product of scalars. **Fail:** any missing half-density/conductor, wrong p=5 term, or Galois-odd test projected to zero and then treated as preserved. **Ambiguous:** formal coefficient matching without continuity/test-domain proof.

## C. The candidate RH-hard gate, with a falsifier

If a signed Weil decomposition `W_K = W_Q + W_chi5` is established on a common test space in its correct sign convention, the desired statement `W_Q>=0` becomes the **relative domination** `W_K>=W_chi5`. This is RH-hard and NOT inferred from separate positivity of the two terms. Even two nonnegative forms can have an indefinite difference.

**Pass:** a source-derived all-test inequality with explicit proof and hostile test-function coverage. **Fail:** an exact test vector with negative relative difference under a purported universal theorem, or a mismatch of test spaces. **Ambiguous:** finite Gram positivity or sampled low-band sign.

Compare the true original completed Weil source to the strict off-line-zero symmetric Fourier-positive control `G(s)=2+cosh(4(s-1/2))`. A method using only parity/reflection/positive Fourier data must fail on this control.

## D. Preserve norm parity without cheating

For the full unit group, independently derive
\[
\lambda_{z,d}\circ\sigma
=\lambda_{-z+i\pi d/\log\varphi,d}.
\]
Test `d=0` and `d=1`, both unit signs, both parities and negative n. Then ask whether a *legal* global Hecke character or marked Tate test can retain the sign, rather than adding a symbol to an untwisted integral. An idele-class character must descend through `K^\times`; a proposed unit-only twist that is not trivial on diagonal units cannot be passed off as a Hecke character.

**Pass:** exact descent and completed conductor/eigenphase. **Fail:** a twist that fails the idele quotient or loses the odd sector when globally averaged. **Ambiguous:** a local character with no global gluing proof.

## E. SUCC integration and validation

- Link this dossier into the existing Pisot-source, Pascal harmonic, prime-Frobenius, Tate-Suzuki, and source-observer ledgers without mutating historical results.
- Check the original half-density, source sign, pole and all-prime coefficients; no nontrivial zeta zero may be a construction input.
- Treat the golden `Q(sqrt5)` and silver `Q(sqrt2)` settings as distinct test carriers; only a proved original-source map selects one.
- Re-run `python scripts/verify_provenance.py`, `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py` and exact-head CI; separately run targeted QR tests. Check Lean only if formal files actually change. Never invent a run.
- Keep the result draft until review. Do not merge, tag, release or promote claims automatically.

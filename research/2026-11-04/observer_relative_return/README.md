# Observer-relative BBP return / two-clock boundary flux

**Research-only additive child of [draft PR #504](https://github.com/femboy2112/SUCC/pull/504) pinned at \`f3327bdce023fe3f68d4c5431b5a7c2b53dac2ed\`.** The original four signed BBP poles, literal zero initial condition, complete integer lifts, source/provenance contracts, historical Lean, production and main are unchanged. Other fronts #503/#505 read-only.

**Main new paper result:** a delayed observer compares \(Z_{n+\ell}\) and \(Z_n\). The exact source recurrence proves that the amplified outstanding radial balance and subsequent negative injections cancel their \(1/n\) leading terms, leaving \(\Delta_\ell Z_n=-\ell/(32n^2)+O_\ell(n^{-3})\). The delayed radial Fourier response at \(H\asymp A^2\log A\) is a classical nonstationary-phase integral with an **exact leading sharp-window endpoint term**:
\[
\frac1A\sum_{n=A}^{2A-1}e\big(H(Z_{n+\ell}-Z_n)\big)
=\frac8{\pi i\ell q}\left(8e(-\ell q/128)-e(-\ell q/32)\right)
+O_\ell(q^{-2}+q/A),\quad q=H/A^2.
\]
The endpoint magnitudes 8 and 1 cannot cancel, hence the sharp response is \(\Theta_\ell(1/\log A)\) on the actual SUCC critical schedule. With a fixed smooth compactly supported observer window, all boundary terms vanish and the corresponding response has arbitrarily high inverse-logarithmic savings. **The difference belongs to the observation window, not the source distribution.**

**Other proved constraints:** exact flat two-clock U(1) transport; \(Y_n+Z_{n+\ell}\) and original \(U_n\) have *equivalent* fixed-h Weyl behavior by a summable perturbation; neither property bounds the original source-selected *coupled* high-frequency maximal-subinterval Weyl sum. Wrong-seed, observer-twirl and artificial anti-correlated-source controls block the false implication.

Read [TWO_CLOCK_THEOREMS.md](TWO_CLOCK_THEOREMS.md), [CLAIM_LEDGER.md](CLAIM_LEDGER.md), [SOURCE_MAP.md](SOURCE_MAP.md), [PREREGISTRATION.md](PREREGISTRATION.md), and [NEXT.md](NEXT.md). Source-level tests are in [tests/test_observer_relative_return.py](../../../tests/test_observer_relative_return.py). A standalone local replay of the nine mathematically equivalent test methods passed 9/9; exact-source identities and finite diagnostics are distinguished from universal paper claims. No native whole-repository test suite, new Lean kernel proof, global mathematical novelty, or hosted CI completion is claimed.

**BASE-16 NORMALITY OF π: OPEN. Original signed maximal-subinterval critical ratchet: OPEN. Original signed Weyl: OPEN.** This round locates a quantitative observer-boundary obstruction rather than proving the target.

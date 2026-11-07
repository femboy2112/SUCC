# Next decisive probes: from phase-locking to source-selective mathematics

**Research-only.** This is the forward route from THEOREMS.md, not a claim to have proved pi normality or RH. Parent: main@d32342d375f44ddf62221ad6aff2f534abdc0a03. Companion draft PRs #470, #471, #534 and #537 are *not* automatically part of main or of this branch.

## Claim boundary and steelman–crucible verdict

**Steelman:** Conjugate Pisot sheets can hide an exponentially small present-time discrepancy while harmonic accumulation preserves a finite source-specific residue; a measured threshold converts that residue into a future action boundary.

**Survives, exactly:** HPB-01...HPB-05 prove a model-level finite boundary with an iff weighted-square-distance criterion, a Galois-conjugate Pisot instantiation, an Abel finite-part identity and perturbation stability.

**Fails, with explicit receipt:** Equating Pisot lock-in to pi normality. HPB-04 proves any such finite boundary forces the first circle Weyl average to 1, whereas equidistribution requires 0. This is a *negative-control theorem*, not a missing positive step.

**Unverified:** An authentic BBP source-specific nonlinear phase transport, or an actual observer/actuator with the model's prescribed harmonic gains and hard threshold.

## P0. Reproduction and audit

Targeted root-discoverable test (stdlib only):

    python -m unittest discover -s tests -p 'test_harmonic_pisot_boundary.py' -v

These finite tests verify two distinct ways of computing phases, signed threshold crossing, exact rational BBP source coefficient balance, an Abel identity, and hostile mutants. The mathematical convergence proofs are in THEOREMS.md, not inferred from tests.

Required whole-repo validation before review/merge consideration (not claimed as run here):

    python scripts/verify_provenance.py
    python -m unittest discover -s tests -p 'test_*.py'
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py

Check exact-head Actions, provenance and claim ledger policies from AGENTS.md. No Lean claim unless a genuine Lean file has been checked (none edited here).

## P1. Verify the Gamma source-map obstruction, not a guessed gamma coefficient

Derive exactly from the four original BBP poles and literal U_0=0:

\[
H_N^{(r)}=\sum_{n=1}^N r(n)=
\frac18\sum_{j=1}^4 c_j
\left[\psi(N+1-a_j/8)-\psi(1-a_j/8)\right],
\quad (c_j,a_j)=(4,7),(-2,4),(-1,3),(-1,2).
\]

Because sum_j c_j=0, the leading log N and universal digamma -gamma terms cancel; first asymptotic source term is r(n)=15/(64n^2)+O(n^{-3}). Construct an exact symbolic proof (not merely a floating-point fit), and compare the source and harmonic observation functional as **different kernels**.

**Pass:** exact formula + cancellation + a declared new kernel map, if any. **Fail:** a proposed argument attributes the external HPB gamma to the original r(n) with no map. **Ambiguous:** a numerical coincidence with gamma, phi^{-1}, or a silver/golden regulator.

## P2. Transfer must respect the zero seed and the fixed character

The authentic completed base-16 orbit is x_n={U_n}={16^n(pi/16)-T_n}; source r(n), U_0=0, and carries cannot be changed. The pi frontier's necessary/sufficient fixed-h gate is

\[
c_A(h)=A^{-1}\sum_{n=A}^{2A-1}e(hU_n)\to0,\qquad h\in\mathbb Z\setminus\{0\}.
\]

To connect Pisot sheets to this orbit, propose an explicit source-preserving map and test it against:
- **Wrong real seed** s_*=-pi/16 with U_n=-T_n, whose circle phases lock at 0; any source-only argument must not falsely certify pi normality here.
- **Rational and periodic shadows**: nearby eventually periodic x_n and rational x=0.
- **Golden/silver changing-frequency charts** from PR #470: return the original fixed-h character exactly before taking a limit; moving-harmonic concentration is not fixed-h signed cancellation.
- **Independent algebraic obstruction:** X^2-X-1 and X^2-2X-1 have no root at 16. Hence no nonzero rational-linear 16-equivariant map from the corresponding unit carrier to a scalar base-16 line.

**Pass:** exact map + zero-seed preservation + a sign-sensitive bound that kills the wrong-seed mutant and helps the fixed-h gate. **Fail:** a map that kills its conjugate mode before inverse gluing, assumes Haar averaging, or proves a conclusion equally for the coherent wrong seed. **Ambiguous:** simulation with no source-selective estimate.

## P3. Find a positive result rather than recycling the anti-normality functional

For z_n=e(hU_n), the HPB real square-defect Q_N is a *locking detector*; Q_infty<infinity would imply Cesaro z_n->1, **the opposite of the desired normality**.

A source-specific result must control the signed complex average at fixed h, not just |z_n-1| or phase smallness. Compare the two orthogonal phase channels
\[
1-\cos(2\pi hU_n),\qquad 1-\sin(2\pi hU_n).
\]
The corresponding *dyadic* means tending to 1 are merely a restatement of the real and imaginary parts of the Weyl gate, **not** a new theorem. The log-weighted means tending to 1 are only necessary, not sufficient.

**Target theorem (OPEN):** derive from the original rational four-pole source and zero seed an original-source signed dyadic inequality \(\left|\sum_{n=A}^{2A-1}e(hU_n)\right|=o(A)\), or a genuinely weaker independently proved sufficient estimate consistent with the existing LS/H2* decomposition. The estimate must discriminate wrong seed s_*, the CB-3 nonstationary seed, and periodic completions.

**Hostile probe:** test any proposed bound on the exact wrong-seed model. If the same reasoning proves cancellation there, reject the proof regardless of how elegant its Pisot/Gamma imagery is.

## P4. Observer-feedback instrumentation (separate engineering/empirical research)

If a real controller is proposed, specify sensor output z_n, harmonic gain 1/n, subtraction log N, actuator constraints, and irreversible latch. Compare one-step and closed-loop reachable sets with and without injected consideration perturbation. Measure whether a finite B_crit predicts actual latch transitions; include reversible and dissipative controls. Phase/budget toy identities do not alone establish observer-dependent physical laws.

## Unpaid debts

- No authenticated nonlinear source-map from original BBP zero-seed selected orbit to phi-power phases.
- No original-source fixed-h signed cancellation inequality for pi.
- No all-test completed signed Weil positivity for RH.
- No independent scholarly priority/referee or formal kernel certification for new HPB claims.
- Numeric B_crit was computed at high precision and finite samples were replayed; a formal interval-arithmetic decimal certificate has **not** been built.

**Decision:** maintain as a draft research instrument with a valuable anti-normality obstruction; do not merge, tag, release, or promote a main-ledger theorem without standard SUCC review gates.

## P5. Constant circular aperture — new author refinement (HPB-C1…C4)

See [CIRCLE_WINDOW.md](CIRCLE_WINDOW.md). The circle's constant geometric window survives trajectory lock-in; the harmonic threshold changes allowed *controls* only if an explicit latch is installed. Select a fixed golden-angular half-width `delta=pi/phi`; its Fourier multipliers never vanish, with an explicit lower bound `2/[delta (sqrt5+1/2) h^2]`. For the authenticated dyadic BBP orbit define an L² aperture discrepancy; its convergence to zero is equivalent to the **still OPEN** fixed-h Weyl gate. Golden Pisot phase locking leaves a strictly positive geometric energy residual `phi^-1`, not Haar mixing.

**Pass:** prove a zero-seed/four-pole original-source decay estimate for this fixed-aperture energy; independently refute the same estimate for wrong seed `s_*=-pi/16` and CB-3. **Fail:** a moving observer-center distribution is presented as source uniformity, a rational aperture silently erases harmonics, or constant geometric width is misidentified with controllable reachability. **Ambiguous:** the aperture criterion alone, with no source-specific decay mechanism.

# Making the Weyl route tractable: the exact toolkit gap and how to close it

**Author:** Ravel. **Date:** 2026-10-27. **Status:** engineering/framework proposal (grounded in repo inspection).

## Diagnosis: why the Weyl route is intractable in SUCC *specifically*

SUCC's proven strengths (verified by inspection):
1. **Exact rational arithmetic** — `Fraction`/`sympy` everywhere (the whole source is rational).
2. **Provenance** — git-blob SHA-1 content addressing, `verify_provenance.py`, frozen imports.
3. **Formal kernel** — 66 Lean 4 files, a real Mathlib-adjacent proof layer.
4. **Method** — steelman/crucible/verdict with receipts; 918-line claim ledger with 8 status labels.

The **structural gap** for the Weyl route:

$$W_N(h)=\frac1N\sum_{n\le N}e(h\,16^n\pi)$$

involves **transcendental π** in an **exponential phase**. SUCC's exact-rational machinery *cannot
touch it directly* — `e(2πi h 16^n π)` is not rational, so every SUCC proof is forced to stop at the
**Green-tail transport boundary** ($U_n = 16^{n-1}\pi - T_n$ with rational $U_n$, summable $T_n$),
and then hand the transcendental part back to *human analytic reasoning*, which is exactly where the
wall lives. **The toolkit has no certificate type for "this exponential sum is sublinear."**

## The concrete machinery to add (in order of tractability)

### M1. A formal "exponential-sum certificate" object (the missing type).

Define a first-class certificate:
```
ExponentialSumCertificate := {
  phase:     (h, b, alpha)   # e(h b^n alpha)
  claim:     sublinear       # |sum| <= C N^{1-delta}
  witness:   (delta, C, proof)  # proof is either Lean or an interval-arithmetic receipt
}
```
This makes the Weyl bound a *type* that SUCC's ledger can label (PROVED / UNVERIFIED / REFUTED),
instead of an amorphous "the sum vanishes." Right now the ledger has **no such row** — that's the gap.

### M2. Interval-arithmetic Weyl probes (extends exactness to the transcendental part).

π is transcendental, but it has **provably correct rational enclosures** (Machin, Chudnovsky,
BBP). SUCC already has `adelic_gaussian_interval.py` and interval machinery. Add:
- A rigorous enclosure of $\{16^n\pi\}$ via **high-precision interval arithmetic** (not `mpmath`
  floats, which this session showed silently loses precision — the `16^n π` artifact).
- Then $e(h16^n\pi)$ is enclosed, and the Weyl sum is a **rigorous interval**, so claims like
  "$|W_N(h)| > 0.5$" or "$|W_N(h)|$ is not yet $< 10^{-6}$" become *certified statements*.
This converts "we observed decay" into "we *proved* the sum is in this interval at N=10^6."

### M3. Lean formalization of the *finite* reduction chain (the part that IS formalizable).

The session's proved reductions are all **finitely formalizable** in Lean:
- All-prime rigidity (Target A) — a clean Fourier/Cesàro statement.
- Source–orbit ×3 equivalence $O(1/N)$ — a clean triangle-inequality + summable-tail bound.
- Universal $O(1/N)$ ×3-defect — a boundedness statement.
- 3-adic memory $v_3 = O(\log_3 n)$ — an elementary valuation recurrence.
These are *exactly* the kind of "tractable load-bearing lemmas" AGENTS.md says to formalize. The
**infinite** step (Weyl → 0) is NOT formalizable today, but every *reduction* around it is. Formalizing
them makes the "one missing arrow" the *only* thing outside the kernel — which is a real robustness win.

### M4. A "sublinearity oracle" with adversarial mutation testing (steelman–crucible at scale).

The method says every claim needs a hostile counterexample. For the Weyl route, build a **mutation
harness** that takes any proposed sublinearity *mechanism* (e.g. "the Green tail forces cancellation")
and immediately tests it against:
- the future-selector $V_n=-T_n$ (coherent, must NOT pass),
- the #320 non-normal mutant,
- the sparse non-normal witness (this session's $0.1001000\ldots$),
- random + structured α.
If a mechanism passes all controls, it's a *candidate*; if it fails one, it's auto-REFUTED with a
receipt. This is the "reduced copy-paste fatigue, verification gates" that USER.md wants — and it's
what makes "full send" *safe* (no fake proof survives).

### M5. The decisive one: an **entropy/measure-rigidity certificate** (the real target).

Since the Weyl route itself is equivalent to ×3-invariance (proved this session), the *tractable*
version is to formalize the **Rudolph–Johnson input** as a first-class hypothesis type:
```
MeasureRigidityInput := {
  orbit:         {16^n pi},
  entropy_free:  PROVED (transcendence => not eventually periodic => h_top > 0),
  x3_invariant:  UNVERIFIED,   # THE single remaining cell
  ergodic:       UNVERIFIED,
  => Haar:       EXTERNAL THEOREM (Rudolph-Johnson 1990, BLMV 2009),
}
```
This makes the *one* open cell explicit and machine-checkable, so progress = filling that one cell,
and any future proof plugs in without rewriting the chain.

## The honest summary

The Weyl route is intractable **not** because the math is intractable in principle, but because
SUCC's toolkit **stops at the rational/transcendental boundary** and has **no certificate type** for
the sublinear exponential-sum statement. The fix is:
1. Add an `ExponentialSumCertificate` / `MeasureRigidityInput` type (M1, M5) so the statement is a
   *ledger-labelable object*.
2. Add rigorous interval-arithmetic Weyl probes (M2) so finite claims become *certified*, not observed.
3. Lean-formalize the finite reduction chain (M3) so everything except the one open arrow is kernel-checked.
4. Add adversarial mutation testing (M4) so "full send" is safe.

**Boundary:** this makes the route *tractable as a research program* (every claim checkable, every
open cell named, every mechanism auto-tested against counterexamples). It does **not** by itself
prove the missing arrow — the Weyl/×3-invariance step is still open. But it converts "we are stuck
on an amorphous hard statement" into "we have a machine-checked chain with exactly one named,
formally-typed open cell," which is the honest maximum of what tooling can buy.

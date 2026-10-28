# Operation π₃ — a certified base-3 digit handle, with genuine ternary BBP sources

**Date:** 2026-10-27. **Research-only child of [#329](https://github.com/femboy2112/SUCC/pull/329), exact parent `00f43cb871a71526bf520f646f594bcece5dbced`.** Unmodified original four signed BBP poles, \(U_0=0\), historical archives and `main`. **Base-3 and base-16 normality of π remain OPEN.**

This is a **working, executable and replayably certified ternary digit handle**, not a new random-access BBP formula directly for π. A request at ternary fractional position \(n\) computes an exact enclosing interval accurate *through position \(n\)*. No floating-point guesses. Repository files: `observational_succ/pi_ternary_handle.py`, `scripts/pi_ternary_digits.py`, `scripts/verify_pi_ternary_certificate.py`, `tests/test_pi_ternary_handle.py`.

## 1. Two published ternary BBP sources of π, via algebraic transforms

In the conventional BBP notation

$$P(s,b,\ell,\mathbf a)=\sum_{k\ge0}b^{-k}\sum_{j=1}^{\ell}\frac{a_j}{(\ell k+j)^s},$$

David Bailey's *Compendium of BBP-Type Formulas for Mathematical Constants* (8 April 2023, section 9, printed page 24, formulas 69 and 76) provides the **literal source identities**

$$\boxed{\pi\sqrt3=\frac19 P(1,729,12,(81,-54,0,-9,0,-12,-3,-2,0,-1,0,0))}\qquad\text{(B69)}$$

and

$$\boxed{\pi^2=\frac2{27}P(2,729,12,(243,-405,0,-81,-27,-72,-9,-9,0,-5,1,0)).}\qquad\text{(B76)}$$

Primary source: https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf. **The published identities are inputs, not new SUCC discoveries.** The literature excludes ordinary degree-one BBP formulas *for π itself* in non-power-of-two bases. These two formulas are for π√3 and π². They do not establish a sublinear-position ternary BBP spigot for π or its normality.

Two further independently specified mathematical sources are the unchanged original signed BBP π formula and the exact Machin identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\), whose alternating Taylor remainder has a rational bound.

## 2. Certify any finite requested ternary prefix with integer arithmetic

For any signed coefficient vector \(a_j\), positive BBP base \(b\), integer order \(s\), and rational front coefficient \(c\), set

$$Q_K=c\sum_{k=0}^{K-1}b^{-k}\sum_{j=1}^\ell\frac{a_j}{(\ell k+j)^s}.$$

Absolute convergence, denominator monotonicity and the geometric sum yield, without sign assumptions,

$$\boxed{|C-Q_K|\le|c|\frac{b^{1-K}}{b-1}\sum_{j=1}^{\ell}\frac{|a_j|}{(\ell K+j)^s}.}\qquad\text{(P3-TAIL)}$$

The implementation stores exact rational endpoints \(L_K,H_K\). If the source encloses \(\pi^2\), then for \(D=3^n\),

$$\boxed{\lfloor D\sqrt{L_K}\rfloor=\mathrm{isqrt}(\lfloor D^2L_K\rfloor),\quad
\lfloor D\sqrt{H_K}\rfloor=\mathrm{isqrt}(\lfloor D^2H_K\rfloor).}$$

If **both integer floors coincide**, they certify \(\lfloor3^n\pi\rfloor\). The integer part of π is 3, written \(10_3\). Subtract \(3\cdot3^n\) and write the n remaining base-3 digits with leading zeros. For B69, reconstruct via \(\pi=(\pi\sqrt3)/\sqrt3\) and exact \(\mathrm{isqrt}(\lfloor D^2C^2/3\rfloor)\) at each positive rational endpoint. A boundary-straddling interval triggers more source terms, **never a guessed digit**. The original BBP channel inherits the certified positive Green-tail inequality from [#308](https://github.com/femboy2112/SUCC/pull/308). Machin gets independently bounded alternating arctan series.

To replay a proof, the verifier reconstructs the rational endpoints from the exact declared source and term count, checks their SHA-256, independently recomputes floor witnesses, and rejects contradictory digits or duplicate source claims.

## 3. Executable handle and exact examples

From the repository root (stdlib Python >=3.10):

~~~sh
python scripts/pi_ternary_digits.py --start 1 --count 108 --certificate ternary-proof.json --pole-depth 6
python scripts/verify_pi_ternary_certificate.py ternary-proof.json
python scripts/pi_ternary_digits.py --start 501 --count 32 --certificate middle.json
python scripts/pi_ternary_digits.py --start 999 --count 2 --source ternary-pi2
python -m unittest discover -s tests -p 'test_pi_ternary_handle.py'
~~~

Positions are **one-indexed fractional digits after the point**. The default `--source all` requires four exact source proofs to agree; a specified single source still yields an interval-certified proof. Operational maximum precision is declared as 4096 fractional digits and may fail explicitly on a resource cutoff. This computes the enclosing prefix through position n, **not independent sublinear random access to n**.

**108 fractional trits certified using all four source routes:**

```
10.010211012222010211002111110221222220111201212121200121100100101222022212012012111210121011200220120210000101
```

The first 37 fractional trits agree with published OEIS [A004602](https://oeis.org/A004602). Requested positions **501–532** were independently certified as

```
11110221222121012002221022121220
```

and positions **999–1000** read `10`, so the thousandth fractional trit is **0**.

**Local authority:** twelve focused standard-library tests pass with genuine exact rational/integer arithmetic, covering source coefficient identities, all four agreement through 129 positions, 1000th-position holdout, OEIS head, source/pole mutations, rational-root floor proofs, certificate replay, five deliberate receipt corruptions and exhaustive 3-adic depth enumeration. Standalone JSON certificates for 1–108 and 501–532 were replayed successfully. Uploaded production module, both scripts and test file are exact Git blobs matching the tested local code (verify hashes in GitHub against logs); repository-wide native/hosted CI is a separate gate, not preclaimed.

## 4. The source's genuinely variable-depth prime-3 arithmetic

**New exact, source-typed observation:** Both B69 and B76 have an active sixth tap, which simplifies identically in its denominator:

$$\boxed{\frac{-12}{12k+6}=-\frac2{2k+1},\qquad
\frac{-72}{(12k+6)^2}=-\frac2{(2k+1)^2}.}\qquad\text{(P3-DUAL)}$$

Define \(r(k)=v_3(2k+1)\). The respective **local unweighted tap valuations** are \(-r(k)\) and \(-2r(k)\). For \(k_j=(3^j-1)/2\), \(r(k_j)=j\) exactly: a variable-length arithmetic pole-depth clock, unbounded across natural indices. For \(k\) modulo \(3^L\), depth \(r<L\) occurs \(2\cdot3^{L-r-1}\) times, and precisely one class has depth at least L. The expected **clipped** depth under a declared uniform finite time bin is \((1-3^{-L})/2\).

In contrast, the **real contribution** of the sixth tap at \(k_j\), including source prefactors and \(729^{-k_j}\), is

$$|B69_{6,k_j}|=2\cdot3^{1-3^{j+1}-j},\qquad
|B76_{6,k_j}|=4\cdot3^{-3^{j+1}-2j}.$$

Thus greater 3-adic pole depth corresponds to *doubly-exponentially tiny* individual real contributions along these special times. It is a source-relative arithmetical complexity observable, **not** a signed real-phase cancellation mechanism. The real series converge, but \(729^{-k}\) is *expanding* in \(\mathbb Q_3\); there is no assertion that the whole series converges 3-adically or that virtual paths are independent.

This is a concrete extension of the variable-length source observation theory in [#329](https://github.com/femboy2112/SUCC/pull/329), keeping distinct the new ternary series' poles and the original four-pole BBP rational forcing.

## 5. What this earns and what it does not

**Disclosed within the stated finite interface:** requested finite π trits through exact source intervals and integer-square-root reconstruction, each with a replayable machine witness. **Paper-proved elementary arithmetic:** tail formula and sixth-tap valuation/distribution. **Cited classical inputs:** B69, B76, original BBP and Machin identities. **OPEN:** authentic real base-3 Weyl cancellation

$$\boxed{\forall h\in\mathbb Z\setminus\{0\}:\ \sum_{n<N}e^{2\pi ih3^n\pi}=o(N),}$$

and the existing base-16 Weyl target for the unchanged original four-pole SUCC orbit. π² and π√3 admit 729-radix source recurrences but square-root/√3 algebraic transport does **not** automatically transfer normality or probability-space independence. The obstruction from [#327](https://github.com/femboy2112/SUCC/pull/327) and [#328](https://github.com/femboy2112/SUCC/pull/328) to overstrong prescribed moving conditional energies remains valid. The next probe must couple **authentic selected signed real phases** to these ternary source witnesses and survive changed-seed, rational-nonnormal and high-valuation controls. No RH claim, no main merge, release or novelty priority.

## Provenance / literature

- D. H. Bailey, *A Compendium of BBP-Type Formulas for Mathematical Constants* (2023), section 9, formulas (69) and (76): https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf.
- [OEIS A004602](https://oeis.org/A004602), external finite ternary-digit reference.
- [SUCC original BBP 2-adic zero boundary #321](https://github.com/femboy2112/SUCC/pull/321), [two-quadratic original Green-tail #308](https://github.com/femboy2112/SUCC/pull/308), and [π-source research #329](https://github.com/femboy2112/SUCC/pull/329).

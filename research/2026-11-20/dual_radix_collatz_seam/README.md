# Operation Dual-Radix Collatz Seam — mirror bookkeeping, two completions, and the 2–3–5 observer triangle

**Research-only source-faithful continuation of SUCC draft [#679](https://github.com/femboy2112/SUCC/pull/679).** Four original signed BBP poles, literal `U_0=0`, inherited archives, formal files, CI, and main remain unchanged. The subject is the user's proposed **mirror = digit bookkeeping change of frame**, with the reflected branch recording a digit and the transmitted remainder retaining the next recursion, together with the requested **2-adic/3-adic/Collatz arithmetic**.

## Strongest proved statements

- **The literal wave-level mirror commutes with the 16-channel digit/remainder unitary** from #679: `U R = R̃ U`, where the output mirror exchanges digit `d↔15−d` *and* remainder `r↔1−r`. A plain reflection alone neither creates nor erases information. Its composition with an actual Collatz step is **not** a conjugacy.
- **A single chronologically recorded digit string has two compatible completions:** `x_R=Σ d_j16^(−j)` in the reals, and a *constructed digit shadow* `y_2=Σ d_j16^(j−1)` in the 2-adics. The same all-5 word is `+1/3` in its real fractional presentation and `−1/3` in its 2-adic least-significant-first presentation. Digit complementation is `x↦1−x` in R and `y↦−1−y` in Z₂. The 2-adic shadow of the original π/16 digit sequence is well-defined, but **not** an intrinsic embedding of real π into Q₂.
- **The exact 2–3–5 reciprocal clock:** `J_n=(16^n−1)/15`; all-5 hex `A_n=5J_n` obeys `3A_n+1=16^n`, all-3 hex `B_n=3J_n` obeys `5B_n+1=16^n`. The 3 branch is a real odd accelerated Collatz one-step-to-1 family; the 5 branch is an explicitly separate affine control. In the 2-adic topology these finite clocks converge toward `−1/3` and `−1/5` while their 3-/5-adic *timestamps* are recoverable by isometric odometers.
- **Exact four-step-per-hex-5 Collatz peeling:** `16^k | (3N+1)` iff the last k hex digits of N are all 5. Writing `N=16^kA+0x55…5`, the ordinary shortcut map satisfies `C^(4k)(N)=3A+1`. This is an all-N exact theorem on a **restricted branch**, not universal Collatz convergence.
- **A nonextendable 2-adic singularity:** the accelerated odd Collatz map has no continuous extension at the two-adic root `−1/3`: two positive odd sequences tending to this root produce outputs 1 and 7, respectively. The unaccelerated shortcut map *does* continuously send the root to 0.
- **First-mismatch valuation:** for q=3,5,15, matching the 2-adic repeating `(15/q)` word for k digits then differing at digit `d'` yields `v₂(qy+1)=4k+v₂(d'−15/q)`. This explicitly places the hidden residual in the next transmitted digit.
- **2+3+5 GPS checksum:** independent calibrated mod-3, mod-5, and parity head readings, with previous mod-15 register, reconstruct one arbitrary new hexadecimal digit. Parity is necessary to distinguish 0 from F. The mathematical redundancy is **not** a physical fault-tolerance guarantee.
- **Source-selected finite π witness:** exact original BBP tail certifies the first twelve digits `3243F6A8885A` of `π/16`. Its source-derived 2-adic digit shadow starts `0x…23` (first recorded digit least significant), so `v₂(5Yπ+1)=4`, `v₂(3Yπ+1)=1`. This finite mismatch does **not** establish normality or derive a new link to the auxiliary 11-adic Fibonacci eigenchannel.
- **Exactly equivalent normality reformulation:** π base-16 normality iff the 2-adic digit shadow is Haar-generic under the **2-adic radix digit-shift**. Frequency of every fixed consecutive-5 or consecutive-3 block can be probed by valuations of `3M_n+1` or `5M_n+1`. An all-late-shell lower density of one such digit is a **conditional sufficient R0 criterion**; still open for the source.

## Reproduction

```sh
cd research/2026-11-20/dual_radix_collatz_seam
python -m unittest -v test_dual_radix.py
python independent_audit.py
python -m compileall -q dual_radix.py test_dual_radix.py independent_audit.py
```

The current scoped receipt is **19/19** focused tests, **17,626** independent exact symbolic/congruence assertions, Python compilation and JSON validity. The full inherited SUCC suite and mandatory root provenance/observer/ordinal gates have **not** been run. Mathematical proof scope and controls are in [THEOREMS.md](THEOREMS.md), status in [CLAIM_LEDGER.md](CLAIM_LEDGER.md), next discriminators in [NEXT.md](NEXT.md), provenance in [PROVENANCE.md](PROVENANCE.md), and executed receipts in [VALIDATION.md](VALIDATION.md).

**No main modifications, merge, release, physical quantum-energy inference, Collatz universal claim, or π-normality promotion.**

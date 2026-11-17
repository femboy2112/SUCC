# Terminal-domain-wall crucible — actual verification and scope

**Date:** 2026-11-16. **Pinned main baseline:** 81be6b897ae980b801a3b9de9e22ef81e8360bfb. **No π-normality or R0 proof is claimed.**

## Executed local exact tests

Re-read and reproduced the parent virtual-form exact test file as a baseline: **10/10 unittest PASS**, whose Git blob is a8a3bc54d9ab4073ecb3339ea6078c0e1cac42ea (parent PR #657).

Then executed the *new* standard-library exact script (same committed bytes):

~~~text
python -m unittest -v /mnt/data/test_terminal_wall_crucible.py
Ran 13 tests — OK (0 failures/errors)
~~~

The tested file has **12,044 UTF-8 bytes** and exact local Git blob SHA-1
**347785e6ff064bc9085d3032cb1f94eafccf0d76**. Its GitHub fetched blob SHA was checked equal before publishing this receipt. The module is [tests/test_terminal_wall_crucible.py](../../../tests/test_terminal_wall_crucible.py).

Controls actually exercised:

- Original literal signed BBP poles, U₀=0 and seven or more direct-fraction versus chronological U_m identities.
- Exact digit/fraction reverse branch y_k=(d_k+y_(k−1))/16 for positive and negative rationals.
- **All 4,096 possible length-three hexadecimal words × three distinct fractions = 12,288 exact inequality tests** of the new two-sided domain-wall norm; no floating-point phases.
- All-0, all-F, and negative near-zero terminal rays; co-moving wrong-seed model is labelled a lawful rational tail control, not a numerically known original T_n.
- Exact +1 integer-carry changes D by ≤1 and J by ≤2, including authentic finite BBP C_m.
- Three independent finite odd-CRT cofactor residue choices plus all-0/all-F terminal suffixes, with full denominator and numerator residues.
- For **M=1,8,32,64**, explicit positive, decreasing zero-seeded rational counterfeit matching the authentic first M forcing terms; entire telescoping identity and eventual exact radix lock, including the terminal O(B^-5) formula.
- Exact finite identities for **the n^-2 Gamma-leading coefficient** and full exponential tail correction (not just rounded approximation).
- Exhaustively counted small low-event symbolic word budgets, with a valid combinatorial upper count.
- Original source C_(2B) phase-fiber clones at **B=16,32,64,128,256**, retaining denominator and fractional phase while suppressing all terminal events.
- Source-fresh primes p=8n−7 (when prime) at n between 2 and 39, with p in the **reduced** denominator exactly once and the phase-fiber clone preserving its numerator residue.

A separate SymPy algebraic calculation independently factored the rational source seam:
\[
r(n)-f_0(n+1)=
\frac{24000n^5+87240n^4+47714n^3-56719n^2+1180n+2773}
{64(n+1)^2(n+2)^2(2n-1)(4n-1)(8n-7)(8n-3)}>0
\]
for every integer n≥1. It also independently recovered the leading source expansions
\(r(n)=15/(64n^2)+151/(512n^3)+O(n^{-4})\) and
\(f_0(n)=15/(64n^2)+1/(32n^3)+O(n^{-4})\).
The exact polynomial inequality is independently justified by the paper argument. SymPy is a separate implementation of the same definitions, not a blind academic witness.

## Authentic original BBP finite terminal observations

Every quantity below was first evaluated as an **exact Python Fraction**; decimals are readability-only. The rational terminal norm values for B=16..256 reproduce the parent PR #657 baseline.

| B | D_B (non 0/F) | J_B (direct 0↔F) | Exact-rational \(\mathcal R_B\) (decimal view) | Phase/cofactor clone \(\mathcal R_B^\star\) (decimal diagnostic) |
|---:|---:|---:|---:|---:|
| 16 | 14 | 0 | 0.075084310973 | 2.062e−5 |
| 32 | 27 | 0 | 0.079825201617 | 4.114e−5 |
| 64 | 57 | 0 | 0.088161132374 | 1.372e−5 |
| 128 | 111 | 0 | 0.089051047282 | 1.113e−5 |
| 256 | 231 | 1 | 0.089039450341 | 8.205e−7 |
| 512 | 449 | 8 | 0.085925198153 | not evaluated |
| 1024 | 876 | 9 | 0.079221124066 | not evaluated |

All seven displayed authentic \(\mathcal R_B\) were compared to **1/20 using exact Fractions**, and every one was greater. The B=512 and B=1024 values are **additional finite diagnostics within the historical Main XXVI training horizon**; they are not prospective held-out validation and cannot establish the eventual lower bound. The domain-wall coercivity bounds were checked exactly on these authentic terminal digits, in addition to all length-three words.

## Counterfeit and calibration history

The zero-seeded positive decreasing rational counterfeit is **constructive for every finite M** in the paper. The tests instantiate M=1,8,32,64, with chosen radix-denominator exponents K=4,12,38,70, respectively. Every M matches its entire initial forcing prefix, obeys the same leading Gamma/n² asymptotic, and has a locked completed rational orbit.

**Preserved failure/calibration:** the first Gamma-leading test used an overstrong fixed 0.0001 bound at n=M+100; it failed because the true \(1/n\) finite correction is about 0.0003. A subsequent *exact* test exposed a sign error in the proposed finite n²g correction. Both were repaired by deriving and testing the **exact rational identity** with opposite signs for the g and r leading corrections. The final script passes 13/13. This failure history is recorded so the tests are not presented as a blind initial pass.

**No tested mathematical falsification of TW-01 through TW-07 occurred.** Paper proof and finite brute-force/test agreement are distinct evidence layers.

## Boundaries and unexecuted gates

- The terminal positive domain-wall density TW26 is **UNVERIFIED**; R0, all-mode π normality, and RH remain **OPEN**.
- The counterfeit shares a **finite prefix** and leading asymptotic of authentic BBP, but differs from its **infinite exact four-pole source**, so it is a method-level falsifier, not a proof π fails R0.
- The phase/cofactor clone preserves one exact terminal phase/denominator; it is **not** a lawful full original time/seed history.
- The combinatorial count of low-energy symbolic forms is **not** a measured Shannon entropy nor a statement about π's Kolmogorov complexity.
- The full repository test discovery, root AGENTS.md provenance/observer/ordinal gates, Main XXIV–XXVI integration suites, Lean, hosted CI success at the final exact head, and external blind mathematics review are **NOT RUN/NOT CLAIMED** in this branch-local validation. Hosted check status should be re-read at the final PR SHA.
- A numerical value for a finite B is not a certificate for an eventual forall-B theorem; new held-out work requires preregistration.

**Verdict:** source-specific finite arithmetic reconstructed, a rigorous new symbolic norm equivalence and strong no-go mutants added. The exact all-shell arithmetic bound remains the next truly verdict-changing theorem.

# Front B — hostile crucible record

Two blind reviewers were given only `../PROOFS.md` (first draft) and the source definitions. Neither saw the author's reasoning.
**Both are same-model (Claude) subagents. They are not independent scholarly referees.** Their scripts are archived here unchanged as receipts. They are not run by the test suite.

## Rigor audit — `auditor/` (proof-by-proof grading)

**Verdict on the draft: BLOCK, narrowly.**
- No false theorem was found.
- CB-1, CB-1g and the forward direction of CB-2 earned PROVED as written.
- Gaps found:
  - the converse of CB-2 was unwritten;
  - CB-2′ had undefined window measures, an unbound `η`, an unstated uniform Lemma 2.1, and an unstated compactness/telescoping step;
  - Lemma 2.3 holds only almost everywhere;
  - Lemma 3.3 smuggled a modulus-of-continuity rate (it needs Hölder `p`) and asserted `j\ge0` without argument;
  - Lemma 3.4's truncation bound was too weak as stated (it needs an explicit `t_0` restriction);
  - CB-4 (⇒) was unwritten;
  - the "Meaning" paragraph overreached.

**All of these are repaired in the current `../PROOFS.md`:**
- Lemma 2.5 (the converse, with Wall's theorem);
- the CB-2′ rewrite;
- the a.e. statement of Lemma 2.3;
- the Hölder regularity in Lemma 3.2;
- the lattice-matching argument;
- `t_0\le0.04` with `L=\lceil5\log_{16}A\rceil`, giving a per-event bound `\le4A^{-3.5}`;
- the CB-4 proof;
- the narrowed "Meaning" paragraph.

## Refutation attempt — `refuter/` (structure-theorem-directed counterexample hunt)

**Verdict: CB-1, CB-1g, CB-2, CB-2′, CB-3 and CB-4 SURVIVED.**

| Probe | What it attacked | Result |
|---|---|---|
| `p1_cb1_orbit.py` | CB-1 on orbits with seeds `0, 1/5, -1/3, 15/16, 1/7, (2^{61}-1)/2^{62}`, `n<400`, every `S_d(n)<1` | 20,244 checks, 0 mismatches |
| `p2_cb1_adversarial.py` | Seed left free, so `y` is placed exactly at the endpoints, at `±10^{-60}` from them, and at the wrap; `n` up to `2^{61}`; extreme splits | 3,764,576 checks, 0 mismatches |
| `p2_cb1_adversarial.py` | Positive one-pole mutant | 10,144 checks, 0 mismatches |
| `p2_cb1_adversarial.py` | **Control:** a forcing with one negative term | 752/3,200 mismatches (positivity is load-bearing; the harness detects failure) |
| `p3_cb1g.py` | CB-1g with `16^dT_n\to1` (gap down to `2.1\cdot10^{-35}`) | Agreement everywhere except exact-endpoint ties. Those are rounding below 200-digit working precision; the exact-rational ties in `p2` are clean |
| `p4_cb3.py`, `p4b_cb3_bump.py` | CB-3 family at `t_0=0.04` | `\min\partial_vΦ=1.0`; calibration residual `\le8\cdot10^{-23}`; exact expectations `\sup|\mathbb Eb-δ|` from `2.6\cdot10^{-6}` (`A=10^5`) to `1.2\cdot10^{-8}` (`A=10^{20}`), against an uncalibrated control of `8.7\cdot10^{-5}` |
| `p6_cb2.py` | The CB-2 kernel: tried to defeat Lemmas 2.3–2.4 | The kernel `\sqrt v L` is real (`|∫|\le5\cdot10^{-35}`), but `a+v+εH` is non-monotone for every `ε>0` tested (`0.1, 10^{-3}, 10^{-6}`). No non-Haar `ν` survives |

**Two tombstones from this review, both now corrected in `../PROOFS.md`:**
1. *Corollary 2 is not an extension of #521 CT-03.* "Admissible" coincides exactly with CT-03's domain: `A\ge2^{2d-3}`, certified for `d\le200` by `p5_domain.py` and independently by `../admissibility_law.py`.
2. *The first CB-2′ remark's witness was defective.* The corrected witness is `G(t)=εt\sin(2\pi\log_2t)`, with dyadic meaning `A=2^j`; this is realised numerically in `p6_cb2.py`.

**Receipt gap flagged by the refuter.** The ledger cited `VALIDATION.md` and `FINITE_RECEIPT.json` before they existed. See `../VALIDATION.md` for their current status.

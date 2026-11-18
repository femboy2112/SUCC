# Read-only audit of the late adelic frontier

**Pinned commit:** `97c7433371feca631991a1b8227b656e92e4abcb`.
Parent: `16d04ab58e213e75ab47e61a170138196dbcd292`.
Branch label: `research/pi-normality-crucible-frontier-2026-11-17`.
The branch label and prose do not establish the author's model identity.
This is same-model mathematical triangulation, not an independent external
referee report. No repository files or git state were modified.

## Inspected objects

At the pinned commit:

- `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md`
  (Git blob `379c014f8ebdf7df82d433f26659660942fa1bbf`);
- `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_VALIDATION.md`;
- `observational_succ/adelic_bbp_normality_crucible.py`
  (blob `ad61a1fd4ac15820e81a0a8aef8fd6101434bb0b`);
- `tests/test_adelic_bbp_normality_crucible.py`
  (blob `8072237302a3042a74b1ad29d994fdf229d90b22`);
- the module's direct dependency `observational_succ/borwein_quantitative_certificate.py`.

Main comparators at `81be6b897ae980b801a3b9de9e22ef81e8360bfb`:
`research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md`
(CG-01) and `research/2026-11-06/prime_frobenius_spectral/THEOREMS.md`
(PF-01 through PF-03). Current local comparators are EPS-01/03 and the
sharp Borwein inverse/L2 theorem already supplied to the parent.

## 1. Prime survival: correct local result, inherited mechanism

ANC-07's selected prime bands and principal parts are correct. Each chosen
prime appears at a single native pole; the coefficient is respectively
4, -1, or -1/2, and propagation multiplies it by a unit power of 16.
Its product has logarithmic rate (8/3)n, while its native LCM envelope has
rate 6n.

The novelty claim needs correction. PF-02 already treats **all** primes
in (2n,4n], including the collided class-3/7 subband omitted by ANC-07.
PF-03 gives the upper class-1/5 single-pole band; ANC-07 includes the
additional explicit final class-5 endpoint 8n-3, which is also an immediate
first-pole calculation. More substantially, CG-01 already proves survival
of every born prime p >= epsilon*n eventually for each fixed epsilon > 0,
and log Q_n = 6n+o(n). ANC-07 alone gives only

\[
8/3\le\liminf\log Q_n/n\le\limsup\log Q_n/n\le6.
\]

It cannot supply the equality 6 without additional arithmetic. The current
EPS theorem advances the cutoff to p >= A*n/log n for any fixed
A > 20 log2, with an explicit finite sufficient condition. These are
different strengths and should not be presented as competing new proofs
of the same frontier.

## 2. Borwein Parseval–Cauchy–Schwarz: correct exponent, no selected saving

Conditional on the stated Erdős–Turán bound, ANC-11's Parseval–CS step
is correct. With a Fourier floor c/h^2 and V = ||L*(mu-m)||_2^2,

\[
\sum_{h=1}^H\frac{|\widehat{\mu-m}(h)|}{h}
\le\frac{\sqrt V}{c}
\sqrt{\frac{H(H+1)(2H+1)}{12}}.
\]

The factor 12 includes the two Fourier signs in Parseval. Replacing
sqrt(V_true) by sqrt(V_terminal)+epsilon is justified by Minkowski.
Optimizing gives discrepancy O((sqrt(V)+epsilon)^(2/5)), or O(V^(1/5))
when epsilon is absent. This overlaps the current sharp 1/5 inverse-energy
theorem. The latter additionally proves the exponent cannot improve
uniformly over probability measures and supplies an explicit coefficient
without using Erdős–Turán. Neither theorem proves V -> 0 for the selected
BBP source.

The rational floor 5733/279752 is valid but weaker than the current direct
bound 63/(289*pi^2). A comparison of exponent 2/5 with 1/5 without naming
whether the variable is sqrt(V) or V would be misleading: they are the
same energy exponent.

## 3. ANC-12: reduced-denominator preservation is false as written

The residue R_sharp = N mod(16^B Pi_star) need not be coprime to the
collided factor Q/Pi_star. The first failure in its declared B >= 2 range
is B = 3:

\[
\begin{gathered}
N=80827484660698633414,\quad Q=24536311574775,\\
\Pi^*=19224941,\quad M=78745358336,\quad
R^\sharp=67379365062,\\
\gcd(R^\sharp,Q)=3,\quad
\operatorname{den}(V^\sharp)=8178770524925=Q/3.
\end{gathered}
\]

The same example **does** preserve the 2-adic residue, all selected prime
principal parts, and D_B = J_B = 0. Its failure is precisely the stronger
reduced-denominator claim. The native test suite skips B = 3 and never
asserts denominator equality, despite a comment claiming that property.

The asserted all-B inequality 16^B Pi_star < Q has no all-B proof in the
manuscript: logarithmic asymptotics establish only an eventual statement.
The bounded scan B = 2,...,80 found no failure of this inequality, which
does not repair the universal quantifier. Also, q_coll ~ exp((20/3)B)
must be replaced by q_coll = exp((20/3+o(1))B). Only logarithmic
equivalence has been shown.

**Repair.** `ANC12_EVENTUAL_REPAIR.md` proves a corrected eventual theorem:
search the primitive progression R = R_0+tM using L > 4^omega(q) terms.
Inclusion–exclusion ensures a coprime term; CG-01 ensures those terms fit
in [0,Q) for every sufficiently large B. This preserves the exact reduced
denominator and both projections. A separate exact B = 3 repair uses
t = 1, R = 146124723398, and keeps Q unchanged. The original failure is
retained verbatim in that appendix.

**Boundary to the repair.** `MESOSCOPIC_CRT_RIGIDITY.md` applies EPS to a
much larger authenticated inventory. The remaining cofactor then has
log q = O(B/log B), so q < 16^B eventually. The same signature permits
exactly phi(q) distinct terminal words in an explicit progression, with
at most one candidate for the all-zero word. Thus ANC-12's freedom
depends materially on its small selected inventory. This rigidity still
does not exclude the authentic low-wall word.

## 4. Source and logical scope

A shell-dependent terminal clone is not a new coherent zero-seeded
trajectory under the original source. An octic period character belongs
to a forcing/history, not intrinsically to a rational endpoint; the clone
does not itself preserve such a source invariant. The valid no-go result
is confined to the listed finite terminal data.

Likewise, adding a new invariant that distinguishes the locked TFL source
does not refute the existing counterexample to the earlier weaker
nonzero-pole-residue hypothesis. It defines a stronger hypothesis and
requires a new source-to-phase theorem. This report does not certify the
full octic quotient or 2-adic logarithm sections; the parent's separate
history audit handles their identified sign issue.

Authentic terminal coercivity, R0, swept Borwein convergence, and full
base-16 normality remain **OPEN**. No unconditional signed saving was
found in the audited results.

## 5. Actual validation and raw receipts

The pinned module, its direct dependency, test file, and manuscripts were
extracted into scratch. Actual
command: `timeout 90s python replay_and_hostile.py`, workdir
`prime_scratch/late_frontier`. Exit 0; 15 tests passed, no failures or
errors, recorded focused-test duration 1.542743021 seconds. The same
bounded run checked B = 2,...,80 for the claimed clone properties and
retained the first five reduced-denominator failures.

The suite is **not all-exact**: its ANC-11 test uses floating
`math.sin` and `math.pi` for 50 modes. The rational counterexamples and
their projections were checked with exact `Fraction` arithmetic. No
SymPy or mpmath claim from the external receipt was independently replayed.

Files:

- `late_frontier/replay_and_hostile.py`: extraction-local focused runner;
- `late_frontier/focused_replay_raw.txt`: native 15-test output;
- `late_frontier/replay_and_hostile_receipt.json`: pin, hashes, results,
  exact counterexamples, bounded fit scan;
- `late_frontier/repaired_b3.py`: independent four-fraction exact repair check;
- `late_frontier/repaired_b3_receipt.json`: all repaired B = 3 values and
  both projections (command `timeout 10s python repaired_b3.py`, exit 0).

No broad gates or repository mutation were performed. Paper proofs carry
the universal claims; finite checks carry only their declared finite scope.

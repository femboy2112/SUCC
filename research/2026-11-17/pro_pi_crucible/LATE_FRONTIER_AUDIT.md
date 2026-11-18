# Final source refresh, exact failures and surviving arithmetic

This dossier was developed against main
81be6b897ae980b801a3b9de9e22ef81e8360bfb. During the operation, two relevant
remote updates appeared. Both were fetched and inspected read-only. No
donor branch, working tree or frozen artifact was changed.

| Source | Earlier observation | Later inspected pin |
|---|---|---|
| PR #663, Borwein kernel/scale frontier | 16d04ab58e213e75ab47e61a170138196dbcd292 | 814cfe06999f9083b5c2eee479d21bfb951d724f |
| research/pi-normality-crucible-frontier-2026-11-17 | Absent from the accessible remote | 97c7433371feca631991a1b8227b656e92e4abcb |

The second branch's parent is 16d04ab58e213e75ab47e61a170138196dbcd292.
The branch name and manuscript attribution do not independently verify
the author's model identity. Its own concluding status leaves normality
open. The audits below do not refute a proof of normality: no such completed
proof is supplied there.

## 1. #663: useful new identities, no original-source cancellation

The refreshed six-file delta proves a universal finite-atomic energy floor
of order N^-4, exact block and binary-tree variance budgets, a dense-horizon
interpolation bound, and the authentic positive Pascal/Gamma tail hierarchy.
Its binomial observer converges to the analytic source carrier, not to the
empirical real-circle phase measure. These are credited contributions.

The source audit found no load-bearing mathematical error in those stated
bounds. Minor qualifications are recorded in
[audits/PR663_REFRESH_WAVELET_AUDIT.md](audits/PR663_REFRESH_WAVELET_AUDIT.md):
an additional contrast need not be linearly or stochastically independent;
normalization by P_M requires M>=1; direct file execution omits test classes
placed after unittest.main, whereas the reported import/discovery command
does find them. The stated 53-test receipt was inspected, not replayed here.
It contains floating diagnostics as well as exact rational checks.

## 2. The adelic branch: three exact corrections

### ANC7: the first logarithm has the wrong sign

Set A=1-2v+2v^2, B=1-2v^2, C=1-v+iv, D=1-v-iv. The original-source series
has derivative

\[
G'(v)=\frac{4v^6-2v^3-v^2-v}{1-16v^8}
      =-\frac{v}{2A}-\frac{v}{2B}.
\]

The corrected primitive is

\[
G(v)=-\frac18\log(A/B)-\frac1{8i}\log(C/D).
\]

The printed first plus sign produces derivative -1/2 at zero, although
the displayed authentic series has derivative zero there. Exact symbolic
subtraction verifies the repaired identity. It is the first sign that
changes; the second minus sign remains.

The corrected logarithms converge uniformly on the 2-adic unit disk in
Q_2(i). At v=1 the two ratios equal -1 and log_2(-1)=0. Thus the authentic
backward seed is indeed zero. The uniqueness statement concerns a bounded
analytic section on all Z_2; boundedness of a forward sequence alone does
not select seed zero. The repaired proof is retained in
[audits/ADELIC_HISTORY_AUDIT.md](audits/ADELIC_HISTORY_AUDIT.md).

### ANC13: the general character equality fails

All eight basis columns of the displayed partial-fraction matrix verify
exactly. Its Gaussian weighted residue sum is 4 alpha_3, rather than
4(alpha_3-alpha_4). The polynomial Q(t)=1 gives

\[
\alpha_3=\alpha_4=1/64,\qquad
4(\alpha_3-\alpha_4)=0,\qquad
\text{Gaussian sum}=1/16.
\]

The restricted r1/r2/coboundary examples have alpha_4=0, so their character
values survive. A restricted period-seed statement also needs regularity
at every integer used by the forward and backward sums: h(n)=1/(n-2)
shows why regularity only at n<=1 is insufficient. Transporting a backward
2-adic value into the real field is justified only after that value has
been proved to be the rational number -h(1).

### ANC12: the reduced denominator can cancel

At the literal source's B=3 shell,

\[
U_6=\frac{80827484660698633414}{24536311574775},\qquad
\Pi^*=19224941.
\]

The proposed R_sharp=N mod(16^3 Pi^*) equals 67379365062 and has
gcd(R_sharp,Q)=3. Its shadow therefore has reduced denominator
8178770524925=Q/3. The 2-adic projection, selected prime principal parts
and zero terminal word survive; preservation of the full reduced
denominator does not.

The native 15-test suite passes because it tests B=2,4,8,12 and never
asserts reduced-denominator equality. Its finite scan to B=80 also cannot
prove a displayed all-B fitting inequality. The denominator asymptotic
must be imported from main CG-01; the draft's divisibility envelope alone
does not prove it. Logarithmic equivalence gives exp((20/3+o(1))B), not a
ratio-one asymptotic to exp(20B/3).

The exact failure and a primitive-progression repair are proved in
[ANC12_EVENTUAL_REPAIR.md](ANC12_EVENTUAL_REPAIR.md). The repaired theorem
is eventual, with no claimed explicit B_0. Its independent finite B=3
witness retains Q exactly. Enlarging the selected prime inventory using
EPS gives the complementary restriction in
[MESOSCOPIC_CRT_RIGIDITY.md](MESOSCOPIC_CRT_RIGIDITY.md).

## 3. Novelty and source boundaries

ANC-07's selected prime laws are valid single-pole calculations already
substantially contained in main PF-02/PF-03; main CG-01 is stronger.
EPS adds a growing-depth height estimate and an n/log n cutoff. The
mesoscopic CRT theorem then couples that larger inventory to integer
winding, without excluding the authentic low-wall language.

ANC-11's Parseval--Cauchy--Schwarz argument gives interval discrepancy
O(V^(1/5)), conditional on its stated Erdős--Turán input. This overlaps
our energy exponent. Our direct measure-inverse proof also establishes
the optimality of that exponent over all circle probabilities and gives
an explicit constant. Neither argument proves decay of authentic energy.

An octic period fingerprint belongs to a source history, not intrinsically
to a rational terminal state. A shell clone carrying selected terminal
data is not thereby a second authenticated history. A stronger fingerprint
excluding a prior locked example does not invalidate that example's
counterexample to weaker hypotheses.

All three audit paths share the model family and repository provenance.
They are mathematical and implementation cross-checks, not blind external
witnesses. No claim of global priority is made.

## 4. Actual execution

- The pinned native adelic suite was replayed once: 15 tests, no failures
  or errors. The same bounded run scanned B=2,...,80. Its receipt is
  evidence/adelic_replay_hostile.json; raw test output is
  evidence/adelic_replay_raw.txt. At least one native test uses floating
  sine/pi, so the whole suite is not labeled exact.
- The exact B=3 repair was run once by the prime path; its original script
  and receipt are archived as audits/repaired_b3_original.py and
  evidence/adelic_repaired_b3.json.
- The root then executed the portable audit_adelic_pinned.py. It checks
  the sign, all eight matrix columns, the general character counterexample,
  and the B=3 denominator failure directly. Exit 0; receipt and full JSON
  output are evidence/audit_adelic_pinned.json and its stdout companion.
- The four-case crt_signature_probe.py checks the exact word classification,
  including a control where q>K and injectivity fails. Exit 0; its receipt
  is evidence/crt_signature_probe.json.

No finite check supplies an all-shell limit. Original-source terminal
coercivity, R0, swept convergence and full base-16 pi normality remain OPEN.

## 5. Closing delta: latest pins and results that survive correction

At the closing source cutoff, #663 is74b9f4806fdfebca4be66e2c5bfdbd9b5fc2273a
and the adelic branch is9ff8544c799b5e4c8eb1db33127438bc3f221045.
The #663 change adopts the larger ANC-11 Fourier constant and adds one
method; its retained 53-test receipt describes the earlier blobs.
The adelic head merged our first published 1d33174c and sister observer
work, then added FQR-01--10. Imported copies are shared provenance.

The original ANC manuscript is unchanged, so the three exact errors above
remain. Its validation does remove the earlier finite-to-all-B sentence
and now reports 25 tests. That receipt was inspected, not replayed here.

The valid new arithmetic deserves credit:

- FQR identifies the full modular coefficient packets with the original
  BBP partial sums or the negative second-formula partial sums. This is
  exact coefficient structure, not signed circle cancellation.
- Its lane-restricted LCM improves the sufficient survival constant to
  A>4 log2+6 after repairing the normalization to F=16 C. The finite
  certificate and full proof are appended to EFFECTIVE_PRIME_SURVIVAL.md;
  the asymptotic coefficient explicitly imports fixed-modulus PNT.
- Its actual-surviving simple-prime inventory leaves q=exp(O(sqrt B)).
  M-04 credits that choice and proves the exact phi(q) word count with
  an elementary cofactor bound. It does not prove universal survival
  at the square-root threshold.
- Its exact grid energy 576/(417605 N^4) for 9|N and refined Fejer floor
  are valid instrument refinements; neither estimates authentic decay.

Corrections and boundaries are equally explicit:

- The claimed valuation range{-1,0} fails at U_1=47/15,p=47. The valid
  consequence is valuation>=-1, or denominator exponent at most one.
- The printed FQR normalization fails its denominator bound at p=13, n=8:
  it gives 7/64, while the claimed denominator envelope is 4. Correct F=7/2
  works. The repaired lane-height theorem survives.
- The top-block carry equation needs modular wrap. A comparison rational
  exposes the missing inference; no authentic no-wrap counterexample was
  found in the bounded B<=32 probe. The corrected congruence preserves a
  comparison of the scaled word qC. It provides no wall-energy transport
  from qC back to the target C.
- FQR-10's backward-seed assertion for H-03 is false: its sinc interpolant
  vanishes at every nonpositive integer, so the discrete backward seed
  is 0, not -q. H-05 writes the proof and makes no Z_2-analyticity claim.
  GSC's different rational coboundary does have seed -delta_B. Adding a
  new hypothesis that distinguishes a prior control does not refute the
  original no-go theorem, which never claimed that hypothesis.

See audits/FQR_FRONTIER_ADDENDUM.md and
audits/ADELIC_9ff8544c_DELTA_ADDENDUM.md. One bounded exact arithmetic
probe was executed by the prime path, archived as
audits/fqr_minimal_arithmetic_probe.py with
evidence/fqr_minimal_arithmetic.json. No upstream 25-test replay or new
broad suite was run. These corrected local theorems still supply no
category D/E exclusion of authentic low-wall asymptotics.

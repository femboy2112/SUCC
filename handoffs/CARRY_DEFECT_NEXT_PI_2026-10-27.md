# Continue from periodic observers and moving mixed-lag loss

Recheck the live head and draft PR of
`research/periodic-mixed-lag-source-2026-10-27`. Its parent is #317 at
`848bad224fef455a9f87ed19e947c936d309c965`. Read `AGENTS.md`,
[the synthesis](../research/2026-10-27/CARRY_DEFECT_SYNTHESIS.md),
[joint proof](../research/2026-10-27/MIXED_LAG_PERIODIC_COERCIVITY.md),
[ledger](../docs/CLAIM_SUPPLEMENT_CARRY_DEFECT.md), and
[validation](../research/2026-10-27/CARRY_DEFECT_VALIDATION.md).

The new proved input is uniform signed loss against every periodic unit
observer and every mixed-lag tuple in the prescribed moving-span schedule.
For $P(E)=\prod_i(E^{\ell_i}-1)$, $d=\sum_i\ell_i$, fixed $h\ne0$ and
$0<\delta<1$, all $p+d\le N^\delta$ obey

$$
\sum_{a\bmod p}\left|\sum_{\substack{n\le N\\n\equiv a\pmod p}}
e(hP(E)U_n)\right|
\le N-\frac{1-\delta}{14}\log_8N+O_h(1).
$$

The all $N$ version and unknown universal onset are in the proof.
The complete future comparison error after $M$ is at most
$11|h|/(112M)$, independent of lag order/span. It compares with the
**completed** frequency $hP(16)$; replacing this with $hP(16)U_n$ loses
the exponentially large counterterm. The periodic inverse denominator is
$|hP(16)|(16^p-1)16^m$; arbitrary template phases cancel only through
the proved within-residue and final-period identities.

The theorem also permits separately optimizing the template on each
eligible geometric block. It proves no cross-block cancellation and no
improvement in logarithmic order. All fixed-mode normalized bounds still
tend to one. The changed seed $V_n=-T_n$ remains the mandatory hostile
control; the original zero selector is load-bearing.

The exact all-center carry instrument bounds Fourier loss from integer
branch dispersion, preserving signed inverse-Green cross terms and the
homogeneous boundary. Its complete quadratic optimization equals circle
variance and has a proved $2L/3$ loss ceiling. Do not promote that identity
or finite count observations into the missing analytic estimate.

The next arithmetic target is growing within-block loss, or a quantitative
signed combination of authentic residue sums. Any van der Corput iteration
must pay its actual lag boundary and error terms; the current logarithmic
saving does not silently become relative cancellation under iteration.

Use the original poles and zero seed, isolated child branches, exact source
passports, and finite hostile controls. Run the four native repository gates
on the finished tree. Replay with `python scripts/carry_defect_probe.py
--verify`. Four Lean declarations cover finite algebra/count implications
only. Commit/push coherent work and open a stacked draft; do not merge,
release, replace archival sources, or report pending CI as passed.

The proposed full-suite timeout increase is a reviewable patch only: the
OAuth push credential lacks workflow scope. The rejected original commit
is preserved locally; see the validation receipt before changing CI or
claiming that the hosted timeout was repaired.

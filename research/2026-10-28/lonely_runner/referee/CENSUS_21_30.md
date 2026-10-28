# Complete two-entry census extended through n=30

**Result.** For every integer `21<=n<=30`, every pair of distinct removed
speeds `1<=r1<r2<=n-1`, and every pair of inserted integers `n<=w1<w2`,
the unshifted set `([n-1] minus {r1,r2}) union {w1,w2}` has loneliness
strictly greater than `1/n`. No speed cutoff or gcd-one assumption is imposed
in this statement. This exact finite classification uses the proved Gamma
bound and the pruning lemmas below; it is not a full Lean-kernel census.

## Additional exact pruning, proved before execution

Let S be the retained baseline speeds and let J be a nonempty component of
their uncovered region at radius `1/n`. Write ell=|J|. If two insertions cover
J, the sharp periodic occupancy bound gives

\[
 \ell\le\frac{4\ell}{n}
 +\frac{2(n-2)}{n^2}\left(\frac1{w_1}+\frac1{w_2}\right)
 <\frac{4\ell}{n}+\frac{4(n-2)}{n^2w_1}.
\]

Since n>4, every candidate obeys the strict bound

\[
 w_1<\frac{4(n-2)}{n(n-4)\ell}.
\tag{R1}
\]

Use the longest exact baseline gap and intersect this bound with Gamma's
parameter-dependent first-speed bound. Integer conversion is `ceil(B)-1`,
including when B is integral. Whole excluded first-speed ranges are counted
as rejected Gamma-domain quadruples, not silently removed from the domain.

The retained baseline gaps are computed once per deletion pair. For a first
insertion w1, its uncovered intervals are exactly

\[
 \left(\frac{nk+1}{nw_1},\frac{n(k+1)-1}{nw_1}\right),
 \qquad0\le k<w_1.
\]

Intersect these with each baseline gap on a common integer denominator.
Only periods meeting that gap need be generated. Intersections with equal
endpoints are empty; nonempty intersections are the exact open residual
components. This avoids rebuilding and sorting every retained source band
for every w1 without changing the mathematical residual region.

There is also a valid center filter for arbitrary deleted pairs. If a removed
r has no retained multiple, then at t=1/r all retained speeds lie farther
than 1/n from an integer. If r does not divide w1, a cover requires r to
divide w2. Thus w2 must be a multiple of the least common multiple of all
such r not dividing w1. The empty least common multiple is 1. This permits
one inserted speed to cover both centers and includes lower-half pairs such
as deleted r,2r. It does not impose the invalid distinct-assignment condition.

For the remaining second speeds, the existing maximum-residual-gap width
bound and exact closed single-band criterion decide full coverage. Every
quadruple in the original Gamma domain is accounted for exactly once as
first-speed occupancy rejection, residual-width rejection, center rejection,
or an individually tested source.

## Executed result and independent verification

The original Gamma domains contain **923,839,088** quadruples and 211,570
first-speed rows. Bound (R1) reduces the latter to **48,534**, with complete
accounting. The integer implementation individually tests **16,372** sources.
A separate implementation imports no SUCC search, witness, or verifier module:
it constructs baseline bands using Fraction, subtracts actual closed source
bands for both insertions, and recomputes the classical deletion formula.
It deliberately omits the center and single-band-winding filters and performs
**39,276** exact Fraction cover checks. Both classifications are empty.

| n | Original Gamma domain | Retained first speeds | Integer gap tests | Fraction cover checks | Covers |
|---|---:|---:|---:|---:|---:|
|21|29,327,142|2,790|1,141|2,315|0|
|22|35,609,279|2,865|835|1,978|0|
|23|45,340,877|3,254|850|1,913|0|
|24|58,767,165|4,086|1,529|3,834|0|
|25|72,566,355|4,391|1,523|3,410|0|
|26|90,783,329|5,168|1,847|4,548|0|
|27|111,840,348|5,665|2,016|4,503|0|
|28|130,705,791|6,121|1,871|4,965|0|
|29|157,640,945|6,471|2,025|4,688|0|
|30|191,257,857|7,723|2,735|7,122|0|

The sequential run took 64.56 seconds for the two census paths, with one
worker pinned to one CPU and peak RSS 38,128 KiB. Timing and resource use
are observations, not deterministic mathematical receipt fields. The
implementations share the proved bounds and mathematical source, so their
agreement is not two independent proofs of Gamma or (R1).

## Required positive controls and exact sources

Full Fraction band unions independently verify the known sources at n=5,
n=8, n=74 and n=284. At each, t=1/n attains minimum distance exactly 1/n,
so the upper cover and lower witness establish equality. In particular:

* n=74 removes 70,72 and inserts 140,144.
* n=284 removes 280,282 and inserts 560,564.

For both large controls the exact individual Goddyn-Wong windows also pass:
r=n-4 is checked against 4,5,6,7, and r=n-2 against 2,3. Tests additionally
pass these controls through every new pruning stage, including (R1), the
integer residual intersection, width cap, center modulus, and all gap tests.

The original n=74 example and simultaneous-acceleration theorem appear in
[Goddyn and Wong, *Tight Instances of the Lonely Runner* (2006)](https://zenodo.org/records/8275490),
PDF page 7, Section 3 and Theorem 3.1. The downloaded PDF has SHA256
`dc9b2a9a8fd9849ee5f05664b83899df83b8ab23a622300625e50465cf463197`.
The n=74 and n=284 members are both explicitly identified in
[Zhang v3, Example 5.2](https://arxiv.org/html/2608.13599v3#S5),
as the first two cases of n=74 mod 210. These are prior-art positive controls,
not new discoveries. No novelty is claimed for the census without further
priority review.

## Files, replay, and limits

New files only; the original census modules remain unchanged:

* `observational_succ/lonely_runner_referee_census.py` — integer implementation.
* `scripts/lonely_runner_referee_fraction.py` — independent Fraction path.
* `scripts/lonely_runner_referee_census.py` — sequential replay and receipts.
* `tests/test_lonely_runner_referee_census.py` — regression and hostile controls.
* `referee/receipts/census-21-30/` — all per-size receipts, raw log and summary.

The twenty per-size census/Fraction JSON receipts are stored as deterministic
gzip with mtime zero and no embedded filename. They contain 10,887,517 raw
bytes and occupy 517,480 compressed bytes. `receipts-index.json` records each
raw-byte SHA256, compressed SHA256, both lengths and the exact filename map.
Byte-identical raw originals were preserved outside the worktree at
`/media/leah/SPANKBANK/SUCCYBOI/lonely-referee-validation/census-raw/` before
removing only the newly generated untracked raw copies from this worktree.
No prior archival receipt was rewritten or removed.

Verify stored byte integrity with
`python scripts/lonely_runner_referee_receipts.py --verify research/2026-10-28/lonely_runner/referee/receipts/census-21-30`.
For independent replay comparison, regenerate raw JSON into a fresh directory
and compare each file's bytes with `gzip.decompress` of the mapped stored file;
do not compare compressed bytes generated by a different compression tool.

Run `python -m unittest discover -s tests -p 'test_lonely_runner_referee_census.py' -v`.
Replay into a fresh output directory with
`python scripts/lonely_runner_referee_census.py --min-n 21 --max-n 30 --output /tmp/succ-census-referee-replay`.

The first-speed occupancy pruning is independently recomputed in both paths,
but its proof is shared and written above. Neither an insufficient budget nor
a partial run returns a complete summary. The result is restricted to the
stated n range and the original zero-shift source; no general Lonely Runner,
shifted-normality, or full-census kernel conclusion follows.

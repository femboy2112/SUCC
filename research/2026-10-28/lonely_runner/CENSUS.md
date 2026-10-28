# Complete two-entry classifications for 5 <= n <= 20

Status: exact finite classifications, conditional only on the paper lemmas
proved in [GAMMA.md](GAMMA.md), with independently checked full-cover
certificates and exact max-min evaluations for every positive result. No
full-census Lean-kernel claim and no academic-novelty claim are made.

## CENSUS-01: statement and exact source

For every integer `5 <= n <= 20`, every `1 <= r1 < r2 <= n-1`, and every
pair of positive integers `n <= w1 < w2`, set

\[
S=[n-1]\setminus\{r_1,r_2\},\qquad V=S\cup\{w_1,w_2\},
\quad L(V)=\max_{t\in[0,1]}\min_{v\in V}\|vt\|.
\]

Then `L(V) <= 1/n` if and only if one of these two cases holds:

| n | Removed | Inserted | Actual speeds | Exact L |
|---|---|---|---|---|
| 5 | 1, 3 | 6, 8 | 2, 4, 6, 8 | 1/5 |
| 8 | 2, 3 | 11, 13 | 1, 4, 5, 6, 7, 11, 13 | 1/8 |

Both examples are known. For every other source in this quantified family,
`L(V)>1/n`. There is no imposed upper cutoff on inserted speeds in this
statement. All shifts are zero; no gcd normalization is performed. In
particular, the `n=5` example has gcd 2 and must survive.

This is a restricted finite-parameter classification, not the general
Lonely Runner conjecture and not a claim about shifted configurations.

## CENSUS-02: complete finite reduction

Let `mu=max(L([n-1] minus {r1}), L([n-1] minus {r2}))`, using the exact
classical deletion values established in Alpha. GAMMA-05 proves that every
source satisfying `L(V)<=1/n` has

\[
w_1<B=\frac{2(n-2)(n-1)}{n(n-4)(\mu-1/n)},\qquad
w_2\le 2(n-1)w_1.
\]

Thus the complete first-speed range is `n <= w1 <= ceil(B)-1`. For each
such `w1`, the complete preliminary second-speed range is
`w1+1 <= w2 <= 2(n-1)*w1`. These are theorem-derived ranges. A resource
budget exceeding neither range is not substituted for this conclusion:
the implementation checks its budget before enumeration and raises on an
insufficient budget, returning no `complete` receipt.

The dependency on Gamma includes its general one-insertion-hole theorem,
whose paper proof uses the precise cover form of Zhang's one-entry
classification. This dependency is explicit; neither floating experiments
nor the finite census independently prove that universal source lemma.

## CENSUS-03: exact residual gap rejection

For a positive integer speed `v`, write

\[
B_v=\bigcup_{k=0}^v
\left[\frac{nk-1}{nv},\frac{nk+1}{nv}\right]\cap[0,1].
\]

After fixing `w1`, the residual region is the complement in `[0,1]` of
the finite closed union over `v in S union {w1}`. Zero and one lie in
that union. Its complement is therefore a finite union of disjoint open
intervals `(a,b)`, all with rational endpoints. Gamma proves that there is
at least one such interval; an empty list causes an explicit contradiction
error in the census, rather than a vacuous acceptance.

The new gap implementation uses the common **integer** denominator
`D=n*lcm(S union {w1})`. Every source-band endpoint is an integer on this
grid: `(nk +/- 1)*D/(nv)`. Sort these integer endpoint pairs, clip to
`[0,D]`, and advance the rightmost covered frontier. A gap is emitted
exactly when the next left endpoint is strictly greater than that
frontier. The sweep invariant is that all processed intervals have been
accounted for, with exactly the emitted gaps before the frontier. Equal
endpoints overlap and never create a gap. Dividing the emitted endpoints
by `D` yields the exact residual components.

For any residual component `(a,b)`, the closed bad bands of `w2` are
separated by positive gaps because `n>=3`. Consequently a connected open
interval can be covered by their union if and only if it lies in a single
closed band. Closure then gives the exact equivalence

\[
(a,b)\subseteq B_{w_2}
\iff \exists k\in\mathbb Z:
w_2b-1/n\le k\le w_2a+1/n
\iff
\left\lceil w_2b-1/n\right\rceil
\le\left\lfloor w_2a+1/n\right\rfloor.
\]

The same `k` need not work for different components. The implementation
checks this integer inequality on **every** component. Since its endpoints
were already covered by the original source union, satisfying all these
tests is equivalent to a full cover of `[0,1]`. A failed component is a
proved source-specific rejection, independent of whether a certificate
generator could find a chain.

In particular, each component requires `w2*(b-a)<=2/n`. Let
`ell=max(b-a)` over all residual gaps. Then every possible cover obeys

\[
w_2\le\left\lfloor\frac{2}{n\ell}\right\rfloor.
\]

This width test rejects an entire finite interval of second speeds at
once. It does not sample those speeds. The remaining candidates undergo
the exact ceiling/floor test. Equality in either bound is retained.
These facts prove that the algorithm accepts exactly the configurations
with `L(V)<=1/n` in the complete Gamma domain.

## Executed classification and independent positive evidence

The full run for `5<=n<=20` took 17.19 seconds in the local environment.
Timing is descriptive execution evidence, not a theorem or a deterministic
receipt field. The complete preliminary domains contain 79,648,374
parameter quadruples. Exact maximum-gap widths reject 79,640,143 of them;
the remaining 8,231 receive individual exact gap tests, accepting two.

| n | Deletion pairs | First speeds | Proved finite domain | Width rejects | Individual gap tests | Covers |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 6 | 206 | 32,410 | 32,400 | 10 | 1 |
| 6 | 10 | 244 | 45,666 | 45,641 | 25 | 0 |
| 7 | 15 | 396 | 92,499 | 92,464 | 35 | 0 |
| 8 | 21 | 531 | 158,145 | 158,026 | 119 | 1 |
| 9 | 28 | 846 | 339,780 | 339,635 | 145 | 0 |
| 10 | 36 | 1,071 | 520,455 | 520,325 | 130 | 0 |
| 11 | 45 | 1,478 | 870,219 | 870,047 | 172 | 0 |
| 12 | 55 | 1,929 | 1,389,066 | 1,388,756 | 310 | 0 |
| 13 | 66 | 2,470 | 2,096,542 | 2,096,297 | 245 | 0 |
| 14 | 78 | 3,199 | 3,475,000 | 3,474,286 | 714 | 0 |
| 15 | 91 | 4,120 | 5,064,147 | 5,063,416 | 731 | 0 |
| 16 | 105 | 4,634 | 6,292,507 | 6,291,801 | 706 | 0 |
| 17 | 120 | 5,684 | 8,845,323 | 8,844,739 | 584 | 0 |
| 18 | 136 | 6,842 | 12,225,840 | 12,224,793 | 1,047 | 0 |
| 19 | 153 | 8,070 | 16,182,075 | 16,181,097 | 978 | 0 |
| 20 | 171 | 9,624 | 22,018,700 | 22,016,420 | 2,280 | 0 |

Every accepted source is independently reconstructed by
`lonely_runner_search.cover_certificate`, then accepted by the separate
integer-pair checker `lonely_runner_verify.verify_cover` with
`require_counterexample=False`. Its exact max-min value is separately
evaluated by the complete pair-breakpoint algorithm in
[CERTIFICATE_THEOREM.md](CERTIFICATE_THEOREM.md). In particular, acceptance
as a cover does not get silently relabelled as equality. The program
records a smaller maximum as a distinct unexpected ordinary counterexample.
No such value occurred.

The `n=8` certificate has 27 checked source intervals; the separate maximum
evaluation checks 158 distinct rational candidates and attains `1/8` at
`t=1/8`. The accepted full certificate files are:

* `certificates/census-n5-r1-3-w6-8.json`, SHA256
  `412366d0338d9e98546ee0f2b2ee5268e51cbd4b1585a8a4c3380046c15f9440`;
* `certificates/census-n8-r2-3-w11-13.json`, SHA256
  `c06d55157c3d6bcb511854668351692dcf12b0417784049a134d2a3afb17777c`.

Each `receipts/census-nN.json` records all deletion pairs, their exact
parameter bounds, exact stage counts and accepted insertions. Its
per-deletion SHA256 commits to the complete rational first-speed transcript
(all residual gaps, width bounds and failed-component counts). A second
SHA256 commits to every individually tested quadruple and its first failed
gap index, or acceptance. Transcripts are reproducible from the source;
hashes are integrity commitments, not stand-alone mathematical proofs.
For `n=8`, the complete receipt SHA256 is
`52f0bef9510b37a6c3c391e282ab709ca5113ef9c301ecd18f8a9ed339cd7a10`.

## Countermodels, controls and limits

Nine focused unit tests pass. They compare **all 531** `n=8` residual gap
sets against the pre-existing independent Fraction sweep, and compare all
119 individually tested sources against that sweep applied to the complete
source including `w2`. Other controls are:

* a bad band exactly spanning a residual gap: changing closed inequalities
  to strict ones rejects a valid source;
* extending a band endpoint by `10^-40`: floating rounding hides a genuine
  uncovered region;
* a nonintegral width bound: replacing floor by ceiling admits an impossible
  speed; exact equality must still be allowed;
* `n=8, R={2,3}, W={8,10}`: checking only the first residual component
  manufactures a false cover; the complete gap list rejects it;
* the gcd-2 `n=5` positive: an unsolicited primitive-only restriction loses
  a real source in the stated domain;
* insufficient execution budget: raises before enumeration and cannot
  manufacture a complete negative result.

The gap sweep, generator, and checker are separate implementations with
shared mathematical provenance. Their agreement is not three unrelated
proofs, and same-model review is not an external independent witness.
The full classification is not yet formalized in Lean. Local replay is
not hosted-CI evidence. Claims outside `5<=n<=20` require their own complete
execution or further paper proof.

## Priority audit

The source [Zhang, arXiv:2608.13599v3](https://arxiv.org/html/2608.13599v3)
was consulted directly. Theorem 6.10 treats all deletion pairs for
`8<=n<=140` with `w2<=8n`; Theorem 6.4 treats `R={2,3}` for `8<=n<=18`
with inserted speeds at most `40n`. Table 1 includes the deeper `n=8`,
`R={2,3}`, `64<w2<=320` check. Those stated interfaces do not give the
present unrestricted-speed classification for every deletion pair.
The new contribution here is removal of that cutoff for the explicitly
executed range, using the proved Gamma finite reduction; the positive
examples themselves are classical. The accepted high-deletion
classification identified in [LITERATURE.md](LITERATURE.md) concerns only
`r1,r2>(n-1)/2` and cannot by its stated interface cover the `n=8` example.
This scoped comparison is not a claim that no other source proves the
same finite classifications. Academic priority remains unverified.

## Replay and next falsification

From the repository root, the following replay is read-only:

```sh
python -m unittest tests.test_lonely_runner_census -v
python scripts/lonely_runner_census.py --n 8 \
  --verify research/2026-10-28/lonely_runner/receipts/census-n8.json \
  --certificate-dir research/2026-10-28/lonely_runner/certificates
```

For each `N` from 5 through 20, use the same command with `--n N`, the
matching `census-nN.json`, and `--max-domain-candidates 25000000`. The
budget is sufficient for every committed case and does not change the
mathematical candidate set. `--output PATH` writes a fresh receipt;
omitting both output and verify prints it to stdout. Certificate output
is optional and explicitly directed by `--certificate-dir`; verify mode
compares these artifacts without writing.

Next falsification tests: independently port the complete residual-gap
criterion to another exact implementation; challenge the unrestricted
one-insertion-hole premise; or produce any nonlisted source in the stated
range with a full independently accepted `1/n` cover. A new run beyond
`n=20` must retain theorem-derived bounds and may not turn a resource
timeout into a negative classification.

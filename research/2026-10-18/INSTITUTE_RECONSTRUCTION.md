# Live research reconstruction — 2026-10-18

Authority: observed Git/GitHub snapshot, document comparison, and explicitly listed local reruns. This is not a blanket re-proof of the 25 research drafts.

## Checkout and authorization

Original checkout `/media/leah/SPANKBANK/SUCCYBOI/SUCC` was clean on `research/deepseek-pdq-megaswarm-2026-10-16` at `98f50bb`. It is preserved. Live default branch is `main@610efacf02556e1c5922bc5d4e87d0087f19b446`. This isolated worktree is `SUCC-institute`, branch `research/institute-nucleus-2026-10-18`, based directly on that default head. `AGENTS.md` requires non-main branches and draft PRs, authorizing this research submission. No merge, tag, release, license change or archival rewrite is performed.

## True commit ancestry

Every listed head has the same merge base with main: `610efacf02556e1c5922bc5d4e87d0087f19b446`. **None is an ancestor of main.** PR base labels and stale SHAs embedded in some PR bodies do not override the live head SHA below. New PR #177 was included because it materially supersedes the analytic frontier in the request.

| PR | Exact head | Nearest ancestor heads in this snapshot | CI at captured head |
|---|---|---|---|
| [#153](https://github.com/femboy2112/SUCC/pull/153) | `c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d` | main | 4 cancelled, 28 success |
| [#154](https://github.com/femboy2112/SUCC/pull/154) | `e9e09201b4414ed6e5e98183bde1b150ef74fdb2` | main | 2 cancelled, 24 success |
| [#155](https://github.com/femboy2112/SUCC/pull/155) | `1a84799575ca38a33ed552cf94a0850b5632525e` | #153 | 20 success |
| [#156](https://github.com/femboy2112/SUCC/pull/156) | `b49904ca529de4204e602c415842159fe7a3ebf6` | #154 | 26 success |
| [#157](https://github.com/femboy2112/SUCC/pull/157) | `1bcebd265ee78ae6faef5995467df6c1d85b42cf` | main | 26 success |
| [#158](https://github.com/femboy2112/SUCC/pull/158) | `a60e52a05459b619f2c8cbf557636f4a76b68e65` | #156 | 2 cancelled, 26 success |
| [#159](https://github.com/femboy2112/SUCC/pull/159) | `6c3f768de3cca5c494ec46681f8997b28e482608` | #158 | 2 cancelled, 30 success |
| [#160](https://github.com/femboy2112/SUCC/pull/160) | `b9bb7324e7e7ccbc51e6fe3c5af61d08e238911e` | #159 | 2 cancelled, 24 success |
| [#161](https://github.com/femboy2112/SUCC/pull/161) | `eb62620300add80f8b38ebf0f7cd54c2a3c5ae36` | #159 | 2 cancelled, 24 success |
| [#162](https://github.com/femboy2112/SUCC/pull/162) | `3512c24bd582f8572d98bc0728d2cf947b7e7d2f` | #157 | 2 cancelled, 24 success |
| [#163](https://github.com/femboy2112/SUCC/pull/163) | `f038076a377b8906789994524664023bc8dd871f` | #161 | 20 success |
| [#164](https://github.com/femboy2112/SUCC/pull/164) | `0fa1fb4e05acbed9bee48f865ddf7e9933f049dc` | #160 | 1 cancelled, 25 success |
| [#165](https://github.com/femboy2112/SUCC/pull/165) | `dea8b7f982fd3eb2361ccd5a12d360bcadfa3689` | #162 | 4 cancelled, 30 success |
| [#166](https://github.com/femboy2112/SUCC/pull/166) | `9b6833569d9baf8407faf8d5dff860bb0ff2e8de` | #165 | 2 cancelled, 24 success |
| [#167](https://github.com/femboy2112/SUCC/pull/167) | `e1b1676202410dc206791d693749f047a0fefeed` | #166 | 22 success |
| [#168](https://github.com/femboy2112/SUCC/pull/168) | `089467b38e5ae2f096dba49a91ab96e9ff48c671` | #164 | 2 cancelled, 24 success |
| [#169](https://github.com/femboy2112/SUCC/pull/169) | `64aa0810d9016c9c6948034d0543424f46db011e` | #153 | 2 cancelled, 24 success |
| [#170](https://github.com/femboy2112/SUCC/pull/170) | `d479e5007cb253facf77b6926547b2d490f21fd4` | #168 | 1 cancelled, 27 success |
| [#171](https://github.com/femboy2112/SUCC/pull/171) | `8c46cca801b57a6381dfac08e41731ca70d38904` | #170 | 2 cancelled, 26 success |
| [#172](https://github.com/femboy2112/SUCC/pull/172) | `793f559ecf4fee9c9b03b98020bb20e3d7e36f3e` | #169 | 2 cancelled, 24 success |
| [#173](https://github.com/femboy2112/SUCC/pull/173) | `a2ea6859416f0cb6a2939ec577453c6ea9227a84` | #165 | 24 success |
| [#174](https://github.com/femboy2112/SUCC/pull/174) | `6fb1dba87ed273350a636b14b248fccacfb88934` | #171 | 2 cancelled, 26 success |
| [#175](https://github.com/femboy2112/SUCC/pull/175) | `8216c6fc042704aecd5fb7872facd681216e4be7` | #172 | 2 cancelled, 24 success |
| [#176](https://github.com/femboy2112/SUCC/pull/176) | `a17197697c0ea0259592500b233419fbedf691cf` | #175 | 20 success |
| [#177](https://github.com/femboy2112/SUCC/pull/177) | `f309d9104ba480c1999c962af1df7c50f19e1bfe` | #174 | 2 unfinished, 24 success |

Raw metadata: [github_snapshot.json](institute/github_snapshot.json). Snapshot timestamp: `2026-10-18T22:47:19.176728+00:00`. Check records include exact `head_sha`, names, timestamps and URLs. Cancelled duplicate jobs remain cancelled. This snapshot is not a claim about future CI.

## Shared provenance and mathematical incompatibilities

- The three main lines are #153→#169→#172→#175→#176 (local traces); #157→#162→#165 with #166/#167 and #173 (clock reconstruction); and #154→#156→#158→#159, branching to #161/#163 and #160→#164→#168→#170→#171→#174→#177 (signed analysis). #155 branches from #153.
- #163 copies `observational_succ/piecewise_suzuki_integrator.py` from #155: both exact blobs are `0934eee9461fbae53c673bc1e1423aa129548b82`. This is a common source, not independent corroboration. Stable whole-commit patch-ID comparison found zero duplicate complete patches among the unmerged commit set; that does not rule out copied files or mathematical duplication.
- #157 requires a global rank-dilation/affine law to recover n^c; calibration fixes c only with an independently specified real Haar density. #162/#165 do not remove the universal prime-power/cofinality/source-access premises. Finite clocks cannot authenticate them.
- #169 distinguishes rational diagonal scaling (gauge) from a one-place idele and shows additive successor does not descend to the multiplicative adele quotient. Those carriers cannot be silently identified.
- #172 retains full prime towers: Boolean parity conjugation does not extend to the p² Möbius coefficient. #175 shows the prime actions are chain-nullhomotopic, so homology erases them; chain-level homotopy defects recover a prime-sector trace only after source weights are supplied.
- #176 positive Möbius projectors preserve finite arithmetic exclusion and Haar bulk counts, but character, conductor and identity-contact data remain non-identifiable from those projectors. The new atomic/Haar paper proves the stronger bounded-star-transport obstruction.
- #155/#163 and #168/#171/#174/#177 share the original signed Suzuki source, but differ in trial spaces, primitive domains, coercivity metrics and truncations. An H² zero-extension bound needs vanishing value AND derivative traces. K-relative domination cannot be used as an L² gap. The Gamma/Carleman and full-continuum dossier is audited separately below.
- Prime-sector equality on smooth compact tests does not establish the completed signed Weil distribution: Gamma, poles, conductor/character phase, half-density and identity contact must match on a common genuine test domain. No new global equality is claimed here.

## Source credentials and validation scope

The historical import manifest pins source commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a` in FuckingRH. The live verifier checks 72 entries: 55 namespace-translated modules and 17 byte-identical research archives. The original signed source `observational_succ/source_weil_hierarchy.py` retains Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. Newly authored files are separately SHA256-bound by the theorem registry.

Local baseline commands and exits are in `institute/receipts/`; the core Lean baseline checks the existing NoGhost theorem set with its false-proof control. The system Python environment had mpmath 1.2.1 below the declared >=1.3 floor, despite package metadata reporting 0.0.0. Final source replay and focused checks use `/tmp/succ-institute-venv/bin/python` with mpmath 1.3.0; no system package was replaced. The full baseline retains its actual environment rather than being relabelled.

Two metadata-collection setup errors were repaired: a trailing slash caused GitHub API 404, and installed gh 2.45 lacks `--slurp`; the collector now explicitly paginates. The captured failed receipt for the latter remains. No mathematical failure was hidden by the repair.

See [causal nucleus](INSTITUTE_CAUSAL_DESCENT.md), [atomic/Haar paper](INSTITUTE_ATOMIC_HAAR.md), [arithmetic and analytic audit](INSTITUTE_ARITHMETIC_ANALYSIS.md), and [hostile review](INSTITUTE_HOSTILE_AUDIT.md). **RH PROVED: NO.**

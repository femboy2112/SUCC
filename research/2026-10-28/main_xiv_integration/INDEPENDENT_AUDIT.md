# Main XIV independent audit and integration contract

Date: 2026-10-28. **Research-status only.** No main merge, release, or academic publication performed by this audit.

## 1. Recovered Git ancestry

Base main: **b763ba8ef375fbac221e29e4396989a635a6ef36**. Recheck live heads and merge bases before execution.

| Lane | Ancestry-minimal leaf and head | What it covers |
| --- | --- | --- |
| Lonely Runner | **#353** at 6174ad022a0dead14bc6a0a4d30ec41ac0ed6c99 | #351 → #353 |
| BBP/Pólya/observer | **#356** at b89fac9aff8bc0ef20dc0f1beda0020d0141701f | #344 → #346 → #347 → #348 → #349 → #352 → #354 → #355 → #356 |
| Wavefront sibling | **#345** at e2defca8b7741efe5aada9d9114a1cc89e0b6bf9 | Forks at #344; six unique files not in #356 leaf |
| Author provenance | **#350** at a1d01657356669ca141bab67b2fe146c6f0f9322 | Standalone single file |
| This audit / n=31 holdout | Research branch from main | Three additive files; no production changes |
| DeepSeek abc draft | 7c79883cdc5dc75812ce7ecc0f5f871785b57670 | **QUARANTINE** — refuted theorem and ineffective test |
| Stale prime-ladder | #334 → #337 | 188 commits behind main at inspection; refuted historical entropy bridge |

A full comparison of the two principal leaves with main found shared modifications in .github/workflows/ci.yml, docs/math_memory/CLAIM_CATALOG.json, docs/math_memory/INDEX.md, and docs/math_memory/TOPIC_ATLAS.md. The catalog contains large cache-related deletion and regeneration churn. Do not choose "ours" or "theirs" as a complete final index. Apply the .lake scanner exclusion once; merge the actual source files and claim supplements, regenerate the catalog from the final tree, and check all namespace/graph/source hashes. Do not drop existing CI commands when reconciling the 25→45 minute timeout.

The six unique files from sibling #345 versus shared ancestor #344 are:

- docs/CLAIM_SUPPLEMENT_WAVEFRONT_INFLATION_PRIOR.md
- handoffs/CLAUDE_WAVEFRONT_PRIOR_INFLATION_NEXT.md
- research/2026-10-28/WAVEFRONT_PRIOR_INFLATION_THEOREMS.md
- research/2026-10-28/WAVEFRONT_PRIOR_INFLATION_VALIDATION.md
- scripts/inflation_prior_minimal.py
- tests/test_wavefront_inflation_minimal.py

Other paths shared between the #345 and #356 comparison listings are inherited from the common #344 ancestry, not six-way source conflicts.

## 2. Lonely Runner evidence and scope

PR #353 claims the all-time unshifted two-entry theorem

\[
L(([n-1]\setminus\{r_1,r_2\})\cup\{w_1,w_2\})\le 1/n
\quad\Longrightarrow\quad
w_2<28n^2
\]

for integers \(n\ge5\), \(1\le r_1<r_2\le n-1\), \(n\le w_1<w_2\). Its manuscript reconstructs the dangerous one-insertion-hole argument directly from coverage, avoiding the parent #351 dependence on an equality-only reading of Zhang's classification. The unrestricted quadratic theorem remains a **paper proof** with external review and originality **UNVERIFIED**. Eighteen new Lean kernel exports prove a narrower *upper-half cubic theorem* and supporting finite-source geometry, not the unrestricted quadratic theorem; #351's 23 earlier exports remain distinct.

At the exact #353 head, seven hosted workflows completed successfully. Actual Python 3.10 and 3.13 job logs reported 9,486 native tests OK. The additional guarded Lean workflow reported 18 checked exports and three false-statement controls. The passing #353 jobs do not validate the untested #356 descendant.

### New independent exact finite holdout: n=31

A separate standard-library Fraction implementation in scripts/main_xiv_lonely_n31_probe.py was executed locally, without importing existing SUCC source or verifier modules. The **tested local Git blob is 2a65ed621b25c14116c430d01f21dc93d9b2d806**; GitHub's uploaded blob SHA was checked and matches.

The finite search domain is **conditional** on GAMMA-05's \(w_1<B_n\), \(w_2\le2(n-1)w_1\), the #353 longest-safe-gap occupancy pruning \(w_1<4(n-2)/[n(n-4)\ell]\), and the established no-one-insertion-cover premise. A removed speed with no retained multiple forces divisibility by at least one inserted speed (evaluate \(t=1/r\)); every residual open gap must fit inside one closed band of \(w_2\).

The verifier uses exact rational endpoints and checks each residual gap \((a,b)\) by the necessary-and-sufficient criterion
\[
\left\lceil w_2 b-1/n\right\rceil\le
\left\lfloor w_2 a+1/n\right\rfloor.
\]
With the --dual option a separate *complete full-source closed-band union* is recomputed for every remaining individual candidate and agreement is asserted.

**Executed results:**

| n | Deleted-speed pairs | Retained first-speed rows | Full independent candidate checks | Accepted |
| --- | ---: | ---: | ---: | --- |
| 5 | 6 | 67 | 9 | removed {1,3}, inserted {6,8} |
| 8 | 21 | 170 | 73 | removed {2,3}, inserted {11,13} |
| 29 | 378 | 6,471 | 2,025 | none |
| 30 | 406 | 7,723 | 2,735 | none |
| **31** | **435** | **7,925** | **2,651** | **none** |

The n=29 and n=30 row/check counts precisely reproduce #353's published receipts. Also checked the full-circle positive controls n=74 (remove 70,72; insert 140,144) and n=284 (remove 280,282; insert 560,564). Both cover. Stable observations and source hash are pinned in research/2026-10-28/main_xiv_integration/N31_EXACT_HOLDOUT_RECEIPT.json.

**Verdict:** a new finite **conditional** classification at n=31. Not a kernel-proved universal bound, not a full-suite or hosted CI pass on this audit branch, not a shifted-runner result, and not an external novelty claim. Replay independently: python scripts/main_xiv_lonely_n31_probe.py --dual 5 8 29 30 31.

## 3. DeepSeek: decisive claims must not enter main

The unmerged branch research/deepseek-primitive-abc-effective-2026-10-28 at **7c79883cdc5dc75812ce7ecc0f5f871785b57670** asserts for pairwise-coprime d,e,f and D=def an effective count
\[
|N_X(d,e,f)-\rho_D X^2|\le X\tau(D)+D
\qquad\text{for every real }X\ge1.
\]

**REFUTED AS STATED.** Put d=e=f=1. For integer X≥2,
\(N_X(1,1,1)=\sum_{m\le X}\varphi(m)-1\).
The proposed uniform estimate implies
\[
\left|\sum_{m\le X}\varphi(m)-3X^2/\pi^2\right|\le X+2.
\]
Montgomery's theorem gives oscillation \(\Omega_\pm(X\sqrt{\log\log X})\) for the totient summatory error, contradicting any global \(O(X)\) inequality. Citation: H. L. Montgomery, *Fluctuations in the mean of Euler's phi function*, Proc. Indian Acad. Sci. Math. Sci. 97 (1987), 239–245, DOI 10.1007/BF02837826. Bibliography verified via https://public.websites.umich.edu/~hlm/rpubs.html. We did not locate an explicit small-X numerical violation in this audit; the published oscillation theorem is the decisive universal counterargument.

The branch's test rounds a floating-point approximation to \(\pi^2/3\) and then verifies a weaker \(4B+1\) inequality rather than the claimed \(B\) bound. This is neither exact nor a test of the actual assertion. The note's statement that the q=1 unrestricted Möbius term already carries the primitive \(1/\zeta(2)\) density is incorrect; the full Möbius inversion supplies that factor.

**Additional incorrect witness:** the branch argues that after deleting r every retained speed lies below 2r. For lower-half r this is false: n=8, deletions {2,3}, insertion 11, t=1/2 retains speed 4, for which \(\|4t\|=0\). This refutes the proposed particular witness, not Codex's complete one-insertion-hole theorem.

**Additional false asymptotic inference:** for \(0\le t<s<2/3\), the already-proved SUCC moment bound \(S_s(X)\le K_sX^2\) yields
\[
X^{-2}\sum_{\operatorname{ris}(abc)>X}\operatorname{ris}(abc)^t
\le K_s X^{-(s-t)}\to0.
\]
Thus the DeepSeek note's sampled high-ris ratios cannot support an asymptotically nonvanishing contribution. SUCC's effective abc mean theorem was also **already merged in PR #212**: power saving for \(0\le t<2/3\) and \(0<\delta<(2-3t)/5\). The endpoint t=2/3 remains open. Preserve the refutation here; **do not import the branch's three files, status claims, or tests**.

## 4. Remaining integration gates

- Never rewrite archived originals, authenticated four-pole forcing, the zero seed, historical theorem IDs, or existing published receipts.
- Merge ancestry-minimal leaves on a new integration branch, retaining their separate histories and source labels; inspect apparent collisions rather than bulk resolving generated files.
- PR #345 is a true sibling with six unique files. PR #334/#337 are stale; do not restore their refuted transcendence→entropy bridge. Salvage specific corrective evidence only by careful cherry-pick and explicit REFUTED labels.
- The later #352–#356 commits contain [skip ci] and have not earned hosted integration authority. Run the entire Python/Lean/source validation matrix on the eventual combined tree; prior PR workflows are not inherited successes.
- Run the mandatory AGENTS.md commands, math-memory catalog rebuild/check, claim registry, graph lints, independent exact certificates, original BBP source pins, and all applicable hosted CI on the final commit.
- Status firewall: π base-16/base-3 normality, RH, general Collatz, and shifted Lonely Runner n=18..94 remain OPEN. The quadratic growth theorem remains paper-level until actually formalized and independently reviewed; academic priority UNVERIFIED.
- Review the PDF manuscript visually if preparing a publication artifact. Do not publish, release, force-push, delete branches, or contact outside scholars without separate authorization.

**Main XIV success definition:** integrated source-faithful research with a passing final-tree validation matrix, correct paper/Lean/finite-status labels, preserved provenance and negative controls, and an exact merge/holdout ledger. Integration is not an academic novelty certificate.

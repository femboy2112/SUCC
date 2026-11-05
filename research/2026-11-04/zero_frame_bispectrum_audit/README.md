# Independent post-Codex audit: where the two-clock coupling route stands

**Source pinned:** draft [#507](https://github.com/femboy2112/SUCC/pull/507), exact head \`c49cc0951981883c8f9a66e3b9c27be18c4fd4b1\`; earlier #506, #504, #505 are properly attributed source/context, NOT independent stochastic evidence. This add-only audit branch changes no canonical source files or frozen contracts. π normality OPEN.

## Findings supported by #507

1. The canonical all-order radial jet is not a convergent fixed infinite-time operator. For fixed n it diverges with m, while joint order m=n yields exponentially small source defect; **the two limits do not commute**. Paper proofs, no external referee.
2. A time-varying exponentially accurate compensating multiplier has total variation Θ(Λ), and its universal maximal-sum multiplier norm has order Θ(Λ). This blocks the simple arbitrary-data transfer but leaves open estimates on the genuine zero-seeded angular stream.
3. The coupled lag family satisfies a square-sum/Bessel bound and has one small lag among sufficiently many, but the Gram of lagged columns cancels the angular factor. Its column-dependent inverse gauge is rank one. **Lag-zero remains unselected**.
4. Reciprocal time-weighting can be inverted at constant cost on **maximal** interval norms. The previous tuned zero applied only to a full-window scalar and cannot be promoted to all subintervals.
5. The exact carry word identifies the initial seed to 16^-N, but no signed count of original realized carry cylinders was proved. The same-forcing coherent counterseed invalidates mean-product factorization; the #505 normal counterseeds demonstrate that the critical ratchet is only a *sufficient*, not *necessary*, normality criterion.
6. Independent checks for this audit: rederived the first four radial source-jet coefficients (15/2, 421/32, 4551/256, 179123/8192) from the exact algebraic generator with SymPy; independently constructed and ran five exact/finite tests for the nonlinear two-clock character at A=128,256,512 (5/5 PASS), with the **exact Git blob SHA identical** to the source executed locally. The finite phase check is numerical after exact rational phase reduction; the all-n error estimate is paper mathematics based on inherited source curvature. No new full/native/hosted CI claimed.

## New source-compatible nonlinear observer to investigate

The third-order delayed-frame character
\[
v_1(n;H)^2\overline{v_2(n;H)}
=e(HU_n)e(-H\Delta^2Z_n)
\]
retains the source angular character, whereas the usual two-column Gram removes it. Genuine radial curvature \`0<z''(x)<=1/(8x^3)\` for x>=128 yields an explicit error at critical depth:
\[
\sup_I A^{-1}\left|\sum_I[v_1^2\bar v_2-e(HU_n)]\right|
\le \pi\Lambda/(4A)=o(1/\log A).
\]
This bypasses the particular **Y-blind Gram representation** and the generic \`Θ(Λ)\` linear multiplier inversion cost at the level of source reconstruction; it does **not** establish signed cancellation or defeat same-forcing coherent counterseeds. A new *source-selected trilinear/carry inequality* is necessary. Full algebra and scope: [PROOFS.md](PROOFS.md).

## A weaker, still-unproved sufficient carry-correlation hypothesis

The published #507 NEXT.md asks for \`K=O_h(log^-3 A)\` at \`D~log³ A\`. A smaller result would already suffice:
\[
D_A/\Lambda_A^2\to\infty,\quad D_A=o(A),\qquad
\sup_I\max(0,K_{A,D_A}(I))=o_h(\Lambda_A^{-2}).
\]
For example \`D_A=ceil(log² A log log A)\`. This follows **exactly** from #507's classical van der Corput inequality; it is NOT a theorem that the genuine source satisfies the stated hypothesis. The coherent wrong seed has K tending to 1/2 and fails. This refined mathematical target may avoid proving more than needed but is still a hard original-source signed-carry statement.

## Priorities for next mathematical campaign

**A — source-selected trilinear correlation, not Gram-only:** derive genuine arithmetic restrictions on \`A^-1 sum_I v_1² conjugate(v_2)\` or on higher source-covariant odd-degree tensors. An algebraic near-identity is not enough. Test coherent seed \`s*=-π/16\`, rational seed 1/5, radial-only source and #505 ternary mutant. The new inequality must identify which original seed/carry condition does the work.

**B — quantitative realized carry-cell sieve:** work directly with the authenticated \`x_(n+d)=16^d x_n+S_d(n)-K_d(n)\`, preserving signed (not just absolute) cell visits. Establish a cancellation rate at the selected zero-seed path; source-identification from complete carries is not a substitute.

**C — run a direct fixed-h Weyl alternative:** the stringent critical ratchet is sufficient but not necessary. Consider whether exact source period/prime constraints yield \`A^-1 sum_{n=A}^{2A}e(hU_n)=o_h(1)\` by a different route. Do not silently replace the unique zero boundary by ensemble averages.

**D — genuine double-clock mixed frames:** test p-class, radix-adic, and real-circle observers jointly only after defining a common transport. Preserve original time ordering and source dependencies; independent marginals do not imply mixing.

## Verdict

The program has **stronger diagnostics, sharper obstructions, and better source fidelity**, not yet a demonstrated normality proof. The primary block is a signed quantitative assertion about the **actual source-selected real numerators and carry-cell visits**. Every proposed shortcut still needs to exclude the coherent wrong seed. Literature: Bailey–Crandall (Experimental Mathematics 10 (2001), DOI 10.1080/10586458.2001.10504441) is conditional on dynamical distribution; Lagarias (Experimental Mathematics 10 (2001), DOI 10.1080/10586458.2001.10504456) warns that shadowing identities apply even when the desired distribution conclusion fails.

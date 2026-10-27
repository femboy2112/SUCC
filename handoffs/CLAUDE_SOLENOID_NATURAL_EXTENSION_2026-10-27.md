# Claude / Codex handoff: ∞-root solenoid natural extension and selected π gate

**2026-10-27. Research branch built from #328 pinned 68c00f5eee86c215dd09271b35b0647a5b56f16e, NOT main.** Read the new full proof dossier and claim supplement before editing. Review original PR #320 §6 (circle-Haar counterexample with independently chosen odd-torsion lifts), #321 (time odometer), #323–#324 (signed π tail), and #328 (source complements). Keep source/archives/zero boundary immutable; no merge/release without fresh authorization.

## Findings to independently audit

1. Do not call z↦16z on Z₂ an odometer. Its contracting real/adic counterpart is repaired by the solenoid automorphism on (R×Z₂)/{(m,−m)}. Formula: (x,z)↦({16x},16z+floor16x). Inverse uses d=z mod16. That adic fiber **remembers digits**; the source-time clock is a distinct Z₂ observable.
2. For a *single coherent T orbit* (rather than arbitrary independently lifted circle points), solenoid Haar-genericity is equivalent to circle base-16 normality. The #320 counterexample remains valid for arbitrary lifts.
3. The source-selected rational real winding lifts j_R(U_n) shadow T^(n−1)j_R(π) because the inherited Green tail is summable. Exact fixed character discrepancy ≤2π abs(m)B/(16^k N). This is a transport identity, not a new signed Weyl saving.
4. The genuine missing 2-adic→real character factor is the odd denominator: u=A/B, q=16^k, R=A/B mod q, K=(BR−A)/q, and e(hu/q)=e(hR/q)e(−hK/B). Test 32/3 against 0 and all original four-pole states, not the residue factor alone.
5. A Haar-preserving **equivariant** measurable factor from the Haar adding machine onto the Haar solenoid is impossible: odometer rigidity versus solenoid Haar mixing. A continuous time-to-winding archive for irrational α is likewise impossible. This does not forbid a selected nonautonomous BBP source argument.
6. A mode with conductor depth k=N has Cesàro mean tending to **one**, even for normal α. Never assert uniform-in-growing-depth Weyl cancellation.

## Execution and next proof work

Run python scripts/solenoid_digit_bridge_probe.py and python -m unittest discover -s tests -p test_solenoid_digit_bridge.py -v, then all AGENTS.md required repository checks and CI. Check native source import, compare branch ancestry and exact file contents, and keep failed gates visible. The uploaded new Python files are local hash-verified; independent native hosted tests have not been claimed.

Priority mathematical probe: a genuinely **source-specific, signed** estimate coupling the residue and complementary odd-denominator characters for U_n from the original signed four poles and U_0=0, possibly using 3/5/7 prime-source clocks. Must distinguish the zero selector from #320 nonnormal mutant and the source-preserving V_n=−T_n selector. Predeclare a quantitative nontrivial saving and holdouts. Do not mistake normality-equivalent character reformulations for a proof. π normality and RH remain OPEN.

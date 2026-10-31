# SUCC: Pascal 2↔3 carrier, source-conditioned measure transport, and Pisot algebra

**2026-10-31. Draft research, stacked on SUCC PR #427 at exact head 8558a95.** π normality, RH, selected ×3 invariance and Furstenberg's zero-entropy conjecture remain OPEN.

The author's proposal asks whether \(3=2+1\), Pascal triangles and Pisot recursion can make the 2-adic and 3-adic carrier dynamics equivalent up to parameterization. **Answer: yes for specified dynamical systems, no for arithmetic groups or canonical Haar statistics.** We construct a fully explicit reversible binary/ternary prefix code giving a homeomorphism \(H:Z₂→Z₃\) with \(H(2x+1)=3H(x)\). It has exact finite modulus certificates and a provable non-Haar pushforward.

**Distinct achievements:**

- CP-01/02: exact Pascal binomial transform \(B(2^n)=3^n\), signed inverse, 2-adic interpolation of \(3^x\) and 3-adic interpolation of \(16^x\), with a counterexample to 3-adically extending \(2^x\).
- CP-03/04: constructive topological conjugacy of the affine 2-adic contraction with the ternary contraction; NO nontrivial continuous additive group map \(Z₂→Z₃\), NO layer-preserving ring equivalence.
- CP-05/06B: the conjugacy cannot preserve additive Haar. The explicit code produces ternary tail probabilities (1/4,1/4,1/2); its count of one-bit codewords has **exact Pascal probability** \(C(m,k)2^{-m}\), versus native ternary Haar \(C(m,k)(1/3)^k(2/3)^{m-k}\). This count captures ALL conditional-tail KL discrepancy exactly; information is conserved per consumed binary bit.
- **CP-10: original zero-selected BBP realization**. Using inherited DSI-4 (exact \(U_n\bmod2^a\) permutations), the transported \(H(U_n)\bmod3^b\) has a genuinely source-certified but NON-Haar ternary law on every complete period. Mod3 distribution is exactly (1/2,1/4,1/4). Its joint distribution with the authentic \(16^n\bmod3^b\) clock factorizes exactly by CRT. Conditioned on the 2-adic unit shell, the original source itself realizes every Pascal codeword-count distribution exactly at finite levels.
- CP-07/08: SUCC already contains PIS-10, the classical theorem that every real number field has a Pisot(-unit) generator; Schmidt 1980 gives eventually periodic Pisot-base expansions for its algebraic members. Explicit β=2+√2 is Pisot while β+1=3+√2 is not: **Pascal shifting does not always preserve the Pisot condition**.
- CP-09: RH/π normality does not follow from any of these source-correct local transformations; the selected Archimedean ×16/×3 phase remains a distinct theorem obligation.

The work is carefully compared with inherited SUCC PIS-01..14 and PR #427; no prior mathematical result is relabeled new. See [full proof](PROOF.md), [claims](CLAIMS.md), [validation](VALIDATION.md), [next source bridge](NEXT.md), [Fraction-only implementation](pascal_crossprime.py), and the root regression test tests/test_pascal_crossprime_conjugacy.py.

**Source firewall:** New additive research files and one discoverable regression only. Original signed four-pole BBP forcing, U₀=0, archived sources, production, formal, workflows, canonical claims, main, and both parent research PRs unchanged. No merge, publication, release, or priority assertion.
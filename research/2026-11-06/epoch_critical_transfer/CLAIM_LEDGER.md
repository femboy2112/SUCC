# Claim ledger — epoch-critical Fejér source transport

| Claim | Status | Test / boundary |
|---|---|---|
| ET-01 | PROVED LOCAL | Unconditional original-zero BBP norm transport for late epochs, explicit pi/(15A²) sqrt(H(H+1)(H+2)/6), O(A^-1/2) at H=A; rational source tail and exact weighted sum proof. |
| ET-02 | PROVED LOCAL | Completed ×16 epoch Fourier ray shift <=2/A, frequency-ray estimate ET2b. Requires expanding orbit, not generic point array. |
| ET-03 | PROVED CONDITIONAL / OPEN PREMISE | C_(A,A)(x)=o(log A) at all sufficiently large A, or relative-dense A_j, implies pi normality. No actual selected energy bound proved. |
| ET-04 | PROVED CONDITIONAL / OPEN PREMISE | All-radius all-epoch B_A(delta)<=A+K A²delta implies Fejér bounded energy and normality, K>=2. Holds for all reals delta in [1/(A+1),1/2] under stated hypothesis, not just a grid. |
| ET-05 | PROVED CONDITIONAL | Under the ET4 pair-count premise, moving from original rational phases to completed pi phases costs <=2K/15 extra in the pair-count upper budget. Source tail and circle triangle inequalities; no new mixing. |
| ET-06 | CERTIFIED FINITE | Complete all-radius exact jump-point K3 checks for A191 and A319 passed following GitHub prereg addendum c0c36518; earlier A16/32/64/128/256 exploratory only. No infinite extrapolation. |
| ET-07 | OBSERVED FINITE | Original critical epoch energies ~1.65..2.47 and tiny source norm shifts measured as ordinary floating-point diagnostics; not rigorous interval energy certificates. |
| ET-08 | EXACT HOSTILE CONTROLS | Constant phase, coherent beta=1/5 and nonnormal H-shadow do not satisfy energy/near-pair hypothesis; non-Haar half-circle grid has bounded finite Fejér energy but lacks ×16 orbit relation. |
| ET-09 | INHERITED / TYPED | PR #532 log den(U_n)>= (5-o(1))n improves #534 coefficient2, but does not by itself exclude real small gaps or prove normality. |
| ET-10 | OPEN | Genuine original-source zero-selected all-epoch real near-pair signed-carry bound, fixed-h Weyl decay, base16 pi normality and RH. |

**Adversarial failed attempt:** the first research-local red test reduced a negative tiny phase modulo 1 and then converted to float, obtaining rounded value 1.0. It was a badly designed test, repaired by exact Fraction equality, not a counterexample to source transport. An additional red test indexed one past the generated circular array; repaired by including time 2A. Both are preserved in INITIAL_RED_TEST_LOG.txt.

**Triangulation:** mathematical proofs are independent of the finite floating diagnostics; the combined-rational independent code uses the same BBP source genealogy and is not a blind outside referee. Source identity, numeral base, exact integer carry and original U0 remain frozen. Exact compatible real completion comes from inherited BBP identity. Stronger denominator theorem and other PRs are read-only inputs, not merged.

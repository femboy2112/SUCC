# Scope ledger: Operation DYADIC EXPOSURE

| ID | Claim | Status | Main proof or authority | Hostile check / boundary |
|---|---|---|---|---|
| DY-01 | eta(-m) in Z[1/2] via finite Stirling triangle, every m>=1 | DISCLOSED (elementary classical proof) | README §1; generating function + binomial basis | m=0 requires separate convention; no ordinary alternating-sum convergence for m>=1 |
| DY-02 | Odd denominator of zeta(1-2k) divides 2^(2k)-1 | DISCLOSED (exact consequence) | README §2, DY-01 and eta functional identity | p=17 at k=4, p=31 at k=5 exposed but absent |
| DY-03 | Each finite dyadic X_(k,R) is in Z[1/2] and tends in R to continued zeta | DISCLOSED | README §3, finite geometric sum | No assertion of p-adic convergence, independence of regularization, or physical construction |
| DY-04 | Same X_(k,R) not Cauchy in any Q_p | DISCLOSED | README §3, exact successive p-valuations | Misapplying real limit at prime places is refuted |
| DY-05 | Odd prime p first occurs at zeta(2-p), v_p=-1 | DISCLOSED (classical) | README §4, von Staudt–Clausen | Not a rule that all p in 2^(2k)-1 survive |
| DY-06 | Every zeta(1-2k) = (-1)^k Gamma(2k) lim N^-2k Tr((L_N^+)^k) | DISCLOSED (classical analytic synthesis) | README §5, spectrum + dominated convergence + reflection | Graph is a declared observer, not physical BBP curvature; k=1 is inherited #420 |
| DY-07 | Prime/Gamma/harmonic logarithmic-derivative identity | DISCLOSED (classical) | README §6, derivative of functional eq + positive Euler product | No convergent negative-side Euler product, no RH conclusion |
| DY-08 | 1+2+4+...=-1 only under a stated meromorphic/f.p. prescription | DISCLOSED (scoped) | README §7 | Starting at 2 gives -2, and ordinary series diverges |
| DY-09 | Pascal inverse central-binomial series computes zeta(2) | CORROBORATED (classical published identity) | DLMF 25.6.8, README §6 | Not a BBP π-digit Weyl estimate |
| DY-10 | Dyadic/Gamma/prime transport implies π normality or RH | UNVERIFIED / NOT CLAIMED | README §8 | Same-source nonnormal counterseed; #421 whole-polar-data shadow |

All local exact test outcomes are finite-scope **OBSERVED** and are separately recorded in VALIDATION.md. Algebraic proof labels do not mean Lean-verified, blind-reviewed, or novel mathematics. The only new-to-SUCC contribution claimed is the combined typed construction, exact interfaces and hostile completion tests, not mathematical priority.

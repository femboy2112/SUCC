# Independent finite diagnostics — tau saddle observer, 2026-11-05

All numerical data in this file are **finite diagnostics**. The sign holdouts, which are separately certified with exact Fraction intervals, were declared prospectively in PREREGISTRATION.md. The sharp n→∞ residual limit is established (within stated assumptions) by the analytic proof in PROOFS.md, not by these samples.

## Rational certified sign transitions

The original radial source moments \((1-E)^kZ_n\) have the exact identity
\[
I_k(n)=-\frac18\sum_{m\ge1}16^{-m}
             \sum_{j=1}^8w_{r,j}\,
              \mathrm B(n+m-1+j/8,k+1),
\]
and for rational a>0, integer k, \(\mathrm B(a,k+1)=k!/\prod_{\ell=0}^k(a+\ell)\in\mathbb Q\). The exact Fraction implementation truncates at m=24 and encloses its *entire omitted tail* using the decrease of B(a,k+1) with a, and \(\sum_{m>24}16^{-m}=16^{-24}/15\). Thus every reported sign is a rigorous rational inequality, not a decimal approximation.

| Source n | predicted real \(k_c\approx \alpha_*n+c_*\) | first negative integer k | status |
|---:|---:|---:|---|
| 1 | 53.422 | 57 | DEVELOPMENT exact |
| 2 | 124.547 | 126 | DEVELOPMENT exact |
| 3 | 195.672 | 197 | DEVELOPMENT exact |
| 5 | 337.922 | 339 | DEVELOPMENT exact |
| 7 | 480.172 | 481 | NEW preregistered exact |
| 11 | 764.672 | 765 | NEW preregistered exact |
| 13 | 906.922 | 908 | NEW preregistered exact |

The asymptotic offset only describes large n; the n=1 mismatch is expected and was not fitted away. Independent 85-digit moment probes at n=10,20,40,80 were developmental.

## Separate high-precision minimum-residual calibration

An independently coded 100-decimal-digit implementation expanded the authenticated algebraic source-jet coefficient generator via the positive power series \(v(s)=1-(1-s)^{1/8}\) and the rational functional equation for \(\mathcal A(s)\). It evaluated the radial moments through a separate \(\mathrm B(a,k+1)\) recurrence and 70 geometric tail terms, then formed the accumulated minimum \(\varepsilon_m(n)=r_o(n)-\sum_{k\le m}b_k I_k(n)\). This code path was constructed **after the original theorem conjecture and after initial preregistration** and is a development/calibration route, not a claimed blind holdout or certified interval arithmetic.

The analytic saddle prediction is \(C_*\tau^{8n}/\sqrt n\) with \(C_*\approx44.844291342999\).

| n | minimizing integer m | measured residual | saddle prediction | measured/predicted |
|---:|---:|---:|---:|---:|
| 1 | 56 | 2.5733362696372 | 0.62175840578322 | 4.138804 |
| 2 | 125 | 0.007232690375977 | 0.006095666067621 | 1.186530 |
| 3 | 196 | 0.00007416442803558 | 0.00006900650592786 | 1.074745 |
| 5 | 338 | 1.063348264813e-8 | 1.027530360860e-8 | 1.034858 |
| 7 | 480 | 1.709596467977e-12 | 1.669397062913e-12 | 1.024080 |
| 10 | 693 | 3.784969120666e-18 | 3.722649646523e-18 | 1.016741 |
| 12 | 836 | 6.623685241705e-22 | 6.532667316746e-22 | 1.013933 |

The differences shrink with n and provide a useful falsifier for algebraic sign/prefactor errors. These values **do not** by themselves certify a universal asymptotic. The local calibration script had SHA-256 \`089b34de6799da449e9c30f641af93e46ff43504b47fb4d81278d8545cdd15fb\`; it was run locally but was NOT committed as a verified script in this PR. Only the exact focused test source is committed and byte-verified.

**No source-selected original signed Weyl cancellation or π-normality theorem is inferred.**

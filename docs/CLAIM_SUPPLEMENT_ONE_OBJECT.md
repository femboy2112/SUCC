# ONE OBJECT source-gluing claim ledger — 2026-10-15

**Research branch:** research/one-object-tate-weil-suzuki-connes-2026-10-15, stacked on the Tate-source PR #103 at 940f0a47ef25b8b553c2f0b45032b37e68c23b02; pre-Phoenix main remains 03db44203147a7b28d445bb9f970fa71360e78c4. No academic novelty claim. **RH PROVED: NO.**

| ID | Claim | Status | Proof/receipt | Missing source/probe |
|---|---|---|---|---|
| O1 | For every h in Cc² and every J>=0, original finite-Gamma signed Weil distribution equals negative distributional second derivative of **contact-matched** Suzuki g_J | CLASSICAL / PROVED LOCAL analytic derivation | explicit pole/ramp/contact/exponential distribution derivatives, rational contact identity; 9 independent quadratures | not sign |
| O2 | C_J converges to Suzuki -psi(1/4)+log(pi); exact rational B_J bounds contact and gamma potential tails; compact g_J uniform error | CLASSICAL digamma + PROVED LOCAL | telescoping series, first-term+integral bound | no Gram global positivity |
| O3 | Source/screw commuting diagram implies Hilbert PSD | REFUTED as a generic implication | exact w(delta_b+delta_-b) fake source; K(t,t)=-2w(t-b)<0 | original zeta could still be PSD |
| O4 | Finite p-adic unit scaling traces are gcd(u-1,p^r); stabilize to local Connes fixed-point denominator away from identity | CLASSICAL / PROVED LOCAL | exact cyclic group kernel plus Fourier intertwiner; independent fixed-point brute oracle | no global adelic trace |
| O5 | Off-identity distribution values determine identity/contact term | REFUTED | T and T+c delta_1 agree on all away-from-identity tests | Connes Fourier-normalized principal value needed |
| O6 | Authentic K_g equals a true Hilbert Gram on **every** finite set iff RH | CLASSICAL EQUIVALENCE / CONDITIONAL SUFFICIENT | Suzuki screw criterion + Moore-Aronszajn; exact kernel equality with independently positive features unverified | **RH-hard, UNVERIFIED** |
| O7 | Direct finite source evaluation verifies W_J(h)=-<g_J,h''> for nine compact polynomial C² bumps | TESTED NUMERICAL | independent pole/prime/arch vs polynomial second-derivative quadratures, 60-digit working precision; 1/3 contact mutation detected | floating rounding not interval-certified |

Full statements, normalization, source family, derivations, caveats, next hostile probes: [ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md](../research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md). Code: observational_succ/one_object_transport.py; exact tests plus numerical holdouts: tests/test_one_object_transport.py; deterministic receipt: scripts/one_object_transport_probe.py. Original prime-power list is imported from completed_weil_transport, with no zero positions as inputs. Contextual independent Suzuki source: https://arxiv.org/pdf/2606.09096 . Connes local trace: https://arxiv.org/pdf/math/9811068 .

**Pending:** verified full Schwartz–Bruhat/adelic Connes principal-value distribution identification, authentic unconditional Hilbert-factor kernel, all-a sign/zero-shift range. Zero-reading, synthetic covariance and proof-by-positivity shortcuts prohibited. **RH OPEN.**


| O8 | Actual source anchored K_g at rational points x=1/4, y=1/2 has strictly positive 2x2 principal minor | PROVED FINITE SOURCE (SHA-pinned parent; exact outward Fraction) | source_weil_hierarchy.screw_interval + genuine Gamma tail; symbolic anchor-cancellation; GitHub two-Python success run 38681543132 | all other finite tuples / all test functions remain open |

The O8 certificate is isolated in observational_succ/one_object_kernel_certificates.py and tests/test_one_object_kernel_certificates.py. Its finite Gram interval is not a fitted numerical spectrum. Exact source SHA is inherited from the existing suzuki_legendre_source parent; no upstream source mutation or academic priority asserted.


| O9 | Connes–Consani positive Sonin compressed trace dominates the **restricted arch-only** Weil form on specified support and Fourier zeros | CLASSICAL IMPORT | arXiv:2006.13771, Theorem 1 | not the p=2+all-primes global zeta Weil form |
| O10 | A positive trace plus arbitrarily small rank-one/compact defect forces global nonnegativity | REFUTED shortcut | exact $\ell^2$ diagonal $T_k=2^{-k}$ and rank-one $D_N=-2^{1-N}|e_N\rangle\langle e_N|$, negative eigenvalue $-2^{-N}$, $\|D_N\|\to0$ | synthetic, not the authentic Weil/Connes defect |

**New exact hostile control:** one_object_transport.sonin_compact_defect_countermodel, test SoninDefectControls. The required alternative is a **source-identified** distribution-level trace equality with a valid quadratic *dominance* bound on its defect. Compactness, source-blind fitting and arch-only restricted positivity cannot be promoted to RH.


| O11 | Two Sonin Fourier-zero conditions have a support-preserving differential generator $v=D(D+1/2)\phi$ in the additive log-chart | CLASSICAL / PROVED LOCAL | integration by parts gives exponential moment multiplier $\lambda(\lambda-1/2)$; exact Fraction coefficients plus numeric compact-test holdout | actual Connes multiplicative input transport and complete Weil sign remain open |

Implementation: one_object_transport.sonin_log_moment_annihilator; tests: SoninMomentDomainTests. This is a lawful construction of restricted test functions, not a new Weil Hilbert space or a general positivity theorem.

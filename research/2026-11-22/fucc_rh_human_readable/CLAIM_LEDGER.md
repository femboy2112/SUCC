# Claim ledger — FUCC arithmetic multiplicity / human-readable RH

Statuses: **PROVED PAPER** (all-quantified derivation included), **OBSERVED FINITE** (scoped exact run), **IMPORTED CLASSICAL**, **IMPORTED FORMALLY VERIFIED EXTERNAL**, **UNVERIFIED**, **REFUTED SHORTCUT**. None of these claims is automatically a new theorem of global scholarly priority.

| ID | Status | Statement / scope | Boundary |
| --- | --- | --- | --- |
| FHR-01 | PROVED PAPER | `[log N,V_m]=log(m)V_m` on c_00, with bounded commutator extension per finite shift. | Weight is real, not p-adic integral multiplicity. |
| FHR-02 | PROVED PAPER | Finite Euler-log FUCC commutator gives `Σ Lambda(n)V_n`; vacuum-to-Riesz vector yields exact `S(X)`. | No signed x^(1/2+ε) estimate follows. |
| FHR-03 | PROVED PAPER / IMPORTED CLASSICAL | Mellin of G equals `(-ζ'/ζ)/(s(s-1))-1/(s-1)^2+(1+γ)/(s-1)` for Re s>1; Laurent pole at 1 cancels. | Analytic continuation/classical Landau criterion needed for zeros. |
| FHR-04 | PROVED PAPER | Height-two formal inverse's a-th derivatives satisfy `v_p ≥ v_p(a!)-(a-1)/(p²-1)` for f∈Z_p[[T]]. | This is a *model*, not a statement about actual CM theta kernels. |
| FHR-05 | PROVED PAPER | Finite integer determinant inequality: prime-power divisibility lower bound ≤ Archimedean Hadamard row-norm upper bound. | Number-field slopes and trace ranking are missing. |
| FHR-06 | REFUTED SHORTCUT | `V_p^a|1>=|p^a>` has nonzero coefficient 1; increasing support-depth does NOT imply coefficient valuation growth. | Can be repaired only by a new integral representation + bounded common pairing. |
| FHR-07 | IMPORTED FORMALLY VERIFIED EXTERNAL | Alpöge–Claude Lean library proves RH and GRH for Dirichlet L-functions; endorsed community verification. | Not independently reconstructed by SUCC, nor a human-readable proof by this packet. |
| FHR-08 | IMPORTED PARTIAL HUMAN GUIDE | Rubinstein (M) + B/C → RH, with the actual local/global (M) supplied by formalized proof rather than the current prose. | The full human-readable (M) derivation is incomplete; see M4–M10. |
| FHR-09 | UNVERIFIED | FUCC/SUCC can construct the full theta-integrality, global lattice slope/rank, and character averaging mechanism of (M) with all quantitative errors. | No SUCC proof of source-to-theta, integrality or rank/slope transfer. |
| FHR-10 | OBSERVED FINITE | Twelve focused test methods and standalone independent SymPy matrix/formal-inverse/resolvent finite audit. | Finite tests are not formal proof of all-n inequalities or external theta/Lean theorem. |

| FHR-11 | PROVED PAPER | Native FUCC p²-shift resolvent `(I-p^-1 V_(p²))^-1 e_1` maps coefficientwise to the exact height-two logarithm `l_p(T)=T+p^-1 l_p(T^(p²))` and has squared Hilbert norm `p²/(p²-1)`. | The **weight 1/p is selected**, not derived from critical FUCC amplitudes; the actual theta-period source map remains UNVERIFIED. |

### Mutations/countermodels

- Add a primitive `V_6`: false von Mangoldt current, since Λ(6)=0.
- Remove the `1/k` Euler-log factor: outputs `k log p` instead of Λ(p^k).
- Treat `log p` as a p-adic integer: *undefined* without explicit number-field model.
- Claim all FUCC powers gain divisibility: killed by the coordinate vector `V_p^a e_1=e_(p^a)`.
- Repeated identical observer heads: rank does not increase; cannot recover a lattice covolume.
- Omit any true Gamma/polar/conductor terms from the completed explicit formula: invalid RH source comparison.

No all-support Weil positivity, pi-normality, quantum vacuum-energy or new RH conclusion is claimed.

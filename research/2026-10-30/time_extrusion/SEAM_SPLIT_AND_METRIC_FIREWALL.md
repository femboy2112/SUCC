# Addendum ET-07 — complementary seam/correction split in the extruded BBP tube

**Research only, 2026-10-30.** Original four-pole source, `U_0=0`, and Main XVI truth-status firewall retained. A conditional Haar reference is not a claim about π's selected digits.

For n>=2 write `y_n={16^(n-1)(pi+16s)}` and the authentic Green tail `T_n>0`. The two disjoint shrinking windows on the same **pure source-recentered circle** are

\[
 C_n=[0,T_n),\qquad A_n=[T_n,T_n+r_n),\qquad C_n\cap A_n=\varnothing.
\]

`C_n` is the **gauge cut-crossing event** `eta_n=1`; `A_n` is the **original forcing correction** event `kappa_n != floor(16 x_(n-1))` of Kepler III (#384). Both definitions are all-seed exact. This makes precise the two ways an extruded triangular path can encounter the codimension-one seam.

## ET-07a: the asymptotically exact 1:15 arithmetic split

The positive four-pole forcing is strictly decreasing and satisfies `r_n~15/(64n²)`. Since `T_n=sum_(j>=1)16^(-j)r_(n+j)`, dominated convergence over j gives

\[
 \boxed{\frac{T_n}{r_n}\longrightarrow\sum_{j>=1}16^{-j}=\frac1{15},\qquad
 \frac{r_n}{T_n}\longrightarrow15.}
\]

Under a **Haar reference distribution of physical initial seeds** (not under the fixed original seed), `y_n` is uniform, so the two window masses are exactly `T_n` and `r_n`. Conditional on the union of the windows, the relative probabilities obey

\[
 \boxed{P_H(C_n\mid C_n\cup A_n)\to1/16,
 \quad P_H(A_n\mid C_n\cup A_n)\to15/16.}
\]

Also the event surprise differential has the exact finite expression and limit

\[
 \boxed{[-\log T_n]-[-\log r_n]=\log(r_n/T_n)\to\log15.}
\]

These are *branch-selection information ratios*, not observed digit frequencies, an Euler totient identity, or a physical Landauer heat law. The factor 15 is the source's radix-16 future Green normalization (`16-1`) and is not an Oily golden-ratio invariant.

## ET-07b: quantitative metric-seed eventual carry agreement

Kepler III's original-source bounds for all n>=3 are `T_n<1/(64n²)` and `r_n<1/(2n²)`. Thus `P_H(C_n\cup A_n)=T_n+r_n<33/(64n²)`. By the elementary union bound and integral comparison, for every N>=3,

\[
 \boxed{P_H\left[\exists n\ge N:\ y_n\in C_n\cup A_n\right]
 \le\sum_{n>=N}(T_n+r_n)
 <\frac{33}{64(N-1)}.}
\]

By Borel–Cantelli, under Haar physical seeds only **finitely many** `C_n` and `A_n` events occur a.s.; then the cocycle `kappa_(n+1)=d_(n+1)+16eta_n-eta_(n+1)` implies literal carries eventually coincide **exactly** with the pure radix digits. This is a sharp distinction between a.e. reference trajectories and the marked zero-seeded trajectory.

**Hostile control:** the coherent changed seed `s*=-pi/16` has `y_n=0`, so `C_n` occurs at **every** n, despite `T_n->0`, and `A_n` never occurs. Its bare pure digit is zero, its literal carry is 15. A deterministic conclusion of eventual carry agreement for the authentic seed would require independent arithmetic information; the source/volume alone cannot supply it.

## Proof-status separation

- The two disjoint target windows and integer cocycle follow from exact original BBP Green identities, not any distribution hypothesis.
- The `1:15` limit uses original source monotonicity plus a geometric series; it is an asymptotic reference law, **not** 1/16 digit normality.
- The Haar eventual-agreement theorem is a Borel–Cantelli consequence and applies to a.e. seed, *not* automatically to the singled-out `s=0`.
- π base-16 normality, original selected `o(N)` signed Fourier saving, and an actualization-dependent physical field update are still OPEN.

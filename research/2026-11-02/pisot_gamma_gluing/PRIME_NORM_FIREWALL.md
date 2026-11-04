# PG-09B — a finite but far-too-weak quantitative norm bound

**Paper-proved corollary of PG-09, not an asymptotic cancellation theorem.**

At a born-prime endpoint b (p=8b−7>5 prime), fix integer h not divisible by p. Let a signed Haar window be
\[
A=\sum_{n=c}^b \varepsilon_n e(hU_n),\quad \varepsilon_n\in\{+1,-1\},\quad\varepsilon_b\neq0.
\]
Set M=b−c+1 and let D be the least common multiple of the denominators of the reduced hU_n for c≤n≤b. The original zero-seed U_n are rational, so each e(hU_n) is a root of unity. Consequently A belongs to the cyclotomic field F=Q(ζ_D) of degree d=φ(D), and is an ALGEBRAIC INTEGER (sum/difference of roots of unity).

PG-09 proves A≠0. Therefore its absolute field norm is a **nonzero integer**, \(|N_{F/\mathbb Q}(A)|\ge1\). Every Galois conjugate σ(A) is again a sum of M unit complex numbers, so \(|σ(A)|\le M\). Isolating the identity embedding yields the exact bound
\[
\boxed{|A|\ge M^{-(\varphi(D)-1)}.}
\]

The corresponding squared Haar difference obeys
\[
\boxed{W=|A|^2\ge M^{-2(\varphi(D)-1)}.}
\]
This is genuinely positive for every listed selected finite source window (and stronger than an unproved numerical claim of nonzero), but the cyclotomic degree grows explosively with original BBP denominators. It provides no useful fixed δ in \(W/E\), no diverging intermediate-scale \(D_J(h)\), and **no π-normality**. In particular replacing the selected amplitude by a Galois-averaged mean-square is NOT justified.

This sharpens the diagnosis of the remaining obstruction: the phase is algebraically distinguished by unique newborn prime factors, but a source-derived quantitative ARCHIMEDEAN lower bound (or source-selected signed cross-block upper bound) is still needed. The one-term field decomposition is not a proof of strong real-circle phase separation.

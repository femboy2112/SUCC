# Spectral reductions and their missing signed premise

This is an executed derivation/obstruction audit for front V. It supplies no
new unbounded Fourier estimate. The actual finite signed estimates are in
`FINITE_CIRCLE.md` and `signed_crt/JOINT_SIGNED_CRT.md`. Classical source
references and their applicability limits are in `LITERATURE_AUDIT.md`.

## Fixed-lag van der Corput route

Put `e(t)=exp(2 pi i t)`, `z_n=e(hU_n)` and `S_N=sum_(n=1)^N z_n`.
Fix 1<=H<=N. Zero-extend z outside that interval. Cauchy--Schwarz on H consecutive
translates gives the exact standard inequality

```
|S_N|^2 <= (N+H-1)/H^2 *
  [H*N + 2 sum_(d=1)^(H-1) (H-d) Re C_d(N)],
C_d(N) = sum_(n=1)^(N-d) e(h*(U_(n+d)-U_n)).
```

One can obtain it directly by summing the square of the H-term sliding
sum: each diagonal appears H times and each lag d appears H-d times.
The zero extension has support of length N+H-1. This derivation does not
assume randomness, independence or prime order.

For each fixed d, the authentic recurrence gives

```
U_(n+d)-U_n = (16^d-1)U_n + F_d(n),
F_d(n) = sum_(t=1)^d 16^(d-t) r(n+t).
```

The exact positive rational r(n) is O(n^-2); hence
`sum_(n>=1) |F_d(n)| < infinity`. The chord inequality therefore gives

```
C_d(N) = sum_(n=1)^(N-d) e(h*(16^d-1)U_n) + O_(h,d)(1).
```

Thus this attempt trades the original signed question for selected signed
questions at frequencies h(16^d-1). No independent cancellation estimate
was obtained. Allowing d to grow requires new control of the exponentially
growing constants; no uniform-in-d estimate is asserted. CG-03 proves the
sharp rational denominator rate for these very differences, but a large
denominator gives no lower bound on their real-circle distance from zero.

The same-forcing coherent seed s=-pi/16 makes the completed phase constant
and all its lag correlations equal to their full length. Its rational-forcing
trajectory differs from that phase by the vanishing Green tail, so the same
correlations are `N+O_(h,d)(1)`. This exact typed countermodel rejects a proof
using only the small forcing, expansion, or the universal difference formula.
It is not a zero-seed counterexample. The dyadic finite controls in SC-05
add preservation of every odd-primary mark without changing this warning.

## Discrepancy and transfer-operator routes

The classical Erdos--Turan inequality bounds interval discrepancy by an
absolute constant times
`1/(H+1) + sum_(h=1)^H |S_N(h)|/(h*N)` (up to the conventional endpoint
normalization). It is an implication from simultaneous signed estimates,
not a source of those estimates. The 64 interval-certified finite means in
this campaign do not make that expression small for unbounded N or H.

Empirical limits of the completed radix orbit are T16-invariant. In Fourier
language invariance says `mu_hat(h)=mu_hat(16h)`. The transfer operator
contracts regular densities in appropriate norms, but a selected orbit's
Dirac measures are not a supplied uniformly regular density. Invariance
alone permits atomic and singular invariant measures; the corrected
Kempner dossier, rechecked in the transfer package, gives the concrete
irrational sparse-digit countermodel with empirical limit delta0. Positive
topological complexity or a favorable annealed law does not establish the
needed entropy of the selected empirical components.

An all-horizon occupancy bound `count(I)<=CN|I|+o_I(N)` with finite C
independent of I would give absolutely continuous invariant limits, hence
Haar measure. We recovered this input for Stoneham c=3,5. We did not prove
it for BBP. Neither the equivalence nor the standard invariance argument is
counted as research progress toward the missing BBP inequality.

## Frobenius and selected-source energy routes

AT-01/02 supply actual p-adic transport and the first corrected lift, derived
from signed source terms. They do not transport the complementary real
character. Integral diagonal/Cartier/Dwork results require additional
arithmetic hypotheses; unnormalized U_n has arbitrarily negative p-adic
valuation, as AT-03 proves. No theorem is imported merely because both
constructions use the word Frobenius.

SC-06 is the concrete signed interaction target retained after these
failures. Its path-energy implication is proved; its authentic, zero-seed,
all-large-prime lower bound is OPEN. Gauss completion and partial summation
were actually tried on that target and produced vacuous bounds. The finite
holdouts are evidence for continued investigation, not a promoted theorem.

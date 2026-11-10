# Attempt: can the original carry-flow law pay the remaining contrast?

This pass read only the frozen **earlier training** table and existing
proofs. No later-source phases, carries, logs or measurements were read.
The exact table hash is in [the countermodel receipt](CYCLE_COUNTERMODELS.json).

## Attempt A: stationarity plus small forcing bounds Dpsi

The proposed proof was to use exact finite-state flow conservation, small
four-pole forcing and sparse carry16 events to replace the actual carry
occupation by the uniform-append reference. The first part is real: for a
path of N edges, incoming and outgoing state counts differ only at its two
endpoints. Every subsequential occupation limit is a stationary circulation.
The second replacement is false without a new source selection theorem.

**Exact graph criterion.** Let G be a finite strongly connected directed
graph, with state cost a(w)=g(w)-mu. Every stationary circulation has mean
cost zero iff every directed cycle has total cost zero. Equivalently there
is a function u on vertices with `a(w)=u(w)-u(v)` on every allowed edge
w->v. To prove this, cycle occupation measures give necessity; cycle
decomposition of a nonnegative balanced flow gives sufficiency. For the
potential formulation, integrate a along a path from a reference vertex;
two path integrals agree after appending a common return path because all
cycle sums vanish. Negate those path integrals to obtain the displayed sign.
The converse telescopes. Thus stationarity kills graph coboundaries; it
does not select uniform digit probabilities.

The frozen tables fail this criterion already on **constant digit cycles**.
Exact dyadic arithmetic, independently passing through the Poisson compiler,
gives:

| h | Frozen menu | Constant digit | Completed point alpha | Innovation magnitude (diagnostic) |
|---:|---|---:|---:|---:|
| 1 | one carry | 12 | 4/5 | 0.1163349569... |
| 1 | two carries | 5 | 1/3 | 0.4744938298... |
| 3 | one carry | 2 | 2/15 | 0.1171362003... |
| 3 | two carries | 6 | 2/5 | 0.4327497726... |

For each row the exact contrast is `g(d,...,d)-mu`, with squared modulus
recorded as a rational. All one-carry examples exceed1/10 and two-carry
examples exceed2/5. These are not claims of a globally worst cycle. The
receipt tests all56 constant cycles with digits1,...,14, then reports the
largest in each of the four declared table/frequency configurations.

**Original-forcing realization.** For a displayed digit d, choose the
same-forcing seed `s_d=d/15-pi/16`. Then the completed orbit is fixed at
`alpha=d/15`, since16 is1 modulo15. The Green identity gives

`U_n(s_d)=16^n d/15-T_n`, and `x_n=d/15-T_n` for all sufficiently large n.

Hence the literal carries are exactly d eventually, the carry-flow equation
holds, the carry16 exceptional density is zero, and the original forcing
and all its smallness estimates hold unchanged. Nevertheless

`Dpsi -> g(d,...,d)-mu != 0`, and `W_A(h;s_d)->e(hd/15)` has modulus1.

The table values in the receipt have modulus<1/2. Thus the residual signed
mean has limiting modulus at least1/2, and every valid residual VdC upper
certificate has liminf at least1/4 after squaring. This is an actual
same-forcing counterexample to the proposed implication, not an arbitrary
assignment of output phases to a graph.

These s_d are irrational nonzero seeds. **Canonical rational prime principal
parts are not assigned to them.** The completed points4/5 and2/5 are not
the original source seed1/5; no nonnormality assertion about seed1/5 is made.

**Verdict:** small forcing + spill sparsity + finite-state stationarity do
not pay Dpsi. They remain useful representation bounds. The exact zero
boundary, or a proved consequence that these controls violate, is missing.

## Attempt B: add rationality and any prescribed finite set of prime tests

Here is a stronger finite-horizon countermodel, with the quantifiers kept
visible. Fix a horizon H, a precision epsilon>0, a finite set P of odd primes,
and prescribed nonnegative valuations K_p. Let

`M=2^max(1,K) product_(odd p in P) p^max(1,K_p)`.

Choose any sufficiently large odd `q=1+tM`, and choose an integer a nearest
`q s_d/M`. The rational seed `s_H=aM/q` obeys

`|s_H-s_d|<=M/(2q)`.

We can therefore make `16^H|s_H-s_d|<epsilon`. Its reduced denominator is
odd and coprime to every prime dividing M; `v_p(s_H)>=K_p`, including the
chosen 2-adic depth. For each p in P included in M, the seed is p-integral,
and so is16^n s_H. Thus its p-primary rational principal part is **exactly
the original-zero principal part at every time**, not just approximately.
The local prime clock and its character estimates at those places survive.

At late times the fixed completed circle point d/15 has a positive distance
from0 and1. For sufficiently small epsilon, all carries in any specified
late subwindow through H equal d exactly. The real phases there are within
`2pi|h|epsilon` of the same-forcing fixed-orbit control. Thus rationality,
arbitrarily many fixed local prime observations, high 2-adic seed agreement,
and long exact carry cycles are compatible with a large signed signal.

This statement chooses **a new rational seed for each horizon and test set**.
It does not construct one fixed rational nonnormal seed. Its extra seed
denominator introduces source support outside the protected finite places;
full original genealogy or the literal U0=0 tag rejects it. This is exactly
why finite local-place authentication cannot be promoted to zero-source
selection.

One may also retain an arbitrary finite **zero-source carry prefix**. For
its length J, the positive interval

`0<s<sigma_J`, `sigma_J=min_(0<=j<=J)(1-{U_j(0)})/16^j`,

keeps all corresponding integer floors and carries unchanged. Completed
numbers that eventually repeat any chosen digit d in1,...,14 are dense:
they have the form `(N+d/15)/16^K`. Choose such an alpha strictly inside
`(pi/16,pi/16+sigma_J)`. Its seed `s*=alpha-pi/16` preserves the zero carry
prefix, and its later completed orbit is fixed at d/15. Apply the rational
approximation construction inside this open seed interval while protecting
the finite late window. The resulting rational seeds share that prefix
and all specified p-primary tests, yet have a long later fixed-carry block.
They do not share the exact initial seed or exact unwrapped zero history.

**Verdict:** finite arithmetic and prefix probes can be satisfied while the
signed target remains large. The countermodels identify the missing uniform
quantifier; they do not refute a theorem using the complete literal-zero
source.

## Productive repair: the analytic retrodictive table

The root proposed a better source-derived rule during this pass:
`g_k=e(h(K_past+1/2)/16^k)`. [CCV7](THEOREMS.md) proves its signed residual
and padded-window error vanish unconditionally at a declared memory rate.
This pays a real residual-estimation step that the trained current-phase
predictors could not pay merely by improving their fit.

The remaining contrast is then exactly localized:

`|W_A-Dpsi_literal|<=4k/A+epsilon_A ->0`.

So **Dpsi decay is equivalent to Weyl decay** for this explicit family.
The result is a source-derived integer-carry target with proved approximation
error, not an independent proof that its occupation is uniform. The fixed
completed-point controls above give nonvanishing Dpsi for this family too,
and the exact zero boundary must do the remaining arithmetic work.

**Pi base16 normality: OPEN. RH: OPEN.**

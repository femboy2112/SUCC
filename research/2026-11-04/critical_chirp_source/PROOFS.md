# Strongest results and the remaining selected-source gap

Use the exact four-pole forcing, `U_0=0`, `U_n=16U_(n-1)+r(n)`, and
`T(x)=sum_(k>=1)16^-k r(x+k)`. Write `e(x)=exp(2 pi i x)` and use the
mission's exact dyadic schedule `H_A(h)=|h|16^j`,
`j=floor(log_16(A² log A/|h|))`, `Lambda=H/A²`. Maximal sums always range
over **all contiguous subintervals**, normalized by A.

## 1. The original source has a sharper all-derivative tail bound

For every real x>0 and integer k>=0,

\[
0<\frac{(k+1)!}{64x^{k+2}}-(-1)^kT^{(k)}(x)
 <\frac{7(k+2)!}{1024x^{k+3}}.
\]

The right coefficient is asymptotically sharp for each fixed k. This is a
theorem about the genuine source tail. Its proof uses the exact positive
Laplace density and dominated convergence, with an independently derived
four-pole/beta-difference rational instrument. It is not signed orbit decay.
Full proof: [AH-01](front_ah/PROOFS.md).

## 2. The coherent threshold holds over a wider frequency range

For the **changed fixed seed** s*=-pi/16, uniformly for sufficiently large
integer A and all positive integer H with `1<=Lambda<=A`,

\[
M_A^{(s_*)}(H)=\frac{256}{\pi\Lambda}
                  +O(\Lambda^{-2}+A^{-1}).
\]

Thus `Lambda M -> 256/pi` whenever `Lambda -> infinity` and `Lambda/A -> 0`.
The parent required `Lambda²/A -> 0`. Twice applying **discrete** summation
by parts to the exact tail avoids its pointwise phase-replacement loss.
Endpoint rounding, maximality and all uniform errors are paid in
[AH-02](front_ah/PROOFS.md); [a separate review](front_cfg/REVIEW_AH.md)
checks the telescoping and endpoints. This improves a countermodel calibration,
not the zero-seed estimate.

## 3. Normality itself does not imply the requested critical rate

There is one fixed real seed s with the **same exact four-pole forcing** and a
base-16 normal completion `y=s+pi/16`, for which

\[
\liminf_{\substack{A\to\infty\\A\text{ dyadic}}}
\frac{\Lambda_A(1)M_A^{(s)}(H_A(1))}{\sqrt{\log A}}
\ge\frac{\cos(\pi/15)}{16}>0.
\]

The seed is explicitly different from zero. All fixed-character full-prefix
Weyl and Abel means nevertheless vanish. The construction modifies only a
density-zero set of digits of a normal number. On terminal blocks of length
`A/sqrt(log A)`, its prescribed digits track the rational chirp `H/(64n²)`
via the radix fixed points `d/15`. Only `O((log A)^(3/2))` positions are lost
at digit switches, so the signed real part stays positive on a contiguous
block. No statistical extrapolation establishes this statement.

A second, simpler fixed normal counterseed satisfies, simultaneously for
**every** fixed h!=0,

\[
\liminf_{\substack{A\to\infty\\A\text{ dyadic}}}
\Lambda_A(h)M_A^{(s)}(H_A(h))\ge256/\pi.
\]

Its terminal zero blocks recover the half-turn constant by a rescaled Riemann
sum, independently of the global maximal asymptotic. Proofs:
[CFG-1/2](front_cfg/PROOFS.md); [hostile cross-review](front_ah/INSTRUMENT_REVIEW.md).
These results refute uniform promotion of qualitative fixed-character decay
plus the seed-blind Gram estimate to the critical rate. They do not refute a
source-specific quantitative theorem for seed zero, or Hypothesis A.

## 4. The radial channel passes the critical expression but fails normality

For the actual endogenous radial projection Z from #499/#500, its own
zero-seeded forcing has order 1/n and `Z_n=1/(32n)+O(n^-2)`. Uniformly for
`1<=Lambda<=A/2`,

\[
M_A^Z(H)\ll\sqrt{\frac{\Lambda+\log(2A)}{A}}.
\]

Consequently at the exact prescribed H_A(h), for every fixed h!=0,

\[
\Lambda_A M_A^Z(H_A)
 =O\!\left(\frac{(\log A)^{3/2}}{\sqrt A}\right)\longrightarrow0.
\]

Yet its fixed-character means tend to one and `J/q -> 1`. There is no
contradiction: the original F4 cost `1+CH/A²` belongs to the original
order-1/n² forcing. The radial variation costs order H/A instead. This proves
that insisting this radial control fail the **same critical expression** would
be a source-map error. Its denominator/coarse-occupancy obstruction remains
valid. The proof uses rational-tail derivatives and elementary Cauchy
differencing with monotone increment sums: [BDE-1](front_bde/PROOFS.md).

## 5. Extensive exact prime data still leave a critical obstruction

There exists a single rational **changed-forcing**, zero-seeded recurrence,
agreeing with any prescribed finite authentic prefix, which has positive
injections and changes only `O(N/log log N)` times through N. It preserves:

- the full authentic injection at every first-prime birth;
- all nonternary principal parts of every state, injection difference and lag;
- every exact state denominator and forcing-prefix LCM;
- all but `O(log log n)` least singular ternary polar digits;
- exact authentic gap denominators outside `O(A^(3/2))` ordered epoch pairs.

Nevertheless, for every fixed h!=0 on the **same** mutant,

\[
|M_A^V(H_A(h))-M_A^{(-T)}(H_A(h))|=O((\log A)^{-4}),
\qquad \Lambda_A M_A^V(H_A(h))\longrightarrow256/\pi.
\]

The construction uses sparse ternary frequency locks at nonbirth times. It
does not preserve the full forcing, literal carries, omitted ternary numerator,
monotonicity or asymptotic forcing jets. It uses finite future injections.
It is therefore a counterexample only to the stated incomplete hypotheses.
Proof: [BDE-3](front_bde/PROOFS.md), using parent T1/T3 with their exact scopes.

The existing parent's exponentially accurate sparse reset already yields the
same critical limit as a corollary of CC-02. That inherited combination is
credited separately as BDE-2; it is not presented as a new construction.

## 6. What the genuine finite signed computation establishes

At A=128,256,512 and h=1,3,-5,17, the two exact source evaluators agree and
the new rational instrument certifies both M and R, including every interval.
For example at A=512,h=1:

    original R in [0.238707419, 0.238707420],
    coherent R in [3.987158786, 3.987158787].

These are outward decimal enclosures of finite exact certificates. Here
Lambda=4, far from the large-Lambda coherent limit; the value is not a test
of 256/pi's asymptotic onset. Other cases are retained without selection in
[SIGNED_RECEIPT.json](SIGNED_RECEIPT.json). The proof of the error budget is
in [INSTRUMENT.md](INSTRUMENT.md). No finite case proves the all-h asymptotic.

## Verdict on the original route

CC-01--04, F1's maximal strengthening, F4, and the dyadic-to-full-prefix
implication survive this round's audit. Van der Corput on the authentic orbit
retains the selected phase at shifted character `H(16^d-1)`; its forcing
multiplier has a critical-scale variation cost. Removing the homogeneous
completion changes the seed. Prime reconstruction pins injections but the
remaining real numerator orientation cannot be discarded. The controls above
prove exactly where the attempted seed-blind, finite-place-incomplete and
qualitative-rate transfers fail.

No source-selected little-o saving for the genuine zero seed was proved.
Pi base-16 normality, original fixed-h Weyl, the original critical ratchet,
and original coarse `J=o(K)` all remain **OPEN**. RH remains **OPEN, separate**.
